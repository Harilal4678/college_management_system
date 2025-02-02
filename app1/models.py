from django.db import models

class studentdetails(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    dob=models.DateField(max_length=30)
    gender=models.CharField(max_length=30)
    course=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    image=models.ImageField(upload_to='student_user')
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.first_name
class staff(models.Model):
    fullname = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=30)
    department = models.CharField(
        max_length=30,
        choices=[
            ('lab_assistant', 'lab_assistant'),
            ('lecturer', 'lecturer'),
            ('clerk', 'clerk'),
        ],
        default='clerk'  # Set a default department
    )
    password = models.CharField(max_length=20)
    image = models.ImageField(upload_to='student_user')
    address = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.fullname} ({self.department})"


    
    def __str__(self):
        return self.fullname
    
class Attendance(models.Model):
    student = models.ForeignKey(studentdetails, on_delete=models.CASCADE)
    date = models.DateField()  # Date of attendance
    status = models.CharField(max_length=10, choices=[('present', 'Present'), ('absent', 'Absent')])  # Attendance status
    lecturer = models.ForeignKey(staff, on_delete=models.CASCADE, null=True, blank=True)  # The lecturer who took attendance

    def __str__(self):
        return f"{self.student.first_name} - {self.date} - {self.status}"
    
class marks(models.Model):
    student = models.ForeignKey(studentdetails, on_delete=models.CASCADE)
    physics=models.IntegerField()
    maths=models.IntegerField()
    computer_science=models.IntegerField()
    lecturer=models.ForeignKey(staff,on_delete=models.CASCADE,null=True,blank=True)
    exam_type=models.CharField(max_length=30,default='quarterly')

    def __str__(self):
        return f"{self.student.first_name}"
    


class Notification(models.Model):
    sender = models.ForeignKey(staff, on_delete=models.CASCADE, related_name="sent_notifications")
    recipient = models.CharField(max_length=10, choices=[('student', 'Student'), ('staff', 'Staff')])  # Recipient type
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically set when the message is created
    is_read = models.BooleanField(default=False)  # To track if the message has been read

    def __str__(self):
        return f"From {self.sender.fullname} to {self.recipient}: {self.message}"
    
class Assignments(models.Model):
    teacher=models.ForeignKey(staff,on_delete=models.CASCADE)
    student=models.ForeignKey(studentdetails,on_delete=models.CASCADE)
    title=models.CharField(max_length=30)
    description=models.CharField(max_length=30)
    due_date=models.CharField(max_length=30)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class AssignmentAnswers(models.Model):
    assignment = models.ForeignKey(Assignments, on_delete=models.CASCADE, related_name='answers')
    student = models.ForeignKey(studentdetails, on_delete=models.CASCADE)  # Linking to the student
    text_answer = models.TextField(blank=True, null=True)  # For text input
    file_answer = models.FileField(upload_to='assignment_answers/', blank=True, null=True)  # For file input
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Answer by {self.student} for {self.assignment.title}"


    
   
   

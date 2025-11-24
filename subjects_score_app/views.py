from django.http import JsonResponse
from django.shortcuts import render,get_object_or_404

from django.template.loader import render_to_string
from .models import Subjects,Grade
from assessment_app.models import Assessment
from studentapp.models import Student

# Create your views here.
def checkAvg(avg):
    if avg >=90 and avg<=100:
        Grade="O"
        Remark="Outstanding"
        emoji="😁"
    elif avg >=80 and avg<90:
        Grade="E"
        Remark="Excellent"
        emoji="☺️"
    elif avg>=70 and avg<80:
        Grade="A"
        Remark="Good"
        emoji="🙂" 
    elif avg>=60 and avg<70:
        Grade="B"
        Remark="Average"
        emoji="🥲" 
    elif avg>=50 and avg<60:
        Grade="D"
        Remark="Pass"
        emoji="😶"
    elif avg<50:
        Grade="F"
        Remark="Fail"
        emoji="😭"

    return Grade,Remark,emoji
def view_marks(request):
    students=Student.objects.all()
    assessments = Assessment.objects.all()
    subjects=Subjects.objects.all()
    return render(request , 'subject_score/add_marks.html',{"students":students, "assessments":assessments , "subjects":subjects})
     

def add_marks(request):
    students=Student.objects.all()
    assessments = Assessment.objects.all()
    if request.method == "POST":
        sub_id = request.POST.get("sub_id")
        stu_id =  request.POST.get("stu_id")
        maths =  int(request.POST.get("maths"))
        physics =  int(request.POST.get("physics"))
        chemistry = int( request.POST.get("chemistry"))
        english =  int(request.POST.get("english"))
        hindi =request.POST.get("hindi").strip()
        bengali =request.POST.get("bengali").strip()
        assmt_id =request.POST.get("assmt_id")

        if hindi.isdigit():
            hindi = int(hindi)
        else:
            hindi = 0 

        if bengali.isdigit():
            bengali = int(bengali)
        else:
            bengali = 0

        # total_marks
        # percentage
         

        try:
                    student = Student.objects.get(id=stu_id)
                    print(student)
                    assmt = Assessment.objects.get(id=assmt_id)
                    print(assmt)
                    if student.language == 'hindi':
                        total_marks = maths + physics + chemistry + english + hindi
                    else :
                        total_marks = maths + physics + chemistry + english + bengali
                    percentage = total_marks // 5
                    print(total_marks)
                    grade_info=checkAvg(percentage)
                    print(grade_info)
                    grade=grade_info[0]
                    remark=grade_info[1]
                    emoji=grade_info[2]

                    
                    Subjects.objects.create(
                                student=student,
                                maths=maths,
                                physics=physics,
                                chemistry=chemistry,
                                english=english,
                                hindi=hindi,
                                bengali=bengali,
                                assessment=assmt,
                                total_marks=total_marks,
                                percentage=percentage

                    )
                    per = Subjects.objects.get(percentage=percentage)
                    Grade.objects.create(grade=grade , remark=remark, emoji=emoji ,student=student,percentage=per )
                    subjects=Subjects.objects.all()
                    html_sub = render_to_string('subject_score/partials/subject_rows.html' , {"subjects":subjects})
                    return JsonResponse({
                            "subjects":html_sub,
                            
                        })
                    

        except Student.DoesNotExist:
            return JsonResponse({"message": "Student not found."}, status=400)
        except Assessment.DoesNotExist:
            return JsonResponse({"message": "Assessment not found."}, status=400)
      
    else:
         return render(request , 'subject_score/add_marks.html',{"students":students, "assessments":assessments})
    
# grade=models.CharField(max_length=3)
#     remark=models.CharField(max_length=250)
#     student=models.ForeignKey(Student , on_delete=models.CASCADE , related_name='grade')
#     percentage = models.ForeignKey(Subjects , on_delete=models.CASCADE , related_name='grade')

def edit_marks(request , pk=None):
    subject = get_object_or_404(Subjects,id=pk) if pk else None
    if request.method == "POST":
        stu_id= request.POST.get("stu_id")
        assmt_id= request.POST.get("assmt_id")
        maths= request.POST.get("maths")
        physics= request.POST.get("physics")
        chemistry= request.POST.get("chemistry")
        english= request.POST.get("english")
        hindi= request.POST.get("hindi")
        bengali= request.POST.get("bengali")
        try:
            student = Student.objects.get(id=stu_id)
            assessment = Assessment.objects.get(id=assmt_id)
            subject.student=student
            subject.assessment=assessment
            subject.maths=maths
            subject.physics=physics
            subject.chemistry=chemistry
            subject.english=english
            subject.bengali=bengali
            subject.hindi=hindi
            subject.save()


            # after save, fetch all data from subject table
            subjects=Subjects.objects.all()
            html_sub = render_to_string('subject_score/partials/subject_rows.html' , {"subjects":subjects})
            return JsonResponse({
                            "subjects":html_sub,
                            "message": "updated successfully."
                            
                        })

        except Student.DoesNotExist:
            return JsonResponse({"message": "Student not found."}, status=400)
        except Assessment.DoesNotExist:
            return JsonResponse({"message": "Assessment not found."}, status=400)
    return JsonResponse({"message": "Invalid request."}, status=400)

def delete_marks(request, pk=None):
    subject = get_object_or_404(Subjects,id=pk) if pk else None
    print(subject)
    subject.delete()
    subjects=Subjects.objects.all()
    html_sub = render_to_string('subject_score/partials/subject_rows.html' , {"subjects":subjects})
    return JsonResponse({
                    "subjects":html_sub,
                    "message": "updated successfully."
                    
                })


# def delete_subject(request, subject_id=None):
#     subject = get_object_or_404(Subject, pk=subject_id)
#     subject.delete()
#     # After deletion, return the updated list of subjects
#     subjects = Subject.objects.select_related("stream")  # Use select_related for optimization
#     html_string = render_to_string("partials/subject_rows.html", {"subjects": subjects})
#     return JsonResponse({"subjects": html_string, "message": "Subject deleted successfully!!"})
      
    







def view_student_records(request):
    grades=Grade.objects.all()
    # print(grades)
    return render(request , 'subject_score/student_records.html',{"grades":grades })
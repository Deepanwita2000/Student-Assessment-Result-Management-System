from django.shortcuts import get_object_or_404, render
from studentapp.models import Student
from django.template.loader import render_to_string
from django.http import JsonResponse
from subjects_score_app.models import Grade,Subjects


# Create your views here.
def read_student(request):
    languages=Student.ROLE_CHOICES
    gender=Student.gender_choices
    cities=Student.city_choices
    students=Student.objects.all()
   
    return render(request , 'student/add_student.html',{"students":students ,"languages":languages,  "gender":gender , "cities":cities,"hasStudents":True})

def create_student(request):
    languages=Student.ROLE_CHOICES
    gender=Student.gender_choices
    cities=Student.city_choices
    if request.method == "POST":
        st_id = request.POST.get("st_id")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        city = request.POST.get("city")
        gender = request.POST.get("gender")
        contact = request.POST.get("contact")
        email = request.POST.get("email")
        language = request.POST.get("language")

        if lname and email:
            if not Student.objects.filter(email=email).exists():
                Student.objects.create(fname=fname ,
                                        lname=lname ,
                                         city=city,
                                          gender=gender,                                                                                     
                                          contact= contact,                                          
                                          email = email,
                                          language=language)
                students=Student.objects.all()
                html = render_to_string('partials/student_row.html' , {"students":students})
                return JsonResponse({
                    "students":html,
                    "addStudents":True
                })
            else:
                return JsonResponse({"message":f"Student ${email} already exists"} , status=400)
        else:
            return JsonResponse({"message":"Student field is empty"} , status=400)

        
    else:
        
        return render(request , 'student/add_student.html', {"languages":languages , "gender":gender , "cities":cities})


def edit_student(request , x=None):
    student =get_object_or_404(Student , id=x) if x else None
    if request.method == "POST":
        st_id = request.POST.get("st_id")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        phy =  request.POST.get("phy")
        math =  request.POST.get("math")
        comp =  request.POST.get("comp")
        email = request.POST.get("email")
        if fname and email:
            if not Student.objects.filter(fname=fname).exclude(id=x).exists():  # Check if the stream name already exists
                student.fname = fname
                student.lname = lname
                student.physics = phy
                student.maths = math
                student.computer = comp
                student.email = email
                student.save()

                students=Student.objects.all()
                html = render_to_string('partials/student_row.html' , {"students":students})
                return JsonResponse({"students":html})
            else:
                return JsonResponse({"message": f"Field name ${fname}exists"}, status=400)
        else:
            return JsonResponse({"message": "Field name cannot be empty!"}, status=400)
    else:
           return render(request , 'student/add_student.html',{"students":students})


def delete_student(request , dX=None):
    student =get_object_or_404(Student , id=dX)
    student.delete()
    students=Student.objects.all()
    print(students)
    html = render_to_string('partials/student_row.html' , {"students":students})
    return JsonResponse({
            "students":html,
            "message":"data deleted successfully"
        })


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

def search_student(request):  
    if request.method == "POST":
        grade_id = request.POST.get("grade_id")   
        grade=get_object_or_404(Grade , id=grade_id)
        print(grade.percentage.student,grade.percentage.percentage,grade.student,grade.student.id)
        # sub_info=Subjects.objects.get(percentage=grade.percentage.percentage)
        # # print(sub_info)
        print(grade_id) 
        print(grade.remark)
        print(grade.emoji)
        print(grade.student)
        print(grade.percentage)
  
        stu_obj = grade.student
        sub_obj = grade.percentage
        subjects= Subjects.objects.get(id=sub_obj.id)
        student= Student.objects.get(id=stu_obj.id)
        print(subjects,student)
        html = render_to_string('partials/student_details.html' , {"student":student , "grade":grade , "subjects":subjects})
        print(html)
        return JsonResponse({
                        "student":html,
                        
                    })
        # avg=0
        # if search_fname:
        #     if Student.objects.filter(fname=search_fname).exists():
        #         student = Student.objects.get(fname=search_fname)
        #         print(type(student))
        #         print(student.fname)
        #         avg=(student.physics + student.computer + student.maths)/3
        #         print(f"{avg:.2f}")
        #         grade_info=checkAvg(avg)
        #         print(grade_info)
        #         grade=grade_info[0]
        #         remark=grade_info[1]
        #         emoji=grade_info[2]
        #         print(grade,remark,emoji)


        #         html = render_to_string('partials/student_details.html' , {"student":student , "average":avg , "grade":grade,"emoji":emoji,"remark":remark})
        #         print(html)
        #         return JsonResponse({
        #                 "student":html,
                        
        #             })
        #     else:
        #         return JsonResponse({"message":f"Student ${search_fname} doesnot exists"} , status=400)
        # else:
        #     return JsonResponse({"message":"Empty"} , status=400)
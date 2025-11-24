$(document).ready(function(){
    console.log("ajax is loaded!!")


    $('#studentForm').hide();

    $('#hide_stu').click(function(e){
        $('#studentForm').hide();
    })

    $('#show_stu').click(function(e){
        $('#studentForm').show();
    })

    $(".edit-student").click(function(e){
         $('#studentForm').show();
    })

    // $("#edit-subjects").click(function(e){
    //      $('#cardForm').show();
    // })

//    $(document).on("click", "#checkbox", function () {
//         //  e.preventDefault()
//          const check = $("#checkbox").val()
//          console.log("checked!!")
//          console.log(check)
//     })

// $('#checkbox').on('click', function() {
//   const anyChecked = $('#checkbox').val();
//  if (anyChecked){
//      console.log("clicked!!")
//  }
// });


    // create and edit
    
    $("#btn-create").click(function(e){
        e.preventDefault()
         console.log("clicked!!")

        //  fetch data from template
                st_id= $("#st_id").val() 
                fname= $("#fname").val()     
                lname= $("#lname").val()
                email= $("#email").val()
                gender = $("#displayValue").val() 
                console.log(gender)
                city = $("#city").val() 
                language=$("#lang").val()
                contact = $("#contact").val() 
              
                console.log(gender)
                // check for empty fields
                if(!fname){
                     $("#empty-fname").text("first name cannot be empty.")
                            .css("color", "red")
                            .fadeIn().delay(2000).fadeOut();
                      
                }

                if(!lname){
                     $("#empty-lname").text("last name cannot be empty.")
                            .css("color", "red")
                            .fadeIn().delay(2000).fadeOut();
                    
                }
                if (!contact.startsWith("+91 ")) {
                    $("#contact-pattern")
                        .text("Contact must start with +91 and a space.")
                        .css("color", "red")
                        .fadeIn().delay(2000).fadeOut();
                    return; // prevent submit
                }
                if (!city) {
                    $("#empty-city").text("City cannot be empty.")
                        .css("color", "red")
                        .fadeIn().delay(2000).fadeOut();
                }

                if (!language) {
                    $("#empty-lang").text("Language is mandatory.")
                        .css("color", "red")
                        .fadeIn().delay(2000).fadeOut();
                }

                if (!gender) {
                    $("#empty-gender").text("Gender is mandatory.")
                        .css("color", "red")
                        .fadeIn().delay(2000).fadeOut();
                }

                

                  if(email){
                     $("#emailHelp").text("We'll never share your email with anyone else.")
                            .css("color", "blue")
                            .fadeIn().delay(2000).fadeOut();
                    
                }
                else{
                     $("#emailHelp").text("email is required.")
                            .css("color", "red")
                            .fadeIn().delay(2000).fadeOut();
                }
               
                 
       

        $.ajax({
            url: st_id ? `/student/edit/${st_id}`:`/student/create/`,
            method:"POST",
            data:{
                st_id:st_id,
                fname: fname,
                lname: lname,
                contact:contact,
                gender:gender,
                language:language,
                email: email,
                city:city,
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
            },
            success: function(response){
                            $("#fname").val("");
                            $("#lname").val("");
                            $("#lang").val("");
                            $("#city").val("");
                            $("#displayValue").val("");
                            $("#email").val("");
                            $("#contact").val("");
                            $("#studentList").html(response.students)

            },
            error: function(error){
                     const errorMessage = error.responseJSON?.message || "An error occurred.";
                $("#message").text(errorMessage)
                    .css("color", "red")
                    .fadeIn().delay(2000).fadeOut();
            },
        })



    })

    // for seach in nav
    $(".btn-outline-success").click(function(e){
        $("#studentForm").text("Score card");
        $("#form-data").hide();
        $("#data_table").hide();
        e.preventDefault()
        // console.log("searched")
        // const srch_name = $("#search_fname").val()
        grade_id = $(this).data("id")
        console.log(grade_id)

        // if (!srch_name) {
        //     $("#message").text("Search name cannot be empty.")
        //         .css("color", "red")
        //         .fadeIn().delay(2000).fadeOut();
        //     return;
        // }
        
        $.ajax({
            url:`/student/search_student/`,
            method:"POST",
            data:{
                grade_id : grade_id,
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
            },
            success:function(srch_response){
                  $("#search_fname").val("")
                $("#studentDetails").html(srch_response.student)
            },
            error: function(error){
                    const errorMessage = error.responseJSON?.message || "An error occurred.";
                $("#message").text(errorMessage)
                    .css("color", "red")
                    .fadeIn().delay(2000).fadeOut();
            },
        })


        

    })

    //edit
        $(document).on("click", ".edit-student", function () {
        const stId = $(this).data("id");
        const fname = $(this).data("fname");
        const lname = $(this).data("lname");
        const gender = $(this).data("gender");
        const city = $(this).data("city");
        const language = $(this).data("language");
        const contact = $(this).data("contact");
        const email = $(this).data("email");
        $("#st_id").val(stId);
        $("#fname").val(fname);
        $("#lname").val(lname);
        $("#lang").val(language);
        $("#city").val(city);
        $("#displayValue").val(gender);
        $("#email").val(email);
        $("#contact").val(contact);
        $("#student-title").text("Edit Details");
        $("#btn-create").text("Update");
    });


    // delete 
    $(document).on("click", ".del-student", function () {
        const st_id = $(this).data("id");
        alert("Do u want to delete the record permanently?")
        console.log(st_id)
        $.ajax({
            url:`/student/delete/${st_id}/`,
            method: "POST",
            data: {
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
            },
            success: function (response) {
                // Reset form and UI
                $("#message").text("deleted successfully!")
                    .css("color", "green")
                    .fadeIn().delay(2000).fadeOut();

                //new table after deleting one row
                $("#studentList").html(response.students);
              
            },
            error: function (error) {
                $("#message").text("Failed to delete the data")
                    .css("color", "red")
                    .fadeIn().delay(2000).fadeOut();
            }
        });
        
        
    });

    

})

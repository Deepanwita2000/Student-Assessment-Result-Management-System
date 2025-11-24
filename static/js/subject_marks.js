$(document).ready(function(){
    console.log("ajax is loaded!!")

    $('#cardForm').hide();

    $('#hide').click(function(e){
        $('#cardForm').hide();
    })

    $('#show').click(function(e){
        $('#cardForm').show();
    })

    // $(".edit-student").click(function(e){
    //      $('#cardForm').show();
    // })

    $(".edit-subjects").click(function(e){
         $('#cardForm').show();
    })

    // create and edit
    $("#add_marks_btn").click(function(e){
        e.preventDefault()
         console.log("clicked!!")

        //  fetch data from template
                sub_id= $("#sub_id").val() 
                stu_id= $("#stu").val()     
                assmt_id= $("#assmt").val()
                maths= $("#maths").val()
                physics= $("#physics").val()
              
                chemistry= $("#chemistry").val()
                english= $("#english").val()
                hindi= $("#hindi").val()
                bengali= $("#bengali").val()


                // check for empty fields
          $.ajax({
            url: sub_id ? `/subjects/edit_marks/${sub_id}/`:`/subjects/add_marks/`,
            method:"POST",
            data:{
                sub_id:sub_id,
                stu_id: stu_id,
                assmt_id: assmt_id,
                maths:maths,
                physics:physics,
                chemistry:chemistry,
                english: english,
                hindi:hindi,
                bengali:bengali,
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
            },
            success: function(response){
                            // $("#fname").val("")    
                            // $("#lname").val("")
                            // $("#email").val("")
                            // $("#phy").val("")
                            // $("#comp").val("")
                            // $("#math").val("")
                            $("#subList").html(response.subjects)

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
   

    //edit
        $(document).on("click", ".edit-subjects", function () {
         sub_id = $(this).data("id");
         maths = $(this).data("maths");
         physics = $(this).data("physics");
         chemistry = $(this).data("chemistry");
         english = $(this).data("english");
         hindi = $(this).data("hindi");
         bengali = $(this).data("bengali");
         percentage = $(this).data("percentage");
         total_marks = $(this).data("total_marks");
         assmt = $(this).data("assessment-id");
         stu = $(this).data("student-id");
        
        $("#sub_id").val(sub_id); // sub id
        $("#stu").val(stu);     // student id
        $("#assmt").val(assmt); // asmt id

        $("#maths").val(maths);
        $("#physics").val(physics);
        $("#chemistry").val(chemistry);
        $("#english").val(english);
        $("#hindi").val(hindi);
        $("#bengali").val(bengali);
        // $("#bengali").val(bengali);
       
        $("#studentForm").text("Edit Details");
        $("#btn-create").text("Update");
    });
    // data-id="{{ sub.id }}" 
    //             data-maths="{{ sub.maths }}"
    //             data-physics="{{ sub.physics }}"
    //             data-chemistry="{{ sub.chemistry }}"
    //             data-english="{{sub.english }}"
    //             data-hindi="{{ sub.hindi }}"
    //             data-bengali="{{ sub.bengali }}"
    //             data-percentage="{{ sub.percentage }}"
    //             data-total_marks="{{ sub.total_marks }}"
    //             data-assessment-id="{{ sub.assessment-id }}"
    //             data-student-id="{{ sub.student-id }}"
               


    // delete 
    $(document).on("click", ".del-subjects", function () {
        const sub_id = $(this).data("id");
        alert("Do u want to delete the record permanently?")
        console.log(sub_id)
        $.ajax({
            url:`/subjects/delete_marks/${sub_id}/`,
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
                $("#subList").html(response.subjects);
              
            },
            error: function (error) {
                $("#message").text("Failed to delete the data")
                    .css("color", "red")
                    .fadeIn().delay(2000).fadeOut();
            }
        });
        
        
    });

    

})

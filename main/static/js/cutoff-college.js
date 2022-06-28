function get_colleges() {
    $(".loader").css("display", "block");
    $.post(
        "college-cutoff/ajax/get-colleges",
        {
            "category_name": $("#id_course_category").val()
        },
        function (data, status) {
            $(".loader").css("display", "none");
            var colleges = data["colleges"];
            $("#id_college").empty();
            $("#id_college").prepend("<option>--select--</option>");
            colleges.forEach(element => {
                $("#id_college").prepend(
                    `<option value="${element.code}">${element.code} - ${element.college}</option>`
                )
            });

        }
    )
}


function get_data() {
    if ($("#id_category").val() !== "") {
        $(".loader").css("display", "block");
        $.post(
            "college-cutoff/ajax/get-data",
            {
                "college_code": $("#id_college").val(),
                "category": $("#id_category").val(),
                "round": $("#id_round").val()
            },
            function (data, status) {
                $(".loader").css("display", "none");
                var colleges = data["course_cutoff"];
                $("#college_cutoff_table").css("display", "block");
    
                $("#course_cutoff").empty();
                $("#college_name").empty();
                $("#college_name").prepend(data["college_name"]);
    
                colleges.forEach(ele => {
                    $("#course_cutoff").prepend(`<tr><td>${ele[0]}</td><td>${ele[1]}</td></tr>`);
                });
            }
        )    
    }
    
}


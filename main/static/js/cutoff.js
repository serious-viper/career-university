

function get_courses(category_name) {
    $(".loader").css("display", "block");
    $.post(
        "kcet-cutoff/ajax/get-courses",
        {
            "course_category_name": category_name
        },
        function (data, status) {
            $(".loader").css("display", "none");
            var courses = data["courses"];
            $("#id_course").empty();
            $("#id_course").prepend("<option>--select--</option>");
            courses.forEach(element => {
                $("#id_course").prepend(
                    `<option value="${element}">${element}</option>`
                )
            });
        }
    )
}




function get_cutoff_table() {
    var course = $("#id_course").val();
    var rank = $("#id_kcet_rank").val();
    var res_category = $("#id_category").val();
    var round = $("#id_round").val();
    if (course !== '--select--' && rank !== '' && res_category !== '--select--') {
        $(".loader").css("display", "block");
        $.post(
            "kcet-cutoff/ajax/get-data",
            {
                "course": course,
                "rank": rank,
                "reservation": res_category,
                "round": round
            },
            function (data, status) {
                $(".loader").css("display", "none");
                $("#scroll_focus").css("display", "block");
                var data_list = data["data"];
                $("#id_data").empty();
                data_list.forEach(element => {
                    $("#id_data").prepend(
                        `<div class="card shadow mb-2">
                            <div class="card-body">
                                <h5 class="card-title">${element[2]}</h5>
                            </div>
                            <ul class="list-group list-group-flush">
                                <li class="list-group-item">College Code: ${element[0]}</li>
                                <li class="list-group-item">Cutoff: ${element[1]}</li>
                                <li class="list-group-item">Hyd- Cutoff: ${element[3]}</li>
                            </ul>
                        </div>`
                    )
                })
                document.getElementById("scroll_focus").scrollIntoView();
            }

        )
    }
}
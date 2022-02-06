$(document).ready(function () {
    $("#myForm").keyup(function () {
        $.ajax({
            url: "/employees-ajax/",
            data: {
                // ordering: $(this).attr('id'),
                search: $("#search").val()
            },
            success: function (response) {
                $(".employees").html("");
                for (let key in response) {
                    $(".employees").append(`<div><h2>${response[key]['fio']} (${response[key]['id']})</h2>${response[key]['position']} | ${response[key]['chief_name']} | ${response[key]['salary']} | ${response[key]['join_date']}</div><hr>`)
                }
            }
        });
    });

    $('.getOrdering').click(function () {
        $.ajax({
            url: "/employees-ajax/",
            type: 'GET',
            data: {
                ordering: $(this).attr('id'),
                search: $("#search").val()
            },
            success: function (response) {
                $(".employees").html("");
                for (let key in response) {
                    $(".employees").append(`<div><h2>${response[key]['fio']} (${response[key]['id']})</h2>${response[key]['position']} | ${response[key]['chief_name']} | ${response[key]['salary']} | ${response[key]['join_date']}</div><hr>`)
                }
            }
        });
    });
});
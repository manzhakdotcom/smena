$(function () {
    $("#delete").click(function () {
        var type = $(this).attr("data-type");
        var id = $(this).attr("data-id");
        var url = window.location.origin + '/journal/delete/' + type + '/' + id + '/';
        $.ajax({
            url: url,
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                console.log('Start')
            },
            success: function (data) {
                console.log('Success')
            }
        });
    });

});
$(function () {
    $(".delete").click(function (e) {
        if (confirm('Вы уверены, что хотите удалить запись?')){
            e.preventDefault();

            $.ajax({
                url: '/journal/delete',
                type: 'get',
                dataType: 'text',
                data: {
                    'type': $(this).attr("data-type"),
                    'id': $(this).attr("data-id"),
                },
                success: function (data) {
                    if('Ok' == data) {
                        alert('Запись удалена. Перезагрузите страницу.')
                    }
                }
            });
        }
    });
});
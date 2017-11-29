function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", $('input[name=csrfmiddlewaretoken]').val());
        }
    }
});

$('button').click(function () {
    $.ajax({
        url: $('form').attr("action"),
        type: "POST",
        data: {
            form: $('form').serialize(),
        },
        error: function () {
            alert('Ошибка получения запроса, перезагрузите страницу');
        },
        success: function (data) {
            if (data.success) {
            $(location).attr('href', data.url_redirect);
            } else  {
            $('#error').text(data.errors);
            }
        }
    });
    return false;
});

$('button').click(function () {


    $.ajax({
        url: $('form').attr("action"),
        type: "POST",
        data: {
            form: $('form').serialize(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },

        error: function () {
            alert('Ошибка получения запроса');
        },
        success: function (data) {


            console.log(data);



            if (data.answer === "ok" ) {

                $(location).attr('href', data.url_redirect);


            } else if (data.answer === "bad" ) {

                $('#error').text(data.errors);

            }

        }
    });
    return false;
});

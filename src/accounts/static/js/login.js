$(function () {
    $('.fa-eye').click(() => {

        $(this).toggleClass("fa-eye");
        $(this).toggleClass("fa-eye-slash");

        if ($('#id_password').attr('type') == 'password') {
            $('#id_password').attr('type', 'text');
        } else {
            $('#id_password').attr('type', 'password');
        }
    });
});




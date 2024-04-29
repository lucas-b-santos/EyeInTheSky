$(function () {

    window.setTimeout(function () {
        $(".alert").fadeTo(1000, 0).slideUp(1000, function () {
            $(this).remove();
        });
    }, 5000);

    let eyeBtn = $('.fa-eye');
    
    for (let i = 0; i < eyeBtn.length; i++) {
        $(eyeBtn[i]).click(function () {
            $(this).toggleClass("fa-eye");
            $(this).toggleClass("fa-eye-slash");

            let id = "#id_password" + (i + 1).toString();

            if ($(id).attr('type') == 'password') {
                $(id).attr('type', 'text');
            } else {
                $(id).attr('type', 'password');
            }
        });
    }
});




$(function () {

    window.setTimeout(function () {
        $(".alert").fadeTo(700, 0).slideUp(700, function () {
            $(this).remove();
        });
    }, 5000);

    $('#password-eye').click(() => {
        $('#password-eye').toggleClass("fa-eye");
        $('#password-eye').toggleClass("fa-eye-slash");

        if ($('#id_password').attr('type') == 'password') {
            $('#id_password').attr('type', 'text');
        } else {
            $('#id_password').attr('type', 'password');
        }
    });

    $("#id_cpf").mask("000.000.000-00");

    // Validação de campos client-side
    const form = document.querySelector('form');

    $("input[name='login_option']").on('input', function() {
        $("#cpf_container").toggleClass("d-none");
        $("#username_container").toggleClass("d-none");
    });

    form.addEventListener('submit', function (event) {
        let formValido = true;

        for (let i = 0; i < form.length; i++) {//retira todas as mensagens de feedback do form
            form[i].classList.remove("is-invalid");
            form[i].classList.remove("is-valid");
        }

        for (let i = 0; i < form.length; i++) {
            if (!form[i].value && form[i].tagName == "INPUT") {//verifica campo vazio
                $("#invalid-feedback-" + form[i].getAttribute("id").slice(3)).html("Preencha este campo.");
                form[i].classList.add('is-invalid');
                formValido = false;
            }
        }
        if (formValido) {
            form.submit();
            return;
        } else {
            event.preventDefault();
            event.stopPropagation();
        }
    });
});




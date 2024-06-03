$(function () {
    $(".errorlist").addClass("text-danger");

    window.setTimeout(function () {
        $(".alert").fadeTo(700, 0).slideUp(700, function () {
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

    /*O Django gera automaticamente os IDs dos campos concatenando a palavra id com o nome do campo
     (id_*nome-do-campo*); logo, eu aplico as máscaras nos devidos campos como é mostrado abaixo.*/
    $("#id_cpf").mask("000.000.000-00");

    // Validação de campos client-side
    const form = document.querySelector('form');

    form.addEventListener('submit', function (event) {

        $(".errorlist").html("");

        let formValido = true;

        for (let i = 0; i < form.length; i++) {//retira todas as mensagens de feedback do form
            form[i].classList.remove("is-invalid");
            form[i].classList.remove("is-valid");
        }

        for (let i = 0; i < form.length; i++) {
            if (!form[i].value && form[i].tagName == "INPUT") {//verifica campo vazio
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




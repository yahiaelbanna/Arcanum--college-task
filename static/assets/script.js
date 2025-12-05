let password = document.querySelector('#password-container')
if (password) {
    let toggle = password.querySelector('span'),
        icon = toggle.querySelector('i'),
        input = password.querySelector('input');

    toggle.addEventListener('click', e => {
        icon.classList.toggle('bx-eye');
        icon.classList.toggle('bx-eye-closed');
        if (icon.classList.contains('bx-eye-closed')) {
            input.type = 'text';
        } else {
            input.type = 'password';
        }
    })
}
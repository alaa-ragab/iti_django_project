const password = document.getElementById("password")
const confirm_password = document.getElementById("confirm_password")
const reset_password_form = document.getElementById("reset-password-form")
const password_error = document.getElementById("password_error");
const confirm_password_error = document.getElementById("confirm_password_error")

reset_password_form.onsubmit = (e) => {
    e.preventDefault()
    if(validateResetPasswordForm()){
        reset_password_form.submit();          
    }
}
function validateResetPasswordForm(){
    let isValid = true
    password_error.innerHTML = "";
    confirm_password_error.innerHTML = "";
    if (!password.value) {
        password_error.innerHTML = "Password can not be empty";
        isValid = false;
    } else if (password.value.length < 8) {
        password_error.innerHTML = "Password must be at least 8 characters";
        isValid = false;
    }

    if (confirm_password.value != password.value) {
    confirm_password_error.innerHTML = "Password does not match"
    isValid = false;
    }
    return isValid  
}

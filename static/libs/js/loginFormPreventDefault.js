
const loginForm = document.getElementById("loginForm")
const login_email = document.getElementById("login_email")
const login_password = document.getElementById("login_password")
const login_email_error = document.getElementById("login_email_error")
const login_password_error = document.getElementById("login_password_error")



loginForm.onsubmit = (e) => {
    e.preventDefault()
    validateLoginForm() 
    if(validateLoginForm()){
        loginForm.submit();
    }                        
}

function validateLoginForm() {
    login_email_error.innerHTML = ""
    login_password_error.innerHTML = ""
    let isValid = true;

    if(!validateEmail(login_email.value)){
        login_email_error.innerHTML = "Not a valid email address"
        isValid = false
    }
    if(!login_password){
        login_password_error.innerHTML = "Password can not be empty"
        isValid = false
    }else if(login_password.value < 8){
        login_password_error.innerHTML = "Password characters must be more than or equal 8 characters"
        isValid = false
    }
    return isValid
}


function validateEmail(email){
    var re = /[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$/
    return re.test(String(email).toLowerCase())

}
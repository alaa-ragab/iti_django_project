const forger_password_form = document.getElementById("forget-password-form")
const registered_email = document.getElementById("email")
const email_error = document.getElementById("email_error")

forger_password_form.onsubmit = (e) => {
    e.preventDefault()
    if(!validateEmail(registered_email.value)){
    email_error.innerHTML = "Not a valid email address"                      
    }else{
            forger_password_form.submit();
        }  
    }


function validateEmail(email){
    var re = /[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$/
    return re.test(String(email).toLowerCase())

}
const registerForm = document.getElementById("registerForm")
const first_name = document.getElementById("first_name")
const last_name = document.getElementById("last_name")
const email = document.getElementById("email")
const password = document.getElementById("password")
const confirm_password = document.getElementById("confirm_password")
const phone_number = document.getElementById("phone_number")
// error_message = document.getElementById("error_message")

const first_name_error = document.getElementById("first_name_error");
const last_name_error = document.getElementById("last_name_error");
const email_error = document.getElementById("email_error");
const password_error = document.getElementById("password_error");
const confirm_password_error = document.getElementById("confirm_password_error")
const phone_number_error = document.getElementById("phone_number_error")




const csrf_token = document.getElementsByName("csrfmiddlewaretoken")
registerForm.onsubmit = (e) => {
    e.preventDefault() 
    if(validateForm()){
        registerForm.submit();
    }                        
}




function validateForm() {
    let isValid = true;
    first_name_error.innerHTML = "";
    last_name_error.innerHTML = "";
    email_error.innerHTML = "";
    password_error.innerHTML = "";
    confirm_password_error.innerHTML = "";
    phone_number_error.innerHTML = "";

    if (!first_name.value) {
        first_name_error.innerHTML = "First Name can not be empty";
        isValid = false;
    }
    
    if (!last_name.value) {
        last_name_error.innerHTML = "Last Name can not be empty";
        isValid = false;
    }

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
    
  

    if (!validateEmail(email.value)) {
        email_error.innerHTML = "Not a valid email";
        isValid = false;
    } 

    if (!phone_number.value) {
        phone_number_error.innerHTML = "Phone Number can not be empty"
        isValid = false;
    }
    else{
        
        // var phone_re  = /^(01)[012][0-9]{8}/
        var phone_re = /^01[012][0-9]{8}/
        if (!phone_re.test(phone_number.value)){
            phone_number_error.innerHTML = "Phone Number must Be 11 digits and starts with {010 or  011 or 012 }"
            isValid = false
        }
    }
    return isValid;
}

function validateEmail(email){
    var re = /[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$/
    return re.test(String(email).toLowerCase())

}




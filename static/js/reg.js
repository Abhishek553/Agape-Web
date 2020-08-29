function validate_reg() {

    let form=document.getElementsByTagName("form")[0];
    let message=document.getElementsByClassName("message");
    let username=form[0].value;
    let email=form[1].value;
    let newpassword=form[2].value;
    let confpassword=form[3].value;

    if(username===""){
        message[0].innerHTML="Please enter your full name";
        return false;
    }
    if(email===""){
        message[1].innerHTML="Please enter email-id";
        return false;
    }
    if(newpassword===""){
        message[2].innerHTML="Please enter password";
        return false;
    }
    if(confpassword===""){
        message[3].innerHTML="Please confirm your password";
        return false;
    }
    
    return true;
}
function validate() {

    let form=document.getElementsByTagName("form")[0];
    let message=document.getElementsByClassName("message");
    let username=form[0].value;
    let password=form[1].value;

    if(username===""){
        message[0].innerHTML="Please enter username";
        return false;
    }
    if(password===""){
        message[1].innerHTML="Please enter password";
        return false;
    }
    return true;
}
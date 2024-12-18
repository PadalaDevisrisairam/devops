function password(){
    let password = document.getElementById("Password").value ;
    let confirmpass=document.getElementById("confirm password").value;
    let phonenumber=document.getElementById("Phonenumber").value;
    let length=phonenumber.toString().length;
    let male=document.getElementById("male").value;
    let female=document.getElementById("female").value;
    if(password !== confirmpass)
    {
        alert("password and the confirm password must be same");
    }
    else if(length !== 10)
    {
        alert("enter valid phone number digits")
    }
    else if(male!=="male" || female!=="female")
    {
        alert("select your gender")
    }
}
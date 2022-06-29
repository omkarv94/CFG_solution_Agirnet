var un = document.querySelector(".un");
var ee = document.querySelector(".ee");
var pp = document.querySelector(".pp");
var cp = document.querySelector(".cp");

function clearErrors(){

    un.value=null;
    ee.value=null;
    pp.value=null;
    cp.value=null;

    // for(let item of errors)
    // {
    //     item.innerHTML = "";
    // }
}

function validateForm(){
    // var returnval = true;

    // console.log(pp.value);
    // console.log(cp.value)
    if (pp.value != cp.value){
        event.preventDefault();
        alert("Confirm password and password should be same");
        // returnval = false;
    }
    else{
        alert("Your registration was successfull. Return to Login page to login into your account");
        clearErrors();
    }
    // return returnval;
}


var state= document.querySelectorAll(".password")
var eye= document.querySelectorAll(".eye1")
// var eyec= document.querySelector(".eye")
var eyec1= document.querySelector(".eye2")
// eyec.style.color='black';

eye.forEach(eyeIcon =>{
    eyeIcon.addEventListener("click",()=>{
        state.forEach(state=>{
            if(state.type==="password"){
                state.type = "text";
                // eyec.style.color='blue';
                eyec1.style.color='blue';
                
            }
            else{
                state.type = "password";
                // eyec.style.color='black';
                eyec1.style.color='black';
            }
        })
    })
})





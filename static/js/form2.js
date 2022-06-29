var state= document.querySelectorAll(".password")
var eye= document.querySelectorAll(".eye1")
var eyec= document.querySelector(".eye")
// var eyec1= document.querySelector(".eye2")
// eyec.style.color='black';

eye.forEach(eyeIcon =>{
    eyeIcon.addEventListener("click",()=>{
        state.forEach(state=>{
            if(state.type==="password"){
                state.type = "text";
                eyec.style.color='blue';
                // eyec1.style.color='blue';
                
            }
            else{
                state.type = "password";
                eyec.style.color='black';
                // eyec1.style.color='black';
            }
        })
    })
})

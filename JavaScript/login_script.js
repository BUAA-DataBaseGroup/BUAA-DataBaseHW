const signinBtn = document.getElementById("signin");
const signupBtn = document.getElementById("signup");
const firstForm = document.getElementById("form1");
const secondForm = document.getElementById("form2");
const containter = document.querySelector(".container")


signinBtn.addEventListener("click",()=>{
    containter.classList.remove("right-panel-active")
})

signupBtn.addEventListener("click",()=>{
    containter.classList.add("right-panel-active")
})

firstForm.addEventListener("submit",(e) => e.preventDefault())
secondForm.addEventListener("submit",(e) => e.preventDefault())

const $submit = document.getElementById("submit"),
      $password = document.getElementById("password"),
      $username = document.getElementById("username");


document.addEventListener("click", (e)=>{
    e.preventDefault();
    if(e.target === $submit){

        if($password.value && $username.value){
        //if($password.value === "12345*" && $username.value === "madur01"){
            //e.preventDefault();

            window.location.href = "../templates/tabla_libro.html"
            //window.location = "../templates/tabla_libro.html";
        }
    else{
        alert("Datos Incorrectos")
    }
    }
})

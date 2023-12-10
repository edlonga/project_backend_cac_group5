const $submit = document.getElementById("submit"),
      $password = document.getElementById("password"),
      $usarname = document.getElementById("usarname");


document.addEventListener("click", (e)=>{
    if(e.target === $submit){
        if($password.value === "1234" && $usarname.value === "admin"){
            e.preventDefault();
            window.location = "../templates/tabla_libro.html";
        }
    else{
        alert("Datos Incorrectos")
    }
    }
})

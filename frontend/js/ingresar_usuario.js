function guardar() {
    let nombre_ingresado = document.getElementById("nombre").value //input
    let apellido_ingresado = document.getElementById("apellido").value 
    let email_ingresado = document.getElementById("email").value 
    let nickname_ingresado = document.getElementById("nickname").value
    let contrasena_ingresado = document.getElementById("contrasena").value 

    console.log(nombre_ingresado,apellido_ingresado,email_ingresado,nickname_ingresado,contrasena_ingresado);
    // Se arma el objeto de js 
    let datos = {
        nombre:nombre_ingresado,
        apellido:apellido_ingresado,
        email: email_ingresado,
        nickname:nickname_ingresado,
        contrasena:contrasena_ingresado,

    }
    console.log(datos);
    
    let url = "https://bibliofilos23529.pythonanywhere.com/registro_usuario"
    var options = {
        body: JSON.stringify(datos),
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
    }
    
    fetch(url, options)
        .then(response => {
            if (response.ok) {
                return response.json(); // o response.text() si la respuesta no es JSON
            } else {
                throw new Error('Algo salió mal en el servidor');
            }
        })
        .then(data => {
            console.log("Usuario creado", data);
            alert("Usuario Guardado");
            window.location.href = "../templates/tabla_usuario.html";

    /*fetch(url, options)
        .then(function () {
            console.log("creado")
            alert("Usuario Guardado")
            // Devuelve el href (URL) de la página actual
            window.location.href = "../templates/tabla_usuario.html";  
            
        })*/

        .catch(err => {
            //this.errored = true
            alert("Error al grabar" )
            console.error(err);
        })
}
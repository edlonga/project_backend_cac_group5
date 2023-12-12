function guardar() {
    let titulo_ingresado = document.getElementById("titulo").value //input
    let autor_ingresado = document.getElementById("autor").value 
    let idioma_ingresado = document.getElementById("idioma").value 
    let edicion_ingresado = document.getElementById("edicion").value
    let genero_ingresado = document.getElementById("genero").value 
    let isbn_ingresado = document.getElementById("isbn").value 
    let imagen_ingresado = document.getElementById("imagen").value 
    let colaborador_ingresado = document.getElementById("colaborador").value 


    console.log(titulo_ingresado,autor_ingresado,idioma_ingresado,edicion_ingresado,genero_ingresado,isbn_ingresado,imagen_ingresado,colaborador_ingresado);
    // Se arma el objeto de js 
    let datos = {
        titulo:titulo_ingresado,
        autor:autor_ingresado,
        idioma:idioma_ingresado,
        edicion:edicion_ingresado,
        genero:genero_ingresado,
        isbn:isbn_ingresado,
        imagen:imagen_ingresado,
        colaborador:colaborador_ingresado
    }
    console.log(datos);
    
    let url = "https://bibliofilos23529.pythonanywhere.com/registro_libro"
    var options = {
        body: JSON.stringify(datos),
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
    }
    fetch(url, options)
        .then(function () {
            console.log("creado")
            alert("Libro Guardado")
            // Devuelve el href (URL) de la página actual
            window.location.href = "../templates/tabla_libro.html";  
            
        })
        .catch(err => {
            //this.errored = true
            alert("Error al grabar" )
            console.error(err);
        })
}
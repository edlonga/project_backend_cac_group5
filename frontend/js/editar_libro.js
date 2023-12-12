function modificar() {
    let id = document.getElementById("id_libro").value
    let titulo_ingresado = document.getElementById("titulo").value
    let autor_ingresado = document.getElementById("autor").value 
    let idioma_ingresado = document.getElementById("idioma").value 
    let edicion_ingresado = document.getElementById("edicion").value
    let genero_ingresado = document.getElementById("genero").value 
    let isbn_ingresado = document.getElementById("isbn").value 
    let imagen_ingresado = document.getElementById("imagen").value
    let colaborador_ingresado = document.getElementById("colaborador").value 
    
    let datos = {
        titulo: titulo_ingresado,
        autor:autor_ingresado,
        idioma:idioma_ingresado,
        edicion:edicion_ingresado,
        genero:genero_ingresado,
        isbn:isbn_ingresado,
        imagen:imagen_ingresado,
        colaborador:colaborador_ingresado
    }

    console.log(datos);

    let url = "https://bibliofilos23529.pythonanywhere.com/update_libro/"+id
    var options = {
        body: JSON.stringify(datos),
        method: 'PUT',
        
        headers: { 'Content-Type': 'application/json' },
        // el navegador seguirá automáticamente las redirecciones y
        // devolverá el recurso final al que se ha redirigido.
        redirect: 'follow'
    }
    fetch(url, options)
        .then(function () {
            console.log("modificado")
            alert("Registro modificado")

            //Puedes utilizar window.location.href para obtener la URL actual, redirigir a otras páginas
           window.location.href = "../templates/tabla_libro.html";
          
        })
        .catch(err => {
            this.error = true
            console.error(err);
            alert("Error al Modificar")
        })      
}
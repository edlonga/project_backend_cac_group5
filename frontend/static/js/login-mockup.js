function enviarForm() {
    var dataForm = new FormData();


    form_data = JSON.stringify({
        "nombre" : document.getElementById("nombre").value,
        "apellido" : document.getElementById("apellido").value,
        "nickname" : document.getElementById("nickname").value,
        "email" : document.getElementById("email").value,
    })
    
    try {
        //remplazar url con el host que se esté usando actualmente
        //IMPORTANTE, USAR HTTPS
        fetch("https://lcs1423.pythonanywhere.com/registro_usuario", {
            method: "POST",
            body: form_data,
            headers : {"Content-Type" : "application/json"}
        })

        alert("formulario recibido con exito")
    } catch (error) {
        alert(error)
    }

}
function enviarForm() {
    var dataForm = new FormData();


    form_data = JSON.stringify({
        "nombre" : document.getElementById("nombre").value,
        "apellido" : document.getElementById("apellido").value,
        "nickname" : document.getElementById("nickname").value,
        "email" : document.getElementById("email").value,
    })

    try {
        fetch("http://127.0.0.1:5000/registro_usuario", {
            method: "POST",
            body: form_data,
            headers : {"Content-Type" : "application/json"}
        })

        alert("formulario recibido con exito")
    } catch (error) {
        alert(error)
    }

}
function validarFormularioSumate() {
    //Obtener los valores
    var nombre = document.getElementById("nombre").value.trim()
    var apellido = document.getElementById("apellido").value.trim()
    var email = document.getElementById("email").value.trim()
    var nickname = document.getElementById("nickname").value.trim()
    var contraseña = document.getElementById("contraseña").value.trim()

    //Verificar si hay campos vacios
    if(nombre==="" || apellido==="" || email==="" || nickname===""|| contraseña===""){
        alert("Por favor, complete todos los campos del formulario.")
        return false
    }

    // Verificar si el nombre contiene solo caracteres alfabéticos (incluidos tildes del español) o espacios
    var nombreTest = /^[a-zA-ZÁÉÍÓÚáéíóúñ ]+$/.test(nombre);
    if(nombreTest===false){
      alert("ingrese un nombre válido con las letras del abecedario.")
      return false
    }

    // Verificar si el apellido contiene solo caracteres alfabéticos (incluidos tildes del español) o espacios
    var apellidoTest = /^[a-zA-ZÁÉÍÓÚáéíóúñ ]+$/.test(apellido);
    if(apellidoTest===false){
      alert("ingrese un apellido válido con las letras del abecedario.")
      return false
    }


    //Si supera las validaciones
    alert("¡Formulario enviado con éxito, puedes ingresar!")
    return true
}

function validarFormularioContacto() {
    //Obtener los valores
    var mail_contacto = document.getElementById("mail_contacto").value.trim()
    var comentario = document.getElementById("comentario").value.trim()

    //Verificar si hay campos vacios
    if(mail_contacto==="" || comentario===""){
        alert("Complete todos los campos del formulario.")
        return false
    }

    //Si supera las validaciones
    alert("Consulta enviada con éxito!")
    return true
}
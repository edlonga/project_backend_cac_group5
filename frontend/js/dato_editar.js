// Procedimiento para traer los datos del registro a editar
// Ej: "id=9&nombre=bulbasaur"
let cadena = location.search; // Cadena con los símbolos & y =

// Crear un objeto URLSearchParams con la cadena
// El objeto URLSearchParams en JavaScript es una
// interfaz que proporciona métodos y propiedades para
// trabajar con las cadenas de consulta (query strings) en URLs.
// Facilitando la obtención de parámetros y valores individuales
let datos = new URLSearchParams(cadena);

// Crear un objeto para almacenar los nombres de las variables y sus valores
let resultado = {};

// Iterar sobre los parámetros y guardar los nombres y valores en el objeto resultado
for (const [titulo, valor] of datos) {
    resultado[titulo] = valor;
    resultado[autor] = valor;
    resultado[idioma] = valor
    resultado[edicion] = valor
    resultado[genero] = valor
    resultado[isbn] = valor
    resultado[imagen] = valor
    resultado[colaborador]=valor
}

// Imprimir el resultado
console.log(resultado); // Esto mostrará un objeto con las variables y sus valores


// Procedimiento para mostrar los datos a editar en el formulario de edición
document.getElementById("id_libro").value = resultado["id_libro"]
document.getElementById("titulo").value = resultado["titulo"]
document.getElementById("autor").value = resultado["autor"]
document.getElementById("idioma").value = resultado["idioma"]
document.getElementById("edicion").value = resultado["edicion"]
document.getElementById("genero").value = resultado["genero"]
document.getElementById("isbn").value = resultado["isbn"]
document.getElementById("imagen").value = resultado["imagen"]
document.getElementById("colaborador").value = resultado["colaborador"]

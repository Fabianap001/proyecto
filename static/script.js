// Slider
var swiper = new Swiper(".mySwiper", {
    slidesPerView: 3,
    spaceBetween: 30,
    loop: true,
    loopFillGroupWithBlank: true,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev"
    },
    breakpoints: {
        0: {
            slidesPerView: 1
        },
        520: {
            slidesPerView: 2
        },
        950: {
            slidesPerView: 3
        }
    }
});

// Carrito
const carrito = document.getElementById('carrito');
const elementos = document.getElementById('lista');
const lista = document.querySelector('#lista-carrito tbody');
const vaciarCarritoBtn = document.getElementById('vaciar-carrito');

cargarEventListeners();

function cargarEventListeners() {
    elementos.addEventListener('click', comprarElemento);
    carrito.addEventListener('click', eliminarElemento);
    vaciarCarritoBtn.addEventListener('click', vaciarCarrito);
    document.addEventListener('DOMContentLoaded', leerLocalStorage);
}

function comprarElemento(e) {
    e.preventDefault();
    if (e.target.classList.contains('agregar-carrito')) {
        const elemento = e.target.parentElement.parentElement;
        leerDatosElemento(elemento);
    }
}

function leerDatosElemento(elemento) {
    const infoElemento = {
        imagen: elemento.querySelector('img').src,
        titulo: elemento.querySelector('h3').textContent,
        precio: elemento.querySelector('.precio').textContent,
        id: elemento.querySelector('a').getAttribute('data-id')
    };
    insertarCarrito(infoElemento);
}

function insertarCarrito(elemento) {
    const row = document.createElement('tr');
    row.innerHTML = `
    <td>
        <img src="${elemento.imagen}" width="100">
    </td>
    <td>${elemento.titulo}</td>
    <td>${elemento.precio}</td>
    <td>
        <a href="#" class="borrar" data-id="${elemento.id}">X</a>
    </td>
    `;
    lista.appendChild(row);
    guardarElementoLocalStorage(elemento);
}

function eliminarElemento(e) {
    e.preventDefault();
    if (e.target.classList.contains('borrar')) {
        e.target.parentElement.parentElement.remove();
        const elementoId = e.target.getAttribute('data-id');
        eliminarElementoLocalStorage(elementoId);
    }
}

function vaciarCarrito() {
    while (lista.firstChild) {
        lista.removeChild(lista.firstChild);
    }
    vaciarLocalStorage();
    return false;
}

function guardarElementoLocalStorage(elemento) {
    let elementos = obtenerElementosLocalStorage();
    elementos.push(elemento);
    localStorage.setItem('elementos', JSON.stringify(elementos));
}

function obtenerElementosLocalStorage() {
    let elementos;
    if (localStorage.getItem('elementos') === null) {
        elementos = [];
    } else {
        elementos = JSON.parse(localStorage.getItem('elementos'));
    }
    return elementos;
}

function leerLocalStorage() {
    let elementos = obtenerElementosLocalStorage();
    elementos.forEach(elemento => {
        insertarCarrito(elemento);
    });
}

function eliminarElementoLocalStorage(id) {
    let elementos = obtenerElementosLocalStorage();
    elementos = elementos.filter(elemento => elemento.id !== id);
    localStorage.setItem('elementos', JSON.stringify(elementos));
}

function vaciarLocalStorage() {
    localStorage.clear();
}

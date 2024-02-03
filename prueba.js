
let persona1 = {
    name: 'jose',
    edad: 25,
    viviendas: [
        {
            calle: '',
            numero: 5,
            pais: ''
        },

        {
            calle: '',
            numero: 5,
            pais: ''
        }
        ,
        {
            calle: '',
            numero: 5,
            pais: ''
        }
        ,{
            calle: '',
            numero: 5,
            pais: ''
        }
    ]
}

let listaNombre = ['jose', 'fer', 'cris']
let propiedadABuscar = 'numero'

let listaViviendas2 = persona1['viviendas']

let listaViviendas = persona1.viviendas

let buscarPropiedad = (vivienda, propiedadABuscar) =>{
    if(vivienda[propiedadABuscar] === 5){
        console.log(vivienda)
    }
}
console.log(persona1.name)
console.log(listaNombre[0])
import { Component } from '@angular/core';

@Component({
  selector: 'app-team',
  standalone: true,
  imports: [],
  templateUrl: './team.component.html',
  styleUrl: './team.component.css'
})
export class TeamComponent {

    /*
        ==========================================
        INTEGRANTES DE K'AK'B'E.LAB
        ==========================================

        Creamos un arreglo llamado "integrantes".

        Un arreglo nos permite guardar varios elementos
        dentro de una misma variable.

        En nuestro caso tendremos 5 integrantes.

        Cada integrante es un objeto que contiene:

        - nombre
        - rol
        - imagen

        Después Angular recorrerá este arreglo y creará
        automáticamente una tarjeta para cada integrante.
    */
    integrantes = [

        {
            nombre: 'Habil',
            rol: 'Coordinación general',
            imagen: 'assets/images/equipo/Ingrentante 1.jpeg'
        },

        {
            nombre: 'Nombre integrante 2',
            rol: 'Comunicación y redes',
            imagen: 'assets/images/equipo/integrante-2.jpg'
        },

        {
            nombre: 'Nombre integrante 3',
            rol: 'Talleres y contenido',
            imagen: 'assets/images/equipo/integrante-3.jpg'
        },

        {
            nombre: 'Nombre integrante 4',
            rol: 'Diseño y experiencia',
            imagen: 'assets/images/equipo/integrante-4.jpg'
        },

        {
            nombre: 'Nombre integrante 5',
            rol: 'Tecnología y desarrollo',
            imagen: 'assets/images/equipo/integrante-5.jpg'
        }

    ];

}

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
        INTEGRANTES
        ==========================================

        Cada objeto contiene únicamente información
        que cambia entre una integrante y otra.

        La carrera y la universidad NO se repiten aquí
        porque todas comparten esa información.
    */
    integrantes = [

        {
            nombre: 'Habil Xol Par',
            rol: 'Coordinación general',
            imagen: 'assets/equipo/integrante-1.jpeg',
            linkedin: 'https://www.linkedin.com/in/habilxol'
        },

        {
            nombre: 'Yoselin Amarilis López',
            rol: 'Comunicación y redes',
            imagen: 'assets/equipo/integrante-2.jpeg',
            linkedin: ''
        },

        {
            nombre: 'Yaxchel Xol Par',
            rol: 'Talleres y contenido',
            imagen: 'assets/equipo/integrante-3.jpeg',
            linkedin: ''
        },

        {
            nombre: 'Tatiana Ivonne López',
            rol: 'Diseño y experiencia',
            imagen: 'assets/equipo/integrante-4.jpeg',
            linkedin: ''
        },

        {
            nombre: 'Evelyn Carolina Castro',
            rol: 'Tecnología y desarrollo',
            imagen: 'assets/equipo/integrante-5.jpg',

            // LinkedIn real de Evelyn.
            linkedin: 'https://www.linkedin.com/in/evelyn-castro-8b761722b'
        }

    ];

}

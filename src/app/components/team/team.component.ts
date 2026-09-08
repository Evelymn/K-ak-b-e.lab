import { Component } from '@angular/core';

@Component({

    // Este es el nombre que utilizamos en HTML:
    //
    // <app-team></app-team>
    selector: 'app-team',

    // Indica que este componente funciona de forma
    // independiente y puede importarse directamente
    // dentro de otros componentes standalone.
    standalone: true,

    // TeamComponent por ahora no necesita importar
    // otros componentes, directivas o pipes.
    imports: [],

    // HTML que pertenece a este componente.
    templateUrl: './team.component.html',

    // CSS que pertenece a este componente.
    styleUrl: './team.component.css'

})
export class TeamComponent {

    /*
        Aquí guardamos la información de las integrantes.

        Angular recorrerá este arreglo desde el HTML
        utilizando @for.
    */
    integrantes = [
        {
            nombre: 'Habil',
            rol: 'Coordinación general',
            imagen: 'assets/equipo/integrante-1.jpeg'
        },

        {
            nombre: 'Nombre integrante 2',
            rol: 'Comunicación y redes',
            imagen: 'assets/equipo/integrante-2.jpeg'
        },

        {
            nombre: 'Nombre integrante 3',
            rol: 'Talleres y contenido',
            imagen: 'assets/equipo/integrante-3.jpeg'
        },

        {
            nombre: 'Nombre integrante 4',
            rol: 'Diseño y experiencia',
            imagen: 'assets/equipo/integrante-4.jpeg'
        },

        {
            nombre: 'Nombre integrante 5',
            rol: 'Tecnología y desarrollo',
            imagen: 'assets/equipo/integrante-5.jpeg'
        }
    ];
}

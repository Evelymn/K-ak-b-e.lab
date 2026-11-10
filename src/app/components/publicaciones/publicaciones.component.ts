
import { Component, inject, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';

import {
  PublicacionesService,
  Publicacion
} from '../../services/publicaciones.service';

@Component({
  selector: 'app-publicaciones',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './publicaciones.component.html',
  styleUrl: './publicaciones.component.css'
})
export class PublicacionesComponent implements OnInit {

  private publicacionesService = inject(PublicacionesService);

  publicaciones: Publicacion[] = [];
  destacada: Publicacion | null = null;
  otrasPublicaciones: Publicacion[] = [];

  cargando = true;
  error = '';

  ngOnInit(): void {
    this.publicacionesService.obtenerPublicaciones().subscribe({
      next: (datos) => {
        this.publicaciones = datos;

        // La primera publicación será la destacada.
        this.destacada = datos.length > 0 ? datos[0] : null;

        // Las demás aparecerán en una cuadrícula.
        this.otrasPublicaciones = datos.slice(1);

        this.cargando = false;
      },
      error: () => {
        this.error = 'No se pudieron cargar las publicaciones.';
        this.cargando = false;
      }
    });
  }
}

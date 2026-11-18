
import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';

import {
  ExperienciasService,
  Experiencia
} from '../../services/experiencias.service';


@Component({
  selector: 'app-experiences',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './experiences.component.html',
  styleUrl: './experiences.component.css'
})
export class ExperiencesComponent implements OnInit {

  // Servicio que consulta nuestra API de Django.
  private experienciasService = inject(ExperienciasService);

  // Lista de experiencias recibidas desde el backend.
  experiencias: Experiencia[] = [];

  // Indica si la solicitud todavía está en proceso.
  cargando = true;

  // Mensaje que mostraremos si ocurre un error.
  error = '';

  // Angular ejecuta este método al inicializar
  // el componente.
  ngOnInit(): void {
    this.cargarExperiencias();
  }

  cargarExperiencias(): void {

    this.cargando = true;
    this.error = '';

    this.experienciasService.obtenerExperiencias().subscribe({

      next: (datos: Experiencia[]) => {
        this.experiencias = datos;
        this.cargando = false;
      },

      error: () => {
        this.error = 'No se pudieron cargar las experiencias.';
        this.cargando = false;
      }

    });
  }
}

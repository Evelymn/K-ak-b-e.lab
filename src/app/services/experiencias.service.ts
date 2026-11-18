
import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

// Representa una fotografía de una experiencia.
export interface FotoExperiencia {
  id: number;
  imagen: string;
  texto_alternativo: string;
  orden: number;
}

// Representa una experiencia recibida desde Django.
export interface Experiencia {
  id: number;
  titulo: string;
  descripcion: string;
  fecha: string;
  categoria: string;
  fotografias: FotoExperiencia[];
}

@Injectable({
  providedIn: 'root'
})
export class ExperienciasService {

  // Permite realizar solicitudes HTTP.
  private http = inject(HttpClient);

  // Ruta relativa que utilizará nuestro proxy.
  private apiUrl = '/api/experiencias/';

  // Obtiene las experiencias publicadas.
  obtenerExperiencias(): Observable<Experiencia[]> {
    return this.http.get<Experiencia[]>(this.apiUrl);
  }
}

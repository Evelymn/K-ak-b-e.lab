
import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Publicacion {
  id: number;
  titulo: string;
  contenido: string;
  autora: string;
  categoria: string;
  estado: string;
  fecha_creacion: string;
}

@Injectable({
  providedIn: 'root'
})
export class PublicacionesService {

  private http = inject(HttpClient);

  private apiUrl = '/api/publicaciones/';

  obtenerPublicaciones(): Observable<Publicacion[]> {
    return this.http.get<Publicacion[]>(this.apiUrl);
  }
}

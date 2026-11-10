
import { Routes } from '@angular/router';

import { HomeComponent } from './components/home/home.component';
import { PublicacionesComponent } from './components/publicaciones/publicaciones.component';

export const routes: Routes = [
  {
    path: '',
    component: HomeComponent,
    pathMatch: 'full'
  },
  {
    path: 'publicaciones',
    component: PublicacionesComponent
  },
  {
    path: '**',
    redirectTo: ''
  }
];


import { Routes } from '@angular/router';

import { HomeComponent } from './components/home/home.component';
import { PublicacionesComponent } from './components/publicaciones/publicaciones.component';
import { ExperiencesComponent } from './components/experiences/experiences.component';

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
    path: 'experiencias',
    component: ExperiencesComponent
  },
  {
    path: '**',
    redirectTo: ''
  }
];

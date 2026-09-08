import { Component } from '@angular/core';

// Importamos nuestro componente Navbar
// para poder utilizarlo dentro de app.component.html.
import { NavbarComponent } from './components/navbar/navbar.component';
// Importamos HeroComponent para poder mostrar
// la sección principal de presentación.
import { HeroComponent } from './components/hero/hero.component';
import { AboutComponent } from './components/about/about.component';

// Importamos TeamComponent para poder mostrar
// la sección de integrantes de k’ak’b’e.lab.
import { TeamComponent } from './components/team/team.component';

@Component({
  selector: 'app-root',

  // standalone significa que este componente
  // funciona sin necesitar un AppModule tradicional.
  standalone: true,

  // Aquí registramos los componentes que queremos
  // utilizar dentro de app.component.html.
  //
  // Como queremos usar:
  // <app-navbar></app-navbar>
  //
  // agregamos NavbarComponent.
 imports: [
    NavbarComponent,
    HeroComponent,
    AboutComponent,
    TeamComponent
    // ActivitiesComponent
],


  templateUrl: './app.component.html',

  styleUrl: './app.component.css'
})
export class AppComponent {

}

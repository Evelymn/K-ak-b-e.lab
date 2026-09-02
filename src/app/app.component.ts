import { Component } from '@angular/core';

// Importamos nuestro componente Navbar
// para poder utilizarlo dentro de app.component.html.
import { NavbarComponent } from './components/navbar/navbar.component';
// Importamos HeroComponent para poder mostrar
// la sección principal de presentación.
import { HeroComponent } from './components/hero/hero.component';


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
    HeroComponent
],


  templateUrl: './app.component.html',

  styleUrl: './app.component.css'
})
export class AppComponent {

}

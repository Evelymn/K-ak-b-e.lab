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
// Importamos PurposeComponent.
//
// Este componente mostrará el propósito de k’ak’b’e.lab:
// por qué nace la comunidad y qué busca construir.
import { PurposeComponent } from './components/purpose/purpose.component';
/*
    Importamos ContactComponent para poder utilizar
    la sección de contacto dentro de nuestra página.
*/
import { ContactComponent } from './components/contact/contact.component';
// Importamos CollaborationComponent.
//
// Esta sección mostrará las diferentes formas
// en que empresas, profesionales e instituciones
// pueden colaborar con k’ak’b’e.lab.
import { CollaborationComponent } from './components/collaboration/collaboration.component';

// Importamos FooterComponent para mostrar
// el pie de página al final de nuestra aplicación.
import { FooterComponent } from './components/footer/footer.component';
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
    TeamComponent,
    PurposeComponent,
    CollaborationComponent,
    ContactComponent,
    FooterComponent
],


  templateUrl: './app.component.html',

  styleUrl: './app.component.css'
})
export class AppComponent {

}

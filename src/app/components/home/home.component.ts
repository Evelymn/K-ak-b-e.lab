
import { Component } from '@angular/core';

import { NavbarComponent } from '../navbar/navbar.component';
import { HeroComponent } from '../hero/hero.component';
import { PurposeComponent } from '../purpose/purpose.component';
import { TeamComponent } from '../team/team.component';
import { ExperiencesComponent } from '../experiences/experiences.component';
import { CollaborationComponent } from '../collaboration/collaboration.component';
import { ContactComponent } from '../contact/contact.component';
import { FooterComponent } from '../footer/footer.component';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [
    HeroComponent,
    PurposeComponent,
    TeamComponent,
    ExperiencesComponent,
    CollaborationComponent,
    ContactComponent,
    FooterComponent
  ],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {}

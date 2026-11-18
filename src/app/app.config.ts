
import { ApplicationConfig, LOCALE_ID } from '@angular/core';

import {
  registerLocaleData
} from '@angular/common';

import localeEs from '@angular/common/locales/es';

import {
  provideRouter,
  withInMemoryScrolling
} from '@angular/router';

import { provideHttpClient } from '@angular/common/http';

import { routes } from './app.routes';

// Registramos los datos del idioma español.
registerLocaleData(localeEs);

export const appConfig: ApplicationConfig = {
  providers: [
    provideRouter(
      routes,
      withInMemoryScrolling({
        anchorScrolling: 'enabled',
        scrollPositionRestoration: 'enabled'
      })
    ),

    provideHttpClient(),

    // Idioma predeterminado de Angular.
    {
      provide: LOCALE_ID,
      useValue: 'es'
    }
  ]
};

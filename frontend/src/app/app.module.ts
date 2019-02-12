import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ToastrModule } from 'ngx-toastr';
import { QuotationsService } from 'src/services/quotations.service';
import { QuotationsComponent } from './components/quotations/quotations.component';
import { ChartsModule } from 'ng2-charts';
import { DatePipe } from '@angular/common';

@NgModule({
  declarations: [
    AppComponent,
    QuotationsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    BrowserAnimationsModule, // required animations module
    ToastrModule.forRoot(), // ToastrModule added
    ChartsModule
  ],
  providers: [QuotationsService, DatePipe],
  bootstrap: [AppComponent]
})
export class AppModule { }

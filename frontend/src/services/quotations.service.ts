import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable } from "rxjs";
import {
    FormGroup,
    FormBuilder,
    FormControl,
    Validators
} from "@angular/forms";
import { environment } from "../environments/environment";
import urljoin from "url-join";
import { Quotation } from 'src/models/quotations.model';

@Injectable()
export class QuotationsService {
    /**
     *
     */

    endPoint: string;

    constructor(protected http: HttpClient) {
        this.endPoint = urljoin(environment.apiUrl, "quotations/");
    }

    getQuotations(): Observable<Quotation[]> {
        return this.http.get<Quotation[]>(this.endPoint)
    }

}

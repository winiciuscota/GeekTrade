import { Component, OnInit } from "@angular/core";
import { QuotationsService } from "../../../services/quotations.service";
import { ToastrService } from "ngx-toastr";
import { Quotation } from 'src/models/quotations.model';

@Component({
    selector: "app-quotations",
    templateUrl: "./quotations.component.html",
    styleUrls: ["./quotations.component.scss"]
})
export class QuotationsComponent implements OnInit {

    quotations: Quotation[];

    constructor(private QuotationsService: QuotationsService) {

    }


    ngOnInit() {
        this.QuotationsService.getQuotations().subscribe(res => this.quotations = res);
    }

}
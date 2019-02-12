import { Component, OnInit } from "@angular/core";
import { QuotationsService } from "../../../services/quotations.service";
import { ToastrService } from "ngx-toastr";
import { Quotation } from 'src/models/quotations.model';
import { DatePipe } from '@angular/common';

@Component({
    selector: "app-quotations",
    templateUrl: "./quotations.component.html",
    styleUrls: ["./quotations.component.scss"]
})
export class QuotationsComponent implements OnInit {

    quotations: Quotation[];
    organizedQuotations: Quotation[][];
    currencies: string[] = ["EUR", "BTC", "USD"];

    constructor(private QuotationsService: QuotationsService, private datePipe: DatePipe) {

    }


    getOrganizedQuotations(): Quotation[][] {
        let organizedQuotations = []
        this.currencies.forEach(cur => {
            let quotations = this.getCurrency(cur);
            organizedQuotations.push(quotations);
        });

        return organizedQuotations;
    }

    private getCurrency(currency: string): Quotation[] {
        return this.quotations.filter(x => x.currency == currency);
    }

    getChartData(currency: string): any {
        let quotations = this.getCurrency(currency);
        let sell = quotations.map(x => x.sell);
        let buy = quotations.map(x => x.buy);
        let variations = quotations.map(x => x.variation);

        return [
            { data: sell, label: 'Sell' },
            { data: buy, label: 'Buy' },
            { data: variations, label: 'Variation' }
        ];
    }

    getLabels(currency: string): string[] {
        let quotations = this.getCurrency(currency);
        let labels = quotations.map(x => this.datePipe.transform(x.created_on, 'dd/MM hh:mm'));

        return labels;
    }

    getVariation(currency: string, days: number): number {
        let d = new Date();
        d.setDate(d.getDate() - days);

        let quotations = this.getCurrency(currency);
        let average = arr => arr.reduce((p, c) => p + +c, 0) / arr.length;

        let result = average(quotations.map(x => x.variation)); // 5

        return result;
    }


    ngOnInit() {
        this.QuotationsService.getQuotations().subscribe(res => {
            this.quotations = res;
            this.organizedQuotations = this.getOrganizedQuotations();
        });
    }



}
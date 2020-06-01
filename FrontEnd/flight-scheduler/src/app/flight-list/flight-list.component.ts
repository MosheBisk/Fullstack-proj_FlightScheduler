import { Component, OnInit } from '@angular/core';
import { Observable } from "rxjs";
import { Flight } from "../models/flight";
import { FlightService } from "../services/flight.service";

@Component({
  selector: 'app-flight-list',
  templateUrl: './flight-list.component.html',
  styleUrls: ['./flight-list.component.css']
})
export class FlightListComponent implements OnInit {

  flights$: Observable<Flight[]>;
  success: boolean = false;

  constructor(private flightService: FlightService) { }

  ngOnInit(): void {
    this.loadFlightsData();
  }

  loadFlightsData(){
    this.flights$ = this.flightService.getAllFlights();
    console.log("loadFlightsData this.flights$ - ", this.flights$);
    
  }

  deleteFlight(flight_id: number){
    this.flightService.deleteFlight(flight_id)
      .subscribe(
        data =>{
          this.success = true;
          this.loadFlightsData();
        },
        error => console.log("Failed to delete flight: " + error)       
      );
  }

  deleteAllFlights(){
    this.flightService.deleteAllFlighits()
      .subscribe(
        data =>{
          this.success = true;
          this.loadFlightsData();
        },
        error => console.log("Faild to delete all: " + error)        
      );
  }

}

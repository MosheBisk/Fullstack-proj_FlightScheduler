import { Component, OnInit } from '@angular/core';
import { Observable, BehaviorSubject } from 'rxjs';
import { Flight } from "../models/flight";
import { FlightService } from "../services/flight.service";
import { ActivatedRoute, Router } from "@angular/router";

@Component({
  selector: 'app-flight-edit',
  templateUrl: './flight-edit.component.html',
  styleUrls: ['./flight-edit.component.css']
})
export class FlightEditComponent implements OnInit {

  // flight = new BehaviorSubject<Flight | null>(null);
  // flight: Observable<Flight>;
  flight: Flight;
  flight_id: number;
  success: boolean = false;
  trip_types = ["One Way", "Round Trip", "Multiple Destinations"];

  constructor(private flightService: FlightService,
              private activatedRoute: ActivatedRoute,
              private router: Router) { }

  ngOnInit(){
    this.activatedRoute.paramMap.subscribe(
      params => {
        this.flight_id = Number(params.get("id"));        
      }
    );
    this.loadFlightData();
  }

  onSubmit(){
    this.updateFlight();
    if (this.success) {
      setTimeout(() => {
      this.onCancel()
    }, 2000);
    } else {
      this.onCancel()
    }
  }

  loadFlightData(){
    console.log("loadFlightData this.flight - ", this.flight);
    
    this.flightService.getFlight(this.flight_id)
    .subscribe(
      flight_data => {
        console.log("loadFlightData flight_data - ", flight_data);        
        this.flight = flight_data;
        // this.flight.next(flight_data);
        console.log("loadFlightData subscribe this.flight - ", this.flight);
      }
    );
    console.log("loadFlightData this.flight 2 - ", this.flight);
  }
  
  updateFlight() {
    this.flightService.updateFlight(this.flight_id, this.flight)
    .subscribe(
      data => {
        // this.flight = data as BehaviorSubject<Flight>; //as Observable<Flight>;
        this.success = true;
        console.log("updateFlight subscribe this.flight - ", this.flight);
      },
      error => console.log("Oops. Cannot update! " + error)      
    );
  }

  onCancel(){
    this.router.navigate(['']);
  }

}

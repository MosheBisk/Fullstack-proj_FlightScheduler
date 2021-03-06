import { Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import { Observable, BehaviorSubject } from "rxjs";
import { Flight } from "../models/flight";

@Injectable({
  providedIn: 'root'
})
export class FlightService {

  private endpoint = 'http://127.0.0.1:8010/flights/';

  constructor(private http: HttpClient) { }

  // GET - A SINGEL Flight
  getFlight(id: number): Observable<any>{
    return this.http.get(this.endpoint + id);
  }

  // GET ALL Flights
  getAllFlights(): Observable<any>{
    return this.http.get(this.endpoint)
  }

  // POST - Add a new flight
  flightCreate(flight: Flight): Observable<object>{
    return this.http.post(this.endpoint, flight)
  }

  // PUT - Update
  updateFlight(id: number, payload: any): Observable<object>{
    return this.http.put(this.endpoint + id, payload);
  }

  // DELETE - A Flight
  deleteFlight(id: number): Observable<any>{
    return this.http.delete(this.endpoint + id);
  }

  // DELETE - ALL Flights
  deleteAllFlighits(): Observable<any>{
    return this.http.delete(this.endpoint);
  }
}

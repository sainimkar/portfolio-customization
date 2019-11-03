import { ReactiveFormsModule } from '@angular/forms';
import { Component, OnInit } from '@angular/core';
import { CosmicServiceService } from './../../services/cosmic-service.service';
import { FormsModule, FormBuilder, FormGroup, FormControl, Validators} from '@angular/forms';
import { User } from 'src/app/user';
import {Router} from "@angular/router";


@Component({
  selector: 'app-services',
  templateUrl: './services.component.html',
  styleUrls: ['./services.component.css']
})
export class ServicesComponent implements OnInit {

  // tslint:disable-next-line: typedef-whitespace
  // tslint:disable-next-line: variable-name
  constructor(private _service: CosmicServiceService, private router: Router){}


  userModel = new User( 20 , 1,  15000, 5000, 5000);

  onSubmit() {
    console.log(this.userModel);

    this._service.clientData(this.userModel)
          .subscribe(
            data => console.log('success', data),
            error => console.error('Error!', error )
        );

        this.router.navigate(['/portfolio']);
  }

  ngOnInit(){}
}



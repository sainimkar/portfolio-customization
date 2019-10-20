import { ReactiveFormsModule } from '@angular/forms';
import { Component, OnInit } from '@angular/core';
import { CosmicServiceService } from './../../services/cosmic-service.service';
import { FormsModule, FormBuilder, FormGroup, FormControl, Validators} from '@angular/forms';
import { User } from 'src/app/user';

@Component({
  selector: 'app-services',
  templateUrl: './services.component.html',
  styleUrls: ['./services.component.css']
})
export class ServicesComponent implements OnInit {

  terms = ['short', 'intermediate', 'long'];
  risk = ['low', 'moderate', 'high'];
  savings = ['0-10%', '10-20%', '20-30%', 'More than 30%'];
  userModel = new User('Sai', 19, 15000, 'short', 'More than 30%', 'high', true);

  ngOnInit() {}

}

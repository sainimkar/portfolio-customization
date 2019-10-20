import { Injectable } from '@angular/core';
import { config } from './../../config/config';
import { HttpClient } from '@angular/common/http';
import { User } from '../user';


@Injectable({
  providedIn: 'root'
})

export class CosmicServiceService {

  _url = '';

  constructor(private _http: HttpClient) { }

  clientData(user: User)
  {
    return this._http.post<any>(this._url, user);
  }

  // getting data for home component
  getHomeData()
  {
    return this._http.get(config.url + config.bucket_slug + "/object-type/homes", {
      params: {
        read_key: config.read_key,
      }
    })
  }

  // get data of services
  getServices()
  {
    return this._http.get(config.url + config.bucket_slug + "/object-type/services", {
      params: {
        read_key: config.read_key,
      }
    })
  }

  //about us data
  getAboutUsData()
  {
    return this._http.get(config.url + config.bucket_slug + "/object-type/abouts", {
      params: {
        read_key: config.read_key,
      }
    })
  }

  // send message
  sendMessage(data: any)
  {
    return this._http.post(config.url + config.bucket_slug + "/add-object/",{
      title: data.email, content: data.message, slug: data.name, type_slug: 'clients', write_key: config.write_key,

      metafields: [
        {
          key: "name",
          type: "text",
          value: data.name
        },
        {
          key: "email",
          type: "text",
          value: data.email
        }
      ]

    })
  }


}

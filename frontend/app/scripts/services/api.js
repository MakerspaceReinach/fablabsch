/*
    FabLabs-CH a community web site for swiss fablabs
    Copyright (C) 2016  Boris Fritscher

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/
'use strict';

/**
 * @ngdoc service
 * @name frontendApp.api
 * @description
 * # api
 * Service in the frontendApp.
 */
angular.module('frontendApp')
  .service('api', function ($http, $q, API_ENDPOINT) {
      var api = this;
      var ready = $q.defer();
      api.ready = ready.promise;

      $http.get(API_ENDPOINT + 'api/spaces')
      .then(function(result){
          api.spaces = result.data;
          ready.resolve();
      });

      api.getSpacePromiseBySlug = function(slug){
          var d = $q.defer();
          api.ready.then(function(){
              for(var i=0;  i < api.spaces.length; i++){
                  if(api.spaces[i].slug === slug){
                      d.resolve(api.spaces[i]);
                      return;
                  }
              }
              d.reject('NOT_FOUND');
          });
          return d.promise;
      };

  });

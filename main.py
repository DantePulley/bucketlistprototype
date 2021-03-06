#This is a comment

#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#



import webapp2
import jinja2


env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):
    
    def get(self):
        main_template = env.get_template('bucketlistproto.html')
        self.response.out.write(main_template.render())
    def post(self): ## here's the new POST method in the MainHandler
        results_template = env.get_template('newr.html')
        
        # the variables that are sent to results.html are user_answer_1 and user_answer_2
        # they contain the input values from the main.html form with names answer1 and answer2
        template_variables = {
            'noun1':self.request.get("noun1"),
            'password':self.request.get("password"),
            'email':self.request.get("email"),
           
            }
        self.response.out.write(results_template.render(template_variables))
        

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

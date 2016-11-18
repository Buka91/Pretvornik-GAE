# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), "templates") # "templates" je pot do .html datoteke
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)
unitDict = {"Mikrometer": {"Mikrometer": 1,
                           "Milimeter": 0.001,
                           "Centimeter": 0.0001,
                           "Decimeter": 0.00001,
                           "Meter": 0.000001,
                           "Kilometer": 0.000000001,
                           "Palec": 1.0 / 25400,
                           "Cevelj": 1.0 / 304800,
                           "Jard": 1.0 / 914400,
                           "Milja": 1.0 / 1609344000,
                           "Navticna milja": 1.0 / 1852000000},
            "Milimeter": {"Mikrometer": 1000,
                          "Milimeter": 1,
                          "Centimeter": 0.1,
                          "Decimeter": 0.01,
                          "Meter": 0.001,
                          "Kilometer": 0.000001,
                          "Palec": 1.0 / 25.4,
                          "Cevelj": 1.0 / 304.8,
                          "Jard": 1.0 / 914.4,
                          "Milja": 1.0 / 1609344,
                          "Navticna milja": 1.0 / 1852000},
            "Centimeter": {"Mikrometer": 10000,
                           "Milimeter": 10,
                           "Centimeter": 1,
                           "Decimeter": 0.1,
                           "Meter": 0.01,
                           "Kilometer": 0.00001,
                           "Palec": 1.0 / 2.54,
                           "Cevelj": 1.0 / 30.48,
                           "Jard": 1.0 / 91.44,
                           "Milja": 1.0 / 160934.4,
                           "Navticna milja": 1.0 / 185200},
            "Decimeter": {"Mikrometer": 100000,
                          "Milimeter": 100,
                          "Centimeter": 10,
                          "Decimeter": 1,
                          "Meter": 0.1,
                          "Kilometer": 0.0001,
                          "Palec": 1.0 / 0.254,
                          "Cevelj": 1.0 / 3.048,
                          "Jard": 1.0 / 9.144,
                          "Milja": 1.0 / 16093.44,
                          "Navticna milja": 1.0 / 18520},
            "Meter": {"Mikrometer": 1000000,
                      "Milimeter": 1000,
                      "Centimeter": 100,
                      "Decimeter": 10,
                      "Meter": 1,
                      "Kilometer": 0.001,
                      "Palec": 1.0 / 0.0254,
                      "Cevelj": 1.0 / 0.3048,
                      "Jard": 1.0 / 0.9144,
                      "Milja": 1.0 / 1609.344,
                      "Navticna milja": 1.0 / 1852},
            "Kilometer": {"Mikrometer": 1000000000,
                          "Milimeter": 1000000,
                          "Centimeter": 100000,
                          "Decimeter": 10000,
                          "Meter": 1000,
                          "Kilometer": 1,
                          "Palec": 1.0 / 0.0000254,
                          "Cevelj": 1.0 / 0.0003048,
                          "Jard": 1.0 / 0.0009144,
                          "Milja": 1.0 / 1.609344,
                          "Navticna milja": 1.0 / 1.852},
            "Palec": {"Mikrometer": 25400,
                      "Milimeter": 25.4,
                      "Centimeter": 2.54,
                      "Decimeter": 0.254,
                      "Meter": 0.0254,
                      "Kilometer": 0.0000254,
                      "Palec": 1,
                      "Cevelj": 1.0 / 12,
                      "Jard": 1.0 / 36,
                      "Milja": 1.0 / 63360,
                      "Navticna milja": 1.0 / 72913.386},
            "Cevelj": {"Mikrometer": 304800,
                       "Milimeter": 304.8,
                       "Centimeter": 30.48,
                       "Decimeter": 3.048,
                       "Meter": 0.3048,
                       "Kilometer": 0.0003048,
                       "Palec": 12,
                       "Cevelj": 1,
                       "Jard": 1.0 / 3,
                       "Milja": 1.0 / 5280,
                       "Navticna milja": 1.0 / 6076.1155},
            "Jard": {"Mikrometer": 914400,
                     "Milimeter": 914.4,
                     "Centimeter": 91.44,
                     "Decimeter": 9.144,
                     "Meter": 0.9144,
                     "Kilometer": 0.0009144,
                     "Palec": 1.0 / 36,
                     "Cevelj": 1.0 / 3,
                     "Jard": 1,
                     "Milja": 1.0 / 1760,
                     "Navticna milja": 12.0 / 24304.462},
            "Milja": {"Mikrometer": 1609344000,
                      "Milimeter": 1609344,
                      "Centimeter": 160934.4,
                      "Decimeter": 16093.44,
                      "Meter": 1609.344,
                      "Kilometer": 1.609344,
                      "Palec": 63360,
                      "Cevelj": 5280,
                      "Jard": 1760,
                      "Milja": 1,
                      "Navticna milja": 1609.344 / 1852},
            "Navticna milja": {"Mikrometer": 1852000000,
                               "Milimeter": 1852000,
                               "Centimeter": 185200,
                               "Decimeter": 18520,
                               "Meter": 1852,
                               "Kilometer": 1.852,
                               "Palec": 72913.386,
                               "Cevelj": 6076.1155,
                               "Jard": 24304.462 / 12,
                               "Milja": 1852 / 1609.344,
                               "Navticna milja": 1}
            }

class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("index.html")

    def post(self):
        first = self.request.get("from_unit")
        second = self.request.get("to_unit")
        third = self.request.get("from")
        params = {"result": first,
                  "result2": second,
                  "result3": third}
        try:
            number_from = float(third)
            number_to = number_from * unitDict[first][second]
            params["result4"] = number_to
            return self.render_template("index.html", params = params)
        except:
            return self.render_template("index.html", params = params)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler) # webapp2.Route(pot, handler) -> pot = neki.com/blog -> vpisemo /blog
], debug=True) # vsaka podstran ima svoj handler, ali pa z if stavki dolocimo vse v enem MainHandler-ju

ckanext-fgp
===========

CKAN Extension for the Canadian Federal Geospatial Project

This extension requires the Reusable, Accessible, Mapping Platform (RAMP). 
For more information on RAMP, see  http://ramp-pcar.github.io/.

Customizing RAMP
----------------

Some minor changes are required to the RAMP distribution to make it work with CKAN. The main 
reason for this is that RAMP uses separate English and French HTML files, while the Open Canada site
uses a language code in the URL to determine the language of the displayed page.

1. RAMP-starter.js: Change pathname = location.pathname.replace(/\/[^/]+$/, "") + "/", to pathname="http://localhost:5000/
2. config.en.json and config.fr.json: Change any URL to use the full path used by Open Canada. A relative path won't work here.
3. bootstrapper.js: 
  1. Add resGetPath:'/locales/__lng__/translation.json' to the i18n.init() parameter array
  2. Change configFile = (lang === "fr") ? "config.fr.json" : "config.en.json"; to 
  configFile = (lang === "fr") ? "http://localhost:5000/config.fr.json" : "http://localhost:5000/config.en.json";

 
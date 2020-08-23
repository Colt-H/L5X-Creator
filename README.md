#L5X Creator 

Program for generating L5x files for Allen Bradley PLCs. 

This tool will create an L5x file to be imported into a blank project. Create the basics of the project without dealing with AB's slow interface. Generate your IO tree, configure the controller, and more. Future features include settings file to automatically populate from.

Stuff needed to do:
 - finish IO tree building feature
 - finish tag adding feature
 - finish program adding feature
 - finish task adding feature
 - implement elementtree module for generating XML code
 - figure out file reading/writing
 - proper date/time for creation date in file

Working so far:
 - Generates a blank L5X file from hardcoded XML data that's able to be imported to ACD file

Stuff I want to do:
 - 
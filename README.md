# L5X Creator

Program for generating L5x files for Allen Bradley PLCs.

This tool will create an L5x file to be imported into a blank project. Create the basics of the project without dealing with AB's slow interface. Generate your IO tree, configure the controller, and more. Future features include settings file to automatically populate from.

## Stuff that needs done

- finish IO tree building feature
- finish tag adding feature
- finish program adding feature
  - for now, will add blank "Main Routine" to each program
  - add functionality to rename sub routines later and change prog types
- finish task adding feature
- figure out file reading/writing
- proper date/time for creation date in file
- input validation
  - firmware revisions
  - product types
- some kind of testing
- database of product codes
  - Remove hardcode product codes and vendor IDs once database is up
- testing for CommMethod and config IDs
- program scoped tags??

### Working so far

- Generates a blank L5X file from hardcoded XML data that's able to be imported to ACD file

### Stuff I want to do

- have prepopulated setting files for export/import to quickly create similar projects
- a GUI?
- import tag list from csv
- import other L5X files as programs/routines

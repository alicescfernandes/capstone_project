# Dev Log

Newer entries are inserted on the TODO section, and then moved into the day that they were done

## Maybe TODO

_Stuff that is not important and just nice haves_

- [ ] Use Yarn instead of NPM
- [ ] Use Axios instead of fetch
- [ ] Adds preload tags for faster loading of scripts
- [ ] Check if the flowbite JS file can be imported from node_modules
- [ ] Django DRF Caching (either Redis or Memcached)
- [ ] Create a "change password page", check if django is able to send emails
- [ ] Display username on the navbar
- [ ] Add proper logging for the python app
- [ ] Consider remove infinite scrolling in favour of actual sections that can show a localized set of charts
- [ ] Add alert when there is still Excel files in processing

## TODO

## 05/11/2025

- [x] Adds more VPS configs for deploy
- [x] Adds Django Unfold

## 05/10/2025

- [x] Fixes user on the quarter selection causing errors for multiple users
- [x] Adds fixed sideabar toc and sections show only on mobile
- [x] Hide Sections when using mobile (ignored)
- [x] Closes the chart zoom modal when the user clicks ESC

## 04/27/2025

- [x] Adds more charts - cashflow
- [x] Fixes quarter navigation when no options are given

## 04/26/2025

- [x] Adds more charts - ad judgement, demand distrib by channel and others
- [x] Loading from an # breaks the charts (<http://localhost:8000/#section-balanced-scorecard>)
- [x] Change the modals to upload files instead of the quarters

## 04/25/2025

- [x] Adds more charts - not sure what it was

## 04/20/2025

- [x] Adds more charts - not sure what it was

## 04/19/2025

- [x] Adds balance sheet (waterfall) charts
- [x] Adds other phase2 charts
- [x] Add a zoom feature on the charts, that would open a popup with the chart that was zoomed in

## 04/18/2025

- [x] Add a user reference to all models
- [x] Read current user and grab the instances that current user created
- [x] Create login page and add the username to the navbar
- [x] Create the logout page
- [x] Create the registration page
- [x] Cleans up even more tailwind classes
- [x] Extract JS from the apps

## 04/17/2025

- [x] Add empty state message when no files are returned
- [x] Remove dark mode from mobile menu
- [x] Fix styling bugs (modal overlay and input) on the new quarter modal
- [x] Cleans up more tailwind classes
- [x] Check mime type of file, to avoid fake xlsx uploads
- [x] When deleting an excel, update the active CSV's to a previous version
- [x] Consider using ~Mongo~ PostgresSQL to store the CSV files (write a POC that replaces the files with ~MongoDB~ PostgresSQL)

## 04/16/2025

- [x] Adds Report code to the repo. Allows me to version control the repo
- [x] Adds build system for report
- [x] Setup github workflows to compile the report on every commit to master
- [x] Fork the branch for the FEIM presentation and freeze it
- [x] Setup Postgres (Only during using auth) (deployment-setup branch)
- [x] Setup docker compose yml for dev
- [x] Skeleton docker-compose yml for prod

## 04/13/2025

- [x] Add Sections - Extract the names from the XSLX file. This will require some template changes. Make sure that the sections are tagged by ID so users can link then (or bookmark them)
- [x] Move sections into navbar

## 04/12/2025

- [x] Add lazy load with intersection observer to the web component
- [x] Ensure that all phase 1 charts are supported, without any bugs or errors
- [x] Loads all files from unpkg CDN.
- [x] Extract remaining tailwind classes into the CSS file
- [x] Add proper collectstatic to the app

## 04/11/2025

- [x] Add sheet parsing to the endpoint
- [x] Make sure that the endpoints and the duplicated file logic still works
- [x] Disable edit excel on the admin, only removals and creations - This was fixed
- [x] Remove "Quarters" from the sheet names
- [x] Remove "Total" lines
- [x] Fix the slug on the admin. this needs to match the chart classification type
- [x] File deletion was disabled
- [x] Make the API return Plotly traces, and use those traces
- [x] File deletion was disabled
- [x] Read chart config from the chart classification type, and return that chart type
- [x] Add support on the backend and frontend to allow for multiple filters (check the dimensions)
- [x] Show legends on the charts even when its a single trace
- [x] Only allow for excel files uploads
- [x] When no data is able to be show, an empty state message
- [X] When a graph has an error, don't render the chart but the error message

### Data filtering problems

The initial approach was to apply "templates" to the data, where each CSV would follow a very strict algorithm that would determine the available options to filter data by, and the X and Y's of the data. Upon further inspection, that logic seems flawed as it will produce graphs that won't be useful to the end user.

Example: on the Competitors Prices - NORAM.csv file, we have two main "filter" columns, Brand and Company, and 3 numeric columns, Price, Rebate, Priority.
If we apply the following filter Brand==Elevatech 3.0 AND Company== CTTG, then we only get a single line of information:
Elevatech 3.0 3,400 0 1

But if we only apply the following filter Company== CTTG, then we get multiple lines of information
Elevatech 3.0 3,400 0 1
Express 3.0   3,000 200 2
TurboLiteV2     1,850 100 3

The second data is more useful than the first, since it immediatly displays all products of the CTTG brand. The same thought process can be applied to all "double" charts, where we should really only filter by a single column information.

The second issue is that i need 2D data, meaning on X and one Y. If i have multiple axises then i cannot represent that data on a 2D scale

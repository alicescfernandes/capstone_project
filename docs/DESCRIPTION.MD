## Description
The project is an website that can display graphs. The graphs are based on data submitted by the users, that are XLSX files extracted from another platform. The purpose of the the app is to allow users to see and manipulate that data. The platform should also provide advanced filtering capabilities that are not possible on the platform that the data is exported from.

### Problem Statement
In ISCAL, the students use a business simulator (Marketplace Simulations - International Corporate Management) for a class on the last semester of the year. That simulator allows the student to apply the lessons learned during previous semesters. The purpose of the simulator is to allow students to group, and play against other groups of the same class. During that simulation, the students have to make bussiness decisions to improve, and whem making those decisions, the students need to crunch the data from platform to understand the market where the product is sold. 

However, when making those decisions, the students need to skip between a lot of sections, manually write on a notebook or export to Excell to visualize it since most of the sections don't have graphs, and just show tables with information. This project attempts to cover that gab by allowing users to upload the data exported from the platform, and allow for better UX and advanced filtering of the data.

### Users
- Each user has a single account on the platform
- We assume that users of the same group will duplicate files, but this structure keeps the project simple without adding custom capabilities to the user 
- Each user can upload XLSX files, and those files will be processed and able to be removed
- The upload will be split by quarters, where the user has to create a quarter on the platform and then upload files to that quarter. The quarters are identified by string "Quarter" and a number, like "Quarter 2" (for the identifier, it will be identified as "Q{N}" being N the quarter number given by the quarter ).
- User authentication will be done using Django's default authentication scheme (https://docs.djangoproject.com/en/5.1/topics/auth/default/)
- [Nice to Have] Users can be deactivated automatically or manually after a semester
- User Model:
  - Username
  - Email
  - Password
  - folder_uuid (randomly generated)

### Quarters
- Each user will be able to create a quarter, and assign it a number. Only one quarter can have that number.
- Each quarter will be unique to the user, Quarters from User A are different than Quarters from User B
- Quarters work like "buckets" for XLSX files, where the user uploads files to that bucket.
- The app will always show the latest quarter on the backend, and on the frontend the user will be able to move from quarter to quarter. 
- When a quarter is created, a folder in the media/uploads/ directory will be created. The name of that folder will be a randomly generated UUID. This avoids guess attacks, eg `media/uploads/<quarterUUID>`


### Charts
- The graph can display data from that section, but for multiple graphs.
- Graphs can also have advanced filtering to allow for a more granular search
- Graphs are fixed, and cannot be changed
- Only charts with corresponding csv's will be shown. The backend will will create the markup to support those graphs (it will not render them on the backend)
- Charts will be rendered on the frontend with the data being parsed by the backend.
- It will use the endpoint: `/api/charts/<str:chart_id>/<str:quarter>/` (eg `/api/charts/segments-by-need/1/`)
- Each chart_id will then have its own parsing of a XLSX file, and this will make sure that the graphs are controlled and intentional.
The endpoint will be in charge of crunching the data, and return a JSON strucuture that can allow the user to manipulate the graph as they see fit. 
- The data of the graph will change when the user changes the quarter on the home page.


### Files
This section describes the files that being uploaded , and what we have to do to said files
- The uploaded files will be of type XLSX (Excell)
- Only XLSX files will be allowed, any other type will be discarded (on the frontend, via allowed extensions)

The XLXS files are strucutured in the following way.  
- The filename of the XLSX file comes identified with the section and quarter that it belongs to (CostumerNeeds-Q2.xlsx)
- Each XLSX can have one or multiple sheets
- The first line is a header of each sheet is the name of the graph
- The first column will always be the subject of the data, eg: if a dataset is about patterns, the first column will be said patterns. This column is the "X axis" of the graphs

- Upon upload of this files, they will be converted into CSV and stored under a specific naming structure that will provide the metadata. This will ensure normalization of the uploaded files, and that are known under predictable names.
- Only one file of the same section can be present, if a user uploads a new file with the same "origin" name, it will overwrite the processed file. 
- The platform will only support specific files, the ones that were bucketed and deemed useful for the user analysis
- The files shall be uploaded to specific directories, pertaining to the user that is uploading them. The Quarter UUID
```
/uploads/
  └── <quarterUUID>/
        ├── balanced_scorecard_q1.csv
        └── balance_sheet_q1.csv
```
- T`he files shall be named by the name of their sheets, and each sheet will create a new CSV

## Pages
- "Create Account" - Allows the users to create account
- "Login" - Allows the user to login
- "Upload" - Allows the user to create quarters and upload files to those. Users can also delete files and quarters from this page.

- [Nice To Have] "Recover Password" - Allows the users to recover the account password
- [Nice To Have] "Settings" - Allows to change password, upload and remove files and create quarters to upload those files


## Stack
- Django for the "full-stack"
- Flowbite as the design system, integrated witihin django
- Pandas to analyse and transform the data into a more workable set
- Plotly as the charting library

## Roadmap
To allow for a phased development, we will split the work into milestoens

1. Create the app without any access control, where the app reads from XLSX files locally
2. We can then work on creating the upload functionality, and display the graphs based on the data uploaded
3. Using Django's Authentication System, we will then create access control for users, and allow for uploads per user
4. Only allow logged in users, and use the files uploaded by each user 
 
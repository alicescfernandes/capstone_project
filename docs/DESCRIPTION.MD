## Description
The project is an website that can display graphs. The graphs are based on data submitted by the users, that are XLSX files extracted from another platform. The purpose of the the app is to allow users to see and manipulate that data. The platform should also provide advanced filtering capabilities that are not possible on the platform that the data is exported from.

### Problem Statement
In ISCAL, the students use a business simulator (Marketplace Simulations - International Corporate Management) for a class on the last semester of the year. That simulator allows the student to apply the lessons learned during previous semesters. The purpose of the simulator is to allow students to group, and play against other groups of the same class. During that simulation, the students have to make bussiness decisions to improve, and whem making those decisions, the students need to crunch the data from platform to understand the market where the product is sold. 

However, when making those decisions, the students need to skip between a lot of sections, manually write on a notebook or export to Excell to visualize it since most of the sections don't have graphs, and just show tables with information. This project attempts to cover that gab by allowing groups to upload the data exported from the platform, and allow for better UX and advanced filtering of the data.

### Users
- Users are split in groups of users
- Each group has a single account on the platform
- Each group can upload XLSX files.
- Each group can also delete XLSX files.
- The upload will be split by quarters, where the group has to create a quarter on the platform and then upload files to that quarter. The quarters are identified by string "Quarter" and a number, like "Quarter 2" (for the identifier, it will be identified as "Q{N}" being N the quarter number given by the quarter ).
- User authentication will be done using Django's default authentication scheme (https://docs.djangoproject.com/en/5.1/topics/auth/default/)

### Charts
- The graph can display data from that section, but for multiple graphs.
- Graphs can also have advanced filtering to allow for a more granular search
- Graphs are fixed, and cannot be changed


## XLSX
The XLXS files are strucutured in the following way.  
- Each XLSX file comes identified with the section and quarter that it belongs to (CostumerNeeds-Q2.xlsx)
- The first line is a header, the name of the graph
- The first column will always be the subject of the data, eg: if a dataset is about patterns, the first column will be said patterns. This column is the "X axis" of the graphs


## Pages
"Create Account / Login" - Allows the groups to create account
"Recover Password" - Allows the groups to recover the account password
"Homepage / Index" - Displays the data in charts. The sole purpose is to display those charts
"Settings" - Allows to change password, upload and remove files and create quarters to upload those files


## Stack
- Django for the "full-stack"
- Flowbite as the design system, integrated witihin django
- Pandas to analyse and transform the data into a more workable set
- Plotly as the charting library



## Roadmap
To allow for a phased development, we will split the work into milestoens

1. Create the app without any access control, where the app reads from XLSX files locally
2. We can then work on creating the upload functionality, and display the graphs based on the data uploaded
3. Using Django's Authentication System, we will then create access control for groups, and allow for uploads per group
 


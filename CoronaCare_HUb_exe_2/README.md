# Project README

## Overview

This project is designed to handle employee data and Covid details. It consists of multiple layers, including the DAL (Data Access Layer), BL (Business Logic Layer), and MyService layer.


## MyService Layer
The MyService layer serves as the API layer for interacting with the application. It contains controllers that handle incoming HTTP requests and delegate processing to the BL layer. Controllers return appropriate HTTP responses with data or error messages.

### Files:
- **CovidDtailesController.cs**: Controller for handling Covid detail-related endpoints.
- **EmployeeController.cs**: Controller for handling employee-related endpoints.


## BL (Business Logic Layer)
The BL layer contains the business logic of the application. It orchestrates data manipulation and validation, calling appropriate methods from the DAL layer. It also contains mapping logic using AutoMapper for mapping between DTOs (Data Transfer Objects) and entities.

### Files:
- **CovidDetailesBl.cs**: Implements the `ICovidDatailesBl` interface for Covid detail-related business logic.
- **EmployeeBl.cs**: Implements the `IEmployeeBl` interface for employee-related business logic.


## DAL (Data Access Layer)
The DAL is responsible for interacting with the database and performing CRUD operations. It contains implementations for various data access interfaces, such as `IEmployeeDal`, `ICovidDetailDal`, etc. Each DAL implementation interacts with the database context (`DB_Context`) using Entity Framework Core.

### Files:
- **CityServiceDal.cs**: Implements the `ICityDal` interface for city-related operations.
- **CovidDetailServiceDal.cs**: Implements the `ICovidDetailDal` interface for Covid detail-related operations.
- **EmployeeServiceDal.cs**: Implements the `IEmployeeDal` interface for employee-related operations.
- **VaccineManufacturerServiceDal.cs**: Implements the `IVaccineManufacturerDal` interface for vaccine manufacturer-related operations.
- **StreetServiceDal.cs**: Implements the `IStreetDal` interface for street-related operations.
- **AddressServiceDal.cs**: Implements the `IAddressDal` interface for address-related operations.


## How to Run the Project
first- open the 'corona_Hub_exe.sln' file at the 'corona_Hub_Exe' dir:
![image-10](https://github.com/TovaGolimstok/HADASIM4_EXE/assets/164151470/6346431c-d6b3-4fc0-a4d3-b8569f141e73)
![image-11](https://github.com/TovaGolimstok/HADASIM4_EXE/assets/164151470/ae0bca3f-d4fb-4e66-9eff-7d7d5dcc8e7b)
in the browse choose the db file from your local computer.
1.connect to the db file in the data connection in the server explorer tool.

2. Set up the database connection string:
      -go to file:'ServiceCollectionExtensions.cs'
      -at line :            string connString = "...here" replace the connString to your connection string of your db connection.
      - go to file:'DB_Context.cs' in models dir in dal layer 
      -at func: 'public OnConfiguring' 
      -change th connstring:at optionsBuilder.UseSqlServer(...here)

3. Run the database migrations to create the database schema.

4. Start the application and make HTTP requests to the defined endpoints.
when you run up the project there will be a swgger up with a locallhost 5073(http://localhost:5073/swagger/index.html):
![image](https://github.com/TovaGolimstok/HADASIM4_EXE/assets/164151470/49581360-7529-4d50-9053-9eed77e51d9e)
and then you can choose to create an employee or just to create employee_covid_detailes to a specific Numberid_employee.
1. create amployee:
![image-1](https://github.com/TovaGolimstok/HADASIM4_EXE/assets/164151470/622f76b6-1547-4071-a8f7-ff78d2adb0b8)
![image-2](https://github.com/TovaGolimstok/HADASIM4_EXE/assets/164151470/4aeea88a-01ca-4e5a-9540-87f5c9be92ce)
and then enter the 'try it out' button:![image-3](https://github.com/TovaGolimstok/HADASIM4_EXE/assets/164151470/937618fc-c29b-4c36-80e3-80cfc03d1d84)

and then enter all the parameters:
![image-4](https://github.com/TovaGolimstok/HADASIM4_EXE/assets/164151470/02e24a05-2d37-4100-985c-509f07a64b0a)
and then run the execute button:![image-5](https://github.com/TovaGolimstok/HADASIM4_EXE/assets/164151470/3755f248-9ac6-4d09-8750-b1b9c245503f)

and there will be a 200 status code of succes:![image-6](https://github.com/TovaGolimstok/HADASIM4_EXE/assets/164151470/aff13114-fea7-4be3-8228-f4bbbf3777f3)


2. gat by id_employee or by number_id_employee:![image-7](https://github.com/TovaGolimstok/HADASIM4_EXE/assets/164151470/43aef08a-042b-4b50-a815-7201b9465d85)

i choose by number_id_employee:![image-8](https://github.com/TovaGolimstok/HADASIM4_EXE/assets/164151470/daa84c50-54c6-4d32-9816-a0d5915e4805)

and then i got the information:![image-9](https://github.com/TovaGolimstok/HADASIM4_EXE/assets/164151470/3d176039-9e08-4d32-97a0-1810928f2d98)


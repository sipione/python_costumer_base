# <h1 align = "center">:snake: PYTHON_COSTUMER_BASE :snake:</h1>
<p align = "center"> recreating my first CRUD in python, but now more professional </p> 


## What technology and methodology were used?
At first, and I think the most obvious, I used python language to construct all the system. Now, going beyond the obviously I would like to demonstrate the <strong>Orientation 
Object (OO) system</strong>, was created in the base two classes which one is instantiated to create Menu object, and the other one is the Client which one is instantiated to 
create the object Client with name and birth date, the age is calculated automated by the class. In addition, the project was made thinking by the <strong>Test Drive 
Development (TDD) method and all the code was thought for the easy and quick maintenance</strong>.

## About class Client
### The class' constructor and "name" attribute
This object is made by a constructor with two instances, name and birth date. At first, in the input field the information typed by the user receive a small treatment eliminating 
all the spaces in the begging and in the end by the .strip() function, at the same moment other small treatment is applied for the Title() function, after that the input content 
is conducted to the object constructor to be instantiated. The name is validated automatically, if the user types a number among the string array the object will not be create and 
an error gone be raised to the user informing the problem, after the validation if everything is ok so the object receives the attribute name.

### The class constructor, the "birthdate" and "age" attributes 
The attribute birth date in the constructor work for two information. At first the date typed in the input field goes to a validator, an intern method to verify if the date 
format in in the standard and if it's valid, cause if the input field content "30/02/2002", for example, an error gone be raised to the user informing this kind of date is invalid
(because February goes until 28th or 29th). After the validation, if everything is ok the date in the format dd/mm/yyy gone be returned to the "self.bith_date" attribute. After 
this validation the same information is donated to other inter method, the age generator. This inters method uses the birth date information and the actual date to calculate the 
age in the construction of the object. An important point is, if the attribute be invocated in other moment the age calc is made again, so the age will not be the same of the 
construction, for this this attribute receive a getter method, the first to protect and avoid being instantiated out of the class; all time this getter is invocated, the getter
use the intern method to calculate based in the birth date, which is static.

<h2 align = "center"> :construction_worker: :construction: CAUTION! :warning: Area in construction :construction: :construction_worker:</h2>


## About class Menu


## The methods responsibilities


## The files division

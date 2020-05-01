# Vehicle Repair Manager

Your task is to create a Vehicle Management System.
For this application you need to create `vehicle_management.db` and several tables.

- BaseUser
- Client
- Mechanic
- Vehicle
- Service
- Mechanic_services
- Vehicle_repair

Take a look at the database schema to understand the structure and recreate it locally on your machines.

### Example GUI for Customer

```python
$ python vehicle_management.py
Hello!
Provide user name:
>>> Roza
Unknown user!
Would you like to create new user?
>>> yes
Are you a client or Mechanic?
>>> Client
Provide user_name:
>>> Roza
Provide phone_number:
>>> 0888 88 88 88
Provide email:
>>> roza@roza.com
Provide address:
>>> Sofia, Hack Bulgaria

Thank you, Roza!
Welcome to Vehicle Services!
Next time you try to login, provide your user_name!

You can choose from the following commands:
list_all_free_hours
list_free_hours <date>
save_repair_hour <hour_id>
update_repair_hour <hour_id>
delete_repair_hour <hour_id>
add_vehicle
update_vehicle <vehicle_id>
delete_vehicle <vehicle_id>
exit
```

### Example GUI for Customer

```python
$ python vehicle_management.py
Hello!
Provide user name:
>>> Roza

Hello, Roza!
You can choose from the following commands:
list_all_free_hours
list_free_hours <date>
save_repair_hour <hour_id>
update_repair_hour <hour_id>
delete_repair_hour <hour_id>
add_vehicle
update_vehicle <vehicle_id>
delete_vehicle <vehicle_id>
exit

command> :list_all_free_hours
+----+-------------+-------+
| id | date | start_hour   |
+----+---------------------+
| 1  | 24-05-2018  | 10:00 |
| 2  | 24-05-2018  | 10:40 |
| 3  | 25-05-2018  | 16:00 |
| 4  | 27-05-2018  | 11:20 |
+----+-------------+-------+

Hello, Roza!
You can choose from the following commands:
list_all_free_hours
list_free_hours <date>
save_repair_hour <hour_id>
update_repair_hour <hour_id>
delete_repair_hour <hour_id>
list_personal_vehicles
add_vehicle
update_vehicle <vehicle_id>
delete_vehicle <vehicle_id>
exit

command> :add_vehicle
Vehicle category:
>>> Automobile
Vehicle make:
>>> Audi
Vehicle model:
>>> A3
Vehicle register number:
>>> X 8888 XX
Vehicle gear box:
>>> Manual

Thank you! You added new personal vehicle!

Hello, Roza!
You can choose from the following commands:
list_all_free_hours
list_free_hours <date>
save_repair_hour <hour_id>
update_repair_hour <hour_id>
delete_repair_hour <hour_id>
list_personal_vehicles
add_vehicle
update_vehicle <vehicle_id>
delete_vehicle <vehicle_id>
exit

command> :save_repair_hour 1
Choose Vehicle to repair:
+----+------------------------------------+
| id |               Vehicle              |
+----+------------------------------------+
| 1  | Audi A3  with RegNumber: X 8888 XX |
+----+------------------------------------+
>>> 1
Choose Service:
+----+------------------------------------+
| id |               Service              |
+----+------------------------------------+
| 1  | Oil Change                         |
| 2  | Tire Change                        |
+----+------------------------------------+
>>> 2

Thank you! You saved an hour on 24-05-2018 at 10:00 for Tire Change!
Vehicle: Audi A3  with RegNumber: X 8888 XX
```

### Example GUI for Mechanic

```python
$ python vehicle_management.py
Hello!
Provide user name:
>>> Mechanic Panda

Hello, Mechanic Panda!
You can choose from the following commands:
list_all_free_hours
list_free_hours <date>
list_all_busy_hours
list_busy_hours <date>
add_new_repair_hour
add_new_service
update_repair_hour <hour_id>
exit

command> :update_repair_hour 4

On 23-05-2018 at 10:30:
Client: Carol Danvers
Vehicle: Audi A6 Saloon
Current Bill: 20$
Choose one of the following:
1 - change start hour
2 - change bill
3 - return to main menu

>>> 2
Current Bill is: 20$
New Bill:
>>> 27.5$

On 23-05-2018 at 10:30:
Client: Carol Danvers
Vehicle: Audi A6 Saloon
Current Bill: 27.5$
Choose one of the following:
1 - change start hour
2 - change bill
3 - return to main menu

>>> 3

Hello, Mechanic Panda!
You can choose from the following commands:
list_all_free_hours
list_free_hours <date>
list_all_busy_hours
list_busy_hours <date>
add_new_repair_hour
add_new_service
update_repair_hour <hour_id>
exit

command> :add_new_repair_hour
Repair hour date:
>>> 26-05-2018
Start Hour:
>>> 13:20

Your created new repair_hour!
+----+-------------+-------+
| id | date | start_hour   |
+----+---------------------+
| 1  | 24-05-2018  | 10:00 |
| 2  | 24-05-2018  | 10:40 |
| 3  | 25-05-2018  | 16:00 |
| 5  | 26-05-2018  | 13:20 |
| 4  | 27-05-2018  | 11:20 |
+----+-------------+-------+

Hello, Mechanic Panda!
You can choose from the following commands:
list_all_free_hours
list_free_hours <date>
list_all_busy_hours
list_busy_hours <date>
add_new_repair_hour
add_new_service
update_repair_hour <hour_id>
exit

command> :add_new_service
Provide New service name:
>>> Oil Change
```

# Business Card Catalog


Your task is to create a Business Card Catalog

You need to create one table: `User` with the following properties:

- `id` - primary key (unique, not nullable, with autoincrement...)
- `full_name` - unique string (not nullable)
- `email` - unique string (not nullable)
- `age` - integer (not nullable)
- `phone` - string (not nullable)
- `additional_info` - text


## Requirements

### 1. Supported actions

- `add` - to insert new business card
- `list` - to list all business cards
- `delete` - to delete a certain business card
- `get` - display full information for a certain business card
- `help` - to list all available options


### 2. Interface

```
$ python main.py

Hello! This is your business card catalog. What would you like? (enter "help" to list all available options)
 >> Enter command: help
#############
###Options###
#############

1. `add` - insert new business card
2. `list` - list all business cards
3. `delete` - delete a certain business card (`ID` is required)
4. `get` - display full information for a certain business card (`ID` is required)
5. `help` - list all available options
```

#### 2.1 `add`

```
>>> Enter command: add
Enter user name: ...  # type here
Enter email: ...  # type here
Enter age: ... # type here
Enter phone: ... # type here
Enter addional info (optional): ... # type here
```

#### 2.2 `list`

```
>>> Enter command: list

#############
###Contacts###
#############

1. ID: 1, Email: i.donchev@hacksoft.io, Full name: Ivaylo Donchev 

2. ID: 2, Email: rositsa@hacksoft.io, Full name: Rositsa Zlateva
```


#### 2.3 `get`

```
>>> Enter command: get

Enter id: ... # type here

Contact info:

###############
Id: 1,
Full name: Ivaylo Donchev
Email: i.donchev@hacksoft.io
Age: 23
Phone: 088......
Additional info: ...
##############
```


#### 2.4 `delete`

```
>>> Enter command: delete

Enter id: ... # type here

Following contact is deleted successfully:

###############
Id: 1,
Full name: Ivaylo Donchev
Email: i.donchev@hacksoft.io
Age: 23
Phone: 088......
Additional info: ...
##############
```

# DBReader - mysql console client.
A Python application that serves as a MySQL client and manager, allowing users to perform various actions on their MySQL databases, such as selecting, dropping, and truncating tables. The application also includes a rich library for designing tables. the application establishes a secure connection to the MySQL server using TLS (Transport Layer Security). This tool can be useful for managing and organizing large amounts of data stored in MySQL databases.
## How does it work?
* <b>Welcome screen, secure password input. </b>
![Welcome screen](/Demo_images/dbreader_welcome.png)
* <b>Main menu screen</b>
![Main menu](/Demo_images/dbreader_menu.png)
* <b>Create a table (currently only fixed params, table creator will be avaible in version 2.0) .</b>
![Create a table](/Demo_images/dbreader_table.png)
* <b>Insert data from DBPersona csv file.</b>
![DBPersona data insert](/Demo_images/dbreader_insert.png)
* <b>Select all records from a table</b>
![Select all records command](/Demo_images/dbreader_select.png)
![Select all records output](/Demo_images/dbreader_select_all.png)
* <b>Table drop command</b>
![Table drop command](/Demo_images/dbreader_drop.png)


## Requirements
1. Install packages
 - rich
```
pip install rich

```
 - mysql-connector
```
 pip install mysql-connector-python

```
 
2. DBReader and DBPersona was created and tested on Ubuntu 22.04 LTS Desktop. 
In general, it is possible that different operating systems may handle encoding differently, so it is always a good idea to be aware of this when working with text data. It is important to ensure that text is properly encoded and decoded when moving between different systems, to avoid issues such as characters appearing incorrectly or data becoming corrupted.
3. Modify 'dbreader_config.ini' file:
 - host = mysql server IP address
 - data_path = path to csv file created with DBPersona


## License
This project is licensed under the ISC License - see the LICENSE.md file for details

## 

### Author
M.Witczak




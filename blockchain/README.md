`pip install flask`

`pip install passlib`




you shold have mysql installed.

you can run the command `pip install flask-mysqldb` and then run:

`mysql.server start`

`killall mysqld mysqld_safe`

`mysql.server start`

if these commands output an error and you're running on windows 10.
you should follow these steps:


Download MySQL form their site downloading "Windows (x86, 32-bit), MSI Installer" the biggerst version from
 the two

Then set it up with the full options and I used "root" as a password and username

Go into the command prompt and type "cd\"

Searching if MySQL is running with the command "net start"

If it is not running thus you are not finding it in the list then type "services.msc" and manually start it

Then type "dir mysqld.exe /s /p"
and you should find something like "Directory of C:\Program Files\MySQL\MySQL Server 8.0\bin"

Change directory with (in this case) "cd C:\Program Files\MySQL\MySQL Server 8.0\bin"

You should be ready to go with "mysql.exe -uroot -p". If it didn't work, make sure the directory is in your PATH variable.

Enter the password in my case I have not change it thus "root"



Execute the following queries:

`mysql> CREATE DATABASE crypto;`

`mysql> USE crypto;`

`CREATE TABLE blockchain(number varchar(10), hash varchar(64), previous_hash varchar(64), data varchar(100), nonce varchar(15));`

`CREATE TABLE users(name varchar(30), username varchar(30), email varchar(50), password varchar(100));`



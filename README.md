## Little scripts for practice or for further usage

### CV Genrator

- Tried the FPDF module. I made my old CV with this. Easy to customize and update. I don't use it anymore.

### Respeller

- I'd like to try some "encrypting". This program uses 2 different methods to hide the information behind the letters. It was important to keep the "format", because I made it for my CV Generator script(in my uploaded version you can check it), so the number values, the character length, the special characters and the line breaks are the same.

### Nameday stealer

- I needed the Name-Date pairs for my database, so found a webpage which I could communicate via requests. Unfortunately, I've got much more "legal" Hungarian names in my db, so I iterate through on it with 5 ms delay(because the server on the other side blocks me) and get the date value, then save the result to a JSON file (my db on the SV3-T360-Alfabot repo can read it with a stored function) like SQL table compatible(Included primary key, every pair a new record for the same name). The missing names are also saved to a .txt file called "rossz".

### Buildfromexcel

- First play with the MSSQL server. You can use the included excel to build a database with different tables. The names, columns, types are customizable (with unhandled boundaries), just keep the structure of the .xlsx. It can also fill the tables with limited data. 

### Youtbe stealer

- Download youtube videos.

### Sleeper

- I just need something to turn my PC off if I fall asleep.


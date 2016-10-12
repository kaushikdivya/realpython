import sqlite3

with sqlite3.connect(":memory:") as connection:
	c = connection.cursor()
	roster_value = (
					('Jean-Baptiste Zorg', 'Human', 122),
					('Korben Dallas', 'Meat Popsicle', 100),
					('Aknot', 'Mangalore', -5) 
	)
	c.execute("DROP TABLE IF EXISTS Roster")
	c.execute("CREATE TABLE Roster(Name	TEXT, Species TEXT, IQ INT)")
	c.executemany("INSERT INTO Roster VALUES(?,?,?)", roster_value)
	c.execute("UPDATE Roster SET Species=? WHERE Name=?", ('Human', 'Korben Dallas'))
	c.execute("SELECT Name, IQ FROM Roster WHERE Species=?",('Human'))
	for row in c.fetchall():
		print (row)
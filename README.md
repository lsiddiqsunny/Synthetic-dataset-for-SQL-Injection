# Synthetic-dataset-for-SQL-Injection
A csv file is provided for writing SQL queries. 

The csv file will be in this structure:

| No | Problem                                 | Solution                             | setObject |
|----|-----------------------------------------|--------------------------------------|-----------|
| 1  | "SELECT * FROM Employees where id="+id1 | "SELECT * FROM Employees where id=?" | id1       |



From this row, we will provide some java code in 3-4 specific structures. 


For example:

Before code:
```
public class Dummy {
void sendRequest(Connection conn) throws SQLException {
        String sql = "SELECT * FROM Employees where id="+id1;
        Statement stmt = conn.createStatement();
        ResultSet rs = stmt.executeQuery(sql);
    }
}
```

After code:
```
public class Dummy {
void sendRequest(Connection conn) throws SQLException {
        String sql = "SELECT * FROM Employees where id=?";
        PreparedStatement stmt = conn.prepareStatement(sql);
        stmt.setObject(1 , id1);
        ResultSet rs = stmt.executeQuery();
    }
}
```

Comments:

- You can find different example of sql queries here: https://github.com/lsiddiqsunny/Database/tree/master/Oracle-SQL-PL-SQL%20-%20A%20Brief%20Introduction
- Some notes on statement and prepared statement: https://www.journaldev.com/2489/jdbc-statement-vs-preparedstatement-sql-injection-example

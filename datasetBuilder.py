import csv
beforecode1_1 = "public class Dummy {\n"+"void sendRequest(Connection conn) throws SQLException {\n"+"\t\tString sql = "
beforecode1_2 = ";\n"+"\t\tStatement stmt = conn.createStatement();\n\t\tResultSet rs = stmt.executeQuery(sql);\n\t}\n}"

aftercode1_1 = "public class Dummy {\n"+"void sendRequest(Connection conn) throws SQLException {\n"+"\t\tString sql = "
aftercode1_2 = ";\n"+"\t\tPreparedStatement stmt = conn.prepareStatement(sql);\n"
aftercode1_3 = "\t\tResultSet rs = stmt.executeQuery();\n\t}\n}"

with open('query.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(row)
            line_count+=1
        else:
            if len(row)<3:
                continue
            
            id = int(row[0])
            before_query = row[1]
            after_query = row[2]
            setObjects = []
            for i in range(3,len(row)):
                setObjects.append(row[i])
            
            f = open("./Before/"+str(id)+".java", "w")
            f.write(beforecode1_1+before_query+beforecode1_2)
            f.close()

            f = open("./After/"+str(id)+".java", "w")
            f.write(aftercode1_1+after_query+aftercode1_2)
            i = 1
            for setObject in setObjects:
                f.write("\t\tstmt.setObject("+str(i)+" , "+setObject+");\n")
                i+=1
            f.write(aftercode1_3)
            f.close()

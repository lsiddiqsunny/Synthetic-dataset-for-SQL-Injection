import csv
beforecode1_1 = "public class Dummy {\n"+"void sendRequest(Connection conn) throws SQLException {\n"+"\t\tString sql = "
beforecode1_2 = ";\n"+"\t\tStatement stmt = conn.createStatement();\n\t\tstmt.execute"
beforecode1_3 = "(sql);\n\t}\n}"

aftercode1_1 = "public class Dummy {\n"+"void sendRequest(Connection conn) throws SQLException {\n"+"\t\tString sql = "
aftercode1_2 = ";\n"+"\t\tPreparedStatement stmt = conn.prepareStatement(sql);\n"
aftercode1_3 = "\t\tstmt.execute"
aftercode1_4  = "();\n\t}\n}"


beforecode2_1 = "public class Dummy {\n"+"void sendRequest(Connection conn) throws SQLException {\n"+"\t\tStatement stmt = conn.createStatement();\n\t\tResultSet rs = stmt.execute"
beforecode2_2 = "("
beforecode2_3 = ");\n\t}\n}"

aftercode2_1 = "public class Dummy {\n"+"void sendRequest(Connection conn) throws SQLException {\n"+"\t\tPreparedStatement stmt = conn.prepareStatement("
aftercode2_2 = ");\n"
aftercode2_3 = "\t\tResultSet rs = stmt.execute"
aftercode2_4 = "();\n\t}\n}"


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
            
            f = open("./Before/"+str(2*(id-1)+1)+".java", "w")
            f.write(beforecode1_1+before_query+beforecode1_2)
            if "select".lower() in before_query.lower():
                f.write("Query"+beforecode1_3)
            else:
                f.write("Update"+beforecode1_3)
            f.close()

            f = open("./After/"+str(2*(id-1)+1)+".java", "w")
            f.write(aftercode1_1+after_query+aftercode1_2)
            i = 1
            for setObject in setObjects:
                if(len(setObject)==0):
                    break
                f.write("\t\tstmt.setObject("+str(i)+" , "+setObject+");\n")
                i+=1
            f.write(aftercode1_3)
            if "select".lower() in after_query.lower():
                f.write("Query"+aftercode1_4)
            else:
                f.write("Update"+aftercode1_4)
            
            f.close()

            f = open("./Before/"+str(2*(id-1)+2)+".java", "w")
            f.write(beforecode2_1)
            if "select".lower() in before_query.lower():
                f.write("Query"+beforecode2_2+before_query+beforecode2_3)
            else:
                f.write("Update"+beforecode2_2+before_query+beforecode2_3)

            f.close()

            f = open("./After/"+str(2*(id-1)+2)+".java", "w")
            f.write(aftercode2_1+after_query+aftercode2_2)
            i = 1
            for setObject in setObjects:
                if(len(setObject)==0):
                    break
                f.write("\t\tstmt.setObject("+str(i)+" , "+setObject+");\n")
                i+=1
            f.write(aftercode2_3)
            if "select".lower() in after_query.lower():
                f.write("Query"+aftercode2_4)
            else:
                f.write("Update"+aftercode2_4)
            f.close()



import glob, os
import csv
from collections import defaultdict
base_dir = "./Extract Query Using JP (Before)/Code/Temp"
os.chdir(base_dir)
queries = []
filedict = defaultdict(int)
for file in glob.glob("*/*.txt"):
    # print(file)
    if 'Map' in file:
        continue
    filename = file.split("\\")[0]
    filedict[filename] = filedict[filename]+1
    print(filename)

for file in glob.glob("*/*.txt"):
    # print(file)
    if 'Map' in file:
        continue
    filename = file.split("\\")[0]
    if filedict[filename]>=2:
        continue
    file = file.replace("\\","/")
    content = open(file, "r")
    # print(content.read())
    query = content.read()
    query = query.strip("'")
    queries.append([file, query])
# query = queries[0][1]
# print(query)
os.chdir('./../../../')
with open('./queries.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerows(queries)


beforecode1_1 = "public class Dummy {\n"+"void sendRequest(Connection conn) throws SQLException {\n"+"\t\tString sql = "
beforecode1_2 = ";\n"+"\t\tStatement stmt = conn.createStatement();\n\t\tstmt.execute"
beforecode1_3 = "(sql);\n\t}\n}"

aftercode1_1 = "public class Dummy {\n"+"void sendRequest(Connection conn) throws SQLException {\n"+"\t\tString sql = "
aftercode1_2 = ";\n"+"\t\tPreparedStatement stmt = conn.prepareStatement(sql);\n"
aftercode1_3 = "\t\tstmt.execute"
aftercode1_4  = "();\n\t}\n}"


beforecode2_1 = "public class Dummy {\n"+"void sendRequest(Connection conn) throws SQLException {\n"+"\t\tStatement stmt = conn.createStatement();\n\t\tstmt.execute"
beforecode2_2 = "("
beforecode2_3 = ");\n\t}\n}"

aftercode2_1 = "public class Dummy {\n"+"void sendRequest(Connection conn) throws SQLException {\n"+"\t\tPreparedStatement stmt = conn.prepareStatement("
aftercode2_2 = ");\n"
aftercode2_3 = "\t\tstmt.execute"
aftercode2_4 = "();\n\t}\n}"

beforecode3_1 = "public class Dummy {\n"+"void sendRequest(Connection conn) throws SQLException {\n"+"\t\tStatement stmt = null;\n\t\tString sql = "
beforecode3_2 = ";\n"+"\t\tstmt = conn.createStatement();\n\t\tstmt.execute"
beforecode3_3 = "(sql);\n\t}\n}"

aftercode3_1 = "public class Dummy {\n"+"void sendRequest(Connection conn) throws SQLException {\n"+"\t\tPreparedStatement stmt = null;\n\t\tString sql = "
aftercode3_2 = ";\n"+"\t\tstmt = conn.prepareStatement(sql);\n"
aftercode3_3 = "\t\tstmt.execute"
aftercode3_4  = "();\n\t}\n}"

beforecode4_1 = "public class Dummy {\n"+"void sendRequest(Connection conn) throws SQLException {\n"+"\t\tStatement stmt = null;\n\t\tsql = "
beforecode4_2 = ";\n"+"\t\tstmt = conn.createStatement();\n\t\tstmt.execute"
beforecode4_3 = "(sql);\n\t}\n}"

aftercode4_1 = "public class Dummy {\n"+"void sendRequest(Connection conn) throws SQLException {\n"+"\t\tPreparedStatement stmt = null;\n\t\tsql = "
aftercode4_2 = ";\n"+"\t\tstmt = conn.prepareStatement(sql);\n"
aftercode4_3 = "\t\tstmt.execute"
aftercode4_4  = "();\n\t}\n}"

beforecode5_1 = "public class Dummy {\n"+"void sendRequest(Connection conn) throws SQLException {\n"+"\t\tStatement stmt;\n\t\tString sql = "
beforecode5_2 = ";\n"+"\t\tstmt = conn.createStatement();\n\t\tstmt.execute"
beforecode5_3 = "(sql);\n\t}\n}"

aftercode5_1 = "public class Dummy {\n"+"void sendRequest(Connection conn) throws SQLException {\n"+"\t\tPreparedStatement stmt;\n\t\tString sql = "
aftercode5_2 = ";\n"+"\t\tstmt = conn.prepareStatement(sql);\n"
aftercode5_3 = "\t\tstmt.execute"
aftercode5_4  = "();\n\t}\n}"


beforecode6_1 = "public class Dummy {\n"+"void sendRequest(Connection conn) throws SQLException {\n"+"\t\tStatement stmt;\n\t\tsql = "
beforecode6_2 = ";\n"+"\t\tstmt = conn.createStatement();\n\t\tstmt.execute"
beforecode6_3 = "(sql);\n\t}\n}"

aftercode6_1 = "public class Dummy {\n"+"void sendRequest(Connection conn) throws SQLException {\n"+"\t\tPreparedStatement stmt;\n\t\tsql = "
aftercode6_2 = ";\n"+"\t\tstmt = conn.prepareStatement(sql);\n"
aftercode6_3 = "\t\tstmt.execute"
aftercode6_4  = "();\n\t}\n}"


beforecode7_1 = "public class Dummy {\n"+"void sendRequest(Connection conn) throws SQLException {\n"+"\t\tsql = "
beforecode7_2 = ";\n"+"\t\tStatement stmt = conn.createStatement();\n\t\tstmt.execute"
beforecode7_3 = "(sql);\n\t}\n}"

aftercode7_1 = "public class Dummy {\n"+"void sendRequest(Connection conn) throws SQLException {\n"+"\t\tsql = "
aftercode7_2 = ";\n"+"\t\tPreparedStatement stmt = conn.prepareStatement(sql);\n"
aftercode7_3 = "\t\tstmt.execute"
aftercode7_4  = "();\n\t}\n}"


beforecode8_1 = "public class Dummy {\n"+"void sendRequest(Connection conn) throws SQLException {\n"+"\t\tstmt = conn.createStatement();\n\t\tstmt.execute"
beforecode8_2 = "("
beforecode8_3 = ");\n\t}\n}"

aftercode8_1 = "public class Dummy {\n"+"void sendRequest(Connection conn) throws SQLException {\n"+"\t\tstmt = conn.prepareStatement("
aftercode8_2 = ");\n"
aftercode8_3 = "\t\tstmt.execute"
aftercode8_4 = "();\n\t}\n}"

beforecode9_1 = "public class Dummy {\n"+"void sendRequest(Connection conn) throws SQLException {\n"+"\t\tStatement stmt;\n\t\tstmt = conn.createStatement();\n\t\tstmt.execute"
beforecode9_2 = "("
beforecode9_3 = ");\n\t}\n}"

aftercode9_1 = "public class Dummy {\n"+"void sendRequest(Connection conn) throws SQLException {\n"+"\t\tPreparedStatement stmt;\n\t\tstmt = conn.prepareStatement("
aftercode9_2 = ");\n"
aftercode9_3 = "\t\tstmt.execute"
aftercode9_4 = "();\n\t}\n}"

with open('queries.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == -1:
            print(row)
            line_count+=1
        else:
            fileno = row[0].split('.')[0].replace('/','_')
            print(fileno)
            line_count+=1
            id = line_count
            before_query = row[1]
            # after_query = row[2]
            # setObjects = []
            # for i in range(3,len(row)):
            #     setObjects.append(row[i])
            # 1
            f = open("./project_Before/"+fileno+"_1.java", "w")
            f.write(beforecode1_1+before_query+beforecode1_2)
            if "select".lower() in before_query.lower():
                f.write("Query"+beforecode1_3)
            else:
                f.write("Update"+beforecode1_3)
            f.close()
            
            f = open("./project_Before/"+fileno+"_2.java", "w")
            f.write(beforecode2_1)
            if "select".lower() in before_query.lower():
                f.write("Query"+beforecode2_2+before_query+beforecode2_3)
            else:
                f.write("Update"+beforecode2_2+before_query+beforecode2_3)

            f.close()

            f = open("./project_Before/"+fileno+"_3.java", "w")
            f.write(beforecode3_1+before_query+beforecode3_2)
            if "select".lower() in before_query.lower():
                f.write("Query"+beforecode3_3)
            else:
                f.write("Update"+beforecode3_3)
            f.close()

            f = open("./project_Before/"+fileno+"_4.java", "w")
            f.write(beforecode4_1+before_query+beforecode4_2)
            if "select".lower() in before_query.lower():
                f.write("Query"+beforecode4_3)
            else:
                f.write("Update"+beforecode4_3)
            f.close()

            f = open("./project_Before/"+fileno+"_5.java", "w")
            f.write(beforecode5_1+before_query+beforecode5_2)
            if "select".lower() in before_query.lower():
                f.write("Query"+beforecode5_3)
            else:
                f.write("Update"+beforecode5_3)
            f.close()

            f = open("./project_Before/"+fileno+"_6.java", "w")
            f.write(beforecode6_1+before_query+beforecode6_2)
            if "select".lower() in before_query.lower():
                f.write("Query"+beforecode6_3)
            else:
                f.write("Update"+beforecode6_3)
            f.close()

            f = open("./project_Before/"+fileno+"_7.java", "w")
            f.write(beforecode7_1+before_query+beforecode7_2)
            if "select".lower() in before_query.lower():
                f.write("Query"+beforecode7_3)
            else:
                f.write("Update"+beforecode7_3)
            f.close()

            f = open("./project_Before/"+fileno+"_8.java", "w")
            f.write(beforecode8_1)
            if "select".lower() in before_query.lower():
                f.write("Query"+beforecode8_2+before_query+beforecode8_3)
            else:
                f.write("Update"+beforecode8_2+before_query+beforecode8_3)

            f.close()

            f = open("./project_Before/"+fileno+"_9.java", "w")
            f.write(beforecode9_1)
            if "select".lower() in before_query.lower():
                f.write("Query"+beforecode9_2+before_query+beforecode9_3)
            else:
                f.write("Update"+beforecode9_2+before_query+beforecode9_3)

            f.close()



            # f = open("./After/"+str(2*(id-1)+2)+".java", "w")
            # f.write(aftercode2_1+after_query+aftercode2_2)
            # i = 1
            # for setObject in setObjects:
            #     if(len(setObject)==0):
            #         break
            #     f.write("\t\tstmt.setObject("+str(i)+" , "+setObject+");\n")
            #     i+=1
            # f.write(aftercode2_3)
            # if "select".lower() in after_query.lower():
            #     f.write("Query"+aftercode2_4)
            # else:
            #     f.write("Update"+aftercode2_4)
            # f.close()

'''
import glob, os
import csv
from collections import defaultdict

base_dir = "./Extract Query Using JP (After)/Code/Temp"
os.chdir(base_dir)
queries = []
filedict = defaultdict(int)
for file in glob.glob("*/*.txt"):
    # print(file)
    if 'Map' in file:
        continue
    if 'String' in file:
        filename = file.split("\\")[0]
        filedict[filename] = filedict[filename]+1
        print(filename)
for file in glob.glob("*/*.txt"):
    if 'Map' in file:
        continue
    # print(file)
    if 'String' in file:
        filename = file.split("\\")[0]
        if filedict[filename]>=2:
            continue;
    if 'String' in file:
        row = []
        row.append(file)
        try:
            content = open(file, "r")
            # print(content.read())
            query = content.read()
            query = query.strip("'")
            row.append(query)
            file = file.replace('String','SetObj')
            file = file.replace("\\","/")
            content = open(file, "r")
            # print(content.read())
            
            for line in content.readlines():
                # print(line)
                line = line.replace('\n','')
                row.append(line)
            # query = content.read()
            # query = query.strip("'")
        except:
            continue
        
        
        
        if len(row)>2:
            queries.append(row)

# query = queries[0]
# print(query)
os.chdir('./../../../')
with open('./queries.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerows(queries)





aftercode1_1 = "public class Dummy {\n"+"void sendRequest(Connection conn) throws SQLException {\n"+"\t\tString sql = "
aftercode1_2 = ";\n"+"\t\tPreparedStatement stmt = conn.prepareStatement(sql);\n"
aftercode1_3 = "\t\tstmt.execute"
aftercode1_4  = "();\n\t}\n}"



aftercode2_1 = "public class Dummy {\n"+"void sendRequest(Connection conn) throws SQLException {\n"+"\t\tPreparedStatement stmt = conn.prepareStatement("
aftercode2_2 = ");\n"
aftercode2_3 = "\t\tstmt.execute"
aftercode2_4 = "();\n\t}\n}"


aftercode3_1 = "public class Dummy {\n"+"void sendRequest(Connection conn) throws SQLException {\n"+"\t\tPreparedStatement stmt = null;\n\t\tString sql = "
aftercode3_2 = ";\n"+"\t\tstmt = conn.prepareStatement(sql);\n"
aftercode3_3 = "\t\tstmt.execute"
aftercode3_4  = "();\n\t}\n}"



aftercode4_1 = "public class Dummy {\n"+"void sendRequest(Connection conn) throws SQLException {\n"+"\t\tPreparedStatement stmt = null;\n\t\tsql = "
aftercode4_2 = ";\n"+"\t\tstmt = conn.prepareStatement(sql);\n"
aftercode4_3 = "\t\tstmt.execute"
aftercode4_4  = "();\n\t}\n}"



aftercode5_1 = "public class Dummy {\n"+"void sendRequest(Connection conn) throws SQLException {\n"+"\t\tPreparedStatement stmt;\n\t\tString sql = "
aftercode5_2 = ";\n"+"\t\tstmt = conn.prepareStatement(sql);\n"
aftercode5_3 = "\t\tstmt.execute"
aftercode5_4  = "();\n\t}\n}"




aftercode6_1 = "public class Dummy {\n"+"void sendRequest(Connection conn) throws SQLException {\n"+"\t\tPreparedStatement stmt;\n\t\tsql = "
aftercode6_2 = ";\n"+"\t\tstmt = conn.prepareStatement(sql);\n"
aftercode6_3 = "\t\tstmt.execute"
aftercode6_4  = "();\n\t}\n}"




aftercode7_1 = "public class Dummy {\n"+"void sendRequest(Connection conn) throws SQLException {\n"+"\t\tsql = "
aftercode7_2 = ";\n"+"\t\tPreparedStatement stmt = conn.prepareStatement(sql);\n"
aftercode7_3 = "\t\tstmt.execute"
aftercode7_4  = "();\n\t}\n}"




aftercode8_1 = "public class Dummy {\n"+"void sendRequest(Connection conn) throws SQLException {\n"+"\t\tstmt = conn.prepareStatement("
aftercode8_2 = ");\n"
aftercode8_3 = "\t\tstmt.execute"
aftercode8_4 = "();\n\t}\n}"



aftercode9_1 = "public class Dummy {\n"+"void sendRequest(Connection conn) throws SQLException {\n"+"\t\tPreparedStatement stmt;\n\t\tstmt = conn.prepareStatement("
aftercode9_2 = ");\n"
aftercode9_3 = "\t\tstmt.execute"
aftercode9_4 = "();\n\t}\n}"


with open('queries.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == -1:
            print(row)
            line_count+=1
        else:
            fileno = row[0].split('.')[0].replace('\\','_')
            print(fileno)
            line_count+=1
            id = line_count
            # before_query = row[1]
            after_query = row[1]
            setObjects = []
            for i in range(2,len(row)):
                setObjects.append(row[i])
            

            f = open("./project_After/"+fileno+"_1.java", "w")
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


            f = open("./project_After/"+fileno+"_2.java", "w")
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

            f = open("./project_After/"+fileno+"_3.java", "w")
            f.write(aftercode3_1+after_query+aftercode3_2)
            i = 1
            for setObject in setObjects:
                if(len(setObject)==0):
                    break
                f.write("\t\tstmt.setObject("+str(i)+" , "+setObject+");\n")
                i+=1
            f.write(aftercode3_3)
            if "select".lower() in after_query.lower():
                f.write("Query"+aftercode3_4)
            else:
                f.write("Update"+aftercode3_4)
            
            f.close()

            f = open("./project_After/"+fileno+"_4.java", "w")
            f.write(aftercode4_1+after_query+aftercode4_2)
            i = 1
            for setObject in setObjects:
                if(len(setObject)==0):
                    break
                f.write("\t\tstmt.setObject("+str(i)+" , "+setObject+");\n")
                i+=1
            f.write(aftercode4_3)
            if "select".lower() in after_query.lower():
                f.write("Query"+aftercode4_4)
            else:
                f.write("Update"+aftercode4_4)
            
            f.close()

            f = open("./project_After/"+fileno+"_5.java", "w")
            f.write(aftercode5_1+after_query+aftercode5_2)
            i = 1
            for setObject in setObjects:
                if(len(setObject)==0):
                    break
                f.write("\t\tstmt.setObject("+str(i)+" , "+setObject+");\n")
                i+=1
            f.write(aftercode5_3)
            if "select".lower() in after_query.lower():
                f.write("Query"+aftercode5_4)
            else:
                f.write("Update"+aftercode5_4)
            
            f.close()

            f = open("./project_After/"+fileno+"_6.java", "w")
            f.write(aftercode6_1+after_query+aftercode6_2)
            i = 1
            for setObject in setObjects:
                if(len(setObject)==0):
                    break
                f.write("\t\tstmt.setObject("+str(i)+" , "+setObject+");\n")
                i+=1
            f.write(aftercode6_3)
            if "select".lower() in after_query.lower():
                f.write("Query"+aftercode6_4)
            else:
                f.write("Update"+aftercode6_4)
            
            f.close()

            f = open("./project_After/"+fileno+"_7.java", "w")
            f.write(aftercode7_1+after_query+aftercode7_2)
            i = 1
            for setObject in setObjects:
                if(len(setObject)==0):
                    break
                f.write("\t\tstmt.setObject("+str(i)+" , "+setObject+");\n")
                i+=1
            f.write(aftercode7_3)
            if "select".lower() in after_query.lower():
                f.write("Query"+aftercode7_4)
            else:
                f.write("Update"+aftercode7_4)
            
            f.close()

            f = open("./project_After/"+fileno+"_8.java", "w")
            f.write(aftercode8_1+after_query+aftercode8_2)
            i = 1
            for setObject in setObjects:
                if(len(setObject)==0):
                    break
                f.write("\t\tstmt.setObject("+str(i)+" , "+setObject+");\n")
                i+=1
            f.write(aftercode8_3)
            if "select".lower() in after_query.lower():
                f.write("Query"+aftercode8_4)
            else:
                f.write("Update"+aftercode8_4)
            f.close()

            f = open("./project_After/"+fileno+"_9.java", "w")
            f.write(aftercode9_1+after_query+aftercode9_2)
            i = 1
            for setObject in setObjects:
                if(len(setObject)==0):
                    break
                f.write("\t\tstmt.setObject("+str(i)+" , "+setObject+");\n")
                i+=1
            f.write(aftercode9_3)
            if "select".lower() in after_query.lower():
                f.write("Query"+aftercode9_4)
            else:
                f.write("Update"+aftercode9_4)
            f.close()
'''
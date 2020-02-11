import sys
def create_stub(file,line):
    line = line.strip()
    left_param = line[:line.find("(")]
    function_name =((left_param.strip().split(" "))[len(left_param.strip().split(" "))-1]).strip()
    return_type = left_param.strip().split(" ")[len(left_param.strip().split(" "))-2].strip()
    all_param_list = line[line.find("(")+1:line.find(")")];
    all_params = all_param_list.split(",")
    data_packet = function_name+"|"+str(len(all_params))
    file.write("\n\t"+line[0: len(line) - 1]+"{\n")
    file.write("\n\t\tString dataPacket = \""+data_packet)
    data_packet = ""
    first = False
    for string in all_params:
        data_type = (string.strip().split(" "))[0].strip()
        var_name = (string.strip().split(" "))[1].strip()
        if first:
            data_packet=data_packet + "+\""            
        data_packet+="|" + data_type + ";\"+" + var_name
        first = True
    file.write(data_packet)
    if(first):
        file.write(";")
    else:
        file.write("\";")
    file.write("\n\t\tString Output = \"\\0\";")
    file.write("\n\t\ttry{")
    file.write("\n\t\t\tURL url = new URL(\"http://localhost:8080/rpc_dir/hello\");")
    file.write("\n\t\t\tURLConnection conn = url.openConnection();")
    file.write("\n\t\t\tconn.setDoOutput(true);")
    file.write("\n\t\t\tBufferedWriter out = new BufferedWriter( new OutputStreamWriter( conn.getOutputStream() ) );")
    file.write("\n\t\t\tout.write(\"username=\"+dataPacket+\"\\r\\n\");")
    file.write("\n\t\t\tout.flush();")
    file.write("\n\t\t\tout.close();")
    file.write("\n\t\t\tBufferedReader in =new BufferedReader( new InputStreamReader( conn.getInputStream() ) );")
    file.write("\n\t\t\tString response;")


    file.write("\n\t\t\tresponse = in.readLine();")

    file.write("\n\t\t\tOutput=response;")
    file.write("}\n\t\tcatch(Exception e){")
    file.write("\n\t\t\tOutput = \"\\0\";\n\t\t}")
    if return_type=="int":
        file.write("\n\t\treturn Integer.parseInt(Output);")
    elif return_type=="float":
        file.write("\n\t\treturn Float.parseFloat(Output);")
    elif return_type=="double":
        file.write("\n\t\treturn Double.parseDouble(Output);")
    elif return_type=="string":
        file.write("\n\t\treturn Output;")


    file.write("\n\t}")

def create_stubs(file,declaration_file):
    with open(declarations_file) as reader:
        while True:
            line  = reader.readline()
            if not line:
                break
            create_stub(file,line)
    return

def append_file(file,mail_file):
    with open(main_file) as reader:
        file.write("\n")
        while True:
            line = reader.readline()
            if not line:
                break
            file.write(line)

def main(declarations_file,main_file):
    with open('Client.java', 'w') as file: 
        file.write("import java.net.*; \n")
        file.write("import java.io.*;\n")

        file.write("public class Client { \n")
        append_file(file,main_file)
        create_stubs(file,declarations_file)
        file.write("\n}")
    return

if __name__=="__main__": 
    declarations_file = sys.argv[1]
    main_file = sys.argv[2]
    main(declarations_file,main_file) 

    

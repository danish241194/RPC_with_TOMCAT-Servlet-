import sys
import os 
import pathlib
def write_definitions(writer,definition_file):
    with open(definition_file) as reader:
        while True:
            line  = reader.readline()
            if not line:
                break
            writer.write("\n")
            writer.write(line)
    return
def main(definition_file):
    with open('Server.java','w') as writer:
        writer.write("import javax.servlet.http.HttpServlet;\nimport javax.servlet.*;\nimport java.io.*;\nimport javax.servlet.http.HttpServletRequest;\nimport javax.servlet.http.HttpServletResponse; \nimport java.lang.reflect.Method; \n");
        writer.write("public class Server extends HttpServlet{\n");
        writer.write(" private final static String _USERNAME = \"username\";\n");
        writer.write("\n\tprotected void doPost(HttpServletRequest request, HttpServletResponse response ) throws ServletException, IOException {\n");
        writer.write("\n\t\t\ttry{");
        writer.write("\n\t\t\tPrintWriter out = response.getWriter();");


        writer.write("\n\t\t\t\tString Response = request.getParameter( _USERNAME );");

        writer.write("\n\t\t\t\tint totalParamters = Integer.parseInt(Response.split(\"\\\\|\")[1]);");
        writer.write("\n\t\t\t\tClass Parameter_Types[] = new Class[totalParamters];");
        writer.write("\n\t\t\t\tObject Parameter_Values[] = new Object[totalParamters];");
        writer.write("\n\t\t\t\tString functionName = Response.split(\"\\\\|\")[0].trim();");
        writer.write("\n\t\t\t\tString paramsString = Response.substring(functionName.length() + 1 + Response.split(\"\\\\|\")[1].length() + 1);");
        writer.write("\n\t\t\t\tint i = 0;");
        writer.write("\n\t\t\t\tfor (String parm : paramsString.split(\"\\\\|\")) {");
        writer.write("\n\t\t\t\t\tString dataType = parm.split(\";\")[0].trim();");
        writer.write("\n\t\t\t\t\tString value = parm.split(\";\")[1].trim();");
        writer.write("\n\t\t\t\t\tif (dataType.equals(\"int\")) {");
        writer.write("\n\t\t\t\t\t\tParameter_Types[i] = int.class;");
        writer.write("\n\t\t\t\t\t\tParameter_Values[i] = Integer.parseInt(value);");
        writer.write("\n\t\t\t\t\t} else if (dataType.equals(\"float\")) {");
        writer.write("\n\t\t\t\t\t\tParameter_Types[i] = float.class;");
        writer.write("\n\t\t\t\t\t\tParameter_Values[i] = Float.parseFloat(value);");
        writer.write("\n\t\t\t\t\t} else if (dataType.equals(\"char\")) {");
        writer.write("\n\t\t\t\t\t\tParameter_Types[i] = char.class;");
        writer.write("\n\t\t\t\t\t\tParameter_Values[i] = value.charAt(0);");
        writer.write("\n\t\t\t\t\t} else if (dataType.equals(\"double\")) {");
        writer.write("\n\t\t\t\t\t\tParameter_Types[i] = double.class;");
        writer.write("\n\t\t\t\t\t\tParameter_Values[i] = Double.parseDouble(value);");
        writer.write("\n\t\t\t\t\t}");
        writer.write("    \n\t\t\t\t\ti++;");
        writer.write("\n\t\t\t\t}");
        writer.write("\n\t\t\t\tString Class_Name = \"Definition\";");
        writer.write("\n\t\t\t\tClass Cls = Class.forName(Class_Name);");
        writer.write("\n\t\t\t\tObject Obj = Cls.getDeclaredConstructor().newInstance();");
        writer.write("\n\t\t\t\tMethod method = Cls.getDeclaredMethod(functionName, Parameter_Types);");
        writer.write("\n\t\t\t\tObject Answer = method.invoke(Obj, Parameter_Values);");
        writer.write("\n\t\t\t\tresponse.setContentType(\"text/html\");");
        writer.write("\n\t\t\t\tout.println((Answer).toString());");
     
        writer.write("\n\t}catch(Exception e){}");
        writer.write("\n\t}");
        writer.write("\n}");


if __name__=="__main__":
    parent_dir = str(pathlib.Path().absolute())
    path = os.path.join(parent_dir,"rpc_dir")
    os.mkdir(path) 
    newpath = os.path.join(path,"WEB-INF")
    os.mkdir(newpath)
    classpath = os.path.join(newpath,"classes")
    os.mkdir(classpath)
    with open(str(newpath)+'/web.xml','w') as writer:
        writer.write("<web-app> <servlet> <servlet-name>ser</servlet-name> <servlet-class>Server</servlet-class> </servlet> <servlet-mapping> <servlet-name>ser</servlet-name> <url-pattern>/hello</url-pattern> </servlet-mapping> </web-app>")
    definition_file = sys.argv[1]
    os.system("sudo javac -d "+"\""+classpath+"\" "+definition_file)
    main(definition_file)
    os.system("javac -d "+"\""+classpath+"\" -cp .:"+sys.argv[2]+" Server.java")
    print("Please Put rpc_dir folder created here in tomcat/webapps")

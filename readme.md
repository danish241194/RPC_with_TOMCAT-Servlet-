# Usage
##Files Format
```
Check Examples Folder to see the format of the files
1. header.h will be having all the declaration of the functions whose definition will be on remote side
2. Definition.java will be having all the definitions of the functions and is hence stored on remote part
3. clientMain.java will be regular java file on clients side where the function calling and logic will be written , see here you dont need to put main function in any class , generator will automcatically do it for you
```
## How to run code generators
Considering you are in src folder

### For Client code generator

```
python clientgen.py ../Example/header.h ../Example/clientMain.java 

```

### For remote code generator

```
python servergen.py ../Example/Definition.java /home/danish/Downloads/tomcat/lib/servlet-api.jar

```

## Working of RPC

1. Copy the folder namely rpc_dic generated by running remote code generator in tomcat/webapps

2. Go to tomcat/bin and run
```
sh startup.sh 
```

3. Compile Client generted java code
```
javac Client.java
```
4. Run Client
```
java Client
```


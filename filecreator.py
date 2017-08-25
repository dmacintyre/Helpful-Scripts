import datetime
import sys
import platform

def main() :
    now = datetime.datetime.now();
    

    print("Welcome to the file template creator");
    print("Your current operating platform is: " + sys.platform);
    print("Your current processor is: " + platform.processor());
    print("The current date is: " + str(now.month) + '/' + str(now.day) + '/' + str(now.year))
    print("The current time is: " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second));
    print("Supported files are as follows: ");
    printPrograms();
    while True:
        try :
            if sys.version[0] == '3' :# check for python 3 and use regular input
                selection = int(input("Enter number of filetype to create: "));
            else :# must be python 2 and use raw_input
                selection = int(raw_input("Enter number of filetype to create: "));
            break
        except ValueError:
            print("That's not an int!")
        
    ############################################################################
    # VHDL Selection
    ############################################################################
    
    if (selection == 1) :

        if sys.version[0] == '3' :# check for python 3 and use regular input
            filename = input("Enter name of the new VHDL file: ");  # get filename
            arch = input("Enter name of architecture: ");           # get architecture name
        else :
            filename = raw_input("Enter name of the new VHDL file: ");  # get filename
            arch = raw_input("Enter name of architecture: ");           # get architecture name
        target = open(filename + ".vhd" , 'w');                 # open file

        # write header
        target.write('-' * 80 + '\n');
        target.write("-- Project : PROJECTNAME\n");
        target.write("-- Author : Donald MacIntyre - djm4912\n");
        target.write("-- Date : " + str(now.month) + '/' + str(now.day) + '/' + str(now.year) + '\n');
        target.write("-- File : " + filename +".vhd\n" );
        target.write('-' * 80 + '\n');
        target.write("-- Description :\n");
        target.write('-' * 80 + '\n');
        target.write("-- $Log$\n");
        target.write('-' * 80 + '\n\n');

        #lib declerations
        target.write("library IEEE;\n");
        target.write("use IEEE.STD_LOGIC_1164.ALL;\n");
        target.write("use IEEE.std_logic_unsigned.all;\n\n");

        #entity declerations
        target.write("entity " + filename + " is\n");
        target.write("    Port (\n");
        target.write("    );\n");
        target.write("end " + filename + ";\n\n");

        #architecture declerations
        target.write("architecture " + arch + " of " + filename + " is\n\n");
        target.write('-' * 80 + '\n');
        target.write("-- Signal Declarations\n");
        target.write('-' * 80 + '\n\n');

        target.write('-' * 80 + '\n');
        target.write("-- Component Declarations\n");
        target.write('-' * 80 + '\n\n');
        target.write('-' * 80 + '\n\n');

        target.write("begin\n\n");
        target.write("end " + arch + ";");

    ############################################################################
    #C Selection
    ############################################################################

    elif ( selection == 2) :

        if sys.version[0] == '3' :# check for python 3 and use regular input
            filename = input("Enter name of the new C file: ");  # get filename
        else :
            filename = raw_input("Enter name of the new C file: ");  # get filename
        
        target = open(filename + ".c" , 'w');                # open file

        target.write("/");
        target.write('*' * 79 + '\n');
        target.write("* " + filename + ".c\n");
        target.write("* " + str(now.month) + '/' + str(now.day) + '/' + str(now.year) + '\n');
        target.write("* Donald MacIntyre - djm4912\n*\n");
        target.write("* Description:\n");
        target.write('*' * 79 + "/\n\n");
        target.write("/* Includes */\n\n");
        target.write("/* Main function */\n");
        target.write("int main(int argc, char *argv[]) {\n");
        target.write("    return 0;\n}");
            
    ############################################################################
    #C++ Selection
    ############################################################################

    elif ( selection == 3) :

        if sys.version[0] == '3' :# check for python 3 and use regular input
            filename = input("Enter name of the new C++ file: ");  # get filename
        else :
            filename = raw_input("Enter name of the new C++ file: ");  # get filename
        
        target = open(filename + ".cpp" , 'w');                # open file

        target.write("/");
        target.write('*' * 79 + '\n');
        target.write("* " + filename + ".cpp\n");
        target.write("* " + str(now.month) + '/' + str(now.day) + '/' + str(now.year) + '\n');
        target.write("* Donald MacIntyre - djm4912\n*\n");
        target.write("* Description:\n");
        target.write('*' * 79 + "/\n\n");
        target.write("/* Includes */\n\n");
        target.write("/* Main function */\n");
        target.write("int main(int argc, char *argv[]) {\n");
        target.write("    return 0;\n}");
    
    ############################################################################
    #Java Selection
    ############################################################################

    elif (selection == 4) :

        if sys.version[0] == '3' :# check for python 3 and use regular input
            filename = input("Enter name of the new java file: ");  # get filename
        else :
            filename = raw_input("Enter name of the new java file: ");  # get filename            
        
        target = open(filename + ".java" , 'w');                # open file

        target.write("/*\n");
        target.write(" * " + filename + ".java\n");
        target.write(" * Donald MacIntyre - djm4912\n *\n");
        target.write(" *\n * Description:\n *\n */\n\n");
        target.write("public class " + filename + " {\n\n");
        target.write("}");

    ############################################################################
    #Python Selection
    ############################################################################

    elif ( selection == 5) :

        if sys.version[0] == '3' :# check for python 3 and use regular input
            filename = input("Enter name of the new python file: ");  # get filename
        else :
            filename = raw_input("Enter name of the new python file: ");  # get filename
            
        
        target = open(filename + ".py" , 'w');                # open file
        target.write("\"\"\"\n");
        target.write(filename + ".py\n\n");
        target.write("Description: \n\n");
        target.write("Donald MacIntyre - djm4912\n");
        target.write("\"\"\"\n\n");

        target.write("def main() :\n\n");
        target.write("if __name__ == \"__main__\":\n    main()");

    ############################################################################
    #Octave Selection
    ############################################################################

    elif (selection == 6) :

        if sys.version[0] == '3' :# check for python 3 and use regular input
            filename = input("Enter name of the new octave file: ");  # get filename
        else :
            filename = raw_input("Enter name of the new octave file: ");  # get filename
        
        target = open(filename + ".m" , 'w');                # open file

        target.write("%Donald MacIntyre\n");
        target.write("%TITLE\n");
        target.write("%" + str(now.month) + '/' + str(now.day) + '/' + str(now.year) + '\n');
        

    ############################################################################
    #textfile
    ############################################################################

    elif ( selection == 7) :

        if sys.version[0] == '3' :# check for python 3 and use regular input
            filename = input("Enter name of the new text file: ");  # get filename
        else :
            filename = raw_input("Enter name of the new text file: ");  # get filename
            
        
        target = open(filename + ".txt" , 'w');                # open file

        target.write("Donald MacIntyre - djm4912\n");
        target.write("ASSIGNMENTTITLE\n");
        target.write("CLASSTITLE\n");
        target.write(filename + ".txt");
        
    ############################################################################
    #Invalid
    ############################################################################
       
    else:
        print("Not a valid selection");


def printPrograms() :
    programs = ["VHDL","C","C++","Java","Python","Octave","textfile"];
    count = 1;
    for p in programs :
        print(str(count) + ". " + p);
        count += 1;

if __name__ == "__main__":         
    main();

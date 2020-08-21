package week3.src;

/**
 * Created by shuxford on 25/12/2015.
 */
public class DoingIt {
    Window myWindow;
    int total;

    public void doIt(Window win){
        myWindow = win;

        //ex01();
        //ex02();
        //ex03();
        ex04();

        //firstExample();
        //secondExample();
        //constants();
        //dataTypesExamples();
        //dataTypesConversions();
        //testing();
    }

    private void ex01(){
        //<<<Documentation for methods of the Window class>>>
        //that can be applied to the instance of Window referenced by the variable myWindow
        //myWindow.clearOut()               clears all text from the output text area
        //myWindow.readIn()                 returns as a String whatever text is in the input text area
        //myWindow.writeOut(someExp)        displays its expression parameter but does NOT throw a line
        //myWindow.writeOutLine(someExp)    displays its expression parameter but does throw a line

        //the two write methods will except any value of a primitive type and display the String version of the value
        //how this kind of flexibility is implemented and what is the String version of a non-String value
        //are topics for much later
        //<<<end>>>

        //YOUR CODE BELOW HERE
        String student = "Student";
        int id;
        String full;
        myWindow.clearOut();
        id = 31552544;
        full = student + " " + id;
        myWindow.readIn(id);
        myWindow.writeOut("Hello, ");
        myWindow.writeOutLine(full);
        //YOUR CODE ABOVE HERE
    }

    private void ex02(){

        //method 1
        myWindow.clearOut();
        myWindow.writeOutLine("1");
        myWindow.writeOutLine("2");
        myWindow.writeOutLine("3");
        myWindow.writeOutLine(1+2+3);


        //method 2
        myWindow.clearOut();
        int number1;
        int number2;
        int number3;
        int number4;
        number1 = 1;
        number2 = 2;
        number3 = 3;
        number4 = number1+number2+number3;
        myWindow.writeOutLine(number1);
        myWindow.writeOutLine(number2);
        myWindow.writeOutLine(number3);
        myWindow.writeOutLine(number4);


        //method 3
        final int number = 1;
        int sum;
        myWindow.clearOut();
        myWindow.writeOutLine(number);
        myWindow.writeOutLine(number+1);
        myWindow.writeOutLine(number+2);
        myWindow.writeOutLine(number+2+3);

    }

    private void ex03(){
        //YOUR CODE BELOW HERE

        //The number of floors of a tall building
        //Data type: final integer
        final int building;
        building = 99;

        //The number of floors of a tall building under construction
        //Data type: integer
        int buc; // buc stands for building under construction
        buc = 20;

        //A distance between two buildings
        //Data type: short
        short distance;
        distance = 3984;

        //The state of a door lock
        //Data type: boolean
        boolean locked = false;
        boolean unlocked = true;


        //Your telephone number
        //Data type: string
        String number;
        number = "12345678";

        //The percentage of students enrolled in FIT1051 this semester to all other units
        //Data type:double + char
        double percentage;
        percentage = 50.0;
        char per='%';

        //Your weight in kilos
        //Data type: double
        double weight;
        weight = 44.0;

        //The weight of a litre of water in kilos
        //Data type: double
        double kilo;
        kilo = 0.001;

        //The state of coin tossing
        //Data type: boolean
        boolean head = true;
        boolean tail = false;

        //The state of dice rolling
        //Data type: integer
        int roll1=1;
        int roll2=2;
        int roll3=3;
        int roll4=4;
        int roll5=5;
        int roll6=6;

        //Whether the stock market was "bear" or "bull" or flat today
        //Data type: boolean
        boolean bear = false;
        boolean bull = true;
        boolean flat = Boolean.parseBoolean(null);

        myWindow.clearOut();
        myWindow.writeOutLine("The number of floors of a tall building: "+building+" floors");
        myWindow.writeOutLine("The number of floors of a tall building under construction: " +buc+" floors");
        myWindow.writeOutLine("The distance between two buildings: "+distance+" meters");
        myWindow.writeOutLine("The door is unlocked: "+locked);
        myWindow.writeOutLine("Your telephone number: "+number);
        myWindow.writeOutLine("The percentage of students enrolled in FIT1051 this semester to all other units: "+percentage+per);
        myWindow.writeOutLine("Your weight in kilos: "+weight+" kg");
        myWindow.writeOutLine("The weight of 1 litre of water in kilos: "+kilo+" kL");
        myWindow.writeOutLine("The state of coin tossing is head: "+head);
        myWindow.writeOutLine("The state of dice rolling: "+roll2);
        myWindow.writeOutLine("The stock market was bull today: "+bull);
        //YOUR CODE ABOVE HERE
    }

    private void ex04(){
        //YOUR CODE BELOW HERE
        int number;
        number = 1;

        double number2;
        number2 = 1.5;

        String number3;
        number3 = "3";

        boolean bool = (number == 1);

        myWindow.clearOut();
        myWindow.writeOutLine(new String(String.valueOf(number))); //int to string
        myWindow.writeOutLine((double) number); //int to double
        myWindow.writeOutLine(bool); //int to boolean

        //YOUR CODE ABOVE HERE
    }

    //SYNTAX TEMPLATES
    //dataType variableName [= dataValue][, variableName [= dataValue] ]…;
    //variableName = expression;
    //final dataType CONST_NAME [= dataValue][, CONST_NAME[= dataValue] ]…;

    //WORKSHOP CODE
    private void firstExample(){
        String firstName = "Stephen";   //declaration and initial assignment
        String lastName, fullName;      //declaration only

        myWindow.clearOut();            //clear display

        lastName = "Huxford";           //assignment of String literal

        fullName = firstName + " " + lastName;  //assignment of String expression

        myWindow.writeOutLine(fullName); //write to display
    }

    private void secondExample(){
        int number1; //declarations first in a method
        int sum;

        myWindow.clearOut();

        //myWindow.writeOutLine(number); //error
        //myWindow.writeOutLine(number1); //error

        number1 = 7;
        myWindow.writeOutLine(number1);

        number1 = number1 + 1; //mathematical impossibility
        myWindow.writeOutLine(number1);

        myWindow.writeOutLine(number1 + 11); //bad style, calculate then display
        sum = number1 + 11;
        myWindow.writeOutLine(number1 + 11);

        myWindow.writeOutLine(number1); //variable value unchanged
    }

    private void constants(){
        final int NUMBER_OF_DEPARTMENTS = 39;

        //NUMBER_OF_DEPARTMENTS = 40; error
    }

    private void dataTypesExamples(){
        char myChar, firstInitial = 'S', fullStop = '.';
        int enrolledStudents = 100, total = 0;
        double weightInKilos, totalWeightInKilos = 0.0;
        boolean testResult = false;

        myWindow.clearOut();
        myWindow.writeOutLine("First initial is " + firstInitial + fullStop);
        myWindow.writeOutLine("Number of enrolled students: " + enrolledStudents + fullStop);
        myWindow.writeOutLine("Test result was " + testResult + fullStop);
    }

    private void dataTypesConversions(){
        float money;
        int dollars; //IDE tells me this var is redundant
        dollars = 3;

        money = dollars; //widening conversion OK, loss of accuracy

        double sum = 17.0, result;
        int count = 10;

        result = sum / count; //copy of count promoted to double

        double moreMoney = 5.67;
        int moreDollars = 3;

        //moreDollars = moreMoney; //type mismatch compiler error reported
        moreDollars = (int) moreMoney; //cast forces conversion with truncation

        String digitString = "123";
        int intTarget;

        //target = (int) "123"; // error inconvertible types

        boolean found = true;
        float floatTarget;

        //floatTarget = (float) found;

    }

    private void testing(){
        myWindow.clearOut();
//
//        double d = 0.1, result = 0.0;
//
//        for (int i = 0; i <=10000000; i++)
//            result += d;
//
//
//        myWindow.writeOutLine("10 million * 0.1 = " + result + " (whooops!!!)");

//        final int MINUTES_IN_AN_HOUR = 60;
//        final int HOURS_IN_A_DAY = 24;
//        final int DAYS_IN_FEBRUARY =29;
//
//        int minutesInMonth = MINUTES_IN_AN_HOUR * HOURS_IN_A_DAY * DAYS_IN_FEBRUARY;

    }


    // =========================================================================
    // UTILITIES ===============================================================
    // =========================================================================
    private static boolean isNumeric(String str){
        return str.matches("-?\\d+(\\.\\d+)?");  //match a number with optional '-' and decimal.
    }

    private static int getRandom(int n1, int n2){
        int retVal = 0;

        retVal = n1 + (int) Math.floor(Math.random() * (n2 - n1 + 1));

        return retVal;
    }

}

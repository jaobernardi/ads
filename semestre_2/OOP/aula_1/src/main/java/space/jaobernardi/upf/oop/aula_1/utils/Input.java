package space.jaobernardi.upf.oop.aula_1.utils;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Input {
 
    public static String getStringInput(String prompt, int max_try) {
        System.out.print(prompt);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int try_count = 0;
        while (try_count <= max_try) {
            try {            
                return br.readLine();
            } catch (Exception IOException) {
                break;
            }
        }
        return null;
    }

    public static String getStringInput(String prompt) {
        return getStringInput(prompt, 10);
    }

    public static String getStringInput(int max_try) {
        return getStringInput("", max_try);
    }

    public static String getStringInput() {
        return getStringInput("", 10);
    }

}

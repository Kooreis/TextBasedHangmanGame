import java.util.Scanner;

public class HangmanGame {
    private static String[] words = {"programmer", "java", "hangman", "game", "console"};
    private static String word = words[(int) (Math.random() * words.length)];
    private static String asterisk = new String(new char[word.length()]).replace("\0", "*");
    private static int count = 0;
}
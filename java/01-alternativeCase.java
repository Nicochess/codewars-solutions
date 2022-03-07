public class StringUtils {
  
  public static String toAlternativeString(String string) {
    char[] charArray = string.toCharArray();

    for(int counter = 0; counter < charArray.length; counter++){
      char letter = charArray[counter];
      
      if(Character.isUpperCase(charArray[counter]))
        charArray[counter] = Character.toLowerCase(letter);
      else
        charArray[counter] = Character.toUpperCase(letter);
    }
    
    return new String (charArray);
  }
}
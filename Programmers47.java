import java.util.Arrays;

class Solution {
    public String solution(int[] numbers) {
        String[] numToStr = new String[numbers.length];

        for(int i=0; i<numbers.length; i++){
            numToStr[i] = String.valueOf(numbers[i]);
        }

        Arrays.sort(numToStr, (o1, o2) -> (o2 + o1).compareTo(o1 + o2));

        if (numToStr[0].equals("0")) return "0";

        StringBuilder sb = new StringBuilder();
        for(int i=0; i<numbers.length; i++) sb.append(numToStr[i]);

        return sb.toString();
    }
}

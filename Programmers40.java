import java.util.Arrays;

class Solution {    
    public int solution(int[] people, int limit) {
        Arrays.sort(people);
        
        int count = 0;
        int min = 0;
        int max = people.length - 1;
        
        while (max >= min) {
            if (people[min] + people[max] <= limit) {
                count++;
                min++;
                max--;
            } else {
                count++;
                max--;
            }
        }
        
        return count;
    }
}

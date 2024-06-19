import java.util.*;

class Solution {
    public int solution(int N, int number) {
        if (number == N) return 1;
        
        List<HashSet<Integer>> dp = new ArrayList<>();
        for (int i=0; i<9; i++) dp.add(new HashSet<>());
        
        // 숫자 하나로 만들 수 있는 건 자기 자신 뿐
        dp.get(1).add(N);
        
        for (int i=2; i<9; i++) {
            // N이 i번 들어간 집합
            HashSet<Integer> ithSet = dp.get(i);
            
            for (int j=1; j<i; j++){
                HashSet<Integer> a = dp.get(j);
                HashSet<Integer> b = dp.get(i-j);
                
                for (int x : a){
                    for (int y: b){
                        ithSet.add(x+y);
                        ithSet.add(x-y);
                        ithSet.add(x*y);
                        if (y!=0) ithSet.add(x/y);
                    }
                }
            }
            // i번 연속된 숫자 넣기
            String n = Integer.toString(N).repeat(i);
            ithSet.add(Integer.parseInt(n));
            
            // number가 있을 경우 바로 리턴
            if (ithSet.contains(number)) return i;
        }
        
        return -1;
    }
}

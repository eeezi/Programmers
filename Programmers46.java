import java.util.*;

class Solution {
    ArrayList<String> results;
    boolean[] visited;
    
    public String[] solution(String[][] tickets) {
        String[] answer = {};
        visited = new boolean[tickets.length];
        results = new ArrayList<>();
        int count = 0;

        dfs(count , "ICN", "ICN", tickets);

        Collections.sort(results);
        answer = results.get(0).split(" ");

        return answer;
    }
    
    public void dfs(int count, String start, String route, String[][] tickets) {
        if (count == tickets.length) {
            results.add(route);
            return;
        }

        for(int i=0; i< tickets.length; i++){
            if(!visited[i] && start.equals(tickets[i][0])) {
                visited[i] = true;
                dfs(count+1, tickets[i][1], route + " " + tickets[i][1], tickets);
                visited[i] = false;
            }
        }
    }
}

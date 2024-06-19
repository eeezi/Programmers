class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int[][] map = new int[n+1][m+1];
        int mod = 1000000007;

        // 물에 잠긴 지역 표시
        for (int[] puddle : puddles) {
            map[puddle[1]][puddle[0]] = -1;
        }

        // 시작점 1로 초기화
        map[1][1] = 1;
        
        for(int i=1; i<n+1; i++){
            for(int j=1; j<m+1; j++){
                if (map[i][j] == -1) continue;
                // 위쪽 탐색
                if (map[i-1][j] != -1) map[i][j] += map[i-1][j] % mod;
                // 왼쪽 탐색
                if (map[i][j-1] != -1) map[i][j] += map[i][j-1] % mod;
            }
        }

        return map[n][m] % mod;
    }
}

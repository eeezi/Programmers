public static int solution(int n, int[] stations, int w) {
        int transmission = w * 2 + 1;   // 전파 범위
        int station = 0;                // 기지국 위치(인덱스)
        int now = 1;                    // 현재 위치
        int answer = 0;

        while (now <= n) {
            // 현재 위치가 이미 설치되어있는 기지국을 전부 넘어섰거나, 설치된 기지국의 범위보다 작은 경우
            if (stations.length <= station || now < stations[station] - w) {
                // 새로운 기지국 설치 후
                // 현재 위치를 기지국을 설치한 범위 밖으로 이동
                answer++;
                now += transmission;
            } else {
                // 이미 설치되어 있는 기지국 범위 인이라면
                // 현재 위치를 이미 설치되어 있는 기지국 밖으로 이동 후
                // 다음 기지국 위치 가리키기
                now = stations[station] + w + 1;
                station++;
            }
        }

        return answer;
    }

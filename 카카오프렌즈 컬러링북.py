// https://programmers.co.kr/learn/courses/30/lessons/1829?language=java
import java.util.*;

class Solution {
    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        
        // 방문 노드
        boolean [][] visited = new boolean[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                visited[i][j] = false;
            }
        }
        
        // 상하좌우
        int[] dx = {0, 0, -1, 1};
        int[] dy = {-1, 1, 0, 0};
        
        Queue<Pair> queue = new LinkedList<>();
        
        // bfs
        for (int i = 0; i < m; i++) {
            
            for (int j = 0; j < n; j++) {
                
                int color = 0;
                int max = 1;
                
                if (picture[i][j] != 0 && !visited[i][j]) {
                    color = picture[i][j];
                    visited[i][j] = true;
                    queue.add(new Pair(i, j));
                    numberOfArea++;
                    
                }
                
                while (!queue.isEmpty()) {
                    Pair pos = queue.poll();
                    
                    // 상하좌우 체크
                    for (int k = 0; k < 4; k++) {
                        int cx = pos.x + dx[k];
                        int cy = pos.y + dy[k];
                        
                        if (cx < m && cx >= 0 && cy < n && cy >= 0) {
                            if (picture[cx][cy] == color && !visited[cx][cy]) {
                                visited[cx][cy] = true;
                                queue.add(new Pair(cx, cy));
                                max++;
                            }
                        }    
                    }                   
                }
                
                if (maxSizeOfOneArea < max) {
                    maxSizeOfOneArea = max;
                }
            }
        }
        
        
        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }
}

class Pair {
    int x;
    int y;
    public Pair(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

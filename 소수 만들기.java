// https://programmers.co.kr/learn/courses/30/lessons/12977?language=java
// 참고 (https://minhamina.tistory.com/38)
import java.util.*;

class Solution {
    int answer = 0;
    public int solution(int[] nums) {
        
        boolean[] visited = new boolean[nums.length];
 
        comb2(nums, visited, 0, 3);
        
        
        return answer;
    }
    
    // 재귀 이용
    public void comb2(int[] arr, boolean[] visited, int depth, int r) {
        if (r == 0) {
            if (check(arr, visited)) answer++;
            return;
        }
        
        if (depth == arr.length) {
            return;
        } else {
            visited[depth] = true;
            comb2(arr, visited, depth + 1, r - 1);
 
            visited[depth] = false;
            comb2(arr, visited, depth + 1, r);
        }
    }
    
    // 소수 체크 함수
    public boolean check(int[] arr, boolean[] visited) {
        int sum = 0;
        for(int i = 0; i < arr.length; i++) {
            if(visited[i] == true)
                sum += arr[i];
        }
        
        for (int i = 2; i < sum / 2; i++) {
            if (sum % i == 0) return false;
        }
        
        return true;
    }
}

import java.util.*;

// https://programmers.co.kr/learn/courses/30/lessons/42583

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        
        Queue<Integer> q = new LinkedList<>();
        
        // 다리 길이 만큼의 큐 생성
        for (int i = 0; i < bridge_length - 1; i++) { 
            // 0은 비어있음
            q.add(0); 
        }

        // 첫 번째 트럭 올라감
        q.add(truck_weights[0]);
        int sum = truck_weights[0];
        int index = 1;
        answer++;
        
        while(!q.isEmpty()) {
            answer++;
            // 다리 q가 한칸 앞으로 감 트럭이 제일 앞이면 무게 빼줌
            sum -= q.poll();
            
            // 남은 트럭 있으면
            if (index < truck_weights.length) {
                if (sum + truck_weights[index] <= weight) {
                    sum += truck_weights[index];
                    q.add(truck_weights[index]);
                    index++;
                } else {
                    q.add(0);
                }
            }
                
        }
        
        return answer;
    }
}
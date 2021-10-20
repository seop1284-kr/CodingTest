import java.util.*;

// https://programmers.co.kr/learn/courses/30/lessons/42587?language=java

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        List<Integer> list = new LinkedList<>();
        
        for (int i = 0; i < priorities.length; i++) {
            pq.add(priorities[i]);
            list.add(i);
        }
        
        int max = pq.poll();
        
        while (true) {
            int num = list.remove(0);
            
            if (priorities[num] == max) {
                answer++;
                if (num == location) {
                    break;
                }
                max = pq.poll();
            } else {
                list.add(num);
            }
            
        }
        
        return answer;
    }
}
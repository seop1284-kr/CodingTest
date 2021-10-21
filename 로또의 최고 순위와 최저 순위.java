import java.util.*;

// https://programmers.co.kr/learn/courses/30/lessons/77484?language=java#

class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = {0, 0};
        
        int count = 0;
        int zero = 0;
        for (int i = 0; i < 6; i++) {
            if (lottos[i] == 0) {
                zero++;
                continue;        
            }
            for (int j = 0; j < 6; j++) {
                if (lottos[i] == win_nums[j]) {
                    count++;
                }
            }
        }
        
        int max = count + zero;
        int min = count;
        
        answer[0] = (max == 0) ? 6 : 7 - max;
        answer[1] = (min == 0) ? 6 : 7 - min;
        
        return answer;
    }
    
}
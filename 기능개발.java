import java.util.*;

// https://programmers.co.kr/learn/courses/30/lessons/42586?language=java#

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int[] answer = {};
        List<Integer> ansList = new ArrayList<Integer>();
        
        // 남은 진도를 속도로 나눈 남은 일정 값을 progresses에 저장
        for (int i = 0; i < progresses.length; i++) {
            progresses[i] = (int)Math.ceil((100 - progresses[i]) / (double)speeds[i]);
            System.out.println(progresses[i]);
        }
        
        int max = progresses[0];
        int n = 1;
        
        // 남은 일정 배열을 반복문으로 하나씩 검사 결과 도출
        // 마지막 확인 추가
        for (int i = 1; i < progresses.length; i++) {
            
            if (max >= progresses[i]) {
                n++;
                if (i == progresses.length - 1) {
                    ansList.add(n);
                    break;
                }
            } else {
                ansList.add(n);
                n = 1;
                max = progresses[i];
                if (i == progresses.length - 1) {
                    ansList.add(1);
                    break;
                }
            }
        }

        // List to Array
        answer = new int[ansList.size()];
        for (int i = 0; i < ansList.size(); i++) {
            answer[i] = ansList.get(i);
        }
        return answer;
    }
}
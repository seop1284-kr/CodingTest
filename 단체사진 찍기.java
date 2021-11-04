// https://programmers.co.kr/learn/courses/30/lessons/1835#
// https://ndb796.tistory.com/429
import java.util.*;

class Solution {
    int answer;
    public int solution(int n, String[] data) {
        ArrayList<Character> arr = new ArrayList<>(List.of('A', 'C', 'F', 'J', 'M', 'N', 'R', 'T'));
        answer = 0;
        permutation(arr, 0, data);
        
        return answer;
    }
    
    public void swap(ArrayList<Character> arr, int i, int j) {
        char temp = arr.get(i);
        arr.set(i, arr.get(j));
        arr.set(j, temp);
    }
        
    // 모든 순열 arr 배열, depth 0 부터 시작,  int[] data 규칙
    public void permutation(ArrayList<Character> arr, int depth, String[] data) {
        // 현재 순열의 길이가 r일 때 체크
        if (depth == arr.size() && check(arr, data)) {
            answer++;
            return;
        }
        for (int i = depth; i < arr.size(); i++) {
            swap(arr, i, depth);
            permutation(arr, depth + 1, data);
            swap(arr, i, depth);
        }
    }
    
    public boolean check(ArrayList<Character> arr, String[] data) {
        
        for (int i = 0; i < data.length; i++) {
            int first = arr.indexOf(data[i].charAt(0));
            int second = arr.indexOf(data[i].charAt(2));
            char op = data[i].charAt(3);
            int v = data[i].charAt(4) - '0';
            
            if (op == '>') {
                if (Math.abs(first - second) <= v) {
                    return false;
                }
            } else if(op == '<') {
                if (Math.abs(first - second) >= v) {
                    return false;
                } 
            } else {
                if (Math.abs(first - second) != v + 1) {
                    return false;
                }
            }
        }
        

        return true;
    }
    
}

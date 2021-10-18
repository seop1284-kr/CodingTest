#!/usr/bin/env python
# coding: utf-8

# In[1]:


# https://programmers.co.kr/learn/courses/30/lessons/42584?language=python3

def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            if prices[i] > prices[j]:
                answer[i] = j - i
                break
            answer[i] = len(prices) - 1 - i
            
    return answer

solution([1, 2, 3, 2, 3])


# In[ ]:





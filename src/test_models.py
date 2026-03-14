import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyAQSmb-EcSQiVh_b9Zyb0QfdS8NlXn0ZkM")

for m in genai.list_models():
    print(m.name)
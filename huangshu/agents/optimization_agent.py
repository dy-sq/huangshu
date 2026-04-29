from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

class OptimizationAgent:
    def optimize(self, code, issues):
        prompt = f"""
代码如下:
{code}

问题:
{issues}

请给出优化建议并提供修改后的代码
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

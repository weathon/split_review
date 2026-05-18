# %%
from openai import OpenAI
import os
import dotenv
dotenv.load_dotenv()

or_client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY")
)

# %%
from datasets import load_dataset
ds = load_dataset("weathon/grpo_dataset")

# %%
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm 
import os
import json

os.makedirs("rollouts", exist_ok=True)
import re
def rollout(idx):
    ans = []
    if os.path.exists(f"rollouts/{idx:05d}.json"):
        with open(f"rollouts/{idx:05d}.json", "r") as f:
            past_scores = []
            for r in json.load(f):
                try:
                    past_scores.append(float(re.search('<score>(.*?)</score>', r).group(1)))
                    ans.append(r)
                except Exception as e:
                    pass

            for s in past_scores:
                if abs(s - ds['train'][idx]['solution']) < 0.7:
                    print(f"skipping rollout for idx {idx} since we already have a close score {s} to the solution {ds['train'][idx]['solution']}")
                    return ans, 0
                
            
                    
    # for each message, we roll out in sequence, but we parallelize across messages, to hit cache and make it cheaper
    messages = ds["train"][idx]["prompt"]
    messages[0]["content"] = messages[0]["content"]#.replace("Give your analysis first, then put your final score in a XML-style tag <score></score>", "Give a brief analysis first, then put your final score in a XML-style tag <score></score>. Do not think for too long.")
    cost = 0
    for _ in range(3):
        for attempt in range(5):
            try:
                _response = or_client.chat.completions.create(
                    model="deepseek/deepseek-v4-flash",
                    messages=messages,
                    temperature=1.2,
                    extra_body={"reasoning": {"enabled": False, "effort": "low"}, "provider": {"only": ["deepseek"]}}
                )
                response = _response.choices[0].message.content
                ans.append(response)
                cost += _response.usage.cost_details["upstream_inference_cost"]
                break
            except Exception as e:
                print(f"rollout {idx} deepseek attempt {attempt + 1}/5 failed: {e}")
                if attempt == 4:
                    raise
        

        try:
            parsed_score = float(re.search('<score>(.*?)</score>', ans[-1]).group(1))
            print("Deepseek", parsed_score - ds['train'][idx]['solution'])
        except Exception as e:
            pass

    for _ in range(3):
        for attempt in range(5):
            try:
                _response = or_client.chat.completions.create(
                    model="qwen/qwen3.5-flash-02-23",
                    messages=messages,
                    temperature=1.2,
                    extra_body={"reasoning": {"enabled": False, "effort": "low"}}
                )
                response = _response.choices[0].message.content
                ans.append(response)
                cost += _response.usage.cost_details["upstream_inference_cost"]
                break
            except Exception as e:
                print(f"rollout {idx} qwen attempt {attempt + 1}/5 failed: {e}")
                if attempt == 4:
                    raise
        
        try:
            parsed_score = float(re.search('<score>(.*?)</score>', ans[-1]).group(1))
            print("Qwen", parsed_score - ds['train'][idx]['solution'])
        except Exception as e:
            pass
        

    with open(f"rollouts/{idx:05d}.json", "w") as f:
        json.dump(ans, f, indent=4)
    print(len(ans))
    return ans, cost



with ThreadPoolExecutor(max_workers=50) as executor:
    rollouts = list(tqdm(executor.map(rollout, range(len(ds["train"]))), total=len(ds["train"])))


# %%
rollouts[0][0][0]

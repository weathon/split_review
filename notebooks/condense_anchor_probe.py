from openai import OpenAI
import dotenv
import hashlib
import os
import sys
import time

dotenv.load_dotenv("../.env")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

cache_dir = "../results/condensed_anchor_cache"
retries = 3

path = sys.argv[1]
with open(path, "r") as f:
    review_text = f.read().split("Score and Decision")[0]

prompt = """Condense this paper's human reviews into one merged anchor review, but preserve evidence.

Rules:
- Merge duplicate points across reviewers, but keep every distinct scoring-relevant point.
- Preserve strength/weakness direction, severity, magnitude, reviewer confidence, and reviewer disagreement.
- Keep concrete named methods, baselines, datasets, tables, figures, equations, examples, and numeric details.
- Put reviewer questions into Weaknesses when they overlap with a criticism, missing experiment, missing comparison, or ablation request.
- If a minority reviewer is more positive or negative, explicitly keep that contrast.
- Shorten wording, not information. Do not turn specific criticisms into vague summaries.
- Only summarize the reviewers. Do not decide whether the paper should be accepted, rejected, improved, or downgraded.
- Do not invent information.
- Do not include the title, abstract, decision, or score header.
- Return only this structure:

## Merged Review

### Summary

### Strengths

### Weaknesses"""

score_header = []
for line in review_text.splitlines():
    if line.startswith("- Decision:") or line.startswith("- Scores:"):
        score_header.append(line)
    if line == "## Abstract":
        break

if len(score_header) != 2:
    raise ValueError(f"missing decision/scores header in {path}")

os.makedirs(cache_dir, exist_ok=True)
cache_key = hashlib.sha256((prompt + "\n\n" + review_text).encode("utf-8")).hexdigest()
cache_path = os.path.join(cache_dir, f"{cache_key}.md")

if os.path.exists(cache_path):
    with open(cache_path, "r") as f:
        print(f.read())
else:
    for attempt in range(retries):
        try:
            print(f"deepseek condense attempt {attempt + 1}/{retries} for {cache_key[:10]}")
            response = client.chat.completions.create(
                model="deepseek/deepseek-v4-flash",
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": review_text},
                ],
                temperature=0,
                extra_body={"reasoning": {"enabled": True, "effort": "low"}, "provider": {"only": ["deepseek"]}},
            )
            condensed_review = "\n".join(score_header) + "\n\n" + response.choices[0].message.content
            tmp_path = f"{cache_path}.{time.time_ns()}.tmp"
            with open(tmp_path, "w") as f:
                f.write(condensed_review)
            os.replace(tmp_path, cache_path)
            print(condensed_review)
            break
        except Exception as e:
            print(f"deepseek condense failed for {cache_key[:10]} attempt {attempt + 1}/{retries}: {e}")
            if attempt == retries - 1:
                raise
            time.sleep(2)

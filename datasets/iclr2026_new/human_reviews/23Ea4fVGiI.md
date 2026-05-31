## Human Reviewer 1

### Summary
This paper introduces a prompting approach based on the Task–Method–Knowledge (TMK) framework, originally from educational research. The authors argue that LLMs often fail on multi-step planning tasks because typical prompts provide only shallow textual goals. TMK decomposes each problem into structured layers: task (goal and conditions), method (procedure), and knowledge (objects and relations). The authors uses PlanBench’s Blocksworld domain in a TMK-formatted json and compare it with the plain prompts on GPT family (GPT-4, GPT-4o, o1-mini, o1, and GPT-5). Results show modest but consistent improvements.

### Strengths
• The paper introduces a simple and interpretable idea: representing planning tasks in a structured TMK format may align with how procedural knowledge is expressed in model pre-training data

• The approach is prompt-based and requires no fine-tuning or external resources, making it easy to reproduce and extend.

• The empirical trend (larger gains for weaker models) is intuitive and suggests the TMK structure provides helpful inductive bias.

### Weaknesses
• The experiments are narrow: only one domain and one benchmark family. Claims about general planning improvement are therefore not well supported.

• There are no comparisons with so many other structured prompting methods (eg CoS, ReAct, least-to-most, chain-of-thought scaffolding and so on). It is unclear whether TMK offers advantages beyond simply using more structured json templates.

• The explanation of why TMK helps remains speculative. No ablation isolates whether improvements come from the educational knowledge model framing or just from better formatting and key-word cues.

### Questions
The writing quality and technical presentation are weak, with many typos, missing citations, and incorrect or inconsistent latex usage (eg mismatched quotes and unescaped underscores). The paper would need careful proofreading and formatting cleanup.

### Soundness
2

### Presentation
1

### Contribution
2

### Rating
2

### Confidence
3

---

## Human Reviewer 2

### Summary
The paper studies integrating the Task-Knowledge-Method (TMK) framework into prompting for LLM reasoning tasks. It focused on the blocksworld task in Planbench and experimented with OpenAI models.

### Strengths
The paper shows the potential of applying a prompting technique to improve the performance of models on the blocksworld task.

### Weaknesses
1. The reviewer finds it difficult to understand what is the core idea/contribution of TMK prompting method proposed in the paper. The paper did poorly in explaining the proposed prompting method.
2. The paper proposes a prompting method, yet there are no examples of the prompt in the paper.
3. Experimental evidence of the advantage of the proposed method is very limited: only OpenAI models, only one task (blocksworld), and many numbers are missing (Table 2)

### Questions
The presentation of the paper needs a lot more work, to list a few:
1. Missing citation in line 39.
2. Missing space in line 50.
3. Missing citation in line 394.
4. A formatting suggestion: most citations in the paper should use `\citep{}` instead of `\cite{}`.
5. Figure 1 is too big, and the resolution of the image is too low.

### Soundness
1

### Presentation
1

### Contribution
1

### Rating
0

### Confidence
5

---

## Human Reviewer 3

### Summary
The paper proposes TMK, a framework to capture specific reasoning structures in LLM reasoning tasks. It features explicit task decomposition, and benefits the LLM reasoning tasks. It proposes a PlanBench benchmark to conduct experiments.

### Strengths
The method focuses on the key problem of long reasoning LLMs, which does not have clear task decomposition during thinking.

### Weaknesses
+ Many fields are missing in Table 2, especially Plain Text + One Shot. Note that it's unfair to compare the other two columns (TMK + One Shot vs Plain Text + Zero Shot). The paper does not have other main results.
+ It does not make sense to replace standard description of blockworlds into irrelevant mystery or random words. No LLM learns it during pre-training, nor people will use those words to describe tasks, nor they will use LLMs like this.
+ It's not easy to understand what TMK is doing (lacking a concrete example of the prompt/formatting).
+ The method is only experimented on blockworlds, which is a toy dataset easily solvable by non-machine learning algorithms like DFS. It's unknown whether the method can be generalized to other meaningful domains, such as mathematical, logical, legal, scientific reasonings.

### Questions
+ There is only 1 item in the list (Line 054)
+ Gpt5 -> GPT-5 (Line 308)
+ Unknown citation (?) (Line 394)

### Soundness
1

### Presentation
1

### Contribution
1

### Rating
0

### Confidence
3
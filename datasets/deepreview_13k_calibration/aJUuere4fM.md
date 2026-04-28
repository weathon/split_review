# Does Refusal Training in LLMs Generalize to the Past Tense?

- Decision: Accept
- Avg Score: 5.75
- Scores: 8, 6, 1, 8

## Abstract
\noindent
    Refusal training is widely used to prevent LLMs from generating harmful, undesirable, or illegal outputs. We reveal a curious generalization gap in the current refusal training approaches: simply reformulating a harmful request in the past tense (e.g., \textit{"How to make a Molotov cocktail?"} to \textit{"How did people make a Molotov cocktail?"}) is often sufficient to jailbreak many state-of-the-art LLMs. We systematically evaluate this method on Llama-3 8B, Claude-3.5 Sonnet, GPT-3.5 Turbo, Gemma-2 9B, Phi-3-Mini, GPT-4o-mini, GPT-4o, o1-mini, o1-preview, and R2D2 models using GPT-3.5 Turbo as a reformulation model. For example, the success rate of this simple attack on GPT-4o increases from 1\% using direct requests to 88\% using 20 past-tense reformulation attempts on harmful requests from \texttt{JailbreakBench} with GPT-4 as a jailbreak judge. Interestingly, we also find that reformulations in the future tense are less effective, suggesting that refusal guardrails tend to consider past historical questions more benign than hypothetical future questions. Moreover, our experiments on fine-tuning GPT-3.5 Turbo show that defending against past reformulations is feasible when past tense examples are explicitly included in the fine-tuning data. Overall, our findings highlight that the widely used alignment techniques---such as SFT, RLHF, and adversarial training---employed to align the studied models can be brittle and do not always generalize as intended.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper reveals a significant vulnerability in LLM safety measures: simply reformulating harmful requests in the past tense often bypasses safety guardrails. Testing multiple leading LLMs (including GPT-4, Claude-3.5, etc.), they found that attack success rates increased dramatically with past-tense reformulation. The vulnerability persists even in newer "reasoning" models like o1-preview, though these models tend to provide less specific harmful information. The issue can be addressed through fine-tuning on past-tense examples, but requires careful balancing to avoid over-refusing legitimate requests

### Strengths
Comprehensive evaluation across multiple leading LLMs and different types of harmful requests, with a clear demonstration of the vulnerability that wasn't previously well-documented. Provides concrete evidence through systematic testing and multiple evaluation metrics used widely in the adversarial robustness field, and demonstrates a clear strategy for mitigating this threat through better finetuning.

### Weaknesses
1. Lack of evaluation on other languages

### Questions
1. Why do you think past-tense reformulations are more successful than future-tense ones? Is it related to how historical information is typically treated in training data?
2. Could this vulnerability be addressed through prompt engineering rather than fine-tuning?
3. Have you tested whether this vulnerability exists in non-English languages, given that LLM safety measures often generalize across languages?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates a gap in refusal training for large language models (LLMs), revealing that simple past-tense reformulations of harmful requests can bypass existing safety defenses. Despite advancements in supervised fine-tuning and reinforcement learning with human feedback, models often fail to reject past-tense prompts, treating them as benign historical inquiries. The authors demonstrate this vulnerability across multiple LLMs, showing high success rates in bypassing safety mechanisms. By highlighting the brittleness of current alignment techniques, this work emphasizes the need for more robust training that generalizes across linguistic variations, including tense, to effectively strengthen LLM safety measures.

### Strengths
**Novel Insight into Refusal Training**: The paper identifies a specific, under-explored vulnerability in LLM refusal training—namely, that past-tense reformulations can bypass safety mechanisms. This insight into linguistic generalization gaps is valuable for improving the robustness of refusal training.

**Thorough Empirical Validation**: By evaluating the past-tense attack across a wide range of advanced models (e.g., GPT-3.5 Turbo, Claude-3.5, GPT-4o), the authors provide convincing evidence that the issue is both widespread and impactful. The systematic comparisons enhance the study’s credibility and relevance.

**Practical Contributions**: The paper proposes straightforward mitigation strategies, such as fine-tuning with explicit past-tense refusal examples, providing actionable insights for developers aiming to improve model safety.

### Weaknesses
 **Limited Solution Exploration**: Although the paper identifies a clear vulnerability, the proposed solution—incorporating past-tense examples in training—is relatively basic and may not address other similar reformulations or linguistic variations. The paper does not explore the potential for more sophisticated methods, such as adversarial training with a broader range of linguistic variations, or techniques that focus on semantic understanding rather than surface-level linguistic features. The proposed solution seems more like a patch rather than a robust fix.

**Lack of Theoretical Analysis**: No theoretical insight is given for why a generalization gap between past-tense and present-tense, which is more interesting and can deepen our understanding to eliminate other underexplored vulnerabilities. The paper lacks a discussion on why LLMs struggle with this specific type of generalization, especially given that the core semantic content of the harmful request remains the same. This absence of theoretical analysis limits the paper's contribution to a purely empirical observation, without providing a deeper understanding of the underlying mechanisms.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper presents a jailbreaking method that involves paraphrasing harmful questions in the past tense. This method is effective across various SOTA LLMs. Furthermore, the paper demonstrates that safety fine-tuning using harmful prompts in the past tense reduces the attack success rate in GPT-3.5-Turbo.

### Strengths
-- Alignment of LLMs is an important domain of research, and the more vulnerabilities that are found, the better it is for researchers and model providers to patch them. This paper presents a cost-effective jailbreaking method that paraphrases harmful prompts in the past tense to attack LLMs, showing that LLM safety training has not generalized to past-tense formulations.

-- The efficacy and simplicity of this attack across various models highlight the urgency of addressing it.

### Weaknesses
1.  While the attack is simple and cost-effective, paraphrasing attacks have proven effective in the past. 

--> One possible reason for this jailbreak's success might be the lack of generalization (or explicit safety training) in handling past tense harmful prompts (as mentioned in the paper).

--> This does not appear to be a novel type of attack.

-->  It would be helpful to know whether this attack was discovered through systematic investigation / brute-force testing.

--> In my opinion, the paper should discuss both successful and unsuccessful approaches that were tried before discovering this prompt.

2. Regarding dataset selection, there are other more comprehensive datasets available that could provide more rigorous results. 

--> The current study's reliance on only 100 harmful questions significantly limits its scope and generalizability.

--> The paper's findings would have been more robust if multiple datasets had been utilized. With results based on just 100 data points, the experimental conclusions cannot be considered sufficiently rigorous.

3. Regarding targeted models: Based on the results in Table 1, a significant limitation is the absence of testing on the GPT-4 model. 

--> While the study examines the progression of the attack from GPT-3.5 to GPT-4o/mini, it overlooks GPT-4, which has demonstrated great robustness in many previous attack scenarios. 

--> Additionally, other prominent language model families, such as Gemini Pro, were not included in the experiment. 


4. Defense-Section 4: The fine-tuning experiments could have been extended beyond GPT-3.5-Turbo to include other open-source LLMs (such as Llama, and Qwen), providing a more comprehensive analysis.

--> The paper's research scope appears limited to paraphrasing harmful questions in the past tense and addressing them through safety training. 

**** As both jailbreaking through paraphrasing harmful prompts and safety training via fine-tuning have been comprehensively studied in the existing literature, the paper lacks a novel contribution.

### Questions
Minor fixes:

1. Please clarify whether its Llama-3-8B [ Instruct or Completion]  model. 

2. Line 21: I think the citation is missing for  Wei et al. for chain-of-thought paper.

3. Line 382: missing dash - in chain of thought. 

Questions: 

From a further research perspective, several questions remain unanswered in the paper: Is it possible to increase the attack success rate with the current approach? What additional strategies could attackers employ? What other potential threat models should be investigated? Can safety training alone prevent this attack, or have other methods been tested?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper focuses on one pretty simple (but surprisingly effective) jailbreaking strategy which involves asking models for harmful information using the past tense in plain English. They find that future tense does not work as well and that AT can work as a defense (unsurprisingly). Based on these two observations, they speculate that failed generalization to past tense is a unique and interesting artifact of either pertaining or fine-tuning to focus (maybe implicitly) on present and future harm.  

Overall, I think that this paper sets out to do something very simple, does it well, and shows that it works surprisingly well. In that sense, I think it's clearly valuable but not particularly remarkable.

### Strengths
S1: I was surprised by the results. I think that this is a new contribution to the best of my knowledge. And I can see these being valuable for red teaming and AT. 

S2: As far as I know, this is one of the first papers that has gone to successfully attack OpenAI o1. For that reason, I think this paper is especially citeable and noteworthy. It won't be the last though.

### Weaknesses
W1: Though valuable and well done, this paper is doing something that many have done before. So aside from some of the unique contributions (which are unique) this paper is also, in a sense, yet another paper to dunking on SOTA models with a niche jailbreaking technique. For that reason, I don' think this paper is breaking amazing ground, and I wouldn't recommend it for a reward. 

W2: I think that the paragraph from 441 to 448 could discuss more related work. I think the chosen papers seem kind of arbitrary. One could also discuss https://arxiv.org/abs/2309.00614, and cite papers on harmfulness probing, latent adversarial training, representation noising, and/or latent anomaly detection. Also describing Zou et al's method as rejecting harmful outputs seems incorrect since it's about latents. 

W3: This paper focuses on attacks, with a simple AT experiment as almost an afterthought. This is good. But since the paper speculates about how these attacks might reveal some limitations of current alignment techniques, this begs the question of whether models that have undergone AT with past tense might have more generalizable robustness in general. Since the scope of the paper is currently so narrow, this kind of experiment (or maybe something similar) would valuable expand it.

### Questions
See above

### Soundness
4

### Presentation
4

### Contribution
3

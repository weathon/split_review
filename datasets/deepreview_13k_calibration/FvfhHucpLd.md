# DIVERSITY OF THOUGHT IMPROVES REASONING ABILITIES OF LARGE LANGUAGE MODELS

- Decision: Reject
- Avg Score: 3.67
- Scores: 3, 3, 5

## Abstract
Large language models (LLMs) are documented to struggle in settings that require complex reasoning. Nevertheless, instructing the model to break the problem into smaller reasoning steps (Wei et al., 2022b), or ensembling various generations through decoding alterations (Wang et al., 2023) boosts performance. Current approaches assume the input prompt is fixed and expect the decoding strategies introduce diversity needed for ensembling. In this work, we relax this assumption and discuss how one can create and leverage variations of the input prompt as a means to diversity of thought to improve model performance. We propose a methodology to automatically improve prompt diversity by soliciting feedback from the LLM. In our new prompting approach, DIV-SE (DIVerse reasoning path Self-Ensemble), we use these diverse prompts as part of an ensemble across multiple inference calls. We also propose a cost-effective alternative where diverse prompts are used within a single inference call; we call this IDIV-SE (In-call DIVerse reasoning path Self-Ensemble). Under a fixed generation budget, DIVSE and IDIV-SE generate more accurate results than the previously discussed baselines using both GPT-3.5 and GPT-4 on several reasoning benchmarks, without modifying the decoding process. Additionally, DIV-SE advances state-of-the-art performance on recent planning benchmarks (Valmeekam et al., 2022), exceeding
the highest previously reported accuracy by at least 29.6 percentage points on the most challenging 4/5 blocks task in the Blocksworld problem. Our results shed light on how to enforce prompt diversity towards LLM reasoning without increasing the generation budget.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes DIV-SE and IDIV-SE as prompting strategies to increase diversity of LLM generated responses to reasoning tasks. Instead of relying on the decoding algorithm (sampling) to generate diverse solutions, this approach creates prompts using different approaches from a pool of approaches suitable for a task. When prompted with these different approaches the LLM is shown to generate diverse solutions. Aggregating the results from these diverse prompts has been shown to be more effective than the self-consistency baseline. 

The method can be summarised as follows:
1. Create Persona, Approach combinations for a given task: Given a dataset - pick a random question q; ask LLM to come up with Personas & Approaches using LLM output (aggregating m x n suggestions from LLMs based in instruction|question|template ) & then picking pick top 5 using word cloud. Similarly let the LLM generate suggestions for apt personas for a given task.
2. Pick an optimal P,A: For all P,A combinations the composite prompt is tried on a held-out set. And those with the highest performance are selected.
3. Create Augmented demonstrations: Once the approaches for a task are selected as per above, we ask the LLM to modify existing demonstrations with the given set of approaches. 
4. Inference: Run with multiple prompts, each with a different augmented demonstration. Then output of these is aggregated. This can be done in a single call to the LLM (IDIV-SE) instead of independent inference steps (DIV-SE).

### Strengths
- Clever inference cost optimisation on top of self-consistency which requires making multiple calls to the model for a given task. With the IDIV-SE approach a single call is sufficient to extract different approaches and their corresponding solutions are obtained from the LLM which are then aggregated.
- A novel take on prompting methods, diversity in prompt hasn't been explored to the best of my knowledge.
- Interesting ablation study on error propagation.
- Paper is very well written, most technical aspects are clearly described.

### Weaknesses
 - The method requires a held out set where different personas and approaches can be tested to pick useful ones. This makes the proposed DIV-SE method somewhat limited in practical applications. CoT prompting on the other hand provide universally applicable prompts, and self-consistency provides a generally applicable framework without needing a held-out set to fine-tune on.

- Results seem mixed: Blocksworld clearly benefits from the diversity in prompting. It is clear on this benchmark that with IDIV-SE more can be achieved in less cost. But on other benchmarks this is not necessarily true e.g. GSM8K (Fig 3 & Fig 4).

- No qualitaitve/quantitative assessment of the synthetically generated demonstrations (using LLMs). For augmented demonstrations - how is the quality of this dataset ensured? I suspect some human annotation to improve the quality of these demonstrations can improve eventual model performance.

- Limited evaluation: Some commonly used reasoning benchmarks are not present, making it hard to compare with prior work like Wang et al's Self Consistency baseline. Arithmetic reasoning: AddSub MultiArith ASDiv SVAMP. Commonsense and symbolic reasoning:  CSQA StrategyQA ARC-e ARC-c Letter Coinflip

- Fig 4 & 5 - For a fair comparison with DIVSE-1 to 5, shouldn't Self Consistency baseline also be given multiple reasoning paths instead of just report SC-1?

- The study could also be extended to other models with smaller sizes e.g. Llama 2 7B variants.
- Difference in effectiveness of DIV-SE could be reported for pre-trained vs chat finetuned/RLHF-ed models.

### Questions
- What does it mean to have a zero shot setting of DIV-SE? Isn't it always atleast one shot as shown in Fig 2? I couldn't find details of how this is done in zero-shot setting. Is the prompt appended with list of approaches but no examples?

- What is the quality of these augmentations? Are they really diverse? Are each of them valid? If yes, are they different from other prompts?

- Sec 2.2 . In practice, for all (persona, approach) combinations, we evaluate the prompt formed using the composition on a held-out set and choose those with the highest performance. This seems like a limitation - for open ended reasoning tasks that could appear in conversational applications, how can this be done outside the benchmarks studied?

- Fig 6 & 8 are referenced in the text but missing in the paper? Did you mean Fig 2?

- Can you explain how different this approach is from self-consistency: I'm not sure if the approach can be described as one bringing diversity in prompting. The diversity is being attempted in the set of approaches taken by the LLM to solve a problem. This is still very similar in spirit to self-consistency - where instead of naively sampling n times, the model is prompted to generate different approaches. The approaches themselves are model generated.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel prompting framework, DIV-SE that ensembles diverse prompts instead of ensembling multiple decoding outputs in self-consistency. The diverse prompts are generated by two steps: 1) instruct an LLM to generate names of approaches or names of personas. 2) generate the rationale for each exemplar and each approach by analogizing to existing CoT examples. It also proposes a cost-effective variant, IDIV-SE, to reduce the cost of multiple inference calls. Compared to self-consistency, DIV-SE and IDIV-SE set up a new Pareto frontier in performance-cost trade-off.

### Strengths
This paper proposes a novel variant of self-ensembling for LLMs, which doesn’t require much prompt engineering and is applicable to many tasks.
The authors experimented with the proposed method on 3 tasks and 4 datasets. The proposed method outperforms self-consistency in performance-cost trade-off on the all datasets except for CommonsenseQA.

### Weaknesses
The methodology part of this paper is not well written. Figure 2 is readable, but Section 2 lacks a clear high-level structure. What are the goals for extracting approaches & personas, augmented demonstrations in the proposed method? Can you describe more details about how you generated the few-shot exemplars for each task? Is it automatically generated by LLM or manually written? If they are automatically generated, what if there are errors in the generated exemplars? Do you need to verify the generated exemplars on a validation set? If you need a validation set for developing this method, it would be not fair to compare it with self-consistency in terms of cost, since self-consistency works out-of-the-box without a validation set.
Merging multiple inference calls into one was first invented and discussed in Batch Prompting[1]. Please cite it and tone down your contribution on this technique.
The paper seems to be written in a rush. Page 5 is badly formatted.

### Questions
Maybe you can put Figure 2 on page 3 instead of page 4?
Section 2.2. “It independently formulates new approaches” -> Is it a hallucination or a feature? It looks like a hallucination to me. If this is important for achieving good performance, can you provide an ablation study based on whether to allow new approaches or not?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
- The authors propose a prompting method to increase the diversity of thoughts. The authors propose a two step solution to generate diverse prompts. First, ask an LLM to generate personas and approaches to solve a task. Next, (in the DIV-SE case), provide few-shot examples using the different approaches in the prompt, and have the LLM generate answers, over which we take a majority vote.
- The authors show a number of cost/accuracy trade off plots for AQUA-RAT, Blocksworld, GSM8K and Commonsense Reasoning. The authors also show results of using various ensemble sizes for DIV-SE.
- The authors examine error propagation in the case of IDIV-SE, and other aggregation strategies beyond a simple majority vote.

### Strengths
- Paper is well written and the method is clear.

### Weaknesses
 - The novelty of the work is very limited. There exists work in which diverse prompts are used to generate diverse reasoning paths: [This paper ](https://arxiv.org/pdf/2206.02336.pdf) should be cited due to its similarity.
- It is not completely clear why DIV-SE works well on Blockworlds and AQUA-RAT, but less so on GSM8K and Commonsense QA.
- IDIV is likely to have significant context length constraints.
- It’s not clear whether adding a persona increases the diversity of output. I suspect the persona does not add much to the method. This requires an ablation.
- The labels on each of the Figures could be clearer. The color codes are missing.

### Questions
- Why are the results for Blockworld 3 in Figure 1 different from the one in Figure 3? Why is the inference cost much lower for DIV-SE-3 and DIV-SE-5 in Figure 3?
- How many trials are the experiments over?
- Can you explain at a high-level why your method is so much stronger on Blocksworld 3 and Blocksworld 4 / 5 compared to the other tasks? Can you provide some outputs of DIV-SE vs. baseline to illustrate?
- Could you clarify what the various colors mean in Figure 1 and Figure 3 (purple, green, blue, orange etc.)?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

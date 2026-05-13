# Planning in Natural Language Improves LLM Search for Code Generation

- Decision: Accept
- Scores: 10, 6, 6

## Abstract
While scaling training compute has led to remarkable improvements in large language models (LLMs), scaling inference compute has not yet yielded analogous gains.
We hypothesize that a core missing component is a lack of diverse LLM outputs, leading to inefficient search due to models repeatedly sampling highly similar, yet incorrect generations.
We empirically demonstrate that this lack of diversity can be mitigated by searching over candidate plans for solving a problem in natural language.
Based on this insight, we propose \method{PlanSearch},
a novel search algorithm which shows strong results across HumanEval+, MBPP+, and LiveCodeBench (a contamination-free benchmark for competitive coding).
\method{PlanSearch} generates a diverse set of observations about the problem and uses these observations to construct plans for solving the problem. By searching over plans in natural language rather than directly over code solutions, \method{PlanSearch} explores a significantly more diverse range of potential solutions compared to baseline search methods.
Using \method{PlanSearch} on top of Claude 3.5 Sonnet achieves a pass@200 of 77.0\% on LiveCodeBench, outperforming both the best pass-rate achieved without any search (pass@1 = 41.4\%) and using standard repeated sampling on top of existing non-search models (pass@200 = 60.6\%).
Finally, we show that, across all models, search algorithms, and benchmarks analyzed, we can accurately predict performance gains from search as a function of the diversity over generated ideas.

## Human Reviews

## Human Reviewer 1

### Rating
10

### Rating Number
10

### Confidence
3

### Summary
This paper investigates the effect of inference-time search in LLMs applied to contemporary coding benchmarks. The investigations start by asking about the appropriate level of abstraction at which to perform search, and identifies "natural language plans" as a useful level through clear experimentation. They introduce a new inference-time search algorithm for LLMs in code generation called "PlanSearch". The algorithm appears general enough to be applied to other domains, though the paper does not pursue this. In the main experiments, the authors find that PlanSearch improves LLM performance on coding benchmarks significantly, and by a large margin compared to standard inference-scaling methods (RepeatedSampling). Further experiments identify "idea diversity" as the key driving factor for PlanSearch's success, with their custom measures of idea diversity being predictive of downstream performance. The authors further discover that instruction-finetuned models can have less diverse ideas than base model variants, raising important questions around the best way to perform LLM post-training.

### Strengths
There were a great many things I liked about this paper, and I learned a lot from its experiments.
- Figure 1 is very compelling and sells the main takeaway immediately: Searching over *ideas* in natural language (PlanSearch) is a significantly more effective way to spend inference-time compute than naive repeated sampling of direct solutions.
- The broad strategy of "generate plan first then generate the solution based on that" is highly applicable to other domains; PlanSearch can be used to generate plans for anything, and could plausibly improve performance across many domains besides code generation.
- Useful takeaway that performance can be seen as a function of diversity of ideas. This is an important lesson for the field which is not currently prioritizing LLMs' diversity of ideas, but should take idea diversity more seriously given this evidence.
- Interesting to see that instruction-tuned models can sacrifice the diversity of ideas present in base models, Figure 30 is a great figure illustrating this effect! This line was quite surprising to me:
  > in many cases, despite instruction tuned models outperforming base models by large margins on a single sample regime (pass@1), this trend disappears—sometimes even reversing—on a multi-sample regime (pass@k). We refer to Figure 30 as an example of this phenomenon

  and this further line in the Conclusion is clear-sighted in pointing out the implication of the problem of losing diversity during post-training:
  > while PLANSEARCH substantially improves diversity over idea space at inference-time, fundamentally, improvements in diversity should also come at the post-training stage
- Section 3 builds a great foundation to motivate why we care about searching over idea sketches: Starts by considering the correct layer of abstraction to search over, run experiments showing the power of the right "idea sketch". Figure 3a and 3b are great.
- Interesting to see that o1-mini, a model which itself already scales inference-time compute, benefits less from this method (which makes sense, but good to know).
- Impressive thoroughness in sharing results, with >40 figures throughout the paper and appendices!

Overall, the paper is very well-written, adds new insights to an emerging topic (diversity and search) with important ramifications for the field, and is very thorough with well-designed experiments, with many interesting results.

### Weaknesses
Few complaints overall. One minor weakness that doesn't cut against the broader claims and lessons of the paper:
- The actual search algorithm of PlanSearch in Section 4.3 feels somewhat arbitrary. If the goal is simply to generate diverse plans, I suspect there will be many other different ways to prompt LLMs to generate diverse ideas besides the specific PlanSearch algorithm as described. Did the authors try other algorithms / prompts? Would have been nice to see the failure cases and understand why this specific design was selected.
  - Ablations in Appendix H address this complaint somewhat, but still assumes the same algorithm structure and is mostly just a "hyperparameter search" which has small effect on the results.
  - To give a concrete example of what I imagine could be a completely different approach: directly prompting models with previously sampled ideas, and asking models to generate different plans.

### Questions
- > Interestingly, we find that IDEASEARCH performs somewhat better, which we speculate comes from differences in splitting solution sketch into two model responses, instead of doing both chain-of-thought and code solution in one model response.

  This is surprising. Is the only difference here that a new model response comes as a new "message" in the chat LLM API?

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
3

### Summary
The authors describe a new method for code generation (for short problems). It involves generating a set of observations about the problem (in natural language), constructing plans to solve it and then generating solutions.

### Strengths
1. The authors achieve impressive results on three benchmarks, e.g. they make Claude 3.5 Sonnet achieves a pass@200 of 77.0% on LiveCodeBench.
2. They provide an interesting motivation for their work: showing that idea generation, not idea execution is the bottleneck of LLMs and they the solutions they generate lack diversity. It's interesting that "a correct sketch is sufficient to produce the correct final solution with relatively high accuracy, even only after 10 tokens of backtranslated solution." and that conditioning on a correct idea or bad idea polarizes the score distribution that much.
3. They provide and elaborate scaffolding for generating solutions.
4. The conducted experiments are sound. I like showing scaling of pass@k as a function of k. I like that all frontier models as well as open-weight models were used in experiments.
5. Results are complemented with an interesting analysis of the role of diversity (Fig. 5)
6. The paper is clearly written

### Weaknesses
1. The authors do not compare with several important baselines, e.g. iterative methods such as ReAct, Reflexion and agentic approaches (e.g. AgentCoder). I thinks that a bit weakness: there are relatively simple methods and scale well to more complex tasks (e.g. SWE-Bench).
2. I don't think it's that surprising or impressive that burning more test-time compute [1, 2, 3] leads to better results. A fair comparison would involve, e.g. a scatter plot of pass@200 on X axis and compute spent on Y axis. Compute spent can be operationalized as either tokens or dollars spent (ideally you'd report both). Then, the question is: is your method strictly optimal? Is it Pareto-optimal? See [1, 2, 3] for a discussion.

More specific points:
3. I think the opening sentence of the abstract is false as of November 2024: "While scaling training compute has led to remarkable improvements in large language models (LLMs), scaling inference compute has not yet yielded analogous gains". See again [1, 2, 3]. 
4. I don't understand this sentence: "LLMs as chatbots, in which models are oftentimes optimized to produce a single correct answer (Rafailov et al., 2024; Ouyang et al., 2022)." RL optimizes for reward (which could be correctness) and DPO optimizes a contrastive loss (e..g. preferring correct responses over incorrect ones). Neither optimizes for a single correct answer. This could be the case for supervised fine-tuning though.

### Questions
See weaknesses

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a new methodology to improve language model test time scaling efficiency. Their study shows that simply sampling more outputs from the same input prompt will have limited diversity, thus limiting the improvement of the model performance. To avoid this issue, they propose to sample the natural language plan of the solution first and then ask the language model to generate a solution based on the plan. They propose an effective method for sampling various plans, and experiments show that the proposed method improved the model accuracy in best-of-n settings.

### Strengths
The paper is well-written. Analysis and ideas are presented progressively, making it easier to follow. The proposed method is well-motivated by the polarized results of different solution sketches. The experiment results also show clear improvement over the baseline model and methods.

### Weaknesses
1. Although the method shows promising results with models including Claude 3.5 sonnet and GPT-4o, etc., the improvement over o1-mini is marginal. Does this suggest the method is not compatible with other inference-time scaling compute?
2. While the proposed method shows promising improvement compared to naive sampling and Pass@1, how does it compare to another search-based method, like MCTS?

### Questions
Please refer to the weakness.

### Soundness
3

### Presentation
3

### Contribution
3

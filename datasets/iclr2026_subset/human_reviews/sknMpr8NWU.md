## Human Reviewer 1

### Summary
The paper proposes Multi-Agent Evolve, a self-improvement framework for large language models (LLMs) using a tri-agent co-evolution setup: Proposer, Solver, and Judge, all instantiated from a single base LLM. The framework uses reinforcement learning with self-generated rewards to improve model performance across reasoning, math, coding, and knowledge tasks without requiring human-annotated data. The authors report improvements over baselines like supervised fine-tuning (SFT) on Qwen2.5-3B-Instruct, with ablations showing the importance of each agent and design choice.

### Strengths
* The idea of using three distinct roles (Proposer, Solver, Judge) co-evolving via RL in a self-play-like setup is novel and extends prior self-play methods to more general domains beyond zero-sum games or verifiable environments.

* The paper addresses the problem of human-curated reward dependence in LLM training, presenting a scalable and domain-agnostic alternative for general-purpose use.

### Weaknesses
* Reward Design is Under-specified: The exact reward functions for the Solver and Judge are not clearly defined. For instance, it is unclear whether the Solver is directly optimized using $V_J(a_i, q)$, and whether the Judge is only trained with the format reward or also receives other signals. This ambiguity hampers reproducibility and understanding.

* Experimental Results Lack Consistency and Explanation: While some benchmarks show improvement, the results are mixed across datasets. For example, MAE(with-ref) performs worse than MAE(no-ref), which is counterintuitive and unexplained. The paper does not provide a convincing hypothesis or analysis for these inconsistencies.

### Questions
1. Clarification of Reward Functions:

   * What is the exact reward function used for the Solver? Is it simply $V_J(a_i, q)$?

   * What is the complete reward for the Judge? Is it only the format reward, or does it include other signals?

2. Definition of Symbols: Please define $\mu_{role}$ and $\sigma_{role}$ in the Task-Relative REINFORCE++ formula.

3. Explanation of Mixed Results:

   * Why does MAE(with-ref) underperform MAE(no-ref) and MAE(half-ref)? This is counterintuitive, as reference data is expected to help. Could you provide a hypothesis or analysis?

   * Why do some datasets (e.g., GSM8K, MATH) show consistent gains while others (e.g., HumanEval+, TruthfulQA) show mixed trends?

4. Computational Cost: How much GPU resource and training time are required for the full training pipeline? Is the method practical for larger models?

5. Formatting and Typographical Issues:

* The abstract is missing a numerical value: "an average improvement of %"

* Please check the quotation marks carefully: for example, "answer-then-refine" in the last line of the first paragraph of Section 4.1, "Unqualified Questions" in the Question Collection paragraph, and the Judging Answers paragraph in Section 4.3.

* Figure 2 caption refers to "Left/Right" but should be "Top/Bottom".

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
2

### Confidence
4

---

## Human Reviewer 2

### Summary
The paper introduces a framework for training multi-agent systems through self-play. The system consists of three LLMs: a proposer, which generates questions; a solver, which attempts to answer them; and a judge, which evaluates both the questions and the corresponding answers. Each component receives rewards that can be leveraged in reinforcement learning to improve the agents’ performance. The approach is implemented using Qwen-2.5 3B and evaluated on multiple datasets.

### Strengths
1. Quantitative improvements across several datasets indicate that the method is promising in terms of training effectiveness.
2. The manuscript is clearly written and easy to follow.

### Weaknesses
I identify several issues with the current version of the manuscript:

1. The main concern is that the framework is evaluated on a single backbone LLM of relatively small size (3B parameters). The observed improvements might simply result from the limited capabilities of Qwen-2.5 3B, which can be enhanced even with noisy training data. How does the method perform with other architectures or larger models? Although it is always possible to include new backbones, I think that for contributions such as this one at least one model with 7-8B parameters is necessary.
2. The novelty of the contribution appears limited. The paper closely resembles MALT (appropriately cited in the manuscript), with the distinction that MALT uses ground-truth data instead of an LLM-as-a-judge and applies DPO for post-training. Architecturally, the contributions are similar, with slightly different roles for the agents. While removing the reliance on ground truth using a judge is an important difference, I remain unconvinced about its necessity (see below).
3. If seed questions are required to bootstrap training, the motivation for replacing the ground truth with a judge seems weak. For such questions, ground-truth answers are typically available, especially in math-oriented tasks, where correct solutions can be computed once the problem is formalized. Why not use them? In the proposed experiments, there is no clear use case demonstrating an advantage of employing a judge over ground truth.

As a minor comment, since no ground truth is used, the method’s performance is inherently limited by that of the judge. This likely explains the use of a much larger network (e.g., a LLaMA 70B variant) to compensate for the shortcomings of Qwen-2.5 3B. What happens if the judge underperforms?

### Questions
1. What happens with other models, and in absence of experiments, why evaluation on Qwen 2.5 3B should be sufficient?
2. Can authors clarify on novelty with respect to MALT?
3. Which is one case in which the judge is better than ground truth, and we do not realistically have ground truth?
4. Are there any collapse due to the judge performance?

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
3

---

## Human Reviewer 3

### Summary
This work proposes a multi-agent evolve (MAE) framework with 3 agents: a proposer, a solver, and a judge. The proposer generates questions that the solver attempts to answer and the judge is used to evaluate that response. In tandem, the 3 agents are given a reward for each example based on the responses from the other agent(s). Notably, the rewards are domain-agnostic and therefore the entire process can be run with little to no human supervision. The authors find that doing so leads to improvement of Qwen2.5-3B-Instruct, highlighting the benefit of their data-efficient method.

### Strengths
* The paper proposes a framework (MAE) where a Proposer agent generates problem instances (possibly grounded on reference) for a Solver agent; this integration and training of a data generator is a little different from mainstream work which pre-generates the data at once; this likely leads to better data/compute efficiency (although it is not measured).
* Empirical results show that using MAE with some references leads to a Solver which is better than SFT on the seed data.
* Additional analyses highlight the importance of both the iterative refinement ability of the Proposer and the importance of a trained Proposer and Judge.

### Weaknesses
The main contribution (of MAE) is not well-situated against simpler baselines. The only baseline compared against is SFT on the seed data (and baseline, no tuning). While half-ref works on held-out sets, it is not a clear winner while with-ref and no-ref perform about the same as without MAE at all. This does not offer a convincing endorsement of using MAE when one would not know when or why to use seed data.

Furthermore, MAE seems to require unnecessary complexity (see below question) over the paradigm of data generation, followed by filtering, followed by solver training.

### Questions
1. L143-145 states that MAE is different because the judge is used for evaluation so it is no longer zero-sum. However, some of the papers cited in this paragraph, like Lin et al., 2025, also have a solver and verifier (judge) framework. Is the self-play in this work different from that?

2. Why is zero-sum self-play (L161) a relevant preliminary?

3. Complexity (related to what was mentioned in Weakness): why must the agents co-evolve? The judge is entirely independent of Proposer and Solver. The Judge is only receiving a format reward, so that can be tuned on the seed data (both problems and solutions). Next, the Proposer is only receiving reward from the Judge, so there could be a separate Proposer<>Judge loop with the same reward as mentioned. Finally, the Proposer can either be 1) used to generate a large dataset en masse (with the Judge acting as a filter) or 2) used in the loop with the Solver, in which the Proposer is now fixed. In 1), that dataset could be even used for a new SFT baseline – it is an expanded dataset of “good” questions as proposed by the judge. I suspect this kind of framework already exists, but even if it doesn’t it is a natural and simpler baseline than having the three agents coevolve but the dependencies be arguably acyclic. 
	* 5.3.2 doesn’t answer this question because we definitely want to train the Judge and Proposer – my point is why does it need to be done together rather than in 3 separate steps?

4. Why does half-ref work better than no-ref or with-ref?

5. Related to 5.3.3 and 5.3.2: in the no-ref and half-ref setting, why do we even need to train a Solver? The Proposer is solving its own question anyway, so how strong is the Proposer on its own - what additional value does the Solver provide?

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
3

---

## Human Reviewer 4

### Summary
The paper proposes Multi-Agent Evolve (MAE), a multi-agent reinforcement learning framework that enables large language models (LLMs) to self-improve without human supervision or external verifiers. MAE instantiates three interacting agents (all derived from the same base LLM): Proposer, Solver, and Judge. These agents co-evolve through a synchronized reinforcement learning loop using Task-Relative REINFORCE++. The Judge provides self-reward signals (quality, difficulty, and format rewards) that guide optimization for all three roles. The authors demonstrate consistent improvements over the base model on Qwen2.5-3B-Instruct across multiple benchmarks (math, coding, reasoning, and general knowledge).

### Strengths
1. The self-evolving multi-agent framework with no verifiable reward or environment feedback and the synchronized parameter update is novel. 

2. The paper is well-written and easy to follow.

### Weaknesses
1. There are only vanilla prompting and SFT baselines, no other multi-agent self-play baselines at all. Hard to understand if this is better or worse than self-play with verifiable rewards.

2. Only one base model (Qwen2.5-3B-Instruct) is used. More models are needed to validate the generalizability of the framework.

3. The failure mode of dataset corruption is only briefly mention in section 5.2 without further explanation of why and how this is solved by improving the prompt or applying format rewards.

4. typo: abstract line 27, no percentage number for improvement.

### Questions
Why SFT is worse than base (even with a large margin) for quite a few datasets in table 1?

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
2
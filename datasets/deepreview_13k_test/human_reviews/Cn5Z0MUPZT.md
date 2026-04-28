# Process Supervision-Guided Policy Optimization for Code Generation

- Decision: Reject
- Scores: 8, 6, 3, 3

## Abstract
Reinforcement learning (RL) with unit test feedback has enhanced large language models’ (LLMs) code generation, but relies on sparse rewards provided only after complete code evaluation, limiting learning efficiency and incremental improvements. When generated code fails all unit tests, no learning signal is received, hindering progress on complex tasks. To address this, we propose a Process Reward Model (PRM) that delivers dense, line-level feedback on code correctness during generation, mimicking human code refinement and providing immediate guidance. We explore various strategies for training PRMs and integrating them into the RL framework, finding that using PRMs both as dense rewards and for value function initialization significantly boosts performance. Our approach increases our in-house LLM’s pass rate from 28.2\% to 29.8\% on LiveCodeBench and from 31.8\% to 35.8\% on our internal benchmark. %Additionally, PRMs enhance code generation in long-horizon scenarios. 
Our experimental results highlight the effectiveness of PRMs in enhancing RL-driven code generation, especially for long-horizon scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces a practical approach for training models with process-oriented feedback for code generation. The approach uses a novel automatic (LLM + unit test -based) data generation process to create a dataset of code with quality labels on every line. The line-by-line labels can be used to trained a Process Reward Model (PRM), which can in turn be used as a dense reward signal for training code models with RL. The approach is shown to outperform the baseline RL-trained code models which are trained on sparse rewards from unit tests. The authors perform careful experiments and ablations to motivate each part of their design.

### Strengths
Nice work overall! I enjoyed reading this and have become more bullish on PRMs as a general research direction after this.
- Very readable and easy to understand.
- Clearly a lot of work was put into it: Devises a novel practical approach for training models with PRMs for code generation, with careful work put into ablations and studying each component.
- Competitive with the SOTA RLTF approach
- Clever method to generate process-level supervision data to train PRMs! The idea of using a best-of-K oracle to label whether each code prefix is feasible or contains unrecoverable errors is a non-obvious but effective way to generate data.
- Section 4.2 and 4.3 were great! Well-reasoned experiments and execution, with great experiment-backed insights on how best to use PRMs in this domain.
  - Particularly appreciated the detail-to-attention uncovering PRM Hacking and implementing mitigations.
  - I like that the main results (Table 1) independently shows the effect of introducing [Value Init], [Dense Reward], and [Value Init + Dense Reward]! Very clear.

### Weaknesses
No clear weaknesses come to mind. There were some choices made which I had different ideas about, but this is not a critique of the work or the claims, so I have put those into the Questions section.

### Questions
- > To ensure that the PRM training data effectively covers the state space the language model may encounter during the next RL training phase, we sample policy models from various stages of the RL baseline training. Specifically, we select 4 checkpoints evenly spaced throughout the RL baseline model’s training process. For each checkpoint, we sample n responses for each coding prompt in the training dataset Dtrain. For each sampled response, we apply the binary search labeling procedure described in Algorithm 1

  For the oracle, is this also using the policy model checkpoints? I see "Our method leverages the model’s own capabilities to generate completions for partial code prefixes and uses automated testing to assess their correctness" which suggests that the policy model itself is used to generate the best-of-K samples. I can appreciate that not requiring a separate oracle model is nice because it is self-contained, but I think this will result in a suboptimal dataset compared to e.g. using a fully-trained RLTF code model as the oracle.

- Reading Section 4.2.2 on RL Training makes me think: Wouldn't a different scheme of data labelling, which labels each line with the "marginal contribution of the line toward success" be more effective than simply rating [0: infeasible, 1: feasible]? Specifically, my intuition is that each added line should improve the success rate of the oracle given K attempts, so my proposed reward is something like "the reward for step M should be the `(success_rate_of_oracle_at_step_M - success_rate_of_oracle_at_step_Mminus1)`". This captures the idea that each line should increase the likelihood of the program succeeding, and naturally avoids reward hacking by simply adding more lines. Of course, this is easier said than done, I expect the process to be noisy, but this formulation for the dataset seems to be better aligned to the true objective.

- (Not a weakness, just a typo) In Section 3.2, I think the authors meant to do citep instead of just cite: "In mathematical domains, LLMs may generate correct answers with faulty reasoning Lightman et al. (2023), making intermediate verification essential" and "While preliminary attempts have been made to incorporate PRMs into RL trainingWang et al. (2024a)"

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes integrating the Process-Reward Model (PRM) that provides line-level rewards into PPO training for single-turn code generation. The authors design a binary search procedure to gather line-level rewards, which is defined as being able to lead to correct code (the authors use best-of-K sampling to approximate it) for PRM training. The authors propose using the PRM as a source of dense reward and/or value function initialization and evaluating the methods' effect on LiveCodeBench and the in-house benchmark using the in-house model.

### Strengths
The contributions of the paper are the following:
1. Adapting the PRM to the PPO pipeline for code generation
2. Details of how the authors design the binary search, collect, and choose PRM training data
3. Empirical results on LiveCodeBench and in-house benchmark show the effectiveness of PRM and analysis to investigate the source of gain

The paper is well-written and easy to follow. It also highlights challenges when incorporating the PRM into the PPO framework (such as reward hacking in Sec 4.3.3). To mitigate reward hacking, it proposes length normalization and neutral labels for comment lines.

### Weaknesses
1. My primary concerns are reproducibility, the lack of experimental details, and data transparency, which hinder the community from reproducing the results presented in the work and accessing the needed efforts. This paper uses an in-house model, and part of the results are reported on the in-house benchmark. This is not inherently an issue but means that there needs to be more details in the text/contributions in other components. Therefore, I encourage the authors to include the following:
-----
#### Description of the In-house model
1. What is the parameter size and architecture? 
2. What is the size of the SFT set, if available (number of tokens/data points) mentioned in L241 and L337? Could the authors show an example of the SFT data? Could the authors provide some basic configuration of the SFT (e.g., lr, number of gradient steps)?

#### PRM data and training
1. Could the authors give some statistics on the different strategies of PRM training data, if available (number of tokens/data points, avg. lines of code, the distribution of the % or the line number where the line-level label turns -1 from +1)? These statistics could be a valuable add-on to Table 2 and the plain strategy. Could the authors show one example of the reward produced by the binary search?

#### PPO training
1. what is the KL penalty (the value of $\beta$ in Eq(3)) used in the exp.? Some basic hyperparams (lr, steps) would be appreciated.
------
2. The proposed PRM data collection requires model checkpoints from RL baseline training (L252). Therefore, the whole pipeline is: RL baseline training -> PRM data generation collection -> PRM training -> RL training w/ PRM. It makes the first RL baseline training mandatory and increases the computation cost. Did the author explore alternatives, such as using a base policy (e.g., in-house-SFT) to conduct PRM data generation and collection?

### Questions
1. On the sensitivity to the $\lambda$: L269 mentions that the authors use different $\lambda$ for correct/incorrect code. I'm curious: Did the author try using the same $\lambda$ or other $\lambda$ during hyperparam sweep? Whether the exp. results deviate much from the ones reported in Table 1?

2. Why the x-axis in Figure 4 could have <1 value as the avg. number of collected response per prompt?

3. L366 says the gain is 5.7% on LiveCodeBench and 12.6% on in-house benchmark relative to the RL baseline. What lines do these numbers correspond to in Table 1? I'm guessing I should be comparing the row of Ours-RL (Dense Reward x, Value Int. x) and the last row. But from Table 1 it's 29.8% - 28.2% = 1.6% and 35.8% - 31.8% = 4%.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper studied using PRM for code generation.

### Strengths
First attempt to use PRM for code LLMs.

### Weaknesses
The current paper delivery is poor, many critical questions is not clearly explained.

Weakness 1: 
The paper discusses using PRM for code generation. But I don't see what specific challenges the proposed method addresses regarding code generation.

The motivation for using PRM in code LLMs (Sec.1 para.2 line 035-043) is that the reward signal is sparse. Sparse reward (or more accurately, the use of bandit feedback) is a common challenge in multi-step reasoning tasks such as math reasoning and code, many research have been conducted to address this challenge, e.g., introducing PRM. 
- If the paper limits its scope to code generation, the paper should clearly explain what are the specific challenges it address regarding the code generation task. I notice that unit test feedback is mentioned as a cause for the sparse reward, but I don't consider it as a particular challenge specific in the code generation task. In its essence, test cases serve as a means of verification of the holistic response -- same in its role as evaluating the correctness of a holistic response using the gold-answer in math reasoning. The natural question is: Is previous methods to deal with sparse rewards in math reasoning directly applicable to code generation? If not, the current paper does not clearly explain this. 
- If the paper targets at proposing new methods for PRM, the paper should clearly state what is new about the methods. 

Based on my current understanding of the paper, the paper answers neither of these.


Weakness 2:
For the current version of this paper, I have doubts on the claimed contributions (line 061)
- From my understanding based on the current paper delivery, the paper only applies previous methods to the code generation task. Reasons detailed as follows:
	- Most importantly, the paper do not clearly explain what additional challenges arise when collecting process supervision for code generation, in contrast to existing works that collect process supervision in reasoning tasks (e.g., OmegaPRM).
	- The paper do not clearly explain how the proposed method differ with previous methods (OmegaPRM), except for the application domain (math versus code). 

         OmegaPRM (https://arxiv.org/pdf/2406.06592) introduces the method of automated process supervision using binary search. The paper mentions in line 147: "Instead, we employ an automated approach inspired by techniques used in recent works", but they do not mention how the proposed method differ with OmegaPRM.
- The paper claims to conduct empirical study of "how to properly and effectively integrate PRMs into RL". I see from section 4.3 that, the paper experiment on using PRM as dense rewards, or/and as Value initialization. Using PRM as dense rewards is studied in MathShepherd (https://arxiv.org/abs/2312.08935). The paper draws a conclusion that using PRM to initialize the value function of PPO does not work, but this paper (https://arxiv.org/abs/2406.03816) explores an effective way to employ PRM for value initialization of PPO. So I don't see valuable contributions in this empirical study. 
- I question the evaluation of the proposed method. There are no results on common benchmarks for code generations, such as APPS, MBPP, HumanEval

### Questions
Better articulate the contributions:
1) What unique challenges arise when applying PRMs to code generation compared to other domains? 
2) How does the approach specifically address these challenges? What are the specific differences between the proposed methods and previous methods that inspire this method?
3) The unique challenges in collecting process supervision for code generation versus mathematical reasoning tasks. A point-by-point comparison of their method with OmegaPRM and other relevant approaches, highlighting any novel aspects specific to code generation. 
4) Analysis of code LLMs trained with the PRM. Any comparisons on how training with/without PRM improve generated code responses. How does the learned PRM generalize? How does PRM help the value estimate during training?
5) Include results on these specific benchmarks (APPS, MBPP, HumanEval) in their evaluation section. If these benchmarks were not used, provide a clear explanation for why they were omitted and how their chosen benchmarks compare in terms of difficulty and relevance.
Discuss how their results on the chosen benchmarks might translate to performance on these more standard benchmarks.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper at hand concerns itself with RL fine-tuning of LLMs from unit test feedback, i.e., obtained in code generation tasks by testing the LLM output against a set of unit tests. The main feature here is the use of a process reward model (PRM) to supply dense rewards at multiple points within a generation (token sequence), rather than just at the end (unit test feedback). While PRMs have been used in several domains before, the key contributions are a recipe to obtain a PRM for code as well as ablations on how to best utilize it during RL fine-tuning.

### Strengths
With direct experience in the paper's domain I found it, for the most part, easy to read and understand. I liked how the paper ablates different parameters for PRM training and usage. The subject of the paper is also of interest within the community as well as for the deployment of code LLMs in products.

### Weaknesses
My main grievance with this paper is that it has very low reproducibility. Models, training data, and evaluation sets are all proprietary; we don't even learn about the size of the models. It does not seem to be a large model, though, indicated by the "lite" name and by the fact that Table 1 only compares to "mini" models from OpenAI and Google. To add to that, a number of crucial details are missing, e.g., hyper-parameters for SFT and RL.

Throughout the paper, the authors claim that their PRM improves exploration. I don't see this claim verified experimentally. Instead, the experiments show better *generalization* to LiveCodeBench and their in-house benchmark, which is not the same. It would be interesting to see if indeed a larger fraction of training problems is solved during training, or whether more diverse solutions are found.

### Questions
In Table 1, you compare "Ours-SFT" against "Ours-RL", but the text in L366/367 refers to it as "RL baseline"? Relatedly, since you train the PRM on data produced during the RLHF phase, does that mean "Ours-RL" numbers are the product of two RL training stages? Where is the model after RLHF then (i.e., the "RL baseline")?

### Soundness
2

### Presentation
3

### Contribution
2

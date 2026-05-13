# Safe Multi-task Pretraining with Constraint Prioritized Decision Transformer

- Decision: Reject
- Scores: 3, 8, 5, 6

## Abstract
Learning a safe policy from offline data without interacting with the environment is crucial for deploying reinforcement learning (RL) policies. Recent approaches leverage transformers to address tasks under various goals, demonstrating a strong generalizability for broad applications. However, these methods either completely overlook safety concerns during policy deployment or simplify safe RL as a dual-objective problem, disregarding the differing priorities between costs and rewards, as well as the additional challenge of multi-task identification caused by cost sparsity. To address these issues, we propose \textbf{S}afe \textbf{M}ulti-t\textbf{a}sk Pretraining with \textbf{Co}nstraint Prioritized Decision \textbf{T}ransformer (SMACOT), which utilizes the Decision Transformer (DT) to accommodate varying safety threshold objectives during policy deployment while ensuring scalability. It introduces a Constraint Prioritized Return-To-Go (CPRTG) token to emphasize cost priorities in the Transformer’s inference process, effectively balancing reward maximization with safety constraints. Additionally, a Constraint Prioritized Prompt Encoder is designed to leverage the sparsity of cost information for task identification. Extensive experiments on the public OSRL dataset demonstrate that SMACOT achieves exceptional safety performance in both single-task and multi-task scenarios, satisfying different safety constraints in over 2x as many environments compared with strong baselines, showcasing its superior safety capability.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes the Safe Multi-task Pretraining with Constraint Prioritized Decision Transformer (SMACOT) for safe offline multi-task reinforcement learning (RL). SMACOT aims to address challenges in safe multi-task RL by using a Constraint Prioritized Return-To-Go (CPRTG) token, which prioritizes safety constraints over reward maximization during training. Additionally, the model employs a Constraint Prioritized Prompt Encoder to aid in task identification using sparse cost information. Experimental results on OSRL tasks reportedly show superior safety performance compared to baselines.

### Strengths
- **Innovative use of transformers in Safe RL**: The paper extends the Constrained Decision Transformer to accommodate safety prioritization in multi-task RL through a novel cost-priorized returns-to-go token and a prompt encoder, similar to the prompt DT structures in unconstrained offline RL settings. 
- **Somewhat clear motivation**: The motivation to prioritize safety constraints and manage cost sparsity issues is well-articulated, which addresses a current challenge in safe RL.

### Weaknesses
Several critical weaknesses significantly limit the contribution, novelty, methodology clarity of this work:

- **Necessity of safety prioritization**: for the Constrained Decision Transformer structure the authors adopted, the action token is essentially conditioned on all the costs, rewards, and states tokens. However, it remains unclear to me what is the specific advantage of this token order: CTG-State-RTG-Action. For example, if the authors want to have a more accurate cost token inputs, why aren't then using other orders like state-CTG-RTG-Action? 
- **Marginal technical contribution over existing work**: The CPRTG and Constraint Prioritized Prompt Encoder for multi-task safe RL seem like minor extensions over established safety-conditioned reinforcement learning methods (e.g., [1, 2]). A comparison with these existing works might be helpful. 
- **Ambiguity for task identification**: the authors mentioned that they remove cost information in the constraint prioritized prompt encoder. However, the authors fail to present any technical details about they can use the cost and distinguish the task merely by the 'input distribution' of state, action, and reward. It seems like the prompt encoder splits the safe and unsafe tokens and still conduct a (reweighted version of) the next token prediction. See questions for more details
- **Unrelated experiment setting**: in research question (2), the authors mentioned they evaluate their approaches in single-agent and multi-agent safe RL tasks. However, the methodology aims to resolve multi-task safe RL instead of multi-agent safe RL. 
- **Unclear experiment contribution**: in the title, the authors mention about safe multi-task pertaining. However, they evaluate the policy transfer results in the experiment as well, and evaluate the difference between training from scratch, FFT and LoRA approaches. However, if the contribution is the CPRTG and prompt encoder in the pretraining phase and still want to show the few-shot adaptivity, they should evaluate the performance of such fine-tuning techniques over other baselines for pertaining as well.


> [1] Yao, Yihang, et al. "Constraint-conditioned policy optimization for versatile safe reinforcement learning." NeurIPS 2023. 
>
> [2] Guo, Zijian, et al., "Temporal Logic Specification-Conditioned Decision Transformer for Offline Safe Reinforcement Learning" ICML 2024.

### Questions
- **About CPRTG**: eventually the output of the model is the action. Is there any difference in the Bayes factorization by ordering CTG, state and RTG one way or another? For example, consider this one-step conditioned generation: 

$$
\begin{aligned}
p(\hat{a}_t, s_t, \hat{C}_t, \hat{R}_t | \{\tau\}\_\{t-1\}) & \propto p(\hat{a}_t |\hat{R}_t,\{\tau\}\_\{t-1\}) p(\hat{R}_t | s_t, \hat{C}_t,\{\tau\}\_\{t-1\}) p(s_t|\hat{C}_t,\{\tau\}\_\{t-1\}) p(\hat{C}_t| \{\tau\}\_\{t-1\})  \\\\
& \propto  p(\hat{a}_t |s_t,\{\tau\}\_\{t-1\}) p(s_t | \hat{R}_t, \hat{C}_t, \{\tau\}\_\{t-1\}) p(\hat{R}_t|\hat{C}_t, \{\tau\}\_\{t-1\}) p(\hat{C}_t|\{\tau\}\_\{t-1\})
\end{aligned}
$$

- **About task identification**: 
  - What is the definition of a task? Is it a cost threshold? Or is it a different morphology of the agent and navigation tasks in OSRL? 
  - How do you identify a task? Is it by a classifier head of the output in the transformer?
  - How do you parameterize the joint distribution of the reward, state and action and use that to identify the task? 

In general, despite a lot of empirical results, the the paper is poorly written and hard to follow. The main points seem to be very ambiguous and keep diverging throughout the paper. I would encourage the authors to rethink their major contribution and significanly revise this paper before it is ready for the top ML conferences.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors propose a new approach called Safe Multi-task Pretraining with Constraint Prioritized Decision Transformer (SMACOT) to address the challenge of learning safe policies from offline data in reinforcement learning (RL). SMACOT uses a transformer-based architecture that can accommodate varying safety threshold objectives and ensure scalability.

### Strengths
The key innovations include:
1. Constraint Prioritized Return-To-Go (CPRTG): a token that emphasizes cost priorities in the inference process, balancing reward maximization with safety constraints.
2. Constraint Prioritized Prompt Encoder: designed to leverage the sparsity of cost information for task identification.
3. As a result, experiments on the public OSRL dataset show that SMACOT achieves exceptional safety performance in both single-task and multi-task scenarios, satisfying different safety constraints in over 2x as many environments compared with strong baselines.

### Weaknesses
1. No mentioning of the work about "Trajectory Transformer" (TT) [1] which is quite similar to Decision Transformer but focuses on the beam-search-based planning as opposed to reward conditioning for DT. The work would be even more solidified if having TT as a baseline.
2. No any ablation / reasoning behind the number $X$ of the samples used to select the $\beta_t$-quantile for $\tilde{R}_t$
3. No any ablation behind the need for the dynamics model $g_i$ in the Section 4.2 for environment-specific encoders.

Additionally, some misprints like "chosose" on Line 237.

[1] Janner, Michael, Qiyang Li, and Sergey Levine. "Offline reinforcement learning as one big sequence modeling problem." Advances in neural information processing systems 34 (2021): 1273-1286.

### Questions
N/A

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
n this work, the authors propose a modified version of decision transformer framework which introduces a constraint prioritized return-to-go token that models the return-to-go token conditioned on the cost-to-go. The proposed framework also utilizes a specialized prompt encoder that helps identify tasks during inference by separately encoding safe and unsafe transitions. This approach introduces an effective method to learn safe RL policies using decision transformers while addressing the conflict between reward maximization and safety constraints. The authors conduct comprehensive evaluations on the OSRL dataset, demonstrating significant improvements over several baseline methods, with their approach achieving safe performance in more than twice as many environments.

### Strengths
- Overall, this paper is well-written. The authors did a great job in describing the multi-task safe RL problem. Also, the authors use figures to illustrate their proposed method
- The authors provided pretty comprehensive empirical evaluation on 26 tasks with thorough ablation studies and clear visualizations demonstrating each component's contribution
- Additional adaptation method such as low-rank adaptation show potential of such pretraining strategy.

### Weaknesses
- It would be great if the authors can provided theoretical analysis for the proposed method. 
- Right now the evaluation seems only focusing on success/failure. The author should consider analysis of the trade-off between safety margin and performance. 
- The transfer learning tasks are still conducted on relatively similar tasks. 
- It seems that there is limited investigation of zero-shot generation performance.

### Questions
Does this pretraining strategy enable decision transformer to demonstrate in-context learning abilities? 
- Have you explored whether SMACOT can adapt to slightly different safety thresholds or constraints without fine-tuning, similar to how large language models can adapt to new tasks through in-context examples?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes SMACOT, a framework for safe reinforcement learning from offline data, addressing both safety and task identification. By introducing a Constraint Prioritized Return-To-Go token, SMACOT balances reward and safety. Experiments on the OSRL dataset show SMACOT’s superior safety performance, meeting safety constraints in over twice as many environments compared to baselines.

### Strengths
1) Well-motivated approach
2) Experimental results are promising
3) Clear and well-structured writing

### Weaknesses
1) The cost constraint functions as a soft constraint, which does not fully guarantee meeting safety requirements.
2) In many cases, the Return-To-Go (RTG) set in Decision Transformer (DT) methods does not align with the actual return achieved, and the same issue applies to cost-to-go. The safty environment may be more sensitive.
3) Time complexity is unkown.

### Questions
1) How to distinguish tasks in unknown environments?
2) Given that the cost constraint functions as a soft constraint, how can it be ensured that safety requirements are fully met?
3) In DT-based framework, how to set proper cost to go?
4) What is the time complexity and the comparison of exact training time with other methods?

### Soundness
2

### Presentation
3

### Contribution
3

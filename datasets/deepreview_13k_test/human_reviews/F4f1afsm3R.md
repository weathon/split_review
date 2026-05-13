# Interpretable Contrastive Monte Carlo Tree Search Reasoning

- Decision: Reject
- Scores: 3, 6, 3, 3, 8

## Abstract
We propose \textbf{(S)}peculative \textbf{(C)}ontrastive \textbf{MCTS}$^\mathbf{*}$: a novel Monte Carlo Tree Search (MCTS) reasoning algorithm for Large Language Models (LLMs), significantly improves both reasoning accuracy and speed. Our motivation comes from: 1. Previous MCTS LLM reasoning works often overlooked its biggest drawback—slower speed compared to CoT; 2. Previous research mainly used MCTS as a tool for LLM reasoning on various tasks with limited quantitative analysis or ablation studies of its components from reasoning interpretability perspective. 3. The reward model is the most crucial component in MCTS, however previous work has rarely conducted in-depth study or improvement of MCTS's reward models. Thus, we conducted extensive ablation studies and quantitative analysis on components of MCTS, revealing the impact of each component on the MCTS reasoning performance of LLMs. Building on this, (i) we designed a highly interpretable reward model based on the principle of contrastive decoding and (ii) achieved an average speed improvement of 51.9\% per node using speculative decoding. Additionally, (iii) we improved UCT node selection strategy and backpropagation used in previous works, resulting in significant performance improvement. We outperformed o1-mini by an average of 17.4\% on the Blocksworld multi-step reasoning dataset using Llama-3.1-70B with \ours.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes speculative contrastive MCTS algorithm. They redefined reward model (using an expert model) in the MCTS based on contrastive decoding. The paper also focus on improving different components of MCTS (e.g., node selection and back propagation) and achieves significant gain.

### Strengths
- I like the overall methodology of reconsidering different components of MCTS and improving them. 
- Achieved empirical performance is impressive, especially compared to o1.

### Weaknesses
- The setup and requirements are not explained well. The introduction focuses on MCTS and its drawbacks but does not clearly explain the authors' goal, objective, and setup. Only in line 148 do they mention that the focus is on using existing LLMs to achieve better reasoning, but this is also not clearly presented. I would appreciate if the goal were explained in the introduction (along with a high-level setup and an example of a known expert). Additionally, in section 3.1, the authors could explain their assumption of access to an expert model.

- In Section 3.3, symbols are not explained. I had to go back and forth multiple times to speculate on the meanings of x_{count, pre}, s^{i}, V, {i}, etc.

- Throughout the paper, the authors kept mentioning a novel reward model, but it only becomes clear on page 5 that the objective is similar to distillation, which aims to mimic the expert. I would have considered adding a few papers focusing on distillation in the related works section. And explaining the setup before hand

- Since the LLM's are stochastic, can you also add uncetainity values across multiple runs in the experiments? That would be helpful.

### Questions
- Around line 241, what is n? and can you also write out JSD formula. Since the paper focus on action-level contrastive decoding and not the token-level decoding, I would expect to theoretically relate L_{CD} and Rewards (JSD, LL, SE) for these two (token level, action level) contrastive decoding. For e.g., with eqn in line 241 you can decompose p(x_i|x_{<i}) = \prod_{j=1}^{i} p(x_{j}|x_{<j}) into token level.  

- line 97, perhaps rephrase with more details. "failed to function from our experiment" does not provide much details/intution

- line 84-90, perhaps rephrase it too. not clear "modes by clustering the prior distribution"

### Soundness
1

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper focuses on improving MCTS as a tool for reasoning in LLMs. The authors introduce a new method, which they call Speculative Contrastive MCTS, that refines previous methods. They create a composite reward model, introducing a method to properly normalize and combine three disparate reward signals. Further, they improve on previous work by modifying the exploration constant in UCT and better tuning the backpropogation method. Finally, they evaluate their model against Chain of Thought and RAP-MCTS (Hao et al 2023) on Blocksworld with various versions of Llama and GPT as the base model.

### Strengths
The authors introduce several improvements to previous MCTS methods, and verify these improvements via an ablation study. In particular, their method of combining three reward signals and adaptively weighting them is interesting and (to my knowledge) novel. They demonstrate a clear improvement on the Blocksworld dataset against RAP-MCTS as well as CoT.

### Weaknesses
**Methodology**
The authors only evaluate their method on the Blocksworld dataset. Showing results on other reasoning datasets such as GSM-8k, even if the experiment is limited in scope, would help show that the method generalizes to different types of tasks. 

The authors could provide more detail as to how they chose hyperparameters, picked the reward clusters, etc. 

In my opinion, the claim that the model is interpretable is not sufficiently motivated. In particular, I do not see how their observations on the distributions of the reward components make the reward more interpretable. 

**Clarity**
There are significant grammatical errors which affect the clarity of the paper, and at some points the meaning of authors’ claims is ambiguous. Of course this is a minor issue as it can be easily fixed.

In the explanation of contrastive decoding, terms x_cont/x_pre and s_EXP/s_AMA are not defined.

### Questions
In the reward model section, it is stated: “Instead of using formal clustering algorithms like k-means, we manually define the regions based on the clear boundaries in the reward’s empirical distribution.” Can you provide more details on how these boundaries were found? 

In section 5.4, how was the constant C found? Would this parameter need to be tuned for new reasoning tasks?

What makes the reward model more interpretable than previous methods? I see how the reward distribution can help evaluate the quality of the reward function, but I am not sure I understand how it can help interpret a particular set of reward values. 

 It is worth noting that the paper has grammatical errors in the first sentences of the abstract and introduction, which should be fixed. 
“We propose (S)peculative (C)ontrastive MCTS∗: a novel Monte Carlo Tree Search (MCTS) reasoning algorithm for Large Language Models (LLMs) [which] significantly improves both reasoning accuracy and speed”
“With the remarkable development of Large Language Models (LLMs), models such as o1 (OpenAI, 2024a) have now gained [a] strong ability [for] multi-step reasoning across complex tasks and [can] solve problems that are more difficult than previous scientific, code, and mathematical problems.”

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This  paper introduces Speculative Contrastive Monte Carlo Tree Search (SC-MCTS*), a novel reasoning algorithm designed to enhance the performance of Large Language Models (LLMs) in multi-step reasoning tasks. The authors aim to address the limitations of previous Monte Carlo Tree Search (MCTS) implementations, such as slower reasoning speed and insufficient analysis of core components, particularly the reward model. SC-MCTS* incorporates a new reward model grounded in contrastive decoding principles, speculative decoding for speed optimization, and refined node selection and back-propagation strategies.

### Strengths
The introduction of a reward model based on contrastive decoding, which emphasizes action-level evaluation, enhances interpretability and robustness.

### Weaknesses
* The impact of the evaluation of intermediate nodes on MCTS performance is significant but not discussed in depth. This oversight may lead to an incomplete understanding of the method's effectiveness.
* The novelty of applying MCTS to planning is somewhat diminished by the fact that this approach is already well-established in the literature. The paper would benefit from a more thorough comparison with existing methodologies to highlight its contributions.

### Questions
1. Could you clarify how planning and reasoning are defined in your framework? What specific characteristics differentiate them?
2. How does separating planning and reasoning lead to improved outcomes in your experiments?
3. The performance of MCTS appears to be influenced by how intermediate nodes are evaluated. Could you provide insights or analysis on this aspect within your methodology?
4. Are there specific scenarios or use cases where your proposed separation provides a distinct advantage over existing integrated approaches?

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
4

### Summary
This paper introduces SC-MCTS* (Speculative Contrastive MCTS), a novel Monte Carlo Tree Search algorithm for LLMs that addresses previous speed and reasoning accuracy limitations. The authors enhance MCTS through three key innovations: a contrastive decoding-based reward model, speculative decoding for 51.9% faster node processing, and improved UCT node selection and backpropagation strategies. Using Llama-3.1-70B, their method achieved a 17.4% performance improvement over o1-mini on the Blocksworld multi-step reasoning dataset.

### Strengths
- Shows significant improvement compared to the baseline
- Accelerates the search process by using speculative decoding

### Weaknesses
- The article is unclear, especially in section 4 where the authors fail to describe how CONTRASTIVE DECODING and SPECULATIVE DECODING are applied in MCTS.
- Using MCTS in LLM reasoning is not a novel approach, as numerous papers have already discussed its application to LLMs. This paper doesn't present any innovative ideas to enhance reasoning capabilities. Although the authors claim speculative decoding as one of their contributions, this inference acceleration paradigm was already mentioned in [1].
- The experimental evaluation is limited to only Blocksworld tasks, without exploring more complex reasoning problems such as MATH and HumanEval (code generation).
- The comparison with baselines is limited, lacking comparisons with other search-based methods like TOT, beam search[2], and Q*[3].

[1]:AlphaZero-Like Tree-Search can Guide Large Language Model Decoding and Training

[2]:Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters

[3]:Q*: Improving Multi-step Reasoning for LLMs with Deliberative Planning

### Questions
- Could you further describe the MCTS process, especially how it integrates with speculative decoding?
- Compared to different search algorithms, particularly heuristic algorithms based on A*, what are the advantages of MCTS?
- The authors need to compare the efficiency and effectiveness (also known as test time scaling law) of different inference time methods to demonstrate how SC-MCTS* better balances the trade-off
- Why does using two models (Expert and Amateur) yield better results in the search context? Perhaps need to further explain where the improvements lie when combining Contrastive Decoding with MCTS compared to using only Expert model for MCTS

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces SC-MCTS∗, a novel enhancement to the Monte Carlo Tree Search algorithm, designed to improve the reasoning capabilities of Large Language Models (LLMs). It combines Contrastive Decoding and Speculative Decoding to not only increase reasoning accuracy but also to significantly reduce the time consumption.

### Strengths
see question

### Weaknesses
see question

### Questions
This paper presents a comprehensive Monte Carlo Tree Search (MCTS) method, SC-MCTS∗, which not only enhances the reasoning accuracy of Large Language Models (LLMs) but also reduces the time required for reasoning. It offers a novel and effective algorithm that significantly boosts both the accuracy and speed of reasoning, as demonstrated through extensive experiments and quantitative analysis. The authors have designed their experiments to include various models and reasoning methods, providing a robust comparison and validation of their proposed SC-MCTS∗ method.

However, a minor shortcoming of the experiments is the absence of performance evaluation on common mathematical test sets, such as GSM8k and MATH. Incorporating these benchmarks would have provided a more comprehensive assessment of the algorithm's generalization capabilities and its effectiveness across different types of reasoning tasks.

### Soundness
3

### Presentation
3

### Contribution
4

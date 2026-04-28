# Earlier Tokens Contribute More: Learning Direct Preference Optimization From Temporal Decay Perspective

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 6, 5, 6

## Abstract
Direct Preference Optimization (DPO) has gained attention as an efficient alternative to reinforcement learning from human feedback (RLHF) for aligning large language models (LLMs) with human preferences. Despite its advantages, DPO suffers from a length bias, generating responses longer than those from the reference model. Existing solutions like SimPO and SamPO address this issue but uniformly treat the contribution of rewards across sequences, overlooking temporal dynamics. To this end, we propose an enhanced preference optimization method that incorporates a temporal decay factor controlled by a gamma parameter. This dynamic weighting mechanism adjusts the influence of each reward based on its position in the sequence, prioritizing earlier tokens that are more critical for alignment. By adaptively focusing on more relevant feedback, our approach mitigates overfitting to less pertinent data and remains responsive to evolving human preferences. Experimental results on several benchmarks show that our approach consistently outperforms vanilla DPO by 5.9-8.8 points on AlpacaEval 2 and 3.3-9.7 points on Arena-Hard across different model architectures and sizes. \revised{Furthermore, additional experiments on mathematical and reasoning benchmarks, such as MMLU, GSM8K, and Math, confirm that our method enhances performance without compromising general capabilities.}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces D2PO (Decay-based Direct Preference Optimization), which aims to mitigate the length bias of DPO through a temporal decay parameter $\gamma$. This follows the principle that the quality of the overall sequence generated can be improved when the earlier tokens are more accurate. The authors show that D2PO outperforms baselines on AlpacaEval2, Arena-Hard and MT-Bench.

### Strengths
1. The authors motivate the problem clearly with the length bias problem of DPO with Figure 1, and showing that earlier tokens are more crucial in alignment settings. Figure 3 motivates the need for temporal decay instead of treating all tokens across a sequence uniformly.
1. Overall it is a complete paper which is well-written and easy to follow. As far as I can tell, the experimental results are also complete with thorough ablations.
1. The comparison between D2PO and the baselines (DPO, SimPO and SamPO) is very clear and I like the details in Figure 2 as well as Table 5 in the Appendix, in addition to the quantitative results.

### Weaknesses
1. Lack of Novelty: the derivation in 3.3 seems like a straightforward extension of Rafailov et, al. (2024) but using discounted return instead of return. 
1. Lack of Theoretical Insight: Intuitively it makes sense that earlier tokens can be more important, and the authors do a good job providing experiments to support this. However, there is no formal motivation (e.g. some theoretical insights under the token MDP setting). The paper lacks a deeper exploration of the implications of the temporal decay, specifically how the choice of decay rate impacts the optimization landscape and convergence properties. It would be beneficial to see a discussion on how the decay parameter interacts with the learning rate and other hyperparameters, and how this interaction affects the stability and efficiency of the training process. Furthermore, the paper does not address the potential for the decay to over-emphasize early tokens, potentially leading to a degradation of later token quality, especially in tasks where long-range dependencies are crucial. This could be particularly problematic in tasks requiring complex reasoning or planning, where later tokens might need to correct or refine earlier decisions.

### Questions
1. In what kind of tasks or settings (e.g. types of datasets) do you think the assumption that earlier tokens are more important may not hold?

### Soundness
3

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
3

### Summary
The paper "Earlier Tokens Contribute More: Learning Direct Preference Optimization from Temporal Decay Perspective" introduces D2PO, a variant of Direct Preference Optimization (DPO) that uses a temporal decay factor to prioritize earlier tokens in model responses. By applying decay to later tokens, D2PO mitigates verbosity bias and aligns responses more closely with human preferences. Empirical results on benchmarks like AlpacaEval 2 and Arena-Hard demonstrate significant performance gains over standard DPO.

### Strengths
1. Innovative temporal decay mechanism that dynamically weights token importance, effectively addressing alignment biases.
2. Demonstrated gains over similar methods in benchmarks like AlpacaEval 2 and Arena-Hard, highlighting the model's capacity to generate concise and relevant responses.
3. Flexible design, capable of operating in both reference-based and reference-free settings.

### Weaknesses
1. Reliance on Instruction-Following Datasets and GPT-4 as the Judge Model: The results in this paper are primarily validated on instruction-following datasets, using GPT-4 as the judge model. These choices raise concerns about generalizability, as instruction-following datasets can introduce noise that may obscure certain aspects of model alignment. Additionally, relying solely on GPT-4’s judgments may bias evaluation outcomes. To ensure robust assessment, further evaluations on alternative, specialized datasets—such as math or logical reasoning datasets—would help verify D2PO's effectiveness in different contexts and task types. This additional testing would strengthen the validity of D2PO's benefits and clarify its performance across a broader range of alignment tasks.

2. Sensitivity to the Gamma Parameter: The performance of D2PO heavily relies on the gamma (γ) parameter, which controls the rate of decay across tokens. While gamma tuning allows flexibility, it may also necessitate extensive fine-tuning to achieve optimal performance across varied tasks. This dependency on precise gamma adjustment could make D2PO less practical in scenarios where rapid adaptation across diverse datasets is required. An exploration of adaptive or task-specific gamma values could improve generalizability and reduce the need for manual tuning.

### Questions
1. Would D2PO’s performance remain consistent on datasets that prioritize logical reasoning or mathematical tasks, where alignment needs may differ from instruction-following datasets?
2. Is there a specific range of gamma values that you would recommend based on your findings, or does it vary significantly across models?
3. Have you considered exploring an adaptive or task-specific gamma parameter to reduce sensitivity and improve D2PO’s generalizability?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a temporal decay mechanism that prioritizes earlier tokens in Direct Preference Optimization (DPO) to improve the alignment of large language models with human preferences. By dynamically adjusting the weights of tokens based on their position, the authors address the length bias seen in existing models, leading to enhanced learning from human feedback. Empirical results demonstrate that this approach outperforms traditional methods like SimPO and SamPO across benchmarks including AlpacaEval and Arena-Hard by large margin.

### Strengths
Presents significant advancements in preference optimization by linking temporal decay concepts to value learning within RL frameworks. 

The authors conduct extensive, controlled experiments comparing their proposed method with a broad spectrum of established baselines, including SimPO, DPO, and KTO.

### Weaknesses
A main bottleneck of the paper is the reliance on automated benchmarks, which can be susceptible to manipulation or "hacking.", see [1]. This raises concerns about the validity of the results, suggesting that human evaluation is neccasary.

Additionally, the empirical results indicate that incorporating length control significantly increases the win rate of the proposed method. This finding suggests that it worth to further compare their approach with works [2] that also focus on length control and its impact on model performance.

### Questions
According to some emprical observation, the gain in autobenchmark could come from length as well as better style control [3]. Have you tried testing on IFEval or gsm8k like tasks?

[3] "https://lmsys.org/blog/2024-08-28-style-control/"

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
Most existing DPO variants assign rewards uniformly across the entire sequence, overlooking temporal dynamics in text generation.
For this purpose, this paper proposes D$^2$PO, an enhanced variant of DPO that incorporates a temporal decay factor, so as to prioritize earlier tokens that can be more critical for RLHF and focus on most relevant feedback.
Experiment results verified the gain of the proposed method over vanilla DPO.

### Strengths
1. The overall direction of token-level reward/credit assignment for RLHF in LMs is promising.
2. Experimental results and ablation studies are comprehensive and generally strong.

### Weaknesses
1. A major concern on this paper is about its contribution/novelty, as it omits several highly relevant related works. For example, the training loss eq. (5) in this paper is (almost) identical to eqs. (8) and (21) in [1]. Furthermore, the idea that earlier tokens can be more important for LMs' generation/alignment/reward optimization (e.g., L21-22, L69-71) has been discussed in [2] (first paragraph of section 3 and appendix F.3). At the minimum level, the authors ought to have a adequate citation and discussion with these prior works. Otherwise, the contribution of this paper is unjustified.

2. Missing evaluation on the OpenLLM benchmark. Does D$^2$PO's improved RLHF come at the cost of general LM ability such as MMLU and/or GSM8K?

3. L253-254: missing citation for maximum entropy RL, such as [3, 4].

### Questions
1. L78-79: why is the more recent feedback potentially outdated?
2. In the derivation of D$^2$PO, how did you cancel the partition function? Note that this is not an issue with the original DPO because it assume a bandit reward so that the partition function depends only on the prompt, which is the same for both chosen and rejected responses. 
3. L211-212: what is the definition of "accuracy"?
4. In eq. (11), should $p_\theta$ be $\pi_\theta$?

### Soundness
3

### Presentation
3

### Contribution
3

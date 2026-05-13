# SimPER: Simple Preference Fine-Tuning without Hyperparameters by Perplexity Optimization

- Decision: Accept
- Scores: 8, 6, 8, 6, 6

## Abstract
Preference optimization has made significant advances in aligning large language models with preference data. However, existing preference optimization objectives require additional hyperparameters that must be extensively manually adjusted to achieve optimal performance, increasing the complexity and time required for fine-tuning large language models. In this paper, we propose a simple
hyperparameter-free preference optimization algorithm for alignment. We observe that we can achieve promising performance simply by optimizing inverse perplexity, which is computed as the inverse of the exponentiated average log-likelihood of the chosen and rejected responses in the preference dataset. The resulting simple learning objective, SimPER, is easy to implement and eliminates the need for expensive hyperparameter tuning and a reference model, making it both learning and memory efficient. We show theoretically that SimPER can avoid overestimation of rejected responses in preference data and is closely related to the total variation distance, encouraging promising mode-seeking behavior for alignment. Extensive experiments on widely used real-world benchmarks: MT-Bench, AlpacaEval 2, and 10 key benchmarks of the Open LLM Leadboard with 5 base models show that SimPER consistently and significantly outperforms existing approaches even without any hyperparameters and the reference model. For instance, despite its simplicity, SimPER outperforms state-of-the-art methods by up to 5.7 points on AlpacaEval 2 and achieves the highest average ranking across 10 benchmarks on the Open LLM Leaderboard. Code for SimPER is publicly available at this link.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposes an effective, hyperparameter-free objective for preference optimization, named SimPER. Comprehensive experiments are conducted on popular benchmarks to verify the effectiveness of SimPER.

### Strengths
- The proposed SimPER training objective is parameter-free, eliminating the need for hyperparameter tuning required in prior work.
    
- The paper provides detailed theoretical analysis and experimental results to demonstrate the superiority of SimPER.

### Weaknesses
I did not observe any significant flaws. However, there is still room for improvement in the details of experimental results.

### Questions
Response length on AlpacaEval 2 is important, so the author(s) may consider adding the average response length to the results. Additionally, as an updated version of MT-Bench, Arena-Hard provides more reliable evaluations compared to MT-Bench and is widely used in previous works of preference optimization. The author(s) might consider including Arena-Hard to better demonstrate performance.

### Soundness
3

### Presentation
3

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
Existing preference optimization techniques often require complex hyperparameter tuning, which complicates the fine-tuning process. In this work, the authors propose a new method for aligning large language models (LLMs) with human preferences. To address this, they propose SimPER, a hyperparameter-free approach that optimizes inverse perplexity—defined as the inverse of the exponentiated average log-likelihood of chosen and rejected responses. They then provide some insights on the reason that the method can work better than other widely adopted methods that SimPER does not push the model away from the chosen responses. They theoretically show that minimizing the proposed loss is approximately minimizing TVD, which is more immune to mode dropping. They validate the method by many commonly adopted benchmarks, and show the method have superior performance without additional hyperparameters.

### Strengths
Hyperparameter tuning has long been a headache in posttraining. SimPER consistently outperforms its alternatives across multiple tasks and datasets without meticulous adjustment of various parameters. This not only is efficient in training, but also enhances the robustness of the model.

In addition to the empirical performance, the authors also provide insights on why such a loss can perform better than its alternatives. 

The proposed loss is fairly easy to implement.  

The proposed method has less length bias.

### Weaknesses
It would be better if the experiments can show the proposed method works well across different scale of models. The majority of the experiments adopts 7-8B models. It would be ideal if we can show usefulness with, e.g., ~3B, ~7B, ~70B models.

In addition, I am confused on the choice of the model. It seems only Fig.4 uses Pythia-2.8B, but all other experiments are with Mistral-7B and/or Llama3-8B? Can you explain why this is the case?

The proposed loss is fairly simple and I do believe simplicity is good. But the presentation of Eq. (5)(6)(7)(8) is redundant. Assuming the notations are well defined (e.g., defined $\log \pi(y|x) = \sum_i \log \pi(y_i|x)$), (8) should be enough.

### Questions
See weaknesses.

In addition, as suggested by Fig. 2, TVD would encourage the appearance of non-existing mode, i.e., it will also encourage the probability of regions with zero/low probabilities in the support of the chosen responses. Do you observe such a behavior in practice? For example, if you substitute the generated samples into a larger (ideally GPT-like) model, do you observe there will be more samples with relatively low perplexity compared to a model trained with SimPO and comparable loss?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors introduced SimPER, a preference optimization technique based on inverse perplexity that eliminates the need for a reference model and hyperparameters. This makes it straightforward to implement and computationally efficient. They demonstrated that SimPER effectively minimizes the Total Variation Distance, which promotes the generation of a subset of high-reward responses (mode-covering behavior) rather than distributing probability equally across all responses. The authors showed that SimPER compares favorably against DPO, IPO, KTO, and SimPO when tested on both pre-trained and instruction-tuned Mistral-7B and LLaMA3-8B models.

### Strengths
- Preference alignment is a timely and impactful area of research.
- The proposed method, SimPER, is well-motivated. It eliminates the need for a reference model and hyperparameters, making it simple to implement and cost-effective, which are significant advantages.
- The experimental setup is sound and modern, incorporating popular and recent LLMs and benchmarks.
- The paper is well-written and easy to follow.

### Weaknesses
 - The authors did not compare SimPER with ORPO [1], another reference model-free preference alignment method.
- Some necessary details and ablations are missing (see Questions).


### Questions
- Can you include ORPO [1] in the experimental setup?
- How sensitive are other preference alignment methods to hyperparameters? Are instruction-tuned models consistently less sensitive to the hyperparameters of the preference alignment methods? (Figure 1)
- What is the training dynamic of DPO mentioned in line 253? (Figure 3)
- How was the reference model incorporated in SimPER in the ablation study? (Table 4)
- Line 72, "post-training process for alignment is usually very expensive", I suggest mentioning the LoRA line of work, which made it significantly less expensive [2, 3].
- Line 201, "data. (Jelinek et al., 1977; Marion et al., 2023; Gonen et al., 2023).", there is a period before the citation.
- Figure 6, I suggest decreasing the opacity as it is difficult to read.

[1] Hong, J., Lee, N., & Thorne, J. (2024). Reference-free monolithic preference optimization with odds ratio. arXiv preprint arXiv:2403.07691.
[2] Hu, E. J., Shen, Y., Wallis, P., Allen-Zhu, Z., Li, Y., Wang, S., ... & Chen, W. (2021). Lora: Low-rank adaptation of large language models. arXiv preprint arXiv:2106.09685.
[3] Dettmers, T., Pagnoni, A., Holtzman, A., & Zettlemoyer, L. (2024). Qlora: Efficient finetuning of quantized llms. Advances in Neural Information Processing Systems, 36.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a simple offline preference optimization objective that eliminates the need for a reference model and any tunable hyperparameters required by previous methods, enhancing LLM alignment performance.

### Strengths
1. The issue of reduced log probability for the chosen response has recently gained considerable attention in the field of LLM alignment. Addressing this issue is a valuable contribution.
2. SimPER reduces the decrease in the likelihood of chosen responses, providing an improvement over SimPO.
3. The experiments are thorough and well-executed, with comprehensive evaluations on both the Open LLM Leaderboard and various chat benchmarks, yielding promising results.

### Weaknesses
1. It appears that Equation (7) might lack an expectation over $x$. If an expectation with respect to $x$ is included, then based on the property $E(A + B) = E(A) + E(B)$, would SimPER’s application extend beyond the paired preference data scenario described in the paper? Specifically, could this formulation be adapted to incorporate comparisons with unpaired alignment algorithms, or even datasets where the preference signal is not derived from pairwise comparisons but from other forms of feedback or scoring mechanisms? The current presentation focuses solely on pairwise preference data, and it is unclear if the method's theoretical underpinnings support a broader application.

2. While Figure 3 shows that SimPER mitigates the reduction in chosen response log probabilities compared to SimPO, the likelihood of the chosen response is still decreasing. This raises questions about the method's ability to truly learn and reinforce the desired behavior. The ORPO paper demonstrates that it is possible to increase the likelihood of the chosen response, suggesting that SimPER might not be fully optimizing the model towards the preferred outputs. It would be valuable to understand why SimPER does not achieve the same level of increase in chosen response likelihood and whether this limitation impacts its overall performance.

3. On Line 295, "model covering" should likely be "model seeking”?

### Questions
See weakness section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a novel loss SimPER for preference learning, which minimizes (resp. maximizes) the perplexity on chosen (resp. rejected) completions and does not introduce any hyper-parameter.
SimPER is applied to align the base and instruct version of Mistral-7B and Llama-3-8B on UltraFeedback and Pythia-2.8B on Anthropic Helpful and Harmless dataset.
The aligned models are evaluated on Open LLM Leaderboard and instruction-following benchmarks AlpacaEval 2 and MT-Bench, where SimPER leads to models with both superior basic capabilities and alignment.

### Strengths
* The paper addresses an important and notorious problem, i.e., sensitivity of alignment algorithms to hyper-parameters.
* In the empirical evaluation, the proposed method achieves significantly higher basic capabilities and alignment.

### Weaknesses
 * If the exponential operation in eq.(8) is removed, the loss degrades into standard fine-tuning that learns the chosen completion and unlearns the rejected completion. It will be beneficial to compare with the standard fine-tuning and elaborate why adding the exponential operation is better.
* I disagree with the analysis on line 249. The authors neglect that the term $w_\theta$ (resp. $d_\theta)$ also depends on $\pi_\theta(y_l|x)$ (resp. $p_\theta(y_l|x))$. For example, in DPO, the weight of $\nabla_\theta\pi_\theta(y_l|x)$ is
$$w=\frac{\beta\sigma(\beta\log\pi_\theta(y_l|x)+C)}{\pi_\theta(y_l|x)}$$
and we have $w\to 0$ when $\pi_\theta(y_l|x)\to 0$. The analysis should consider the interplay of the gradient and its weight, especially when the probability of the rejected response is low.
* My primary concern is whether the proposed method can be scaled to iterative preference learning [1, 2], which is currently employed by the state-of-the-art open-weight models [3, 4]. For instance, implementing iterative DPO on Llama-3-8B-Base can achieve advanced performance on academic benchmarks while scoring 31.3 on AlpacaEval 2 and 8.46 on MT-Bench [5], significantly outperforming offline setting. Conducting such evaluation should be straight-forward given the only difference is the loss term?
* I noticed that the Table 2 is largely copied from [6], which is fine but contradicts with the statement “We thoroughly tuned the hyper parameters for each baseline” on line 371? By the way the MT-Bench score for Llama-3-8B-Base seems was mistakenly duplicated as the result where GPT-4-Turbo serves as the judge.
* Could you please provide the scores for SFT model in Tab. 3 to illustrate the alignment tax?
* Minor: typo in eq. (4) and expression for $d_\theta$ on line 244.

### Questions
- Given that the loss can be decomposed into the terms corresponding to chosen and rejected completions (eq. 7), does SimPER not require the chosen and rejected completions appear in pairs like KTO, making the algorithm more general?

### Soundness
3

### Presentation
3

### Contribution
3

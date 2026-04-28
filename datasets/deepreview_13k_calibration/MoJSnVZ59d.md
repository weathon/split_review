# SafeDPO: A Simple Approach to Direct Preference Optimization with Enhanced Safety

- Decision: Reject
- Avg Score: 6.40
- Scores: 6, 6, 6, 8, 6

## Abstract
As large language models (LLMs) continue to advance and find applications across a growing number of fields, ensuring the safety of LLMs has become increasingly critical. To address safety concerns, recent studies have proposed integrating safety constraints into reinforcement learning from human feedback (RLHF). However, these approaches tend to be complex and often unstable, as they encompass complicated procedures in RLHF along with additional procedures required by the safety constraints. Inspired by direct preference optimization (DPO), we introduce a new algorithm called \textit{SafeDPO}, which is designed to implicitly optimize the safety alignment objective within a single stage of policy learning. The resulting algorithm can be implemented by introducing only one additional hyperparameter, which aims to further enhance safety, along with minor modifications to the DPO implementation. Consequently, SafeDPO successfully eliminates the necessity of fitting a reward and a cost model, as well as sampling from the language model during fine-tuning, while still enhancing the safety of LLMs. Finally, we demonstrate that SafeDPO achieves competitive performance compared to the current state-of-the-art safety alignment algorithm, both in terms of aligning with human preferences and improving safety.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces SafeDPO, an approach for enhancing the safety of LLMs by incorporating safety constraints into the process of reinforcement learning from human feedback (RLHF). The innovation of SafeDPO, compared to existing work like safe RLHF, is its ability to directly consider and optimise safety alignment without the need to train reward and cost models. Empirical evidence comparing SafeDPO against state-of-the-art approaches (Safe RLHF and three DPO variants) demonstrates its ability to minimise the probability of yielding unsafe responses while selecting the most preferable outputs between the set of feasible (safe) outputs.

### Strengths
+ SafeDPO is an interesting approach that aims to address the challenging problem of making LLMs produce outputs that are more closely aligned with human-based safety considerations. There is an increasing body of research investigating this problem, and as such, SafeDPO aims to contribute in this direction. 

+ Good set of experiments using state-of-the-art approaches and building on the experimental setup utilised in existing research.

### Weaknesses
 - The work, albeit interesting, appears incremental compared to Safe RLHF and the other SoTA research it is compared against, with the improvements being marginal. Please be explicit about the innovations compared to Safe RLHF and DAAs (Rafailov et al., 2024a).

- A key statement underpinning SafeDPO is that it is efficient in terms of computational time, memory usage, and data requirements. However, no evidence is provided to corroborate this statement. This is a major limitation, and the authors should either provide evidence (e.g., complexity analysis, efficiency improvement, training time, memory usage) compared to the baselines they compared their work against or revise their statements accordingly.

- The 'mildness' of the assumptions underpinning the core of SafeDPO (especially the statements underpinning Propositions 3.1 and 3.3) is not articulated convincingly, and the authors are encouraged to revisit these points.

### Questions
(Q1) It is reported that the intractable distribution is replaced by a tractable distribution without *theoretically* introducing any bias (Section 3.2). This is a key part of the theoretical framework underpinning SafeDPO. Could you please elaborate on the correctness of the above statement, as it is not entirely clear how this was achieved based on the information provided in this section? 

(Q2) In several places throughout the paper (including the main contributions), you report that SafeDPO is efficient in computation time, memory usage, and data requirements. Unless I have missed this information in the main paper or the Appendix, I cannot see any evidence corroborating these claims. Could you please provide some details that would enable developing an understanding of the foundation for these improvements yielded by SafeDPO?

(Q3) Propositions 3.1 and 3.3 are founded on "mild assumptions". Although the proofs are provided in Appendices A.1 and A.3, could you please clarify the statement on the assumptions underpinning these propositions and provide a justification why these assumptions are considered mild?

(Q4) The impact of hyperparameter Δ in Equation (17) is briefly illustrated through the experiments presented in Section 5. Please elaborate on what this means from a practical perspective and how the Δ value could be calibrated or selected depending on the considered task.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes SafeDPO, a safety alignment fine-tuning algorithm for LLMs that aims to reduce time and memory overhead from SafeRLHF. RLHF fine-tuning uses a pair of human-labeled (more preferred vs. less preferred) outputs to fine-tune LLM. It is complex because it takes extra efforts to fit a reward and a cost model, while DAA reduces complexity by fitting the LLM policy end-to-end. SotA RLHF algorithms have already been used in solving the safety alignment problem (SafeRLHF), and the goal of SafeDPO is to find a DAA version of solution. The trick here is to set reward to negative infinity for unsafe responses (cost < 0) as in Equation 10. On top of this reward definition, the authors show a way to construct the supervised learning dataset, by swapping the more preferred and less preferred LLM outputs based if the more preferred one is considered more harmful. Furthermore, an additional offset into the loss function is introduced, as a multiplier to the difference between the harmfulness of the two outputs.

### Strengths
1. The motivation is good: to reduce computational complexity in RLHF-based safety alignment.

### Weaknesses
1. The contribution seems incremental.
(1) Section 3.1 only provides a piecewise reward function, by setting all harmful responses with negative infinity reward.
(2) Section 3.2 provides a swap of more preferred vs. less preferred labels based on harmfulness to preprocess training data, which confuses me (see my point 3 below).
(3) Section 3.3 adds an additional fine-tuning hyperparameter \Delta, but the effect is trivial. As shown in Fig 4, large \Delta has approximately the same harmless ratio as no \Delta (\Delta = 0), and helpfulness even degenerates as \Delta increases. Introducing this hyperparameter seems to have a negative effect according to the experiment results.

2. In Equation 10, where does r(x, y) and c(x, y) come from? Are they obtained the same way as in other DAA methods, such as DPO?

3. In Proposition 3.2, the term "... can be regarded as sampled from ..." is a confusing expression. I do not get what does it mean.

4. The major contribution claimed by this paper is the computational complexity reduction from RLHF baselines, but there is no experimental complexity comparison or analysis.

5. The presentation is hard to follow because too many notations are used.

### Questions
Please see weaknesses. If they are addressed properly, I am willing to raise my score.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper tries to address an important problem regarding the safety genearation of Large Language Model. This paper proposed a novel alignment method called SafeDPO that is stable and efficient. The paper also demenstrates theotical analysis to show the safety alignment objective can be achieved with a single optimization objective. The experiments conducted by the authors show the effectiveness of the proposed SafeDPO by outperforming current baselines.

### Strengths
1. This work introduces a novel approach by proving that the LLM safety alignment objective can be achieved with a single optimization objective under mild assumptions. The rigorous and sound proof provided in the Appendix further validates this approach.
2. This work only requires a single-stage training compared to previous methods that might need training during muliple stages such as training reward and cost model or iteratively optimizing the objective. 
3. I think the offset $\Delta$ that added to the objective function is novel.

### Weaknesses
1. Although the authors state that their method is efficient in times, sample usage and memory usage, I did not find any comparsion between existing methods and proposed SafeDPO to support this argument. It would help to include any training time comparisons, memory usage measurements, or sample efficiency metrics compared to baseline methods.
2. The experient results only report average performance in Figure 2, could the author include std here to show each method's stableness? For example, adding error bars to FIgure 2.
3. Minor Issue: I think the related work section should move ahead.

### Questions
1. As metioned in Weakness 2. Could the author give both avg and std statistics of their results?
2. From my understanding, the authors prevents the LLM generating unsafe responses by setting the reward to -$\infty$. Could this also be achieved by Multi-objective DPO[1] that has two objectives for maxmizing reward $r(x,y)$ and let the cost $c(x,y)$ less than 0. Ideally, can the author compare their methods with [1]. I understand due to the limited time, it might not feasible to train a new model to compare but can the author offers some insights and compare Multi-objective DPO to the proposed method such as a theoretical comparison or discussion of the similarities and differences between SafeDPO and Multi-objective DPO

[1] Beyond One-Preference-Fits-All Alignment: Multi-Objective Direct Preference Optimization. (https://arxiv.org/abs/2310.03708)

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work proposes an algorithm to align LLM in the safety constrained setting. The proposed algorithm utilizes the safety indicators in the annotated datasets; and avoids helpfulness or safety modeling. 

On the testing set of SafeRLHF-30K, this works demonstrates that it outperforms previous baselines, obtaining a better trade-off between helpfulness and harmfulness.

### Strengths
- Comparing to previous works, this work avoids helpful or safety reward modeling. Therefore, this work is more computationally efficient.
- While previous works focus on utilizing the harmless preference annotation, this work utilizes the safety indicators. This is novel.
- In the experiment section, this work demonstrates that it denominates the SOTA method PPO-$\lambda$ in both model-based and GPT-4 based evaluation.

### Weaknesses
 - The GPT-4 model evaluation from the original Safe-RLHF paper[1] (**Evaluation Datasets** in section 4.1). It would be good to have a consistent evaluation sets so that the comparison between PPO-$\\lambda$ and the proposed method is fair and straightforward. I would recommend the authors to conduct evaluation on the dataset as in [1]; or provide an explanation for why a different dataset was chosen and how it compares to the one used in [1].

- The helpfulness score of DPO-HELPFUL is lower than the rest, which is not intuitive and different from other works like [2]. This raises another concern about whether DPO baselines are fully and appropriately trained. Some analysis or explanation of the current results would be helpful.

### Questions
- Could you provide un-normalized model-based helpfulness and harmless scores? In this way, it would be more convenient to compare with he original results in [1].

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduced SafeDPO which is a variation of DPO. It implemented an additional hyperparameter and used a maximum likelihood estimation with helpfulness preferences and safety indicator to eliminate the explicit training process of reward and cost models in the safe RLHF approach. The paper has shown good results via theoretical analysis and experiments. It also addressed the practical issue of samples needed via a small modification of the algorithm.

### Strengths
Overall, this is a novel, well-written paper which covers both the theoretical aspect and the empirical aspect. While the modifications are fairly minor compared to the original algorithms of DPO and safe RLHF, overall it has created a new algorithm with good implication in practice and can help further address safety issues in LLMs. The paper is presented logically and well-supported by theoretical analysis and experimental results - although some of the propositions are under mild assumptions, it is acceptable within the framework of the algorithm and within the scope of the paper.

### Weaknesses
The paper does not have any notable weaknesses. A mild observation is that using the 2 evaluation methods (using the beaver-7b-unified cost and reward models vs GPT-4), the conclusion seems to vary a lot regarding helpfulness - although they are consistent regarding harmlessness. Furthermore, the analysis might be more comprehensive if the paper delves a bit more into the model performance/helpfulness vs safety/harmlessness within subsets/categories of the dataset (which seems to be a subset of BEAVERTAILS which has 14 potential harm categories).

### Questions
* Why does the definition of the harmless ratio differ between model-based evaluation and GPT4 evaluation?
* The results regarding helpfulness seems to differ a lot between these two evaluation methods, could you elaborate on why this might be the case please? (for GPT4 evaluation, safe DPO and PPO-$\lambda$ have highest helpfulness but only ranked medium in model-based evaluation)
* Do you have any further analysis of the model helpfulness vs harmlessness across the harm categories as defined by the PKU-SafeRLHF-30K dataset?

### Soundness
3

### Presentation
3

### Contribution
3

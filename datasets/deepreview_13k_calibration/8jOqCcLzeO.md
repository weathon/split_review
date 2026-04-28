# Longhorn: State Space Models are Amortized Online Learners

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Modern large language models are built on the straightforward principle of sequence modeling via next-token prediction.
While the Transformer remains the dominant architecture for sequence modeling, its quadratic decoding complexity with respect to sequence length poses a major limitation. State-space models (SSMs) present a compelling alternative, offering linear decoding efficiency \DIFdelbegin \DIFdel{and high }\DIFdelend \DIFaddbegin \DIFadd{while maintaining }\DIFaddend parallelism during training. However, many existing SSMs rely on linear recurrence designs that appear somewhat ad hoc.
In this work, we explore SSM design through the lens of online learning, conceptualizing SSMs as meta-modules for specific online learning problems. This approach links SSM design to formulating precise online learning objectives, with state transition rules derived from optimizing these objectives.
Based on this insight, we introduce a novel deep SSM architecture based on the implicit update for optimizing an online regression objective. Our experimental results show that our models outperform state-of-the-art SSMs, including the Mamba model, on standard sequence modeling benchmarks and language modeling tasks.

\begin{figure}[h!]
    \centering
    \DIFdelbeginFL %DIFDELCMD < \includegraphics[width=0.75\linewidth]{figures/validation_ppl.pdf}
\DIFdelendFL \DIFaddbeginFL \includegraphics[width=0.8\linewidth]{figures/validation_ppl.pdf}
    \captionsetup{width=0.8\linewidth}
    \DIFaddendFL \caption{\textbf{(left)} The average perplexity on eight downstream datasets for GLA, Mamba\DIFaddbeginFL \DIFaddFL{, }\DIFaddendFL and \ours{} (1.3B model) over seen tokens on SlimPajama. \ours{} leads to a 1.8x speed up in sampling efficiency. \textbf{(right)} \ours{}, pretrained with 2048 context length, extrapolates up to 16x longer context at inference.}
    \label{fig:fig1}
\end{figure}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
Longhorn formulates state-space models by solving an online regression problem. By designing various online learning objectives, it can induce different linear recurrent models, providing a unified framework and principled approach for developing new models. This work adopts an objective that encourages the hidden state to remain close to its previous state (i.e., \( ||S_{t+1} - S_t||_F \)) and includes a term that promotes key-input association (i.e., \( ||S k_t - x_t||_{\text{diag}(\beta_t)^2} \)). While the optimal solution is derived, it presents computational challenges. To address this, a diagonal approximation is used, resulting in a model computationally similar to Mamba (and thus similarly efficient) but with improved empirical performance, as demonstrated on synthetic datasets and medium-scale language modeling and image modeling.

### Strengths
1. The paper is well-written and easy to follow. 
2. The formulation via online learning for solving in-context associative recall is interesting and elegant. It explains why Longhorn (and also DeltaNet) performs well in MQAR tasks.
3. Empirical results look good.

### Weaknesses
1. The main issue with this work is that the implementation does not fully align with the theory. Using a diagonal matrix to approximate an “identity-plus-low-rank” dense matrix is coarse, and it’s unclear if the theoretical advantage translates to this setting.
2. In Eq5, the norm \(\text{diag}(\beta_t)\) appears unusual and is not well-motivated or empirically validated. Why is a vector-valued \(\epsilon\) necessary? If not, the DeltaNet structure could leverage the kernel from Yang et al. (2024, https://arxiv.org/abs/2406.06484), which would easily scale up the head dimension and likely benefit recall-intensive tasks requiring a large state size. Longhorn, as it stands, cannot be expressed in matmul form, leading to similar challenges as in Mamba. Would Mamba2-like optimization, potentially resulting in a DeltaNet-like model with scalar \(\epsilon\), be preferable?
3. MQAR is a synthetic dataset and insufficient to demonstrate Longhorn’s advantages in recall-intensive tasks. Results on real-world recall-intensive tasks proposed in Arora 2024 [https://arxiv.org/abs/2402.18668] would provide a stronger case. Could you report zero-shot accuracy on these tasks? A table similar to [Table 1, https://arxiv.org/abs/2407.05483] would be very useful and necessary.
4.  This work lacks several ablation studies. For instance, the "value" projection is removed compared to standard models, yet this change is not analyzed. Additionally, the model does not clarify the benefits of parameter tying.

### Questions
Are there any actual wall-time comparisons in terms of training & inference?

### Soundness
3

### Presentation
4

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
This paper introduces Longhorn, a new state-space model (SSM) architecture. By adopting an online learning optimization perspective, the authors unify several popular SSM architectures, bringing clarity to the structural differences between them. The explanation in Appendix A and Table 4 are especially helpful for understanding these nuances. Building on this unified approach, the authors propose a simplified SSM structure through a novel value retrieval mechanism based on key structures, offering insightful explanations of their method. The paper concludes by deriving a closed-form update formula for the state S in the SSM, supported by effective empirical results.

### Strengths
1. The paper is well-written and easy to follow. The clarity of explanation makes complex ideas accessible, particularly in sections like Appendices A and B, which provide valuable insights into the nuances of different approaches.
2. The novelty of the new formulation for the Longhorn approach is impressive. The retrieval-based perspective is both innovative and elegantly presented, offering a fresh solution that enhances the field.
3. The exploration of SSM structure variances through online learning optimization is also intriguing and adds depth to the paper’s contribution.

### Weaknesses
1. While this paper presents a focused study on architecture, the data and model scale seem limited. The experiments are primarily conducted on relatively small datasets and models, which raises questions about the generalizability of the findings to larger, more complex scenarios. Specifically, the absence of experiments on datasets exceeding 100B tokens and models larger than 1B parameters limits the conclusions that can be drawn about the scalability of the proposed Longhorn architecture.
2. The reduction in perplexity compared to Mamba is notable. However, the results in Table 2 appear mixed, with some downstream tasks showing only marginal improvements or even decreases in performance. This inconsistency across different tasks makes it difficult to ascertain the true benefits of the proposed architecture. A more detailed analysis of why certain tasks show improvements while others do not is needed to fully understand the model's capabilities and limitations.
3. Including additional experiments, such as MMLU, GSM-8K, and more extensive long-context benchmarks, would strengthen the findings and provide a more robust evaluation of the model's capabilities. The current evaluation lacks a comprehensive assessment of the model's ability to handle diverse tasks, especially those requiring reasoning and long-range dependencies. The absence of these benchmarks makes it difficult to compare the proposed model with existing state-of-the-art models in a broader context.

### Questions
see weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces Longhorn, a novel state-space model (SSM) architecture designed as a meta-module that effectively handles sequence modeling problems. It described a theoretical framework based on online learning principles to derive the closed-form solutions for the online associative recall problem. 

The empirical results convincingly demonstrate that Longhorn surpasses other state-of-the-art SSMs in performance, particularly highlighted by its impressive recall capabilities on the Multi-Query Associative Recall (MQAR) benchmark.

### Strengths
- the online learning framework provides a fair theoretical underpinning for understanding the Linear attention model / SSMs. This approach not only supports the conceptual innovations presented but also enhances the interpretability of SSM behaviors in practical applications.

- emirpical results: Longhorn has good sample efficiency compared to STOA models such as Mamba and GLA. This advantage is critical in scenarios where computational resources are limited.

### Weaknesses
Appoximation: while the diagonal approximation is a key aspect of Longhorn's implementation, its impact on the theoretical framework's alignment with empirical results remains unclear to me. I would expect a deeper exploration into how this approximation influences model performance could bridge the gap between theoretical predictions and observed outcomes.

### Questions
1. can you provide more details on the sample efficiency experiments? Say, what kinds of hyper-parameters did you try? Can you do an abaltion study? 

2. Echoing the weakness of the paper, it is unclear to me that after using such an appoximation, is the theory framework still well aligned to the experiments?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a novel perspective on SSM models through the lens of online learning, offering a fresh analytical framework. The learning process consists of two losses: one ensuring minimal state updates, and another optimizing the reconstruction of current x from the state using key k. Within this framework, the authors propose Longhorn, which introduces differential importance weighting for various dimensions during reconstruction. Experimental results across different scales, tasks, and sequence lengths demonstrate Longhorn's superior compression rate on PassKey tasks and better length generalization, while maintaining comparable performance with baseline SSMs on other tasks. While the theoretical framework shows significant value, the paper makes an approximation step without thoroughly discussing its impact on the overall theory, which intuitively could lead to substantial differences.

### Strengths
- Novel theoretical perspective analyzing SSMs through online learning
- Proposed theoretical framework shows strong potential for length generalization
- Comprehensive empirical validation across various settings

### Weaknesses
 - Insufficient discussion of the approximation's impact, creating a gap between theory and practice
- Limited comparison with contemporary methods (e.g., Mamba2 and DeltaNet); given the concurrent timing with DeltaNet, would appreciate author response on this comparison

### Questions
- There appears to be a discrepancy between the significant improvements in PPL versus the modest gains in downstream task metrics. Could the authors elaborate on this phenomenon?
- Could the authors provide analysis on why DeltaNet struggles with extrapolation, while Longhorn demonstrates superior extrapolation capabilities, especially given their similarities in the update equation?
- Is there an ablation study on the beta parameters in the OCP formula? What guidelines exist for its optimal selection?

### Soundness
2

### Presentation
3

### Contribution
2

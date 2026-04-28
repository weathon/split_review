# Mutual-Inform SMoE: Improving Routing Stability via Probabilistic Graphical Model

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 5, 5, 8

## Abstract
Sparse Mixture of Experts (SMoE) has emerged as a breakthrough approach for achieving unprecedented scalability in deep learning. By enabling models to expand their parameter count exponentially while selectively activating only a small subset of parameters per sample, SMoEs maintain high efficiency. However, SMoE models are susceptible to routing fluctuations, leading to instability and non-robustness. In this work, we unveils SMoE-based attention as a point estimate of a regression function of a 3-layer hierarchical mixture of experts regression. Through this probabilistic graphical model (PGM) framework, we highlight the conditional independence in expert-selection process of tokens, which exposes the model to routing fluctuation and non-robustness. Motivating by this PGM framework, we propose Mutual-Inform SMoEs, including Similarity and Attention-Inform SMoE, which eliminate the assumption of conditional independence by allowing tokens to directly influence each other on expert-decisions. We theoretically demonstrate that our methods lower the entropy in decision-making, enabling more confident and consistent expert assignments. Finally, we empirically validate our models on ImageNet classification and Wikitext-103 language modeling, showing significant improvements in reducing routing fluctuations, enhancing performance, and increasing model robustness compared to baseline Transformer-SMoE models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper formalized the transformer attention head as a probabilistic graph model and suggested that independent expert selections for different tokens in Sparse MoE contributes to the routing fluctuations. Based on such analyses, the authors proposed two intuitive approaches of aggregating other tokens' expert selections into the decision of the current token with either similarity between output features or adapted attention scores as the weights. Experiments in the paper demonstrated that such techniques could bring the improvements in terms of model performance and routing stability.

### Strengths
The structure of the paper is well-organized and comprehensive. The paper clearly identified the potential issues behind routing fluctuations at start and formed two solutions step by step.

### Weaknesses
1. The paper's writing did not fully meet the standard of a professional research publication .
- Lack of rigorous and concise formula definitions although the authors tried to analyze the problems in a formal way.
**a**. Diverse meanings of the same subscript in different formula. In Line 75-77, the subscript should be $k$ rather than $i$. It is not appropriate to use $i$ in line 87. Please do not confuse these two index symbols and try to keep one index have a unique meaning
**b**. Some notations lack explanations. What does the $f$ in Eq. (3) mean? What does $\hat{E}$ in Figure 1 mean? In Eq. (1), A and V should have subscripts. Also, the distribution whose mean is calculated should be listed under $E$ in Eq. (5) & (8).
**c**. Some equations have errors. In line 87-93, It would be better if the renormalization operation is taken over M rather than N. Namely, the denominator in Line should be the sum of M items since the remaining (K-M) scores are $-\infty$. In Eq. (4), "| X=X".
**d**. For some conventional definitions like the meaning of P(A) and E(A) in line 152-153, it is not necessary to point out them in the main text.
**e**. Putting lots of formulas/notations into the paper sometimes makes the content hard to follow if there is not enough illustrations and explanations. For example, Figure 1 is hard to parse without any captions about the definitions of symbols. It could be companied with graph illustrations of attention blocks or Sparse MoE.
- Redundant text. The preliminary and approach sections are redundant.  In Sec 1.2., there is no need to put too many words to explain the commonly-known fact that selecting top M values to calculate softmax is equivalent to the normalization over top M values after softmax. and I am not convinced that this explanation is necessary for further analyzes.  The explanations of two context-dependent expert selection methods could be condensed. The paper should be delivered in a concise way with compact information.
- Some typos. In line 20,  "Motivated by" not "Motivating by". In line 166, it should be "Considering". In line 255, 261, 267, there are some indexes (5, 6, 7) coming from nowhere. In line 290, it should be "similar to". In 128-129 “is as” and a misplaced comma seems confusing to me.
- Others. The EMPIRICAL ANALYSIS and EXPERIMENTAL RESULTS could be merged rather than set apart.


2. The novelty of the paper is questionable. There is lack of sufficient literature review. The papers listed in the related sections seem to be "out-of-date", i.e. published two years ago and the proposed methods were compared against a limited set of long time-established baselines. Although it is interesting to see that the authors fit the MoE into PGM framework, the proposed "attention-like" aggregation techniques are still quite simple and straightforward, making me question the necessity of using this complicated PGM framework.

3. Experiments. In Figure 2, the entropy curve for the baseline is missing in the right plot, and the dynamics of fluctuation values across different layers should be analyzed.

### Questions
See the above weaknesses part.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes "MUTUAL-INFORM SMOEs", MoEs with a tweaked routing mechanism that allows for information sharing between routed tokens. The authors motivate their proposed method as a solution to reducing the routing fluctuation problem in MoEs. They provide theoretical justification for their method's reduction in routing fluctuation by showing that the entropy of routing decisions of "MUTUAL-INFORM SMOEs" is upper bounded by standard topK + softmax routing. The authors provide additional experiments on language modeling (standard + adversarially perturbed text) and image classification, showing that their method outperforms a standard topK + softmax baseline in routing fluctuation and validation perplexity.

### Strengths
- The Attention-Inform (S)MoE and Similarity-Inform (S)MoE routing functions are novel and potentially interesting to the community. The introduction of routing mechanisms that can share information between tokens can lead to better-performing MoEs.
- It is nice to see the theoretical justification for the proposed method.
- I like the idea of including an adversarial test set. 
- Providing code for the method is appreciated and helps validate the results.

### Weaknesses
My **main concern** is the lack of comparison to previous work that also improves the *routing fluctuation* problem of MoEs. Authors cite [1,2] numerous times when referring to the routing fluctuation problem. However, they do not provide a comparison to Stablemoe or X-MoE. To the best of my knowledge, [1,2] are the only works that claim this *routing fluctuation* problem exists in MoEs and to provide a solution for it. As clear follow-up work to [1,2], both more than two years old, it is very important to directly compare to their method. Adding a comparison to these methods would greatly strengthen the contributions of the work.

**Other concerns** 
- The method relies on the attention matrix for similarity scores between different tokens. How does this influence the computational and memory complexity of an MoE forward pass? Providing figures that show the timings with respect to a baseline would address this concern. Specifically, it is unclear if the computation of the similarity scores adds significant overhead, especially with longer sequences, and how this scales with the number of tokens and attention heads.
- The introduction is structured unconventionally and I found myself taking time to find the motivation for the work.
- It would be helpful to understand how the performance of M-I SMoE changes as the number of experts is increased, the granularity of the experts changes, and the number of active parameters changes. For example, it is not clear how the method behaves with a larger number of experts or if there is a point of diminishing returns. Also, the impact of varying the number of top-k experts utilized during routing should be explored.
- The architecture of the MoEs used (e.g., number of experts per layer) should be reported in the main text, not only in the appendix.
- I am unable to find the dimensions of the transformer used in the language modeling experiments.


Typos:
- "Motivating by this PGM framework" Motivating --> Motivated
- Page 10: "We leave it for future work. We leave it for future work"

### Questions
- Is routing fluctuation discussed as a problem for MoEs outside of papers [1,2]?


[1] Stablemoe: Stable routing strategy for mixture of experts ( https://aclanthology.org/2022.acl-long.489/ )
[2] On the Representation Collapse of Sparse Mixture of Experts ( https://arxiv.org/pdf/2204.09179 )

### Soundness
2

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
This paper proposes a novel perspective on Sparse Mixture of Experts (SMoE) through a probabilistic graphical model (PGM) framework. The authors identify that the conditional independence in expert selection for tokens leads to routing fluctuations and model instability. To address this, they introduce Mutual-Inform SMoE with two variants: Similarity-Inform and Attention-Inform, which allow tokens to influence each other's expert assignments based on their similarities or attention patterns. They provide theoretical analysis showing their method reduces entropy in routing decisions and demonstrate empirical improvements on ImageNet classification and WikiText-103 language modeling tasks.

### Strengths
1. The paper provides a novel theoretical foundation for understanding SMoE through PGM, offering valuable insights into the routing fluctuation problem and presenting a well-grounded solution. The mathematical derivations and proofs are rigorous and well-presented.

2. The proposed solution is elegant and practical, requiring minimal additional computational overhead while showing significant improvements in both performance and stability. The two variants (Similarity-Inform and Attention-Inform) provide flexibility in implementation.

3. The experimental evaluation is comprehensive, covering both vision and language tasks, with thorough analysis of routing stability, entropy reduction, and robustness against various types of perturbations.

### Weaknesses
1. While the paper demonstrates improvements in routing stability, it doesn't fully explore the trade-offs between stability and adaptability. A more detailed analysis of whether increased stability might sometimes come at the cost of reduced model flexibility would be valuable.

2. The hyperparameter sensitivity analysis is limited, particularly regarding the temperature parameter $\tau$ in Similarity-Inform SMoE and $\sigma$ in Attention-Inform SMoE. Understanding how these parameters affect performance would be crucial for practical implementations.

3. The experiments focus primarily on medium-sized models. Given that routing issues often become more pronounced in larger-scale settings, evaluation on larger models would strengthen the paper's claims.

4. While the paper mentions load balancing benefits in the appendix, this aspect deserves more attention in the main text, as it could be a significant practical advantage of the proposed approach.

### Questions
1. How does the approach scale with very large numbers of experts (e.g., hundreds or thousands)?

2. Have you explored the possibility of dynamically adjusting the influence of token similarities based on training progress?

3. How does the method perform when applied to multi-modal tasks where routing patterns might be more complex?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work addresses a core limitation of SMoEs—routing instability—by introducing collaborative token routing mechanisms, enhancing both model robustness and efficiency. This is show both theoretically and in a few benchmarks.
	
**Contributions:**

Probabilistic Graphical Model (PGM) Framework: Introduces a PGM framework to model SMoE-based attention, showing that expert selection is conditionally independent for each token, leading to unstable routing.

Mutual-Inform SMoE Models: Proposes two new SMoE variants:
- Similarity-Inform SMoE: Routes similar tokens to the same expert, using token similarities from the MoE layer.
- Attention-Inform SMoE: Utilizes relationships from the attention layer to inform expert assignments, aligning expert choice with token interactions.

This is validated theoretically (with entropy reduction) and empirically (with task specific benchmarks)

### Strengths
**Originality:** Introduces Mutual-Inform SMoE, a novel approach for stabilizing SMoE routing using token similarity and attention dependencies. Innovatively reinterprets SMoE through a probabilistic graphical model (PGM), which is a fresh way of addressing routing challenges.

**Quality:** Very rigorous theoretical framework (congrats!); sound mathematical proofs back claims about reduced entropy and improved stability. 

**Significance:** Addresses a critical issue in SMoEs (routing instability), with potential to impact scalable model design for large-scale LLM and vision applications. Improvements in both standard and adversarial settings underscore its value in robust model deployment.

### Weaknesses
### Presentation weaknesses:
- Writing needs to be considerably improved (sentences unclear, leading to confusions)
- Many typos need fixing (eg: Abstract: In this work, we unveil**s**; Motivat**ing** by this PGM framework…)
- Proofs could be explained a bit better than just a series of latex equations.

### Empirical work weaknesses
- The empirical validation is weak, more benchmarks would be appreciated. The experiments could be strengthened by comparing against more recent or diverse baselines
- Mutual-Inform SMoE models show strong results, additional ablations would clarify the impact of individual components (e.g., temperature parameters, entropy reduction mechanisms). Including these would highlight the contributions of each module in performance gains.
- There is a lack of discussion on the computational costs of the method, and the computation penalty for using these more performant models compared to the baseline.

### Questions
- How does this work compare to other, more modern methods and across more benchmarks?
- What is the computational cost of these methods?

(See weaknesses for details)

### Soundness
4

### Presentation
1

### Contribution
3

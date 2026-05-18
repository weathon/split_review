- Decision: Reject
- Scores: 5, 6, 5

## Merged Review

### Summary
The paper proposes a stable reparameterization technique to alleviate the curse of memory in state-space models, supported by theoretical analysis and empirical evaluation on synthetic data, language modeling (Hyena-SSM on Wikitext), and image classification. Reviewer opinions are mixed: one reviewer (score 6) finds the theoretical derivation concrete and the paper well‑organized, while the other two (both score 5) acknowledge the theoretical contribution but raise significant concerns about the empirical validation and the disconnect between theory and experiments. One reviewer increased their score after clarifications but still rated 5.

### Strengths
- Choosing an appropriate implicit parameterization for SSMs is practically important, and the paper provides a principled criterion (gradient‑norm scale) to rank parameterizations. [R1]
- The theoretical connections (e.g., Volterra series) are interesting and well‑presented. [R1]
- The paper is well organized; the overall workflow is easy to follow. [R2]
- The derivation appears concrete, and the main theorems about the curse of memory and the necessity of reparameterization are thoroughly supported with assumptions and proofs. [R2, R3]
- The analysis identifies the root cause (recurrent weights converging to the stability boundary) and argues that reparameterization can lift the memory limitation. [R2]

### Weaknesses
- Disconnect between theory and experimental results: experiments are limited to a small‑scale Hyena‑SSM on Wikitext, with no multiple runs, no variation of hyperparameters, and no testing on different applications. Appendix D shows that the ranking of parameterizations changes completely when the learning rate is tweaked. [R1]
- Eq. (2) does not correspond to a practical instantiation of SSM‑based models, which use a linear readout ($c^T h_t$) followed by a pointwise shallow MLP (with or without gating). [R1]
- Missing explorations: no consideration of small hypernetworks or alternative parameterizations; the paper parameterizes only the poles of the SSM implicitly, not the residues; the effect of the entire architecture block (gating + SSM) on the choice of parameterization is not investigated. [R1]
- No downstream evaluation or validation loss is reported for the language model; the empirical evaluation focuses on training behavior (training loss, stability) and does not demonstrate concrete improvements on test/validation performance. [R1, R2]
- The theorems are established only for the shallow (single‑layer) case; the paper does not clarify how shallow the model must be or why the results do not extend to deeper architectures. [R2]
- The introduction does not adequately illustrate the practical disadvantage of exponential‑decay memory, which is the core problem addressed. [R2]
- The theoretical analysis is limited to linear time‑invariant (LTI) systems approximating linear decay; it is unclear how the reparameterization would interact with non‑linear activation functions, time‑varying components, or multi‑layered architectures. [R3]
- The claim that the “best” reparameterization should satisfy Lipschitz continuity of the gradient with respect to the weight lacks rigorous justification. The paper does not clearly establish why Lipschitz continuity is necessary or sufficient for stable training, nor does it connect this property to convergence or improved generalization. [R3]
- It is not clearly justified why the gradient‑to‑weight ratio (the proposed criterion) is related to better training outcomes. [R3]
- It remains unclear whether the analysis can be extended to more complex models such as multi‑layer RNNs or transformer‑based RNNs. [R3]
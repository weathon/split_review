- Decision: Reject
- Scores: 3, 3, 5, 6, 3

## Merged Review

### Summary
The paper investigates whether transformers can use in-context learning (ICL) to mimic the Kalman filter (KF) for state and output estimation in linear dynamical systems. The authors provide a hand-coded transformer (Algorithm 1) that implements KF update equations using operations amenable to attention-based architectures, and empirically compare the transformer's predictions (mean squared prediction difference) against the KF, SGD, ridge regression, and ordinary least squares. Experiments show close alignment with the KF, including robustness to missing hyperparameters (e.g., when state transition or noise covariance matrices are omitted from context), and an extension to dual-Kalman filtering is given in the appendix. While reviewers agree the topic is relevant (bridging control/estimation theory and deep learning), they diverge sharply on the paper’s depth, novelty, and empirical rigor. Reviewers 3 and 4 are more positive (scores 5 and 6; R4 with low confidence 2), calling the work a fresh perspective and an advance on prior ICL literature, and praising the robustness to missing hyperparams. Reviewers 1, 2, and 5 (scores 3) find the paper incomplete, with insufficient theoretical derivation, weak empirical evaluation (no out-of-distribution tests, no comparison to ground truth, no ablation on model size or context length), missing positioning in related work, and presentation problems.

### Strengths
- The paper studies a relevant and interesting connection between control/estimation theory and deep learning, fitting the contemporary research focus on ICL. (R2, R4)
- It provides a fresh perspective on predicting states of linear time-invariant systems using transformers and ICL. (R4)
- It extends the literature on transformers’ ability to represent incremental learning algorithms (e.g., SGD) to the Kalman filter, an advance over prior work (e.g., Goel et al., who only showed a transformer can implement a *specific* KF). (R1, R3)
- The theoretical construction (Algorithm 1) showing the KF can be reduced to operations in (11)–(12) is a natural extension of Akyürek et al. (2022). (R3, R5)  — *Note: R3 considers this a straightforward corollary, while R1 treats it as a significant step.*
- The empirical results demonstrate that the trained transformer’s predictions are close to the optimal KF predictions. (R4, R5)
- The robustness to missing hyperparameters (e.g., state transition matrix, noise covariances) is impressive and suggests the transformer is doing more than the hand-coded architecture, meriting further investigation; filtering with unknown hyperparameters is still an active area. (R3)
- Equations are logical and well-presented; the method is overall well-written and mathematically correct. (R2, R5)

### Weaknesses
**Theoretical claims lack derivation and detail.**
- The paper does not provide a derivation of its theoretical claims; Algorithm 1 is simply asserted as a transformer-appropriate KF implementation, contrasting with Akyürek et al. (2023) who include a detailed derivation. (R1)
- The theoretical result is a relatively straightforward corollary of Akyürek et al. (2022)—only needing to show the KF can be reduced to operations in (11)–(12)—but the paper does not explain how to *arrange* multiple such operations within the layers of a single network. The required number of layers appears to grow linearly with sequence length, which conflicts with the experiments using fixed-depth transformers. (R3)
- The index matrices \(I_{B1}, \dots, I_{B8}, I_F\) and the derivation of contexts (20) and (28) are not stated or derived; readers are left to infer them, hampering reproducibility. (R2)
- No derivation or explanation is given for Algorithm 1 (and Algorithm 2 in the appendix). (R2)

**Empirical evaluation is insufficient and incomplete.**
- Only a proxy metric (mean squared prediction difference) is used on a test set drawn from the same distribution as training; no out-of-distribution generalization is tested. In contrast, Garg et al. (2022) investigate OOD performance as well as dependence on model capacity and problem dimensionality—both of which would be important here to support the claim of truly learning the KF equations. (R1)
- Results are reported only as relative performance (difference to KF) rather than absolute error against the ground truth state/output. Including ground truth and errors for all methods would be much stronger. (R2)
- Plots (e.g., Figure 1) are clipped; they should be split to show full range (e.g., on log scale) and detailed differences between better algorithms. (R2)
- There is no ablation study on context length or model size, although the paper mentions that MSPD peaks when context length equals state dimensionality (Figure 1). This behavior is not discussed or visualized for multiple state dimensions. (R1, R4)
- The paper does not report computational requirements. (R4)
- “Sufficiently long context” (line 481) is not specified; impact of context length on performance is not analyzed. (R5)
- Scalability to large datasets (e.g., \(10^6\) points) is not addressed; possible use of low-rank/sparse representations for (20) is not discussed. (R5)
- The paper does not consider time-varying \(F\), \(Q\), or \(R\) (though \(F\) is stated as time-varying in (4) but later treated as time-invariant). (R2)
- The choice of experimental setup (beginning of Section 4: strategies for generating \(F\), architecture, training schedule) is not motivated; why specifically Strategies 1 and 2 for \(F\)? (R1)
- Maximum marginal noise of 0.025 is not contextualized relative to the scale of dynamics (low or high noise). (R1)
- Only one learning rate is considered for SGD; tuning could bring SGD closer to KF performance. (R2)

**Missing comparisons, baselines, and related work.**
- The paper lacks sufficient positioning in existing literature: it does not discuss recent works connecting transformers to linear state space models (e.g., [1],[2]) or works on learning Kalman filters unrelated to transformers ([3],[4]). (R2)
- Missing references for the GPT-2 model and the Adam optimizer. (R2)
- Extension to nonlinear systems is not addressed; comparing ICL with extended/unscented Kalman filters or Gaussian variational inference would add value. (R4, R5)

**Presentation and clarity issues.**
- The title is misleading: the transformer learns to *estimate* hidden states/outputs of a linear system, not the “behavior” (i.e., the dynamical representation). (R2)
- The appendix only extends to dual-Kalman filters instead of providing additional details of the main method (e.g., RAW operator, index matrices, derivations). (R2)
- Positional embeddings are not mentioned in the theoretical analysis, but they are likely essential for implementing the elemental operations (page 5) and for sequential KF calculations. (R3, R5)
- Algorithm 1 is described in convoluted prose; pseudocode would be far more readable. (R5)
- Several specific technical errors: (i) In (9) and (10) the inverse should be a pseudoinverse; (ii) the statement that eigenvalues on the unit circle are unstable is false—they are marginally stable; (iii) Eq. (1) shapes do not agree; (iv) Eq. (1) has an extra bracket and uses “Softmax” instead of “\operatorname{Softmax}”; (v) line 243: \(n+1\) should be \(n\) (thrice); (vi) line 259: “\mathcal{A}_append” should be “\mathcal{A}_prepend”. (R1, R2, R3, R5)
- Notation confusion: \(R\) is used both for the covariance of measurement noise and for the real numbers \(\mathbb{R}^n\); use \(\mathbb{R}\) for real numbers. (R5)
- Equations (9) and (10) should use pseudoinverses; (4) should be stated for time-invariant \(F\) (or justification given). (R2)
- In (21) and (30), \(T_\theta\) is undefined. (R1, R5)
- The need for observability/detectability of \((F, H)\) (since \(F\) and \(H\) are randomly generated) is not discussed; these properties affect KF performance and thus transformer comparison. (R2)
- On page 5, the four elemental operations could be written mathematically rather than prose (e.g., \(G^l[K] = G^{l-1}[I] G^{l-1}[J]\)). (R3)
- Several typos and grammar mistakes (e.g., “comprising of”, “assuming one can simply run a fixed number of steps”, “causal linear estimator” not defined). (R1, R2)
- In Figure 1, error is unexpectedly low at context length zero; intuition is not explained. (R5)
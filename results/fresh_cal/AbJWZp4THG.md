Now I have all the information I need. Let me construct the final consolidated review.

---

## Summary

This paper introduces FedAda², a class of federated optimization algorithms that achieve joint server-client adaptivity without communicating preconditioners between server and clients, while using memory-efficient local optimizers (SM3) to reduce on-device memory cost. The paper provides an O(T^{-1/2}) convergence guarantee for non-convex objectives and empirically evaluates FedAda² on StackOverflow, CIFAR-100, and GLD-23K against baselines including FedAvg, FedAdam/FedAdaGrad, and expensive "Direct Joint Adaptivity." The key finding is that avoiding preconditioner transmission and using SM3 compression maintains competitive performance while being substantially more communication- and memory-efficient.

## Strengths

- **Communication-efficient joint adaptivity validated across three datasets**: Figure 1 (top row) shows FedAda² achieves test accuracy competitive with the expensive "Direct Joint Adap." baseline on StackOverflow, CIFAR-100, and GLD-23K, while Figure 2 demonstrates faster convergence than direct joint adaptivity when measured by transmitted bits. This directly supports the paper's central claim that preconditioner transmission can be avoided without degrading model quality.

- **Convergence analysis with standard rate**: Theorem 6 and Corollary 8 provide a deterministic O(T^{-1/2}) convergence guarantee for non-convex objectives under the analyzed setting. The paper explicitly notes this rate matches prior federated non-convex optimization works (Reddi et al., 2021; Wang et al., 2022; Tong et al., 2020, among others), situating the contribution within established theory.

- **Empirical advantage under differential privacy**: In the StackOverflow DP setting (Section 6.1, noise multiplier σ=1), FedAda² with zero-initialized client preconditioners and SM3 compression "achieved even better performance than direct joint adaptivity" (Figure 1 top-left), showing that the efficiency gains do not necessarily harm the privacy-utility trade-off.

- **Robustness across asymmetric optimizer configurations**: Section 6.1 reports that FedAda² maintains strong training dynamics across unbalanced preconditioner setups (e.g., server Adam with client AdaGrad), and the analysis in Section 5 generalizes to a class of memory-efficient local optimizers. This flexibility is a practical advantage over frameworks that assume symmetric or fixed optimizer pairings.

- **Memory-efficiency via SM3 approximation without degrading performance**: The paper demonstrates that SM3 compression of local preconditioners does not substantively harm performance and can, in some settings (DP StackOverflow, GLD-23K under constrained client resources), match or exceed full preconditioner storage.

## Weaknesses

### Fatal
None.

### Major

- **Theory-empirics gap undermines the claimed theoretical support**: The convergence analysis (Theorem 6, Corollary 8) assumes access to full-batch client gradients and relies on a gradient clipping mechanism parameterized by ε_s (Section 5). The paper explicitly acknowledges this: "we assume access to full batch client gradients which are bounded" and later states "the gradient descent setting used in the analysis of Theorem 6 is conceptually equivalent to accessing oracle client workers capable of drawing their entire localized empirical data stream. While this constraint is a limitation of our theory…" (Section 5.1). However, the experiments use practical settings with stochastic gradients and adaptive optimizers (Adam, AdaGrad, SM3). The paper claims generalization to these settings is deferred to the appendix, but the full-batch-versus-stochastic gap means the headline O(T^{-1/2}) guarantee is formally for a different (simpler) setting than the one empirically evaluated. This disconnect means the empirical results cannot be taken as direct validation of the theory, nor does the theory fully explain the empirical behavior. While this gap is common in the optimization literature and the paper acknowledges it, the abstract claims that "Theoretically, we demonstrate that FedAda² achieves the same convergence rates… as its more resource-intensive counterparts" without qualifying the full-batch assumption, which overstates the support.

- **The central ablation yields a counterintuitive, unexplained result that should be investigated**: The baseline "Joint Adaptivity without Preconditioner Communication" is identical to FedAda² except it does not compress the local preconditioner (i.e., it uses full AdaGrad/Adam locally instead of SM3). Section 6.2 states that "eliminating server preconditioner transmission destabilizes the accuracy, resulting in significantly poorer performance for the worst losses, while retaining the best performing losses" and that "Surprisingly, approximating the preconditioners in a memory-efficient manner using SM3 restabilizes the losses." This means the *compressed* variant outperforms the *uncompressed* variant — a finding that, if true, suggests that full preconditioners introduce harmful noise rather than the compressed ones being a "good enough" approximation. The paper offers only a speculative hypothesis ("denoising effect of projections during SM3 compression") and does not investigate this phenomenon through controlled experiments (e.g., varying compression rank, comparing to explicitly regularized full preconditioners, analyzing gradient variance). Without such analysis, the empirical advantage of FedAda² over its direct ablation is not convincingly explained and may reflect a hidden regularization benefit rather than efficient approximation of the intended adaptive mechanism.

### Minor

- **Tension between different descriptions of the same ablation**: The Figure 1 caption states "not transmitting the global preconditioner does not degrade performance," but Section 6.2 states that "eliminating server preconditioner transmission destabilizes the accuracy, resulting in significantly poorer performance for the worst losses." These can be reconciled (the caption refers to best-performing hyperparameters; the sensitivity analysis considers worst-case performance across a hyperparameter sweep), but the paper does not clearly distinguish these interpretations, creating apparent inconsistency that complicates interpretation of the core claim.

- **DP setting yields a relatively weak privacy guarantee**: The StackOverflow DP experiment uses noise multiplier σ=1, yielding (ε,δ)=(13.1, 0.0025). An ε of 13.1 is a modest privacy level (typically ε<10 is considered meaningful and ε<1 is strong). While the paper does not overclaim on this front, the results should be interpreted with this context, and the practical significance of improvements under this privacy regime is limited.

### Trivial
None.

## Nice-to-Haves

- **Investigate why SM3 compression improves over the full uncompressed preconditioner**: This is the paper's most surprising finding and the one most central to its narrative. Controlled experiments varying compression rank/ratio, comparing against explicit ℓ₂ regularization of the full preconditioner, and measuring gradient variance with and without SM3 would significantly strengthen the contribution.

- **Align the theory with the stochastic setting or provide bridging evidence**: Since the theory assumes full-batch gradients, an empirical study varying local batch size to test whether the theoretical assumptions are violated in practice would help bridge the gap.

- **Clarify the apparent tension between "not degrading performance" and "destabilizing accuracy"** by explicitly distinguishing best-case and worst-case performance metrics.

## Removed Points

These points were flagged for removal from the main review with justification:

1. **"Paper is incomplete/disorganized, missing introduction, no algorithm statement"** — REMOVED. The extracted text shows a garbled section header on line 7 ("\section{13: end for }") with no introduc/like tory content before it. The paper references Section 1 (line 109), Algorithm 1 (lines 35, 55, 61, 99), and Algorithm 5 (line 31), confirming these sections exist in the original submission. The missing content is a PDF extraction artifact, not an author error. Per instructions, formatting/parsing criticisms must be removed.

2. **"No related work section"** — REMOVED. Sections 1–4 (which would contain introduction, related work, and algorithm description) were garbled by the parser. The paper extensively cites prior work (Reddi et al., 2021; Wang et al., 2022; Anil et al., 2019; McMahan et al., 2017; Xie et al., 2020; Tong et al., 2020; Sun et al., 2023, etc.), confirming these discussions existed.

3. **"Missing experimental details (hyperparameters, training protocols)"** — REMOVED. The paper references Appendices C.1 and C.2 for optimizer-specific details. Per instructions, weaknesses about missing appendix content are removed because the parser strips appendices from all submissions.

4. **"Direct Joint Adaptivity is a strawman baseline"** — REMOVED. The paper also includes "Joint Adaptivity without Preconditioner Communication" as a fair communication-efficient baseline. Including an expensive upper-bound baseline alongside fair comparisons is standard practice and does not constitute a staged comparison.

5. **"Blended Optimization discussion is confusingly placed"** — REMOVED. This is a presentational preference, not a substantive methodological weakness.

6. **Strength: "no known convergence results of jointly adaptive FL that support Adam and AdaGrad"** — REMOVED. The paper's own theory is for full-batch GD with gradient clipping, not for Adam/AdaGrad directly (deferred to the inaccessible appendix). When a strength conflicts with a verified weakness (the theory-empirics gap), the weakness wins.

## Novel Insights

The most interesting signal from the reviews is the central tension the paper creates for itself: its strongest empirical finding — that SM3 compression *improves* over the full, uncompressed local preconditioner — is also its least explained. This result, if confirmed and understood, would shift the paper's narrative from "efficient approximation without performance loss" to "compression acts as a regularizer that improves performance," which is a different and potentially more interesting claim. The paper does not engage with this possibility, treating the result as a fortunate auxiliary observation rather than a finding that could redefine the contribution.

## Suggestions

1. **Investigate the SM3 regularization effect systematically.** Run controlled experiments varying SM3 compression rank/ratio, compare against explicit ℓ₂ regularization of the full preconditioner, and measure gradient variance with and without SM3. This is the single most important thing to strengthen the paper.

2. **Either align the theory with the stochastic setting or add a batch-size ablation study.** If the theory cannot be extended, at minimum show empirically that reducing batch size does not violate the theoretical conditions (e.g., by testing convergence across different local batch sizes).

3. **Distinguish clearly between optimal and worst-case performance** when describing the effect of removing preconditioner transmission. The paper currently uses "does not degrade performance" (optimal hyperparameter case) and "destabilizes accuracy" (worst-case across hyperparameters) without separating these claims, which creates unnecessary confusion.

## Score and Decision

**Originality**: Moderate — the idea of avoiding preconditioner communication is a natural extension of prior work; the combination with SM3-style compression is the primary novel element.

**Importance of research question**: High — communication and memory efficiency in federated learning is practically important and well-motivated.

**Claims support**: Moderate — empirical results are generally well-supported across three datasets with 20 runs and 95% CI, but the theory does not fully align with the experimental setting, and the central ablation (SM3 vs. full preconditioner) is unexplained.

**Soundness of experiments**: Moderate — the evaluation uses three diverse datasets, multiple baselines, and proper statistical reporting. However, the counterintuitive SM3 effect and weak DP context leave questions about whether the results are fully understood.

**Clarity of writing**: Cannot fully assess due to parser artifacts, but the available content is coherent and structured.

**Value to research community**: Moderate — if the SM3 regularization effect is understood, FedAda² would be a practically useful contribution to federated learning.

The paper makes a genuine empirical contribution: FedAda² works well in practice and the core idea (avoiding preconditioner transmission + SM3 compression) is well-motivated and validated across multiple datasets. However, two significant weaknesses — the theory-empirics gap and the unexplained SM3 regularization benefit — meaningfully reduce confidence. These are addressable but require substantive additional analysis, not just presentational fixes. The paper is publishable with major revisions that address these issues.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>
- Decision: Reject
- Avg Score: 4.75
- Scores: 6, 5, 3, 5
Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

## Summary

The paper introduces a sheaf-theoretic framework for decentralized federated multi-task learning (FMTL) that addresses both feature heterogeneity (different model sizes) and sample heterogeneity across clients. By modeling client relationships as cellular sheaves with learnable restriction maps and using sheaf Laplacian regularization, the proposed Sheaf-FMTL algorithm enables communication-efficient decentralized learning by exchanging low-dimensional projections. The framework subsumes several existing FL/FMTL approaches and is shown empirically to achieve up to 100× communication savings over the dFedU baseline on Rotated MNIST while maintaining comparable accuracy, and to outperform standalone local training when clients have different model sizes.

## Strengths

- **Communication efficiency demonstrated with clear empirical evidence**: Figure 2(b) shows Sheaf-FMTL achieves comparable or higher accuracy than dFedU while transmitting dramatically fewer total bits — for Rotated MNIST with γ=0.01, roughly 100× fewer bits. The x-axis of Figure 2(b) is total transmitted bits, so this directly measures communication-accuracy trade-offs under an equalized budget.

- **Handling of heterogeneous model sizes across clients**: Experiment 2 (Figure 3) on modified Vehicle and School datasets shows that Sheaf-FMTL significantly outperforms stand-alone local training when clients have different model dimensions (d_i). The paper explicitly acknowledges that it is the first algorithm addressing this scenario in a decentralized topology, which is a genuinely novel capability.

- **Flexible task-relationship modeling via learnable restriction maps**: The sheaf formalism with matrix-valued restriction maps P_ij (Section 3.2) subsumes fixed scalar-weight approaches (e.g., graph Laplacian regularization, which corresponds to P_ij = I). The restriction maps are optimized jointly with model parameters, enabling the framework to learn task relationships from data rather than assuming them a priori.

## Weaknesses

### Fatal
None.

### Major

- **Limited baselines undermine the empirical evaluation.** For the same-model-size setting (Experiment 1), the only baseline is dFedU — a single comparison point. An ablation against a graph-Laplacian-regularized variant (i.e., fixing P_ij = I) would isolate whether the learned restriction maps themselves provide a benefit beyond the sheaf structure. For the different-model-size setting (Experiment 2), only local training is compared, which is a lower bound that any collaborative method should exceed. While the paper justifiably notes that no existing decentralized FMTL method supports different model sizes, the absence of any adapted baseline (e.g., projecting models to a common dimension) limits what this experiment can establish about relative advantage. The paper's empirical claims would be substantially strengthened by at least 1–2 additional decentralized FMTL baselines for the same-model-size setting and one adapted baseline for the different-model-size setting.

### Minor

- **Missing experimental details hinder reproducibility.** The paper does not report: (a) the nature of heterogeneity introduced in "Heterogeneous CIFAR-10.1" (a non-standard variant), (b) the number of clients, (c) the communication graph topology (ring, random, fully connected?), (d) model architectures per client, or (e) how the regularization strength γ is set per client. These are standard reporting requirements for FL experiments.

- **No error bars or confidence intervals.** Figures 2 and 3 show single-run results. Without variance estimates, it is impossible to assess whether the observed improvements over dFedU are statistically significant or within run-to-run noise.

- **Unsupported privacy claim in the conclusion.** The conclusion states the method "preserves client privacy," but the paper offers no privacy analysis — no differential privacy guarantee, no formal treatment of what information leakage the sheaf framework prevents beyond standard FL data locality. This overclaim should be removed or substantiated.

- **Task type ambiguity for Vehicle/School datasets.** Figure 3 reports "test accuracy" for the Vehicle dataset and "MSE" for the School dataset, without clarifying whether these are classification or regression tasks. The paper should state the task type per dataset explicitly.

- **Convergence rate not stated in the main text.** The abstract claims "a sublinear convergence rate in line with state-of-the-art," but the specific rate (e.g., O(1/T), O(1/√T)) and key assumptions (e.g., L-smoothness, μ-strong convexity, bounded variance) are not stated anywhere in the available main body. Even if the full proof resides in a section stripped by the parsing process, a summary of the guarantee should appear in the abstract or introduction. This makes the theoretical contribution unverifiable from the main text alone.

### Trivial
None.

## Nice-to-Haves

- **Ablation study separating the effect of learnable restriction maps vs. the sheaf structure itself.** Running Sheaf-FMTL with P_ij fixed to identity (recovering graph Laplacian regularization) would isolate whether learning the restriction maps adds value over a simpler sheaf baseline.
- **Sensitivity analysis over γ** (the edge-space dimension factor). The paper uses γ ∈ {0.01, 0.03} but does not study how performance and communication vary with this critical hyperparameter. A sweep would illuminate the communication-accuracy trade-off frontier.
- **Empirical overhead measurements.** Table 1 reports storage and computation costs in asymptotic notation only. A concrete numerical example (e.g., wall-clock time per round for a 50-client graph) would help practitioners assess whether the overhead is acceptable.

## Removed Points

These points were raised by the reviewers but are excluded from the main review for the reasons below:

1. **"Communication savings claim is misleading without equalizing the communication budget."** — REMOVED (factually incorrect). Figure 2(b) *does* control for total communication budget: the x-axis is the total number of transmitted bits. The comparison is presented as accuracy vs. bits, which is exactly the equalized-budget framing the critic demands.

2. **"Should compare to FedRep, pFedMe, Ditto, FedBABU."** — REMOVED as scope-creep. These are server-based personalized FL methods, not decentralized FMTL methods. Adapting them to a decentralized topology would be a significant engineering effort orthogonal to the paper's contribution. The general concern about baseline breadth is retained above, but these specific suggestions are not appropriate for a decentralized setting.

3. **"Theoretical convergence analysis is insufficiently specific (fatal)."** — DEMOTED to minor. The specific rate and assumptions were likely in Sections 3.3/3.4, which were stripped by the PDF parser. The valid remaining concern is that the main text (abstract/intro) should summarize the guarantee explicitly — this is captured above as a minor weakness.

4. **"Graph connectivity and γ sensitivity analysis missing."** — MOVED to Nice-to-Haves. These are useful extensions, not weaknesses of the current evaluation.

5. **"Scalability discussion about storage overhead."** — MOVED to Nice-to-Haves. The paper already discusses storage costs in the text (lines 102–103) and Table 1, reasonably noting that the overhead is offset by communication savings and is acceptable in cross-silo settings. The critic's concern is addressed.

6. **"Pure formatting/style nitpicks"** — REMOVED per hard rules. Parser artifacts are not author errors.

## Novel Insights

The harsh critic correctly identifies the paper's chief limitation (thin baselines), while the strength finder correctly identifies the paper's genuine empirical contribution (100× communication savings, heterogeneous model sizes). The critical synthesis is that these two observations are not contradictory: the paper's *specific* evidence is compelling within its narrow scope (one baseline, one setting), but the *breadth* of evidence is insufficient for a paper that also makes theoretical, methodological, and unifying claims. The most impactful next step for the authors is not to add more datasets or more unrelated methods, but to ablate the core mechanism (learnable P_ij vs. fixed P_ij = I vs. dFedU) — this would directly test whether the sheaf flexibility, not just the low-dimensional communication, drives the improvement. The privacy overclaim is a separate, easily fixable issue.

## Suggestions

- **Add at least one additional baseline** for the same-model-size experiment (e.g., a graph-Laplacian-regularized FMTL method that fixes P_ij = I) and one adapted baseline for the different-model-size experiment (e.g., projecting all models to a common space via a learned linear layer).
- **Report the specific convergence rate and key assumptions** (e.g., "Under L-smoothness and μ-strong convexity, Sheaf-FMTL converges at rate O(1/T)") in the abstract or introduction.
- **Add error bars** (standard deviation over 3–5 random seeds) to all experimental figures.
- **Document the following experimental details** in a table: dataset heterogeneity, number of clients, graph topology, model architectures, and hyperparameter selection.
- **Remove or substantiate the privacy claim** in the conclusion. If the paper only means "raw data stays local," rephrase to "does not require sharing raw data" — the current wording implies a formal guarantee that is not provided.

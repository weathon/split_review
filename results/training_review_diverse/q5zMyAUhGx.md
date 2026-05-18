Now I have all the information needed to produce the consolidated review.

---

## Summary

This paper provides the first rigorous generalization bounds for Kolmogorov–Arnold Networks (KANs), covering two settings: (1) activation functions expressed as linear combinations of basis functions, and (2) activation functions lying in a low-rank RKHS (Matérn kernel). The bounds are derived under standard assumptions (Lipschitz conditions, moment conditions on the loss), adapt covering-number arguments and Maurey's sparsification lemma to the KAN architecture, and do not require the loss function to be bounded—covering regression-type losses via a truncation argument. An empirical study on simulated data, MNIST, and CIFAR-10 shows that a complexity measure derived from the bounds tracks the excess loss during training.

## Strengths

1. **First rigorous generalization bounds for KANs.** The paper explicitly notes that "there is currently no recent research focusing on quantifying the complexity of KANs" (Section 1, Contributions) and fills this gap with bounds for two broad families of activation functions. The extension of norm-based generalization bound techniques (Bartlett et al. 2017, Anthony & Bartlett) from MLPs to KANs is non-trivial because KANs place learnable univariate functions on *edges* rather than fixed nonlinearities on *nodes*, requiring careful handling of Lipschitz constants and operator norms at each layer.

2. **Bounds hold for unbounded loss functions.** Theorem 2 (thm-main2) uses a truncation argument to go beyond the bounded-loss setting common in prior margin-based analyses. The paper explicitly highlights that the result "does not require the boundedness assumption on the loss function" (Section 1, Contribution (v)), making it applicable to squared loss, pinball loss, Huber loss, etc.

3. **Novel low-rank RKHS analysis.** Theorem 3 (thm-main3) provides generalization bounds for KANs whose activation functions lie in a low-rank RKHS. The authors state that "the results for KANs with a low-rank structure in Section 2.3 appear to be new, and we are not aware of comparable results for MLPs in the recent literature" (Section 1, Related Works). Remark 4 (rm1) further connects this to fine-tuning (analogous to LoRA), which is a non-trivial extension.

4. **Bounds free of combinatorial parameters except logarithmic factors.** The covering-number bound in Theorem 1 (thm-cover) depends only on $\log(2\tilde{d}\tilde{p})$ rather than linearly on the number of nodes or basis functions. This is a genuine technical achievement—naive covering estimates would scale with network width—and the paper correctly notes that the $l_1$ norms $B_i$ can adapt to the actual sparsity structure.

5. **Empirical connection to a computable complexity measure.** The numerical study demonstrates that the theoretical complexity measure $\tilde{\alpha}$ tracks the excess loss across training epochs on four simulation settings, MNIST, and CIFAR-10 (Figure 1). The paper uses this to suggest a potential regularization strategy, bridging theory and practice.

## Weaknesses

### Fatal

None. The theoretical development is technically sound, the assumptions are standard and clearly stated, and the derivations correctly adapt the covering-number framework to the KAN architecture. No error invalidates the core claims.

### Major

None. The paper's primary contribution is theoretical, and the theory is well-executed. The empirical section is appropriately scoped as an illustration of the theory rather than a standalone empirical contribution.

### Minor

1. **The basis function choice in the experiments is not explicitly stated.** Section 3 describes how the complexity measure is computed (via the formula proportional to $(\prod_j \rho_j)^{2/3} \sum_i (B_i c_i)^{2/3}$ and how Lipschitz constants are estimated (via the upper bounds in Remark 4), but it does not state which specific basis functions (e.g., B-splines with what order and knot spacing) were used for the edge activations. While the original KAN paper (Liu et al. 2024) uses B-splines and the simulations follow that paper's examples, this lack of explicit specification makes the empirical description slightly less self-contained than it could be.

2. **The practical regime for the low-rank RKHS bound is not discussed.** Theorem 3 (thm-main3) assumes $\tilde{d} > \nu$ (the maximum width exceeds the Matérn smoothness parameter) and the bound scales polynomially with the ranks $r_i$ and Lipschitz constants, with exponent $(d_{i-1}/\nu) \vee 1$ that can be large. The paper is honest about this scaling, but it does not comment on when this bound is practically meaningful (i.e., when $d_{i-1}$ is small relative to $\nu$). A brief discussion of the interpretable regime would help readers gauge the bound's practical scope.

3. **The product of Lipschitz constants is not discussed.** Like many norm-based bounds for deep networks, the complexity measure involves $\prod_j \rho_j$, which can grow exponentially in depth. The paper does not discuss whether this product is likely to be manageable in practice (e.g., through spectral normalization or implicit regularization during SGD). The empirical section normalizes the curves, so the reader cannot gauge typical magnitudes.

### Trivial

None.

## Nice-to-Haves

- **Quantitative correlation measures:** The paper claims the complexity measure "tightly correlates" with excess loss based on visual inspection of aligned curves. Reporting a rank correlation (e.g., Spearman's $\rho$) or $R^2$ between the complexity measure and excess loss across epochs would substantiate this claim more concretely and distinguish genuine tracking from normalization artifacts.

- **Ablation on network structure:** A small study showing how the normalized complexity measure changes when the network is regularized, or when its depth/width is varied, would strengthen the argument that the bound captures the right complexity.

- **Explicit discussion of when the low-rank bound is useful:** A brief paragraph noting the regime where $d_{i-1}$ is small enough relative to $\nu$ for the bound to yield meaningful rates would help practitioners.

## Removed Points

These points were flagged in the original reviews but are removed here with justification:

- **"How Lipschitz constants and $l_1$ norms are estimated from trained KANs is unclear."** Removed because the paper explicitly addresses this: Section 3 states that "the Lipschitz constants $\rho_j$s were estimated by their upper bounds provided in Remark 4," and Remark 4 gives explicit formulas linking $\rho_j$ to the spectral norm of the coefficient matrix and basis-function Lipschitz constants. $B_i$ is the $l_1$ norm of the coefficient matrix, directly computable from trained weights. The paper provides sufficient methodological detail for a theory paper.

- **"How $\|X\|_2$ is handled in the complexity measure is unclear."** Removed because Assumption 1 states $\|X\|_2 \leq D$, and the complexity measure formula used in the experiments (the simplified version with $C=0$) is proportional to $\tilde{\alpha}$. Since $D$ is a constant across experiments, using a proportional measure is standard and justified. The handling is adequately described.

- **"The empirical details are largely deferred to the appendix."** Removed because the parser strips appendix sections from all submissions; the referenced appendix exists in the original paper. Moreover, the main text already provides the essential details: the complexity measure formula, how Lipschitz constants are estimated, the normalization procedure, the simulation setups, and datasets. For a theory paper, this is an appropriate level of empirical description.

- **"The bound's dependence on $d_i r_i$ is linear, not logarithmic."** Removed because this is an accurate description of the bound, not a flaw. The paper correctly states that the low-rank bound "scales polynomially with the underlying ranks," which is an honest characterization. The comparison is to the basis-function case, which was already noted to have logarithmic dependence on combinatorial parameters.

- **"The $l_1$ norm $B_i$ can implicitly depend on the number of nodes."** Removed because this is a correct observation about the nature of $l_1$ norms, not a weakness. The paper's claim is that the *explicit* dependence on combinatorial parameters is removed outside of logarithmic factors; this is stated accurately. The $l_1$ norm adapts to the actual sparsity structure, which is a feature, not a bug.

## Novel Insights

None beyond the paper's own contributions. The reviews largely affirm the paper's theoretical contributions without introducing unexpected perspectives. The one insightful observation—that the fine-tuning connection (Remark 4) links KAN bounds to the LoRA literature—is already present in the paper.

## Suggestions

1. **Explicitly state the basis function family used in experiments** (e.g., "B-splines of degree 3 with grid size $G$") in the main text of Section 3, or add a short supplementary table.
2. **Add a paragraph discussing when the low-rank bound yields practically meaningful rates** (i.e., when $d_{i-1}$ is small relative to $\nu$), and what happens when $\tilde{d} \leq \nu$.
3. **Report a rank correlation or $R^2$** between the complexity measure and excess loss across training epochs to quantitatively support the "tightly correlated" claim.
4. **Add a brief comment** on whether the product of Lipschitz constants $\prod_j \rho_j$ is likely to be well-behaved in practice under standard training (e.g., via spectral norm control or implicit regularization).

## Score and Decision

This is a solid theoretical contribution that fills a clear gap in the KAN literature. The derivations are technically sound, the assumptions are standard, and the paper is clearly written. The two settings (basis-function and low-rank RKHS) are well-motivated, and the bounds bring genuine insight into what controls KAN generalization. The empirical validation, while not the paper's primary contribution, credibly illustrates the theory. The weaknesses identified are minor and do not threaten the core claims.

**Originality:** High — first generalization bounds for KANs, with a novel low-rank RKHS analysis.
**Importance:** High — provides theoretical foundations for an architecture of growing research interest.
**Claims well supported:** Yes — theory is rigorous, empirical results are consistent with theory.
**Soundness of experiments:** Adequate for a theory paper; minor transparency issues.
**Clarity:** Good — the paper is well-organized and the technical material is presented clearly.
**Value to the community:** High — useful for researchers working on KAN theory and applications.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
Here is my final consolidated review:

## Summary

This paper proposes a Generalized Exact Path Kernel (gEPK), extending the Exact Path Kernel of Bell et al. (2023), which decomposes a trained neural network's prediction into a sum over training steps and training data points of inner products between test-time and training-time parameter gradients (Theorem 3.1). The paper then uses this representation to (1) provide a conceptual framework for understanding why several gradient-based OOD detection methods work, (2) derive a truncated-basis approach for OOD detection, and (3) develop a method for estimating signal manifold dimension from training-input gradients. Experiments on MNIST, FMNIST, and CIFAR provide proof-of-concept demonstrations.

## Strengths

- **Generalized Exact Path Kernel theorem (Theorem 3.1)**. The paper proves an exact decomposition of the trained model prediction as a double sum over training steps and training data of inner products between parameter gradients, without the symmetry or continuity restrictions of the original EPK. This is a formally sound theoretical extension that provides a foundation for connecting model predictions to both input and parameter gradients (Section 3, Equation 16).

- **Signal manifold dimension estimation via training-input gradients (Section 5)**. The paper derives an expression (Equation 28) relating the matrix of training-point-to-test-prediction sensitivities to the signal manifold perceived by the model. The empirical result that MNIST requires only 94/784 (12%) components for 95% explained variation vs. 1064/3096 (34%) for CIFAR provides concrete evidence that this decomposition captures differences in intrinsic dimensionality (Figure 1).

- **Cross-model comparison of input-gradient subspaces (Section 5, Figure 4)**. The gEPK decomposition enables comparing input-gradient subspaces across models with different initializations. Figure 4 shows that the top singular components are shared between models with different random seeds, linking this decomposition to adversarial transferability and offering a new angle for studying feature sharing across architectures.

- **OOD detection without test labels (Corollary 4.2, Section 4.2)**. By deriving spanning vectors for the prediction subspace and connecting them to an SVD basis, the paper provides a principled OOD detection method that does not require ground-truth labels for test points (unlike several prior gradient-based methods). The proof-of-concept experiment (Figure 2) demonstrates separation between MNIST and FMNIST projections.

## Weaknesses

### Fatal
None.

### Major

- **Disconnect between the central theoretical claim (Theorem 3.1) and the experimental validation.** The full gEPK representation involves a path integral over the continuous training trajectory and a double sum over all training steps and training data. However, none of the experiments actually implement this representation: the OOD experiment (Figure 2) uses only the final training step and only last-layer gradients; the dimension estimation (Section 5) uses training-input gradients of the final trained model without the path integral; Figures 1 and 4 compute ∇_{x_train}f(x_test;θ_trained) directly, which does not require Theorem 3.1. The paper acknowledges these simplifications (lines 155–161) but never tests whether the full path integral representation provides any empirical benefit over the simplified approximations. If the path integral can be dropped, that is itself a finding that should be demonstrated; if it cannot, the experiments do not support the theoretical claims. This structural gap undermines the empirical credibility of the paper's applied claims.

- **Connections to prior OOD methods are suggestive rather than rigorous.** Section 4.1 attempts to express GradNorm, ReAct, DICE, ASH, VRA, and GradOrth in terms of the gEPK, but the derivations are imprecise. For ASH, the connection is asserted without derivation: "Meaning this truncation is picking a representation for which ⟨...⟩ is high for many training points." For GradNorm, the description concludes "this approach is averaging across the parameter gradients...which we can see is only a related subset of the full basis" — a conceptual observation rather than a formal equivalence. Multiple statements use hedging language ("may be equivalent," "may explain some part of the performance advantage") that conflicts with the abstract's stronger claim that these methods "are in effect projections onto a reduced representation." The paper would need either explicit proofs of exact/approximate equivalence or carefully designed experiments showing the gEPK score matching or outperforming these methods to substantiate its unifying claims.

- **Dimension estimation section lacks comparison to established baselines and statistical rigor.** Section 5 claims that the rank of G(x) "represents the dimension of the subspace on which the model perceives a test point," but the paper provides no comparison to any existing intrinsic dimension estimator (including several cited in the related work, e.g., Ansuini et al., 2019; Costa & Hero, 2004b; Facco et al., 2018). The results in Figure 1 are presented without error bars, standard deviations, or multiple trials, making it impossible to assess whether the observed differences between datasets are statistically significant or robust across model initializations.

### Minor

- **No quantitative OOD metrics or baseline comparisons.** The OOD experiments show only a histogram of projection norms (Figure 2, left) without AUROC, AUPR, or FPR@TPR95 values. No comparison to any existing OOD method is reported. The paper states "as the purpose of this paper is not to develop state of the art OOD detection methods, a comparison with recent benchmarks is not provided" — this is a defensible scope choice for a theory paper, but it does leave the practical relevance of the proposed framework unquantified.

- **Experimental reproducibility is limited.** The paper does not specify model architectures, training hyperparameters (learning rate, batch size, optimizer, number of epochs), dataset preprocessing, or the number of random seeds used. The "toy problem (3 Gaussian distributions embedded in 100 dimensional space)" is mentioned but not described in sufficient detail to reproduce.

- **Notation inconsistency in the proof of Theorem 3.1.** The theorem statement defines S training steps, but the proof (line 73) writes "For all N training steps" and indexes the sum up to N, where N was previously used for the number of training data. This creates confusion (S vs. N).

- **Equation 26 (G_j) has a notational imprecision.** After asserting that terms vanish except when i=j, the equation still references x_i in the remaining expression where it should reference x_j (or equivalently, x_i with i=j). The mathematical idea is correct but the notation is sloppy.

### Trivial
None.

## Nice-to-Haves

- A small-scale experiment (e.g., a 2-layer MLP on a 2D synthetic dataset) where the full gEPK with the path integral can be computed, comparing its OOD detection performance and dimension estimates against the simplified versions used in the paper. This would either validate the full theory or honestly reveal that the path integral is unnecessary.
- Explicit derivation showing that at least one prior OOD method corresponds exactly or provably approximately to a gEPK-based quantity, rather than the current speculative comparisons.
- Error bars or confidence intervals on the dimension estimates (Figures 1 and 5) to quantify robustness.

## Removed Points

These points are flagged to be removed from the critique; treat them with caution:

- **"Section 5 derivation is incorrect / gradients are nonzero for all i" (Harsh Critic).** The critic claimed that d/dx_j of the gEPK sum terms is nonzero for all i, and that the paper's claim "these gradients will be zero except when i=j" is incorrect. After verifying the derivation: φ_{s,t}(x) depends on the test point x (not x_j), and φ_{s,0}(x_i) and dL(x_i,y_i)/df(x_i) depend on x_i. Derivatives w.r.t. x_j vanish whenever i≠j, so the claim is correct. The critic's objection is factually wrong.

- **"No Section 1 establishing connection to input gradients" (Harsh Critic).** The paper's Section 1 (Introduction, lines 14-15) explicitly states "This paper demonstrates a generalization (the gEPK) of the EPK from Bell et al. (2023), which can exactly measure the input gradient ∇_{x_train}f(x_test;θ_trained)." The criticized passage on line 123 refers back to this. The connection is established.

- **"ODIN description is misleading" (Harsh Critic).** The paper correctly states that ODIN "perturbs inputs by applying perturbations calculated from input gradients" — it does not claim ODIN uses parameter gradients. The description is accurate.

- **"Claim that ODIN directly inspired GradNorm needs support" (Harsh Critic).** This is a reasonable historical statement about the chronology of methods, not a central claim of the paper. It does not affect the technical contribution.

- **"Figure 4 caption is unclear" (Harsh Critic).** The caption clearly states that black = positive contribution, red = negative contribution, and explains the SVD sorting. The confusion appears to be a misreading.

- **"Section 6 mentions disconnected future directions" (Harsh Critic).** The future directions (implicit priors, robust learning under distribution shift) are reasonable extensions of the framework.

- **Parser artifacts** (garbled LaTeX in GradOrth description "x_2^\overline{\phantom{x}}", typos, formatting issues). These are artifacts of the PDF-to-text extraction, not errors in the original submission.

- **Strength 2 from Strength Finder** ("Unified theoretical explanation for multiple OOD methods"). The strength overstates what the paper achieves — the connections are conceptual/suggestive rather than rigorous derivations. Since this conflicts with the verified weakness about imprecise connections, it is moved here.

## Novel Insights

The most valuable perspective from the reviews is that the paper is caught between two ambitions: it wants to be a pure theory paper (proving the gEPK theorem) and simultaneously an applied/empirical paper (explaining SOTA OOD methods and measuring signal dimension). Neither the harsh critic nor the strength finder fully resolves this tension. The harsh critic evaluates it as an empirical paper and finds the experiments wanting; the strength finder evaluates it as a theory paper and accepts the experiments as proof-of-concept. The paper's actual contribution is the theoretical framework (Theorem 3.1 and the spanning-vector analysis), which is sound as a mathematical extension of Bell et al. (2023). The applied claims about OOD are the weakest part — not because they are wrong, but because the paper never tightens the connection between the full theory and the simplified practice. The dimension estimation idea is genuinely novel and the cross-model comparison (Figure 4) is an interesting direction, but both need more rigorous validation.

## Suggestions

1. **Reconcile theory with experiments.** If the paper's primary contribution is theoretical, explicitly scope the experiments as illustrations of what the theory enables, not as validation. Remove or hedge claims like "showcase OOD using natural gEPK based decomposition" if the full gEPK is not being computed. Alternatively, add one controlled experiment (e.g., a small model on a synthetic dataset) where the full path integral IS computed, to verify that the simplified approximations preserve the ranking or key properties.

2. **Tighten the OOD unification claims.** Replace the current speculative descriptions in Section 4.1 with either (a) exact derivations showing that specific OOD scores equal truncated gEPK inner products, or (b) a clear statement that the gEPK provides a conceptual lens, not a formal unification. The abstract's claim that methods "are in effect projections onto a reduced representation" needs to match the precision in the body.

3. **Add basic quantitative evaluation.** Even without SOTA benchmarking, report AUROC or a similar metric for the truncated-basis OOD method on MNIST vs. FMNIST, with standard deviations over 3–5 random seeds. For dimension estimation, compare the estimated intrinsic dimensions to at least one baseline (e.g., two-NN from Facco et al., 2018) to calibrate whether the numbers (94 for MNIST, 1064 for CIFAR) are plausible.

4. **Fix notational issues.** Clarify the distinction between S (training steps) and N (training data) in the proof of Theorem 3.1. In Equation 26, either write G_i (since i=j) or explicitly note that the index has been collapsed.

## Score and Decision

The paper presents a theoretically sound extension of the Exact Path Kernel and explores interesting applications to OOD understanding and dimension estimation. The theoretical core (Theorem 3.1) is a valid contribution. However, the paper's primary weakness is a structural disconnect between its strongest theoretical claim and the simplified approximations used in experiments, combined with imprecise treatment of OOD method connections that does not match the strong language in the abstract. The experimental validation is too thin to support the applied claims. Given that the theory itself is reasonable but the paper overclaims relative to what is actually demonstrated, the paper falls short of the standard for acceptance in its current form. Major revisions addressing the theory-experiment gap and the precision of the OOD connections are needed.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
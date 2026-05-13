Now I have a thorough understanding of the paper. Let me now carefully evaluate the harsh critic's claims and check them against the paper.

**Harsh Critic's claims and my assessment:**

1. **Confounded evaluation in self-supervised experiments (Critical Issue 1):** The paper explicitly states (line 219): "the projectional layer of SGD and SAM are linear layers, while RJR's is the R-Stiefel layer." This is a genuine confound. RJR in the SSL settings uses both RJR optimization AND a different architectural component (R-Stiefel layer) compared to baselines. The paper acknowledges this two-fold nature but doesn't disentangle the effects. This is a valid major concern — without an ablation isolating the R-Stiefel architecture from the RJR optimizer, the improvement in SSL could be attributable to the different architecture.

2. **Confounded evaluation in supervised learning (Critical Issue 2):** In the supervised setting (Table 1), RJR enforces strict orthogonality on convolutional filters, while baselines have no such constraint. The comparison is between "orthogonal filters + RJR" vs. "unconstrained filters + SGD/SAM." The paper argues (Section 5.2) that they're replacing soft orthogonal regularization (Xie et al.) with hard manifold constraint. The paper does acknowledge the inductive bias of orthogonal filters. However, the baseline comparisons include Riemannian-SAM and Riemannian-SGD which also optimize on the Stiefel manifold (so they also enforce orthogonality). Let me check if Riemannian-SAM also constrains filters to Stiefel manifold.

Looking at Table 1's description: "we compare and contrast RJR with Momentum SGD, SAM, Riemannian-SAM (Yun & Yang, 2023), and Riemannian SGD (Bonnabel, 2013)."

Wait — Riemannian-SAM and Riemannian-SGD also constrain the same parameters to lie on the Stiefel manifold. So the baselines RSGD and Riemannian-SAM also have orthogonal filters. The fair comparison is RJR vs. Riemannian-SAM (both use manifold constraints). This partially addresses the critic's concern — the paper already has fair comparisons against other manifold methods. But the comparison against standard SGD and SAM is indeed confounded (different architecture). However, the paper's main claim is that RJR improves over existing manifold optimizers, not that it's better than vanilla SGD/SAM.

Actually, re-reading Section 6: "In this setting, RJR is incorporated to force the orthogonality on the convolutional layers. Specifically, we imposed orthogonality on a single convolutional layer in the middle of the architecture in all settings."

This says RJR forces orthogonality — it's unclear whether Riemannian-SAM and RSGD also impose orthogonality on the same layer in the same way. Given that they are Riemannian methods, they likely also constrain parameters to the Stiefel manifold. So the comparisons with Riemannian-SAM and RSGD should be fair (same architectural constraint, different optimizer).

For the self-supervised case, the concern is stronger because the R-Stiefel layer is an additional architectural change that baselines don't have. This is a real confound.

3. **Theorem 1 without proof (Critical Issue 3):** The theorem is stated but no proof is provided in the body. This is a valid concern — Theorem 1 is the core theoretical motivation and without proof, the claimed improvement from O(√k) to O(√d) cannot be verified. The constants M and D are indeed not well-specified. However, proofs in supplementary material are standard in ML papers and may have been stripped. Per my instructions, I should not criticize missing proofs in an appendix.

Wait, the instructions say: "REMOVE weaknesses about missing appendix, missing proofs in appendix, or absent references. The parser strips those sections from all papers; they exist in the original submission." So I need to remove this criticism.

4. **Heuristic gap between theory and algorithm (Critical Issue 4):** The paper shows that Theorem 1 motivates minimizing ‖grad_θ L_S‖ and ‖P_θ ∇²L_S‖_σ. For the SAM-like term (λ₁), the Taylor expansion in Eq. (4) establishes the connection that perturbation in the normalized gradient direction implicitly regularizes the gradient norm. However, for the Jacobian terms (λ₂), there's no corresponding Taylor expansion or argument showing that perturbing along normalized grad_θ(zε) and ∇_θ(zε) implicitly minimizes their norms. The paper simply states this generalizes the SAM approach. This is a valid theoretical concern — the connection between the perturbation direction and implicit regularization for the Jacobian terms is not formally established, making this step heuristic rather than theoretically justified.

Let me now also verify additional claims:

- **Robustness claim without adversarial experiments**: The abstract says "improve robustness and generalization." The word "robustness" appears in two contexts: (1) the abstract says "improve robustness and generalization" and (2) Section 2 mentions "Another desired property of the model is robustness, which could be improved when encouraging the model's parameters to satisfy strict conditions." The paper doesn't conduct adversarial robustness experiments, so the "robustness" claim is somewhat vague — they seem to use it in the sense of optimization robustness (finding flat minima) rather than adversarial robustness. Still, the claim could be misleading.

- **No comparison with EJR**: The paper acknowledges RJR generalizes EJR (Lee et al., 2023) but doesn't experimentally compare with it. This is a valid concern since EJR is the most directly comparable method.

- **SAM perturbation radius ρ**: Not reported in the paper as far as I can see. This is reproducibility information — but per my instructions, I should consider this as a minor reproducibility concern rather than a major one.

Let me now synthesize the final review.</think>Now I have read the entire paper. Let me carefully synthesize the final review.

## Summary

The paper introduces Riemannian Jacobian Regularization (RJR), an optimization method for problems where parameters lie on Riemannian manifolds. Motivated by a generalization bound (Theorem 1) that depends on intrinsic manifold dimension \(d\) rather than ambient dimension \(k\), RJR simultaneously regularizes the Riemannian gradient norm and projected Hessian spectral norm, generalizing both SAM and Euclidean Jacobian Regularization (EJR). The algorithm is evaluated on supervised learning (orthogonal CNN filters), labeled self-supervised learning (SupCon with R-Stiefel projection head), and unlabeled self-supervised learning (SimCLR).

## Strengths

- **Unified theoretical framework**: The paper generalizes prior SAM-based and Jacobian-regularization methods to Riemannian manifolds in a clean way. Setting \(\lambda_2=0\) recovers Riemannian-SAM, \(\lambda_1=0\) on Euclidean space recovers EJR, and \(\lambda_2=0\) on Euclidean space recovers SAM. This unification is clearly established in Section 4.2.

- **Mechanistic validation through ablations**: Figures 2–3 provide direct evidence that RJR achieves lower Hessian spectral norms (10.52 vs. 13.93 for Riemannian-SAM) and gradient norms, consistent with the theoretical motivation. This mechanistic validation is more informative than end-to-end accuracy comparisons alone.

- **Broad empirical evaluation**: The paper tests RJR across multiple settings (supervised, SupCon, SimCLR), multiple architectures (ResNet34/50, EfficientNet, PyramidNet), and multiple datasets (CIFAR10/100, STL10, Aircraft), which exceeds the typical scope for optimization papers.

## Weaknesses

### Fatal
None.

### Major

- **Confounded evaluation in self-supervised experiments**: In Tables 2–3, RJR uses an R-Stiefel projection head (U ∈ St(n,p) + diagonal S) while baselines SGD and SAM use standard linear projection heads. The paper explicitly acknowledges this (Section 6, line 219): "the projectional layer of SGD and SAM are linear layers, while RJR's is the R-Stiefel layer." This is a structural confound: the claimed improvements (up to 7% on CIFAR100) could be partially or entirely attributable to the different projection head architecture rather than RJR's optimization. Without an ablation that tests (a) baselines with R-Stiefel heads + SGD/SAM, and/or (b) RJR with a standard linear head, the self-supervised results cannot isolate the optimizer's contribution from the architectural变更. This weakens a core empirical claim.

- **Heuristic gap between theory and algorithm for Jacobian terms**: Theorem 1 motivates minimizing \(\|\text{grad}_\theta \mathcal{L}_S\|\) and \(\|P_\theta \nabla^2 \mathcal{L}_S\|_\sigma\). For the SAM-like term \(\lambda_1\), the Taylor expansion (Eq. 4, Section 4.2) establishes that perturbing in the normalized gradient direction implicitly regularizes the gradient norm. For the Jacobian terms \(\lambda_2\), however, no such derivation is provided — the paper asserts by analogy that perturbing along normalized \(\text{grad}_\theta(z\varepsilon)\) and \(\nabla_\theta(z\varepsilon)\) implicitly minimizes their norms, but this connection is not formally or empirically established. This leaves the core algorithmic step beyond the SAM component as heuristic rather than theoretically grounded.

- **No comparison with EJR (the direct Euclidean precursor)**: The paper states (Section 4.2) that RJR generalizes EJR (Lee et al., 2023), yet no experimental comparison with EJR appears. This is a significant omission: EJR is the most directly comparable baseline (it also regularizes Jacobian norms, just without manifold structure), and comparing against it would directly isolate the contribution of the Riemannian extension.

### Minor

- **Supervised comparison conflates constraint with optimizer when comparing against SGD/SAM**: While the paper includes fair comparisons with Riemannian-SAM and RSGD (which also enforce Stiefel constraints), the comparisons against standard SGD and SAM in Table 1 conflate the inductive bias of orthogonal filters with the optimizer's effect. This is less severe than the SSL confound since the Riemannian baselines provide fair optimizer-only comparisons, but the improvements over SGD/SAM should not be attributed solely to RJR.

- **Robustness claim is vague**: The abstract states RJR can "improve robustness and generalization," but no adversarial robustness experiments are presented. The paper uses "robustness" to mean optimization stability (flat minima), but the term could mislead readers expecting adversarial robustness results.

### Trivial
- None.

## Nice-to-Haves

- An ablation in the self-supervised setting with an R-Stiefel head + standard SGD/SAM (without RJR) would directly isolate the optimizer's contribution from the architecture's.
- A comparison with EJR on the supervised orthogonal CNN task would clarify the value added by the manifold-aware formulation over the Euclidean one.
- A formal justification (even informal, beyond analogy) for why perturbing along the Jacobian directions implicitly regularizes their norms would strengthen the theory-to-algorithm connection.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Theorem 1 proof missing**: The harsh critic flagged the missing proof of Theorem 1 as a critical issue. However, per the review instructions, proofs in appendices are standard and the parser strips appendices. The proof likely exists in the original submission's supplement. Removed because this is a "missing appendix/proof" issue.

- **SAM perturbation radius ρ unreported**: The harsh critic noted SAM's ρ is not reported. This is a minor reproducibility concern about a baseline hyperparameter, not the paper's method. Removed as a trivial reproducibility nitpick.

- **"Same computational complexity as SAM" claim is misleading**: The critic argued the claim ignores cost of computing z = Σf_θ(x) and tangent space projections. The paper itself acknowledges RJR "is expected to be slower due to additional computations involving the Jacobian and Riemannian gradients" and has a runtime figure. The claim about "same asymptotic complexity" for backward passes is reasonable (single backward pass), and the nuance is addressed. Removed as already addressed by the paper.

- **Tight confidence intervals suspicious**: The critic questioned the 53.12 ± 0.05 interval. This is just a standard result from 5 runs and not evidence of any problem. Removed as unsubstantiated suspicion.

- **Hessian spectra measured at 400 steps**: The critic noted this is "not over full training convergence." This is a reasonable snapshot comparison for ablation purposes and does not invalidate the finding. Removed as overly picky.

- **Strength finder claim about O(√d) bound**: The strength finder claims the intrinsic dimensionality improvement is a core strength. While interesting, this claim depends on the unverified proof of Theorem 1 (constants M, D are undefined, and whether they depend on k is unclear). I keep this as a potential strength but weaken it since the theoretical novelty restson an unverified bound.

## Novel Insights

The key insight that emerges across the reviews is that this paper's contribution is best understood as two coupled innovations — an algorithmic one (RJR as a Riemannian extension of SAM+EJR) and an architectural one (R-Stiefel metric learning layer) — and the current evaluation makes it difficult to disentangle their individual contributions in the self-supervised experiments. The supervised experiments with Riemannian-SAM/RSGD baselines provide cleaner evidence for the optimizer alone, but even there, the comparison with soft orthogonal regularization methods (which the paper explicitly cites but doesn't compare against experimentally) would isolate the value of hard manifold constraints + RJR vs. soft penalties.

## Suggestions

- Add at least one ablation in the self-supervised experiments: run SGD/SAM with the R-Stiefel projection head (without RJR on U) to determine how much of the improvement comes from the R-Stiefel architecture vs. the RJR optimizer.
- Compare against EJR (Lee et al., 2023) on at least the supervised orthogonal CNN task.
- Provide an informal derivation or empirical verification that perturbing along normalized Jacobian directions implicitly regularizes the Jacobian norms, closing the theory-to-algorithm gap for the λ₂ terms.

## Score and Decision

The paper presents a well-motivated and unified Riemannian optimization framework that cleanly subsumes prior methods. The theoretical generalization bound, while promising, is stated without proof (likely in a supplement). The main empirical contribution is undermined by the confounded self-supervised experiments, where architectural differences (R-Stiefel head) are entangled with the optimizer. The supervised experiments with Riemannian-SAM/RSGD baselines provide fair comparisons and show meaningful improvements (3% on average), but the missing EJR comparison and the heuristic gap between theory and algorithm for the Jacobian terms leave the core contribution partially unvalidated. The paper has genuine novelty and the results are promising, but the evaluation needs deconfounding experiments to support its claims convincingly.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
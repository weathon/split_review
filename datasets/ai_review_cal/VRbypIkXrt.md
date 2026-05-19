- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5
I have thoroughly verified all claims against the paper. Let me now produce the final consolidated review.

---

## Summary

This paper proposes MetaOptimize, a framework that dynamically adjusts meta-parameters (primarily step sizes) during training by minimizing a discounted sum of future losses. The approach derives causal surrogate gradients via eligibility traces, introduces low-complexity Hessian-free approximations (2×2, L-approximation), and wraps around any first-order optimizer for both base and meta updates. The framework subsumes existing methods like IDBD and hypergradient descent as special cases. Experiments on CIFAR-10, ImageNet, and TinyStories show that Hessian-free variants match or exceed fixed step-size baselines, several adaptive methods (DoG, Prodigy, Mechanic, gdtuo), and tuned cosine schedules on *training* metrics, while adding modest computational overhead.

## Strengths

- **Principled formalization with a causal gradient proxy.** Section 3 introduces a forward-view objective minimizing discounted future losses (Eq. 1) and derives a backward-view approximation (Eq. 3–4) via eligibility traces that can be computed causally. This provides a clear, theoretically grounded optimization target.
- **General framework wrapping any first-order optimizer.** Algorithm 1 defines a generic meta-update rule (Eq. 6) that accepts arbitrary base-update and meta-update algorithms. The block matrix \(G_t\) (Eq. 7) cleanly separates dependencies, making the framework modular and broadly applicable.
- **Low-overhead Hessian-free approximations achieve competitive performance.** Section 6 derives variants that eliminate Hessian-vector products. Table 1 reports that for (AdamW, Lion) on ImageNet, per-iteration time overhead is +44% and space overhead 33%, which is substantially lower than methods like gdtuo (+85% time, +64% space), while maintaining competitive training curves.
- **Robustness to initial step-size choices over several orders of magnitude.** Figure 1b demonstrates that MetaOptimize (Lion, Lion) achieves the same final performance even when initial step sizes are 100× smaller than the optimal fixed value — a property not shared by most adaptive methods.
- **Unifies and clarifies prior algorithms as special cases.** Section 5 explicitly shows that IDBD, its extension (Xu et al. 2018), and hypergradient descent (Baydin et al. 2017) are recovered under the L-approximation with SGD (\(\gamma=0\) for hypergradient descent). This provides a useful theoretical lens for understanding existing methods.

## Weaknesses

### Fatal

None.

### Major

- **Only training metrics are reported; no test/validation evaluation.** All learning curves and reported numbers are training accuracy or training loss (Fig. 1a, 2a, 2b). The abstract claims "performance competitive to those of best hand-crafted learning rate schedules across various machine learning applications," but without test-set evaluation this claim about *generalization* performance is unsupported. While training curves are the primary metric for optimization convergence (the paper's core focus), the framing invites comparison on ultimate model quality, and the omission of test metrics weakens the experimental support for that broader claim. The authors should report held-out accuracy (CIFAR-10 test set, ImageNet validation, TinyStories validation loss/perplexity) to fully substantiate the stated claims.

- **No systematic ablation of the proposed approximations.** The paper introduces 2×2, L-approximation, and Hessian-free variants, but never compares them against each other or against the full Hessian-based MetaOptimize in a controlled experiment. The paper states "we have empirically observed in simple settings" (line 252) that the 2×2 approximation has minimal impact, but no data is provided. Since the approximations are a core part of the contribution, an ablation study (e.g., on a small problem like an MLP on CIFAR-10) is needed to justify the claim that the approximations preserve performance.

### Minor

- **CIFAR-10 experiments only compare against fixed step-size baselines, not against tuned schedulers.** Unlike the ImageNet and TinyStories experiments (which include cosine decay comparisons), CIFAR-10 only compares against fixed step-sizes (line 418–420). Adding a cosine or step-decay scheduler baseline would strengthen the CIFAR-10 results.
- **No experimental comparison to IDBD or its neural-network extensions.** The paper claims these are special cases of the L-approximation (line 313) and that MetaOptimize "extends" IDBD research (line 518), but no experimental comparison is presented. While IDBD is not a state-of-the-art baseline for modern deep learning, including it (at least on a small problem) would substantiate the claimed improvement over prior work.
- **No multiple seeds or confidence intervals reported.** All experiments appear to be single runs. For CIFAR-10 (which is small enough to run multiple trials) this is a straightforward fix. For ImageNet-scale experiments, single runs are standard practice but basic variance estimates would still strengthen the results.
- **Hyperparameter tuning of baselines is not detailed.** The paper states baselines are "well-tuned for each task separately" (line 361) but does not describe the tuning procedure, search ranges, or final chosen hyperparameters. This would be helpful for reproducibility.

### Trivial

- The complexity table (Table 1) does not break down overhead for the baseline schedulers (cosine decay is essentially free, but noting this explicitly would be cleaner).
- The explanation for why \(\eta=10^{-3}\) works universally (lines 500–501) is heuristic; a brief empirical validation (e.g., a sensitivity plot on a small problem) would strengthen the claim.

## Nice-to-Haves

- A brief comparison of Hessian-free variants vs. full Hessian-based MetaOptimize on a small synthetic or low-dimensional problem (e.g., quadratic minimization) to validate the approximation quality.
- Guidance for practitioners on choosing base/meta optimizer pairings beyond the few combinations tested.
- A discussion of whether the training-metric improvements translate to test-set gains on CIFAR-10 and ImageNet, where overfitting patterns can differ between optimizers.

## Removed Points

These points from the harsh critic are flagged to be removed — treat them with caution:

1. **"This omission invalidates the experimental contribution in its current form"** — overstatement. The paper provides meaningful training-metric comparisons; the omission weakens but does not invalidate the contribution.
2. **"Training curves can be misleading due to overfitting"** — speculative; no evidence of overfitting is presented, and the paper studies stationary supervised learning where training loss is the direct optimization target.
3. **"DoG excluded without explanation"** — the paper *does* explain: "learning curve of DoG is not depicted due to its relatively poor performance" (line 453). The exclusion is transparent, not selective.
4. **"No statistical significance or multi-run results"** — partially true but overstated. Single-run ImageNet experiments are standard; the critic's concern about "artifacts" in TinyStories is speculative without evidence.
5. **"The approximations are justified only by 'empirically observed' claims with no supporting ablation study"** — the paper does reference empirical observations; the criticism that no data is shown is valid but already captured under "Major" weaknesses above.
6. **"Complexity table does not include overhead of baseline schedulers"** — a formatting nitpick; cosine/scheduler overhead is negligible and not central.
7. **"η=10⁻³ claim is anecdotal"** — the paper provides a reasoned justification (lines 500–501), even if heuristic.
8. **Strength Finder: generic strengths about "addressed an important problem"** — dropped as superficial; only concrete, evidence-backed strengths are retained.
9. **Strength Finder: "outperforms...recent adaptation methods"** — retained in weakened form since results are on training metrics only.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any perspective not already present in the paper itself. One observation from synthesis: the paper's claimed robustness to initial step-size (verified in Fig. 1b) is potentially its strongest empirical asset — it is a property few adaptive methods can demonstrate and is well-evidenced even within the current experimental scope. The reviews did not highlight this as strongly as the paper's own presentation does.

## Suggestions

1. **Add test/validation metrics to all three benchmarks.** This is the single most impactful improvement and directly addresses the paper's claim about "performance competitive to hand-crafted schedules."
2. **Include an ablation study** comparing 2×2, L-approximation, Hessian-free, and (if feasible) full Hessian MetaOptimize on a small problem (e.g., a small MLP on CIFAR-10 subset, or a synthetic quadratic). This would validate the approximations that are central to the practical contribution.
3. **Add multiple seeds (at least 3–5) for CIFAR-10** and report mean ± std; for ImageNet/TinyStories, add a note that single-run results are standard at this scale.
4. **Add a cosine-decay scheduler baseline to CIFAR-10 experiments** for consistency with the other benchmarks.
5. **Describe the hyperparameter tuning procedure for baselines** (search range, final chosen values) in an appendix or supplement.

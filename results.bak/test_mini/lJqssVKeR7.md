Now I have all the evidence I need. Let me write the consolidated review.

## Summary

This paper proposes HiSo, a Hessian-informed zeroth-order federated optimization method that learns a global diagonal Hessian approximation from scalar-only communicated updates, preserving the dimension-free communication advantage of prior ZO-FL work (DeComFL) while accelerating convergence. The key idea is to use the already-communicated update vectors $\Delta x$ to estimate a diagonal preconditioner $H_r$, which then biases the random perturbation directions in subsequent ZO gradient estimates toward more informative directions. The paper provides a generalized scalar-only FL framework, a non-convex convergence analysis showing the potential for dimension-independent and Lipschitz-independent rates under a "well-approximated condition," and experiments on CNN-MNIST and OPT-series LLM fine-tuning benchmarks showing 1.4–5.4× communication round speedups over DeComFL.

## Strengths

1. **Novel algorithmic design that preserves scalar-only communication while incorporating curvature.** HiSo's core idea — learning a diagonal Hessian preconditioner $H_r$ from the scalar-valued update vectors $\Delta x$ that are already communicated (Eq. 12) — is clever and non-trivial. The curvature information accelerates descent without transmitting a single extra parameter. The update rule $\Delta x = g \cdot H^{-1/2}u$ (Eq. 8–10) cleanly reduces to standard ZO-SGD when $H=I$ and to a Newton-like preconditioned update when $H$ approximates the Hessian.

2. **First convergence analysis for ZO-FL with curvature-aware updates and multiple local updates.** Theorem 1 provides a non-convex convergence guarantee for HiSo without requiring the well-approximated condition. Corollaries 1–3 show that under the well-approximated and low-whitening-rank conditions, the rate can be $\mathcal{O}(\sqrt{\zeta/mR})$ — independent of dimension $d$ and Lipschitz constant $L$. Corollary 3 extends this to $\tau>1$ local updates, addressing an open issue in DeComFL's analysis. The theory provides a plausible explanation for why ZO can converge much faster than its worst-case $\mathcal{O}(d)$ bound.

3. **Generalized scalar-only communication framework.** Algorithm 1 decouples the dimension-free communication protocol from the specific ZO-SGD update, enabling a broader class of ZO optimizers (including HiSo) to be deployed within the same framework. This is a useful conceptual contribution beyond the specific HiSo algorithm.

4. **Empirical validation on LLM fine-tuning across multiple model sizes.** The experiments cover OPT-125M, 350M, 1.3B, and 2.7B on SST-2, QQP, and SQuAD. HiSo consistently outperforms all ZO baselines (FedZO, DeComFL) in both accuracy and communication cost (Table 3). The learned Hessian distribution (Fig. 5, right) shows a long-tail structure supporting the low-effective-rank motivation.

## Weaknesses

### Fatal
None.

### Major

1. **The central claim of "Hessian-informed" acceleration lacks direct empirical validation.** The paper's core mechanism — that the learned $H_r$ meaningfully approximates curvature — is not directly tested. The paper does not compare $H_r$ against the true Hessian diagonal (or a proxy) for any model, nor does it check whether $\text{Tr}(H^{-1/2}\Sigma H^{-1/2})$ (the "well-approximated condition" from Definition 17) is actually small in practice. The paper acknowledges this gap ("Although it is hard to determine if this approximation holds in the context of LLMs…") but this undercuts the central narrative implied by the title and Corollaries 1–3. Without this check, the improved convergence could be explained by an adaptive learning-rate effect (like RMSProp in a ZO setting) rather than curvature-informed preconditioning. An ablation that replaces the learned $H_r$ with a fixed diagonal or random diagonal would help isolate the mechanism.

2. **The speedup metric in Table 2 is biased.** Table 2 reports "the number of rounds needed to match DeComFL's best test accuracy." Since HiSo achieves higher final accuracy than DeComFL in every setting (Table 3), it naturally reaches DeComFL's lower peak faster. This conflates "converges to a specific threshold faster" with "converges to a higher value." A fairer comparison would report rounds to reach a common accuracy threshold that both methods can achieve, or provide convergence curves showing accuracy vs. rounds for all tasks (analogous to Fig. 5 for CNN-MNIST) so readers can assess speedup at any accuracy level. The "1–5× speedup" claim as presented is inflated relative to standard community practices.

### Minor

3. **Key hyperparameters for LLM experiments are not reported.** The paper states $P=5$ for all ZO methods but does not specify the smoothing parameter $\mu$, learning rate $\eta$, Hessian momentum $\nu$, or any clipping thresholds used in the OPT experiments. ZO methods are known to be sensitive to $\mu$, and without these values the results are not reproducible. This is a significant omission for a paper making empirical claims.

4. **Computational overhead is not quantified.** HiSo requires generating $H_r^{-1/2}u$ perturbations and updating $H_r$ via Eq. (12) each round. The paper reports communication and memory costs in the appendix but does not report wall-clock time or per-round FLOPs relative to DeComFL. This matters because the claimed speedup in rounds could be partially offset by higher per-round computation.

5. **The theoretical speedups in Corollaries 1–3 depend on an unverified condition.** The paper is transparent about this (the Remarks in Sec. 5.2 explicitly state the limitation), but the Corollaries as written state rates like $\mathcal{O}(\sqrt{\zeta/mR})$ without caveating that these hold *only* under the well-approximated condition. A reader scanning the results could easily interpret these as proven rates for the algorithm. The corollaries should state "Under the well-approximated condition (Definition 17), ..." upfront.

6. **Eq. (12)'s motivation from squared $\Delta x$ to Hessian diagonals is heuristic.** The paper draws an analogy to Adam/RMSProp, but in the ZO setting the connection between $\mathbb{E}[(\Delta x)^2]$ and the true Hessian diagonal is not formally established. The paper describes $\Delta x$ as "a free variable" and uses its squared entries to approximate Hessian diagonals (Eq. 12), but the reasoning is more intuition than derivation. This does not invalidate the method, but the paper should be clearer about the heuristic nature of this step.

### Trivial

7. **The CNN-MNIST experiment (Fig. 5) shows an ablation on $\nu$ and a Hessian histogram but does not compare HiSo against any ZO method other than DeComFL.** An identity-preconditioned or constant-diagonal baseline would strengthen the Hessian-specific attribution.

8. **The number of random seeds/runs for the standard deviations in Table 3 is not stated.**

## Nice-to-Haves

- **Validate the Hessian approximation explicitly** for a small model (e.g., OPT-125M): compute a proxy for the true diagonal Hessian (via Hutchinson estimator) and compare against the learned $H_r$ at various training stages to show that $\text{Tr}(H^{-1/2}\Sigma H^{-1/2}) \ll Ld$.
- **Provide convergence curves for all LLM tasks** (accuracy vs. communication rounds) to complement the summary statistics in Tables 2 and 3.
- **Ablate the Hessian component** by comparing HiSo against a version with $H_r$ fixed to identity or to a random diagonal matrix.
- **Add a brief intuition for the $\tau > 1$ client drift result** in the main text (rather than only in the appendix).

## Removed Points

- **Criticism that PEFT baselines are insufficient**: The paper references "other FL+PEFT baselines" in the appendix (Appendix E); since the appendix was stripped by the parser, this criticism cannot be verified against the actual submission. Removed per policy.
- **Criticism about Sec. 4.1 derivation being "overcomplicated"**: Subjective style judgment that does not affect correctness. Removed.
- **Criticism about missing related work**: Per policy, I cannot verify the existence of unmentioned works.
- **Criticism about missing limitations section**: Not a standard requirement for ICLR submissions, and the paper does include a "Remarks" section that partially serves this purpose.
- **"Toy experiment uses synthetic eigenvalues with no connection to LLM training dynamics"**: The experiment is explicitly described as illustrative (Fig. 4 caption: "An Illustration"), not as an empirical claim. Removed.
- **"The baseline set could be stronger" (specific claim about missing ZO-FL methods)**: The paper compares against DeComFL (SOTA ZO-FL) and FedZO, which are the most relevant baselines; additional baselines are reported in the appendix.

## Novel Insights

The two reviewer inputs largely agree on the paper's strengths (clever algorithmic design, theoretical analysis with dimension-free potential, real LLM experiments) and weaknesses (Hessian approximation not validated directly, speedup metric biased, hyperparameters undisclosed). The harsh critic's framing that the Hessian mechanism is "the central narrative" and that its lack of validation is a significant gap sharpens what would otherwise be a minor concern into a major weakness. Conversely, the Strength Finder's identification of the long-tail Hessian distribution (Fig. 5, right) as corroborating evidence for the low-effective-rank motivation provides some counterbalance. The tension is genuine: the paper makes a plausible claim about curvature-driven acceleration with supporting (but not definitive) evidence, and the empirical results stand on their own regardless of the exact mechanism. The key insight from synthesizing both reviews is that the paper would be significantly strengthened by a single direct experiment validating the Hessian approximation, but the underlying method and empirical results are already solid enough to stand as a contribution.

## Suggestions

1. **For the rebuttal**: Provide hyperparameter values ($\mu$, $\eta$, $\nu$) for all LLM experiments, and include convergence curves (accuracy vs. rounds) for at least one LLM task to address the speedup metric concern.
2. **For the final version**: Add an ablation comparing HiSo against a version with $H_r$ fixed to identity on a small model (CNN-MNIST or OPT-125M). This would directly test whether the learned $H_r$ is responsible for the improvement.
3. **Add a dedicated limitations paragraph** explicitly stating that (a) the Hessian approximation has not been directly validated, (b) the theoretical dimension-free rates depend on an unverified condition, and (c) there is an accuracy gap vs. first-order methods that is the price of the communication savings.
4. **Restructure Corollaries 1–3** to lead with "Under the well-approximated condition (Definition 17), ..." to avoid misinterpretation.

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
- Weak band (<3.5): *FN-NOW* (avg 3.0, Reject) — Newton-type FL with low-rank Hessian, but had fundamental theoretical concerns; *HERON-SFL* (avg 3.2, Withdrawn) — ZO+FO hybrid FL with limited validation.
- Middle band (3.5–7.5): *Stochastic Gaussian ZO* (avg 4.0, Reject) — ZO theory with flawed convergence analysis; *FedNewton* (avg 4.5, Reject) — Newton-type FL with restrictive squared-loss theory; **Meerkat** (avg 5.0, Accept Poster) — ZO sparse federated LLM fine-tuning, most topically similar.
- Strong band (>7.5): *Polar Express* (avg 8.0, Oral) — matrix sign methods for Muon, breakthrough-level contribution in different area.

**Round 2 (Narrowing, 4.5–7.5):**
- *Meerkat* (avg 5.0, Accept Poster, scores 6/2/6/6) — HiSo is comparable in novelty and empirical scope. Meerkat has stronger experiments but HiSo has a more novel algorithmic idea (Hessian-informed vs. sparsity). HiSo's evidential gaps (unvalidated Hessian, biased metric) are somewhat larger than Meerkat's weaknesses.
- *Cost-Aware Client Selection* (avg 5.5, Accept Oral) — Stronger theory but weaker experiments than HiSo. HiSo has better empirical validation for its target setting.
- *GH-OFL* (avg 6.0, Accept Poster) — One-shot FL with clean contribution; less related but similar evaluation quality.

**Round 1 bracket:** 4.0–6.5 / **Final score positioned relative to anchors:** Better than the 4.0 ZO theory paper (which had fundamental theoretical errors) and comparable to Meerkat (5.0) but with somewhat larger evidential gaps offset by more novel algorithm. Slightly below the 5.5–6.0 papers which had cleaner validation.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>
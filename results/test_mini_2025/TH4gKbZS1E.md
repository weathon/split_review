Now I have all the calibration data I need. Let me write the final consolidated review.

---

## Summary

This paper conducts an empirical comparison of KAN vs MLP on 10 one-dimensional functions spanning six categories (regular, non-differentiable, jump-discontinuous, singular, oscillatory, and noisy). The study matches parameter counts (~120 and ~240) across architectures, varies training sample size, and tests two optimizers (L-BFGS and Adam). The goal is to determine whether KAN's reported advantages hold across different function regularity types, particularly when functions are irregular or corrupted by noise.

## Strengths

- **Systematic function categorization.** Table 1 defines six distinct function types (regular, continuous with non-differentiable points, jump, singular, coherent oscillation, noisy) with concrete examples (f1–f10). This taxonomy provides a useful organizing framework for the KAN vs MLP comparison and directly enables the paper's central finding that relative performance depends on function regularity.

- **Controlled parameter count between architectures.** Table 2 explicitly lists matched architectures (e.g., MLP [1,39,1] = 118 params, KAN [1,5,1] grid=3 k=3 = 120 params). This ensures observed test loss differences are not trivially artifacts of capacity disparity.

- **Evidence that KAN does not always outperform MLP.** The paper's body text and conclusion consistently report that MLP achieves lower stabilized test loss on functions with non-differentiable points (f3, f4) and jump discontinuities (f5, f6). Section 3.2 states "the KAN's performance is worse than the MLP's" for f3/f4, and Section 3.3 states "the MLP outperforms the KAN" for f5/f6 (lines 113, 117). This is a meaningful empirical finding given the enthusiastic claims in the original KAN literature.

- **Computational cost difference documented.** Tables 3 and 4 report wall-clock time per optimizer/network combination. For example, fitting f7: MLP+L-BFGS takes 8.3s while KAN+L-BFGS takes 588.8s (a ~70× slowdown). This provides concrete evidence for the practical cost of KAN.

- **Sample-size scaling study across function types.** The paper varies training samples from 50 to 5000 across multiple function types (Figures 1–3, 9–11) and documents when increased sampling helps (f1–f6) versus when it does not (f7–f10), supporting the conclusion about diminishing returns for low-regularity functions.

## Weaknesses

### Major

- **Figure 3 caption directly contradicts the body text.** Section 3.3 (line 117) states: "Results show that the MLP outperforms the KAN" for jump-discontinuity functions f5 and f6. However, the Figure 3 caption (line 242) reads: "In all cases, KAN (red dashed line) fits the target function (green squares) much better than MLP (blue dashed line)." These statements are mutually exclusive. The body text and conclusion (Section 5, line 163) consistently claim MLP outperforms KAN for f3–f6, suggesting the caption is the error, but this is never acknowledged or resolved. A reader cannot determine which result is correct for two of the ten test functions without external resolution. This is a concrete error that undermines confidence in the reporting of results.

- **Comparisons on singular/oscillatory functions conflate architecture advantage with compute advantage.** Sections 3.4 and 3.5 compare KAN and MLP at "the same number of epochs" (lines 127, 137), but Tables 3 and 4 show KAN is 9–70× slower per epoch than MLP. For example, fitting f7 with Adam: MLP takes 4.3s, KAN takes 38.5s; fitting f9: MLP+Adam takes 4.6s while KAN+L-BFGS takes 237.6s (a 52× gap). When the paper reports that "KAN outperformed MLP" (Figure 6, Figure 8), it is comparing after giving KAN vastly more compute. The conclusion that KAN converges faster on these functions is based on training steps, not wall-clock time or FLOPs. The time data is presented in separate tables but never incorporated into the comparison methodology.

- **No statistical significance anywhere in the paper.** Every experiment appears to be a single run with no reported variance, confidence intervals, or standard deviations across random initializations. For a purely empirical study making comparative claims (e.g., "MLP outperforms KAN on f3–f6," "Adam exceeds L-BFGS for both networks except f9"), this is a fundamental gap. Given the small models and simple 1D functions, running multiple seeds (at least 10) would be trivially feasible and is standard practice for empirical comparisons.

- **Noise evaluation pipeline is critically underspecified.** The paper introduces noise to functions (Section 4) but does not specify: (a) the noise distribution (Gaussian? uniform? other?), (b) the SNR definition (values 0, 4, 10 appear in figure captions but are never defined in text), (c) whether test loss is computed against the clean underlying function or the noisy observations, or (d) whether any regularization or early stopping was used to prevent overfitting. If test loss is measured against noisy data, lower loss could simply reflect memorizing noise. Without these details, the noise experiments (Figures 9–11) do not support the conclusions drawn from them.

### Minor

- **Experimental scope is limited.** All experiments are on 1D scalar functions with a single hidden layer. The paper's own framing correctly notes that in real applications, "the features of these functions are typically not available as prior knowledge" (line 49), yet the experimental setup provides the kind of controlled toy setting where architectural differences are most apparent. Extrapolating these 1D results to the high-dimensional, structured problems motivating the KAN vs MLP debate is speculative. The contribution would be strengthened by at least one 2D function or a small-scale realistic task.

- **Test set details are absent.** The paper uses "test loss" as its primary metric throughout but never states the test set size, how it is constructed, or whether it is drawn from the same distribution as the training data (with or without noise). This is basic experimental hygiene.

- **KAN hyperparameters (grid=3, k=3) are fixed without ablation.** The spline grid size and order directly control KAN's capacity and smoothness. An ablation varying these parameters (or reporting the best found via simple search) would strengthen the claim that observed KAN underperformance on f3–f6 is architectural rather than attributable to a suboptimal hyperparameter choice.

- **MLP activation function is not explicitly stated.** The paper describes MLP architectures (e.g., [1,39,1]) but never specifies the activation function. It appears to be ReLU by convention, but this should be explicit.

## Removed Points

These points from the inputs were filtered out as noise, speculation, or violations of the filtering rules. Treat them with caution.

- *"The paper cites numerous KAN application papers without critically engaging with them—this reads more as a show of literature volume."* — Removed as a stylistic/presentation criticism about literature survey style that does not bear on correctness or soundness of the experiments themselves.

- *"The conclusion that 'raising the sampling rate is a potent method to enhance fitting performance for f1–f6' is based on a small set of functions and a narrow sample range (50–5000)."* — Removed as nitpicky: 50–5000 spans two orders of magnitude and is reasonable for a controlled study; the sample size criticism is already covered by the limited-scope weakness.

- *"The conclusion that 'Adam exceeded L-BFGS in performance for both networks in every instance except f9' is drawn from limited runs without statistical testing."* — Subsumed by the broader no-statistical-significance weakness above (duplicate).

- *"The paper's own gap ('imperfections of KANs') is already established in prior work (Zhang 2024, Shen et al. 2024, Yu et al. 2024); the incremental contribution is unclear."* — This conflates existence of prior claims with the value of independent empirical verification. The paper's contribution is in systematically testing *when* the imperfection manifests across function types, which is not redundant with prior work.

- *Strength Finder claimed "the text claims are the authoritative source" about the Figure 3 contradiction.* — The contradiction is real; the review treats it as such regardless of which side is correct.

- *Various formatting/presentation nitpicks from the harsh critic about figure readability, grammar, and writing style.* — Removed per format-filtering rules (these are parser artifacts or stylistic judgments).

- *"Noise magnitude calibration: the paper treats noise uniformly across functions"* — The paper uses SNR values; different absolute noise levels for different function scales is a consequence of SNR specification, which is standard practice. This criticism overreaches.

## Nice-to-Haves

- **Multi-seed reporting** (mean ± std over at least 10 random seeds) would transform the reliability of every quantitative claim in the paper. This is the single highest-impact improvement.
- **Compute-fair comparison** — comparing at equal wall time or equal FLOPs (not equal epochs) for f7–f10 would clarify whether KAN's apparent advantage is architectural or simply a compute budget artifact.
- **Clarifying the noise evaluation pipeline** — specifying noise distribution, test loss target (clean vs. noisy), and whether early stopping/regularization was used — would make the noise experiments interpretable.
- **Ablation on KAN grid size and spline order** would strengthen claims about which function types favor which architecture.
- **One higher-dimensional experiment** (e.g., a 2D function or a small symbolic regression benchmark) would substantially increase the paper's relevance.

## Novel Insights

None beyond the paper's own contributions. The two synthesizers did not surface an observation about the paper that the paper itself does not already state.

## Suggestions

1. **Resolve the Figure 3 contradiction immediately.** Determine whether the caption or the text is correct, fix the error, and ensure all figure-caption pairs are consistent.
2. **Report multi-seed statistics.** Add mean ± std over at least 10 random initializations for all experiments. This is quick (the models are small) and would address the single most concerning methodological gap.
3. **Add a compute-fair comparison for f7–f10.** Either compare at convergence (where both models plateau) or report results at equal wall time alongside the epoch-based comparison. Discuss the time gap explicitly when making claims about convergence speed.
4. **Specify the noise evaluation pipeline.** State the noise distribution, how test loss is computed (clean vs. noisy target), and whether any regularization is applied.
5. **State the test set size** and how it was constructed, for every experiment.
6. **Explicitly state the MLP activation function** and consider a brief ablation of KAN grid/spline parameters.

## Score and Decision

**Calibration protocol summary:**

**Round 1 (bracketing):** Three queries across KAN-vs-MLP empirical comparisons. Weak anchors (<3.5): KAE (3.0, withdrawn), KAN variable basis (2.5, withdrawn), TabKANet (3.0, withdrawn). Middle anchors (3.5–7.5): KAN expressiveness/spectral bias (6.25, accepted poster), KAAN (4.25, rejected), KAT (6.8, accepted poster). Strong anchors (>7.5): KAN original (7.2, oral), convex duality (8.0, oral), noisy interpolation (8.0, spotlight). The paper is clearly far below the strong anchors and below the middle anchors with theoretical contributions. The relevant comparison band is the lower portion of the middle band and the weak band. Initial bracket: [2.5, 5.0].

**Round 2 (narrowing inside bracket):** Focused queries on empirical KAN/MLP studies with limited scope. Legendre-KAN (3.5, rejected) — proposes a new variant but limited to symbolic tasks, no noise analysis, comparable scope to our paper. KAAN (4.25, rejected) — new architecture, tested on real benchmarks (tabular, CIFAR-10), has compute-fairness concerns. KAE (3.0, withdrawn) — straightforward KAN application, criticized for insufficient experiments. UKAN (5.33, rejected) — novel algorithm with GPU acceleration. Our paper is pure empirical (no new method), purely 1D, has a verified caption contradiction, and lacks multi-seed statistics. It is weaker than Legendre-KAN (3.5) which at least proposes something new, and comparable to KAE (3.0) in terms of contribution strength and execution quality. The paper sits at the lower end of the bracket.

**Round 3:** Single query to verify placement between 2.5 and 4.5 confirmed the paper is below KAAN (4.25) and comparable to Legendre-KAN (3.5) and KAE (3.0).

**Final score:** 3.0 — The paper asks a reasonable question and provides a useful function taxonomy, but the execution has multiple significant problems (caption contradiction that prevents determining a key result, compute-fairness confound, no statistical significance, underspecified noise evaluation) that prevent the claims from being reliably supported. A revision fixing these issues could plausibly reach the 4–5 range, but in its current form the evidence is not trustworthy enough to inform the community.

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>
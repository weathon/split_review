Now I have sufficient calibration context. Let me produce the final review.

## Summary

This paper provides a theoretical and empirical analysis of Multi-Grade Deep Learning (MGDL), which decomposes end-to-end training into sequential shallow "grades" trained on residuals. The contributions include convergence theorems for GD on MGDL, a convexity result for single-layer ReLU grades, eigenvalue-based stability analysis showing MGDL's iteration matrix eigenvalues stay within (-1,1), and experiments on image regression, denoising, deblurring, CIFAR classification, and transformer-based time-series forecasting.

## Strengths

1. **Consistent empirical advantage across diverse tasks (Tables 1–5, Figures 2–8).** The paper demonstrates MGDL outperforming standard end-to-end training on image regression (0.42–3.94 dB PSNR gains), denoising (0.16–4.23 dB), deblurring (0.85–2.84 dB), and time-series forecasting with transformers (MGT test MSE 1.8×10⁻² vs SGT 8.9×10⁻²). The breadth of tasks—coordinate-based regression, image restoration, and financial time series—shows the method's versatility.

2. **Eigenvalue analysis provides a mechanistic explanation for stability differences (Section 7, Figures 4–6).** The paper tracks the eigenvalues of I − ηH(W) during training and shows that SGDL's eigenvalues exit (−1,1) while MGDL's remain within it, directly correlating with oscillatory vs. stable loss decay. This pattern is confirmed across synthetic regression, image tasks, and CIFAR-10, giving a concrete testable mechanism.

3. **Quantified learning-rate robustness (Section 6, Figure 2).** The paper systematically maps the usable learning-rate interval for both methods, showing MGDL remains stable over a much wider range (e.g., η ∈ [0.08, 0.3] for high-frequency targets) compared to SGDL (η ≈ 0.005 only). This quantifies the robustness advantage rather than merely claiming it.

4. **Extension of MGDL to transformers (Section 8, Tables 4–5).** The demonstration that multi-grade training benefits transformer architectures on time-series forecasting represents a nontrivial architectural generalization of the MGDL idea.

## Weaknesses

### Major

1. **No test accuracy reported for CIFAR-10/100 classification (evidential gap).** The paper claims in the contributions list and throughout that MGDL "consistently outperforms SGDL with greater stability" on classification. The CIFAR-100 section (line 223) states it evaluates "in terms of both accuracy and training dynamics," and the conclusion claims "better accuracy." Yet the paper reports **only training loss curves** for CIFAR-100 (Figure 3) and training loss plus timing for CIFAR-10 (Section 7). No test accuracy, Top-1 error, confusion matrices, or any metric that measures classification performance is provided. Training loss is not a proxy for accuracy on classification benchmarks. This single gap directly undermines the paper's claim to have demonstrated MGDL's advantage on classification tasks, which is listed as a core contribution (item 3 in contributions list).

2. **No statistical significance, repeated trials, or error bars (evidential gap).** Every quantitative result in the paper (Tables 1–5) reports a single run. There is no mention of random seeds, standard deviations, or confidence intervals anywhere. Given that MGDL involves sequential training where earlier-grade solutions determine later-grade inputs, variance across runs could be significant. Without repeated trials, the reader cannot assess whether the reported PSNR gains (e.g., 0.42–3.94 dB in Table 1) are reliable or within run-to-run noise. For a paper whose central claim is that one method *consistently* outperforms another, the absence of any statistical evidence is a serious weakness.

3. **Convexity theorem (Theorem 3) does not apply to the main experiments (structural disconnect).** Theorem 3 proves that when *each grade* is a *single hidden-layer* ReLU network, the nonconvex problem reduces to a sequence of convex subproblems. The proof is clearly scoped to single-layer grades (line 116: "when each grade in MGDL is realized as a single hidden-layer ReLU network"). However, every main performance experiment uses grades with 2–3 hidden layers per grade (architecture 27 specifies n_h=2 for image regression in line 156; n_h=3 for denoising/deblurring in line 164). The convexity result is therefore irrelevant to the empirical findings it is presented alongside. The framing "extending convexification from shallow to deep architectures" (line 148) implies broader reach than what is actually proved. The paper should explicitly acknowledge this gap rather than presenting theory and experiments as mutually reinforcing.

### Minor

4. **Theorems 1 and 2 are standard GD convergence results with an unproven claim.** Theorem 1 (GD with η < 2/α converges to a stationary point for smooth nonconvex objectives) is textbook material (Nesterov's classical analysis). The paper's distinguishing claim (line 112) is that αₗ ≪ α (much smaller Hessian spectral norm for shallow grades), implying a larger admissible learning rate. However, no bound on αₗ/α is derived, no architecture-specific analysis is given, and the statement "thereby improving stability and robustness compared to SGDL" is asserted without proof. The eigenvalue analysis in Section 7 provides *empirical* support for this claim (by showing MGDL eigenvalues stay in (−1,1)), but the theorems themselves do not establish it.

5. **Missing ablation: training shallow networks independently as an ensemble.** The paper compares MGDL against standard end-to-end training but does not include a baseline where the shallow grade networks are trained independently (not sequentially on residuals) and combined as an ensemble. This ablation would isolate whether MGDL's advantage comes from the sequential residual-fitting structure or simply from the fact that optimizing shallow networks is easier regardless of training protocol. Without this baseline, the mechanism behind MGDL's gains is less certain.

6. **Eigenvalue analysis is descriptive, not predictive.** The eigenvalue analysis (Section 7) shows that MGDL's eigenvalues stay in (−1,1) while SGDL's exit this range, but this is observed *after* training, not derived from architectural properties. The claim that "the shallower structure of MGDL keeps them inside (−1,1)" (line 259) is a plausible post-hoc explanation but is never established theoretically. Theorem 4 itself is a standard linearization argument. The analysis explains *that* MGDL is more stable but does not predict *under what conditions* the eigenvalue gap closes.

### Trivial

7. The architecture definitions (equations 26–29) are referenced but not shown in the main text; a brief summary of model sizes (total parameter counts for SGDL vs. MGDL) would help readers assess whether the comparison is parameter-matched. (The appendix was stripped by the parser, but this should ideally be in the main text.)

## Nice-to-Haves

- A principled bound on αₗ/α (the Hessian spectral norm ratio between shallow grades and the full deep network) would turn the heuristic claim in Theorem 2 into a genuine theoretical contribution.
- Measuring gradient norms per layer across methods would directly address the paper's claim about mitigating vanishing/exploding gradients.
- Including the ensemble-of-shallow-networks baseline mentioned in weakness 5 would strengthen causal interpretation.

## Removed Points

These points were raised by the reviewers but removed after verification against the paper:

1. *Missing baselines (greedy layer-wise pretraining, ResNet):* The paper's stated scope is MGDL vs. SGDL; requesting every related architectural innovation is scope creep. However, the specific ensemble ablation (kept as weakness 5) is directly relevant. (Removed because it conflates scope creep with a valid ablation concern.)

2. *Theorems 1-2 are "not novel":* While these are standard results, many papers include them for self-containedness. The issue is the overclaiming about αₗ ≪ α (kept as weakness 4), not the theorems themselves. (Partially merged into weakness 4.)

3. *MGT faster than SGT contradicts linear scaling claim:* The paper says training time "scales linearly with the number of grades" but does not claim it is slower than SGDL. MGT is faster because per-grade convergence is dramatically faster. This is internally consistent. (Removed as factually incorrect criticism.)

4. *FC networks are niche for image regression:* Using coordinates-to-intensity mapping is a well-established approach in the implicit neural representations literature. The paper's choice does not invalidate the results. (Removed as scope creep / opinion.)

5. *No spectral bias measurement:* The paper mentions spectral bias in the introduction but does not claim to measure it. Claiming its absence is a criticism of an unstated goal. (Removed because the paper's claims are about stability and accuracy, not about spectral bias quantification.)

6. *Pure formatting nitpicks* (typos, missing labels, figure readability, line break issues): These are parser artifacts from PDF extraction, not author errors. (Removed per hard rules.)

## Novel Insights

None beyond the paper's own contributions. The reviewers' analyses largely recapitulate the paper's claims without identifying genuinely new connections the authors missed.

## Suggestions

1. **Report test accuracy for CIFAR-10/100.** This is the single highest-leverage addition. Without it, the classification claim is unsupported and the paper cannot deliver on a listed contribution.

2. **Add repeated trials (≥5 seeds) with error bars** to Tables 1–5. The paper claims *consistent* superiority, which demands statistical evidence.

3. **Acknowledge the gap** between the single-layer convexity result and the multi-layer experiments, and either (a) extend the theory to deeper grades or (b) adjust the claims to match what is actually proved.

4. **Add the ensemble ablation** (training shallow networks independently vs. sequentially on residuals) to disentangle whether the advantage comes from the sequential structure or from having shallower networks.

5. **Move the architecture details into the main text** so readers can verify parameter counts are matched between MGDL and SGDL.

---

## Calibration Anchors

**Round 1 bracketing** placed the paper between 4.0 and 6.0.

**Round 2 narrowing anchors (all from the middle band):**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| `OZZYqfplS3.md` (PC Stability) | 4.00 | R1 | This paper is empirically stronger but has similar theory-practice gaps; both were rejected. Slightly better than this anchor. |
| `MY8SBpUece.md` (Feature Learning) | 5.50 | R1 | This anchor has rigorous theory but limited scope, and was rejected. The current paper has weaker theory but broader experiments; comparable overall quality. |
| `J4Dvxv7WnG.md` (Deep MF EOS) | 7.00 | R1 | This anchor was accepted with both rigorous theory and experiments. The current paper is clearly weaker. |
| `zPaTnGjgpa.md` (Stability/Instability) | 4.20 | R1,R2 | Similar eigenvalue analysis but this anchor has more causal claims; current paper slightly better due to broader experimental validation and honest descriptive framing. |
| `kiwyQsZIGP.md` (Few-Shot Eval) | 5.00 | R2 | Different topic; used for general quality calibration of papers with evidential gaps. |
| `55EO8gSCBT.md` (Nonstationary Opt.) | 5.50 | R2 | Methodologically rigorous but rejected for scope issues; current paper has broader empirical claims but similar methodological gaps. |
| `UMOlFJzLfL.md` (SGD Stability) | 5.75 | R2 | Accepted despite limited experiments due to novel, rigorous theory. Current paper has weaker theory and significant evidential gaps, making it clearly weaker. |
| `O0FOVYV4yo.md` (Local PL) | 5.00 | R2 | Rejected; focused theoretical paper. Current paper comparable in overall quality. |

**Narrowing decision:** The paper sits between the 4.00 PC anchor and the ~5.5 feature learning anchor. It is empirically broader than the PC paper but has the same theory-practice gap. It is weaker than the 5.75 SGD stability paper (which was accepted for its rigorous novel theory) and weaker than the 5.50 feature learning anchor (which at least had rigorous proofs). The evidential gap on classification (no test accuracy) and absent statistical rigor are decisive: they prevent the paper from reaching the 5+ range where borderline-acceptable papers sit. **Final score: 4.5.**

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
Now let me do calibration searches to score this paper.Round 1 bracket: **3–5**. Now let me read one anchor per band and narrow.Now I have enough calibration. Let me read one of the round-2 anchors at score 4.0 to finalize:Now I have enough material. Let me write the final consolidated review.

---

## Summary
STNAdam is a stochastic Adam variant for "nonconvex + weakly-convex" composite optimization that couples two iteration trajectories — an extrapolation track driven by Nesterov momentum and a regular update track — both conditioned by Adam-style adaptive step sizes. Under the Kurdyka–Łojasiewicz (KL) property, the paper establishes convergence in expectation to a stationary point and provides explicit rates depending on the KL exponent. The method supports plug-in variance-reduced gradient estimators (SGD, SAGA, SARAH) and is empirically evaluated on low-light image enhancement (LIE) using the LOL dataset.

---

## Strengths

- **Novel two-track iterative framework**: Algorithm 1 and Figure 1 concretely distinguish STNAdam from single-track variants (NAG, Adam, NAdam) by maintaining coupled extrapolation and update trajectories. The mechanism — enlarging the update neighborhood while continuously refining the descent direction — is clearly motivated and algorithmically non-trivial.

- **Rigorous convergence analysis under general conditions**: The convergence theory is genuinely non-trivial. Lemma 2 establishes expected decrease of an energy function (Eq. 9), Theorems 1 and 2 respectively give convergence in expectation to a stationary point and explicit convergence rates for three KL exponent regimes ($\vartheta \in (0,\frac{1}{2}]$, $(\frac{1}{2},1)$, $\vartheta=0$). The unification of SGD, SAGA, and SARAH through a single set of estimator conditions (Lemma 1) is elegant.

- **Modular variance-reduction compatibility**: The formulation in Lemma 1 cleanly abstracts away the gradient estimator, enabling direct instantiation with SAGA and SARAH without re-deriving the convergence. This is practically valuable and theoretically tidy.

- **Consistent gains over single-track optimizers**: Table 2 shows STNAdam-SGD (PSNR 18.06) outperforming SNAdam (17.14) and SAdam (16.38) using the same task and model, providing at least a partial signal that the two-track structure contributes positively.

---

## Weaknesses

### Fatal
*None.*

### Major

- **Two-track contribution is not experimentally isolated from variance reduction.** The paper's signature claim is that the two-track coupled iteration is the key innovation. In Table 2, the gap between STNAdam variants is dominated by the choice of gradient estimator: STNAdam-SARAH (22.26) vs. STNAdam-SAGA (21.05) vs. STNAdam-SGD (18.06) — a 4.2 dB spread driven by variance reduction. The two-track structure's independent contribution, by contrast, appears only in STNAdam-SGD vs. SNAdam (18.06 vs. 17.14, both using vanilla SGD), which is 0.9 dB. Without a control that applies variance reduction *without* the two-track structure (e.g., a single-track NAdam-SAGA or NAdam-SARAH baseline), the paper cannot attribute performance gains to the two-track design versus the well-established variance-reduction effect. This is the ablation most directly needed to support the central claim.

- **Timing results are implausible and unexplained.** Table 2 reports STNAdam-SARAH as *the fastest* method at 2.64e-05 s, faster than plain SGD (2.85e-05 s) and SNAdam (2.81e-05 s). SARAH requires periodic computation of full gradients and the two-track framework executes two proximal steps per iteration, so STNAdam-SARAH should be categorically more expensive per iteration than SGD in any realistic setting. The paper does not define what "Time(s)" measures — per-iteration, per-epoch, total training time, or inference time — and provides no explanation for this result. Without clarification, the timing column undermines trust in the quantitative results generally.

- **Evaluation is too narrow for the paper's stated scope.** The Introduction and contributions explicitly position STNAdam as an Adam enhancement for modern deep learning tasks (Section 1, 1.2). All empirical evidence, however, comes from a single application (low-light image enhancement) on a single dataset (LOL). No classification, NLP, or other standard benchmark appears. The LIE energy minimization model (Eq. 14) is a relatively small-scale structured inverse problem, not representative of the large-scale deep-learning settings the Introduction invokes. The gap between scope and evidence is a significant mismatch.

- **Citation error: SAdam is misattributed to "Kingma & Ba (2014)" in Table 2.** Kingma & Ba (2014) is the original Adam paper. SAdam was developed by Wang et al. (2019) for strongly convex problems and extended by Le-Duc et al. (2024) for nonconvex+convex settings, both of which are correctly cited in Section 1.1. The misattribution in Table 2 creates uncertainty about which algorithm was actually implemented as the SAdam baseline. Additionally, SNAdam is attributed to "Reddi et al. (2019)" in Section 1.1 but to "Xie et al. (2024)" in contribution (iii) and Table 2 — these are two different algorithms (AMSGrad vs. SAdan), and it is unclear which version was run.

### Minor

- **Abstract overstates convergence guarantee.** The abstract states that STNAdam "almost surely converges to a stationary point." However, Theorem 1(ii) — the main convergence result — establishes that the sequence $\{\bar{x}^k\}$ converges to a stationary point *in expectation*, not almost surely. Almost-sure (a.s.) properties appear in Lemma 4 (items 1 and 5) for auxiliary sequences, but the main stationarity claim in Theorem 1 is in expectation. This distinction is material and the abstract should be corrected.

- **Dynamic parameter scheduling still requires unknown problem constants.** The paper claims in contribution (ii) that hyper-parameters "can be dynamically scheduled within some iterate-dependent finite intervals, removing hand-tuning." However, the lower bound $\underline{\gamma}$ in Eq. (6) depends on $V_1$, $V_\Upsilon$, $\rho$ (estimator constants from Lemma 1), and $M$, $s$ which depend on Lipschitz constant $L$ and weak-convexity modulus $\tau$ per Lemma A.1. Similarly, $\underline{\lambda}$ in Eq. (7) requires $L$ and $\tau$; Eq. (8) requires both $L$ and $\tau$ explicitly. The paper does not describe how these constants are estimated in the LIE experiments. Remark 3 acknowledges this obliquely ("the moduli $L$ and $\tau$ are appropriately increased if necessary") but does not resolve it. The "removes hand-tuning" claim is overstated.

- **Convergence proof outline skips Step 4 in main text.** After Step 3 (Lemma 5, p. 7), the text jumps directly to "Step 5" (Theorem 2), with no Step 4 visible in the main body. This makes the proof structure difficult to follow for readers of the main paper alone.

### Trivial
- The comparison in Table 2 with NPE, DeHz, LIME, LR3M, Retinex-Net mixes these purpose-built LIE algorithms (with different objective formulations and model architectures) against general-purpose optimizers applied to the LR3M objective. The table is useful context but should not be interpreted as evidence about optimizer quality relative to those methods.

---

## Nice-to-Haves

- Adding TNAdam-SAGA and TNAdam-SARAH (single-track variants with variance reduction but without the two-track structure) would provide the direct ablation needed to isolate the two-track contribution.
- Convergence curves (objective value vs. iterations) would make the practical advantage of the two-track structure intuitive.
- A brief discussion connecting the KL exponent $\vartheta$ in Theorem 2 to the specific LIE objective would help make the theory feel less disconnected from the experiments.
- Extending experiments to at least one standard deep-learning benchmark (e.g., image classification or language modeling) would better support the paper's general-purpose framing.
- A precise definition of what "Time(s)" measures in Tables 2–3.

---

## Removed Points
*These points are flagged as removed; treat them with caution.*

- **"Removes hand-tuning" as a full strength**: The strength finder calls the dynamic parameter scheduling "a non-trivial feature for an accelerated adaptive method" and a removal of manual tuning. This conflicts with the verified weakness that the intervals depend on $L$ and $\tau$. The strength is demoted to a minor weakness.

- **"Almost-sure convergence" as a strength**: The strength finder lists "almost-sure global convergence to a stationary point" as a strength. As verified against Theorem 1(ii), the convergence claim is in expectation. The a.s. property (Lemma 4, items 1 and 5) applies to the distance-to-accumulation-set, not to stationarity of the limit point. Removed as stated.

- **Comparison with NPE/DeHz/LIME/Retinex-Net as optimizer evaluation**: Removed as a framing concern only (the harsh critic raised this as a failure of evaluation validity, but the paper simply includes these as reference points for the image quality obtained; the core optimizer comparison is within the SGD/SAdam/SNAdam/STNAdam group, which is appropriate).

- **"Reproducibility: missing mini-batch sizes and SARAH reset frequency"**: Removed per hard rule on reproducibility nitpicks for implementation details.

---

## Novel Insights

The idea of coupling two iteration trajectories in an Adam-style optimizer — one doing exploratory Nesterov extrapolation and another doing a refined proximal update — is a genuinely original structural contribution to the accelerated Adam literature. The observation that this framework can be paired with any variance-reduced gradient estimator through a unified abstract condition (Lemma 1), and that the parameter schedules' lower bounds can be derived from the convergence proof itself, is an interesting design principle worth developing further. However, the paper's current experimental validation does not yet demonstrate that the two-track structure provides benefits beyond what variance reduction alone achieves.

---

## Suggestions

1. **Add single-track variance-reduced baselines**: Run NAdam-SAGA and NAdam-SARAH on the LIE task. This is strictly within the paper's existing scope and will directly demonstrate (or quantify) the two-track advantage independent of variance reduction.
2. **Clarify and fix the timing column**: Define what "Time(s)" measures and explain why STNAdam-SARAH appears faster than SGD.
3. **Correct the SAdam and SNAdam citations** in Table 2 to match what was actually implemented; verify the two are distinct algorithms.
4. **Align the abstract with Theorem 1**: Change "almost surely converges" to "converges in expectation" in the abstract.
5. **Discuss how $L$ and $\tau$ are estimated** in the LIE experiments; this is necessary to evaluate whether the "removes hand-tuning" claim is practically meaningful.

---

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `Og7ZZd7hDm.md` (Federated Composition Optimization) | 3.25 | R1 (low) | Rejected; similar theoretical scope, comparable evaluation narrowness |
| `5nldnvvHfw.md` (Adaptive Exponential Decay for Adam) | 2.50 | R1 (low) | Rejected; weaker theory, no rigorous convergence; STNAdam is stronger here |
| `mEBSeSk49H.md` (Adam under Non-uniform Smoothness) | 4.25 | R1/R2 (mid) | Rejected; pure theory, separates Adam from SGDM; comparable theoretical depth but broader scope |
| `CVldG5ohCy.md` (Adam through Second-Order Lens) | 4.00 | R2 (mid) | Rejected; evaluates on multiple regression + classification tasks at various scales; STNAdam has deeper theory but far narrower experiments |
| `6rEcB9m9AI.md` (Memory-Augmented Adam) | 4.75 | R2 (mid) | Rejected; evaluated on ImageNet; broader experimental scope than STNAdam |
| `AqHbMV28o7.md` (Stochastic Proximal Point Methods) | 4.50 | R2 (mid) | Rejected; comprehensive analysis, broader framework; comparable depth |
| `n3TkrH7fEr.md` (Inexact Stochastic Proximal Point) | 6.25 | R1 (mid, upper) | Accepted; tighter assumptions and broader convergence guarantees, cleaner overall |
| `xxaEhwC1I4.md` (Last-Iterate Convergence of SGD) | 6.67 | R1 (mid, upper) | Accepted; broader theoretical contributions, well-executed |

**Round 1 bracket**: 3–5.

**Round 2 narrowing**: Papers at 4.0–4.5 (Adam Second-Order Lens, Unified Stochastic Proximal Point) have either broader experimental evaluation or more comprehensive theoretical contributions. STNAdam's theory is non-trivial but the experimental section has three compounding major problems — an unexplained timing anomaly, a citation error for a baseline, and no ablation of the key claimed contribution. This pushes the paper below those anchors. The paper is above the "Adaptive Exponential Decay for Adam" (2.5) anchor because the convergence analysis and algorithmic novelty are genuinely more substantial. The paper sits between 3.25 and 4.0, closer to 3.5.

**Axes summary:**
- *Originality*: Moderate — two-track design is novel for Adam-style optimizers.
- *Importance of research question*: Moderate — relevant but niche (one application).
- *Claims well-supported*: Weak — central claim (two-track advantage) not ablated; timing anomalous; abstract overclaims a.s. convergence.
- *Soundness of experiments*: Weak — single task/dataset, unexplained timing column, citation errors in Table 2.
- *Clarity of writing*: Adequate — but has inconsistencies (Step 4 missing, abstract vs. theorem mismatch).
- *Value to research community*: Limited in current form — narrow scope and unvalidated key claim.

**Final score: 3.5 — Reject.** The paper has a genuine theoretical contribution but the empirical evidence for the key algorithmic claim is insufficient and the experimental section has multiple serious issues that need to be addressed before the paper can be accepted.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>
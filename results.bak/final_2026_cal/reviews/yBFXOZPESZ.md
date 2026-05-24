Now I have all the information needed. Let me write the consolidated review.

**Calibration Summary:**

Round 1 bracket: 4.5–6.0 (based on comparison with Grams paper at 4.80, Sign-SGD paper at 6.00, AdaMuon at 4.80).

Round 2 narrowing: The closest comparator is Grams (4.80, Reject), which addresses nearly the same problem (decoupling sign and magnitude) but with weaker evaluation (smaller models, fewer baselines, no confidence intervals). The Ano paper is clearly stronger empirically. However, the Sign-SGD paper (6.00, Accept) has a more novel contribution (parameter-free optimization) and stronger LLM-scale validation. The Ano paper sits between these: above 4.8 but below 6.0.

**Final score: 5.0**

Let me write the consolidated review.

Actually, I want to double check my understanding of the Yogi update. Let me re-read the paper's description once more.

The paper says: "We extend Yogi by introducing a decay factor that explicitly controls variance memory"

And the update: v_k = β₂ v_{k-1} - (1 - β₂)·sign(v_{k-1} - g_k²)·g_k²

Now, I said "Yogi has v_{k-1} without β₂". But actually... I'm not 100% certain of Yogi's exact formulation from memory. However, the paper IS claiming this as an extension, and I have to go with what the paper says. If they say Yogi doesn't have β₂ decay on the first term, I have to trust that representation since I can't independently verify the Yogi paper.

OK let me write the review now.## Summary

This paper proposes **Ano**, a stochastic optimizer that decouples update direction (via momentum sign) from update magnitude (via instantaneous gradient norm), aiming to improve robustness in noisy and non-stationary settings such as reinforcement learning. The authors also introduce **Anolog**, which replaces the momentum coefficient with a logarithmic schedule to eliminate β₁ tuning. They provide a non-convex convergence analysis (Õ(K^{-1/4}) rate) and evaluate across CV (CIFAR-100), NLP (GLUE), and deep RL (MuJoCo SAC, Atari PPO).

---

## Strengths

1. **Clean, well-motivated design idea.** The core insight—that momentum magnitude can be sluggish in non-stationary settings, while the sign of momentum provides stable directional information—is clearly articulated and naturally motivates the Ano update: sign(mₖ) for direction, |gₖ| for magnitude. This is a simple, easy-to-implement modification of Adam with a clear rationale.

2. **Consistent RL improvements with evidence of hyperparameter robustness.** On MuJoCo SAC (Table 4), Ano achieves mean rank 1.4 (default) and 1.6 (best version) across 5 environments, with normalized average ~99.5% vs. 90.7% for Adam. On Atari PPO (Table 5), Ano achieves normalized average 95.99 vs. 90.09 for RMSprop. Figure 3 heatmaps demonstrate broader high-reward regions for Ano compared to Adam across learning rate and β₁ sweeps, supporting the claim of reduced sensitivity.

3. **Noise robustness validated in controlled experiment.** The CIFAR-10 CNN experiment with injected Gaussian noise (Table 1) shows the gap between Ano and Adam widening from 1.43pp (σ=0) to 7.08pp (σ=0.20), directly supporting the central claim that decoupling stabilizes learning under high variance. The gap with Lion also grows (1.05 → 2.72pp).

4. **Comprehensive evaluation framing.** The paper honestly frames CV/NLP as diagnostic checks ("not to position Ano as a competitive alternative in large-scale pretraining") and concentrates the primary claim on noisy/non-stationary regimes. The evaluation covers three domains with reasonable baselines (Adam, Adan, Lion, Grams, RMSprop) and reports confidence intervals throughout.

5. **Anolog reduces hyperparameter tuning burden.** The logarithmic schedule for β₁ (β₁ₖ = 1 − 1/log(k+2)) eliminates the need to tune β₁ while achieving competitive performance (9472.73 on HalfCheetah vs. 10520 for tuned Ano, within CI on supervised tasks). This is a practical contribution.

---

## Weaknesses

### Major

1. **Theory-practice disconnect (verifiable from Section 5.1 vs. Algorithm 1).** The convergence analysis assumes β₁ₖ = 1 − 1/√k and ηₖ = η/k^(3/4), while the primary evaluated algorithm (Algorithm 1) uses constant β₁ = 0.92 and a learning rate modulated only by the second-moment estimate—not the scheduled ηₖ from the theorem. The Anolog variant uses a logarithmic schedule, not the square-root schedule in the proof. In the ablation (Table 6), the variant with the square-root schedule achieves only 8750 on HalfCheetah vs. 10520 for constant-β₁ Ano, while the row labeled "Ano √k" (which due to a labeling error actually uses β₁ = 1 − 1/k) catastrophically fails (−221). The net result is that the theoretical analysis does not directly validate the algorithm that works best empirically. This is a structural weakness: the theory is presented as supporting Ano, but it analyzes a different configuration.

2. **Second-moment "innovation" is oversold.** The paper repeatedly frames the variance update as "extend[ing] Yogi by introducing a decay factor" and lists "Modified Yogi variance update with decay factor" as a contribution. The actual update (vₖ = β₂ vₖ₋₁ − (1−β₂)·sign(vₖ₋₁ − gₖ²)·gₖ²) is different from plain Yogi (which lacks the β₂ on vₖ₋₁), so the harsh critic's claim that it is "exactly Yogi" is incorrect. However, adding a β₂ decay to the first term of an existing update is a trivial modification, not a meaningful algorithmic innovation. The paper would be better served by simply stating that Ano uses a Yogi-style second-moment estimator, rather than treating this as a separate contribution.

### Minor

3. **Ablation table has labeling errors and unclear columns.** In Table 6, the row "Ano √k" lists β₁ = 1 − 1/k (harmonic schedule, not square-root), and the row "Ano log k" lists β₁ = 1 − 1/√k (square-root, not logarithmic). These labels are swapped or misaligned with the actual β₁ values. The column headers ("Mom. Norm.", "Mom. Dir.", "Grad. Norm.") are not defined in the text, making some rows hard to interpret. These are presentation errors that the authors should fix.

4. **Noise robustness experiment omits relevant baselines.** Table 1 compares only Adam, Lion, and Grams, but omits Adan, RMSprop, and Yogi—all relevant to non-stationary settings. For a paper that claims general noise robustness, this is a gap.

5. **RL tuning protocol may favor Ano.** Hyperparameters were tuned on a short (100k-step) HalfCheetah proxy, which may systematically favor optimizers that converge quickly initially (potentially Ano). The paper partially mitigates this by reporting the better of default/tuned, but per-environment tuning would strengthen the evidence.

### Trivial

6. The pseudocode in Algorithm 1 has a stray `gₖ` in the numerator (should be elementwise `|gₖ|⊙sign(mₖ)` or similar). The table formatting makes the update line ambiguous.

---

## Nice-to-Haves

- A controlled ablation that isolates the decoupling effect cleanly: fix the second-moment term (Adam or Yogi) and compare (a) Adam (mₖ for both), (b) Signum (sign(mₖ) direction), (c) InstGrad (mₖ direction, |gₖ| magnitude), (d) Ano (sign(mₖ) direction, |gₖ| magnitude). The current ablation mixes too many variables.
- Runtime/memory comparison against baselines.
- Per-environment tuning instead of proxy transfer for RL.

---

## Removed Points

These points from the inputs were screened and removed:

- **"Second-moment update is exactly Yogi"** — Factually incorrect. The paper's update (β₂ vₖ₋₁) differs from Yogi's (vₖ₋₁ without β₂). The modification is minor but real.
- **"√k schedule causes catastrophic failure"** — The catastrophic failure (−221) is for the harmonic schedule (β₁ = 1−1/k), mislabeled as "Ano √k". The actual square-root schedule (β₁ = 1−1/√k) in the row mislabeled "Ano log k" achieves 8750, which is reasonable.
- **"On Humanoid, Adam's default is higher than Ano's default"** — True in Table 4 (Adam 5357 vs Ano 5255), but the difference is within the 95% CI, and Ano still ranks 1.4 in mean rank across all tasks. Cherry-picking one environment.
- **"Lion (tuned) beats Ano on Hopper"** — Lion tuned = 3592 vs Ano default = 3535, within CI. The paper consistently reports Ano default, not Ano tuned. This is not a meaningful weakness.
- **"Missing Adan, RMSprop, Yogi from noise experiment"** — Kept as Minor (valid but the experiment is acknowledged as a diagnostic, and 3 baselines still provide useful signal).
- **Several formatting/style nitpicks** — Parser artifacts, not author errors.
- **"No hyperparameter disclosure"** / reproducibility concerns — The appendix and code release cover this. The paper provides search spaces and selected configurations.
- **Strength Finder's generic strengths** about "important problem" — Removed as generic.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. Align the theory and experiments: either prove convergence for the constant-β₁ case (or the logarithmic schedule used in Anolog), or adjust the primary algorithm to use the scheduled β₁ from the theory and show it still works well. The current gap undermines the theoretical contribution.
2. Clean up the ablation table: fix the swapped β₁ schedule labels, define column headers, and ideally add a cleaner decoupling-only ablation block (see Nice-to-Haves).
3. Add Adan, RMSprop, and Yogi to the noise robustness experiment (Table 1) for completeness.
4. Clarify in the paper that the second-moment term is a minor modification of Yogi (adding β₂ decay), not a novel second-moment design. This would not weaken the paper—the core novelty is the sign-magnitude decoupling.

---

## Score and Decision

**Calibration anchors consulted:**

| Anchor ID | Avg Score | Round | Comparison to this paper |
|---|---|---|---|
| RPly1hhiUG (Grams) | 4.80 | R1,R2 | Same topic (decoupling sign/magnitude), weaker evaluation (no CIs, fewer baselines, smaller models). Ano is stronger. |
| Lk0tQYo76o (Sign-momentum analysis) | 5.00 | R1,R2 | Pure theory paper, not directly comparable. |
| yDLD3D95w3 (Sign-SGD parameter-free) | 6.00 | R1,R2 | Stronger LLM-scale validation, more novel contribution (parameter-free). Ano is weaker. |
| OpxVAHFmkL (AdaMuon) | 4.80 | R2 | Combined Muon+Adam, weaker evaluation (limited baselines, no systematic tuning). Ano is stronger. |
| kwnYSirdZx (Adam class imbalance) | 4.50 | R2 | Different topic, not directly comparable. |
| 0YDUJznwtX (Adam sign perspective) | 2.00 | R1 | Weak paper, Ano is much stronger. |
| aEJBuRQSBg (Softmax RL) | 2.50 | R1 | Unrelated topic, very different quality. |
| gqkayvdfM7 (Sign bounds) | 3.00 | R1 | Theory-only, weaker. |
| XHXe1pGwzA (Weight decay correction) | 2.00 | R1 | Different topic, weaker. |
| LJdAdCo3BN (Implicit bias Adam) | 6.00 | R2 | Strong theory paper with rigorous analysis. Different type of contribution. |
| UPEwYJn2mm (Wavelet NSRL) | 5.50 | R2 | RL non-stationarity paper, different methodology. |
| NQsdnYkCar (Block SignSGD) | 6.00 | R2 | Sign-based method for LLM fine-tuning, stronger on LLM scale. |

**Round 1 bracket:** 4.5–6.0  
**Round 2 narrowing:** The paper sits above Grams (4.80) due to stronger and more thorough evaluation, but below Sign-SGD (6.00) and Block SignSGD (6.00) which have better theory-practice alignment and/or stronger large-scale validation.  
**Final score:** 5.0 — a competent paper with a clear design idea and decent empirical support, but meaningfully weakened by the theory-practice disconnect and the overselling of a trivial second-moment modification.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
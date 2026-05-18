Now I have good calibration. Let me write the consolidated review.

## Summary

This paper identifies *model-fitting* in diffusion guidance, where samples become over-optimized for the specific classifier used during sampling rather than generalizing to the intended condition. It proposes Compress Guidance (CompG), which applies guidance gradients only at a subset of timesteps (concentrated early in the process) and reuses them elsewhere. Experiments across ADM, CADM, DiT, GLIDE, and Stable Diffusion on ImageNet and MSCOCO show that CompG reduces the number of guidance steps by up to 5× while maintaining or slightly improving FID/sFID and reducing compute.

## Strengths

1. **Practical finding validated across multiple architectures.** The paper demonstrates that reducing guidance frequency can maintain or improve quality across five different model families (ADM, CADM, DiT, GLIDE, Stable Diffusion), both classifier and classifier-free guidance, and across multiple resolutions (64×64, 128×128, 256×256). This breadth suggests the effect is not an artifact of a single architecture (Tables I–IV).

2. **Polynomial scheduling ablation shows distribution matters.** By varying the exponent \(k\) in Eq. 15, the paper shows that concentrating guidance toward early timesteps systematically reduces the required number of guidance steps (from 50 at \(k=1\) down to 28 at \(k=6\)) while maintaining or improving FID (Table V, FID improving from 1.91→1.82). This demonstrates that *how* one distributes a fixed guidance budget is a meaningful design choice.

3. **Simultaneous quality and efficiency improvement in some settings.** On ImageNet 64×64 with ADM, CompG improves FID from 6.40 (vanilla guidance, 250 steps) to 5.91 (50 guidance steps) while reducing GPU hours from 54.86 to 31.80 (Table I). This simultaneously breaks the usual quality-efficiency trade-off, which is the paper's most compelling result.

4. **Simple and practical method.** The proposed technique (skip gradient computation at most timesteps, reuse the last computed gradient at skipped timesteps) is trivial to implement on top of existing pipelines and introduces no additional hyperparameters beyond the polynomial exponent \(k\) and the total number of guidance steps.

## Weaknesses

### Major

1. **Theoretical framing (Theorem 1, Eqs. 9–11) is not rigorous and does not support the method.** The proof of Theorem 1 assumes \(\epsilon_\theta(\mathbf{x}_{t_1}, t_1) \approx \epsilon_\theta(\mathbf{x}_{t_2}, t_2) \approx \epsilon\) with equal approximation error \(\Delta\) across timesteps — an unjustified claim. The rewriting of the sampling equation as gradient descent (Eq. 9, labeled \(\gamma_1 \nabla D_{KL}\)) is a rearrangement of terms with no derivation showing it is the gradient of the claimed KL divergence. The theory does not produce any testable prediction or design principle that the method follows from; the proposed method (skip guidance, reuse gradients) is an empirical observation that stands independently. This section attempts to give a formal veneer to an essentially empirical contribution but does not constitute valid theoretical support. **However, the method itself does not depend on this theory**, so the empirical contribution can be evaluated separately.

2. **Evidence for the core "model-fitting" diagnosis has a confound.** The paper's central conceptual claim is that guidance over-applies because samples become "tuned" to the guidance classifier's parameters. The key evidence is an accuracy gap: on-sampling classifier 90.8% vs. off-sampling classifier (same architecture, different weights) 62.5% (Table in Section III-A). The paper states the off-sampling classifier has "the same architecture and performance as the on-sampling classifier" and that "the only difference between the two models is the parameters." However, it does not clarify whether the off-sampling classifier was trained on noisy images at all diffusion timesteps (as the on-sampling ADM classifier was). Without this detail, the gap could partially reflect distribution mismatch rather than model-fitting per se. The ResNet152 comparison (34.2%) provides a useful reference but does not resolve this confound since ResNet152 is a clean-image classifier. The claim is plausible but not bulletproof as presented.

3. **No comparison in terms of NFEs (number of function evaluations).** The paper reports GPU hours and number of guidance steps but never the total NFEs, which is the standard efficiency measure in the diffusion sampling literature. Since CompG reuses old gradients at skipped timesteps (the \(\Gamma_t\) mechanism in Eq. 12), it incurs some overhead that GPU-hour measurements conflate with other factors. Reporting FID vs. NFEs would enable fair comparison and is standard practice.

4. **Gradient reuse mechanism is not validated.** The method reuses the guidance gradient from the last guidance step at subsequent non-guidance timesteps (\(\Gamma_t\) in Eq. 12). The paper provides no empirical analysis of whether gradients from, say, timestep \(t\) remain a useful direction five or ten steps later. Without measuring gradient similarity across timesteps, this mechanism is an unvalidated assumption. An ablation comparing CompG with gradient reuse vs. simply skipping guidance steps (the "otherwise" branch without \(\Gamma_t\)) would isolate the benefit of reuse.

### Minor

1. **Marginal improvements in off-sampling accuracy from CompG.** Table III shows CompG raises off-sampling accuracy from 62.5% to 64.2% and ResNet accuracy from 34.17% to 34.93% — very small gains. The claim that CompG "solves" model-fitting is overstated given these numbers.

2. **No confidence intervals or statistical significance.** All FID/sFID numbers are reported as point estimates without variance across runs. This makes it impossible to assess whether improvements (e.g., FID 11.96→11.65 on ADM-256) are reliable or within noise.

3. **Missing NFE-controlled baseline.** The paper does not compare to a simple baseline that uses the same total number of guidance steps but distributes them via a simple alternative schedule (e.g., only the first N steps, or a random schedule). The comparison to Early Stopping (which stops after step 200) and Uniform Skipping (every 5 steps) partially addresses this, but an equivalent-NFE comparison with a non-reuse scheme would be cleaner.

4. **Some FID improvements are small.** On CADM-256 (Table II), CompG achieves FID 4.52 vs. vanilla 4.58 — a 0.06 difference. On DiT-CompCFG, FID goes from 2.25 to 2.19. These improvements are modest and may not be perceptually meaningful.

### Trivial

None of note — the parser-stripped presentation issues flagged by reviewers are artifacts, not author errors.

## Nice-to-Haves

- An analysis of gradient cosine similarity across adjacent timesteps to justify the gradient reuse mechanism.
- A plot of \(\|\nabla_{\mathbf{x}_t} \log p_\phi(y|\mathbf{x}_t)\|\) across timesteps to show gradient magnitude decreases late in sampling.
- Validation that the off-sampling OADM-C classifier was trained on identical noise-augmented data as the on-sampling classifier (to address the confound in the model-fitting evidence).

## Removed Points

These points from the harsh critic are flagged for removal; treat them with caution:

- **"The central claim of model-fitting is not supported by the evidence (Structural)"** — Partially kept above as Major #2, but the critic's stronger claim that the evidence is "invalidated" is an overstatement. The paper's evidence is suggestive (same architecture, different weights, large accuracy gap) and the critic's accusation of confound relies on assuming the off-sampling classifier training differed from the on-sampling one — the paper states the opposite. The critic's third evidence point (color bias) being called "anecdotal" is overly dismissive of valid qualitative evidence.

- **"The runtime improvements are largely mechanical: applying guidance at fewer timesteps trivially reduces compute"** — This is a non-criticism; the paper's contribution is that reducing guidance steps also *improves quality*, not just that it saves compute. The compute savings are reported as a secondary benefit.

- **"Figure 2 caption claims superiority... but the numbers... are not statistically validated"** — Lack of confidence intervals is kept as Minor #2; the critic's framing that this invalidates the results is too harsh.

- **"Table II... the text says '42% reduction' — 31.80/54.86 ≈ 58%, so the reduction is actually 42%"** — The critic's math is wrong. 31.80/54.86 = 0.58 (CompG takes 58% of vanilla time), so the reduction is 100% − 58% = 42%. The paper is correct.

- **"The caption of Table I claims 'approximately 42%... and 23%' but the numbers show 42% and 23% respectively"** — The critic appears to be saying the numbers match the caption, which is not a criticism. Nonsensical point.

- **"No comparisons are made to... DPM-Solver, consistency models, progressive distillation"** — These address a different problem (reducing total sampling steps, not guidance efficiency within a fixed sampling budget). Scope creep.

- **"Missing comparison to any recent work on efficient diffusion sampling"** — See above. These works are orthogonal to the paper's contribution (guidance frequency reduction within a fixed sampling schedule).

- **Pure formatting/style nitpicks** about table spacing, non-standard notation, and undefined metrics — removed per instructions.

## Novel Insights

None beyond the paper's own contributions. The core observation — that guidance gradients are more useful early in the sampling process and can be applied at a subset of timesteps — is the paper's main insight and is well-supported empirically, even though the "model-fitting" explanation for *why* this works is not fully validated.

## Suggestions

1. **Tighten the model-fitting evidence.** Explicitly state that the off-sampling OADM-C was trained on the same noise-augmented data distribution as the on-sampling classifier, or retrain it with that protocol. If the gap persists, it cleanly supports the model-fitting claim.

2. **Drop or substantially revise the theoretical section (Theorem 1, Eqs. 9–11).** The current framing is not rigorous and invites justified criticism. Replace it with a simpler, defensible observation: guidance gradients across nearby timesteps are correlated, and empirically, early timesteps contribute more to conditional information. Validate the correlation claim with a simple experiment.

3. **Add NFE-based efficiency comparisons** (e.g., FID vs. number of guidance function evaluations) for all methods, and report results over multiple random seeds with mean ± std.

4. **Ablate gradient reuse.** Compare CompG (with \(\Gamma_t\)) against a version that simply skips guidance at non-sampled timesteps (no reuse) to quantify the benefit of the reuse mechanism.

5. **Add a simple baseline: the same number of guidance steps applied only at the earliest timesteps** (no polynomial scheduling, no reuse). This would isolate the effect of the scheduling from the effect of gradient reuse.

## Score and Decision

**Calibration anchors:**

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| Universal Guidance (pzpWBbnwiJ) | 5.25 (Accept) | Similar type (guidance improvement paper). This paper has weaker theory but broader architecture validation. Comparable overall. |
| Revamping Diff. Guidance (b3CzCCCILJ) | 6.00 (Accept) | Stronger theoretical framing of CFG alternatives. The current paper has weaker theory but is more practically focused. Slightly weaker. |
| Representative Guidance (gWgaypDBs8) | 7.33 (Accept) | Stronger empirical validation and clearer contribution. This paper is notably weaker. |
| Feature-guided Score Diff. (kwY3eL3QVh) | 5.50 (Reject) | Mixed reviews, similar quality level empirically. The current paper has broader experiments but similar theoretical weakness. Comparable. |
| Dreamguider (Hpu3KIX8Am) | 4.00 (Reject) | Similar topic (guidance efficiency). The current paper has stronger empirical validation across more settings. Better. |
| Rectified Diff. Guidance (Y4kJp8GQmV) | 4.25 (Reject) | Limited experiments. The current paper has broader empirical validation. Better. |
| Memorization→Generalization (XeGSIr7z6u) | 3.40 (Reject) | Serious methodological flaws. The current paper is clearly stronger. |
| Diff. Process w/ Implicit Latents (NW5vSJXO9V) | 3.67 (Reject) | Not strong empirically. The current paper is stronger. |

The paper makes a useful empirical contribution — demonstrating that guidance frequency can be substantially reduced while maintaining or improving quality — and validates it across a broad range of models and datasets. However, the theoretical framing is not rigorous, the central "model-fitting" diagnosis has a confound that weakens the conceptual contribution, and the evaluation lacks standard rigor (no NFEs, no statistical significance, unvalidated gradient reuse). The method is simple and practical, but the paper's strongest claims are not fully supported.

Relative to the anchors: this paper is stronger than the 3–4 range papers and on par with the mid-5 papers, but not as strong as the 6+ papers that have clearer theoretical backing or more thorough evaluation.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
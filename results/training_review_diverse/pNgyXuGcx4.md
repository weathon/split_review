Now I have a thorough understanding of the paper and can produce the consolidated review.

## Summary

This paper investigates whether reduced-precision (particularly FP8) LLM training is cost-effective compared to mixed-precision BF16. The authors find that MS-AMP O1 FP8 training shows a persistent loss gap on GPT-2 (120K steps), and through systematic bit-reduction simulations on Llama models (120M and 7B), demonstrate a monotonic relationship between mantissa-bit width and training instability. The paper's main methodological contribution is a loss-landscape sharpness metric adapted from Keskar et al. (2017) to the logit space of the last token in autoregressive models, intended as an early indicator of impending training divergence.

---

## Strengths

- **A sharpness metric adapted to autoregressive models with computational efficiency.** The metric operates on the last-token logit space (Equation 2), requiring only a single forward pass per measurement. The motivation is well-grounded: standard loss-landscape visualizations (Li et al., 2018) remain smooth even during divergence (Figure 2), and the last token receives attention from all prior tokens, making it a natural aggregation point. The paper shows that sharpness rises monotonically for E8M5 models at 7B scale (Table 1) while the loss curve remains flat—exactly the early-warning behavior the metric is designed for.

- **Systematic bit-reduction experiments establish a clear monotonic relationship between mantissa bits and training stability.** By clamping mantissa bits incrementally (E8M7 → E8M5 → E8M4 → E8M3) in Llama-120M and Llama-7B models (Sections 4.2–4.3, Figures 7–8), the paper shows that each removed mantissa bit reduces stability. E8M3 and E8M4 diverge early; E8M5 exhibits rising sharpness with stable loss. This controlled ablation goes beyond prior work's binary FP8-vs-BF16 comparisons.

- **Surprising baseline finding: BF16 mixed-precision has a non-negligible divergence rate.** Of 188 BF16 runs, 18 (~10%) diverged at only 5% of training, while 0 of 70 TF32 runs diverged (Section 1). This result legitimizes the paper's concern that even the current best practice operates in a fragile regime.

- **MS-AMP O1 experiments quantify a persistent loss gap.** Figure 6 shows that FP8 training (with LM head excluded) does not converge to the BF16 loss even after 120K steps, and data quality interacts with FP8 stability (Figure 12). This provides concrete evidence for the paper's claim that FP8 narrows the effective hyperparameter space.

- **Multi-seed robustness experiments (18 seeds per condition).** Figure 9 shows that E8M5 models exhibit more frequent loss spikes than BF16 at elevated learning rates, supporting the claim of increased instability even before full divergence.

---

## Weaknesses

### Fatal
None.

### Major

- **The sharpness metric's predictive claim is supported only by correlational evidence, not validated prediction.** The abstract and introduction state the metric can "predict when training divergence will occur." However, the evidence is: (i) Figure 7 shows sharpness rising before divergence in three 120M runs (no non-diverging baseline shown in the same plot), (ii) Table 1 shows E8M5 sharpness increasing at 5K steps but training was not continued to verify divergence, and (iii) no threshold analysis, precision/recall, or controlled comparison across multiple seeds for diverging vs. non-diverging trajectories is provided. The paper itself notes "no exact sharpness threshold exists for training collapse," which is honest but underscores that the metric is a diagnostic signal, not a validated predictor. The claim in the abstract overstates what is demonstrated.

- **The central economic claim about FP8 rests on a narrow empirical base.** The paper argues that "currently available methods for FP8 training are not robust enough to allow their use as economical replacements." This claim is tested with exactly one FP8 library (MS-AMP O1) on one architecture (GPT-2 via nanoGPT). Other FP8 frameworks (Transformer Engine, MS-AMP O2/O3) and more recent recipes (Fishman et al., 2024, cited by the paper as showing Llama 7B FP8 divergence at 200B tokens) are not evaluated. While the bit-reduction simulations provide complementary evidence about the general phenomenon, the direct real-FP8 comparison is too narrow to support a sweeping verdict. The Discussion section partially acknowledges this, but the abstract and introduction frame the conclusion more strongly than the evidence warrants.

- **The 7B experiments (Table 1, Figure 8) lack variance estimates.** Training a 7B model for 5K steps requires ~one week on 8×A100s, making multiple seeds expensive but not unjustified to request. Without multiple seeds or confidence intervals, it is unclear whether the sharpness values in Table 1 are reproducible or whether the E8M5 loss curve in Figure 8 is representative. Given that the paper's own BF16 experiments (Section 1) show 10% divergence due to seed variation alone, single-seed results at 7B scale are a genuine limitation.

### Minor

- **The bit-reduction simulation's relationship to real FP8 hardware is under-discussed.** The simulated approach clamps bits in software (with a high-precision accumulator, per Figure 3), but real FP8 uses specific hybrid formats (E4M3 forward, E5M2 backward), specialized rounding modes, and per-tensor scaling factors (Micikevicius et al., 2022). The paper does not discuss whether these hardware features would mitigate, exacerbate, or be orthogonal to the simulated effects. The simulation is internally consistent and valuable as an analysis tool, but the gap between E8M3/E8M5 simulations and actual E4M3/E5M2 hardware behavior is not bridged.

- **No statistical significance tests for the multi-seed experiments.** Figure 9 compares 18 seeds each for E8M5 vs. BF16 at two learning rates, and the E8M5 runs show "more frequent loss spikes." However, the paper does not quantify whether the difference in spike frequency or loss trajectory is statistically significant, nor does it report the proportion of diverged runs. A simple comparison metric (e.g., proportion of runs exceeding a loss threshold) would strengthen the claim.

- **The cost analysis is illustrative but does not model trade-offs.** The $100K restart anecdote (Section 1) motivates the problem, but the paper never quantifies the break-even point where FP8's per-step speed advantage would compensate for increased instability. If FP8 trains 2× faster but requires 10% more restarts, the net cost could still favor FP8. The paper argues qualitatively that the instability costs "outweigh the benefits" without a sensitivity analysis.

### Trivial
None that survive filtering (parser artifacts removed).

---

## Nice-to-Haves

- **Validate the sharpness metric as a predictor.** Run a set of experiments where training continues until divergence or a fixed budget, with multiple seeds per precision level, and evaluate whether sharpness values above a threshold predict divergence with reasonable precision/recall. This would turn a suggestive correlation into actionable evidence.
- **Compare against at least one other FP8 method** (e.g., Transformer Engine default settings) on the same architecture and scale to test generality.
- **An ablation comparing the proposed last-token-logit sharpness to the original Keskar et al. (2017) approach on embedding space** (even at small scale) would strengthen the justification for the architectural choice.
- **Report confidence intervals or distribution bands for all main experiments**, particularly the 7B sharpness values.

---

## Removed Points

These points were flagged by reviewers but are removed or downgraded as per the meta-review guidelines:

1. **"Fishman et al. (2024) show stable Llama 7B FP8 training for 200B tokens"** — This misreads the paper. The paper correctly cites Fishman et al. as **finding divergence after 200B tokens** (line 53), which supports the paper's claim. Removed as factually wrong.

2. **"Section 3.2 (Masking) is empty"** — Parser artifact; section content exists in the original submission. Removed per parser-artifact rule.

3. **"The $100K restart cost derivation is unclear"** — The derivation is clearly explained: $98.32/hr × 1024 nodes × (20+40)/60 hr ≈ $100K. Removed as the reviewer misread a clear passage.

4. **"Why O2 and O3 were not tested"** — The paper explicitly states "we use only the most basic optimization scheme so as to verify the effects of the least invasive modifications" (line 70). This is a defensible methodological choice. Removed as the paper already addresses this.

5. **"Not clear why searching logit space of a single token captures global properties"** — The paper justifies this: "the last token is the only one to receive inputs from all other tokens" (line 90). A reasonable theoretical motivation. Removed as the paper already addresses this.

6. **"No baseline for runs that do not diverge"** — Incorrect. Table 1 includes E8M7 sharpness values, and the text explicitly compares E8M7's "gradual increase" with E8M3/E8M4/E8M5 (line 215). Removed as factually wrong.

7. **Missing related works** — Per instructions, cannot verify which related works are missing and should not mention them.

8. **Formatting/style nitpicks, typo concerns** — These are parser artifacts, not author errors.

---

## Novel Insights

The reviewer reviews surface one genuinely novel observation beyond the paper's own contributions: the finding that even standard BF16 training shows a ~10% divergence rate at only 5% of training (18/188 seeds) is both surprising and significant for the field. None of the reviewers note this as the paper's strongest empirical discovery, but it arguably provides the most compelling motivation for the paper's line of inquiry. The sharpness metric itself is an interesting adaptation, but the reviewers' main collective insight is that the paper's central economic claim about FP8 would be better served by framing itself as a diagnostic framework (metric + simulation methodology) rather than a verdict on FP8's viability — a reframing that would make the paper more defensible against the evidentiary gaps identified.

---

## Suggestions

1. **Reframe the central claim.** The paper's strongest contributions are the sharpness metric and the bit-reduction analysis methodology. The paper would be strengthened by framing its conclusion as "FP8 training introduces hidden instabilities that can be quantified and monitored via our metric" rather than "FP8 is not cost-effective." The latter requires broader evidence than currently provided.

2. **Validate the sharpness metric as a predictor** by extending training for E8M5 models until divergence or a fixed budget, with multiple seeds, and establishing a sharpness threshold with precision/recall analysis.

3. **Add variance information** for the 7B experiments. Even reporting the range across seeds for a subset of conditions would help.

---

## Score and Decision

This paper tackles a timely and practically important problem. Its core contributions — the sharpness metric adapted for autoregressive models and the systematic bit-reduction analysis — are sound and valuable to the community. The writing is clear and the experiments are well-motivated. However, the paper overclaims on two fronts: (1) the sharpness metric is presented as a "predictor" but is only shown to correlate with divergence, and (2) the central economic claim about FP8 outruns the evidence (one library, one architecture). These are addressable weaknesses that do not invalidate the core methodology but prevent the paper from being as strong as it could be. With a more measured framing and targeted additional validation, this would be a solid paper.

**Score**: 6.0 — A competent paper with a worthwhile contribution, whose overclaiming and narrow empirical base in one dimension prevent it from being stronger. Suitable for a main conference with minor revisions to calibrate claims.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
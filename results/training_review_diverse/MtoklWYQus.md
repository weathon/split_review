Now I have all the information I need. Let me compile the final review after thorough verification.

---

## Summary

This paper proposes DyNet, a family of all-in-one image restoration networks built around a weight-sharing mechanism where transformer block weights are reused across subsequent blocks within each encoder-decoder level. This design allows two variants (DyNet-L and DyNet-S) to share the same checkpoint while differing only in depth, enabling flexible deployment. The authors also introduce a dynamic pre-training strategy that trains both variants concurrently (claiming 50% GPU hour savings) and curate Million-IRD, a 2M-image high-resolution dataset. The main empirical result is that DyNet-S surpasses PromptIR by 0.43 dB average PSNR while reducing GFlops by 31.34% and parameters by 56.75%.

## Strengths

1. **Weight-sharing mechanism for flexible deployment is well-conceived and empirically validated.** The core idea — reusing a single initialized transformer block's weights across subsequent blocks within each encoder-decoder level — is novel for all-in-one IR. By simply changing the reuse frequency (f=[4,6,6,8] for DyNet-L vs f=[2,3,3,4] for DyNet-S), the same checkpoint supports both a bulky and a lightweight variant. This flexibility is absent in prior work like PromptIR, which requires separate models. The main results in Table 1 confirm that both variants outperform PromptIR, validating the approach.

2. **Strong empirical results across multiple tasks.** DyNet-L achieves a 0.68 dB average PSNR improvement over PromptIR in the all-in-one setting (Table 1), and DyNet-S achieves 0.43 dB improvement with substantial efficiency gains. These gains hold across denoising, deraining, and dehazing. Single-task results (Tables for dehazing, deraining, denoising) also show consistent improvements (e.g., +1.81 dB on Rain100L deraining, +0.76 dB on SOTS dehazing vs. PromptIR). The ablation study (Table 5) confirms that even without pre-training, DyNet variants match or slightly exceed PromptIR performance while using 56.75% fewer parameters.

3. **The Million-IRD dataset is a practical resource whose utility is demonstrated.** The ablation in Table 5b shows that pre-training on Million-IRD yields a 0.41 dB average PSNR improvement for DyNet-L over the non-pre-trained variant. While the dataset's superiority over alternative pre-training corpora is not benchmarked, the fact that large-scale pre-training improves results is clear and the dataset is a tangible contribution to the community.

4. **Dynamic pre-training is a conceptually elegant efficiency trick.** Training both variants concurrently in a single session (randomly alternating between them, updating shared weights) is a clean solution to what would otherwise require two separate pre-training runs. The design is clearly described in Section 3.2 and Figure 3, and the resulting models perform well.

## Weaknesses

### Fatal
None.

### Major

1. **The "50% reduction in GPU hours" claim is stated as a factual achievement but is never empirically validated.** The paper claims this savings repeatedly (abstract, Section 3.2, conclusion) but provides no experiment comparing dynamic pre-training against separate pre-training of DyNet-L and DyNet-S. There is no measurement of actual GPU hours for either scenario. Furthermore, because only one branch is active per iteration (Section 3.2), each variant receives roughly half the gradient updates it would get in separate training — yet the paper does not discuss whether this affects convergence or final quality, nor does it compare against separately pre-trained baselines. The savings are logically plausible but unverified, and the absence of this comparison weakens a claimed contribution. *(Verified: the paper states the 50% claim at lines 7, 39, 43, 137, 379, 390 without any accompanying GPU hour measurement or baseline comparison.)*

2. **The claimed superiority of placing prompts at skip connections (vs. on the decoder as in PromptIR) is not cleanly ablated.** The paper describes this as a "fundamental correction" (line 112) and attributes part of DyNet's improvement to it. However, the ablation in Table 5 compares DyNet (weight-sharing + skip-connection prompts) against PromptIR (no weight-sharing + decoder prompts). Because the design differs in *both* weight-sharing and prompt placement simultaneously, the contribution of prompt placement alone cannot be isolated. The improvement in Table 5a (DyNet-L without pre-training: 32.33 dB vs. PromptIR: 32.06 dB) could stem from the weight-sharing mechanism acting as a regularizer, the prompt placement, or both. A proper ablation would compare: (a) weight-sharing + decoder prompts, (b) weight-sharing + skip-connection prompts, (c) no weight-sharing + no prompts. Without this, the claim is overstated. *(Verified: the paper states this as a "fundamental correction" at lines 112 and 377, but the ablation at Table 5a does not isolate the prompt-placement variable.)*

### Minor

3. **The Million-IRD dataset's value is not benchmarked against alternative pre-training corpora.** The ablation (Table 5b vs. 5a) shows that pre-training on Million-IRD helps, which is expected from any large-scale pre-training. However, the paper does not compare against pre-training on existing IR datasets (e.g., LSDIR with ~85K images) or against an unfiltered random subset of Laion-HR. Without these baselines, the reader cannot judge whether the substantial curation effort (processing ~100M images with quality metrics) yields a meaningful advantage over simpler alternatives. The dataset is still a contribution, but the value-add of quality filtering is unquantified. *(Verified: Table 5 only compares with vs. without Million-IRD pre-training, no alternative dataset baseline.)*

4. **Factual inconsistency about existing dataset sizes.** Line 148 states that "LSDIR, NTIRE, Flickr2K, when combined, offer only a few thousand images," but line 157 correctly states that these datasets collectively have 90K images. The "few thousand" characterization is inaccurate and weakens the paper's motivation for a million-scale dataset. *(Verified at lines 148 and 157.)*

5. **Fine-tuning implementation details are incomplete.** The pre-training setup is well-specified (L1 loss, Adam, LR 1e-4, 1M iterations, batch size 32, line 195), but the fine-tuning stage (used for all main results) only mentions "120 epochs" without stating the loss function, optimizer hyperparameters, learning rate schedule, or batch size. This affects reproducibility. *(Verified: lines 200-205 describe fine-tuning only by number of epochs and "adopt the training protocol from PromptIR.")*

6. **No error bars, confidence intervals, or multiple-run statistics.** All results are reported as single-point PSNR/SSIM values. Given that many of the reported gains over PromptIR are small (e.g., 0.09–0.24 dB for denoising at various noise levels in Table 1), it is not clear whether these differences are statistically significant. *(Verified: no variance reporting in any table.)*

7. **Threshold values for NIQE, BRISQUE, and NIMA filtering are not reported.** The paper states that "we empirically define thresholds" (line 163) but never discloses them, limiting reproducibility of the Million-IRD curation pipeline. *(Verified: line 163 mentions thresholds T_NIQE, T_BRISQUE, T_NIMA but provides no values.)*

8. **Real-world dehazing results rely on an external GWA pre-processing step with no quantitative evaluation.** Figure 7 shows visual results for real-world dehazing, but the paper uses a Gray-World Assumption preprocessing step that is not part of the core model. No quantitative results on a standard real-world dehazing benchmark (e.g., Dense-Haze, NTIRE) are provided. *(Verified: lines 259-263 describe the GWA module and show only visual results.)*

### Trivial

9. **Minor notation ambiguity in Eq. (1).** The reuse notation $w^b$ for $b>1$ could be misinterpreted as separate weights rather than shared copies. The surrounding text and diagram clarify this, but a brief clarification would help.

10. **DyNet-L has identical GFlops to PromptIR (242.35)**, as shown in Table 5. The paper's efficiency claims focus on DyNet-S (31.34% reduction in GFlops, 56.75% reduction in params), which is accurate, but this should be stated more explicitly for DyNet-L.

## Nice-to-Haves

- A comparison of dynamic pre-training vs. separate pre-training (controlling for number of iterations) would directly validate the 50% GPU hours claim and address the most significant gap.
- An ablation varying prompt placement (decoder vs. skip connections) while keeping weight-sharing fixed would cleanly support the "fundamental correction" claim.
- Reporting the quality metric thresholds used for Million-IRD filtering would improve reproducibility.
- Error bars or multiple-seed runs would strengthen confidence in the small-margin improvements.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"The paper never discusses how the switch is performed at deployment time"* — The paper clearly explains that changing the reuse frequency switches between variants (Section 3.1, lines 96-97: "By simply altering the frequency of weight sharing, users can easily modify the network's depth"). Removed because the paper already addresses this.

- *"Eq. (1) is ambiguous" (presented as a major issue)* — This is a minor notation clarity point, not a substantive weakness. The surrounding text and Figure 2 clearly describe the weight-sharing mechanism. Downgraded to Trivial.

- *Criticisms about missing appendix content or proofs* — Removed per instructions; these are parser artifacts.

- *"Demanding comparison against methods/domains outside the paper's stated scope"* — Removed as scope creep.

- *Some generic strengths from Strengths Finder that are superficial or unsupported* — The strength about dynamic pre-training's "50% reduction" is listed as a strength, but since this claim is unvalidated (as discussed in Weakness #1), it conflicts with a verified weakness. The strength is retained only as a *design attribute* rather than an empirically validated claim.

## Novel Insights

The most interesting observation from the reviews is not captured by the paper itself: the three main contributions (weight-sharing architecture, dynamic pre-training, Million-IRD dataset) are each presented as independently important, yet none is rigorously decoupled from the others. The paper would be significantly stronger if it systematically isolated each variable. That said, the weight-sharing mechanism itself genuinely appears effective — even without pre-training, DyNet variants with 56.75% fewer parameters match or exceed PromptIR — which suggests the architecture has intrinsic merit beyond what the training recipe or dataset provides.

## Suggestions

1. **Run the critical missing ablation: dynamic vs. separate pre-training.** Train DyNet-L and DyNet-S separately on Million-IRD for the same total iterations and compare quality and GPU hours. This single experiment would either validate the 50% savings claim or reveal trade-offs that need discussion.
2. **Isolate prompt placement** by comparing (weight-sharing + decoder prompts) vs. (weight-sharing + skip-connection prompts) vs. (weight-sharing, no prompts) in the all-in-one setting.
3. **Benchmark Million-IRD against at least one alternative pre-training corpus** (e.g., LSDIR-only, unfiltered Laion-HR subset) to quantify the benefit of quality filtering.
4. **Report the NIQE/BRISQUE/NIMA threshold values** used for filtering and include error bars for the main results.

## Score and Decision

The paper makes a solid empirical contribution: DyNet's weight-sharing architecture consistently outperforms PromptIR while using fewer parameters, and the dynamic pre-training + Million-IRD combination provides further gains. The core claims are supported by Table 1 and Table 5. However, two important sub-claims (the 50% GPU hours savings and the prompt-placement advantage) are stated as contributions but lack proper experimental support, and the dataset contribution is not benchmarked against alternatives. These are addressable gaps rather than fatal flaws. The paper's central thesis — that weight-sharing produces efficient, flexible, well-performing all-in-one IR models — is convincingly demonstrated.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
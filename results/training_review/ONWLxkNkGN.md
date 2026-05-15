Here is the consolidated review.

## Summary

InstantIR introduces a diffusion-based blind image restoration method that dynamically generates and integrates "instant generative references" during the reverse process. The architecture features three modules — a DINO-based Degradation Content Perceptor (DCP) for compact LQ encoding, a consistency-distilled one-step Previewer that decodes restoration previews on the fly, and an Aggregator that fuses previews with the LQ input. The method also proposes an adaptive sampling algorithm (AdaRes) that adjusts condition strength based on an indicator δ derived from preview-denoising discrepancy, and demonstrates controllable semantic editing via text prompts. Experiments show top scores on non-reference perceptual metrics (MANIQA, MUSIQ) across both synthetic and real-world benchmarks.

## Strengths

- **Novel previewing mechanism for iterative alignment with the generative prior.** The Previewer module — a consistency-distilled one-step generator that decodes a restoration preview from the DCP embedding at each diffusion step — is a technically creative solution to a genuine BIR problem: encoding errors from input distribution shift. The ablation (Table \ref{ablation1}) shows that removing the distilled previewer crashes MUSIQ from 66.35 to 38.33, confirming the reference information it provides is critical.

- **State-of-the-art perceptual quality on non-reference metrics.** Across all four benchmark settings (synthetic/real-world, 512²/1024²), InstantIR achieves the highest MANIQA and MUSIQ scores, often by substantial margins (e.g., MANIQA 0.4819 vs. 0.3941 for CoSeR on real-world 512²; MUSIQ 68.59 vs. 67.51 on synthetic 512²). These are the metrics the method optimizes for, and the improvements are consistent and non-trivial.

- **Text-conditioned DCP training demonstrably improves low-level fidelity in previews.** Figure \ref{preview_row} provides convincing visual evidence that DCP trained jointly with text preserves hue, structure, and pose in early-stage previews, whereas an image-only DCP captures only coarse semantics. This is an instructive design insight.

- **Adaptive restoration (AdaRes) is a well-motivated, principled algorithm.** The δ indicator (Eq. \ref{relative_dis}) cleanly separates four degradation levels in Figure \ref{fig:trajectory}(c), and the logic of amplifying fine-grained encoding for higher-quality inputs is sound. The ablation (Table \ref{ablation2}) shows marginal but consistent improvements from AdaRes across CLIPIQA, MANIQA, and MUSIQ.

## Weaknesses

### Fatal
None.

### Major

- **The method systematically sacrifices restoration fidelity, and the paper does not adequately grapple with this.** Across all benchmarks, InstantIR has the lowest or near-lowest PSNR and SSIM, often by large margins (e.g., real-world 512²: PSNR 21.75 vs. Real‑ESRGAN 27.29, a >5 dB gap; synthetic 512²: PSNR 18.54 vs. StableSR's 20.42). The paper dismisses this as "misalignment of PSNR and SSIM scores with visual quality" and includes them "for reference purpose," but this is insufficient for a paper framed as *restoration*. The ablation (Table \ref{ablation2}) directly confirms that the full pipeline (with references and AdaRes, PSNR 21.06) achieves *lower* fidelity than the no-reference baseline (PSNR 22.24). The conclusion acknowledges the issue in one sentence but provides no analysis of the tradeoff — e.g., under what conditions the fidelity loss is acceptable, how often the method hallucinates plausible but incorrect details, or whether users would prefer the perceptually appealing outputs despite lower pixel accuracy. Without a user study or failure-case analysis, the core claim of "blind image restoration" is only partially supported.

- **The adaptive sampling algorithm is inadequately validated.** The δ indicator is motivated by Figure \ref{fig:trajectory}, which shows *only four examples* (one per degradation level) with no statistics (mean, variance, sample size) reported. The threshold η in Algorithm \ref{adares} is a critical hyperparameter — it determines how many early time-steps are excluded from adaptive control — yet its value is never stated, ablated, or discussed. No sensitivity analysis is provided. For a claimed contribution that is explicitly named "Adaptive Restoration," the evidential support is thin.

### Minor

- **Cross-reference error and misleading naming in the distillation ablation.** The text in Section \ref{previewer} states "The second row in Tab.~\ref{ablation2} shows a significant drop in the non-reference metrics," but the distillation ablation data reside in Table \ref{ablation1}, not \ref{ablation2} (which is about references and AdaRes). Additionally, the row labeled "+Distillation" in Table \ref{ablation1} actually *removes* consistency distillation (using DDIM predictions instead), which is confusing and should be renamed (e.g., "w/o Distillation" or "DDIM Reference").

- **Creative restoration capability is presented without quantitative evaluation.** Figure \ref{outdomain_edit} shows appealing semantic editing results, but no quantitative evaluation (prompt-following metrics, user study, or comparison to editing methods) is provided. This is presented as an additional capability, so the absence of evaluation is acceptable only if it is clearly scoped as a qualitative demonstration — but the paper should be clearer that this is preliminary.

- **No dedicated limitation or failure-case analysis.** The paper mentions the PSNR/SSIM disparity in the conclusion but does not systematically discuss when the previewer hallucinates, what types of degradation cause failure, or how practitioners should judge whether the output is trustworthy. Given the fidelity concerns, this is a noticeable omission.

### Trivial

- The pseudo-code in Algorithm \ref{adares} lists `η` as a required input but never specifies its value or how it relates to the total time-steps T (30 steps in experiments). A note on its default setting would help reproducibility.

- Table \ref{ablation2} uses checkmark/crossmark symbols for "References" and "AdaRes" but the legend for these symbols is not defined in the caption.

## Nice-to-Haves

- A user study comparing perceptual preference between InstantIR and the best competitor (e.g., CoSeR or Real‑ESRGAN) would substantially strengthen the claim that the perceptual quality gain justifies the fidelity loss.

- Reporting mean ± std of the δ indicator over a larger set of inputs across degradation levels would validate its reliability as a quality indicator beyond the four illustrated trajectories.

- A scatter plot of PSNR vs. MANIQA for individual images would help readers understand the fidelity-perceptual tradeoff at the instance level.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **Harsh critic's claim that "the paper treats the perceptual improvement as universally positive, but the loss of fidelity is severe — this is a critical trade-off that is not discussed."** — Partially inaccurate. The paper *does* discuss this tradeoff, stating: "Previewer with consistency distillation can directly sample from the data distribution, providing more informative generative references" and acknowledges the PSNR gap in the conclusion. However, the discussion is brief and not deeply analyzed, so the core concern about insufficient treatment of the tradeoff stands in the Major section above, while the claim of "not discussed at all" is removed.

2. **Harsh critic's framing that "the method does not restore the original image with sufficient fidelity" as a fatal flaw.** — This concern is real and is kept as Major, but it is not Fatal because (a) the method does not claim SOTA on PSNR/SSIM, (b) several recent BIR papers (StableSR, SUPIR) similarly prioritize perceptual quality, and (c) the paper acknowledges the issue. The framing as a deal-breaker for the entire contribution is removed.

3. **Harsh critic's claim that "the contribution would need to be re-framed as generative enhancement or creative restoration."** — Overstatement. The method does perform restoration (it recovers content from degraded inputs), just with a perceptual rather than fidelity-optimized objective. This is removed as it overreaches the evidence.

4. **Strength Finder's generic/unsubstantiated strengths:** Some phrasing is retained but several generic formulations (e.g., "robust compact representation via DINO") are condensed since the specific mechanism is already captured in the kept strengths.

## Novel Insights

The key insight emerging across the reviews is that InstantIR's core innovation — on-the-fly generative references via a distilled one-step previewer — is genuinely novel and produces state-of-the-art perceptual quality, but this strength is paired with a systematic fidelity weakness that the paper handles too dismissively. The tension is not unique to this paper (it mirrors a broader field trend toward perceptual over fidelity metrics), but InstantIR's PSNR gap is larger than that of concurrent methods like CoSeR, making the tradeoff starker. The adaptive restoration algorithm is a clever attempt to modulate this tradeoff at inference time, but its empirical validation is too thin to support the claimed generality. A second interesting observation is that the text-conditioned DCP preserves significantly more low-level information in early previews than an image-only variant — this suggests that cross-modal training (even for a modality-agnostic task like restoration) may regularize the encoder to retain spatial structure, which is a finding worth further study.

## Suggestions

1. **Add a thorough limitations section.** Discuss the fidelity-perceptual tradeoff explicitly: quantify the PSNR drop, show where the method hallucinates vs. restores faithfully, and describe conditions under which the Aggregator's fidelity anchor fails. This would strengthen rather than weaken the paper.

2. **Ablate and report the η threshold.** At minimum, state its value in the experiment setup and run a sensitivity analysis (e.g., η = 5, 10, 15, 20) showing its effect on both perceptual and fidelity metrics.

3. **Rename "+Distillation" → "w/o Distillation" (or similar)** in Table \ref{ablation1} to avoid confusion, and fix the cross-reference in Section \ref{previewer} to point to the correct table.

4. **Consider a small user study (30–50 participants, preference judgment on 20 pairs)** comparing InstantIR with the best competitor (CoSeR or Real‑ESRGAN) to establish whether the perceptual quality advantage is human-visible despite the fidelity loss. This would directly address the most substantive concern.

5. **Report mean ± std of δ across the test set** (stratified by degradation level) to substantiate the claim that it is a reliable quality indicator, replacing the current single-example-per-level trajectories.

## Score and Decision

**Score:** 6.0  

The paper presents a technically original and well-engineered system with clear evidence of perceptual quality improvements. The previewing mechanism and consistency-distilled one-step reference generation are genuine contributions. However, the fidelity gap is large and insufficiently analyzed, and the adaptive sampling algorithm's validation is thin. These problems are addressable with additional analysis and experiments, but in the current form the paper's central claim — a state-of-the-art *restoration* method — is only partially supported. The work would benefit from reframing to more accurately reflect the fidelity-perceptual tradeoff, or from adding the missing analyses.

**Decision:** Reject  

The paper has real technical contributions and the core idea is promising, but the evaluation has a significant gap: the method systematically achieves the worst PSNR/SSIM across all benchmarks without adequate discussion of when or why this is acceptable for restoration. The adaptive sampling contribution is under-validated. These issues are not fatal in principle — they could be addressed with additional experiments, a user study, and a more honest framing — but in the current submission they are substantive enough to preclude acceptance. A resubmission with the identified gaps filled and the claims properly scoped would be competitive.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
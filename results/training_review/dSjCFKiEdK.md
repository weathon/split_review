Now I have a thorough understanding of the paper and the reviews. Let me compose the final consolidated review.

---

## Summary

InstructBrush proposes an instruction inversion method for visual prompt editing that extracts editing effects from exemplar before/after image pairs and applies them to new images. Its two main innovations are: (1) **Attention-based Instruction Optimization** — optimizing instruction features (Keys and Values) directly in the cross-attention layers of an instruction-based diffusion model, rather than in the text encoder's embedding space; and (2) **Transformation-oriented Instruction Initialization** — using CLIP sensitivity to extract editing-relevant unique phrases from the image pairs while discarding content-specific information. The paper also introduces **TOP-Bench**, a benchmark with 25 editing effects (750 images) for evaluating visual prompt editing.

---

## Strengths

- **Attention-based optimization in cross-attention feature space is a novel and well-motivated idea.** The paper identifies a genuine limitation of prior work (Visii): inverting instructions in the text encoder's embedding space loses fine-grained editing details because the text encoder is trained on coarse text-image pairs. Optimizing K/V features directly in cross-attention layers, which are projected into an image-consistent representation, is a natural and principled solution. The ablation in Table 2 supports that this component contributes meaningfully (e.g., LPIPS improves from 0.156 to 0.139 on TOP-Bench when attention-based instruction is added).

- **Transformation-oriented initialization cleverly avoids content contamination.** Visii's caption-based initialization (using a caption of the after-editing image) introduces scene/content information from training images, hurting generalization. The proposed method extracts unique phrases via CLIP sensitivity, truncates phrases below a threshold η, and constructs a template instruction like "turn \<p_x\> into \<p_y\>." This directly addresses a known failure mode, and the ablation shows it improves CLIP image similarity (0.727 → 0.737).

- **The paper provides clean ablations that decompose contributions.** Table 2 systematically ablates each of the three proposed components, allowing readers to assess their individual impact. This is more informative than many papers that only show the full method vs. a single baseline.

- **TOP-Bench provides a standardized testbed.** Despite its modest size, the benchmark covers 25 diverse editing effects (global and local) with fixed train/test splits, enabling standardized comparisons that did not previously exist for this task.

---

## Weaknesses

### Fatal
None.

### Major

1. **The quantitative evidence is thin to support the headline claim of "superior performance."** The test set contains only 125 images (5 per editing effect × 25 effects). No confidence intervals, error bars, or statistical significance tests are reported. With n=5 per effect, a few unlucky test images could shift the rankings. While the aggregate numbers in Table 1 favor InstructBrush, the paper's central claim would be much more convincing with bootstrapped intervals or per-effect breakdowns showing consistent wins.

2. **The benefit of the time-aware instruction component is not convincingly demonstrated.** The paper presents it as a contribution, yet the ablation (Table 2) reveals a trade-off that is not discussed: removing time-aware instruction *improves* PSNR and SSIM while *decreasing* CLIP directional similarity and DINO scores. The paper claims it "captures more details" but does not explain this trade-off, and the supporting visualization is deferred to the appendix (Figure 15). A component that helps semantic alignment at the cost of pixel-level fidelity needs a more careful analysis than provided.

### Minor

1. **The ablation does not fully isolate the benefit of attention-based optimization from the benefit of the new initialization.** The "w/o Attention-based Instruction" condition removes attention optimization but retains the proposed initialization. This shows that attention optimization + new init > text-space optimization + new init, but it does not show whether attention optimization alone (without the new init) would outperform Visii's full pipeline (text-space optimization + caption init). A more controlled comparison — e.g., attention optimization with caption-based initialization vs. Visii — would strengthen the paper.

2. **How the qualitative comparison with Visii is not fully controlled.** Visii uses caption-based initialization, while InstructBrush uses transformation-oriented initialization AND attention-based optimization. The qualitative results (Figure 3) convincingly show InstructBrush avoids content leakage, but it is unclear how much of this improvement comes from the initialization vs. the optimization space. The ablation partially addresses this but could be more explicit.

3. **The GPT-4o + IP2P baseline is underspecified.** The paper states it "leverages GPT4o to compare differences between reference image pairs to obtain textual captions" but does not specify how many reference pairs are provided to GPT-4o, the prompt template used, or whether the same 10 training pairs are used. This makes the baseline hard to reproduce or interpret.

4. **The initialization failure rate is not quantified.** The paper acknowledges that when no phrase passes the sensitivity threshold η, the method falls back to a "None" instruction with no editing prior (Section 7). However, it does not report how many of the 25 editing effects in TOP-Bench suffer from this failure, nor whether performance degrades accordingly for those effects. This undermines the generality claim.

5. **Training time is mentioned as a limitation but not quantified.** The paper notes that optimization-based methods "increase the time cost" (Section 7) but provides no actual training time or compute requirements (e.g., GPU-hours per editing effect), making it difficult for readers to assess practical feasibility.

6. **No failure case analysis.** The paper shows only successful results. Showing at least 2–3 failure cases (e.g., artifacts, unsuccessful generalization) and discussing why they occur would improve the paper's scientific rigor.

### Trivial
None.

---

## Nice-to-Haves

- **One-shot evaluation (1 reference pair):** The paper focuses on few-shot (10 pairs), which is a reasonable choice. But evaluating with 1 pair would test whether the method degrades gracefully in the hardest case and would broaden the paper's applicability.
- **Sensitivity to number of training pairs:** A plot varying the number of reference pairs (1, 5, 10) would quantify data efficiency.
- **Cross-attention map visualizations:** Showing attention maps for the learned instruction vs. baselines would provide intuitive evidence that the optimization captures editing direction rather than content.

---

## Removed Points

- **Missing discussion of Custom Diffusion and K/V personalization methods:** Removed per hard rule: do not suggest missing related works.
- **Claim that InstructBrush is "worse than Visii on LPIPS and CLIP image similarity on TOP-Global":** Removed because it could not be verified from the text extraction (tables are images) and is directly contradicted by the strength finder's specific numbers. If the reviewer confused the direction of LPIPS (lower is better), this criticism would be factually wrong.
- **Criticism about missing details for after-set phrase extraction:** The paper states "With the above method, we can get the unique phrases \<p_x\> and \<p_y\> for sets {x} and {y}" (line 105), which clearly implies the same procedure applies symmetrically. The criticism is unwarranted.
- **Missing related works / missing appendix content / missing proofs:** Removed per hard rules.
- **Generic strengths from Strength Finder (e.g., "honest acknowledgment of limitations"):** Removed as generic and lacking specific concrete content.

---

## Novel Insights

The reviews reveal an interesting tension in the paper's contribution structure: the two main innovations (attention-based optimization and transformation-oriented initialization) are conceptually separable, yet the experimental design does not fully disentangle their individual effects against the prior work's pipeline. This creates a blind spot where a reader cannot tell whether attention-based optimization alone would outperform Visii's text-space optimization if both used the same initialization. The time-aware instruction component adds further complexity with mixed ablation results. The paper's core idea — that cross-attention features are a more expressive optimization space than text embeddings for representing editing effects — remains compelling and well-justified, but the evidence for it would be stronger if the paper had a more controlled comparison (e.g., attention-based optimization with caption initialization vs. Visii). None of the identified issues are fatal, and the paper's qualitative results are visually convincing, but the quantitative foundation needs reinforcement.

---

## Suggestions

1. **Strengthen quantitative evidence:** Add bootstrapped 95% confidence intervals to Table 1, report per-effect results (showing how many of the 25 effects InstructBrush wins), and include a statistical significance test (e.g., paired permutation test).
2. **Add a controlled comparison:** Compare attention-based optimization with caption-based initialization (the Visii initialization) against Visii's text-space optimization with the same initialization. This would directly isolate the benefit of the attention-based optimization space.
3. **Clarify the time-aware instruction trade-off:** Either explain why PSNR/SSIM decrease when this component is added (while semantic metrics improve), or present explicit visual evidence (Figure 15) in the main paper to justify the claim.
4. **Quantify initialization coverage:** Report for each of the 25 TOP-Bench effects whether the sensitivity threshold η was met, and show performance with/without successful initialization.
5. **Specify the GPT-4o baseline fully:** Provide the prompt template, number of example pairs given, and any post-processing steps.

---

## Score and Decision

**Originality:** Good — attention-based optimization in cross-attention space is a novel application of the idea.  
**Importance of research question:** High — visual prompt editing addresses a genuine gap where users cannot describe edits in language.  
**Claims well supported:** Partially — the headline claim of "superior performance" is backed by aggregate metrics, but the small test set (n=5 per effect) without statistical testing weakens the evidence.  
**Soundness of experiments:** Moderate — reasonable setup and clean ablation, but missing controlled comparison and statistical rigor.  
**Clarity of writing:** Good — well-organized with informative figures; some experimental details are vague.  
**Value to community:** Positive — the benchmark and method provide a foundation for future work.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
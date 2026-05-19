Now I have all the information I need to write the final consolidated review. Let me synthesize everything.

## Calibration Summary

**Round-1 bracket**: Based on initial calibration, I placed this paper between 4 and 6. The weak anchors (score ~3) had fundamental problems (broken evaluations, unclear contributions), while the strong anchors (score 8+) had rigorous theoretical grounding and comprehensive evaluations. This paper falls in between.

**Round-2 narrowing anchors** (all topically relevant):
- **CGDL (4.50, Reject)**: Weak evaluation, unclear contribution. Our paper is stronger.
- **TaSe (5.00, Reject)**: Decent method, but limited evaluation breadth. Comparable.
- **M-CBM (5.50, Accept Poster)**: Methodological concerns but clear contribution. Comparable.
- **Temporal Concept Dynamics (5.50, Accept Poster)**: Interesting analysis but narrow scope and evaluation gaps. Comparable.
- **Directional Textual Inversion (6.00, Accept Poster)**: Strong theoretical grounding, clean solution, but limited baselines. Our paper is weaker — less theoretical depth and more evaluation gaps.
- **T2I-ConBench (5.50, Reject)**: Useful contribution but limited evaluation. Comparable.
- **Consistent T2I / SDeC (6.00, Accept Poster)**: Solid theoretical framing and evaluation. Our paper is weaker.

This paper is stronger than the 4.5 papers and lower-end 5.0 papers, but weaker than the 6.0 papers. I place it at **5.0** — borderline between accept/reject with real contributions but meaningful evaluation gaps.

Now writing the review.

---

## Summary

2-3 sentence summary of the paper's contribution.

## Strengths

- strength 1 with evidence
- strength 2 with evidence

## Weaknesses

### Fatal
None.

### Major
- weakness 1 — why it matters
- weakness 2 — why it matters

### Minor
- weakness 1 — why it matters

### Trivial
- weakness 1

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision## Summary

This paper proposes a framework for learning disentangled visual concept embeddings along language-specified axes (e.g., *category*, *color*, *style*) by distilling from pre-trained vision-language models. It trains a set of concept encoders using two objectives: a reconstruction loss that inverts a frozen T2I model (DeepFloyd) and a text-anchoring loss that pulls embeddings toward BLIP-2's text predictions. At inference, concept embeddings from different images can be remixed for compositional generation, and a test-time finetuning procedure adapts to unseen concepts. The method is trained purely on synthetic images but transfers to real photographs.

## Strengths

1. **Novel framework for multi-axis disentangled concept learning.** The paper proposes training amortized concept encoders (one per axis) with both a reconstruction objective (Eq. 1) and a text-anchoring loss (Eq. 2). This goes beyond per-instance Textual Inversion by producing a shared embedding space that supports feed-forward inference and explicit axis-level control. (Section 3.1, Section 3.2)

2. **Training on synthetic data, inference on real images.** The encoders are trained exclusively on ∼669 DeepFloyd-generated images per dataset, yet at test time extract meaningful concept embeddings from real photographs (Fig. 2, Fig. 4). This demonstrates the method does not require expensive human annotations. (Section 4.1)

3. **Ablation study validates the anchor loss.** Removing the anchor loss $\mathcal{L}^\text{anchor}_k$ leads to poor disentanglement and recomposition (Section 4.4, Fig. 4), confirming that the text-anchoring mechanism is essential for axis separation. The ablation differentiates the contribution of the anchor loss from the encoder architecture itself.

4. **Both automatic and human evaluation.** The paper reports CLIP alignment scores (Table 1) and a human ranking study with 20 participants (Section 4.3), providing complementary evidence beyond a single metric.

## Weaknesses

### Fatal
None.

### Major

1. **Missing comparison against the most relevant baseline: Domain-Tuning.** The paper compares against Null-text Inversion + Prompt-to-Prompt and InstructPix2Pix — both image editing methods that were not designed for axis-disentangled concept manipulation. Domain-Tuning (Gal et al. 2023) is the most closely related method: it also trains amortized concept encoders using a T2I reconstruction loss and a CLIP image encoder, and the paper explicitly states it is "inspired by" Domain-Tuning (line 245). Yet Domain-Tuning is not included as a baseline in any quantitative or qualitative comparison. This is a significant gap because (a) it is the natural competitor that isolates the paper's claimed improvements (the anchor loss and the per-layer architectural change), and (b) the paper's results may not appear as strong against this baseline. The ablation against "per-instance optimization" (Section 4.4) is not a substitute for a direct Domain-Tuning comparison.

2. **Test-time finetuning claim is only qualitatively supported.** The ability to generalize to unseen concepts via test-time finetuning is listed as a core contribution (lines 76–77), but the only evidence is qualitative (Fig. 2 description, lines 280–283). There are no CLIP scores, no comparison against alternatives (e.g., standard Textual Inversion on the test image), no measurement of how many iterations are needed on average, and no analysis of whether disentanglement is preserved after adaptation. This claim is insufficiently supported by the evidence presented.

### Minor

1. **The disentanglement metric could be more direct.** The CLIP-alignment evaluation (Section 4.3, Table 1) measures alignment with modified prompts and with single-axis prompts. This partially captures whether non-target axes are preserved — for instance, checking alignment with "a photo of an apple" after a color change tests category preservation. However, the evaluation does not compare alignment *before* vs. *after* editing for the unchanged axes, which would provide a cleaner disentanglement signal. The human evaluation partially addresses this but is reported as an "average average score" without confidence intervals or per-axis breakdown.

2. **No statistical uncertainty reported.** The quantitative results (CLIP scores, human evaluation) are reported as point estimates without confidence intervals, standard deviations, or significance tests. Given the small training set (∼669 images) and the stochastic nature of the T2I generator, variance could be meaningful. This makes it difficult to assess whether reported differences between methods are reliable.

3. **Limited scope of concept axes and domains.** Training is on 5 domains with 2–3 axes each (category, color, material, style, season). The paper does not analyze scalability to more axes (e.g., adding texture, shape, pose) or more complex compositional prompts with simultaneous multi-axis changes. The method's generality is therefore not fully tested.

### Trivial

- The human evaluation reporting as "average average score normalized to 0-1" is ambiguous (Section 4.3). A clearer description of the normalization and aggregation is needed.
- The anchor loss weight $\lambda_k$ is set to 0.0001 for *category* and 0.001 for other axes (Section 4.1), but no sensitivity analysis is provided for this tuning choice.

## Nice-to-Haves

- **Direct comparison against Textual Inversion / Custom Diffusion** adapted to the axis-editing task would strengthen the evaluation. For example, learning a placeholder token on the test image and then prompting with axis-specific text (e.g., "a photo of a ⟨*⟩ which is orange in color") would directly test whether the multi-encoder approach outperforms per-instance inversion.
- **A before-vs-after disentanglement metric**: computing CLIP alignment with the *original* prompt for unchanged axes after an edit, and reporting the degradation, would provide a cleaner disentanglement signal.
- **Quantitative evaluation of test-time finetuning** (CLIP alignment before/after finetuning) and a comparison to per-instance optimization methods on the same images.

## Removed Points

- **Criticism that the quantitative metric "does not measure preservation of non-target axes"** — this is partially inaccurate. The single-axis prompt evaluation (e.g., measuring alignment with "a photo of an apple" after changing color) *does* measure whether the category was preserved. The critic's framing overstates the gap. I have kept the concern as a minor weakness about a more direct metric being preferable, but removed the stronger claim that the metric is invalid.
- **Criticism about insufficient baselines** — restructured from "baselines are uninformative" (which was overstated; InstructPix2Pix and Null-text Inversion + P2P are legitimate editing baselines for the task) to the specific missing comparison against Domain-Tuning, which is the most relevant baseline and has no obvious reason for omission.
- **Criticism about hyperparameter sensitivity of $\lambda_k$** — moved to Nice-to-Haves/Trivial because a sensitivity study is standard practice but not required for validity at the current evidence level.
- **Strength about test-time finetuning being "supported by qualitative results"** — removed because this strength conflicts with the verified weakness that this claim is only qualitatively supported. The strength claim is too strong relative to the evidence.
- **Generic strengths from the Strength Finder** about "important problem" — removed as lacking specific content.
- **Concerns about BLIP-2 accuracy analysis** — moved to Nice-to-Haves. While interesting, this is a secondary concern that the paper partially acknowledges (line 66: "BLIP-2 struggles to discern" fine-grained nuances).
- **Concerns about domain gap** — moved to Nice-to-Haves. Testing on a different synthetic distribution would be informative but is beyond the paper's stated scope of "train on synthetic, test on real."

## Novel Insights

The two reviews (Harsh Critic and Strength Finder) align on the paper's core value — the framework design is well-motivated and the combination of reconstruction and text-anchoring losses is sensible — but diverge sharply on whether the evaluation convincingly supports the claims. The key insight from synthesizing them is that **the paper's evidential weakest point directly contradicts its strongest claimed contribution**: the test-time finetuning procedure, listed as a contribution, has no quantitative support whatsoever. Meanwhile, the most severe evaluative gap (missing Domain-Tuning baseline) goes to the heart of whether the paper's architectural innovations outperform an existing amortized concept learning method that it explicitly builds on. The paper would be significantly strengthened by addressing these two gaps, which are connected — Domain-Tuning also supports test-time adaptation.

## Suggestions

1. **Add Domain-Tuning as a baseline.** This is the most direct comparison and would isolate the paper's claimed improvements (the anchor loss, per-layer design). If the proposed method outperforms Domain-Tuning, the paper's central claim becomes significantly stronger.
2. **Quantitatively evaluate test-time finetuning.** Report CLIP alignment scores (both target-axis and preserved-axis) after finetuning on unseen concepts, and compare against standard Textual Inversion applied to the same test images. This would transform the finetuning claim from a qualitative observation into a validated contribution.
3. **Add uncertainty estimates.** Report standard deviations or confidence intervals for all quantitative metrics across multiple seeds or dataset splits.
4. **Report a before-vs-after disentanglement analysis.** For axis-changes, show CLIP alignment with the original (pre-edit) prompt on the unchanged axes to directly measure whether those axes are preserved, rather than only checking that the new axis concept appears.

## Score and Decision

**Round-1 bracket**: 4–6 (informed by weak anchors at ~3 with fundamental flaws, and strong anchors at 8+ with rigorous evaluations).

**Round-2 narrowing**: Compared against 8 anchors in the 4.5–6.5 range. The paper is clearly stronger than the 4.5 anchors (CGDL, "Selectively Extracting and Injecting Visual Attributes" — both had limited scope and weak evaluation) and comparable to the 5.0–5.5 anchors (TaSe at 5.00/Reject, M-CBM at 5.50/Accept Poster, Temporal Concept Dynamics at 5.50/Accept Poster, T2I-ConBench at 5.50/Reject). It is weaker than the 6.0 anchors (Directional Textual Inversion with stronger theoretical framing; Consistent T2I/SDeC with tighter evaluation). Within this band, the paper sits at the lower end because the two major weaknesses (missing Domain-Tuning baseline, test-time finetuning unsupported) are addressable but leave the central claims less convincingly demonstrated than comparable papers that were accepted.

**Final score**: 5.0

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
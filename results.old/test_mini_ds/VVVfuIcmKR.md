Now I have enough calibration data. Let me construct the final review.

## Summary

This paper demonstrates that using CLIP representations for intra-modal tasks (e.g., image-to-image retrieval) is inherently suboptimal because CLIP's contrastive training objective neglects intra-modal alignment while enforcing inter-modal alignment. The authors propose converting intra-modal tasks into inter-modal ones via optimization-based modality inversion (OTI for images→text, OVI for text→images), showing consistent improvements across 15 datasets and 5 VLM variants. A critical control experiment — applying OTI to zero-shot classification (an inter-modal task) degrades performance — confirms that the gains stem from leveraging CLIP's inter-modal alignment rather than from optimization itself.

## Strengths

- **Quantitative evidence of intra-modal misalignment (Sec. 2, Dogs vs. Cats experiment)** — After filtering to ensure perfect inter-modal alignment, intra-modal image retrieval achieves only 81.4% mAP and 71.5% R-Precision, directly revealing that CLIP's intra-modal similarity rankings are wrong for a substantial fraction of relevant items. This is a clean, compelling demonstration of the core problem.

- **Consistent improvement across 15 datasets and 5 VLM variants (Table 1)** — OTI-based inter-modal retrieval outperforms the intra-modal baseline on every dataset and every model tested (OpenAI CLIP ViT-B/32, ViT-L/14; OpenCLIP DataComp B/32, L/14; SigLIP-B/16). The breadth rules out explanations tied to a specific architecture, pretraining dataset, or contrastive loss formulation.

- **Causal asymmetry via zero-shot classification control (Sec. 6.3, Table 2 right)** — Applying the *same* OTI-inverted features that improve image retrieval *degrades* zero-shot classification (e.g., ImageNet: 75.4% → 67.7% with ViT-B/32). This demonstrates that modality inversion does not universally improve tasks — it only helps when converting an intra-modal task into an inter-modal one, directly supporting the core thesis.

- **Geometric analysis of inverted features (Sec. 6.4, Fig. 3c)** — Pairwise cosine similarity distributions on COCO show that OTI-inverted features (R=1, 150 steps) produce similarity values closer to text-image distributions than to image-image distributions, confirming they remain on the text manifold and exploit cross-modal alignment.

- **Connection to intra-modal pretraining and modality gap (Sec. 6.5, 6.6)** — SLIP (which adds a SimCLR-style intra-modal loss) reduces the gap between intra- and inter-modal retrieval performance, and fine-tuning CLIP to close the modality gap (high temperature) eliminates the advantage of the inter-modal approach. These auxiliary experiments reinforce the causal story, though the evidence base is limited (3 datasets each).

## Weaknesses

### Fatal
None.

### Major
None that threaten the core claims. The paper's central argument — that intra-modal CLIP representations are suboptimal and that inter-modal approaches improve intra-modal tasks — is well-supported.

### Minor
- **SLIP and modality gap experiments cover only 3 datasets each (Tables 3, 4).** The paper makes broad claims that "SLIP reduces intra-modal misalignment" and "closing the modality gap alleviates intra-modal misalignment," but these auxiliary conclusions rest on Cars, EuroSAT, and Flowers (SLIP) or Cars, EuroSAT, and CIFAR-100 (modality gap). A pattern over 3 datasets is suggestive, not demonstrative. Since the paper already has features computed for all 15 datasets in Table 1, expanding these analyses would be straightforward and would substantially strengthen these secondary claims.

- **No variance or confidence intervals reported for any retrieval result.** Tables 1 and 2 report mAP without standard deviations, confidence intervals, or significance tests. Many improvements are modest (e.g., +1–2 mAP on several datasets), so without variance estimates it is unclear whether these differences are reliably above noise. While the consistent directional trend across 15 datasets mitigates this concern somewhat, individual dataset comparisons remain ambiguous.

- **OVI hyperparameter sensitivity is not analyzed.** The paper provides a detailed analysis of OTI's sensitivity to optimization steps and the number of pseudo-word tokens R (Sec. 6.4, Fig. 3a/b), but no equivalent analysis for OVI (number of pseudo-patches P, optimization steps). This asymmetry makes it harder to assess whether OVI's improvements are robust or dependent on narrow hyperparameter tuning.

- **The causal attribution is not fully isolated.** The paper's central claim is that OTI/OVI improve intra-modal tasks *because* they leverage inter-modal alignment. The zero-shot classification control (Sec. 6.3) is a clever and partially effective control, but it does not rule out the possibility that any nontrivial feature transformation — even within the same modality — could improve retrieval by acting as a denoising or feature-refinement step. A baseline that optimizes pseudo-patches through the *image* encoder alone would more directly isolate the effect of crossing modalities. This does not invalidate the empirical finding, but it weakens the precision of the causal explanation.

### Trivial
- The OVI description in Sec. 5.2 introduces nearest-neighbor interpolation without justifying the choice over alternatives (e.g., bilinear interpolation). A brief rationale would be helpful.

## Nice-to-Haves
- **Within-modality optimization baseline:** Adding a control where pseudo-patches are optimized through the *image* encoder (same modality) for retrieval would cleanly isolate whether the benefit comes from crossing modalities or from optimization itself.
- **Runtime/cost reporting:** The paper acknowledges OTI/OVI are computationally expensive (150/1000 steps) but provides no concrete numbers. A brief GPU-time-per-query figure would help readers assess practical trade-offs.
- **Simple feature transformation baselines:** Adding baselines like feature mean-centering or whitening would help contextualize the size of the OTI improvement.
- **OVI hyperparameter analysis:** Extending the analysis in the style of Fig. 3a/b to OVI (varying P and optimization steps) would improve completeness.

## Removed Points
- **Criticism that "single-feature level" is overstated because OTI uses a template sentence:** The paper transparently describes the "a photo of" template. The claim about "single-feature level" refers to not needing external data or trained mapping networks, which is accurate. This is a misunderstanding. **Removed.**
- **Strength Finder's generic strengths about "this paper addresses an important problem":** These are superficial and lack specific content. **Removed.**
- **Missing related works:** Not verifiable without external sources. **Removed.**
- **Formatting/style nitpicks, missing appendix, and similar artifacts:** These are parser issues, not author errors. **Removed.**
- **Reproducibility concerns about unreleased models/datasets:** All cited entities are assumed to exist. **Removed.**
- **Speculative fatal flaws (e.g., "if normalization were X, values would be impossible"):** Not grounded in paper content. **Removed.**
- **Criticisms about missing variance for auxiliary SLIP/modality gap experiments:** Already covered in the main weakness about limited datasets. **Merged.**

## Novel Insights
None beyond the paper's own contributions. The harsh critic and strength finder both converge on the same assessment: the paper's central finding is solid, the zero-shot classification control is elegant, and the main limitations are about precision (variance, limited auxiliary datasets) rather than validity.

## Suggestions
1. **Add variance estimates** (bootstrapped CIs or standard deviations over multiple splits) for the retrieval results, especially for the smaller improvements (+1–2 mAP).
2. **Expand the SLIP and modality gap experiments** from 3 datasets to at least the same 15 used in the main retrieval evaluation. The features are already computed; this requires only running additional comparisons.
3. **Add a within-modality optimization baseline** (optimizing pseudo-patches through the image encoder alone) to more cleanly isolate the benefit of crossing the modality gap.
4. **Include a brief OVI hyperparameter sensitivity analysis** (varying P and optimization steps), even if deferred to supplementary material.
5. **Report approximate GPU-time per query** for OTI and OVI to help readers assess computational cost.

## Score and Decision

**Round 1 (Bracketing):** The paper is clearly stronger than the weak-band anchors (LLM2CLIP at 3.0, RetFormer at 3.0, Mul2Vec at 3.0, Multimodal CIL at 2.33) which have fundamental flaws, narrow scope, or incorrect methodology. The paper is comparable to mid-band anchors (AlignCLIP at 6.29, Understanding CLIP at 6.50, SemiCLIP at 5.80, Contrastive Gap at 4.75) but weaker than strong-band anchors (CLIP Data Selection at 7.50, Interpreting CLIP at 8.0). **Initial bracket: 5.0–6.5.**

**Round 2 (Narrowing):** Retrieved anchors within the bracket — AlignCLIP (6.29, accepted): proposes a method to reduce the modality gap, similar solid empirical contribution with some novelty concerns. Understanding CLIP Transfer (6.50, accepted): theoretical analysis with small-scale experiments. SemiCLIP (5.80, accepted): semi-supervised CLIP adaptation, well-executed but incremental. The paper under review is:
- **Better than** the Contrastive Gap paper (4.75) which had a fundamental misunderstanding of CLIP's loss function
- **Comparable to** AlignCLIP (6.29) — both are solid empirical papers with clear contributions and addressable weaknesses
- **Comparable to** SemiCLIP (5.80) — both make genuine contributions with experimental thoroughness
- **Slightly weaker than** Understanding CLIP Transfer (6.50) which provides theoretical analysis in addition to experiments

**Final score: 6.0.** The paper makes a clear, well-supported contribution demonstrating intra-modal suboptimality of CLIP and showing that inter-modal approaches improve performance. The weaknesses (limited auxiliary experiments, no variance reporting, incomplete causal isolation) are addressable and do not undermine the core finding.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
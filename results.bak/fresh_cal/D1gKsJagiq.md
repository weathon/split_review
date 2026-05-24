Now I have a thorough understanding of the paper and can verify claims directly. Let me compose the final review.

## Summary

This paper proposes Dual-Stream Adapters (DSA), a parameter-efficient adapter architecture tailored for anomaly segmentation in driving scenes. The method introduces three novel components: (i) an anomaly prior module that learns separate initial ID and OOD feature embeddings via distinct level encodings, (ii) a dual-stream feature refinement module that symmetrically processes each stream through cross-attention with a frozen ViT backbone, and (iii) an uncertainty-based hyperbolic loss that uses Cityscapes void labels as OOD supervision. DSA achieves competitive or state-of-the-art results on Fishyscapes, SMIYC, and Road Anomaly benchmarks while using 38% fewer trainable parameters than Mask2Anomaly with Swin-L.

## Strengths

1. **Novel dual-stream architecture explicitly tailored for anomaly segmentation** — Unlike general-purpose vision adapters (ViT-Adapter, Side Adapters), DSA introduces separate streams for ID and OOD features via distinct level encodings in the anomaly prior module and symmetric cross-attention refinement. Figure 3 clearly contrasts this design with existing adapters. Table 1 confirms that DSA-Tiny outperforms the single-stream ViT-Adapter and Side Adapters on anomaly segmentation metrics, establishing that specialization for the anomaly segmentation task brings concrete gains.

2. **Component-wise ablation validates each proposed component** — Table 5(a) on SMIYC RO-21 shows that removing the anomaly prior module, dual-stream feature refinement, or the hyperbolic loss each causes a significant drop in AuPRC and FPR95. This establishes that all three novel components contribute meaningfully to the overall performance.

3. **Competitive results across multiple benchmarks with parameter efficiency** — Table 3 shows DSA-Large achieves the best *average* performance across Fishyscapes, SMIYC, and Road Anomaly datasets. The method's core design goal — reducing training parameters while maintaining competitive anomaly segmentation — is achieved. The removal of the injector cross-attention (motivated in the paper) further streamlines the design.

4. **Hyperbolic loss formulation is well-motivated** — The loss leverages a known property of Poincaré ball embeddings (Atigh et al., 2022) — that L2 distance to the origin captures uncertainty — and applies it to supervise feature separation using void labels. This provides a principled, mathematically grounded training signal that does not require external outlier data.

## Weaknesses

### Fatal
None.

### Major

1. **The dual-stream architecture's benefit is not isolated from increased model capacity.** The paper compares DSA-Tiny against ViT-Adapter and Side Adapters (Table 1), but these are single-stream adapters with *fewer* trainable parameters. A single-stream adapter with *the same total parameter count* (e.g., doubled feature dimensions or additional refinement modules) could match the reported gains simply through added representational capacity. Without this control experiment, the paper cannot attribute improvements to the *architectural choice* of dual streams versus the *confounding variable* of extra parameters. The ablation in Table 5(a) partially addresses this by removing components, but the capacity confound remains because the single-stream baseline is not capacity-matched.

2. **The advantage of hyperbolic space over an equivalent Euclidean formulation is not demonstrated.** The loss ablation in Figure 6(b) compares the hyperbolic loss against binary cross-entropy and a contrastive loss, but these are fundamentally different objectives. A proper ablation would compare against a Euclidean analogue of the *same* distance-to-origin objective (e.g., projecting features into Euclidean space, computing L2 distance to the origin, and applying the same sign-based ID/OOD push-pull). Figure 6(a) varies the Poincaré ball curvature but does not include a Euclidean baseline (effectively curvature=0). Without this comparison, the claimed advantage of hyperbolic geometry over Euclidean space for the proposed loss is not empirically supported.

### Minor

1. **No in-distribution segmentation results are reported.** The paper claims the method "maintains higher accuracy on the in-distribution data" (Section 1, line 17), but no mIoU or other ID segmentation metrics on Cityscapes val/test are provided anywhere in the text. This claim must be backed by evidence, and it matters because trade-offs between ID accuracy and anomaly detection performance are a known risk.

2. **The "state-of-the-art" claim is overstated without qualification.** The abstract says "dual-stream adapters achieve the best results," but the Table 3 caption states "on average our DSA-Large model obtains the best results." Being best on average does not mean best on every benchmark, and Figure 1 plots only one data point per method (the average). The 38% parameter reduction claim is valid but contextualizes only training parameters, not the total system cost (frozen ViT-L backbone storage and inference).

3. **Weight sharing between the two streams is ambiguous.** The paper describes "the same sequence of operations is implemented for the OOD stream" (Section 4.2) — it is unclear whether the ID and OOD streams share cross-attention and FFN parameters or learn independent parameters. This matters for parameter counting and for understanding whether the two streams truly specialize.

4. **The use of Cityscapes void/background as OOD supervision is not analyzed.** The paper uses void labels as OOD supervision (Section 4.3) without examining potential false positives on void regions (sky, building facades, road margins) that are not actually anomalous. While other methods (marked ∇ in Table 3) also use void labels, an analysis of how void-label supervision affects predictions on these regions would strengthen the paper.

5. **No statistical significance measures are reported.** Given the small margins between methods on some benchmarks (e.g., differences of 0.2–0.5% AuPRC), single-run results without confidence intervals or multiple trials make it impossible to assess whether the reported gains are reliable.

### Trivial
None — all identified issues are at least minor in substance.

## Nice-to-Haves

- A capacity-matched single-stream baseline (same total trainable parameters, single stream) to isolate the architectural benefit of the dual-stream design.
- A Euclidean version of the distance-to-origin loss (same formulation, Euclidean distance instead of hyperbolic) to demonstrate the specific advantage of hyperbolic geometry.
- Analysis of false positives on Cityscapes void regions (sky, building surfaces, road margins) when void = OOD supervision is used.
- ID segmentation mIoU on Cityscapes val/test to substantiate the claim of maintaining ID accuracy.
- Inference FLOPs and latency comparison to complement the training parameter efficiency narrative.
- Explicit statement on whether ID and OOD streams share weights.

## Removed Points

Criticisms removed with justification:

1. *"The paper does not control for the supervision signal when claiming state-of-the-art"* (Harsh Critic, Issue #2). **Removed** because Table 3's caption explicitly marks which methods use void labels (∇) and which use outlier exposure (♠). The paper does disclose and differentiate the supervision signals used by each method.
2. *"The equation in the PDF is an image"* (Section-by-Section Notes). **Removed** — this is a PDF extraction artifact, not a paper flaw.
3. *"The removal of the injector is motivated only empirically"* (Section-by-Section Notes). **Removed** — empirical motivation is standard and valid; the paper also already provides rationale (parameter efficiency).
4. *"The level encoding is quite weak as the sole mechanism for specialization"* (Section-by-Section Notes). **Removed** — this is a subjective opinion about design strength, not a verifiable weakness. The ablation study shows the encoding contributes non-trivially.
5. *"The loss weight is set to 0.1 without justification"* — converted to a removed point as this is a standard tuning detail; many papers set loss weights without exhaustive justification.
6. *Strength Finder: generic/superficial strengths dropped* — e.g., "parameter-efficient design choice justified" is kept as part of the broad evaluation but is not elevated as a standalone strength.

## Novel Insights

The reviews surface a consistent pattern: the paper's contributions are individually well-motivated but each suffers from an incomplete isolation experiment. The dual-stream architecture is compared against smaller-capacity single-stream baselines but not against a capacity-matched single-stream control; the hyperbolic loss is ablated against different loss families but not against a Euclidean instance of the same loss family; the void-label supervision is used and disclosed but never analyzed for its side effects. None of these gaps are fatal — each is fixable — but together they prevent the paper from proving that its specific architectural and geometric choices are what drive the reported improvements, rather than confounding factors (capacity, different loss objectives, dataset artifacts).

## Suggestions

1. **Add a capacity-matched ablation.** Design a single-stream adapter with the same total trainable parameters (e.g., 2× feature dimension or 2× refinement modules) and compare performance. This directly tests whether the dual-stream *architecture* or simply *more parameters* is responsible for the gains.

2. **Add a Euclidean loss ablation.** Implement the same distance-to-origin push-pull loss using Euclidean distance (no exponential map) and compare against the hyperbolic version. This isolates the benefit, if any, of hyperbolic geometry.

3. **Report ID segmentation mIoU.** Provide Cityscapes val mIoU for DSA and baselines to substantiate the claim that ID accuracy is maintained or improved.

4. **Qualify the "state-of-the-art" claim.** State explicitly in the abstract and conclusion that DSA-Large achieves the best *average* performance, and note the specific benchmarks where it is first versus second best.

5. **Clarify weight sharing.** State explicitly in Section 4.2 whether the ID and OOD streams in the dual-stream feature refinement module have independent or shared parameters.

## Score and Decision

The paper addresses a timely and practical problem (training-efficient anomaly segmentation), proposes a novel architecture with clear motivation, and achieves competitive results validated by component ablations. The weaknesses are substantive but addressable — they do not invalidate the core contribution (the dual-stream design and its empirical effectiveness) but do prevent the paper from proving its strongest claims about *why* the design works. The two major weaknesses (capacity confound, unvalidated hyperbolic advantage) require additional experiments that could be completed during a revision.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
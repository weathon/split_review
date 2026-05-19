Now I have a good understanding of the calibration anchors. Let me write the consolidated review.

## Summary

CONCORD proposes a training-free, inference-time method for dataset distillation that uses LLM-retrieved fine-grained concepts (descriptive attributes) to guide the diffusion denoising process. The method retrieves distinguishable concepts per category via LLM prompting, filters them for validity against real data using CLIP, and then employs a contrastive objective (positive + similarity-weighted negative concepts) to steer the reverse diffusion. Experiments on ImageNet-1K, ImageNet-100, ImageWoof, and Food-101 show consistent improvements over Minimax and Stable Diffusion unCLIP baselines, achieving state-of-the-art results.

## Strengths

1. **Novel and well-motivated core idea**: The paper identifies a genuine limitation in generative-prior-based dataset distillation — the lack of explicit instance-level control during generation — and addresses it by injecting LLM-retrieved fine-grained concepts into the diffusion process. The motivation (Fig. 1 showing missing/incorrect details in baseline images) is clear and compelling.

2. **Contrastive matching with similarity-weighted negative concepts is effective**: The paper demonstrates through ablation (Tab. 5, 6) that the contrastive objective with weighted negative sampling (favoring similar categories while maintaining diversity) provides clear and stable gains over alternatives (random negatives, fixed-range negatives, cosine objective, classifier guidance). This design choice is well-justified.

3. **State-of-the-art results across multiple datasets and baselines**: CONCORD achieves the best reported accuracy on ImageNet-1K at IPC 50 (66.4% with Minimax+CONCORD, Tab. 2) and shows consistent improvements on ImageWoof, ImageNet-100, and Food-101 across both Minimax and unCLIP baselines. The gains are systematic, not cherry-picked.

4. **Generalizability**: The method is evaluated on two different generative pipelines (Minimax, Stable Diffusion unCLIP Img2Img) and across four datasets spanning different domains and granularities, demonstrating that the concept-informing mechanism is not tied to a specific diffusion pipeline.

5. **Training-free at inference**: CONCORD operates without additional training of the diffusion model, making it practical to apply to existing pipelines as a plug-in.

## Weaknesses

### Fatal
None.

### Major

1. **Inconsistency in the informing weight λ between the main experimental setup and the parameter analysis.** Section 4.1 (Implementation Details) states: "The informing weight λ in Eq. 9 is set as 1." However, Section 4.4 (Parameter Analysis) states: "Through comparison, we set the value of λ as 2.0 for balance between sufficient control and stable denoising." It is unclear which λ was used to produce the main results in Tables 1–3. If the main experiments used λ=1 while the optimal λ=2 (per Fig. 4b), the reported results may be understated — but equally, the reader cannot verify the results are optimal. **This is a concrete inconsistency that undermines trust in the reported numbers and must be resolved.** The authors must clarify exactly which λ was used for each experiment and why.

2. **No quantitative ablation comparing fine-grained concepts against class-name-only conditioning.** The paper's central thesis is that fine-grained, LLM-generated concepts provide better control than coarse signals. The only direct comparison is qualitative (Fig. 3, which shows some support). The quantitative ablation in Table 4 compares two prompt designs (classification-style vs. distinguishable-style) for concept *retrieval*, neither of which is a "class name only" baseline. Without an ablation using the class name (e.g., "beagle") as the sole concept in the same matching objective, it is possible that improvement comes from any text conditioning rather than from the granularity of retrieved concepts. This is an evidential gap for the paper's core claim.

### Minor

3. **Overstated claim about not relying on pre-trained classifiers.** The abstract states the method operates "without replying on pre-trained classifiers" and the introduction says it "eliminates the dependence on pre-trained classifiers." However, CONCORD heavily depends on **CLIP**, a pre-trained vision-language model, for both concept validity filtering (Eq. 10) and the matching objective (Eqs. 11–12). While CLIP is not a classifier trained on the target dataset, it is still a pre-trained external model that provides the gradient signal for guidance. The distinction from classifier guidance (Dhariwal & Nichol) is valid, but the current phrasing is misleading. The paper should acknowledge this reliance explicitly and discuss whether CLIP's availability could be a limitation for specialized domains.

4. **Missing computational overhead analysis.** The paper acknowledges added computational cost in the limitations section but provides no quantification. For a method that is claimed to be practical, a wall-clock time comparison (time per generated image with and without CONCORD, total distillation time) would significantly strengthen the paper. This is not a fatal omission but would substantially improve reproducibility assessment.

### Trivial
None.

## Nice-to-Haves

- A discussion of what happens when LLM-retrieved concepts are not well-captured by the CLIP embedding space (i.e., when the validity filter may discard useful concepts that CLIP does not represent well).
- Clarifying in Algorithm 1 which exact objective (Eq. 11 vs. Eq. 12) is used at each step.
- A runtime/overhead table as noted in Minor weakness 4.

## Removed Points

- **Typo "replying on"**: This is a parser artifact; the original submission does not have this issue.
- **Tables presented as embedded images**: Parser limitation, not a paper defect.
- **Variance values not visible in extracted tables**: Parser limitation.
- **Missing discussion of LLM concepts not captured by CLIP**: Speculative/scope-creep; the paper acknowledges limitations generally.
- **Missing related works**: Cannot verify without external knowledge.
- **Pure formatting/style nitpicks**: Not author issues.
- **Strawman weaknesses that misunderstand the paper**: None found in the inputs, but several speculative concerns from the harsh critic's section-by-section notes were removed per the filtering rules.
- **Strength Finder's generic strengths**: Strength Finder claim about "Training‑free approach without pre‑trained classifiers" partially conflicts with verified weakness #3 — the weakness wins. The qualified version (training-free *at inference*, relying on CLIP for guidance) is preserved in the strengths section.

## Novel Insights

The reviews surface an interesting dynamic: the harsh critic and strength finder agree that CONCORD's core idea is strong and well-motivated, but the harsh critic's most valid points are not about the method's soundness *per se* but about gaps in verification (the λ inconsistency and the missing class-name baseline). This pattern suggests that the paper's novelty is intact but its experimental presentation needs tightening. A meta-level observation: CONCORD's reliance on CLIP for the matching objective means the method inherits both the strengths and blind spots of CLIP's embedding space — this is a property shared with many CLIP-guided generation methods and is not unique to this paper, but it deserves more explicit acknowledgment.

## Suggestions

1. **Resolve the λ inconsistency**: State clearly which λ was used for each main experiment, and if λ=1 was used instead of λ=2 (the ablation's optimal), re-run the main tables with λ=2.0 to report the true optimal performance.

2. **Add a class-name-only baseline**: Insert a row in Table 4 (or a separate table) where the only concept is the class name (e.g., "beagle") using the same matching objective. This directly validates the core claim about fine-grained concepts.

3. **Qualify the "no pre-trained classifiers" claim**: Acknowledge reliance on CLIP explicitly and discuss domain limitations.

4. **Add a computational cost table**: Report wall-clock generation time with and without CONCORD for a representative setting (e.g., IPC 50 on ImageWoof).

## Score and Decision

**Round-1 bracket:** [4.5, 5.5]

**Round-2 anchoring:** Narrowed against DAP (5.50, Accept Poster) and CoDA (4.50, Accept Poster), the two most topically similar anchors. CONCORD's core idea is more novel than CoDA's clustering+guidance pipeline, placing it above 4.5. However, CONCORD's λ inconsistency is a more concrete weakness than DAP's clarity issues, placing it slightly below DAP at 5.0. CONCORD is comparable in quality to PDS (5.60, Accept Poster) and stronger than DIVER (4.50, Reject).

**Anchor papers consulted:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| Hvge3NzkJN.md (DAP) | 5.50 | R1/R2 | More polished presentation but less novel core idea; CONCORD is slightly weaker due to λ inconsistency |
| 6ycBM1nsS3.md (CoDA) | 4.50 | R1/R2 | CONCORD has a more novel and cleaner idea than CoDA's heuristic pipeline |
| FMSp8AUF3m.md (DDOQ) | 5.00 | R1 | Comparable quality; DDOQ has better theory but CONCORD has more novel application |
| jKGvmZixqc.md (DIVER) | 4.50 | R2 | CONCORD is notably stronger than DIVER (rejected) |
| bl3drImevi.md (PDS) | 5.60 | R2 | CONCORD is slightly lower due to λ issue; PDS is multimodal DD |
| JRfZuc6zqI.md (Flash-DD) | 5.50 | R2 | FLASH-DD was rejected despite its score; CONCORD's weaknesses are less severe |
| aeexHSFefN.md (MMD Guidance) | 4.50 | R2 | Not DD-specific, less relevant; CONCORD is stronger |
| ulEcmq3IhC.md (Concept Sliders) | 4.00 | R2 | Not DD, less relevant; CONCORD is substantially stronger |

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>
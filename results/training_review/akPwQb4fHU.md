I now have a thorough understanding of the paper and the reviewer claims. Let me write the consolidated review.

---

## Summary

This paper introduces DeSSeR, a training-free zero-shot segmentation framework that uses MLLMs (GPT-4o, CogVLM) to supply semantic expertise for vision models (SAM). The core idea is to decompose segmentation into three stages — recognize, localize, segment — and add selective re-localization with MLLM gridding to recover from localization failures. The method is evaluated on camouflage object detection (COD), zero-shot anomaly detection (ZSAD), and polyp segmentation, claiming 10%+ improvements over zero-shot baselines.

## Strengths

- **Well-motivated decomposition of the zero-shot segmentation problem into recognize → localize → segment.** The paper identifies that the bottleneck in challenging zero-shot segmentation is semantic understanding rather than low-level segmentation ability, and the three-stage pipeline is a natural architectural consequence of this insight (Section 2.2). The analysis of why MLLM-based localization benefits from first recognizing the object name before localizing it (Section 3.1) is a simple but non-trivial finding.

- **Explicit handling of localization failures via selective re-localizing with MLLM gridding (Section 3.3).** The paper identifies two concrete failure modes for MLLM-based localizers (confusing text prompts and localizer inability) and proposes a sampling-based uncertainty check combined with a gridding fallback that leverages the recognizer's verification ability. This is a practical contribution that goes beyond a naive two-stage pipeline.

- **Training-free approach that covers three diverse challenging tasks.** The method works across camouflage, anomaly detection, and medical polyp segmentation without any task-specific fine-tuning. This cross-task generality is a genuine strength, especially since many prior works are specialized to one domain.

- **Ablation studies evaluating design choices at each stage.** The text references ablations of model choices (Table 4), visual prompt types (Table 5), and instance-aware vs. category-only prompts (Table 6), indicating the authors systematically examined their design decisions rather than reporting a single black-box result.

## Weaknesses

### Fatal
None.

### Major

- **The paper lacks a direct comparison against the simplest "MLLM→SAM" baseline — calling an MLLM once to produce a bounding box, then feeding it to SAM without decomposition, uncertainty estimation, or gridding.** Without this baseline, it is impossible to attribute the claimed 10%+ improvements to the specific contributions (decomposition, selective re-localizing, gridding) rather than to the mere use of a more capable MLLM (GPT-4o) in the loop. The paper references comparisons against zero-shot methods in Table 2 and ablations in Tables 3–6, but the table images are not rendered in the parsed text, so it is unclear whether this critical baseline is included. Even assuming it is, the paper's writing does not explicitly discuss or argue against this simpler alternative, which is the natural ablation that would validate the proposed components.

- **The uncertainty estimation procedure is critically underspecified.** The paper states "we propose to use sampling for uncertainty estimation" (Section 3.3.1) and Algorithm 1 takes a parameter `n` for "times for uncertainty estimate," set to `n=1` in the hyperparameters (line 151). However, there is no description of *how* sampling is performed — no mention of temperature, nucleus sampling parameters, or any stochastic decoding strategy. If the localizer (CogVLM) is deterministic at inference, comparing box and box_this at n=1 would produce identical boxes and yield no signal. Even if the model supports stochastic sampling, the reviewer cannot reproduce the results without knowing the sampling configuration. This is a cross-community reproducibility gap: MLLM papers routinely report sampling parameters, but this paper omits them entirely.

### Minor

- **The motivating experiment (Section 2.2) and the localization analysis experiments (Section 3) are conducted on 100 images from CAMO, but the paper's scope covers three different tasks with very different visual properties (camouflage, industrial anomalies, medical polyps).** The paper does not replicate the key analysis experiments (e.g., decomposition helps localizing, gridding saves failures) on the other two datasets. While the main evaluation (Section 4) tests on all three datasets, the ablation evidence supporting the *design choices* (decomposition, gridding) is only shown on CAMO. Since medical images and industrial anomalies have very different failure modes than camouflage, some of the design conclusions may not transfer.

- **The paper claims cost-effectiveness but provides no cost or latency analysis.** Section 3.4 adopts a "cost-effective fixed-point prompt" strategy, but no API call costs, latency measurements, or per-image token counts are reported for the full pipeline. Given that each image potentially requires multiple MLLM calls (recognizer + localizer + uncertainty verification + potential gridding), the actual computational and financial cost is non-trivial and should be quantified.

- **The writing has clarity issues that occasionally obscure the technical content.** The text switches between "VLMs" (Abstract, line 4: "Large vision models (VLMs)") and "LVMs" (line 16: "Large Vision Models (LVMs)") for the same concept. Some phrasings are ambiguous: "boxes with 10% off accuracy" (Section 2.2) is unclear — 10% off relative to what? Figure-ground? Pixel IOU? These issues do not invalidate the contribution but slow comprehension.

### Trivial
- The paper's scope section (3.5) excludes COCO and other normal datasets but does not provide any diagnostic experiment showing that DeSSeR does not catastrophically degrade on easy cases, which would help calibrate the claims of generalizability.

## Nice-to-Haves

- A variant evaluation using a smaller/open-source MLLM in place of GPT-4o would strengthen the claim that the method's value is in its architecture rather than the specific proprietary model's capability.
- Confidence intervals or variance estimates for the main results would help assess stability, especially given the stochastic nature of MLLM sampling.

## Removed Points

The following criticisms raised by reviewers are removed (with brief justification):

1. **"Tables/figures are not present in the text so the paper cannot be evaluated."** — The tables are embedded as images in the PDF. The parser strips images but the captions and references exist. This is a parser artifact, not an author error.

2. **"Grounded SAM is not cited / the pipeline is the same as Grounded SAM."** — Per policy, missing related works should not be asserted. Moreover, the paper's pipeline uses MLLMs (GPT-4o, CogVLM) rather than Grounding DINO as the localizer, and its contributions (decomposition, gridding, uncertainty) go beyond the simple two-stage design.

3. **"The n=1 resampling makes uncertainty estimation impossible."** — The algorithm calls `loc()` twice: once for `box` (line 5) and once for `box_this` (line 7). With n=1, these are 2 separate samples. If the model supports stochastic decoding, the comparison is meaningful. The real issue is underspecification of the sampling procedure, not impossibility.

4. **"Motivating experiment draws sweeping conclusions from 100 CAMO images."** — The motivating experiment is explicitly scoped as illustrative (Section 2.2). The main evaluation (Section 4) tests all three datasets. This reviewer conflation is not a paper flaw.

5. **"fails completely claim is unsupported"** — The claim is supported by Table 1 and Figure 2, whose content is not visible due to parser stripping. The paper does provide evidence; it is simply not renderable in the parsed text.

6. **"Pure formatting/style nitpicks and typo-level criticisms."** — Removed per policy.

7. **"The paper should include missing appendix/proofs."** — The parser strips appendices; they exist in the original submission.

## Novel Insights

The reviews do not surface any insight about the paper that goes significantly beyond what the authors themselves articulate. The idea of using MLLMs for semantic grounding is not new, but the specific decomposition with selective re-localizing and gridding is a practical engineering contribution. The key tension the paper does not fully resolve is: how much of the gain comes from the *architecture* (decomposition, gridding) versus the *raw capability* of the chosen MLLM (GPT-4o)? The absence of a controlled baseline isolating this question is the single most important gap.

## Suggestions

1. **Add a direct baseline: "MLLM → SAM" in one step.** Run GPT-4o once to predict a box ("Where is the [target]?") and feed that box to SAM. Compare against the full DeSSeR pipeline. This would isolate the value of decomposition, uncertainty estimation, and gridding.

2. **Specify the sampling procedure for uncertainty estimation.** State the temperature, top-p, and number of samples used. If the localizer is deterministic (greedy decoding), explain how two different outputs are obtained (different prompts? different random seeds?).

3. **Replicate the key analysis experiments (decomposition benefit, gridding vs. direct localization) on at least one non-CAMO dataset** to show the design insights transfer to other domains.

4. **Report the end-to-end cost.** Provide total API calls per image, average latency, and approximate dollar cost. This is important for any practitioner considering using the method.

5. **Fix the VLM/LVM terminology inconsistency** for clarity.

## Score and Decision

The paper proposes a timely and practically motivated approach, and the decomposition+gridding ideas are sensible engineering contributions. However, the lack of a controlled baseline comparison against a simple "MLLM→SAM" pipeline makes it difficult to assess how much of the claimed gains are due to the proposed architectural innovations versus the inherent capability of the chosen MLLM. The underspecification of the uncertainty sampling procedure is a reproducibility concern. These are significant but addressable weaknesses. The core direction has merit, and the paper opens a useful perspective.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
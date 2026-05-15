Now I have all the information I need. Here is my consolidated review:

---

## Summary

This paper investigates *when* image data should be introduced during vision-language model (VLM) pre-training, challenging the standard practice of fully pre-training the LLM on text before adding vision. The authors train ~300 models at 79M and 1B scales, resuming from intermediate text-only checkpoints (20%, 40%, 60%, 80%, 100%) and continuing with image-text mixtures. They report that introducing images during the cooldown phase (at ~80% of text-only pre-training) yields a 2% average improvement over the conventional approach of starting from a fully pre-trained text model, and that a 10–20% visual token ratio is optimal at the 1B scale.

## Strengths

- **Well-motivated, practically important research question.** The paper targets a genuine gap in the VLM literature: most popular recipes fully pre-train the LLM on text before adding vision, but the community lacks systematic evidence on whether this two-stage separation is optimal. The question has direct implications for how future VLMs are trained.

- **Clean experimental framework using intermediate checkpoints.** The approach of resuming from DCLM-1B checkpoints at multiple pre-training milestones (20%–100%) is methodologically sound. It allows the authors to vary the timing of image introduction while holding the model architecture, data, and compute budget fixed, providing a controlled test of when to add vision data.

- **Evaluation across diverse vision and text tasks with a principled aggregate metric.** The paper evaluates on 6 vision-language tasks and a suite of text benchmarks, using the "stable score" (accuracy minus random baseline) to produce a clean, interpretable aggregate. This multi-task evaluation strengthens confidence that findings are not artifacts of a single benchmark.

- **Transparency about the LR schedule confound.** The paper explicitly marks the 100% checkpoint with hollow circles in Figure 4 (different LR schedule), states that "the learning rate schedule is different and could affect the results" (line 128), and describes the scheduler discontinuity in the text. This transparency is a methodological strength.

## Weaknesses

### Fatal

None.

### Major

- **The headline comparison (80% vs 100%) is confounded with the learning rate schedule.** The paper's primary quantitative claim—that introducing images at 80% of text-only pre-training yields a 2% improvement over introducing them after full pre-training—compares two settings that differ not only in the checkpoint used but also in the LR schedule. The 80% checkpoint continues the original cosine decay; the 100% checkpoint requires a re-warmup with a different peak LR (3×10⁻³). The paper acknowledges this difference and marks the 100% points with hollow circles, but nonetheless interprets the performance drop at 100% causally as evidence that "continued training is preferable to re-training a 100% fully pre-trained text model" (line 129). This interpretation is not fully justified: the observed drop could stem partly or entirely from the schedule discontinuity rather than the checkpoint selection. The broader trend (20% → 80% improvement with more text pre-training) remains clean and supports the value of intermediate checkpoints, but the specific 80% > 100% claim needs a controlled comparison—e.g., applying the same re-warmup to the 80% checkpoint or trying an alternative schedule for 100%—to be fully persuasive.

- **The optimal image-text ratio claim (10–20% visual tokens) cannot be evaluated from the provided text.** This finding is advertised in the abstract and introduction (line 23) as a central contribution, and the paper promises supporting experiments in Sections 3.2 and 3.3. However, these sections are absent from the parsed paper text (Section 3.2 is only a header; Sections 3.3–3.5 are entirely missing). Similarly, the findings about instruction fine-tuning timing (Sections 3.4, 3.5) are referenced but cannot be verified. While this is likely a PDF-parsing artifact rather than an author omission, it means the review can only assess the paper's methodological framework and Section 3.1 results, not the full contribution.

- **The 28B token budget for multimodal pre-training may not be optimal for all checkpoints.** The paper fixes the amount of multimodal training at 28B tokens (20× model parameters, following Chinchilla scaling for text-only training). It is unclear whether this budget is appropriate for multimodal data or whether it might systematically disadvantage certain checkpoints (e.g., earlier checkpoints with higher initial LR may benefit more or less from a fixed 28B continuation). While not a fatal flaw, this is a methodological assumption worth interrogating.

### Minor

- **Only one model scale (1B) is evaluated for the core finding in Section 3.1.** The paper mentions 79M-scale experiments for early exploration, but the primary experiment on the timing of image introduction is only presented at 1B. The claim that "this fraction appears to be a function of scale" (line 23) for the ratio experiment does not extend to the timing experiment, leaving open the question of whether the 80% sweet spot generalizes to other model sizes.

- **The paper overstates the strength of the evidence in the conclusion.** The conclusion (line 153) says "our work ... demonstrates that a more integrated approach ... can yield superior downstream results." Given the LR schedule confound and the missing experimental body, "suggests" or "indicates" would be more appropriate than "demonstrates."

### Trivial

None.

## Nice-to-Haves

- A control experiment applying the same re-warmup schedule to the 80% checkpoint (or applying a continued-cosine schedule to the 100% checkpoint with a higher LR floor) would cleanly disentangle the timing effect from the schedule effect and substantially strengthen the primary claim.
- The paper could discuss whether the 28B token budget should be scaled proportionally to the number of visual tokens (which are information-dense) rather than total tokens.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"Missing experimental sections 3.2–3.5 — the paper is incomplete."* The abstract and conclusion clearly reference results from these sections (e.g., "our experiments reveal that 10% to 20% of tokens should be visual" at line 23, "mixing together instruction fine-tuning ... actively hurts the model" at line 25), confirming they exist in the original submission. Per the meta-review instructions, parser-stripped content is not an author error and should not be counted as a weakness.
- *"300 models trained but only one result shown."* This assumes Sections 3.2–3.5 are absent by author choice rather than parser artifact. Since those sections exist in the original submission, the criticism is invalid.
- *"Weakness about reproducibility/model availability."* No such criticism was present; noted for completeness.
- *Strength Finder strength about "ablation on instruction fine-tuning timing" and "optimal image-text token ratio":* These are claimed strengths of the paper but cannot be independently verified from the parsed text. They remain valid as claimed contributions assuming the missing sections exist in the original submission.

## Novel Insights

The most interesting observation emerging from the review is a methodological tension: the very property that makes the 80% checkpoint attractive (it is in the middle of a cosine schedule with a non-negligible LR) also makes it difficult to compare fairly against the 100% checkpoint (which has reached the LR floor). This highlights a broader challenge for research on "when to introduce modalities during pre-training" — training stage and learning rate schedule are intrinsically coupled, and disentangling them requires careful experimental design (e.g., comparing multiple schedule variants at the same checkpoint). The paper's transparency about this issue is commendable, but the field would benefit from a standardized protocol for such comparisons.

## Suggestions

1. **Add a control experiment for the LR schedule confound.** Either (a) take the 80% checkpoint and apply the same re-warmup schedule used for 100%, or (b) train the 100% checkpoint with a higher final LR that allows cosine continuation without re-warmup. This would isolate the timing variable and either confirm or qualify the headline result.

2. **Tone down the causal language in Sections 3.1 and 5.** Where the paper says "suggesting that continued training is preferable to re-training" (line 129), add a caveat that the comparison is confounded with the schedule. The conclusion should reflect the limitation rather than claiming a definitive demonstration.

3. **Restore the missing experimental sections in the final version.** The paper's contribution relies on the full experimental suite (ratios, instruction mixing, fine-tuning duration). Without them, the paper reads as a single-experiment study plus a research proposal.

4. **Include per-task results** alongside the stable score aggregate to allow readers to assess consistency of findings across individual benchmarks.

## Score and Decision

The paper addresses an important and timely question with a clean experimental framework. The main weakness—the LR schedule confound in the headline comparison—is real but mitigated by the paper's transparency and by the fact that the broader trend across 20%–80% (which uses a consistent schedule) already supports the value of intermediate checkpoints. The missing experimental sections are a parser artifact, not an author omission. The methodological approach and research question are sound, and the findings (even with the caveats) provide useful guidance for VLM practitioners.

**Score: 6.0** — Solid paper with a meaningful contribution; the primary claim needs a cleaner control experiment but the overall direction and findings are valuable.

**Decision: Accept**

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
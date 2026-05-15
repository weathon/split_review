Now I have all the information needed. Let me produce the consolidated review.

---

## Summary

This paper identifies a performance bottleneck in 3D MLLMs (PointLLM) where larger backbones (13B) underperform smaller ones (7B), tracing it to feature–text misalignment. It proposes **Streamlining Preference Alignment (SPA)**, a single-stage post-training method that applies 3D masking to generate negative inputs and uses ground-truth text as an anchor, eliminating the need for a reference model and separate text-pair generation. The paper also introduces **3DCQA**, a benchmark that converts captions into multiple-choice questions for more stable evaluation. Experiments on object-level (ModelNet40, Objaverse Caption) and scene-level (ScanQA) tasks show consistent improvements over the base PointLLM and over DPO/SimPO baselines.

## Strengths

1. **Empirically grounded motivation.** The paper systematically demonstrates (Figures 1, 3, Section 3.1) that larger LLM backbones underperform smaller ones in PointLLM, and that this is not resolved by improving the 3D encoder or extending fine-tuning alone. This is a concrete, non-obvious finding that challenges the scaling assumption in 3D MLLMs.

2. **Conceptually clean method with practical advantages.** SPA (Section 3.2) replaces the conventional two-stage preference optimization pipeline (generate text pairs → apply DPO/SimPO on pairs) with a single loss derived from contrasting clean vs. masked 3D inputs against a fixed ground-truth text. Table 4 shows SPA outperforms both DPO and SimPO (across two pair-generation modes) on classification and captioning, while requiring no extra text sampling or reference model — a genuine efficiency gain.

3. **Systematic ablation on augmentation design.** Table 2 investigates noise level (25–50% optimal) and noise type, showing that 3D masking (FPS+KNN clustering) yields better generalization than random dropping or Gaussian noise. This grounds SPA's core design choice in empirical behavior of point cloud features.

4. **Informative visualization.** Figure 6 provides a t-SNE comparison of decision boundaries under SFT, standard post-training, and SPA, illustrating how SPA combines supervised anchors with improved separation from negatives — a useful intuition for why the method works.

## Weaknesses

### Fatal
None.

### Major

1. **The central motivating claim — that SPA resolves the 13B < 7B bottleneck — is not directly tested.** The paper is framed around a surprising bottleneck (Figure 1: 13B PointLLM underperforms 7B PointLLM on classification and captioning) and claims SPA "successfully overcame the performance bottleneck" (abstract). However, the experiments never present a direct comparison of 7B vs. 13B **with and without SPA** on the exact metrics where the bottleneck was originally shown (ModelNet40 classification, Objaverse captioning). Table 3 evaluates 13B PointLLM + SPA on the 3DCQA benchmark, and Table 1 shows overall improvements, but neither isolates whether SPA closes or reverses the 13B < 7B gap on the bottleneck's own terms. The paper's core narrative is incomplete without this verification.

2. **The 3DCQA benchmark is introduced without validation of its reliability.** Section 3.3 proposes converting captions into multiple-choice questions using Llama-3.1, but:
   - No human agreement study or manual quality check is reported. The paper relies entirely on "let the language model select the question which can be reasonably inferred" as the sole quality filter.
   - No detailed statistics are provided: number of questions, difficulty distribution, or category coverage beyond a few nominal counts (e.g., "Color 89, Texture 55" in Table 3 headers).
   - While the paper notes that the 200 Objaverse objects used in evaluation are excluded from training (line 135), the benchmark questions are derived from the same caption source (Objaverse/ScanQA captions) that models saw during training. The risk of test-set contamination through shared caption distributions is not discussed.
   - An evaluation benchmark used to support the paper's main results should meet a higher standard of documented validation.

3. **The framing as "preference alignment" is mismatched with the actual mechanism; the InfoNCE equivalence is asserted without rigorous justification.** SPA's loss compares the same ground-truth text under a clean vs. a masked input. This is contrastive learning on input perturbations, not preference optimization over different outputs for the same input — the standard setting for DPO/SimPO. The paper derives its loss using the Bradley-Terry model (line 82) but applies it to *input preferences* (which input is preferred given a fixed output), a significant departure from standard usage that is not discussed. The claimed "fundamental equivalence" to InfoNCE (line 55) is stated but never proven: InfoNCE typically uses many negatives and a categorical cross-entropy, while SPA uses a single negative and a binary sigmoid. These are meaningfully different regimes. This is not a fatal flaw — the method stands on its own merits — but the paper overclaims its connection to the preference-alignment literature.

### Minor

4. **No confidence intervals or multi-seed results are reported.** Tables 1–4 show point estimates without variance. Given the modest performance gaps (often under 5 percentage points in Table 3), some improvements may not be statistically significant. This is a standard concern for single-run evaluations but limits confidence.

5. **The anchor-stability claim (Section 3.2, Figure 6) rests on thin evidence.** The paper argues that using ground-truth as an anchor provides more stable training than reference-model-generated outputs, but the only supporting evidence is a qualitative t-SNE plot of logit probabilities from two selected feature dimensions. No ablation removes the anchor (e.g., using reference-model outputs instead of ground truth) to quantify its contribution.

6. **The comparison with DPO/SimPO (Table 4) is reasonably designed but lacks computational cost reporting.** The paper implements DPO with the *same* masking strategy used by SPA in its "data augmentation" mode — this is actually a controlled comparison (same augmentation, different loss). However, the paper highlights efficiency as a key advantage but never reports training time, GPU hours, or number of generated samples needed for each method, which would make the efficiency claim concrete.

### Trivial
None.

## Nice-to-Haves

- A direct 7B vs. 13B comparison on ModelNet40 and Objaverse Caption with and without SPA, presented as a simple bar chart, would complete the paper's narrative loop.
- A human evaluation or agreement study on a sample of 3DCQA questions would significantly strengthen confidence in the benchmark.
- An ablation replacing the ground-truth anchor with reference-model outputs would isolate the anchor's contribution.
- Reporting results over 3 random seeds with means and standard deviations would improve statistical rigor.

## Removed Points

*These points were flagged in reviewer inputs but are removed as either factually incorrect, based on misreading, or parser artifacts. They are listed here for traceability but should not be weighted in assessment of the paper.*

- **Criticism that DPO/SimPO comparison is "confounded" because DPO uses SPA's masking strategy.** The paper implements DPO with *two* modes (text corruption and data augmentation). In the data augmentation mode, DPO uses masking to *generate text pairs*, then applies the DPO loss. SPA uses masking *directly in the loss*. Both use the same augmentation — this is a controlled comparison, not a confounded one. The asymmetry (DPO needs a Stage 1 to generate text; SPA doesn't) is the whole point.
- **Criticism about "single-view image scenarios" (line 144).** This is a parser artifact (the original likely said "single-view scenarios" or similar).
- **Phrase "less than 7B parameters" (line 142).** This contradicts the paper's own motivation (13B < 7B) and is likely a parser artifact from the PDF extraction.
- **Criticism that Figure 3 caption is garbled.** Parser artifacts; not author errors.
- **Generalized reproducibility concerns about missing training logs or hyperparameter details.** These are standard for a conference submission.
- **Request for adding more models/datasets beyond what is already adequate.** The model zoo is sufficient for the claims made.
- **Missing related work references.** Cannot be confirmed without external sources.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Complete the narrative loop.** Add a simple experiment: compare 7B PointLLM vs. 13B PointLLM vs. 13B PointLLM + SPA on the exact ModelNet40 and Objaverse Caption metrics from Figure 1. Even a single table or bar chart would validate the core claim.
2. **Validate the 3DCQA benchmark.** Report human agreement rates on at least 50–100 sampled questions, provide category-level statistics (question counts, difficulty distribution), and discuss potential contamination from shared caption sources.
3. **Tone down the "preference alignment" framing.** The method is best described as "contrastive post-training via input perturbation." The InfoNCE equivalence claim should be qualified: it is equivalent only in the single-negative, binary-sigmoid special case.
4. **Add an ablation removing the anchor** (e.g., use a reference model's output instead of ground truth) to quantify the anchor's contribution to stability.
5. **Report variance.** Add at least 2–3 random seeds and report means ± std for key results, particularly the 3DCQA scores where gaps are small.

## Score and Decision

**Originality:** 6/10 — The bottleneck observation is interesting and the input-side contrastive approach to post-training is reasonably novel, though the "preference alignment" frame is overstretched.

**Importance of research question:** 7/10 — Understanding why larger backbones fail in 3D MLLMs and developing efficient post-training are timely and relevant.

**Claims well-supported:** 5/10 — The central bottleneck-claim is not directly tested, and the 3DCQA benchmark lacks validation. The method's general effectiveness is supported, but the narrative linking motivation to results is incomplete.

**Soundness of experiments:** 5/10 — Reasonable breadth of tasks but missing the key control experiment, no statistical variance, and the main benchmark is unvalidated.

**Clarity of writing:** 6/10 — The method derivation is clear, but some framing is mismatched and several parser artifacts obscure the text.

**Value to community:** 6/10 — SPA is a useful methodological variant for 3D MLLM post-training. With strengthened validation it could be a solid contribution.

The paper has a genuine contribution (SPA as an efficient, input-contrastive post-training method for 3D MLLMs) and a well-documented empirical observation (the 13B < 7B bottleneck). However, the central narrative linking these two — that SPA resolves the bottleneck — is stated but never directly verified. The 3DCQA benchmark, used to report some of the main results, lacks the validation expected of a new evaluation framework. The method's actual mechanism (input-side contrastive learning) is more modest than the "preference alignment" framing suggests. These gaps are addressable but leave the paper in a borderline state.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Borderline Accept</orange>
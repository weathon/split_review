- Decision: Reject
- Avg Score: 5.00
- Scores: 8, 3, 6, 3
Now I have all the information I need. Let me construct the final consolidated review.

---

## Summary

This paper introduces the vVLM benchmark (300 questions, 900 QIA triplets) to evaluate whether Vision-Language Models rely on language priors instead of visual cues. The benchmark is formally grounded by three mathematical criteria and uses generative image models (DALL·E-3, Flux) to create images that deliberately contradict language priors. Human evaluation shows >98% accuracy on test answers, while GPT-4o achieves only 66.17% — a 32+ point gap. The paper also proposes Image DPO, a training method that corrupts images (blur, pixelation, semantic edit) while keeping question-answer pairs fixed, creating good-bad pairs for DPO training. Results show Image DPO improves performance on the vVLM benchmark and several general VQA benchmarks across LLaVA and Cambrian models.

## Strengths

1. **Principled benchmark design with formal criteria**: Equations 1–3 define three clear conditions requiring VLMs to use visual information. Human evaluation validates the design (98.33% on test answers vs. GPT-4o's 66.17%), confirming the benchmark is unambiguous for humans but exposes a substantial limitation in current VLMs.

2. **Clear empirical demonstration of the language-prior problem**: GPT-4o scores 66.17% on vVLM^F-Score vs. 98.33% for humans; GPT-4o (text-only) scores near 0% on test answers, confirming test answers cannot be inferred from text alone. Scores across a wide range of models (Table 2) consistently show a large gap, establishing the benchmark's diagnostic utility.

3. **Counterintuitive finding about distractor facts (Section 5)**: The analysis reveals that strong models (GPT-4o) actually benefit from misleading distractor facts, while weaker models (LLaVA-1.5-13B) are misled, and models with poor instruction-following (Cambrian-8B) suffer 2× instruction-failure rates. This insight is non-trivial and demonstrates the benchmark's ability to probe nuanced model behavior beyond simple accuracy ranking.

4. **Image quality ablations (Figure 5)**: Systematic degradation (blur, pixelation, resize) shows vVLM^F-Score drops rapidly with increasing severity while Prior score stays ~50%, cleanly demonstrating that model performance depends on image quality — supporting the claim that models use visual cues when available but default to language priors otherwise.

## Weaknesses

### Fatal

None.

### Major

1. **Image DPO's training signal coherence is unchecked.** The method creates "bad" pairs by corrupting the image (blur, pixelation, semantic editing) while keeping the answer unchanged, then trains the model to prefer the clean-image pair. The paper states these "should form a bad question-image-answer pair" (line 102) but never verifies that the answer remains valid or plausible for the corrupted image. For semantic edits (e.g., changing an object's color), the answer may become actively incorrect — so the DPO signal could teach the model to distrust images that contradict the answer rather than to attend more carefully to visual details. The paper provides no human validation, no automated check, and no analysis of answer consistency across corruption levels. This is not a missing control; it is a question about whether the training objective is coherent. (Verified: paper line 102–103 states the assumption without verification.)

2. **The claimed mechanism ("relies more on visual input") is asserted but not tested.** The paper argues Image DPO "encourages the model to rely more on visual input" (abstract, lines 14, 86, 234) but conducts no experiment that directly tests this. There is no text-only probe to check whether language bias is actually reduced, no attention analysis, no measurement of the gap between prior and test accuracy before vs. after Image DPO. The observed gains on downstream benchmarks are consistent with multiple alternative hypotheses (data augmentation, better instruction following, reduced overfitting) that have nothing to do with overcoming language priors. Without a probing experiment isolating the claimed mechanism, the explanation remains speculative. (Verified: no such analysis appears in the paper.)

### Minor

1. **Statistical reporting is absent.** No confidence intervals, no variance across runs, no significance tests are reported for any experimental result. On a 300-question benchmark where a shift of a few correct answers changes reported scores by ~0.3%, this is a meaningful gap in rigor. (Verified: paper reports only point estimates.)

2. **Human evaluation is underspecified.** The paper reports "over 98% accuracy" from a "human study" (line 127) but does not specify the number of annotators, their background, whether they were paid, the instructions provided, or inter-annotator agreement. These details matter for a benchmark that claims to show a stark human–VLM gap. (Verified: paper mentions only "human study" and the accuracy figure.)

3. **Benchmark scope limitations not discussed.** The benchmark uses only synthetic images from two generators (DALL·E-3, Flux), which may have systematic artifacts affecting model behavior differently from natural images. The modest size (300 questions, 900 QIAs) is reasonable for a targeted probe but should be acknowledged as a limitation. The paper does not discuss these constraints. (Verified: no limitations section or discussion of these issues.)

### Trivial

None.

## Nice-to-Haves

- **Ablation of corruption types**: Which corruption type (blur vs. pixelation vs. semantic edit) contributes most to Image DPO's effect? Are there cases where corruption renders the image genuinely unanswerable? An ablation would strengthen the method analysis.
- **Direct text-only probing**: After Image DPO training, evaluate the model on text-only queries to measure whether language-prior reliance has actually decreased — this would directly test the claimed mechanism.
- **Qualitative examples of Image DPO training pairs**: Showing a few examples of chosen/rejected pairs (clean vs. corrupted image with the same QA) would build intuition and allow readers to assess answer validity informally.

## Removed Points

*These points were flagged by reviewers but removed during consolidation with brief justification:*

- **"Evidence is weak — only 0.84 pp improvement over Text-DPO on vVLM^F-Score and regression on vVLM^P-Score"**: The specific numerical claims (41.67 vs. 40.83, 43.33 vs. 44.83) come from image tables (Tables 3–4) that cannot be independently verified from the paper text. The paper text states Image DPO "achieved the highest performance in vVLM^F-Score" and "second-best" on vVLM^P-Score — which is consistent with the paper's claims. Removed due to unverifiability of exact numbers.
- **"CHAIR results inconsistent with claimed direction"**: Same issue — numbers are in image tables, not text. Cannot verify.
- **"SEED-Bench regression (68.75 → 68.35)"**: Same issue.
- **"Reproducibility details insufficient"**: The paper provides a reasonable high-level description of the generation pipeline (prompts through GPT-4, human filtering cycles, specific image models used). The level of detail is standard for this type of work.
- **"Missing related work"**: Rule: do not mention missing related work as you cannot verify their existence.
- **Formatting/style nitpicks, typos, grammar issues**: Parser artifacts, not author errors.
- **"Could the model learn to distrust corrupted inputs instead of attending more?"**: This is re-stated more precisely in the retained Major weakness #1 (training signal coherence). Merged.

## Novel Insights

The reviews surface a key tension: the vVLM benchmark is a genuinely strong contribution, but the Image DPO method — which occupies a full section and is presented as a central contribution — has validation gaps that are not acknowledged. The strongest critique is not about performance magnitude but about whether the DPO training signal teaches what the authors claim it teaches. This is a *method-concept mismatch* issue: the concept ("rely more on visual input") is compelling, but the method's design (corrupting images while keeping answers fixed) is presented without evidence that the answers remain valid for corrupted images, and without any direct test of the claimed mechanism. The paper would be strengthened by either (a) adding these critical experiments or (b) reframing the method as a preliminary exploration rather than a validated technique.

## Suggestions

1. **Verify answer validity after corruption**: Conduct a human or automated check to confirm that the answer remains plausible for each corrupted image (or at minimum, report the fraction of pairs where it does). Report per-corruption-type statistics.
2. **Add a direct test of the mechanism**: After Image DPO, run a text-only evaluation (same questions without images) to check whether language-prior accuracy decreases. Compare the prior vs. test accuracy gap before and after training.
3. **Report confidence intervals or variance**: Even bootstrap estimates over the 300-question benchmark would significantly strengthen claims about the size of improvements.
4. **Acknowledge benchmark limitations explicitly**: Add a brief discussion of the synthetic-image-only nature and the modest size of the benchmark.

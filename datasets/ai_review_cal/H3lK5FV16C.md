- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3
Now I have a complete picture of the extracted paper. Let me write the consolidated review.

---

## Summary

This paper proposes Robust Environmental Design (RED), a novel defense against adversarial patch attacks on road sign classifiers. Instead of modifying the classifier (e.g., via adversarial training), RED modifies the road sign itself — learning patterns to be applied to sign backgrounds such that patch-based attacks become less effective without requiring any changes to the classifier or adversarial training. The paper motivates the approach well, draws a clear distinction from prior attack-aware and attack-agnostic defenses, and describes a thorough evaluation design spanning digital simulation and physical experiments across two datasets (GTSRB, LISA) and two attack types (Sticker-Attack, Patch-Attack).

## Strengths

1. **Novel problem framing — environment-centric rather than classifier-centric defense.** The paper shifts the burden of robustness from the model to the object itself. The introduction (lines 43-45) explicitly states that RED "achieve[s] robustness against patch attacks *without* requiring adversarial training" and that "the model $f$ is trained only on clean data." This is a genuinely different strategy from the vast majority of adversarial defense work, which targets the classifier.

2. **Well-motivated research question with clear positioning against prior work.** The introduction (lines 39-42) cleanly categorizes defenses into Attack-Aware (adversarial training) and Attack-Agnostic (randomized smoothing, image sanitization), then positions RED as distinct from both — an environmental modification approach. This framing is clear, accurate, and helps the reader understand the paper's contribution.

3. **Comprehensive evaluation design.** The experimental section describes tests in both digital settings (digital-RED-LISA, digital-RED-GTSRB) and physical settings (printed signs photographed under varying lighting, distance, and time of day), against two distinct patch-based attack paradigms (Sticker-Attack from Eykholt et al. 2018 and Patch-Attack from Brown et al. 2017) on two standard road sign datasets. The digital simulation applies color transformations learned from photographed patches and homography-based spatial transformations (lines 89-93), indicating methodological care in bridging the sim-to-real gap.

4. **Honest acknowledgment of scope limitations.** The Social Impact Statement (lines 111) notes that RED "requires the ability to edit objects... This may not be feasible for all objects (e.g., pedestrians, wild animals, plants, etc.)." This candid discussion of applicability boundaries strengthens the paper's credibility.

## Weaknesses

### Fatal

None. The core issue raised by the harsh critic — that the method section and results sections are missing from the extracted text — is a **parser/extraction artifact, not a flaw in the original paper**. The extracted text contains literal `\input{no_aware_attack}` (line 77), `\input{experimentResults}` (line 99), and `\input{physical_experiment}` (line 101), which are raw LaTeX include directives that should never appear in a properly rendered PDF extraction. Their presence indicates the text extraction pipeline failed to capture the content of those sections, which were present in the original PDF. Per the meta-instructions, formatting artifacts from PDF extraction are not paper flaws.

However, the practical consequence for this review is that the method and all quantitative results are unavailable for evaluation.

### Major

- **The method description and all experimental results are absent from the extracted text, making it impossible to evaluate the paper's core claims.** The paper claims "significantly reduces vulnerability to patch attacks, outperforming existing techniques" (abstract, line 10) and "high levels of robustness compared to baseline models" (introduction, line 48), but neither the learning algorithm (objective function, optimization procedure, pattern representation) nor any quantitative evidence (tables, figures, comparison numbers, ablation studies) is present in the extracted version. The experimental section (Section 3) describes only the setup and methodology — datasets, models, attack types, how digital and physical data were collected — but contains zero results. This is a parser artifact, not an author error, but it means the review cannot verify whether the claims are supported.

### Minor

None.

### Trivial

None.

## Nice-to-Haves

- Inclusion of the method algorithm description, objective function, and training procedure (clearly intended in the original submission given the `\input{no_aware_attack}` structure).
- Inclusion of quantitative results tables and comparisons (clearly intended given the `\input{experimentResults}` and `\input{physical_experiment}` structure).

## Removed Points

**These points are flagged to be removed; treat them with caution.**

1. **Harsh critic's claim: "The paper as submitted is missing its core method and all experimental results... This is a structural flaw."** — Removed because the missing content is a parser/extraction artifact, not an author omission. The `\input{}` commands appearing literally in the extracted text are evidence that the PDF extraction pipeline failed to capture sections that were present in the original submission. Per instructions: "formatting artifacts are parser issues, not paper problems."

2. **Harsh critic's claim: "The paper is not reviewable in its current form."** — This follows from point 1 and is removed for the same reason. The paper as originally submitted was a complete manuscript; the extracted text is an incomplete artifact of the extraction process.

3. **Harsh critic's claim: "Section-by-section notes... Method (missing)" and "Experiments... empty scaffold."** — Removed as these are the same criticism as point 1, restated.

4. **Strength Finder's strength: "Empirical outperformance over baselines across multiple attacks"** — This strength is based on the abstract's claim of outperforming existing techniques, but since no result data is available in the extracted text for verification, this strength cannot be confirmed. Partially demoted: the experimental *design* (breadth of attacks and datasets) is a genuine strength, but the claimed *outperformance* is unverifiable here.

5. **Strength Finder's strength: "Use of standard benchmarks and attack implementations"** — Valid and retained, with the caveat that the actual results aren't visible.

6. **Strength Finder's strength: "Explicit simulation of real-world deployment conditions"** — Valid and retained as it describes the experimental methodology which IS present in the text.

7. **Strength Finder's strength: "Recognition of feasibility constraints"** — Valid and retained.

## Novel Insights

None beyond the paper's own contributions. The paper's core insight — that one can achieve robustness against patch attacks by redesigning the physical object rather than hardening the classifier — is itself the novel observation that drives the work. The reviews do not surface additional cross-connections or perspectives that the paper itself does not already provide.

## Suggestions

- Ensure that the PDF extraction pipeline captures the method and results sections for the current review format. This paper clearly had those sections in the original submission, but their absence in the extracted text prevents meaningful evaluation of whether the claims are supported.

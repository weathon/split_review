Now I have enough calibration to write the final review.

## Summary
The paper presents GRAID, a framework that generates qualitative spatial-reasoning VQA pairs from 2D bounding-box detections, producing 8.5M VQA pairs across BDD100k, NuImages, and Waymo. The authors report a human-validated correctness of 91.16% on the GRAID-BDD (no-depth) variant versus 57.6% on the community OpenSpaces port of SpatialVLM, and show via fine-tuning that the data transfers across question types, datasets, and to external benchmarks (BLINK, A-OKVQA, NaturalBench, VSR, RealWorldQA).

## Strengths
- **Large, openly released dataset of qualitative spatial VQA pairs**: 8.5M pairs across three driving corpora with six variants (Table 2), targeting a kind of spatial supervision that prior pipelines do not provide cleanly.
- **Strong cross-dataset generalization in RQ1**: training Llama 3.2 11B on 10% of GRAID-BDD lifts held-out GRAID-BDD accuracy from 31% → 80.7% and unseen GRAID-NuImages from 38% → 67.1% (Section 5), giving credible evidence the model learns transferable spatial concepts rather than memorizing templates.
- **Held-out question-type generalization in RQ2**: training on only six question types yields ~+47.5 pp overall on held-out GRAID-BDD and ~+38.0 pp on GRAID-NuImages (Figure 3), including improvements on the Size & Aspect category never seen at training time — a non-trivial composability result.
- **Transfer to external benchmarks in RQ3**: substantial absolute deltas on BLINK (+15.94 pp overall, +41.13 pp Relative Depth, +30.77 pp Spatial Relations) and +32.5 pp on A-OKVQA for Llama 3.2 11B, with similar gains across Gemma 3 4B, Qwen2.5-VL 3B, and Qwen3-VL 8B, showing the improvement is not specific to one backbone.
- **SPARQ efficiency design**: lightweight predicates (e.g., `at_least_x_classes`, IoU=0) reject candidates cheaply — 0.02 ms predicate vs 28 ms realization for `LargestAppearance` (~1407× speedup), with predicate success implying realization 78.8% of the time, enabling generation at the 8.5M-pair scale.
- **Explicit human evaluation of competing pipelines**: rather than relying only on downstream metrics, the authors directly measure 250 OpenSpaces samples (57.6% correct) and 317 GRAID-BDD samples (91.16% correct, 4 annotators), with explanations of failure modes (ambiguous masks for SpatialRGPT, hallucinated quantitative answers for OpenSpaces).

## Weaknesses

### Fatal
None. The contribution is real and verifiable from the text.

### Major
- **The 91.16% vs 57.6% headline is not a like-for-like framework comparison.** OpenSpaces is being scored on metric distance estimation with a [50%, 200%] tolerance band, while GRAID is scored on qualitative binary questions (Figure 1; Section 4). The paper itself states this is precisely the motivation ("rather than asking how far an object is in terms of metric distance, it's easier to answer which object is closer"), but it then continues to frame the validity gap as evidence of GRAID's *framework* superiority in the abstract, intro, and conclusion. The honest claim is "qualitative questions over 2D boxes are easier to label correctly than metric questions over monocular depth, and they suffice to train good spatial reasoners" — the paper has the evidence to defend that, but not the broader framework-vs-framework headline. This is a reframing-of-claims issue, not a numerical error.
- **The RQ3 SFT comparison rests on a single baseline that the paper itself has called ~half-wrong.** Section 5 RQ3 compares fine-tuning on GRAID-BDD vs. OpenSpaces (the same 57.6%-valid community SpatialVLM port). Beating a baseline whose answers are known-noisy does not isolate whether GRAID's *framework* design is better — only that its outputs are cleaner. A second well-curated baseline (e.g., the original SpatialVLM dataset, SpatialRGPT's OpenSpatialDataset on a subset where masks are unambiguous, or even random-baseline-level no-finetune ablations re-reported in absolute terms) would substantially strengthen the conclusion. Without it, the framework-quality claim cannot be cleanly separated from the noise level of one baseline.
- **Algorithm 1 / prose inconsistency for the framework's worked example.** Section 3.2 motivates the `RightOf` realizer by saying pairs must "lie on similar planes" to avoid the case where "is an object truly to the right of another if they are also on different heights?" Algorithm 1 — the only formal specification — only checks `x_min^(1) > x_max^(2)` and `IoU(b1,b2)=0`; no plane / vertical-alignment check appears. Either the algorithm lacks the check the prose claims is essential (a question-quality issue), or the algorithm description is incomplete (a reproducibility issue). For the worked example used in both Sections 3.1 and 3.2, this matters and should be reconciled.

### Minor
- **The depth-variant datasets are not characterized by the headline validity number.** Table 1 lists "Avoids single-view 3D reconstruction" as a categorical feature of GRAID, but Section 4 introduces depth-question variants that do consume predicted depth (mitigated by `margin_ratio`). Per Table 2, with-depth variants are roughly half of the 8.5M pairs. The 91.16% figure was measured on GRAID-BDD *without* depth (n=317). The depth-variant validity should be reported separately, and Table 1 should be slightly qualified (e.g., the framework supports depth-free operation; depth is opt-in).
- **Statistical reporting is thin for the headline numbers.** The 91.16% (n=317, 4 annotators) and 57.6% (n=250) are reported without confidence intervals, inter-annotator agreement, or per-question-type breakdowns. Given how much rhetorical weight the abstract places on these figures, even simple Wilson intervals and per-template validity would be valuable.
- **The "cross-dataset" generalization in RQ1 is between three driving datasets with similar class taxonomies.** BDD ↔ NuImages ↔ Waymo are all on-road scenes with overlapping classes; the +29.1 pp transfer is meaningful but is a narrower claim than the prose ("entirely different cities, scenes, objects, and visual contexts") implies. The RQ3 external benchmarks (A-OKVQA, BLINK, etc.) carry most of the actual non-driving transfer evidence, and the prose around RQ1 should be calibrated to reflect that.
- **Several held-out question types in Figure 3 show no improvement at all.** "Count less than threshold," "Count greater than threshold," "Rank top-k largest," "Which object type appears more," and "Location by quadrants" appear unchanged before/after SFT. The paper acknowledges regression in `LessThanThresholdHowMany` and attributes it to overfitting, but the broader pattern of flat-improvement primitives is not engaged with and is actually the most informative signal in the figure about which spatial concepts the template-driven SFT fails to teach.
- **The "GRAID requires only object detection outputs" claim inherits all detector-quality risk that the validity study does not measure.** The human evaluation uses ground-truth boxes (Section 4 makes this explicit). The framework claim that "anyone can run GRAID on their own images with their own detector" implicitly relies on detector quality. An experiment running GRAID with an off-the-shelf detector and re-measuring validity would directly substantiate the framework claim — the paper's current evidence speaks only to ground-truth-box inputs.

### Trivial
- The OpenSpaces evaluation conclusion in Section 4 — "57.6% of answers in the dataset were incorrect" — is loosely generalized in the abstract ("a dataset produced by a current training data generation pipeline has a 57.6% human validation rate"). It should remain attributed to the community port specifically.

## Nice-to-Haves
- A like-for-like baseline: restrict the SpatialVLM evaluation to its qualitative-only questions (where they exist) or generate GRAID-style qualitative questions from SpatialRGPT's 3D ground truth and compare validity head-to-head. That would let the central quality argument stand on a sharper comparison.
- Report per-template validity for at least one dataset (especially across question categories) so the 91.16% can be interpreted by template type.
- A deeper analysis section on which primitives SFT failed to transfer (the flat or regressed bars in Figure 3) — this is among the most interesting empirical findings and is currently a footnote.
- One experiment with a noisy off-the-shelf detector instead of GT boxes, to support the framework-vs-dataset distinction.

## Removed Points
*These points were flagged for removal — treat them with caution.*
- *Harsh critic's "compounded errors in 3D reconstruction are asserted rather than measured" critique.* Removed because this is field-known and the paper's contribution does not hinge on quantifying it; nice-to-have at most.
- *Harsh critic's "Section 3.1 detector reliance is hand-wavy" critique.* Partially addressed: the paper deliberately uses GT boxes to evaluate framework quality in isolation (Section 4 explicitly: "we select to directly leverage these high-quality labels in GRAID's generation rather than train our own object detectors so that we can evaluate GRAID's effectiveness in isolation"). The framework-vs-detector concern is retained as a Minor weakness; the rest is scope-related.
- *Harsh critic's "RQ3 absolute scores hidden, only deltas shown" concern.* The harsh critic noted Tables 4–6 are referenced but not visible in the extracted text. Since these tables exist in the original submission, this is a parser artifact rather than an author error.
- *Strength-finder's "fine-tuning improves on external benchmarks beyond driving scenes"* — kept as a strength, but only because the paper actually reports cross-domain BLINK/A-OKVQA gains; if the only evidence were within-driving it would have been removed.

## Novel Insights
None beyond the paper's own contributions. The empirical observation that template-driven SFT on six qualitative primitives transfers to many unseen qualitative primitives (Figure 3) is interesting but is essentially the paper's RQ2 claim.

## Suggestions
- Reframe the abstract and conclusion around the **question-type** thesis ("qualitative bounding-box questions are easier to label correctly, and a clean dataset of them suffices to train better spatial reasoners") rather than a framework-vs-framework comparison the experiments do not establish.
- Add the plane / vertical-alignment check to Algorithm 1 or rewrite the Section 3.2 prose to match the algorithm and report how often 2D-only relations yield 3D-ambiguous results.
- Add at least one additional fine-tuning baseline in RQ3 beyond OpenSpaces.
- Report 91.16% and 57.6% with Wilson 95% CIs and inter-annotator agreement; break validity down by template.
- Run GRAID with an off-the-shelf detector on a held-out image set and report the validity delta vs. GT boxes — this directly substantiates the framework claim.
- Devote analysis space to the flat-improvement primitives in Figure 3.

---

## Axis-by-axis assessment
- **Originality**: Moderate. The "qualitative-from-2D-boxes" thesis is a sensible reframing of an existing problem space, and SPARQ's predicate/realize split is a tidy engineering contribution; neither is a deep technical novelty.
- **Importance of research question**: High. Spatial reasoning is a known VLM failure mode and the quality of synthetic VQA data is a real bottleneck.
- **Whether claims are well supported**: Mixed. RQ1/RQ2 are well supported; the headline 91.16% vs 57.6% framing overreaches given the qualitative-vs-metric asymmetry; RQ3 rests on a single weak baseline; the depth variants are not characterized by the headline number.
- **Soundness of experiments**: Reasonable but not adversarial. The human eval is small but informative; SFT setups are described enough to be plausible; the within-driving cross-dataset generalization claim is slightly oversold.
- **Clarity of writing**: Generally clear. The Algorithm 1 / Section 3.2 prose mismatch is the most significant clarity issue.
- **Value to the research community**: Genuinely positive — an 8.5M-pair, openly released, high-correctness qualitative spatial VQA corpus is useful, even if some of the framing should be reworked.

---

## Anchors retrieved and used

Round 1 (bracketing):
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/V73W8MXnNW.md` (avg 3.00, weak band) — narrower topic, weaker scope; GRAID clearly above.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/IlleFmPNb6.md` (avg 3.40, weak band) — RAG VQA, distant topic; GRAID clearly above.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ky2JYPKkml.md` (avg 3.00, weak band) — generic multi-modality, distant; GRAID clearly above.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/TCSaLeANpN.md` (avg 3.00, weak band) — synthetic 3D buildings, distant.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/vXG7d2VlHU.md` (avg 4.50, middle band, read) — **Sparkle**: extremely close in spirit (basic spatial primitives → composite generalization via SFT, rejected). GRAID is broader in scope (3 source datasets, 22 templates, 8.5M pairs, external benchmarks) and includes a substantial human-eval study Sparkle lacks; GRAID should sit above.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/uBhqll8pw1.md` (avg 4.00, middle band) — 3D scene VLM eval.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/84pDoCD4lH.md` (avg 7.40, strong band, read) — **COMFORT**: thorough multilingual frame-of-reference benchmark with rigorous experimental design; GRAID is less analytically deep and has framing problems.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/wFAyp2CUnq.md` (avg 4.00, middle band) — attention-based spatial reasoning.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Q6a9W6kzv5.md` (avg 8.00, strong band) — PhysBench, comprehensive benchmark.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/WyEdX2R4er.md` (avg 8.00, strong band) — distant topic.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/3i13Gev2hV.md` (avg 8.00, strong band) — distant topic.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/7gUrYE50Rb.md` (avg 8.00, strong band) — EQA dataset.

Round-1 bracket: roughly between 4.5 (Sparkle) and 6.5; GRAID is more thorough than Sparkle but is hurt by the headline-framing and single-RQ3-baseline issues, so unlikely to reach the 7+ band.

Round 2 (narrowing within 4.5–6.5):
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/G6DLQ40VVR.md` (avg 6.25, read) — **DivScene**: dataset + agent + benchmark, well-executed but reviewers flagged "tries to do too many things" and synthetic-only. GRAID is roughly comparable in ambition, slightly weaker in baseline comparison; should sit a bit below DivScene.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/lCqNxBGPp5.md` (avg 5.00) — visual reasoning vs language priors VQA dataset; comparable position.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/wLzhEQq2hR.md` (avg 6.00) — diagram understanding VLM eval.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/x07rHuChwF.md` (avg 5.00) — Euclid synthetic visual descriptions; comparable position.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ZPCBcR7Drg.md` (avg 5.00) — traffic-sign dataset.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/c2R7ajodcI.md` (avg 6.00, read) — **All-Seeing-1B**: billion-region VQA + model, accepted; thorough analysis though imperfect. GRAID is substantially narrower in scope but the comparison anchors the 6.0 line.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ubuGgIPVD0.md` (avg 5.00) — TSTTC driving dataset.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/DD11okKg13.md` (avg 6.00) — object-centric VQA representations.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/U17KoLrXE8.md` (avg 5.25) — captioning benchmark.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ITq4ZRUT4a.md` (avg 6.00) — Davidsonian scene graph.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/WK6K1FMEQ1.md` (avg 6.75) — SPACE spatial cognition benchmark.

After narrowing: GRAID sits above Sparkle (4.5) because of (a) much broader dataset coverage, (b) external-benchmark transfer evidence, and (c) explicit head-to-head human-eval study. It sits below DivScene (6.25) and the accepted All-Seeing (6.0) because RQ3 has only one baseline and the headline framing is overclaimed. It is closest to the Euclid/vVLM 5.0 anchors — substantive empirical work with a real claim-overreach issue — but a touch above them due to the size and quality of the released dataset and the strength of RQ1/RQ2. Landing at 5.0 reflects "solid dataset contribution dragged down by a single-baseline RQ3 and a headline that the experiments do not establish in its current framing."

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
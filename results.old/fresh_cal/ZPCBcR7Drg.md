Now I have everything I need. Let me compile the final review.

---

## Summary

This paper introduces MapDR, a dataset for integrating traffic sign regulations into vectorized HD maps, comprising over 10,000 video clips, 400,000 images, and 18,000 annotated lane-level rules collected from three Chinese cities. It defines two sub-tasks — Rule Extraction from Traffic Signs (decoding signs into structured `{key:value}` rules) and Rule-Lane Correspondence Reasoning (associating rules with lane centerlines as a bipartite graph) — along with corresponding metrics. A multimodal baseline (Vision-Language Encoder + Map Element Encoder) is provided.

## Strengths

- **First dataset providing both formatted driving rules and rule-lane correspondence.** Table 1 systematically compares MapDR against six prior datasets (nuScenes, Argoverse2, CTSU, OpenLane, RS10K, OpenLaneV2) and shows MapDR is the only one that checks both "Fmt." (structured rule annotations) and "Corr." (rule-to-lane mapping). This concretely fills a gap that the paper identifies and motivates — prior datasets either lack structured rules (OpenLaneV2 uses single-label classification) or lack lane association (CTSU).

- **Well-defined sub-tasks with explicit evaluation metrics.** Section 3 formalizes both sub-tasks mathematically (rule extraction as multi-property prediction, correspondence as bipartite graph matching). Section 4.2 defines precision, recall, and AP for rule extraction (Eq. 1), correspondence reasoning (Eq. 2), and the combined task (Eq. 3–5). This provides a clean framework that prior benchmarks, which the paper discusses (CTSU, VTKGG, OpenLaneV2), do not offer.

- **Ablation study quantifying component contributions.** Table 2 isolates the effect of attention mechanisms, layout embedding, instance embedding, and type embedding. For example, intra & inter-instance attention in VLE improves Rule Extraction recall from 57.56% to 71.75%, and type embedding in MEE raises Correspondence Reasoning precision from 69.68% to 78.05%. These controlled experiments provide concrete evidence for design decisions.

## Weaknesses

### Fatal
None.

### Major

1. **No dataset release statement.** For a paper whose primary contribution is a dataset and benchmark, there is no commitment to public release — no URL, no license, no distribution mechanism. The paper states only that "all data newly collected." Without release, the benchmark cannot be used by the community, and the contribution's impact is severely limited. This must be explicitly addressed (e.g., "dataset will be released under CC-BY-NC license at [URL]").

2. **No quantitative annotation quality assessment.** The paper states annotations are "carefully validated" but provides no inter-annotator agreement (e.g., Fleiss' kappa for rule attributes, agreement on correspondence edges), no error analysis, and no per-attribute accuracy on a held-out expert review set. For a benchmark that involves subjective interpretation of traffic sign rules and assignment to lanes, the absence of any reproducibility or consistency evidence is a significant gap — readers cannot assess whether the annotations are reliable enough to serve as a ground truth standard.

3. **Insufficient evaluation baselines.** The only quantitative comparison is against an unmodified ALBEF+BERT baseline that fails to converge on the correspondence reasoning sub-task, producing no meaningful comparison. No existing models are adapted and evaluated on either sub-task (e.g., ALBEF, LLaVA, or even OpenLaneV2's approach). No simple heuristic (e.g., spatial proximity matching for correspondence) is tested. No human performance is established. For a benchmark paper, the community needs reference points — even low scores from adapted prior methods or simple heuristics provide context. Without them, the reported 44.60% overall AP cannot be interpreted as good, poor, or expected, and the claim that the method is a "strong baseline" (abstract, introduction) is unsubstantiated.

### Minor

1. **Qualitative MLLM evaluation is insufficient.** The paper reports that MLLMs were "qualitatively evaluated" on a subset and concludes they "understand traffic signs to a certain extent but lack spatial association capability" — with no sample size, no metrics, no error taxonomy, and no systematic protocol. This one-sentence evaluation does not support the claims being made and should either be removed or replaced with a proper quantitative study.

2. **No validation split used.** The dataset is split 9:1 train/test, with no validation set. Ablation studies and hyperparameter tuning (50 epochs for VLE, 120 for MEE) are conducted without a held-out validation set, which risks overfitting the test set. A standard train/val/test split (e.g., 8:1:1) should be used; the test set should be reserved for final evaluation only.

3. **Clustering component is not evaluated.** The rule extraction pipeline (Section 6.2) includes a clustering step that groups symbols and texts using [STC] token similarity under contrastive loss. However, clustering accuracy is never measured or ablated — errors in grouping would propagate to rule extraction, but this sensitivity is not analyzed.

4. **Limitations section is incomplete.** The paper's limitation paragraph mentions only dynamic elements (traffic lights). Other important scope constraints are not discussed: the dataset covers only Chinese traffic signs; each clip contains exactly one traffic sign; no temporal reasoning across frames is performed; the vectorized map is generated algorithmically (similar to MapTRv2) but the quality/noise level of these vectors is not assessed, even though the correspondence annotations inherit any map-vector errors.

5. **"Strong baseline" claim is unsupported.** The method is described as a "strong baseline" in both the abstract and introduction, yet achieves only 44.60% overall AP with no comparison to any alternative approach or heuristic. The term "strong" is self-serving without external reference points.

### Trivial
- The assumption that centerlines represent lanes (Section 3) is not discussed for edge cases (e.g., lanes without explicit centerlines, complex intersections). The paper states "generally vehicles follow the center of lanes," which is reasonable, but acknowledging edge cases would improve rigor.
- The choice of the 8 predefined rule properties is stated without justification — a brief rationale or reference to traffic sign standards would help.

## Nice-to-Haves
- **Human performance study** on a sample of the test set would provide an upper bound and contextualize the 44.60% AP.
- **Partial-credit metrics** (e.g., per-attribute accuracy for rules) alongside the strict exact-match metric would provide more fine-grained signal for rule extraction.
- **Simple heuristic baselines** (e.g., nearest-centerline by spatial proximity for correspondence) would provide a non-trivial lower bound and help demonstrate task difficulty.
- **Error analysis** (confusion matrices for rule attributes, distance-based breakdown of correspondence errors) would help the community understand where the task is hard.

## Removed Points
*These points were raised by at least one reviewer but are removed after verification for the reasons stated below:*

- **"Paper does not discuss why existing MLLM methods cannot be applied."** — Removed because Section 2.2 *does* address this: "MLLM-based benchmarks... prioritize end-to-end motion planning over precise rule extraction from traffic sign, lacking evaluation for rule reasoning." The paper provides a reasoned explanation for why direct application is not straightforward.
- **"Related work section lacks discussion of LingoQA, nuScenes-QA."** — Removed; these are cited in Section 2.2 as part of the MLLM-based benchmarks that the paper discusses.
- **"8 rule properties not justified / not discussed whether they are complete."** — Demoted from a standalone weakness to a trivial note. The paper presents the properties as part of the annotation design; a brief justification would improve clarity but this is not a substantive flaw.
- **"Long-tail distribution raises questions about dataset balance."** — Removed; the paper acknowledges this as a natural real-world distribution, which is standard for realistic benchmarks.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions

1. **Commit to dataset release** in the paper, specifying the license and distribution mechanism. This is the single most important change.
2. **Add inter-annotator agreement statistics** for both sub-tasks on a held-out annotation set. Establish a baseline for expected annotation consistency.
3. **Evaluate at least one existing model** (e.g., LLaVA or a standard VLM adapted via prompting) on both sub-tasks, even if scores are low. Add a simple spatial heuristic for the correspondence sub-task. Report human performance on a sample.
4. **Introduce a validation split** (e.g., 8:1:1) and report ablations using it. Reserve the test set for final evaluation only.
5. **Either remove the qualitative MLLM evaluation** or replace it with a proper quantitative study (sample size, metrics, error categories).
6. **Add an error analysis section** (confusion matrices, distance-vs-accuracy plots for correspondence) to surface where the task is difficult.
7. **Reduce method description detail** (move architecture figures to appendix) and use the freed space for dataset quality analysis and baseline comparisons, consistent with the paper being a dataset/benchmark contribution rather than a methods paper.

## Score and Decision

The paper addresses a genuinely underexplored and well-motivated problem. The dataset fills a clear gap (Table 1), and the task formulation is clean. However, three major weaknesses — no release commitment, no annotation quality metrics, and insufficient baselines to make the benchmark meaningful — significantly limit the paper's impact and verifiability in its current form. These are structural omissions for a dataset/benchmark paper, not minor presentation issues. The method and ablation studies are solid, but the experimental validation is too weak to establish the benchmark as a useful community resource.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
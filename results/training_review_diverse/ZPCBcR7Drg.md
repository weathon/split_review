Now I have all the information I need. Let me produce the consolidated review.

## Summary

MapDR introduces a new dataset and task for integrating traffic sign regulations into vectorized HD maps. The dataset contains over 10,000 video clips (400,000+ images) from three Chinese cities with 18,000+ lane-level rules annotated as structured key-value pairs with explicit rule-to-lane correspondence. The paper defines two sub-tasks—Rule Extraction from Traffic Signs and Rule-Lane Correspondence Reasoning—with formal metrics, and provides a multimodal baseline (VLE+MEE) that demonstrates task feasibility.

## Strengths

- **First dataset explicitly pairing formatted driving rules with lane-level correspondences.** Table 1 shows MapDR is the only existing dataset that jointly provides formatted rules (Fmt.) and rule–lane correspondence (Corr.) alongside both sign and lane annotations, whereas prior datasets (CTSU, OpenLaneV2, VTKGG) cover at most two of these dimensions. This fills a genuine gap between sign recognition datasets and lane perception datasets.

- **Clear, mathematically precise task definitions with reusable metrics.** Sections 3.1 and 3.2 define both sub-tasks formally: rule extraction as $R = \mathcal{M}(X)$ with optional OCR input, and correspondence reasoning as a bipartite graph $G = (R \cup L, E)$ between rules and centerlines. Section 4.2 provides precision/recall for each sub-task plus an overall AP metric following standard benchmark design. This level of formalization is missing from prior related datasets (CTSU, OpenLaneV2).

- **Systematic ablation study validating architectural choices.** Table 3 decomposes contributions cleanly: intra/inter-instance attention improves rule extraction recall from 57.56% to 71.75% (VLE), and type embeddings boost correspondence precision from 69.68% to 78.05% and recall from 72.76% to 82.16% (MEE). The ablations confirm that MEE without attention mechanisms fails to converge entirely (marked $*$), which is a non-trivial finding that justifies the proposed design.

- **Diverse, real-world data collection with practical metadata.** The dataset spans three major Chinese cities across different times and weather conditions (Section 4.1), provides camera intrinsics, 3D sign positions, ENU-transformed coordinates, and vectorized local maps. Privacy processing (obscured faces/license plates) and the explicit $100\text{m} \times 100\text{m}$ clip framing around traffic signs add practical value for downstream use.

## Weaknesses

### Fatal

None.

### Major

- **Annotation quality is unsubstantiated by any quantitative metric.** The paper states "All annotations are carefully validated" (line 38) but reports no inter-annotator agreement rate, no validation protocol, no error statistics, and no information about how many annotators per sample or how disagreements were resolved. For a dataset that is the paper's central contribution, this is an evidential gap. Without it, the 74.54% rule recall score cannot be separated from annotation noise—a 25% error rate could reflect ambiguity in the annotations rather than task difficulty. This must be addressed before the dataset can be confidently adopted by the community.

### Minor

- **Only one working baseline is presented, limiting benchmark characterization.** The paper evaluates its VLE+MEE method alongside a trivial ALBEF/BERT adaptation that fails to converge on the correspondence sub-task. For a paper that presents itself as a *benchmark*, this leaves the difficulty, discriminative power, and saturation point of the benchmark uncharacterized. This is a common limitation for first-of-its-kind tasks (no pre-existing methods to compare against), and does not threaten the core dataset contribution. However, adding even one simple non-learning baseline (e.g., OCR + template matching + lane proximity heuristics) would substantially strengthen the paper's benchmark claim.

- **OCR source and quality are unspecified.** The method uses OCR results as input (lines 106, 193, 217) but never states which OCR engine was used, whether the dataset provides ground-truth text, or what the OCR accuracy is. This is a reproducibility gap for the baseline—other researchers cannot replicate the method's inputs.

- **The 8 predefined rule properties are only shown in the demo figure, not listed in text.** Line 145 mentions "8 predefined properties" but does not enumerate them. A table listing all properties and their possible values would remove ambiguity and improve the paper as a reference.

- **Qualitative MLLM evaluation (Section 5.3) is too vague to be informative.** The paper reports that MLLMs "understand traffic signs to a certain extent but lack spatial association capability" without any quantitative results, sample sizes, or systematic evaluation protocol. Either remove this or replace it with actual numbers on a held-out subset.

- **No validation split is specified.** The paper reports training/testing at a 9:1 ratio (line 223) but does not mention a validation split. It should clarify how hyperparameters were tuned (early stopping? held-out validation?).

- **Map accuracy is not evaluated.** The vectorized maps are generated "using our algorithm similar to MapTRv2" (line 137), but no measurement of map quality (e.g., lane detection recall, centerline accuracy) is reported. Since the correspondence task depends on map quality, this context would be helpful.

- **No discussion of why the baseline failed to converge.** The paper notes the baseline "failed to converge" during correspondence reasoning but offers no speculation about the cause (e.g., insufficient multimodal interaction, optimization difficulty). Even a brief explanation would aid future method design.

### Trivial

- The paper states the baseline failed to converge "resulting in no statistics evaluation" but could more precisely say "no meaningful statistics could be computed" to avoid confusion about whether metrics were zero or undefined.

## Nice-to-Haves

- Consider reporting a partial-credit metric for rule extraction (e.g., average per-property accuracy) alongside the strict exact-match metric, to provide finer-grained signal.
- An error analysis characterizing whether failures arise primarily from rule extraction (recall 74.54%) or correspondence reasoning (recall 82.16%) would guide future work.
- A per-property agreement analysis for the annotation process would be a useful addition even if full inter-annotator statistics are resource-intensive to collect on the entire dataset.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Strength: "Qualitative MLLM evaluation identifies remaining challenge."** This conflicts with the verified weakness that the evaluation is too vague to be meaningful. Moved here because the weakness is verified and the strength is not backed by quantitative evidence.
- **Criticism: "The benchmark is demonstrated with only one method, severely undercutting its utility" — framed as a structural/fatal flaw.** This overstates the severity for a first-of-its-kind task. Having a single working baseline is standard practice for newly introduced tasks at top venues. The point is retained as a Minor weakness (above) rather than Fatal/Major because it does not invalidate the core dataset contribution.
- **Criticism: "At least two or three distinct baselines are necessary to establish the benchmark's validity."** Demanding 2–3 additional baselines for a task that did not previously exist is outside standard expectations for this paper class. One additional simple baseline (non-learning) would be sufficient.
- **Criticism about missing related works.** Excluded per instructions — no external sources to verify.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a tension between the paper's "benchmark" framing and the single-baseline evaluation, but do not reveal any insight about the data or task that the authors missed.

## Suggestions

1. **Foremost:** Report inter-annotator agreement statistics (even on a subset) for the annotations. A kappa score or per-property agreement rate would address the most serious weakness.
2. **Add one simple non-learning baseline** (e.g., OCR → rule template matching → lane proximity heuristic) to demonstrate that the benchmark is nontrivial even for reasonable baselines.
3. **Specify the OCR engine and whether ground-truth text is provided** in the dataset release.
4. **Enumerate the 8 rule properties** in a table in the main text.
5. **Either remove the MLLM qualitative evaluation or replace it with quantitative results** on a defined subset.
6. **Clarify the validation strategy** (or confirm that hyperparameters were tuned on the test set, noting the limitation).

## Score and Decision

The paper introduces a well-motivated dataset for an under-explored problem, with clear task definitions, formal metrics, and an informative ablation study. Its central gap—unvalidated annotation quality—is the main barrier to community adoption. This is addressable in revision. The single-baseline limitation is minor for a first-of-its-kind task and does not undermine the core contribution.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
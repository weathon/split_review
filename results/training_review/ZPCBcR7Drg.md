Here is the consolidated review:

---

## Summary

MapDR introduces a dataset and benchmark for the underexplored task of integrating lane-level driving rules from traffic signs into vectorized HD maps. It provides over 10,000 video clips (400K+ images) from Chinese urban scenes, with 18,000+ driving rules annotated in structured {key:value} form and explicitly linked to lane centerlines. Two sub-tasks are formally defined — Rule Extraction from Traffic Signs and Rule-Lane Correspondence Reasoning — along with associated metrics. A baseline method (VLE+MEE) combining vision-language encoding with map-element encoding is also presented.

## Strengths

- **First dataset to jointly provide formatted rule annotations and lane-level correspondence.** Table 1 shows MapDR is the only existing dataset with both "Fmt." and "Corr." checked, while prior datasets (CTSU, OpenLaneV2, VTKGG) each lack at least one of these components. This directly fills the gap identified in the introduction and constitutes the paper's primary contribution.

- **Clean formalization of two novel sub-tasks.** Section 3 defines Rule Extraction and Rule-Lane Correspondence Reasoning as precise mathematical problems (bipartite graph formulation), and Section 4.2 provides unambiguous metrics (precision/recall for each sub-task and overall AP). This establishes a reproducible evaluation protocol for future work.

- **Ablation studies validate the necessity of the proposed architectural components.** Tables 2a/2b show that without intra/inter-instance attention, MEE fails to converge for correspondence reasoning, and removing type embedding drops recall from 82.16% to 72.76%. These controlled experiments demonstrate that the architectural choices are not gratuitous.

## Weaknesses

### Fatal
None.

### Major

- **The "strong baseline" claim is unsupported by the evaluation.** The baseline against which VLE+MEE is compared is a stripped-down version of the same architecture (minimal modifications to ALBEF/BERT) that fails to converge for the correspondence sub-task. No comparisons are made to simpler interpretable alternatives — e.g., rule extraction via template-based OCR parsing, rule–lane association based on spatial proximity between sign polygons and centerlines, or a zero-shot prompted VLM. Without such comparisons, the statement that VLE+MEE provides a "strong baseline" (Abstract, §1, §6) is overclaimed, and the overall AP of 44.60% lacks context for judging tractability. This is the paper's most significant weakness.

- **No quantitative evaluation of MLLMs, only qualitative remarks.** The paper invokes MLLM limitations to justify the structured approach (§5.3), stating that MLLMs "lack spatial association capability." However, only qualitative observations are reported — no precision/recall/AP numbers on any MapDR subset. Given that VLM-based methods (including zero-shot approaches) are among the most natural alternatives for this task, the absence of quantitative comparison is a significant omission that weakens the motivation for the proposed structured pipeline.

### Minor

- **Source of OCR input in experiments is ambiguous.** The rule extraction pipeline (§3.1) treats OCR as optional input. In §5, the VLE encodes "OCR results" but the paper never clarifies whether these come from ground-truth polygon projections (described in §4.1) or from an automatic OCR system. If ground-truth polygons are used, results are not indicative of real-world performance; if automatic OCR, the impact of OCR errors is unquantified. This ambiguity makes it difficult to interpret the Rule Extraction metrics.

- **Limited annotation validation details.** The paper states that "all annotations are carefully validated" (§1) but provides no information on the annotation pipeline, number of annotators, inter-annotator agreement, or handling of ambiguous cases. For dataset contributions, these details are important for establishing ground-truth reliability.

- **Single train/test split with no error bars or multiple runs.** Results are based on one 9:1 split with no reported variance. While single-run evaluation is common in this sub-field, for a benchmark paper reporting a baseline, some indication of stability would strengthen confidence.

### Trivial
None.

## Nice-to-Haves

- A heuristic baseline (e.g., spatial proximity-based rule-lane association) would help contextualize whether the learned correspondence (78.05% precision) is meaningfully better than a simple geometric rule.
- Clarifying whether the 8 predefined rule properties are listed in the appendix (which the parser strips) — if not, they should be stated in the main paper.
- An error breakdown (what fraction of failures come from rule extraction vs. correspondence, and whether errors concentrate on certain rule types or scene layouts) would aid future research.

## Removed Points

These points are flagged to be removed, treat them with caution:

- *Strength Finder's claim about "Qualitative evaluation of MLLMs highlights benchmark's difficulty"* — Moved here because it conflicts with the verified weakness that no quantitative MLLM evaluation is provided. A purely qualitative claim does not constitute robust evidence.
- *Harsh Critic's concern about OpenLaneV2 adaptation* — The critic suggests testing whether OpenLaneV2's "single-label classification" limitation is severe by evaluating on MapDR. This would require re-annotating OpenLaneV2 data, which is outside the paper's stated scope.
- *Criticism about the 8 predefined properties not being listed* — The parser strips appendix sections where these are likely enumerated; this is a parser artifact, not an author omission.
- *Concern about centerlines discarding lane width/boundary information* — The paper explicitly states the choice is analogous to prior work (OpenLaneV2) and is a standard simplification, not an oversight.
- *Nitpick about "first time" claim regarding prior art* — The paper acknowledges OpenLaneV2 and VTKGG in §2.2 and Table 1 correctly shows their limitations; the claim is properly scoped.

## Novel Insights

None beyond the paper's own contributions. The reviews primarily surface standard concerns (baseline strength, evaluation breadth, experimental clarity) rather than uncovering novel meta-insights about the problem or methodology.

## Suggestions

1. **Add at least one non-neural baseline.** A simple pipeline using rule extraction via OCR + template matching and spatial-proximity-based rule-lane association would ground the difficulty of the task and make the "baseline" claim meaningful.
2. **Report quantitative MLLM results on a held-out test subset.** Provide precision/recall for at least one modern VLM (e.g., GPT-4o, LLaVA-NeXT) to substantiate the claim that MLLMs lack spatial association capability, and to motivate the structured approach.
3. **Clarify the OCR data source.** State explicitly whether the OCR text fed to VLE in the experiments is from ground-truth polygon text or from automatic recognition, and ablate the impact of OCR errors if applicable.
4. **Expand annotation documentation.** At minimum, report the number of annotators and per-property inter-annotator agreement to establish dataset quality.

## Score and Decision

The paper addresses a genuine and previously overlooked problem, and the MapDR dataset with its structured annotations and formalized metrics is a solid contribution. However, the experimental evaluation is significantly underdeveloped: the baseline claim is unsupported by meaningful comparisons, and the dismissal of MLLMs relies on qualitative observations alone. These evidential gaps prevent the paper from demonstrating that the task is tractable with current methods. The dataset alone does not outweigh the insufficient validation. A substantially strengthened version would address the major weaknesses above.

**Originality:** 7/10 — The task formulation and dataset are novel.  
**Importance of Question:** 8/10 — Integrating traffic sign rules into HD maps is practically important and underexplored.  
**Claims Supported:** 4/10 — The dataset claim is supported; the "strong baseline" claim is not.  
**Soundness of Experiments:** 5/10 — Ablations are informative, but the lack of baselines and quantitative MLLM comparison undermines soundness.  
**Clarity of Writing:** 7/10 — Generally clear, though the OCR ambiguity is a notable omission.  
**Value to Community:** 7/10 — The dataset has potential value if released; the baseline as presented is less valuable.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
Now I have a thorough understanding of the paper and can verify the reviewer claims directly against the text. Let me write the consolidated review.

---

## Summary

This paper proposes Open-vocabulary Multimodal Emotion Recognition (OV-MER), a paradigm shift from fixed-label emotion recognition to allowing prediction of arbitrary numbers and categories of emotions. The authors construct the OV-MERD dataset (248 emotion categories from MER2023 samples) via a human-LLM collaboration strategy, define set-based evaluation metrics with GPT-based and Emotion-Wheel-based grouping to handle semantic synonymy, and benchmark 12 MLLMs. The core finding is that current MLLMs achieve at most ~55 Fₛ, far below the CLUE-Multi oracle (80 Fₛ), highlighting the difficulty of the task.

## Strengths

- **Human-LLM collaboration demonstrably enriches annotation over human-only baselines.** Figure 20 shows that the human-LLM strategy produces longer descriptions (covering minor cues humans miss), more labels per sample, and a broader label vocabulary. This is a clear methodological contribution to dataset construction for nuanced emotion tasks.

- **Formalizes a new task with concrete infrastructural components.** The paper defines OV-MER as a distinct paradigm (contrasted with one-hot and multi-label MER in Figure 1), provides the OV-MERD dataset with 248 categories (vastly exceeding the 1–10 in prior datasets, Table 20), set-based metrics (Fₛ, Precₛ, Recₛ), and a systematic benchmark. This groundwork enables future research even if individual design choices are debated.

- **Comprehensive benchmarking with diagnostic ablations.** 12 MLLMs are evaluated under both English and Chinese branches (Table 1), with multimodal combination experiments (Table 2) and ablations comparing three CLUE-MLLM generation strategies (S0/S1/S2, Figure 6). The ablation showing S2 (two-step) outperforms S1 (direct input) provides actionable insight about task decomposition for MLLMs.

- **Useful comparison of GPT-based vs. EW-based grouping metrics.** Table 4 shows high Pearson correlation (up to 0.942) between GPT and EW-based metrics, establishing that the cheaper, reproducible EW-based method can substitute for API-dependent GPT grouping. This is a practical contribution to metric design for open-vocabulary settings.

## Weaknesses

### Fatal
None. The paper makes genuine contributions even though methodological concerns exist. The core claims — that OV-MER is a meaningful new task and that current MLLMs struggle at it — are not invalidated.

### Major

1. **Circularity between ground-truth construction and the CLUE-Multi oracle baseline inflates the reported upper bound.** The ground-truth labels are derived by feeding human-checked clues into GPT-3.5 to generate CLUE-Multi descriptions, then extracting labels (also via GPT-3.5) from both English and Chinese versions, merging them, and conducting manual checks (lines 86–98). The CLUE-Multi baseline (Table 1, 80.05 Fₛ) uses the *identical pipeline* — same human-checked clues, same GPT-3.5 merging, same GPT-3.5 label extraction — minus the cross-language merging and final manual checks. The high score therefore largely reflects GPT-3.5's self-consistency between monolingual and cross-lingual+human-verified outputs, not genuine emotion recognition ability. The paper acknowledges that "the OV labels extracted from the monolingual CLUE-Multi differ from the ground truth" (line 228), but does not discuss how this confounds the interpretation of CLUE-Multi as an upper bound. The MLLM comparisons among themselves remain valid, but the gap between MLLMs (~55) and CLUE-Multi (80) is misleading as a measure of how far MLLMs are from human-level OV-MER.

2. **The evaluation metric collapses the open vocabulary into coarse groups, partly undermining the paper's central motivation.** The paper motivates OV-MER by arguing that basic emotion categories (6–7) are too coarse and that nuanced labels matter (Figure 1). Yet the metric (Eq. 4) operates on *group IDs* after applying a grouping function G(·) that clusters semantically similar labels. GPT-based grouping treats synonyms as identical; EW-based grouping (M3-L1/L2) maps 248 labels into at most ~20 coarse buckets (the inner levels of emotion wheels). The high correlation (PCC 0.942) between GPT and EW metrics in Table 4 suggests both methods produce similar coarse granularity. This means the metric cannot distinguish between a model that correctly predicts "frustrated" vs. "annoyed" (a fine-grained distinction the paper claims is important) and one that gets the coarse group right but the nuance wrong. The paper never evaluates fine-grained label-level accuracy — only group-level set overlap. This is a genuine tension between the stated goal and the measurement instrument.

### Minor

1. **No inter-annotator agreement reported for ground-truth labels.** The paper describes two rounds of manual checks on *clues* (lines 82–85) and manual checks on merged *labels* (line 98), but provides no quantification of agreement (e.g., Cohen's Kappa, percentage overlap) among annotators for either stage. Without this, the reader cannot assess the reliability of the ground truth or whether the "manual checks" mainly catch obvious duplicates vs. independently verify label appropriateness. Given that 248 emotion categories are subtle and the label extraction pipeline uses GPT-3.5 (known for prompt sensitivity), the absence of inter-annotator statistics is a meaningful gap in dataset documentation.

2. **Underspecified dataset construction details.** Several important parameters are omitted: (a) the number of samples selected from MER2023 and the precise selection strategy ("evenly select samples," line 131, is vague); (b) the number of annotators per round and the specific nature of the final "manual checks" on merged labels (are annotators shown the video and asked to verify each label, or just reviewing a list?); (c) the threshold used in the label filtering step (the 0.82 similarity score in line 98 is presented as an observation, not a decision threshold, but the merging criteria are unclear). These details matter for reproducibility and quality assessment.

3. **The CLUE-MLLM pipeline tests description-generation ability more than direct emotion recognition.** The CLUE-MLLM baselines use the MLLM to generate an emotion-related description, then GPT-3.5 to extract labels from that description. This design makes it difficult to disentangle whether a low score reflects the MLLM's failure to recognize emotions or GPT-3.5's failure to correctly extract labels from the description. The paper's own ablation (Figure 6, S2 vs. S1) shows this two-step approach outperforms direct multimodal input — consistent with task simplification, not improved emotion understanding. Future work would benefit from baselines that directly output emotion labels from multimodal input without the LLM middleman.

### Trivial
- The similarity score of 0.82 between Y_EE and Y_CE (line 98) is discussed as evidence of language differences, but no interpretation is given for what this score means for label quality.

## Nice-to-Haves

- **Fine-grained evaluation at the label level.** Beyond group-level Fₛ, reporting per-label-type accuracy (e.g., rare vs. common labels, fine-grained distinctions like "frustrated" vs. "annoyed") would directly test whether the metric captures nuance. A soft match metric using emotion embedding similarity (rather than hard group membership) could reward partial semantic closeness without collapsing to coarse categories.
- **A small human-only ground-truth subset** where annotators independently assign open-vocabulary labels (without LLM pre-annotation) would serve as a sanity check and help quantify the ceiling of the LLM-based pipeline.
- **Sensitivity analysis of the label extraction pipeline** to LLM choice (GPT-4 vs. GPT-3.5), prompt wording, and temperature would clarify the robustness of the ground truth.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Circular evaluation "renders the benchmark meaningless" / "self-consistency test of GPT-3.5":** Overstated. The ground truth involves human checks on clues (two rounds, different annotators) and manual checks on merged cross-lingual labels. The MLLM baselines provide valid relative comparisons. The circularity is a real limitation for the CLUE-Multi baseline, but the benchmark is not meaningless. Moved to Major weakness with softened wording.
- **"No human validation at the label level":** Inaccurate. The paper states "merge the labels extracted from both languages and conduct manual checks. These checked labels are regarded as the ground truth" (line 98). Human validation does occur at the label level. The missing element is formal inter-annotator agreement reporting, not the absence of human validation entirely. Moved to Minor weakness.
- **"The improvement [from multimodal fusion] is still far below CLUE-Multi... The paper interprets this as positive":** The paper does acknowledge the limitations of current MLLMs (Section 7, line 541: "current MLLMs struggle to achieve satisfactory results"). The critic mischaracterizes the paper's interpretation.
- **"The CLUE-MLLM baselines are oddly structured... This does not test the MLLM's inherent emotion recognition ability at all":** The paper's ablation (Figure 6) directly compares S0, S1, S2 strategies and discusses why two-step outperforms one-step. The design is a conscious choice, not an oversight. Retained the substance (that this makes interpretation harder) as a Minor weakness with adjusted framing.
- **Strength Finder's "set-based evaluation metrics that handle open vocabulary" kept, but tension with weakness about coarse grouping acknowledged.**
- **Strength Finder's "comprehensive benchmark and diagnostic experiments" kept as is.**

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel observation that the paper itself missed — they surface methodological critiques, not new scientific findings.

## Suggestions

1. **Address the circularity.** Either (a) construct a held-out human-only ground-truth subset where annotators independently assign open-vocabulary labels (without LLM pre-annotation), and benchmark all methods (including CLUE-Multi) against it, or (b) clearly separate the CLUE-Multi results from the MLLM comparisons, presenting CLUE-Multi as an "oracle pipeline consistency" score rather than an "upper bound" on emotion recognition.

2. **Add a fine-grained evaluation layer.** Report not just group-level Fₛ but also (a) label-level exact match rate, (b) performance on rare vs. frequent labels, and (c) a soft metric (e.g., embedding similarity in an emotion space) that rewards partial semantic match without collapsing to coarse group membership. This would directly address the tension between the open-vocabulary goal and the group-collapsing metric.

3. **Document inter-annotator agreement.** Report agreement statistics (e.g., set overlap, Kappa) for both the clue-checking stage and the final label-checking stage. Specify the number of annotators per round, the specific checking protocol for final labels, and the criteria used during merging.

4. **Add direct-emotion-prediction baselines.** Include experiments where MLLMs are prompted to output emotion labels directly from video+audio+text (without the description middleman) to provide a cleaner measure of MLLMs' emotion recognition capability.

5. **Report the number of GPT-based groups.** Currently the paper does not disclose how many groups GPT-3.5 creates from the 248 labels. Reporting this number would clarify the effective granularity of the evaluation.

## Score and Decision

The paper addresses an important limitation of current MER (fixed, coarse label sets) and provides substantial groundwork — a dataset, metrics, and benchmarks. The human-LLM collaboration strategy for annotation is a clear positive contribution, and the EW-based metric analysis is practically useful.

However, the evaluation has two structural issues that prevent full acceptance. First, the CLUE-Multi oracle baseline (80 Fₛ) is confounded with the ground-truth construction pipeline, making the reported gap to MLLMs misleading as a measure of emotion recognition ability. Second, the metric collapses open-vocabulary labels into coarse groups, partly undercutting the very motivation — capturing nuanced distinctions — that the paper uses to justify the paradigm. These are not fatal flaws (the MLLM relative comparisons are valid, and the dataset is still a contribution), but they are serious enough that the paper in its current form overclaims what it has demonstrated.

With major revisions — human-validated ground-truth subset, fine-grained metric, direct prediction baselines — the paper could be strong. In its current form, it should be rejected from a top venue but encouraged for resubmission after addressing the core evaluation concerns.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
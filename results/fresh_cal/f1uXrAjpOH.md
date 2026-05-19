Now I have all the information needed to produce the final consolidated review. Let me compose it.

## Summary

This paper proposes Open-vocabulary Multimodal Emotion Recognition (OV-MER), a paradigm shift that relaxes the traditional fixed-label-space constraint to allow predicting any number and category of emotion labels. The authors contribute: (1) **OV-MERD**, a dataset with 248 emotion categories (1–9 labels per sample) constructed via a human-LLM collaborative annotation pipeline; (2) **set-based evaluation metrics** (Precision_s, Recall_s, F_s) with GPT-based and EW-based emotion grouping strategies that are shown to be highly correlated (PCC=0.942); and (3) **a comprehensive benchmark** of 16 MLLMs plus heuristic baselines, revealing that current MLLMs still struggle (best GPT-4V achieves only 55.51 F_s) compared to a human-LLM collaborative pipeline (80.05 F_s).

## Strengths

- **Human-LLM collaborative annotation pipeline with quantitative evidence of label enrichment.** Section 3.1 and Figure 20 directly compare human-only vs. human-LLM annotation across three dimensions (clue length, label count, word cloud), showing that the proposed strategy produces longer descriptions, more labels per sample, and a broader emotional vocabulary. This provides concrete evidence supporting the claim of richer label coverage.

- **Set-based evaluation metrics with validated grouping that addresses open-vocabulary ambiguity.** Section 4 defines precision/recall over grouped label sets, and Table 4 reports a Pearson correlation of 0.942 between the EW-based M-avg and GPT-based grouping. This demonstrates that the metric is both reproducible (EW-based approach avoids API dependency for evaluation) and produces consistent rankings with the GPT-based approach.

- **Comprehensive benchmark establishing OV-MER as a challenging task.** Table 1 evaluates 16 MLLMs plus CLUE variants, showing GPT-4V at 55.51 F_s — a clear demonstration that current state-of-the-art MLLMs perform far below the human-LLM collaborative baseline (80.05 F_s). This provides a well-documented baseline for future work.

- **Ablation on CLUE-MLLM generation strategies (S0/S1/S2).** Figure 6 systematically compares three strategies, demonstrating that the two-step extraction (S2: separate description generation followed by label extraction) consistently outperforms joint input (S1), providing a principled design choice for reducing task complexity.

- **Language-agnostic label merging methodology.** Section 3.2 reports a similarity score of 0.82 between English and Chinese label sets and describes a label-merging pipeline with manual checks to eliminate language bias — a concrete methodological contribution for cross-lingual robustness.

## Weaknesses

### Fatal
None.

### Major

- **The CLUE-Multi baseline shares its description source with the ground-truth pipeline, making the performance gap in Table 1 misleading as a measure of model capability.** The CLUE-Multi description (generated via ALLM/VLLM pre-annotation → manual checks → LLM merging) serves as the input to *both* the CLUE-Multi baseline *and* the ground-truth extraction pipeline (Section 3.2, lines 94–98). Although the paper notes (Section 5.2, line 228) that "the OV labels extracted from the monolingual CLUE-Multi differ from the ground truth" because the ground truth merges bilingual extractions with additional manual checks, the shared source remains decisive. The 80.05 vs. 55.51 gap overwhelmingly reflects the baseline's privileged access to a description already curated for emotion recognition, not a genuine comparison between annotation paradigms. The paper should either (a) clearly frame CLUE-Multi as an approximate upper bound rather than a baseline, with explicit disclosure in the table caption, or (b) evaluate it against a ground truth produced via an independent pipeline (e.g., held-out human-only annotations) where this overlap is eliminated. The MLLM comparisons among themselves are unaffected — this issue is confined to CLUE-Multi's standing relative to them.

- **The claimed superiority of human-LLM annotation over human-only annotation lacks external validation.** Section 6 (Figure 20) shows that human-LLM collaboration produces longer descriptions, more labels, and a broader word cloud, and the paper interprets this as evidence of "richer and more comprehensive" annotations. However, there is no external criterion — no independent human evaluation, no downstream task validation, no comparison against an independently collected ground truth — to confirm that these differences constitute *better* annotations rather than simply *different* ones. Longer descriptions and more labels could include noise or spurious emotions. The claim that the strategy is "more accurate" or "more nuanced" is not directly supported by the evidence presented. Including an independent human rating study comparing the quality of human-LLM vs. human-only labels on a random subset would substantially strengthen this claim.

### Minor

- **Dataset documentation gaps.** The paper does not report: (1) the total number of samples in OV-MERD (only "evenly select samples from MER2023"); (2) the number of annotators involved; (3) inter-annotator agreement for the two rounds of manual checks. These are standard reporting requirements for a dataset paper and are needed for the community to assess label reliability.

- **Reliance on proprietary API models for core components limits reproducibility.** The dataset construction, CLUE-MLLM generation, GPT-based grouping, and synonym/word-form expansion all depend on GPT-4V and GPT-3.5 at specific API versions. The paper partially mitigates this with EW-based metrics as a reproducible alternative for evaluation, but the dataset itself is inseparable from these proprietary models. Releasing the exact prompts and the manual-checked intermediate clues (not just final descriptions) would substantially improve reproducibility.

- **Only two experimental runs are reported** (Section 6, line 284: "conduct each experiment twice"). For a benchmark paper, a small number of runs limits the ability to estimate variance meaningfully, especially given the stochasticity of LLM-based pipelines.

- **Baseline hyperparameters (e.g., LLM temperature, decoding strategy) are not specified.** Without this information, independent replication of the results is difficult.

### Trivial

- The paper reports both English and Chinese results side-by-side throughout but does not clearly justify why both are needed for the benchmark, given that the ground truth merges both languages.

## Nice-to-Haves

- **Held-out evaluation with independent ground truth.** The strongest improvement would be to hold out a subset where ground truth is produced via an independent pipeline (e.g., human-only annotations with separate validation), enabling a fair comparison between CLUE-Multi and MLLMs without pipeline overlap concerns.

- **Downstream validation of annotation quality.** A small user study asking independent raters to compare human-LLM vs. human-only emotion labels for appropriateness/completeness on a random sample would strengthen the annotation strategy claims.

- **Exact prompts in an appendix.** Releasing the verbatim prompts used for GPT-4V pre-annotation, GPT-3.5 merging, and label extraction would reduce reproducibility barriers.

## Removed Points

**These points are flagged to be removed, treat them with caution:**

- "The circularity is a structural flaw that makes the paper's core results uninformative." This overstates the severity. The circularity affects only the CLUE-Multi baseline's comparison with MLLMs; the MLLM comparisons among themselves, the dataset, the task definition, and the evaluation metrics remain valid contributions.

- "Reporting both English and Chinese inflates the table without clear rationale." This is a subjective formatting complaint. The paper provides a rationale (Section 5.2, line 228: investigating language differences).

- "The paper's core results do not support the conclusions drawn from them." This is an overstatement contradicted by the evidence. The paper's main conclusions (OV-MER is a challenging task, current MLLMs struggle, EW metrics correlate with GPT metrics) are supported by the data.

- "CLUE-Multi should be excluded from the benchmark table entirely." This is an overly prescriptive demand. The baseline is informative if properly contextualized (as an approximate upper bound).

## Novel Insights

The most noteworthy observation emerging from these reviews is the **tension between the paper's dual use of the CLUE-Multi description** as both the evaluation baseline input and the ground-truth source. This design choice, while procedurally natural (the same curated description is the richest available representation), creates an ambiguity that cuts to the heart of what OV-MER benchmarks are intended to measure: is the task "recognize emotions from raw multimodal input" or "extract emotions from a curated emotion-centric description"? The reviewers correctly identified that these are different tasks with different difficulty profiles, and the paper would benefit from explicitly disentangling them. A second notable insight is that the paper's defense of its annotation strategy relies on internal comparisons (human-only vs. human-LLM within the same pipeline) rather than external validation against an independent standard — a structural limitation that any dataset paper in this space would face but that warrants explicit acknowledgment and mitigation.

## Suggestions

1. Redesign Table 1's presentation of CLUE-Multi: add a footnote or row label clearly stating that CLUE-Multi uses the same description source as the ground-truth pipeline, making it an approximate upper bound rather than a directly comparable baseline.
2. Add inter-annotator agreement statistics for the two rounds of manual checks and report the total dataset sample count in Section 3.3.
3. Provide a small-scale external validation of annotation quality (e.g., independent raters comparing human-LLM vs. human-only labels on 50–100 samples).
4. Release the exact prompts used at each stage of the pipeline.
5. Report baseline decoding hyperparameters (temperature, sampling strategy) to aid reproducibility.

## Score and Decision

**Score:** 7.0 — The paper identifies and operationalizes a genuinely important new paradigm in MER, produces substantial groundwork (dataset, metrics, benchmark), and provides solid evidence for most claims. The main weaknesses (pipeline circularity affecting one baseline comparison, and insufficient external validation of annotation quality) are significant but addressable and do not invalidate the paper's core contributions. The MLLM benchmark, evaluation metrics, and task formulation remain valuable independently of the CLUE-Multi comparison issue.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
Now I have a thorough understanding of the paper and the reviews. Let me synthesize the final review.

## Summary

This paper introduces OpenMeta, a benchmark for metagenomic function prediction that integrates 23 models across 14 datasets covering small-scale, large-scale, fine-grained, and hierarchical classification tasks. The paper evaluates pre-trained and non-pre-trained models, general and specialized models, and sequence-based vs. hierarchical-data-based models. The central finding is that FGBERT (a metagenomic pre-trained model) consistently outperforms genomic pre-trained models (DNABERT2, HyenaDNA, NT), and the paper identifies the absence of unified models that process both sequence and hierarchical phylogenetic data as a key research gap.

## Strengths

- **First standardized benchmark for metagenomic function prediction.** OpenMeta fills a genuine void — prior benchmarks (GUE, GenomicBenchmarks, NT) target single-species genomic tasks, while metagenomic function prediction lacked any standardized evaluation framework. The benchmark integrates 23 models and 14 datasets spanning operon prediction, ARG identification, enzyme classification, virulence factor prediction, nitrogen cycle analysis, and disease phenotype prediction (Sec. 4, Tables 3–5).

- **Multi-dimensional categorization of models.** Models are systematically compared along three orthogonal axes — pre-trained vs. not pre-trained, general vs. specialized, and sequence-based vs. hierarchical-data-based — providing more structured analysis than prior genomic benchmarks (Sec. 4.1, Table 3).

- **Inclusion of hierarchical phylogenetic data.** By incorporating tree-based disease prediction tasks (Cirrhosis, T2D) with PopPhy-CNN, the benchmark extends beyond sequence-only analysis and highlights the value of structural information in metagenomics (Sec. 4.2, Tables 12–13, Fig. 4).

- **Identification of a genuine research gap.** The paper convincingly shows that no existing model jointly processes metagenomic sequences and hierarchical phylogenetic trees, providing a clear direction for future work (Sec. 5.2(B), Conclusion).

- **Task-appropriate evaluation choices.** The use of Macro F1 for imbalanced multi-class data and False Negative Rate for fine-grained ARG prediction shows awareness of practical constraints in metagenomic applications (Sec. 4.3).

## Weaknesses

### Major

- **Only one metagenomic pre-trained model is tested, yet the paper claims "metagenomic pre-trained models" are superior.** The paper's headline finding — that metagenomic pre-trained models outperform genomic ones — rests entirely on FGBERT. Other pre-trained models that could be considered metagenomic (e.g., LookingGlass, DNABERT-S, MG-BERT) are not included. The paper should either (a) include additional metagenomic pre-trained models or (b) explicitly scope the claim to FGBERT, acknowledging that the advantage may reflect FGBERT's specific architecture and pre-training strategy rather than a general property of metagenomic pre-training. The paper mentions LookingGlass (line 90) and ViBE (line 91) in related work but does not test them as baselines.

- **No error bars or variance estimates reported, despite the checklist claiming otherwise.** The checklist states "Yes" for error bars (line 614), but no tables or figures in the paper report standard deviations, confidence intervals, or number of runs. Results are presented as single Macro F1 values. For a benchmark that aims to establish reliable comparisons, readers cannot assess whether a gap of 0.02–0.05 in F1 is meaningful or noise. This is the most impactful improvement needed and undercuts the quantitative comparisons throughout Section 5. *Note to authors: if error bars are present in the tables but were not visible due to formatting, please clarify.*

- **Benchmark framing creates unnecessary circularity concerns.** The paper states it is "based on the FGBERT model" (line 47) and explicitly incorporates FGBERT's downstream tasks (lines 150–154). Although the datasets are standard public resources (CARD, PATRIC, ENZYME, VFDB, NCycDB, etc.) and not proprietary to FGBERT, this phrasing creates the perception that the benchmark was designed to showcase FGBERT's strengths. The authors should reframe the benchmark's task selection as an independent process or explicitly justify why these tasks represent the core challenges of metagenomic function prediction without reference to any single model.

### Minor

- **Hierarchical data evaluation is thin.** Only two disease datasets (Cirrhosis, T2D) and one specialized hierarchical model (PopPhy-CNN) are included. The conclusion that "hierarchical models are needed" would be stronger with more datasets (e.g., from HMP or curatedMetagenomicData) and tests of whether sequence-based models can be adapted to hierarchical inputs (e.g., by aggregating predictions from constituent sequences or feeding abundance vectors into a classifier).

- **Hyperparameter details for general models are underspecified.** The paper states that pre-trained models used "default hyperparameters" (line 699–700), but for general models (SVM, RF, CNN, LSTM, Transformer), the configuration and any hyperparameter search are not described. Since encoding methods (K-mer, one-hot, word2vec) may interact with hyperparameter choices, this limits reproducibility.

- **Compute resources not reported in the paper.** The checklist says "Yes" for compute resources, but no GPU hours, hardware types, or cluster details are provided in the main text or supplement.

- **The claim that "no model can process both metagenomic sequence and hierarchical phylogenetic tree data" (line 335) is stated as an absolute.** The paper does not discuss whether existing sequence models could be adapted (e.g., by flattening tree features or concatenating representations). Acknowledging attempted adaptations (and why they fail) would strengthen the claim.

### Trivial

- The critique of genomic benchmarks in Section 3.2 (lines 136–150, four enumerated limitations) is repeated nearly verbatim in the supplement (lines 740–748). Tightening by cross-referencing would avoid redundancy.

## Nice-to-Haves

- Including additional metagenomic pre-trained models (e.g., DNABERT-S, MG-BERT) if publicly available, or testing whether continued pre-training of a genomic model on metagenomic data changes results, would substantially strengthen the claim that metagenomic pre-training is necessary.
- Expanding the hierarchical data benchmark with more disease datasets and testing adapted sequence models would provide a clearer picture of the gap the authors identify.
- A brief discussion of why existing metagenomic evaluation efforts (e.g., CAMI for taxonomic profiling) do not cover function prediction would sharpen the motivation.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Criticism that the paper does not compare against CAMI or DREAM challenges.** CAMI focuses on taxonomic profiling, not function prediction. This is scope creep — the paper covers functional prediction, and requesting taxonomic benchmarks would turn it into a different paper.
- **Claim that "the tasks, preprocessing, and difficulty levels were presumably chosen to align with FGBERT's strengths."** This is speculative and unsupported by evidence. The datasets used (CARD, PATRIC, ENZYME, VFDB, NCycDB, NCRD) are standard public resources, not proprietary to FGBERT.
- **Criticism about missing related works** (e.g., "discussion of existing metagenomic evaluations is absent"). There are no established function prediction benchmarks in metagenomics — this absence is precisely the paper's motivation.
- **Formatting/style nitpicks** about parser artifacts that do not exist in the original submission.
- **Claim that the paper "does not include the development of new models" as a weakness rather than the legitimate scope choice it is** — the paper explicitly acknowledges this as a limitation (Section 6).

## Novel Insights

None beyond the paper's own contributions. The reviews surface the tension between the paper's claim of being a "comprehensive" benchmark and the reality that it is built from one model's task taxonomy and tests only one metagenomic pre-trained model, but this is a limitation the authors can address rather than a novel insight.

## Suggestions

1. **Restructure the paper's framing.** Remove or clarify the phrase "based on the FGBERT model." Describe task selection as an independent process motivated by the core challenges of metagenomic function prediction. If FGBERT's task taxonomy happens to be a good starting point, say so openly and justify why each task/dataset was chosen on its own merits.

2. **Add error bars.** Run experiments at least 3 times with different seeds and report mean ± std for all tables. This is essential for a benchmark that aims to set a new standard.

3. **Include more metagenomic pre-trained models or scope the claim.** If other metagenomic pre-trained models exist and are accessible, test them. If not, reframe the finding as "FGBERT outperforms genomic pre-trained models" rather than "metagenomic pre-trained models are superior."

4. **Expand the hierarchical data evaluation** with more disease datasets and tests of whether sequence models can be adapted to hierarchical inputs.

5. **Report compute resources** (GPU type, hours) in the main text or supplement.

## Score and Decision

**Originality:** 7/10 — First benchmark for metagenomic function prediction; useful task taxonomy and hierarchical data inclusion.
**Importance:** 8/10 — Metagenomics is a growing field that lacks standardized evaluation; a good benchmark would be highly impactful.
**Claims well supported:** 5/10 — The core finding rests on a single model and lacks error bars. The benchmark itself is solid but the strongest claims are over-extrapolated.
**Soundness:** 5/10 — Missing error bars and an incomplete set of metagenomic pre-trained models weaken quantitative comparisons.
**Clarity:** 6/10 — Generally clear but the "based on FGBERT" phrasing raises unnecessary concerns.
**Value to community:** 7/10 — The benchmark, datasets, and model collection will be useful even if individual claims need tightening.

The paper contributes a valuable benchmark to an underserved area, but the evaluation lacks the rigor needed to support its strongest claims. The weaknesses are addressable in a revision and do not invalidate the core contribution.

**Score:** 6.0
**Decision:** Accept

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
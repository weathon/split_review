## Summary

This paper introduces OpenMeta, a multi-task benchmark for metagenomic function prediction that integrates 14 datasets (ranging from 1,000 to 213,000 sequences) and evaluates 23 models across three dimensions: pre-trained vs. not pre-trained, general vs. specialized, and sequence-based vs. hierarchical-data-based. The benchmark covers small-scale, large-scale, fine-grained, and hierarchical classification tasks. The main finding is that the metagenomic pre-trained model FGBERT consistently outperforms three genomic pre-trained models (DNABERT2, HyenaDNA, NT) across all tasks, and the paper identifies a research gap in unified models that process both sequence and hierarchical data simultaneously.

## Strengths

- **First benchmark explicitly designed for metagenomic function prediction**: The paper identifies a genuine gap — existing genomic benchmarks (GUE, GenomicBenchmarks, NT) are built on single-species data and lack environmental diversity and functional annotation integration. OpenMeta fills this with datasets spanning gene, functional, bacterial, and environmental levels (Section 4.2, Table 4), covering tasks from operon prediction (4,315 sequences) to nitrogen cycle prediction (219,089 sequences).

- **Systematic three-axis categorization of models**: The paper organizes models along pre-training status, specialization, and data type (sequence vs. hierarchical), providing a useful conceptual framework that clarifies the landscape for practitioners (Section 4.1, Table 3). This goes beyond simply listing models and helps identify where gaps exist.

- **Inclusion of hierarchical (phylogenetic tree) data**: The benchmark incorporates phylogenetic tree-structured data for disease prediction (Cirrhosis, T2D) via PopPhy-CNN (Section 4.2). This moves beyond flat sequence classification and surfaces a real gap — no model currently processes both sequence and hierarchical data simultaneously (Section 6, lines 361–364).

- **Fine-grained evaluation with domain-relevant metrics**: For ARG prediction, the benchmark uses the NCRD dataset with fine-grained categories (420 Gene Families, 1,912 Gene Names) and reports False Negative Rate (FNR), which is meaningful for clinical applications where missed resistance genes carry high cost (Section 4.3, lines 222–229). The analysis of which antibiotic classes each method covers (Figure 3) provides practical insight beyond aggregate scores.

## Weaknesses

### Fatal
None.

### Major
- **The central claim that "metagenomic pre-trained models outperform genomic pre-trained models" is not supported by the experimental design.** Only one metagenomic pre-trained model (FGBERT) is compared against three genomic models (DNABERT2, HyenaDNA, NT). These models differ simultaneously in pre-training data, tokenization (BPE vs. 6-mer vs. protein-based), architecture (BERT with ALiBi vs. Hyena operators vs. RoFormer vs. BERT with contrastive learning), and pre-training scale (billions of metagenomic sequences vs. human/multi-species genomes). The design does not isolate pre-training *domain* as the causal factor. A controlled experiment — e.g., pre-training the same architecture on both genomic and metagenomic data — would be needed to support the headline claim. As it stands, the paper demonstrates that FGBERT outperforms these three particular models, not that metagenomic pre-training generically confers an advantage. This does not invalidate the benchmark's value, but the paper's strongest advertised finding is overstated.

- **The hierarchical-data experiments are too thin to support strong conclusions.** Only two datasets are used — Cirrhosis (232 cases) and T2D (440 cases) — both very small by ML standards. Results on Cirrhosis are discussed briefly (Table 12 shows PopPhy outperforming general models), but results on T2D (Table 13) receive essentially no textual analysis or discussion. Variance or significance is not reported. This does not convincingly demonstrate the value of modeling phylogenetic tree structure, especially given the tiny sample sizes and the lack of synthetic or simulated experiments to supplement real data.

### Minor
- **The fine-grained benchmark compares only four methods (FGBERT, DeepARG, RGI, PLM-ARG), two of which (RGI and DeepARG) are specialized ARG prediction tools, not general models.** RGI is described by the paper as a "template-matching method" (Appendix, line 862) — essentially a database lookup, not a learned model. The scope of this comparison is narrow and does not test the generalization of the benchmark across diverse model families.

- **Models are listed in the "23 supported methods" count even when they cannot be evaluated.** The paper notes that CNN-MGP, PlasGUN, and DeepMicrobes are "unsuitable for our multi-classification benchmark" because they are binary classifiers (Section 5.1, lines 236–237). Listing them inflates the method count without contributing evidence. While the paper is transparent about this exclusion, the framing as "23 representative models" (abstract) is somewhat misleading.

- **T2D hierarchical results are presented but not discussed.** Table 13 shows performance on the T2D dataset, but the main text only discusses Cirrhosis results (Section 5.1, lines 332–335). Leaving comparative results unexplained reduces the completeness of the benchmark's analysis.

### Trivial
None.

## Nice-to-Haves
- Cross-validation experiments (e.g., evaluating FGBERT's architecture on genomic tasks and genomic models on metagenomic data) would cleanly quantify the domain gap and transform the comparison from a model-vs-model claim into a substantiated finding about pre-training domain.
- Error bars or significance tests on the main results would strengthen confidence in the reported performance differences.
- Including conventional metagenomic profiling tools (MetaPhlAn, Kraken2, etc.) as baselines would contextualize the deep learning methods against established bioinformatics approaches.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **"Results are embedded as images; not verifiable."** The tables appear as image placeholders because the PDF parser cannot extract their content. In the original submission, these are proper tables. This is a parser artifact, not an author error.
- **"Ignores CAMI challenges."** This criticizes the paper for not citing a specific related benchmark (CAMI). Per policy, I cannot validate the existence or relevance of uncited external benchmarks, and I do not penalize papers for missing related work I cannot confirm.
- **"Metric inconsistency across tasks."** The paper uses Macro F1 as the primary metric and adds Accuracy, Precision, Recall, and FNR for the fine-grained ARG task specifically because FNR is clinically relevant for antibiotic resistance (Section 4.3). The design choice is justified.
- **"Strawman: no analysis of why genomic models fail."** The paper is a benchmark paper, not a mechanistic analysis paper. Demanding embedding-space analysis or feature importance for why models fail is scope creep for a benchmark contribution.

## Novel Insights
The reviews do not surface any insight that the paper itself does not already state. The key observation — that no existing model unifies sequence-level and phylogenetic-tree-level processing — is the paper's own articulated research gap. The review process confirms that the benchmark framework is useful, but the headline comparative claim requires more careful experimental control before it can serve as a reliable finding.

## Suggestions
1. **Temper the headline claim.** Rephrase "metagenomic pre-trained models outperform genomic pre-trained models" to "FGBERT, a metagenomic pre-trained model, outperforms current genomic pre-trained models on metagenomic tasks" — this is what the evidence supports.
2. **Expand the hierarchical-data analysis.** At minimum, report and discuss the T2D results with the same detail as Cirrhosis. Adding significance tests or synthetic hierarchical data would strengthen the argument that tree structure matters.
3. **Add at least one more metagenomic pre-trained model** (e.g., Metagenome-scaffold-based models or DNABERT-S if available) even as a small experiment to broaden the comparison beyond a single metagenomic model.
4. **Release a standardized evaluation pipeline** with fixed train/validation/test splits, hyperparameters, and scripts to maximize adoption and reproducibility.

## Score and Decision

This paper addresses a real need — standardized evaluation in metagenomics — and the benchmark framework itself has utility. The dataset collection, task taxonomy, and three-axis model categorization provide a useful resource. However, the paper's central experimental finding is undermined by a confounded comparison (one metagenomic model vs. three genomic models with different architectures, tokenizations, and pre-training scales), and the hierarchical-data experiments are too thin to support their conclusions. The contribution is real but the claims outstrip the evidence.

**MY FINAL SCORE: <pineapple>5.5</pineapple>**
**MY FINAL DECISION: <orange>Reject</orange>**
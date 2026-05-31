## Summary

ReefNet introduces a large-scale dataset of ~925K genus-level hard coral point annotations from 76 globally distributed sources plus a new Red Sea collection, all taxonomically aligned to the World Register of Marine Species (WoRMS). The paper provides two benchmark settings—within-source (in-distribution) and cross-source (domain generalization)—and evaluates supervised fine-tuning across multiple architectures as well as zero-shot vision-language models. Results show that while within-source performance is promising (up to 84% macro recall), performance degrades sharply under domain shift (best 56% macro recall), establishing a challenging benchmark for domain-adaptive coral classification.

## Strengths

- **Large-scale, taxonomically standardized dataset**: With 925K genus-level annotations across 44 genera from 26 marine ecoregions, ReefNet is substantially larger and more geographically diverse than existing fine-grained coral datasets. WoRMS mapping ensures compatibility with biodiversity research.
- **Expert-verified labels with quantified quality control**: Manual verification of ~9K samples (73% initial agreement) followed by two-stage filtering (source/genus then source-genus level) produces a high-confidence subset with 92% expert agreement, providing reliable ground truth.
- **Two complementary benchmark settings**: The within-source and cross-source splits directly address real-world deployment scenarios (local adaptation vs. global generalization) and reveal a clear performance gap that will drive research on domain adaptation for ecological monitoring.
- **Comprehensive model evaluation**: The paper benchmarks 12 model variations (CNNs, ViTs, VLMs, MLLMs) across multiple loss functions, including biological pretraining (BioCLIP-FT) and self-supervised pretraining (MAE), giving the community a thorough performance baseline.

## Weaknesses

### Major

- **Lack of uncertainty quantification**: The main results in Table 3 report single runs without standard deviations or confidence intervals. Given the high variance expected from cross-source generalization, this undermines the reliability of performance comparisons between models.
- **Small expert verification sample**: Only 8,962 annotations (≈1%) were manually reviewed, yet the entire dataset filtering (removing sources, genera, source-genus pairs) depends on this small sample. Whether the verified subset is representative of the full 925K annotations is not established.
- **Limited analysis of domain shift factors**: The paper documents that cross-source performance drops severely but provides almost no analysis of which specific covariates (camera, depth, water clarity, regional assemblage) drive the degradation. Understanding the nature of domain shift would greatly increase the benchmark's value.
- **Zero-shot evaluation is superficial**: The best zero-shot macro recall is 10.33% (BioCLIP). The paper tests prompt engineering variants for Qwen2.5-VL but does not analyze failure modes or suggest why zero-shot is so poor. The numbers are too low to draw meaningful conclusions beyond "models don't know corals."

### Minor

- **Comparison to existing datasets is slightly misleading in Table 1**: BenthicNet is listed with 287K hard coral annotations, but ReefNet's 925K is claimed as an advantage. However, BenthicNet also supports WoRMS and has broader benthic coverage; the paper should clarify that the 925K figure is genus-level *hard coral* annotations, which is indeed finer-grained than BenthicNet's benthic-level labels.
- **Textual descriptions are not fully utilized**: The paper extracts genus descriptions from books and uses them only in one MLLM experiment (Qwen-Book). The claim of enabling "language-grounded classification" is not evaluated systematically (e.g., via retrieval-augmented classification or prompt ensembling).
- **Loss function ablation uses a different architecture (ViT-L-384) from the main benchmark**: This makes it hard to assess whether the reported gains from CB-Focal would transfer to the architectures used in Table 3.

### Trivial

- The paper states "with-in-source" in a few places instead of "within-source" but this is a minor typographical issue.

## Nice-to-Haves

- Per-source breakdown of cross-source performance (e.g., which held-out sources are hardest and why).
- Evaluation of simple domain adaptation baselines (e.g., CORAL, DANN) to calibrate the challenge level of the cross-source benchmark.
- Analysis of how geographic imbalance (Hawaii dominates) affects per-class and per-region performance.

## Novel Insights

The finding that self-supervised pretraining (MAE on ViT) substantially outperforms biologically pretrained models (BioCLIP-FT) on cross-source generalization is noteworthy and counterintuitive. It suggests that generic visual representations learned from diverse natural images transfer better across reef domains than taxonomic-specific pretraining, possibly because BioCLIP's pretraining distribution (iNaturalist, etc.) is still far from underwater imagery. This insight could guide future pretraining strategies for marine applications. Additionally, the observation that more training data (even at lower quality, 80% expert agreement) yields better cross-source performance than less data at higher quality (91%) is a practical finding for dataset construction.

## Suggestions

1. Report all main results with standard deviations over at least 3 random seeds to establish statistical reliability.
2. Add a figure or table showing per-source macro recall on the cross-source test set, identifying which held-out sources are most difficult and what covariates (e.g., camera type, depth) correlate with difficulty.
3. Evaluate at least one standard domain adaptation method (e.g., DANN or self-training) on the cross-source splits to provide a stronger baseline and better characterize the benchmark's difficulty.
4. Clarify the representativeness of the verified sample: provide the distribution of the 8,962 reviews across sources and genera compared to the full dataset.

## Score and Decision

The paper makes a strong contribution by releasing a large, carefully curated, and taxonomically standardized coral classification dataset with a well-designed benchmark. The weaknesses—primarily lack of uncertainty quantification and limited analysis of domain shift—are not fatal but should be addressed before publication. The work is timely, relevant, and likely to have impact on both the ML community (domain generalization, fine-grained classification) and conservation science.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
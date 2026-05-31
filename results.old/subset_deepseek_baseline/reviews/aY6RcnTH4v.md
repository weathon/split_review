## Summary

ReefNet is a large-scale, taxonomically standardized benchmark for genus-level hard coral classification, aggregating approximately 925K point annotations from 76 CoralNet sources plus a new Red Sea dataset (Al-Wajh Lagoon), all mapped to the World Register of Marine Species (WoRMS) taxonomy. The paper introduces within-source (in-distribution) and cross-source (out-of-distribution) evaluation settings, performs expert verification on a stratified subset to ensure label quality, and benchmarks a range of supervised and zero-shot models. The dataset, code, and pretrained models are planned for public release.

## Strengths

- **High ecological and practical importance.** The paper addresses a pressing need for automated, scalable coral reef monitoring, and the dataset fills a clear gap by providing large-scale, expert-verified, taxonomically consistent genus-level annotations from diverse biogeographic regions. No existing public dataset offers this combination of scale, taxonomic standardization to WoRMS, and geographic breadth.

- **Rigorous dataset curation and quality control.** The multi-stage filtering pipeline (source selection, label standardization, expert verification on 8,962 annotations, source-genus filtering) is well-motivated and carefully executed. The resulting splits with 82–96% expert agreement provide a reliable foundation for benchmarking, and the transparency about remaining bias (e.g., geographic imbalance) is honest.

- **Well-designed benchmark settings and comprehensive evaluation.** The within-source and cross-source splits mirror realistic deployment scenarios, and the experiments cover a wide range of architectures (CNNs, ViTs, BioCLIP-FT) and loss functions. The ablation on class-balanced and focal losses adds practical guidance. The cross-source results convincingly demonstrate the severity of domain shift, establishing a challenging baseline for future work.

- **Valuable insights from zero-shot and MLLM experiments.** The finding that domain-specific textual descriptions (from books) improve zero-shot MLLM performance over generic GPT-4o descriptions, and that BioCLIP outperforms other VLMs, provides actionable knowledge for practitioners aiming to leverage language-grounded models for marine biology.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- The paper does not report inter-rater reliability statistics (e.g., Cohen’s κ) among the marine biologists who performed the expert verification. While the micro-averaged agreement rate is given, understanding expert consensus on difficult cases would further strengthen confidence in label quality.
- The zero-shot evaluation uses a single fixed prompt template for each VLM. Given the sensitivity of zero-shot performance to prompt wording, the results (especially low numbers) may not fully reflect the models’ potential. A brief prompt sensitivity study or the use of multiple templates would be more thorough.

### Trivial
None.

## Nice-to-Haves
- Since many images contain multiple coral genera, a multi-label evaluation setting (where a point annotation targets one patch but the image may have other genera) could be a natural extension. The paper acknowledges this challenge in a qualitative example but does not quantify the effect on evaluation.
- Providing per-image confidence estimates or calibrated probabilities would be useful for practitioners who need to triage uncertain predictions for expert review.

## Novel Insights

Beyond the dataset itself, the paper reveals that self-supervised pretraining (MAE) yields the strongest cross-source generalization among all evaluated methods—outperforming both supervised ImageNet pretraining and BioCLIP-FT (which excels in within-source settings). This suggests that learning robust visual representations from unlabeled data may be more important for handling domain shifts in coral imagery than pretraining on biological taxonomy. Additionally, the zero-shot experiments show that domain-specific, high-quality textual descriptions (from reference books) can meaningfully improve MLLM performance even when base model performance is very low, highlighting a promising direction for vision-language models in specialized ecological domains.

## Suggestions
- Report inter-rater agreement (e.g., κ statistic) for the expert verification subset to quantify label reliability more rigorously.
- Consider adding a baseline with standard data augmentation strategies (e.g., RandAugment) to the cross-source experiments, as augmentation is a common tool for domain generalization and may improve results.

## Score and Decision

MY FINAL SCORE: <score>8</score>
MY FINAL DECISION: <decision>Accept</decision>
## Summary

LEMoN proposes a label error detection method for multimodal (image-text) datasets. The method computes a score as a linear combination of (1) direct CLIP similarity between image and text, (2) the distance between the query's text and the texts of the query image's nearest neighbors (sₙ), and (3) the distance between the query's image and the images of the query text's nearest neighbors (sₘ). Exponential weighting terms (τ₁, τ₂) downweight distant neighbors and likely-mislabeled neighbors to avoid noise propagation. The method is evaluated on six datasets spanning both classification (CIFAR-10/100) and captioning (MSCOCO, Flickr30k, MMIMDb, MIMIC-CXR) settings, with both synthetic and real-world noise, and compared against seven baselines.

## Strengths

- **Formally unifies CLIP similarity and Deep kNN under a single framework.** The paper shows (lines 107–108) that setting β=γ=0 recovers CLIP similarity and that a specific parameter setting recovers Deep kNN. This is not an ad-hoc combination but a principled extension that clarifies the relationship among prior methods.

- **Outperforms all task-unaware baselines in both classification (>4% F1) and captioning (>3% F1 average) settings.** In classification, LEMoN stays within 2% of task-specific methods (AUM, Datamap) that require training a full classifier, while requiring no task-specific training — a meaningful practical trade-off.

- **Real-world blinded human evaluation provides direct evidence that LEMoN's signal transfers to naturally occurring errors.** Across all four datasets tested, LEMoN-flagged examples are confirmed mislabeled at higher rates than CLIP similarity-flagged examples (e.g., CIFAR-100: 20.5% vs 11.0%; Flickr30k: 41.0% vs 32.5%). The annotation procedure uses blind, randomly interleaved presentation.

- **Filtering with LEMoN improves downstream classification accuracy beyond what task-specific methods achieve.** On CIFAR-10, LEMoN-filtered data yields the highest downstream accuracy, outperforming AUM and Datamap despite those methods having higher raw label-error detection F1 — a non-obvious finding.

- **Hyperparameter robustness is quantified across 16 dataset/noise combinations.** LEMoN-fixed (default hyperparameters, no validation set) incurs only a 1.7% average AUROC drop (std=1.3%, worst-case 3.9%) compared to LEMoN-opt (lines 172–173).

- **Systematic noise injection with three distinct types** (random, category-based, noun-overlap) for captioning datasets, moving beyond the single noise type common in prior work.

## Weaknesses

### Fatal
None.

### Major
- **Scalability gap between motivating problem and evaluation.** The paper opens by motivating label error detection for datasets with "millions of labeled instances" (line 15) from sources like LAION. The method requires computing nearest neighbors in both image and text embedding spaces for every query point. On MSCOCO (~120K samples) this is tractable, but at the motivating scale (millions to hundreds of millions) it is not without approximate nearest neighbor (ANN) methods. The paper does not discuss whether ANN methods preserve detection quality, how the neighborhood computation would be approximated at scale, or even acknowledge this as a limitation. The limitations paragraph (lines 237–241) omits this entirely despite it being central to the method's framing. This is a methodological gap between the paper's scope claim and its demonstrated regime.

### Minor
- **Superior detection accuracy does not translate to better downstream captioning quality.** The paper reports (line 182) that LEMoN "performs comparably to the baseline in improving downstream results" on the captioning task. If the headline detection gains over CLIP similarity (Table 3) do not yield meaningfully better downstream captioning, the practical significance of those gains for this application is diminished. The paper acknowledges this honestly but does not analyze *why* — e.g., whether CLIP similarity already catches the most harmful errors, leaving only innocuous ones for LEMoN to find.

- **Real-world evaluation is small and has overlapping confidence intervals for two datasets.** The manual annotation (Table 5, 200 samples per dataset) shows LEMoN ahead on all four datasets, but for CIFAR-10 (10.0%±4.2 vs 5.5%±3.2) and MSCOCO (25.5%±6.0 vs 19.5%±5.5) the 95% binomial CIs overlap. Only a single annotator was used, and inter-annotator agreement is not reported — a concern for a subjective task like judging caption correctness.

- **Single filtering threshold (top 40%) for the captioning downstream experiment.** Unlike the classification filtering experiment (Figure 4), which shows a sweep over thresholds and reveals where LEMoN excels, the captioning experiment only reports one threshold. This makes it impossible to determine whether LEMoN would provide value at more aggressive or lenient filtering rates.

### Trivial
- **Typo in Eq. 3 (line 102):** The sₘ equation uses τ₂,ₙ in the exponential term, but by symmetry with Eq. 2 it should be τ₂,ₘ.
- **Abstract overclaims novelty** (line 5): "no prior works have proposed other methods to filter noisy multimodal data" — BLIP's CapFilt (cited in the paper itself) is a method that filters noisy captions, though it requires supervised training on clean data. The in-paper text (line 30) is more precise ("no prior works have proposed or rigorously compared methods to identify errors in settings with natural language labels").

## Nice-to-Haves

- An ablation of k (neighborhood size) would strengthen the hyperparameter robustness claim, as the paper only evaluates fixed k=30 vs. optimized k.
- A discussion of whether and how ANN methods (e.g., FAISS) could be used at scale, and whether detection quality degrades with approximate search.
- A threshold sweep for the captioning downstream experiment, analogous to Figure 4 for classification.
- Reporting of inter-annotator agreement for the real-world evaluation.

## Removed Points

Points from the inputs that were filtered out:

- **"The downstream captioning experiment undermines the paper's strongest practical claim"** → Demoted from "Critical Issue" to Minor. The paper is transparent that LEMoN performs comparably, not worse. This is a meaningful observation about scope but not a flaw in the paper's methodology.
- **"Synthetic vs real noise conflation"** → Partially merged into the Minor weakness above. The real-world evaluation is present and shows consistent advantage; the CIs overlap, but the paper explicitly acknowledges the "small-scale" nature.
- **"MIMIC-CXR conclusion is undercut by CheXzero outperforming both"** → Removed. The paper's claim is specifically about viability *when no pretrained model exists* — it shows noisy-data pretraining beats a broad-domain biomedical model. The paper explicitly says "clean data from the same domain is certainly superior." The critic misreads this.
- **"No statistical tests"** → Downgraded to Nice-to-Have. Reporting means and stds over 3 runs plus binomial CIs for the real-world evaluation is standard practice for this subfield.
- **"Missing ablation of k"** → Moved to Nice-to-Have.
- **"Computation time comparison"** → Moved to Nice-to-Have.
- **"Missing related works"** → Removed per hard rule (cannot confirm without external sources).
- Several generic strengths from the Strength Finder about "importance of the problem" → Removed.
- **"CapFilt oracle framing could be clearer"** → The paper explicitly calls CapFilt "an oracle" (line 149). No issue.
- **"Single annotator for real-world evaluation"** → Kept as Minor, merged into the existing real-world evaluation point.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Address the scalability gap directly.** Add a paragraph to the limitations or discussion section acknowledging that the current evaluation is on datasets up to ~120K samples, and discuss how ANN methods (e.g., FAISS) could be applied, or bound the regime in which exact search is practical.
2. **Provide a threshold sweep for the captioning downstream experiment**, matching the methodology used for classification (Figure 4). This would reveal whether LEMoN provides value at specific operating points.
3. **Expand the real-world evaluation** with either more samples or multiple annotators to strengthen the statistical grounding of the claim that LEMoN outperforms CLIP similarity on real data.
4. **Analyze the captioning downstream discrepancy** — test the hypothesis that the additional errors LEMoN catches are benign for downstream training, perhaps by characterizing the types of errors each method catches.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
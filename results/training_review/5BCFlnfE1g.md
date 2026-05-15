Here is my consolidated final review.

---

## Summary

This paper reconstructs CLIP's data curation pipeline — metadata construction from WordNet/Wikipedia, substring matching, and per-query balancing — and proposes MetaCLIP, a scalable algorithm that applies this process to CommonCrawl. The paper shows that MetaCLIP-curated data (400M–2.5B pairs) yields strong zero-shot classification performance (e.g., 70.8% ImageNet for ViT-B/16, 82.1% for ViT-bigG), outperforming LAION-400M and published CLIP checkpoints under matched training budgets.

## Strengths

- **First detailed, open reconstruction of CLIP's metadata curation process.** The paper provides the first public, step-by-step breakdown of CLIP's metadata construction — including specific sources (WordNet synsets, Wikipedia unigrams/bigrams/titles), estimated thresholds (PMI ≥ 30, PageView frequency ≥ 70), and the balancing procedure — enabling full reproducibility and freeing the community from reliance on blackbox model-based filters (Section 3, Algorithm 1).

- **Consistent outperformance over CLIP's own published checkpoints and over LAION.** MetaCLIP applied to CommonCrawl achieves higher zero-shot accuracy than CLIP's WIT400M checkpoints across ViT-B/32 (+2.1% IN), ViT-B/16 (+2.5% IN), and ViT-L/14 (+0.7% IN), and also outperforms LAION-400M (Section 4, Table 1). While the comparison against CLIP's checkpoints has confounds (see Weaknesses), the gap is consistent and replicated at multiple model scales.

- **Demonstration that balancing is critical, not just data scale.** The ablation (Table 3) shows that the unbalanced 1.6B pool yields only 61.9% ImageNet (ViT-B/32), while the balanced 400M subset achieves 65.5% — a 3.6% gain with 4× less unique data, isolating the curation+balancing pipeline as the primary driver of quality rather than raw scale.

- **Scales effectively without additional compute or model filters.** The algorithm scales from 400M to 1B and 2.5B pairs within the same training budget (12.8B seen pairs), producing strong results on larger models (ViT-bigG: 82.1% ImageNet) without any external model or extended training (Table 2).

- **Rigorous experimental isolation of data effects.** The paper fixes architecture, training schedule, batch size, and total seen pairs (12.8B) across all experiments, and reports low standard deviation (±0.1% for ImageNet ViT-B/32), ensuring performance differences are causally attributable to data curation rather than training confounds.

## Weaknesses

### Fatal
None.

### Major

- **The comparison against CLIP's published checkpoints is confounded by data source.** MetaCLIP is trained on CommonCrawl, while CLIP's checkpoints were trained on an unknown proprietary data source (WIT400M). The paper asserts it "strictly follows the CLIP training setup" but cannot verify that hyperparameters, pre-processing (face-blurring effects, deduplication strategy), and training dynamics match exactly. Observed performance gaps (e.g., +2.5% on ViT-B/16) could partially reflect differences in the raw data pool rather than the curation method per se. A properly controlled baseline would train on a known reproduction of CLIP's data (e.g., LAION-400M) from scratch using the exact same code and settings as MetaCLIP — the paper does compare to LAION-400M and outperforms it, which partially addresses this, but the headline comparison to "CLIP's data" remains confounded. The claim that MetaCLIP "outperforms CLIP's proprietary data source" should be caveated as "MetaCLIP on CommonCrawl outperforms published CLIP checkpoints trained on unknown data under our training setup."

- **The ablation isolating balancing from epoch count is confounded.** The key ablation (Table 3) compares unbalanced 1.6B (12.8B / 1.6B = 8 epochs) vs balanced 400M (12.8B / 400M = 32 epochs). The paper attributes the 3.6% gap to balancing, but the difference could also be driven by the unbalanced set seeing each sample only 8 times (underfitting) vs 32 times (better convergence). Fixing the number of epochs (e.g., train both sets for 8 epochs) or the number of unique data points (e.g., subsample the unbalanced 1.6B to 400M) would be needed to isolate balancing effects cleanly. The current design conflates two variables.

### Minor

- **The paper's framing as "demystifying"/"revealing" CLIP's data is somewhat overstated.** The paper acknowledges that "our approach may differ from CLIP's as these are not known publicly" (line 79) and estimates several thresholds (PMI, PageView frequency) to hit a 500k-query budget. It uses PageViews as a proxy for Wikipedia search volume. Since CLIP's actual thresholds, data source, and exact pipeline are unknown, the paper provides a plausible reconstruction rather than a definitive revelation. This is a valuable contribution, but the title and framing overstate what is concretely established. Reframing as a "reconstruction and open-source reimplementation" would be more precise.

- **The metadata includes stopwords/function words (e.g., "of", "the", "and") whose visual informativeness is near zero.** The paper acknowledges this (Table 3, line 149) and claims they "enhance text quality," but provides no analysis or evidence for this claim. In practice, these entries have extremely low sampling probabilities (e.g., 20k/120M ≈ 0.00017 for "of"), so their practical harm is likely negligible. However, the paper's justification is speculative and unsubstantiated. A simple ablation removing stopwords from the metadata would clarify their actual impact.

- **Metadata threshold estimation lacks sensitivity analysis.** The paper estimates PMI ≥ 30 and View Frequency ≥ 70 to reach 500k entries, but does not study how varying these thresholds changes the metadata composition or downstream performance. The only threshold ablated is the balancing cap *t*.

- **Per-task standard deviations and confidence intervals are not reported.** Only a single standard deviation (±0.1% for ImageNet ViT-B/32) is given. Given the experimental cost of training CLIP models, this is understandable, but the paper's conclusions rely on small margins (e.g., +0.7% on ViT-L/14) and would benefit from statistical characterization.

- **The independent sampling algorithm (Algorithm 1) is described as "equivalent" to CLIP's curation, but this equivalence is approximate.** CLIP likely built an inverted index and exactly subsampled to 20k per query, while MetaCLIP uses probabilistic independent sampling that only controls expected counts. The paper does not analyze the distribution of actual counts or discuss when the approximation might diverge from exact balancing.

### Trivial
- The pseudocode uses `random.random()` without specifying a random seed, a minor oversight for reproducibility.
- The "Ablation Study" section text has a truncated comparison ("58.5 vs 58") on line 408.

## Nice-to-Haves
- **Controlled CLIP data replication:** Train a CLIP model on a known reproduction of CLIP's data (e.g., the original WIT400M if accessible, or a constructed proxy) using the exact same training code and hyperparameters as MetaCLIP, to directly isolate curation method from data source.
- **Epoch-controlled balancing ablation:** Compare balanced vs. unbalanced data at the same number of epochs (not just same seen-pair count), to disentangle balancing effects from repetition effects.
- **Metadata composition ablation:** Vary the metadata source (e.g., remove stopwords, use only WordNet, use only Wikipedia) and measure performance impact.
- **Comparison to DataComp filtering strategies** under a shared experimental protocol.

## Removed Points

These points are flagged to be removed — treat them with caution.

1. **"CLIP used a teacher model to filter its data"** — The reviewer claimed Radford et al. used a teacher CLIP model to filter their own data, making the paper's claim that CLIP uses a "pure NLP-based approach" misleading. This is factually wrong: the CLIP paper describes a metadata/substring-matching curation pipeline with no model-based filtering. Model-based filtering was introduced by LAION, not CLIP. Removed as factually incorrect.

2. **"Stopwords flood the dataset with noise via the 20k cap"** — The reviewer argued that stopwords like "of" would allocate 20k pairs each, "flooding the dataset with noise." This ignores the algorithm's sampling probability: for "of" with count 120M, the sampling probability is 20k/120M ≈ 0.00017, making the actual contribution of stopword entries negligible. The paper's justification is weak, but the practical concern is unfounded. Removed as technically invalid.

3. **"Missing link or verification that pipeline is reproducible"** — The paper states "We make our pipeline... publicly available." Criticizing lack of a link in a submission is a formatting nitpick. Removed per hard rule on formatting/style nitpicks.

4. **"The paper criticizes LAION for labor-intensive filters but MetaCLIP's pipeline is also complex"** — The paper's criticism is about reliance on a blackbox model, not about pipeline complexity per se. The reviewer's comparison is a misreading. Removed as misunderstanding the paper.

5. **"Missing related work"** — All such criticisms are removed per instructions (cannot confirm existence of unmentioned works).

6. **"Hardware differences (64/128 V100s vs 256 V100s) affect training dynamics"** — The paper matches the global batch size (32,768), which is the critical parameter for CLIP training dynamics. Number of GPUs with equivalent batch size is standard practice. Removed as strawman.

7. **"The ablation on t (15k, 20k, 35k) shows 15k gives same ImageNet accuracy"** — The paper acknowledges all values give "slightly worse" performance and does not claim 20k is magic. The difference is marginal. This is not a genuine weakness.

8. **"Online balancing achieves higher accuracy (66.1%) than offline (65.5%), contradicting the claim that balancing is essential"** — This conflates "offline vs online balancing method" with "balancing vs no balancing." Both online and offline balancing dramatically outperform the unbalanced set (61.9%), so the claim that balancing is essential is supported, not contradicted. Removed as a misreading.

## Novel Insights
The most interesting finding is the characterization of the "tail/head transition" (Figures 2-3): only 3.2% of metadata entries account for 94.5% of total substring matches, and the balancing cap t=20k aligns with the point where head entries begin exhibiting exponential growth in match counts. This provides a principled explanation for why t=20k works — it converts the cumulative count curve from exponential to linear growth — and suggests a heuristic for choosing t on different data pools (maintain the same tail/head ratio rather than the same absolute threshold). This insight is practically actionable for anyone building large-scale vision-language datasets.

## Suggestions

1. **Reframe the contribution.** Replace "demystifying/revealing CLIP's data" with "reconstructing CLIP's data curation pipeline" or "open-source replication of CLIP's curation approach." Explicitly state which steps are verified (WordNet, Wikipedia unigrams), which are estimated (PMI threshold, pageview threshold), and which are unknown (data source, exact CLIP thresholds). This would better align the framing with what the paper actually establishes.

2. **Add an epoch-controlled ablation.** Train the unbalanced 1.6B pool for only 8 epochs (the current setup) and also train a balanced 400M subset for 8 epochs (fewer seen pairs). This would disentangle the effect of balancing from the effect of more training iterations. If the gap persists at 8 epochs, the balancing claim is strongly supported.

3. **Add a stopword removal ablation.** Remove function words (of, the, and, etc.) from the metadata and measure performance. If performance is unchanged, this would either confirm that these entries have negligible impact (and remove the need for speculative justification) or reveal a genuine issue.

4. **Explicitly acknowledge confounds in the CLIP comparison.** Add a sentence to Section 4 noting that CLIP checkpoints were trained on an unknown data source with possibly different pre-processing, and that the comparison is indicative rather than controlled.

5. **Analyze the distribution of actual counts from the independent sampling algorithm** to verify how closely it matches the intended exact cap of t.

## Score and Decision

This paper makes a significant practical contribution: it provides the first open, model-free reconstruction of CLIP's data curation pipeline and demonstrates that it produces highly competitive training data from CommonCrawl. The core technical claims (the curation+balancing pipeline works well, balancing is important, the pipeline scales) are well-supported by experiments. The paper is clearly written and the algorithm is simple enough for the community to adopt.

However, the paper has two notable weaknesses: (1) the headline comparison against CLIP's proprietary data is confounded by data source differences, and (2) the key ablation isolating balancing from epoch effects conflates two variables. Neither weakness invalidates the paper's core contribution, but both require more careful framing and additional experimental controls to fully substantiate the strongest claims. These are addressable in revision.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
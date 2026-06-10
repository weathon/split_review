## Summary

This paper introduces BirdSet, a large-scale curated collection of bird sound recordings from Xeno-Canto (≈530,000 recordings, ≈9,734 species, 6,800+ hours) paired with eight strongly labeled soundscape test sets (400+ hours). It standardizes label formatting via eBird taxonomy, provides uniform 32kHz/5-second-segment preprocessing, and releases everything on Hugging Face with a reproducible codebase. The paper also benchmarks six model architectures across three training scenarios (large-scale, medium, dedicated fine-tuning) on multi-label classification under covariate shift.

## Strengths

- **Standardized large-scale dataset that addresses real fragmentation in avian bioacoustics.** Table 1 (related datasets) systematically documents 16 prior publications using 17 different data sources with incompatible tasks, metrics, and preprocessing. BirdSet is the first to unify these under a consistent curation pipeline with uniform metadata, open access on Hugging Face, and a reproducible codebase. This is a concrete, well-executed contribution that eliminates a significant data-processing bottleneck for the field.

- **Massive scale and diversity of the test collection.** The eight soundscape datasets span diverse geographic regions (Peru, Germany, Hawaii, Senegal, etc.), cover 21–132 species each, and exhibit varying class imbalance (Pielou's J from 0.54 to 0.78). At 400+ evaluation hours with strong labels, this is a substantially larger and more diverse test bed than any prior work in avian bioacoustics, enabling evaluation of generalization across different acoustic environments.

- **Comprehensive literature review and challenge taxonomy.** Sections 2.1–2.4 provide a structured breakdown of four audio-classification challenges (datasets, model training, model robustness, evaluation) with thorough citation of prior work, and map each challenge to a concrete evaluation use case in BirdSet. This provides a useful research roadmap that goes beyond simply releasing a dataset.

- **Systematic benchmarking across architectures and training regimes.** The paper evaluates six models (EfficientNet, ConvNext, AST, EAT, W2V2, Perch) under three training scenarios (LT, MT, DT) on all eight test sets using three threshold-free metrics with multiple seeds. This is the broadest controlled comparison in avian bioacoustics to date.

## Weaknesses

### Major

- **Overclaimed "surpasses AudioSet" framing.** The abstract and introduction repeatedly claim BirdSet "surpasses" AudioSet with "↑17%" more hours and "↑18×" more classes. This comparison conflates fundamentally different label ontologies: AudioSet's 527 classes are general acoustic event types (dog bark, car horn, speech), while BirdSet's ≈10,000 classes are a biological species taxonomy for a single domain. The 18× factor is not a measure of superiority but a reflection of fine-grained biological classification versus general sound ontology. The "↑17% more hours" likewise compares curated 10-second clips (AudioSet) with variable-length focal recordings (BirdSet) that differ in label structure and curation. The paper would be stronger if it positioned BirdSet honestly as a complementary, domain-specific resource rather than claiming to "surpass" a dataset designed for a different purpose. This overclaiming permeates the abstract, introduction (line 21), and the "Related benchmarks" section (line 173), and undercuts the paper's credibility.

- **Thin empirical analysis for a benchmark paper.** The paper provides a leaderboard (Table in Figure 4) but does not analyze *why* performance varies across datasets. Observations such as "PER and UHH are challenging due to complex overlaps…and location-specific background noise" (line 282) are qualitative and unsupported by quantitative evidence linking dataset properties (class imbalance, signal-to-noise ratio, species diversity, annotation density) to model performance. The authors candidly acknowledge this in the limitations: *"While our benchmark indicates generalization performance in multi-label audio classification, it does not analyze BirdSet's underlying characteristics affecting model performance"* (line 376). For a paper whose title and central framing are about a benchmark, the lack of diagnostic analysis is a significant gap. A benchmark should help researchers understand *what* makes a dataset hard and *which* model properties matter, not just report scores.

### Minor

- **Perch baseline comparison is not scrutinized for data overlap.** The paper excludes BirdNET due to "potential test data leakage" (line 279) but does not apply similar scrutiny to Perch, which was also trained on Xeno-Canto data (the same source as XCL). While the specific snapshot may differ, the domain overlap is substantial and could inflate Perch's performance (especially on T1-Acc). The paper should either discuss this limitation or provide a controlled comparison where all models are trained on the same BirdSet data.

- **MT and DT scenarios reported only as aggregates.** The main results table (Figure 4) provides per-dataset breakdowns for the LT scenario but only aggregate "Score" columns for MT and DT. Per-dataset results for all three scenarios would allow readers to understand when large-scale pre-training helps versus when dedicated fine-tuning suffices.

- **Limited description of event detection quality.** The paper uses `bambird` for event detection in focal recordings (line 225) but does not describe the method's accuracy or how detection quality affects downstream training. Since event detection determines the segmentation of training samples, this is a relevant detail for evaluating data quality.

### Trivial

- **Label cardinality per segment is not reported.** The paper reports Pielou's evenness per dataset but does not show how many segments contain 0, 1, 2+ species. This is useful context for understanding multi-label difficulty.
- **Table 1 in the dataset section (line 248) reports segments and annotations but not the total recording hours in hours** (despite hours being emphasized in the abstract). Adding hours per dataset to the table would connect the claims to the data.

## Nice-to-Haves

- A scatter plot or table correlating per-dataset AUROC with dataset properties (evenness J, number of classes, annotation density) would substantially increase the diagnostic value of the benchmark.
- The paper could frame the AudioSet comparison as "BirdSet offers complementary value as a domain-specific resource at a scale that fills a gap AudioSet cannot address" rather than claiming superiority.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"No standard deviations in main results table."** Removed because the paper explicitly states that standard deviations are in the appendix (line 279). The appendix was stripped by the parser; the information exists in the original submission.
- **"Training hyperparameters not in main text."** Removed for the same reason — details are in the appendix.
- **Line 260 formatting artifact ("92  & 51").** Removed as a parser-induced formatting error, not a paper defect.
- **Generic criticism about "missing variance information essential for cross-study comparability."** While variance info is useful, the paper addresses this via the appendix. This specific framing was merged into the removed point above.
- **Strength Finder's claim that BirdSet "surpasses" AudioSet is a strength.** Removed because this conflicts with a verified weakness. The scale itself is a genuine strength; the "surpasses" framing is not.

## Novel Insights

The most interesting observation from the reviews is the tension between Perch's dominance on T1-Acc (retrieval-oriented) and ConvNext's dominance on AUROC/CMAP (discrimination-oriented). This split highlights that different model architectures capture fundamentally different aspects of the multi-label classification task, and that benchmark conclusions depend heavily on metric choice — a finding that the paper surfaces but does not deeply analyze. A systematic investigation of this metric architecture interaction across datasets would be a valuable follow-up.

## Suggestions

1. **Reframe the AudioSet comparison.** Drop "surpasses" and the percentage arrows. Position BirdSet as a large-scale domain-specific resource that fills a gap AudioSet cannot address, rather than as a replacement or improvement. This change requires no additional experiments and eliminates the most distracting weakness.

2. **Add per-dataset results for MT and DT scenarios.** The data clearly exists (it aggregates into the "Score" columns). A per-dataset bar chart per metric for all three scenarios would greatly increase the paper's informativeness.

3. **Include a correlation analysis** between per-dataset model performance (AUROC) and dataset properties (evenness J, number of classes, annotation density). This would directly address the gap acknowledged in the limitations.

4. **Discuss the Perch data overlap** explicitly, either by quantifying the Xeno-Canto overlap between BirdSet's XCL snapshot and Perch's training snapshot, or by acknowledging this as a limitation of the comparison.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
Now I have verified the key claims against the paper. Let me write the consolidated review.

## Summary

This paper tackles detection of illicit Bitcoin CoinJoin transactions through a combination of large-scale dataset construction, novel feature engineering (KeyLinker address clustering and Shared Send Untangling complexity metrics), and a semi-supervised learning framework. The authors collect 163M CoinJoin transactions (4.6M labeled) and show through systematic ablation that their feature set is effective, while claiming that "quality over quantity" in features — rather than naive data expansion — drives SSL success.

## Strengths

1. **Large-scale, purpose-built dataset of CoinJoin transactions.** The paper assembles 163M CoinJoin transactions spanning Bitcoin's full history up to block 882,421, with 4.6M labeled from multiple external sources (Table 1). This is the most comprehensive public-verification CoinJoin dataset described in the literature and represents a meaningful resource for the blockchain forensics community. (Section 5.1, Table 1)

2. **Systematic ablation isolating the contribution of each feature group across three model classes.** Tables 2 and 3 provide per-feature-set results (from Default alone through full feature set) for XGBoost, CatBoost, and Random Forest, allowing readers to assess the marginal contribution of each feature family (REUSE, CS, OTC, SSU). The consistent finding that `Default+REUSE+CS+SSU` yields the best results, and that adding OTC does not improve performance, is a concrete empirical observation. (Tables 2, 3)

3. **Domain-grounded feature design.** The KeyLinker clustering (based on cryptographic public key reuse, offering stronger guarantees than heuristic methods) and SSU complexity metrics (classifying transactions by untangling difficulty) are well-motivated by the specific challenges of CoinJoin analysis. These go beyond generic feature engineering and reflect genuine domain expertise. (Sections 2.2, 5.1)

## Weaknesses

### Major

1. **The core claimed result — that SSL outperforms supervised learning — is contradicted by the paper's own data.** Contribution 3 states that the "semi-supervised learning framework outperforms supervised baselines" (Section 1, line 33) and the abstract claims SSL "effectively leverages unlabeled data." Yet the best XGBoost F1-score goes from 0.844 (supervised, Table 2) to 0.845 (SSL, Table 3) — a change of 0.001, well within noise. Many configurations show no change or slight degradation. The paper acknowledges "did not produce dramatic metric gains" (Section 6.3) but maintains the outperformance framing in the abstract and contributions. This disconnect between the narrative and the evidence is a fundamental problem: the central claim that SSL provides a meaningful improvement — and by extension the title's emphasis on SSL — is not supported by the experiments. The paper's valuable contributions (dataset, features) would be better served by an honest reframing.

2. **No comparison against any prior method.** The paper cites multiple prior works achieving 91–97% accuracy on related Bitcoin classification tasks (Section 3: Nerurkar 2022, Rathore et al. 2022, Alarab et al. 2020) and compares against only three gradient-boosted models (XGBoost, CatBoost, Random Forest) trained on its own features. Without benchmarking against even a single representative prior approach — e.g., a GNN-based detector, a Random Forest with standard features, or the feature-selection method of Sie et al. (2024) — there is no way to assess whether the proposed feature engineering advances the state of the art. The reported F1 of 0.845 and ROC AUC of 0.97 are plausible, but their significance relative to existing methods is unknown.

3. **No variance or uncertainty reporting.** All results in Tables 2 and 3 are reported as point estimates without standard deviations, confidence intervals, or cross-validation fold variance. This is particularly problematic because the paper makes strong comparative claims about small differences: the deduction that OTC features "introduce noise" (abstract) rests on an F1 drop of 0.003 for XGBoost (0.844 → 0.841) and 0.001 for CatBoost (0.824 → 0.823). Without any measure of variability, the reader cannot assess whether these differences are systematic or simply random fluctuation.

4. **Pseudo-labeling procedure lacks critical implementation details.** Section 6.3 describes the SSL process only qualitatively: "select the top fraction of samples on both sides of the decision boundary, adjusting the share of positives and negatives." The paper does not report how many pseudo-labeled samples were added per batch, what the confidence threshold or top-fraction value was, or the resulting class distribution of the expanded training set. These details are necessary for reproducibility and for evaluating whether the quality-filtering mechanism actually selected better pseudo-labels.

### Minor

1. **The "data quality" principle is described but not operationalized.** Section 5.2 introduces the idea that pseudo-labels from SSU Simple/Separable transactions and KeyLinker clusters are "high quality," but no formal quality metric is defined or measured. The argument would be strengthened by, e.g., computing precision of pseudo-labels against held-out ground truth for different quality tiers.

2. **Label conflict resolution from multiple external sources is opaque.** The paper states that contradictions among labels from WalletExplorer, Elliptic++, MBAL, and Kaggle were "resolved manually" (Section 5.1) but provides no details on the resolution criteria, the frequency or types of conflicts, or how subjective adjudication was handled. This is a reproducibility concern for the dataset contribution.

3. **The formal model's tag propagation rule is over-simplified.** Equation (1) states `∀ A, A' : A ∼ A' → Tag(A) = Tag(A')`, which unconditionally propagates labels through clustering relations. As the paper concedes indirectly, clustering heuristics are probabilistic and this rule would propagate errors. The formalization would benefit from a probabilistic treatment.

4. **OTC vs. KeyLinker is never tested in a head-to-head ablation.** The paper compares feature sets that include both REUSE+CS and OTC, or REUSE+CS without OTC, but never runs an experiment where OTC *replaces* REUSE (KeyLinker) features. This would be the cleanest test of the claim that KeyLinker is higher-fidelity than OTC.

### Trivial

None.

## Nice-to-Haves

- A naive SSL baseline (self-training without quality filtering) would directly demonstrate the value of the "quality over quantity" approach.
- Reporting computational cost of the clustering and feature extraction steps (CS, OTC, KeyLinker on 1.15B transactions) would clarify practical deployability.
- A discussion of potential label bias in the 4.6M labeled CoinJoin transactions (e.g., easy-to-label transactions being overrepresented) would strengthen the limitations section.

## Removed Points

The following criticisms were raised in input reviews but are excluded for reasons stated:

- **"The tag propagation rule is unrealistic" (Harsh Critic, Section 4):** This is a standard simplifying assumption in formal models. Every modeling framework makes idealizing assumptions; flagging this without specifying why it harms the paper's actual results is not a substantive weakness.
- **"Decision to avoid SMOTE/ADASYN is insufficiently justified":** The paper provides a reasonable justification (pseudo-labeling later introduces new positives). While an ablation would be nice, this is a standard design choice, not a weakness.
- **"Table 2 formatting makes it unreliable" (Harsh Critic):** The table is parseable; repeated rows reflect different configurations/hyperparameters, not errors. Formatting artifacts from PDF parsing should not be attributed to the authors.
- **"Paper does not discuss CoinJoin transaction label bias" (Harsh Critic):** This is a speculative concern about what the paper does not discuss, not a concrete error. A valid nice-to-have, not a weakness.
- **Strength Finder claim that "controlled experiment proves SSL improvement contingent on feature quality":** The evidence does not support "proves" — the SSL improvement over supervised is 0.001 F1. This strength is removed as overclaimed.
- **"Missing related works":** Excluded per policy — I cannot confirm existence of specific missing references.
- **All formatting/style/typo criticisms and reproducibility nitpicks about unreleased code or hyperparameters:** Excluded per policy.

## Novel Insights

The most interesting observation that emerges from combining the reviews is that the paper's evidence actually supports a different — and perhaps more honest — narrative than the one it tells. The data show that feature engineering (KeyLinker + SSU) yields good detection performance with gradient-boosted models in both supervised and SSL settings, and that adding OTC heuristics provides no benefit. This is a genuine insight about feature quality in blockchain analytics. But the attempt to wrap this in an SSL framing, complete with the claim that SSL "outperforms" supervised learning, backfires because the SSL results are virtually identical to the supervised results. The paper's real contribution — the dataset and the feature ablation — is obscured by the overstated SSL narrative.

## Suggestions

1. **Reframe the paper around the dataset and feature engineering contributions**, and either (a) provide clear evidence that SSL improves upon supervised learning (by comparing with a naive SSL baseline and reporting statistically significant gains), or (b) drop the claim that SSL "outperforms" and present the SSL experiment as a demonstration that performance is maintained while expanding training data, which is a weaker but honest finding.

2. **Add at least one external baseline** — e.g., a Random Forest with standard transaction features (number of inputs/outputs, total value, fee) without the proposed domain-specific features, or a simple GNN-based classifier — to contextualize the F1 of 0.845 relative to existing approaches.

3. **Report cross-validation variance** (standard deviations across folds) for all metrics in Tables 2 and 3 so that small differences can be assessed for significance.

4. **Provide concrete details of the pseudo-labeling procedure**: number of samples added per iteration, selection threshold, and resulting class distribution.

5. **Run a head-to-head ablation** comparing REUSE (KeyLinker) against OTC features directly, replacing one with the other rather than just adding OTC to an already-strong feature set.

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/jOZCfCvH4c.md` | 2.00 | 1 | Ethereum SSL for illicit detection — similar topic but weaker (smaller dataset, less thorough ablation, lower novelty). This paper is clearly stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/Wj0qUfH7b3.md` | 2.67 | 1 | Bitcoin address clustering with GNNs — similar domain, comparable weaknesses (no SOTA baselines), but this paper has a larger data contribution and more systematic evaluation. This paper is somewhat stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/n41veICTrg.md` | 4.50 | 1 | Smart contract vulnerability detection (blockchain, different task). Comparable evaluation rigor but stronger empirical validation. This paper is weaker. |
| `/home/wg25r/review_agent/human_reviews_2026/ZURYrJgigi.md` | 5.00 | 1 | Graph anomaly detection with SSL — stronger methodology, comprehensive baselines, variance reporting. This paper is notably weaker. |
| `/home/wg25r/review_agent/human_reviews_2026/pE7trvliXi.md` | 4.00 | 2 | Tabular SSL — clean empirical methodology, clear improvement demonstration. Similar strengths in systematic evaluation but this paper has weaker evidence for claims. Comparable. |
| `/home/wg25r/review_agent/human_reviews_2026/i8b5T0ezsk.md` | 4.50 | 2 | Tabular anomaly detection — strong empirical benchmarking, theoretical grounding. This paper has less rigorous experimental evidence. Weaker. |
| `/home/wg25r/review_agent/human_reviews_2026/W1whWBesWC.md` | 3.50 | 2 | Fraud graph detection — similar evaluation challenges. This paper has a larger data contribution but weaker empirical validation. Roughly comparable. |

**Round 1 Bracket:** [3.5, 5.5]. The paper is clearly above the weak blockchain papers (2.0–2.67) due to its dataset scale and systematic ablation, but below papers at 4.5–5.0 that have stronger empirical validation (SOTA baselines, variance reporting, unambiguous improvement evidence).

**Round 2 Narrowing:** Within the [3.5, 5.5] bracket, comparison with anchors at 3.5–4.5 confirms the paper sits near 4.0. It is stronger than the 3.5 anchor (W1whWBesWC) due to its dataset and cleaner ablation, comparable to the 4.0 anchor (pE7trvliXi) in systematic evaluation, but weaker than the 4.5 anchors (i8b5T0ezsk, n41veICTrg) which have stronger empirical evidence for their core claims.

### Assessment

- **Originality:** Moderate. The feature engineering (KeyLinker, SSU metrics) and dataset are genuinely novel. The SSL framework is a standard self-training approach.
- **Importance of question:** High. Illicit transaction detection in cryptocurrency is practically important.
- **Claims well-supported:** No. The central claim about SSL improvement is contradicted by the data. The OTC noise claim rests on negligible metric differences without variance.
- **Soundness of experiments:** Below threshold. Missing SOTA baselines, no variance reporting, opaque pseudo-labeling details.
- **Clarity:** Good. The paper is well-structured and the methodology sections are clear.
- **Value to community:** The dataset and feature insights could be valuable, but the current framing and weak evidence limit impact.

The paper has genuine contributions (dataset, feature engineering) but the experimental evaluation does not support the paper's central narrative. The SSL "demonstration" is the headline contribution yet produces no meaningful improvement over supervised learning. The lack of SOTA baselines and variance reporting further weaken the empirical case. A major revision is needed.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>
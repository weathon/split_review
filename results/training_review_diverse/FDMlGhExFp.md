Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

This paper introduces TabDPT, a tabular foundation model that combines a row-based transformer encoder (building on TabPFN) with retrieval-augmented self-supervised pre-training on real data. The model performs both classification and regression via in-context learning without any task-specific fine-tuning or hyperparameter optimization, achieving state-of-the-art or tied performance on the OpenML-CC18 (classification) and OpenML-CTR23 (regression) benchmarks compared against tuned tree-based and neural baselines. The paper also presents a scaling analysis across model and data sizes and introduces duel-based Elo ratings for tabular model comparison.

## Strengths

- **State-of-the-art zero-shot performance.** Table 1 shows TabDPT achieves the highest AUC on CC18 (0.929) and the highest Correlation (0.833) and R² (0.729) on CTR23, outperforming tuned baselines including XGBoost, CatBoost, LightGBM, TabR, and MLP-PLR. On CC18 accuracy, TabDPT (0.873) is statistically tied with TabR (0.874) with overlapping confidence intervals. This directly supports the central claim that ICL without fine-tuning can match or exceed per-dataset trained methods.

- **First scaling analysis for tabular foundation models.** The paper systematically varies model size (33K to 78M parameters) and training data (52M to 2B cells), fitting a joint power-law model following Hoffmann et al. (2022). The observation that real data yields predictable improvements while synthetic data plateaus at larger model sizes is new to the tabular domain and suggests that future gains will come from curating larger real-data training sets.

- **SSL on real data is the critical component.** The ablation study (Figure 4b) shows that replacing the self-supervised objective with only the original supervised target causes the largest performance drop on both AUC and R², validating the paper's core methodological design choice.

- **Massive inference speed advantage.** Figure 4a demonstrates that even the largest TabDPT model is at least one order of magnitude (up to 4 orders) faster than tuned baselines on large datasets, since ICL eliminates per-dataset training and HPO.

- **Introduction of duel-based Elo ratings for tabular model comparison.** The paper adapts duel-based ranking methods (Elo scores, win-rate matrices) to the tabular domain, allowing comparison of algorithms when not all datasets are shared across methods — a practical contribution given the lack of a single accepted benchmark.

## Weaknesses

### Fatal
None.

### Major
None. The weaknesses identified below are addressable and do not threaten the paper's core claims.

### Minor

- **Contamination analysis lacks quantitative transparency.** The paper describes a detailed contamination-check pipeline (metadata extraction, k-d tree matching, manual review) but reports *no numbers* — no counts of how many training–evaluation dataset pairs were flagged, how many were removed, or what thresholds triggered a flag (Section 4.3, lines 250–262). Because both training data and evaluation benchmarks (CC18, CTR23) are drawn from OpenML, the reader cannot independently assess whether residual overlap might inflate zero-shot performance. The check was performed and the methodology is sensible, but without quantitative disclosure the central SOTA claim is weakened.

- **Scaling-law claims are stronger than the data warrant.** The paper fits a five-parameter joint power-law model \((\ell(P,D)=A/P^\alpha + B/D^\beta + E)\) to at most five or six discrete model sizes and a similar number of data sizes (Section 5.2). No confidence intervals, residuals, or out-of-sample validation (e.g., leave-one-size-out) are provided for the reported exponents \(\alpha=0.42,\ \beta=0.39\). The qualitative trend — performance improves with scale and real data beats synthetic — is plausible and interesting, but the presentation of a "validated scaling law" outpaces the empirical support. The paper would benefit from a more cautious framing (e.g., "consistent with a power-law trend").

- **Ablation base model performance not reported.** Figure 4b reports *reduction* in AUC/R² relative to a 28M-parameter base model (line 399), but the absolute performance of that base model is not given. A 0.05 drop means different things depending on whether the base AUC is 0.90 vs. 0.95, making it difficult for the reader to gauge practical impact.

- **SSL method details are underspecified.** The description of the random-column prediction objective (Section 3.2, lines 173–174) states that for classification, "if the number of unique values is high, we distribute the values over random partitions and use those as target classes." The threshold defining "high" and the procedure for assigning partitions are not specified. These details matter for both reproducibility and understanding why "Supervised Target" causes the largest ablation drop.

### Trivial

- None beyond the minor points listed above.

## Nice-to-Haves

- A comparison with a version of TabDPT that receives a small amount of per-dataset fine-tuning (e.g., 5–10 rounds of hyperparameter search) would help bound the gap between zero-shot and tuned performance and strengthen the paper's argument.
- Providing training hyperparameters (optimizer, learning rate schedule, batch size) would aid reproducibility, though the model weights will be released.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Abstract may imply dominance across all metrics."** The abstract claims "state-of-the-art performance" on CC18 and CTR23. TabDPT is best on 3 of 4 metrics and statistically tied on the 4th (accuracy, overlapping CIs with TabR). This characterization is factually accurate; the criticism is overly pedantic.

2. **"TabPFN not in win-rate/Elo analysis."** The win-rate analysis (Section 5.1) is explicitly scoped to compare with Tabula-8B (an LLM-based approach). TabPFN is a different class of ICL model without HPO, and its exclusion from a specific analysis focused on LLM comparison is a deliberate design choice, not an omission.

3. **"Tabula-8B paragraph disrupts flow."** The paragraph in Section 4.1 (line 242) comparing token counts with Tabula-8B provides meaningful context about data scale. It is a presentation choice, not a substantive flaw.

4. **"Missing training hyperparameters (batch size, learning rate, optimizer, attention heads)."** Per meta-reviewer guidelines, these are treated as reproducibility nitpicks. The paper reports the key architecture details (78M parameters, 16 layers, 600K steps) and states that models and weights will be released.

## Novel Insights

The most interesting insight emerging from the reviews is that the *tension* between the paper's two main claims — (a) that real-data SSL is critical, and (b) that the evaluation benchmarks share the same source (OpenML) as the training data — creates an unresolved question about how much of the SOTA is attributable to the method vs. to dataset familiarity. The paper's contamination check was performed, but the lack of quantitative disclosure keeps this question alive. This is not a fatal flaw but is the most substantive concern a skeptical reader would have. The scaling analysis, while methodologically limited, raises the genuinely novel observation that synthetic data from the TabPFN prior plateaus for larger models while real data continues to improve — a result that, if confirmed with more data points, would have concrete implications for how the field should invest in pre-training data.

## Suggestions

1. **Add a table or paragraph disclosing the contamination check quantitatively**: number of training–evaluation pairs flagged at each stage of the pipeline, how many were removed, and how many CC18/CTR23 datasets had any metadata-level similarity to training data. This directly addresses the most significant reviewer concern.
2. **Recast the scaling-law section** as reporting trends "consistent with power-law scaling" rather than a validated law. Add confidence intervals for the exponents and, if feasible, a leave-one-out robustness check.
3. **Report the absolute performance of the base model** in the ablation figure or caption so that the reduction bars are interpretable.

## Score and Decision

The paper makes a genuine contribution: it demonstrates that ICL with SSL on real data can produce a tabular foundation model competitive with thoroughly tuned per-dataset methods, at a fraction of the inference cost. The experimental design is generally sound, the baselines are strong and contemporary, and the release of code and weights will benefit the community. The two main weaknesses — underreported contamination analysis and overclaimed scaling law — are addressable and do not undermine the core contribution. I assess the paper as solidly above the acceptance threshold.

Score: 7.0 (clear accept)

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
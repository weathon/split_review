- Decision: Reject
- Avg Score: 4.60
- Scores: 3, 6, 6, 3, 5
Now I have all the information I need to write the consolidated review.

## Summary

This paper introduces the concept of partial channel dependence (PCD) for time series models, operationalized via a channel mask (CM) that combines a dataset-level correlation matrix with learned domain parameters (α, β). The mask is applied element-wise to the attention matrix of Transformer-based architectures, enabling a flexible middle ground between channel-independent (CI) and channel-dependent (CD) processing. Evaluations across forecasting, classification, imputation, and anomaly detection — using iTransformer (single-task) and UniTS (multi-task foundation model) — show that the CM consistently improves performance, with the ablation confirming both mask components are necessary. The paper also proposes a CD ratio metric to characterize dataset-specific dependence levels.

## Strengths

1. **Clean, well-motivated idea with a simple implementation.** The concept of PCD is clearly motivated (varying channel dependence across datasets is real, and prior TSFMs overlook it). The channel mask reduces to two scalar parameters (α, β) plus a precomputed correlation matrix per dataset, making it lightweight and easy to integrate into any Transformer with channel-wise attention. The framing of global (correlation-based) vs. local (attention-based) CD is intuitive and grounded.

2. **Consistent and often substantial gains across diverse settings.** On iTransformer (Table 2), CM improves MSE on all 13 forecasting datasets, with striking gains on PEMS datasets (12.7%–40.2%). On UniTS under prompt-tuning, CM improves all 20 forecasting tasks and 18 classification tasks (Table 3, Table 1 summary). Few-shot and zero-shot settings also show consistent gains. The breadth of the evaluation across four tasks and multiple regimes is a genuine strength.

3. **Ablation and diagnostic analyses convincingly isolate the mechanism.** Table 5 (ablation) shows that using only the correlation matrix or only domain parameters underperforms the combined mask. Table 11 (domain parameter extensions) shows that the simple scalar α,β outperforms more complex vector/matrix parameterizations, confirming that the correlation structure — not just added capacity — drives the gains. The metric comparison (Table 8) shows correlation-based CMs outperform those based on Euclidean distance, cosine similarity, or DTW.

4. **The CD ratio is a useful diagnostic.** The proposed CD ratio provides a quantitative way to characterize dataset-specific dependence. The correlation between CD ratio and performance gain of CD over CI (Figure 3) supports the paper's motivating claim and offers a practical tool for deciding when PCD will help.

5. **Efficiency and robustness are well-demonstrated.** The overhead is minimal (~2–3 sec/epoch extra training, <1 ms extra inference, Table 10). Robustness to missing values up to 75% (Figure 6) and the global+local CD ablation (Table 9) further strengthen the practical case.

## Weaknesses

### Fatal
None.

### Major

1. **Missing comparisons with other time-series foundation models.** The paper argues that prior TSFMs overlook implicit channel-dependence heterogeneity and proposes CM to address this for TSFMs. Yet the multi-task evaluation compares UniTS+CM only against UniTS and task-specific models (iTransformer, TimesNet, PatchTST, GPT4TS). Contemporaneous TSFMs (MOMENT, MOIRAI, Timer, TimesFM) are cited in related work but never included as baselines. The caption for Table 3 claims "SOTA performance," but the comparison set excludes the most relevant category of models. It is therefore unclear whether UniTS+CM is competitive with other TSFMs, or whether the CM idea applies to / benefits other TSFM architectures. Adding at least one other TSFM comparison (or a clear discussion of why it is not feasible) would substantially strengthen the paper.

2. **No statistical significance or error bars.** All results are single-run point estimates. Several gains are small (e.g., 0.3% on ETTh2, Table 2; 0.6% on ETTh1 zero-shot horizon, Table 7b). Without standard deviations over multiple seeds, it is impossible to assess whether these improvements are reliable or within noise. At minimum, the headline comparisons should report variability.

### Minor

3. **Intro overclaims the universality of gains.** The introduction (lines 86–91) states that applying CMs "yields performance gains across all 20 and 13 forecasting tasks" without qualification. However, Table 3 shows that in the **supervised** setting, several individual horizons degrade (e.g., ETTh1 H=192: UniTS+CM 0.438 vs. UniTS 0.428; ETTh1 H=336: 0.478 vs. 0.462). The table caption correctly clarifies that "all 20" refers to the prompt-tuning setting, but the intro does not carry this qualification. The claim should be bounded to the setting where it holds.

4. **Zero-shot domain parameter selection is ad-hoc.** For unseen datasets, the method requires heuristics (averaging parameters from training datasets or selecting the closest by correlation). The paper acknowledges this and shows the heuristics work, which is good. However, the method is described as "plug-and-play" (lines 87, 1048), which is misleading if deployment on a truly novel dataset requires manual heuristic selection or fine-tuning. A more precise framing would be that the CM is architecture-plug-and-play but dataset-specific for optimal results.

5. **Masked channel prediction experiment only on iTransformer, not UniTS.** The masked channel prediction diagnostic (Table 9) is a clever test of whether the model captures channel dependence, but it is only run on iTransformer, not on the foundation model UniTS. Since the paper's main TSFM claim rests on UniTS, this diagnostic should be extended.

### Trivial

6. **The CD-ratio to performance-gain correlation (Figure 3) is reported only qualitatively.** The paper states the gain "is highly correlated with the CD ratio" but provides no numerical correlation coefficient. Reporting Pearson's r or Spearman's ρ would strengthen this claim.

## Nice-to-Haves
- Causal validation: perturbing the correlation matrix (e.g., shuffling rows/columns) and showing performance degrades would more directly tie the gains to the correlation structure.
- Implementation details: specifying which attention layers in UniTS are modified (temporal vs. channel attention) would aid reproducibility.

## Removed Points
*These points are flagged to be removed; treat them with caution.*
1. "No direct evidence the mask's structure causes improvement" — The paper already provides extensive evidence: ablation (Table 5) isolating correlation + domain parameters, metric comparison (Table 8) showing correlation outperforms other statistics, and domain-parameter extensions (Table 11) showing scalar α,β outperform fully learned matrices. This concern is substantially addressed.
2. "Parameters comparison with GPT4TS is misleading" — The comparison (164.5M vs 1.57M) is a factual statement showing efficiency; it is not misleading. The paper is comparing against a published baseline.
3. "No discussion of near-zero correlation or numerical stability" — These are speculative concerns about edge cases, not concrete problems visible in the paper.
4. "Missing related work" — The paper cites MOMENT, MOIRAI, and Timer in its related work section.
5. Formatting and presentation nitpicks.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Bound the "consistent gains" claim in the abstract/intro to the experimental conditions where it strictly holds (prompt-tuning for forecasting, noting that supervised shows average improvement but some individual settings degrade).
2. Add at least one TSFM baseline (e.g., MOMENT or MOIRAI) to the main forecasting table, or clearly discuss why such comparison is infeasible (different APIs, training frameworks) and temper the SOTA claim accordingly.
3. Report standard deviations over 3–5 seeds for the main results, especially for datasets with small gains.
4. Extend the masked channel prediction diagnostic to UniTS to strengthen the claim that CM helps TSFMs capture channel dependence.
5. Add a numerical correlation coefficient (Spearman/Pearson) to the CD-ratio vs. gain analysis.
6. Clarify the "plug-and-play" claim: the CM is architecture-plug-and-play but requires dataset-specific learning of α,β; zero-shot deployment works via heuristics but is not parameter-free.

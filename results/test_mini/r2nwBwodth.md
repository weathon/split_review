Now I have all the evidence I need. Let me produce the final consolidated review.

## Summary

The paper introduces PFML (Prediction of Functionals from Masked Latents), a self-supervised learning method for time-series data. Instead of reconstructing raw signals (as in MAE) or learned targets (as in data2vec), PFML predicts precomputed statistical functionals (mean, variance, skewness, kurtosis, ZCR, ACF statistics) of masked latent embeddings. The core argument is that this objective inherently avoids representation collapse because the functional targets retain variance as long as the input varies — a claim supported by clean theoretical reasoning and demonstrated empirically across 30 pre-training runs (0 collapses for PFML vs. 26/30 for data2vec). The method is evaluated on five clinically relevant classification tasks across three modalities (multi-channel IMU, speech, single-channel EEG), showing superior results to MAE and competitive results with data2vec.

## Strengths

1. **Novel and well-motivated SSL objective.** Predicting statistical functionals rather than raw signals or learned targets is a genuinely new idea in the time-series SSL literature. The paper provides clean theoretical reasoning (Assumptions 1 and 2) for why this objective avoids representation collapse, and the empirical evidence (0/30 collapse rate for PFML vs. 26/30 for data2vec in Table 3) directly validates the theory. This is the paper's strongest contribution.

2. **Convincing empirical demonstration of collapse avoidance.** Across 10 runs each on three distinct modalities, PFML never experienced representation collapse, while data2vec collapsed in 7/10 (IMU), 9/10 (speech), and 10/10 (EEG) runs. This is a striking result and directly supports the paper's central claim.

3. **Competitive downstream performance across three real-world modalities.** PFML outperforms MAE on all five classification tasks and matches or exceeds data2vec on most, notably achieving 78.4% UAF1 on sleep stage classification vs. data2vec's 75.7% and MAE's 76.7% (Table 1). The evaluation covers clinically relevant tasks (infant posture/movement, emotion recognition, sleep staging), demonstrating generality.

4. **Conceptual and practical simplicity.** PFML uses fixed, precomputed functionals and a straightforward MSE loss, requiring neither the complex target construction (moving average teacher, layer normalization) of data2vec nor the contrastive sampling of many SSL methods. The paper explicitly aims for a method that is "straightforwardly applicable to different time-series data domains," and the simplicity of the approach supports this goal.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **No variance or statistical significance reporting for downstream results.** All fine-tuning and linear evaluation results in Tables 1 and 2 are presented as single numbers. The paper uses cross-validation (10-fold for IMU and EEG), and reports that scores are computed from aggregate confusion matrices, but never reports per-fold variability, standard deviations, or confidence intervals. Given that some comparisons are close (e.g., posture classification), readers cannot assess whether differences are reliable. This is the single most actionable weakness — straightforward to fix and would substantially strengthen the paper.

2. **Missing hyperparameter specifications.** The method description and experiments do not report several hyperparameters that would be needed for faithful reproduction: the number of Transformer encoder blocks \(T\), initial learning rate, batch size, exact values of \(p_m\) and \(l_m\) used for each dataset, dropout rates in the temporal model, and the number of pre-training epochs. The paper states "minimal hyperparameter optimization" was used, but without reporting the actual values used, this claim cannot be evaluated.

3. **Ablation studies described qualitatively without tabular results.** The additional hyperparameter experiments (Section 4.4) on masking strategies, functional ablation, and mask type are described only in text — no tables or quantitative results are provided. For example, "it is more beneficial to mask embeddings" and "using the full set of 11 functionals provides the best outcome" are claims supported only by qualitative description. Given that the paper's supplementary experiments are limited, this makes key design decisions harder to verify.

4. **data2vec performance on EEG warrants further investigation.** PFML and MAE both outperform data2vec "by a large margin" on sleep stage classification (Table 1), while data2vec collapsed in 10/10 pre-training runs on EEG (Table 3). The paper notes they used "the best hyperparameter combinations for each SSL method" and the same model architecture, but data2vec's complete collapse on EEG suggests its hyperparameters (e.g., EMA decay, target normalization) may not be well-suited to this modality. This does not invalidate PFML's contribution (PFML's robustness is the point) but the claim of being "competitive with the state-of-the-art" is weaker if the comparison method was operating in an unfavorable regime.

### Trivial
None.

## Nice-to-Haves
- Reporting per-fold scores (e.g., box plots or standard deviations) for the cross-validation results.
- Providing the hyperparameter values (learning rate, batch size, \(T\), \(p_m\), \(l_m\)) in a supplementary table.
- Adding quantitative results tables for the ablation experiments in Section 4.4.
- A correlation analysis of the 11 functionals on each dataset to quantify potential redundancy.
- Investigating whether a wider range of data2vec hyperparameters (especially EMA decay) improves its EEG performance.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Missing baseline: using functionals directly as features (from Harsh Critic).** The reviewer argues PFML should be compared against a model that uses the 11 functionals as input features. This misunderstands the paper's contribution: PFML's claim is that *predicting* functionals is a better SSL objective than predicting raw signals (MAE) or learned targets (data2vec). The "functionals as features" baseline tests feature engineering vs. representation learning, not the SSL objective. The paper already controls for this via the "no pre-training" baseline (chance-level performance) and the MAE comparison (same architecture, different targets). The comparison against MAE specifically isolates the benefit of predicting functionals over raw signals.
- **Questioning existence of cited references or tools.** None present in this review.
- **Formatting/style nitpicks.** None present in this review.
- **Strawman weaknesses.** The claim that PFML is not novel because "autoencoding is established" is not raised by the reviewers and would be incorrect — PFML's novelty is its use of functionals as prediction targets, not the autoencoding framework.
- **Generic strengths from Strength Finder** were filtered; only specific, evidenced strengths are retained above.

## Novel Insights

A genuinely interesting observation emerges from this paper that goes beyond its own contributions: the dramatic collapse rate difference between data2vec (26/30) and methods with data-dependent targets (PFML 0/30, MAE 1/30) suggests that the choice of training target — specifically, whether the target variance is *guaranteed* by the data itself or is *learned* — is the single most important design decision for collapse-avoiding SSL in time series. The paper's theoretical argument (functionals with data-dependent variance → no collapse) is simple but the empirical contrast is stark. This reframes the SSL design space for time series: rather than asking how to *prevent* collapse with regularization (VICReg, BYOL's predictor, data2vec's normalization), one can ask how to *engineer the targets* so collapse is structurally impossible. This insight could inspire a new family of SSL methods where targets are chosen specifically for their variance-preserving properties rather than for their informativeness.

## Suggestions

1. **Add variance reporting** (standard deviations or per-fold scores) to Tables 1 and 2. This is the single most impactful improvement — it would convert qualitative "competitive" claims into statistically grounded ones.
2. **Provide a supplementary table** listing all hyperparameter values used for each dataset and each SSL method, including learning rate, batch size, \(T\), \(p_m\), \(l_m\), dropout rates, and number of pre-training epochs.
3. **Convert the qualitative ablation descriptions** in Section 4.4 into quantitative tables or figures. The masking strategy, functional ablation, and mask type experiments are valuable but currently unverifiable from the text alone.
4. **Investigate data2vec on EEG more thoroughly** — if data2vec can achieve competitive performance with better-adapted hyperparameters, this context would strengthen the paper by providing a fairer comparison; if not, it would further reinforce PFML's robustness advantage.

## Score and Decision

### Calibration Anchors

- **xJ5CF1aOOX** (avg 2.50): A self-supervised pre-training model for time series classification with poor writing, unclear contribution, and shallow experiments. PFML is substantially stronger — clearer writing, better-motivated contribution, and more thorough evaluation.
- **V8YwPdoSlr / CHRONOS** (avg 3.50): SSL for ECG time-series with unclear method and insufficient related work. PFML is clearly stronger — tests on three modalities vs. one, has a cleaner theoretical argument, and directly addresses a well-defined problem (representation collapse).
- **nphsoKxlFs / DynaCL** (avg 4.00): Contrastive SSL for time series with temporal adjacent sampling. PFML has a more novel core idea (functionals as targets) and stronger collapse-avoidance evidence, though DynaCL's experiments are broader.
- **WS7GuBDFa2 / PITS** (avg 6.25): Masked time-series modeling with patch-independent embedding. Comparable quality — PITS has more extensive experiments and clearer reporting, while PFML has a more novel SSL objective and stronger collapse evidence. PFML is slightly weaker on presentation rigor.
- **pAsQSWlDUf / SoftCLT** (avg 6.50): Soft contrastive learning for time series. Stronger than PFML overall — clearer writing, more thorough ablations, more comprehensive experimental validation. PFML's core idea is arguably more novel, but the execution is less polished.
- **8zJRon6k5v / ACSSM** (avg 8.00): Amortized control of continuous state space model for irregular time series. Significantly stronger — deeper theoretical contribution, more rigorous experiments, cleaner presentation. PFML is not at this level.
- **1CLzLXSFNn / TimeMixer++** (avg 8.00): General time series pattern machine. Much broader in scope with extensive benchmarks. PFML is more narrowly focused and does not match this breadth.

Relative to the calibration set, PFML sits below the strong-accept papers (6.5+) due to missing variance reporting and hyperparameter details, but above the weak papers (4.0-) due to a genuinely novel contribution and solid multi-modal evaluation. It is most comparable to the ~5–6 range papers like PITS and DynaCL.

MY FINAL SCORE: 5.5
MY FINAL DECISION: Reject
Now I have all the information needed. Let me write the consolidated review by carefully verifying each claim against the paper.

---

## Summary

This paper proposes PFML (Prediction of Functionals from Masked Latents), a self-supervised learning method for time-series data that replaces raw-signal reconstruction with prediction of statistical functionals (mean, variance, zero-crossing rate, etc.) of masked latent embeddings. The core claim is that this objective inherently avoids representation collapse without requiring special countermeasures like EMA teachers or contrastive sampling. PFML is evaluated on five classification tasks across IMU, speech, and EEG data, compared against MAE and data2vec.

## Strengths

1. **Inherent avoidance of representation collapse by design, empirically validated**. The paper provides a clear theoretical argument (Assumptions 1–2, Section 3.2): if input frames exhibit temporal variance, the functional targets also vary, so a collapsing constant output would incur high loss. This is not just hand-waving — it is backed by 30 pre-training runs (10 per modality) where PFML suffered zero collapses, while data2vec collapsed in 8–10/10 runs (Table 3). This is a directly measured advantage over a leading modality-agnostic SSL method.

2. **Competitive performance across multiple real-world modalities**. PFML is evaluated on five classification tasks spanning three data modalities (IMU, speech, EEG). On sleep stage classification from EEG, PFML and MAE substantially outperform data2vec. On IMU posture/movement and speech emotion, PFML matches data2vec and clearly beats MAE (Table 1). The breadth of evaluation strengthens the claim of cross-modal applicability.

3. **Conceptually simpler than the state-of-the-art comparator**. PFML requires no contrastive sampling, no clustering, no moving-average teacher network, no target normalization schemes, and no layer-averaged targets. The functional set is fixed at 11 operations across all experiments. This simplicity is a genuine practical advantage for researchers applying SSL to novel time-series domains.

4. **Linear evaluation confirms feature quality**. Frozen PFML features consistently outperform MAE and are competitive with data2vec when used with only a linear classifier (Table 2), while a randomly initialized model yields chance-level accuracy. This rules out the possibility that PFML's fine-tuning success is driven by the downstream classifier adapting to degenerate features.

5. **Systematic hyperparameter analysis validates key design choices**. The paper explores masking strategies (input vs. embedding), mask probability/length, functional set size, and mask token types (Section 4.5). For example, discarding functionals degrades performance, confirming that richer targets improve learning, and embedding masking outperforms input masking. These experiments strengthen confidence that the specific design choices are principled, not arbitrary.

6. **Resource-conscious and reproducible**. The authors deliberately run pre-training on a single GPU with small minibatches, providing architecture details and hyperparameters that are directly usable (Limitations). This contrasts with many SSL methods that require large-scale distributed training and makes PFML accessible to labs with limited computational resources.

## Weaknesses

### Fatal

None.

### Major

1. **Fine-tuning results lack uncertainty quantification across multiple seeds, weakening the headline comparative claims.** The fine-tuning results in Table 1 and linear evaluation in Table 2 report a single performance number per method per task. For IMU and EEG, 10-fold cross-validation at the recording/subject level is used (final score from an aggregate confusion matrix across folds), and for speech a single train/val/test split is used. However, in no case are the results reported across multiple random seeds for pre-training or fine-tuning initialization. The paper stakes strong comparative claims ("PFML is superior to MAE" and "competitive against data2vec") on these numbers, yet the reader cannot judge whether the observed differences are robust or within noise. The collapse experiments *do* run pre-training 10 times (Table 3), which shows the authors appreciate the importance of multiple runs, but those runs are never linked to the fine-tuning results — we do not know whether the fine-tuned models come from a single seed, the best of 10, or an average. Since data2vec collapses in 50–80% of runs for IMU and speech, the reported data2vec performance may come from the few runs that did not collapse, potentially biasing the comparison in its favor in those modalities (while the EEG results, where data2vec collapsed in all 10 runs, would not be affected). This is not a fatal flaw — the cross-validation structure provides *some* robustness — but it substantially weakens the credibility of the central comparative claims as currently presented.

### Minor

2. **The representation collapse detection criterion, while empirically motivated, would benefit from more transparent justification and visualization.** The paper defines collapse as variance of embeddings or outputs falling below 0.01 for 10 consecutive epochs *while validation loss decreases* (Section 4). The reviewer's concern about the loss simultaneously decreasing during variance drop is reasonable — the paper states this was found to be "a good indicator of an upcoming representation collapse" in preliminary experiments, but does not explain the mechanism or show supporting plots. Additionally, the paper examines only variance-based collapse detection and does not discuss dimensional collapse (where variance is preserved but feature dimensions become correlated) or rank collapse in Transformer outputs. Given that the paper's main selling point is avoiding collapse, a simple qualitative plot of output variance vs. training epoch for PFML and data2vec would significantly strengthen this evidence. The zero-collapse rate across 30 runs remains compelling empirical evidence even without this addition, so this is a presentation gap rather than a structural flaw.

3. **The MAE baseline is a modified version (embedding masking rather than input masking), making the "superior to MAE" claim less direct than stated.** The paper transparently acknowledges this modification (Section 4, line 92): "In order to make the prediction of functionals directly comparable with predicting the input signal, we use a slightly modified version of MAE where we mask embeddings instead of masking inputs." However, the conclusion remains phrased as "PFML is superior to a conceptually similar pre-existing SSL method, MAE" (abstract, conclusion). This is somewhat imprecise — PFML is compared against a modified MAE, not the original algorithm. The paper's own hyperparameter experiments (Section 4.5) show that embedding masking outperforms input masking for PFML, so if the same holds for MAE, the comparison might actually *favor* the baseline (embedding-masking MAE would be a stronger baseline than input-masking MAE). The direction of bias is unclear. A clean solution would be to either add original-MAE results as an additional baseline or rephrase the claim to "superior to a variant of MAE adapted for comparable evaluation." This does not invalidate the contribution but warrants clarification.

### Trivial

- The paper uses "superiority... in terms of representation collapse" (line 104) when comparing PFML against data2vec on collapse frequency — this conflates "avoiding collapse" with "superiority," which are distinct qualities. The collapse results show PFML avoids what data2vec suffers from, which is an advantage, not superiority in a general sense.

- The paper reports that for the one MAE collapse, "the model loss started diverging from the beginning of the pre-training process" (line 157), which arguably is not representation collapse in the standard sense (convergence to constant output) but a failure to converge at all. This detail is inconsistent with the collapse definition and should be clarified.

## Nice-to-Haves

- **Multiple seeded fine-tuning trials**: Even 3–5 random seeds per method per task would substantially strengthen the evidence. Reporting means and standard deviations (or at least best/median) would allow readers to assess the robustness of the reported differences.
- **Visualization of output variance over training epochs**: A simple plot showing PFML maintaining output variance while data2vec's variance collapses during pre-training would make the collapse-avoidance claim immediately transparent and remove the need to reason about the loss/variance criterion.
- **Original MAE (input-masking) baseline**: Adding this as a supplementary comparison would clean up the "superior to MAE" claim, or alternatively, the paper could explicitly note this limitation.
- **Statistical comparisons**: A statement like "PFML outperformed MAE in 4 of 5 tasks with >2% absolute F1 difference" would help readers interpret significance absent error bars.

## Removed Points

- **Reviewer's concern that collapse definition is "puzzling" because loss shouldn't decrease when outputs become constant**: This criticism misunderstands the paper's empirically derived detection criterion. The paper states this was found in *preliminary experiments* to be a reliable indicator of upcoming collapse, not a theoretical claim about loss dynamics during collapse. Moreover, the zero-collapse empirical result (30 runs) stands independently of the detection mechanism's causal explanation. Kept in Minor #2 at reduced severity.

- **Reviewer's claim that threshold 0.01 is "arbitrary and dataset-dependent"**: The paper computes functionals from z-score normalized signals (line 94), making the 0.01 threshold meaningful as a fraction of unit variance. The reviewer provides no evidence that this threshold would misclassify collapse across the three modalities. Kept only as part of Minor #2's request for visualization.

- **Reviewer's "Other Observations" about hyperparameter experiments being limited to select tasks**: This is a scope-appropriate design choice for a hyperparameter ablation and does not constitute a weakness. Moved here.

- **Reviewer's comment about "simplicity claim should acknowledge functional selection burden"**: The paper already acknowledges this in Limitations (Section 5, line 176): "carefully selecting the number and type of functionals specifically for different modalities may lead to better results." Moved here.

## Novel Insights

None beyond the paper's own contributions. The reviews identify important methodological gaps but do not surface new technical insights about the method itself.

## Suggestions

1. **Add multiple seeded fine-tuning runs** (even 3–5 per method per task) and report means with standard deviations or range. This is the single most impactful improvement: it directly addresses the weakest link in the evidence chain for the paper's headline claims.
2. **Add a qualitative plot** showing output variance and validation loss over training epochs for PFML and data2vec across one representative modality. This would make the collapse-avoidance claim transparent and visual.
3. **Clarify the MAE comparison**: either add original (input-masking) MAE results as a supplementary baseline, or revise the claim to explicitly note that the comparison is against an embedding-masking variant of MAE.
4. **Tighten the language on the "superior to MAE" claim** to reflect the modification transparently described in the methodology.

## Score and Decision

This paper proposes a novel and conceptually appealing SSL method for time-series data with a strong theoretical motivation for collapse avoidance and credible empirical evidence across three modalities. The main weaknesses are (a) the lack of uncertainty quantification for fine-tuning results, which tempers the strength of the comparative claims, and (b) several presentation gaps in the collapse analysis. However, no weakness is fatal — the core contribution is original, the experiments cover meaningful breadth, and the collapse-avoidance advantage over data2vec is convincingly demonstrated (30 runs, zero collapses). The paper would be strengthened substantially by adding multiple seeded fine-tuning runs, but its current contribution stands as a solid empirical paper with a clear, useful idea. I recommend acceptance.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
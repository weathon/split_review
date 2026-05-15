Now I have a thorough understanding of the paper and the calibration anchors. Let me synthesize the final review.

---

## Summary

DGNet proposes a self-supervised learning framework for EEG-based dementia classification that decomposes EEG signals into five canonical frequency bands (δ, θ, α, β, γ), processes each with independent CNN encoders and adaptive-temperature SimCLR projection heads, and fine-tunes on limited labeled data. Evaluated on 65 subjects (AD vs. CN) under leave-one-subject-out cross-validation, the model achieves 92.90% accuracy, with ablation studies showing substantial contributions from each component. The multi-band design is neurophysiologically well-motivated and the ablation evidence is clear, but the evaluation is limited to a single small dataset and several methodological details are under-specified.

## Strengths

- **Neurophysiologically grounded multi-band design**: The decomposition into five standard EEG frequency bands, each with independent encoders and projection heads, directly leverages known dementia-related spectral signatures (increased δ/θ, decreased α/β/γ). The ablation shows this matters: single-head drops accuracy from 92.90% to 73.52%, and the 5-head version without full SSL still reaches 79.55%, confirming band-specific encoding adds value beyond raw capacity (Table 3).

- **Clear and informative ablation study**: The ablation (Table 3) systematically removes self-supervision (→63.35%), multi-band heads (→73.52% single-head, →79.55% multi-head without adaptive temp), data augmentation, adaptive temperature, and regularization, with each removal producing a measurable accuracy drop. This isolates the contribution of each design choice.

- **Adaptive-temperature contrastive learning is effective for EEG**: Incorporating learnable per-band temperatures with regularization into the NT-Xent loss yields clear gains: fixing τ = 0.1 drops accuracy to 86.53%, and removing regularization drops it to 90.64% (Table 3). This demonstrates that SSL tailoring beyond off-the-shelf SimCLR benefits EEG representation learning.

- **Subject-independent evaluation**: LOSO cross-validation is the appropriate protocol for clinical EEG, preventing subject-level data leakage. The model achieves strong performance under this rigorous regime.

## Weaknesses

### Fatal

None.

### Major

- **Evaluation limited to a single small dataset**: All experiments use one dataset of 65 subjects (AD vs. CN) from a single hospital. While the results are promising, no cross-dataset or cross-site validation is provided. This limits confidence in generalizability for a method positioned as a screening tool. A second dataset, even a small one, would substantially strengthen the contribution.

- **SSL pre-training protocol within LOSO is not specified**: The paper states LOSO is used for linear evaluation, but does not clarify whether SSL pre-training was also performed within each LOSO fold (i.e., pre-trained on 64 subjects, evaluated on the held-out 65th) or performed once on the entire dataset. If pre-training was done once on all 65 subjects, the test subjects' data would have been seen during pre-training in each fold, constituting leakage. This ambiguity undermines trust in the reported performance.

### Minor

- **No variability measures reported**: The paper reports single-point accuracy and F1 scores for the proposed method across all tables, while the closest competitor (BI-MCGNN, Table 2) reports 91.25 ± 0.38. Without standard deviations across LOSO folds, the 1.65-point lead over BI-MCGNN is difficult to interpret. Reporting per-fold statistics would strengthen the claims.

- **Ambiguous comparison protocol in Table 2**: The text states "all models were evaluated using strict LOSO cross-validation" but the table cites published papers from 2023–2025. It is unclear whether the authors re-ran these methods under identical conditions or are comparing against numbers from the literature that may have used different preprocessing, segmentation, or subject inclusion criteria. This weakens the claimed superiority over prior work.

- **"w/o augmentation" ablation conflates two variables**: The ablation replaces contrastive learning with MSE reconstruction when removing augmentation (Table 3). This changes both the SSL objective and the presence of augmentation simultaneously, preventing isolation of augmentation's specific contribution. A fairer ablation would keep the contrastive objective while removing augmentations.

- **No ablation varying the number of bands**: The paper claims the 5-band decomposition is important, but does not compare against, e.g., a 3-band split or a single-band model with equivalent total capacity. This would help distinguish the benefit of the specific band decomposition from simply having more parameters.

### Trivial

- The notation "[5, 128-dimensional] embedding" (Section 2.1) is awkwardly phrased; the intended meaning (5 vectors of 128 dimensions each) is recoverable but the presentation could be clearer.

- Figure 3 (spectrogram visualization of embeddings) is not explained: how a 128-dimensional embedding vector is transformed into a spectrogram is not described, making the figure uninformative as presented.

- The paper does not state whether the 23 FTD subjects were used for SSL pre-training (unlabeled), which would give the model access to 88 subjects rather than 65 during pre-training. This should be disclosed.

## Nice-to-Haves

- A within-fold SSL pre-training verification experiment (e.g., subject-level cluster purity of learned representations) would address leakage concerns.
- Clinical validation of learned representations against known dementia spectral signatures (e.g., showing the model actually captures increased δ/θ and decreased α/β/γ in AD).
- Comparison with a supervised baseline using the same architecture and augmentations to disentangle SSL benefit from augmentation benefit alone.
- Evaluation on a second, independent dataset to establish generalizability.

## Removed Points

These points were flagged for removal; treat them with caution.

- *"Structural — Unreliable evaluation protocol given the tiny dataset, and complete absence of variability measures... invalidates the headline quantitative claims by itself."* — The claim that the evaluation is fundamentally "unreliable" and that missing SDs "invalidate" all claims is excessive. LOSO is a well-established, rigorous protocol; the absence of SDs is a presentation weakness (moved to Minor) but does not invalidate the results. The paper's core ablation results (which are comparative within the same protocol) remain informative even without per-fold SDs.

- *"Suspiciously large gap between SSL and full-supervision that is not accounted for... raises serious concern about data leakage or overfitting."* — A 29-point gap between SSL and training-from-scratch on a 65-subject dataset is large but not inherently suspicious; SSL is precisely designed to help when labeled data is scarce. The leakage concern is valid (moved to Major as a protocol clarity issue), but the framing as "extraordinary" and the implication of misconduct is unwarranted. The paper provides a genuine architectural reason for the gap (multi-band SSL pre-training vs. CNN from scratch).

- *"Low baseline accuracies (39–49%) suggest these baselines were not tuned for this small dataset."* — Many of these are standard EEG models evaluated out-of-the-box; the paper states fine-tuning was performed when pretrained weights were available. The comparison may not be perfectly fair but this is common practice. The relative gap is large enough that the qualitative conclusion (multi-band SSL outperforms standard EEG models) is robust.

- *"The paper does not describe any hyperparameter search for baselines."* — Exhaustive hyperparameter tuning of 12 baselines is impractical and not standard in this literature. Moved to removed.

- *"The framing is overwrought but does not affect the technical content."* — Pure style critique; removed.

- *Strength: "Rigorous, subject-independent evaluation"* — LOSO is good practice but the paper does not specify whether SSL pre-training follows the same fold structure, which limits how "rigorous" the evaluation can be called. Kept the LOSO strength but qualified.

- *Strength: "Strong benchmarking against recent methods... consistently outperforms them all."* — The comparison protocol is ambiguous (whether methods were re-run or numbers taken from literature). This strength is partially undermined by the protocol clarity issue. The strength is kept but the weakness is noted.

## Novel Insights

Beyond the paper's own contributions, the most interesting finding is the interaction between multi-band decomposition and contrastive learning: the ablation shows that multi-band heads alone (without SSL, 79.55%) outperform single-head with SSL (73.52%), suggesting the band decomposition may be as or more important than the SSL objective for this task. This is not explicitly discussed in the paper but emerges from comparing Table 3 rows.

## Suggestions

- Clarify whether SSL pre-training was performed within each LOSO fold or once on the full dataset. If the former, state it explicitly; if the latter, re-run the experiments with per-fold pre-training and report corrected results.
- Report mean and standard deviation of per-subject accuracy across LOSO folds for the proposed method in Tables 1–3.
- Add an ablation with a matched-capacity single-band model to isolate the benefit of band decomposition from model capacity.
- Clarify in Table 2 which results are from re-running methods vs. taken from published papers, and note any differences in protocol.
- Explain the methodology behind Figure 3 (how embeddings become spectrograms) or remove the figure if it serves no clear purpose.
- Disclose whether FTD subjects were used for SSL pre-training.

## Score and Decision

### Anchor comparison

| Anchor | Avg Score | Decision | Comparison to DGNet |
|--------|-----------|----------|---------------------|
| LEAD (KuhCUX2oIt) | 4.00 | Reject | Similar topic (EEG+AD). LEAD had larger dataset but marginal architectural gains; DGNet has clearer ablation and more focused contribution. DGNet is stronger. |
| BayesENDS (7w9GUhqSnN) | 3.20 | Reject | Similar topic (EEG+AD). BayesENDS had major evaluation gaps; DGNet's evaluation is more complete and its ablation more informative. DGNet is stronger. |
| CLIQ (rNNSuV4ZP9) | 3.00 | Reject | Both use contrastive SSL for EEG. CLIQ had weaker evaluation; DGNet's ablation study is more thorough. DGNet is stronger. |
| M-EEG (FwPbnIEGpk) | 5.50 | Reject | Dataset/benchmark paper. M-EEG contributes a major resource (6,081 patients). DGNet cannot match this scale. M-EEG is stronger. |
| ST-EEGFormer (5Xwm8e6vbh) | 5.50 | Accept (Poster) | Benchmarking paper. Exceptionally rigorous, large-scale, multi-dataset evaluation. DGNet's single-dataset evaluation is substantially weaker. ST-EEGFormer is stronger. |
| CodeBrain (msJgEkjwh5) | 5.00 | Accept (Poster) | EEG foundation model. CodeBrain has a more novel architecture; DGNet is more application-focused. Roughly comparable in contribution level, but CodeBrain has broader evaluation. |
| VISTA (IajjifoLwo) | 5.00 | Reject | EEG decoding framework. VISTA has a more methodologically novel approach. DGNet is more straightforward. Comparable evaluation scope. |

DGNet has a well-motivated method and a clear ablation study that supports its claims. However, the evaluation is limited to a single small dataset (65 subjects, one site), the SSL pre-training protocol within LOSO is ambiguous, and variability measures are absent. These issues place it above the 3–4 range (where papers had major evaluation gaps or unconvincing gains) but below the 5.5 range (where papers contributed major resources or exceptionally rigorous multi-dataset evaluation). The paper is borderline.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
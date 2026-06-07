## Summary

DGNet proposes a self-supervised multi-band EEG representation learning framework for dementia classification. The model decomposes EEG signals into five canonical frequency bands (delta through gamma), processes each band through independent CNN encoders and projection heads with per-band adaptive temperature parameters, and trains via SimCLR-style contrastive learning. Evaluated on a 88-subject AD-vs-CN classification task, the method reports 92.90% accuracy. The core architectural idea — separate encoding per frequency band with per-band adaptive temperature — is reasonably motivated by the known neurophysiology of dementia and supported by a complete ablation study.

## Strengths

1. **Systematic component-wise ablation (Table 3)**: Each design choice is independently removed — w/o SSL (63.35%→92.90%), single-head (73.52%), w/o augmentation (78.58%), constant temperature (86.53%), w/o regularization (90.64%). This gives direct quantitative evidence that the multi-band head, adaptive temperature, regularization, data augmentation, and SSL pretraining each contribute to the final performance. This level of ablation completeness is more thorough than most EEG SSL papers.

2. **Multi-band independent encoding is neurophysiologically grounded**: Processing each frequency band through a separate encoder (rather than a shared one) is well-motivated by the known dementia spectral signatures (increased delta/theta power, decreased alpha/beta/gamma power). The ablation confirms the multi-head design outperforms single-head (79.55% vs 73.52%).

3. **Leave-One-Subject-Out evaluation**: LOSO is a strong protocol for EEG that prevents subject-level train/test contamination when implemented correctly, and the paper correctly notes its importance for handling inter-individual EEG variability.

## Weaknesses

### Major

1. **Baseline models in Table 1 perform at or near chance, making the central comparison unreliable.** 
   EEGNet (46%), Deep4Net (49%), EEGInception (39%), TIDNet (44%), S-JEPA (50%), BIOT (53%), Labram (54%), and EEGConformer (57%) are all at or near chance for binary AD-vs-CN classification (50% random baseline). These are established EEG architectures. Meanwhile, Table 2 shows that *other published methods on the same dataset* achieve substantially higher performance: DICE-Net at 83.28%, MJANet at 85.23%, BI-MCGNN at 91.25%. This strongly suggests the Table 1 baselines were not properly configured, not given equivalent preprocessing, or not evaluated under the same protocol. The paper provides no explanation for this collapse. Since the paper's central claim of "significantly outperforming all comparison models" (Section 4.1) depends entirely on Table 1, the comparative evidence is compromised.

2. **Unaddressed data leakage risk between SSL pre-training and LOSO evaluation.** 
   The paper states "We perform contrastive learning on unlabeled EEG data" (Section 2) and later describes LOSO evaluation (Section 3.4), but never clarifies whether the held-out subject's unlabeled EEG data was included in SSL pre-training. If pre-training used all 88 subjects (including the test subject in each LOSO fold), the encoder has already been exposed to the test subject's data — a clear data leakage that would inflate accuracy. If pre-training is done per-fold excluding the test subject, the paper must describe how 88 separate pre-training runs were managed, which is computationally significant and unmentioned. Without clarification, this gap could invalidate the entire evaluation. The paper's own claim that LOSO "prevents data leakage between subjects" (Section 3.4) refers only to the linear evaluation stage, not the pre-training stage.

### Minor

3. **Abstract's relative improvement numbers are incorrect.** The abstract claims "31.5% relative performance improvement over training from scratch" and "25.4% improvement over the single-head approach." From Table 3: (92.90 − 63.35) / 63.35 = **46.6%** (not 31.5%), and (92.90 − 73.52) / 73.52 = **26.4%** (not 25.4%). The 31.5% figure is off by 15 percentage points. The 25.4% vs 26.4% discrepancy is small, but the 31.5% error is a significant arithmetic mistake in the headline quantitative claim.

4. **No FTD results despite dataset containing three classes and paper framing promising "Dementia Classification."** The dataset includes AD (36), FTD (23), and CN (29) subjects, yet all experiments are AD vs CN only. Frontotemporal dementia is a major dementia subtype. Including FTD-vs-CN or three-way classification would demonstrate broader clinical relevance and help validate that the learned representations capture dementia-relevant (not AD-specific) patterns.

5. **Incorrect description of "linear evaluation" in Section 2.1.** The text states that in linear evaluation "all parameters of the model including those of the encoder are updated during training," which contradicts the standard SSL definition (frozen encoder, only classifier trained). The experimental section correctly uses frozen weights, but this inconsistency signals confusion about a core evaluation concept.

6. **No confidence intervals or variance reported.** With 88 subjects in LOSO and binary classification, a single subject accounts for ~1.14 percentage points. Reporting 92.90% without any variance measure (binomial CI, per-subject accuracy distribution) gives a misleading impression of precision.

### Trivial

7. Architecture dimensions (32→64→128 channels, 128-dim embeddings) are stated without justification or ablation.

## Nice-to-Haves

- Statistical significance testing (e.g., McNemar test) comparing DGNet to the best-performing baseline would strengthen the claims.
- Per-band contribution analysis (which frequency bands drive classification performance) would further validate the paper's central architectural innovation.
- Reporting whether the model generalizes to the FTD class would substantially broaden the clinical relevance.

## Removed Points

The following points from the harsh critic or strength finder were excluded:

- *"Abstract/Introduction is disproportionately long"* — Style nitpick about motivational writing.
- *"Equation 1 does not resemble NT-Xent"* — The paper presents Eq. 1 as the proposed adaptive variant and Eq. 2 as the standard NT-Xent for reference. The distinction is clear enough despite notational density.
- *"No code or reproducibility details"* — The parser strips appendices; code release statements may exist in the original submission.
- *"Missing related works"* — Cannot verify completeness without external search; may cause hallucination.
- *"Formatting/typo issues"* — Parser artifacts, not author errors.
- *"The ablation components interact in non-additive ways"* — This is an observation, not a flaw. Non-additive interactions are expected in complex systems.
- *"Section 2.1 describes two approaches but only one is used"* — The paper can mention alternatives without implementing them; this is not a weakness.
- *"Multi-head (5 heads) at 79.55% is substantially lower than expected"* — This is an interpretation issue, not a methodological flaw. The ablation is correctly structured.

## Novel Insights

None beyond the paper's own contributions. The key observation that per-band independent encoders with adaptive temperature parameters improve over both single-head and non-adaptive variants is the paper's core finding and is adequately demonstrated by the ablation.

## Suggestions

1. Fix the abstract's relative improvement numbers to match Table 3.
2. Clarify the SSL pre-training / LOSO interaction: explicitly state whether held-out subjects are excluded from pre-training in each fold, and if so, how the 88 pre-training runs were managed.
3. Investigate and report why established baseline architectures (EEGNet, Deep4Net, EEGInception, etc.) perform at or near chance on this dataset under the reported protocol. Without this, Table 1 cannot be interpreted.
4. Report at minimum AD-vs-FTD and three-way classification results using the FTD subjects already available in the dataset.
5. Add per-subject accuracy distributions or binomial confidence intervals for all LOSO results.

## Score and Decision

**Calibration anchors used (all rounds):**

| Path | Score | Round | Comparison |
|------|-------|-------|------------|
| TkbjqexD8w.md | 3.00 | R1 | Weaker novelty, but evaluation issues less severe than the paper under review |
| 6uReXuDWrw.md | 2.00 | R1 | UniEEG — limited scope, well below this paper |
| PcE0yAGAGW.md | 2.20 | R1 | FSL-MIC — limited contributions |
| g3PuaFh5vV.md | 2.50 | R1 | Neural decoding — better rigor but different area |
| xJ5CF1aOOX.md | 2.50 | R1 | Time series SSL — generic |
| dhLIno8FmH.md | 6.75 | R1 | Strong EEG paper with clean evaluation; paper under review is much weaker |
| IAFStwZPNu.md | 5.67 | R1 | Speech decoding from MEG — stronger evaluation |
| V5Zn0VVvBE.md | 5.40 | R1 | ST-EEGFormer — rejected for limited novelty, not evaluation issues; paper under review has better novelty but worse evaluation |
| V5lBNcD65H.md | 4.75 | R1 | MTEEG — similar evaluation concerns, slightly higher due to multi-dataset eval |
| YKfJFTiRz8.md | 5.00 | R1/2 | EEG graph SSL — stronger multi-dataset evaluation |
| KO09K3rBSr.md | 4.80 | R1 | MUSE — contrastive EEG, similar quality issues |
| ul6EYKM1Kv.md | 4.50 | R2 | Cognition-supervised EEG — comparable evaluation concerns (scores: 3,6,6,3) |
| wJ6Bx1IYrQ.md | 4.00 | R2 | EEGPT — large-scale but evaluation design issues |
| tWNHQq7gZX.md | 5.00 | R2 | Sleep decoder — well-executed |
| tfTGSm31F7.md | 4.00 | R2 | EpilepsyFM — single-domain focus |

**Bracket determination**: R1 bracketing placed the paper in 3.5–7.5. R2 narrowing with four additional anchor papers showed the paper sits below the ~4.5 line due to structural evaluation problems (baseline collapse, data leakage risk) that are more severe than those in the 4.5–5.0 range papers. Closest comparable: ul6EYKM1Kv (4.50) and wJ6Bx1IYrQ (4.00), both rejected. The paper has better architectural novelty than these comparables, but worse evaluation integrity. Score is calibrated to 3.5.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>
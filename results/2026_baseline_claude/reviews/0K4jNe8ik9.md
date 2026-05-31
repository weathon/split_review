## Summary

DGNet (Delta2Gamma Network) is a self-supervised EEG representation learning framework for dementia classification that decomposes EEG signals into five canonical frequency bands (δ, θ, α, β, γ) and applies independent CNN encoders with separate SimCLR projection heads to each band. The approach uses an adaptive NT-Xent contrastive loss with learnable per-band temperature parameters and regularization. Evaluated on an 88-subject dataset under LOSO cross-validation, the model reports 92.90% accuracy and 92.85% F1-score for AD vs. CN binary classification.

---

## Strengths

- **Neurophysiologically grounded design**: The decomposition into five canonical EEG frequency bands is directly motivated by established spectral biomarkers of AD (delta/theta power increase, alpha/beta/gamma power decrease), making the multi-head architecture a principled rather than arbitrary design choice.
- **Systematic ablation study**: Table 3 isolates the contribution of SSL pre-training, multi-head design, augmentation, adaptive temperature, and regularization, demonstrating that each component adds measurable value.
- **Competitive LOSO results**: The proposed method achieves 92.90% accuracy under strict LOSO cross-validation, outperforming several recent domain-specific methods (DICE-Net, MJANet, Dual-Branch) on the same dataset.

---

## Weaknesses

### Fatal
None definitively fatal, but the methodological concern below is critical and must be addressed.

### Major

1. **Potential data leakage in SSL pre-training**: The paper applies LOSO cross-validation only during linear evaluation, but it is not stated whether each LOSO fold's held-out test subject is excluded from the SSL pre-training pool. If the encoder was pre-trained on all 88 subjects' unlabeled EEG (including the test subject), the encoder implicitly learns the test subject's signal distribution before classification, inflating all reported results. This is a well-known pitfall in SSL evaluation and its absence from the paper is a critical omission.

2. **Suspicious and unexplained performance gap vs. supervised baselines**: Supervised models in Table 1 achieve only 39–74% accuracy on what is a binary classification task (AD vs. CN). EEGNet achieving 46% on a two-class problem is near chance, and ATCNet/CTNet at 74% are far below the proposed 93%. The paper provides no analysis of why established supervised methods perform so poorly. If baselines were trained with suboptimal hyperparameters or on a less favorable split, the comparison is unfair and the claimed advantage is overstated.

3. **No confidence intervals or variance over LOSO folds**: All numbers in Tables 1–3 are reported as point estimates without standard deviation across LOSO folds. With only 65 subjects (AD vs. CN), per-fold variance can be substantial, and the lack of error bars makes it impossible to assess statistical reliability. BI-MCGNN (Table 2) correctly reports ± values, making it incomparable to the proposed method's bare point estimate.

4. **Inconsistency in claimed relative improvements**: The abstract claims "31.5% relative performance improvement over training from scratch." Table 3 shows 63.35% (scratch) vs. 92.90% (proposed), giving a relative improvement of ~46.5%, not 31.5%. The claimed 25.4% improvement over single-head is similarly inconsistent (~26.4% computed from the table). These discrepancies undermine confidence in the reported numbers.

### Minor

1. **Only binary classification evaluated**: The dataset contains three groups (AD, FTD, CN), but all experiments report only AD vs. CN accuracy. The three-class problem, where FTD is clinically difficult to distinguish from AD, is more medically relevant and would demonstrate broader utility.

2. **Ablation table ordering creates interpretational ambiguity**: "Multi-head (5 heads)" at 79.55% follows "w/o augmentation" at 78.58%, but "w/o augmentation" is described as a completely different training paradigm (MSE reconstruction loss instead of contrastive loss), not simply SimCLR minus augmentation. This makes it hard to isolate the true role of augmentation.

3. **Large unexplained jump from multi-head to adaptive multi-head**: The gap from "Multi-head (5 heads)" (79.55%) to "Adaptive 5 band heads" (92.90%) from adding only adaptive temperature is ~13.3 percentage points. This unusually large boost for a temperature scheduling change is not sufficiently analyzed or explained.

### Trivial

- The paper alternates between "DGNet" and "DGNNet" in Figure 1.

---

## Nice-to-Haves

- Report LOSO fold-level distributions (mean ± std) for all ablation conditions.
- Include an explicit statement about test-subject exclusion from SSL pre-training for each LOSO fold.
- Evaluate on the three-class (AD/FTD/CN) task to strengthen clinical relevance.
- Show confusion matrices per LOSO fold to characterize per-class errors.

---

## Novel Insights

The per-band adaptive temperature mechanism in the NT-Xent loss is an interesting extension of SimCLR: EEG frequency bands have substantially different power distributions and signal-to-noise ratios, so allowing each band's contrastive loss to operate at its own learned temperature is a principled inductive bias. The paper's own ablation supports this, showing ~6-point accuracy gains from constant-to-adaptive temperature (86.53% → 90.64%) and a further 2-point gain from adding regularization that induces the temperature toward d'/2. Whether this generalization holds across datasets and EEG recording setups is an open and worthwhile question.

---

## Suggestions

- Re-run all LOSO folds with test-subject data strictly excluded from the SSL pre-training pool and report results with ± standard deviation; this single clarification would significantly strengthen the paper's credibility.
- Provide a standardized training protocol for baseline comparisons (e.g., same LOSO folds, same number of epochs) to ensure the performance gap is not an artifact of training inequality.
- Recalculate or clarify the "31.5% relative improvement" claim to match Table 3 numbers.

---

## Score and Decision

The idea of frequency-band-specific self-supervised EEG representation learning is neurophysiologically motivated and the multi-band SimCLR design is coherent. The ablation study demonstrates each component contributes meaningfully. However, the paper suffers from a critical unaddressed methodological concern (potential data leakage in SSL pre-training), no uncertainty quantification, an implausible performance gap against supervised baselines that is left unexplained, and internal numerical inconsistencies. These are not cosmetic issues — they directly bear on whether the claimed 93% accuracy is trustworthy. The paper needs at minimum a clean re-run with proper LOSO-aware pre-training splits and confidence intervals before the results can be accepted.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>
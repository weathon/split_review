Now I have a clear calibration picture. Let me finalize the review.

**Round 1 Bracket:** The paper sits between ~4.0 and ~5.5 based on comparison with anchors:
- Below dhLIno8FmH (6.75): that paper had cleaner methodology and more convincing validation
- Above TkbjqexD8w (3.00) and PcE0yAGAGW (2.20): those had more fundamental flaws
- Comparable to YKfJFTiRz8 (5.00), KO09K3rBSr (4.80), ul6EYKM1Kv (4.50)

**Round 2 Narrowing:** Reading the full reviews for V5Zn0VVvBE (5.40) and KO09K3rBSr (4.80) and YKfJFTiRz8 (5.00):

- V5Zn0VVvBE (5.40): Rejected for limited novelty, missing key baselines. But its methodology (MAE pre-training, cross-dataset evaluation) was sound. DGNet has more serious methodological issues (pre-training leakage, loss function ambiguity), making it slightly weaker.
- KO09K3rBSr (4.80): Rejected for limited originality, marginal gains, presentation issues. DGNet's contributions are somewhat more substantial (comprehensive ablation showing clear gains), but the methodological issues are more serious.
- YKfJFTiRz8 (5.00): Rejected for insufficient evidence, marginal improvements, confusing method. DGNet is at a comparable level — real contributions undermined by significant methodological and presentation issues.

DGNet is most comparable to these papers. The pre-training leakage issue and loss function ambiguity are significant concerns, but there are genuine strengths in the architecture, ablation, and documentation. Score: **5.0**.

---

## Summary

This paper proposes DGNet, a self-supervised contrastive learning framework for EEG-based dementia classification (AD vs. CN). The architecture decomposes EEG signals into five canonical frequency bands (δ, θ, α, β, γ), processes each through independent CNN encoders and projection heads with band-specific adaptive temperatures, and pre-trains via a multi-head contrastive objective. Evaluation on a 65-subject dataset with Leave-One-Subject-Out cross-validation reports 92.90% accuracy against 12 benchmark models and 9 prior published results.

## Strengths

- **Neurophysiologically grounded architecture**: The five-band decomposition directly maps onto well-established dementia EEG biomarkers — increased delta/theta and decreased alpha/beta/gamma power (Section 1, lines 25–28). This gives the architectural design principled motivation beyond empirical tuning.

- **Comprehensive ablation study** (Table 3): The paper systematically isolates each component — training from scratch (63.35%), single-head SSL (73.52%), multi-head without adaptive temperature (79.55%), constant temperature (86.53%), and without regularization (90.64%). The decomposition makes the contribution of each mechanism explicit and verifiable.

- **Well-documented preprocessing and EEG-specific augmentations** (Sections 2.2, 3.2–3.3): The paper specifies concrete filter parameters (6th-order Butterworth, 0.5–45 Hz), ICA-based artifact removal, average referencing, and a suite of five EEG-tailored augmentations (Gaussian noise σ=0.03, amplitude scaling 0.8–1.2, 10% time/frequency masking, channel dropout) with EEG-relevant motivations.

- **Broad benchmark comparison** (Table 1): The method is compared against 12 established models spanning CNN-only, CNN+RNN, CNN+Attention, and SSL-pretrained architectures, providing useful context for the reported performance.

## Weaknesses

### Major

- **Pre-training data leakage under the claimed LOSO protocol**: The paper applies LOSO cross-validation only during the linear evaluation stage, while pre-training is performed once on all available data (Section 3, line 124: "During the pre-training stage, the model was trained... In the subsequent linear evaluation stage, Leave-One-Subject-Out (LOSO) cross-validation was used"). This means the encoder is exposed to test subjects' raw EEG data during contrastive pre-training. The paper itself states LOSO's purpose is "preventing data leakage between subjects and ensuring complete independence between the training and validation sets" (Section 3.4, line 148), yet this independence is not maintained at the pre-training stage. With only 65 subjects (36 AD + 29 CN) and SimCLR's instance discrimination task, segments from test subjects participate as negatives during pre-training, creating a pathway for subject-specific information to influence the learned representations. The reported 92.90% accuracy therefore cannot be interpreted as generalization to completely unseen subjects under the paper's own stated evaluation standard.

- **Mathematical formulation of the core loss is inconsistent with the claimed SimCLR/NT-Xent framework**: Equation 1 describes a loss that linearly maximizes positive pair similarity and minimizes only the hardest negative (via argmax over N negatives), plus temperature regularization terms. This is structurally different from the standard NT-Xent softmax loss shown in Equation 2, which sums over all negatives in a softmax denominator. The paper repeatedly claims to use SimCLR (abstract, Section 2.1, Section 2.3), but Equation 1 is closer to a margin-based hardest-negative objective. Meanwhile, line 108 states that "the multi-head implementation computes independent NT-Xent losses for each frequency band," suggesting Equation 2 is the actual implementation. The relationship between Equations 1 and 2 is never clarified, making it impossible to determine the actual training objective. If Equation 1 is the actual loss, the SimCLR framing is misleading; if Equation 2 is the actual loss, Equation 1 is an incorrect specification and the mathematical description is unreliable.

### Minor

- **"w/o augmentation" ablation is mislabeled** (Table 3): The condition labeled "without data augmentation" actually replaces the contrastive pre-training objective entirely with a masked reconstruction task (15% masking, MSE loss, line 199–200). This does not isolate the effect of augmentations within the contrastive framework — it compares two entirely different SSL paradigms. The label inaccurately describes what was tested.

- **No variance reported for the proposed method despite LOSO**: LOSO produces one result per fold (65 folds for 65 subjects), yet the paper reports only point estimates (92.90% accuracy, 92.85% F1) without standard deviation. The closest competitor in Table 2 (BI-MCGNN) reports ±0.38, making the absence of variance for the proposed method conspicuous. Without variance estimates, the claim of state-of-the-art performance lacks statistical grounding.

- **Several baselines perform at or near chance** (Table 1): Deep4Net (49%), EEGInception (39%), EEGNet (46%), TIDNet (44%), BIOT (53%), and Labram (54%) all perform near chance for a binary classification task. No details are provided about how these baselines were configured, tuned, or adapted for this specific dataset, making the comparison uninformative about relative method quality. The gap may reflect configuration issues rather than genuine superiority.

- **Neurophysiological motivation is not empirically validated**: The introduction builds a detailed case linking frequency-band EEG signatures to dementia, but the paper provides no evidence that the learned representations capture these spectral signatures. Figure 3 shows embedding spectrograms but offers no comparison of spectral power between AD and CN, no band-level attention or importance analysis, and no validation that the model relies on the bands the motivation says it should. The frequency-band design is evaluated only through downstream accuracy.

- **Cross-paper comparisons not controlled for preprocessing differences** (Table 2): The comparison against previously published results does not account for differences in preprocessing, segmentation, artifact rejection, electrode selection, or train/test construction, making these comparisons unreliable as evidence of superiority.

- **Contradictory descriptions of the evaluation protocol**: Section 2.1 (line 80) describes "linear evaluation" as updating "all parameters of the model including those of the encoder," while Section 3 (line 124) states the encoder weights are kept frozen. Although the actual protocol (frozen encoder) is clear from Figure 1 and Section 3, the contradictory description in Section 2.1 — combined with the fact that the "classifier" is a 3-layer MLP (512→256→2) with ReLU non-linearities rather than a true linear probe — undermines confidence in the experimental reporting.

### Trivial

- **Abstract improvement percentages do not match Table 3**: The abstract claims "31.5% relative performance improvement over training from scratch," but (92.90 − 63.35) / 63.35 = 46.6%. The claimed "25.4% improvement over the single-head approach" computes to (92.90 − 73.52) / 73.52 = 26.4%.

- **Regularization target outside the stated temperature range**: The regularization Ω(τ) in Equation 3 pushes τ toward 2/d′ ≈ 0.0156 (with d′=128), which lies below the stated temperature range of 0.05–0.5 (line 124). This means the regularization is always active in one direction.

- **Frequency band extraction described inconsistently**: Line 66 describes "parallel 1-dimensional convolution layers" while line 68 describes "bandpass filters" — these are different mechanisms whose relationship is not clearly explained.

## Nice-to-Haves

- Applying LOSO at the pre-training stage (or explicitly discussing why the current protocol is acceptable) would strengthen the generalization claim.
- Per-band spectral analysis comparing representation importance between AD and CN would connect the neurophysiological motivation to empirical evidence.
- Including the 23 FTD subjects for a 3-class or AD-vs-FTD evaluation would make better use of the available data.
- A direct, within-protocol comparison against the strongest baseline using identical preprocessing and LOSO would be more informative than cross-paper comparisons.

## Removed Points

These points were flagged by reviewers but are not included in the assessment:

- **Criticism of prose style ("tsunami that is shaking the very foundations…")**: This is a stylistic preference, not a scientific weakness. Removed.
- **Criticism that "single-dataset evaluation" is a fatal flaw**: Single-dataset evaluation is common in clinical EEG studies due to data availability. Demoted from major to context. The lack of variance reporting is the substantive issue, which is retained.
- **Claim that performance gaps are "implausible"**: The harsh critic asserted the 29.55-point SSL gain and temperature mechanism gains are extraordinary. This is a judgment call without concrete evidence of error; the ablation in Table 3 is internally consistent. Removed as a standalone weakness; the pre-training leakage concern (retained as Major) addresses the underlying validity question more precisely.
- **Criticism about the sleep research connection in Section 3.3**: The paper's reference to sleep research for 30-second epoch segmentation is slightly strained but harmless. Not a substantive weakness. Removed.
- **Criticism about the "Attached code" reference not providing key details**: The paper does provide substantial implementation details (optimizer, lr, batch size, scheduler, early stopping). Remaining gaps are minor reproducibility concerns, not a weakness. Removed.
- **Demand for FTD class inclusion**: The paper explicitly scopes to AD vs. CN classification. Including FTD would be a nice-to-have, not a weakness. Moved to Nice-to-Haves.
- **Criticism about baselines not being properly tuned**: This is speculative — we cannot know whether the baselines were misconfigured. The valid concern (no tuning details provided) is retained. The speculative framing is removed.
- **Criticism questioning existence of cited models/benchmarks**: Removed per hard rule.

## Novel Insights

None beyond the paper's own contributions. The idea of band-specific adaptive temperatures in multi-head contrastive learning is reasonable, but the paper does not establish that this produces representations with interpretable neurophysiological properties beyond improved classification accuracy. Without analysis of whether the learned temperatures or band representations reflect the neurophysiological signatures the introduction motivates, the contribution remains an engineering improvement.

## Suggestions

- Clarify whether LOSO was applied during pre-training. If not, either re-run with LOSO at both stages or explicitly discuss why the current protocol is acceptable given the unsupervised nature of pre-training and what safeguards exist against subject-specific leakage.
- Resolve the discrepancy between Equations 1 and 2: either correct Equation 1 to match the standard NT-Xent with adaptive temperatures, or stop claiming SimCLR and present the actual loss formulation as a deliberate design choice.
- Report per-fold mean and standard deviation for all LOSO metrics.
- Rename the "w/o augmentation" ablation to accurately describe what was tested (e.g., "masked reconstruction pre-training").
- Fix the abstract percentages to match Table 3.

## Calibration Anchors

All anchors retrieved across rounds, with comparison:

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| dhLIno8FmH (NICE — EEG image decoding) | 6.75 | R1 | Stronger: cleaner methodology, more comprehensive validation, mostly minor weaknesses |
| IAFStwZPNu (Brain's Bitter Lesson — speech decoding) | 5.67 | R2 | Somewhat stronger: broader scale, clearer contribution, fewer methodological concerns |
| V5Zn0VVvBE (ST-EEGFormer) | 5.40 | R2 | Slightly stronger: sound methodology, mainly novelty/missing-baseline criticisms |
| YKfJFTiRz8 (EEG-DisGCMAE) | 5.00 | R1/R2 | Comparable: real SSL contribution for EEG, undermined by insufficient validation and presentation issues |
| KO09K3rBSr (MUSE — EEG image recognition) | 4.80 | R2 | Comparable: SSL for EEG, marginal gains from key component, presentation issues |
| ul6EYKM1Kv (Cognition-supervised learning) | 4.50 | R1/R2 | Comparable: interesting idea but significant methodological concerns |
| TkbjqexD8w (Invariant spatiotemporal — seizure) | 3.00 | R1 | Weaker: more fundamental methodological flaws |
| 6uReXuDWrw (UniEEG) | 2.00 | R1 | Much weaker: serious problems throughout |

**Round 1 Bracket:** 4.0–5.5  
**Round 2 Narrowing:** Comparison with V5Zn0VVvBE (5.40), YKfJFTiRz8 (5.00), KO09K3rBSr (4.80) places DGNet at approximately 5.0 — it has more substantive architectural contributions and a better ablation than KO09K3rBSr, but more significant methodological issues (pre-training leakage, loss function ambiguity) than V5Zn0VVvBE. It is most comparable to YKfJFTiRz8.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
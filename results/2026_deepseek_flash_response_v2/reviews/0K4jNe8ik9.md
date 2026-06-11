Now let me produce the final review.

---

## Summary

This paper proposes DGNet, a self-supervised multi-band EEG representation learning framework for dementia classification. The model decomposes EEG signals into five frequency bands (delta through gamma), processes each band through an independent CNN encoder and projection head, and applies adaptive-temperature contrastive loss for pre-training, followed by linear evaluation with Leave-One-Subject-Out (LOSO) cross-validation. The method reports 92.90% accuracy on AD vs. CN binary classification with 65 subjects.

## Strengths

1. **Neurophysiologically principled architecture**: The five-band decomposition (delta 0.5–4 Hz through gamma 30–45 Hz) with independent encoders for each band is grounded in established EEG literature showing that dementia is characterized by increased low-frequency power and decreased high-frequency power. The architecture faithfully preserves band-specific information rather than mixing frequencies early, which maps directly to known dementia biomarkers.

2. **Ablation study that cleanly isolates the contribution of every design choice**: Table 3 systematically removes each component (SSL pre-training → 63.35%, single-head → 73.52%, no augmentation → 78.58%, constant temperature → 86.53%, no regularization → 90.64%) against the full model (92.90%), providing direct quantitative evidence that every introduced component contributes positively. This level of ablation granularity is a genuine strength.

3. **EEG-specific data augmentation with explicit parameters**: Section 2.2 specifies concrete augmentation parameters (Gaussian noise σ=0.03, amplitude scaling factor 0.8–1.2, 10% masking in time/frequency, 10% channel dropout), making the self-supervised learning protocol reproducible and tailored to EEG signal characteristics.

## Weaknesses

### Fatal
None.

### Major

1. **Potential subject-level data leakage between SSL pre-training and LOSO evaluation**: The paper describes LOSO cross-validation only for the linear evaluation stage (Section 3.4, line 146), while the pre-training stage description (line 124) does not mention any subject-level partitioning. This strongly implies the SSL encoder was pre-trained once on the entire dataset (all 88 subjects), after which LOSO splits were applied only for linear classifier training. If so, for each LOSO fold, the encoder has already seen the held-out test subject's unlabeled EEG data during pre-training. While the pre-training is unsupervised, the encoder learns distributional features from that subject's signals — on a small dataset with 88 subjects and high inter-subject variability, this is a form of leakage that undermines the subject-independence guarantee that LOSO is meant to provide (as the paper itself notes in line 148, LOSO "prevents data leakage between subjects"). The paper must either confirm that nested LOSO was used (pre-train on N−1 subjects per fold) or provide a control experiment showing pre-training on all vs. training-only subjects produces equivalent results.

2. **Suspiciously poor baseline performance suggests evaluation pipeline issues**: In Table 1, multiple established EEG models perform substantially below chance on a roughly balanced binary task (36 AD vs. 29 CN): EEGInception (39%), TIDNet (44%), EEGNet (46%), FBCNet (48%), Deep4Net (49%). Even EEGConformer (57%) and BIOT (53%) perform near or below the naive majority-class baseline (~55%). This pattern across diverse architectures (CNN, attention, hybrid) — many of which have demonstrated strong performance on other binary EEG classification tasks — strongly suggests something is systematically wrong with the baseline evaluation pipeline rather than genuine architectural weakness. Possible causes include hyperparameter mismatch, preprocessing incompatibility, or a label-related bug. The reported baseline results do not serve as meaningful comparison points, and the large gap to the proposed method (92.90%) cannot be interpreted as superiority without ruling out evaluation artifacts.

### Minor

1. **Concrete numerical error in the abstract's headline claims**: The abstract states a 31.5% relative improvement over training from scratch and 25.4% improvement over the single-head approach. Computing from Table 3: (92.90 − 63.35) / 63.35 = 46.6% (not 31.5%), and (92.90 − 73.52) / 73.52 = 26.4% (not 25.4%). The 31.5% figure does not match any calculation from the reported numbers. These are concrete errors in the paper's headline numerical claims.

2. **Discrepancy between Equation (1) and the claimed NT-Xent loss**: The paper states it uses "independent NT-Xent losses for each frequency band" (line 108) and Equation (2) correctly gives the standard NT-Xent form. However, Equation (1) — which is supposed to be the actual multi-band loss used — does not match this form. It uses a linear combination of positive similarity and a single maximum-negative similarity term, without any softmax over all negatives. If the implementation actually uses standard NT-Xent per band (as the text states), then Equation (1) misrepresents the actual loss. If Equation (1) is actually what is implemented, it is not a standard contrastive loss and the paper's characterization is misleading.

3. **No variance reporting despite LOSO producing per-subject fold results**: LOSO with 65 subjects produces 65 per-subject accuracy values from which mean and standard deviation can be computed. Yet the paper reports only point estimates (92.90% accuracy, 92.85% F1) without any variance. The BI-MCGNN baseline in Table 2 reports mean ± std (91.25 ± 0.38). Without variance, it is impossible to assess whether the 1.65 pp gap over BI-MCGNN is statistically significant.

### Trivial
None.

## Nice-to-Haves
- The dataset includes 23 FTD subjects whose data is never used in any classification experiment. Including AD vs. FTD or 3-class evaluation would strengthen the clinical relevance.
- A comparison against a standard single-encoder SimCLR (without multi-band heads) pre-trained on the same data would better isolate the multi-band architecture's contribution.

## Removed Points

These points were removed from the main review with brief justification:

- **"Unfair baseline comparison because baselines don't get SSL pre-training"**: Removed — the ablation study (Table 3, w/o SSL row at 63.35%) already isolates the SSL contribution. The primary concern with baselines is their below-chance performance (kept as Major above), not the asymmetric training protocol.
- **"Bandpass filter implementation unclear"**: Removed — the paper's description of the frequency band extractor is somewhat ambiguous (learned conv vs. fixed filters) but this is a presentation clarity issue that does not threaten the core claims.
- **"Architecture dimension mismatch"**: Removed — the paper describes [C, L/32] → GAP → [5, 128-dimensional] which is standard and interpretable.
- **"Downstream task terminology discrepancy"**: Removed — the paper describes two approaches and uses one; a minor wording issue.
- **"Model name inconsistency (DGNet vs DGNNet)"**: Removed — trivial formatting issue.
- **Strength Finder generic strengths** (e.g., "addressed an important problem", "large performance margin"): Removed — the performance margin claim depends on the baseline comparison that is itself suspect.
- **"No evaluation on 3-class or AD-vs-FTD"**: Moved to Nice-to-Haves — within the paper's stated scope (AD vs. CN), this is a suggestion, not a weakness.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Clarify the pre-training / LOSO protocol**: State explicitly whether SSL pre-training was performed per LOSO fold or on the entire dataset. If the latter, provide a control experiment comparing performance when pre-training includes vs. excludes the test subject.
2. **Investigate baseline evaluation pipeline**: Diagnose why multiple established EEG models perform below chance on a roughly balanced binary task. Verify that preprocessing, hyperparameters, and label assignment are consistent.
3. **Correct numerical claims**: Fix the 31.5% figure in the abstract (should be approximately 46.6% based on Table 3 values).
4. **Align Equation (1) with the actual implementation**: Either rewrite Equation (1) to match the standard NT-Xent loss used per band, or justify why the formulation in Equation (1) is actually what was implemented.
5. **Report variance across LOSO folds**: Compute and report standard deviation for all metrics.

## Calibration Anchors

**Round 1 (bracketing):**
| Path | Avg Score | Decision | Comparison |
|------|-----------|----------|------------|
| TkbjqexD8w.md | 3.00 | Reject | Cross-patient seizure classification; weaker methodology and smaller scope |
| 6uReXuDWrw.md | 2.00 | Reject | UniEEG universal EEG representation; fundamental pretraining issues |
| PcE0yAGAGW.md | 2.20 | Reject | FSL-MIC few-shot MI; limited evaluation |
| 04RGjODVj3.md | 3.00 | Reject | HyperEEGNet; small dataset (9 subjects) |
| dhLIno8FmH.md | 6.75 | Accept | EEG image decoding with contrastive learning; stronger execution and analysis |
| YKfJFTiRz8.md | 5.00 | Reject | EEG graph contrastive pre-training; similar data leakage concerns |
| tWNHQq7gZX.md | 5.00 | Reject | Universal Sleep Decoder; similar methodology concerns |
| KO09K3rBSr.md | 4.80 | Reject | EEG image recognition with contrastive learning; marginal improvements |
| kbjJ9ZOakb.md | 8.00 | Accept | Neuroscience paper; not comparable in domain |
| agPpmEgf8C.md | 8.00 | Accept | Neuroscience RL; not comparable |
| cNmu0hZ4CL.md | 8.00 | Accept | Neural dynamics; not comparable |
| PdaPky8MUn.md | 8.00 | Accept | Long sequence models; not comparable |

**Round 2 (narrowing):**
| Path | Avg Score | Decision | Comparison |
|------|-----------|----------|------------|
| ul6EYKM1Kv.md | 4.50 | Reject | Cognition-supervised saliency; ethical concerns, weak results — weaker than our paper |
| IAFStwZPNu.md | 5.67 | Reject | Speech decoding with SSL; cleaner execution but weaker results — slightly stronger than our paper |
| vFanHFE4Qv.md | 6.50 | Accept | Neuroscience contrastive learning; not directly comparable |
| cWEfRkYj46.md | 6.00 | Accept | Intracranial decoding; cleaner evaluation — stronger than our paper |

**Round 1 bracket**: 3.5–5.5  
**Round 2 narrowing**: Pulled toward the lower end of the bracket (closer to 4.5–5.0 rejected anchors) due to verifiable issues (data leakage ambiguity, below-chance baselines, numerical error) that are absent from the stronger anchors at 5.67+. The paper is above the 3.0-level papers but below the 5.67+ threshold for acceptance.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
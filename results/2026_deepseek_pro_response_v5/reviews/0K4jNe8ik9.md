## Final Review

---

## Summary
DGNet proposes a self-supervised learning framework for EEG-based dementia classification (AD vs. CN). The method decomposes EEG signals into five standard frequency bands (δ, θ, α, β, γ), trains independent CNN encoders per band using a SimCLR contrastive objective with adaptive per-band temperatures and regularization, then freezes the encoders and trains an MLP classifier. Evaluated on a 65-subject dataset under leave-one-subject-out cross-validation, the full model reports 92.90% accuracy.

## Strengths
- **Clinically-grounded frequency-band decomposition**: The architectural choice to process five canonical EEG bands separately is explicitly motivated by established neurophysiological biomarkers of dementia (increased low-frequency power, decreased high-frequency power; Section 1, lines 25–28). The ablation study supports this design: multi-head (79.55%) substantially outperforms single-head (73.52%), confirming that per-band encoding captures diagnostically relevant information missed by a shared encoder.
- **Appropriate cross-validation protocol**: The paper uses Leave-One-Subject-Out (LOSO) cross-validation (Section 3.4), the appropriate standard for EEG research, preventing subject-level data leakage and providing a stringent estimate of generalization to unseen subjects.
- **Detailed implementation specifications**: The paper provides concrete architectural parameters (three conv blocks with 32→64→128 channels, kernel size 7), training hyperparameters (AdamW, batch sizes 64/32, learning rate 1e-4, 100 epochs, weight decay 1e-5), and augmentation parameters (Gaussian noise σ=0.03, amplitude scaling [0.8, 1.2], 10% masking), supporting reproducibility.
- **Adaptive temperature mechanism with empirical validation**: The loss formulation extends NT-Xent with per-band learnable temperatures and regularization, and the ablation confirms this matters empirically (constant τ: 86.53% vs. adaptive: 92.90%).

## Weaknesses

### Fatal
None.

### Major
- **Misleading ablation: "w/o augmentation" changes the SSL paradigm, not just augmentations**: Table 3's "w/o augmentation" row (78.58%) does not remove augmentations from the SimCLR pipeline. Instead, the paper explicitly states (line 199): "we masked 15% of the EEG signal and trained the encoder model to reconstruct it using mean squared error (MSE) loss." This replaces contrastive SimCLR with masked-reconstruction pretraining using a different loss function — conflating the SSL objective, training signal, and augmentation removal simultaneously. The result cannot isolate the effect of augmentations, which undermines the ablation's claim to decompose component contributions cleanly.
- **Undefined "Multi-head (5 heads)" ablation configuration**: The "Multi-head (5 heads)" row at 79.55% in Table 3 lacks an explicit specification of which components are active. From context it appears to be multi-head SimCLR with fixed temperature and no regularization, but the paper never states this. The 13.35 percentage-point gap from this row to the full "Adaptive 5 band heads" (92.90%) is attributed to adaptive temperature and regularization — a large gain for optimization refinements — and without a clear configuration, the reader cannot properly assess this attribution.

### Minor
- **Terminology error in "Downstream Task" description**: Section 2.1 (line 80) states: "In the second approach, known as linear evaluation, all parameters of the model including those of the encoder are updated." This is backwards — in the SSL literature, linear evaluation means freezing the encoder. However, the figure caption and Section 3.4 confirm the encoder is frozen in practice, so this appears to be a text error rather than an experimental one.
- **Inconsistent classifier dimensions**: The Figure 1 caption describes layers of "612 and 256 units," while Section 2.1 (line 82) describes "512 nodes" for the first hidden layer.
- **Unverifiable relative improvement claims in the abstract**: The abstract claims "31.5% relative performance improvement over training from scratch" and "25.4% over the single-head approach." Using Table 3 numbers, (92.90−63.35)/92.90 ≈ 31.8% and (92.90−73.52)/73.52 ≈ 26.4%. The discrepancies are small but the calculation method appears inconsistent between the two percentages.
- **No variance reported for LOSO results**: With only 65 subjects, variance across LOSO folds matters for assessing whether the 1.65-point gap over BI-MCGNN (91.25% ± 0.38%, Table 2) is meaningful. The paper does not report standard deviations on its own main results.

### Trivial
- The "linear evaluation" MLP classifier uses hidden layers with ReLU, BN, and dropout — it is not a linear classifier, so the term "linear evaluation" is used loosely even when corrected.

## Nice-to-Haves
- The paper drops the 23 FTD subjects from the analysis without explanation; including multi-class or FTD vs. CN analysis would broaden the contribution.
- No comparison against a simple band-power baseline (extract band power features + linear classifier) to contextualize whether the deep learning pipeline adds value over standard spectral analysis.
- No discussion of limitations (small single-hospital dataset, narrow task, generalizability concerns) is provided.
- No statistical significance testing is reported for any pairwise comparison.

## Removed Points
These points were considered and deliberately excluded:
- **Harsh Critic claim that baseline comparison is "fundamentally unreliable"**: Table 1 does show several benchmark models with surprisingly low accuracy (e.g., EEGNet at 46%). However, the paper states benchmark model details are in the appendix (stripped by the parser), and per the review guidelines, criticisms depending on missing appendix content must be demoted. The low baseline numbers warrant clarification during rebuttal but the claim of fundamental unreliability cannot be verified without the appendix.
- **Harsh Critic claim about frequency band boundary inconsistency**: The introduction cites standard clinical band definitions (0-4, 4-8, 8-12, 12-30 Hz) while the methods section specifies exact implementation boundaries (0.5-4, 4-8, 8-13, 13-30, 30-45 Hz). These are not contradictory — the introduction summarizes literature standards and the methods gives precise implementation choices. Removed as a non-issue.
- **Harsh Critic claim about pretraining data being "not truly unlabeled"**: SSL pretraining on the same dataset with labels withheld is standard practice in the SSL literature. Not a flaw.
- **Harsh Critic claim that the method is "incremental"**: This is a subjective novelty judgment. The combination of frequency-band decomposition, SimCLR, and adaptive NT-Xent for EEG dementia classification is a reasonable engineering contribution, even if each component exists independently.
- **Strength Finder claim about "comprehensive benchmarking"**: Table 1 compares 12 models, which is thorough in scope, but the absence of documented baseline tuning procedures (possibly in the stripped appendix) makes this a qualified strength rather than an unambiguous one.
- **Harsh Critic complaints about introduction length and conclusion brevity**: These are stylistic preferences, not substantive issues.

## Novel Insights
None beyond the paper's own contributions. The core finding — that per-band contrastive learning with adaptive temperatures improves EEG representation quality for dementia classification — is demonstrated empirically but does not yield a broader insight about representation learning or EEG analysis that generalizes beyond this specific setup.

## Suggestions
- Redesign the "w/o augmentation" ablation to genuinely remove augmentations from the contrastive pipeline (same SimCLR loss, same encoder, no augmentations applied to either view), to cleanly isolate the contribution of augmentations.
- Explicitly define the configuration of each ablation row in Table 3, particularly "Multi-head (5 heads)," specifying which components (adaptive temperature, regularization, augmentations) are active in each row.
- Report standard deviations across LOSO folds for all main results.
- Fix the "linear evaluation" terminology in Section 2.1 and reconcile the classifier dimension discrepancy (612 vs. 512).
- Clarify how the relative improvement percentages in the abstract are computed.

## Calibration

### Round 1 — Bracketing
| Anchor | Score | Comparison to DGNet |
|---|---|---|
| 6uReXuDWrw (UniEEG) | 2.00 | DGNet substantially stronger — better evaluation, clearer contribution |
| PcE0yAGAGW (FSL-MIC) | 2.20 | DGNet clearly stronger |
| p30YulvDbj (MDD single-channel) | 2.00 | DGNet clearly stronger |
| TkbjqexD8w (Seizure IRM) | 3.00 | DGNet better — LOSO, ablation, multiple baselines |
| Ww599CnVnU (Sleep MSMS) | 4.25 | DGNet comparable — stronger results but similar novelty concerns |
| wJ6Bx1IYrQ (EEGPT) | 4.00 | DGNet comparable |
| YKfJFTiRz8 (EEG-DisGCMAE) | 5.00 | DGNet below — narrower scope, significant ablation issues |
| tWNHQq7gZX (Sleep Decoder) | 5.00 | DGNet below |
| KO09K3rBSr (Mind's Eye) | 4.80 | DGNet below |
| dhLIno8FmH (Decoding images) | 6.75 | DGNet clearly below |
| NPNUHgHF2w (CBraMod) | 6.75 | DGNet clearly below |
| vFanHFE4Qv (Neuron Platonic) | 6.50 | DGNet clearly below |
| PdaPky8MUn (Never from Scratch) | 8.00 | DGNet far below |

**Round 1 bracket: 3.0–5.5**

### Round 2 — Narrowing
| Anchor | Score | Comparison to DGNet |
|---|---|---|
| ejVuTFFkl6 (EEG-ImageNet) | 4.25 | Comparable tier |
| tfTGSm31F7 (EpilepsyFM) | 4.00 | DGNet slightly better — clearer ablation, stronger results |
| V5Zn0VVvBE (ST-EEGFormer) | 5.40 | DGNet clearly below — much broader scope and evaluation |

DGNet sits between EpilepsyFM (4.00) and Ww599CnVnU (4.25). It has stronger empirical gains than both but shares the limited novelty concern and has a concrete methodological flaw (the ablation conflation) that neither anchor exhibits. Settled at **4.0**.

---

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>
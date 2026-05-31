Now I have all the information I need. Let me produce the final consolidated review.

## Summary

SPECTRUM proposes a temporal-frequency multimodal representation learning framework for online handwriting verification (OHV). The model combines a multi-scale interactor for fine-grained cross-domain feature interaction, a self-gated fusion module for global modality integration, and a multimodal distance-based verifier (MDV) that leverages both temporal (DTW) and frequency (Euclidean) distances. Evaluated on MSDS-ChS, MSDS-TDS, and DeepSignDB, the method achieves state-of-the-art or competitive results, particularly on the first two datasets. The paper also explores biometric-level fusion of Chinese signatures and token digit strings.

## Strengths

1. **Novel temporal-frequency multimodal integration, validated by ablation.** The paper demonstrates that jointly modeling temporal and frequency modalities via the multi-scale interactor and self-gated fusion consistently outperforms temporal-only baselines. Ablation results (Table 4) show clear gains: adding the multi-scale interactor yields 0.90%/0.64% global EER improvements on MSDS-TDS/MSDS-ChS skilled forgery (lines 1→3), and the full model outperforms the baseline by substantial margins (e.g., 5.30 vs. 7.85 on ChS skilled 4v1). The contribution of each component is quantified.

2. **Multi-scale interactor with learnable frequency modulation.** The design splits the input into even/odd sub-sequences, applies 1D FFT with learnable complex weights to the odd path, and recombines them for cross-domain interaction (Fig. 3, Eqs. 1–3). The ablation shows the multi-scale version significantly outperforms a single-scale version (Table 4, lines 2 vs. 3: 4.91 vs. 5.91 on TDS skilled), demonstrating that multi-scale frequency learning is beneficial beyond single-scale frequency modeling.

3. **State-of-the-art or competitive results on multiple benchmarks.** On MSDS-ChS and MSDS-TDS (Tables 1–2), SPECTRUM achieves the best EERs in nearly all skilled-forgery configurations (e.g., 5.30/2.47 vs. next best 5.91/2.90 on ChS; 3.38/1.20 vs. 4.13/1.42 on TDS). On DeepSignDB (Table 3), it achieves the best EER for stylus-based skilled forgery (0.85w) and competitive results elsewhere.

4. **Biometric-level fusion yields further gains.** Section 4.4 and Table 5 show that combining Chinese signature and Token Digit String from the same writers improves performance over single-biometric baselines, with SPECTRUM benefiting the most (e.g., skilled 4v1 global EER 1.76 vs. 2.80 for Sig2Vec). This broadens the paper's contribution beyond feature-level multimodal learning.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Frequency feature extraction (f_F) is ambiguously described.** The paper states (Sec. 3.3, line 125) that "the frequency features f_F of the last multi-scale interactor are compressed by a selective pooling layer," and Fig. 2's caption explains that "the multi-scale interactor in the last M^4I block exclusively outputs frequency features, which are pooled to yield f_F." However, the detailed description of the multi-scale interactor (Sec. 3.1) describes a process where the odd sub-sequence goes through DFT → learnable modulation → IDFT, producing a time-domain output. It is never explicitly stated at which point the frequency-domain representation is extracted before the IDFT in the last block, or whether the last block skips the IDFT step. While the high-level mechanism is indicated, the exact architectural modification is underspecified, creating a reproducibility gap. A reader cannot reconstruct how f_F is produced without guessing.

2. **No statistical validation (confidence intervals, multiple seeds).** The key results in Tables 1–4 report only single-run EERs without standard deviations or significance tests. Given that the margins between SPECTRUM and the next best method on skilled forgery are modest (0.61–0.75% absolute EER), and the ablation contributions range from 0.06% to 0.90%, it is unclear whether these differences are statistically significant given the inherent variability of open-set handwriting verification. Reporting results over multiple random seeds would substantially strengthen the paper's conclusions.

3. **Missing training hyperparameters and scale specifications.** The paper does not specify learning rate, optimizer, batch size, number of epochs, gradient clipping, or hardware. While code release is promised, these details are standard to include in the paper itself. Furthermore, the specific scale values *l* for the three single-scale interactors (m=3 is stated, but e.g., whether l = 8, 16, 32 or similar) are not provided, hindering reproducibility of the multi-scale design.

4. **The even/odd splitting strategy is not ablated or justified against alternatives.** The paper splits handwriting sequences into even and odd time-steps (Sec. 3.1), assigning even for temporal preservation and odd for frequency analysis. No ablation compares this design against alternatives such as using the full sequence for both branches, applying FFT to the full sequence, or learning the split. The rationale provided (Discussion, line 97) is qualitative, and the arbitrary nature of the split leaves open whether a different design could achieve comparable or better results.

5. **On DeepSignDB (the largest dataset), performance is not consistently superior.** The paper acknowledges (Sec. 4.2, point 2) that Sig2Vec "primarily holds sway" on this dataset and notes a notable decline on finger-written random forgery. This limits the claim of "pronounced outperformance" to the MSDS datasets and is not fully reconciled with the paper's central narrative. While the limitation is discussed in Sec. 5, it should be foregrounded more precisely to avoid overclaiming.

6. **The MDV weighting formula (Eq. 7) lacks rigorous justification or ablation.** The sigmoid-weighted fusion of temporal scores using frequency scores is a specific design choice (asymmetric — frequency weights temporal but not vice versa). The paper provides intuition (lines 119–121) but does not ablate this formula against simpler alternatives such as additive fusion, multiplicative fusion, or symmetric weighting. Given that the MDV contributes only 0.06–0.21% improvement (Table 4), the design is not the main source of gains, but the lack of analysis makes it unclear whether this particular fusion strategy is optimal.

### Trivial
None.

## Nice-to-Haves

- Compare the even/odd split strategy against using the full sequence for both temporal and frequency analyses.
- Compare against a "Temporal-only" model that replaces the frequency branch with a second temporal branch of comparable capacity, to isolate the specific benefit of frequency modeling (as opposed to increased model capacity).
- Include results over multiple random seeds with standard deviations for key comparisons.

## Removed Points

These points from the reviewers were considered and removed (with justification):

1. **"Unfair comparison: baselines not given frequency features or MDV" (Harsh Critic #2).** REMOVED — This criticism is directly contradicted by the paper's own ablation data (Table 4, lines 6 vs. 7), which shows that MDV contributes only 0.06–0.21% improvement. The main performance gains come from the multi-scale interactor and fusion module, not the verifier. The baselines use their own standard verifiers (DTW for DsDTW, selective pooling + Euclidean for Sig2Vec), and comparing against published SOTA methods with their native verifiers is standard practice. Giving frequency features or MDV to temporal-only baselines is not feasible since those baselines do not produce frequency features.

2. **"Frequency as a separate modality is overselling" (Harsh Critic, Section-by-Section).** REMOVED — The paper explicitly acknowledges in the introduction (line 14) that "frequency is an intrinsically connected modality to the time domain." Using "modality" as a framing device is standard and well-justified in the multimodal learning literature; this is a semantic nitpick.

3. **"Loss function reliance on DsDTW; no comparison against using loss with temporal-only backbone" (Harsh Critic).** REMOVED — This comparison IS implicitly present in the ablation study, where the Baseline model (lines 1) is a temporal-only backbone. The incremental gains from adding frequency components to this baseline directly measure what the multimodal representation adds beyond what the loss provides.

4. **"Baseline in ablation is very weak" (Harsh Critic, Section-by-Section).** REMOVED — Ablation studies standardly start from a simple baseline and add components. The paper's ablation design (Table 4) cleanly isolates each component's contribution. The suggestion of adding a "Temporal-only" model of comparable capacity is reasonable but belongs in Nice-to-Haves, not as a weakness.

5. **Generalized concern sweeps without concrete anchors.** Various speculative criticisms from the Harsh Critic ("could the metric be measuring a proxy?", "are confounders controlled?") that lack a specific sentence, equation, or table in the paper to attach to have been removed per the filtering discipline.

## Novel Insights

None beyond the paper's own contributions. The key observation — that frequency-domain features can meaningfully complement temporal features in OHV, and that multi-scale interaction with learnable modulation is effective — is well-articulated in the paper itself. The additional finding that biometric-level fusion (signature + TDS) further improves performance is a genuine secondary contribution.

## Suggestions

1. Explicitly describe how f_F is extracted in the last M^4I block — specify whether the IDFT is skipped, or which intermediate representation is pooled. A precise mathematical description or a dedicated figure panel would resolve this ambiguity.

2. Add training hyperparameters (learning rate, optimizer with settings, batch size, epochs) and the specific scale values *l* used for the three interactors to the paper or appendix.

3. Report results over at least 3 random seeds with standard deviations for the key comparisons in Tables 1–2 and the ablation in Table 4.

4. Add an ablation that compares the even/odd split against using the full sequence in both branches, to validate this design choice empirically.

5. Tone down the "pronounced outperformance" language for DeepSignDB, or add analysis explaining why the method underperforms on finger-written random forgeries.

## Score and Decision

**MY FINAL SCORE: <score>7.0</score>**
**MY FINAL DECISION: <decision>Accept</decision>**
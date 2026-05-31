## Summary

This paper introduces the Signal Dice Similarity Coefficient (SDSC), a structure-aware reconstruction metric for time-series self-supervised learning. SDSC extends the Dice Similarity Coefficient from binary segmentation to continuous signals by measuring signed amplitude intersections, yielding a bounded [0,1] score reflecting local waveform polarity and magnitude overlap. The proposed metric replaces only the MSE reconstruction branch of SimMTM (leaving its contrastive InfoNCE loss unchanged), enabling a controlled analysis of how structure-aware reconstruction affects downstream representation quality. A hybrid loss combining SDSC and MSE with uncertainty-based weighting is also proposed to balance structural fidelity and amplitude precision.

---

## Strengths

- **Well-motivated problem with concrete illustration.** Table 1 and Figure 1 provide a clear, systematic demonstration of MSE's blind spots: phase-inverted signals receive low MSE despite semantic reversal, zero-valued outputs receive the same MSE as 2× scaled waveforms, and noisy signals can appear numerically accurate. The SDSC scores in Table 1 correctly flag all these failure cases.

- **Clean, controlled experimental design.** The decision to replace only the reconstruction branch of SimMTM while keeping InfoNCE fixed is methodologically sound. It isolates the effect of the loss function and prevents confounds from contrastive objective changes. The paper is explicit about this throughout.

- **Principled mathematical formulation.** Extending DSC to continuous signals via area-under-curve as a proxy for waveform shape is a natural and theoretically well-reasoned analogy. The discrete approximation (Eq. 5), the sigmoid-based differentiable Heaviside (Eq. 7), and the hybrid loss with learned uncertainty weighting (following Kendall et al., 2018) are all properly developed.

- **Multi-baseline comparison.** The paper compares against MSE, SoftDTW, PCC, and SI-SNR — not just a single baseline. Honest acknowledgment that SoftDTW and DILATE can be stronger in some forecasting settings (while being quadratic in complexity) adds credibility.

- **Transparency about limitations.** The paper explicitly states that SDSC is alignment-free, not tolerant to global shifts, and that it underperforms MSE in amplitude-heavy tasks like epilepsy classification. This honesty strengthens trust in the reported results.

---

## Weaknesses

### Fatal
None.

### Major

1. **Marginal empirical improvements without statistical significance testing.** In forecasting (Table 4), SDSC and Hybrid achieve average MSE of 0.294 vs. 0.295 for baseline MSE — a difference of 0.001, which is well within run-to-run variance for these benchmarks. On the Electricity dataset, SDSC achieves 0.200/0.293 vs. 0.200/0.291 (worse on MAE). In frozen classification (Table 5), the in-domain improvement is ~1 accuracy point; in cross-domain and fine-tuning settings (Table 6), SDSC is outperformed by MSE or PCC. No confidence intervals, standard deviations across seeds, or significance tests are reported for any downstream results. This makes it impossible to determine whether any of the observed differences are statistically meaningful or simply noise, which is critical given how small the differences are.

2. **Evaluation limited to a single backbone (SimMTM).** All conclusions about "structure-aware representation learning" are drawn exclusively from SimMTM. The paper acknowledges this and defers generalization to future work, but the scope of claims in the abstract and conclusions substantially exceeds what a single-backbone experiment can support. Given that the downstream improvements are already marginal within SimMTM, there is limited basis for broad claims about the superiority of structure-aware objectives.

3. **Pre-training reconstruction quality regresses significantly under SDSC.** In Table 2 (forecasting), SDSC-trained models have MSE=0.6348 vs. 0.4852 for MSE-trained models — a 31% increase in reconstruction error. The paper argues this is acceptable because "structural alignment suffices," but this argument is supported only by the observation that downstream performance is approximately equal. The reasoning is partly circular: similar downstream performance under worse reconstruction could equally indicate that the pre-training task is decoupled from downstream performance, rather than that SDSC provides genuinely better representations.

### Minor

1. **Scale-invariance of SDSC may be problematic.** Table 1 shows that SDSC = 0.6667 for both 0.5× and 2× scaled signals — identical scores despite very different amplitude distortions. For tasks where amplitude magnitude carries semantic content (e.g., epilepsy amplitude thresholds, EMG force estimation), this scale-blindness is not just a limitation but could actively mislead training. The paper mentions this but does not quantify its impact.

2. **The SDSC motivation example (inverted signal, MSE = 0.0200) is constructed for a low-amplitude regime.** The motivating example of MSE failing on phase-inverted signals depends on small amplitude. For standard-amplitude signals, phase inversion would produce significantly higher MSE, weakening this particular motivating case. A broader discussion of when this failure mode is actually encountered in practice would strengthen the motivation.

3. **Weak correlation evidence (Figure 3) is insufficient to establish misalignment between MSE and structural quality.** Pearson = −0.324 between MSE and SDSC during training is used to argue MSE is unreliable for structural learning, but this correlation is measured on a single dataset (ETTh1) under a single training run. The histogram comparison (Figures 3b/3c) shows a shift of only ~0.02 SDSC units between the two model types.

### Trivial

- The paper defines "structure-aware" as local sign and magnitude overlap. This is narrower than what the term typically implies in time-series analysis (which often includes frequency, phase, and morphology). A sharper terminological boundary would prevent misinterpretation.

---

## Nice-to-Haves

- Adding error bars or confidence intervals from multiple seeds for all downstream tables would substantially strengthen any claim of improvement over MSE.
- Evaluating SDSC in at least one other SSL framework (e.g., TI-MAE, TimeSiam) — even preliminarily — would move the paper from a single-case study toward a generalizable finding.
- An ablation comparing the learned uncertainty weighting in the hybrid loss against fixed λ in the main paper (rather than the appendix) would clarify whether the adaptive mechanism is necessary.

---

## Novel Insights

The paper's most genuinely novel observation is the analysis in Figure 3 and Table 3: at a fixed MSE level, SDSC-trained models exhibit a tighter and higher SDSC distribution than MSE-trained models. This suggests that SDSC training acts as a regularizer toward structural consistency even when amplitude reconstruction quality (as measured by MSE) is held constant — a finding that is non-obvious and worth further investigation. However, this insight is underexplored in the paper and its downstream implications remain unclear given the minimal performance deltas.

---

## Suggestions

- Report mean ± std over at least 3 seeds for all key downstream tables (Tables 4, 5, 6) so reviewers can assess statistical significance.
- Include at least one additional SSL backbone experiment (even a lightweight one) to support the broader claims about structure-aware reconstruction being generally beneficial.
- Provide a direct explanation of how SDSC behaves for typical EEG/ECG amplitude scales (not just the low-amplitude regime in Table 1 Figure 1a) to verify that the phase-inversion failure mode of MSE is practically common.
- Consider framing the paper more narrowly as a controlled study of reconstruction objectives in SimMTM, rather than a general claim about SSL for time series; the narrower framing is better supported by the evidence.

---

## Score and Decision

The paper addresses a legitimate and important problem (reconstruction loss design for time-series SSL) with a clear method (SDSC), a principled formulation, and a controlled experimental design. However, the empirical improvements are consistently marginal (< 1% in classification, near-zero in forecasting), lack statistical validation, and are demonstrated on only a single backbone. The theoretical contribution — extending DSC to continuous signals — is conceptually straightforward. The gap between the broad claims about structure-aware representation learning and the narrow, weakly-supported evidence significantly limits the paper's impact at ICLR. The honest acknowledgment of limitations is commendable, but does not compensate for the insufficient evidence.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>
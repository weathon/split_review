## Summary

The paper proposes HG-Diff-IB, a hierarchical graph-coding diffusion model with adaptive information bottleneck for multichannel speech enhancement. It introduces: (1) a hierarchical alignment method that maps STGCN-extracted graph features to corresponding UNet layers via a linear interpolation rule; (2) a layer-wise AdaIN-based modulation that injects graph-coding into intermediate diffusion features; and (3) an adaptive information bottleneck whose compression coefficient $\beta_{\text{adapt}}$ is derived from an attention mechanism on input STFT features. Experiments on a custom 108-sample test set show improvements in PESQ and STOI over five baselines.

---

## Strengths

- **Hierarchical layer-specific conditioning is well-motivated**: Rather than applying a single conditioning signal uniformly across all UNet layers, the hierarchical alignment (Eq. 1) assigns graph-coding features at matched depths, which is conceptually principled and supported by the ablation in Table 2.
- **Ablation study compares conditioning strategies**: The comparison of FiLM, AdaGN, and AdaIN for layer-wise modulation provides useful evidence that AdaIN is preferable for this task, and the addition of the IB module shows a clear jump in PESQ at low SNRs (−5 dB, 0 dB), specifically +4.09% and +3.32%.
- **SNR-adaptive bottleneck addresses a real limitation**: Fixed-strength compression hurts high-SNR performance; Table 2 shows the adaptive IB slightly recovers this relative to fixed IB, demonstrating the intended behavior.

---

## Weaknesses

### Fatal

1. **PESQ values are implausibly low across all methods, including the proposed one.** PESQ ranges from −0.5 to 4.5; values below 2.0 represent "bad" speech quality. The best reported average PESQ is 1.2647, barely above the noisy input of 1.0662. Standard modern speech enhancement systems achieve PESQ > 2.5–3.5 on comparable conditions. This either indicates a serious flaw in the evaluation pipeline (e.g., incorrect waveform reconstruction, wrong sampling rate alignment, or misuse of the PESQ API) or that all methods—including the proposed one—are essentially failing on this dataset. No explanation is given for why all methods perform this poorly, and such results cannot be taken as evidence that the system works.

2. **Mathematical inconsistency between Eq. 4 and Eq. 6.** The adaptive IB loss is defined in Eq. 4 as $L_{IB} = -I(Z; Y) + \beta_{\text{adapt}} I(Z; X)$, but in Eq. 6 the same symbol $L_{IB}$ is redefined as $\|\mathcal{F}_\phi(x_t) - x_{0,t}\|_2^2 + \beta_{\text{adapt}} I(Z; X)$. The mutual information term $-I(Z; Y)$ is silently replaced by an L2 reconstruction loss without justification, while the second term $\beta_{\text{adapt}} I(Z; X)$ (mutual information) is retained but never explained how it is practically estimated or computed. No tractable estimator for $I(Z; X)$ is described anywhere in the paper.

3. **$\beta_{\text{adapt}}$ does not produce a scalar as required.** Eq. 5 defines $\beta_{\text{adapt}} = \text{softmax}(W^Q \mathbf{x}_t \cdot W^K \mathbf{x}_t^\top / \sqrt{d_k})$, which is an attention matrix of shape $T \times T$. The paper then uses $\beta_{\text{adapt}}$ as a scalar tradeoff parameter in Eqs. 4 and 6. No aggregation or dimension reduction is described. The claim that this quantity represents "estimated SNR" is also unsubstantiated—the attention self-similarity matrix of STFT features is not an SNR estimator without further derivation.

### Major

4. **Evaluation on a non-standard, private 108-sample test set only.** The entire empirical claim rests on 108 test utterances. No standard multichannel benchmark (e.g., CHiME-3/4/6, REVERB, spatialized LibriMix, or even VoiceBank-DEMAND for single-channel comparators) is used. The small test set makes statistical reliability questionable and prevents any comparison to the broader literature.

5. **Percentage-based gains are misleading on such a compressed scale.** Claiming "16.72% improvement over Diffwave" corresponds to an absolute gain from ~1.08 to ~1.26 PESQ—a change that is perceptually negligible and within what could easily be measurement noise. Reporting relative percentages on near-floor values inflates the apparent magnitude of results.

6. **Unfair or unclear baseline comparison.** The paper evaluates against single-channel baselines (DiffWave, CDiffuSE, DOSE) that do not use multichannel input, while the proposed method uses a six-channel microphone array. This is not disclosed prominently. The "Diffusion" entry in the ablation table has numerically identical values to G-DiffuMSE in Table 1, suggesting the ablation baseline is G-DiffuMSE, but this is never stated explicitly, making the ablation design opaque.

### Minor

7. **The hierarchical alignment (Eq. 1) is essentially linear interpolation** between layer indices. This is a reasonable and simple approach but is presented as a methodological contribution without acknowledging that similar layer-matching strategies are standard in U-Net skip-connection or feature-pyramid designs.

8. **STOI results in the ablation are not consistently improved by the proposed modules.** At 5 dB and 10 dB, +AdaIN achieves *higher* STOI than both ++IB and ++adaptiveIB variants, contradicting the claim that each addition improves performance across all conditions.

### Trivial

- The description of what constitutes "shallow" vs. "deep" graph-coding features (Sec. 2.1) inconsistently attributes phonetic/semantic content to shallow features and only "frame-level" features to deep ones, which is the opposite of typical deep network behavior.

---

## Nice-to-Haves

- Evaluation on VoiceBank-DEMAND or another community-standard benchmark would make results interpretable and comparable.
- A clear tractable approximation for $I(Z; X)$ (e.g., a VIB-style Gaussian approximation) would make the IB loss mathematically grounded.
- A listening/MOS evaluation would help validate perceived quality improvements, especially given the suspicious PESQ range.

---

## Novel Insights

The paper's core idea—using SNR-conditioned compression strength in an information bottleneck to adaptively suppress noise—is conceptually appealing. If correctly formulated and evaluated, dynamically tying $\beta$ to signal conditions could be a useful inductive bias for speech enhancement. However, the current formulation does not rigorously instantiate this idea (the connection between the attention matrix and SNR is not derived), so no insight beyond what is already claimed by the authors can be confirmed from the evidence presented.

---

## Suggestions

- Audit the PESQ evaluation pipeline: verify waveform sampling rates, number of channels passed, and PESQ implementation (narrow-band vs. wide-band). PESQ values around 1.0–1.5 on 0–10 dB SNR conditions are far below what is expected and suggest a systematic error.
- Replace the attention-matrix $\beta_{\text{adapt}}$ with an explicit SNR estimator (e.g., a learned scalar regression head trained on clean/noisy signal pairs) and provide a mathematically consistent IB loss formulation with a tractable mutual information bound.
- Evaluate on at least one standard benchmark to validate generalization claims.

---

## Score and Decision

The paper presents an interesting architectural idea, but two fatal issues—(1) implausibly low PESQ scores suggesting a broken evaluation pipeline, and (2) a mathematically inconsistent information bottleneck formulation where a matrix is used as a scalar and the mutual information term is replaced by an L2 loss without justification—together with evaluation on only 108 samples using non-standard benchmarks, prevent the core claims from being trusted. These are not presentation issues but validity issues.

MY FINAL SCORE: <score>2</score>
MY FINAL DECISION: <decision>Reject</decision>
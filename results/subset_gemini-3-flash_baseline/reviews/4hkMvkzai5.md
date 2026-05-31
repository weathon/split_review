## Summary
The paper introduces DeCodec, a neural audio codec designed to learn universal disentangled representations. Unlike standard codecs that entangle audio components, DeCodec factorizes input audio into orthogonal subspaces for speech and background sound (BGS) using a Subspace Orthogonal Projection (SOP) module and a Representation Swap Training (RST) procedure. Within the speech subspace, it further decouples semantic and paralinguistic information via semantic guidance (SG). This hierarchical disentanglement allows the codec to serve as a unified front-end for tasks like speech enhancement, voice conversion, and robust ASR by simply selecting or recombining specific latent components.

## Strengths
- **Novel Disentanglement Framework:** The paper moves beyond simple speech-component decomposition (like content/pitch) to address the more challenging problem of speech vs. background sound decoupling within a unified codec framework.
- **Methodological Soundness:** The combination of the SOP module (architectural constraint) and the RST procedure (training objective) is well-reasoned. The theoretical justification in Section 3.6, using the mean value theorem to show how the swap loss enforces independence, is a strong addition.
- **Versatility and Utility:** The model demonstrates "zero-cost" speech enhancement and voice conversion through latent manipulation. The ability to perform these tasks without specialized downstream models highlights the value of the learned representation space.
- **Strong Empirical Results:** DeCodec outperforms specialized speech enhancement (SE) models like SELM and StoRM in background suppression (BAK scores) and overall quality (OVL) on the DNS Challenge test set, which is impressive for a general-purpose codec.
- **Robustness:** The experiments show that the semantic representations learned by DeCodec are significantly more robust to noise than existing speech tokenizers (e.g., SpeechTokenizer), as evidenced by the WER improvements in noisy conditions.

## Weaknesses
### Fatal
None.

### Major
- **Bitrate Comparison Clarity:** The paper compares DeCodec (at 4.0+4.0 kbps) against baselines like HiFi-Codec (2.0 kbps) and DAC (4.5 kbps). Since DeCodec uses two parallel RVQs, the total bitrate is effectively doubled compared to some baselines. While the performance is high, the efficiency trade-off (performance per bit) is not explicitly discussed, making it difficult to judge if the gains are due to the disentanglement or simply the higher bit budget.
- **Evaluation of Background Sound Quality:** While speech reconstruction and enhancement are thoroughly evaluated, the quality of the *decoupled background sound* itself is less explored. The paper mentions BGS preservation for TTS, but quantitative metrics (e.g., FAD or BGS-specific SDR) for the isolated background component would better support the claim of "universal" disentanglement.

### Minor
- **One-shot VC Performance:** The WER for one-shot VC (Table 3) remains quite high (~50%). While the paper provides a reason (voicing time mismatches), this suggests that the paralinguistic/semantic split might still have some leakage or that the reconstruction from swapped tokens is not yet robust enough for high-quality synthesis.
- **Complexity:** The introduction of parallel RVQs and the SOP module increases the model's parameter count and computational overhead compared to a standard DAC. A brief mention of the inference latency or parameter count relative to DAC would be beneficial.

### Trivial
- The term "RBS Representation" in Figure 1's caption is likely a typo for "BGS" (Background Sound), though it does not affect understanding.

## Nice-to-Haves
- Audio samples of the isolated background sound (N) to verify that speech is not leaking into the noise component.
- A comparison of the SOP module against a simpler MLP-based separation to prove the necessity of the orthogonal projection constraint.

## Novel Insights
The core insight is that the "front-end separation" and "feature extraction" steps of an audio pipeline can be unified into a single codec by enforcing subspace orthogonality in the latent space. By using a representation swap training (RST) procedure—analogous to CycleGAN's consistency but applied to additive components—the model learns to treat speech and noise as independent, recombinable tensors. This effectively transforms a compression tool into a controllable generative front-end where "denoising" is reduced to a zeroing-out operation in the latent domain.

## Suggestions
- Include a table or plot comparing SDR vs. Bitrate for DeCodec and DAC to demonstrate that the disentanglement provides value beyond just increased capacity.
- Provide a more detailed breakdown of the "Residual Semantic" vs "Semantic" components in the experiments to show exactly what paralinguistic information (e.g., emotion, prosody) is captured in the residual.

## Score and Decision
The paper presents a significant step forward in neural audio coding by successfully integrating disentanglement into a high-fidelity reconstruction framework. The methodology is sound, and the applications (SE, VC, ASR) demonstrate the practical utility of the approach.

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>
## Summary
The paper proposes HG-Diff-IB, a multichannel speech enhancement framework that integrates a diffusion model with a hierarchical graph-coding mechanism and an adaptive information bottleneck (IB). The core idea is to provide layer-specific guidance to the diffusion denoiser using features from a Spatial-Temporal Graph Convolutional Network (STGCN) and to use an IB module to compress redundant noise information. The IB compression is dynamically adjusted based on the estimated SNR to balance noise suppression and speech preservation.

## Strengths
- The paper addresses a relevant problem in diffusion-based speech enhancement: the lack of layer-specific guidance and the presence of redundant information in conditioning features.
- The hierarchical alignment method (Eq. 1) provides a systematic way to map graph-coding features to specific depths of the UNet denoiser, moving beyond simple global concatenation.
- The introduction of an adaptive information bottleneck that scales with SNR is well-motivated, as low-SNR signals typically require more aggressive feature compression to remove noise.
- The experimental results show consistent improvements over several competitive baselines (CDiffuSE, G-DiffuMSE, DOSE) across multiple SNR levels, particularly in very noisy (-5dB) conditions.

## Weaknesses
### Major
- **Clarity of the Adaptive IB Mechanism:** The calculation of $\beta_{adapt}$ in Eq. 5 is described as being derived from "temporal similarity of the input STFT features" using a softmax over a query-key dot product. However, $\beta$ in Information Bottleneck theory is typically a scalar hyperparameter. Eq. 5 appears to produce a matrix (attention-like). It is unclear how this matrix is reduced to a scalar or a vector to modulate the IB loss in Eq. 4 and Eq. 6.
- **Optimization Details:** Section 2.3.2 mentions a "cooperative optimization strategy" where the graph network is updated during the sampling process (inference) for 10 epochs. This suggests a test-time adaptation or a very unconventional sampling routine. If the graph network is updated during inference, the computational overhead would be significant, yet there is no discussion of inference latency or the feasibility of this approach for real-time applications.
- **Baseline Comparison:** While the paper compares against G-DiffuMSE (2025), the absolute PESQ scores across all models (including the proposed one) are quite low (ranging from 1.1 to 1.4). In the field of speech enhancement, PESQ scores below 1.5 usually indicate very poor intelligibility or significant artifacts. It is unclear if this is due to the extreme difficulty of the synthetic dataset or a specific implementation choice (e.g., narrow-band vs wide-band PESQ).

### Minor
- **Mutual Information Estimation:** The paper uses $I(Z; Y)$ and $I(Z; X)$ in the loss function but does not specify how these mutual information terms are estimated (e.g., using MINE, variational bounds, or assuming Gaussian distributions). This makes the method difficult to reproduce.
- **Ablation Specifics:** In Table 2, the "++IB" and "++adaptiveIB" rows show improvements, but the paper does not explicitly detail the architecture of the bottleneck layer itself (e.g., is it a VAE-style bottleneck with KL divergence?).

## Nice-to-Haves
- A comparison of computational complexity (FLOPs/RTF) between the proposed method and the baselines, especially given the "cooperative optimization" during sampling.
- Evaluation on a standard public dataset like VoiceBank-DEMAND to allow for broader comparison with the state-of-the-art.

## Novel Insights
The primary novel insight is the coupling of SNR-aware Information Bottleneck theory with hierarchical diffusion conditioning. While IB has been used for representation learning, applying it to dynamically "filter" the conditioning signal in a diffusion process based on the estimated noise level is a clever way to handle the trade-off between guidance and noise leakage.

## Suggestions
- Clarify the dimensionality of $\beta_{adapt}$ and how the softmax output in Eq. 5 is transformed into the trade-off coefficient used in the loss function.
- Provide more details on the "cooperative optimization" in Section 2.3.2. Specifically, clarify if this happens during training or at test-time (sampling). If it is test-time, provide the time cost.
- Explain the low absolute PESQ values to ensure they are not a result of an evaluation error.

## Score and Decision
The paper presents a technically sound extension of diffusion models for multichannel speech enhancement. The hierarchical guidance and adaptive IB are well-integrated. However, the lack of clarity regarding the MI estimation and the potentially high cost of the optimization strategy during sampling are concerns.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
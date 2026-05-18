## Summary

This paper proposes BDIA-transformer, a method for making transformers exactly bit-level reversible without modifying their architecture at inference time. The key idea is to interpret each transformer block as Euler integration of an ODE, then apply bidirectional integration approximation (BDIA) with a randomly sampled binary parameter γ ∈ {−0.5, 0.5} per block per training sample. During training, this creates an ensemble of ODE solvers that regularizes the model and improves validation accuracy. Activation quantization with 1-bit side information per activation per block enables lossless online back-propagation. At inference, E[γ]=0 recovers the standard transformer update (up to activation quantization). Experiments on ViT (CIFAR-10/100), encoder-decoder translation, and GPT-2 text prediction show improved validation performance over baselines with reduced training memory.

## Strengths

- **BDIA-transformer achieves higher validation accuracy than both standard ViT and RevViT while reducing training memory.** Table 1 shows BDIA-ViT reaches 89.10% on CIFAR-10 (vs. 88.15% for ViT and 86.22% for RevViT) and 66.09% on CIFAR-100 (vs. 61.86% for ViT and 61.89% for RevViT), while peak memory is 693.4 MB compared to 1570.6 MB for ViT. This directly supports the dual claims of improved performance via regularization and memory reduction via reversibility.

- **The inference architecture is identical to the standard transformer up to activation quantization.** Section 4.2 derives that setting E[γ]=0 reduces the BDIA update to x_{k+1} = x_k + h_k(x_k), and Section 4.3 (Eq. 12) shows the only inference change is activation quantization. This is a key differentiator from prior reversible models (RevNet, RevViT, i-RevNet) that require non-standard architectures even at inference.

- **Exact bit-level reversibility is achieved with provably lossless online back-propagation using lightweight side information.** Section 4.3 provides the quantization scheme (Eqs. 9–11) and the reverse formula (Eq. 13) that exactly recovers x_{k-1} from (x_k, x_{k+1}) using only 1-bit side information per activation per block. This eliminates the error accumulation shown in Fig. 2, a critical issue for deep transformer models.

- **The regularization effect is systematically validated across multiple tasks and architectures.** Experiments on ViT (image classification), encoder–decoder transformer (language translation, Fig. 4), and GPT-2 (text prediction, Fig. 5) all show BDIA yields lower validation loss or higher accuracy than baselines, despite higher training loss. This demonstrates the generality of the ensemble-of-ODE-solvers interpretation.

- **The ablation study (Table 2) isolates the contribution of the γ parameter.** All non-zero γ values (±0.25, ±0.5, ±0.6) improve CIFAR-10 accuracy over the baseline (γ=0), with ±0.5 performing best (89.12% vs. 88.15% for γ=0). This directly confirms that the model regularization, not architectural modification, drives the performance gain.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The optimizer used for baselines vs. BDIA is not clearly stated.** The paper reports using the SET-Adam optimizer for BDIA-ViT (line 265), but does not explicitly state whether the ViT and RevViT baselines in Table 1 were trained with the same optimizer or with standard Adam from the original open-source code. This creates a confound: part of the observed gain could theoretically be optimizer-driven rather than γ-driven. The γ=0 ablation in Table 2 (which achieves 88.15%, matching the ViT baseline) suggests the setups are consistent, but the optimizer used for that ablation is also not stated. The paper should explicitly clarify (a) which optimizer was used for each baseline and ablation condition, and (b) whether the baselines were re-run in-house or numbers were taken from existing results.

- **The claim about RevViT is based on limited evidence.** The paper asserts that RevViT yields "either inferior or comparable validation performance to that of its original counterparts" (line 295) and implies this is a general finding, but it is supported only by CIFAR-10/100 experiments with 6-block ViT. A single architecture/dataset regime is insufficient to support a dismissive tone about an established method. The authors should either temper this claim or add evidence on deeper architectures or ImageNet-scale data.

- **The memory analysis is limited to one shallow model.** Peak memory numbers are reported only for a 6-layer ViT (Table 1). The paper does not analyze how the memory trade-off (side-information storage vs. activation savings) scales with depth, batch size, or sequence length for realistic LLM-scale models. A scaling formula or discussion of packing strategies for the 1-bit masks would strengthen practical credibility.

- **The inference quantization requirement could be flagged more prominently.** While the paper is transparent (abstract says "up to activation quantization"; Eq. 12 explicitly includes Q_l), the headline phrasing "unchanged standard architecture for inference" and "identical to conventional transformers" (lines 4, 21, 123) could mislead a casual reader into thinking no modifications at all are needed. A dedicated note on what the l=9 quantization means in practice — precision loss relative to FP32, whether it can be turned off — would clarify adoption requirements.

- **The choice of l=9 for quantization is not justified.** The paper fixes the quantization precision at 2^{-9} without any ablation or sensitivity analysis. An experiment examining l=7, 9, 11 (or similar) would demonstrate robustness and clarify the trade-off between precision and the feasibility of the side-information scheme.

### Trivial
None.

## Nice-to-Haves

- **Reconstruction error for ViT:** Figure 2 shows reconstruction error only for GPT-2. Showing the same for ViT would strengthen the motivation for the quantization scheme.
- **Scaling analysis of memory:** A formula for total memory saved vs. side-info stored as a function of depth, batch size, and sequence length would make the memory claim more actionable.
- **Quantization precision ablation:** Testing l=7, 9, 11 would demonstrate robustness and help readers understand the precision trade-off.

## Removed Points

- **"The inference architecture is not unchanged — activation quantization is a change" (harsh critic's Point 1, in its strongest form):** This criticism overstates the issue. The paper transparently qualifies its claims with "up to activation quantization" in the abstract, in Section 4.3 (Eq. 12 explicitly shows Q_l), and in the conclusion. The architecture itself (attention + FFN structure, residual connections) is indeed unchanged; only the numerical precision of activations differs. The criticism is downgraded to a minor presentation point above, not maintained as a structural weakness. The substantive kernel — that the qualifier could be more prominent — is retained.

## Novel Insights

The reviews surface a useful meta-point: the paper occupies an interesting middle ground between reversible architectures (which change the model for inference) and quantization-aware training (which changes precision but not architecture). By combining a randomized ODE-solver ensemble during training with a quantization-enabled exact reversibility mechanism that collapses to a near-standard architecture at inference, the paper bridges two normally separate lines of work. This positioning — reversible training that regularizes *and* saves memory while being near-drop-in at inference — is a genuinely differentiated contribution.

## Suggestions

1. State explicitly which optimizer was used for each baseline and ablation condition — ideally in a single table or sentence.
2. Add a brief discussion of what the l=9 quantization means in practice: how much accuracy is lost relative to FP32, and whether the model can be evaluated without Q_l if reversibility is not needed.
3. Temper the claims about RevViT to match the evidence, or add experiments on deeper architectures.
4. Include a short analysis of how memory savings scale with model depth and sequence length.
5. Add an ablation on quantization precision (e.g., l=7, 9, 11) to justify the l=9 choice.

## Score and Decision

This paper presents a technically novel and mathematically sound method. The core idea — using randomized bidirectional integration with binary γ and quantization-enabled exact reversibility — is clever and well-executed. The empirical results are consistent across three different tasks and architectures, and the ablation study cleanly isolates the regularization effect. The identified weaknesses (optimizer reporting gap, limited RevViT evaluation, no quantization ablation) are all addressable and do not threaten the core contribution.

**Originality:** High — the combination of BDIA-inspired ODE averaging with quantization-based exact reversibility for transformers is novel.  
**Importance:** High — reversible training that both regularizes and collapses to a near-standard inference architecture addresses a real need in large-model training.  
**Claims support:** Mostly good, with one reporting gap (optimizer) that needs clarification.  
**Soundness:** The derivations are correct and the experiments support the main claims.  
**Clarity:** Generally clear, though the inference quantization qualifier could be more prominently placed.  
**Value:** Positive — the method is practical and the regularization benefit is demonstrated across tasks.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
Now I have enough information for calibration. Let me synthesize everything.

**Round 1 bracket**: This paper is clearly above the low band (avg scores 3.0-3.4 — those papers have significant flaws or limited results) and well below the high band (avg scores 8.0+ — landmark papers with exceptional breadth/validation). The plausible bracket is **5.0-7.0**.

**Round 2 narrowing**: The closest topical anchors are CtrLoRA (6.00, controllable generation efficiency), Qihoo-T2X (6.40, efficient DiT via sparse attention), LinFusion (6.25, linear attention for efficiency), and MT-Diffusion (5.75). PKA has stronger *motivational grounding* (attention sparsity analysis) than CtrLoRA, is more *focused and well-validated* than Qihoo-T2X on its target task, and similar to LinFusion in strength. The main weaknesses (understated F1 trade-off, lack of quantitative metrics in some ablations) are real but minor. The paper's core claims are well-supported.

**Final score**: 6.0 — the paper has clear contributions, strong efficiency results, and generally supports its claims; weaknesses are addressable.

Now let me write the full review.## Summary

This paper addresses the computational bottleneck in multi-condition Diffusion Transformers caused by the "concatenate-and-attend" strategy. Through empirical analysis of attention patterns, the authors identify that computation is redundant in condition-specific ways — spatially aligned conditions concentrate attention along the diagonal, while subject-driven conditions activate only keyword-relevant regions. They propose **PKA (Patch-wise and Keyword-Aware Attention)**, which decomposes full attention into two efficient modules: **Position-Aligned Attention (PAA)** for one-to-one spatial condition processing and **Keyword-Scoped Attention (KSA)** for masked subject attention, complemented by a **Condition Cache** and an **early-timestep sampling** strategy. Experiments on multi-condition tasks (Subject-Canny, Subject-Depth, Canny-Depth) demonstrate up to 10× inference speedup and 5.12× VRAM reduction while maintaining or improving generation quality.

## Strengths

1. **Well-motivated by empirical attention analysis**: Figures 2 and 3 provide direct evidence that attention in multi-condition DiTs is highly redundant — diagonal concentration for spatial conditions and localized activation for subject conditions. This empirical grounding is stronger than prior work that simply accepts the "concatenate-and-attend" overhead without analyzing where computation is wasted. The analysis directly motivates the architectural decomposition.

2. **Substantial and well-measured efficiency gains**: Figures 7 and 8 show that PKA's inference time and VRAM consumption remain nearly flat as conditions scale from 1 to 16, while baselines grow sharply. The reported speedup (3.90×–10×) and VRAM reduction (2.46×–5.12×) are measured on the same hardware with controlled token counts (1024 tokens per condition) and directly support the paper's core efficiency claim.

3. **Generative quality maintained or improved across most metrics**: Table 1 shows PKA achieves the best FID, SSIM, CLIP-I, and DINOv2 on all three multi-condition tasks (e.g., Subject-Canny FID 52.99 vs. UniCombine 61.03; DINOv2 0.926 vs. 0.901). On controllability, PKA achieves best or near-best F1/MSE scores on most tasks, demonstrating that the attention reduction does not come at a categorical quality cost.

4. **Graceful efficiency-quality trade-off via KSA**: Figure 10 demonstrates that KSA's mask threshold ε provides an intuitive control knob — increasing ε from 0 to 0.4 reduces latency from 16.99s to 15.26s and VRAM from 368MB to 242MB with only subtle detail degradation. This shows the method is not sensitive to hyperparameter tuning.

## Weaknesses

### Minor

1. **Understated F1 trade-off on Subject-Canny task**: The paper describes the F1 gap (Ours 0.414 vs. UniCombine 0.551) as a "minor exception of a narrow margin," but this is a ~25% relative drop in edge controllability. While PKA outperforms on all quality/consistency metrics on this same task (FID, SSIM, CLIP-I, DINOv2 by clear margins), the framing is too generous. The paper would benefit from acknowledging this as a trade-off — better visual quality and subject consistency at the cost of some edge-map precision — and discussing possible explanations (e.g., edge detector mismatch, different feature prioritization).

2. **PAA ablation lacks quantitative quality metrics**: Figure 9 compares PAA against full attention and sliding window attention only on latency and VRAM, with the quality claim supported solely by visual inspection ("both methods produce high-fidelity images"). While the full-system results in Table 1 validate overall quality, a quantitative control metric (e.g., F1 or MSE between condition and generated structure) in the PAA-specific ablation would more directly verify that the one-to-one approximation does not sacrifice spatial control quality in isolation.

3. **Early-timestep sampling lacks quantitative convergence evidence**: Figure 11 provides only visual comparisons across different (μ, δ) settings. No learning curves (e.g., loss, FID, or control metrics over iterations) are shown to quantify the convergence benefit. The perturbation analysis in Figure 5 grounds the motivation, but the central claim that this strategy "accelerates convergence" would be stronger with quantitative support.

4. **KSA mask reuse assumption not empirically validated**: The paper assumes temporal consistency of the relevance mask across consecutive timesteps (computing at t, reusing at t+1) and cites Zhou et al. 2025, but provides no experiment measuring mask overlap or comparing one-step versus reused masks. An IoU analysis across timesteps would validate that regions do not shift significantly between steps.

### Trivial

1. **Keyword selection process unspecified**: The paper states the keyword set 𝕂 "typically contains just 1 to 2 tokens" but does not describe how keywords are obtained from arbitrary prompts (e.g., noun extraction via parser, manual specification). This is a minor reproducibility gap.

2. **No limitations discussion**: The paper does not discuss scenarios where PKA might struggle (e.g., spatial conditions with long-range dependencies, ambiguous prompts for keyword masking).

3. **No confidence intervals in Table 1**: Given the modest training budget (20k iterations, batch size 1 with gradient accumulation 4), reporting variance across seeds would strengthen the quantitative evidence.

## Nice-to-Haves

- The paper could be strengthened by adding learning curves for the early-timestep sampling strategy (FID or control metric over iterations) rather than relying solely on visual comparisons.
- A mask IoU analysis between successive denoising steps would validate the KSA temporal consistency assumption.
- The Condition Cache mechanism is a reasonable engineering choice (standard KV caching in transformer decoding) and is noted as such; this does not detract from the paper's contributions.

## Removed Points

- **KSA mask reuse "fatal flaw" framing** (Harsh Critic #3): The critic frames this as potentially "silently degrading subject fidelity." This is speculative — the claim is not that mask reuse fails, but that it *could* fail. Given that the overall results (Table 1) show PKA achieves best subject consistency metrics (CLIP-I, DINOv2), any degradation from mask reuse is not empirically observed. Demoted from the critic's framing to Minor weakness.

- **"Condition Cache is not novel"**: While true that KV caching is standard, the paper does not claim this as a core novelty — it is presented as a structural consequence of the condition-token design. This is not a weakness; it is simply a practical implementation choice that the paper transparently describes.

- **Resolution handling concern** (PAA requires same spatial resolution): In DiTs with patch-based encoding, conditions are encoded at the same latent resolution as the noisy image. This is standard practice in the methods the paper builds on (OminiControl, UniCombine). Not a meaningful gap.

- **Strength about "early-timestep sampling accelerates convergence"** (from Strength Finder): Listed as a core strength, but the evidence is exclusively qualitative. I have largely moved this into the weakness section as lacking quantitative support.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Acknowledge the Subject-Canny F1 trade-off explicitly and discuss possible causes (e.g., edge detector sensitivity, PAA's one-to-one approximation being less suited to fine edge details than global attention).
2. Add F1/MSE metrics to the PAA ablation (Figure 9) comparing PAA against full attention on spatial control fidelity.
3. Include learning curves (FID or loss over iterations) for the early-timestep sampling study in Figure 11.
4. Validate KSA mask stability with an IoU analysis between consecutive denoising steps.
5. Specify the keyword extraction process (e.g., "we extract the first noun phrase from the prompt") for reproducibility.
6. Add a brief limitations section discussing when PKA may be less effective.

## Score and Decision

**Calibration anchors consulted:**
- Round 1: Jt1gGIumJo (3.00), rnTb9dm9zx (3.00), vK8C37eHXM (3.20), AjunxrcKa2 (3.40) — low band, much weaker papers
- Round 1: kALZASidYe (3.75), yPxhj1FKhG (3.67), 3Gga05Jdmj / CtrLoRA (6.00), gKui6QvvfK (5.25) — middle band
- Round 1: gU58d5QeGv (8.00), fV0t65OBUu (8.00), N8Oj1XhtYZ / SANA (8.50), OlzB6LnXcS (8.00) — high band, landmark papers
- Round 2: lWGXftRS5h (5.00), iG7qH9Kdao (5.00), leBbjaUxut (5.00), lTrrnNdkOX / Qihoo-T2X (6.40) — narrows bracket
- Round 2: D2as3jDmRA / LinFusion (6.25), lTrrnNdkOX / Qihoo-T2X (6.40), qmXedvwrT1 (6.67), cbv0sBIZh9 / MT-Diffusion (5.75) — further narrowing

**Round 1 bracket**: 5.0–7.0 (well above the 3.0–3.4 band, below the 8.0+ landmark band).

**Narrowing**: Compared to CtrLoRA (6.00), PKA has stronger motivational grounding and more novel technique. Compared to Qihoo-T2X (6.40), PKA is more focused with cleaner problem framing. Compared to LinFusion (6.25) and MT-Diffusion (5.75), PKA's results are similarly compelling. The paper's weaknesses (understated trade-off, lack of quantitative metrics in some ablations) are real but minor and addressable.

**Final score**: 6.0 — a solid paper with clear contributions, strong empirical efficiency results, and well-grounded motivation; the weaknesses are real but do not threaten the core claims.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
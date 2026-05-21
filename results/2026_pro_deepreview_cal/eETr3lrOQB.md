Now I have a thorough understanding of both the paper and the calibration anchors. Let me synthesize the final review.

---

## Summary

VQ-Transplant proposes a framework that decouples VQ module development from full tokenizer retraining by freezing a pre-trained encoder, substituting the VQ module, and then lightly adapting the decoder (5 epochs on ImageNet-1k). The paper also introduces MMD-VQ, a distribution-aligned quantization method using Maximum Mean Discrepancy. The framework achieves a 21.8× training speedup over the original VAR tokenizer while obtaining competitive or superior reconstruction fidelity (r-FID 0.81 vs. VAR's 0.92).

## Strengths

- **Genuine practical impact with massive efficiency gains**: The framework delivers a 21.8× reduction in total training time (22h on 2×A100 vs. 60h on 16×A100 for the original VAR) while achieving better r-FID (0.81 vs. 0.92). This directly addresses the computational barrier to VQ research that the paper identifies as its primary motivation.

- **Comprehensive empirical validation across VQ methods and configurations**: Five distinct VQ algorithms (Vanilla, EMA, Online, Wasserstein, MMD) are tested in both multi-scale and fixed-scale configurations, with detailed reporting of quantization error, codebook utilization, and reconstruction metrics at each stage (substitution and adaptation). The ablation on adaptation duration (Tables 4-5, Figure 3) shows consistent, controllable r-FID improvements from 1 to 20 epochs.

- **Strong cross-dataset generalization**: VQ-Transplant with Wasserstein VQ and MMD VQ transfers effectively to FFHQ, CelebA-HQ, and LSUN-Churches (Tables 8-10), achieving state-of-the-art reconstruction — notably r-FID of 1.21 on FFHQ, substantially outperforming prior full-training methods like VQGAN-LC (r-FID 3.81).

- **Clear demonstration that decoder adaptation is necessary and effective**: Table 3 shows that VQ substitution alone degrades reconstruction (MMD VAR r-FID 1.52 after substitution vs. VAR's 0.92), while just 5 epochs of decoder adaptation bring r-FID to 0.91 and surpass the original. This directly validates the core two-stage design.

## Weaknesses

### Fatal
None.

### Major

- **Missing control experiment for attribution of reconstruction gains**: The paper never evaluates what happens when the original VAR's decoder alone is fine-tuned on ImageNet-1k for the same 5-epoch protocol while keeping the native VQ module frozen. The original VAR tokenizer was trained on OpenImages, while VQ-Transplant's adaptation is performed on ImageNet-1k (an OpenImages subset). The improvement from VAR's 0.92 r-FID to MMD VAR's 0.81 r-FID could therefore partially reflect dataset-specific decoder adaptation rather than the VQ transplant itself. The paper shows in Table 6 that VQ-Transplant dramatically outperforms from-scratch MMD VAR training, which is strong evidence for the framework's value — but it does not isolate the contribution of VQ substitution from decoder dataset-adaptation. This weakens the specific claim that VQ-Transplant *with the new VQ module* is responsible for exceeding the original tokenizer's fidelity. The core efficiency contribution of the framework remains unaffected.

### Minor

- **Narrow tokenizer diversity for "plug-and-play" claim**: The framework is tested almost exclusively on the VAR tokenizer. The LDM-16 experiment is mentioned briefly (line 274) with "lower adaptability" noted and details relegated to Appendix D. Demonstrating successful transplants on at least one qualitatively different tokenizer architecture (e.g., a discrete tokenizer like VQGAN) would strengthen the generality claim. The current evidence primarily supports "VQ-Transplant works well with VAR" rather than the broader "plug-and-play for arbitrary pre-trained tokenizers."

- **Marginal practical advantage of MMD-VQ over Wasserstein VQ**: The empirical differences between MMD-VQ and Wasserstein VQ are small throughout. In Table 3 (multi-scale, K=4096, after adaptation), MMD VAR achieves r-FID 0.91 vs. Wasserstein VAR's 0.93; at K=8192, 0.81 vs. 0.83. The theoretical motivation for MMD over Wasserstein (non-parametric, no Gaussian assumption) is well-articulated, but the practical benefit in these settings appears modest. The paper would benefit from acknowledging this explicitly.

### Trivial

- Table 2 mixes baselines with different token counts and codebook sizes without explicit grouping or controlled comparison notes. The VAR row uses 680 tokens while fixed-scale VQ-Transplant rows use 512 tokens, which should be noted in the table discussion.

## Nice-to-Haves

- A downstream generative evaluation (e.g., training a small autoregressive model on tokens produced by VQ-Transplant) would substantially increase the paper's impact and better connect to the stated motivation that discrete tokenization ultimately serves generation.
- The weaker LDM-16 results should be surfaced in the main text as a limitation rather than only in the appendix.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic's claim about "secondary, related issue" of decoder adaptation-only controls for longer epochs**: The harsh critic suggested that if the original VAR decoder were adapted for 20 epochs, its r-FID might also keep decreasing. This is speculative — the paper already provides an extensive from-scratch vs. transplant comparison (Table 6) showing from-scratch training for 7 epochs yields far worse results. The missing control for the *original* VQ + decoder adaptation at 5 epochs is the real concern; extending this to 20 epochs is speculative and was removed.

- **Harsh critic's claim about "the plug-and-play generality is tested almost exclusively on a single pretrained tokenizer" being a "secondary, but related" issue that "weakens the claim"**: Kept but downgraded from the harsh critic's framing to Minor — the LDM-16 experiment does exist (just not detailed in the main text), and the VAR results are thorough.

- **Harsh critic's claim about "generative evaluation"**: Moved to Nice-to-Haves. The paper's scope is reconstruction quality and efficient VQ iteration; generative evaluation would strengthen but is not required for the core claims.

- **Harsh critic's mention of "legal/accessibility constraints of using industry-pretrained checkpoints"**: Removed. This is scope creep — the paper's goal is to democratize VQ research, and using publicly available checkpoints is standard practice. No specific legal issue is identified.

- **Strength Finder's generic strengths**: Several strengths about "the paper addressed an important problem" were removed as overly generic. Only concrete, evidence-backed strengths were retained.

## Novel Insights

The most interesting insight emerging from this work is that a frozen encoder from a high-quality pre-trained tokenizer provides a feature space rich enough that multiple VQ methods can be swapped in and achieve competitive reconstruction after only lightweight decoder adaptation. This suggests that encoder quality, rather than joint encoder-VQ optimization, is the dominant factor in tokenizer fidelity — a finding with implications beyond the specific framework proposed. The paper's demonstration that distribution-aligned VQ methods (Wasserstein, MMD) consistently achieve lower quantization error and higher codebook utilization after substitution compared to standard methods (Table 3) provides empirical guidance for future VQ design within transplant-style frameworks.

## Suggestions

- Add the decoder-only adaptation baseline for the original VAR tokenizer on ImageNet-1k using the same 5-epoch protocol. This single experiment would directly resolve the attribution concern. If the control underperforms VQ-Transplant, the paper's conclusions are strongly supported; if it performs similarly, reframe the contribution to emphasize that VQ-Transplant enables *changing the VQ method* while matching original fidelity — still a valuable contribution.
- Surface the LDM-16 results and limitations in the main text to give readers an honest picture of the framework's current generality.
- Acknowledge in the text that MMD-VQ and Wasserstein VQ perform similarly in practice, and that MMD-VQ's main advantage is theoretical robustness.

## Score and Decision

**Bracketing (Round 1):** The paper sits above the 5.75-tier anchors (BSQ tokenizer, variable-length token representations — both have significant experimental gaps) and below the 8.00-tier anchors (Rotation Trick for VQ — a cleaner contribution with stronger validation). Initial bracket: 6.0–7.5.

**Narrowing (Round 2):** Compared against Qinco2 (6.40), VQ-Transplant is comparable in quality but makes a more broadly impactful contribution. Compared against LARP (7.50) and Transformer-VQ (7.33), VQ-Transplant falls short due to the missing control experiment and narrower validation of generality. The paper lands between these clusters.

**Anchor comparison summary:**

| Anchor | Score | Round | Comparison |
|---|---|---|---|
| BSQ-ViT (yGnsH3gQ6U) | 5.75 | R1, R2 | VQ-Transplant stronger — more comprehensive experiments, clearer practical impact |
| Variable-length tokens (mb2ryuZ3wz) | 5.75 | R1, R2 | VQ-Transplant stronger — better results, more thorough ablations |
| BPE tokens (3TnLGGHhNx) | 6.00 | R1 | VQ-Transplant stronger — BPE had weak experimental evidence |
| Qinco2 (2zMHHZ569S) | 6.40 | R2 | Comparable; VQ-Transplant has broader impact but a notable evidential gap |
| LARP (Wr3UuEx72f) | 7.50 | R2 | VQ-Transplant weaker — LARP has cleaner validation of its core claims |
| Transformer-VQ (oDdzXQzP2F) | 7.33 | R2 | VQ-Transplant weaker — Transformer-VQ has theoretical backing and clean evaluation |
| Rotation Trick (GMwRl2e9Y1) | 8.00 | R1 | VQ-Transplant weaker — cleaner contribution, more thorough validation |

**Final assessment:** VQ-Transplant is a genuinely useful framework that addresses a real practical obstacle in VQ research. The efficiency gains are substantial and well-quantified. The experiments are comprehensive in breadth of VQ methods and datasets. The primary weakness — a missing control that would isolate the effect of VQ substitution from dataset-adaptation effects — is real but addressable, and does not undermine the framework's core efficiency contribution. The paper is a clear accept.

**Calibration note:** The score is set at 6.5, positioned above the 5.75–6.00 cluster (which had more significant experimental gaps) and Qinco2 (6.40, a solid but narrower contribution), but clearly below the 7.33–8.00 cluster (which had cleaner validation and fewer evidential gaps). The missing control prevents a higher score but the framework's practical value and experimental breadth prevent a lower one.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
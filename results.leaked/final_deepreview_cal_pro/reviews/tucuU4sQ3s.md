Now I have all the information I need. Let me synthesize the final review.

**Calibration summary:**

*Round 1 bracketing:*
- Low band (<3.5): JIlIYIHMuv (2.50), WM5G2NWSYC (2.00), gNoqEdT2wO (2.33), ZaudLwn0Hm (2.50) — all rejected, clearly weaker than NuSA-CL.
- Mid band (3.5–7.5): G9Ea7mlqGO (3.80, rejected, simple method, weak novelty), sb7qHFYwBc (6.50, C-CLIP, accepted, LoRA+distillation), TLADT8Wrhn (6.25, TiC-CLIP, benchmark paper), k9NYnsC4Mq (5.67, PROOF, rejected, inference mismatch issues).
- High band (>7.5): gc8QAQfXv6 (9.00, Function Vectors, deeply novel mechanistic interpretability), 3i13Gev2hV (8.00, hyperbolic embeddings), 1aF2D2CPHi (8.00), WyEdX2R4er (8.00).

*Initial bracket:* NuSA-CL is clearly above the 5.67–6.50 mid-range cluster but below the 8.0+ tier → **bracket: 6.5–8.0**.

*Round 2 narrowing:*
- Hcb2cgPbMg (6.25, Spectral Regularization): accepted, but reviewers noted marginal improvements and only graphical results. NuSA-CL is stronger on empirical thoroughness.
- mz8owj4DXu (6.50, Scalable LM): accepted, complex method, decent results. NuSA-CL is simpler and more elegant.
- sb7qHFYwBc (6.50, C-CLIP): NuSA-CL surpasses it on novelty, analysis depth, and efficiency results.
- kIP0duasBb (6.67, TTA with CLIP): less relevant topic.

NuSA-CL is better than all round-2 anchors. Given the thin theory and missing statistical rigor holding it below the 8.0 tier, the score lands at **7.0**.

---

## Summary
NuSA-CL proposes a memory-free continual learning method for vision-language models (CLIP) that constrains low-rank weight updates to an approximate null space of the current parameters, identified via SVD before each task. The update is then merged back into the backbone, maintaining a fixed parameter budget with zero external storage. The method achieves state-of-the-art performance among storage-free approaches on the MTIL benchmark and strong long-sequence scalability on class-incremental CIFAR-100, while using 1.5M trainable parameters and minimal GPU resources.

## Strengths

- **Novel and elegant core mechanism.** The three-stage cycle — SVD-based null-space identification, persistent constrained adaptation (ΔW = Uₙ M Vₙᵀ with only M trainable), and weight merging — is a clean, well-motivated design that distinguishes NuSA-CL from prior work which uses low-energy subspaces only for initialization (MiLoRA) or requires stored gradients (InflORA). The persistent constraint is the defining innovation.

- **Compelling efficiency–performance tradeoff.** Table 1 provides concrete evidence: NuSA-CL uses 1.5M parameters, 0 additional storage, 6.6 GB peak GPU memory, and 1.21 GPU-hours while achieving 68.6 Transfer / 75.1 Avg / 82.8 Last on the MTIL benchmark — the best among all storage-free methods and competitive with storage-based methods that require 40× more parameters (MoE-Adapters: 59.8M) or 39× more GPU-hours (ZSCL: 47.24).

- **Strong long-sequence scalability.** On the 50-step class-incremental CIFAR-100 benchmark (Table 3), NuSA-CL achieves 71.85% Last accuracy, a 4.4 percentage-point margin over the next-best method (ZSCL, 67.36%), demonstrating that the null-space adaptation remains effective even after 50 sequential tasks without spectral collapse.

- **Convincing spectral analysis of learning dynamics.** Figure 2 and associated appendix tables show that NuSA-CL's effective rank progressively increases across tasks (e.g., vision output layer from ~447 to ~454) while LoRA and Full-FT remain static, providing direct evidence of knowledge accumulation rather than overwriting. The analysis also shows the null space does not saturate — even after 10 tasks, the most saturated layer retains 313 null directions, more than double the update rank rₘₐₓ = 128.

- **Thorough ablation studies.** Table 4a validates the persistent constraint as essential (Transfer drops from 68.58 to 62.60 when Uₙ, Vₙ are unfrozen). Figure 3 demonstrates that the tail (null-like) subspace consistently yields lower forgetting than top or random subspaces across all ranks. Robustness to the energy cutoff ρ is established across a wide range (0.80–0.999).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **No statistical grounding reported.** No standard deviations, confidence intervals, or number of runs are provided for any result. Given that continual learning metrics are sensitive to optimization randomness and data sampling (and CIFAR-100 splits are class-order dependent), the reliability of reported margins — often 1–2% between methods — cannot be fully assessed. This is a moderate limitation but one that is common in the field and does not undermine the central findings.

- **Theoretical motivation is parameter-space only, not function-level.** The interference bound (Lemma 1 / Theorem 2) constrains the Frobenius inner product between a weight matrix and its update, which is a local stability condition. As the authors acknowledge, this does not guarantee that functional behavior on past tasks is preserved in a deep non-linear composition. The theory provides intuition but the paper's claims rest primarily on empirical evidence. The authors are appropriately cautious in their interpretation of the theory; the overstatement lies mainly in framing it as a "principled mechanism for mitigating catastrophic forgetting" when it is better described as a principled motivation.

- **Overstated language in the InflORA comparison.** Section 5.2 describes NuSA-CL as "decisively outperforming InflORA" on the 5-shot benchmark, but the actual margins are 1.3% (Transfer), 1.4% (Avg.), and 0.6% (Last) — modest differences that do not warrant "decisive." The comparison should be stated more precisely.

### Trivial

- The term "intrinsic null space" is imprecise — the tail singular vectors form a low-energy subspace, not a true null space (singular values are non-zero). "Low-energy subspace" would be more accurate.
- The variable `d` in Equation 1 (the rank computation) is used without explicit definition; it is presumably min(m, n) of the weight matrix.
- "The ultimate form of scalability" in the introduction is hyperbolic.

## Nice-to-Haves

- A capacity-matched LoRA variant (reducing LoRA rank or selective layer adaptation to match NuSA-CL's 1.5M parameter budget) would help isolate the effect of the null-space constraint from raw parameter reduction.
- A direct function-level interference measure (e.g., change in logit predictions on held-out past-task samples after each update) would complement the parameter-space analysis and strengthen the empirical validation.
- Sensitivity to task order is not examined; even a brief discussion or small experiment would strengthen the scalability narrative.

## Removed Points

These points from the input reviews were considered and removed:

- **"Parameter-count comparison conflates model design with the null-space constraint effect"** — REMOVED. The 1.5M vs 15.7M parameter difference is a direct consequence of the method design: NuSA-CL learns only an r×r matrix M per layer instead of the two projection matrices A (m×r) and B (r×n) used by LoRA. This is the method's contribution, not a conflation. The paper does specify which layers are adapted (Section 6.3: "attention projection matrices, e.g., W_q, W_k, W_v, W_o" on both encoders). A capacity-matched LoRA baseline would be nice-to-have but its absence does not invalidate the comparison.

- **"Core training hyperparameters absent from main text"** — REMOVED. The paper states the backbone (CLIP ViT-B/16), update rank cap (rₘₐₓ = 128), and energy cutoff threshold (ρ). The harsh critic assumed missing appendix content; the original submission includes implementation details. This is a parser artifact, not an author error.

- **"SVD memory footprint during training not discussed"** — REMOVED. Peak GPU memory is reported (6.6 GB) in Table 1, which already accounts for storing factorized bases during training. The data is on the page.

- **"CIFAR-100 protocol not fully detailed (class names as text prompts, classifier construction)"** — REMOVED. The paper uses CLIP's standard zero-shot classification protocol (text prompts with class names), which is standard and well-understood in the community. Requiring explicit re-description is a nitpick.

- **"The bound in Section 4 does not justify the claim that the constraint intrinsically protects prior knowledge"** — PARTIALLY RETAINED but downgraded to Minor. The paper explicitly qualifies the theory as "a local stability condition rather than a full function-level guarantee" (Section 4). The harsh critic's framing as a "structural weakness in the reasoning" overstates the issue given the authors' own hedging.

- **Strength Finder: "Proven memory-free efficiency" / "Strong scalability"** — RETAINED with evidence.

- **Strength Finder: "Null-space dynamics confirm accumulation" / "Ablation validates persistent constraint"** — RETAINED with evidence.

## Novel Insights

The paper's spectral analysis provides a genuinely interesting mechanistic picture: conventional fine-tuning (LoRA, Full-FT) leaves the spectral structure of weights nearly static — the effective rank barely changes — suggesting these methods primarily overwrite existing principal components. In contrast, NuSA-CL's null-space-constrained updates actively grow the effective rank by populating previously low-energy directions, offering a concrete spectral signature of knowledge accumulation vs. overwriting. This is a useful lens for understanding why the method works and could inform future work in continual learning.

## Suggestions

- Report mean and standard deviation over at least 3 runs for key results (especially MTIL Table 1 and CIFAR-100 Table 3). If multi-run evaluation is infeasible for MTIL given its scale, explicitly state this and note it as a limitation.
- Replace "decisively outperforming" with more measured language (e.g., "consistently outperforming") for the InflORA comparison.
- Define `d` explicitly in Equation 1 and consider replacing "intrinsic null space" with "low-energy subspace" for precision.
- Consider adding a capacity-matched LoRA baseline (reduced rank) as a supplementary experiment to further isolate the benefit of the subspace constraint.

## Score and Decision

**Anchor comparison:**
| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| JIlIYIHMuv | 2.50 | R1 | Far weaker — rejected, limited novelty |
| WM5G2NWSYC | 2.00 | R1 | Far weaker — rejected, vague method |
| G9Ea7mlqGO | 3.80 | R1 | Weaker — rejected, simple method, weaker evaluation |
| k9NYnsC4Mq | 5.67 | R1/R2 | Weaker — rejected, inference mismatch issues |
| Hcb2cgPbMg | 6.25 | R2 | Weaker — marginal improvements, only graphical results |
| TLADT8Wrhn | 6.25 | R1/R2 | Different category (benchmark paper) |
| sb7qHFYwBc | 6.50 | R1/R2 | Weaker — simpler LoRA+distillation method, less analysis |
| mz8owj4DXu | 6.50 | R2 | Comparable — but NuSA-CL has cleaner method, better efficiency |
| kIP0duasBb | 6.67 | R2 | Different category (TTA) |
| gc8QAQfXv6 | 9.00 | R1 | Stronger — deeper mechanistic insights, stronger theory |
| 3i13Gev2hV | 8.00 | R1 | Different topic (hyperbolic embeddings) |

**Bracket:** Round 1 placed the paper between 6.5 and 8.0. Round 2 narrowed to 7.0 — NuSA-CL is clearly stronger than all mid-range anchors (5.67–6.67) due to superior novelty, empirical thoroughness, and efficiency gains, but falls below the 8.0+ tier due to thin theoretical support, absence of statistical error characterization, and modest margins against some competitors.

**Score rationale:** The core method is novel, well-designed, and convincingly validated through strong empirical results and thoughtful spectral analysis. The weaknesses (no error bars, parameter-space-only theory, overstated language) are real but addressable and do not threaten the central contribution. NuSA-CL advances the state of memory-free continual learning for VLMs with a clean mechanism and compelling efficiency results.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
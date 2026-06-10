Now I have enough data to finalize my assessment. Let me compile the final review.

Based on calibration:
- **Round 1 bracket**: 6.5–8.0 (clearly above C-CLIP at 6.50, below top-tier VLM papers at 8.0)
- **Round 2 narrowing**: 6.5–7.5 (comparable to Concept Drift at 7.00, stronger than Spectral Regularization at 6.25)

**Comparison with anchors:**
- vs. C-CLIP (6.50): NuSA-CL has a more principled method, stronger results (10× fewer params, better performance), comprehensive ablations, and theoretical grounding. Clearly stronger.
- vs. Spectral Regularization (6.25): NuSA-CL has more comprehensive experiments, clearer practical contribution, and stronger results. Stronger.
- vs. Concept Drift (7.00): NuSA-CL has cleaner methodology, more comprehensive CL experiments, and clearer contribution framing. Comparable or slightly stronger.
- vs. Second-Order Compositionality (7.50): Different focus but NuSA-CL's practical impact is narrower (single backbone). Slightly weaker.

**Final score: 7.0**

---

## Summary
This paper proposes NuSA-CL, a memory-free continual learning framework for vision-language models that constrains LoRA-style weight updates to the approximate null (low-energy) subspace of current weight matrices identified via SVD. The persistent constraint—freezing the null-space basis vectors U_n and V_n while training only a small intermediate matrix M—enables stable sequential adaptation with a fixed parameter budget through weight merging. Experiments on MTIL (11 vision datasets), 5-shot MTIL, and class-incremental CIFAR-100 with CLIP ViT-B/16 demonstrate competitive performance with storage-based methods while using 10–40× fewer parameters and zero external storage.

## Strengths
- **Dramatic parameter efficiency with strong performance.** Table 1 shows NuSA-CL uses only 1.5M trainable parameters (vs. 15.7M for LoRA/MiLoRA, 59.8M for MoE-Adapters) yet achieves the best Transfer (68.6%), Avg. (75.1%), and Last (82.8%) among all storage-free methods, closely matching storage-based SOTA (MoE-Adapters: 68.9/76.7/85.0) at a fraction of the cost.
- **Persistent constraint validated by controlled ablation.** Table 4a shows that unfreezing U_n and V_n causes steep degradation: Transfer drops from 68.58 to 62.60 and Last from 82.79 to 77.32, directly confirming the persistent constraint is the critical mechanism distinguishing NuSA-CL from initialization-only approaches like MiLoRA.
- **Tail subspace consistently outperforms Top and Random.** Figure 3a shows Tail achieves the lowest forgetting at every tested rank (e.g., 2.57% vs. 4.44% vs. 4.57% at r=128), providing direct evidence for the paper's core premise that low-energy spectral directions form a lower-interference region.
- **Strong scalability on long task sequences.** Table 3 shows NuSA-CL's advantage widens with sequence length on CIFAR-100: at 50 steps, it achieves 71.85% Last vs. ZSCL's 67.36% (+4.49%), validating the dynamic null-space recomputation strategy for lifelong learning.
- **Quantitative spectral analysis (Figure 2).** Tracks effective rank and null ratio across 10 tasks, showing NuSA-CL's effective rank progressively increases while LoRA and FullFT remain static—direct mechanistic evidence that NuSA-CL accumulates knowledge in underutilized dimensions rather than overwriting principal components.
- **Fair comparison protocol.** Re-implements LoRA, MiLoRA, and InflLoRA within a unified CLIP framework with consistent rank and post-task merging (Section 5.1), reducing confounds from implementation differences.

## Weaknesses

### Fatal
None.

### Major
- **Single model scale limits the significance of scalability claims.** All experiments use CLIP ViT-B/16 (Section 5.1: "All experiments use the CLIP ViT-B/16 backbone"). The paper's central claim about "the ultimate form of scalability" rests on a single, relatively small backbone. The SVD step scales cubically with dimensionality, and null-space dimension behavior could differ for larger models. The paper acknowledges this (Section 7) and provides scaling guidance (Section 5.1), but even one larger-scale experiment would substantially strengthen the narrative.

- **Theoretical bounds lack empirical verification of key quantities.** Lemma 1 (Eq. 5) bounds |⟨W, ΔW⟩_F| ≤ σ_max^null · ‖M‖_F, and Theorem 2 sums this across tasks. However, the actual values of σ_max^null are never reported. Since the paper's motivation hinges on the null space having small singular values relative to dominant ones (Section 3.1), reporting these quantities alongside the effective rank analysis (Figure 2) would turn the theoretical section from plausible motivation into empirically grounded theory. The paper honestly notes the bounds are "local stability conditions rather than function-level guarantees" (Section 4.2), which is commendable, but the bound quantities themselves remain unexamined.

### Minor
- **Ambiguous ablation setup for subspace selection.** Section 6.2 describes comparing "three low-rank initialization strategies—Top, Tail, and Random," but the word "initialization" raises the question of whether U_n and V_n are frozen across all three conditions or only for Tail. Table 4a separately validates the persistent constraint, so this ambiguity doesn't undermine the paper's claims, but clarifying the setup would strengthen the analysis.

- **Default hyperparameter ρ = 0.95 not stated in implementation.** Section 5.1 states r_max = 128 but does not explicitly state the energy cutoff threshold ρ. This can only be inferred from Table 4b (where ρ = 0.95 is bolded). For reproducibility, this should be stated in Section 5.1.

- **Non-standard use of "null space" terminology.** The paper uses "null space" to mean "low-energy spectral subspace" rather than the standard linear algebraic definition (the kernel of the linear map). The paper signals this with "intrinsic null space" and "approximate null space" (Section 3.1), but a brief explicit clarification would help readers from different backgrounds.

### Trivial
None.

## Nice-to-Haves
- Reporting σ_max^null values across layers and tasks to directly validate the theoretical narrative.
- Reporting the rank of each layer's actual null space (d − k) to show whether any layers have d − k < r_max = 128.
- Brief preliminary analysis of task ordering sensitivity (acknowledged as future work in Section 7).

## Removed Points
These points are flagged to be removed, treat them with caution:
- None removed. All points from the harsh critic and strength finder were verified against the paper and either kept or would have been removed for being already addressed.

## Novel Insights
The most novel observation is that the persistent null-space constraint (not just initialization there) is the key differentiator, validated by both the controlled ablation (Table 4a) and the spectral dynamics analysis (Figure 2). The progressive increase in effective rank under NuSA-CL—compared to static behavior under LoRA/FullFT—provides a compelling mechanistic explanation: the method actively accumulates knowledge into underutilized spectral directions rather than overwriting existing principal components. This spectral accumulation vs. overwriting distinction is a useful conceptual framing for the continual learning community.

## Suggestions
- Add experiments on at least one larger CLIP backbone (e.g., ViT-L/14) to substantiate scalability claims.
- Report σ_max^null values across layers and tasks to empirically verify the theoretical bounds.
- Explicitly clarify whether the subspace selection ablation (Section 6.2) applies the persistent constraint uniformly across Tail, Top, and Random conditions.
- State ρ = 0.95 explicitly in Section 5.1 for reproducibility.

## Calibration Report

**All retrieved anchors:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| JIlIYIHMuv (LVLM-CL) | 2.50 | 1 | Much weaker method and experiments; NuSA-CL is clearly stronger |
| WM5G2NWSYC (Projected Subnetworks) | 2.00 | 1 | Weak contribution; NuSA-CL is far stronger |
| gNoqEdT2wO (MCIL Benchmark) | 2.33 | 1 | Benchmark-only paper with limited methodology; NuSA-CL much stronger |
| TxIrMD6lAN (Task-Specific Adapters) | 3.00 | 1 | Simpler method, weaker results; NuSA-CL clearly stronger |
| k9NYnsC4Mq (PROOF) | 5.67 | 1 | Expansion-based approach; NuSA-CL has stronger results and more principled method |
| 9aZ2ixiYGd (Vision-Language Synergy) | 5.00 | 1 | Prompt-based; NuSA-CL has broader evaluation and stronger results |
| EKfcngSxwD (Task Codebook) | 4.67 | 1 | Weaker experiments; NuSA-CL clearly stronger |
| sb7qHFYwBc (C-CLIP) | 6.50 | 1 | Similar setting but simpler method (LoRA + contrastive loss); NuSA-CL is more principled with stronger results |
| bqv7M0wc4x (ICL-TSVD) | 5.50 | 2 | Theory-practice bridge but different focus; NuSA-CL has stronger practical contribution |
| 9vkgAaCI3F (RDAC) | 5.25 | 2 | Analysis framework, not a method paper; different contribution type |
| u3dHl287oB (Task Similarity & Overparameterization) | 5.67 | 2 | Theoretical analysis paper; NuSA-CL has stronger empirical contribution |
| Hcb2cgPbMg (Spectral Regularization) | 6.25 | 2 | Similar spectral theme but marginal improvements; NuSA-CL has stronger results and clearer contribution |
| b20VK2GnSs (Concept Drift) | 7.00 | 2 | Comparable quality but different focus (pre-training adaptation); NuSA-CL has cleaner methodology |
| OZVTqoli2N (Second-Order Compositionality) | 7.50 | 2 | Stronger theoretical contribution; NuSA-CL has narrower but solid practical impact |
| dOAkHmsjRX (Budgeted Online CL) | 7.50 | 2 | Different focus (online CL with FLOP budget); NuSA-CL comparable in quality |
| 9bMZ29SPVx (CLIP Data Selection) | 7.50 | 2 | Different focus; NuSA-CL is comparable but with narrower scope |

**Round 1 bracket**: 6.5–8.0. The paper is clearly above rejected papers (2–3 range) and accepted-but-weaker CL papers (5.0–6.5), but below top-tier VLM analysis papers (8.0).

**Round 2 narrowing**: 6.5–7.5. NuSA-CL is stronger than C-CLIP (6.50) and Spectral Regularization (6.25) due to more principled methodology, stronger results, and comprehensive ablations. Comparable to Concept Drift (7.00) but with cleaner experimental methodology. Slightly below the 7.50 anchors which have either stronger theoretical depth or broader scope.

**Final score: 7.0** — The paper is a solid, well-motivated contribution with a novel mechanism (persistent null-space constraint), strong empirical validation, and comprehensive ablations. The main weaknesses (single model scale, unverified theoretical bounds) are real but fixable and do not undermine the core contribution.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
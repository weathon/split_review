Now I have enough calibration data. Let me finalize the review and score.

**Calibration summary:**
- TensorGPT (3.75, Reject): WASI clearly stronger — better experiments, real hardware, broader scope
- "Activations Aren't Cheap in LoRA" (4.25, Reject): WASI better — genuine novel framework vs. reformulation
- "Unlocking SVD-Space" (4.40, Reject): WASI better — more practical validation
- LoRA-FA (5.33, Reject): Comparable — both achieve memory savings, both have missing baselines and presentation gaps. WASI achieves larger savings (62×) and has real hardware validation
- TinyTrain (5.25, Reject): Comparable — both on-device training, similar experimental limitations
- Zeroth-Order FT (5.80, Accept): Similar novelty level, similar issue patterns (limited datasets, unfair comparisons noted by reviewers), but accepted
- Differentiable Learning (5.67, Accept): WASI has stronger practical validation

WASI is clearly above the 3.75-4.40 rejects, comparable to LoRA-FA (5.33, rejected) but with stronger hardware validation, and slightly below Zeroth-Order FT (5.80, accepted) due to more severe baseline gaps. My score: **5.0**.

## Summary
This paper proposes WASI (Weight-Activation Subspace Iteration), a method for efficient on-device training of transformer models by jointly compressing both weight matrices and activation maps into stable low-rank subspaces via warm-started subspace iteration. WASI combines prior ASI (activation compression) with a new WSI (weight compression) component, and is evaluated on ViT, SwinT, and TinyLlama with on-device latency measurements on a Raspberry Pi 5.

## Strengths
- **Well-validated foundational assumptions**: Figure 3a demonstrates remarkable stability of weight ranks across 40 training epochs during ViT fine-tuning on Pets. Figure 3b shows WSI requires 1.36× fewer FLOPs than full SVD while achieving 35.36% higher accuracy at matched FLOP budgets. Figure 4 confirms activation energy concentrates in first few singular values. Together these provide strong empirical grounding for the method's core premise.
- **Joint weight-activation compression is a genuine advance over prior work**: Unlike ASI (activations only) or SVD-LLM (weights only via LoRA adapters), WASI compresses both. Figure 5 shows WASI achieves up to 100× higher memory efficiency than SVD-LLM at similar accuracy on ViT/CIFAR-10, because it avoids co-storing frozen weights alongside LoRA adapters.
- **Real-world hardware validation**: Figure 8 reports wall-clock timing on a Raspberry Pi 5 (Cortex-A76, 8GB RAM), showing WASI achieves ~1.4× speedup over vanilla training even at the least aggressive compression (ε=0.9). This goes beyond simulation-based FLOP counts and demonstrates practical deployability.
- **Substantial resource reductions across diverse architectures**: Figure 6 shows up to 62× memory reduction on SwinT across five datasets (CIFAR-10/100, CUB, Flowers, Pets) at ε=0.9 without accuracy loss. Figure 7 extends to TinyLlama showing up to 953.86× activation memory reduction.
- **Dynamic programming rank-search improvement**: Replacing ASI's brute-force exponential rank search with a DP strategy (Appendix A.2) is a concrete algorithmic improvement for practical on-device deployment.

## Weaknesses

### Fatal
None

### Major
- **Critical algorithmic mechanism deferred entirely to appendix**: The factored weight update (Eq. 11) is the operational core of WASI, yet how the gradient $\overline{\partial \mathcal{L}/\partial \mathcal{W}_i}$ is computed and represented in factored $(L_i, R_i)$ form is described only as "a linear operator applied in the low-rank space (see Appendix A.1)" at line 159. Adding a full-rank gradient to $L_i R_i$ would destroy low-rank structure; if projected, the projection has cost and approximation implications. The main text provides no description of this mechanism — not even a one-sentence summary. While the appendix exists in the original submission, a reader evaluating soundness from the main text alone cannot assess whether the method handles this correctly.

- **Missing LoRA baseline**: LoRA is discussed extensively in Related Work (lines 41-45) as the most prominent low-rank training method, with the paper noting its drawbacks (co-existing frozen weights + adapter increases training memory; merged weights lose inference benefits). Yet these drawbacks are precisely what a quantitative comparison should demonstrate. Excluding the most widely-used low-rank training baseline is a significant gap for a method claiming to advance the state of the art in low-rank transformer training.

- **Thin TinyLlama experiment undermines generality claim**: The TinyLlama experiment (Sec. 4.3) tests only ε=0.1, only the last 5 layers, and only BoolQ, justified by "limited resources" (line 227). The accuracy range (64–66%) is extremely narrow, and the headline compression ratios (953.86× activation memory, 30.27× inference FLOPs) come from this single aggressive configuration without multiple ε values, multiple datasets, or variance estimates. This is the primary evidence that WASI generalizes beyond vision transformers.

### Minor
- **"Up-to" claims from disjoint experiments**: The abstract cites "up to 62× memory" (SwinT at ε=0.9) and "up to 2× FLOPs" from different experiments and architectures. A consolidated table at a fixed ε across all model-dataset combinations would let readers assess typical savings rather than cross-referencing multiple figures with different axes.

- **Single-run results with no variance reporting**: All results appear to be single runs. For small accuracy differences (e.g., 64–66% on TinyLlama), mean ± std over multiple runs would strengthen confidence.

- **Attention layers excluded from main measurements**: Line 177 notes focus on "linear layers within multi-perceptron blocks." Since attention is a major component of transformer memory/compute, the main results may overstate savings for real workloads. Extended results in Appendix B.3, but the main paper should note what fraction of total memory/compute is captured.

- **SwinT figure lacks ablation baselines**: Figure 6 shows only WASI vs. vanilla for SwinT, with ASI and SVD-LLM pushed to the appendix. Since WASI = WSI + ASI, showing ASI alone in the main paper is essential to understand how much gain comes from the novel WSI component versus prior ASI work.

## Nice-to-Haves
- A summary table presenting accuracy-memory-FLOPs trade-offs at ε=0.9 across all model-dataset combinations would replace scattered "up-to" claims with a coherent picture.
- Including ASI-only results in Figure 6 (SwinT) would complete the ablation: WASI vs. ASI individually.
- At least a one-paragraph description of how gradients are projected into the (L, R) factorization in the main text would let readers evaluate soundness without cross-referencing the appendix.

## Removed Points
These points are flagged to be removed, treat them with caution:
- The harsh critic's concern about SVD-LLM being "applied outside its domain" is mitigated: the paper explicitly acknowledges this (line 47, Appendix A.4) and applies the same compression ratios for fairness. Using it as a baseline is reasonable.
- The harsh critic's point about the appendix being "missing" is invalid per filtering rules — the appendix exists in the original submission; the parser stripped it.

## Novel Insights
The key insight is the observation that both weight and activation subspaces remain remarkably stable during transformer fine-tuning (validated in Fig. 3a), which allows computing expensive SVD once and reusing the subspace via cheap iteration thereafter. The 35% accuracy advantage of WSI over full SVD at matched FLOPs (Fig. 3b) is particularly compelling — it demonstrates that warm-started subspace iteration not only saves compute but actually improves convergence quality, likely because it implicitly regularizes toward the pre-trained subspace.

## Suggestions
- Add a one-paragraph summary of $f_{LR}$ and the factored gradient mechanism in Section 3.3.
- Include LoRA as a baseline in the main experimental results.
- Strengthen the TinyLlama experiment by varying ε (even 3 values) and reporting variance.
- Add ASI to Figure 6 (SwinT) to complete the ablation in the main paper.
- Create a consolidated table at ε=0.9 showing accuracy, memory savings, and FLOPs reduction across all model-dataset pairs.

## All Retrieved Anchors

| Round | Path | Avg Score | Comparison |
|-------|------|-----------|------------|
| 1 | E4Fk3YuG56.md (Cut Your Losses) | 2.67 | Different topic; not directly comparable |
| 1 | 04RLVxDvig.md (NanoMoE) | 3.00 | WASI clearly stronger — better validation |
| 1 | b7HOhqXiZs.md (DeMo) | 2.60 | WASI clearly stronger |
| 1 | ZTvUT49JjL.md (Implicit Bias) | 3.40 | WASI clearly stronger — more practical |
| 1 | FVgizbs3o2.md (TensorGPT) | 3.75 | WASI stronger — broader scope, hardware validation |
| 1 | 7Cx05z4pUc.md (Decomposed Learning) | 5.00 | Similar range; WASI has more practical relevance |
| 1 | pAVJKp3Dvn.md (Differentiable Learning) | 5.67 | WASI comparable but with more practical validation |
| 1 | RtzxJLPxGk.md (Adapprox) | 6.40 | WASI weaker — Adapprox has more thorough experiments |
| 1 | TwJrTz9cRS.md (HiRA) | 8.00 | WASI clearly weaker — HiRA has cleaner ablations |
| 1 | vf5aUZT0Fz.md (DEPT) | 8.00 | WASI clearly weaker |
| 1 | d8w0pmvXbZ.md (Small-scale proxies) | 8.00 | WASI clearly weaker |
| 1 | t7P5BUKcYv.md (MoE++) | 8.00 | WASI clearly weaker |
| 2 | 8Agcic0csh.md (Unlocking SVD-Space) | 4.40 | WASI stronger — better hardware validation |
| 2 | 3KEwJGYNzH.md (AutoTrunc) | 4.00 | WASI stronger |
| 2 | FVgizbs3o2.md (TensorGPT) | 3.75 | (duplicate of round 1) |
| 2 | 3ylNuZXtMg.md (Activations Aren't Cheap) | 4.25 | WASI stronger — novel framework vs reformulation |
| 2 | xNdE7RiRyP.md (TinyTrain) | 5.25 | Comparable — similar limitations |
| 2 | xzSUdw6s76.md (PalmBench) | 5.80 | Different type (benchmark); not directly comparable |
| 2 | myYzr50xBh.md (Zeroth-Order FT) | 5.80 | Similar novelty level; accepted with similar issues |
| 2 | RbKThNNFxr.md (LoRA-FA) | 5.33 | Most comparable — similar scope, similar gaps |

**Round-1 bracket**: 4.5–6.5. WASI was clearly above the 3.75–4.40 rejects and below the 8.0 accepts.

**Round-2 narrowing**: LoRA-FA (5.33, Reject) is the closest anchor — both propose memory-efficient training, both have missing baselines and presentation gaps. WASI achieves larger savings (62× vs 1.4×) and has real hardware validation, but has a more severe missing baseline (LoRA) and thinner secondary experiment (TinyLlama). Zeroth-Order FT (5.80, Accept) has similar issue patterns but was accepted. WASI sits between LoRA-FA (5.33) and Zeroth-Order FT (5.80), closer to LoRA-FA given the deferred mechanism and missing LoRA baseline. Final score: **5.0**.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
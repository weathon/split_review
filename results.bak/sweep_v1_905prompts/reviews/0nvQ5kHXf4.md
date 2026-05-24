Now I have all the information needed. Let me compile the final consolidated review.

## Summary

This paper introduces WASI (Weight-Activation Subspace Iteration), a method that jointly compresses transformer weights and activations into low-rank subspaces during fine-tuning. The key insight is that the parameter subspace remains stable across training iterations, so expensive SVD can be replaced by cheaper subspace iteration. WASI is evaluated on ViT, SwinT, and TinyLlama across multiple datasets, with on-device validation on a Raspberry Pi 5. The method achieves up to 62× memory reduction and 1.4× speedup over vanilla training while maintaining accuracy.

## Strengths

- **On-device speedup validated on real hardware**: Section 4.4 (Fig. 8) shows WASI achieves ~1.4× faster training and inference per iteration on a Raspberry Pi 5 at ε=0.9, directly demonstrating feasibility on the kind of resource-constrained device the method targets. This moves beyond simulation.

- **Large memory reductions with accuracy preservation**: For SwinT at ε=0.9, WASI cuts memory by up to 62× and FLOPs by 1.5× while matching vanilla accuracy, and even slightly exceeding it on CUB (Sec. 4.3, Fig. 6). The trend across five datasets is consistent.

- **Generalization to decoder-only LLM**: WASI is tested on TinyLlama with BoolQ, showing activation memory drops of 953.86× and weight memory drops of 30.12× over fine-tuned layers, with no accuracy loss (Sec. 4.3, Fig. 7). This demonstrates the method is not architecture-specific.

- **Theoretical complexity analysis**: Section 3.4 and Figure 2 provide closed-form expressions for compression rates and speedup ratios as functions of rank and feature dimensions, giving practitioners a principled way to predict resource gains before deployment.

- **Better accuracy-efficiency trade-off than prior partial approaches**: WASI (joint weight+activation compression) outperforms both activation-only ASI and weight-only SVD-LLM in memory efficiency at comparable accuracy (Fig. 5), validating the benefit of joint compression.

- **Core algorithmic assumption is empirically supported**: Fig. 3a shows layer ranks remain stable across 40 fine-tuning epochs, and Fig. 3b shows WSI achieves 1.36× lower FLOPs than repeated SVD at the same accuracy, supporting the subspace stability hypothesis that motivates the method.

## Weaknesses

### Fatal
None.

### Major
None that invalidate the core claims. See Minor section for the most significant concerns.

### Minor

- **Subspace stability evidence is incomplete**: The paper validates only rank (scalar) stability via singular values (Fig. 3a), not the stability of the singular *vectors* themselves. Since WSI reuses left/right factor matrices (L, R) across iterations, even moderately rotating singular vectors would cause the approximation to drift. The WSI-vs-SVD comparison (Fig. 3b) provides indirect practical evidence, but direct cosine-similarity tracking between factor matrices across iterations would be more conclusive. This does not invalidate the results — the empirical performance is clear — but it would strengthen the theoretical grounding.

- **Backward-pass and rank-selection details are underspecified**: Equations (8)-(11) describe the forward pass through decomposed weights and compressed activations, but the backward computation of gradients through the joint decomposition is only sketched ("f_LR(·) denotes a linear operator applied in the low-rank space," citing the appendix). The perplexity-based rank-selection strategy (Sec. 3.3) is mentioned for ASI but not explained for the vision setting — perplexity is a language metric and its mapping to vision tasks is not justified. Code is provided, which mitigates reproducibility concerns, but the paper itself should be self-contained on these points.

- **Initial SVD cost is not reported**: WSI performs a full SVD at iteration 0 (Algorithm 1). On a resource-constrained device, this one-time cost could be substantial, yet it is not measured or factored into the reported speedups or memory savings. For the on-device scenario the paper targets, reporting total training time (including initialization) would be important.

- **TinyLlama results use partial-model evaluation**: The paper honestly states "we only fine-tune up to the last 5 layers" and "log the resource consumption only at the layers that are fine-tuned" (Sec. 4.3). The headline 953.86× activation memory reduction applies only to those layers, not the full model. While the context is provided in-text, readers could over-interpret this number; a full-model memory breakdown would clarify the practical benefit.

- **Limited on-device evaluation scope**: Only one model-dataset combination (ViT on CIFAR-10) is tested on real hardware, and the reported Fig. 8 bars lack error bars or confidence intervals. Additional combinations (e.g., SwinT on a downstream dataset) and variance estimates would strengthen the deployment claims.

- **No comparison against subnetwork fine-tuning or LoRA+activation-compression baselines**: The paper compares against ASI and SVD-LLM, but on-device training methods like subnetwork fine-tuning (Lin et al., 2022) or LoRA with activation compression would better isolate WASI's specific contribution. This gap does not undermine the reported results, but it limits the paper's ability to claim WASI is the best approach for the setting.

### Trivial

- Figure labels "m" and "B" in the legend of Fig. 2 are not explicitly defined in the caption (though "B" is batch size from context).
- The claim "first method for efficient model-activation-decomposition-aware training" in the introduction is somewhat overstated — prior work jointly compressed weights and activations in other settings — but this does not affect the technical contribution.

## Nice-to-Haves

- An ablation study separating the contributions of weight compression (WSI) from activation compression (ASI) to quantify which component drives the savings.
- Tabular results (accuracy, peak memory, FLOPs per ε) to complement the figures, which are sometimes dense with overlapping curves.
- Confidence intervals or variance estimates across multiple training runs for the main results.
- A comparison including subnetwork methods and LoRA variants to contextualize WASI within the broader on-device training landscape.

## Removed Points

- **"ASI is an adapted baseline"** — The paper explicitly states they extend their own prior work (ASI) to support 3D activation tensors (Sec. 3.3). This is a reasonable and transparent modification, not an unfair comparison.
- **"SVD-LLM cannot be directly applied"** — The paper acknowledges this limitation (Sec. 2, App. A.4) and notes it applies the same compression ratios for fairness. The adaptation is necessary to create a comparable baseline.
- **"953× numbers are misleading without context"** — The paper clearly states in the TinyLlama section that resource consumption is logged only for fine-tuned layers. The abstract and conclusion reference only the 62× number from SwinT (full-model), not the 953× number.
- **Missing related works** — Cannot verify without external sources.
- **Formatting nitpicks** (small markers, unclear axes, figure readability) — Parser artifacts or minor presentation issues that do not affect the scientific contribution.
- **Reproducibility concerns about undisclosed hyperparameters** — Code is provided; basic training details are in the paper and appendix.
- **"First method" overstatement** — While slightly ambitious, this is a framing choice common in papers and does not affect the validity of the technical contribution.

## Novel Insights

None beyond the paper's own contributions. The core observation — that the joint subspace of weights and activations remains stable during fine-tuning, enabling cheap subspace iteration for both — is the paper's genuine insight, and it is already presented as the central contribution.

## Suggestions

- Add direct cosine-similarity tracking between WSI factor matrices (L, R) across consecutive iterations (e.g., for 2-3 layers) to directly validate singular-vector stability, not just rank stability.
- Provide a full-model memory breakdown for TinyLlama (fine-tuned layers + frozen layers) alongside the per-layer numbers, to give a complete picture of the deployment memory footprint.
- Report the cost (time/FLOPs) of the initial full SVD at iteration 0 and include it in the total training budget comparison against vanilla training.
- Clarify how the "pre-tuning perplexity" heuristic maps to vision tasks, or replace it with a vision-natural metric (e.g., reconstruction MSE threshold).
- Add error bars or multiple-run statistics to the Raspberry Pi 5 latency results (Fig. 8).

## Calibration Anchors

**Round 1 (Bracketing):**
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| igGeaxOiFM (HoLoRA) | 3.00 | 1 | Weaker — incremental LoRA variant with thinner evaluation |
| xi3sDtf8A0 (L-MSA) | 3.00 | 1 | Weaker — layer selection only, no on-device validation |
| 04RLVxDvig (NanoMoE) | 3.00 | 1 | Weaker — limited scope and evaluation |
| ulGwcj1egv (FiRST) | 3.00 | 1 | Weaker — latency reduction only, no training efficiency |
| xNdE7RiRyP (TinyTrain) | 5.25 | 1 | Similar domain (on-device training) but for CNNs/MCUs; WASI has stronger theoretical grounding and targets transformers |
| 8Agcic0csh (SVD-Space Align.) | 4.40 | 1 | Related SVD-based training but has major flaws (wrong proofs, weak evaluation); WASI is more sound |
| 1RrOtCmuKr (JLCM) | 6.33 | 1 | Different task (inference compression via quantization); higher quality but less directly comparable |
| 7Cx05z4pUc (Decomposed Learning) | 5.00 | 1 | SVD-based learning but on toy tasks; WASI has broader evaluation |
| TwJrTz9cRS (HiRA) | 8.00 | 1 | Higher quality PEFT paper but different focus (LLMs, not training efficiency) |
| vf5aUZT0Fz (DEPT) | 8.00 | 1 | Higher quality pre-training paper; not comparable |
| E4Fk3YuG56 (Cut Your Losses) | 8.50 | 1 | Higher quality but addresses a different problem (cross-entropy memory) |
| TJo6aQb7mK (Spectra LLM) | 7.60 | 1 | Higher quality but different focus (ternary pretraining) |

**Round 2 (Narrowing):**
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| E5YmIBvOqV (Filter Subspace) | 6.00 | 2 | Accepted. Cleaner PEFT paper for CNNs. WASI targets a harder problem (on-device training of transformers) with hardware validation, but has more method-description gaps |
| 5btFIv2PNb (LoR-VP) | 6.33 | 2 | Accepted. Visual prompting via low-rank. Thorough evaluation but different problem. WASI comparable in quality |
| DM6Q45HWSk (EVA) | 4.75 | 2 | Rejected. LoRA initialization method with marginal gains; WASI has stronger empirical evidence |
| pAVJKp3Dvn (GBLR) | 5.67 | 2 | Accepted. Methodologically rich structured matrices paper; WASI has stronger deployment validation |
| hHNVn4hFPk (Compress then Serve) | 5.25 | 2 | Rejected. LoRA serving compression; narrower scope |

**Round-1 bracket:** 4.5–6.5. **Round-2 narrowing:** The paper is stronger than the ~4.75 rejected anchors (EVA, SVD-Space Alignment) and comparable to the ~5.67–6.0 accepted anchors (GBLR, Filter Subspace). It is weaker than the ~6.33+ anchors (JLCM, LoR-VP) which have more complete evaluation or cleaner exposition. The method gaps (backward-pass details, rank-selection clarification) and evaluation limitations (partial TinyLlama, single on-device combination) prevent it from reaching the 6+ acceptance tier. The score reflects a paper with genuine contributions and solid empirical support, but with presentation and evaluation gaps that need addressing.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
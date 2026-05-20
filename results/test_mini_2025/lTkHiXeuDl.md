## Summary

HMoRA augments LoRA with a mixture-of-experts architecture featuring (1) a hierarchical hybrid routing scheme where shallow layers emphasize token-level routing and deeper layers emphasize task-level routing, controlled by a layer-dependent mixing coefficient α⁽ˡ⁾; (2) a Constrained Generalized Jensen-Shannon (CGJS) divergence auxiliary loss that simultaneously improves routing certainty and expert balance; and (3) optional lightweight designs that reduce trainable parameters. Evaluated on Flan v2 multi-task instruction tuning and seven NLP benchmarks, HMoRA with lightweight designs (3.9% trainable parameters) achieves 63.88 average accuracy vs. full fine-tuning's 63.15, while the full version reaches 64.16.

---

## Strengths

1. **Hierarchical hybrid routing motivated by LLM layer properties.** The paper identifies that prior multi-granular routing methods treat all layers uniformly, whereas LLMs capture token-level features in shallow layers and semantic-level features in deeper layers (Geva et al., 2021). HMoRA's layer-dependent α⁽ˡ⁾ = σ(−ε + 2ε·l/L + μ) (Eq. 8) directly addresses this, and Appendix E.5 (referenced) shows that setting ε > 0 (increasing α with depth) improves performance over uniform mixing. This is a principled architectural insight.

2. **CGJS auxiliary loss that simultaneously handles certainty and balance.** The CGJS divergence (Eq. 11) with separate hyperparameters γ_b (balance cap) and γ_c (certainty cap) is a novel formulation. Table 1 shows it outperforms both the no-loss baseline (62.83→63.65 for soft, 62.87→63.72 for top-k) and the standard load-balancing loss (63.19 for top-k with load-balance vs. 63.72 with CGJS). Figure 3 provides entropy visualizations confirming that the CGJS loss improves certainty (lower solid lines) while maintaining balance (higher dashed lines), whereas the load-balancing loss improves balance at the cost of certainty.

3. **Outperforms full fine-tuning with substantially fewer parameters.** HMoRA with lightweight designs (3.90% trainable parameters) achieves higher average accuracy (63.88) than full fine-tuning (63.15) across seven benchmarks while outperforming or matching on 5/7 individually. The full version HMoRA w/o LW (6.31% parameters) surpasses full fine-tuning on all seven benchmarks (64.16 vs. 63.15).

4. **Comprehensive baseline comparison against multiple MoE+LoRA variants.** Table 2 compares against MoLoRA, MixLoRA, and HydraLoRA (all with matched e=8, r=8), consistently outperforming all of them (64.16 vs. 63.02, 62.38, 62.70). The ablation in Table 3 confirms the task-router auxiliary loss contributes meaningfully (64.16 → 63.18 when removed).

5. **Unsupervised task differentiation on unseen tasks.** The quantitative study (Section 4.3) reports that with the CGJS loss, the task router differentiates 42/57 MMLU sub-tasks (73.68%) vs. 0 without any auxiliary function and only 7 (12.28%) with a load-balancing loss. The t-SNE visualizations (Figure 4) provide qualitative support.

---

## Weaknesses

### Fatal

None.

### Major

1. **No variance reporting for any experimental result.** Every result in Tables 1, 2, and 3 reports only the mean over 5 runs, with no standard deviations, confidence intervals, or statistical significance tests. The headline improvements — HMoRA vs. full FT (64.16 vs. 63.15, Δ≈1.0 pp) and HMoRA w/ LW vs. MoLoRA (63.88 vs. 63.02, Δ≈0.86 pp) — are small. Without variance, it is impossible to assess whether these differences reflect genuine improvement or random noise. This is the single most important evidential gap and the main factor limiting the paper's strength.

2. **No training or inference cost comparison against the baseline methods.** The lightweight designs analysis (Figure 2c) compares different internal configurations (Base, +Hydra LoRA, +Ghyra LoRA, +Phyra LoRA, +All) but provides no cost comparison against the actual baselines used in Table 2 (MoLoRA, MixLoRA, HydraLoRA). Since these baselines have different architectures (e.g., MixLoRA applies MoE only to FFN, not all dense layers), their computational footprints likely differ from HMoRA's. A cost-accuracy Pareto plot would substantially strengthen the practical argument.

### Minor

3. **Validation protocol could conflate model selection with test evaluation.** The paper performs early stopping and checkpoint selection based on "validation sets of all benchmarks" (the same seven benchmarks whose test sets are reported), then selects the best checkpoint by "the highest averaged accuracy across all benchmarks" for final test evaluation. While this is common practice in PEFT research and applies equally to baselines, it does mean the reported numbers are not purely independent test-set evaluations — the benchmarks' validation splits were consulted during model selection. The paper should clarify whether the validation splits are distinct from the test splits for each benchmark.

4. **Only evaluated on 1.5B and 1B parameter models.** Demonstrating effectiveness on larger models (7B+) would increase significance, especially since the routing overhead from the task encoder is more justifiable at larger scales where parameter efficiency matters most.

### Trivial

None that survive the filtering criteria.

---

## Nice-to-Haves

- **Compare hierarchical α schedule against a static-α baseline** (e.g., α=0.5 at all layers) to more cleanly isolate the benefit of the depth-dependent design.
- **Report per-task analysis of where HMoRA underperforms** relative to full fine-tuning or MoLoRA — currently the discussion is limited to noting which benchmarks are won/lost.
- **Discuss the computational overhead of the task encoder** (Transformer encoder processing embeddings per input) at inference time — it adds a forward pass that is not negligible.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Differentiation metric definition is unclear** — The harsh critic claimed the "differentiation" metric in Section 4.3's quantitative study is undefined. **Removed** because the quantitative study details are in Appendix E.8, which was stripped by the parser. The original submission likely contains the precise criterion.
- **Missing task encoder hyperparameters** (depth, hidden dimension) — **Removed** because architectural details are in Appendix C (stripped).
- **Hierarchical routing ablation insufficient** (no comparison against static α) — **Removed** because the comparison between ε > 0 and ε = 0 in Appendix E.5 tests the hierarchical claim, and further controls (static α) may also be in the stripped appendix. The main paper already provides evidence that the depth-dependent schedule matters.
- **Missing related works** — **Removed** because I cannot verify whether a work exists or was cited; the related works section adequately covers MoE and MoE-LoRA literature.
- **Figure 2(c) appears garbled** — **Removed** because this is a parser artifact, not a submission error.
- Pure formatting nitpicks, typo claims, and reproducibility concerns about large artifacts — **Removed** per hard rules.
- The Strength Finder's generic/superficial strengths (e.g., "the paper addresses an important problem") — **Removed**; only concrete, evidenced strengths are retained above.

---

## Novel Insights

The most interesting observation across the reviews that is not already prominent in the paper is the *tension between the hierarchical routing insight and the computational overhead it incurs*. The paper's core architectural insight — that routing granularity should vary by layer depth — is well-motivated by prior work on LLM internal representations (Geva et al., 2021). However, realizing this insight requires per-layer routing, a task encoder, and a CGJS loss that operates on per-batch routing distributions. The paper convincingly shows that this pays off in accuracy, but the cost-accuracy trade-off relative to simpler baselines (like MoLoRA or LoRA-r64, which are simpler but competitive) remains under-explored. The lightweight designs partially address this, but a systematic cost-accuracy comparison with all baselines would resolve whether the hierarchical design earns its complexity premium.

---

## Suggestions

1. **Report standard deviations or confidence intervals for all main results** (Tables 1, 2, 3). With 5 runs available, this is straightforward and would substantially strengthen the paper's credibility.
2. **Add a cost-accuracy comparison** (e.g., training time, inference throughput, or GPU-hours) against the external baselines used in Table 2, not just against internal lightweight variants.
3. **Clarify the validation/test split** for each benchmark and confirm that the validation sets used for early stopping are distinct from the test sets reported.
4. **Explicitly define the "differentiation" criterion** used in the quantitative study of Section 4.3 (e.g., clustering purity, threshold-based separation) in the main text so the claim is independently verifiable.

---

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| XVHXVdoV11 (Collective Model Intelligence) | 3.40 | 1 (weak) | Different domain, much weaker relevance; HMoRA is significantly stronger |
| 49ti6LOUw5 (UnoLoRA) | 3.00 | 1 (weak) | Single-shared-LoRA approach, limited to GLUE; HMoRA is substantially stronger |
| 762u1p9dgg (MOEfication) | 3.40 | 1 (weak) | MoE sparsification for inference speed; different task, but similar quality tier — HMoRA is somewhat stronger |
| dO06t9iVO3 (Mixture-of-Adapters) | 3.00 | 1 (weak) | CV domain generalization; less relevant, but HMoRA is stronger |
| LWvgajBmNH (MoRE) | 4.00 | 1 (middle) | Closest topical match. MoRE evaluated only on GLUE, marginal improvements, limited novelty. HMoRA's evaluation is more comprehensive (7 benchmarks, multiple MoE+LoRA baselines) and its methodological contributions (hierarchical routing, CGJS loss) are more substantial. HMoRA is clearly stronger. |
| l0gZS0sAlf (ELREA) | 5.80 | 1 (middle) | Gradient-clustering for LoRA experts, well-executed, accepted as poster. HMoRA has comparable scope but weaker evidential support (no SD, no cost comparison vs. baselines). HMoRA is somewhat weaker. |
| uHTmx0nRfX (MoTE) | 4.75 | 1 (middle) | MoE for embedding models; different domain. HMoRA is comparable in quality. |
| yOOJwR15xg (MeteoRA) | 6.20 | 1 (middle) | MoE gating for pre-existing LoRA adapters with efficient kernels, accepted as poster. HMoRA's contributions are more architectural (routing design, loss) but its experiments are on smaller models and lack variance reporting. HMoRA is weaker. |
| CKdlPUWDEE (ME-Switch) | 5.00 | 2 (4.5–6.0) | Quantization+router for serving multiple FT models. Rejected mainly for missing baselines. HMoRA has more novel methodological contributions. Comparable quality overall. |
| huy8g3iKy0 (Dense Backprop) | 5.50 | 2 (4.5–6.0) | Dense gradients for MoE routing. Accepted reject (3, 5, 6, 8 — mixed). HMoRA has cleaner experimental design but less theoretical depth. Roughly comparable. |
| RQ9fQLEajC (Routoo) | 4.67 | 2 (4.5–6.0) | LLM routing for cost-quality tradeoff. Rejected for limited novelty. HMoRA has stronger novelty. |
| xXTkbTBmqq (OLMoE) | 8.67 | 1 (strong) | Large-scale open MoE model, oral accept. Incomparable scale and scope. |
| w4abltTZ2f (FLoRA) | 8.00 | 1 (strong) | Batched LoRA for heterogeneous requests, oral accept. Much stronger engineering contribution. |

**Initial bracket (Round 1):** 4.5 – 6.0  
**Narrowing (Round 2):** The paper is clearly stronger than MoRE (4.00), comparable to ME-Switch (5.00), and somewhat weaker than ELREA (5.80). The missing standard deviations for small-margin improvements (~1 pp) are the primary factor holding it back from the 5.5–6.0 range. The paper has genuine and well-motivated novel contributions, but the evidential gap is meaningful for a venue like ICLR where claims of outperforming full fine-tuning should be rigorously supported.

**Final score: 5.0** — A borderline paper with solid methodological contributions and reasonable scope, held back by the lack of statistical significance reporting for its small-margin claims.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
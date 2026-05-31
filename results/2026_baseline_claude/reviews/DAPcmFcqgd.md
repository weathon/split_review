## Summary

MoEP (Modular Expert Paths) proposes a sparse decoder-only language model architecture that adds sparsity without expanding the total parameter count. The architecture wraps a stack of small parallel Transformer blocks (at half the hidden dimension) between MoE shrink/grow projection blocks, while applying top-k routing at both the parallel-block level and the MoE-projection level. The model is trained and evaluated on the BabyLM strict-small track (10M words, 28M parameters) and compared primarily against a GPT-2 baseline.

---

## Strengths

- **Clean research question**: The goal of achieving sparsity without inflating total parameter count is well-motivated and distinct from most MoE work, which trades total params for activation sparsity.
- **Reproducibility**: Code and model weights are publicly released, and the experimental setup follows an official shared benchmark (BabyLM), making comparisons transparent.
- **Training dynamics insight**: The checkpoint analysis (Appendix A.3) showing that MoEP reaches near-peak performance earlier in training than dense GPT-2 is a concrete, quantitative observation supporting the claim of better sample efficiency.

---

## Weaknesses

### Fatal

None that fully invalidate the approach, but the following major issues together severely undermine the paper's claims.

### Major

1. **Overstated performance claims**: The abstract and Section 5.1 claim MoEP "achieved the highest performance across all models, including the official BabyLM baselines." This claim depends critically on including AoA scores. Excluding AoA, GPT-BERT (causal) achieves a macro average of 54.10, substantially above MoEP's 49.00. The paper's own GPT-2 replica and MoEP-SwiGLU have no AoA scores, making their comparison asymmetric. The "best overall model" conclusion therefore rests on an incomplete and inconsistently available metric.

2. **Unfair within-paper comparison (parameter count)**: The central claim is that MoEP achieves sparsity without expanding the parameter count. Yet Table 2 shows MoEP-SwiGLU has **38M parameters vs. 28M for GPT-2 and MoEP** — a 35% increase. MoEP-SwiGLU is evaluated on equal footing with the others without explicitly flagging this discrepancy.

3. **Severely limited scale**: Every conclusion — about sparsity, sample efficiency, routing behavior — is drawn from a single 10M-word, 28M-parameter experiment. The paper itself concedes in the conclusion that it is "unclear whether scaling up… would preserve MoEP relative performance." At this scale, differences on the order of 1–2 macro-average points lie well within the variance of such benchmarks, making the claimed advantage unreliable.

4. **No ablation studies**: The design involves several interacting choices (number of parallel blocks $P$, hidden dimension ratio $d_P/d_L$, number of experts $E$, routing top-k, shrink/grow architecture). None of these are ablated. It is therefore impossible to attribute the modest gains to the architecture vs. implementation differences vs. tokenizer differences.

### Minor

1. **Unusual load-balancing loss**: The balancing term (Equation 2) is the entropy $-\sum_i p_i \log p_i$, which is maximized at uniform routing — the opposite sign from the standard auxiliary loss in Switch Transformers (which minimizes auxiliary terms). Using entropy maximization as a positive objective is unconventional and the paper does not discuss this design choice or its interaction with the cross-entropy loss.

2. **Training dynamics interpretation is weak**: The appendix attributes MoEP's later score degradation to "overfitting" but provides no supporting evidence (e.g., train/validation loss curves). Routing collapse or instability are equally plausible explanations.

3. **Ambiguous contribution claim**: Contribution #3 promises "analysis of expert networks routing behavior," but the actual analysis consists of training curves with no breakdown of which experts are selected, how routing entropy evolves, or whether experts specialize.

### Trivial

- The paper cites MoR (Bae et al., 2025) with an arXiv link dated "2507.10524" (July 2025), yet the paper also references the future BabyLM 2025 workshop; these timeline details appear internally consistent but are worth noting.

---

## Nice-to-Haves

- A FLOPs-matched comparison (not just parameter-matched) would better support the efficiency narrative.
- Routing histograms or per-expert utilization plots over training would substantiate the "routing behavior" analysis claim.
- An experiment at 100M+ word scale would meaningfully test scalability, even if only one additional data point.

---

## Novel Insights

MoEP's architectural pattern — shrink into a parallel sparse middle stack, then grow back to full dimension — is a reasonable and underexplored combination of techniques. The observation that routing at the block level can accelerate early learning (peak performance reached before dense baselines with the same wall-clock budget) is a practically useful finding. However, it is not rigorously established at this scale, and the architectural components are each borrowed from prior work (PaLM-style parallelism, top-k MoE routing, dimensionality-reduction projections). The combination is novel but modestly so.

---

## Suggestions

- Report macro averages both with and without AoA consistently across all models, or explain why AoA is excluded for some.
- Add at minimum a parameter-matched ablation: MoEP without block-level routing (i.e., equal-weight averaging of parallel blocks) to isolate the routing contribution.
- Scale to at least one additional dataset/regime to test whether the 1–2 point macro advantage persists.

---

## Score and Decision

The paper tackles a legitimate and interesting problem, but the experimental evidence is insufficient to support the claims made. The primary performance claim depends on a metric that is unavailable for several of the compared models, and the GPT-BERT baselines clearly outperform MoEP under the consistent (AoA-excluded) macro average. The scale is too small for robust conclusions, and the lack of ablations means the architectural contribution cannot be isolated. In its current form this reads as a promising workshop paper, not an ICLR submission.

MY FINAL SCORE: <score>3</score>
MY FINAL DECISION: <decision>Reject</decision>
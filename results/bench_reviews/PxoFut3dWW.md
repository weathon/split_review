---

## Summary

Wanda (Pruning by **W**eights **and** **a**ctivations) proposes a simple yet effective post-training pruning method for LLMs. The core idea is to score each weight by the product of its magnitude and the ℓ₂-norm of the corresponding input activation channel, pruned on a *per-output* basis. Without any weight update or retraining, Wanda achieves near-SparseGPT perplexity at ~300× less metric-computation time, motivated theoretically by a diagonal approximation of the OBD/OBS Hessian-based metric.

---

## Strengths

- **Near-SparseGPT performance without weight update**: Tables 2–3 confirm that at 50% unstructured sparsity, Wanda matches or beats SparseGPT on most model sizes (e.g., LLaMA-13B: 6.15 vs. 6.21; LLaMA-2-7B: 6.42 vs. 6.51). For 4:8 structured sparsity, Wanda outperforms SparseGPT on 4 of 7 configurations in perplexity. The no-weight-update constraint is a genuine practical advantage.

- **Dramatic and credible speedup**: Table 5 shows pruning metric computation of 0.54s (LLaMA-7B) versus SparseGPT's 203.1s — a real and hardware-verified difference stemming from O(d²) vs. O(d³) complexity. This matters practically for use cases involving repeated pruning.

- **Principled theoretical connection to OBD**: Equation 3 shows Wanda is recoverable from SparseGPT's metric under λ=0 and a diagonal approximation, providing meaningful lineage. The framing of Wanda as a local-neuron OBD analogue is intellectually coherent and connects the work to a decades-long research thread.

- **Unusually thorough ablation**: Table 4 crosses three pruning metrics × five comparison groups. The finding that per-output grouping consistently beats per-layer for LLMs (across all metrics), and that this trend does not appear for vision models, is a non-obvious and practically useful insight.

- **Robustness to minimal calibration data**: The paper shows (Figure 3) that even a single calibration sample yields perplexity 7.66 for LLaMA-7B, versus 7.26 for 128 samples — a practically important finding that SparseGPT cannot replicate due to the full Hessian inverse estimation.

- **Large sparse vs. small dense finding**: Zero-shot results in Section 4.1 confirm that 50% sparse LLaMA-65B (66.67%) outperforms dense LLaMA-30B (65.38%), providing concrete practical guidance for practitioners choosing between model sizes.

---

## Weaknesses

### Fatal
None.

### Major

- **Evaluation restricted to the LLaMA family**: All experiments use LLaMA-7/13/30/65B and LLaMA-2-7/13/70B only. The paper's core motivation — outlier activation features — was originally observed and documented in OPT and BLOOM-family models. Restricting experiments to one model family raises a legitimate question about whether the results are specific to LLaMA's training regime or generalizable across transformer architectures. A single evaluation on OPT or another architecture would materially strengthen the generalizability claim.

### Minor

- **2:4 structured sparsity gap on small models is understated in framing**: The paper explicitly acknowledges that "on smaller models (e.g., 7B), SparseGPT outperforms Wanda on 2:4 sparsity" (Section 4.2), which is commendable. However, the gap is non-trivial: LLaMA-7B (11.53 vs. 11.00 ≈ 4.8%), LLaMA-2-7B (11.02 vs. 10.17 ≈ 8.4%), LLaMA-13B (9.58 vs. 9.11 ≈ 5.2%). Since 2:4 sparsity is the most hardware-relevant sparsity pattern (NVIDIA sparse tensor cores), this weakness deserves slightly more prominent acknowledgment than a single sentence in the analysis section.

- **The diagonal Hessian approximation step is stated but not validated**: Equation 3 involves `diag((X^T X)^{-1}) ≈ (diag(X^T X))^{-1}`, labeled "diagonal approx." but with no quantification of how tight this approximation is for LLM activations — which are known to have correlated outlier features. The empirical success of Wanda is sufficient to justify the metric, but the OBD derivation is presented as a theoretical contribution; readers naturally expect some bound or empirical verification of the approximation quality.

- **"Exact sparse subnetworks" claim needs qualification**: Property 3 in Section 3 states that Wanda's success without weight update "suggests that LLMs have effective sparse sub-networks that are *exact*." The 70% sparsity result (reported at the end of Section 4 weight update analysis: Wanda alone yields perplexity 84.50 vs. 29.65 with sequential update) directly shows this claim has a sparsity-dependent boundary. The paper mentions this result but does not reconcile it with the "exact" framing.

### Trivial
- The 7 zero-shot task names are not listed in the main body — only described as "seven tasks from EleutherAI LM Harness." Per-task breakdowns are not expected in a paper of this scope, but a brief listing of the task names would help readers interpret the aggregate accuracy.

---

## Nice-to-Haves

- A sparsity sweep from 10% to 70% for unstructured pruning (beyond the 50% focus) would precisely identify where Wanda's no-weight-update advantage breaks down relative to SparseGPT, providing clearer guidance for practitioners.
- Visualization of which weights are masked under Wanda vs. magnitude pruning overlaid on the input activation norm profile — this would make the "outlier feature preservation" mechanism visually transparent.
- Analysis of why (output, 1) is best for Wanda while (input, 1) is best for magnitude: Table 4 contains richer signal than the paper fully explains; understanding the metric-group interaction would sharpen the conceptual contribution.

---

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **Harsh Critic, "300× speedup is only metric computation"**: The paper explicitly states this in Section 4.3: "we measure the accumulated time for computing the pruning metric at each layer (excluding the forward pass process shared by both methods)." The paper is transparent — this is not an overstatement.

- **Harsh Critic, "per-output granularity is metric-specific, not a general principle"**: The paper's Section 3 claim ("consistently better than layer-wise pruning for LLMs") is technically accurate — per-output beats per-layer for all three metrics in Table 4. The paper acknowledges that (input, 1) is best for the magnitude metric in the analysis section. No factual misrepresentation.

- **Harsh Critic, "missing movement pruning comparison"**: Wanda's scope explicitly covers post-training pruning without retraining; movement pruning requires training-time gradient access. The two baselines (magnitude, SparseGPT) are the relevant ones. Omitting movement pruning does not weaken the core claim.

- **Strength Finder, "The problem is important / addresses a growing challenge"**: Generic framing removed per the filter rule.

- **Harsh Critic, "no end-to-end wall-clock comparison"**: The paper does report end-to-end latency (1.24× speedup for LLaMA-7B) and is explicit that the 300× figure is metric-computation-only. Criticism is based on a misread.

---

## Novel Insights

The most genuinely novel insight in the paper is that *comparison granularity matters as much as metric choice* for LLM pruning, and that this effect is unique to LLMs (not observed in vision models). Table 4 demonstrates that Wanda's metric applied with a layer-wise comparison group (perplexity 7.95) is nearly indistinguishable from SparseGPT with a layer-wise group (7.91), while switching to per-output grouping is what makes Wanda competitive (7.26). This implies that a significant portion of SparseGPT's reported advantage over naive magnitude pruning was actually attributable to its implicit (input, 128) comparison group rather than its Hessian metric — a subtle and practically important finding.

---

## Suggestions

1. **Add at least one non-LLaMA evaluation** (e.g., OPT-6.7B or OPT-30B): Given the paper's motivation rests explicitly on outlier features documented in OPT-family models, this would substantially broaden the generalizability claim and is feasible within a reasonable compute budget.
2. **Quantify the diagonal approximation quality**: Compute and report `||diag((X^T X)^{-1}) - (diag(X^T X))^{-1}||` for a representative LLM layer versus, say, a ResNet layer, to empirically support or bound the OBD connection.
3. **Add a sparsity sweep figure (10%–70%)**: The boundary where Wanda's no-weight-update advantage holds is practically important; a Pareto curve against SparseGPT would be a high-value addition.
4. **Clarify the "exact sparse subnetwork" claim with a qualifier** acknowledging the 70% sparsity boundary condition, making the theoretical interpretation more defensible.

---

## Score and Decision

**Axis evaluation:**
- *Originality*: High — the combined metric (weight × activation norm) and per-output grouping insight are novel and practically motivated.
- *Importance of research question*: High — post-training LLM compression without retraining is a significant practical problem.
- *Claim support*: Good — core claims are well-supported across 7 model sizes with perplexity and zero-shot tasks; the 2:4 small-model gap is acknowledged honestly.
- *Soundness of experiments*: Good — thorough ablation, calibration robustness, fine-tuning study; limited by LLaMA-only evaluation.
- *Clarity of writing*: Strong — method description is clear, Algorithm 1 in PyTorch is a model of simplicity, and the OBD derivation is easy to follow.
- *Value to research community*: High — a clean, fast baseline method for LLM pruning that enables future work.

**Anchor comparison:**

| Path | Avg Score | Comparison to paper under review |
|------|-----------|----------------------------------|
| `IC5RJvRoMp.md` | 7.50 | LLM-Streamline also proposes a new compression method with stronger novelty (layer replacement module); Wanda is simpler but has stronger generalization evaluation concerns |
| `ud8FtE1N4N.md` | 6.67 | Sparse pre-training scaling study — comprehensive empirical scope, similar quality; Wanda has a more targeted practical contribution |
| `B9klVS7Ddk.md` | 6.75 | LLM compression benchmark analysis — purely diagnostic, no new method; Wanda proposes a real method |
| `pOBvr1PxFd.md` | 6.00 (Rejected) | OWL builds on Wanda to propose non-uniform layerwise sparsity; weaker theoretical motivation and muddled empirical interpretation than Wanda |
| `ldJXXxPE0L.md` | 6.00 | LLM pruning capability analysis — solid empirical contribution, similar quality tier |
| `wV9iMiyQcc.md` | 5.33 (Rejected) | RotPruner — training-based pruning, less elegant and less well-supported than Wanda |
| `zZU69H8tcr.md` | 3.75 (Rejected) | SparsitySolver RL-based pruning — poorly motivated and weak results; clearly worse than Wanda |
| `rO62BY3dYc.md` | 3.75 (Rejected) | Pruning via Ranking — generic structured pruning without LLM-specific insight; clearly worse than Wanda |
| `IU4L7wiwxw.md` | 4.50 (Rejected) | PGZ gradient-based LLM pruning — comparable setting, weaker method and results |

Wanda sits firmly in the 6.0–7.0 tier. Its contribution is cleaner and better-supported than the 6.0-scoring papers (OWL, ldJXXxPE0L). The single significant weakness — LLaMA-only evaluation — prevents a 7.0 score (where IC5RJvRoMp sits, with broader architectural coverage and a more novel design). Given the elegant simplicity of the method, the strong ablations, and the real practical impact, a **6.5** is appropriate.

**Score: 6.5 — Accept**

The paper makes a genuine and well-executed contribution to LLM compression: a simple, principled, and fast pruning method that achieves near-SparseGPT quality without weight updates. The evaluation is thorough within the LLaMA family, the speedup is real and dramatic, and the ablation surfaces a non-obvious insight about comparison granularity. The main gap is the lack of cross-architecture validation. The weaknesses do not threaten the core claim.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
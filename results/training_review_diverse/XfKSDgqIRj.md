Now I have verified all claims against the paper. Let me produce the final consolidated review.

---

## Summary

This paper proposes COAT, a framework that pushes FP8 training to its memory limits by quantizing both optimizer states and activations into FP8 — beyond prior frameworks like TransformerEngine (which only does FP8 compute for linear layers) and FP8-LM (which only partially quantizes optimizer states). Two key technical contributions are presented: (1) **Dynamic Range Expansion (DRE)** — a power-function-based transformation applied per quantization group to better align optimizer-state distributions with FP8's representation range before quantizing, backed by a formal derivation of the optimal exponent; and (2) **Mixed-Granularity Activation Quantization** — using per-group quantization (1×G) for non-linear layers where accuracy is sensitive, and per-tensor quantization with Group Scaling for linear layers to exploit Tensor Core efficiency. Experiments span LLM pretraining (OLMo-1B, OLMo-7B continuation), math fine-tuning (Llama-2-7B), and VLM SFT (VILA1.5-7B), achieving 1.54× memory reduction and 1.43× speedup vs. BF16 while maintaining nearly lossless accuracy. COAT also enables training larger models on fewer GPUs and doubling batch sizes in distributed settings.

## Strengths

- **Dynamic Range Expansion is a principled solution to a genuine, overlooked problem.** The paper identifies that optimizer states under per-group quantization have far lower dynamic range (first-order <1e4, second-order <1e1) than FP8 E4M3's capacity (~2×10^5), wasting representational capacity. DRE (f(x)=sign(x)|x|^k) is derived from the simple observation that (R_X)^k = R_E4M3 gives the optimal k, and the resulting 1.63× MSE reduction on the effective update term m/√v (Table 1) provides concrete evidence that the method reduces quantization error. The ablation showing DRE's compatibility with DE8 format (Table 7, 1.41× further error reduction) demonstrates the idea is not FP8-specific.

- **Mixed-Granularity Activation Quantization achieves near-ideal memory reduction.** The decomposition of activation memory (Table 2) precisely identifies non-linear layers as ~50% of the footprint. By applying per-group quantization (1×G, avoiding cross-token axes that harm accuracy) to non-linear layers and per-tensor quantization to linear layers, COAT achieves 1.65× activation memory reduction — within 2.4% of the theoretical 1.69× upper bound and substantially better than TransformerEngine's 1.20×.

- **Practical benefits clearly demonstrated in realistic distributed training.** COAT enables full-parameter Llama-2-7B training on a single H100 GPU (where BF16 and TE OOM), Llama-2-13B on 2 GPUs, and Llama-30B on 8 GPUs. It also consistently doubles the micro-batch size in multi-GPU settings (e.g., Llama-2-13B on 4 GPUs: BS=2 vs. BS=1 for BF16/TE), achieving up to 2.25× speedup. These are practically valuable results for memory-constrained training.

- **Consistent accuracy across multiple training paradigms.** The method is validated on LLM pretraining (OLMo-1B, OLMo-7B), LLM fine-tuning (Llama-2-7B on math), and VLM SFT (VILA1.5-7B) — three distinct training regimes — with accuracy gaps ≤0.3% from BF16 in all cases, supporting the "nearly lossless" characterization within the scope of experiments conducted.

## Weaknesses

### Major

- **Limited pretraining scale weakens the "nearly lossless at scale" claim.** The OLMo-1B experiment runs for only 22B tokens — a small fraction of typical full pretraining (100B–1T tokens) — and the OLMo-7B experiment is just a 1000-step (4B token) continuation from an existing checkpoint. While the results are consistent across the runs conducted, this evidence does not rule out systematic divergence over longer training horizons. The paper's central claim about lossless performance would be substantially stronger with evidence from a longer training run or at least an explicit discussion of the extrapolation risk. The final training loss shows a gap (BF16 2.995 vs. COAT 3.008), and though small, a single seed cannot distinguish noise from systematic bias. This does not invalidate the paper's contribution, but it limits the strength of the generalization claim.

- **Missing experimental comparison with FP8-LM.** FP8-LM (Peng et al., 2023) is the most directly related prior work — it also quantizes gradients and first-order momentum to FP8. The paper mentions FP8-LM in related work and notes its limitations (no activation quantization, second-order momentum left in FP16), but does not provide a head-to-head comparison on memory, throughput, or accuracy. Without this, it is difficult for readers to quantify COAT's incremental contribution over FP8-LM beyond what the paper's architectural analysis suggests. Adding even a single comparison (e.g., on the OLMo-1B setup) would significantly strengthen the positioning.

### Minor

- **No training ablation isolating DRE's effect.** The paper justifies DRE via MSE reduction on static optimizer-state snapshots (1.63×), which is meaningful but not a substitute for an end-to-end training comparison with and without DRE (keeping all else fixed). A training ablation showing that removing DRE leads to measurable accuracy degradation would directly confirm that the MSE improvement translates to real training benefits and would guard against the possibility that the MSE gap is inconsequential in practice.

- **Computational overhead of on-the-fly k calculation is not analyzed.** DRE computes k = log_{R_X}(R_E4M3) per group per step, and applies power (x^k) and root (x^{1/k}) operations during each optimizer update. With k values reaching 5–15 for second-order momentum (Figure 1c), these operations are non-trivial. While the optimizer step is not on the critical forward/backward path, a latency breakdown or analytical estimate would help verify that this overhead is negligible in practice.

- **The VILA1.5-7B TransformerEngine baseline underperforms BF16 (62.80 → 61.88).** This is an unusual result given TE's widely reported near-lossless behavior. The paper notes sequence lengths were padded to multiples of 4, which may affect TE's calibration, but no further explanation is offered. While this anomaly does not undermine COAT's own accuracy (62.51, close to BF16), it raises a question about whether the TE baseline was optimally configured, and by extension whether COAT's claimed advantage over TE on this task reflects genuine superiority or a configuration issue.

- **Speedup comparison with TE is mixed in end-to-end settings.** The abstract states COAT is "on par with or surpassing TransformerEngine's speedup." This characterization is roughly accurate, but the details are worth noting: on Llama-2-7B/8GPUs, COAT achieves 1.36× vs. TE's 1.42× (behind); on Llama-2-13B/8GPUs, it's 1.44× vs. 1.43× (essentially tied). The cases where COAT substantially exceeds TE (e.g., 13B/4GPU: 2.25× vs. 1.21×) are enabled by larger batch sizes made possible by memory savings, not by faster per-iteration computation. This distinction is discussed in the paper (line 371) but could be stated more prominently in the abstract and conclusion.

### Trivial

None.

## Nice-to-Haves

- A full-scale pretraining run (100B+ tokens) with multiple seeds would be the definitive validation of the lossless claim, but the present evidence is reasonable for a conference submission given the compute costs involved.
- A comparison against 8-bit Adam on optimizer-state memory would help contextualize the DRE component relative to prior optimizer-quantization work.
- Reporting per-component latency breakdown (quantization, DRE power/root ops, Group Scaling overhead) during actual training would preempt concerns about unaccounted overhead.

## Removed Points

*"DRE lacks a proper theoretical foundation"* (Harsh Critic) — REMOVED: The paper provides a clear mathematical derivation (Section 4.1–4.2) showing that f(x)=sign(x)|x|^k expands dynamic range from R_X to (R_X)^k, and derives the optimal k = log_{R_X}(R_E4M3). The reviewer's claim that "it is not clear a priori that this reduces error" is contradicted by the empirical MSE reduction (1.63×) reported in Table 1.

*"The speedup is an artifact of memory savings enabling larger batches, not of the quantization method itself"* (Harsh Critic) — REMOVED: The paper explicitly attributes the 2.25× speedup to batch-size increases (line 371) and clearly separates per-iteration speed (Tables 4, 5) from batch-size-enabled gains. Memory savings that enable larger batches are a legitimate, practically useful speedup mechanism, not an artifact.

*"Group Scaling... not benchmarked against delayed scaling in actual training throughput"* (Harsh Critic) — DOWNGRADED to Nice-to-Have: The paper's speed comparison (Figure 3b) is against just-in-time scaling (the relevant baseline for the max-reduction overhead claim), not delayed scaling. The comparison with delayed scaling is about *precision* (line 205), not speed. The reviewer conflates two separate claims.

*Strength Finder's claim of "Broad experimental validation" as a top-tier strength* — KEPT but qualified: The breadth across LLM pretraining, fine-tuning, and VLM is genuine, but the pretraining depth is limited. This is an accurate strength when taken as measuring breadth rather than depth.

## Novel Insights

The reviewer interactions surface a recurring tension in systems-for-ML papers: the "nearly lossless" claim requires strong statistical evidence (multiple seeds, long training runs) to be fully convincing, but the cost of such evidence for large models often exceeds what is feasible for a single paper. The DRE technique is genuinely interesting because it identifies a precise mismatch (FP8's dynamic range vs. optimizer states' narrower range) and proposes a near-optimal fix (the power function with an analytically derived exponent), which is more principled than most ad-hoc quantization tuning. The mixed-granularity approach to activations is less novel in isolation (following Jetfire and VS-Quant), but combining it with the precision flow design (saving FP8 activations directly without extra quant ops) is a practical engineering contribution. The main gap in evidence is not about correctness of the reported numbers but about extrapolation — whether the 0.013 loss gap at 22B tokens would grow, shrink, or stay constant over a full pretraining run.

## Suggestions

1. **Add an FP8-LM comparison** on the OLMo-1B setting (memory, throughput, accuracy). This would be the single most impactful addition for establishing incremental contribution.

2. **Run or add a DRE vs. no-DRE training ablation** on a medium-scale setup (e.g., OLMo-1B for 10B tokens) to directly verify that DRE's MSE improvement translates to training quality. This could replace one of the existing experiments.

3. **Clarify the VILA TE baseline** — either explain why TE underperforms BF16 (e.g., calibration sensitivity to padded sequence lengths) or provide a corrected TE run.

4. **Add a brief analysis** of the per-step overhead of DRE (power/root operations) in the optimizer step, either analytically or via a microbenchmark.

5. **Make the speedup decomposition explicit** in the abstract/conclusion: distinguish between the per-iteration speedup (1.36–1.57× from FP8 compute and reduced memory traffic) and the batch-size-enabled speedup (up to 2.25× in memory-constrained settings).

## Score and Decision

The paper presents genuine, practically useful innovations (DRE, mixed-granularity activation quantization with precision flow) supported by experiments across multiple training paradigms. The weaknesses — limited pretraining scale, missing FP8-LM baseline, and absence of a DRE training ablation — are substantive but not fatal; they limit the strength of the evidence for the "nearly lossless at scale" claim without invalidating the core technical contribution. The paper is clearly written, the claims are appropriately scoped in the main text (if slightly generous in the abstract's speedup characterization), and the practical benefits (enabling single-GPU training of 7B models, doubling batch sizes) are convincingly demonstrated.

I recommend acceptance with minor revisions addressing the suggested additions.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
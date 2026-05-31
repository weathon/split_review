Now I have thoroughly read the paper and verified all claims against the source text. Let me produce the consolidated review.

---

## Summary

This paper proposes BDIA-transformer, a method to make standard transformers exactly bit-level reversible during training while preserving the original architecture at inference. The key idea is to reinterpret each transformer block as Euler integration of an ODE, then apply Bidirectional Integration Approximation (BDIA) with random \(\gamma_k \in \{\pm 0.5\}\) per block per sample to average consecutive integration steps. This creates an ensemble of ODE solvers during training that regularizes the model. Combined with activation quantization and 1-bit side information per activation, the method enables lossless online back-propagation. At inference, \(\mathbb{E}[\gamma_k]=0\) recovers the original transformer forward pass (up to activation quantization). Experiments on ViT (CIFAR10/100), machine translation, and GPT-2 show validation improvements and substantial memory savings.

## Strengths

1. **Exact bit-level reversibility with unchanged inference architecture** — The paper derives update equations (9)–(14) that make the transformer exactly reversible under fixed-point arithmetic, while equation (15) shows that replacing \(\gamma_k\) with \(\mathbb{E}[\gamma_k]=0\) recovers the original transformer forward pass. This is a meaningful advance over prior reversible DNNs that require architectural modifications. No prior work achieves this property.

2. **Consistent regularization benefit on image classification** — Table 1 shows BDIA-ViT achieves 89.10% on CIFAR10 (vs 88.15% for ViT and 86.22% for RevViT) and 66.09% on CIFAR100 (vs 61.86% and 61.89%). The ablation in Table 2 confirms the regularization comes from the random \(\gamma\) ensemble, not from quantization: any non-zero \(\gamma\) outperforms \(\gamma=0\), with \(\gamma=\pm0.5\) giving the best result (89.12% vs 88.15%).

3. **Substantial training memory reduction** — Table 1 reports peak memory of 693.4 MB for BDIA-ViT versus 1570.6 MB for standard ViT (56% reduction) with only 1 bit of side information per activation per block.

4. **Robustness to inference-time solver choice** — Figure 1 demonstrates that BDIA-ViT maintains nearly constant validation accuracy across \(\gamma \in [-0.5, 0.5]\) during inference, whereas ViT's accuracy drops sharply, supporting the claim that the ensemble of ODE solvers produces a more robust model.

5. **Clear differentiation from RevViT** — The paper benchmarks against the existing reversible vision transformer and shows RevViT underperforms ViT (86.22% vs 88.15% on CIFAR10), while BDIA-ViT outperforms both. This establishes that BDIA does not trade performance for reversibility, unlike prior art.

## Weaknesses

### Fatal
None.

### Major

- **Translation experiment lacks a task-standard metric** — Section 5.2 reports only training/validation loss curves for English-French translation with no BLEU scores (or other translation quality metric). Loss is a weak proxy for actual translation quality, and the paper's claim that BDIA "significantly improves the validation performance" on this task is unsupported by the evidence provided. This is the one task where transformers are the canonical architecture, and the omission is a significant evidential gap. The ViT experiments are strong, but the translation claim needs BLEU scores with multiple runs to stand.

### Minor

- **GPT-2 experiment is illustrative but lacks rigor** — Section 5.3 uses 0.05% of an unnamed dataset with a single run and no confidence intervals. The paper appropriately frames this as a preliminary investigation ("our primary objective for this task is to find out if BDIA can help to alleviate the over-fitting issue"), but the evidence for the claim that BDIA "significantly alleviates" overfitting would be much stronger with multiple seeds, a named dataset, and perplexity reporting.

- **Side information block count inconsistency** — Line 297 states side information \(\{\boldsymbol{s}_k\}_{k=0}^{3}\) is stored for "the first 4 transformer blocks." With \(K=6\) blocks, the BDIA update applies for \(k=1,\ldots,5\), requiring 5 side information vectors (\(\boldsymbol{s}_0\) through \(\boldsymbol{s}_4\)). This small numeric discrepancy should be reconciled to avoid confusion about memory accounting.

### Trivial

- **Caption inconsistency in Figure 3/4/5** — The captions for the translation and GPT2 figures state "\(\{\gamma_k\}_{k=1}^{K-1}\) in the training procedure of BDIA-ViT were randomly drawn" when the figures are about BDIA-transformer and BDIA-GPT2, not BDIA-ViT. These are copy-paste artifacts.

## Nice-to-Haves

- **Empirical comparison with dropout** — The paper draws a conceptual analogy to dropout (Section 4.2) but does not compare empirically. A dropout ablation would help contextualize the regularization mechanism, though this is not required for the paper's core claims.
- **Memory breakdown** — A fine-grained breakdown of peak memory (model parameters, activations, side information, optimizer states) would help readers understand the sources of savings and overhead, but the aggregate numbers already make the case.
- **Broader regularization comparison** — The paper could compare to other regularizers (stochastic depth, weight decay tuning), but this extends beyond the paper's scope of enabling reversible transformers.

## Removed Points

These points from the input reviews are removed as per the filtering criteria:

1. **"Exact reversibility claim is not empirically verified"** — The paper provides a mathematical derivation (equations 11–14) showing exact reconstruction under fixed-point arithmetic. Figure 2 demonstrates the error WITHOUT quantization (motivating why quantization is needed). The derivation is the evidence; asking for an empirical plot of zero reconstruction error is a trivial confirmation of a mathematical proof, not a genuine gap.

2. **"Memory savings are overstated / incomplete accounting"** — The paper reports peak memory (693.4 MB for BDIA-ViT vs 1570.6 MB for ViT) and explicitly states these include "both the model parameters and the training states." The claim that accounting is "incomplete" misreads the paper: the 693.4 MB figure already incorporates side information overhead.

3. **"Missing reproducibility details (open-source repository URL, hyperparameters)"** — The paper contains garbled URL text (parser artifact). The original submission would have proper references. Per instructions, parser artifacts are not author errors.

4. **"Missing related works"** — Cannot be verified without external sources; per instructions, this should not be mentioned.

5. **"Comparison to RevViT is unfair"** — Not raised by reviewers; noted for completeness.

6. **Several generic/speculative concerns from the harsh critic about "could the metric be measuring a proxy" without specific textual basis** — Removed as unanchored speculation.

## Novel Insights

None beyond the paper's own contributions. The two reviews surface a clear picture: the core technical contribution (BDIA for reversible transformers) is sound and the ViT evidence is strong, but the evaluation on language tasks is incomplete in ways that prevent full assessment of the method's generality.

## Suggestions

1. **Add BLEU scores** for the translation experiment with at least 3 random seeds, along with confidence intervals. This is the single most impactful improvement.
2. **Name the dataset** and add perplexity (with multiple seeds) for the GPT-2 experiment.
3. **Resolve the side information block count** — clarify whether 4 or 5 blocks of side information are stored, and align the notation (\(\{s_k\}_{k=0}^3\) vs \(\{s_k\}_{k=0}^4\)) with the mathematics.
4. **Fix the figure captions** that incorrectly reference "BDIA-ViT" for non-ViT experiments.

## Score and Decision

**Originality:** Good — adapting BDIA from diffusion models to transformers for reversibility is a novel connection.  
**Importance of research question:** High — memory-efficient training of large transformers is a pressing problem.  
**Claims support:** Mixed — well-supported for image classification and the core reversibility claim; under-supported for translation.  
**Soundness of experiments:** Moderate — ViT experiments are rigorous (3 runs, ablation); translation/GPT2 are preliminary.  
**Clarity of writing:** Good — the technical derivation is clear; some small presentation issues.  
**Value to community:** The method is practical (preserves inference architecture) and the regularization benefit is genuine.

The core technical contribution is solid and the ViT experiments convincingly demonstrate the method's benefits. The main weakness is the incomplete translation evaluation, which is addressable. The paper should be accepted contingent on adding BLEU scores for the translation task.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
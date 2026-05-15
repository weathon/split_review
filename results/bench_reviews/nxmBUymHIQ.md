Now I have enough information to synthesize the final review.

## Summary

This paper proposes LoLoRA, a method that uses local unsupervised updates (primarily Hebbian PCA / HPCA) on the LoRA A matrix during the forward pass, avoiding the need to store activations for A's backward pass and thereby saving memory. The paper provides a theoretical result (Theorem 4.4) showing that the optimal A matrix spans the top-r eigenvectors of the input covariance matrix, which justifies the use of PCA-based local update rules. Experiments span RoBERTa-large on GLUE, LLaMA-3.1-8B on MetaMathQA, LLaVA-7B on multimodal data, and ablations on TinyLlama-1.1B.

## Strengths

- **Rigorous theoretical characterization of optimal A initialization**: Theorem 4.4 formally proves that under a random regression model, the optimal A spans the top r eigenvectors of the input covariance matrix. This result is novel relative to prior work like EVA, which provided only experimental evidence for PCA-based initialization. The connection to Oja's HPCA rule is correctly drawn, and the extension to autoencoder-based local updates (Theorem 4.6) adds breadth.

- **Comprehensive ablation study**: The paper systematically compares five local update rules (HPCA, HPCA no mean, HPCA svd-first, AE, SoftHebb) and four initialization strategies (Uniform, Orthogonal, PiSSA, EVA) across multiple ranks. This ablation (Tables 5 and 6) provides actionable guidance — HPCA and AE converge to the dominant eigensubspace and perform best, while SoftHebb degrades — strengthening the empirical foundation.

- **Memory savings maintained across multiple settings**: On MetaMathQA, LoLoRA uses 26 GB extra memory vs LoRA's 30 GB (~13% reduction). On GLUE, both LoLoRA and LoRA-FA show up to 20% less memory than standard LoRA. The memory benefit over standard LoRA is real and consistent.

- **Practical advantage of avoiding a separate precomputation pass**: Unlike EVA, which requires an offline incremental PCA pre-pass over the data, LoLoRA's online HPCA updates converge to a similar subspace during training without this overhead (as noted in the ablation summary). This is a genuine practical benefit in streaming or resource-constrained settings.

## Weaknesses

### Major

- **The method performs indistinguishably from LoRA-FA with EVA initialization across all benchmarks, undermining the claim that local updates add value.** On every experiment, LoLoRA HPCA ties with LoRA-FA (EVA) within error bars: MetaMathQA (0.829±0.004 vs 0.829±0.005), LLaVA (loss 1.075 vs 1.070), and GLUE (Tables 1-2 show no consistent advantage). The ablations tell the same story: LoLoRA HPCA (uniform) at r=8 yields perplexity 2.535 vs LoRA-FA (EVA)'s 2.536 — statistically identical. Since EVA initialization is a known one-shot precomputation from prior work (Paischer et al., 2024), the central empirical claim that LoLoRA's online *updates* provide a benefit over a good initialization is unsupported. The only remaining advantage — avoiding the EVA precomputation pass — is real but weak given that EVA is a one-time cost. The paper would need to demonstrate a scenario (e.g., non-stationary data, streaming settings, or consistent quality improvement) where online updates matter, but no such evidence is provided.

- **The theoretical analysis (Theorem 4.4) assumes i.i.d. Gaussian entries for ΔW₀, stripping away all task structure.** Under this assumption, the only structure comes from the input covariance, so the PCA subspace is optimal by construction. In real fine-tuning, ΔW₀ is highly structured by the downstream task — the assumption essentially assumes away what makes fine-tuning different from random regression. The paper acknowledges this limitation (line 392: "each submodule isolated with stationary targets") but still presents the theory as a rationale for the method. While the theory is mathematically clean and provides intuition, the gap between the assumed setting and actual fine-tuning is large enough that the theory provides only weak support for the method's practical applicability. No analysis is provided on why the assumption approximately holds in practice or whether the PCA subspace remains optimal under realistic task structure.

### Minor

- **No analysis of why local updates fail to improve over EVA initialization.** If the theory motivates online HPCA updates to handle non-stationary input distributions, the fact that LoLoRA matches (but never beats) the one-shot EVA initialization suggests either (a) the data distribution is effectively stationary during fine-tuning, or (b) the HPCA updates are not actually adapting the subspace beyond the initialization. The paper does not investigate this — e.g., by tracking the principal angles between the learned A subspace and the true PCA subspace over time. This analysis would substantially clarify whether the local updates are doing meaningful work.

- **The gap between Full LoRA and both LoLoRA / LoRA-FA is non-trivial and unaddressed.** In Table 6, Full LoRA uniformly outperforms LoLoRA by ~0.015 perplexity (e.g., 2.521 vs 2.535 at r=8). This gap is larger than any difference between LoLoRA variants. The paper does not discuss this gap or provide the reader with context on whether the memory savings justify the quality loss. Including an ablation where A is trained with SGD but B is trained with frozen A would help isolate whether the gap is due to the frozen B (low-rank bottleneck) or the local A updates.

- **Hyperparameters for the local optimizer are not analyzed.** Algorithm 1 introduces an explicit optimizer Opt_loc for matrix A with its own learning rate, and the HPCA rule uses a smoothing factor (0.98) for mean subtraction. Neither of these is ablated or discussed beyond a brief mention in the conclusion. The memory cost of Opt_loc's state is reported (Table 4 shows 24.1 GB vs LoRA-FA's 23.9 GB on LLaVA) but the sensitivity to these hyperparameters is unknown.

- **The conclusion overstates the results.** It claims "HPCA consistently outperforms standard LoRA-FA in two out of three experimental setups." Against LoRA-FA with *uniform* initialization this is true, but "standard LoRA-FA" is ambiguous — the more relevant comparison (LoRA-FA with EVA) shows no consistent advantage. On GLUE, LoLoRA and LoRA-FA (EVA) are essentially tied across all eight tasks, with neither clearly dominant.

### Trivial

- Table 4 shows LoLoRA memory (24.1 GB) slightly exceeding LoRA-FA (23.9 GB) on LLaVA; this is consistent with the extra optimizer state and is acknowledged in the conclusion. Not a flaw per se, but the Abstract's "further reducing memory" should be read as "further reducing memory vs standard LoRA" (not vs LoRA-FA) for precision.

## Nice-to-Haves

- An experiment where the data distribution shifts during training (e.g., mixed-domain curriculum) would directly test the claimed advantage of online adaptation over one-shot EVA.
- Tracking the principal angles between the learned A subspace and the true top-r PCA subspace over training steps would clarify whether HPCA converges appropriately and whether the subspace drifts.
- A one-sentence caveat in the Abstract that the method's memory matches LoRA-FA (rather than reducing beyond it) would improve accuracy.

## Removed Points

These points were flagged by reviewers but are removed for the following reasons:

- *"Abstract claim of 'further reducing memory' is misleading"* — The Abstract compares to standard LoRA, not LoRA-FA. The "further" refers to "beyond standard LoRA," which is correct (30 GB → 26 GB on MetaMathQA). The paper also acknowledges the slight overhead vs LoRA-FA in the conclusion. This is a parser-agnostic reading issue, not an author error.

- *"Section 3.2 citing Zhang et al. contradicts the paper's motivation"* — The paper coherently argues: freezing A is fine structurally, but *random* initialization of A is suboptimal. There is no contradiction. The critic conflates "freezing" with "random initialization."

- *"Theorem 4.5 is never used again"* — The result is explicitly discussed in the Implications section (line 243: "these results highlight the asymmetry of adapters A and B") and provides theoretical support for why the paper focuses on improving A rather than B. It is a supporting result, not orphaned.

- *"Section 5.1 summary claim is misleading"* — Checking the data: LoLoRA is numerically better than LoRA-FA (EVA) on 3 of 8 GLUE tasks, worse on 2, and tied on 3. "Slightly better" is a reasonable characterization, especially given that EVA initialization underperforms relative to uniform on this setting.

- Missing related works — I have no external sources to confirm whether missing references exist. This point is excluded per instructions.

- Formatting/style nitpicks — excluded per instructions.

## Novel Insights

The most thought-provoking takeaway from the reviews is the tension between the paper's theoretical framing and its empirical results. Theorem 4.4 is a clean result: under a random-target regression model, the optimal A is determined entirely by the input covariance, not the task. The HPCA updates provably converge to this subspace. But empirically, a one-shot PCA initialization (EVA) achieves identical results — meaning the local updates are, in practice, merely maintaining the initialized subspace rather than adapting to anything new. This suggests that either (a) fine-tuning distributions are sufficiently stationary that online adaptation buys nothing, or (b) the HPCA updates in the forward pass are too constrained to meaningfully adapt to task structure beyond covariance estimation. Either interpretation undermines the paper's motivating narrative. A paper that framed itself more modestly — as "a streaming alternative to EVA that avoids a separate precomputation pass" rather than "a method that improves over frozen-A baselines via local updates" — would have been more honest about what the data actually shows.

## Suggestions

1. **Reframe the contribution honestly.** The method's real value is as a *streaming replacement for EVA initialization* that avoids a separate precomputation pass, not as a method that improves over well-initialized LoRA-FA. The paper's titling, abstract, and conclusion should reflect this.

2. **Either demonstrate a setting where online updates matter, or remove the adaptivity claim.** The most convincing path would be a controlled experiment with deliberate distribution shift during training (e.g., mixing data from different domains or tasks in a curriculum). If the HPCA updates adapt to the shifting covariance while fixed EVA does not, the claimed advantage would be demonstrated. Without such evidence, the paper should acknowledge that the current experiments show stationarity and that the method's benefit is limited to convenience (no precomputation).

3. **Add the missing baseline: LoRA-FA with PCA initialization from a single batch, then frozen.** This would cleanly separate the effect of initialization from the effect of ongoing updates. The current "HPCA (svd first)" baseline does SVD on the first batch but *continues* HPCA updates afterward, so it does not isolate the initialization effect.

4. **Investigate and discuss the Full LoRA gap.** The 0.015 perplexity gap between Full LoRA and LoLoRA (Table 6) should be acknowledged and contextualized. If this gap is inherent to any method that freezes A's backward pass, that is an important limitation to state explicitly.

5. **Ablate the local optimizer hyperparameters.** The smoothing factor (0.98) and local learning rate affect convergence of HPCA and are worth analyzing, even briefly, to help practitioners apply the method.

## Score and Decision

**Calibration anchors (all from human review corpus):**

| Path | Avg Score | Comparison |
|------|-----------|-----------|
| OXmRvlihi3.md (LoRA-FA paper) | 3.50 | Very similar topic and structural problem: method doesn't clearly outperform simpler baselines. Current paper has stronger theory but equally weak empirical case. |
| f3KD7jfSWY.md (CERSA) | 4.50 | Comparable quality level — both have memory-efficiency motivation with incremental empirical benefit over baselines. |
| 4nNqVpC3td.md (LoRA-DA) | 5.00 | Stronger theoretical framework, similar empirical modesty. Current paper is slightly weaker empirically. |
| kObvnQ6pUx.md (Gradient Intrinsic Dimensionality) | 5.50 | Clearer empirical advantage demonstrated; the method actually improves over baselines. Current paper is notably weaker. |
| f9M9LgE5kt.md (LaLoRA) | 5.00 | Better empirical evaluation and clearer practical benefit. Current paper has stronger theory but less convincing results. |
| QD4DL0OUmZ.md (LoRAct) | 4.00 | Similar tier — both papers address activation memory in fine-tuning with methods that don't strongly outperform alternatives. |
| KXJa6pPx0o.md (LoRA-SB) | 4.00 | Similar pattern: theory-driven method with modest empirical differentiation from existing approaches. |
| EjH5I9ziug.md | 2.50 | Much weaker paper — unclear methodology, poor experiments. Current paper is substantially stronger. |

The paper has a clean theoretical result and a reasonable experimental scope, but the central empirical finding — that LoLoRA performs indistinguishably from LoRA-FA (EVA) — does not support the claimed contribution of online local updates. The method's only clear advantage (avoiding a separate precomputation pass) is modest relative to the complexity it introduces. Compared to accepted papers in this space (avg ~5.5+), the empirical story is too weak.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
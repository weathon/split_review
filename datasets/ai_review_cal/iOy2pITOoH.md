- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 6, 5
Now I have all the information I need. Let me produce the consolidated final review.

---

## Summary

Spark Transformer modifies the standard Transformer architecture to achieve sparse activations in both FFN and attention through two key ideas: (1) a dimension-splitting trick that repurposes a subset of input dimensions as a low-cost predictor (no extra parameters), and (2) a statistical top-\(k\) operator that estimates a threshold via the sample mean and standard deviation (O(d) FLOPs) rather than sorting. Training a Spark Gemma-2 2B model from scratch using the Gemma-2 recipe, the paper reports 8% nonzeros in FFN activations and ≤256 attended tokens, yielding a 3.1× FLOPs reduction and 1.7–1.79× wall-clock speedup on CPU inference while matching Gemma-2 on standard benchmarks.

## Strengths

1. **High sparsity with matched quality on standard benchmarks**: Table 2 shows Spark Gemma-2 achieves only 8% FFN nonzeros and ≤256 attended tokens while matching Gemma-2 on benchmarks (e.g., MMLU 55.9 vs. 55.6, HellaSwag 71.9 vs. 72.0). This directly supports the core claim of drastic FLOPs reduction without quality loss on the evaluated tasks.

2. **Theoretically grounded and efficient statistical top-\(k\)**: Section 2 introduces Statistical-Top\(_k\), an O(d)-FLOP alternative to O(d log d) sorting. Theorem 1 provides a rigorous error bound (vanishing as d grows) under an i.i.d. Gaussian assumption, and Theorem 2 establishes continuous differentiability, supporting gradient-based training. The variational form (Eq. 5) connects it to soft thresholding.

3. **Measured CPU speedups on real hardware**: Figure 3 reports 1.35–1.79× decoding speedup on a 16-core CPU and 1.70× prefill speedup (Table 3), with 86 ms/token decode on a 4-core CPU. These are concrete efficiency gains validated in gemma.cpp, not just theoretical FLOP counts.

4. **Minimal training overhead from statistical top-\(k\)**: Figure 4 demonstrates that Statistical-Top\(_k\) introduces negligible training slowdown compared to the JAX approximate top-\(k\) operator (approx\_max\_k), even at low recall. This confirms its practical value for large-scale training.

5. **Unified single-stage framework**: The dimension-splitting predictor (Eq. 9, 14) handles both FFN and attention sparsity with no extra parameters and no post-training stage — a clean architectural contribution that contrasts with prior multi-stage approaches.

## Weaknesses

### Fatal

None.

### Major

1. **No controlled baseline isolating the predictor from the sparsity itself**. The paper compares Spark Gemma-2 against the dense Gemma-2 baseline and against existing methods (ProSparse, LLaMA ReGLU) at different scales and architectures. There is no ablation comparing Spark Transformer against a simple alternative — e.g., applying an exact top-\(k\) mask (by sorting) to the same Gemma-2 architecture at the same sparsity level, without the dimension-split predictor. Without this control, the reader cannot determine whether the predictor and Statistical-Top\(_k\) provide any benefit over brute-force top-\(k\) thresholding at the same sparsity level. The claim of "superiority over existing methods" — particularly over methods that use post-training sparsification — is therefore underdetermined by the current evidence. *Why it matters: This is the central experimental question for a method paper. The current design does not rule out the hypothesis that a simpler pipeline (e.g., fine-tune Gemma-2 with a standard top-\(k\) mask) would achieve similar quality and sparsity.*

2. **No evaluation on tasks requiring long-range dependencies**. The Spark Attention mechanism caps attended tokens at 256 out of an 8k context window — a 32× reduction. The paper evaluates only on standard benchmarks (MMLU, HellaSwag, ARC, etc.), which typically rely on short contexts (≤2k tokens). Without evaluation on long-context benchmarks (e.g., LongBench, RULER, or evidence-retrieval tasks with 4k+ context), the claim that attention sparsity is "harmless" has not been tested in the regimes where it would matter most. *Why it matters: If the attention sparsity causes degradation on long-context tasks, the practical value of the approach is substantially limited.*

### Minor

1. **Hyperparameter ablation (Fig. 5) is limited to 25k steps (~5% of 480k training)**. The ablation for \(r\) and \(k\) reports only early-training loss curves, not final benchmark performance. While the trends are suggestive, early loss is not reliably predictive of end-of-training quality — a full-training ablation for at least one alternative choice (e.g., \(r=256\) or 3% sparsity) would be more convincing.

2. **Attention design choices are not ablated**. The Spark Attention mechanism (Eq. 14) uses a two-path design with a softplus nonlinearity on the second path, described as "empirically observed to offer quality benefits" — but no ablation compares this against simpler alternatives (e.g., applying Statistical-Top\(_k^{(-\infty)}\) directly to the full score \(K^\top q\), replacing softplus with identity or ReLU, or using only the predictor path). The reader cannot tell whether this design complexity is necessary for the reported quality.

3. **Training FLOPs and sparsity utilization are not clearly stated**. The paper trains using the Gemma-2 recipe but does not clarify whether the sparse activation patterns are exploited during training to reduce training FLOPs, or whether the model is trained with dense computation and sparsity is only exploited at inference. The training slowdown measured (Figure 4) captures only the overhead of computing Statistical-Top\(_k\), not the full training FLOP picture. This should be stated explicitly.

### Trivial

None.

## Nice-to-Haves

- A FLOPs and wall-clock breakdown by component (predictor, FFN main, attention main, projections) would help explain the gap between the 3.1× FLOPs reduction and the 1.7–1.79× measured speedup.
- A comparison against a ReLU-based Gemma-2 variant would strengthen the motivation that modern gated activations lack natural sparsity.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Table 2 is a black box relying on visual extraction"** — The table exists as an image in the original submission; the text-parser could not render it. This is a parser artifact, not a paper flaw.
2. **"Section D.1 cannot be verified"** — The appendix exists in the original submission (referred to as Sections D.1, D.2). Per policy, missing appendix content is a parser artifact, not an author error.
3. **"FLOPs counts in Table 1 lack derivation"** — The paper provides equations for FLOPs calculations (Eq. 10, 11, 15, 16) and the text around Table 1 describes the derivation. This criticism is factually incorrect.
4. **Criticisms about missing related work** — Per policy, no external sources are available to confirm whether specific works are missing.
5. **"Superiority over existing methods is not supported" (as phrased)** — The primary comparison against the dense Gemma-2 baseline is valid and supports the core claim. The concern about the *predictor's* specific value is kept separately as Major weakness #1.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the need for tighter controlled experiments but do not identify novel observations about the method itself.

## Suggestions

1. Add a controlled ablation: train/fine-tune Gemma-2 2B with exact top-\(k\) (sorting-based) masking at the same 8% / 256-token sparsity levels, without the dimension-split predictor, and compare quality. This directly isolates the value of the predictor design.
2. Evaluate on at least one long-context benchmark (e.g., LongBench with contexts of 4k+ tokens) to validate that the ≤256-token attention limit does not degrade performance on tasks requiring long-range reasoning.
3. Ablate the attention design: compare the proposed two-path + softplus design against simpler alternatives (e.g., applying Statistical-Top\(_k^{(-\infty)}\) to the full \(K^\top q\) without dimension split).
4. Clarify explicitly whether the sparse computation paths reduce FLOPs during training or only at inference.
5. Extend the hyperparameter ablation for \(r\) and \(k\) to final benchmark performance (or at least to later training checkpoints) rather than only 25k-step loss curves.

Now I'll compose the final consolidated review.

## Summary

This paper proposes DenseAttention, a simplified attention mechanism that removes Softmax, LayerNorm, residual connections, and K/V/O projection matrices from the standard Transformer. By reducing attention to pure matrix multiplications, the authors exploit the associative property to compute exact all-pairwise interactions in O(N d²) time and O(N) memory instead of O(N² d). They introduce MaxNormActivation for numerical stability in place of Softmax and propose Cosine RelPE as a more efficient alternative to RoPE. The method is validated on the Long Range Arena (LRA) benchmark (achieving SOTA among Transformer-based models) and through BERT-scale MLM pretraining on sequences up to 16K tokens.

## Strengths

- **Exact O(N) computation with no loss of pairwise interactions.** Unlike most efficient-attention methods that rely on approximation, sparse masking, or kernel tricks, DenseAttention computes the exact same all-pairwise interactions by exploiting the associativity of matrix multiplication (Section 3.1, lines 141–150). The operation Q(K^T V) is mathematically identical to (Q K^T)V — this is a clean and principled contribution.

- **Theoretical analysis of numerical stability with provable bounds.** Proposition 1 (line 107) formally shows that removing Softmax causes output variance to grow at least cubically with input variance. Proposition 2 (line 125) shows that bounding L∞ norm of inputs controls this growth, leading to the bound max(|Z_ij|) ≤ d under scaling factor a = 1/N^{1/3} (lines 119–129). This provides mathematical grounding for the MaxNormActivation design, going beyond the purely empirical approach typical in this area.

- **New SOTA among Transformer-based models on LRA, competitive with SSMs.** Table 1 (line 225) shows DenseAttention achieves the best average score among all Transformer-based architectures on the Long Range Arena benchmark and outperforms S4 on 4 of 6 tasks. This demonstrates that removing Softmax and other components does not inherently hurt long-context modeling ability.

- **Very strong speed on long sequences.** Table 4 and Figure 2 show the high-level (non-CUDA-optimized) DenseAttention implementation achieving substantially higher throughput than FlashAttention-2 on long contexts (e.g., ~12× faster at 16K sequence length). The O(N) regime in particular enables processing of very long sequences that are impractical with standard quadratic attention.

## Weaknesses

### Major

- **No downstream task evaluation, undermining the claim of "performing similarly or better than BERT-large."** The BERT-scale experiment (Table 3) evaluates only MLM loss and accuracy on the out-of-domain C4 dataset. There is zero evaluation on any downstream NLP benchmark — no GLUE, no SQuAD, no sentence-pair tasks, no classification. Lower MLM perplexity is a necessary condition for a better language model but far from sufficient; architectural changes that reduce pre-training loss frequently fail to transfer to downstream tasks. This is especially important given the paper's radical simplifications (removing K/V/O projections, LayerNorms, one residual connection, Softmax) — changes that could plausibly degrade representational quality in ways that MLM loss alone does not capture. Without any fine-tuning evaluation, the central claim of the BERT-scale experiment is unsubstantiated.

- **Uncontrolled BERT-large comparison.** The DenseAttention model uses 32 layers versus BERT-large's 24, with different training procedures (4-stage curriculum vs BERT's original training). The paper claims "approximately the same number of parameters" (line 256) but **never reports actual parameter counts** — a critical omission. Adding 8 extra FFN layers (each with d×4d + 4d×d parameters) adds roughly 64d² parameters (~67M for d=1024), even after accounting for removed projection matrices. The training procedure is also radically different: four stages with different sequence lengths, sample counts, and batch sizes. Comparing against a single fixed BERT-large checkpoint confounds architectural differences with differences in scale, data, and training protocol, making the quality comparison uninterpretable.

### Minor

- **The speed comparison with FlashAttention compares operations of fundamentally different complexity.** DenseAttention computes a raw matrix product (XW_Q X^T X) with no Softmax, no masking, no dropout, and no elementwise normalization — these are precisely the operations that make FlashAttention's kernel design necessary. The paper frames DenseAttention as "outperforming" FlashAttention, but the two are not computing the same function. The relevant question is whether DenseAttention's computational advantage translates to better *task performance per unit time*, which is not addressed. This does not negate the speed result but overstates what it demonstrates.

- **The "drop-in replacement" claim is misleading.** The paper states the architecture "can serve as a drop-in replacement" (line 25) for the standard Transformer. In reality, DenseAttention removes Softmax, both LayerNorms, one residual connection, all biases, dropout, masking, and the K, V, and O projections, while adding MaxNormActivation at both ends of the block and requiring the PAD token to be the zero vector. This requires significant architectural changes to any existing Transformer implementation. The architecture is clearly described, so this is primarily a framing issue, but it sets inaccurate expectations.

- **The multi-head notation is underspecified.** The formulation `DenseAttention_h(X) = X W_{Q_h} X_h^T X_h` (line 167) does not define what X_h is. The paper analogizes to multi-query attention (line 170), suggesting shared K and V across heads (i.e., X_h = X for all heads), but this is not explicitly stated. This ambiguity affects reproducibility of the multi-head variant.

- **No Conclusion/Discussion section.** The paper ends abruptly with the speed evaluation (line 279). There is no discussion of limitations, failure cases, settings where DenseAttention might underperform, or analysis of which architectural simplifications are most critical. Given the radical nature of the proposed changes, a candid discussion of representational trade-offs would substantially strengthen the paper.

### Trivial

- Minor presentation issues: Table 3 does not report N=16384 results for the 4-head model or BERT baseline, making the comparison incomplete. The paper mentions "Appendix C" (line 152) but the appendix is not present in the submission.

## Nice-to-Haves

- A controlled ablation comparing DenseAttention against standard Transformer with the same number of layers, same training data, and same training budget would isolate the effect of the architectural changes.
- Statistical significance or multi-seed variance reporting would strengthen the empirical claims, though single-run reporting is common practice in large-scale pretraining experiments.
- Analysis of attention patterns (e.g., effective receptive field, entropy of attention distributions) would help validate the claim that removing Softmax does not harm the model's ability to attend selectively.
- Direct comparison against other linear-time attention mechanisms (Performer, cosFormer, Linear Transformers) on LRA or a shared benchmark would clarify the paper's positioning relative to prior efficient-attention work.

## Removed Points

These points were flagged for removal; treat with caution:

- *"Missing comparison against other linear attention methods (Performer, cosFormer, etc.)"* — The LRA benchmark paper itself provides many such baselines, and the paper compares against the SOTA Transformer baselines (Amos et al., 2024) and S4. This criticism is partially inaccurate.
- *"No statistical significance/variance reporting"* — Common practice in large-scale pretraining experiments; moved to Nice-to-Haves.
- *"No analysis of attention patterns"* — Would strengthen but not a weakness; moved to Nice-to-Haves.
- *"Cosine RelPE — RoPE's overhead is negligible"* — This is a debatable implementation claim on both sides; the paper does not provide measurements proving RoPE is a bottleneck, but neither does the critic prove it isn't. Removed as speculative.
- *"Proposition 1 analysis is for a simplified case"* — The paper explicitly acknowledges this (line 105: "considering simplified version"). This is the paper describing its own limitation, not a hidden flaw.
- *"Section 4.1 — LRA doesn't compare against Performer/Linear Transformers"* — Redundant with the first removed point.

## Novel Insights

The most striking observation across the reviews is the tension between the paper's clean theoretical contribution (exact O(N) attention via associativity — mathematically elegant and clearly superior to every approximation-based linear attention method on principle) and the fragility of its empirical validation. The reviewers converge on the idea that the paper has a genuinely interesting architectural insight but overclaims its empirical support. Another noteworthy insight is that the paper's strongest empirical result (LRA SOTA among Transformers) is on a benchmark where the paper's main efficiency advantage (linear time) is least relevant — LRA sequences are up to 16K, but the O(N²) regime is still viable there. This suggests the architecture's conceptual validity is best demonstrated on LRA, while its practical efficiency advantage would be most relevant on much longer sequences (>64K), which the paper does not test.

## Suggestions

1. **Add downstream fine-tuning evaluation.** Fine-tune the DenseAttention model on GLUE/SuperGLUE and compare against BERT-large fine-tuned under identical conditions. This is the single highest-impact addition — without it, the claim of matching BERT-large's quality is unsupported.
2. **Report explicit parameter counts and compare models with the same number of layers.** Train a 24-layer DenseAttention model and report exact parameter counts for all architectures, making the comparison controlled and interpretable.
3. **Frame the speed comparison more carefully.** Acknowledge that DenseAttention and FlashAttention compute different functions, and report task-performance-per-second rather than raw throughput.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
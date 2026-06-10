Here is the final consolidated review.

---

## Summary

SOLOS proposes a training-efficient framework for context-compression-augmented LLMs, enabling training on sequences up to 100K tokens on modest hardware (8× RTX3090). Its core technical contribution is a sparse optimization scheme combining (a) decoder-only incremental computation to avoid recomputation across segments, and (b) reservoir sampling-based gradient estimation that keeps encoder memory constant regardless of sequence length while providing unbiased gradient estimates.

## Strengths

- **Reservoir sampling for unbiased gradient estimation with formal proof (Section 3.4, Eq. 12–15).** The paper derives that reservoir sampling with a correction factor of (j−1)/S yields an unbiased estimator of the true gradient. This is a principled improvement over ad-hoc eviction strategies (local window or random), which the paper correctly identifies as either biased or infeasible. The proof is mathematically sound: unbiasedness follows from marginal probabilities and linearity of expectation, independent of sampling correlations.

- **Incremental computation on decoder with equivalence proof (Section 3.4, Eq. 10).** The paper identifies that naive incremental computation causes redundant recomputation of ∂m_i/∂Θ across segments. Its solution—running incremental backpropagation only on the decoder, accumulating ∇_{m_i}, and performing a single backward pass through the encoder at the end—is accompanied by a formal equivalence proof via an indicator function, provably eliminating recomputation while matching the exact gradient.

- **Clean architectural design with concrete parameter count (Section 3.2).** The parallel encoder-decoder architecture using dual LoRA adapter sets (one for the projector, one for the encoder) with weight sharing is clearly described. The paper documents a specific 2% parameter increase for LLaMA2-7B, supporting the claim of training feasibility on limited hardware.

- **Well-motivated problem framing (Section 1).** The paper convincingly argues that prior context-compression methods (AutoCompressor, Activation Beacon) underperform because they cannot train on long sequences due to computational cost, and that enabling long-sequence training is the path to closing the gap with uncompressed models.

## Weaknesses

### Fatal

None.

### Major

1. **Entire experiments section (Section 4) is absent from the extracted text.** The paper jumps from Section 3.4 directly to Section 5 (Limitations). Table 3 (LongBench results) is an unreadable embedded image. No experimental setup, quantitative results, ablation studies, baseline comparisons, or training hyperparameters are present in the available text. The abstract makes strong empirical claims ("significantly outperforms other context-compression-augmented LLMs," "matches the performance of state-of-the-art long-context models," "near-perfect reconstruction") that cannot be verified from the presented material. This is the paper's most serious issue — without the experiments, the core evidentiary basis is inaccessible.

2. **No empirical study of reservoir sampling gradient variance or convergence.** The paper proves unbiasedness (first moment) of the reservoir-sampled gradient estimator, which is theoretically sound. However, it provides no analysis of gradient variance, no comparison of convergence trajectories between reservoir-sampled and dense gradients, and no diagnostic experiments showing the practical fidelity of the estimator. The per-segment correction factor (j−1)/S grows with segment index, potentially amplifying gradient noise for early segments in very long sequences. Without variance analysis, it is unclear whether the estimator is practically useful beyond being theoretically unbiased.

### Minor

1. **Segment independence trade-off unexamined (Section 3.3).** The paper frames independent segment encoding (where later segments cannot attend to earlier compressed representations during encoding) as a simplifying strength and departure from prior work (AutoCompressor, Activation Beacon). However, the potential cost of this design choice — losing fused cross-segment representations that enable long-range coherence — is not empirically analyzed. The paper asserts that the decoder's attention over concatenated KV caches can compensate, but provides no supporting evidence.

2. **No training details reported in the extracted text.** Data sources, learning rates, batch sizes, number of segments \(k\), segment length \(l\), number of special tokens \(c\), reservoir size \(S\), LoRA rank, and training steps are absent from the available text. These are necessary for reproducibility.

3. **No wall-clock training time reported.** The paper emphasizes "8× RTX3090" but does not state the actual training duration for 100K-token sequences.

4. **No comparison to a non-compressed dense model on a matched compute budget.** The inference-cost comparison in Figure 1(a) is referenced but the actual latency/memory numbers are absent from the text.

### Trivial

- Notation in Eq. (5) (∇Θ^{J}j) and the indicator function in Eq. (8–9) contain formatting artifacts that should be cleaned up.

## Nice-to-Haves

- A controlled experiment training SOLOS at multiple sequence lengths (2K, 8K, 32K, 100K) to directly validate the central hypothesis that longer training drives performance gains.
- A small-scale convergence diagnostic comparing reservoir-sampled vs. dense gradient trajectories on a short sequence (k ≤ 8) where dense training is feasible.
- An ablation study isolating the impact of independent vs. fused segment encoding.

## Removed Points

These points were raised by reviewers but removed after verification against the paper:

- **"Reservoir sampling proof ignores correlation structure; unbiasedness claim is incomplete"** — The harsh critic argued that ignoring joint distribution correlations across segments/time steps invalidates the unbiasedness claim. This is mathematically incorrect. Unbiasedness (E[estimator] = true value) depends only on marginal expectations and linearity of expectation, which hold regardless of correlation. The proof in Section 3.4 is valid for the claim it makes. The critic's secondary point about variance (which the paper does not study) is retained as Major weakness #2.
- **"The paper's critique of other methods applies equally to SOLOS"** — The paper criticizes prior methods for having prohibitive training cost because they use the LLM as context encoder. SOLOS also uses the LLM as context encoder but *solves* the cost problem via memory-efficient optimization. The critique identifies the problem; SOLOS provides the solution. This is a clear distinction.
- **Notation/formatting nitpicks** (garbled equations, "binom(1)(0)", infinite summation ranges) — These are parser artifacts that do not exist in the original submission.
- **Missing appendix content, proofs, or references** — Removed per hard rules: the parser strips these sections from all papers; they exist in the original submission.
- **"No comparison of 8× and 32× compression ratios"** — This comparison would appear in the (parser-stripped) experiments section; cannot be verified as present or absent from the original.

## Novel Insights

The reviews converge on a point not explicitly made in the paper: the per-segment correction factor (j−1)/S in the reservoir sampling estimator grows monotonically with segment index. For very long sequences (e.g., 100K tokens → many segments), early segments receive large correction factors, which could amplify gradient noise even if the estimator remains unbiased. This variance-amplification effect — distinct from the unbiasedness property the paper focuses on — is the practical concern that should be empirically investigated. The paper's analysis stops at the first moment, but practical training stability depends on higher moments.

## Suggestions

1. If experiments exist in the original submission, ensure they are presented as readable text rather than embedded images in any camera-ready version. The claims in the abstract require verifiable evidence.
2. Add a small-scale diagnostic experiment comparing the convergence trajectory of reservoir-sampled training against dense training on a short sequence (k ≤ 8).
3. Include all training hyperparameters (k, l, c, S, LoRA rank, learning rate, batch size, data sources) in the main paper.
4. Add an ablation quantifying the impact of independent vs. fused segment encoding to justify the architectural departure from prior work.

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>
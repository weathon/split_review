Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper introduces MC-SMoE, a framework for compressing Sparse Mixture-of-Experts (SMoE) models by first merging redundant experts guided by routing statistics (activation frequency and router-logit similarity), then compressing the merged experts via low-rank and structural sparse decomposition. On *switch-base-32*, M-SMoE achieves ~60% memory reduction with performance matching or exceeding the full SMoE on several tasks, while MC-SMoE reaches ~80% memory reduction with modest degradation on most benchmarks. The work is well-motivated, the ablations are thorough, and the core idea of using routing-policy signals to guide merging is novel.

## Strengths

- **Routing-statistics-guided merging is empirically validated and outperforms alternatives.** The paper uses router logits (not weights or gradients) to measure expert similarity and shows consistent superiority over seven other similarity functions (Table 4). This is a genuine methodological contribution that directly supports the paper's main claim.

- **Merge-then-compress pipeline delivers substantial efficiency gains.** MC-SMoE achieves ~80% memory reduction with <1% performance degradation on 5 of 8 tasks (MRPC, COPA, SQuAD, WikiQA, HotpotQA). The comparison against compression-only (C-SMoE) in Table 5 cleanly isolates the benefit of merging before compressing, showing MC-SMoE outperforms C-SMoE at a smaller model size.

- **Thorough ablation study validates each design choice.** The paper isolates the contributions of adaptive merging ratios, permutation alignment, frequency-weighted averaging, and knowledge distillation (Tables 2–6 and associated analyses). Each component is shown to improve over its ablated counterpart, giving strong empirical support to the design.

- **Broad evaluation across 8 benchmarks.** Results are reported consistently on diverse tasks (classification, QA, entailment, sentiment) using *switch-base-32*, with additional zero-shot evaluation on *fairseq-moe-15b* (in appendix), spanning two SMoE architectures.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The dominant expert selection rule, though present in Algorithm 1, is not explained in prose with sufficient clarity for direct reproduction.** Algorithm 1 specifies `$\mathcal{D} \gets \texttt{top}\left(k, \texttt{row-normalize}(\mathtt{A})\right)$` and the Table 2 caption states "it maintains an average of 8 experts in other SMoE layers." However, the paper never states the exact computation of $k$ — i.e., whether $k = 8 \times (\text{non-first SMoE layers})$, or whether $k$ is determined by a different global budget formula. The footnote about normalizing the most active expert to 1.0 only guarantees at least one dominant expert per layer but doesn't resolve how the global threshold is set. Since this directly determines the compression ratio, a one-sentence clarification would meaningfully improve reproducibility.

2. **The abstract's "virtually no loss in performance" overstates results on several tasks.** While the paper's detailed text (Section 4.2) correctly restricts the "<1% degradation" claim to a specific subset of tasks, the abstract makes an unqualified blanket claim. For MC-SMoE, SST-2 drops from 95.75 to 93.35 (2.4 pt), MultiRC drops from 76.19 to 73.98 (2.2 pt), and WinoGrande drops from 61.80 to 59.52 (2.3 pt). These are above what many readers would consider "virtually no loss." Tightening the abstract's language to match the paper's own careful phrasing in Section 4.2 would improve accuracy without weakening the contribution — the results are still strong.

3. **Computational overhead of the merging setup is not discussed.** The paper states that activation frequencies are computed using "a randomly picked subset of training data" but gives no guidance on subset size, the time required for forward passes to collect router logits, or the wall-clock cost of the merging procedure itself. For practitioners evaluating whether this method is worth adopting, this information is relevant.

### Trivial

1. **Knowledge distillation description has a minor inconsistency.** The training details (Section 4.1) only mentions applying KD to M-SMoE and MC-SMoE, while the table caption and Section 4.3 explicitly state KD is used for all baselines. The paper is unambiguous overall about KD being applied uniformly, but the training details section could be updated for consistency.

## Nice-to-Haves

- A brief discussion of the wall-clock time or data requirements for the merging procedure (subset size, forward-pass cost) would help practitioners assess practical feasibility.
- The stable-rank analysis (Figure 3/4) is presented as an observation that "suggests" a mechanism. Adding a sentence acknowledging its correlational nature would be appropriate (currently the text is careful but could be more explicit).

## Removed Points

- **Zero-shot results "missing" from main text** — Removed per policy: the parser strips appendix content that exists in the original submission. The paper states zero-shot evaluation was conducted on *fairseq-moe-15b*; these results are assumed to be in the appendix.
- **KD ambiguity as a structural concern** — The paper states "we by default use KD for all merged and compressed SMoEs, including our M-SMoE, MC-SMoE, and all baselines" (Section 4.3), which is explicit. The reviewer's cited inconsistency is a one-sentence phrasing issue in Section 4.1, not a real ambiguity.

## Novel Insights

Beyond the paper's own contributions, a genuinely novel observation emerging from these reviews is that the paper's central claim — routing statistics contain the clues for effective expert merging — is supported by a surprisingly clean ablation hierarchy: router logits work best because they directly reflect the *learned routing distribution* of each expert, which is a better similarity signal than weight-space distance, feature overlap, or gradient alignment. This insight is not merely "router logits work" but rather that the router's output distribution naturally encodes the co-adaptation pattern of experts during training, which weight-based or gradient-based measures fail to capture. This could inform future work on SMoE analysis beyond compression.

## Suggestions

1. Add one sentence to Section 3.1 explicitly stating the formula for determining $k$: e.g., "Let $L'$ be the number of non-first SMoE layers; we set $k = 8 \times L'$, maintaining an average of 8 dominant experts per layer."
2. Replace "virtually no loss in performance" in the abstract with a more precise phrase such as "≤1% degradation on most tasks and ≤2.5% on the rest, while achieving up to 80% memory reduction."
3. Add a sentence in Section 4.1 or 4.3 about the size of the subset used to compute activation frequencies (e.g., number of batches or tokens) and approximate runtime overhead.

## Score and Decision

This is a solid paper with a genuine contribution, thorough experiments, and well-designed ablations. The weaknesses are minor (reproducibility clarity on one parameter, a slight overstatement in the abstract, and a missing practical detail). None threaten the core claims. The method is well-motivated and empirically supported.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
Now I have verified the paper is accessible and complete. Let me produce the final consolidated review.

**Decision: Accept**

Here is my reasoning: The paper's core claims (compute-matched performance matching BPE baselines, robustness advantages, cross-lingual adaptation benefits) are all well-supported by extensive experiments at up to 7B parameters. The five retained weaknesses are minor — none threaten the central contribution. The missing inference benchmarks and variance reporting are standard omissions in large-scale LM papers that can be addressed in a revision. The Lambada analysis request and word accuracy validation are valuable but secondary. The cross-lingual confound is acknowledged by the authors themselves. Compared to the criteria of a top venue, this paper makes a solid, well-scoped contribution to an important problem, with honest limitations and clear experiments.

## Summary

This paper proposes a hierarchical autoregressive transformer that processes text at both character and word levels, eliminating the need for a trained subword tokenizer. A lightweight bidirectional encoder produces word embeddings from characters, a causal word-level backbone processes the word sequence, and a compact decoder produces next-character predictions. Experiments at 1B, 3B, and 7B scales with compute-matched comparisons show on-par performance with BPE baselines on downstream tasks, significantly better robustness to input perturbations, and faster cross-lingual adaptation with better knowledge retention.

## Strengths

- **Scaling to 7B parameters with compute-matched comparison against subword baselines** (Section 4.3, Table 1). This is a substantial scaling advance over prior hierarchical approaches (MegaByte: 320M, Thawani et al.: 77M, Sun et al.: ~100M), and the compute-matched methodology (Section 4.2) ensures fairness.

- **Systematic robustness evaluation across four perturbation types on four benchmarks** (Section 4.4, Figure 4). The baseline suffers a 3× larger accuracy drop on all-caps perturbations. This is a novel contribution — prior hierarchical work (Sun et al., MegaByte, Thawani et al., Slagle) did not investigate robustness.

- **Cross-lingual continued pretraining with 1.9× faster training, higher German accuracy, and better English retention** (Section 4.5, Figure 5). This concretely demonstrates three claimed benefits simultaneously — flexibility, faster adaptation, and knowledge retention — that no tokenizer-based model can match.

- **Controlled ablation separating architecture quality from splitting-rule quality** (Section 4.3). The hierarchical architecture with 8-byte splitting improves over MegaByte by 2.6 ppt in byte accuracy, showing architecture superiority independent of the splitting rule. The additional gain from whitespace splitting further validates semantic splitting as a useful inductive bias.

- **Formal computational cost analysis with empirical token/word ratios** (Section 2.3, Figure 2). The clean FLOPs model (Eq. 7–8) and the measured ratio S_W ≈ 0.69 S_T give concrete, verifiable justification for the efficiency advantage.

## Weaknesses

### Fatal

None.

### Major

None — the paper's core claims (compute-matched performance, robustness, cross-lingual adaptation) are all well-supported by the evidence presented. No issue threatens the central contribution.

### Minor

- **Lambada result reported but not analyzed.** The hierarchical model outperforms the baseline by up to 68% relative at 7B (Table 1 and Section 4.3). While this does not contradict the "matching performance" claim (it strengthens it), the complete absence of analysis leaves the mechanism mysterious — is it better handling of rare/morphologically complex word endings? An evaluation artifact? A genuine architectural advantage for cloze-style tasks? Understanding this would substantially deepen the scientific contribution.

- **No variance or confidence intervals reported.** Every downstream score in Table 1 and Figure 4 is a single point estimate. Several comparisons have margins of 0.1–0.2 ppt (MMLU at 1B: 25.3 vs 25.4; HellaSwag at 7B: 59.8 vs 59.9; WinoGrande at 3B: 56.8 vs 56.7), making it impossible to tell whether the observed differences are meaningful or within evaluation noise. The paper's central "matching performance" claim rests on these numbers.

- **Inference characteristics not benchmarked.** The paper describes the nested-loop inference procedure and claims "near parity of FLOPs" via KV caching (Sections 2.2, 2.3), but provides no measurements of latency, throughput, or memory usage. For practitioners evaluating adoption, these are primary practical concerns.

- **Cross-lingual confound acknowledged but not resolved.** The paper correctly notes that German data causes BPE tokenizer fragmentation, making the baseline more expensive per document and the hierarchical model 1.9× faster (Section 4.5). Dotted lines in Figure 5 partially address this, but the comparison is still asymmetric in data volume. A control where both models see the same number of German tokens (not FLOP-matched) would better separate architectural adaptation from data-quantity effects.

- **Word accuracy as guiding metric is an untested assumption.** The architecture sweep (Section 4.1) adopts word accuracy over byte accuracy based on intuition: byte accuracy "can be improved by merely making the decoder better at completing words given the first few characters, which does not improve word accuracy." This reasoning is plausible but empirically unvalidated — does word accuracy actually correlate better with downstream performance than byte accuracy?

### Trivial

None.

## Nice-to-Haves

- **Same-backbone-size ablation.** A comparison where the hierarchical model uses the same backbone size as the baseline (accepting higher compute per token) would isolate whether the architecture's design itself contributes beyond the parameter reallocation advantage. This is a nice-to-have rather than a core gap, since the compute-matched comparison is the correct primary framing.

## Removed Points

These points were flagged during meta-review filtering; treated with caution.

- **Same-backbone-size ablation as a weakness:** Removed — it misunderstands the paper's framing. The architecture's efficiency advantage (enabling a larger backbone for the same compute) is inherent to the design, not a confound. Separating "architecture" from "parameter allocation" would require denying the architecture its primary benefit.
- **"17 downstream tasks" vs visible table count:** Removed per hard rules — the parsed PDF renders table images that are not machine-readable; the paper text states 17 tasks. Parser artifacts do not constitute author errors.
- **Attention FLOPs quadratic scaling concern:** Removed — the paper explicitly acknowledges this as a standard simplification and notes that feed-forward FLOPs dominate for typical settings.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Add confidence intervals or standard errors to Table 1 and Figure 4.
- Analyze the Lambada result: break down per-word accuracy by frequency, morphological complexity, and whether the evaluation protocol interacts differently with the two architectures.
- Report inference throughput (tokens/second) and KV cache memory for both architectures at comparable FLOP budgets.
- Validate the word-accuracy vs byte-accuracy choice by correlating both metrics with downstream task performance across the architecture sweep data.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>
Now I have all the evidence I need. Let me produce the final consolidated review.

---

## Summary

This paper proposes MC-SMoE, a two-stage method for efficient Sparse Mixture-of-Experts (SMoE) inference. First, M-SMoE merges redundant experts using routing-policy-guided grouping: it identifies "dominant" experts by activation frequency, groups non-dominant experts by router-logit similarity, and performs frequency-weighted averaging. Second, the merged experts (which exhibit lower stable-rank) are further compressed via low-rank + sparse decomposition. Experiments on switch-base-32 across 8 benchmarks show M-SMoE achieves ~60% memory reduction with matched or better performance on most tasks, and MC-SMoE reaches ~80% memory reduction with minor degradation.

## Strengths

- **Routing-statistics-guided expert grouping is novel and well-validated.** The paper introduces a principled method for grouping experts using router-logit cosine similarity (Eq. 1) and activation-frequency-based dominance, which departs from prior merging methods that assume shared initialization. The ablation in Table 4 shows router-logits consistently outperforms 7 alternative similarity functions (e.g., COPA: 68.0% vs. next-best 65.0%).

- **Merged experts are empirically shown to be more compressible.** Figure 3 demonstrates that stable-rank systematically decreases after merging. The practical payoff is in Table 7: MC-SMoE (merge+compress, 381M) outperforms C-SMoE (compress-only, 570M) by 3 points on COPA and 0.37 F1 on SQuAD, despite being 33% smaller — directly validating that merging improves compressibility.

- **Thorough ablation of each design component.** Every design choice — adaptive vs. uniform merging ratio (Table 2), router-logits vs. 7 alternative grouping functions (Table 4), frequency-weighted vs. uniform/Fisher merging (Table 6), permutation alignment (Table 7), and knowledge distillation (Table 8) — is isolated and validated independently, with the proposed choice consistently winning.

- **Comprehensive evaluation across diverse settings.** Results span 8 supervised fine-tuning benchmarks on switch-base-32 (encoder-decoder) and zero-shot evaluation on fairseq-moe-15b (decoder-only, 15B parameters), covering both model families. The main results (Table 1) show M-SMoE matches or exceeds Full SMoE on 5/8 tasks, and MC-SMoE achieves 80% memory reduction with <1% degradation on 5/8 tasks.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **The causal framing of the low-dimensionality claim overstates the evidence.** The paper says merging "promotes" and "encourages" lower dimensionality (Section 3.2 title: "Merging Encourages Expert Decomposition"; line 98: "promotes a lower dimensionality"; line 95: "lower dimensionality achieved through the merging process"). The evidence is correlational: stable-rank decreases after merging, and MC-SMoE outperforms C-SMoE. The practical benefit (MC-SMoE > C-SMoE) is real, but the causal mechanism is not established — the decrease could simply reflect that averaging weights dampens extreme singular values. This does not undermine the empirical contribution, but the language should be softened to describe an observed property rather than a causal effect.

2. **Sensitivity to the global budget $k$ is not explored.** Algorithm 1 takes $k$ (the number of retained experts) as a fixed input. Only one configuration (~8 experts/layer after skipping the first) is evaluated. Without analysis of how performance varies with $k$ (e.g., retaining 4 or 12 experts/layer), the method's robustness is unclear, and practitioners lack guidance for choosing this parameter. This is a straightforward experiment (vary $k$, report the cost-performance trade-off curve) that would meaningfully strengthen the paper.

3. **The first SMoE layer is excluded from merging without explanation.** The paper states (Table 1 caption) that "the first SMoE layer has a profound impact on the model's performance, and merging it results in more significant performance degradation," citing LLM-Pruner. No diagnostic analysis is provided (e.g., activation frequency distribution, router logit patterns, or stable-rank behavior in the first layer vs. later layers). This makes the method not fully general — it relies on a case-by-case decision about which layers to skip — and raises the question of whether this limitation extends to other SMoE architectures (e.g., the decoder-only fairseq-moe-15b results).

### Trivial

1. **FLOPs definition is incorrect.** The footnote on line 20 defines FLOPs as "floating point operations per second." FLOPs (lowercase 's') conventionally means floating-point operations (total count); FLOPS (uppercase 'S') means operations per second. The paper then uses TFLOPs to report total operations per forward pass (line 168, Table 1), which is inconsistent with its own definition. This is a minor notational error that should be corrected.

2. **"Virtually no loss" is slightly overstated.** While the paper quantifies degradation as <1% on 5/8 tasks (line 202), the remaining tasks show larger drops: SST-2 drops 95.75→93.35 (~2.4%) and MultiRC drops 76.19→73.98 (~2.2%). The abstract's "virtually no loss" is defensible as a summary but would benefit from the qualification already present in the main text.

## Nice-to-Haves

- **Control for model size in the merging-vs-compression comparison.** The current comparison (Table 7) shows MC-SMoE (381M) > C-SMoE (570M), which is already strong evidence. A tighter control — comparing MC-SMoE against a C-SMoE variant explicitly pruned to the same 381M parameter count — would further strengthen the claim that merging improves compressibility specifically (rather than simply being a more effective way to achieve a small model).

- **Report the overhead of obtaining the compact model.** The paper focuses on inference efficiency (memory, FLOPs) but does not report the cost of the merging process itself: computing activation frequencies (one forward pass on a data subset), weight-matching alignment, and the fine-tuning/KD step. Including this would present a complete efficiency picture.

## Removed Points

- **"Lack of ablation on pipeline components" (Harsh Critic Issue 3):** Removed — factually incorrect. The paper includes ablations for uniform vs. frequency-weighted merging (Table 6), adaptive vs. uniform ratio (Table 2), permutation alignment (Table 7), and KD (Table 8). These directly isolate the novel components from auxiliary ones.

- **"Router-logit aggregation procedure is unspecified":** Removed — the procedure is clearly defined. H = W_r(X^T) produces an [n × b] matrix (Eq. 1), and cosine similarity between rows H_{i,*} and H_{j,*} (line 78) naturally aggregates across the batch. No additional aggregation step is needed.

- **"KD benefit for baselines is uncontrolled":** Removed — paper explicitly states KD is used for all methods equally (line 268: "we by default use KD for all merged and compressed SMoEs, including our M-SMoE, MC-SMoE, and all baselines").

- **"Comparison conflates model size in Table 7":** Removed — asymmetry favors the baseline (C-SMoE has 570M parameters vs. MC-SMoE's 381M), so the criticism is invalid by the reviewer's own logic.

- **"Missing zero-shot results table":** Removed — the raw text mentions zero-shot evaluation on fairseq-moe-15b (line 168), and any accompanying table would have been in a parser-stripped appendix section.

- **"First-layer skipping for fairseq-moe-15b unclear":** Removed — cannot verify against the extracted text; the zero-shot details are in a parser-stripped section of the original submission.

## Novel Insights

The reviews surface a genuinely useful observation that the reviews themselves do not fully articulate: the paper's strongest contribution is arguably not the merging algorithm per se, but the *discovery that merging and compression compose synergistically* — merging first improves compressibility, so the two operations together outperform compression alone even with fewer total parameters. This two-stage design insight (merge-then-compress) is distinct from prior work that either prunes/compresses directly or merges without further compression. The weakness about causal framing (Issue 1) actually underscores this: even if the low-dimensionality mechanism remains correlational, the practical synergy is empirically robust and directly actionable.

## Suggestions

1. Soften the causal language in Section 3.2: replace "encourages" and "promotes" with "results in" or "is empirically associated with."
2. Add a sensitivity analysis for the global budget $k$ (e.g., vary k to retain ~4, ~6, ~10, ~12 experts/layer and report the cost-performance Pareto frontier).
3. Add a brief diagnostic analysis of the first SMoE layer (activation patterns, stable-rank, or router behavior) to explain why it resists merging, or at minimum note this as a limitation for future work.
4. Correct the FLOPs/FLOPS notation in the footnote.
5. In the abstract, replace "virtually no loss in performance" with a quantified bound (e.g., "average degradation <1% across 5 of 8 tasks") to match the actual results.

## Score and Decision

This is a solid paper with a clear, practical contribution: a routing-policy-guided merging method for SMoE that demonstrably saves 60–80% memory with limited performance trade-offs. The experiments are extensive (8 benchmarks, 2 model families), the ablations are thorough, and the results are convincing. The weaknesses are minor — a narrative over-claim about causality, an unexplored hyperparameter ($k$), and a few presentation issues — none of which threaten the core empirical findings. The paper makes a useful contribution to efficient SMoE inference.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
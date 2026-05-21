Now I have enough context. Let me synthesize the final review by cross-referencing every point against the paper.

---

## Summary

MoEP proposes a decoder-only Transformer architecture that combines top-k routing across parallel Transformer blocks with MoE-style shrink/grow projection layers, aiming to add sparsity while keeping total parameter count fixed. The authors evaluate on the BabyLM strict-small track (28M parameters, ~10M words) and claim that MoEP outperforms the GPT-2 baseline and other BabyLM baselines, with faster early learning dynamics.

## Strengths

- **Controlled comparison with GPT-2 baseline**: The paper retrains a GPT-2 baseline under identical conditions (same tokenizer, training data, hyperparameters, seed), enabling a fair architectural comparison. Table 1 shows MoEP (49.00 macro avg excluding AoA) modestly outperforms the re-trained GPT-2 (48.10) and the HuggingFace GPT-2 baseline (46.60).

- **Interesting finding on expert design at small scale**: The linear-expert MoEP variant (28M params) outperforms the SwiGLU variant (38M params) on macro average (49.00 vs 47.70 excluding AoA), suggesting that simpler expert designs can be more effective under tight parameter budgets — a useful practical observation.

- **Genuinely novel architectural combination**: The integration of layer-level parallel-block routing with dedicated MoE shrink/grow projections operating at different hidden dimensions is a non-trivial design that has not been explored in exactly this form. Prior layer-level MoE work (e.g., MoLE) operates in fine-tuning with frozen weights; MoEP trains from scratch with fully parameterized parallel blocks.

## Weaknesses

### Major

- **Insufficient statistical evidence for the central claims**: The entire evaluation uses a single seed (seed=42, Table 3) with no standard deviations, confidence intervals, or multi-seed analysis. The macro-average improvement of MoEP over GPT-2 is small (49.00 vs 46.60 excluding AoA, +2.4 points). Without any measure of variance, it is impossible to determine whether this difference reflects a genuine architectural benefit or noise in the evaluation protocol. For a paper proposing a new LLM architecture, this level of evidence is insufficient to establish the claimed advantage.

- **Conditional outperformance claim is misleading in the introduction**: The introduction states MoEP "was able to outperform all BabyLM strict-small baseline models, including the GPT-2 and GPT-BERT models as well." Table 1 shows this is true *only* when the AoA task is included in the macro average. Without AoA, GPT-BERT causal (54.10), GPT-BERT focus-causal (53.65), and GPT-BERT mixed-causal (52.40) all substantially outperform MoEP (49.00). MoEP's AoA score (53.7) is an extreme outlier compared to the baselines' AoA scores (-3.9 to 14.5), so this single task drives the entire "best overall" conclusion. Section 5.1 is honest about the conditionality, but the abstract and introduction are not.

- **Missing critical ablations that would isolate the contribution**: The architecture bundles multiple design choices — parallel blocks at reduced dimension, top-2 routing within parallel layers, MoE shrink/grow projections with top-2 gating, and load-balancing loss. With only three model variants evaluated (GPT-2, MoEP, MoEP-SwiGLU), it is impossible to know whether gains come from the routing mechanism, the parallel structure, the dimensionality reduction, or some interaction. Reasonable ablations not present include: (a) a dense model matched to MoEP's *active* per-token compute, (b) a variant where parallel blocks are simply averaged (removing routing sparsity), and (c) varying the number of parallel blocks or top-k.

- **No efficiency measurements despite "efficiency" in the title**: The paper's title prominently features "Efficient Sparsity," and the abstract frames sparsity as a solution to computational overhead. Yet the paper reports no training throughput, inference latency, memory footprint, or FLOP counts — not even a coarse comparison on the A100 used. This omission leaves the core efficiency claim completely unsubstantiated.

### Minor

- **No language modeling perplexity reported**: Perplexity is the most direct measure of the training objective and is less susceptible to idiosyncrasies of the BabyLM task suite. Including perplexity would help clarify whether MoEP genuinely learns better language representations or merely fits the evaluation tasks differently.

- **Training dynamics analysis is qualitative only**: The claim that MoEP "extracted useful patterns earlier" (Section 5.1) and reaches peak performance sooner (Appendix A.3) is based on visual inspection of learning curves with no quantitative metrics (e.g., area under the curve, time-to-threshold, statistical comparison). This weakens an otherwise interesting observation about sample efficiency.

- **The demonstration is limited to a single small-scale setting**: The paper acknowledges in Section 6 that scaling behavior is unknown. While this is honest, evaluating only at 28M parameters on 10M words means the paper cannot speak to whether sparsity benefits persist at scales where sparsity is practically relevant — a significant gap for a paper positioned as contributing to LLM architecture design.

### Trivial

- **MoEP-SwiGLU has 38M parameters, not 28M**: Table 2 clearly discloses this, so it is not hidden. However, the abstract's framing of "keeping the total parameter count fixed" applies only to the linear MoEP variant. This is a minor clarification issue.

## Nice-to-Haves

- Reporting multi-seed results with confidence intervals to establish statistical reliability of the observed improvements.
- Adding a dense baseline matched to MoEP's active compute budget to test whether sparsity itself provides benefit over clever resource allocation.
- Measuring and reporting training throughput and inference latency on the A100 to ground the efficiency claims.
- Reporting language modeling perplexity alongside downstream task scores.

## Removed Points

These points were flagged for removal, treat them with caution:

- **Criticism that the paper lacks comparison with models at larger scale**: The paper explicitly scopes itself to the BabyLM strict-small track and honestly acknowledges in Section 6 that scaling behavior is unknown. Demanding scaling experiments is scope creep for a paper that deliberately operates within the BabyLM framework.

- **Criticism questioning whether cited models/tools exist (e.g., "not yet released," "cannot be independently verified")**: All cited models (PaPaformer, MoLE, GPT-BERT, BabyLM) exist as referenced. The reviewer's concern about Llama 4's peer-review status is moot — the paper itself acknowledges this in a footnote and cites official announcements and prior Llama papers.

- **Concern about the aggregation definitions being unclear**: Table 1's footnote explicitly defines BLiMP, WUG, and Readings aggregations. The reviewer's claim that these are "not defined until a footnote" is technically true but the footnote is on the same page as the table. This is not a substantive weakness.

- **Criticism that PaPaformer comparison is unsupported**: The paper states in Section 1: "we also show that improving routing mechanism increased performance within parallel architecture even though MoEP did not employ the PaPaformer style of modularity." While not a controlled comparison, this is a stated observation about routing improving parallel architectures generally, not a direct comparative claim requiring a head-to-head experiment.

- **Formatting/style nitpicks about table headings**: The table format issues (missing AoA values for GPT-2 and MoEP-SwiGLU) are noted in the paper itself ("Note that our GPT-2 and MoEP-SwiGLU results do not include AoA scores"). This is disclosure, not a flaw.

- **Generic strength about "addressing an important problem"**: Removed as superficial and not grounded in specific evidence from the paper.

## Novel Insights

None beyond the paper's own contributions. The reviews converge on a consistent picture: the architectural idea is interesting and underexplored, but the experimental evidence is too thin to support the claims at the level needed for acceptance. The key insight — that a small-scale BabyLM evaluation cannot anchor architectural claims meant for LLM design — is a meta-observation about evaluation standards rather than a novel technical insight.

## Suggestions

- The simplest path to substantially strengthening this paper would be to run 3-5 seeds and report means with standard deviations. This alone would address the most serious weakness (inability to distinguish signal from noise in the 2.4-point gain).
- Add one key ablation: a "MoEP-no-routing" variant where parallel blocks are averaged rather than routed, keeping all other design choices fixed. This would cleanly isolate whether the routing mechanism specifically contributes to the gains.
- Report perplexity alongside task scores — it is cheap to compute from existing checkpoints and would substantially strengthen the evidence for genuine representational improvement.
- Tone down the introduction's claim about outperforming GPT-BERT models; state explicitly that this holds only when AoA is included and that GPT-BERT variants are stronger on the non-AoA macro average.

## Score and Decision

**Anchor comparison:**

| Paper | Score | Round | Comparison |
|-------|-------|-------|------------|
| NanoMoE | 3.00 | R1 | Weaker — toy problems only, missing full evaluation pipeline |
| Sparse Training | 3.50 | R1 | Weaker — narrower contribution, less controlled comparison |
| LokiLM | 3.60 | R2 | Weaker — technical report format, less architectural novelty |
| Power Scheduler | 4.25 | R2 | Comparable — interesting idea, thorough experiments but flawed evidence; MoEP has better controlled comparison but similar overclaim issues |
| Effects of Scale | 4.60 | R2 | Comparable — interesting question, inconclusive results; MoEP has clearer methodology but similar evidence insufficiency |
| Few Heads are Enough (EPA) | 5.67 | R2 | Stronger — better novelty, clearer ablations, though also small scale |
| Self-MoE | 6.00 | R1 | Stronger — more practical, better experimental support |
| Jamba | 6.25 | R2 | Much stronger — large-scale, comprehensive, clear contribution |
| MoLEx | 6.33 | R2 | Stronger — better experimental validation of layer-level MoE |
| No Need to Talk | 7.33 | R1 | Much stronger — extensive expensive experiments, clear contribution |
| OLMoE | 8.67 | R1 | Much stronger — fully open SOTA MoE, large scale |

**Round 1 bracket**: Between 3.5 and 7.5, narrowed to 4.0–6.0 after reading anchors.  
**Round 2 narrowing**: The paper is closest to the Power Scheduler (4.25) and Effects of Scale (4.60) anchors — interesting idea, some positive signals, but insufficient evidence to firmly support the claims. It is clearly weaker than EPA (5.67), which had better ablations and clearer contribution despite similar scale limitations. I place MoEP slightly above Power Scheduler because its evaluation is more comprehensive (full BabyLM suite vs selected tasks) and its architectural contribution is more novel, but below EPA due to the overclaim issue and missing critical ablations.

**Final score: 4.5** — The architectural idea has merit and the BabyLM evaluation is properly controlled, but the single-seed evidence, conditional outperformance claim, missing efficiency measurements, and absent ablations collectively mean the paper does not provide sufficient support for its claims to warrant acceptance.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
Now I have a thorough understanding of both the paper and the reviewer claims. Let me produce the final review.

## Summary

This paper systematically investigates redundancy across three Transformer components — entire Blocks, MLP layers, and Attention layers — using a cosine-similarity-based importance metric. The central finding is that attention layers are surprisingly redundant: removing up to 50% of attention layers in Llama-2-70B yields only a ~2.4 point average performance drop while achieving a 1.48× speedup. The paper also shows this redundancy persists throughout training (on MAP-Neo-7B) and proposes a Joint Layer Drop strategy that outperforms single-type pruning at high sparsity. The contribution is primarily an empirical characterization of where structural redundancy lives in Transformer LLMs, rather than a new pruning algorithm.

## Strengths

- **Systematic cross-model and cross-scale validation.** The finding that attention layers are far more redundant than MLP layers or entire blocks holds across Llama-2 (7B, 13B, 70B), Llama-3 (8B, 70B), and Mistral-7B (Tables 1–4). For example, Llama-3-70B drops 32 of 80 attention layers with zero average performance loss and 1.35× speedup (Table 2). This breadth substantially strengthens the paper's core claim.

- **Attention Drop vs. Block/MLP Drop is a clean comparison that isolates the source of redundancy.** The paper's experimental design — comparing the effect of dropping the same number of modules from each component type — cleanly demonstrates that the redundancy is concentrated in attention layers. Block Drop (analogous to ShortGPT's approach) and MLP Drop both cause severe degradation at moderate drop ratios, while Attention Drop maintains near-baseline performance.

- **Joint Layer Drop shows practical utility at high sparsity.** Combining importance scores from both attention and MLP layers and dropping the lowest-scoring ones (regardless of type) outperforms dropping only one type. For Llama-2-13B, dropping 31 combined layers retains 90% of MMLU performance (Section 7), demonstrating the method's value for aggressive compression.

- **KV-cache memory reduction analysis.** The paper quantifies that Attention Drop reduces KV-cache memory by up to 50% (Table 5), connecting the pruning strategy to a concrete deployment benefit beyond inference speed.

## Weaknesses

### Fatal
None.

### Major

1. **Training-stage claim rests on a single model family.** Section 6.2 uses checkpoints only from MAP-Neo-7B to conclude that attention layer redundancy is "inherent and consistent throughout the training process." One model family (even with multiple checkpoints) is insufficient evidence for a universal architectural claim. The observed pattern — attention importance scores stay low throughout training — could be idiosyncratic to MAP-Neo's training setup, data distribution, or model size. This does not invalidate the paper's core claim about redundancy in trained models, but the conclusion about training-stage consistency needs to be scoped as a case study rather than a general property.

### Minor

2. **Ambiguity in the SDR metric definition.** The paper defines ΔAvg. as "the percentage change in average performance" (Section 4), but the actual computed values use absolute point differences rather than relative percentages. For example, Attn-16 on Llama-2-13B has avg 68.2→66.1 (a 2.1-point drop), and the reported γ of 0.07 is consistent with 2.1/29 (absolute points / speedup percentage), not ~3.1/29 (relative percentage / speedup percentage). This inconsistency between the stated definition and the actual computation should be corrected.

3. **Ambiguous phrasing of performance drops.** The abstract states "a 2.4% performance drop" (73.9→71.5) and the text similarly reports "a 1.3% decline" (68.2→66.9). These are absolute point drops expressed as percentages, which is a common but imprecise convention. The paper should clarify throughout whether it reports absolute point changes or relative percentage changes, especially when these numbers appear in the abstract — the paper's most visible claim.

4. **Calibration dataset for main experiments is underspecified.** Section 3.1 mentions using C4, CodeAlpaca, MathInstruct, and LIMA for a motivation analysis, but it is not stated which dataset(s) produced the importance scores used to generate the main results (Tables 1–4). This is a reproducibility gap.

5. **No validation of the similarity metric against alternative importance measures.** The paper assumes that high cosine similarity between a module's input and output implies redundancy, but does not validate this against alternative measures (e.g., gradient-based sensitivity, contribution to final loss, or random ablation baselines). The metric is inherited from prior work (ShortGPT), but given the paper's central reliance on this metric for its empirical claims, some validation would strengthen confidence that the observed pattern is not an artifact of the measurement.

### Trivial
None.

## Nice-to-Haves

- Per-task breakdowns of performance at various dropping ratios would help practitioners understand which tasks are most affected. The current paper averages over 8 tasks; the reviewer's observation that MMLU drops substantially on Llama-2-13B even at moderate attention removal (55.1→48.2 at Attn-16) while BoolQ stays nearly flat is worth discussing.
- A simple random-layer-drop baseline would further isolate whether the similarity-based ordering provides meaningful benefit over chance.
- If available, training checkpoints from additional model families (e.g., OLMo or Pythia, which also release checkpoints) would substantially strengthen the training-dynamics analysis.

## Removed Points

The following criticisms from the reviewer were removed per policy:

- **"48.4% speedup is inconsistent with 1.48×"** — Removed as factually wrong. A speedup factor of 1.48× means speed increases by 48% (not time saved by 32.4%, which the reviewer incorrectly computed). 48.4% ≈ 1.484×, consistent with the reported 1.48× within rounding. The reviewer confused speedup with time reduction.
- **"Missing comparison to existing pruning methods (ShortGPT, LLM-Pruner, SliceGPT)"** — Removed per policy. Block Drop, which the paper explicitly compares against, is ShortGPT's method. The paper shows Attention Drop consistently outperforms Block Drop. LLM-Pruner and SliceGPT operate at a different granularity (weight-level pruning, not layer removal) and are not directly comparable. The reviewer's framing of this as a novelty failure misreads what is already in the paper.
- **"Formatting/style issues with Figure 1"** — Removed as pure formatting nitpicks.

## Novel Insights

The most valuable observation emerging from the reviews — beyond the paper's own contributions — is the asymmetry between attention and MLP redundancy. The paper shows attention layers can be removed almost indiscriminately while MLP layers cannot. This asymmetry is striking because attention is often regarded as the defining innovation of the Transformer architecture. The fact that a model can lose half its attention layers and still function near-baseline suggests that the Transformer's representational power may reside more in its MLP computations and residual stream structure than in its attention mechanism per se. The Joint Layer Drop result further hints that attention and MLP layers serve partially compensatory roles — removing redundant attention layers first, then redundant MLP layers, yields better results than either alone, suggesting the two module types provide distinct and partially independent contributions to model capacity.

## Suggestions

1. Correct the SDR definition to match the actual computation (absolute point change, not percentage change) and use consistent terminology for performance drops throughout.
2. Add a brief discussion or table specifying the calibration data and parameters used to compute importance scores for the main experiments.
3. Scope the training-dynamics conclusion (Section 6.2) as a case study on MAP-Neo-7B rather than claiming it as an inherent architectural property, or add validation from additional model families.
4. Add a brief validation of the similarity metric against a complementary importance measure (e.g., measuring actual performance change from ablating each layer individually) to demonstrate the metric's ordering is meaningful.
5. Include a brief discussion of which tasks are most affected by attention removal and why.

## Score and Decision

The paper makes a genuine empirical contribution: it systematically characterizes where redundancy lives in Transformer LLMs, showing that attention layers are substantially more dispensable than MLP layers across multiple model families and scales. The experiments are otherwise well-conducted, the results are clean, and the practical implications (simpler architecture design, KV-cache savings, inference speedup) are clearly demonstrated. The weaknesses are all addressable and none threaten the core empirical finding. I recommend acceptance with minor revisions.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
Now I have a thorough understanding of the paper and can verify all reviewer claims against the actual paper text. Let me construct the consolidated review.

## Summary

This paper investigates structured redundancy in decoder-only Transformers by measuring module-level importance via input-output cosine similarity. The central finding is that attention layers are disproportionately redundant compared to MLP layers and entire blocks — a pattern that holds across Llama-2 (7B–70B), Llama-3 (8B, 70B), and Mistral-7B. The authors propose Attention Drop (removing low-importance attention layers) and Joint Layer Drop (jointly pruning attention + MLP layers), demonstrating that removing 40–50% of attention layers yields <3% performance degradation while achieving 35–48% speedups. Training-dynamics analysis on MAP-Neo-7B further suggests that attention redundancy is consistent across training stages.

## Strengths

- **Comprehensive cross-model validation of attention-layer redundancy.** The paper tests five model variants across three families (Llama-2, Llama-3, Mistral) and four scales (7B–70B). In every case, attention layers can be pruned far more aggressively than MLP layers or entire blocks with minimal performance loss. For example, Llama-3-70B retains 75.2 average (vs. 75.1 baseline) after dropping 32 of 80 attention layers (Table for Llama-3). This breadth convincingly establishes the core empirical finding.

- **Joint Layer Drop is a clean and well-motivated extension.** By ranking attention and MLP importance scores in a single merged list, Joint Layer Drop naturally drops the most redundant layers of either type. Figure 6 shows it consistently outperforms single-type dropping at high sparsity — e.g., Llama-2-13B retains ~90% of MMLU performance after dropping 31 combined layers. This provides a practical algorithmic contribution beyond the analysis.

- **Training-dynamics analysis adds architectural insight.** Tracking MAP-Neo-7B checkpoints across pretraining (Figure 5) reveals that attention layers maintain low importance scores throughout training, while MLP and block importance increases. This goes beyond a static pruning study and offers evidence that attention redundancy is a structural property, not a post-training artifact.

- **SDR metric enables principled comparison.** The Speedup Degradation Ratio (γ = ΔAvg/ΔSpeedup) cleanly quantifies the efficiency trade-off and makes cross-method comparison systematic. The consistently tiny γ values for Attention Drop (often ≤0.05) versus double-digit γ for MLP/Block Drop provide an intuitive, at-a-glance validation of the paper's central claim.

## Weaknesses

### Fatal

None.

### Major

- **Missing random-drop baseline for attention layers — the similarity-based selector is not validated against a trivial alternative.** The paper's method uses a similarity-based metric to select which attention layers to prune, yet all experiments compare only *across* module types (Attention vs. MLP vs. Block), not *within* the attention stack. Figure 3 plots importance-based dropping curves against "random guessing" on the benchmarks (a task floor), not against random dropping of attention layers. Without a random-drop curve for attention layers specifically, the reader cannot distinguish whether (a) the similarity metric identifies genuinely more/less redundant layers, or (b) attention layers are so uniformly redundant that any selection strategy (including random) would work. This is a methodological gap that directly bears on the paper's claim about "identifying" redundancy using the metric. A simple additional curve in Figure 3 (left panel for attention) would resolve this. The core finding (attention layers are redundant) would survive either outcome, but the contribution of the *selector* specifically would be properly scoped.

### Minor

- **SDR (γ) calculation is underspecified, making some table values irreproducible.** The definition states γ = ΔAvg / ΔSpeedup, where ΔAvg is "the percentage change in average performance." For Attn-4 on Llama-2-13B (baseline 68.2 → Attn-4 68.5, speedup 1.05×), a reading of ΔAvg as a *negative* change (performance gain) would give γ ≈ −0.09, yet the table reports −0.05. For Attn-8 (68.2 → 68.1, −0.15% relative change, speedup 1.13×), γ should be ≈ −0.01 but the table reports +0.01. These mismatches suggest either a different arithmetic convention or rounding effects that are not explained. Since the paper's comparative story (γ_Attn ≪ γ_MLP) is robust to these details, this does not threaten the conclusions, but the metric's definition should be stated precisely (e.g., whether ΔAvg is absolute percentage points or relative percent, and whether the sign convention treats performance *gains* as negative degradation).

- **Training-dynamics analysis is limited to one model family (MAP-Neo-7B).** The paper claims attention redundancy is "an inherent property" (line 478) based on checkpoints from a single model. While MAP-Neo-7B is the only model with publicly released continuous checkpoints, the generalization of this claim would be strengthened by at least one corroborating model. The paper should either acknowledge this limitation more explicitly or soften the claim from "inherent property" to "consistent across the training stages of the models we examined."

- **Joint Layer Drop results lack a tabular breakdown at specific sparsity levels.** Figure 6 shows performance curves, but the text's quantitative claim ("dropping 31 layers... retains 90% of the performance on the MMLU task") references a figure panel that averages over tasks. A supplementary table with exact averages at key sparsity points (e.g., 15, 20, 25, 31 layers) would make these results more precise and citable.

- **Calibration dataset used for the main pruning experiments is not explicitly stated.** The paper mentions using "multiple calibration datasets" (C4, CodeAlpaca-20k, MathInstruct, LIMA) but does not specify which one(s) were used to compute importance scores for the experiments in Tables 1–2 and the Llama-3 table. If pruning decisions are sensitive to this choice, the missing detail affects reproducibility.

### Trivial

- The abstract's "2.4% performance drop" (73.9 → 71.5) is 2.4 *absolute points*, not a relative percentage. This is a common ambiguity in ML papers but could confuse casual readers.

## Nice-to-Haves

- **A brief discussion of *why* attention layers might be so redundant**, e.g., whether the residual stream encodes rich contextual information that makes many attention computations unnecessary, or whether deeper layers learn redundant attention patterns. The paper currently reports the phenomenon without offering a hypothesis.
- **Evaluation on a task that stresses long-range dependencies** (e.g., Multi-Needle-in-a-Haystack or a retrieval-based benchmark), since pruning half the attention layers could degrade long-range mixing even if standard benchmarks show no loss. This would help bound the claim.

## Removed Points

- *"Speed measurement methodology is not reported in enough detail"* — The paper (Section 5, Speed Measurement paragraph) explicitly states that both prefill and generation are included, specifies the sequence length (2048+2048), hardware (single A6000), and quantization details. The criticism is factually incorrect.
- *"Similarity-based metric is assumed without validation"* — The paper clearly states this as a hypothesis (line 74) and the pruning results across all experiments serve as empirical validation. The reviewer acknowledged this as "acceptable."
- *"The 2.4% performance drop phrasing is imprecise"* — Moved to Trivial as it's a minor, common notational ambiguity.
- *"Evaluation on long-range dependency tasks is missing"* — This is scope creep; the paper evaluates on 8 standard benchmarks including reasoning (ARC-C, OBQA), commonsense (HellaSwag, PIQA, WinoGrande), and knowledge (MMLU, BoolQ, RTE). Demanding additional task types beyond this already standard suite would require the paper to be broader than intended. Moved to Nice-to-Haves.

## Novel Insights

The reviews surface one insight beyond the paper's own contributions: the random-drop-baseline question creates a useful conceptual distinction between two claims that the paper conflates. Claim A ("attention layers are redundant") is well-supported by the existing data. Claim B ("our similarity metric identifies the *most* redundant attention layers") is plausible but unvalidated against random selection. The paper would be stronger by explicitly separating these claims and acknowledging which one is fully proven by the existing experiments.

## Suggestions

1. **Add a random-drop baseline for attention layers** in Figure 3 (or a supplementary figure). Plot importance-based dropping and random dropping on the same axes. This directly addresses the major weakness and either validates the selector or honestly scopes the contribution.
2. **Clarify the SDR arithmetic**: specify whether ΔAvg is computed as absolute percentage-point change, relative (%) change, or something else. Include a worked example (e.g., the Llama-2-13B Attn-4 case) so readers can verify the γ values.
3. **State which calibration dataset** was used for the main experiments, or clarify that the reported results are averaged over multiple calibration choices.
4. **Add a small table** to the Joint Layer Drop results with exact average scores at ~5 key sparsity levels (e.g., 15, 20, 25, 31 layers dropped) for both models.
5. **Acknowledge the single-model limitation** of the training-dynamics analysis more explicitly and soften the claim of "inherent property" to reflect the available evidence.

## Score and Decision

This paper makes a clear, well-supported empirical finding — attention layers in decoder-only LLMs are substantially more redundant than MLP layers — and validates it across five model scales and three families. The proposed Attention Drop and Joint Layer Drop are practical methods that follow directly from the analysis. The major weakness (missing random-drop baseline) is a methodological gap that affects the interpretation of the *selector's* contribution but does not invalidate the core finding. The minor issues (SDR clarity, training-dynamics scope, tabular precision) are all addressable. I consider the paper above the acceptance threshold with moderate revisions.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
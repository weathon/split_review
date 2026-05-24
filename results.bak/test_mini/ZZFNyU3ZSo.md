Now I have all the information needed. Let me compose the final consolidated review.

---

## Summary

This paper studies token redundancy in unified multimodal transformers (models handling both generation and understanding tasks) and proposes UniMoD, a task-aware token pruning method. Through systematic empirical analysis (attention weight patterns, ARank-based redundancy measurement, and competitive pruning experiments), the authors show that token redundancy differs significantly across tasks and layers. UniMoD addresses this by using separate task-specific routers with capacities determined by ARank values, and a layer-switch module that selects which transformer layers to convert into MoD blocks. Applied to Show-o (1.4B) and Emu3 (8.5B), UniMoD reduces training FLOPs by ~15% and ~40% respectively while maintaining or modestly improving performance on several benchmarks.

## Strengths

1. **Systematic empirical analysis that genuinely motivates the design.** Section 3 provides a principled investigation of unified transformers from three angles: attention weight patterns (Observation 1, Fig. 2), layer importance and token redundancy via ARank (Observations 2-4, Fig. 3, Table 1), and task interactions (Observation 5, Fig. 4, Table 2). These observations are clearly stated and supported by evidence, and they directly inform the design choices in UniMoD — task-specific routers, ARank-guided layer selection, and separate per-task capacities. This analysis goes well beyond the typical motivation section and is a useful contribution in its own right.

2. **Meaningful FLOPs reductions with maintained performance on Show-o.** On Show-o (Table 3), UniMoD reduces training FLOPs from 51.1 to 43.3 (~15%) while matching or improving 6 out of 8 benchmarks (e.g., MME +37.7, DSG +1.4, GenEval -0.01). Unlike the trivial baselines (Interleaved Layer, EarlyExit) which collapse generation quality (GenEval drops from 0.62 to 0.29/0.26), UniMoD preserves it. The ablation study (Table 5) further confirms that all components contribute, with task-aware routers outperforming a single router for both tasks.

3. **Clean ablation isolating each component's contribution.** Table 5 systematically ablates three design choices: Basic MoD (direct application), removing the layer-switch module, and removing the task-aware router. Each variant underperforms UniMoD across understanding and generation metrics, with Basic MoD catastrophically failing on generation (GenEval 0.15). The controlled pruning rate across ablations strengthens the causal claims.

## Weaknesses

### Fatal

None.

### Major

1. **Emu3 evaluation is not properly anchored to the original model, undermining the 40% FLOPs reduction claim.** The paper states: "Emu3 does not release MMU training resources, we use the LLaVA-v1.5-mix-665K dataset" and "Our full Emu3 results differ from the original paper because we use alternative training datasets, as the official code and data are not publicly available." This means both the "Emu3" baseline row and the "UniMoD" row in Table 3 are reproductions fine-tuned on different data — not the original Emu3 model. It is unclear whether the baseline represents the original model's capability or a weakened reproduction. Without anchoring to the published Emu3 performance (or a clearly characterized reproduction that demonstrably matches it), the claim of "40% FLOPs reduction while maintaining performance" is an internal comparison whose external validity is uncertain. The paper does acknowledge this limitation, but it remains a significant evidential gap for one of the two headline results.

2. **The main comparison baselines are too weak to establish advantage.** Table 3 compares UniMoD only against "Interleaved Layer" (skip every other layer unconditionally) and "EarlyExit" (exit at layer 12). Both are trivial and predictably collapse performance, especially on generation tasks. The most natural baseline — a uniform MoD (as in MoMa, Lin et al. 2024b) — is not in the main table; it appears only in the ablation (Table 5, "Basic MoD") at 40.8 TFLOPs. While the ablation shows Basic MoD fails at the same pruning rate, having only trivial baselines in the headline results makes the comparison look more favorable than it would against a stronger, better-tuned uniform MoD. Including Basic MoD (or a comparable single-router variant) in the main results table would provide a more informative benchmark.

### Minor

3. **No variance or statistical significance reported.** Every metric in every table is a single point estimate. Several reported changes are small: GQA 56.3→54.5 (Show-o), POPE 76.0→74.7 (Emu3), VQAv2 68.3→66.2 (Show-o). Without standard deviations or error bars, it is impossible to tell whether these are genuine degradation or run-to-run noise. Three random seeds per setting would suffice to establish which performance shifts are meaningful.

4. **Router architecture and training objective are not described.** The paper states that each router "assigns scores to tokens and retains the Top-K tokens" (line 249) and gives the routing equation (Eq. 4), but does not specify the router's architecture (linear layer? small MLP?), how routers are initialized, whether they are trained jointly with the model, or whether an auxiliary load-balancing loss is used. The competitive pruning experiment (Section 3.4) mentions an auxiliary loss, but the main method does not. While the original MoD paper (Raposo et al., 2024) describes a generic router, the task-specific nature of the routers here may require additional design choices that should be documented.

### Trivial

5. **Minor inconsistency in layer selection description.** Section 4.1 states "we select the half of layers with the lowest [ARank] values for each task," but Section 5.1 says for Show-o "we transform the last 12 layers into MoD layers for both tasks." Show-o has 24 layers (half = 12), but "lowest ARank values" and "last" may not coincide. The paper should clarify whether these procedures yield the same set or why the discrepancy exists.

6. **Anomalous GQA=0.0 in Table 1.** Skipping layer 3 during inference gives GQA 0.0, while neighboring layers (1: 35.0, 5: 48.0) produce plausible scores. This sharp discontinuity is not explained and may indicate a peculiarity in how the experiment was conducted (e.g., a crash or a modality-specific effect). A brief explanation would be helpful.

## Nice-to-Haves

- Adding a Basic MoD baseline to the main results table (Table 3) with the prune ratio tuned to match UniMoD's FLOPs budget would strengthen the comparison.
- Reporting a small number of runs (e.g., 3 seeds) for the main table metrics would help readers assess significance.

## Removed Points

The following points from the reviewers are removed as they do not meet the filtering criteria:

- **"Competitive token pruning experiment is somewhat artificial"** — This is a methodological preference, not a specific identified flaw. The experiment is presented as an analysis tool (Observation 5), not as a final method.
- **"Basic MoD could be tuned to produce better results"** — Speculative. The paper controls for pruning rate in the ablation. The critic provides no evidence that tuning would change the outcome.
- **"MoMa comparison should be more explicit"** — The paper already discusses MoMa (line 125: "its application of MoD involves only a simplistic combination, without a design tailored for unified transformers"). The contrast is made.
- **"Missing related works"** — No external confirmation is available.
- **"Appendix sections missing"** — The parser strips appendices; they exist in the original submission.
- **"Formatting/style nitpicks"** and **"Typo/grammar issues"** — These are parser artifacts, not author errors.
- **"Should compare against the best achievable uniform MoD"** — As noted, speculative. No evidence that Basic MoD at alternative prune ratios would match UniMoD.
- **Missing hyperparameters/implementation details** — The paper provides adequate implementation details for a conference submission (batch size, datasets, GPU count, pruning ratios, capacity scaling).

## Novel Insights

None beyond the paper's own contributions. The two reviews essentially agree on the paper's strengths and weaknesses; no new perspective emerged from synthesizing them.

## Suggestions

1. **Anchor the Emu3 baseline to the published model.** If the official Emu3 model weights are now available, evaluate UniMoD as a fine-tuning method on the original model. If not, characterize the reproduction baseline more carefully (e.g., show its performance relative to published Emu3 numbers on shared benchmarks) and frame the experiment as an ablation of the pruning method under controlled conditions rather than as a comparison to Emu3.
2. **Move Basic MoD (or an optimized uniform MoD) into the main results table.** This directly tests whether task-aware routers outperform a single router at the same FLOPs budget.
3. **Add error bars or confidence intervals** for at least the main table metrics.
4. **Clarify the router design** (architecture, initialization, training objective, any auxiliary losses) and the relationship between the ARank-based layer selection and the "last 12 layers" procedure.
5. **Explain the GQA=0.0 anomaly** in Table 1.

## Score and Decision

**Calibration summary:**

| Anchor Paper | Avg Score | Round | Comparison to This Paper |
|---|---|---|---|
| "All You Need Are Random Visual Tokens?" | 4.00 | R1 (weak band) | Weaker — primarily observational, limited method contribution |
| "Unbiased Token Pruning" (UTP) | 4.50 | R1 (middle band) | Comparable — both have concrete methods with evaluation gaps |
| "MMTok" | 5.00 | R1 (middle band) | Comparable — MMTok has cleaner evaluation but less novel problem framing |
| "Adaptive Routing of Experts via Fuzzy Rule" | 5.00 | R2 (narrow) | Similar — both address routing in multimodal settings with some gaps |
| "Nüwa" | 5.50 | R2 (narrow) | Stronger — more comprehensive evaluation and baselines |
| "PruneSID" | 5.50 | R2 (narrow) | Stronger — training-free with thorough empirical validation |

**Round 1 bracket:** The paper falls between the weak band (<3.5) and the strong band (>7.5). Topic-similar papers sit at 4.0–5.5.

**Round 2 narrowing:** Comparing within the 4.0–5.5 range, UniMoD has stronger analysis than UTP (4.5) but weaker evaluation than Nüwa (5.5) or PruneSID (5.5). The Emu3 baseline ambiguity and weak main baselines prevent it from reaching the 5.5 level, while the well-motivated design and controlled ablation place it above the observational papers at 4.0.

**Final score:** 5.0. The paper's core idea is sound and the analysis is genuinely informative. However, the two major weaknesses (Emu3 baseline ambiguity and weak main baselines) limit confidence in the headline claims. The paper's real contribution — showing that task-aware routing matters for unified transformers — is still supported, but the current experimental framing overstates the evidence.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
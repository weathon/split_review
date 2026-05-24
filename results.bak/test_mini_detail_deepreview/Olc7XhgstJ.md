## Summary

This paper proposes Steady Thought (ST), a three-stage framework that segments LLM reasoning into discrete "thoughts," generates oracle completions of each thought without switching (via logit suppression of trigger words like "wait"/"alternatively"), and then applies a thought-level preference optimization (STPO) that rewards commitment to promising thoughts and penalizes wasteful switching. Experiments on three models (1.5B–14B) across four math/code benchmarks show consistent accuracy gains (up to 5.3%) and token reductions (up to 39.3%), with evidence that the model abandons promising reasoning paths less frequently after training.

## Strengths

1. **Novel formalization of under-thinking as a thought-level preference optimization problem.** Section 2.1 explicitly models reasoning trajectories and defines commit vs. switch trajectories at the point of divergence (Equations 1–2). This framing is principled and directly motivates the STPO objective, which operates on the *conditional* probability of a continuation given a specific thought prefix rather than on whole responses.

2. **Consistent gains across multiple models, scales, and datasets.** Table 1 shows accuracy improvements on every model–dataset combination (3 models × 4 datasets = 12 settings), with the largest gains on challenging OOD code tasks (e.g., +5.3% on LiveCode for Qwen3-8B). Token reductions are substantial and monotonic (17–39%). The results include a held-out domain (LiveCode) trained only on math data, supporting generalization.

3. **Direct behavioral evidence for the claimed mechanism.** Table 2 shows that ST reduces the percentage of correct intermediate thoughts (PCT) — a proxy for invalid switching — from 54.90% → 40.40% (DeepSeek-1.5B, MATH500) and from 14.50% → 7.90% (AIME2024). This directly supports the claim that ST makes the model's thought-switching more purposeful.

4. **Ablation isolating thought-level optimization from generic training.** Table 4 compares STPO against SFT and DPO on the same preference data for DeepSeek-1.5B. STPO achieves the best accuracy–token tradeoff (84.4%, 2809 tokens vs. DPO's 82.6%, 4273 tokens on MATH500), showing that the length-normalized, thought-level design matters beyond mere preference optimization.

## Weaknesses

### Fatal
None.

### Major

- **The main comparison is against inference-time baselines; training-based baselines are only partially provided.** Table 1 compares ST against NoThink, NOWAIT, and SEAL — all test-time interventions that require no training. This makes it impossible to tell whether ST's gains come from the thought-level design or simply from running any preference optimization on self-generated data. Table 4 partially addresses this by comparing SFT, DPO, and STPO on the 1.5B model, but this ablation is limited to one model and two datasets. The main table should include a training-based baseline (e.g., DPO or SimPO trained on the same preference pairs) for each of the three model sizes. Without this, the central claim that the *thought-level construction* is the source of improvement is not fully disentangled from generic preference optimization.

### Minor

- **The oracle completion stage uses logit suppression that creates an unanalyzed distribution mismatch.** In Stage 2, the model generates completions of a segmented thought while trigger words ("wait," "alternatively") are suppressed to near-zero probability. This produces a continuation the model *would not have generated* under its natural policy. This oracle-generated continuation is then treated as the "chosen" response in preference optimization. The paper does not discuss whether this causes the model to learn an unnatural style, or whether the learned preferences transfer to unconstrained decoding at test time. The empirical results suggest it works, but the mechanism is unclear — the model could simply be mimicking the oracle rather than learning a principled commitment strategy.

- **The logit suppression procedure is underspecified.** Section 3.2 states: "sharply decrease the logits for these words, effectively suppressing their selection by driving their prediction probability close to zero." The magnitude of suppression, whether it is clamped to a fixed negative value or gated by entropy, and whether the trigger word list is exhaustive or just representative are not stated. For a method that relies on this as a core data-generation step, these details matter for reproducibility.

- **No confidence intervals or significance tests.** The paper reports averaged results (8 runs for AIME2024, 2 for LiveCode) but provides no variance estimates. Since some accuracy differences are small (1–2%), the reader cannot assess whether these are statistically meaningful. This is standard for many large-scale benchmark evaluations, but given that the paper draws strong conclusions from these margins, some variance reporting would strengthen the evidence.

- **The "steadiness score" formalization in Section 2.1 is introduced but never directly used.** It is equated to the policy's log-probability in the next sentence, making the abstract framing somewhat redundant. The paper could state the preference objective more directly.

### Trivial
- The caption of Table 1 uses a down-arrow (↓) for both accuracy and tokens, but accuracy should be "↑" (higher is better) and tokens "↓" (lower is better). The values are reported correctly; only the arrow direction is wrong.

## Nice-to-Haves
- Adding an OOD dataset beyond LiveCode (e.g., a logical reasoning task like LogiQA) would strengthen the generalization claim.
- Analyzing whether ST-trained models naturally suppress trigger words at test time without explicit logit control (e.g., tracking frequency of "wait"/"alternatively" before vs. after ST) would clarify the mechanism.
- An ablation that removes the logit suppression in Stage 2 and instead uses rejection sampling to find non-switching completions would disentangle the oracle effect from the thought-level preference design.

## Removed Points

- **Entropy threshold tuning missing for other models.** The critic notes that Table 3 shows tuning only for DeepSeek-1.5B and that results for other models are deferred to Appendix D. The appendix is stripped by the parser; this information exists in the original submission. *Removed per rule: parser-stripped appendix content.*

- **Training details absent (learning rate, batch size, epochs, etc.).** The paper defers these to Appendix E. *Removed per rule: parser-stripped appendix content.*

- **"Up to 39.3%" token reduction claim questioned.** The critic initially flagged this but then verified it is correct (Qwen3-8B on MATH500: 4724→2869 = 39.3%). *Removed: the reviewer resolved their own concern and confirmed the claim is accurate.*

- **Baselines are "not contemporary."** The critic suggests missing "compute-optimal scaling" or "adaptive thinking budgets" baselines without citing specific methods. The paper competently compares against the three most directly relevant baselines in this sub-area (NoThink, NOWAIT, SEAL). *Removed: vague and scope-creep.*

- **Strength Finder's generic claims.** Some strength descriptions included generic phrasing ("addressed an important problem") that are present in the strengths list but are backed by specific references to tables/figures; those specific anchors are kept. Generic-sounding phrases that appear within otherwise specific strength descriptions are retained as context.

## Novel Insights

The most interesting insight that emerges from cross-referencing the paper with the reviews is that the entropy-threshold segmentation (Section 3.1) provides a continuous knob between fine-grained and coarse-grained thought tokens, and that the "wrong" threshold (too low or too high) hurts performance via opposite mechanisms — too fine-grained makes it hard to find complete correct thoughts, while too coarse-grained reduces training data volume. This tradeoff is empirically characterized in Table 3. A second insight is that the model's behavior on hard problems (e.g., DeepSeek-1.5B on AIME2024) is qualitatively different: ST *increases* the number of thoughts while still reducing total tokens and improving accuracy, suggesting it learns to explore more efficiently rather than simply truncating reasoning. The review process does not surface additional novel insights beyond what the paper already provides.

## Suggestions

1. **Add DPO/SimPO training baselines to Table 1 for all three model sizes.** This is the single highest-impact change. Use the same preference pairs (same chosen/rejected construction) for both DPO and STPO; if STPO outperforms DPO under identical data, the thought-level framing is validated. If not, the contribution is better described as "effective preference optimization data construction."

2. **Analyze the effect of logit suppression during oracle completion.** Run an experiment where Stage 2 is done with unconstrained decoding and oracle completions are selected by rejection sampling (keeping only completions that do not switch). Compare ST trained with this alternative against the current logit-suppression oracle. If results are similar, the distribution mismatch concern is largely resolved; if worse, the paper should explain why suppression is necessary.

3. **Report standard deviations or bootstrap confidence intervals** for the main results, especially for smaller accuracy deltas (e.g., 1–2% on GSM8K).

4. **Specify the logit suppression mechanism precisely** in the main text: the suppression factor, whether it is constant or adaptive, and the complete trigger word list used.

5. **Fix the arrow direction** in Table 1's header (Acc should be ↑, Tokens ↓).

## Score and Decision

**Calibration Anchors**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| TPO (Tree Preference Optimization) | O0sQ9CPzai.md | 6.33 (Accept) | R1/R2 | Similar fine-grained preference optimization for reasoning. TPO tests on 3 models, as ST does, but includes a more complete set of training baselines. ST has a more novel framing (under-thinking) but weaker baseline comparisons. ST is slightly weaker overall. |
| Step-Controlled DPO | ZRDa2IT1sQ.md | 6.00 (Reject) | R1/R2 | Very similar topic — step-level preference optimization for math. SCDPO's main weakness was incremental contribution and missing baselines. ST has a similar weakness profile but a more original framing (under-thinking vs. step errors). Comparable quality. |
| Rational Metareasoning | jRZ1ZeenZ6.md | 5.00 (Reject) | R1 | Token-efficiency goal, different methodology (VOC rewards + expert iteration). ST is stronger on novelty and experimental coverage. |
| Planning Tokens | UJkgGbLfWA.md | 5.00 (Reject) | R2 | Structural reasoning improvement via learned tokens. ST has stronger empirical results and more principled formulation. |
| General Preference Modeling | xS4XOS4NQ5.md | 5.00 (Reject) | R1 | Preference representation learning, different problem scope. The comparison is less direct but helps anchor the lower end. ST is more focused and empirically cleaner. |

**Round 1 bracket**: 5.0–6.5 (clearly above weak papers scored 2.5–3.0, clearly below strong papers scored 8+).

**Round 2 narrowing**: The paper is most comparable to SCDPO (6.00) and TPO (6.33). Against SCDPO, ST has a more novel framing but similar evaluation gaps. Against TPO, ST has the same model count but lacks training-based baselines across all models. Considering that the missing training baselines in the main table are the most significant unresolved issue, the paper sits slightly below these anchors.

**Final score**: 5.5 — a solid paper with a genuinely interesting approach and consistent results, but the evaluation's main weakness (inability to disentangle thought-level training from generic preference optimization across all models) prevents a higher score. The issues are addressable in a revision.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
Now I have a clear calibration. Let me compare:

**Round 2 comparisons:**
- **SPO (5.80, Reject)**: Limited experiments (one model, one dataset), baseline performance issues, method is combination of known components. ST is clearly stronger — broader empirical validation (3 models, 4 datasets, OOD), clearer motivation.
- **3D-Properties (6.25, Accept)**: Analysis of DPO degradation with theoretical depth but limited novelty in regularization. ST has more novel method contribution and broader empirical scope, but less theoretical depth. Comparable.
- **TPO (6.33, Accept)**: Novel list-ranking formulation for multi-branch reasoning but restricted to Qwen models, missing baselines. ST has broader model coverage and OOD evaluation but weaker comparison structure. Comparable, ST slightly below on experimental design rigor.

**Positioning**: ST is clearly above SPO (5.80), comparable to 3D-Properties (6.25) and TPO (6.33). ST's two Major weaknesses (training-vs-inference comparison asymmetry, unvalidated exploration flexibility claim) are real but not fatal — Table 4 does partially address the training comparison, and the core empirical results with OOD generalization are solid. I score ST at **6.0**.

---

## Summary
This paper proposes Steady Thought (ST), a framework to mitigate "under-thinking" in Large Reasoning Models — the tendency to abandon promising reasoning thoughts through excessive switching. ST operates in three stages: (1) entropy-based thought segmentation, (2) forced thought completion via logit suppression of switching trigger words, and (3) STPO, a SimPO-derived preference optimization that trains the model to prefer completed thoughts over wasteful switching trajectories. Experiments on three models (1.5B, 8B, 14B) across math and code benchmarks show accuracy improvements (up to 5.3%) with token reductions (19–39%).

## Strengths
- **Thought-level preference optimization is a genuine conceptual contribution, validated by ablation**: Rather than globally suppressing thought switching like prior work (NOWAIT, SEAL), ST constructs preference pairs at the point of reasoning divergence. Table 4 shows STPO outperforms both SFT (80.4% → 84.4% on MATH500) and DPO (82.6% → 84.4%) on the 1.5B model, confirming that the thought-level granularity and SimPO-inspired loss contribute beyond standard training approaches.
- **Robust empirical validation across model scales, task types, and OOD generalization**: Table 1 demonstrates consistent accuracy gains (+1.9% for 1.5B, +3.12% for 8B, +2.52% for 14B) with simultaneous token reductions across four datasets. Critically, LiveCode — an OOD code dataset — shows ST (trained exclusively on math) improves Qwen3-8B accuracy by 5.3% while reducing tokens by 19.0%, providing evidence for generalizable reasoning discipline.
- **Dual behavioral analyses provide convergent evidence for the mechanism**: Figure 2 shows the proportion of the final thought increases substantially after ST (e.g., 8.28% → 32.36% on LiveCode for Qwen3-8B), and Table 2 shows the percentage of correct intermediate thoughts drops (e.g., 45.2% → 39.0% on AIME2024 for Qwen3-8B). Together these indicate deeper commitment and fewer wasted switches.
- **Clear problem formalization via the Bradley-Terry preference model** (Section 2.1): Defines Commit and Switch trajectories, introduces a latent Steadiness Score, and expresses the preference relationship in a way that directly motivates the STPO objective.

## Weaknesses

### Fatal
None.

### Major
- **Main comparison (Table 1) conflates training effect with method effect**: ST is a training-based method requiring preference pair generation and fine-tuning. Every baseline in Table 1 — Vanilla, NoThink, NOWAIT, SEAL — is a zero-shot inference-time intervention. No training-matched baseline (e.g., SFT or DPO on the same data) appears in the main results. Table 4 provides SFT and DPO comparisons, but only on a single model (1.5B) and two datasets, segregated from the main comparison. A reader cannot determine from Table 1 how much of ST's improvement comes from the training process itself versus the thought-level conditioning that is the paper's claimed contribution. The SFT/DPO baselines should appear alongside ST in the main results to isolate the contribution of thought-level preference optimization.
- **The "preserves exploration flexibility" claim — which distinguishes ST from suppression-based methods — is never experimentally validated**: The paper repeatedly claims ST preserves the ability to explore alternative thoughts when necessary (Abstract: "without detriment to the model's capability for preliminary exploration"; Introduction: "a more selective mechanism—one that preserves the ability to explore new reasoning thoughts when the current trajectory is unpromising"; Contributions: "without compromising their flexibility to explore alternative reasoning trajectories"). Yet no experiment tests whether ST-trained models retain the ability to productively switch thoughts when a trajectory is genuinely unpromising. The evidence — reduced output length, fewer thoughts, lower proportion of correct intermediate thoughts, maintained/improved accuracy — is equally consistent with the model simply learning to switch less, which suppression methods also achieve. This is the paper's key conceptual differentiator from prior work, and it is asserted without validation.

### Minor
- **NOWAIT exhibits catastrophic failure on Qwen3-8B that the paper does not discuss**: Table 1 shows NOWAIT on Qwen3-8B drops MATH-500 accuracy from 91.4% to 61.0% while tokens explode from 4,724 to 13,274 (2.8×). GSM8K drops from 95.6% to 73.3% with tokens increasing 7×. Since ST's Stage 2 (Thought Completion) uses the same logit suppression technique as NOWAIT (albeit applied to thought completions rather than full problems), this anomaly warrants at least a brief discussion to assure readers that the training data generated via this technique is reliable.
- **The "proportion of correct thoughts" metric in Table 2 has an unresolved alternative interpretation**: The paper interprets lower PCT after ST as evidence of fewer invalid switches (Section 4.4.2). However, a lower proportion of correct intermediate thoughts could also reflect the model generating fewer correct thoughts overall, not just fewer abandoned ones. The absolute number of correct intermediate thoughts is not reported. Reporting absolute counts alongside proportions would strengthen the interpretation.
- **Entropy threshold analysis is conducted only on the 1.5B model** (Section 4.4.3, Table 3): The chosen threshold of 3.0 is claimed optimal for the 1.5B model, but the paper does not verify whether this threshold generalizes to the 8B and 14B models.

### Trivial
None.

## Nice-to-Haves
- An experiment that directly tests whether ST-trained models still switch productively when the first thought is incorrect — e.g., measuring the switch-away rate from incorrect first thoughts on problems the model eventually gets right.
- Training-matched baselines (SFT, DPO on the same data) included in Table 1 for all model sizes, not just the 1.5B ablation in Table 4.
- A brief discussion of the NOWAIT Qwen3-8B anomaly and why the same logit suppression technique is reliable when used in ST's Stage 2 thought completion.

## Removed Points
These points were flagged for removal. Treat them with caution.

- **[HC] Near-total absence of training and implementation details makes the paper unreproducible**: The paper references Appendix D and E for threshold tuning and computational costs. Per review guidelines, missing/stripped appendix content is not a paper flaw. Hyperparameter details (β, γ, learning rate, batch size, etc.) are implementation details that likely exist in the full submission's appendix.
- **[HC] Data contamination between training and evaluation is unaddressed**: The concern that omni-math training data might overlap with MATH-500/AIME/GSM8K is speculative without concrete evidence of overlap. The LiveCode OOD results (5.3% accuracy gain on a code dataset after math-only training) provide evidence against pure memorization. No specific contaminated example is identified.
- **[HC] The Steadiness Score formalization is "mostly decorative"**: This is a value judgment, not a concrete weakness. The formalization provides a clear theoretical framing that directly motivates the STPO objective.
- **[SF] Efficient and pragmatic thought completion via logit suppression**: While a reasonable design choice, this is essentially the same technique as NOWAIT (a baseline), and the paper does not claim novelty here. It is a supporting implementation detail, not a strength.

## Novel Insights
The paper's insight that under-thinking can be reframed as a preference optimization problem at the thought level — teaching models *when* to commit rather than globally suppressing switching — is genuinely novel. The evidence supports that thought-level conditioning (STPO) outperforms both SFT and whole-trajectory DPO (Table 4), suggesting that the granularity of the preference signal matters. However, the failure to validate the "preserves exploration" claim leaves open whether ST is meaningfully different from suppression methods in practice, or merely achieves similar effects through a different mechanism (training rather than inference-time intervention). The OOD LiveCode results (+5.3% accuracy on code after math-only training) are a particularly striking and not-fully-explained finding that merits further investigation.

## Suggestions
- Move the SFT and DPO baselines from Table 4 into Table 1 for all model sizes, or explain why this was feasible only for the 1.5B model. This would allow readers to assess ST's contribution independently of the training effect.
- Add a targeted experiment: on problems where the model's first thought is incorrect, measure whether ST-trained models switch away at rates comparable to the base model. This would directly test the "preserves exploration flexibility" claim.
- Briefly discuss the NOWAIT Qwen3-8B anomaly and explain why the same logit suppression technique is reliable when used in ST's Stage 2 thought completion (applied to thought prefixes rather than full problems).
- Report absolute counts of correct intermediate thoughts alongside the PCT metric in Table 2 to rule out the alternative interpretation.

## Anchor Comparison Summary
| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| Reward Learning From Preference With Ties | 3.00 | R1 | ST clearly stronger: much broader experiments, clearer motivation |
| Planning with MCTS | 3.00 | R1 | ST clearly stronger: more rigorous empirical validation |
| IUPO | 5.50 | R1/R2 | ST moderately stronger: cleaner motivation, broader model coverage, OOD evaluation |
| Soft Preference Optimization (SPO) | 5.80 | R2 | ST moderately stronger: broader empirical coverage (3 models, 4 datasets vs. 1 model, 1 dataset) |
| 3D-Properties | 6.25 | R2 | ST comparable: ST has more novel method and broader empirics; 3D has more theoretical depth |
| TPO | 6.33 | R1/R2 | ST comparable: TPO has more novel formulation; ST has broader model coverage and OOD evaluation |
| Rethinking Reward Modeling | 8.00 | R1 | ST clearly below: 8.0 paper has strong theory + massive empirical scope |
| WizardMath | 8.00 | R1 | ST clearly below: 8.0 paper has more thorough methodology and evaluation |

**Bracket**: Round 1 placed ST between 5.5–6.5. Round 2 narrowed to 5.8–6.33, with ST sitting slightly above SPO (5.80), roughly comparable to 3D-Properties (6.25) and TPO (6.33), but with structural weaknesses (training-vs-inference comparison, unvalidated flexibility claim) that pull it toward the lower end of that comparable range. Final score: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
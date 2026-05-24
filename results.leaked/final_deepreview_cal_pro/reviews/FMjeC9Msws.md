Now I have sufficient calibration data. Let me synthesize everything and write the final review.

**Bracket**: Round 1 placed this paper between ~5.5 and 8.0. Round 2 narrowed to ~6.0-7.5 by comparing against "Does RLHF Scale?" (5.50, clearly weaker) and "Scaling Law with LR Annealing" (6.75, comparable). The paper is stronger than the IL scaling laws paper (6.20, had cherry-picked environments and 4x forecast error) and comparable to the LR annealing paper (6.75). It falls below the precision scaling laws paper (8.00, cleaner theory) and the knowledge capacity paper (7.25, crisp theoretical finding).

Final score: **7.0**.

---

## Summary

This paper presents a large-scale empirical study (400k+ GPU-hours) of scaling laws for RL training of LLMs. The authors fit sigmoidal compute-performance curves that separate asymptotic reward (A) from compute efficiency (B), systematically ablate design choices (off-policy setup, loss type, precision, aggregation, normalization, filtering, curriculum), and combine the best options into **SCALERL**, a recipe that scales predictably. The centerpiece is a 100,000 GPU-hour training run where performance extrapolated from the first 50k hours closely matches the final observed pass rate. Leave-one-out experiments and scaling across model size, context length, and batch size further validate the framework.

## Strengths

- **Predictive scaling framework with large-scale validation**: The sigmoidal fit (Equation 1) on validation pass rate extrapolates accurately: fitting on the first 50k GPU-hours closely predicts performance at 100k GPU-hours for the 8B model (Figure 1a), and fitting on 16k extrapolates to 45k for the 17B×16 MoE. The same holds for LOO experiments (8k→16k, Figure 5) and across design axes (Figure 6).

- **Systematic, scaling-aware ablation methodology**: Rather than comparing final performance at a single compute point, each design choice is evaluated through fitted parameters A (asymptote) and B (efficiency). This yields non-obvious findings: e.g., CISPO/GSPO losses substantially raise A over DAPO (Figure 4b), FP32 logits raise A from 0.52 to 0.61 (Figure 4c), while PipelineRL improves B without changing A (Figure 4a). This decomposition of asymptotic ceiling vs. convergence speed is a genuinely useful analytical lens.

- **Leave-one-out experiments confirm cumulative benefit**: Starting from SCALERL, reverting one component at a time (Figure 5) shows that individual ablations barely change the asymptote but collectively degrade efficiency. The power-law transformation to visualize B differences is a clean demonstration that the recipe's components are non-redundant.

- **Generalization across multiple scaling axes**: The framework extends to larger MoE models (17B×16 Scout), longer generation lengths (14k→32k tokens), larger batch sizes, and multi-task RL (math+code, Appendix A.13). In all cases, extrapolated curves align with extended training, demonstrating the framework's breadth beyond the initial 8B math-only setting.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **The origin of the fixed A=0.685 in LOO re-fitting is unexplained**: In the Figure 5 LOO experiments, individual fitted A values range from 0.590 to 0.610, yet the re-fitting uses a fixed A=0.685. The paper states this comes from averaging asymptotic rewards across runs, but 0.685 exceeds every individually fitted A. This value appears to come from the longer 100k GPU-hour SCALERL run (where performance reaches ~0.68-0.70), but this connection is not stated. The re-fitting analysis is sensible but the missing justification creates confusion and undermines what is otherwise a clean result.

- **Extrapolation validation is limited to modest multiplicative factors**: The main extrapolation demonstrations are 50k→100k (2×) for the 8B model, 16k→45k (~2.8×) for the MoE, and 8k→16k (2×) for LOO experiments. While these validate the framework, they operate at already-substantial compute budgets. The paper's abstract claims the framework enables "extrapolation from smaller-scale runs," but the gap between the smallest fitting budget (8k GPU-hours) and the largest prediction target (100k) is not demonstrated in a single leap. Demonstrating a fit at 4k-8k predicting 100k would substantially strengthen the central claim.

- **Scope is predominantly math reasoning**: Despite the broad title ("Scaling Reinforcement Learning Compute for LLMs"), the primary experiments are on verifiable math tasks (Polaris-53k, with AIME-24 for downstream transfer). The paper acknowledges this limitation and includes preliminary multi-task results (math+code), but the evidence base is narrow relative to the framing. This limits confidence that the observed scaling regularities (e.g., which design choices affect A vs. B) generalize to other domains like general instruction-following or agentic tasks.

- **SCALERL combines existing techniques rather than introducing novel methods**: The recipe integrates PipelineRL, CISPO, FP32 logits, prompt-level averaging, batch-level advantage normalization, zero-variance filtering, and no-positive resampling — all drawn from prior work. This is a legitimate engineering contribution, but the paper's "new SOTA" framing should be tempered: the recipe is a curated combination rather than an algorithmic innovation.

### Trivial

- The comparison to prior recipes (GRPO, DAPO, Magistral, MiniMax) relegates configuration details entirely to Appendix A.17. A summary table of key hyperparameters for each compared recipe in the main text would improve verifiability of Figure 2.

## Nice-to-Haves

- A hardware-independent compute metric (e.g., total FLOPs or tokens processed) would improve reproducibility and cross-hardware comparison, though GPU-hours on a single hardware type is standard and defensible for internal comparisons.
- Reporting variance across multiple evaluation checkpoints or seeds would strengthen confidence in the fine-grained LOO comparisons, though the compute cost of multiple independent seeds at this scale is acknowledged as prohibitive.
- Discussing sensitivity of the sigmoidal fit to the choice of fitting start point and the risk of overfitting to the validation distribution, as noted in Appendix A.7, would benefit from a brief mention in the main text.

## Removed Points

These points from the harsh critic were considered and removed:

- **"No statistical significance or variance across independent training runs"** — REMOVED. At 400k+ GPU-hours total, replicating key experiments with multiple seeds is infeasible. The paper evaluates across multiple checkpoints with 16 generations per prompt, which provides within-run variance. This is standard practice for this scale of work.

- **"GPU-hours is hardware-specific; use FLOPs or tokens instead"** — REMOVED as a weakness, moved to Nice-to-Haves. All experiments use the same Nvidia GB200 GPUs, making internal comparisons valid. GPU-hours is a standard reporting convention in the field.

- **"Comparison to baselines lacks fair hyperparameter tuning"** — REMOVED as a major criticism. The baselines are published, named recipes (GRPO, DAPO, Magistral, Minimax-M1). Reproducing them faithfully and comparing under identical conditions is a reasonable methodology. Demanding that the authors conduct extensive hyperparameter sweeps for competitors' recipes is scope creep and not standard practice for this type of large-scale study. The "SOTA" claim is addressed as a minor weakness above.

- **"The fit's A is sometimes only weakly constrained by data"** — REMOVED. The paper discusses fitting robustness in Appendix A.7 and validates extrapolations against extended training points, which directly tests whether A is well-constrained. The critic's concern is speculative without evidence that fits are actually unstable.

- **"Early-stage decisions at 3.5k-4k GPU-hours might not hold at scale"** — REMOVED. The paper explicitly addresses this by running LOO experiments at 16k GPU-hours and showing the combined recipe scales to 100k GPU-hours. The concern is preemptively answered by the experimental design.

- **"Figure 2 deviations for some baselines not interpreted"** — REMOVED. The paper explicitly notes this: "We validate the predictability by running each method for longer, which align closely with the extrapolated curves for stable recipes like SCALERL and MiniMax." The paper acknowledges that some recipes are less stable/predictable and the data supports this.

- **"Missing discussion of identifiability/coupling between B and C_mid"** and **"Why sigmoidal over other saturating functions"** — REMOVED. The paper notes the sigmoid choice is discussed in Appendix A.4 and parameter interpretation in Appendix A.8. These are reasonable details to defer to appendix.

- **"KL regularization ablation"** — REMOVED. The paper explicitly states this choice follows large-scale training reports and is a reasonable design decision. Criticizing the absence of an ablation on KL regularization is scope creep.

## Novel Insights

Beyond the paper's own contributions, the reviews converge on a meta-observation: the distinction between asymptotic ceiling (A) and compute efficiency (B) is a genuinely useful diagnostic for RL research that the field has been missing. Pre-training scaling laws focus on loss prediction; this work shows that for RL, separating "how good can this recipe get" from "how fast does it get there" provides actionable guidance for recipe design. The finding that many popular interventions (loss aggregation, curriculum, normalization) primarily affect B rather than A — while loss type and precision shift A — gives practitioners a decision tree: to raise the ceiling, change the loss or fix numerical precision; to get there faster, tune the off-policy setup and data curriculum. This decomposition, validated at scale, may influence how future RL-for-LLM research reports and compares results.

## Suggestions

- Clarify the origin of A=0.685 in the LOO re-fitting (Figure 5). If it comes from the 100k GPU-hour SCALERL run's fitted asymptote, state this explicitly and justify why using a higher A from a longer run is appropriate for comparing LOO variants trained to only 16k.
- Demonstrate a single-leap extrapolation from a genuinely small budget (e.g., fit on ≤8k GPU-hours, predict at 50k+) to directly validate the "extrapolation from smaller-scale runs" claim in the abstract.
- Temper the "state-of-the-art" framing — SCALERL is a curated combination of existing techniques, not a new algorithm. The contribution is the scaling methodology and the systematic ablations, not claiming algorithmic superiority over published recipes.
- Move a summary of baseline recipe configurations (currently in Appendix A.17) into the main text or a clearly referenced table to improve the verifiability of Figure 2.

## Score and Decision

**Calibration anchors referenced:**

| Anchor | Avg Score | Round | Comparison |
|---|---|---|---|
| MpA6HMD7Wq | 3.00 | R1 | Unrelated; much weaker |
| BjZP3fTlVg | 3.00 | R1 | Unrelated; much weaker |
| D0XpSucS3l | 4.50 | R1 | Scaling laws for agents; less systematic, single env, no downstream eval. Our paper stronger. |
| FIXk0RP960 | 5.50 | R2 | "Does RLHF Scale?" — smaller scale, less systematic, reads as technical report. Our paper clearly stronger. |
| xI71dsS3o4 | 5.75 | R2 | Survey paper; not directly comparable. |
| LYS3RhIYCq | 6.20 | R1 | IL scaling laws; cherry-picked envs, 4x forecast error. Our paper more systematic, more accurate predictions. |
| o9YC0B6P2m | 6.75 | R2 | LR annealing scaling law; comparable quality, cleaner theory but narrower scope. Our paper comparable or slightly stronger empirically. |
| FxNNiUgtfa | 7.25 | R2 | Knowledge capacity scaling laws; crisp theoretical finding. Our paper slightly weaker on theoretical depth. |
| wg1PCg3CUP | 8.00 | R1 | Precision scaling laws; unified theory, cleaner validation. Our paper weaker on theoretical unity. |

**Bracket**: Round 1 placed the paper between ~5.5 and 8.0. Round 2 narrowed to 6.0-7.5 by comparing against FIXk0RP960 (5.50, clearly below) and o9YC0B6P2m (6.75, most comparable). The paper is stronger than the IL scaling laws anchor (6.20) and comparable to the LR annealing anchor (6.75), but falls short of the crisp theoretical contributions at 7.25-8.00. Final score: **7.0**.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
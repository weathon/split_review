- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 3, 8, 6
Now I have all the information needed to produce a thorough, verified review. Here is my consolidated judgment:

---

## Summary

VisualAgentBench introduces a benchmark spanning five environments across three scenarios (Embodied, GUI, Visual Design) for evaluating LMMs as interactive visual agents. It additionally provides 4,482 training trajectories collected through a hybrid pipeline (Program-based Solvers, LMM Agent Bootstrapping, Human Demonstrations) and demonstrates that behavior cloning on this data substantially improves open LMMs. The paper evaluates 9 proprietary LMM APIs and 8 open models, revealing a 36.2% success rate ceiling (gpt-4o) and providing analyses of visual grounding choices and planning behavior (ReAct thought, error recovery).

## Strengths

- **Diverse multi-environment coverage exceeding prior single-domain benchmarks.** The benchmark includes five datasets across Embodied (OmniGibson, Minecraft), GUI (Mobile, WebArena-Lite), and Visual Design (CSS), which is genuinely broader than prior work focused on single domains. Evidence: Section 1 and the paper's description of its three scenarios with distinct challenges (lines 60–62, 111–121).

- **Hybrid training data pipeline that demonstrably improves open LMM performance.** The 4,482 trajectories allow open models like InternVL-2 to outperform several proprietary APIs (e.g., gemini-1.0-pro) after behavior cloning. Evidence: lines 71–74 ("behavior cloning on the VAB training set markedly enhances the capabilities of open LMMs as visual agents, with most surpassing the performance of proprietary LMMs like gemini-1.0-pro") and line 213 ("InternVL-2... outperforms gemini-1.0-pro on all evaluated environments").

- **Extensive and systematic evaluation of both proprietary and open LMMs.** 9 proprietary LMM APIs and 8 open models are evaluated under standardized prompting/training formats. Evidence: Section 4.1 (lines 174–198) enumerates all baselines, and the main results (lines 199–220) quantify relative performance.

- **Fine-grained ablation studies on visual grounding design.** Controlled experiments with/without object labels in embodied tasks, Set-of-Marks in GUI tasks, and natural language descriptions in CSS tasks identify specific failure modes. Evidence: Section 5.1 (Figures 2–3, Table 2/6) shows performance drops of 10–26% when these visual grounding aids are removed.

- **Planning behavior analysis beyond simple success rates.** The finding that removing thought from ReAct can *improve* performance on some tasks (Table 4/7) and the error-recovery analysis (Figure 4) provide actionable insights that challenge common practice. Evidence: lines 303–312 and Table 7.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Per-environment quantitative detail is sparse in the main paper.** The main text provides an example task and action space for each environment but does not report per-environment task counts (except WebArena-Lite: 165 tasks), average trajectory lengths, or data source composition splits. While the appendix covers this via `\input{3_1_training}` and statistics tables (stripped by the parser), a reader of the main paper cannot assess task diversity or difficulty granularity without consulting supplementary material. This does not invalidate the benchmark but reduces the main text's self-containedness.

- **The "gap" analysis between proprietary and open LMMs conflates multiple uncontrolled variables.** The paper highlights that fine-tuned open models still lag behind top proprietary ones (line 217: "the gap... is much wider than expected"). This comparison simultaneously varies model scale, training data, and evaluation protocol (prompting vs. fine-tuning), making it difficult to attribute the gap to any specific factor. The paper does acknowledge this implicitly but could better contextualize the comparison (e.g., by separating the effect of model scale from the effect of fine-tuning). This is a framing issue, not an error — the descriptive finding that open models trained on VAB still lag behind gpt-4o is valid as a factual statement.

- **No confidence intervals or significance tests for reported success rates.** Results are reported as point estimates without variance. Given the limited task counts (e.g., 165 for WebArena-Lite), some reported differences (e.g., the ±1.5–3.7% ReAct/no-thought differences in Table 7) may not be statistically significant. Standard practice for agent benchmarks is to report bootstrapped confidence intervals or inter-run variance.

- **Per-task difficulty distributions are not shown.** The paper reports only average success rates. Showing the distribution of difficulty (e.g., tasks solved by all vs. no models) would help assess the benchmark's granularity and saturation risk.

### Trivial

- Line 207 states "we present the first systematic evaluation of gpt-4o-mini on agent tasks" — this claim is unsupported by citation and may be difficult to verify; rephrase as "we evaluate gpt-4o-mini."

## Nice-to-Haves

- **Human performance baseline.** A human ceiling would contextualize the 36.2% gpt-4o score and clarify the practical headroom for improvement.
- **Per-source breakdown of training trajectories** (how many from Program-based Solvers vs. LMM Bootstrapping vs. Human Demonstrations) in the main text, even if the full details are in the appendix.
- **Code and data release statement** (standard for benchmark papers; likely part of camera-ready).

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"Training data construction is underspecified in the main paper"* — The training section exists in the original submission via `\input{3_1_training}` (line 160). The parser stripped this content. Per policy, criticisms about missing appendix/supplementary content should be removed. The main text does summarize the three hybrid methods and total trajectory count.

- *"Open LMMs 0% without fine-tuning: no numbers are shown"* — Factually incorrect. Line 211 explicitly states "resulting in 0% success rates." The number is provided.

- *"Reproducibility concerns about model/data release"* — Models, benchmarks, and datasets cited are assumed to exist per policy. Release statements are standard for final versions.

- *"Missing related works"* — Per policy, the reviewer cannot confirm whether a missing citation exists and should not penalize on this basis.

## Novel Insights

The Harsh Critic's analysis of the ReAct/thought removal experiment (Table 7) surfaces an underexplored phenomenon: directly outputting an action without a reasoning chain yields comparable or better performance for strong models like gpt-4o and claude-3.5-sonnet on some agent tasks. This challenges a widespread assumption in the LLM-agent literature that explicit reasoning necessarily helps. Additionally, the visual grounding ablations show that LMMs' strong performance on standard VQA/recognition benchmarks does not transfer to interactive agent settings — object labels (OmniGibson) and Set-of-Marks (GUI) remain essential crutches, indicating that the vision-language interface for agentic tasks is qualitatively different from perception tasks.

## Suggestions

1. **Add a main-text table** with per-environment statistics: number of tasks, average trajectory length, train/test split, and data-source composition (program-based vs. bootstrapped vs. human). This would significantly improve the main paper's self-containedness without requiring appendix access.

2. **Report bootstrapped 95% confidence intervals** for the main results (Table 1) and for the ablation analyses (Tables 6–7). This is especially important for the ReAct/no-thought comparison where differences are small (0.8–3.7%).

3. **Add a per-task difficulty heatmap** or distribution plot showing how many tasks each model solves, to reveal benchmark granularity and potential ceiling/floor effects.

4. **Soften the "gap" framing** to acknowledge that open vs. proprietary comparisons are inherently multi-variate. The descriptive finding is valuable — it just doesn't need a causal wrapper.

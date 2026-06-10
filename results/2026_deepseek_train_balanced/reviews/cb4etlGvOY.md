## Summary

This paper proposes SALA (Self-Adaptive Language Agent), an in-context learning method that uses a single LLM to generate thoughts, actions, and self-corrections from previous failed trials in text-based games. The method builds on ReAct and Reflexion, replacing the two-LLM Reflexion setup with a single LLM that produces its own adaptation text when a task fails. The paper evaluates on 12 ALFWorld tasks using gemma-2-9b-it, reporting 83% success for SALA vs. 67% for a ReAct baseline, with case studies showing two tasks solved via cross-trial self-correction.

## Strengths

- **Verified cross-trial self-correction via concrete case studies**: The paper provides end-to-end traces for tasks 6 and 12 (lines 197–198) where the agent failed in trial 1, generated a concrete adaptation text, and then *successfully* completed the task in trial 2 with different actions. These traces directly demonstrate the core mechanism working.

- **Systematic model selection across 8 open-source LLMs**: Table 1 evaluates 8 different open-source models (gemma-2-9b, gemma-2-9b-it, Mistral-7B-v0.3, Mistral-7B-Instruct-v0.3, Llama-2-7b-hf, Phi-3-medium-128k-instruct, deepseek-llm-7b-base, zephyr-7b-alpha) under identical ReAct conditions on ALFWorld, providing empirical justification for choosing gemma-2-9b-it.

- **Qualitative failure-mode taxonomy**: The paper identifies three specific failure patterns (retrieving objects from wrong locations, selecting semantically related but incorrect items, misordering sub-goals; lines 162), which contextualizes the improvements and remaining limitations transparently.

## Weaknesses

### Fatal

None. The core claim (a single LLM can self-correct across trials) is demonstrated in principle, but the strength of evidence is insufficient for a top venue.

### Major

- **Internal inconsistency in reported results**: Table 2 shows ReAct succeeding on tasks 3, 4, 5, 6, 8, 10, 11, 13, and 14 — **9 out of 12** evaluable tasks (75%), not the 67% (8/12) stated in the text (lines 195–196). The paper reports a baseline that is worse than what its own data table shows, inflating the apparent improvement from 8 percentage points (83% vs. 75%) to 16 points (83% vs. 67%). This is a factual error in the paper's central quantitative claim.

- **Evaluation on 12 of 134 ALFWorld tasks with no statistical rigor**: The paper evaluates on 14 tasks, excludes 2 for "environment bugs" (tasks 7 and 9), leaving 12. The original ALFWorld benchmark contains 134 tasks, and the original ReAct paper evaluated on all of them. With n=12, the difference between methods is at most 2 tasks — one or two random successes or failures would change the result entirely. No confidence intervals, standard deviations, multiple random seeds, or per-task-type breakdowns are reported. This is a single-run, small-sample comparison that cannot support the paper's conclusions.

- **Missing Reflexion baseline despite positioning against it**: The paper's claimed distinction from Reflexion (single LLM vs. two LLMs) is central to its narrative (lines 16, 28, 167–168). Yet Reflexion is never evaluated as a baseline. The paper literally uses Reflexion's exemplars ("concatenating the two Reflexion exemplars after the two ReAct exemplars," line 168), making it unclear whether SALA is a novel method or a reimplementation of Reflexion with a different model configuration. Without a Reflexion comparison using the same base model and task set, the paper cannot support its claimed advantage.

- **Exclusion of tasks 7 and 9 without independent verification**: The paper asserts that both methods succeeded on tasks 7 and 9 but the environment failed to indicate completion (lines 195). This is presented as a statement of fact with no supporting evidence (e.g., partial logs, environment state dumps). If these are treated as failures instead of exclusions, the reported success rates change, and the method's advantage shrinks or disappears.

### Minor

- **Compression step is ambiguously specified**: Algorithm 1 generates the thought $t^{ep}_0$ from $s^{ep}_0$ (line 87), then overwrites $s^{ep}_0$ to $s_0$ (line 89) before generating the action. The thought is conditioned on the full previous trajectory, but the action sees only the compressed initial prompt plus that thought. The algorithm's sequencing is confusing (lines 87–90 appear to apply compression *after* thought generation but *before* action generation in the same iteration), and no ablation tests whether compression helps or hurts performance.

- **Missing decoding details**: Temperature, top-p, random seed, and other generation parameters are not reported, affecting reproducibility.

- **No ablation studies**: The effects of compression, number of exemplars, maximum trials (9), and the self-adaptation mechanism itself are not isolated.

### Trivial

- The abstract contains a stray "git}" at the end (line 4) — a parser artifact, but worth noting for a final submission.

## Nice-to-Haves

- A Reflexion baseline using the same gemma-2-9b-it model on the same task set.
- Evaluation on the full 134-task ALFWorld benchmark, or a principled justification for the 12-task subset.
- Ablation of the compression step to verify it does not harm performance.
- Reporting of multiple runs with variance statistics.

## Removed Points

These points from the inputs were considered but removed after verification against the paper:

- **"The 12-hour evaluation protocol for model selection is fundamentally flawed"** — The model selection experiment (Table 1) is a screening step to choose a base model, not the main evaluation. Different models attempting different numbers of tasks in a fixed time window is standard for compute-budgeted screening, and the main evaluation (Table 2) uses controlled tasks. Removed because the criticism targets a supporting experiment, not the paper's core claims.

- **"SALA is not meaningfully different from Reflexion" / "Reflexion already works with one LLM"** — Whether Reflexion's original implementation requires two LLMs is a claim about the original paper that cannot be verified from the text under review. The paper's characterization may oversimplify Reflexion, but SALA's single-LLM design is a real architectural choice. The valid part of this concern (missing Reflexion baseline) is already captured as a Major weakness.

- **"The core empirical claim has no evidentiary basis"** — Overstates the case. The case studies (tasks 6 and 12) provide concrete evidence of cross-trial adaptation, which is the method's core mechanism. The problem is insufficient breadth of evidence, not absence of any evidence.

- **"Strawman distinction from Reflexion"** — The paper explicitly describes how it differs (single LLM vs. two-LLM setup), and the method includes a compression step absent from Reflexion. The distinction is real, though the missing Reflexion baseline prevents assessment of its significance.

- **Strength: "Measurable success-rate improvement over a controlled ReAct baseline"** — Re-framed as the internal inconsistency (75% vs. 67%) undermines the precision of this claim, but the comparison is fair in design. Moved from Strengths to the Weaknesses section as the inconsistency reveals the reported improvement is partially an artifact of miscomputation.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the same concerns the paper's small-scale evaluation invites: the method is interesting in principle, but the empirical evidence is too weak to determine whether it is genuinely better than ReAct or comparable to Reflexion.

## Suggestions

1. **Correct the internal inconsistency**: Ensure the reported success rate for the ReAct baseline matches Table 2 (9/12 = 75%, not 8/12 = 67%) and update all derived claims accordingly.
2. **Add a Reflexion baseline**: Run Reflexion with gemma-2-9b-it on the same 12 (or preferably, the full 134) tasks so the claimed improvement can be assessed.
3. **Expand the evaluation**: Either evaluate on the full 134-task ALFWorld benchmark or provide a rigorous justification for the chosen subset, and report results across multiple random seeds with variance.
4. **Clarify the compression step**: Rewrite Algorithm 1 so the ordering of thought generation, compression, and action generation is unambiguous, and add an ablation study testing compression's effect.
5. **Report generation hyperparameters**: Include temperature, top-p, and seed settings for reproducibility.

## Score and Decision

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>
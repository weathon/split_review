- Decision: Reject
- Avg Score: 3.50
- Scores: 5, 3, 3, 3
Now I have all the information needed. Let me produce the consolidated final review.

## Summary

This paper proposes CCL (called "Collaborative Multi-dimensional Course Learning" in the abstract and "Coevolving Multidirectional Curriculum Learning" in the body), a co-evolutionary curriculum learning framework for multi-agent sparse-reward problems. CCL maintains a population of intermediate tasks co-evolved with agent policies trained by MAPPO. It introduces a variational individual-perspective crossover operator that decomposes tasks at the per-agent level, a sigmoid-based fitness function for task evaluation, and a soft-selection mechanism that mixes new and historical tasks. Experiments are reported on five tasks across MPE and Hide-and-Seek environments.

## Strengths

- **Variational individual-perspective crossover operator**: CCL decomposes intermediate tasks at the level of individual agents (Section 4.2, Eq. for D_{i,j} on line 214), computing a per-agent direction for task generation. This addresses a real gap in prior curriculum methods that evaluate tasks only at the global level, and is a genuinely novel mechanism for multi-agent sparse-reward settings.

- **Co-evolutionary framework with soft selection**: The algorithm (Algorithm 1, lines 20–22) maintains a history of past tasks and combines new and old tasks via a soft selection rate α, explicitly synchronizing task difficulty with agent capabilities as policies improve. This design choice is principled and the co-evolution framing is appropriate for the problem.

- **Adaptive mutation step size**: The ablation study (Fig. 3, described on line 235) evaluates adaptive vs. fixed vs. no mutation, verifying that adapting the mutation step based on task fitness improves performance. This is a practical refinement over static step-size approaches.

## Weaknesses

### Fatal
None.

### Major

1. **Fitness function is mathematically inverted relative to its stated purpose** — The paper states (line 109): *"Ideally, tasks with success rates close to 0 or 1 are deemed unsuitable for training. As success rates move from the midpoint to the extremes, task quality declines."* However, the proposed fitness function (line 112) f̃ = 1/(1+e^{-2|r-0.5|}) **increases** as |r-0.5| grows: at r=0.5 the value is 0.5, but at r=0 or r=1 it rises to ≈0.73. This means the function assigns its *highest* values to tasks the paper explicitly calls "unsuitable." The ablation comparison uses a linear function f̃ = −k|r-0.5| (which *correctly* peaks at r=0.5) and claims the sigmoid "delivers better performance" — yet the sigmoid is doing the opposite of what the paper's stated goal prescribes. Either the mathematical formulation is wrong, the paper misdescribes its intent, or the function is being used in a non-standard way that is never explained. This directly affects the core selection/crossover mechanism and must be resolved.

2. **Task representation is critically underspecified** — The paper evolves a population of "intermediate tasks" but never defines what a task *is* in terms of its mathematical encoding. Are tasks subgoal coordinates, reward-modifier parameters, partial observations, or environment configuration vectors? The crossover equations use variables θ_{i,j}^A and θ_{i,j}^B (line 214) — notation conventionally reserved for *policy parameters* — without clarifying whether these are task parameters or agent parameters. The initial task domain Ω₀ (line 103) and the distance measure d(s_i, g_i) suggest goals, but the crossover direction operates on θ vectors, creating a representation gap. Without this definition, the evolutionary operators (crossover, mutation, fitness-driven selection) are not reproducible.

### Minor

1. **Two different full names for the same acronym** — The abstract calls CCL "Collaborative Multi-dimensional Course Learning" (line 4), while the introduction and Algorithm 1 call it "Coevolving Multidirectional Curriculum Learning" (lines 16, 117). These are materially different names for the same contribution, suggesting careless editing.

2. **Identical section titles for 4.1 and 4.2** — Both sections 4.1 and 4.2 have the exact same title "THE VARIATIONAL INDIVIDUAL-PERSPECTIVE EVOLUTIONARY OPERATOR" (lines 95, 99). Section 4.1 is a three-sentence high-level intro that should not be a separate subsection; section 4.2 contains the actual methodology. This creates structural confusion.

3. **Baseline adaptation details are vague** — For POET, the paper states (line 228): *"we employ the same coding techniques used in CCL."* This is not a controlled comparison — it alters the baseline method. For VACL, no multi-agent adaptation is described. Without knowing how single-agent curriculum methods were extended to MAS, the reported outperformance is difficult to interpret.

4. **Limited statistical rigor** — Results are reported over only 3 random seeds (line 226) with no confidence intervals or significance tests. For the Hide-and-Seek environment, the paper states (line 233) that *"specific algorithms were excluded from the comparison because some baseline strategies did not converge"* — this non-convergence is itself informative and should be reported as a result rather than silently omitted.

5. **Ablation text for fitness function is internally inconsistent** — Line 236 states: *"as the agent's success rate approaches 0 or 1, the task's suitability to the agent's abilities decreases exponentially."* This claim contradicts the mathematical behavior of the sigmoid function (which assigns *higher* values at the extremes) and is inconsistent even with the paper's own earlier description. The ablation comparison therefore lacks a coherent interpretation.

### Trivial
None.

## Nice-to-Haves

- Clarify whether the fitness function is used as a maximization or minimization criterion in the evolutionary selection process. If it is inverted intentionally, state this explicitly and explain why.
- Provide a concrete example of an "intermediate task" encoding for one of the experimental environments (e.g., MPE propagation task).
- Report the number of training steps, wall-clock time, and hyperparameter settings (population size n_p, sample size n_t, soft selection rate α, number of prototypes k).

## Removed Points

*These points are flagged to be removed; treat them with caution:*

- **"Experimental results are absent (images not extracted)"** — The tables and figures are embedded as images, which were not extracted by the PDF parser. This is a parser artifact, not an author error. The paper text on lines 226–233 *does* contain numeric claims ("CCL achieves over 95% high performance"), so the evidence is partially present. Per instructions, formatting/parser artifacts should not count as weaknesses.
- **"Algorithm 1 line 8 is garbled"** — The extracted text `1+e−2|1rj −0.5|` shows character corruption from the PDF parser. The original submission likely renders this correctly. Per instructions, parser formatting issues are removed.
- **"Sections 4.1 and 4.2 are verbatim duplicates"** — This is factually inaccurate. While they have the same section title and similar introductory language, the *text* differs (compare line 97 vs. line 101). The structural sloppiness is retained as a Minor weakness; the "verbatim duplicate" characterization is removed.
- **Strength Finder claim #3: "Sigmoid-based fitness function is a strength"** — Given the verified inversion issue (Major Weakness #1), treating this inverted function as a strength conflicts with the verified weakness. Per instructions, when a strength and weakness disagree, the weakness wins.
- **Strength Finder claim that CCL "achieves over 95% success while all baselines fail to converge"** — This claim is stated in the paper text (line 232), but is partially undermined by the baseline exclusion issue (Minor Weakness #4) and the fitness inversion (Major Weakness #1). It is retained as contextually relevant but not as an independent strength.
- **Criticism about missing related work** — Per instructions, missing related work should not be mentioned as the reviewer cannot verify completeness.
- **"Reproducibility: undisclosed hyperparameters"** — While hyperparameters are indeed not listed, the paper does provide several (n_p, n_t, α, k) in the Algorithm 1 header. Per instructions, nitpicks about trivial implementation details are removed.
- **Criticism about "only three random seeds" being described as "evidential failure"** — This is retained as a Minor weakness (limited statistical rigor) but downgraded from the critic's fatal framing.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix the fitness function.** Clarify whether the sigmoid is intended to be f̃ = 1 − 1/(1+e^{-2|r-0.5|}) (which would peak at r=0.5) or whether the current form is correct but used as a minimization criterion. Reconcile the math with the verbal description, re-run experiments if needed, and correct the ablation interpretation accordingly.

2. **Define the task representation concretely.** Specify the parameterization of an intermediate task (e.g., subgoal coordinates, reward modifier weights) and distinguish task parameters from policy parameters in the notation. A concrete example from one of the five environments would resolve most of the ambiguity.

3. **Report baseline adaptation details.** For each baseline (POET, GC, GoalGAN, VACL), describe how it was extended from single-agent to multi-agent settings. If a baseline could not converge in HnS, report this as a result.

4. **Resolve the naming inconsistency** and the duplicate section titles for a cleaner presentation.

5. **Add significance tests or confidence intervals** to support the claimed outperformance over baselines.

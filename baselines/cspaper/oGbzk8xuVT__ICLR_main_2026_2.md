---
job_id: 8bf33895-9c56-49fc-808d-5d5b6c6822b2
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: oGbzk8xuVT.pdf
paper: BuilderBench – A Benchmark for Generalist Agents
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope as a benchmark and software contribution for reinforcement learning, embodied agents, open-ended exploration, and robotics-style control.

## Minimum Quality
Pass ✅. The submission contains the core components expected for a benchmark paper, including an abstract, motivation/introduction, related work, environment/task design, protocols, experiments, and conclusion. While I have substantial concerns about evaluation design, mathematical precision, and benchmark validation, these are review-time scientific issues rather than desk-reject-level omissions.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden instructions, suspicious formatting, or content aimed at manipulating automated reviewers within the provided paper text.

# Expected Review Outcome:
## Summary
This paper introduces BuilderBench, a benchmark for studying open-ended exploration and generalization in embodied agents via block-building tasks. The benchmark includes a MuJoCo+JAX simulator, a curated suite of 42 structure-building tasks intended to test physics, geometry, and long-horizon planning, and two protocols: a multitask self-supervised setting and a simpler single-task supervised “training wheels” setting. The paper also reports reference results for several RL and self-supervised exploration methods, with the main conclusion that current methods perform poorly even on relatively simple tasks.

## Strengths
The paper tackles a worthwhile problem. There is a real gap between current benchmarks that emphasize narrow task completion and the broader aspiration of training agents that acquire reusable physical knowledge and construction skills through interaction. A benchmark designed specifically around this gap is timely and relevant.

The task design is often intuitive and well motivated. The case-study tasks in **Section 5.1** are the strongest part of the paper. In particular, **Figures 2, 3, 4, and 5** do a good job of making the intended reasoning challenges concrete rather than merely asserted. The T-block and four-cube packing examples in **Figure 2** illustrate that the benchmark is not just “move objects to target coordinates,” but can require exploiting orientation-dependent support and packing geometry. Likewise, **Figure 3** for the Hexagonal Portal communicates the need for temporary scaffolding and nontrivial sequencing, and **Figure 4** makes the counterweight/scaffold reuse story easy to understand. For a benchmark paper, this kind of visual grounding matters a lot, and here it helps.

The benchmark setup is appealingly simple while still expressive. The combination of a 5D action space, rigid-body physics, and cube-based construction gives a clean starting point for studying motor control, sequencing, and some forms of physical reasoning without requiring a huge engineering stack.

The paper makes a practical contribution by providing both a hardware-accelerated simulator and simple reference implementations. If the code is indeed as easy to use as claimed, this could lower the barrier to entry for research on open-ended RL and manipulation-oriented exploration.

I also appreciate the inclusion of two protocols. **Figure 1** clearly separates the intended self-supervised training regime from the single-task supervised debug mode. This is a sensible design choice for a benchmark paper, because otherwise the benchmark could be so difficult that researchers receive no intermediate signal when prototyping new methods.

Finally, the empirical results, although limited, do support one narrow but important claim: the benchmark is hard for current off-the-shelf methods. **Figure 6** shows that MEGA and SFL only make progress on the simplest settings, and **Figure 7** shows that even when training directly on the test goals, performance collapses quickly as task complexity increases. This is useful as a sanity check that the benchmark is not trivial.

## Weaknesses
I think the benchmark idea is promising, but the current paper falls short of convincingly validating the benchmark as a benchmark for “generalist agents,” and several technical details are either underspecified or mathematically incorrect.

1. **The central claim about evaluating open-ended generalization is not yet convincingly supported by the actual experimental protocol.**  
   The paper repeatedly frames BuilderBench as a benchmark for “generalist agents” and for self-supervised pretraining that supports solving unseen tasks, see **Abstract**, **Section 1**, and **Section 6**. However, the empirical evaluation in the main paper is much narrower. In **Section 7** and **Figure 6**, the self-supervised evaluation is only on “12 of the lowest complexity tasks,” and only for environments with one, two, and three cubes. In **Figure 7**, the supervised evaluation is on 17 tasks, not the full 42-task suite. This matters because benchmark papers live or die by how convincingly they instantiate the evaluation they advocate. Right now, the paper argues for a broad benchmark of open-ended generalization, but the evidence mostly shows that a handful of baseline methods struggle on a restricted subset of tasks. That supports hardness, but not yet the stronger claim that the benchmark meaningfully measures generalist capability.

2. **The train/test notion of “unseen tasks” is not formalized sharply enough, and this weakens the benchmark’s scientific story.**  
   In **Section 6**, the paper says that during self-supervised training the agent “does not receive any task specification,” and that during evaluation it is tested on hand-designed tasks it is unlikely to have seen. But the paper does not define a task distribution, a split construction, or a quantitative notion of overlap between training experience and evaluation tasks. Since the self-supervised algorithms sample goals from previously visited states, and the environments are fixed by cube count, the distinction between “unseen target structures” and “states reachable during training” is conceptually important and should be made rigorous. Without a clearer definition of what counts as out-of-distribution, it is hard to interpret success or failure as evidence of generalization rather than simply of sparse exposure.

3. **The evaluation target appears misaligned with the paper’s own notion of task success, especially regarding stability.**  
   The paper emphasizes throughout **Section 5.1** that the intended solutions must be *physically stable*, not just momentary placements. For example, the examples in **Figures 2–5** hinge on whether structures topple, require scaffolding, or need counterweights. However, the actual reward definition in **Appendix A.2** appears to check only geometric proximity of cube centers to assigned target positions, with success defined by all assigned distances being below 2 cm. There is no explicit stability test, no perturbation-based check, and no temporal persistence criterion. This is a serious mismatch. If the benchmark’s conceptual contribution is that it tests reasoning about stability, the scoring function should reflect that directly. Otherwise, a method may be rewarded for transient, brittle configurations that contradict the paper’s motivating examples.

4. **The reward/assignment formulation is underspecified, and in at least one place mathematically incorrect.**  
   The most concrete issue is in **Appendix A.2**, where the paper states that the assignment of cubes to targets “is a convex optimization problem and can be solved efficiently with GPUs using the hungarian algorithm.” That is not right as written. The linear assignment problem over permutations is a discrete combinatorial optimization problem, not a convex optimization problem in the usual sense. This is not just a wording nitpick, because benchmark papers should be careful about the exact objective used for evaluation.  
   There is an even more important ambiguity: in **Section 4** and **Example 5** on **Page 6**, the paper allows \(k \le n\), meaning the target structure may specify fewer target positions than the number of cubes in the environment. But **Appendix A.2** says “every cube is assigned a specific target position from the target structure,” which is impossible when \(n > k\) unless duplicate targets, dummy targets, or a partial matching objective are introduced. None of this is formally defined. This is not a minor implementation detail, because the “maximum overhang” task in **Figure 5** explicitly relies on having extra cubes that are necessary for construction but not part of the final specified target. The evaluation function for exactly this case needs to be defined cleanly in the main paper.

5. **The task specification may not be expressive enough relative to the claimed reasoning requirements.**  
   In **Section 4**, tasks are specified only by target cube positions in \(\mathbb{R}^{3k}\). Yet many of the paper’s headline examples, especially in **Figure 2**, rely crucially on cube orientation. The T-block and packing examples specifically require rotating cubes by roughly \(45^\circ\). If orientation is not part of the task specification and not part of the stated target, then there are two possibilities, neither fully satisfying. Either the benchmark intentionally defines under-specified goals and expects agents to infer latent orientation constraints from physics, in which case this should be made explicit and analyzed carefully, or the benchmark may admit unintended equivalent solutions or ambiguous success conditions. As written, the paper leans on orientation-sensitive reasoning in the examples, while formally defining tasks only through positions.

6. **The baseline evaluation is too thin for a benchmark paper aiming to become a standard reference point.**  
   Benchmark papers do not need to beat strong baselines, but they do need to establish a credible reference sheet for future work. Here, the baseline section is a bit too shallow. In the self-supervised setting, **Figure 6** reports only a few methods and only on low-complexity tasks. In the supervised setting, **Figure 7** includes more algorithms, but the main paper gives very little detail on architecture parity, hyperparameter tuning fairness, compute budgets, or the reason particular methods were selected over more recent alternatives. Since one of the paper’s explicit goals is to accelerate algorithmic progress, the reference baselines need to be stronger and more transparently controlled than what is currently shown.

7. **The main paper overclaims benchmark breadth relative to what is actually visible in the main results.**  
   The paper emphasizes “over 42 diverse target structures,” but the main text does not provide a complete main-paper summary of the suite beyond the five case studies, nor a structured breakdown of task families, difficulty tiers, or coverage statistics. The complete list is deferred to **Appendix E**, and the appendix tables mostly list task names with brief ability tags. For a benchmark paper, one would ideally want a concise main-paper table summarizing the suite by cube count, skill category, horizon, and whether tasks are known solvable by the authors. Without that, the reader is asked to trust the curation more than inspect it.

8. **The LLM evaluation in Section 7.1 is not very informative and feels underdesigned.**  
   The binary failure table in **Figure 8** is not sufficient to support the discussion around language models. The evaluation uses a single prompting setup and only five tasks from **Section 5.1**, with outcomes summarized as X/failed. There is no protocol for judging partial correctness, no prompt sensitivity analysis, no comparison to humans following the plans, and no attempt to separate physical misunderstanding from planning failure. Since the rest of the paper is about embodied RL, this section is not essential; but if included, it should be much more rigorous or much more modestly framed.

9. **The positioning against prior open-ended embodied benchmarks is somewhat selective.**  
   The related work in **Section 2** discusses Minecraft broadly via **Guss et al. (2019)**, but the paper does not engage with more direct modern open-ended embodied benchmarks built on Minecraft-style settings, especially MineDojo. Given how central the paper’s argument is about open-ended interaction, a fuller comparison to MineDojo-style embodied generalist benchmarks would strengthen the novelty and positioning substantially. Right now, the comparison to prior work is partly persuasive, but not fully convincing.

10. **Presentation is mixed: the motivating narrative is clear, but several scientific details are left too informal.**  
   There are places where the paper reads more like a project pitch than a benchmark specification. The slogan-like framing in the abstract and introduction is fine in moderation, but the benchmark definition itself needs more precision. The exact evaluation function, task formalization for \(k<n\), stability criterion, and train/test split semantics are not where they need to be for a paper whose main contribution is the benchmark itself.

A few smaller but still relevant points:
- **Figure 6** and **Figure 7** support the paper’s claim that the benchmark is difficult, but they also highlight a limitation: the benchmark validation is mostly “methods fail,” rather than “the benchmark cleanly distinguishes different capabilities.” A mature benchmark should ideally show both.
- The table embedded in **Figure 8** is a weak results table for drawing conclusions. By contrast, the appendix’s **Table 1** is useful for qualitative positioning, but it is only qualitative and in the supplement.
- The paper states in **Section 5.2** that a minority of tasks have unknown solutions even to the authors. That is an interesting design choice, but for a benchmark it also raises a concern: if some tasks lack verified solutions, then they are better framed as challenge tasks rather than standard benchmark items unless solvability bounds or expert demonstrations are eventually provided.

## Questions
1. **Please define the evaluation objective precisely for the case \(k < n\).**  
   In **Section 4** and **Figure 5**, some tasks specify fewer target cubes than available cubes. In **Appendix A.2**, however, the reward description sounds like a one-to-one assignment from every cube to a target. What is the exact optimization problem being solved? If dummy targets, duplicated targets, or a subset-matching objective are used, please write it explicitly. A clean formal definition here would materially increase my confidence.

2. **How is physical stability enforced during evaluation?**  
   The examples in **Figures 2–5** make stability the whole point of the benchmark, but the reward in **Appendix A.2** appears geometric. Do you check stability after placement, after a settling period, or under perturbations? If not, can you justify why center-position matching is a faithful proxy?

3. **Can you formalize the train/test generalization story more carefully?**  
   In the self-supervised protocol of **Section 6**, what exactly is the distribution over training experiences, and what makes the evaluation tasks “unseen” in a measurable sense? A clearer split definition, plus perhaps statistics on accidental overlap with evaluation structures, would help a lot.

4. **Why are task orientations excluded from the task specification?**  
   Several flagship examples, especially the ones visualized in **Figure 2**, hinge on rotated cubes. Is the benchmark intentionally requiring the agent to infer orientation from physical feasibility, or is the omission simply for simplicity? I would like a sharper statement of the intended semantics.

5. **Can you provide stronger benchmark characterization beyond “current methods fail”?**  
   For example, a useful addition would be per-task metadata such as horizon estimates, number of irreversible decisions, requirement for scaffolding, or whether the authors verified a solution. This could make the benchmark more diagnostically valuable.

6. **What was the baseline selection rationale, and how much tuning did each method receive?**  
   For a benchmark paper, readers need to know whether poor results come from benchmark difficulty or from relatively untuned reference implementations. Clarifying compute budgets, architecture choices, and tuning parity could change my assessment.

7. **Would you consider separating “standard benchmark tasks” from “challenge tasks with unknown solutions”?**  
   I like the ambition, but mixing verified and unverified tasks in one benchmark suite may complicate interpretation. A rebuttal clarifying how these subsets should be used would be helpful.

8. **Can you add at least one compact quantitative summary table in the main paper?**  
   The main results are currently mostly in **Figures 6 and 7**, and the LLM results table in **Figure 8** is too limited. A table listing tasks, success rates, and perhaps best method by setting would make the paper much easier to assess.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns stood out from the main paper. The work presents a simulation benchmark for RL and embodied reasoning. I do not see direct privacy, discrimination, or human-subject issues in the current scope.

## Soundness Rating
2: fair. The benchmark idea is plausible and some experiments support the claim that the tasks are difficult, but several core technical details of the evaluation are underspecified, and the reward formulation contains at least one concrete mathematical error.

## Presentation Rating
2: fair. The motivating examples and figures are strong, especially **Figures 1–5**, but the benchmark specification itself lacks the precision expected for a benchmark paper, and some key definitions are deferred or ambiguous.

## Contribution Rating
2: fair. The environment and task-suite look potentially useful, and the paper could become a helpful resource, but the current version does not yet validate or specify the benchmark strongly enough to justify a stronger contribution score.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The benchmark idea is interesting and the task visualizations are compelling, but the current paper overreaches relative to the precision of its formalization and the strength of its validation. My main concerns are the mismatch between the claimed notion of stable construction and the apparent geometric-only evaluation, the underspecified reward/matching objective for \(k<n\), and the limited evidence for the broader “generalist agent” framing.

## Reviewer Confidence
4: confident. I am confident in this assessment and carefully checked the benchmark setup, reward description, figures, and the alignment between the paper’s claims and its actual evaluation, although some implementation details remain unclear from the main paper.
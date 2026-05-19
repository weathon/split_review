- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 8, 6
Now I have all the information I need. Let me produce the consolidated final review.

## Summary

This paper presents Video Language Planning (VLP), an algorithm that composes vision-language models (VLMs) and text-to-video models via tree search for long-horizon robot planning. VLMs serve as policy proposers and heuristic evaluators, while the video model serves as a learned dynamics model. A parallel hill-climbing search with beam pruning generates long-horizon video plans, which are then executed via goal-conditioned policies. Experiments span three robot platforms (Language Table, 7DoF mobile manipulator, ALOHA bi-manual) in both simulation and real-world settings.

## Strengths

- **Novel, well-motivated composition of VLMs and video models via tree search.** The paper clearly articulates why VLMs alone cannot reason about dynamics and why video models alone cannot plan over long horizons, then proposes a principled integration where the VLM generates candidate text actions, the video model rolls out visual consequences, and the VLM again scores outcomes. This decomposition is sensible and the forward-search advantage over one-step planning (contrasted with HiP) is clearly described (Section 2).

- **Empirical demonstration on three distinct robot platforms in both simulation and reality.** The paper shows execution on Language Table, a 7DoF mobile manipulator, and the 14DoF bi-manual ALOHA platform. This multi-platform evidence is a genuine strength — many planning papers focus on a single platform.

- **Scaling with inference-time compute.** The paper reports that increasing the branching factors for video samples, language action proposals, and beam count all improve video plan quality (Section 3.1, ablation references). This is a concrete, testable property: plan quality improves with more search.

- **Ablations isolate the contribution of each design choice.** The paper ablates the planning procedure itself (with vs. without the value function), the branching factors, the planning horizon in execution, and the goal-conditioned policy design (dense vs. sparse conditioning on video frames). These ablations support the claim that each component of VLP contributes.

## Weaknesses

### Fatal
None.

### Major

- **HiP, the closest prior work, is discussed but never empirically compared.** The Related Work section (line 172–173) explicitly says "Most similar to our work, HiP... combines language models, video models, and action models for hierarchical planning" and claims VLP improves upon HiP by using forward search instead of one-step planning. However, HiP is absent from all experimental baselines (Section 3 lists PaLM-E, UniPi, LAVA, RT-2). The claimed advantage over the most directly comparable prior method is therefore unsubstantiated. This is a significant gap because the paper's central methodological argument (forward search > one-step planning) is exactly what a HiP comparison would test.

- **The fix for exploitative model dynamics is presented without any analysis.** The paper correctly identifies a real failure mode — the planner can exploit video model artifacts (objects teleporting) to inflate the heuristic score — but addresses it by discarding videos whose heuristic exceeds "a fixed threshold" (Section 2.2). This threshold is not analyzed: no sensitivity sweep, no report of how often plans are discarded, no measurement of false positives (valid high-progress plans being incorrectly discarded), and no comparison to alternative approaches (e.g., penalizing implausible transitions). The Limitations section (Section 5) acknowledges the video model's imperfections but does not evaluate the threshold fix. For a central component of the planning robustness story, this is undermotivated.

### Minor

- **Video plan quality evaluation relies on lightweight visual assessment.** The paper reports that 50 videos per method were "visually assessed" for task completion (Section 3.1). No inter-rater reliability, no confidence intervals, and no automated metric are reported. While this is a secondary evaluation (the main execution results use automated success/failure metrics), the quantitative claims about video plan quality would be stronger with structured evaluation.

- **Generalization experiments are only qualitative.** The paper's generalization section (Section 3.4) shows VLP handling new objects, new lighting, and deployment in a different building, but presents only sample images — no task success rates or comparison baselines under distribution shift. The claim that "VLP generalizes to new objects and configurations" (Introduction) is plausible given Internet-scale pretraining, but the evidence is anecdotal.

- **Compute cost vs. performance trade-off is not reported.** The paper notes that increasing branching factors improves performance "at the cost of inference time" (Section 3.2), but no wall-clock times or compute budgets are given. For a practical robotics system, knowing the real-time trade-off between search depth/breadth and execution success is essential.

- **VLM heuristic training details are underspecified.** The paper describes training the heuristic to predict "number of steps left" from trajectory snippets (Section 2.1), but does not specify the dataset composition, snippet length distribution, or whether the VLM sees only the current image or a history. These details affect reproducibility.

### Trivial
None.

## Nice-to-Haves

- The paper could add HiP as a baseline in both the video synthesis and execution experiments.
- A systematic analysis of the heuristic threshold (sweep, discard rate, impact on execution success) would strengthen the planning robustness claim.
- Quantitative generalization results (success rates with sample sizes under distribution shift) would turn qualitative demonstrations into stronger evidence.
- Reporting wall-clock planning times alongside success rates would help practitioners assess the method's practical deployability.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Harsh Critic's concern about "absence of quantitative tables in the parsed text."** This is a parser artifact; the original submission contained full tables. The criticism about visual assessment of 50 videos is retained because it is verifiable from the paper text itself (line 117), but the broader complaint about missing tables is not a valid weakness of the paper.
- **Harsh Critic's speculation about threshold needing to be "hand-tuned per domain" and "could discard valid high-progress plans."** While the lack of analysis on the threshold is a valid weakness (retained above), the speculative claims about what "must" be true are removed. The core criticism is that the threshold is unanalyzed, not that it is necessarily fragile in a particular way.
- **Strength Finder's claim that "Prevention of heuristic exploitation" is a strength.** The paper merely identifies the problem and proposes an unanalyzed fix; this is better captured in the retained weakness about the lack of analysis.
- **Strength Finder's claim about generalization as a strength in unqualified form.** Generalization is shown qualitatively; the claim is retained only insofar as the paper demonstrates *some* generalization evidence, but the weakness about its qualitative nature takes precedence.
- **Harsh Critic's "Section-by-Section Notes" about missing algorithm listing and algorithm description.** These are parser artifacts; the original paper includes Algorithm 1. The complaint about underspecified training details is partially retained (Minor weakness above) but the broader claim that "missing details affect reproducibility" is reduced to the specific, verifiable gap: dataset composition and snippet length are not given.

## Novel Insights

The reviews do not surface insights beyond the paper's own contributions. The core observation — that VLMs and video models have complementary strengths (semantic reasoning vs. dynamics modeling) and can be combined via tree search — is well articulated by the paper itself. The reviews' main value is in identifying the specific empirical gaps (missing HiP comparison, unanalyzed threshold) rather than contributing new conceptual observations.

## Suggestions

1. **Add HiP as an empirical baseline** in both the video synthesis evaluation and the execution experiments. If re-implementing HiP is impractical, at minimum provide a clear argument (with supporting evidence) for why the comparison is not feasible, and discuss how the claimed advantage over HiP should be interpreted without a direct comparison.
2. **Provide a systematic analysis of the heuristic threshold.** Report a sweep over threshold values, the frequency of plan discarding, and the impact on execution success. Ideally, move toward a more principled approach (e.g., penalizing heuristic scores for implausible transitions, or using an ensemble of heuristics).
3. **Strengthen the generalization evaluation** with quantitative success rates (and sample sizes) for the new-object, new-lighting, and new-building conditions, rather than relying solely on qualitative images.
4. **Report wall-clock planning times** alongside the ablation of branching factors to contextualize the compute-performance trade-off.

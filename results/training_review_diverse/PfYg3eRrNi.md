Now I have all the information I need. Let me construct the final review.

## Summary

The paper introduces Agent Workflow Memory (AWM), a method that induces reusable, abstracted sub-routines ("workflows") from successful agent trajectories and integrates them into agent memory to guide future web navigation tasks. AWM operates in both offline (using annotated training examples) and online (supervision-free streaming) scenarios. On WebArena, AWM improves over the top published autonomous method (BrowserGym) by 51.1% relative success rate; on Mind2Web, it achieves a 24.6% relative improvement in step success rate over MindAct. The method also demonstrates cross-task, cross-website, and cross-domain generalization.

## Strengths

1. **Novel workflow induction with explicit abstraction for reusability**: The LM-based induction method extracts sub-routines (not full trajectories) and replaces example-specific values with placeholders (e.g., `{product-name}`). This design is shown to outperform rule-based induction that preserves concrete contexts: on Mind2Web, LM-based induction yields +2.8 step success rate (from 43.4% to 45.1%) and +2.8 task success rate (from 2.0% to 4.8%) over the rule-based variant (Table tab:mind2web-rule-lm).

2. **Substantial and consistent empirical gains across two major benchmarks**: On WebArena, AWM improves over BrowserGym by 51.1% relative success rate and outperforms SteP (which uses human-expert-written workflows) by 7.9% (Section 4.1). On Mind2Web cross-task, AWM achieves a 24.6% relative improvement in step success rate over MindAct (Section 4.2). These gains are on execution-based (WebArena) and step-wise (Mind2Web) evaluations.

3. **Robust generalization across tasks, websites, and domains**: On Mind2Web cross-website and cross-domain splits, AWM surpasses baselines by 8.9–14.0 absolute points, with larger margins as the train-test distribution gap widens (Section 4.2). On WebArena, AWM consistently outperforms baselines on a cross-template subset (Section 4.1).

4. **Flexible operation in both offline and online scenarios**: AWM works when high-quality annotated examples exist (offline) and also in a fully supervision-free streaming setting (online) where only test queries are available (Section 3.3). This versatility contrasts with methods that require fixed curated examples.

5. **Systematic ablation of design choices**: The paper examines workflow sub-routine abstraction (rule vs. LM induction, Section 6.1), text vs. code representation (Section 6.2), environment state representation (Section 6.3), and workflow use in action space (Section 7). These analyses provide concrete guidance for future workflow design.

## Weaknesses

### Fatal
None.

### Major

1. **The online scenario's evaluator module is a crucial but unexamined component.** The online setup uses an LM-based evaluator (citing Pan et al.) to judge whether a trajectory succeeded before inducing workflows from it (Section 3.3, line 109). The paper provides no analysis of this evaluator's accuracy on either WebArena or Mind2Web, nor any discussion of how label noise from evaluator errors might affect the quality of induced workflows. This is not a minor gap: if the evaluator makes systematic errors (e.g., false positives on partially correct trajectories), the agent could internalize flawed workflows that degrade future performance. The evaluator is adopted from prior work, but its reliability is never validated for the specific tasks and environments used here. The comparison to rule-based induction (Section 6.1) does not address this, since rule-based induction does not use an evaluator. The paper's claim of strong online results rests on an unverified foundation.

### Minor

2. **Workflow quality is asserted but not systematically measured.** The paper describes how workflows are induced via LM prompting and shows that LM-based induction outperforms rule-based induction. However, there is no quantitative evaluation of workflow quality in the main text — e.g., what fraction of induced workflows are actually correct, how often they are used, whether the abstraction process sometimes removes essential context. The paper references a human examination in the appendix (Section 3.3, line 83), but this is not quantified in the main text. Since the entire method depends on the quality of induced workflows, providing at least a small-scale audit (e.g., human annotation of 50–100 workflows) in the main paper would substantially strengthen the contribution.

3. **The claim that the online margin grows as distribution gap widens is not fully substantiated in the available text.** Section 4.2 reports that on Mind2Web cross-task/cross-website splits, AWM scores "8.9–14.0 absolute points higher" with larger margins for wider distribution gaps. The underlying breakdown by specific cross-task/cross-website/cross-domain split or a visual showing this trend is not present in the available text. The main results tables appear to have been in \input files that the parser stripped; if those tables contain the breakdown, this point is moot, but as presented in the available text the trend is asserted without per-split numbers.

4. **Workflow count and memory growth are not reported.** The paper never reports how many workflows are induced per website or in total. Without this, the reader cannot gauge whether the method is adding a handful of highly reusable workflows or hundreds of niche ones. This is important for both the offline and online settings, as it affects context length and the risk of memory bloat.

5. **Statistical significance is not reported.** The absolute improvements are large, but the paper does not report confidence intervals, standard deviations, or number of runs. Especially for Mind2Web (where baseline task success rates are very low, e.g., 2.0%), small numbers of successes could be noisy. This is common practice in LLM agent evaluations but is worth flagging.

### Trivial
None.

## Nice-to-Haves

- Provide a human-annotated sample of trajectories on each benchmark comparing evaluator judgments to ground truth, to validate the online pipeline's reliance on the LM evaluator.
- Add an ablation that retrieves raw (non-abstracted) successful trajectories instead of inducing workflows, to isolate the benefit of abstraction over simple instance-based memory.
- Report how often induced workflows are actually used across test tasks, and whether performance correlates with the presence of a relevant workflow in memory.
- A figure or table showing the breakdown of the 8.9–14.0 point margin by specific cross-task/cross-website/cross-domain split would clarify the generalization trend.

## Removed Points

- **Synapse comparison missing from tables**: The reviewer criticized that Synapse results are not shown in the available tables. The paper explicitly states it compares to both MindAct and Synapse (line 142), and the main result tables are in `\input` files (`sections/results/mind2web`) that were stripped by the parser. These likely exist in the original submission. Removed per the rule that parser-stripped content is assumed to exist.

- **"Supervision-free" claim misleading**: The reviewer argued that "supervision-free" is misleading because the LM evaluator requires supervision. The term "supervision-free" in context refers to the AWM pipeline not requiring human-annotated training examples or human-written workflows. Using a pre-trained LM as an evaluator is not the same kind of supervision. This is a reasonable usage of the term and the criticism is a strawman.

- **Cross-site transfer limitation on WebArena**: The reviewer noted that cross-site transfer is not evaluated on WebArena. The paper explicitly states that it groups examples by website (line 120), making this a design choice, not a weakness.

- **HTML vs. description drop "may not be statistically reliable"**: The 1.7-point drop is modest, but this is a standard ablation with no statistical claims being made. This is a nitpick that does not affect the paper's core claims.

- **Generic/superficial strengths from Strength Finder**: None serious enough to remove.

## Novel Insights

None beyond the paper's own contributions. The reviewers' comments largely converge on the same gap: the online evaluator's reliability is unexamined, and workflow quality lacks systematic measurement. No reviewer identified a flaw the authors had not anticipated or a direction the paper had not already scoped.

## Suggestions

1. **Validate the LM evaluator.** Provide a human-annotated sample of trajectories (50–100 per benchmark) comparing evaluator judgments to ground truth, and report precision/recall. Show that induced workflows from evaluator-labeled successes are comparable in quality to those from ground-truth successes. This is the single most impactful fix.

2. **Report workflow statistics.** Include the number of workflows induced per website/total, their usage frequency across test tasks, and a small-scale human quality audit (e.g., what fraction are judged correct, usable, appropriately abstracted).

3. **Clarify the Synapse comparison.** Make explicit whether Synapse numbers are used as a baseline or whether Synapse is used as a framework for ablation. If Synapse results exist in the stripped tables, reference them clearly in the main text.

4. **Strengthen the generalization trend evidence.** Provide a table or figure showing the per-split breakdown for the 8.9–14.0 point margin claim, ideally with a measure of distribution shift on the x-axis.

5. **Add standard deviations or confidence intervals** where feasible, especially for low-base-rate metrics like task success rate on Mind2Web.

## Score and Decision

**Originality**: Good — inducing reusable, abstracted sub-routines from agent trajectories and using them as in-context memory is a well-motivated and relatively underexplored direction.

**Importance**: High — improving web agent generalization across tasks, websites, and domains is a central challenge in the field.

**Claims**: Partially supported — the core empirical gains are large and compelling, but the online scenario rests on an unvalidated evaluator, and workflow quality is not directly measured.

**Soundness**: Adequate — the experimental setup is generally sound and the ablations are informative, but the lack of evaluator validation and workflow quality metrics weakens the online results.

**Clarity**: Good — the method is clearly described, and the pipeline figures are helpful.

**Value to community**: Potentially high — the workflow induction approach is practical and could be adopted by other web agent systems.

**Overall assessment**: The paper presents a novel and well-motivated method with impressive empirical gains on challenging benchmarks. The central weakness is that the online scenario depends on an unvalidated LM evaluator whose accuracy is never analyzed. This does not invalidate the contribution — the offline results stand on their own, and the online results are plausible — but it prevents full confidence in the online claims. The paper also lacks a systematic quality audit of the induced workflows, which would strengthen the core mechanism's credibility. With additional evaluator analysis and workflow quality metrics, this would be a strong paper.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
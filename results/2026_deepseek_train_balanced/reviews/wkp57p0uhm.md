## Summary

The paper introduces WebCanvas, an online evaluation framework for web agents that replaces static action-accuracy metrics with "key nodes" — essential milestones any valid task solution must traverse. The authors contribute Mind2Web-Live (542 tasks derived from Mind2Web with 2439 key nodes), an open-source agent framework, and a large-scale evaluation of 20+ models on live websites. The core idea of milestone-based evaluation for live web environments addresses a genuine gap between overly strict action-level metrics and outcome-only evaluation that fails for non-reproducible environments.

## Strengths

- **Key node concept bridges a genuine evaluation gap**: The paper correctly identifies that action-prediction accuracy (Mind2Web, SeeAct) penalizes valid alternative solutions, while outcome-only evaluation (WebArena, GAIA) fails in non-reproducible live environments. The key node approach — intermediate milestones that any valid path must traverse — is a practical middle ground. The Rotten Tomatoes example (§2.2) with multiple valid paths all hitting the same three key nodes illustrates the concept clearly.

- **Empirical justification for why intermediate evaluation is necessary**: §4.2 reports that only 46 out of 104 test-set tasks (44%) have a final key node that is a sufficient condition for task completion. This concretely demonstrates that outcome-only evaluation would be inadequate for live web environments and directly supports the need for the proposed approach.

- **Large-scale model comparison with controlled methodology**: The paper evaluates 20+ models (GPT-4, Claude-3 variants, Gemini, DeepSeek-V2, multiple Qwen sizes, Mixtral, Mistral) in the same live environment with consistent methodology (Table 3 / Table 4). Standard deviations from three runs are reported for the main comparison (Table 1), providing a useful resource for the community.

- **Controlled reward experiment separating self-reward from human-labeled reward**: §4.3 and Table 5 isolate the effect of reward quality, comparing self-reward (GPT-3.5, GPT-4, GPT-4V as reward models) against human-labeled reward. The result that self-reward models underperform or match the no-reward baseline while human-labeled reward increases Completion Rate cleanly supports the claim that reward-signal quality is the bottleneck, not the presence of a reward module per se.

## Weaknesses

### Fatal

None.

### Major

- **The reward experiment's main result is incompletely reported, and the paper's conclusion selectively favors one metric over another.** Table 5 shows that GPT-4 with human-labeled reward improves Completion Rate from 46.9% to 52.3% but *decreases* Task Success Rate from 16.9% to 12.3%. The paper states "the performance of web agent improves with the integration of a reward module with human-labeled reward" (line 292) without acknowledging the Task SR decline. The abstract claims "web agents can benefit from human-provided key node annotations" (line 56). This is misleading — the reward helps agents earn partial credit on more key nodes but makes them *worse* at completing entire tasks. This trade-off may reflect a known pathology where step-level reward signals cause agents to overfit to local subgoals at the expense of global task completion. The paper should discuss this candidly rather than selectively reporting the favorable metric. The finding itself is interesting, but the omitted discussion is a significant gap.

- **The headline claim about "discrepancy" between offline and online evaluation is drawn from comparisons that conflate environment change with metric change.** The paper primarily compares offline Step SR (action-prediction accuracy) with online Completion Rate (key-node achievement) — metrics that "differ" as the paper itself acknowledges (line 210-211). The claim that models "do not necessarily maintain their competency in dynamic online environments" (line 54) attributes the difference to environment dynamics, but the two settings differ simultaneously on *environment* and *metric*. Notably, the Task SR metrics — which *are* directly comparable between offline and online — show a weaker pattern: e.g., MindAct's Task SR(0) declines from 10.0% to 7.5%, while GPT-4's stays at 10.0%. The ranking reversal is partially present in comparable metrics but is much less dramatic than the Step SR vs. Completion Rate comparison suggests. The paper should either (a) reframe the comparison using only directly comparable metrics, or (b) explicitly acknowledge that the headline numbers conflate two sources of variation.

### Minor

- **Dataset filtering characterizes 31% of discarded tasks without analyzing potential selection bias.** Of 780 original Mind2Web tasks, 96 (12%) expired and 142 (18%) were discarded due to "ambiguous task definitions and the difficulty in clearly defining key nodes" (line 115). The paper provides no analysis of whether these 142 discarded tasks cluster by domain, interaction type, complexity, or task length. If tasks where key nodes are hard to define are systematically the tasks requiring multi-step reasoning or loosely coupled page states, the benchmark may have inadvertently filtered out the most challenging evaluation scenarios. An analysis comparing discarded vs. retained tasks along dimensions like domain, number of steps, and action types would either confirm representativeness or reveal blind spots.

- **No breakdown of URL-based vs. element-based key nodes.** The paper states a preference for URL-based identification "which enhanced the Benchmark's robustness against layout changes" (line 75), with element-level methods only "for key nodes that cannot be represented by URLs." However, the paper does not report what fraction of the 2439 key nodes use each method, whether element-based key nodes have different reliability, or whether this design choice introduces domain bias (e.g., favoring multi-page tasks over single-page or AJAX-heavy applications). This makes it difficult to assess what capability profile the benchmark actually measures.

- **The Efficiency Score (ES = L/P) has a structural property that the paper does not discuss.** ES measures steps per achieved key node (lower is better). However, because it is normalized by total achieved step score, it is entirely insensitive to *how many* key nodes were achieved. An agent that reaches 1 key node in 2 steps (ES=2.0) appears more efficient than one reaching 5 key nodes in 10 steps (ES=2.0). The paper reports ES alongside Completion Rate without discussing this interaction, which could lead to misleading interpretations when comparing agents with different completion profiles.

### Trivial

- The limitations section (line 353) is brief — three sentence-fragments — for a paper whose core contribution is about evaluation methodology. A more thorough engagement with known failure modes would strengthen the contribution.
- The abstract describes annotation tools as "lightweight" but provides no quantitative evidence (annotation time per task, setup cost, tool size) to support this claim.

## Nice-to-Haves

- A per-domain breakdown of model rankings. The paper states agents handle "entertainment-related tasks more adeptly than those involving shopping or travel" (line 256) but provides no table or figure to support this claim, despite promising to "analyze the performance discrepancies across various websites, domains, and experimental environments" (line 12).
- An error analysis on key node matching — precision/recall of the three evaluation functions (exact match, include match, semantic match) against human judgment, particularly for the LLM-based semantic match which could introduce noise.
- Standard deviations for the full model comparison table (not just the 6-model subset in Table 1), especially given the noisy nature of live web evaluation.

## Removed Points

The following points raised by the harsh critic are removed with justification:

- **Critique about deterministic transition assumption (§2):** The formal model uses a deterministic transition function as a modeling convenience. The paper explicitly acknowledges network instability and dynamic web content in the limitations. This is standard practice, not a flaw.

- **"Generalize" vs. "transfer" framing (§5):** This is a semantic distinction without practical difference. The paper's point — that a model trained on static snapshots doesn't work well when deployed on live websites — is clear regardless of the verb used.

- **Critique about Table 4 (case study) "positioning live-web as always superior":** The table simply positions WebCanvas on a set of criteria; it is not claiming superiority of live-web over sandboxed evaluation across all dimensions. The critic reads an implicit normative claim that isn't there.

- **Critique about "half human engagement" being underspecified:** While the quantification is imprecise, it is a reasonable summary for a conference paper. Cost details can be provided upon request.

- **Critique about Efficiency Score being "structurally unsound":** The critic's example (agent A achieves 5 nodes in 15 steps vs. agent B achieves 3 nodes in 9 steps, both ES=3.0) actually demonstrates the metric working correctly — both agents require 3 steps per key node, so they are equally efficient. The metric measures step economy per key node, which is exactly what it claims to measure. The concern about perverse incentives applies to any efficiency metric and is already mitigated by reporting it alongside Completion Rate and Task SR.

- **Strength Finder's overstatement about "statistical rigor" (20+ models with ±):** Only 6 models in one table have standard deviations; the complete 19-model table lacks them. The strength is retained but calibrated.

## Novel Insights

The most genuinely novel observation that emerges from the review — beyond what the paper itself claims — is the reward paradox: human-labeled key node annotations improve intermediate progression (Completion Rate) but degrade end-to-end task completion (Task SR). This suggests that finer-grained reward signals may cause agents to optimize for local milestones at the expense of the global objective, an effect reminiscent of reward hacking in RL. The paper presents the data for this insight but does not analyze or even acknowledge the trade-off. A dedicated investigation of why this happens (does the reward cause earlier termination? over-exploitation of easy subgoals? accumulation of noisy memory?) would be a valuable contribution to the web agent community.

## Suggestions

1. **Acknowledge and analyze the reward trade-off**: Report the Task SR decrease alongside the Completion Rate increase for human-labeled reward. Provide a per-task breakdown — in how many of the 130 sampled tasks does reward help vs. hurt each metric? Analyze whether the reward causes agents to terminate early or over-invest in intermediate steps.

2. **Reframe the offline-online comparison**: Either (a) use only directly comparable metrics (Task SR(0) and Task SR(1) appear in both settings), or (b) explicitly acknowledge that the headline comparison confounds environment change with metric change and discuss what can and cannot be concluded.

3. **Characterize the filtered tasks**: Analyze the 142 discarded tasks across domain, number of steps, action types, and complexity to establish whether Mind2Web-Live is representative or has systematic blind spots.

4. **Report the URL-based vs. element-based key node breakdown**: Include the fraction of key nodes using each identification method and discuss whether reliability differs between them.

5. **Add a per-domain performance table or figure**: The claim about entertainment vs. shopping/travel performance (line 256) deserves quantitative support.

## Score and Decision

**Score:** 5.5  
**Decision:** Accept

The paper makes a genuine contribution with the key node evaluation concept, the open-source infrastructure, and the large-scale model evaluation. However, the selective reporting on the reward experiment and the overclaiming on the offline-online comparison weaken the narrative. These are fixable with revision, and the core methodological contribution is solid.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>
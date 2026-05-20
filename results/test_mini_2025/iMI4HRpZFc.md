Now I have sufficient calibration. Let me write the consolidated review.

## Summary

This paper formalizes the notion of "delusions" in target-directed RL agents — false beliefs about reachability that arise from improper training data distributions. It introduces a taxonomy of delusions: generator-side (G.1: nonexistent targets, G.2: temporarily unreachable) and estimator-side (E.0/E.1/E.2: misevaluation of different target types). Based on this analysis, it proposes two mitigation strategies materialized as hindsight relabeling approaches ("generate" and "pertask") and a hybrid 2-slotted framework that separates training data for generators and estimators. Experiments on a custom environment (SSM) with the Skipper method show reductions in delusional behaviors and improvements in OOD generalization.

## Strengths

1. **Systematic taxonomy of delusions in target-directed RL.** The paper partitions generator failures into G.1 (nonexistent) and G.2 (temporarily unreachable) targets, and estimator failures into E.0, E.1, and E.2 types (Section 3.1–3.2). This taxonomy goes beyond prior work (Zhao et al., 2024) that gave isolated examples without a structured categorization. The distinction between G.1 and G.2 is clean and practically useful.

2. **Root-cause analysis identifying training-deployment mismatch as the core problem, with targeted mitigation strategies.** Section 4 identifies that agents "only learn from experienced data" but must evaluate unexperienced targets at decision time. The "pertask" strategy (Section 4.1.2) specifically addresses E.2 delusions by exposing the estimator to targets from other episodes in the same task — this is a genuinely novel contribution not present in prior HER work.

3. **The hybrid 2-slotted approach (Section 4.3) is a pragmatic design contribution.** The insight that generators and estimators have conflicting training-data needs (generators should avoid problematic targets; estimators should learn about them) is well-motivated, and the proposed solution of independent relabeling processes for each component is clean and implementable. Table 1 provides a useful summary of trade-offs among relabeling strategies.

4. **Solid experimental methodology.** The paper uses 20 seeds per condition, reports 95% CIs (and acknowledges when 50% CIs are used due to overlap), and evaluates on multiple criteria (estimation errors, behavior frequencies, OOD performance). This is above-average statistical rigor for the field.

## Weaknesses

### Fatal
None.

### Major

1. **Limited empirical evidence for claimed generality.** The main paper presents results from only one environment (SSM, a custom diagnostic environment) with one method (Skipper). Three of four experiment sets are deferred to the appendix due to page limits. While the paper asserts all four sets "align in terms of conclusions" (Section 5.6), the main text does not include summary statistics or a compact table from the other experiments, making it difficult for the reader to assess the breadth of evidence. The SSM environment is specifically designed to manifest G.2 delusions through sword/shield mechanics and lava; the paper would be substantially stronger if it demonstrated the same phenomena on at least one standard, non-custom benchmark in the main paper.

2. **Generalization to structurally different forms of unreachability is not tested.** The paper claims the proposed strategies help the estimator "figure out the features shared by problematic targets, s.t. OOD delusions can also be identified" (Section 4.1.2). However, the OOD evaluation only varies difficulty parameters and initial states within the same structural framework (sword/shield/lava on SSM). The estimator never confronts a structurally different form of unreachability from what it saw during training (e.g., an entirely different environmental mechanism causing G.2). This limits the strength of the "preemptive" claim — the paper shows generalization within seen categories, not to genuinely novel types of delusional targets.

3. **The "generate" strategy is explicitly an adaptation of prior work with insufficiently delineated novelty.** The paper states that Zhao et al. (2024) "identified delusional behaviors resulted from E.1 delusions ... and proposed to train the estimator additionally with candidate targets proposed by the generator" (Section 4.1.1). The paper's "generate" strategy recasts this as a JIT HER relabeling strategy. The paper does clearly cite the prior work, but the novelty boundaries could be sharper: "generate" is an adaptation (with the HER-specific implementation being the incremental contribution), "pertask" is genuinely novel, and the hybrid 2-slotted framework is also novel. The paper's overall framing sometimes implies more novelty for "generate" than is warranted.

### Minor

4. **Mixture proportions are chosen without principled justification or sensitivity analysis.** The hybrid strategies use proportions such as 50% episode / 50% generate, 50% episode / 50% pertask, and 2/3 episode / 1/3 pertask with 1/4 generate (Section 5.4). These appear arbitrary, and no analysis is provided showing that performance is robust across a range of proportions or that these specific ratios are optimal. This weakens the practical applicability of the framework.

5. **Selective inclusion of baselines across subfigures.** The paper states it focuses on F-* variants (future for generator) for "fairer comparison (excluding bad generator performance)" (Section 5.4). This is a reasonable experimental control, but the behavior frequency plots (Figure 3c and 3g) only show hybrid strategies, excluding even F-E, F-P, and F-G. While the OOD performance plot (Figure 3h) does include all variants, the omission from behavior plots makes it harder to directly attribute behavior changes to specific estimator strategies.

6. **The empirical guidelines (Section 7) are reasonable but untested as a recipe.** The paper presents four steps as actionable guidelines, but no experiment validates that following this recipe leads to improved results across different methods or environments beyond what is already demonstrated. As presented, the guidelines mostly restate the paper's own analysis rather than constituting a validated framework.

### Trivial
- Figure 3 is dense; the legend is shared across subplots but individual panels are labeled only in the caption and not directly in the figure images, making cross-referencing cumbersome.
- The behavior frequency plots use 50% CIs due to "chaotic overlap" (Figure 3 caption), but the reason for the chaotic overlap is not explained.

## Nice-to-Haves
- A sensitivity analysis of mixture proportions showing robustness across a range of values would strengthen the practical contribution.
- A table or compact summary of the three appendix experiment sets in the main paper, even if brief, would help readers assess generality without reading the appendix.
- Quantitative runtime/compute cost of "generate" vs. other strategies would help practitioners weigh the trade-off.

## Removed Points

- **"Circular argument" (Harsh Critic, Critical Issue 1):** Removed as factually inaccurate. The training data includes G.1/G.2 targets from *training tasks*, while evaluation measures estimation error on held-out instances from *different tasks* and OOD settings with different difficulty/initial states. This is standard supervised evaluation, not circular. The paper does not claim the estimator learns to reject the *same exact targets* seen in training, but rather that exposure during training enables the estimator to recognize shared features of problematic targets at test time. The valid concern about limited *structural* generalization is retained as Major Weakness #2.

- **"Categories not disjoint" (Section-by-Section Notes):** The critic claimed G.1/G.2 categories are not disjoint. The paper explicitly says G.1 targets "do not correspond to valid states in the task MDP" while G.2 targets "correspond to valid states in the task MDP, but cannot be fulfilled from the current state" — these are definitionally disjoint. Removed as factually incorrect.

- **"Missing hyperparameters and details" (Missing Parts):** The paper is 8 pages with page limits, and the parser strips appendices. This is a known artifact, not a genuine paper weakness. Removed per Hard Rules.

- **"Vague reference to prior methods" (Section 2 Notes):** The critic says the paper is vague about which methods Zhao et al. showed challenges for. The paper is citing Zhao et al. for their findings, not claiming credit. This is standard citation practice. Removed.

- **"Insufficient evidence for broad claims about target-directed decision-making" (framed as fatal by critic):** This is a valid scope concern but not fatal — the paper acknowledges the limitation (3/4 experiments in appendix) and the taxonomy contribution is independent of empirical breadth. Retained as Major Weakness #1 with appropriate severity calibration.

- **Generic/superficial strengths from Strength Finder removed:** "Actionable empirical guidelines" (the guidelines are restatements of the paper's own analysis, not validated independently); "Clear summary table" (useful but supporting, not a core strength).

## Novel Insights

None beyond the paper's own contributions. The harsh critic and strength finder do not surface any observation that the paper itself does not articulate. The reviews independently validate the paper's framing and add no new conceptual lens.

## Suggestions

1. **Broaden the empirical scope in the main paper.** Either move one of the appendix experiment sets (especially the G.1-dominant environment with LEAP) to the main paper, or include a compact table summarizing all four experiment sets with key metrics, so readers can assess generality without consulting the appendix.

2. **Test generalization to structurally different types of unreachability.** Design an experiment where the estimator is trained on G.2 delusions caused by one mechanism (e.g., state-class transitions from sword/shield) and evaluated on G.2 delusions caused by a different mechanism (e.g., one-way doors, irreversible resource consumption). This would directly support the claim that the estimator learns "shared features" of unreachability.

3. **Add a sensitivity analysis for mixture proportions.** Show that hybrid strategy performance is robust across a range of mixture ratios (e.g., 10% increments), or provide a principled method for selecting proportions based on environment characteristics.

4. **Sharpen the novelty delineation.** Explicitly state in the contributions list which strategies are novel vs. adaptations of prior work. The paper currently does this implicitly but would benefit from making it explicit.

## Score and Decision

**Bracketing (Round 1):** Anchored by three queries on hindsight experience replay / goal-conditioned RL delusions. Weak anchors (avg <3.5) scored 1.5–3.0 (OZ3NXrF3gQ: 2.50, N581Nje6fH: 1.50, PDAflvlxYY: 3.00, VCscggkg2t: 3.00). Middle anchors (3.5–7.5) scored 4.25–7.00 (BH8Nrt2dPf: 4.25, 9jMoHuqjfg: 4.50, oXjnwQLcTA: 6.00, 0akLDTFR9x: 7.00). Strong anchors (>7.5) scored 7.75–8.50 (agPpmEgf8C: 8.00, v593OaNePQ: 8.00, EpVe8jAjdx: 8.50, or8mMhmyRV: 7.75). **Round-1 bracket:** 4.0–6.5.

**Narrowing (Round 2):** Two queries targeting 4.0–6.5 range. Compared against BH8Nrt2dPf (4.25, Accept Poster) — this paper had very mixed reviews (6,5,3,3) with the contribution considered obvious by some reviewers; the current paper's taxonomy is clearly non-obvious and better received. Compared against oXjnwQLcTA (6.00, Accept Poster) — this paper had solid theory (convex dual derivation) and comprehensive experiments on standard benchmarks; the current paper is weaker on both theoretical depth and experimental breadth. Compared against 9jMoHuqjfg (4.50, Withdrawn/Reject) — this paper was criticized for limited novelty and questionable comparisons; the current paper's taxonomy and controlled experiments are clearly stronger. Compared against mYp2KwjCWx (4.75, Reject) — criticized for outdated baselines and narrow evaluation; the current paper has better statistical practices and a more coherent contribution.

**Final placement:** The paper sits below the 6.0 solid-accept anchors (oXjnwQLcTA, 0akLDTFR9x) due to limited experimental breadth in the main paper and lack of theoretical analysis, but above the 4.2–4.8 borderline region (BH8Nrt2dPf, 9jMoHuqjfg, mYp2KwjCWx) due to its genuinely novel taxonomy, well-designed experiments, and clean presentation. Score: **5.5**.

### Anchors Table

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| OZ3NXrF3gQ | 2.50 | 1 | Much weaker — withdrawn paper with no clear contribution |
| N581Nje6fH | 1.50 | 1 | Much weaker — basic approach, rightfully rejected |
| PDAflvlxYY | 3.00 | 1 | Weaker — limited experiments, unclear novelty |
| VCscggkg2t | 3.00 | 1 | Weaker — niche problem, limited evaluation |
| BH8Nrt2dPf | 4.25 | 1,2 | Weaker — mixed reviews, contribution considered obvious by some; current paper has clearer novelty |
| 9jMoHuqjfg | 4.50 | 1,2 | Weaker — novelty concerns, unfair comparisons; current paper's taxonomy is more novel |
| mYp2KwjCWx | 4.75 | 2 | Slightly weaker — similar empirical scope but less clear contribution |
| oXjnwQLcTA | 6.00 | 1,2 | Stronger — solid theory, comprehensive benchmarks; current paper lacks both |
| 0akLDTFR9x | 7.00 | 1 | Stronger — solid theory, strong empirical results on standard benchmarks |
| agPpmEgf8C | 8.00 | 1 | Much stronger — oral-level paper with deep analysis |
| v593OaNePQ | 8.00 | 1 | Much stronger — oral-level paper with different subfield |
| EpVe8jAjdx | 8.50 | 1 | Much stronger — spotlight paper with stronger claims and experiments |
| or8mMhmyRV | 7.75 | 1 | Much stronger — oral-level paper, different subfield |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
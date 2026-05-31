## Summary
The paper re-evaluates prominent claims that **programmatic policies** generalize out-of-distribution (OOD) better than **neural policies** on three RL benchmarks (TORCS, Karel, Parking). It argues much of the previously observed gap is attributable to experimental confounds (e.g., observations, reward shaping/search), while also proposing a principled regime where programmatic representations can have an inherent advantage: tasks requiring **working memory that grows with input size**, illustrated via FUNSEARCH synthesis of BFS on a modified Karel variant.

## Strengths
- **Clear multi-benchmark re-evaluation tied to specific experimental factors.** The paper explicitly targets TORCS, Karel, and Parking as “three core benchmarks used in influential papers” (Abstract; also Sec. 1 and the setup around “We consider TORCS… KAREL… and PARKING” at line ~51), rather than arguing from a single anecdote.
- **Parking section candidly exposes metric-dependent conclusions and difficulty.** Sec. 4.3 explicitly notes contradictory readouts depending on metric—“However, looking at the test ‘Success Rate’ alone suggests that DQN is the winner…”—and concludes “Independent of the metric considered, our results show that PARKING is a challenging domain…” (lines ~266–267). This transparency is valuable in a confound-analysis paper.
- **Useful conceptual decomposition of “representation enables OOD generalization” into expressivity vs discoverability.** The abstract states the two-part criterion: a representation enables OOD generalization if (i) the induced policy space contains a generalizing policy and (ii) the search algorithm can find it (Abstract, lines ~9–10). Even before the later sections, this framing helps interpret why empirical comparisons can be misleading.

## Weaknesses

### Fatal
None.

### Major
- **The paper’s headline claim “neural … can match or exceed … on TORCS, Karel, and Parking” is overstated given its own Parking results and narrative.** The abstract claims neural policies “can match or exceed the OOD generalization of programmatic policies” across all three (Abstract, line ~9). But in Parking the paper itself presents a mixed picture: it states PSM “generalize[s] better” by “Successful-on-100,” yet also states “looking at the test ‘Success Rate’ alone suggests that DQN is the winner,” and ultimately concludes the domain is “challenging … for both” (Sec. 4.3, lines ~266–267). This internal inconsistency matters because the paper positions itself as a careful re-evaluation; the cross-benchmark takeaway should be calibrated to what the results actually show for each benchmark.
- **Seed asymmetry undermines the robustness/“Successful-on-100” comparison in Parking, and the paper leans on that metric in its interpretation.** Sec. 4.3 says “we trained 30 independent models of PSM and 15 of DQN” (line ~264), while Table 3 defines “Successful-on-100” as the fraction of trained models that solve all 100 initial states (lines ~246–250). With unequal numbers of trained seeds, “Successful-on-100” becomes a non-comparable tail statistic (more trials increase the chance of observing a rare perfect seed), yet the text uses this to argue “PSM policies generalize better… as two out of 30 models could solve all 100 test initial states” (line ~266). Because this is one of only three benchmarks and the paper’s abstract makes a broad cross-domain claim, this fairness issue meaningfully weakens the evidential basis for the re-evaluation’s headline conclusion.

### Minor
- **The paper does not commit to a primary OOD generalization metric, leading to metric-switching within Parking’s interpretation.** Table 3 reports both “Successful-on-100” and “Success Rate” (lines ~246–250) and Sec. 4.3 alternates between them: first emphasizing “Successful-on-100” in favor of PSM, then emphasizing the train–test gap in “Success Rate,” then noting test “Success Rate” favors DQN (line ~266). Reporting multiple metrics is fine, but for a confound-analysis paper it would be stronger to pre-specify which metric operationalizes “OOD generalization” (or explicitly treat them as different notions, e.g., seed-robustness vs average-case), rather than letting the narrative pivot between them.
- **The “policy spaces … similar to those of neural networks” explanation is asserted more than substantiated in the visible text.** The abstract makes a strong mechanistic claim: “domain-specific languages used induce policy spaces similar to those of neural networks” (Abstract, line ~9). In the extracted main text provided here, this is not accompanied by a concrete supporting argument (e.g., a mapping, complexity comparison, or analysis of learned programs vs network realizability). This does not invalidate the empirical re-evaluation, but it weakens the paper’s causal/explanatory story relative to its strength of framing.

### Trivial
None.

## Nice-to-Haves
- **Tighten the bridge between the two halves (re-evaluation vs memory-scaling advantage) by explicitly scoping the “common neural architectures” limitation and positioning it as a regime statement.** The abstract claims “Commonly used neural architectures cannot encode a solution … due to their fixed-capacity design” (Abstract, line ~9). Later, the paper already partially qualifies this by noting memory-augmented models “can in principle approximate” needed structures but “imperfectly and lack formal correctness…” (lines ~312–313). Making this scoping more explicit earlier (e.g., “fixed-state controllers / constant-memory agents”) would improve coherence and avoid readers interpreting it as an overly general “neural can’t” claim.

## Removed Points
These points are flagged to be removed, treat them with caution.
- **“Parking uses 30 seeds for each policy type.”** Removed because the paper explicitly contradicts this: it states “We trained 30 independent models of PSM and 15 of DQN” (Sec. 4.3, line ~264). (The earlier sentence in Sec. 4.3 saying “For each policy type, we trained 30 independently seeded models” at line ~260 is inconsistent with the later clarified numbers; the concrete numbers at line ~264 and Table 3 are what the paper actually uses.)
- **Speculative concerns about whether FUNSEARCH evidence is “about representation or search.”** While conceptually interesting, the paper itself frames FUNSEARCH as “proof of concept” (line ~304) and explicitly contrasts guarantees (“programmatic representations can provide such guarantees,” lines ~312–313). Without more on-page detail tying this to the earlier confound story, criticisms that hinge on speculation about what FUNSEARCH “really demonstrates” are better treated as nice-to-have framing improvements rather than substantive flaws.

## Novel Insights
The most consequential issue is not that Parking is “mixed,” but that the paper’s own Parking design (unequal seeds) interacts directly with its most rhetorically salient robustness metric (“Successful-on-100”), making the section simultaneously (i) central to the cross-benchmark abstract claim and (ii) the least methodologically aligned with that claim. Because the paper is explicitly arguing that prior work suffered from uncontrolled experimental factors, this internal mismatch is especially salient: the re-evaluation’s credibility benefits disproportionately from pre-committing to an OOD metric and matching seed budgets whenever a tail/robustness statistic is used.

## Suggestions
- Align the abstract/intro claims with the per-benchmark outcomes: e.g., state clearly that results are strong on TORCS/Karel but **mixed on Parking**, unless the Parking protocol is adjusted to support a stronger statement.
- In Parking, either (a) equalize the number of trained seeds across PSM and DQN when reporting “Successful-on-100,” or (b) emphasize metrics that are comparable under unequal seed counts (and explicitly interpret “Successful-on-100” as exploratory unless seed budgets match).
- Define (near the beginning of Sec. 4, or in the intro) one primary OOD metric (and optionally one secondary) and use that consistently across benchmarks; if different benchmarks require different metrics, explicitly justify why.
- If the “policy spaces are similar” explanation is meant to be a key mechanism (as the abstract suggests), add a compact, concrete supporting analysis (even qualitative) grounded in the actual learned policies/programs in these benchmarks.

## Score and Decision
**Originality:** Moderate (re-evaluation + a clear regime claim about memory-scaling tasks).  
**Importance:** High—clarifying confounds in a widely cited “programmatic generalizes better” narrative is valuable.  
**Support for claims:** Mixed; strongest where results are clean, weakest in Parking where the headline claim and fairness/metric issues bite.  
**Experimental soundness:** Generally careful, but Parking’s unequal seeds + reliance on a tail metric is a meaningful methodological flaw for the paper’s stated purpose.  
**Clarity:** Mostly clear; the paper is commendably explicit about metric contradictions in Parking, but the global claim should be tightened.  
**Community value:** High if claims/metrics are made crisper; as written, the overbroad headline reduces reliability.

MY FINAL SCORE: <score>6.0</score>  
MY FINAL DECISION: <decision>Reject</decision>
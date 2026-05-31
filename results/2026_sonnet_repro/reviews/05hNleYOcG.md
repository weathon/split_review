Now let me do the calibration search to properly score this paper.**Round 1 bracket**: The paper sits above the weak jailbreaking papers (1.4–3.0) and likely below the top-tier papers (8.0). Most comparable are the middle-band multi-turn attack papers at 5.33–5.75. PLAGUE has more thorough ablation and better empirical results on harder models, but has notable overclaimed claims. Initial bracket: **5.0 to 7.0**.Let me read the AutoDAN-Turbo anchor (most directly comparable to PLAGUE) and one more anchor.Now I have enough to write the review. Let me synthesize everything.

**Anchor comparison summary:**
- ActorAttack (multi-turn attack, 5.33, Reject): Less rigorous ablation, fewer baselines, limited methodology vs. PLAGUE
- MHJ (multi-turn human jailbreaks, 5.75, Reject): Dataset paper, different type
- AutoDAN-Turbo (lifelong jailbreak, 7.17, Accept): Most directly comparable — single-turn lifelong learning, similar plug-and-play design, very strong empirical results; PLAGUE extends to multi-turn with more complex framework but has more meaningful weaknesses

**Round 1 bracket**: 5.0–7.0
**Round 2 narrowing**: PLAGUE is clearly above 5.33–5.75 (better ablation, more baselines, stronger results on hard targets), but below AutoDAN-Turbo (7.17) due to overclaimed abstract failing for 3/5 models, modest lifelong learning contribution, and baseline modification concerns. Final estimate: **6.0**.

---

## Summary

PLAGUE is a three-phase (Planner → Primer → Finisher) plug-and-play framework for automated multi-turn LLM jailbreaking with a lifelong-learning memory component. The framework dissects multi-turn attacks into planning, context-building, and finisher stages, and augments them with backtracking, reflection, and semantic retrieval of previously successful strategies. PLAGUE achieves state-of-the-art attack success rates on strongly safety-aligned models including OpenAI o3 (SRE 0.814) and Claude Opus 4.1 (SRE 0.673 with Crescendo as Finisher), with a systematic ablation study demonstrating the contribution of each component.

---

## Strengths

- **Substantial empirical gains on genuinely hard targets.** Table 2 shows PLAGUE achieves SRE 0.814 on o3 vs. 0.616 for the next-best baseline (ActorBreaker), a 32% relative gain; and Table 4 shows SRE 0.673 on Claude Opus 4.1 vs. 0.480 for Crescendo (40.2% relative gain). These two models are acknowledged in the safety literature as highly resistant, making the margin practically significant.

- **Rigorous incremental ablation.** Table 3 builds from GOAT (baseline) to PLAGUE step by step: GOAT (0.587 SRE on o3) → +BT (0.612) → +R (0.761) → +P (0.773) → +RSS (0.814). Each component is assigned a measurable, independent contribution. This is more disciplined than most ablations in the jailbreaking literature.

- **Demonstrated plug-and-play modularity.** Table 4 shows that swapping the Finisher from GOAT to Crescendo for Claude Opus 4.1 lifts SRE from 0.465 to 0.673, outperforming stand-alone Crescendo (0.480) and confirming that the Planner+Primer scaffolding generalizes across Finisher modules. Section 5.1 further discusses using ActorBreaker's planner within PLAGUE (Figure 3).

- **Efficiency analysis.** Table 5 shows PLAGUE invokes the target LLM approximately as many times as Crescendo (≈3–4 calls) despite adding a Planner phase (only 1 additional call), demonstrating that the performance gains are not simply a result of a larger query budget.

---

## Weaknesses

### Fatal
None.

### Major

- **The abstract's ">30% improvement across leading models" is not supported for 3 of 5 evaluated models.** From Table 2: o1 SRE is 0.931 vs. best baseline 0.798 (GOAT) — approximately 17% relative gain; DeepSeek-R1 SRE is 0.978 vs. 0.978 (GOAT) — 0% gain; Llama 3.3-70B SRE is 0.958 vs. 0.950 (GOAT) — 0.8% gain. The abstract states "improving attack success rates (ASR) by more than 30% across leading models" without qualification. This claim holds only for o3 and Opus 4.1. The paper partially notes that Deepseek-R1 is near-saturation, but the abstract does not qualify the claim for o1 or Llama. The actual results table (Table 2) is accurate, but the abstract is misleading as written. This needs correction.

- **The Crescendo baseline modification creates an asymmetric comparison.** Section 4 states: "We remove any explicit backtracking counts from their attack and limit their maximum number of turns to six." Crescendo's backtracking is a core adaptive mechanism. PLAGUE retains its own backtracking module (Section 3.4). Removing backtracking from Crescendo while keeping it in PLAGUE produces a structurally uneven comparison. The paper offers no ablation or justification showing that this modification is budget-neutral or that it corresponds to Crescendo's behavior under a fair configuration.

- **Per-model Finisher selection in Table 2 is post-hoc.** The main results table shows PLAGUE with GOAT as Finisher for four models, but with Crescendo as Finisher (Table 4) for Opus 4.1 (marked with *). The best Finisher is selected per model without a pre-specified rule. This means the published headline numbers represent the best configuration found across multiple runs, not a single fixed method. While the paper frames this as demonstrating plug-and-play modularity, Table 2's combined numbers effectively cherry-pick the best Finisher variant per model.

### Minor

- **The lifelong learning component — the framework's marketing centerpiece — makes a modest measured contribution.** In Table 3, "Retrieving Successful Strategy" (RSS) adds +4.1% SRE on o3 (0.773 → 0.814) and +3.4% on Opus 4.1 (0.431 → 0.465). By contrast, Reflection contributes +14.9% on o3 alone (0.612 → 0.761). The paper's title and framing place lifelong learning prominently, but it is the smallest contributor in the ablation. The implementation also introduces a confound: the strategy library is built sequentially during the 200-goal run, so early goals see an almost-empty library while later ones benefit from a richer one. The growth trajectory and per-goal retrieval statistics are not reported.

- **The random-retrieval fallback is unquantified.** Section 3.3.1 states: "If fewer than two strategies are retrieved, a strategy is randomly retrieved from the library." The paper does not report how frequently this fallback occurs. If most retrievals early in the run are random (as the library is sparse), the semantic similarity-based mechanism operates only for a fraction of goals. The paper criticizes AutoDAN-Turbo for retrieval frequency issues, yet does not resolve the analogous question for PLAGUE.

- **The GOAT history-disabled comparison is asserted but not shown.** Section 4 states: "Through extensive ablation, we also observe that the impact on GOAT's performance with and without an attack history is negligible." Disabling attack history alters the core adaptive mechanism of GOAT, which relies on prior response summaries to guide subsequent turns. The claim of negligible impact is supported only by a single sentence; no table or figure is provided. Since GOAT is the baseline PLAGUE most directly improves upon and also serves as the Finisher module, the accuracy of this characterization is central to the comparison.

- **The modified StrongREJECT prompt is not described.** Section 4 states the evaluation uses "a slightly modified version of the original evaluation prompt." Since all baselines are re-evaluated with the same modified prompt, internal consistency is preserved. However, the modification is not described and no validation against the unmodified prompt is offered, making it impossible to compare these numbers with published jailbreaking results that use standard StrongREJECT.

### Trivial

- None.

---

## Nice-to-Haves

- An ablation isolating (a) initialized strategies only vs. (b) newly discovered strategies vs. (c) random fallback in the RSS module would resolve whether lifelong learning provides real benefit beyond Crescendo's two seeded examples. The paper criticizes AutoDAN-Turbo for relying on human-initialized strategies ("only human-generated strategies appended during initialization seem to yield a discernible improvement") but never demonstrates that PLAGUE's freshly discovered strategies are the source of RSS's gain.
- Reporting results with both GOAT and Crescendo as Finisher for at least one additional model (e.g., o3) beyond Opus 4.1 would transform the modularity claim from a single data point into a demonstrated pattern.
- A single run with an alternative attacker model (e.g., GPT-4o or Claude Sonnet instead of DeepSeek-R1, which itself achieves 97.8% as a target) would strengthen generalizability claims.
- Reporting sensitivity to the backtracking thresholds (7/10 for Primer, 3/10 for Finisher, Section 3.4/3.5) would validate that the current settings are reasonable.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"X-Teaming comparison is unfair (fewer TextGrad steps)."** The paper openly acknowledges this in Section 5.1 ("We attribute X-Teaming's low performance … to fewer TextGrad steps") with details in Appendix C.4. Per the hard rules, since the asymmetry favors the baseline over PLAGUE, this is not a valid weakness. Removed.

- **"Non-standard evaluator model implies unavailability or non-existence."** The paper cites Qwen3-235B-A22B-fp8 as the evaluator. Per the hard rule, any citation to a model/tool/dataset in the paper is taken as existing. Removed as an existence concern; only the "modification not described" aspect is retained in Minor above.

- **"Rubric Scorer and Evaluator may disagree (temperature mismatch)."** The Rubric Scorer runs at temperature 0.6 while the Evaluator at temperature 0.0. The concern is purely speculative — there is no demonstration in the paper that this leads to systematic error, nor any specific result where the divergence is manifest. Removed.

- **"AutoDAN-Turbo observation used to motivate RSS may be incorrect."** The harsh critic notes "only human-generated strategies seem to yield improvement for AutoDAN-Turbo" and asks if PLAGUE's RSS benefit is also from initialized strategies. This is a valid research question but the observation from Section 2.1 is the paper's own stated motivation. The concern is recast as a Nice-to-Have ablation rather than a kept weakness.

- **Strength: "Lifelong-learning memory retrieval based on semantic goal similarity provides a novel mechanism."** This strength conflicts with the verified weakness that (a) the measured contribution of RSS is modest (4.1% on o3) and (b) the mechanism's actual operation (vs. random fallback) is unquantified. The strength as stated is misleading; removed from strengths per the conflict rule.

---

## Novel Insights

The paper's most genuinely novel observation is that Reflection — not lifelong learning or planning initialization — accounts for the largest single component contribution to ASR in the ablation (Table 3: from 0.612 to 0.761 SRE on o3, vs. 0.041 for RSS). This inverts the framework's own rhetorical priorities and suggests that iterative self-critique within a multi-turn attack is the key driver of jailbreak effectiveness on safety-aligned models. The paper does not fully foreground this finding, but it points to a promising and relatively underexplored direction: in multi-turn attacks, the quality of the Attacker's internal feedback loop may matter more than memory of past successes.

---

## Suggestions

1. **Fix the abstract claim**: Revise "improving ASR by more than 30% across leading models" to accurately reflect where the gains hold (o3 and Opus 4.1). The actual numbers in Table 2 are honest; the abstract is not.

2. **Justify or equalize the Crescendo modification**: Either show an ablation of Crescendo with and without backtracking to confirm the performance gap is not driven by the modification, or run Crescendo in its full configuration.

3. **Report the RSS fallback frequency**: Add one column or sentence in the RSS analysis reporting what fraction of the 200 goals triggered semantic retrieval vs. random retrieval at each stage of the run.

4. **Show the GOAT history ablation**: Provide the supporting table referenced by the one-sentence claim about negligible impact of disabling GOAT's history.

5. **Describe the StrongREJECT modification**: Add the modified evaluation prompt to the appendix and note the delta from the original.

---

## Score and Decision

**Axis evaluation:**
- *Originality*: Moderate-to-high. Three-phase decomposition of multi-turn attacks with lifelong memory is novel in this setting; individual components (backtracking, reflection, retrieval) are borrowed from prior work but their assembly is new.
- *Importance of research question*: High. Multi-turn jailbreaking of frontier models is a practically significant safety concern.
- *Claims well-supported*: Moderate. The ablation is rigorous; the headline abstract claim is not supported for 3/5 models.
- *Soundness of experiments*: Moderate. Internally consistent evaluation; the Crescendo baseline modification and the per-model Finisher selection are genuine concerns.
- *Clarity of writing*: Good. The methodology is clearly explained; the abstract is misleading.
- *Value to research community*: Good. A modular, open-source framework with ablation benchmarks serves the red-teaming community.

**Anchor comparison:**
- Round 1 brackets: Weak papers (1.4–3.0); Middle (5.33–5.75); Strong (8.0)
- Round 2 anchors: ActorAttack (5.33, Reject) — PLAGUE is clearly better in ablation rigor and empirical scope; MHJ (5.75, Reject) — different type; AutoDAN-Turbo (7.17, Accept) — most directly comparable (lifelong learning + plug-and-play jailbreak), single-turn; PLAGUE extends to multi-turn with more components but has more substantive weaknesses (abstract overclaim, Crescendo modification concern, modest RSS contribution).

PLAGUE is meaningfully better than the 5.33–5.75 anchors but sits below AutoDAN-Turbo's 7.17 due to the abstract overclaim (failing for 3/5 models), the unverified GOAT modification assertion, and the asymmetric Crescendo comparison. Placing at **6.0**: a weak accept reflecting real contributions, solid ablation, and compelling results on hard targets, tempered by important presentation and comparison issues that require revision.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
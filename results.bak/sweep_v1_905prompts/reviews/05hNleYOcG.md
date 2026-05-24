Now I have sufficient calibration data. Let me write the consolidated review.

**Bracket analysis:**
- Round 1 bracket: Between ~4 and ~7. The paper is clearly stronger than the weak bracket papers (1.4–3.0) and the mid-bracket rejected papers (3.67–5.75). It is weaker than the strong-bracket papers (7.75–9.5) which make different types of contributions.
- Round 2 narrowing: AutoDAN-Turbo (7.17, Accept) is the closest relative — a lifelong-learning jailbreak framework, but single-turn only. PLAGUE extends to multi-turn with modular phases. "Jailbreaking Leading Safety-Aligned LLMs" (6.14, Accept) is simpler but very thorough. "Uncovering Model Vulnerabilities" (5.75, Reject) is human-driven with limited model coverage.
- Final placement: PLAGUE is stronger than the rejected mid-bracket papers (tested on 5 models vs 1-2, has ablations and efficiency analysis, fully automated) but has real weaknesses in baseline validation and lifelong learning evidence that prevent it from reaching the AutoDAN-Turbo tier. I place it at **6.0**.

Now let me write the full review.

---

Actually, let me reconsider the Harsh Critic's points carefully before finalizing.

**Critic Point 1: Ablation study does not isolate components - the Primer is missing.**
Looking at the paper: Section 3.5 says "We demonstrate results with GOAT as our Finisher in Table 3, adding one component from our framework at a time." The Table 3 shows: GOAT → +BT → +R → +P → +RSS.

When "P" (Planner) is added to GOAT as Finisher, the plan from the Planner needs to be processed somehow before feeding to the Finisher. The Primer is the component that does this processing (Section 3.4: "the Primer receives both the conversation history and the planner-generated query"). So when "P" is added, the Primer must also be included since the Primer is what transforms the plan into the context that the Finisher uses. The paper's description in Section 3.5 says "freezing the generated planning context" which is the Primer's job.

However, the critic's point that this should be stated explicitly IS valid. The paper says "adding one component from our framework at a time" but "P" actually bundles the Planner AND Primer together (since the Primer can't function without the Planner). This is at best a clarity issue, and the critic overstates it as a "structural issue."

**Critic Point 2: Lifelong learning not demonstrated.**
The only evidence is RSS in Table 3. The paper doesn't show retrieval hit rates, temporal trends, or whether improvement comes from initial 2 strategies. This IS a valid concern, though the magnitude depends on how convincing one finds Table 3's improvement. The improvement from P (0.773) to P+RSS (0.814) on o3 is about 5%, which could come from the initial 2 strategies alone. Without showing temporal trends, we can't verify the lifelong learning claim. This is a reasonable concern - I'll call it a Major weakness.

**Critic Point 3: Baseline configuration changes.**
For Crescendo: "remove any explicit backtracking counts from their attack." This is ambiguous - it could mean removing limits on backtracking (helping Crescendo) or removing the ability to backtrack (hurting it). Given the budget is fixed at 6 turns, removing backtracking limits may not change much. But the paper doesn't validate this. Valid concern.

For GOAT: The paper claims impact of changes is "negligible" based on "extensive ablation" but shows no data. This IS a weakness - the paper should show the data, even briefly.

For ActorBreaker: K=2 limit is fair since PLAGUE uses K=2. The critic's concern is weaker here.

**Critic Point 4: Duplicated ActorBreaker row.**
This is a parser artifact - the original PDF likely doesn't have this. I should remove this criticism.

**Critic Point 5: Attacker model consistency.**
The paper says "Deepseek-R1 as our primary Attacker model across all our experiments." The baselines section says "we explain the changes we make to the configurations" for baselines - it doesn't say they use the same attacker model. This is a valid concern - if baselines use weaker attacker models (e.g., GPT-4 instead of Deepseek-R1), the comparison favors PLAGUE. Valid concern.

Let me finalize the review now.## Summary

This paper presents PLAGUE, a modular three-phase framework (Planner → Primer → Finisher) with a lifelong-learning memory bank for generating multi-turn jailbreak attacks on LLMs. The framework disentangles planning, context-building, and delivery into interchangeable modules, and incorporates a strategy-retrieval memory that stores successful plans indexed by goal embeddings. Evaluated on 200 HarmBench goals across 5 frontier models (o3, o1, Deepseek-R1, Claude Opus 4.1, Llama 3.3-70B), PLAGUE achieves strong results (81.4% SRE on o3, 67.3% on Claude Opus 4.1) with competitive query budgets. The paper demonstrates that GOAT, Crescendo, and ActorBreaker can serve as drop-in Finisher modules, validating the plug-and-play design.

## Strengths

1. **State-of-the-art attack success rates across multiple frontier models**: Table 2 shows PLAGUE achieves 81.4% SRE on OpenAl o3, 93.1% on o1, and 97.8% on Deepseek-R1—outperforming all baselines on these models. These are among the highest reported ASRs on models widely considered highly resistant to jailbreaks, providing direct evidence for the paper's central empirical claim.

2. **Systematic ablation quantifying each component's contribution**: Table 3 progressively adds Backtracking, Reflection, Planner, and Strategy Retrieval to a GOAT baseline on o3, showing SRE rising from 0.587 → 0.612 → 0.761 → 0.773 → 0.814. This design gives clear, quantified evidence that each phase independently drives the claimed improvements.

3. **Plug-and-play modularity validated by component swapping**: Table 4 replaces the GOAT Finisher with Crescendo on Claude Opus 4.1, improving SRE from 0.48 (Crescendo alone) to 0.673 (PLAGUE with Crescendo Finisher). This directly supports the framework's modularity claim and shows the same architecture can be reconfigured for different victim models.

4. **Efficiency analysis showing gains come from design, not query budget**: Table 5 reports that PLAGUE uses only ~3.85 target calls on o3 (versus GOAT's 3.08 and Crescendo's 3.14), while nearly doubling ASR over GOAT. The paper consistently holds baselines to the same 6-turn budget, making the efficiency comparison meaningful.

5. **Comprehensive evaluation across 5 models with consistent methodology**: All methods are evaluated on the same 200-sample HarmBench set, with two metrics (Bin-ASR and SRE), and averaged over 3 runs. This is a more thorough evaluation than most prior multi-turn attack papers.

## Weaknesses

### Major

1. **Baseline modifications are not validated, potentially undermining headline comparisons**. The paper modifies Crescendo by "remov[ing] any explicit backtracking counts from their attack" (Section 4) and modifies GOAT by adding a Rubric Scorer, disabling attack history, and enabling early stopping—claiming "negligible" impact based on "extensive ablation" without showing any data. Since the paper's headline improvements (32.14% over GOAT on o3, 40.2% over Crescendo on Claude Opus 4.1) depend critically on these baselines being unfettered, the lack of validation is a significant gap. The paper should report each baseline under both its original configuration and the modified configuration under identical budgets. Without this, a reader cannot determine whether the reported gaps reflect genuine superiority or a weakened comparison.

2. **The lifelong-learning claim lacks direct evidence of temporal accumulation**. The sole evidence for the lifelong-learning component is the RSS (Retrieving Successful Strategy) step in Table 3, which shows a ~5-point SRE improvement on o3. However, the memory is initialized with two strategies from Crescendo (Section 4), so this improvement could come entirely from these initial examples rather than from accumulated experience. The paper does not report: (a) retrieval hit rates, (b) whether ASR improves over the course of the 200-goal run (e.g., early vs. late goals), (c) average number of strategies retrieved per attack, or (d) how often the retrieval falls back to random selection when cosine similarity falls below 0.6. Without such evidence, the "lifelong learning" framing is not supported by the presented data.

3. **Attacker-model consistency across baselines is not clarified**. The paper states "Deepseek-R1 as our primary Attacker model across all our experiments" (Section 4), but does not specify whether the same Attacker model is used for Crescendo, GOAT, and ActorBreaker baselines. Each of these baselines could be using different default attacker models in their official implementations. If baselines use a weaker attacker model than Deepseek-R1, the performance gap could partially reflect the attacker model choice rather than the PLAGUE framework. This must be explicitly stated.

### Minor

4. **The ablation column "P" (Planner) bundles the Planner and Primer phases without clarification**. The paper describes the Planner and Primer as two separate phases (Section 3.3, 3.4), and the Primer is described as essential for building adversarial context from the plan. Yet Table 3 adds "P" as a single component and the text says "adding one component from our framework at a time" (Section 3.5). If "P" includes both Planner and Primer, this should be stated explicitly. If not, the comparison is between a Planner-only GOAT variant and the full PLAGUE system that also uses a Primer, making the ablation not isolate the Planner's contribution. This is a clarity issue that the authors should resolve.

5. **No statistical significance or variance reported**. All results are averages over 3 runs, but no standard deviations or confidence intervals are reported. With 200 samples per run, ASR variance could be non-negligible, especially for models near the middle of the range (e.g., Claude Opus 4.1). This would strengthen the reliability claims.

### Trivial

6. The paper does not report total monetary cost or inference-time overhead of the Planner and Evaluator models (Deepseek-R1 for planning, Qwen3-235B for evaluation), which is relevant for practitioners weighing the cost-performance trade-off.

## Nice-to-Haves

- Showing temporal trends in ASR (early vs. late goals) to demonstrate that the memory bank genuinely accumulates useful strategies over the course of a run.
- Reporting Crescendo under both its original backtracking configuration and the modified configuration under the same 6-turn budget.
- At least one concrete multi-turn attack trajectory (appendix) illustrating how the Primer builds context and the Finisher exploits it.
- Discussion of potential defense strategies or mitigations.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Duplicated ActorBreaker row in Table 2** — This is a parser artifact from PDF extraction; the original submission does not have this issue.
- **"Fatal structural issue" with the ablation isolating components** — The critic frames the missing Primer in the ablation as a structural flaw. However, when "P" (Planner) is added to GOAT as a Finisher, the Primer is naturally included because the Primer transforms the plan into the context that the Finisher consumes. The paper describes "freezing the generated planning context" (Section 3.5), which is the Primer's function. This is a clarity issue, not a structural flaw, and is downgraded to Minor above.
- **Criticism that the Rubric Scorer change could "considerably" change GOAT's behavior** — The paper claims this impact is "negligible" based on ablation (Section 4). While the paper should show the data, the critic's assertion that the change is necessarily harmful is speculation without evidence, especially since early stopping could HELP GOAT by focusing on successful runs.
- **Request for more models/datasets** — The paper already evaluates 5 frontier models on the standard 200-sample HarmBench, which is among the more comprehensive evaluations in this area.

## Novel Insights

The most interesting insight to emerge from reading across the reviews is that PLAGUE's modular architecture reveals an asymmetric model vulnerability pattern: different components contribute differently per model (reflection matters most for o3, backtracking matters most for Claude Opus 4.1). This suggests that the best attack configuration is model-dependent, and a plug-and-play framework like PLAGUE is valuable precisely because it enables this targeted customization. The paper's observation that Claude Opus 4.1 shows particular resistance to GOAT-based strategies (possibly due to alignment on GOAT-like attack data in its training) while remaining vulnerable to Crescendo-based variants is a concrete finding that could inform defensive alignment research.

## Suggestions

- Validate baseline modifications: report Crescendo with and without backtracking limits, and GOAT with and without the Rubric Scorer + history changes, under identical 6-turn budgets.
- Clarify whether all baselines use Deepseek-R1 as their attacker model. If not, rerun the strongest baselines with Deepseek-R1 to isolate the framework's contribution.
- Provide evidence for lifelong learning: plot moving-average ASR over the 200-goal sequence to show that later attacks benefit from accumulated memory, and report retrieval hit rates and average number of retrieved strategies.
- Clarify in Table 3 that "P" includes both the Planner and Primer phases, or separate them if feasible.
- Include standard deviations or 95% confidence intervals for all main results.

## Score and Decision

**Calibration anchors:**

| Anchor | Avg Score | Round | Comparison to this paper |
|--------|-----------|-------|-------------------------|
| NEMESIS (5kMwiMnUip) | 1.40 | 1 | Much weaker — simplistic approach, no proper evaluation |
| Incremental Exploits (KyKTjRtyNG) | 3.00 | 1 | Weaker — single baseline, limited model coverage |
| Playing Language Game (BeOEmnmyFu) | 2.50 | 1 | Weaker — narrow scope, no multi-turn evaluation |
| BlackDAN (kT6oc5CpEi) | 3.00 | 1 | Weaker — focuses on single-objective optimization |
| Uncovering Model Vulns (fFtmpqLFvw) | 5.75 | 1, 2 | Weaker — human-driven, evaluated on 1 model only |
| Derail Yourself (kvvvUPDAPt) | 5.33 | 1 | Weaker — limited evaluation (50 samples, 2 models) |
| Quack (1zt8GWZ9sc) | 3.67 | 1 | Weaker — role-playing approach, limited evaluation |
| Leveraging Context (w0b7fCX2nN) | 3.75 | 1 | Weaker — fewer models, less thorough evaluation |
| AutoDAN-Turbo (bhK7U37VW8) | 7.17 | 2 | Stronger — more thorough lifelong learning evidence, but single-turn only |
| Jailbreaking w/ Simple Adaptive (hXA8wqRdyV) | 6.14 | 2 | Comparable — simpler method, similar model coverage, accepted despite missing baselines |
| Improved Optimization-Based (e9yfCY7Q3U) | 6.25 | 2 | Comparable — optimization-based, accepted with minor concerns |
| ArrAttack (sULAwlAWc1) | 7.00 | 2 | Stronger — defense-aware attacks, accepted despite missing baselines |

**Round 1 bracket:** The paper sits well above the weak bracket (1.4–3.0) and above the mid-bracket rejected papers (3.67–5.75). It is below the top bracket (7.75+). **Initial bracket: 5.0–7.0.**

**Round 2 narrowing:** The closest relatives are AutoDAN-Turbo (7.17, Accept — single-turn lifelong learning jailbreak), "Jailbreaking Leading Safety-Aligned LLMs" (6.14, Accept — simpler method, accepted despite missing baseline comparisons), and the rejected mid-bracket papers (5.33–5.75) which have significantly narrower evaluation. PLAGUE has a more comprehensive evaluation than the mid-bracket papers and a more novel framework than the 6.14 paper, but its baseline-validation gap and thin lifelong-learning evidence prevent it from reaching the AutoDAN-Turbo tier. **Final score: 6.0.**

**Justification:** The paper's core contributions—a modular three-phase framework validated by component-swapping experiments, SOTA results on multiple frontier models, and an efficiency analysis—are genuine and well-supported. However, the unvalidated baseline modifications cast uncertainty on the headline improvement percentages, and the lifelong-learning claim needs stronger temporal evidence. These are fixable in revision. Relative to calibration anchors, the paper is clearly stronger than the rejected mid-bracket papers (5.33–5.75) and comparable to accepted papers in the 6–7 range that had similar gaps.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
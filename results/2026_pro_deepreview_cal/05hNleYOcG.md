Now I have a thorough understanding of the paper and the calibration landscape. Let me synthesize the final review.

---

## Summary

PLAGUE is a plug-and-play framework for multi-turn LLM jailbreaking that decomposes attacks into three phases — Planner, Primer, and Finisher — augmented by backtracking, reflection, and a lifelong learner that retrieves successful strategies from memory. The framework achieves strong attack success rates (81.4% SRE on OpenAI o3, 93.1% on o1, 97.8% on Deepseek-R1, 95.8% on Llama 3.3-70B, and 67.3% on Claude Opus 4.1 using a Crescendo-based Finisher), substantially outperforming prior multi-turn attacks across evaluated models. The modular design allows individual components to be swapped (e.g., using Crescendo instead of GOAT as the Finisher for Claude), and ablations show incremental gains from each added mechanism.

## Strengths

- **Modular, well-motivated framework with strong empirical results.** PLAGUE decomposes multi-turn jailbreaking into Planner, Primer, and Finisher phases with backtracking, reflection, and lifelong retrieval. Table 2 shows large margins over baselines across five leading models: e.g., 81.4% SRE on o3 vs. 61.6% (ActorBreaker) and 58.7% (GOAT); 93.1% on o1 vs. 79.8% (GOAT). These are substantial improvements over prior state-of-the-art.

- **Rigorous ablation demonstrates incremental contributions of each component.** Table 3 builds up from vanilla GOAT (0.587 SRE on o3), adding backtracking (+0.025), reflection (+0.149), planner (+0.012), and strategy retrieval (+0.041) to reach 0.814. The ablation isolates each mechanism's contribution, confirming that the full framework is more than the sum of heuristic tweaks.

- **Plug-and-play modularity is empirically validated.** Table 4 demonstrates that swapping GOAT for Crescendo as the Finisher on Claude Opus 4.1 lifts SRE from 0.465 to 0.673 — a 40.2% improvement over standalone Crescendo. This directly validates the framework's central design claim that components can be tailored per model.

- **Efficiency analysis shows gains come at modest inference cost.** Table 5 demonstrates that PLAGUE's total LLM calls are comparable to Crescendo (e.g., 6.53 vs. 5.28 on o3) while delivering far higher ASR, and it requires fewer evaluator calls than Crescendo.

- **Turn-level scaling study is informative.** Figure 2 shows ASR scaling from 36.7% (2 turns) to 81.4% (6 turns) with a plateau at 8 turns, empirically justifying the 6-turn budget choice and providing practical guidance.

## Weaknesses

### Fatal

None.

### Major

- **Baseline modifications are described but not empirically validated against original implementations.** The paper modifies GOAT (runs without attack history, stops early at rubric score > 8/10), Crescendo (removes backtracking counts, caps at 6 turns), and ActorBreaker (limits to K=2 actors). For GOAT, the paper states impact of history removal is "negligible" from ablation, but no comparison data is shown. For Crescendo, removing backtracking counts could degrade performance since the original design relies on them; limiting turns to 6 is necessary for budget fairness but changes the attack's behavior. While the reported margins are large enough that the core finding likely holds, the absence of a side-by-side comparison between modified and original implementations weakens confidence in the exact magnitude of PLAGUE's advantage. A minimal fix would be to show original-vs-modified ASR on a validation subset for each baseline.

### Minor

- **ASR@K selection uses the internal Rubric Scorer, creating a potential over-optimization path.** The attack maximizes the rubric score during execution, and ASR@2 then selects the attempt with the highest rubric score for final judge evaluation. While the final evaluation is conducted by the external StrongREJECT judge (𝕁, not the Rubric Scorer), any correlation between rubric and judge scores could inflate reported ASR. A cleaner methodology would use the judge for selection or report the average without selection. The paper is transparent about this choice and it is not uncommon in jailbreak literature, but it merits acknowledgment as a methodological limitation.

- **The abstract's 67.3% Opus 4.1 figure uses a different Finisher module without qualification.** The abstract states "67.3% on Claude's Opus 4.1" alongside "81.4% on OpenAI's o3" as though both use the same PLAGUE configuration. In fact, the default PLAGUE (GOAT Finisher) achieves only 46.5% on Opus 4.1; the 67.3% comes from substituting Crescendo as the Finisher (Table 4). The paper is fully transparent about this in the body text and Table 2's footnote, but the abstract should explicitly note this configuration difference to avoid misleading readers.

- **No variance estimates reported.** Results are averaged over three runs, but no confidence intervals or standard deviations are provided. Given multi-turn attack variance, this makes it difficult to assess whether small differences (e.g., some ablation increments in Table 3) are statistically meaningful.

- **Lifelong-learning retrieval mechanism is under-analyzed.** The RSS component contributes modest gains (e.g., +0.041 SRE on o3, +0.034 on Opus 4.1 in Table 3), but the paper provides no analysis of retrieval precision, how often retrieved strategies are actually relevant, or how the memory bank grows over time. The paper's framing emphasizes lifelong learning as a key contribution, yet the quantitative evidence for its practical benefit beyond the seeded strategies is thin.

### Trivial

- The claim in the introduction that "multi‑turn jailbreaks lack a formal investigation into what makes them work" is somewhat overstated — ActorBreaker and RACE already analyze component contributions — though PLAGUE's own analysis (Table 3) does go deeper than prior work.

- The paper uses "ASR" and "SRE" interchangeably, which can cause confusion when binary-ASR is also reported alongside SRE in the same tables.

## Nice-to-Haves

- An ablation that removes components from the full PLAGUE (rather than only building up from GOAT) would confirm contributions are not order-dependent.
- Sensitivity analysis of rubric scoring thresholds (e.g., what if the Primer threshold were 6/10 instead of 7/10?) would strengthen claims of robustness.
- Reporting retrieval precision and memory-bank growth statistics would substantiate the lifelong-learning narrative.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic's claim that baseline modifications are a "structural weakness" that makes the evaluation "untrustworthy."** The paper describes all modifications transparently, claims to have tested GOAT's history impact (finding it negligible), and the margins are large enough (e.g., +20 SRE points on o3) that degradation alone cannot explain the advantage. This is a legitimate concern but not structural or fatal.

- **Harsh Critic's claim that the Opus 4.1 presentation "undermines the paper's integrity."** The paper is explicit in Tables 2 and 4 about which configuration achieves which result, and the body text (Section 5.1) discusses the configuration difference openly. The abstract could be more precise, but this is not an integrity issue.

- **Harsh Critic's note about missing appendix for verifying Rubric Scorer prompts and backtracking algorithm.** The parser strips appendix sections from all papers; they exist in the original submission.

- **Harsh Critic's claim that the AutoDAN-Turbo criticism is presented "without citation or empirical evidence."** The paper presents this as their own observation (line 59: "a major drawback we observe"), which is a qualitative claim, not a factual error.

- **Strength Finder's claim that "lifelong learning via goal-similarity-based strategy retrieval improves attack success" as a standalone major strength.** The gains from RSS are modest (+0.041 SRE on o3) and the mechanism is under-analyzed; this is better framed as a supporting finding rather than a headline strength.

- **Criticism about reproducibility (undisclosed hyperparameters, complete training logs).** The paper discloses key parameters (temperature, models used, retrieval threshold, similarity threshold, budget, K=2) in the experimental setup; remaining details are standard practice to omit in the main text.

## Novel Insights

The paper's cross-model ablation (Table 3) reveals an interesting finding that the dominant success factor differs by model: for OpenAI o3, reflection provides the largest gain, while for Claude Opus 4.1, backtracking is the most impactful component. This pattern suggests different models have qualitatively different safety vulnerabilities — some are more susceptible to feedback-driven optimization (o3) while others are more vulnerable to context management (Claude). This insight, while not deeply explored, hints at a more nuanced taxonomy of LLM safety failures than the literature typically provides.

## Suggestions

- Show a head-to-head comparison of modified vs. original baselines on a validation subset (e.g., 50 HarmBench samples) to address the baseline fairness concern directly.
- Either justify the rubric-based ASR@K selection with evidence that rubric and judge scores are sufficiently decorrelated, or switch to judge-based selection / averaging.
- Qualify the Opus 4.1 result in the abstract by noting the finisher variant (e.g., "67.3% on Claude Opus 4.1 (using Crescendo as Finisher)").
- Add a quantitative analysis of the retrieval mechanism: precision-at-k, how often retrieved strategies differ from seeded ones, and growth statistics of the memory bank.
- Report standard deviations or confidence intervals.

## Score and Decision

**Calibration summary:**

| Anchor Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| NEMESIS | 1.40 | R1 | Much weaker — basic jailbreak survey, no systematic framework |
| Incremental Exploits (MRCJ) | 3.00 | R1 | Weaker — limited multi-turn approach, narrower evaluation |
| BlackDAN | 3.00 | R1 | Weaker — single-turn focus, narrower scope |
| Quack | 3.67 | R1 | Weaker — role-playing framework, limited evaluation |
| PAIR | 4.75 | R2 | Weaker — iterative refinement, narrower scope |
| Derail Yourself (ActorAttack) | 5.33 | R2 | PLAGUE is stronger — better ablations, broader eval, clearer contribution |
| DAG-Jailbreak | 5.50 | R2 | PLAGUE is stronger — larger empirical gains, better ablation |
| Uncovering Model Vulnerabilities (MHJ) | 5.75 | R1/R2 | PLAGUE is stronger — automated method vs. human dataset, broader model coverage |
| Simple Adaptive Attacks | 6.14 | R2 | Comparable — PLAGUE has more methodological novelty but similar evaluation concerns |
| Improved Techniques for Optimization-Based JB | 6.25 | R2 | Comparable — PLAGUE has broader multi-turn scope |
| AgentHarm | 6.75 | R2 | Different category — benchmark contribution |
| ArrAttack | 7.00 | R2 | PLAGUE is somewhat weaker — narrower method, less transfer analysis |
| Curiosity-driven Red-teaming | 8.00 | R1 | PLAGUE is weaker — CRT has stronger theoretical grounding and cleaner evaluation |

**Round 1 bracket:** 5.5–7.5. PLAGUE is clearly stronger than the 3–5.5 range papers and weaker than the 8+ range.

**Round 2 narrowing:** PLAGUE lands between 6.0 and 7.0. It is stronger than the 5.33–5.75 multi-turn attack papers (ActorAttack, MHJ) due to better methodology and broader evaluation. It is comparable to the 6.14–6.75 papers in contribution level, trading off stronger empirical results and modular design against some methodological imprecision in evaluation.

**Final score:** 6.5. The paper makes a genuine contribution with a well-designed modular framework and strong empirical results across an impressive range of models. The evaluation methodology has real but addressable weaknesses (baseline modification transparency, ASR@K selection, no variance reporting) that pull it down from the 7+ range, but the core contribution stands.

**Originality:** Good — modular decomposition of multi-turn attacks with lifelong learning is novel in this space.  
**Importance:** High — multi-turn jailbreaking is an underexplored and critical safety concern.  
**Claims supported:** Mostly — strong results but some methodological looseness in evaluation.  
**Soundness:** Fair — experiments are comprehensive but baseline and metric choices could be tighter.  
**Clarity:** Good — the paper is well-structured and the three-phase design is clearly communicated.  
**Value to community:** Solid — the framework is a useful tool for red-teamers and the cross-model vulnerability analysis is informative.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
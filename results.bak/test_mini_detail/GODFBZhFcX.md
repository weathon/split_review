Now let me finalize my calibration before writing the review.

**Round 1 Bracket:** The paper clearly sits in the middle band (3.5–7.5). The weak anchors (avg 2.0–3.25) are rejected/withdrawn papers with fundamental flaws. The strong anchors (avg 7.75–8.0) are oral/spotlight papers with major contributions. This paper falls between them.

**Round 2 Bracket:** CaPo (avg 6.0) is the most directly comparable — same benchmarks (C-WAH, TDW-MAT), same problem setting (LLM multi-agent embodied cooperation), and was accepted as poster. CaPo's reviews questioned its novelty (it was seen as an incremental extension of CoELA via prompt engineering). PCE has a more novel core idea (extracting assumptions into decision trees, explicit uncertainty scoring) and broader evaluation (3 LLM backbones, scaling analysis, component ablation, user study). Compared to ThinkBot (avg 5.75, accepted poster), PCE has more thorough evaluation. I place PCE between CaPo (6.0) and COMBO (6.67). Final score: **6.0**.

---

## Summary

This paper introduces PCE, a Planner-Composer-Evaluator framework for decentralized multi-agent embodied planning under partial observability. The core idea is to extract the implicit assumptions latent in LLM reasoning traces, structure them into a decision tree where internal nodes encode environment assumptions and leaves map to actions, then score each root-to-leaf path by scenario likelihood, goal-directed gain, and execution cost. This allows agents to select actions rationally without relying on heavy inter-agent communication. Experiments on C-WAH (10 episodes) and TDW-MAT (24 episodes) across three LLM backbones (GPT-4o mini, GPT-OSS:20B, Gemma3:4B) show PCE consistently achieves better task efficiency and success rates than communication-centric baselines (CoELA, REVECA, CaPo, CoTS), with a user study providing preliminary evidence of perceived trust and efficiency.

## Strengths

- **Novel and principled approach to uncertainty in LLM-based planning.** The idea of explicitly extracting, structuring, and scoring the implicit assumptions that LLMs already generate in their reasoning traces is genuinely novel. Unlike prior work that relies on communication-heavy coordination or generic tree-search over reasoning steps (ToT), PCE treats environment assumptions as first-class decision variables and scores them via likelihood, gain, and cost — a well-motivated formulation grounded in decision theory. This shifts the paradigm from communication-centric mitigation to structured reasoning over uncertainty.

- **Consistent empirical superiority across diverse benchmarks and backbones.** Tables 1 and 2 show PCE achieves the best Total Steps on C-WAH (e.g., 42.76 vs. 60.40 for CoELA with GPT-4o mini) and highest Total success rate on TDW-MAT (e.g., 87.50% vs. 62.50% for CoELA with GPT-4o mini) across all three LLM backbones. This consistency demonstrates the framework's advantage is not tied to a single model or environment. The evaluation covers 3 backbones spanning commercial, open-source, and reasoning-specialized models.

- **Ablation study confirms each component's necessity.** Table 3 shows that removing the Planner, Composer, or Evaluator individually degrades performance (Total Steps: full PCE 42.76; w/o Planner 56.46; w/o Composer 46.82; w/o Evaluator 47.34), providing clear causal evidence that the full pipeline is required. Additionally, Figure 3 demonstrates that PCE's benefits are additive to scaling model capacity (Gemma3:4B→12B→27B) and reasoning depth — structured uncertainty handling provides gains that mere scaling cannot.

- **User study with real participants.** Figure 4 shows that PCE scores highest on all four Likert-scale questions (Appropriateness, Usefulness, Efficiency, Trust) compared to no-communication and always-communication variants, bridging simulation metrics to human perception of collaborative quality.

## Weaknesses

### Major
- **No statistical significance or variance reporting.** All results in Tables 1–3 and Figure 3 are reported as point estimates with no standard deviations, confidence intervals, or significance tests. This is the most consequential weakness given the small evaluation budgets: C-WAH has only 10 episodes and TDW-MAT has 24 episodes. With such small samples, the reported differences (e.g., PCE 42.76 vs. REVECA 46.80 on C-WAH GPT-4o mini, a ~9% difference) could be driven by variance rather than genuine improvement. The paper repeatedly claims PCE "consistently outperforms" baselines, but without variance estimates or information about how many runs/seeds were used, this claim is not fully supported. This affects nearly every quantitative result in the paper.

- **LLM-based likelihood and gain estimation not validated in the main text.** The entire Evaluator hinges on LLM estimates of scenario likelihood (ℒ) and conditional gain (𝒢) normalized to [0,1]. The paper acknowledges these are approximations (Section 4.4) and references human-expert correlation studies in the appendix (A.10, A.11). However, the main paper provides no evidence that these estimates are sufficiently accurate to support the claimed performance gains. Without such validation, it remains unclear whether the observed improvements come from genuinely useful structuring of assumptions or from noise that happens to correlate with good actions. Given that the method's core mechanism depends entirely on these estimates, this is a significant evidential gap.

### Minor
- **Overclaimed "comparable token usage" for specific comparisons.** The abstract and conclusion state PCE achieves "comparable token usage" to baselines. While this holds in aggregate across C-WAH, on TDW-MAT with GPT-4o mini, PCE's total token consumption (197,807) is ~75% higher than CoELA (113,058). PCE achieves much higher success rates, but describing this as "comparable" is imprecise. The paper also uses more tokens than CoELA on TDW-MAT with Gemma3:4B (184,809 vs. 98,350) and GPT-OSS:20B (337,225 vs. 237,499). The claim should be more carefully scoped.

- **Ablation shows w/o Composer performs well with minimal communication.** Table 3 shows the w/o Composer variant achieves 46.82 Total Steps (vs. full PCE 42.76, w/o Evaluator 47.34) with only 0.26 communication actions — meaning the Planner+Evaluator alone, without the structured tree, already outperforms all baselines except full PCE. This raises an unresolved question about the marginal contribution of the Composer beyond what the Evaluator provides directly from the Planner's raw trace. The paper should disentangle whether the Composer primarily generates useful communication actions or genuinely improves physical action selection.

- **User study compares against trivial baselines, not full methods.** The user study (Section 5.3) compares PCE against "w/o Com" (no communication) and "Com always" (forced communication) rather than against the full baseline methods (CoELA, REVECA) used in the main experiments. This design primarily validates that some communication is better than none — a known result — rather than demonstrating that humans perceive PCE as more trustworthy than existing approaches.

### Trivial
- The "PCE" bar appears twice in Figure 4's description (line 246 mentions "PCE (blue)" twice).

## Nice-to-Haves
- Include standard deviations or confidence intervals for main results (Tables 1–3), or at minimum report the number of random seeds/runs.
- Add a brief validation of the Evaluator's ℒ and 𝒢 estimates in the main paper (e.g., correlation with ground-truth frequencies or task progress).
- Discuss representative failure cases (e.g., where the Composer generated an incorrect assumption tree) to calibrate expectations about limitations.
- Report the mean and variance of participant ratings in the user study (Figure 4 currently lacks error bars).

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Criticism about missing implementation details for Composer (prompts, ranking policy).** The paper states "Detailed prompting strategies for Planner, Composer, and Evaluator are provided in Appendix A.12." The parser strips appendices; this content exists in the original submission. *[REMOVED: parser artifact]*

- **Criticism about missing appendix content (A.10, A.11 human-expert correlation studies).** Same parser issue — the appendices exist in the original submission. *[REMOVED: parser artifact]*

- **Criticism about missing failure cases / generalization to free-form dialogue.** These are valid observations but are scope extensions, not weaknesses of the current submission. *[REMOVED: scope creep]*

- **Strength Finder claim about "gains are additive to scaling" being a key strength.** This is actually well-supported by Figure 3 and the text. *[KEPT — this is validated]*

- **Strength Finder's generic statement about "addressing an important problem."** This is generic and not specific to this paper. *[REMOVED: generic]*

## Novel Insights

The harsh critic's observation about the w/o Composer ablation revealing near-optimal performance with minimal communication (0.26 Comm) is the most insightful point that goes beyond what the paper itself discusses. This suggests the Composer's primary value might be in generating the structured tree that enables better Evaluator scoring, rather than in directly producing better actions — but the ablation does not cleanly separate these mechanisms. The Structure Finder correctly identified that the consistent superiority across 3 diverse LLM backbones is the strongest single piece of evidence, but neither reviewer noted that this consistency also indirectly validates the Evaluator: if the LLM-based estimation were pure noise, one would expect more variance across backbones rather than the monotonic improvements observed.

## Suggestions

1. **Add statistical rigor.** Report standard deviations and number of runs for the main results. This is the single action that would most strengthen the paper. Even approximate confidence intervals via bootstrapping over the 10/24 episodes would be informative.

2. **Validate the Evaluator's estimates in the main text.** Show a simple correlation between LLM-predicted scenario likelihoods and actual scenario frequencies, or between predicted gains and actual task progress on a representative subset. This would substantially increase confidence in the core mechanism.

3. **Sharpen the token usage claim.** Replace "comparable token usage" with something more precise like "PCE achieves competitive token efficiency, using fewer tokens than most baselines while sometimes trading higher per-step cost for shorter episodes compared to the lightest baseline (CoELA)."

4. **Add a targeted analysis of the Composer's marginal contribution.** Compare a variant where the Evaluator scores actions directly from the Planner's raw trace (no tree) against the full PCE, controlling for whether the chosen action is physical or communicative. This would clarify what the structured tree representation uniquely enables.

## Score and Decision

**Calibration Anchors (all rounds):**

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| CaPo (ICLR 2025 poster) | 6.00 | R1 | Most directly comparable (same benchmarks, same problem). PCE has a more novel core idea and broader evaluation. Both lack statistical rigor. **PCE is somewhat stronger.** |
| COMBO (ICLR 2025 poster) | 6.67 | R1/R2 | Different approach (world models + tree search). More technical depth but different contribution type. **Comparable.** |
| EMOS (ICLR 2025 poster) | 6.75 | R1/R2 | Heterogeneous robot systems; different focus. Had limited baseline comparisons. **Comparable.** |
| ThinkBot (ICLR 2025 poster) | 5.75 | R2 | Single-agent EIF, single benchmark. PCE has broader evaluation. **PCE is stronger.** |
| HAZARD Challenge (ICLR 2025 poster) | 6.75 | R2 | Benchmark paper with basic LLM agent. Different contribution type. **Comparable.** |
| TeamCraft (ICLR 2025 withdrawn) | 3.25 | R1 | Rejected/withdrawn with significant weaknesses. **PCE is much stronger.** |
| Talking Vehicles (ICLR 2025 reject) | 3.75 | R1 | Rejected. **PCE is much stronger.** |

**Round 1 Bracket:** 3.5–7.5 (middle band).

**Round 2 narrowing:** CaPo (6.0) is the most directly comparable accepted paper. PCE has a more novel contribution and broader evaluation but shares the core weakness of missing statistical rigor. Placed between CaPo (6.0) and COMBO (6.67). Final score: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
## Summary

PCE (Planner-Composer-Evaluator) is a framework that extracts implicit environmental assumptions from LLM reasoning traces and structures them into a scored decision tree for uncertainty-aware action selection in embodied multi-agent cooperation under partial observability. The core idea—treating assumptions as first-class decision variables in a tree, scoring paths by scenario likelihood, goal-directed gain, and execution cost—enables agents to rationally choose between physical and communication actions without heavy dialogue. Across two benchmarks (C-WAH and TDW-MAT) and three LLM backbones, PCE consistently achieves the best task performance while dramatically reducing communication, with solid ablation studies supporting the indispensability of each module.

## Strengths

- **Consistent outperformance across all configurations.** Tables 1 and 2 show PCE achieves the best Total Steps on C-WAH (42.76, 49.60, 59.20 across backbones) and the best Total success rate on TDW-MAT (87.50, 81.25, 70.83) against CoELA, REVECA, CaPo, and CoTS. These are not marginal wins—on TDW-MAT with GPT-4o mini, PCE reaches 87.50% versus the next-best REVECA at 81.25%, and CoELA at 62.50%.

- **Genuinely novel conceptual contribution.** The paper clearly differentiates PCE's decision tree (internal nodes = environmental assumptions, leaves = actions) from Tree-of-Thoughts (reasoning steps in single-agent fully-observable settings) and CoTS (communication-dependent joint search). Treating communication as an evaluated atomic action rather than a search prerequisite is a clean and distinctive design choice (Section 2, Section 4.3).

- **Dramatic communication reduction.** Tables 1 and 2: PCE uses 1.70 communication actions on C-WAH (GPT-4o mini) versus 8.72–10.24 for baselines; on TDW-MAT, 3.58 versus 43.76–108.92. This directly validates the paper's central premise that structured reasoning over assumptions can replace heavy dialogue-based coordination.

- **Scaling ablation demonstrates additive value.** Figure 3 shows that increasing Gemma capacity from 4B→12B→27B or GPT-OSS:20B reasoning depth from Low→Medium→High yields only modest improvements for the "Planner only" baseline, while PCE consistently maintains a substantial performance gap. This supports the claim that structured uncertainty handling is complementary to, not subsumed by, model scaling.

- **Component ablation confirms each module's role.** Table 3 shows removing Planner (56.46 steps), Composer (46.82), or Evaluator (47.34) each degrades performance relative to full PCE (42.76), with the Planner removal causing the largest drop.

## Weaknesses

### Fatal
None.

### Major

- **Overclaimed token efficiency.** The abstract and conclusion state PCE achieves "comparable token usage" across both benchmarks, but this is not supported by the TDW-MAT results. From Table 2: with GPT-4o mini, PCE uses 197K tokens versus CoELA's 113K (75% higher); with GPT-OSS:20B, 337K versus 237K (42% higher); with Gemma3:4B, 185K versus 98K (88% higher). Section 5.1 states PCE "achieves high performance while maintaining low *Usages*," which is accurate for C-WAH (Table 1) but misleading for TDW-MAT. The paper should honestly acknowledge that PCE trades higher token consumption for substantially better task performance on the harder benchmark, and reframe this as a favorable trade-off rather than claiming parity. This is the paper's most significant framing issue—it doesn't invalidate the results but misrepresents them.

### Minor

- **Scaling ablation limited to C-WAH.** Figure 3 and Section 5.2 only report the capacity/reasoning-depth scaling ablation on C-WAH. The paper's abstract and Section 2 claim PCE's benefits "complement both forms of scaling," but this claim is only demonstrated on one of two benchmarks. Reporting the same ablation on TDW-MAT would substantially strengthen the generalizability claim.

- **User study lacks statistical rigor.** With only 12 participants and no confidence intervals, p-values, or effect sizes reported, it is impossible to determine whether the 1–2 point differences on the 7-point Likert scale (Figure 4) are statistically meaningful. The conditions also compare PCE against two artificial extremes (no communication at all vs. communication before every action), which makes PCE look favorable by design rather than testing it against a realistic baseline like CoELA's actual behavior.

- **Evaluator scoring validation not surfaced in main text.** The entire Evaluator depends on three LLM-estimated quantities (scenario likelihood, conditional gain, execution cost) that are inherently uncalibrated. The paper references Appendix A.10 and A.11 for human-expert correlation studies, but the main text does not summarize these findings. A reader evaluating the paper on its face cannot assess whether the scoring mechanism actually works. At minimum, one sentence of key results from these studies should appear in the main text.

- **Per-step LLM call and token breakdown not provided.** The paper acknowledges that "PCE's three-module LLM architecture incurs higher per-step inference cost" compared to CoELA's two inferences per step (Section 5.1), but does not quantify how many LLM calls are made per step (especially given the Composer's tree expansion up to depth D=3) or break down which module consumes the most tokens. This analysis would help readers understand whether the overhead scales gracefully.

### Trivial

- **Comm metric emphasis tension.** The paper explicitly states "*Comm* does not have an intrinsic 'better is lower' or 'better is higher' interpretation" and treats it as "descriptive" (Section 5, Metrics), yet PCE's low communication is repeatedly highlighted as a benefit in the discussion (Section 5.1). The paper should either evaluate communication reduction as a formal contribution with statistical tests, or consistently treat it as diagnostic. The current framing is inconsistent.

## Nice-to-Haves

- A qualitative error analysis showing representative failure cases (when PCE produces incorrect assumptions or poor scenario trees) would increase credibility and guide future work.
- Hyperparameter sensitivity for D (tree depth) in the main text, since D directly controls the method's core mechanism and is currently entirely deferred to the appendix.
- Brief discussion of what would need to change to apply PCE beyond household tasks, to bound the contribution's scope.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Unexamined reliability of LLM-generated scoring"** — Partially addressed by the paper's references to Appendix A.10 and A.11 (human-expert correlation studies). The critic's concern that the main text doesn't summarize these findings is valid and kept as a minor weakness, but framing it as "unexamined" overstates the gap since validation exists in the appendix.
- **"Figure 3 ablation framing overstates what it shows"** — The critic claims the ablation compares PCE against "a stripped-down variant, not a standard scaling baseline." However, the "Planner only" comparison is a reasonable ablation that directly tests the value of the Composer-Evaluator; this is standard ablation practice, not a misleading framing.
- **"Depth limit D=3 and early stopping are not well-defined"** — The paper states "expansion is limited at depth D or stops early when further splits would not materially affect action choice" (Section 4.3) and defers prompting details to Appendix A.12. This is standard practice for a method paper; the main text gives the reader sufficient understanding of the mechanism.

## Novel Insights

The paper's most genuine novel insight is that LLM planning traces already contain implicit environmental assumptions that can be extracted and structured into a decision tree for principled uncertainty reasoning—no special model access or training is required. This reframes the problem from "how should agents communicate to reduce uncertainty?" to "how should agents reason over their own assumptions to select actions?", treating communication as just another action in the utility-maximization space. The consistent result that this structured reasoning provides additive benefits beyond model scaling (Figure 3) is a valuable empirical finding for the embodied agents community.

## Suggestions

- **Reframe the token usage claim honestly.** Replace "comparable token usage" in the abstract and conclusion with a statement that PCE trades higher per-step computation for substantially better task performance and far less communication, and argue that this trade-off is favorable. This is actually a stronger argument than claiming false parity.
- **Surface the scoring validation results.** Add 1–2 sentences in Section 4.4 or 5.2 summarizing the key findings from Appendix A.10/A.11 (e.g., "Human-expert correlation studies in Appendix A.10–A.11 show X correlation between LLM-predicted scores and expert judgments").
- **Report the scaling ablation on TDW-MAT.** This would make the "scaling doesn't help as much as PCE" claim much more convincing, given TDW-MAT is the harder benchmark.

## Calibration Report

**Anchors retrieved:**
- BW8O4wHgbo (3.00, R1): LLM multi-agent path finding analysis — rejected, weak empirical contribution
- ByLO7p0oCF (3.00, R1): DebUnc uncertainty in multi-agent debate — rejected
- koza5fePTs (2.00, R1): LLM planning benchmarking — rejected
- cSnbM9SIJJ (3.00, R1): Large-scale multi-agent simulation — rejected
- EnXJfQqy0K (6.50, R1+R2): **CoELA** — direct baseline on same benchmarks, accepted; PCE is clearly stronger in novelty and results
- KRv9NubipP (6.00, R1+R2): **CaPo** — direct baseline, accepted; criticized as incremental extension of CoELA; PCE is substantially more novel
- Mvn48u0ehO (4.33, R1): MAPF via decision transformer — rejected
- pwKokorglv (4.00, R1): Embodied instruction following — rejected
- Q6a9W6kzv5 (8.00, R1): PhysBench — benchmark paper, different contribution type
- 7gUrYE50Rb (8.00, R1): EQA-MX — benchmark paper
- or8mMhmyRV (7.75, R1): MaestroMotif — skill design from AI feedback
- DzGe40glxs (8.00, R1): Interpreting emergent planning — different contribution type
- Glcsog6zOe (5.25, R2): Tree-Planner — tree-based task planning, less novel mechanism
- GBIUbwW9D8 (5.75, R2): R-MCTS — reflective tree search for agents
- YXRyYkb1im (6.67, R2): **COMBO** — compositional world models for multi-agent cooperation, direct comparison
- T5QLRRHyL1 (7.00, R2): **PARTNR** — benchmark for human-robot collaboration
- Ey8KcabBpB (6.75, R2): EMOS — multi-robot operating system
- Za3M6OZuCU (6.75, R2): Communication-through-actions in MDPs

**Round 1 bracket:** 4.5–7.5. The weak anchors (2–3) are clearly below PCE. The middle anchors include direct baselines CoELA (6.50) and CaPo (6.00), which PCE clearly outperforms. The strong anchors (7.75–8.00) are primarily benchmark papers of different contribution type.

**Round 2 narrowing:** Inside the bracket, PCE is clearly above CoELA (6.50) and CaPo (6.00)—more novel, better results, more backbones tested. COMBO (6.67) is a reasonable peer; PCE has cleaner conceptual novelty and more comprehensive evaluation. PARTNR (7.00) is a different type of contribution but sets a reasonable comparable bar for acceptability.

**Final positioning:** 7.0. PCE is above CoELA/CaPo due to genuine novelty and stronger empirical results, comparable to COMBO and PARTNR, but held back from 7.5+ by the token usage overclaim and user study limitations.

## Evaluation Summary

**Originality:** High. The idea of extracting implicit assumptions from LLM traces and structuring them into a decision tree for uncertainty-aware planning is novel and cleanly distinguished from prior work (ToT, CoTS, CoELA).

**Importance of research question:** High. Reducing communication dependency in embodied multi-agent cooperation under partial observability is a well-motivated and practical problem.

**Claims well supported:** Mostly. Task performance claims are thoroughly supported across backbones and benchmarks. The "comparable token usage" claim is not supported on TDW-MAT. The user study conclusions lack statistical backing.

**Soundness of experiments:** Good. Comprehensive across 3 backbones × 2 benchmarks with strong ablations. The main gaps are the missing TDW-MAT scaling ablation and per-step cost breakdown.

**Clarity of writing:** Good overall. The method is clearly presented with illustrative examples. The metrics section is thoughtful. The token usage framing is the main clarity problem.

**Value to the community:** High. The paper opens a genuinely new direction for uncertainty-aware planning that is applicable across LLM backbones and does not require special model access.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
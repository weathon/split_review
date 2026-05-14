Now I have a thorough understanding of the paper, the reviewer claims, and the calibration anchors. Let me write the consolidated review.

---

## Summary

PLAGUE is a modular, plug-and-play framework for multi-turn LLM jailbreak attacks that decomposes the attack lifecycle into Planning, Primer, and Finisher phases, augmented with a lifelong-learning memory bank that retrieves successful past strategies. The paper reports strong empirical results across five frontier models (o3, o1, Deepseek-R1, Claude Opus 4.1, Llama 3.3-70B), with systematic ablations isolating the contribution of each component and an efficiency analysis showing low inference overhead.

## Strengths

- **The modular framework is genuinely useful and well-validated.** Table 4 shows that swapping the Finisher from GOAT to Crescendo for Claude Opus 4.1 lifts SRE from 46.5% to 67.3%, and integrating ActorBreaker's planner improves diversity by 15% with negligible ASR degradation. This plug-and-play property is demonstrated, not just claimed.

- **The step-by-step ablation (Table 3) is informative and well-structured.** Incrementally adding backtracking, reflection, planning, and strategy retrieval to GOAT shows clear, monotonic improvements (o3 SRE: 0.587 → 0.612 → 0.761 → 0.773 → 0.814), giving the community a clear picture of where the gains come from.

- **The efficiency analysis (Table 5) is a practical contribution.** PLAGUE uses roughly the same number of target model calls as Crescendo (~3) and only one planner-phase attacker call while delivering substantially higher ASR. This matters for cost-aware red-teaming.

- **The paper evaluates against a comprehensive set of recent baselines** (ActorBreaker, GOAT, Crescendo, AutoDAN-Turbo, X-Teaming, FITD) on the hardest currently available safety-aligned models, including o3 and Claude Opus 4.1, making it one of the more thorough evaluations in this space.

## Weaknesses

### Major

- **The lifelong-learning memory is built from the test set during evaluation, confounding its claimed benefit.** The memory bank R^(+) is initialized with only two strategies (Section 3.3) and then accumulates strategies from successful attacks *on the same HarmBench test set* during evaluation (Section 3.5). Later test goals thus benefit from information extracted from earlier test goals—an effect that is distinguishable from generalization. The paper includes no cold-start evaluation, no leave-one-goal-out protocol, and no separate development set for memory construction. 

  *Why this matters:* The RSS (Retrieving Successful Strategies) component is presented as a key contribution and is included in the headline Table 2 results. However, the ablation in Table 3 shows that PLAGUE without RSS (GOAT+BT+R+P) already achieves SRE=0.773 on o3, which still substantially beats all baselines (best baseline GOAT: 0.587). So the core claim of SOTA performance survives, but the specific contribution of the lifelong-learning component is not cleanly measured. The authors need to add a cold-start evaluation (memory frozen at initial two strategies) to disentangle the framework's intrinsic performance from test-time adaptation.

### Minor

- **The ASR@K protocol is ambiguously described for baselines.** The paper states "We use K=2 for all our experiments" and the table headers read "ASR@2," but the text descriptions for GOAT and Crescendo (Section 4) do not explicitly confirm they were run with K=2 independent attempts and best-of-2 selection. The table headers suggest they were, but the ambiguity should be resolved. This is unlikely to change conclusions given the large performance margins (e.g., PLAGUE 0.814 vs. GOAT 0.587 on o3), but clarity is needed for reproducibility.

- **No variance estimates or confidence intervals are reported.** The paper states results are averaged over three runs, but only point estimates are provided. Given the inherent stochasticity of multi-turn attacks and the use of a 200-sample test set, reporting standard deviations would strengthen the trustworthiness of the claimed improvements. This is a standard expectation and feasible to add.

- **The claim of "scaling linearly" (Figure 2 caption) is inaccurate.** The data show performance plateaus at 6 turns and slightly declines at 8 turns—this is saturating, not linear scaling. The text itself acknowledges a "natural plateauing," so the figure caption over-claims.

### Trivial

- The assertion that removing GOAT's attack history has "negligible" impact (Section 4) is stated without supporting evidence or a control experiment. A brief note quantifying this would improve rigor.

## Nice-to-Haves

- A cold-start evaluation with the memory frozen at its initial two strategies (no test-time updates) would cleanly separate the framework's intrinsic capability from the memory adaptation effect. This is the single most important experiment to add.

- Reporting ASR as a function of how many prior test goals the memory has seen (e.g., bucketing goals by position in the evaluation order) would help quantify the magnitude of test-time adaptation.

- A control experiment replacing similarity-based retrieval with random retrieval from the memory would clarify whether similarity or mere exposure to additional strategies drives the RSS gain.

## Removed Points

These points are flagged to be removed — treat them with caution.

1. **Harsh Critic claimed ASR@K is applied unequally and that GOAT/Crescendo were run as one-shot while PLAGUE got K=2.** *Removed because:* The table headers explicitly state "ASR@2" for all methods including baselines, and the paper states "We use K=2 for all our experiments." The harsh critic appears to have misread the ambiguous baseline descriptions as evidence of unequal treatment when the table headers indicate otherwise. Kept as a Minor weakness about ambiguous description, not an actual evaluation flaw.

2. **Harsh Critic claimed "the same variance exists for baselines too" regarding K=2 justification.** *Removed because:* The paper's justification for K=2 ("to counteract the increased variance observed due to a multitude of possible paths in multi-turn conversations") is a reasonable design choice, not an unfair advantage. Whether baselines also have variance is irrelevant to the justification.

3. **Harsh Critic claimed the plateau at 6 turns "may reflect memory saturation, not a fundamental property of the attack design."** *Removed because:* This is pure speculation with no evidence. The paper's own explanation (attacker forgetting earlier turns in long contexts, drifting from objective) is at least as plausible.

4. **Strength Finder: "The PLAGUE framework achieves state-of-the-art attack success rates."** *Kept but qualified.* The headline numbers are strong but include the potentially contaminated RSS component. However, the non-RSS ablation still beats all baselines.

5. **Strength Finder: "The lifelong learning memory bank with goal-similarity retrieval improves success rates."** *Kept but qualified.* The improvement is real (0.773→0.814 on o3) but is confounded with test-time adaptation. The direction is correct; the magnitude may be inflated.

## Novel Insights

The most genuinely novel insight from this paper is the decomposition of multi-turn attack success into separable, model-dependent factors: for o3, reflection is the dominant contributor while for Claude Opus 4.1, backtracking matters most (Table 3). This suggests different safety-aligned models have different structural vulnerabilities, and a modular framework that can tailor components per model is practically valuable—different from prior work that treats all models uniformly. Additionally, the finding that planning-driven diversity (integrating ActorBreaker's planner) can be achieved with "negligible degradation in ASR" (Section 5.1) challenges the common assumption that diversity and success rate necessarily trade off.

## Suggestions

- The single most important revision is to add a cold-start evaluation: run PLAGUE with only the initial two strategies and no memory updates, and report these numbers alongside the full system. Given that the non-RSS ablation already does something close to this, this should be straightforward.

- Clarify in Section 4 whether GOAT, Crescendo, and AutoDAN-Turbo were run with K=2 independent attempts and the same best-of-2 rubric selection as PLAGUE. One sentence per baseline would resolve the ambiguity.

- Add standard deviations to Table 2 and Table 3 (even if computed across the 3 runs or via bootstrapping across the 200 goals).

- Fix the Figure 2 caption: replace "scales linearly" with "scales with conversation turns" or similar.

## Score and Decision

### Anchor Comparison

| Anchor Paper | Path | Avg Score | Comparison to PLAGUE |
|---|---|---|---|
| ACCEPT (few-shot jailbreak w/ genetic updating) | B7oQWswV7y.md | 6.50 (Reject) | ACCEPT has cleaner methodology but evaluates on older models and lacks efficiency analysis. PLAGUE has stronger empirical results on harder models but a messier evaluation due to the memory issue. PLAGUE is somewhat weaker. |
| SEMA (multi-turn jailbreak w/ RL) | 6eSNG1VNkl.md | 5.00 (Accept Poster) | SEMA accepted with missing baselines and incomplete ablations. PLAGUE has better model coverage, stronger ablation, and efficiency analysis, but shares similar evaluation concerns. PLAGUE is slightly stronger. |
| GRAF (multi-turn jailbreak) | f9BuANYtJf.md | 4.40 (Reject) | GRAF rejected for evaluation issues and novelty concerns. PLAGUE has substantially stronger results, ablation, and model coverage. PLAGUE is clearly stronger. |
| CoaxChain (multi-turn jailbreak) | 6yCZEruFu9.md | 3.50 (Reject) | Rejected for limited evaluation and cost concerns. PLAGUE is far stronger. |
| "LLMs Get Lost In Multi-Turn" | VKGTGGcwl6.md | 8.00 (Accept Oral) | Different topic, but sets the bar for methodological rigor. PLAGUE's evaluation cleanliness doesn't match this level. |
| MultiBreak (benchmark) | uJgfj5EJ2W.md | 4.50 (Reject) | Benchmark paper with different contribution type. PLAGUE's attack contributions are stronger. |
| AJF (adaptive jailbreak) | bQQkWXYjuy.md | 2.50 (Reject) | Weak results, limited evaluation. PLAGUE is far stronger. |
| MAPA (multi-turn VLM attack) | h0lOaeDwF2.md | 2.50 (Reject) | Different modality, weak results. PLAGUE is far stronger. |

### Scoring Rationale

The core strengths—a genuinely modular and well-ablated framework with strong empirical results across five frontier models—are enough to place this paper above the medium-band anchors (SEMA at 5.0, GRAF at 4.40). The framework ablation without RSS (0.773 vs. best baseline 0.587 on o3) cleanly demonstrates SOTA performance independent of the memory concern. The efficiency analysis and plug-and-play validation (Table 4, Table 5) are practical contributions the community will use.

However, the lifelong-learning memory contamination prevents this paper from reaching the high band (6.0+). The RSS component's claimed benefit is confounded with test-time adaptation, and the headline numbers include this confounded component. This is a fixable evaluation design issue—not a fatal flaw—because the non-RSS results already support the core claim. Compared to ACCEPT (6.50), PLAGUE's methodology is less clean; compared to SEMA (5.0), PLAGUE is more thorough and achieves stronger results. A score of 5.5 reflects a solid contribution with one significant but addressable evaluation concern.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
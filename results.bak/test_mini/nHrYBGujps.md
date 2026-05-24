Now I have sufficient calibration data. Let me write the consolidated review.

## Summary

BIRD-INTERACT is a benchmark that evaluates LLMs on multi-turn, dynamic text-to-SQL interaction. It converts single-turn tasks from LIVESQLBENCH into interactive scenarios requiring ambiguity resolution, knowledge retrieval, error recovery, and state-dependent follow-ups — all mediated by a function-driven user simulator that prevents ground-truth leakage. The benchmark includes 600/300 tasks spanning the full CRUD spectrum, two evaluation settings (protocol-guided *c*-Interact and agentic *a*-Interact), and budget-constrained interaction limits. Experiments with 7 frontier LLMs show that even the strongest model (GPT-5) achieves only 8.67% end-to-end success in *c*-Interact and 17.00% in *a*-Interact, confirming the task remains largely unsolved.

## Strengths

1. **Function-driven user simulator with strong empirical validation.** The two-stage design (Section 3.3) maps system requests to three constrained actions (AMB/LOC/UNA) before generating responses. On USERSIM-GUARD (2,100 labeled questions), this reduces UNA failure rates from 67.4% (baseline) to 2.7% (Figure 6). Human alignment improves substantially: GPT-4o with function calling achieves Pearson r=0.84 (p=0.02) vs. 0.61 without (p=0.14) (Table 3). This directly supports the claim that the simulator enables fair, realistic end-to-end evaluation.

2. **Two complementary evaluation settings reveal distinct model-specific deficiencies.** The *c*-Interact (protocol-guided) and *a*-Interact (agentic) settings (Section 4) expose divergent model behaviors. GPT-5 achieves 14.50% SR in *c*-Interact but 29.17% in *a*-Interact — the largest gap among all tested models (Table 2). This demonstrates that the benchmark isolates communication capability from SQL generation skill, which static-transcript benchmarks (e.g., CoSQL) cannot support.

3. **Memory grafting experiment isolates communication as the bottleneck.** By supplying GPT-5 with interaction histories from O3-mini, its success rate jumps from 13.8% to 20.5% (Figure 5), while providing the same histories to the original better model yields no gain. This cleanly demonstrates that the benchmark's difficulty stems from interactive dialogue strategy, not SQL generation ability.

4. **Challenging task suite over the full CRUD spectrum with state-dependent follow-ups.** The benchmark covers 410 BI and 190 DM tasks (Table 1), with each task containing ambiguous priority sub-tasks and follow-ups that depend on intermediate database state. The strongest model reaches only 17% end-to-end success in *a*-Interact, confirming the difficulty gap relative to single-turn or static multi-turn benchmarks.

## Weaknesses

### Major
None.

### Minor
1. **Single-run evaluation limits precision of model comparisons.** All success rates are based on a single run per model (temperature=0, line 177), acknowledged due to cost. While the broad ordering is reliable, differences between close models (e.g., O3-Mini vs. Gemini-2.5-Pro in *a*-Interact follow-ups: 8.50% vs. 10.33%) and debugging increments as small as 0.24 percentage points are within noise. The standard error of a binomial proportion at ~17% on 600 tasks is ~1.5pp. The paper does not discuss variance or provide confidence intervals. Bootstrapped estimates over the task set would strengthen the quantitative claims without requiring additional API calls. This is a common limitation in LLM evaluation but should be acknowledged more transparently.

2. **No quantitative model-level comparison against existing interactive benchmarks (CoSQL, SParC).** The paper convincingly argues that existing benchmarks use static transcripts and SELECT-only scopes (Section 1), and Appendix E provides a dataset-level comparison. However, running the same models on CoSQL or SParC would concretely demonstrate that BIRD-INTERACT captures a *different* or *harder* evaluation. Without this, the reader must rely on argumentation alone to assess how incremental the contribution is relative to adding a user simulator to existing tasks. The human alignment study (Table 3) validates simulator realism but not comparative task difficulty.

3. **Cost multiplier justification for *a*-Interact action space is incomplete.** The 9 actions are enumerated (Section 4.2), and cost multipliers are shown in Figure 3. Models overuse *submit* and *ask* (60.87% of actions), attributed to "pre-training bias" toward trial-and-error. However, if low-cost actions like *Retrieve Knowledge* are available, the paper does not ablate whether the cost structure itself incentivizes non-exploratory behavior. Without an experiment equalizing all action costs, the "pre-training bias" conclusion, while plausible, is not uniquely supported.

4. **ITS analysis is limited by model coverage.** Figure 4 shows only 4 of the 7 models; Qwen-3 exhibits flat or non-monotonic trends. The "ITS Law" is defined as a property a model *can* satisfy (Section 5.2), but the evidence for it as a general phenomenon is limited. The paper appropriately focuses on Claude-3.7-Sonnet as the clearest example, but the framing could be tempered.

### Trivial
- The budget formula $B = B_{\text{base}} + 2m_{\text{amb}} + 2\lambda_{\text{pat}}$ uses a factor of 2 without explicit justification in the main text.
- The "Idealized Performance" line in Figure 4 would benefit from a clearer caption specifying whether it is human expert performance or the best model's single-turn score.
- The debugging reward penalty (reward=0.7) is only shown in Figure 3 but not stated in the text of Section 4.1.

## Nice-to-Haves
- **Per-category breakdown by ambiguity type** (superficial, knowledge, environmental) would deepen behavioral analysis and guide future method development.
- **Action distribution table** (all 9 actions per model) in the main text would strengthen the *a*-Interact behavior analysis, which currently reports aggregate percentages for only two actions.
- **Free-mode experiments** (mentioned in Future Work, Section 8) would complement the stress-mode results and clarify whether budget constraints drive observed behaviors.

## Removed Points

- **"600 tasks selected from 900" confusion**: The paper clearly states FULL has 600 tasks and LITE has 300 tasks (Table 1, line 117). This reflects a misreading of the paper.
- **ITS Law overclaim**: The paper defines the law as a property a model *can* satisfy and only claims Claude-3.7-Sonnet "exhibits clear scaling behavior" (Section 5.2). The criticism that the paper claims this as a universal property is not supported by the text.
- **Missing debugging reward details**: The reward penalty (0.7) is shown in Figure 3 and referenced in the text ("details can be found in Figure 3," Section 4.1). The paper addresses this.
- **LITE results not in main text**: Per the instructions, do not penalize for content moved to appendix (parser strips appendices from all papers).
- **Reproducibility nits about hyperparameters**: Temperature=0 and top_p=1 are stated; reasoning model defaults are acknowledged. This is standard practice.
- **Missing related works**: Cannot be verified without external sources.
- **Formatting/style concerns**: Parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The harsh critic and strength finder both surface the same key findings: the function-driven user simulator is well-validated, the memory grafting experiment is a clean isolation of the interaction bottleneck, and the gap between c-Interact and a-Interact performance reveals model-specific communication deficiencies. No reviewer identified an unrecognized limitation or a surprising implication that the authors themselves had not considered.

## Suggestions

1. Report bootstrapped 95% confidence intervals for the main success rates by resampling the task set. This addresses the single-run concern without additional API expenditure.
2. Run the same agent/prompt setup on CoSQL (or report comparable published numbers) to quantify how much harder BIRD-INTERACT is than the closest existing benchmark.
3. Add an ablation in *a*-Interact where all actions have equal cost, to separate pre-training bias from cost-driven behavior in the action distribution analysis.
4. Include a table of all 9 action frequencies per model in Section 5.2 to support the trial-and-error bias conclusion.

## Score and Decision

**Calibration summary** (all anchors retrieved across rounds):

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Octopus | BdlIQGetYv.md | 2.50 | R1 (weak) | Much weaker — auto-generated, quality issues, withdrawn |
| ConDABench | jOxfpsnDFo.md | 2.50 | R1 (weak) | Much weaker — smaller scale, interactive DA, withdrawn |
| SQLAgent | voLoLHms2K.md | 3.33 | R1 (weak) | Weaker — method paper with shallow baselines, withdrawn |
| BIRD-Ent | gXkIkSN2Ha.md | 3.60 | R1 (weak) | Weaker — synthetic enterprise, concerns about quality, withdrawn |
| EHR-ChatQA | hLweUPBz7k.md | 4.00 | R1 (mid) | Weaker — smaller scale (64 AdaptQA instances), accepted poster |
| KnowMT-Bench | 66v0c2oOHK.md | 4.80 | R2 (narrow) | Weaker — template-based, smaller, rejected |
| ATAD | 9HacBDFOjt.md | 5.00 | R2 (narrow) | Weaker — single task family, accepted poster |
| DAComp | EtzJy9yI5J.md | 5.33 | R2 (narrow) | Comparable — broader scope but less user simulator validation, poster |
| VitaBench | rtcX9qOBaz.md | 5.50 | R2 (narrow) | Comparable — similar tier, more scenarios but less validation, poster |
| AMemGym | sfrVLzsmlf.md | 6.00 | R2 (narrow) | Slightly stronger — interactive memory benchmark, poster |
| LLMs Get Lost… | VKGTGGcwl6.md | 8.00 | R1 (strong) | Stronger — novel finding about multi-turn degradation, Oral |
| Gaia2 | 9gw03JpKK4.md | 8.00 | R1 (strong) | Stronger — broader agent benchmark with dynamic environments, Oral |

**Round-1 bracket**: The paper sits clearly above the weak band (2–3.6) and below the strong band (7.5+), placing it in the [4.5, 7.0] range.

**Round-2 narrowing**: Comparing against VitaBench (5.50, poster) and DAComp (5.33, poster) — both accepted benchmarks with similar rigor — BIRD-INTERACT has larger task scale (600 vs 100/210), more thorough user simulator validation (USERSIM-GUARD + human alignment study), and cleaner empirical insights (memory grafting, ITS analysis). Its main weaknesses (single-run evaluation, missing model-level comparison to existing benchmarks) are addressable and do not undermine the core contribution. This places it at the high end of the comparable-anchor cluster, slightly above VitaBench and AMemGym.

**Final score: 6.0**

The paper represents a solid, well-constructed benchmark contribution with a validated user simulator, informative empirical findings, and clear practical value. The weaknesses are real but manageable — no fatal flaw threatens the core claims. The paper is clearly above the acceptance threshold.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
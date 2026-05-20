Now I have all the information I need. Let me synthesize the final review.

## Summary

BIRD-INTERACT re-imagines text-to-SQL evaluation by shifting from single-turn, static benchmarks to a dynamic interactive environment. The paper contributes: (1) a function-driven user simulator that prevents ground-truth leakage (2.7% failure rate on unanswerable questions vs. 67.4% for baselines), (2) two evaluation settings (protocol-guided *c*-Interact and autonomous *a*-Interact) with budget-constrained awareness, and (3) 900 interactive tasks covering the full CRUD spectrum, each with ambiguity injection and state-dependent follow-up sub-tasks. The strongest model (GPT-5) achieves only 8.67% success in *c*-Interact and 17.00% in *a*-Interact, demonstrating a large gap between SQL generation and strategic interaction abilities.

## Strengths

- **Novel function-driven user simulator that demonstrably solves the ground-truth leakage problem.** The two-stage approach (action classification → response generation) is a principled solution to a well-known weakness of LLM-as-user approaches. The USERSIM-GUARD evaluation (2,100 expert-labeled questions) is rigorous: the function-driven approach cuts UNA failure rates from 67.4% to 2.7% (Figure 6).

- **First interactive text-to-SQL benchmark covering the full CRUD spectrum.** While prior work (COSQL, SParC, MINT) restricts to SELECT-only queries, BIRD-INTERACT includes 190 DM tasks (INSERT, UPDATE, DELETE, DDL) in the full set (Table 1). This is essential for production-grade database assistants and meaningfully broadens evaluation scope.

- **The benchmark is genuinely challenging and reveals concrete insights about LLM interaction strategies.** Even the best models score ≤25.52% normalized reward (Table 2). The memory grafting experiment (Figure 5) cleanly isolates communication strategy as the bottleneck for GPT-5, and the action-distribution analysis shows models systematically prefer costly trial-and-error over strategic exploration.

- **Dual evaluation settings with budget constraints are well-designed.** *c*-Interact and *a*-Interact capture distinct real-world deployment scenarios (conversational assistant vs. autonomous agent). The budget mechanism with user-patience parameterization enables stress-testing. The finding that models exhibit different relative strengths across the two modes (GPT-5: worst in *c*-Interact, best in *a*-Interact) is a genuine empirical discovery.

- **Human alignment validation on the simulator.** The Pearson correlation of 0.84 (p=0.02) between the function-driven GPT-4o simulator and human users (Table 3), versus 0.61 (p=0.14) for the baseline, provides credible evidence that the simulator captures realistic interaction patterns.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core contributions are valid and supported by evidence.

### Minor

- **The Interaction Test-Time Scaling (ITS) "law" is overclaimed.** The paper defines the ITS Law as reaching or surpassing idealized single-turn performance given enough turns, but no model actually achieves this in either setting (Figure 4). In *a*-Interact, several models show flat or decreasing performance with more patience, directly contradicting the claimed scaling. The observation that Claude-3.7-Sonnet improves with more turns in *c*-Interact is interesting and worth reporting, but calling it a "law" and framing it as a general phenomenon is not supported by the data. This should be downgraded to "ITS observation" or "ITS trend" with appropriate caveats.

- **The claim that ambiguous queries are "unsolvable without clarification" is asserted but not experimentally verified.** The paper states this as a quality-control property (Section 3.2), but no ablation experiment demonstrates that models fail at chance on the ambiguous queries when prohibited from interaction. Such an experiment would directly support the benchmark's central premise. (The paper does show low absolute success rates, but without an interaction-free baseline, one cannot attribute the difficulty specifically to the need for interaction.)

- **The human-correlation study for the user simulator is limited in scale and reporting.** The study uses only 100 tasks (of 900) and lacks detailed protocol description in the main text (budget constraints, allowed responses, annotation guidelines). While the 0.84 correlation is encouraging, this is a modest basis for the claim of "high-fidelity" simulation. The paper does not report confidence intervals or discuss cases where simulator and human judgments diverge.

- **The memory grafting experiment has a confound.** GPT-5's improvement when given interaction histories from Qwen-3-Coder and O3-mini could reflect not just better interaction strategy but simply having a longer or different context. The "without grafting" baseline is GPT-5's own (worst) performance, so improvement from any external history is expected. An ablation where GPT-5 receives its own successful interaction histories (when available) would better isolate the communication-deficiency hypothesis.

- **Single-run evaluations limit reliability.** The paper acknowledges this (Section 5), but with narrow margins between some models (e.g., 16.33% vs. 15.83% follow-up SR in *c*-Interact between Gemini-2.5-Pro and O3-Mini), variance is a concern for model rankings.

### Trivial

- The main text lacks concrete worked examples demonstrating state-dependency in follow-up sub-tasks (e.g., how INSERT modifies the database state and how the follow-up depends on it). A short illustrative example would strengthen the exposition.
- No confidence intervals are reported for the human-correlation coefficients in Table 3.

## Nice-to-Haves

- Include an explicit ablation where models are forced to solve ambiguous queries without any interaction (patience=0 and no clarification allowed) to verify the "unsolvable without clarification" claim.
- Report action costs used in *a*-Interact more prominently in the main text (currently deferred to Appendix J).
- Add multiple runs (e.g., 3) for a subset of models and budget settings to assess the stability of rankings.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"Reward weights (70/30) justified only in appendix"** — Removed per rule about missing appendix content; the parser strips appendices from all papers.
2. **"Action costs not reported in main text"** — Removed per rule about missing appendix content; the paper points to Appendix J for details.
3. **"Budget constraint justification is heuristic"** — Removed because it is a normal design choice for benchmarks; most benchmark design parameters are heuristic and this is not a weakness.
4. **"Claim of restoring missing realism overstates"** — Removed as a subjective opinion; the paper's claims about realism are appropriately scoped.
5. **"State-dependency claim weak without concrete examples"** — Removed as a formatting/stylistic preference; the paper's description is adequate for the main text (Appendix H.5 presumably contains the taxonomy).

## Novel Insights

The reviews surface a tension that the paper does not fully resolve: the user simulator is simultaneously the paper's strongest technical contribution (demonstrably preventing ground-truth leakage) and the source of its most persistent validity concern (whether simulated interactions reflect real user behavior). This tension is inherent to the task — avoiding human-in-the-loop evaluation while maintaining ecological validity — and BIRD-INTERACT makes an unusually systematic attempt to address both sides, but the evidential gap between the two remains the salient issue for future work building on this benchmark.

## Suggestions

1. Downgrade the "ITS Law" to a more measured claim (e.g., "ITS observation" or "ITS trend") and explicitly note that no model reaches the idealized single-turn baseline in the tested range.
2. Run an interaction-free ablation on a subset of ambiguous tasks to verify the "unsolvable without clarification" premise. Even 50 tasks would significantly strengthen the paper's central claim.
3. Expand the human-correlation study to at least 200 tasks and report confidence intervals and qualitative divergence examples.
4. Add a short illustrative example of state-dependent follow-up sub-tasks in the main text (can be a footnote or callout box).

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/BdlIQGetYv.md` (Octopus) | 2.50 | Auto-generated text-to-SQL benchmark without human validation. BIRD-INTERACT is significantly stronger — it has real human annotation, validated simulator, and genuine methodological novelty. |
| `/home/wg25r/review_agent/human_reviews_2026/hxEHr5gJBY.md` (TQA-Bench) | 4.00 | Multi-table QA benchmark. BIRD-INTERACT has comparable scale but more methodological innovation (interactive framework, user simulator design). |
| `/home/wg25r/review_agent/human_reviews_2026/hLweUPBz7k.md` (EHR-ChatQA) | 4.00 | Interactive database QA benchmark in the EHR domain — closest genre match. BIRD-INTERACT is larger (900 vs. small task count), covers CRUD vs. SELECT-only, has more rigorous simulator validation (2,100-question USERSIM-GUARD). |
| `/home/wg25r/review_agent/human_reviews_2026/gXkIkSN2Ha.md` (BIRD-Ent) | 3.60 | Enterprise extension of BIRD. BIRD-INTERACT introduces a fundamentally new evaluation paradigm (interaction) rather than scaling an existing one. |
| `/home/wg25r/review_agent/human_reviews_2026/UAUimofy3W.md` (Non-Collab User Sim) | 4.67 | User simulator for tool agents — comparable focus on simulation quality. BIRD-INTERACT has broader benchmark scope and more rigorous simulator evaluation. |
| `/home/wg25r/review_agent/human_reviews_2026/EtzJy9yI5J.md` (DAComp) | 5.33 | Broad data agent lifecycle benchmark with strong reviewer support (one 8). BIRD-INTERACT is comparable in quality, slightly narrower in scope but with a more novel interaction paradigm. |
| `/home/wg25r/review_agent/human_reviews_2026/PL51SpN6ZJ.md` (SimBench) | 6.00 | High-quality behavioral simulation benchmark with 20 diverse datasets. BIRD-INTERACT has less comprehensive validation but comparable methodological rigor within its domain. |

**Score rationale:** BIRD-INTERACT clearly outperforms the cluster of text-to-SQL benchmarks in the corpus (Octopus 2.50, TQA-Bench 4.00, BIRD-Ent 3.60). It is stronger than the closest comparable interactive database benchmark (EHR-ChatQA 4.00) due to its larger scale, CRUD coverage, and more rigorous simulator evaluation. It is comparable to DAComp (5.33) — both make genuine benchmark contributions with well-designed evaluations and actionable empirical findings. It is slightly weaker than SimBench (6.00) in terms of validation breadth. Minor weaknesses (overclaimed ITS "law," missing interaction-free ablation, modest human study scale) prevent it from reaching the 6+ tier, but the core contributions are solid and empirically grounded.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>
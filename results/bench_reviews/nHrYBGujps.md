Now I have a thorough understanding of both the paper and the calibration anchors. Let me write the consolidated review.

## Summary

BIRD-INTERACT introduces a benchmark for interactive text-to-SQL evaluation that couples databases with a hierarchical knowledge base and a function-driven user simulator, supporting both protocol-guided conversational (_c_-Interact) and agentic (_a_-Interact) evaluation settings across 900 tasks (600 FULL, 300 LITE) spanning full CRUD operations. The key innovation is a two-stage function-driven user simulator that maps model questions to constrained symbolic actions (AMB/LOC/UNA) before generating responses, dramatically reducing ground-truth leakage compared to naive LLM-based simulators. The benchmark reveals that even GPT-5 completes only 8.67% (_c_-Interact) and 17.00% (_a_-Interact) of tasks end-to-end, with further analysis through memory grafting and interaction test-time scaling isolating communication strategy as a decisive factor beyond raw SQL generation ability.

## Strengths

- **Function-driven user simulator eliminates information leakage with strong empirical evidence**: The two-stage simulator reduces failure rates on unanswerable (UNA) questions from up to 67.4% for baseline simulators to as low as 2.7% (Figure 6, USERSIM-GUARD benchmark of 2,100 questions). This is a principled methodological contribution to interactive evaluation that directly addresses a known weakness of LLM-based simulators.

- **Memory grafting experiment cleanly isolates interaction skill from SQL generation ability**: When GPT-5 receives clarification histories from better-communicating models (Qwen-3-Coder, O3-mini), its success rate improves significantly (Figure 5). This provides direct causal evidence that the benchmark measures interactive communication as a capability separable from raw SQL generation — a key validation of the benchmark's design.

- **Task suite covers the full CRUD spectrum with state-dependent follow-ups**: Unlike prior benchmarks limited to SELECT-only queries, BIRD-INTERACT includes Data Management tasks (INSERT, UPDATE, DELETE, ALTER) verified by executable test cases that assert database postconditions (Appendix G.2), and introduces genuine state dependency where follow-up sub-tasks require reasoning over modified database states or newly created objects.

- **Interaction Test-Time Scaling validates the benchmark's sensitivity**: Figure 4 demonstrates that several models improve monotonically with increasing interaction turns on the LITE set, with an "Idealized" single-turn baseline showing substantially higher performance — confirming the benchmark measures strategic information gain and not merely single-turn query quality.

- **Rigorous human annotation with strong quality control**: The benchmark construction involved 12 expert annotators through a multi-stage selection process (90% qualification exam threshold), double-blind annotation for USERSIM-GUARD (Fleiss' Kappa 0.93), and human evaluation of 300 randomly sampled data points achieving 97.3% overall acceptance rate (98.7% for SQL correctness, 95.3% for ambiguity annotation quality).

## Weaknesses

### Fatal

None.

### Major

- **Missing single-turn unambiguous baseline on BIRD-INTERACT-FULL limits interpretation of headline results**: The paper's abstract and introduction prominently cite the 8.67% and 17.00% task completion rates to argue that interaction is the critical bottleneck. However, no corresponding success rate is reported for the FULL task suite when all ambiguities are resolved upfront (i.e., the original unambiguous single-turn setting from which tasks were derived). Figure 4 provides this "Idealized" baseline for the LITE set, but its absence for the FULL set means the contribution of interaction difficulty versus inherent SQL complexity cannot be disentangled for the headline numbers. If the single-turn baseline on FULL were also low, the primary framing — that interaction is the principal bottleneck — would need substantial qualification. This is addressable with additional experiments and does not invalidate the benchmark design, but it currently makes the central empirical claim less conclusive than presented.

### Minor

- **Human-alignment correlation study is underpowered (n=7 models)**: Table 3 reports Pearson correlations between system-model success rates under human users versus simulators, using only 7 data points. Correlations on such a small sample are inherently unstable, and the reported p-values (e.g., p=0.02, p=0.03) are unreliable for inference at this sample size. The paper's stronger evidence for simulator quality comes from the USERSIM-GUARD evaluation (Figure 6, Table 11), which is far more convincing. The correlation study is a supplementary validation that currently overstates its statistical reliability. This does not threaten the core contribution but the authors should either expand the study or appropriately caveat the statistical claims.

- **Base budget for _a_-Interact lacks justification or sensitivity analysis**: The _a_-Interact evaluation uses a fixed base budget of 6 with λ_pat=3 throughout. While the ITS experiment (Figure 4) varies patience for the LITE set, the base budget itself is never varied. Different budget regimes could shift action-distribution patterns and model rankings. The paper's inferences about model behavior (e.g., bias toward trial-and-error over exploration) may not generalize across budget levels. This is a methodological gap that limits confidence in the action-distribution analysis but does not undermine the benchmark's core value.

### Trivial

- None.

## Nice-to-Haves

- **Zero-patience (no clarification) condition on FULL**: Would directly validate that ambiguous queries are genuinely unsolvable without interaction, strengthening the benchmark's necessity claim beyond annotator agreement.

- **Error classification beyond the 50-case sample**: A coarser automated analysis of all failure trajectories (e.g., did the model ask any clarification? was the submission syntactically valid?) would enrich diagnostic value.

- **Free-mode evaluation without budget constraints**: The paper itself proposes this in Section 8 (Future Work). Including preliminary results would provide contrast to the stress-mode findings and is a natural extension.

## Removed Points

These points were flagged for removal; treat them with caution.

- **"Reliance on LIVESQLBENCH may introduce artifacts"** (from Harsh Critic, Section-by-Section Notes, Section 3): The paper explicitly acknowledges building on LIVESQLBENCH and describes the conversion process in detail. The concern about artifacts is speculative and not grounded in any observed evidence. The paper's quality control process (necessity checks, recoverability after clarification) directly addresses conversion quality. Removed as unsubstantiated.

- **"The claim that ambiguous queries are unsolvable without clarification is not supported by quantitative verification"** (from Harsh Critic): This is partially addressed by the annotation protocol (Appendix H.1: "each ambiguous query must be unsolvable without clarification") and is essentially a design constraint enforced during annotation. I've moved a version of this to Nice-to-Haves as a zero-patience condition suggestion.

- **"Performance on different ambiguity types not systematically broken down"** (from Harsh Critic, Deeper Analysis): Appendix K (Figures 14, 15) does break down performance by ambiguity type and by linear vs. higher-order knowledge chain breaking. This concern is factually incorrect — the analysis exists. Removed.

- **"GPT-5's poor c-Interact performance may stem from deficiency in interactive communication abilities" — speculative claim** (implied in Harsh Critic): The memory grafting experiment (Figure 5) directly tests and supports this hypothesis. The paper does not overclaim; it states this as a hypothesis and tests it. Removed.

- **Strength Finder claims about "problem importance"**: The generic claim that "this paper addressed an important problem" is superficial. Removed as it lacks specific evidence and is a subjective judgment.

## Novel Insights

The memory grafting experiment (Figure 5) reveals something genuinely non-obvious: GPT-5 — the strongest model on many benchmarks — underperforms specifically because of poor communication strategy, not weak SQL skills. Feeding it better interaction histories from weaker-overall models substantially boosts its success rate. This suggests that interactive text-to-SQL may require capabilities (strategic questioning, multi-turn reasoning about what to ask next) that are orthogonal to the generation capabilities measured by single-turn benchmarks, and that these capabilities do not necessarily correlate with model scale or general reasoning ability. This has implications beyond this paper for how we evaluate and improve LLMs for collaborative tasks.

## Suggestions

- Add a single-turn unambiguous baseline on BIRD-INTERACT-FULL. This is the most impactful addition: it would directly quantify how much of the difficulty comes from interaction versus inherent SQL complexity, making the paper's central empirical claim fully substantiated. The experiment is straightforward to run — evaluate the same models on the original LIVESQLBENCH tasks from which the interactive tasks were derived.

- Expand the human-alignment study beyond 7 models (e.g., by using per-task correlations across the 100 sampled tasks for each model) or appropriately caveat the current results as preliminary and supplementary to the USERSIM-GUARD evaluation.

- Provide at least one alternative base-budget level for _a_-Interact (e.g., 4 or 8) to assess whether action-distribution patterns and model rankings are stable.

- Consider whether any of the recommendations in the "Nice-to-Haves" section are feasible to add within the rebuttal period.

## Score and Decision

**Calibration anchor comparison:**

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| Octopus (BdlIQGetYv) | 2.50 | Clearly inferior — auto-generated data without human validation, no principled user simulator, major quality concerns |
| EHR-ChatQA (hLweUPBz7k) | 4.00 | Weaker — similar interactive DB QA concept but smaller scale, simpler LLM-based simulator without function-driven safeguards, less rigorous human validation |
| VitaBench (rtcX9qOBaz) | 5.50 | Comparable — similar ambition as an interactive agent benchmark with user simulator; BIRD-INTERACT has a stronger simulator methodology (function-driven) and more rigorous human validation, but VitaBench has broader domain coverage; the missing single-turn baseline on FULL is BIRD-INTERACT's most notable gap relative to this tier |
| LearNAT (q6kXd8Gpfj) | 6.00 | Different category (method paper, not benchmark); not directly comparable |
| SPARTA (8KE9qvKhM4) | 5.00 | Roughly comparable quality and ambition; BIRD-INTERACT has a more novel simulator design |
| BIRD-Ent (gXkIkSN2Ha) | 3.60 | Weaker — narrower contribution |

BIRD-INTERACT sits between EHR-ChatQA (4.00) and VitaBench (5.50). It is substantially stronger than EHR-ChatQA due to the principled function-driven simulator design, the USERSIM-GUARD evaluation, the CRUD coverage, and the rigorous human quality control. It is comparable to VitaBench in ambition and execution, exchanging VitaBench's broader domain coverage for a more methodologically sound simulator. The missing single-turn baseline on FULL is the primary factor keeping it from the higher tier — this is an addressable gap that does not invalidate the benchmark but currently leaves the headline claims less fully supported than they could be.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
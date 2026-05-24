Now I have sufficient calibration data. Here is my final consolidated review:

---

## Summary

BIRD-INTERACT introduces a benchmark for evaluating LLMs on interactive text-to-SQL tasks through dynamic multi-turn interactions, replacing the static conversation transcripts used in prior benchmarks. The benchmark contributes (1) a function-driven user simulator that prevents ground-truth leakage, validated to align with human behavior (Pearson 0.84), (2) two evaluation settings—conversational (*c*-Interact) and agentic (*a*-Interact)—that probe distinct model capabilities, and (3) 900 challenging tasks covering the full CRUD spectrum with ambiguity injection, state-dependent follow-up sub-tasks, and budget-constrained evaluation. Experiments show that even the strongest models (GPT-5, Gemini-2.5-Pro) achieve low success rates (≤29%), and diagnostic analyses (memory grafting, interaction test-time scaling) reveal that communication skill, not SQL ability, is often the bottleneck.

---

## Strengths

- **Function-driven user simulator with strong empirical validation.** The two-stage mechanism (Section 3.3) that maps system requests to constrained symbolic actions (`AMB()`, `LOC()`, `UNA()`) before generating responses demonstrably prevents ground-truth leakage: on the USERSIM-GUARD dataset (2,100 questions), it reduces failure rates on Unanswerable questions from 67.4% (baseline) to as low as 2.7% (Figure 6). Human alignment is also strong—Pearson 0.84 (p=0.02) between the function-driven simulator and human experts across 100 tasks (Table 3), compared to 0.61 for the baseline. This addresses a recognized weakness of LLM-as-simulator approaches.

- **Comprehensive CRUD task suite with state dependency.** Unlike prior multi-turn benchmarks (COSQL, SParC) limited to SELECT queries, BIRD-INTERACT covers Create, Read, Update, and Delete operations (190 DM + 410 BI tasks in FULL). Follow-up sub-tasks depend on modified database states from preceding queries (Section 3.2), a realistic property absent from existing datasets. Inter-annotator agreement >93% (Table 1) confirms annotation quality.

- **Two evaluation settings reveal distinct model capabilities.** The *c*-Interact (protocol-guided conversation) and *a*-Interact (autonomous agentic) settings produce qualitatively different model rankings (Table 2). GPT-5 is worst in *c*-Interact (14.50% SR) but best in *a*-Interact (29.17% SR), demonstrating that the benchmark isolates communication effectiveness from autonomous planning—a capability not offered by static-history benchmarks. This duality is a genuine design contribution.

- **Memory grafting experiment cleanly isolates communication from SQL ability.** Providing GPT-5 with interaction histories from Qwen-3-Coder and O3-Mini improves its success rate from 13.8% to 18.8% and 20.5% respectively (Figure 5). This diagnostic experiment provides unique evidence that interaction strategy, not SQL generation capability, is the limiting factor—a finding with clear implications for future system design.

- **Interaction Test-Time Scaling (ITS) finding.** Figure 4 shows monotonic improvement with increasing user patience for several models in *c*-Interact, with Claude-3.7-Sonnet able to match or exceed its idealized single-turn performance given sufficient turns. This is a novel empirical observation about how models benefit from interaction opportunities.

---

## Weaknesses

### Major
None.

### Minor

- **Single-run evaluation limits fine-grained model comparison.** The paper notes it conducts "single runs due to cost" (Section 5) with temperature=0. While temperature=0 makes model outputs deterministic, the user simulator and interaction dynamics may introduce variability. Many pairwise differences in Table 2 are small (e.g., Gemini-2.5-Pro vs O3-Mini on *c*-Interact reward: 20.92 vs 20.27), and without variance estimates it is unclear which differences are meaningful. This is a common limitation in benchmark papers, but for a leaderboard-intended benchmark the authors should at minimum discuss the expected impact of variance or provide a repeatability study on a subset.

- **"ITS Law" overstates the evidence.** The claim of an "ITS Law" (Section 5.2) is based on four models and three patience levels on LITE. While the scaling trend is a legitimate and interesting observation, describing it as a "law" implies a generality that the data do not support. The paper would be more credible presenting this as an observed scaling pattern and noting that it may not generalize to all models or budget regimes.

- **Clarity of the *c*-Interact action space could be sharper.** Section 4.1 describes *c*-Interact as a dialogue between system and user simulator where the system "may engage in clarification dialogue before generating SQL" with a "single debugging opportunity." Section 4.2 describes *a*-Interact with "9 discrete actions" and direct tool access. However, Figure 3(b) lists system actions (Retrieve Knowledge, Execute SQL, etc.) that appear above both settings, and it is not fully explicit whether the *c*-Interact system can autonomously invoke tools like schema retrieval or SQL execution, or whether all environment queries must go through the user simulator. The distinction is largely inferable but stating it explicitly would prevent misinterpretation.

- **User simulator derives clarifications from ground-truth SQL.** Although the two-stage function-driven approach prevents direct leakage, the `AMB()` and `LOC()` actions ultimately generate responses using the annotated GT SQL as a "clarification source" (Section 3.3). The paper partially addresses this through the human correlation study, but it remains an inherent limitation of simulator-based evaluation: the simulator is more cooperative and precise than a real user might be. A brief explicit acknowledgment of this caveat in the conclusion would strengthen the paper's scientific framing.

### Trivial
- The paper uses "sub-task 1" and "follow-up sub-task" terminology but sometimes refers to them as "priority sub-task" and "follow-up sub-task" interchangeably. Consistent naming would improve readability.

---

## Nice-to-Haves
- **Extend the non-interactive baseline to a subset of FULL tasks.** The paper already provides an "idealized" single-turn comparison on LITE (Figure 4), which convincingly demonstrates that performance drops under interaction. Extending this to a random subset of FULL tasks would provide even stronger evidence that difficulty stems from interaction rather than SQL complexity, but this is not necessary for the paper's core claims.
- **A small taxonomy of failure modes** (e.g., asking irrelevant questions vs. failing to ask the right ones vs. misinterpreting feedback) from the LITE set would add analytical depth.
- **Qualitative side-by-side examples** comparing AI-simulator and human-simulator interactions would help readers assess the simulator's realism beyond the correlation statistic.

---

## Removed Points

These points were removed with justification:

1. **"Missing direct evidence that the benchmark specifically tests *interaction* rather than just hard SQL tasks"** (from Harsh Critic). The paper already provides direct evidence: Figure 4 compares interactive vs. idealized (non-interactive) performance on LITE across four models, and the memory grafting experiment (Figure 5) provides converging evidence. The request to extend this to FULL is a scope-creep nice-to-have, not a genuine weakness.

2. **"Normalized Reward is defined by reference to Appendix F, which is not present"** (from Harsh Critic). Appendix F is stripped by the parser; it exists in the original submission. Not a paper weakness.

3. **"Could briefly discuss other interactive benchmarks like WebArena or SWE-bench"** (from Harsh Critic). Missing related works that the reviewer does not know exist cannot be a weakness. The paper's related work section adequately covers the relevant text-to-SQL and interactive benchmark literature.

4. **"Reproducibility concerns about undisclosed hyperparameters, prompt engineering, temperature settings"** (from Harsh Critic). The paper states temperature=0, top_p=1, default reasoning settings, and refers to appendices. Temperature=0 is standard for deterministic evaluation; demanding full prompt text in the main body is not standard practice.

5. **Strength Finder claim about "ITS finding" being a central strength**: This is a legitimate observation but overstated—it is more of a supporting finding than a core contribution. Demoted to supporting rather than core strength in the merged review.

---

## Novel Insights

None beyond the paper's own contributions. The key analytical insight that emerges across the reviews is that the memory grafting experiment (Figure 5) is a particularly elegant diagnostic: by showing that GPT-5 with another model's interaction history outperforms native GPT-5, the paper cleanly decouples SQL competence from interaction skill in a way that few prior benchmarks enable. This design pattern (grafting histories across models) could be adopted more broadly in interactive benchmarks.

---

## Suggestions

1. **Add variance estimates on a subset.** Run 3–5 trials of 2–3 models on LITE to quantify run-to-run variability, report mean ± std, and discuss how this affects interpretation of the FULL results. This would address the single-run concern without the cost of re-running the entire benchmark.

2. **Soft-pedal the "ITS Law" terminology.** Frame the scaling finding as an "observed scaling behavior" or "ITS pattern" and note that it is established on a limited set of models and patience levels. The empirical observation is interesting on its own terms.

3. **Explicitly clarify the *c*-Interact action affordances in Section 4.1.** State whether the system has access to schema retrieval, knowledge base queries, and direct SQL execution in *c*-Interact, or whether all such queries must go through the user simulator.

4. **Add a limitations paragraph at the end** that briefly discusses (a) the GT-SQL-derived nature of simulator clarifications, (b) the single-run evaluation, and (c) the domain specificity of the benchmark to text-to-SQL (i.e., interaction patterns may differ in other domains).

5. **Consider adding a failure-mode taxonomy** from the LITE set to deepen the analysis of what models do wrong in interaction.

---

## Score and Decision

**Calibration Report:**

*Round 1 (Bracketing, score <3.5 / 3.5–7.5 / >7.5):*
- Weak anchors (≤3.40): Harnessing Wikipedia Graph for MEQA (3.40), Instruction Following Rethinking (3.00), Structure-Rich Text Benchmark (3.25), Pose-Driven Query (1.67)
- Middle anchors (3.5–7.5): **MINT** (6.75), **τ-bench** (6.50, read in full), **CityBench** (7.00, read in full), Lab Safety Benchmark (4.00)
- Strong anchors (>7.5): Cheating Automatic Benchmarks (7.75), BigCodeBench (9.00), Cybench (8.67), Training on Test Task (8.00)

*Initial bracket:* 5–8.

*Round 2 (Narrowing):*
- **τ-bench** (6.50, Accept) — Customer-service tool-agent benchmark with LLM-simulated users. BIRD-INTERACT's user simulator is more robustly validated (function-driven, Pearson 0.84 vs no comparable human validation in τ-bench) and its task suite (900 tasks, full CRUD) is larger and more diverse. BIRD-INTERACT is stronger.
- **MINT** (6.75, Accept) — General multi-turn interaction benchmark. BIRD-INTERACT provides domain-specific depth (text-to-SQL with knowledge bases, ambiguity injection, state dependency) that MINT lacks, and validates its user simulator against humans. Comparable or slightly stronger.
- **CityBench** (7.00, Reject) — Interactive simulator benchmark for urban tasks. Despite the 7.00 average, it was rejected due to shallow analysis and experimental design issues. BIRD-INTERACT does not share those flaws.
- **DiscoveryBench** (7.00, Accept) — Data-driven discovery benchmark. Less directly comparable (SQL isn't the focus) but in the same quality tier.

*Final calibration:* The paper sits between τ-bench (6.50) and DiscoveryBench (7.00). It is stronger than τ-bench due to the principled user simulator design and human validation, and comparable to DiscoveryBench in scope and rigor. The weaknesses identified are minor and addressable. I place it at 7.0—a solid benchmark contribution with well-supported claims and clear value to the community.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
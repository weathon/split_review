Now let me write my final, consolidated review.

## Summary
BIRD-INTERACT is a benchmark for evaluating LLMs on multi-turn, interactive text-to-SQL tasks. Built on LIVESQLBENCH, it features (1) a function-driven user simulator that prevents ground-truth leakage, (2) two evaluation settings (protocol-guided c-Interact and agentic a-Interact), and (3) 900 tasks spanning the full CRUD spectrum with controlled ambiguity injection. The paper benchmarks 7 frontier LLMs, finding that even GPT-5 achieves only 8.67% success in c-Interact and 17% in a-Interact, and uses a memory grafting experiment to demonstrate that interaction skill is a bottleneck separate from SQL generation capability.

## Strengths
1. **Function-driven user simulator with strong validation against ground-truth leakage.** The two-stage approach (Section 3.3) maps system queries to three allowed actions (AMB/LOC/UNA) before generating responses, validated on the USERSIM-GUARD dataset (2,100 expert-labeled questions, Section 6). The simulator reduces failure rates on Unanswerable questions from up to 67.4% (baseline) to 2.7% (Figure 6), and achieves 0.84 Pearson correlation with human users (p=0.02) versus 0.61 (p=0.14) for baselines (Table 3). This is a concrete methodological improvement over prior LLM-as-simulator approaches and is critical for the reliability of any interactive benchmark.

2. **Dual evaluation settings reveal non-obvious model behaviors.** The c-Interact vs. a-Interact settings (Section 4) surface mode-specific model rankings: GPT-5 goes from worst in c-Interact (14.50% SR) to best in a-Interact (29.17% SR), while Qwen-3-Coder shows the opposite pattern (22.00% vs. 13.33%). This demonstrates that interaction mode is a decisive factor — a finding invisible in any single-setting benchmark — and provides a useful framework for future interactive evaluation design.

3. **Memory grafting diagnostic experiment.** The experiment (Section 5.2, Figure 5) provides controlled evidence that the bottleneck in c-Interact is interaction strategy rather than SQL generation: GPT-5's success rate improves from 13.8% to 20.5% when given interaction histories from better-interacting models. This is a novel evaluation technique for interactive benchmarks.

4. **Systematic ambiguity injection with quality control.** The paper defines three categories of ambiguity (superficial query, knowledge, environmental) with a principled annotation process achieving 93%+ inter-annotator agreement (Table 1). Quality control ensures ambiguous queries are "unsolvable without clarification yet fully reconstructable once clarifications are provided" (Section 3.2), providing a replicable methodology.

5. **Coverage of full CRUD spectrum with state dependency.** Unlike prior interactive benchmarks (CoSQL, SParC) that are SELECT-only, BIRD-INTERACT includes both BI and DM operations (Table 1) with state-dependent follow-up sub-tasks requiring reasoning over modified database states.

## Weaknesses

### Fatal
None.

### Major
1. **No human performance baseline on the benchmark tasks themselves.** The paper claims BIRD-INTERACT "restores missing realism" and that tasks "can only be resolved through dynamic interaction," but provides no human performance data on its own tasks. While the user simulator is validated against humans (Table 3, on 100 tasks for correlation analysis), this validates the simulator, not the benchmark's solvability or difficulty calibration for humans. Without knowing whether human database experts would score 90%, 50%, or 20%, the very low absolute success rates (e.g., 8.67% for GPT-5 in c-Interact) are hard to interpret. This is a standard expectation for benchmark papers claiming to measure real-world task completion — WebArena (human baseline of 78.24%) provides an example of best practice in a closely related area.

2. **Single-run evaluation with no variance reporting.** The paper states (line 163) it conducted "single runs due to cost." For a benchmark whose purpose is to establish reliable model rankings, this is a significant limitation. Temperature=0 reduces LLM output stochasticity but does not eliminate variance from the interaction trajectory itself — a single differently-phrased clarification question can cascade into a different outcome. Several reported differences between models are small (e.g., 8.33% vs 8.50% vs 8.67% for three models on c-Interact follow-up SR in Table 2), and without variance estimates it is impossible to assess whether these differences are meaningful. The paper acknowledges this briefly but should discuss its implications more prominently.

### Minor
3. **The "ITS Law" is stated but not demonstrated.** Section 5.2 defines: "A model satisfies this law if, given enough interactive turns, its performance can match or even surpass that of the idealized single-turn task." However, no model in the reported results actually satisfies this — none reaches the idealized single-task performance line in Figure 4. Presenting this as a "law" without quantitative evidence that any model satisfies it is premature. The empirical observation that some models improve monotonically with more turns is valuable on its own and does not need the law framing.

4. **Memory grafting experiment conflates strategy and information.** The experiment gives GPT-5 the full interaction histories (both questions and answers) from better-performing models. The improvement could partly reflect GPT-5 gaining access to the clarified information from the answers, rather than learning a better questioning strategy. The paper's broad conclusion — that the bottleneck is in the interaction phase, not SQL generation — is still supported, but the claim about "interactive communication abilities" specifically would be stronger with an additional control (e.g., giving GPT-5 only the questions, not the answers received).

5. **No analysis of whether injected ambiguities read as natural user utterances.** Quality control ensures ambiguous queries are technically solvable with clarification, but there is no human evaluation (e.g., naturalness ratings) of whether the resulting ambiguous queries resemble real user utterances. This is relevant to the paper's "realism" framing.

6. **Ecological validity of ambiguity injection is undiscussed.** Every ambiguity is created by masking knowledge nodes or removing query details, paired with a ground-truth clarification source. This is a clean, controllable design, but the paper does not discuss how this artificial ambiguity structure relates to naturally-occurring ambiguity in database interactions (underspecified goals, domain terminology mismatches, implicit assumptions about business logic). An honest limitations discussion would strengthen the paper.

### Trivial
None.

## Nice-to-Haves
- An additional control condition for the memory grafting experiment: give GPT-5 only the questions (not answers) from better models, or give better models GPT-5's questions, to more cleanly separate interaction strategy from information gain.
- Variance estimates or multiple runs for at least a representative subset of tasks.
- Human naturalness ratings for a sample of injected ambiguous queries.
- More justification for the 70/30 priority/follow-up reward split.

## Removed Points
- **BI vs. DM contradiction (removed — factually wrong).** The harsh critic claimed the paper's statement that BI is "more challenging" than DM contradicts Table 2, where DM has higher SR. Higher SR means *easier*. The data uniformly shows BI SR < DM SR, confirming the paper's claim. This was a reviewer misreading.
- **"Static conversation transcripts" criticism (removed — the paper's design is fundamentally different from prior static-transcript approaches, as clearly explained in Section 1).**
- **Ground-truth leakage concern (removed — paper explicitly addresses this via the function-driven simulator, with empirical validation in Section 6).**
- **Reward structure justification (removed — scope-appropriate; the structure is clearly defined).**
- **Missing appendix/proofs concerns (removed — parser strips these).**
- **All formatting/style nitpicks (removed per instructions).**

## Novel Insights
The observation that different models have fundamentally different aptitude profiles across interaction modes (c-Interact vs. a-Interact) — and that these profiles can invert rankings — is genuinely novel and important for the design of interactive evaluation protocols. The finding that GPT-5, despite being the strongest model in a-Interact, is the worst in c-Interact, while Qwen-3-Coder shows the opposite pattern, suggests that interaction paradigms are not a mere implementation detail but a decisive evaluation dimension. The memory grafting methodology itself is a useful technique for future interactive benchmarks.

## Suggestions
1. **Add a human performance baseline** — have 3-5 database experts attempt a stratified sample of tasks.
2. **Report at minimum bootstrapped confidence intervals** for the main results, or run multiple trials on a subset of tasks.
3. **Add a control condition to the memory grafting experiment** where GPT-5 receives only the questions (not answers) from better models.
4. **Conduct a small human naturalness study** for the injected ambiguous queries.
5. **Tone down the "ITS Law" framing** — the empirical observation of scaling is valuable without naming it a law.
6. **Add a dedicated limitations section** discussing the artificial nature of ambiguity injection and the single-run limitation.

## Score and Decision

**Calibration anchors:**
- DB-GPT-Hub (3.75, R1): A text-to-SQL benchmarking framework. Significantly weaker — lacks methodological novelty, thin validation. BIRD-INTERACT is much stronger.
- τ-bench (6.50, R2): Interactive benchmark with LLM-as-user-simulator (tool-agent-user interaction). Most comparable anchor. τ-bench has cleaner execution but weaker simulator validation. BIRD-INTERACT is slightly below due to missing human baseline and single-run issues.
- WebArena (6.33, R2): Realistic web agent environment with human baseline (78.24%). More impactful. BIRD-INTERACT has stronger simulator validation but lacks human baseline.
- HoloBench (6.25, R2): Text-to-SQL derived benchmark (90 questions). BIRD-INTERACT has larger scale and more systematic methodology.
- MMIE (8.00, R1): Top-tier multimodal benchmark (20K examples). Significantly higher quality. BIRD-INTERACT is not at this level.
- RM-Bench (8.00, R1): Top-tier reward model benchmark. Exceptionally thorough. BIRD-INTERACT is not at this level.

Round 1 bracket: 5.0–7.0. Round 2 narrowing places the paper at approximately 6.0 — comparable to accepted interactive/benchmark papers at the 6.0–6.5 level but with slightly more prominent gaps (human baseline, single-run) that prevent it from reaching the 6.5 level of τ-bench.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
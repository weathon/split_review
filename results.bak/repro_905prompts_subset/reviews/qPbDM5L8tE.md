Now I have all the information I need. Let me compose the final review.

---

## Summary

CoRAL is a modular framework for contact-rich robotic manipulation that separates perception (VLM for pose tracking and physical parameter estimation) from planning (LLM for cost function generation, contact strategy formulation, and online adaptation), coupled with an MPPI controller and a memory unit for experience reuse. The architecture is evaluated on six simulated manipulation tasks against VLA baselines and human-designed cost functions.

## Strengths

1. **Explicit VLM/LLM role separation is convincingly validated as critical.** The *CoRAL (Unified VLM)* ablation, which merges perception and planning into a single VLM, achieves 0/10 on four of six tasks and at most 2/10 on the remaining two (Table 1). This stark contrast demonstrates that the modular separation — not just model scale — is the key design choice enabling success on contact-rich tasks. This is the paper's strongest experimental result.

2. **LLM-driven online adaptation demonstrably improves robustness.** The *w/o Refinement* ablation (which disables the outer-loop adaptation) shows dramatic performance drops on tasks requiring physical reasoning: T1 falls from 4/10 to 0/10, T3 from 10/10 to 3/10 (Table 1). Because the inner-loop MPPI controller is held constant, this gap cleanly isolates the value of the LLM's ability to diagnose failures and revise plans mid-execution.

3. **The memory unit provides measurable, though modest, gains from experience reuse.** On T1 (Push+Pick Board), memory boosts success from 2/10 to 4/10, and on T3 (Pick+Place Cluster) from 9/10 to 10/10 (Table 1). Completion times also improve consistently (e.g., T4: 52s vs. 109s). The effect size is small but directionally consistent across tasks.

## Weaknesses

### Major

1. **Figure 4 (mass correction) is internally inconsistent with the text, undermining a central claim.** The paper states that the evaluation world was initialized with mass 2.0 kg (ground truth 0.1 kg) and friction 0.9 (ground truth 0.5). However, Figure 4 shows an estimated mass starting at 1.0 kg and converging to ~0.85 kg — neither matching the claimed initial value of 2.0 kg nor converging to the ground truth of 0.1 kg. The axes and narrative do not align. Three interpretations are possible: the figure depicts a different experiment than described, the text is incorrectly written, or the result is unreliable. In any case, the reader cannot trust the quantitative evidence for the paper's headline demonstration of online parameter adaptation. This is a serious credibility issue. (The *w/o Refinement* ablation still independently supports the value of the adaptation loop, but the specific mass-correction evidence presented in Figure 4 is invalid as-is.)

2. **LLM cost-function generation is critically underspecified.** The core technical novelty is that the LLM outputs a mathematical cost function and contact strategy. The paper provides a single illustrative example (Eq. 2) but does not specify: (a) the prompt template used to elicit this structured output from GPT-4o, (b) how syntactically invalid or mathematically inconsistent cost functions are handled (the example includes an indicator function `I{no contact}` that is discontinuous and would make MPPI optimization difficult without smoothing — no discussion of this), (c) what percentage of LLM calls produce usable cost functions, or (d) what happens when the LLM generates a cost function unrelated to the task. Without this information, the method's core claim — that an LLM can *reliably* formulate a control objective — remains unvalidated. This makes it impossible to assess whether the framework will generalize beyond the specific examples shown or whether it can be reproduced by other researchers.

### Minor

3. **Statistical support is weak for several claimed improvements.** All experiments use 10 trials per condition with binary success/failure outcomes. The paper uses "significantly" for comparisons where the gap is 2 trials (e.g., "significantly to 4/10" vs. 2/10 on T1; 9/10 vs. 10/10 on T3). No confidence intervals or statistical tests are reported. While the large-margin baseline comparisons (e.g., 0/10 vs. 7/10) are meaningful even with 10 trials, several ablation comparisons could easily arise from random variation. The paper should either run more trials or qualify the language.

4. **The contact strategy ablation (T6) appears to report a single-run comparison without variance.** The paper states the guided approach was "83.9% faster (32 vs. 199 steps)" and end-effector travel was "63.9% shorter (1.33 m vs. 3.69 m)" (Sec. 4.1.4). No indication is given that these are averaged over multiple trials, nor are standard deviations reported. If this is a single trajectory comparison, it provides limited evidence for the claim that the LLM contact strategy "transforms an intractable search problem into a solvable one."

5. **Simulation-only evaluation for a system claiming to handle "contact-rich manipulation."** Contact-rich effects like stiction, deformation, impact, and spatially-varying friction are notoriously difficult to simulate faithfully. Evaluating exclusively in MuJoCo, with the same physics engine used for both planning and evaluation (sim-to-sim), provides no evidence of robustness to real-world physical effects. The paper acknowledges this in one sentence in the conclusion but does not treat it as a limitation of the present contribution. For a paper whose central claim is about *contact-rich* manipulation, this is a significant gap.

### Trivial

6. The RAG retrieval description (Eq. 1) says episodes are indexed "in a latent semantic space" but provides no details on the embedding model, similarity metric, or indexing scheme. This is a minor reproducibility gap but does not affect the validity of the results presented.

## Nice-to-Haves

- Provide the full prompt template(s) used for GPT-4o in the LLM (Task Formulation) and LLM (Online Adaptation) modules.
- Replace Figure 4 with a clean mass-correction experiment showing convergence to the true value over multiple trials with variance.
- Run at least 30–50 trials per condition for the key ablation comparisons (memory, refinement) to support statistical analysis.
- Include at least one real-robot demonstration to ground the "contact-rich" claim.

## Removed Points

- **Fabrication accusation on Figure 4**: The harsh critic claimed "likely fabrication." The inconsistency is real and serious, but there is no evidence of deliberate fabrication; it could be a mislabeled figure or poorly written description. Removed the fabrication framing but kept the inconsistency as a Major weakness.
- **"LLM outputting nonsensical cost functions" failure mode analysis**: Reasonable request but speculative without testing. The paper does not provide this, so it is kept under weakness #2 (underspecified cost generation) rather than as a separate point.
- **"Missing example of explainability output in main text"**: Valid but the appendix was stripped during parsing. Not the authors' fault.
- **"Comparison with VLA baselines is unfair/incomplete"**: The comparison is acknowledged by the harsh critic as "not unfair." The paper states the baselines use LIBERO checkpoints and are tested zero-shot. This is standard practice. Removed.
- **Strength about explainability**: The paper claims explainability but provides no example in the main text (only references a stripped appendix). Cannot verify. Removed from strengths.
- **"Unified VLM failure could reflect GPT-4o's numerical reasoning limits"**: Speculative. The ablation demonstrates role separation is important regardless of the specific model. Removed.
- **Cost function indicator function discontinuity**: Kept as part of weakness #2 but downgraded from separate point — the paper notes Eq. 2 is "illustrative" and the LLM is free to choose any terms.
- **Formatting/style nitpicks**: All removed per instructions.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix the Figure 4 inconsistency.** Replace with clean data: run the mass-correction experiment with proper labels (initial estimate, true value in evaluation world, corrected estimates over adaptation cycles), report over multiple independent trials with variance.
2. **Fully specify the LLM prompting pipeline.** Provide the exact prompt template, a representative sample of generated cost functions, and a quantitative analysis of how often the LLM produces usable versus invalid outputs.
3. **Expand the trial count** for key ablation comparisons to at least 30 per condition, with confidence intervals and statistical tests where claims of "significant" improvement are made.
4. **Add at least one real-robot experiment** on a task involving genuine contact dynamics to validate the sim-to-real transfer capability, or change the framing from "contact-rich manipulation" to "simulated contact-rich manipulation."

## Score and Decision

### Calibration

**Round 1 bracket (initial pass):** I queried the human-review corpus for LLM-based robotic manipulation papers across three bands. Weak-band anchors (avg 3.0–3.4) included *LARG2*, *GRAIL*, and *From Appearance to Motion* — papers where the idea was present but evaluation or contribution was thin. Mid-band anchors (avg 4.0–5.25) included *Generating Robot Policy Code for High-Precision and Contact-Rich Manipulation Tasks* (avg 4.0), *Instruct2Act* (avg 5.0), and *Make a Donut* (avg 5.25). Strong-band anchors (>7.5) included *GenSim* (avg 8.0) and *Geometry-aware RL* (avg 8.0) — papers with comprehensive validation. Based on this bracketing, I estimated a plausible range of 3.5–5.5.

**Round 2 narrowing:** I pulled additional anchors within that bracket. *LLMPhy* (avg 4.4), *Residual-MPPI* (avg 6.25), *HAMSTER* (avg 6.0), and *GenBot* (avg 5.5) provided more granular comparisons.

**Final calibration against specific anchors:**

- *Generating Robot Policy Code* (avg 4.0, with real-robot experiments for contact-rich tasks): CoRAL has a more sophisticated architecture (separate VLM/LLM roles, online adaptation via outer loop, memory) but lacks real-robot validation and has a serious evidence inconsistency (Figure 4). CoRAL is slightly weaker due to the evidence problem. → anchors toward 3.5–4.0.
- *LLMPhy* (avg 4.4, physical reasoning benchmark): CoRAL's architectural contribution is stronger, but its evaluation has more credibility issues. Comparable overall.
- *Instruct2Act* (avg 5.0, with both simulation and real experiments): CoRAL's architecture is more novel, but Instruct2Act has cleaner evaluation. CoRAL is weaker on the evidence dimension.
- *Make a Donut* (avg 5.25, with real-robot dough manipulation): Similar in having a demonstration-free LLM+planning approach, but Make a Donut had real-robot validation. CoRAL is notably weaker here.

The Figure 4 inconsistency meaningfully reduces confidence in the paper's quantitative evidence. Combined with the underspecified LLM prompting pipeline and simulation-only evaluation, the paper falls below the average of the middle-band anchors.

**Final score: 4.0**

Anchors consulted:
| Anchor | Avg Score | Round | Comparison to CoRAL |
|--------|-----------|-------|---------------------|
| Q6HYM1EMu8 (LARG2) | 3.0 | R1 | Weaker architecture, comparable evaluation rigor |
| wl1Kup6oES (Appearance to Motion) | 3.0 | R1 | Different approach (visual pretraining), comparable weakness |
| oyXoGJQlUf (GRAIL) | 3.0 | R1 | Similar LLM+robotics gap |
| b9Ne5lHJ8Y (MuJoCo Manipulus) | 3.4 | R1 | Benchmark paper, different category |
| WtHKqtHVXo (Generating Robot Policy Code) | 4.0 | R1 | Most similar — contact-rich LLM control; had real experiments but less architecture; CoRAL ≈ slightly weaker due to Figure 4 issue |
| JWrl5pJCnl (Instruct2Act) | 5.0 | R1 | Broader evaluation with real experiments; CoRAL weaker |
| iTsHStJKcm (Make a Donut) | 5.25 | R1 | Had real-robot; CoRAL weaker |
| cbVnJa4l2o (LLM+A) | 4.0 | R1 | Similar quality tradeoffs |
| qGL6fE1lqd (LLMPhy) | 4.4 | R2 | Comparable rigor; CoRAL more novel architecturally but weaker evidence |
| gVnJFY8nCM (Residual-MPPI) | 6.25 | R2 | Stronger paper overall |
| h7aQxzKbq6 (HAMSTER) | 6.0 | R2 | Stronger evaluation with real experiments |
| s3FTX4Ay55 (Articulate-Anything) | 6.2 | R2 | Different focus, stronger execution |
| fZZ4ubttru (GenBot) | 5.5 | R2 | More ambitious scope, comparable evaluation concerns |
| RQDuFF1rOn (Wonderful Team) | 3.67 | R2 | Weaker overall |
| OI3RoHoWAN (GenSim) | 8.0 | R1 | Clearly superior — CoRAL not in this band |
| 7BLXhmWvwF (Geometry-aware RL) | 8.0 | R1 | Clearly superior |
| KsUh8MMFKQ (Thin-Shell Manipulation) | 8.0 | R1 | Clearly superior |
| or8mMhmyRV (MaestroMotif) | 7.75 | R1 | Clearly superior |

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>
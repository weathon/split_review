Now I have enough context for calibration. Let me write the final review.

**Round 1 bracket**: Based on comparing to anchors, the paper sits between the 4.0 papers (Generating Robot Policy Code, LLM+A) and the 5.25 paper (Make a Donut). 

**Round 2 narrowing**: Compared to Instruct2Act (5.0) — CoRAL tackles harder contact-rich problems and has a cleaner ablation structure, but the mass-correction inconsistency is a significant issue that this anchor doesn't have. Compared to Plan-Seq-Learn (6.67) — CoRAL is clearly below this, lacking the same empirical breadth and real-system validation.

CoRAL is slightly above the 4.0 anchors (better architecture, more thorough ablations) but below the 5.25 anchor (mass-correction issue, no real-robot validation). Within its bracket, I place it at the lower end due to the unresolved inconsistency.

Here is the final consolidated review:

## Summary
CoRAL proposes a modular neuro-symbolic framework for zero-shot contact-rich robotic manipulation. It integrates FoundationPose for 6-DoF tracking, GPT-4o as a VLM for physical parameter estimation, a separate GPT-4o LLM role for generating MPPI cost function structures and contact strategies, and a closed-loop adaptation mechanism that refines both the world model and plan mid-execution. A RAG-based memory unit enables cross-task reuse. The framework is evaluated in simulation on six contact-rich tasks against VLA baselines (OpenVLA, π_0.5), human-expert-designed cost baselines, and several ablations.

## Strengths
1. **LLM-formulated MPPI cost function structure**: Unlike prior work (VLMPC, IMPACT) that uses VLMs only for perceptual guidance or static cost maps, CoRAL's LLM generates the analytical structure and relative weights of the MPPI cost function itself (Eq. 2), including task-specific terms. The Unified VLM ablation (0/10 on four of six tasks, Table 1) provides direct evidence that this architectural choice matters.

2. **Closed-loop online adaptation with explicit LLM-driven correction**: The outer loop (Section 3.4) enables the LLM to revise physical parameter estimates and strategy mid-execution. The w/o Refinement ablation drops from 4/10 to 0/10 on T1 (Table 1), providing concrete evidence that this mechanism is critical for multi-stage tasks.

3. **Contact strategy biasing with quantitative efficiency evidence**: The guided contact strategy on T6 reduces planning steps by 83.9% (32 vs. 199) and end-effector path by 63.9% (1.33 m vs. 3.69 m) compared to the unguided variant. This directly demonstrates that symbolic contact biasing substantially prunes the search space for long-horizon contact problems.

4. **Controlled VLM/LLM role separation ablation**: The Unified VLM variant fails catastrophically (0/10 on T1, T3, T5, T6), directly validating the paper's core architectural hypothesis about role separation.

5. **Memory unit shows measurable cross-task reuse gains**: Ablation results (Table 1) show consistent improvements from memory on both success rate (T1: 2/10→4/10, T3: 9/10→10/10) and completion times (T4: 109s→52s, T6: 164s→106s).

## Weaknesses

### Major
1. **Mass-correction experiment internally inconsistent**: Section 4.1.4 describes initializing the Evaluation World with mass 2.0 kg (ground truth 0.1 kg), claiming the system corrects online to converge "remarkably close to their true values." However, Figure 4 shows corrected mass converging to ~0.85 kg from an initial estimate of 1.00 kg — neither matching the stated 2.0 kg initial condition nor the 0.1 kg ground truth. The y-axis range (0.75–1.00 kg) also does not cover the described values. No corresponding figure is provided for the friction correction described in the same paragraph. Since this experiment is the headline demonstration of online parameter adaptation, the inconsistency makes a central robustness claim unverifiable as presented.

### Minor
2. **Statistical support is weak for key conclusions**: All results use 10 binary-success trials per condition. For binomial outcomes with n=10, the 95% confidence interval width is roughly ±30 percentage points. Differences treated as meaningful (e.g., memory improving T1 from 2/10 to 4/10) lie within this noise. No confidence intervals, variance measures, or significance tests are reported.

3. **LLM-controller interface underspecified for reproducibility**: (a) How the LLM's text output is parsed into a structured, runnable cost function is not described — only an illustrative example (Eq. 2) is given, with no specification of the output format, constraints, or parser. (b) How the LLM specifies contact region parameters {c_j, e_j} for Eq. (3) is not specified. (c) The RAG-based memory retrieval (Eq. 1) does not specify which embedding model, similarity metric, or match threshold is used.

4. **Completion time overhead not discussed**: CoRAL takes substantially longer than baselines on several tasks (e.g., T2: 45s vs. 5s for OpenVLA; T4: 52s vs. 32s for single-stage expert). The paper acknowledges "computational latency" in the conclusion but provides no timing breakdown or analysis of where the bottleneck lies.

5. **The explainability claim lacks systematic evaluation**: The paper provides one anecdotal example of the LLM diagnosing a cost-weight issue but no systematic evaluation of diagnostic accuracy, frequency, or comparison to alternatives.

### Trivial
6. **Outer loop trigger condition underspecified**: N_retry=15 is given but what constitutes a "persistent failure" in measurable terms is not defined.

## Nice-to-Haves
- Real-robot validation of at least one task would substantially strengthen deployment claims
- Ablation of the VLM's physical parameter estimation accuracy (mass, friction) would clarify error tolerances
- Analysis of how often and why the outer loop triggers across trials would illuminate adaptation dynamics

## Removed Points
These points were raised by reviewers but removed after cross-checking against the paper:
- **"Zero-shot framing is overextended"**: Removed. The paper defines "zero-shot" as "without relying on extensive tele-operated action datasets" — a standard usage in robotics. The memory unit augments rather than contradicts this framing.
- **"Simulation-only evaluation is critical"**: Demoted to Nice-to-Have. The paper's experiments are explicitly in simulation. Requiring real-robot validation sets an unreasonably high bar for early-stage method papers.
- **"VLA baselines are unfair"**: Removed. The paper transparently uses officially released LIBERO checkpoints. The finding that these models fail outside their training distribution is a legitimate result.
- **"Expert (FSM) outperforms CoRAL — framing dishonest"**: Removed. The paper explicitly acknowledges this gap in Section 4.1.2.
- **"Unified VLM ablation is a straw man"**: Removed. Testing the design hypothesis by comparing separated vs. unified models is a standard and appropriate ablation.
- **"Missing analysis of outer loop triggers"**: Moved to Nice-to-Have.

## Novel Insights
The harsh critic and strength finder converge on a useful observation: the paper's strongest evidence for online adaptation is not the mass-correction experiment (which has an internal inconsistency) but rather the w/o Refinement ablation on T1 (0/10 vs. 4/10) and the guided-vs-unguided contact strategy comparison on T6. This suggests the paper could be substantively improved by simply correcting or removing the problematic mass-correction figure and relying on the ablation evidence, which tells a coherent and well-controlled story about which components matter and why.

## Suggestions
- Reconcile the mass-correction experiment: correct either the text description (2.0→0.1 kg) or Figure 4 (1.0→0.85 kg) so they are internally consistent
- Add confidence intervals or standard deviations to success rate and timing results
- Specify the LLM output parsing mechanism (prompt format, constraints, parser) for reproducibility
- Report a breakdown of computation time per pipeline stage
- Define the inner-loop failure criterion for outer loop triggering

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
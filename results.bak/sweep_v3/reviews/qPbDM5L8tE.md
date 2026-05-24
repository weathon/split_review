Now I have all the evidence needed. Let me produce the consolidated review.

## Summary

CoRAL presents a modular neuro-symbolic framework for zero-shot contact-rich robotic manipulation that decouples perception (VLM → physical parameter estimation), reasoning (LLM → cost function design and contact strategy), and low-level control (MPPI with reactive feedback). The architecture includes a memory unit for experience reuse and an outer adaptation loop that refines the world model and plan upon repeated failure. Evaluated on six simulated manipulation tasks (including push-and-pick, force-controlled pushing, and wall-assisted flipping), CoRAL succeeds where end-to-end VLA baselines (OpenVLA, π₀.₅) fail entirely, though it is generally outperformed by a human-designed FSM cost baseline.

## Strengths

- **Zero-shot success on contact-rich tasks where VLA baselines fail outright.** Table 1 shows CoRAL achieves 4/10 (T1), 9/10 (T4), 9/10 (T5), and 7/10 (T6), while both OpenVLA-OFT and π₀.₅ score 0/10 on all four contact-rich tasks. This provides direct evidence that the decoupled architecture can handle physically demanding manipulation without task-specific fine-tuning.

- **The VLM/LLM role separation is causally necessary.** The "CoRAL (Unified VLM)" ablation, which gives a single VLM both perception and planning responsibilities, scores 0/10 on five of six tasks (Table 1). The full system with separated roles succeeds on four of those, supporting the core architectural claim with a clean ablation.

- **LLM-guided contact strategy dramatically reduces search complexity.** In the "Flip with Wall" task (Section 4.1.4), the LLM-provided contact strategy yields 83.9% fewer steps (32 vs. 199) and a 63.9% shorter end-effector path (1.33 m vs. 3.69 m) compared to an MPPI that receives only the cost function without contact guidance. This quantified result convincingly shows the value of symbolic contact reasoning.

- **Explainable failure diagnosis.** Section 4.1.4 demonstrates a case where the LLM diagnoses a poorly weighted cost function in natural language and adjusts specific weights to recover — a transparency advantage over black-box policies that the paper concretely illustrates.

## Weaknesses

### Fatal
None. The paper's core contributions are not invalidated, though one significant claim is undermined (see Major).

### Major

- **The mass-correction robustness experiment (Section 4.1.4, Figure 4) contains a clear and unresolved inconsistency between text and figure.** The text states the Evaluation World was initialized with a severely overestimated mass of **2.0 kg** versus a ground truth of **0.1 kg**, with friction at **0.9 vs. 0.5**. However, Figure 4 shows a y-axis ranging only from 0.75 to 1.00 kg, an "Initial Mass" constant at **1.00 kg** (not 2.0 kg), and a "Corrected Mass" that drops to approximately **0.85 kg** — not 0.1 kg. Friction correction is not shown at all. The text claims "the agent's belief about both mass and friction converged remarkably close to their true values," but the figure depicts convergence to 0.85 kg when the stated ground truth is 0.1 kg — off by a factor of 8.5. This is not a minor labeling issue; the figure and text describe fundamentally different experiments or the figure does not support the stated claim. Since this is the primary quantitative evidence for online physical parameter adaptation (Contribution 3), this inconsistency substantially weakens that claim. The paper should either provide a corrected figure with clear convergence to the stated ground truth, or remove the claim.

- **Simulation-only evaluation without acknowledgment as a limitation.** All experiments are conducted in MuJoCo via ROBOSUITE. Contact-rich manipulation is known to be highly sensitive to physical parameter mismatches between simulation and reality (the paper itself acknowledges this by testing robustness to mass/friction perturbations). The limitations section (Section 5) discusses computational latency and vision model fidelity but does not mention that results are simulation-only or discuss what would be required for real-world transfer. For a framework whose stated contributions include "robustness and adaptability in unknown environments," the lack of real-hardware validation — or at minimum an explicit discussion of the sim-to-real gap — is a significant omission. The paper could be reframed as a simulated proof-of-concept, but it currently presents itself more broadly.

- **Statistical evidence is thin.** All success rates are based on 10 trials per condition. For a binary metric, a 4/10 result has a 95% confidence interval of roughly [12%, 74%]. The paper draws conclusions like "memory boosted the success rate significantly from 2/10 to 4/10" (Section 4.1.3) — a difference of 2 trials — without any statistical testing or variance reporting. Improving to at least 30 trials per condition and reporting confidence intervals would substantially strengthen the evaluation.

### Minor

- **Absolute success rates on the most interesting tasks are modest.** CoRAL achieves 4/10 on the multi-stage Push+Pick Board (T1) and 7/10 on Flip with Wall (T6). The human-designed FSM baseline achieves 8/10 and 9/10 respectively (Table 1). The paper's framing ("narrows the gap") is honest, but the gap remains large on the hardest tasks.

- **Memory unit benefit is small and statistically fragile.** The improvement from removing memory is 2/10 → 4/10 on T1 (two trials), 9/10 → 10/10 on T3 (one trial), and essentially flat on other tasks. With 10 trials per condition, these differences are within measurement noise. No analysis of retrieval accuracy, memory size scaling, or the effect of memorized vs. novel task configurations is provided.

- **No computational cost breakdown.** The paper mentions "computational latency" as a limitation in passing (Section 5) but provides no wall-clock time per trial, number of LLM/VLM API calls per task, or analysis of where the bottleneck lies. For a system that chains multiple GPT-4o calls with MPPI rollouts, this information is important for assessing practical deployability.

- **Success criteria not defined.** The paper reports binary success/failure but never specifies the automated threshold or human evaluation protocol used to determine success for each task.

### Trivial
None.

## Nice-to-Haves
- Real-robot validation on at least 2-3 of the presented tasks (especially T1 and T6) would transform this from a simulated proof-of-concept into a convincing demonstration of the claimed robustness.
- An ablation replacing FoundationPose with a different 6-DoF tracker (rather than removing it entirely) would better isolate the contribution of precise pose tracking vs. the specific tracker choice.
- Including prompt templates or a summarized prompt structure in the appendix would improve reproducibility.

## Removed Points

These points were raised in the inputs but are removed from the main review for the following reasons:

1. *"Baselines are tested zero-shot on tasks far from their training distribution"* — This is not a weakness; testing zero-shot generalization on out-of-distribution tasks is exactly the point of the comparison. The paper is honest about the experimental setup. REMOVED.

2. *"Single-stage expert getting 0/10 on T1 seems suspiciously low"* — Speculation without evidence about implementation quality. REMOVED.

3. *"Unified VLM ablation is underspecified"* — The paper describes it as "a single multimodal prompt for both perception and planning" — sufficient detail for an ablation. REMOVED.

4. *"The paper does not acknowledge simulation-only scope in main text"* — This is addressed in the main Weaknesses section above. The removed point's framing as a "structural issue" is overstated; many robotics papers at top venues are simulation-only. But the lack of explicit acknowledgment is noted in Major weakness #2.

5. *"Strengths" that are generic or sycophantic* (e.g., "the problem is important") — REMOVED. Only concrete strengths with specific evidence are retained.

6. *Formatting/style nitpicks and missing-appendix references* — REMOVED per hard rules.

## Novel Insights

The reviews surface one insight beyond the paper's own contributions: the mass-correction figure (Figure 4) vs. text inconsistency suggests that the paper may contain a genuine experimental error rather than merely a presentation flaw. The text describes an extreme perturbation (2.0 kg → 0.1 kg ground truth), but the figure shows a mild correction (1.00 kg → 0.85 kg). If the correction capability only operates within ±15% of the initial estimate, the claim of "converging remarkably close" under a 20× overestimate is unsupported. This points to a deeper issue: the paper's robustness claims may be more limited than advertised. Conversely, the contact-strategy ablation (83.9% speedup) is quantitatively sound and well-isolated, and the VLM/LLM separation ablation is clean. The paper's strongest evidence is for contributions 1 (modular architecture enabling zero-shot contact-rich manipulation) and 4 (contact strategy pruning search space), while contribution 3 (online physical parameter adaptation) is the weakest-supported major claim.

## Suggestions

1. **Fix or remove the mass-correction experiment.** Align the figure with the text description, or if the data does not show convergence to the stated ground truth, remove the experiment and explicitly downgrade the associated claim.

2. **Acknowledge the simulation-only scope explicitly** in the limitations section and briefly discuss sim-to-real transfer requirements.

3. **Increase trial counts** (at least 30 per condition) and report confidence intervals or Bayesian estimates for binary success rates.

4. **Define success criteria** for each task.

5. **Provide wall-clock times and API call counts** per task to ground the computational latency concern.

## Score and Decision

### Calibration Anchors

| Paper | Avg Score | Comparison |
|---|---|---|
| **Residual-MPPI** (`gVnJFY8nCM.md`) | 6.25 (Accept) | Stronger evaluation (MuJoCo + GTS), clean methodology, no figure-claim inconsistencies. CoRAL is weaker — less thorough evaluation, unresolved figure issue. |
| **RoboFlamingo** (`lFYj0oibGR.md`) | 6.50 (Accept) | SOTA on CALVIN benchmark, thorough ablations. CoRAL addresses a harder problem (contact-rich zero-shot vs. imitation learning) but has weaker evidence. |
| **Make a Donut** (`iTsHStJKcm.md`) | 5.25 (Reject) | Similar structure (LLM + MPC for manipulation), has real-robot experiments. CoRAL has broader task set but no real-robot and a problematic figure. |
| **CORN** (`KTtEICH4TO.md`) | 4.75 (Accept) | Real-robot zero-shot transfer, 300+ objects. CoRAL has less comprehensive evaluation but tackles a different problem setting. |
| **Generating Robot Policy Code** (`WtHKqtHVXo.md`) | 4.00 (Reject) | Real-robot contact-rich manipulation via LLM. CoRAL has broader task variety but shares the simulation-only limitation and adds a figure inconsistency. |
| **GRAIL** (`oyXoGJQlUf.md`) | 3.00 (Reject) | Very weak evaluation (single 2D maze domain). CoRAL is clearly stronger in breadth and execution. |

**Score rationale:** The paper's core idea (modular VLM+LLM+MPPI for zero-shot contact-rich manipulation) is sound and partially well-supported (Table 1, contact strategy ablation). However, the central robustness experiment (Figure 4) contains an unresolvable text/figure contradiction that undermines a headline claim, the evaluation is entirely simulated without acknowledgment, and statistical power is low throughout. These issues collectively prevent acceptance. The paper sits between the "weak but has merit" cluster (score ~4) and the "borderline" cluster (score ~5), closer to 4 given the verifiable figure inconsistency.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>
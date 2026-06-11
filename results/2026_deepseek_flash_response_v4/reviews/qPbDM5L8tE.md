## Summary

CoRAL proposes a modular neuro-symbolic framework for contact-rich robotic manipulation that integrates vision models (FoundationPose, GPT-4o as VLM) with an LLM (GPT-4o) that generates cost functions and contact strategies for an MPPI controller. The system features nested feedback loops: an inner loop for reactive control and an outer loop where the LLM diagnoses failures and refines the world model and plan online. The paper evaluates on six simulated tasks in MuJoCo, comparing against OpenVLA, π0.5, and human-expert-designed cost baselines, with ablations testing each component.

## Strengths

1. **LLM-generated contact strategy quantitatively prunes the search space**: Section 4.1.4 shows that on the Flip with Wall task, the LLM-guided contact strategy reduces planning steps by 83.9% (32 vs. 199) and end-effector travel by 63.9% (1.33 m vs. 3.69 m) compared to unguided MPPI sampling. This is a clean, apples-to-apples ablation that directly supports the claim that LLM-generated contact strategies make long-horizon contact problems tractable.

2. **Ablation evidence for VLM/LLM role separation**: The Unified VLM ablation (collapsing perception and planning into a single model) catastrophically fails (0/10 on four of six tasks, 2/10 on the simplest). This empirically validates the paper's central architectural claim that separating vision for perception from an LLM for strategy formulation is critical.

3. **Well-motivated expert-designed baselines**: The human-expert-designed cost baselines (single-stage and FSM, Table 1) provide a meaningful upper bound. The paper honestly reports that the FSM variant outperforms CoRAL on every task, while CoRAL matches or exceeds the single-stage expert on the harder tasks (T1, T5, T6).

4. **Explicit, formalized LLM output structure**: Equations (2) and (3) specify precisely how the LLM's output is structured as a weighted cost functional and parametric contact surface regions, going beyond free-text plans in prior work (Inner Monologue, ECoT) and making the LLM-controller interface precise and reproducible.

## Weaknesses

### Major

1. **Figure 4 and the mass-correction experiment are internally inconsistent and do not support the stated conclusion.** The text (line 220) states the Evaluation World was initialized with mass = 2.0 kg vs. ground truth = 0.1 kg, and that the LLM drove the estimate "remarkably close" to the true value. However, Figure 4 shows "Initial Mass" constant at 1.0 kg (not 2.0 kg) and "Corrected Mass" dropping from 1.0 kg to ~0.85 kg — a factor of 8.5× away from the 0.1 kg ground truth. The claim of convergence "remarkably close" to the true value is unsupported by the presented data. This directly undermines one of the four claimed contributions: the "LLM-driven, closed-loop feedback mechanism that enables the system to adapt its plan mid-execution." The paper must present internally consistent evidence for this flagship experiment.

2. **VLA baselines are evaluated zero-shot on tasks outside their training distribution, conflating distribution shift with architectural limitation.** OpenVLA-OFT and π0.5 are tested using LIBERO checkpoints on custom tasks (T1, T4, T5, T6) involving force control, flipping, and wall fixtures — maneuvers unlikely to appear in the LIBERO dataset. Their near-zero performance is unsurprising. The paper's stronger claim that "even fine-tuning an end-to-end policy is insufficient" (line 193) is not supported by this comparison; the VLAs were not fine-tuned on these tasks. A comparison to fine-tuned VLAs or to the modular neuro-symbolic approaches cited in the related work (IMPACT, VLMPC, Inner Monologue) would be more informative.

### Minor

1. **No statistical significance testing with only 10 binary trials per condition.** With n=10, 95% confidence intervals are wide (e.g., 4/10 has CI ~12–74%). Several ablation comparisons discussed as meaningful (e.g., 9/10 vs. 7/10 on T3; 9/10 vs. 9/10 on T4) are within the noise. Results should be interpreted cautiously.

2. **The reactive control gain K_f (Eq. 7) is not specified, ablated, or analyzed.** This term is central to the claim of robustness against the sim-to-real gap, yet no experimental results involve it directly. Its value, whether it was tuned per task, and its effect on performance are not reported.

3. **No experimental comparison to the closest related-work methods (IMPACT, VLMPC).** The related work (line 43) positions CoRAL as "significantly advancing" the paradigm of integrating foundation models with motion planners, but the closest prior methods are never compared experimentally. This makes the claimed advance difficult to assess.

4. **Limited specification of LLM prompts and error handling.** The paper does not describe the prompt structure for the LLM, how the LLM knows which state/action variables are available (line 91), or how the system handles invalid cost terms. This is relevant for reproducibility.

5. **The mapping between standard LIBERO tasks and Table 1 is unclear.** The paper states that "two benchmark tasks from the LIBERO suite" were incorporated (line 151), but it is not specified which Table 1 entries correspond to these tasks.

### Trivial

None.

## Nice-to-Haves

- Real-world validation or a discussion of what would be required to transfer the system to hardware, given the paper's explicit framing around sim-to-real robustness.
- Reporting LLM API call counts and costs per task, as a practical concern for deployment.
- A friction correction figure alongside the mass correction figure, since the text claims both were corrected online.

## Removed Points

- **"Underperformance against human-expert baselines is underemphasized"** — Removed because the paper's language ("narrows the gap," "approaching") is appropriately modest. CoRAL outperforms the single-stage expert on T1 (4/10 vs. 0/10) and T6 (7/10 vs. 3/10). The framing is accurate.
- **"Simulation-only evaluation"** — Demoted to Nice-to-Haves. Simulation evaluation is standard practice in manipulation research; the paper acknowledges this limitation (line 242).
- **"Unified VLM catastrophic failure is suspicious / prompt quality confound"** — Removed as speculative. The paper's explanation (role separation is critical) is the natural interpretation of the data.
- **"Friction correction figure missing"** — Moved to Nice-to-Haves. Not a flaw.
- **"Expert baselines had privileged information"** — The paper clearly states expert costs were "tuned in a separate design environment" and evaluated as-is in the randomized test environment. This is a reasonable setup.

## Novel Insights

Reviews converge on a nuanced picture: CoRAL's architecture is genuinely well-motivated and the task suite is creative. The ablation chain cleanly isolates each component's contribution. However, the central empirical demonstration of online adaptation — the mass-correction experiment that embodies the "closed-loop feedback" contribution — is presented with internally contradictory data (text claims 2.0 kg initial, 0.1 kg ground truth; figure shows 1.0 kg initial and correction to 0.85 kg, which is nowhere near 0.1 kg). This is not a generic weakness; it is a specific evidence failure at precisely the point where the paper needs to be most credible. Additionally, the VLA comparison conflates distribution shift with architectural limitation, and the closest related-work methods are never compared experimentally.

## Suggestions

1. Fix the mass-correction experiment: present a figure where the axis values, initial estimate, ground truth, and corrected values are all internally consistent and clearly labeled. If the correction converges to a value far from ground truth, acknowledge this and discuss implications.
2. Include a comparison to at least one modular neuro-symbolic baseline from the related work (IMPACT or VLMPC) on at least one task, to ground the claimed differentiation.
3. Report confidence intervals or individual trial data for the binary success metrics.
4. Specify the prompt templates used for the VLM and LLM modules for reproducibility.
5. Clarify the mapping between standard LIBERO tasks and Table 1 entries.

## Score and Decision

**Score: 4.5 — Weak Reject**

**Calibration anchors (all rounds):**

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|-----------|
| GRAIL | 3.00 | R1 | Much weaker; simpler LLM planning, minimal evaluation |
| Diff-Transfer | 3.40 | R1 | Much weaker; narrower scope |
| From Appearance to Motion | 3.00 | R1 | Much weaker; different problem |
| Intelligent Control | 3.50 | R2 | Much weaker; simplistic LLM+controller tuning |
| LLM+A | 4.00 | R2 | Weaker; simpler prompt-based approach, less evaluation |
| **Generating Robot Policy Code** | **4.00** | **R1,R2** | **Most similar topic. CoRAL has broader evaluation (6 vs 2 tasks) and better ablations, but that paper has real robot validation while CoRAL has the mass-correction evidence problem. CoRAL slightly stronger overall.** |
| **LLMPhy** | **4.40** | **R1,R2** | **Similar scope (simulation-only LLM+physics). Comparable quality; CoRAL has more tasks but the evidence issue levels it.** |
| Make a Donut | 5.25 | R1,R2 | Stronger; has real-world experiments |
| Open-World Planning | 5.50 | R2 | Stronger; more thorough evaluation across domains |
| GenBot | 5.50 | R1 | Stronger; larger scale |
| Zero-Shot Robotic Manipulation | 6.25 | R2 | Significantly stronger; accepted |
| Plan-Seq-Learn | 6.67 | R2 | Significantly stronger; accepted with 25+ tasks |
| GenSim | 8.00 | R1 | Much stronger; accepted |
| Thin-Shell Object Manipulations | 8.00 | R1 | Much stronger; accepted |
| Geometry-aware RL | 8.00 | R1 | Much stronger; accepted |
| Data Scaling Laws | 8.00 | R1 | Much stronger; accepted |

Round 1 bracket: 4–6. Round 2 narrowed to 4.0–5.5. CoRAL sits above the ~4.0 papers (better architecture, more thorough ablations) but below the ~5.25+ papers (weaker due to the mass-correction evidence problem and missing comparisons to closest baselines). Final calibrated score: 4.5.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
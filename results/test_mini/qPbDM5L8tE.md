Now I have sufficient calibration data. Let me write the final consolidated review.

## Summary

CoRAL proposes a modular framework for zero-shot contact-rich robotic manipulation that separates perception (FoundationPose for pose tracking, VLM for physical parameter estimation) from reasoning (LLM for cost function generation and contact strategies) from control (MPPI with reactive feedback). It introduces an online adaptation loop where the LLM refines both its world model and plan based on execution outcomes, and a memory unit for experience reuse. The key empirical claim is that this neuro-symbolic architecture significantly outperforms end-to-end VLA models (OpenVLA, π₀.₅) on contact-rich manipulation tasks.

## Strengths

- **Strong ablation study cleanly validates the modular design.** Table 1 shows that removing FoundationPose (CoRAL w/o Pose Tracking) yields 0/10 on all complex tasks, and fusing perception and planning into a single VLM (CoRAL Unified VLM) also produces catastrophic failure (0/10 on T1, T5, T6). The w/o Refinement and w/o Memory ablations show systematic degradation. This provides convincing evidence that each component in the architecture serves a distinct, necessary function.

- **Quantitatively outperforms end-to-end VLA baselines on the tasks that require physical reasoning.** On T1 (Push+Pick Board), T4 (Push with Constant Force), T5 (Flip Box), and T6 (Flip w/ Wall), CoRAL achieves success rates of 4/10, 9/10, 9/10, and 7/10 respectively, while OpenVLA-OFT scores 0/10, 0/10, 1/10, 0/10 and π₀.₅ scores 0/10, 0/10, 3/10, 0/10. The gap is substantial and consistent across all four contact-heavy tasks.

- **LLM-generated contact strategy provably reduces planning complexity.** Section 4.1.4 quantifies this with a direct ablation on T6: the guided strategy reduces required steps by 83.9% (32 vs. 199) and end-effector path by 63.9% (1.33 m vs. 3.69 m) compared to random sampling, demonstrating that the symbolic biasing of the search space is not just a nice idea but has measurable impact.

- **Explainability is demonstrated concretely.** The paper shows a failure-recovery trace where the LLM correctly diagnoses a misweighted cost function and reports the adjustment in natural language (Section 4.1.4). This is a genuine advantage over black-box VLA policies that the paper makes tangible.

## Weaknesses

### Major

- **Direct contradiction between the text and Figure 4 undermines the central robustness claim.** The text (Section 4.1.4) states: *"we intentionally initialized the Evaluation World with a severely overestimated mass (2.0 kg vs. a ground truth of 0.1 kg)"* and claims the corrected mass converges *"remarkably close"* to the true value. However, Figure 4 (and its caption) shows: y-axis ranging 0.75–1.00 kg, corrected mass converging to ≈0.85 kg from a starting value of ≈1.0 kg, and an "Initial Mass" line constant at 1.0 kg. Neither 2.0 kg (the claimed initial evaluation-world mass) nor 0.1 kg (the claimed ground truth) appear anywhere in the figure's range. A correction from ~1.0 kg to ~0.85 kg is not a correction from 2.0 kg toward 0.1 kg, and 0.85 kg is *not* close to 0.1 kg. This is not a minor labeling issue — the figure and the textual description describe quantitatively different experiments. Because online physical parameter adaptation is one of the paper's headline contributions, this inconsistency is a serious credibility problem.

- **No quantitative comparison against the most closely related neuro-symbolic planners.** The paper discusses IMPACT, VLMPC, OneTwoVLA, ThinkAct, and Inner Monologue in the related work (Section 2) and positions CoRAL as advancing the same paradigm of integrating foundation models with planners. Yet the experimental evaluation compares CoRAL only to end-to-end VLAs (OpenVLA, π₀) and to human-designed cost functions. Without any comparison against IMPACT or VLMPC — systems that also use a VLM to guide a planner — the paper cannot substantiate its claim that *its particular design choices* (LLM generates the cost function structure, symbolic contact strategies, online adaptation via LLM) represent a meaningful advance over existing integration strategies. This is a major gap for a paper that situates itself within this line of work.

### Minor

- **Method specification is too vague for reproducibility.** The paper says the LLM is "free to introduce any cost terms constructible from the available state, pose, and action variables" (Section 3.2) and gives an illustrative example in Eq. 2. But it does not specify: (a) the prompt provided to the LLM, (b) the output format/convention for the cost function, (c) how the LLM's output is parsed into executable code, (d) the mechanism by which the LLM generates geometric contact parameters in Eq. 3 (centers, radii, tangent vectors), or (e) the prompt provided to the VLM for mass/friction estimation. These are not implementation details to relegate to an appendix — they are core to the claimed contribution of having an LLM *generate* cost functions and strategies, and need to be described for the method to be assessed or built upon.

- **Simulation-only evaluation with no real-world validation.** The paper claims robustness for *"deploying robots in unknown environments"* (Section 4.1.4) but evaluates only in simulation. While simulation is acceptable for an initial proof-of-concept, the gap between the language used ("robust," "deploying") and the evidence provided is notable. Real-world validation on even one task would substantially strengthen the claims.

- **Low statistical power and no variance reporting.** All results are based on 10 trials with binary success/failure and no confidence intervals. On tasks where success rates differ by 1–2 trials (e.g., 4/10 vs. 2/10 on T1 with vs. without memory), the difference is not statistically significant. The efficiency numbers in Section 4.1.4 (83.9% faster, 63.9% shorter) are reported for a single ablation with no indication of variance or multiple trials.

- **No validation of VLM physical parameter estimates.** The VLM (GPT-4o) estimates mass and friction from appearance, but the paper provides no evaluation of how accurate these estimates are — no comparison of VLM estimates to ground truth, no analysis of typical error magnitudes. The ablation that removes the VLM entirely (Unified VLM) shows catastrophic failure, but this does not isolate whether the *physical parameter estimates themselves* are accurate or merely that removing them collapses the system.

### Trivial

- Figure 4's y-axis labeling is unclear regardless of the contradiction: the "Initial Mass" line at 1.0 kg and the "Corrected Mass" starting at 1.0 kg are indistinguishable at t=0.
- The RAG retrieval formula in Eq. 1 says the LLM embeds the task into "a latent semantic space" but does not specify the embedding function.

## Nice-to-Haves

- A failure analysis for the tasks with lower success rates (T1 at 4/10, T6 at 7/10). Does the LLM generate poor cost functions for these tasks? Does the MPPI fail to converge? Does the memory retrieval retrieve irrelevant experiences? Understanding failure modes would improve the paper and guide future work.
- Replacing the LLM with a rule-based planner or simpler heuristic for cost function generation as an ablation, to isolate whether the LLM's language-based reasoning adds value over a structured baseline.
- Reporting the full range of randomization used for object masses, friction, and dimensions in the evaluation protocol.

## Removed Points

- **"Uneven comparison to end-to-end baselines"** — The harsh critic argues CoRAL receives privileged information (3D object models, simulator rollouts) that OpenVLA and π₀ do not. While this is factually correct, it reflects a design difference between paradigms (neuro-symbolic using explicit models vs. end-to-end learning from pixels), not an unfair comparison. CoRAL is being compared on the question: *which approach performs better on these tasks?* That CoRAL uses object models is inherent to its approach, not a hidden advantage. The claim is that the neuro-symbolic paradigm is more effective, and the comparison supports that claim.

- **"Low absolute performance on the tasks"** — The harsh critic notes 4/10 on T1 and 7/10 on T6 are modest. But these tasks were designed to be challenging for vision-based planners, and the baselines score 0/10. The paper's claim is about outperforming existing methods, not about achieving deployable reliability. This criticism conflates "low relative to perfect" with "does not support the paper's claims."

- **"Contact detection noise in real systems"** — The critic notes the indicator penalty for "no contact at t" could be noisy with real force sensors. Valid speculation but not a verified weakness of the paper as written; the paper uses a physics engine where contact detection is clean.

- **"OneDemo is missing comparisons"** and similar missing-related-work notes — removed per instructions that related-work gaps should not be flagged.

- Several generic rigor/scope criticisms from the harsh critic that were category-driven rather than specific to a concrete issue in the paper.

## Novel Insights

None beyond the paper's own contributions. The two independent reviews identify similar points: the figure contradiction is real and damaging, the method needs better specification, and the missing neuro-symbolic baselines are a genuine gap. The strength finder correctly identifies the ablation study and the contact-strategy ablation as the paper's strongest empirical evidence.

## Suggestions

1. **Resolve the Figure 4 contradiction.** The paper must either provide a corrected figure that matches the stated experimental setup (2.0 kg initial, 0.1 kg ground truth) or revise the text to match what the figure actually shows. A detailed plot showing the full trajectory of the mass estimate with clearly labeled ground truth, initial estimate, and corrected values would be much more informative.

2. **Add comparisons against at least one neuro-symbolic baseline** (e.g., IMPACT or VLMPC) to substantiate the claim that CoRAL's specific design — LLM-generates-the-cost-function — advances the paradigm. If these methods cannot be run in the same environment, a clear qualitative comparison of design choices would partially address the gap.

3. **Specify the LLM interface precisely.** Provide the prompt templates (or their structure), the output format, and the parsing mechanism that converts the LLM's text output into executable cost functions and geometric parameters. This is essential for reproducibility and for the community to assess the method's generality.

4. **Run a real-world experiment on at least one task** to demonstrate that the simulation results transfer. Even a single task with a few trials would dramatically increase the paper's credibility.

5. **Report confidence intervals or more trials** (e.g., 20+ trials per condition) for the main results, and report variance for the efficiency numbers in Section 4.1.4.

## Score and Decision

Let me first establish my calibration bracket.

**Round 1 bracket:** Based on the calibration search, papers on modular LLM/VLA frameworks for manipulation cluster around 1.5–3.0 (weak, rejected/withdrawn) and 4.5–5.5 (middle, rejected/borderline). Strong papers at 6.5+ involve large-scale datasets, real-world validation, or novel training paradigms. CoRAL sits between the weak and middle anchors: it has concrete experiments and a clean ablation design that places it well above papers like GRACE (1.5), but the Figure 4 contradiction and missing baselines are significant liabilities.

**Initial bracket: 4.0–5.5**

**Narrowing:** Within this bracket, CortexVLA (4.5, Reject), MoSEL (4.5, Reject), Semantic World Models (5.0, Reject), and PDDLLM (5.5, Accept Poster) are the relevant anchors. CoRAL has a stronger ablation study than CortexVLA and more concrete evaluation than MoSEL. However, CoRAL has the Figure 4 integrity issue that none of these anchors have. Semantic World Models (5.0) had minor method-specification issues but no central-evidence contradiction.

CoRAL is comparable to CortexVLA (4.5) in overall ambition and quality of evaluation, but the Figure 4 issue is more serious than any single weakness in CortexVLA (which was criticized for being an engineering integration rather than a novel scientific contribution). This places CoRAL slightly below the CortexVLA cluster.

**Anchors consulted:**
| Path | Avg. Score | Round | Comparison |
|------|-----------|-------|------------|
| SESeW4EvPd (GRACE) | 1.50 | 1 | Well below CoRAL — vague methodology, poor writing |
| tkLDNUzL80 (Phys. Grounded Commonsense) | 2.67 | 1 | Below CoRAL — weaker empirical evidence |
| JLZYYvJwh4 (CoMP) | 3.00 | 1 | Below CoRAL — task-specific, narrower scope |
| vprM1GQdmx (MALLVi) | 3.00 | 1 | Below CoRAL — simpler architecture, fewer tasks |
| MZjccYMFlV (CortexVLA) | 4.50 | 1,2 | Comparable but CoRAL has Figure 4 contradiction |
| QVjyFrXOrn (MoSEL) | 4.50 | 1,2 | Comparable; CoRAL has cleaner ablations but worse central evidence |
| KfaZaYYCvt (Semantic World Models) | 5.00 | 2 | Above CoRAL — methodologically cleaner, no central contradiction |
| Y1VgLHbzCC (PDDLLM) | 5.50 | 2 | Above CoRAL — accepted, sound methodology |
| 4jcnded6fA (BiNoMaP) | 5.33 | 1 | Above CoRAL — more thorough evaluation |
| PGUC3mmMoi (RoboInter) | 7.00 | 2 | Well above CoRAL — large dataset, real-world validation |
| fzmittHfq3 (FALCON) | 6.50 | 2 | Well above CoRAL — stronger contributions, accepted |

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>
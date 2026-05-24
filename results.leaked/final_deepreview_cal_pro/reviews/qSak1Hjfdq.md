---

## Summary
This paper formalizes the All-Day Multi-Scenes Lifelong VLN (AML-VLN) problem, where vision-and-language navigation agents must continually learn across diverse scenes and illumination conditions without forgetting. The authors propose Tucker Adaptation (TuKA), which represents multi-hierarchical navigation knowledge as a 4th-order tensor and uses Tucker decomposition to decouple shared core skills from scene-specific and environment-specific experts. A Decoupled Knowledge Incremental Learning (DKIL) strategy consolidates shared subspaces while constraining task-specific experts. The resulting agent, AllDayWalker, is evaluated on a new AllDay-Habitat benchmark with 24 tasks spanning simulation and real-world scenarios, and consistently outperforms 13 continual-learning adapters and test-time adaptation baselines.

## Strengths
- **Strong empirical results with large margins**: On the 24-task AML-VLN benchmark, AllDayWalker achieves 65% average success rate compared to 52% for the next-best adapter (SD-LoRA), and an average forgetting rate F-SR of only 11% (Table 2). The margin over all baselines is substantial and consistent across tasks.
- **Convincing ablation for 4th-order tensor representation**: Figure 8 demonstrates that the 4th-order tensor (decoupling scene and environment knowledge into separate factor matrices U³, U⁴) consistently outperforms a 3rd-order tensor (which couples scene and environment into a single dimension) across all 20 simulation tasks. This validates the core design choice of multi-hierarchical decoupling.
- **Generalization to unseen scene–environment combinations**: On six completely unseen scenarios with novel scene–environment pairings (Table 5), AllDayWalker achieves 55% average SR, outperforming BranchLoRA (40%) and SD-LoRA (39%) by 15–16 percentage points, demonstrating that the decoupled representation transfers beyond the training distribution.
- **Physically grounded benchmark construction**: The AllDay-Habitat platform extends the Habitat simulator with three imaging degradation models (atmospheric scattering, low-light, overexposure) grounded in real camera physics, providing a reproducible and diverse evaluation platform for multi-environment VLN that is a genuine contribution beyond the method itself.

## Weaknesses

### Fatal
None.

### Major
None. The core claims are well-supported by the evidence presented.

### Minor
- **Negative forgetting values are unexplained**: Table 2 reports F-SR of −3% (T14) and −4% (T20) for AllDayWalker. Since F-SR is defined as (M-SR − SR)/M-SR where M-SR is the joint multi-task training upper bound, negative values mean the continual learner outperforms joint training — an unusual result that warrants discussion (e.g., was M-SR trained to convergence? is there positive transfer between tasks?). The paper offers no explanation, which weakens confidence in the forgetting metric.
- **No standard deviations or significance testing**: Tables 1 and 2 report single-point SR and F-SR values for all methods across 24 tasks. Without standard deviations over multiple runs or statistical significance tests, it is impossible to assess whether the reported margins (especially on near-zero forgetting tasks or noisy low-SR tasks like T2 and T5) are robust to random variation. This is standard practice in the field for navigation benchmarks, but would strengthen the claims.
- **Selective baselines in generalization evaluation**: Table 5 compares generalization only against BranchLoRA and SD-LoRA, omitting other strong performers from Table 1 such as O-LoRA (52% avg. SR) and HydraLoRA (38% avg. SR). Without these comparisons, the generalization advantage claim is less comprehensive than the main results.
- **Hyperparameter sensitivity not analyzed**: The DKIL loss balances three terms with λ₁=0.2, λ₂=0.2, λ₃=0.1 set without ablation or sensitivity analysis. Given that these weights control the trade-off between knowledge consolidation, expert consistency, and orthogonal constraints, understanding their robustness matters for practical adoption.
- **Fisher information computation under-specified**: Equation 5 defines Fisher importance weights via an expectation over task data, but the number of samples used to approximate this expectation and the sampling strategy are not described.

### Trivial
- Table 1 has two missing entries in the SD-LoRA row (T23, T24), which appears to be a rendering artifact.
- The task ordering for the lifelong learning sequence is described only as "randomized"; reporting the exact order (even in appendix) and whether results hold over multiple random orders would improve reproducibility.

## Nice-to-Haves
- Decoupling the contribution of the Tucker architecture from the retrieval mechanism and DKIL strategy: applying the same CLIP-based retrieval and anti-forgetting regularizers to the best MoE-LoRA baseline would isolate how much gain comes from the higher-order tensor representation alone.
- A deeper discussion of when the shared decoder U¹ matters: Table 3 shows sharing U¹ contributes little to performance (63% vs 65% SR), which the paper attributes to storage savings, but a more substantive explanation would add insight.
- Reporting SPL and OSR metrics in tabular form (rather than only radar charts in Figure 7) for precise cross-method comparison.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **"Task-agnostic inference protocol is unclear and likely unfair for baselines"**: The paper explicitly states that task-id is agnostic during testing for all methods (Section 5.1). The MoE-LoRA baselines (HydraLoRA, Dense MoLE, Sparse MoLE, BranchLoRA) use their own learned routing mechanisms that do not require explicit task identification — HydraLoRA sums over all expert B modules, Dense/Sparse MoLE use learned gating, O-LoRA forward-passes through all orthogonal LoRA modules, and SD-LoRA composes from previously learned skills. No oracle task identity is needed, so the comparison is not confounded by a task-identification protocol. This criticism misinterprets how the baseline architectures operate at inference time.

- **"Orthogonal constraint may inadvertently affect old experts"**: The paper states (line 148) that old experts {U³[i,:]} for i≠s and {U⁴[j,:]} for j≠e are frozen during new-task training. Since frozen parameters receive no gradient, the orthogonal loss computed over the full expert matrix only affects the newly trained (unfrozen) rows. The concern is therefore unfounded.

- **"Real-world deployments are unclear — are these physical robot trials?"**: The paper clearly distinguishes simulation tasks (T1–T20, 5 simulation scenes × 4 environments) from real-world tasks (T21–T24, 2 real-world scenes × 2 environments: normal and low-light). The benchmark construction section (Section 5.1) explicitly states this distinction. The term "real-world" refers to captured real scenes (as in standard VLN practice), not physical robot deployments; this is consistent with how the field uses the term.

- **"No parameter counts reported"**: The paper states parameter settings (r=6 for task-specific LoRA, r=16 with K=8 for MoE-LoRA, r=32 with K=8 for shared-A MoE-LoRA, and r₁=r₂=8, r₃=r₄=64 for TuKA) and defers full parameter comparison to Appendix C. Since the appendix is stripped in this version, the information likely exists in the original submission.

- **"Task ordering not reported — essential for lifelong learning"**: The paper states the order is randomized and refers to Appendix §E for details. This is likely addressed in the original submission.

- **"The fidelity of synthetic degradations to real-world imaging conditions is not evaluated"**: This is scope creep — the paper's contribution is using these degradations as a controlled testbed, not validating their photorealism against real camera data.

- **"Limitations not acknowledged in conclusion"**: The paper does not have a dedicated limitations section, but the conclusion paragraph is brief due to space. This is a presentation preference, not a substantive flaw.

- **Demands for appendix content (proofs, detailed results tables, additional figures)**: The parser strips appendices. References to Appendix C (hyperparameters), E (benchmark details), H (3rd-order tensor details), J (5th-order tensors), and K (SPL/OSR tables) point to content that likely exists in the original submission. Criticizing their absence from the stripped copy is not valid.

## Novel Insights
The paper's key insight — that navigation knowledge across scenes and environments is naturally multi-hierarchical (core skills × scene-specific × environment-specific), and that a 4th-order Tucker decomposition provides an architecturally natural way to decouple these dimensions — is genuinely novel in the continual learning literature. The ablation showing that a 3rd-order tensor (which couples scene and environment into one dimension) underperforms the 4th-order variant provides empirical support for this representational argument. This perspective — that the rank/tensor-order of the adaptation method should match the hierarchical structure of the knowledge being represented — may be applicable beyond VLN to other multi-factor continual learning settings.

## Suggestions
- Add standard deviations (over 3+ random seeds) to Tables 1 and 2 to substantiate the significance of the reported margins, particularly for low-SR tasks where noise may dominate.
- Briefly discuss the two negative F-SR values (−3%, −4%) and verify that the joint-training upper bound M-SR was trained to convergence.
- Include O-LoRA and HydraLoRA in the generalization comparison (Table 5) to match the comprehensiveness of the main results table.
- Provide a sensitivity analysis for λ₁, λ₂, λ₃ (even a brief range-check in the appendix) to demonstrate that the method is not brittle to these hyperparameters.

## Score and Decision

**Calibration anchors considered:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| JIlIYIHMuv (LVLM-CL) | 2.50 | R1 | Much weaker — unclear method, poor evaluation |
| WM5G2NWSYC (Projected Subnetworks) | 2.00 | R1 | Much weaker — weak method, limited experiments |
| sb7qHFYwBc (C-CLIP) | 6.50 | R1 | Similar quality — multimodal CL with LoRA, benchmark, strong results |
| rwmwFnmjAX (Continual LLaVA) | 4.75 | R1 | Weaker — limited novelty, reviewer concerns |
| gc8QAQfXv6 (Function Vectors for CF) | 9.00 | R1 | Clearly stronger — deep theoretical analysis, top venue |
| Q5Sawm0nqo (Tucker SFDA) | 6.17 | R2 | Our paper is stronger — broader application, more baselines, benchmark contribution |
| OALIb8oNfl (FLoRA) | 5.75 | R2 | Our paper is stronger — more complete system, lifelong learning, broader evaluation |
| YR79EyejsG (Lifelong Robot Learning) | 5.75 | R2 | Our paper is stronger — cleaner method, more baselines, benchmark contribution |
| G6DLQ40VVR (DivScene) | 6.25 | R2 | Our paper is stronger — both method and benchmark, stronger empirical results |
| bqv7M0wc4x (ICL-TSVD) | 5.50 | R2 | Our paper is stronger — more novel method, broader evaluation |

**Round 1 bracket**: 5.5 – 7.5 (above rejected papers at 2-5, below clearly exceptional papers at 8-9).

**Round 2 narrowing**: Compared against Q5Sawm0nqo (6.17, Tucker decomposition for SFDA), FLoRA (5.75, Tucker for PEFT), DivScene (6.25, navigation benchmark), and C-CLIP (6.50, multimodal CL). The paper under review is methodologically more novel than C-CLIP (Tucker decomposition vs. LoRA+contrastive), has a more comprehensive evaluation (13 baselines), and contributes a benchmark. Its weaknesses (no std devs, unexplained negative forgetting) are modest and addressable. It is comparable to C-CLIP and stronger than the 5.75–6.17 anchors.

**Final score**: 6.5, based on strong methodological novelty, comprehensive empirical validation with large margins, and a useful benchmark contribution, partially offset by the absence of variance reporting and an unexplained anomaly in the forgetting metric.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
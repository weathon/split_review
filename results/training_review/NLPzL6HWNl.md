Now I have a thorough understanding of the paper. Let me write the final consolidated review.

## Summary

This paper identifies three "discordances" that cause LoRA to underperform in privacy-preserving federated learning (FL): (1) aggregation error from separately averaging the two low-rank matrices, (2) noise amplification from the quadratic structure under DP-SGD, and (3) sensitivity to the scaling hyperparameter α. To address these, the paper proposes FFA-LoRA (Federated Freeze-A LoRA), which freezes the randomly initialized A matrix and only trains/shares the B matrix. This halves the trainable parameters, eliminates the aggregation error, reduces noise amplification, and removes α sensitivity. Experiments on RoBERTa classification tasks under differential privacy show that FFA-LoRA substantially outperforms vanilla LoRA, with especially dramatic gains on MNLI (e.g., 78.81% vs 39.46% at ε=6).

## Strengths

- **Mathematically identifies the root cause of LoRA's instability in privacy-preserving FL.** Equations (3)–(4) formally show that separately averaging A and B matrices in FedAvg produces a product term different from the ideal model-averaging update — a concrete, falsifiable explanation for why LoRA underperforms under data heterogeneity.

- **Proposes a simple modification that directly eliminates the identified problems.** FFA-LoRA (freeze A, train B) makes the update linear in trainable parameters: Equation (5) shows that federated averaging of B matrices exactly recovers the intended model update. This simultaneously addresses all three discordances — aggregation error, noise amplification, and α sensitivity — with a single, easily adoptable change.

- **Demonstrates large and consistent gains under differential privacy.** On MNLI (matched) at ε=6, FFA achieves 78.81% vs LoRA's 39.46%, with drastically lower variance (±0.8 vs ±14.3). This pattern holds across all three privacy budgets and all five GLUE tasks, providing strong evidence that FFA is substantially more robust to DP noise.

- **Halves communication and computation costs while improving accuracy.** FFA freezes half the LoRA parameters, reducing trainable parameters by 50% and communication cost proportionally. Despite using fewer parameters, FFA outperforms LoRA in the majority of settings, including when compared at matched parameter budgets (FFA rank 8 vs LoRA rank 16 on SST-2: 94.10% vs 93.98%).

- **Provides a theoretical connection between FFA and large-α LoRA.** Theorem 1 proves that as α → ∞, LoRA's update trajectory converges to FFA's, explaining why FFA is insensitive to α and simplifying hyperparameter tuning.

## Weaknesses

### Fatal
None.

### Major

- **The "consistently outperforms" claim is overstated.** When parameter-matched in the non-private setting (Table 3: FFA rank 16 vs LoRA rank 8, both 1.57M parameters), FFA *underperforms* LoRA on MNLI (matched 85.82% vs 87.01%, mismatched 86.38% vs 87.33%) while outperforming on other tasks. The paper's statement that "the advantage of FFA becomes more apparent" under parameter-matched comparison is not supported by the MNLI results. The core claim of *consistent* superiority requires acknowledging this mixed picture, especially since MNLI is the task with the strongest heterogeneity where the paper's theoretical motivation should apply most clearly.

- **The LLaMA/GSM-8K and Food-101 vision experiments lack essential details.** The LLaMA experiment (Section 5.3) is described in a single paragraph: "Our method has achieved an accuracy of 17.12% ... significantly better than the best performance of LoRA at 15.68%." No details are given for: number of clients, data partitioning scheme, rank, α, learning rate, batch size, local update steps, communication rounds, or how the "best performance" of LoRA was obtained. The vision experiment on Food-101 is dismissed in one sentence as "performs similarly." These experiments cannot be evaluated or used as evidence in their current form. Either remove them or fully document the setup.

- **Promised ablations on α sensitivity and initialization are absent.** The ablation section (Section 4.2) raises the question "How do FFA and LoRA behave when we choose different α for scaling?" and states that "the scaling factor does not affect the overall performance" — but provides no empirical data, table, or figure. The initialization sensitivity question ("How does different initialization on A affect performance?") is raised immediately afterward with no results presented. These are substantive gaps in the experimental evaluation, especially since α sensitivity (Discordance 3) is a core motivation for the method.

- **The paper does not explicitly state that A₀ is shared/broadcast identically to all clients.** The theoretical advantage of FFA in Equation (5) — that averaging B matrices recovers the correct model update — depends on all clients using the *same* A₀. If each client independently samples its own A₀, the aggregation error returns. The paper never clarifies this design choice. This is a critical implementation detail that affects both the theoretical claims and practical deployment.

### Minor

- **The main DP comparison (Table 1) uses equal rank but unequal parameter counts.** Both methods use r=8, but FFA trains half the parameters. The paper provides a partial parameter-matched comparison under DP for QNLI (Table 5), but extending this controlled comparison to all tasks and privacy levels would make the headline DP results more interpretable. (Note: the reviewer's claim that *no* parameter-matched DP comparison exists is incorrect — Table 5 does provide one for QNLI, where FFA wins across all ε levels.)

- **High LoRA variance in Table 1 (up to 10.7% std non-private, 14.3% at ε=6) vs FFA (1.1%, 0.8%) raises questions about tuning.** The paper tests only 4 learning rates for each method. The extreme LoRA variance could partially reflect insufficient hyperparameter search rather than exclusively a structural advantage of FFA. However, the fact that this variance persists even at the *best* learning rate (the reported values are from the best configuration across 20 runs) does indicate genuine instability in LoRA, consistent with the paper's thesis.

- **The noise amplification analysis (Discordance 2) compares noise norms in parameter space rather than impact on the loss.** While the synthetic verification is suggestive, the analysis does not directly connect the amplified parameter noise to optimization or final model quality. This limits the strength of the theoretical motivation for Discordance 2.

### Trivial
None.

## Nice-to-Haves

- Extend the parameter-matched DP comparison (FFA rank 2r vs LoRA rank r) to all five GLUE tasks and all three privacy levels, to fully deconfound the parameter-count effect from the method advantage.
- Provide full experimental specifications for the LLaMA and vision experiments (or remove them if insufficient).
- Add convergence curves (accuracy vs communication rounds) for LoRA and FFA under DP, to illustrate the stability advantage dynamically.
- Present the promised α-ablation and initialization-ablation results with error bars.
- Explicitly state whether A₀ is shared globally or per-client, and discuss the implications if it is per-client.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"Aggregation error is known, not a new observation."* The paper does not claim the individual discordance is novel; the contribution is the synthesis of three discordances in the specific context of privacy-preserving FL and the proposed unified fix. This criticism mischaracterizes the paper's scope.
- *"Figure 1 is a placeholder."* Figures are stripped by the PDF parser; the original submission contains the figure. This is a review artifact, not a paper flaw.
- *"Theorem 1 not proven in main text."* Proofs are deferred to the appendix, which is standard and was stripped by the parser.
- *"Multiple new studies have considered similar approaches, weakening novelty."* The paper itself acknowledges this (line 261) and correctly notes its distinct contribution is the FL+DP analysis. The reviewer's concern is already addressed by the authors.
- *"Discordance 3 explanation is imprecise."* The explanation (lines 185–192) is informal but reasonable for an empirical/systems paper. It provides an intuitive mechanism without claiming formal proof, which is appropriate for the paper's scope.
- *"Formatting/grammar/typography nitpicks."* Removed per policy — these are parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Soften the "consistently outperforms" claim.** Acknowledge that under non-private, parameter-matched conditions on MNLI, LoRA outperforms FFA (85.82 vs 87.01). Reframe the conclusion to state that FFA consistently outperforms LoRA *under differential privacy* and provides better parameter efficiency and robustness to heterogeneity overall, rather than claiming universal superiority.

2. **Provide the missing experimental details** for the LLaMA and vision experiments, or remove them. The current presentation weakens rather than strengthens the paper.

3. **Run and report the α-ablation and initialization-ablation experiments.** These are directly relevant to the paper's claimed advantages (Discordance 3) and their absence is a clear gap.

4. **Explicitly state how A₀ is initialized across clients** — whether it is the same random seed shared globally, or each client uses an independent seed. If the former, state this clearly; if the latter, discuss the implications for the aggregation error analysis.

5. **Add a simple table or figure** comparing FFA rank 2r vs LoRA rank r under DP across all tasks to remove any confound from the unequal-parameter comparison in Table 1.

## Score and Decision

The paper addresses a relevant practical problem with a clean, well-motivated solution and provides strong empirical evidence for its advantages under differential privacy — the gains on MNLI at ε=6 (78.81% vs 39.46%) are genuinely striking. However, the experimental presentation has significant gaps (undocumented LLaMA/vision experiments, missing ablation results), and the core claim of "consistent outperformance" is not fully supported by the parameter-matched non-private comparison. The paper's contributions are real and useful, but it overstates its evidence and omits important implementation and experimental details. With revisions addressing the flagged issues, this could be a solid contribution.

**Score:** 5.5  
**Decision:** Borderline — revisions required to address overclaims and incomplete experiments.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
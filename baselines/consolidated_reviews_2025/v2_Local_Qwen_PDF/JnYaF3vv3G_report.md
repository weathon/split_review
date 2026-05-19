## Summary
# Final Review Report

## Summary
This paper introduces LabelDP-Pro, a novel family of label differential privacy (LabelDP) training algorithms that adapt DP-SGD for settings where only labels are sensitive. By interleaving gradient projection operations with private stochastic gradient descent, the method leverages public input features to denoise gradients, effectively reducing the dimensionality of DP noise from the full model size $d$ to the number of classes $K$. The authors provide a memory-efficient implementation using advanced autodiff primitives, theoretical bounds on excess error for convex optimization, and extensive empirical evaluations on item-level and user-level privacy benchmarks. The results demonstrate significant utility improvements over randomized response and standard DP-SGD in the high-privacy regime ($\epsilon < 1.0$).

## Strengths
1. **Novel Algorithmic Synthesis:** The core idea of projecting DP-SGD gradients onto a subspace spanned by public feature gradients is elegant and well-motivated. It effectively bridges the gap between central DP noise scaling and label-only privacy requirements.
2. **Practical Implementation:** The use of advanced autodiff (JVP/VJP) to compute projections without materializing large gradient matrices is a significant engineering contribution, making the method feasible for deep learning workloads.
3. **Strong Empirical Validation:** The paper provides comprehensive evaluations across multiple datasets (MNIST, CIFAR-10, Criteo) and privacy regimes, consistently demonstrating superior utility in the high-privacy setting compared to strong baselines.
4. **Theoretical Grounding:** The bias-variance analysis and excess error bounds for convex optimization provide a solid theoretical foundation that aligns well with empirical observations, particularly the reduction of dependency from $d$ to $K$.

## Weaknesses
1. **Algorithm Pseudocode Ambiguity:** Algorithm 1 does not explicitly account for the sampling of an alternative batch $I^P_t$ required by the ALTCONV denoiser, which may confuse implementers regarding privacy amplification mechanics.
2. **Hyperparameter Selection Transparency:** The smoothing coefficient $\lambda$ is stated to typically be 0.75, but the selection protocol (fixed heuristic vs. validation tuning) is not clearly specified, potentially affecting reproducibility across datasets.
3. **Theory-Experiment Linkage:** While Table 3 and Table 4 present empirical and theoretical results respectively, the text lacks an explicit discussion connecting the $O(\sqrt{K})$ theoretical bound to the observed empirical gains, leaving the theoretical contribution slightly disconnected.
4. **Crossover Phenomenon Explanation:** The threshold $\epsilon^*$ beyond which RR outperforms LabelDP-Pro is noted but deferred to the appendix. Inline intuition regarding DP-SGD noise floors and projection overhead would strengthen the main narrative.
5. **User-Level Gradient Aggregation:** Section 6 omits details on whether per-user gradients are summed or averaged before clipping, which is critical for fair comparison and reproducibility in user-level DP settings.

## Key Issues
- **Reproducibility of Projection Implementation:** The discrepancy between Algorithm 1 and the ALTCONV denoiser's requirement for an independent batch $I^P_t$ creates ambiguity. Without explicit pseudocode updates, reproducing the privacy amplification benefits may be error-prone.
- **Hyperparameter Sensitivity:** The reliance on $\lambda=0.75$ without a clear tuning protocol raises concerns about robustness across different model architectures and privacy budgets. If $\lambda$ is dataset-dependent, the method's practicality may be reduced.
- **Theoretical-Practical Gap:** The convex optimization bounds in Table 4 are informative but do not directly address the non-convex deep learning setting. A brief discussion on how the $O(\sqrt{K})$ scaling translates to empirical deep learning gains would bridge this gap.
- **User-Level DP Protocol Clarity:** The lack of specification regarding per-user gradient aggregation (sum vs. average) and clipping order is a critical reproducibility issue for the user-level experiments in Section 6.

## Actionable Suggestions
1. **Update Algorithm 1:** Explicitly include the sampling of an alternative batch $I^P_t$ in the pseudocode or add a clear comment indicating that the Denoiser may internally sample additional public features for projection.
2. **Clarify $\lambda$ Selection:** State whether $\lambda=0.75$ is a fixed default or selected via validation. If tuned, report the search range and protocol to ensure reproducibility.
3. **Bridge Theory and Experiments:** Add a paragraph explicitly linking the $O(\sqrt{K})$ theoretical bound to the empirical results in Table 3, explaining how dimensionality reduction and amplification by subsampling jointly drive utility gains.
4. **Explain $\epsilon^*$ Crossover:** Provide inline intuition for why RR outperforms LabelDP-Pro at larger $\epsilon$, focusing on the diminishing returns of projection when DP-SGD noise is already minimal.
5. **Specify User-Level Aggregation:** Clearly define whether per-user gradients are summed or averaged, and confirm that clipping is applied per-user before aggregation to maintain fair comparison with baselines.

## Storyline Options + Writing Outlines
**Abstract Outline:**
- S1: Define LabelDP and its motivation (public features, private labels).
- S2: Highlight the challenge of high-privacy regimes where RR fails due to exponential noise scaling.
- S3: Introduce LabelDP-Pro: adapting DP-SGD via gradient projection onto public feature subspaces.
- S4: State key empirical gains (e.g., accuracy at $\epsilon=0.1$) and theoretical bounds ($O(\sqrt{K})$ vs $O(\sqrt{d})$).
- S5: Conclude with practical impact on item-level and user-level privacy applications.

**Introduction Outline:**
- P1: Establish DP importance and the asymmetric sensitivity of real-world data (e.g., advertising).
- P2: Contrast RR's local DP limitations with DP-SGD's central DP advantages, highlighting the noise scaling gap.
- P3: Propose LabelDP-Pro as a synthesis: leveraging public features to denoise DP-SGD gradients via projection.
- P4: Summarize contributions: method, efficient autodiff implementation, theoretical bounds, and empirical SOTA results.
- P5: Preview structure and key findings, emphasizing the high-privacy regime focus.

## Priority Revision Plan
| Priority | Action | Expected Impact |
|---|---|---|
| P0 | Update Algorithm 1 to include alternative batch sampling $I^P_t$ for ALTCONV. | Resolves reproducibility ambiguity and clarifies privacy amplification mechanics. |
| P0 | Specify per-user gradient aggregation (sum vs. average) and clipping order in Section 6. | Ensures fair comparison and reproducibility for user-level DP experiments. |
| P1 | Clarify $\lambda$ selection protocol (fixed vs. tuned) in Section 3.3. | Improves method robustness and reproducibility across datasets. |
| P1 | Add inline explanation for $\epsilon^*$ crossover phenomenon in Section 5.2. | Strengthens narrative coherence and demonstrates deeper method understanding. |
| P2 | Explicitly link Table 3 empirical gains to Table 4 theoretical $O(\sqrt{K})$ bounds. | Bridges theory-experiment gap and reinforces contribution impact. |

## Experiment Inventory & Research Experiment Plan
**Completed Experiment Inventory:**
| Exp ID | Objective | Setup | Metrics | Outcome | Limitation |
|---|---|---|---|---|---|
| E1 | Item-level LabelDP utility | MNIST, CIFAR-10, $\epsilon \in [0.01, 2.0]$ | Accuracy | LabelDP-Pro > RR/DP-SGD at low $\epsilon$ | Limited to image benchmarks |
| E2 | Denoiser ablation | MNIST, SELF SPAN/CONV vs ALTCONV | Accuracy | ALTCONV best due to amplification | No variance reporting |
| E3 | User-level DP utility | Criteo, $k \in \{2,5,10\}$ | AUC | Consistent gains over RR | Single real-world dataset |
| E4 | SelfSL integration | CIFAR-10 + SimCLR | Accuracy | High utility with public features | Relies on visual priors |

**Proposed Research Experiments:**
1. **Variance & Significance Testing (P0):** Report mean $\pm$ std over $\ge 3$ seeds for all main results to establish statistical reliability.
2. **Non-Visual Domain Evaluation (P1):** Test LabelDP-Pro on tabular/text datasets (e.g., Adult, AG News) to verify generalization beyond image-specific SelfSL priors.
3. **Hyperparameter Sensitivity Analysis (P1):** Sweep $\lambda$ and projection steps across datasets to demonstrate robustness or provide tuning guidelines.

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 7.5/10
The paper presents a novel and practically impactful method for label differential privacy, with strong empirical results and solid theoretical grounding. The core idea of projection-based denoising is elegant and well-executed. However, minor ambiguities in algorithm pseudocode, hyperparameter selection, and user-level gradient aggregation slightly reduce reproducibility confidence. Addressing these issues would significantly strengthen the manuscript.

**Post-Revision Target:** [8.5, 9.0]/10
With clear pseudocode updates, explicit hyperparameter protocols, and variance reporting, the paper would achieve high reproducibility and robustness standards, making it a strong contribution to the private ML community.
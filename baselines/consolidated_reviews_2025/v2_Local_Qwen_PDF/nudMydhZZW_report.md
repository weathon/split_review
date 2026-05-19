## Summary
# Final Review Report

## Summary
This paper investigates distributed temporal difference (TD) learning for networked multi-agent Markov decision processes (MAMDPs) from a primal-dual ODE dynamics perspective. The authors propose a distributed TD-learning algorithm inspired by control-system frameworks (Wang and Elia, 2011) that avoids the doubly stochastic matrix assumption required by many existing methods. By establishing exponential convergence for the continuous-time primal-dual dynamics under null-space constraints, the paper derives finite-time mean-squared error bounds for the discrete algorithm under both i.i.d. and Markovian observation models. Theoretical results are supported by empirical demonstrations on cycle and star graph topologies, validating the dependence of convergence rates on graph connectivity and the role of a tunable scaling parameter $\eta$.

## Strengths
1. **Theoretical Rigor:** The paper provides a solid finite-time analysis of distributed TD-learning under both i.i.d. and Markovian observation models, deriving explicit mean-squared error bounds that depend on graph connectivity and step-size schedules.
2. **Algorithmic Flexibility:** By leveraging a control-system-inspired primal-dual framework, the proposed algorithm removes the doubly stochastic matrix assumption, enabling application to directed and time-varying networks without major modifications.
3. **Practical Tuning Insight:** The introduction of the scaling parameter $\eta$ offers a practical mechanism to balance consensus and dual updates, with theoretical and empirical guidance on its spectral scaling relative to the graph Laplacian.
4. **Clear Mathematical Structure:** The use of Lyapunov analysis with projected dual variables ($\bar{L}\bar{L}^\dagger$) effectively handles the rank-deficiency of the graph Laplacian, demonstrating a clean and reproducible theoretical approach.

## Weaknesses
1. **Abstract Lacks Concrete Results:** The abstract does not state the achieved convergence rate or the specific form of the mean-squared error bound, reducing its effectiveness as a standalone summary.
2. **Introduction Gap Statement is Implicit:** The motivation for the new analysis is not sharply contrasted with prior limitations (e.g., doubly stochastic constraints, restrictive initialization), making the contribution feel incremental rather than necessary.
3. **Related Work is List-Style:** The literature review reads as a chronological summary rather than a structured synthesis by framework category, failing to explicitly differentiate the proposed approach from strongest baselines.
4. **Markovian Analysis Fixes $\eta=1$:** The Markovian case simplifies the proof by fixing $\eta=1$ without justification, creating a disconnect with the i.i.d. tuning guidance and weakening the generality of the results.
5. **Experiments Lack Main-Text Baselines:** Direct comparison with baseline distributed TD algorithms is deferred to the appendix, reducing the immediate empirical impact and reproducibility of the novelty claim.

## Key Issues
1. **Claim-Evidence Alignment in Abstract:** The abstract promises finite-time analysis but omits the actual convergence rates ($O(\exp(-\alpha_0 k))$ and $O(1/k)$), leaving readers without a clear scientific payoff.
2. **Novelty Positioning in Introduction:** The gap between existing doubly stochastic/gradient-tracking methods and the proposed control-system approach is not explicitly articulated, weakening the motivation for the new framework.
3. **Reproducibility of $\eta$ Tuning:** While $\eta$ is introduced for variance control, the lack of a concrete tuning rule or theoretical bound in the main text may hinder practical implementation and fair comparison.
4. **Empirical Validation Scope:** Deferring baseline comparisons to the appendix reduces the persuasiveness of the experimental section. Main-text validation against at least one representative baseline is necessary to substantiate the claimed advantages.

## Actionable Suggestions
1. **Revise Abstract:** Add one sentence explicitly stating the convergence rates (exponential with bounded bias under constant step-size, $O(1/k)$ under diminishing step-size) and the key advantage (removal of doubly stochastic matrix assumption).
2. **Sharpen Introduction Gap:** Explicitly contrast prior works (relying on doubly stochastic matrices or gradient tracking) with the proposed control-system approach, highlighting the limitation of existing methods on directed/time-varying networks.
3. **Restructure Related Work:** Organize by framework category (doubly stochastic averaging vs. control-system/primal-dual) and explicitly state how this paper differs from the strongest baselines in assumptions and convergence guarantees.
4. **Clarify $\eta$ Tuning:** Add a brief remark or proposition linking $\eta$ to the graph Laplacian spectrum (e.g., $\eta \approx \sqrt{2}/\lambda_{\max}(L)$) and reference experimental findings to bridge theory and practice.
5. **Include Baseline Comparison in Main Text:** Move at least one comparative plot or table (e.g., vs. Doan et al., 2019) to the main experiments section to strengthen empirical validation and reproducibility.
6. **Expand Conclusion:** Summarize validated findings, acknowledge limitations (undirected graph assumption, linear approximation), and outline prioritized future work (directed networks, nonlinear approximators, policy optimization).

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem & Domain):** Distributed TD-learning for networked MAMDPs enables cooperative policy evaluation without centralized data aggregation.
- **S2 (Significance/Challenge):** Existing methods rely on doubly stochastic mixing matrices, limiting applicability to directed or time-varying networks and complicating implementation.
- **S3 (Prior Gap):** Finite-time analyses for control-system-inspired primal-dual dynamics under null-space constraints remain underexplored, particularly for stochastic TD settings.
- **S4 (Proposed Method):** We propose a distributed TD algorithm leveraging primal-dual ODE dynamics, eliminating doubly stochastic requirements while maintaining rigorous convergence guarantees.
- **S5 (Key Result & Implication):** We derive explicit mean-squared error bounds showing exponential convergence under constant step-sizes and $O(1/k)$ rates under diminishing step-sizes, validated empirically across diverse graph topologies.

### Introduction Outline (Complete)
- **P1 (Big Picture):** TD-learning is foundational for RL; distributed variants enable scalable multi-agent policy evaluation.
- **P2 (Concrete Gap):** Prior distributed TD algorithms depend on doubly stochastic averaging or gradient tracking, inheriting constraints that hinder deployment on directed/time-varying networks.
- **P3 (Proposed Idea):** Control-system-based primal-dual dynamics offer a flexible alternative, naturally handling rank-deficient Laplacians without doubly stochastic normalization.
- **P4 (Evidence Preview):** We establish finite-time bounds under i.i.d. and Markovian observations, demonstrating favorable scaling with graph connectivity and tunable variance control via $\eta$.
- **P5 (Contribution Summary):** (1) Theoretical advance on primal-dual dynamics with null-space constraints; (2) Algorithmic design removing doubly stochastic requirements; (3) Finite-time error bounds and empirical validation.

## Priority Revision Plan
| Priority | Action Item | Expected Impact | Effort |
|---|---|---|---|
| **P0** | Revise Abstract to include concrete convergence rates and key advantage. | Improves self-containment and reader engagement. | Low |
| **P0** | Sharpen Introduction gap statement by contrasting with doubly stochastic/gradient-tracking limitations. | Strengthens motivation and novelty positioning. | Low |
| **P1** | Restructure Related Work by framework category and explicitly differentiate from baselines. | Clarifies literature positioning and contribution boundaries. | Medium |
| **P1** | Add $\eta$ tuning guidance (spectral scaling rule) and link to experiments. | Enhances reproducibility and practical utility. | Low |
| **P1** | Include at least one baseline comparison plot/table in main experiments. | Strengthens empirical validation and persuasiveness. | Medium |
| **P2** | Expand Conclusion to summarize findings, state limitations, and outline future work. | Provides clear takeaway and research roadmap. | Low |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | Validate bias dependence on graph connectivity ($\lambda_{\min}^+$) | Cycle graph, $N \in \{8, 16, 32\}$, constant step-size | Mean-squared error | Error increases as $N$ grows, matching Theorem 4.2 | Yes | No baseline comparison |
| E2 | Validate bias dependence on $\lambda_{\max}(L)$ | Star graph, varying $N$, diminishing step-size | Mean-squared error | Error scales with $N$, consistent with bound | Yes | Limited topology variety |
| E3 | Verify $\eta$ tuning effect on stability/bias | Random graph, $N=32$, varying $\eta$ | Mean-squared error | Optimal $\eta \approx \sqrt{2}/\lambda_{\max}(L)$; divergence if $\eta$ too small/large | Yes | No theoretical bound provided |

### Research-Theme Gap Diagnosis
The current experiments validate theoretical bounds but lack direct comparison with baseline distributed TD algorithms (e.g., Doan et al., 2019; Wang et al., 2020). This gap weakens the empirical support for the claimed advantage of removing doubly stochastic constraints. Additionally, experiments are limited to undirected graphs, whereas the algorithm's extension to directed networks is a key motivation.

### Proposed Research Experiments
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|---|---|---|---|---|---|---|---|
| Algorithmic advantage over doubly stochastic methods | Proposed algorithm converges faster/with lower bias on directed/time-varying graphs | Compare on directed cycle and time-varying random graphs | Doan et al. (2019), Wang et al. (2020) | MSE, convergence time | Outperforms baselines or remains stable when baselines diverge | Medium | Strengthens novelty claim |
| $\eta$ tuning robustness | Spectral scaling rule $\eta \approx c/\lambda_{\max}(L)$ generalizes across topologies | Sweep $\eta$ on grid, ring, and small-world graphs | Fixed $\eta=1$ baseline | MSE, stability threshold | Consistent optimal $\eta$ range across graphs | Low | Improves reproducibility |
| Directed graph extension | Algorithm maintains convergence without doubly stochastic construction | Apply to directed cycle and random directed graphs | N/A (theoretical validation) | MSE, consensus error | Converges to correct value function | Medium | Validates key motivation |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6.5/10

**Rationale:** The paper presents a theoretically sound distributed TD-learning algorithm with rigorous finite-time analysis under both i.i.d. and Markovian settings. The removal of the doubly stochastic matrix assumption is a meaningful contribution that broadens applicability to directed and time-varying networks. However, the score is moderated by the lack of concrete result statements in the abstract, implicit gap positioning in the introduction, list-style related work, and absence of main-text baseline comparisons. These issues reduce the immediate impact and reproducibility of the claims.

**Post-Revision Target:** [7.5, 8.5]/10

**Path to Target:** Addressing the P0/P1 revision items (abstract/result clarity, introduction gap sharpening, related work restructuring, $\eta$ tuning guidance, and main-text baseline comparison) would significantly strengthen the paper's narrative, empirical validation, and practical utility, justifying a score increase to the strong accept range.
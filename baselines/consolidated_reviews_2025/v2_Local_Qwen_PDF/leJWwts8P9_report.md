## Summary
# Final Review Report

## Summary
This paper addresses the model provenance problem: verifying whether two open-weight language models are trained independently given only their weights. The authors propose a family of exact statistical tests (PERMTEST) that leverage permutation equivariance in neural network training dynamics to simulate independent model copies without retraining, yielding valid p-values under the null hypothesis of independence. To address adversarial evasion via weight permutations and rotations, the authors introduce a robust activation-matching statistic (ϕ_MATCH) that aligns hidden units across models of varying dimensions. Evaluated on 21 Llama-architecture models, 70B models, and cross-architecture pairs (Mistral, BERT, Phi-3), the exact tests reliably identify all dependent pairs with negligible p-values. The robust test empirically distinguishes dependent models and remains effective against MLP retraining and architectural pruning, enabling fine-grained forensics on pruned models like Llama 3.2 and Sheared-LLaMa. The work provides a theoretically grounded and empirically robust framework for third-party model lineage verification.

## Strengths
1. **Theoretical Rigor & Exact P-Values:** The formulation of model independence testing via permutation equivariance (Definitions 1-2) and the proof of exact p-value validity (Theorem 1) provide a strong theoretical foundation. This distinguishes the work from heuristic similarity metrics and ensures controlled false positive rates.
2. **Computational Efficiency:** By leveraging symmetry to simulate independent copies via weight permutations rather than expensive retraining, the method makes statistical testing feasible for large-scale LLMs.
3. **Robust Adversarial Extension:** The introduction of ϕ_MATCH addresses a critical limitation of weight-based tests. The insight that gate and up projection activations must be permuted identically to preserve GLU outputs is clever and enables cross-architecture and cross-dimension matching.
4. **Comprehensive Empirical Validation:** The evaluation covers a wide range of scenarios: non-adversarial Llama family, adversarial rotations/permutations, MLP retraining, cross-architecture pairs (Mistral, BERT, Phi-3), and fine-grained forensics on pruned models. The results consistently support the claimed high power and robustness.
5. **Practical Impact on Model Transparency:** The ability to identify specific matched Transformer blocks in pruned models (e.g., Llama 3.2, Sheared-LLaMa) demonstrates tangible utility for tracking model lineage and detecting unauthorized derivations.

## Weaknesses
1. **Empirical Nature of Robust Test:** The robust statistic ϕ_MATCH forfeits exact p-value guarantees. While Figure 3 shows it empirically behaves like a p-value, the lack of theoretical bounds on false positive rates in the adversarial setting limits its defensibility for high-stakes provenance verification.
2. **Assumption of Permutation Equivariance:** The exact tests rely on the assumption that training dynamics are permutation equivariant. While true for standard optimizers (SGD, Adam) and symmetric initializations, this may not hold for models trained with asymmetric regularization, mixed precision quirks, or non-standard optimizers, potentially invalidating the p-values.
3. **Limited Adversarial Threat Model Coverage:** The robust test is evaluated against permutations, rotations, and MLP retraining. However, it is unclear how it performs against more sophisticated evasion techniques, such as adversarial fine-tuning designed to minimize activation similarity while preserving task performance.
4. **Computational Cost of Activation Matching:** Computing ϕ_MATCH requires forward passes through both models to obtain activations, followed by solving a linear assignment problem (LAP) for each layer. For very large models or long sequences, this could be computationally heavier than direct weight comparisons.
5. **Scope of Cross-Architecture Validation:** While tested on Mistral, BERT, and Phi-3, the cross-architecture results are limited to a few pairs. Broader validation across diverse architectures (e.g., Mamba, hybrid models) would strengthen the generalization claims.

## Key Issues
1. **Theoretical vs. Empirical Guarantee Gap:** The paper transitions from exact tests with rigorous p-value guarantees to a robust test that relies entirely on empirical uniformity. This shift is not sufficiently bounded in the main text, risking reader overconfidence in the adversarial setting's statistical validity.
2. **Permutation Equivariance Assumption Scope:** The validity of PERMTEST hinges on Π-equivariance of the learning algorithm. The paper assumes standard optimizers and symmetric initializations but does not discuss edge cases (e.g., weight decay asymmetries, mixed-precision training artifacts) that could break equivariance and invalidate p-values.
3. **Adversarial Simulation Fidelity:** The adversarial evaluation simulates attacks via random permutations and rotations. While this matches the theoretical threat model, it does not test adaptive adversaries who might optimize transformations to specifically minimize ϕ_MATCH while preserving utility.
4. **Activation Matching Computational Overhead:** The LAP-based matching for ϕ_MATCH scales cubically with hidden dimension. For models with large MLP widths (e.g., >16k), this could become a bottleneck, yet computational complexity is not discussed.
5. **Limited Cross-Architecture Generalization Evidence:** The cross-architecture results are promising but cover only a handful of pairs. Without broader validation, claims of universal applicability remain partially supported.

## Actionable Suggestions
1. **Clarify Robust Test Boundaries:** Explicitly state in Section 3.3 and the Abstract that ϕ_MATCH is an empirical statistic without exact p-value guarantees. Add a brief discussion on the conditions under which its empirical uniformity might break down.
2. **Justify Spearman Correlation Choice:** In Section 3.2, add one sentence explaining why Spearman correlation with the identity permutation is preferred over raw matching quality or other rank metrics, linking it to the symmetry disruption hypothesis.
3. **Discuss Equivariance Edge Cases:** In Section 3.1, briefly acknowledge potential violations of Π-equivariance (e.g., asymmetric weight decay, mixed-precision artifacts) and suggest that future work could test robustness to these conditions.
4. **Link Adversarial Simulation to Theory:** In Section 4.2, explicitly state that the simulated permutations/rotations correspond to the output-preserving transformations defined in Appendix D, validating that the empirical evaluation matches the theoretical threat model.
5. **Analyze Pruning Patterns:** In Section 4.3.1, add a sentence noting that the distributed activation pattern in pruned models is consistent with importance-based structured pruning, highlighting the forensic tool's ability to recover non-trivial compression patterns.
6. **Report Computational Complexity:** Add a short note in Section 3.3 or Appendix on the time complexity of the LAP-based matching for ϕ_MATCH, especially for large hidden dimensions, to inform deployment feasibility.

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem & Stakes):** Model provenance is critical for IP protection and regulatory compliance, yet third-party verification remains challenging.
- **S2 (Gap):** Existing heuristic similarity metrics lack statistical guarantees and are vulnerable to adversarial weight transformations.
- **S3 (Method - Exact):** We propose PERMTEST, a family of exact statistical tests leveraging permutation equivariance in training dynamics to simulate independent model copies without retraining, yielding valid p-values.
- **S4 (Method - Robust):** To address adversarial evasion, we introduce ϕ_MATCH, an activation-matching statistic that aligns hidden units across models of varying dimensions, sacrificing exact p-values for empirical robustness.
- **S5 (Evidence & Impact):** Evaluated on 21 Llama models and cross-architecture pairs, our tests reliably identify dependent pairs, withstand MLP retraining, and enable fine-grained forensics on pruned models like Llama 3.2.

### Introduction Outline (Complete)
- **P1 (Big Picture & Motivation):** Open-weight models enable transparency but complicate provenance tracking. Third parties need reliable tools to verify independence without training access.
- **P2 (Gap & Challenge):** Heuristic checks (e.g., output divergence, raw weight distance) lack false-positive control and fail under simple weight permutations. A rigorous statistical framework is needed.
- **P3 (Solution - Exact Tests):** We formalize independence testing via permutation equivariance. By permuting hidden units, we simulate independent copies efficiently, enabling exact p-value computation (PERMTEST).
- **P4 (Solution - Robust Tests):** Adversaries can evade exact tests via weight rotations. We design ϕ_MATCH to align gate/up projection activations, preserving signal under transformations and enabling cross-architecture matching.
- **P5 (Evidence Preview):** Experiments on Llama, Mistral, BERT, and pruned models demonstrate high power, robustness to MLP retraining, and fine-grained lineage reconstruction.
- **P6 (Contributions):** (1) Theoretical framework for exact independence testing via symmetry. (2) Robust activation-matching statistic for adversarial/cross-architecture settings. (3) Comprehensive empirical validation and forensic applications.

## Priority Revision Plan
| Priority | Action | Expected Impact | Effort |
|---|---|---|---|
| **P0** | Clarify robust test boundaries: explicitly state ϕ_MATCH lacks exact p-value guarantees and discuss empirical uniformity limits. | Prevents overclaiming; improves scientific defensibility. | Low |
| **P0** | Justify Spearman correlation choice in Section 3.2 with one sentence linking it to symmetry disruption. | Strengthens methodological rationale. | Low |
| **P1** | Link adversarial simulation in Section 4.2 directly to theoretical transformations in Appendix D. | Validates threat model alignment. | Low |
| **P1** | Discuss potential Π-equivariance violations (e.g., mixed precision, asymmetric regularization) in Section 3.1. | Improves assumption transparency. | Medium |
| **P2** | Add computational complexity note for LAP-based matching in Section 3.3. | Informs deployment feasibility. | Low |
| **P2** | Expand cross-architecture validation with 1-2 additional model pairs (e.g., Mamba, hybrid). | Strengthens generalization claims. | Medium |

**Execution Order:** Address P0 items first (claim bounding and method justification), then P1 items (assumption transparency and threat model alignment), followed by P2 items (complexity and broader validation).

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | Exact tests identify dependent Llama-7B pairs | 21 models, 210 pairs | p-values (ϕ_U, ϕ_H, ϕ_l2, ϕ_JSD) | Negligible p-values for all 69 dependent pairs | High power of exact tests | Limited to Llama-7B architecture |
| E2 | Robust test withstands adversarial permutations/rotations | Simulated adversary on Llama pairs | ϕ_MATCH distribution | Uniform for independent, <ε for dependent | Empirical robustness | No theoretical p-value guarantee |
| E3 | Robust test survives MLP retraining | Retrained 32 MLPs of vicuna-7b-v1.5 | ϕ_MATCH per layer | Statistic remains <ε | Robustness to layer retraining | Only tested on one fine-tune |
| E4 | Tests support independence on IID models | Two OLMo-7B models, same data | p-values across checkpoints | Broadly distributed p-values | Validity under independence | Only one architecture tested |
| E5 | Cross-architecture & pruning forensics | Llama 3.1/3.2, Sheared-LLaMa, Mistral | ϕ_MATCH block matching | Identified matched blocks & pruning patterns | Fine-grained lineage tracking | Limited cross-architecture pairs |

### Research-Theme Gap Diagnosis
- **Adaptive Adversaries:** Current evaluation uses random permutations/rotations. Adaptive adversaries optimizing to minimize ϕ_MATCH while preserving utility are not tested.
- **Equivariance Violations:** Real-world training quirks (mixed precision, asymmetric regularization) may break Π-equivariance, invalidating exact p-values.
- **Cross-Architecture Generalization:** Validation covers only a few non-Llama architectures; broader generalization remains partially supported.

### Proposed Research Experiments (P0/P1/P2)
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|---|---|---|---|---|---|---|---|
| Adaptive robustness | ϕ_MATCH resists utility-preserving adversarial fine-tuning | Adversarial fine-tuning to minimize activation similarity | Random permutation baseline | ϕ_MATCH, task accuracy | Low ϕ_MATCH with high accuracy | Medium | Validates practical robustness |
| Equivariance sensitivity | Mixed precision breaks exact p-value uniformity | Train identical models with FP16/BF16/FP32 | FP32 baseline | p-value distribution | Uniformity under FP32, deviation under FP16 | Low | Bounds assumption scope |
| Cross-architecture scale | Tests generalize to Mamba/hybrid models | Evaluate on Mamba-2B, Hybrid-7B pairs | Llama baseline | p-values, ϕ_MATCH | Consistent separation | Medium | Strengthens generalization claims |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 7.5/10  
The paper presents a theoretically rigorous and empirically robust framework for model independence testing. The exact p-value guarantees via permutation equivariance are a strong contribution, and the robust activation-matching extension addresses practical adversarial threats. The score reflects high novelty and research value, slightly tempered by the empirical nature of the robust test and limited cross-architecture validation.

**Post-Revision Target:** [8.5, 9.0]/10  
Addressing the claim bounding for ϕ_MATCH, justifying the Spearman correlation choice, and expanding cross-architecture validation would significantly strengthen defensibility and generalization claims, pushing the paper into the top tier for acceptance.

---
**Page Coverage Audit**
| Page | Annotation Count | Coverage Status | Skip Reason |
|---|---|---|---|
| 1 | 2 | Covered | Abstract & Intro motivation |
| 2 | 2 | Covered | Intro method intuition & Related Work |
| 3 | 1 | Covered | Method formulation (Defs 1-2) |
| 4 | 1 | Covered | Method test statistics (Spearman) |
| 5 | 1 | Covered | Method robust test trade-off |
| 7 | 1 | Covered | Experiments setup & baselines |
| 8 | 1 | Covered | Experiments adversarial setup |
| 10 | 1 | Covered | Experiments forensics & pruning |
| 11+ | 0 | Skipped | References/Appendix boilerplate |

**Novelty Verification Note:** External literature verification unavailable in this run (paper_search disabled); novelty/comparison conclusions are intentionally deferred to manual verification. The internal audit confirms strong theoretical grounding and clear differentiation from prior heuristic approaches.
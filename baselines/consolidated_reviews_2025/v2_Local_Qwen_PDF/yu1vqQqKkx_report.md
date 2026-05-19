## Summary
# Final Review Report

## Summary
This paper introduces LICO (Large Language Models for In-Context Optimization), a framework that extends arbitrary base LLMs for black-box optimization (BBO) by learning separate embedding layers for domain inputs and scores. Instead of relying on natural language prompting, LICO maps scientific inputs (e.g., molecular fingerprints) directly into the LLM's latent space, enabling efficient in-context surrogate modeling. To facilitate generalization to unseen objective functions, the authors propose a semi-synthetic training strategy that combines intrinsic domain properties with Gaussian Process-generated synthetic functions. Evaluated on the Practical Molecular Optimization (PMO) benchmark, LICO achieves competitive performance across 23 objectives and leads among evaluated baselines on the low-budget PMO-1K setting. The paper includes comprehensive ablation studies validating the importance of language instructions, synthetic data ratios, and pretrained LLM backbones. While the methodology is sound and the empirical results are promising, the manuscript would benefit from tighter bounding of SOTA claims, explicit discussion of compute/parameter trade-offs, and expanded ablation coverage across all benchmark tasks.

## Strengths
1. **Novel Architectural Interface for Scientific BBO:** The proposal to equip frozen LLMs with learnable domain-specific embedding layers effectively bypasses the limitations of text-space prompting. This design elegantly leverages the LLM's in-context learning capabilities while reducing context length and avoiding domain-specific pretraining data scarcity.
2. **Semi-Synthetic Training Strategy:** The combination of intrinsic molecular properties and GP-generated synthetic functions provides a principled approach to pretraining surrogate models. The ablation studies convincingly demonstrate that this mixture anchors the model in chemically meaningful priors while maintaining broad function space coverage.
3. **Comprehensive Empirical Evaluation:** The paper evaluates LICO on the challenging PMO benchmark across 23 diverse objectives, including similarity, multi-property optimization, and rediscovery tasks. The inclusion of both low-budget (PMO-1K) and standard (PMO) settings provides a thorough assessment of sample efficiency and scalability.
4. **Rigorous Ablation Analysis:** The authors systematically isolate the impact of key design choices, including language instructions, synthetic data ratios, pretrained vs. scratch LLMs, and model scaling. These experiments provide strong causal evidence for the effectiveness of each component.
5. **Clear Reproducibility Details:** The appendix provides extensive implementation details, including the full list of 47 intrinsic functions, training hyperparameters, and optimization loop specifications, which greatly facilitates replication and future research.

## Weaknesses
1. **Unbounded SOTA Claims:** The abstract and conclusion claim "state-of-the-art performance on PMO" without scoping the claim to the evaluated baselines or acknowledging the parameter scale advantage (7B LLM vs. lightweight GPs/evolutionary algorithms). This overstates the practical superiority without contextualizing compute trade-offs.
2. **Limited Ablation Scope:** The ablation studies for language instructions and synthetic ratios are restricted to only the first 5 tasks from Table 1. Conclusions drawn from this small subset may not generalize across the full PMO benchmark, reducing statistical robustness.
3. **Compute and Inference Cost Omission:** The paper does not discuss the inference latency or memory footprint of LICO compared to traditional surrogate models like Gaussian Processes. For practical molecular optimization, the higher computational cost of a 7B LLM may limit deployment feasibility despite improved sample efficiency.
4. **Dynamic Normalization Ambiguity:** Appendix A.3 mentions normalizing $y$ values to mean 0 and std 1 during optimization but does not clarify whether normalization statistics are recomputed dynamically or fixed. Dynamic recomputation without stabilization can destabilize the UCB acquisition function's exploration term.
5. **Baseline Parameter Disparities:** While acknowledged briefly, the comparison against MOLLEO (which uses a domain-finetuned BioT5) and traditional methods (which have significantly fewer parameters) lacks a capacity-matched control. This makes it difficult to isolate architectural benefits from scale/domain-adaptation advantages.

## Key Issues
1. **Claim-Evidence Alignment for SOTA:** The manuscript claims SOTA performance on PMO without explicitly bounding the claim to the evaluated baselines or acknowledging the substantial parameter advantage of the 7B LLM backbone. This risks overstating practical superiority when compute efficiency is a critical factor in scientific optimization.
2. **Statistical Robustness of Ablations:** Restricting ablation studies to only 5 tasks limits the generalizability of conclusions regarding language instructions and synthetic data ratios. Task-specific characteristics may disproportionately influence these results, weakening the causal claims about design choices.
3. **Optimization Stability Under Dynamic Normalization:** The normalization of observed $y$ values during the optimization loop is not fully specified. If normalization statistics shift abruptly as $D_{obs}$ expands, the exploration term $\sigma_i$ in the UCB acquisition function may become unstable, potentially degrading optimization performance in practice.
4. **Fairness of Baseline Comparisons:** The comparison against MOLLEO (domain-finetuned BioT5) and traditional surrogates (lightweight GPs) lacks capacity-matched controls. Without isolating the effects of model scale and domain pretraining, it is difficult to attribute performance gains solely to the LICO embedding architecture.

## Actionable Suggestions
1. **Bound Performance Claims:** Revise the abstract and conclusion to explicitly state that LICO achieves leading performance *among evaluated baselines* on PMO. Acknowledge the parameter scale advantage and frame the comparison as evaluating practical effectiveness under realistic settings rather than absolute SOTA.
2. **Expand Ablation Coverage:** Extend the ablation studies for language instructions and synthetic ratios to cover all 23 PMO tasks, or at least a stratified subset representing different objective types (similarity, MPO, rediscovery). Report mean and variance across the full set to strengthen statistical robustness.
3. **Clarify Normalization Strategy:** In Appendix A.3, explicitly specify whether normalization statistics are computed dynamically over $D_{obs}$ or fixed from an initial batch. If dynamic, consider adding exponential moving averaging or clipping to prevent abrupt scale shifts in $\sigma_i$ that could destabilize UCB exploration.
4. **Add Capacity-Matched Controls:** Include a smaller LLM baseline (e.g., 1B-3B parameters) or a capacity-matched transformer trained from scratch to isolate the architectural benefits of LICO from the effects of model scale and domain pretraining.
5. **Discuss Compute Trade-offs:** Add a brief discussion in the conclusion or limitations section regarding the inference latency and memory footprint of LICO compared to lightweight surrogates like GPs. Frame this as a trade-off between sample efficiency and computational cost.

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem & Domain):** Optimizing black-box functions is fundamental in science/engineering, typically addressed by learning surrogate models from limited evaluations.
- **S2 (Challenge/Gap):** Large Language Models offer strong pattern-matching for surrogate modeling, yet direct prompting fails in scientific domains due to scarce domain-specific pretraining data and the difficulty of articulating complex structures in natural language.
- **S3 (Proposed Method):** We introduce LICO, a framework that extends arbitrary base LLMs for black-box optimization by learning separate embedding layers for domain inputs and scores, enabling in-context surrogate modeling in latent space.
- **S4 (Training Strategy):** To facilitate generalization to unseen objectives, we propose a semi-synthetic training strategy combining intrinsic domain properties with Gaussian Process-generated synthetic functions.
- **S5 (Key Result & Bounded Implication):** On the PMO benchmark, LICO achieves competitive performance across 23 objectives and leads among evaluated baselines on the low-budget PMO-1K setting, demonstrating effective in-context optimization without task-specific fine-tuning.

### Introduction Outline (Complete)
- **P1 (Big Picture & BBO Context):** Define black-box optimization and its ubiquity in scientific discovery. Explain the iterative surrogate modeling paradigm and the core challenge of generalizing from sparse data.
- **P2 (LLM Potential & Text-Space Limitations):** Introduce LLMs as promising surrogate models due to in-context learning. Highlight three critical limitations of text-space prompting: domain restriction, data scarcity in pretraining corpora, and context length inflation.
- **P3 (LICO Solution & Architecture):** Propose LICO as a domain-agnostic interface. Explain the architectural design: learnable embedding layers map inputs/scores to the LLM's latent space, bypassing natural language bottlenecks and enabling compact in-context reasoning.
- **P4 (Semi-Synthetic Training & Generalization):** Detail the training strategy. Explain why mixing intrinsic properties (chemical priors) with synthetic GP functions (diversity) is essential for generalizing to unseen downstream objectives.
- **P5 (Evidence Preview & Contributions):** Preview empirical results on PMO, highlighting sample efficiency and competitive performance against strong baselines. Summarize contributions: (1) LICO architecture, (2) semi-synthetic training, (3) comprehensive evaluation and ablations.

## Priority Revision Plan
| Priority | Action Item | Expected Impact | Effort |
|---|---|---|---|
| **P0** | Bound SOTA claims in Abstract/Conclusion to "among evaluated baselines" and acknowledge parameter scale advantage. | Improves scientific defensibility and prevents reviewer pushback on overclaiming. | Low |
| **P0** | Clarify dynamic normalization strategy in Appendix A.3 (e.g., EMA smoothing) to ensure UCB stability. | Resolves potential optimization instability and improves reproducibility. | Low |
| **P1** | Expand ablation studies (language instructions, synthetic ratios) to cover all 23 PMO tasks. | Strengthens statistical robustness of design choice conclusions. | Medium |
| **P1** | Add capacity-matched control (smaller LLM or scratch transformer) to isolate architectural benefits. | Isolates LICO's contribution from model scale/domain-adaptation effects. | Medium |
| **P2** | Discuss inference compute trade-offs vs. lightweight GPs in Conclusion/Limitations. | Provides balanced view of practical deployment feasibility. | Low |
| **P2** | Categorize intrinsic properties in Appendix A.1 by chemical domain (topological, electronic, etc.). | Clarifies feature coverage and strengthens semi-synthetic training rationale. | Low |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | LICO vs. baselines on PMO-1K | 23 tasks, 1K budget, 5 seeds | AUC Top-10 | LICO leads aggregated score | SOTA on low-budget | Ablations only on 5 tasks |
| E2 | LICO vs. baselines on PMO | 23 tasks, 10K budget, 5 seeds | AUC Top-10 | Competitive with Genetic GFN/Augmented Memory | Generalization capability | Compute cost not reported |
| E3 | Language instruction ablation | 3 variants, 5 tasks | AUC Top-10 | Full prompt best | Language tokens critical | Limited task coverage |
| E4 | Synthetic ratio ablation | 4 ratios, 5 tasks | AUC Top-10 | 0.1 ratio best | Semi-synthetic training vital | Limited task coverage |
| E5 | Pretrained vs. Scratch LLM | 7B models, 5 tasks | AUC Top-10 | Pretrained significantly better | Pattern-matching transfer | No capacity-matched control |
| E6 | LLM scaling laws | 1.8B-7B models, 8 tasks | Sum Performance | Performance scales with size | Larger LLMs benefit LICO | Inference latency not measured |

### Research-Theme Gap Diagnosis
The core research value lies in demonstrating that LLMs can serve as domain-agnostic surrogate models via embedding alignment. However, the current experiments lack explicit validation of (1) optimization stability under dynamic normalization, (2) capacity-matched architectural isolation, and (3) compute efficiency trade-offs. These gaps limit the practical deployment claims and causal attribution of performance gains.

### Proposed Research Experiments (P0/P1/P2)
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|---|---|---|---|---|---|---|---|
| Ablation robustness | Language/synthetic benefits generalize across tasks | Run E3/E4 on all 23 PMO tasks | Same variants | AUC Top-10 variance | Consistent delta across tasks | Low | Stronger causal claims |
| Capacity isolation | LICO architecture outperforms scale-matched baselines | Train 1B-3B LLM + scratch transformer | Capacity-matched controls | AUC Top-10 | LICO wins despite equal params | Medium | Isolates architectural novelty |
| Optimization stability | Dynamic normalization stabilizes UCB exploration | Add EMA smoothing to y-normalization | Baseline dynamic norm | Optimization trajectory | Smoother utility scores | Low | Improves reproducibility |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6.5/10

**Rationale:** The paper presents a novel and well-motivated framework (LICO) for leveraging LLMs as domain-agnostic surrogate models in black-box optimization. The semi-synthetic training strategy and embedding alignment design are conceptually strong, and the empirical results on PMO are competitive. However, the score is moderated by unbounded SOTA claims, limited ablation scope (only 5 tasks), and lack of explicit discussion on compute trade-offs and capacity-matched controls. These issues reduce the defensibility of the contribution and the clarity of practical deployment feasibility.

**Post-Revision Target:** [7.5, 8.5]/10

**Path to Target:** Bounding performance claims, expanding ablations to all 23 tasks, clarifying normalization stability, and adding a capacity-matched control would significantly strengthen the causal attribution of gains and improve scientific rigor. Addressing these points would elevate the paper to a strong acceptance candidate.
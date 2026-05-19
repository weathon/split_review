## Summary
# Final Review Report

## Summary
This paper introduces HD-Explain, a post-hoc, example-based prediction explanation method that leverages Kernelized Stein Discrepancy (KSD) to define a model-dependent kernel for measuring data correlations. By relaxing the joint distribution assumption to isolate conditional model influence, HD-Explain efficiently retrieves fine-grained, instance-level training examples that support a test prediction. The authors propose two quantitative metrics, Hit Rate and Coverage, to evaluate explanation precision and diversity. Experiments across multiple image classification benchmarks demonstrate that HD-Explain significantly outperforms Influence Functions, Representer Point Selection (RPS), and TracIn in both explanation fidelity and computational scalability. The method offers a theoretically motivated and computationally efficient alternative for enhancing model transparency, though its reliance on marginal relaxations and sensitivity to low-level raw features warrant careful practical consideration.

## Strengths
1. **Novel Theoretical Integration:** The paper creatively adapts Kernelized Stein Discrepancy, traditionally used for goodness-of-fit testing and sampling, to the task of example-based prediction explanation. The derivation of a model-dependent kernel that encodes data correlations without parameter inversion is conceptually elegant and mathematically grounded.
2. **Strong Empirical Performance:** HD-Explain demonstrates substantial gains over established baselines (Influence Function, RPS, TracIn) in both Hit Rate (>80% vs ≤10%) and Coverage metrics. The quantitative evaluation under controlled data augmentations provides robust evidence of the method's instance-level granularity and retrieval stability.
3. **Computational Scalability:** By bounding the cache size to data dimensionality rather than model parameters, HD-Explain achieves significant computational efficiency. This scalability advantage makes the method practical for large-scale neural classifiers where Hessian-based influence methods are infeasible.
4. **Transparent Limitation Analysis:** The authors honestly acknowledge the method's sensitivity to low-level raw features and the impact of kernel selection. The inclusion of the HD-Explain* variant and empirical kernel comparisons (RBF, IMQ, Linear) demonstrates a responsible approach to methodological validation.

## Weaknesses
1. **Theoretical Relaxations Lack Rigorous Bounding:** The derivation of the score function relies on two strong approximations: assuming a uniform empirical marginal distribution $P_D(x)$ and treating discrete labels as continuous sparse features. While these enable computational tractability, their impact on the KSD correlation metric is not theoretically bounded or empirically validated against rigid discrete Stein operators. This leaves a gap in the methodological soundness.
2. **Proxy Metrics Limit Faithfulness Claims:** Hit Rate and Coverage are valuable for measuring retrieval stability and diversity, but they serve as proxy metrics rather than direct measures of model faithfulness. The evaluation relies on augmented in-distribution samples, which may not reflect explanation quality under true out-of-distribution shifts or adversarial perturbations. The paper overstates the implications of these metrics without acknowledging their scope limitations.
3. **Generic Contribution Statements:** The initial contribution claims are overly broad ("novel example-based explanation method", "thorough evaluation") and lack technical specificity. They do not explicitly mention the KSD kernel mechanism, the proposed metrics, or the concrete empirical gains, reducing the immediate impact and clarity of the paper's value proposition.
4. **Insufficient Mechanistic Validation:** The four-term decomposition of the KSD kernel provides intuitive insights into raw similarity versus model-dependent correlation, but the relative contributions of each term remain conjectural. Without term-level ablation, it is unclear whether performance gains stem primarily from the Stein operator corrections or the underlying kernel similarity bias.

## Key Issues
1. **Uniform Marginal Assumption Validity:** The assumption that $P_D(x)$ is uniform ($\nabla_x \log P_D(x) = 0$) simplifies the score function but may not hold for datasets with complex input manifolds or class-imbalanced distributions. If the empirical marginal is highly non-uniform, the kernel may inadvertently capture input density variations rather than pure conditional model influence.
2. **Discrete Label Approximation Risk:** Treating one-hot labels as continuous sparse features to enable differentiation is a heuristic approximation. Without validation against theoretically sound discrete Stein discrepancy methods, there is a risk that the derived score function misrepresents the true label-space geometry, potentially affecting explanation fidelity for multi-class or hierarchical label structures.
3. **Baseline Comparison Fairness:** Baselines are restricted to the last layer to ensure computational scalability, which inherently limits their representational capacity. While this controls for compute budget, it may conflate methodological superiority with architectural constraints. The performance gap should be explicitly disentangled from the last-layer restriction.
4. **Sensitivity to Low-Level Features:** HD-Explain's reliance on raw input gradients makes it susceptible to superficial attributes (e.g., background color, object position). This limitation is acknowledged but lacks a clear practical mitigation strategy in the main text, potentially undermining deployment confidence in real-world scenarios with high visual variance.

## Actionable Suggestions
1. **Validate Relaxations Empirically:** Add a sensitivity analysis comparing the relaxed score function against a theoretically rigid discrete Stein operator (e.g., Yang et al., 2018) on a small subset. Quantify the Hit Rate degradation to bound the impact of the uniform marginal and discrete label approximations.
2. **Clarify Metric Scope:** Explicitly state that Hit Rate and Coverage serve as proxy metrics for retrieval stability and diversity, rather than direct measures of model faithfulness. Add a sentence acknowledging that evaluation is limited to in-distribution perturbations and does not guarantee out-of-distribution robustness.
3. **Disentangle Baseline Constraints:** Clarify that baselines were restricted to the last layer to ensure computational fairness. Add a brief discussion on whether the performance gap stems from KSD's superior correlation modeling or the baselines' architectural limitations under last-layer constraints.
4. **Provide Practical Mitigation Guidelines:** Connect the raw-feature sensitivity limitation to the HD-Explain* variant. Recommend HD-Explain* as the default choice for natural images with high background variance, and provide a concise decision rule for kernel selection (e.g., IMQ for geometric robustness, Linear for large-scale efficiency).
5. **Add Term-Level Ablation:** Include a small ablation study evaluating HD-Explain using only the raw similarity term (Term ①) versus the full kernel. This would empirically validate the intuition that Stein operator corrections are essential for faithful instance-level explanations.

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem & Stakes):** Example-based prediction explanations are essential for model transparency, yet existing methods struggle with computational scalability or produce coarse, class-level prototypes.
- **S2 (Prior Gap):** Influence-based approaches rely on parameter perturbations or latent similarities, which incur prohibitive costs (Hessian inversion) or lack instance-specific granularity.
- **S3 (Proposed Method):** We introduce HD-Explain, a data-centric explanation method that leverages Kernelized Stein Discrepancy (KSD) to define a model-dependent kernel encoding fine-grained data correlations without parameter inversion.
- **S4 (Key Results):** Experiments across image classification benchmarks show HD-Explain achieves >80% Hit Rate under noise perturbations and substantially higher Coverage than baselines, demonstrating superior precision and diversity.
- **S5 (Bounded Implication):** These results establish KSD-based correlation as a scalable and faithful alternative for post-hoc model transparency, with practical guidelines for kernel selection and layer adaptation.

### Introduction Outline (Complete)
- **P1 (Big Picture & Value):** Training data points shape model behavior, making example-based explanations critical for trustworthiness, error tracing, and model summarization.
- **P2 (Current Landscape):** Modern methods construct influence chains via parameter perturbations (Influence Functions) or representation similarities (RPS, TracIn), offering valuable insights but facing inherent trade-offs.
- **P3 (Core Gap):** Parameter-based methods suffer from scalability bounds due to Hessian inversion, while representation-based methods often yield class-level explanations that ignore instance-specific nuances. Both rely on approximations that degrade faithfulness.
- **P4 (Proposed Solution):** We propose HD-Explain, which bypasses parameter perturbation entirely by exploiting KSD to encode model-dependent data correlations directly, enabling efficient and fine-grained retrieval.
- **P5 (Evidence Preview):** Quantitative evaluations using Hit Rate and Coverage metrics demonstrate that HD-Explain significantly outperforms baselines in explanation fidelity and computational efficiency across multiple domains.
- **P6 (Contributions):** Explicitly list the three contributions: (1) KSD-based explanation method, (2) quantitative evaluation metrics, (3) comprehensive empirical validation showing precision, consistency, and scalability gains.

## Priority Revision Plan
| Priority | Action Item | Expected Impact | Effort |
|---|---|---|---|
| **P0** | Rewrite Abstract & Contributions to include specific mechanism (KSD kernel), metrics (Hit Rate, Coverage), and bounded quantitative results. | Improves clarity, scientific credibility, and immediate value communication. | Low |
| **P0** | Add transitional context before Equation (1) acknowledging the conditional-vs-joint distribution gap and the upcoming marginal relaxation. | Bridges theoretical discontinuity and improves methodological clarity. | Low |
| **P1** | Include a sensitivity analysis or ablation comparing relaxed score function against rigid discrete Stein operators, and validate term-level contributions (Term ① vs ②-④). | Strengthens theoretical soundness and mechanistic understanding. | Medium |
| **P1** | Explicitly state that Hit Rate/Coverage are proxy metrics for retrieval stability/diversity, and clarify baseline last-layer restriction for fairness. | Prevents overinterpretation and isolates methodological advantage. | Low |
| **P2** | Expand Conclusion to include validated findings, bounded limitations (raw-feature sensitivity), and concrete future work (theoretical validation, generative extension). | Enhances scientific maturity and provides clear next steps. | Low |
| **P2** | Provide practical mitigation guidelines connecting raw-feature sensitivity to HD-Explain* recommendation and kernel selection rules. | Improves deployment confidence and practical usability. | Low |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | Qualitative explanation comparison | CIFAR-10, SVHN, OCH, MRI; ResNet-18 | Visual inspection | HD-Explain retrieves visually similar, instance-specific examples | Fine-grained explanation | Subjective evaluation; lacks domain expert validation for medical data |
| E2 | Quantitative Hit Rate/Coverage under Noise Injection | 4 datasets, 300k+ augmented runs | Hit Rate, Coverage, Run Time | HD-Explain >80% Hit Rate, high Coverage; baselines ≤10% | Precision & diversity gains | Proxy metrics; limited to in-distribution perturbations |
| E3 | Quantitative evaluation under Horizontal Flip | Same setup as E2 | Hit Rate, Coverage | HD-Explain performance drops; HD-Explain* more robust | Raw-feature sensitivity | Highlights limitation without explicit mitigation guideline |
| E4 | Kernel ablation (RBF, IMQ, Linear) | 4 datasets | Hit Rate, Coverage, Run Time | IMQ best quality; Linear fastest | Kernel selection impact | No theoretical guidance on kernel choice per domain |
| E5 | Data debugging (mislabel retrieval) | CIFAR-10, multi-class label flips | Precision@K, Recall@K | HD-Explain* outperforms baselines | Side-benefit validation | Not main contribution; limited to one dataset |

### Research-Theme Gap Diagnosis
The core research value lies in demonstrating that KSD-based correlation offers a scalable, faithful alternative to parameter-perturbation methods. However, the current experiments lack: (1) theoretical validation of the uniform marginal and discrete label relaxations, (2) term-level ablation to isolate Stein operator contributions, and (3) out-of-distribution or adversarial robustness tests to bound generalization claims.

### Proposed Research Experiments
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|---|---|---|---|---|---|---|---|
| Relaxation validity | Uniform marginal approximation minimally impacts Hit Rate | Compare relaxed score vs rigid discrete Stein operator on CIFAR-10 subset | Yang et al. (2018) discrete KSD | Hit Rate delta | Δ < 5% | Low | Bounds theoretical risk |
| Term contribution | Stein operator terms (②-④) are essential for instance-level fidelity | Ablate kernel: Term ① only vs Full kernel | HD-Explain baseline | Hit Rate, Coverage | Full kernel significantly outperforms Term ① | Low | Validates mechanistic intuition |
| OOD robustness | HD-Explain maintains explanation stability under domain shift | Evaluate on CIFAR-10-C (corruptions) or ImageNet subset | Baselines (last-layer) | Hit Rate drop % | Smaller drop than baselines | Medium | Strengthens generalization claims |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6.5/10

**Rationale:** The paper presents a conceptually elegant and empirically strong method for example-based prediction explanation, leveraging KSD to achieve significant gains in precision, diversity, and scalability over established baselines. The core intuition is well-motivated, and the quantitative evaluation is rigorous. However, the score is moderated by the lack of theoretical bounding for key relaxations (uniform marginal, discrete label approximation), the reliance on proxy metrics without explicit scope limitations, and generic contribution statements that dilute the immediate impact. With targeted revisions to clarify theoretical assumptions, validate mechanistic intuitions, and tighten claim-evidence alignment, the manuscript can reach a higher standard of scientific defensibility.

**Post-Revision Target:** [7.5, 8.5]/10

**Path to Target:** Address P0/P1 revision items (rewrite contributions/abstract, add relaxation sensitivity analysis, include term-level ablation, clarify metric scope). These changes will significantly strengthen theoretical soundness and empirical transparency without requiring extensive new experiments.
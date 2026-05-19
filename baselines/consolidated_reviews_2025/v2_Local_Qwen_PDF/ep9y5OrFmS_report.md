## Summary
# Final Review Report

## Summary
This paper investigates the geometric relationship between parameter magnitude pruning masks and the top-k Hessian eigenspaces throughout the training of deep neural networks. Motivated by the parallel observation that both structures undergo early crystallization and stabilization, the authors propose casting pruning masks as rank-k orthogonal matrices on the Stiefel manifold. This formulation enables the direct comparison of their spans using Grassmannian metrics. After reviewing several metrics, the authors select the overlap metric for its interpretability and computational efficiency. Experiments on a small MLP trained on subsampled MNIST demonstrate that the overlap between pruning masks and top Hessian eigenspaces is significantly higher than random chance throughout training, peaking at initialization and subsequently stabilizing. The findings suggest a geometric alignment between large parameter magnitudes and directions of high loss curvature, offering a novel perspective on early training dynamics and potential pathways for fast Hessian approximations.

## Strengths
1. **Novel Geometric Formulation:** The paper provides an elegant mathematical framework by casting boolean pruning masks as elements of the Stiefel manifold, enabling direct subspace comparison with Hessian eigenvectors via Grassmannian metrics. This bridges two previously independent lines of research (pruning and curvature analysis).
2. **Rigorous Metric Analysis:** The synthetic experiments and theoretical proof (Lemma A.1) thoroughly evaluate Grassmannian metrics. The justification for selecting the overlap metric based on its bounded range, linear expectation, and computational efficiency is well-reasoned and empirically validated.
3. **Clear Empirical Demonstration:** The experiments clearly show that the overlap between pruning masks and top Hessian eigenspaces is significantly above random chance throughout training. The observation of early peak overlap followed by stabilization provides a fresh perspective on the "loss of plasticity" and early training dynamics.
4. **High-Quality Writing and Structure:** The manuscript is well-organized, with a logical flow from motivation to mathematical formulation, metric selection, and empirical validation. The use of figures and appendices to support the main claims is effective.

## Weaknesses
1. **Limited Experimental Scale and Generalizability:** The empirical validation relies exclusively on a single small MLP (7030 parameters) trained on a subsampled MNIST dataset. While computationally necessary for exact Hessian analysis, this severely limits the generalizability of the claims. Hessian spectral properties and pruning dynamics are known to vary significantly across architectures (e.g., CNNs, Transformers) and optimization regimes. The paper does not discuss how the observed overlap dynamics might differ in larger, highly overparameterized networks.
2. **Overstated Causal and Practical Claims:** The abstract and conclusion repeatedly claim that "largest parameter magnitudes tend to coincide with the directions of largest loss curvature" and that this can be leveraged for "fast and effective low-rank Hessian approximations." The overlap metric measures subspace similarity, not a direct causal coincidence. Furthermore, the paper does not demonstrate this approximation in any downstream task (e.g., optimization or pruning accuracy), making these statements speculative rather than validated results.
3. **Superficial Mechanistic Interpretation:** The results show that overlap is largest at initialization and then decays to a stable level. The connection to "loss of plasticity" is noted but remains thin. The paper lacks a deeper discussion on *why* the overlap decays (e.g., Hessian eigenspace rotation to align with the data manifold vs. pruning masks remaining anchored to initialization magnitudes), missing an opportunity to provide stronger theoretical insight.
4. **Missing Variance and Statistical Reporting:** The experiments report results for a single training run without variance estimation (e.g., multiple random seeds). Given the stochastic nature of SGD and initialization, reporting mean ± std over multiple seeds would significantly strengthen the reliability of the overlap trends and stabilization claims.

## Key Issues
1. **Claim-Evidence Mismatch on Practical Utility:** The paper claims the overlap phenomenon can approximate the top Hessian subspace at linear cost. However, no downstream experiment validates this approximation (e.g., using the mask-derived subspace for Newton steps or pruning). This is a speculative suggestion presented as a validated benefit.
2. **Generalizability Overreach:** Conclusions are generalized to "deep learning" broadly based on a single 7k-parameter MLP on subsampled MNIST. Modern DL regimes (large batch, Adam, ResNets/Transformers) exhibit different Hessian spectra (e.g., edge of stability, heavy-tailed distributions) and pruning dynamics. The lack of validation in these regimes is a critical gap.
3. **Causal Wording Without Causal Design:** Phrases like "largest parameter magnitudes tend to coincide with the directions of largest loss curvature" imply a direct causal or structural coincidence. The overlap metric only measures geometric span similarity. Without matched ablations (e.g., random masks of same sparsity, or magnitude masks on randomized Hessians), the causal interpretation is not established.
4. **Single-Seed Experimental Reporting:** The absence of variance reporting (multiple seeds) makes it difficult to assess the stability of the overlap trends. Small perturbations in initialization or SGD noise could theoretically alter the early stabilization dynamics.

## Actionable Suggestions
1. **Bound Claims to Tested Settings:** Replace broad statements like "in deep learning, largest parameter magnitudes tend to coincide..." with bounded wording: "in this MLP setting, large parameter magnitudes are geometrically aligned with directions of high loss curvature." Explicitly acknowledge the scale limitation in the Conclusion.
2. **Add Variance Reporting:** Repeat the main experiment with at least 3 different random seeds. Report mean ± std for the overlap curves in Figure 4 to demonstrate statistical reliability.
3. **Deepen Mechanistic Discussion:** In Section 5, expand the interpretation of the overlap decay. Explain that the Hessian eigenspace likely rotates to align with the data manifold during training, while pruning masks remain anchored to the initial magnitude distribution. This divergence explains the decay, while persistent above-chance overlap indicates structural parameter importance.
4. **Clarify Metric Selection Justification:** In Section 4.2, explicitly note that the overlap metric's bounded range [0, 1] and linear expectation make it more interpretable across sparsity levels than distance metrics scaling with sqrt(k), reinforcing its selection.
5. **Include a Downstream Validation (Optional but Recommended):** If feasible, add a small ablation showing that using the top-k magnitude parameters as a proxy for the top Hessian subspace yields competitive performance in a simple second-order update or pruning task. If not feasible, clearly label this as future work rather than a validated benefit.

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem/Domain):** Neural network training exhibits two parallel early-stabilization phenomena: the crystallization of magnitude-based pruning masks and the compression of the loss Hessian eigenspace.
- **S2 (Gap):** Prior work treats parameter importance and loss curvature as independent diagnostics, leaving their potential geometric relationship unexplored throughout training.
- **S3 (Method):** We cast both pruning masks and Hessian eigenvectors as orthonormal matrices on the Stiefel manifold, enabling direct span comparison via Grassmannian metrics.
- **S4 (Key Result):** Experiments on a trained MLP reveal that the overlap between these subspaces is significantly above random chance throughout training, peaking at initialization and subsequently stabilizing.
- **S5 (Implication):** This geometric alignment suggests that large parameter magnitudes track directions of high loss curvature, offering a novel perspective on early training dynamics and potential pathways for fast curvature approximations.

### Introduction Outline (Complete)
- **P1 (Big Picture & Pruning):** Introduce DNN overparameterization and the efficiency of pruning. Highlight the Lottery Ticket Hypothesis and early stabilization of magnitude masks.
- **P2 (Parallel Phenomenon & Hessian):** Introduce the Hessian's role in curvature analysis. Highlight the separation into top/bulk subspaces and the early stabilization of the top eigenspace.
- **P3 (Gap & Motivation):** Explicitly state the gap: despite parallel stabilization, these lines of research remain disconnected. Connecting them could unify first- and second-order insights.
- **P4 (Proposed Solution):** Introduce the Stiefel manifold formulation and Grassmannian metrics as the bridge to quantify subspace similarity.
- **P5 (Contributions & Evidence):** List the three contributions (formulation, metric selection, empirical overlap evidence) and preview the main findings (Figure 1).

## Priority Revision Plan
| Priority | Action Item | Expected Impact | Effort |
|---|---|---|---|
| **P0 (Critical)** | Bound strong claims in Abstract/Conclusion to the tested MLP setting; replace causal wording ("coincide") with geometric alignment. | Prevents overgeneralization and improves scientific defensibility. | Low |
| **P0 (Critical)** | Add explicit limitation statement in Section 5 Setup regarding scale constraints and potential differences in larger architectures. | Manages reader expectations and addresses generalizability concerns. | Low |
| **P1 (High)** | Repeat main experiment with >=3 random seeds and report mean ± std overlap curves. | Validates statistical reliability of stabilization trends. | Medium |
| **P1 (High)** | Deepen mechanistic discussion in Section 5 on why overlap decays (Hessian rotation vs. mask anchoring). | Strengthens theoretical insight and contribution depth. | Low |
| **P2 (Medium)** | Clarify metric selection justification in Section 4.2 by emphasizing overlap's bounded range and interpretability. | Improves methodological rigor and narrative flow. | Low |
| **P2 (Medium)** | Add a small downstream validation (e.g., mask-based Hessian proxy for one Newton step) or clearly label utility claims as future work. | Closes the claim-evidence gap for practical applications. | High |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | Synthetic metric behavior | Random matrices/masks, varying D and r | Grassmannian metrics | Overlap is stable, linear, and informative | Metric selection | N/A |
| E2 | Overlap expectation proof | Theoretical derivation on Stiefel manifold | Expectation of overlap | E[overlap] = k/D | Theoretical baseline | N/A |
| E3 | Training dynamics overlap | MLP (7030 params), subsampled MNIST, SGD | Overlap, IoU, dist metrics | Overlap > chance, peaks at init, stabilizes | Early stabilization link | Single seed, small scale |

### Research-Theme Gap Diagnosis
The core claim of geometric alignment between pruning masks and Hessian eigenspaces is supported but lacks statistical robustness (single seed) and generalizability (small MLP). The practical utility claim (fast Hessian approximation) is entirely unsupported by downstream experiments.

### Proposed Research Experiments
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|---|---|---|---|---|---|---|---|
| Statistical Reliability | Overlap trends are stable across initializations. | Repeat E3 with 5 seeds. | Same setup. | Mean ± std overlap curves. | Low variance across seeds. | Low | Validates robustness. |
| Mechanistic Insight | Overlap decay is due to Hessian rotation vs mask anchoring. | Track principal angles of top eigenvectors over time. | Random mask baseline. | Eigenvector cosine similarity. | Eigenvectors rotate more than masks. | Low | Deepens theoretical contribution. |
| Practical Utility | Mask subspace approximates Hessian for optimization. | Use top-k magnitude params for 1-step Newton update. | Full Hessian Newton, SGD. | Test accuracy after 1 step. | Competitive with full Hessian. | Medium | Validates practical claim. |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6/10
The paper presents an elegant geometric formulation and rigorous metric analysis, successfully demonstrating a non-trivial overlap between pruning masks and Hessian eigenspaces. However, the score is tempered by the limited experimental scale (single small MLP), lack of variance reporting, and overstated causal/practical claims that extend beyond the validated evidence.

**Post-Revision Target:** [7, 8]/10
If the authors bound their claims to the tested setting, add multi-seed variance reporting, and deepen the mechanistic discussion of the overlap decay, the paper would become significantly more defensible and impactful. Adding a small downstream validation of the Hessian approximation would further strengthen the practical contribution.
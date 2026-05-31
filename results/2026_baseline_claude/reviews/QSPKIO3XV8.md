## Summary

The paper proposes **Dimension Domain Co-Decomposition (3D)**, a PINN-based framework that unifies dimension decomposition (a single shared MLP processes coordinate–index pairs instead of per-dimension networks) with an automatic, MoE-driven domain decomposition (a soft router adaptively partitions the space without pre-defined subdomains or interface conditions). A novel **Variable Interpretability (VI)** metric—based on subspace alignment via QR/SVD—is introduced to quantify how well the learned per-dimension components match the ground-truth factors. Experiments on Poisson, Wave, Burgers, and Linear Transport equations demonstrate parameter savings, competitive accuracy, and interpretable decompositions.

---

## Strengths

- **Shared-MLP parameter efficiency**: Using a coordinate–index pair as input to a single MLP replaces $d$ separate MLPs, giving dimension-independent parameter count. Table 1 and memory benchmarks confirm 50–70% reductions scaling with $d$, with no sacrifice in accuracy (and often an improvement over vanilla PINNs).
- **VI metric is principled and well-specified**: The metric uses orthonormal basis alignment via QR decomposition and singular-value-based scoring (Eq. 6), is scale-invariant, bounded in $[0,1]$, and handles the case where the true rank is smaller than $r$ correctly. Table 2 provides quantitative, multi-seed VI measurements across problem families.
- **Interface-free domain decomposition**: The dense-MoE router removes the need for pre-defined subdomains and explicit interface penalties. Figures 4–5 show the router correctly identifies the Burgers shock at $x=0$ and the diagonal stripe structure of Linear Transport without supervision, and this is consistent across five different random seeds.
- **Dimensional fine-tuning**: The separable parameterization allows a model trained in $d=5$ to be fine-tuned for $d=8$, which is not possible for standard MLP-based PINNs. This is a practically useful property.

---

## Weaknesses

### Fatal
*None that invalidate the core claims.*

### Major

1. **Missing comparison with the closest competitor (SPINNs)**: SPINNs (Cho et al., 2023) is explicitly identified as the most related prior work throughout Sections 1–3, yet no accuracy or training-speed comparison with SPINNs appears anywhere in the main experiments. Since the shared-MLP design is positioned as an improvement over SPINNs (parameter sharing, MoE compatibility), the lack of a head-to-head benchmark is a significant evidentiary gap. The reader cannot judge whether 3D actually outperforms SPINNs in practice.

2. **Domain decomposition experiments are insufficiently tested against baselines**: The Burgers and Linear Transport results demonstrate *that* the router discovers meaningful structure, but no accuracy comparison against APINNs or XPINNs is provided. For Burgers ($\nu = 0.01/\pi$), the error of $0.0011$ from 3D is reported in isolation; the performance of standard domain-decomposition methods on the same problem is well-documented in the literature, making the omission visible.

3. **The "co-decomposition" scenario is not demonstrated jointly**: Dimension decomposition and domain decomposition are evaluated on largely disjoint problem sets (Poisson/Wave for dimension, Burgers/Transport for domain). The Burgers and Transport equations are 1D in space, making dimension decomposition trivial. There is no experiment where both a genuinely high-dimensional problem *and* sharp features co-exist, which would be the natural showcase for the combined 3D framework.

4. **VI is restricted to separable solutions**: The authors acknowledge this in the conclusion, but the limitation is fundamental. All VI experiments use solutions that are *exactly* separable products (e.g., $\prod_j \sin(\pi x_j)$). For any non-separable PDE, VI requires constructing a separable approximation (e.g., Fourier truncation) as a proxy reference; the quality of this proxy directly determines the validity of VI, and no methodology or experiments for this general case are provided.

### Minor

- **Limited benchmark scale**: The highest-dimensional problem is 10D (Poisson), which is relatively easy due to its separable product structure. Claims about mitigating the curse of dimensionality would be better supported by experiments in at least 20–50 dimensions.
- **Vanilla PINNs baseline uses much larger networks**: For 10D Poisson, the baseline uses a 4-layer, width-64 MLP (4929 params) against the shared MLP (5392 params), which is fair. For 5D Poisson, however, vanilla PINNs uses a 10-layer, width-64 MLP whose parameter count is not reported and appears substantially larger, making the accuracy comparison potentially unfair.
- **K selection**: The optimal number of experts $K_{\text{optimal}}$ is described as the point after which adding more experts yields no new structure. No principled selection criterion or sensitivity analysis is presented, leaving $K$ a manual hyperparameter.

### Trivial
*None.*

---

## Nice-to-Haves

- A direct quantitative comparison with SPINNs (accuracy, training time) on the same benchmarks.
- An experiment combining high-dimensional input with sharp features (e.g., Burgers in 3D or 4D space) to validate the co-decomposition benefit.
- A brief discussion of a heuristic or procedure for constructing separable approximations of $G_j$ when the solution is non-separable.

---

## Novel Insights

The Variable Interpretability (VI) metric is the paper's most original standalone contribution. Its formulation—column-normalizing the learned and reference factor matrices, extracting orthonormal bases via QR, and measuring subspace containment via squared singular values of the cross-Gram matrix—cleanly handles the case where the predicted rank $r$ exceeds the ground-truth rank $s$ (measuring coverage rather than identity of subspaces). This is a non-trivial and reusable design. The observation that the 1D Wave equation with $r=1$ achieves $VI=1$ while higher wave-speed cases require $r=5$, attributable to the spectral bias of PINNs amplified by high-frequency temporal components, is a concrete, interpretable diagnostic that previously had no quantitative analogue in the PDE-solving literature.

---

## Suggestions

1. Add a comparison table against SPINNs for the Poisson and Wave benchmarks (accuracy and training time), using comparable parameter budgets.
2. Add at least one experiment on a non-trivial co-decomposition problem: a genuinely high-dimensional PDE (≥20D) with non-smooth structure, or a PDE where domain decomposition provides a measurable benefit in accuracy over a single-expert 3D.
3. Compare domain decomposition accuracy and decomposition quality against APINNs on the Burgers benchmark.
4. Clarify the computational cost of VI (the QR+SVD step at evaluation time) and discuss when VI is feasible or infeasible as a metric.

---

## Score and Decision

The paper introduces a clean and efficient shared-MLP dimension decomposition, a well-defined subspace-based interpretability metric, and automatic MoE-driven domain partitioning. The individual components are sound and the VI metric is the most original contribution. However, the absence of any head-to-head comparison with SPINNs (the closest related work) and with APINNs/XPINNs, combined with the lack of experiments that stress-test the joint co-decomposition, substantially weakens the empirical case for the framework's claimed advantages. The VI metric's restriction to separable solutions further limits its generality. These gaps make the paper's contributions feel incremental and incompletely validated for the ICLR bar.

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>
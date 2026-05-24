Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper proposes Neural Network Ising Machines (NPIM), which applies algorithm unrolling to dynamical Ising machines by parameterizing the update step with a small MLP and training it via zeroth-order evolutionary optimization. The method is evaluated on two families of benchmarks: neural-CO benchmarks (MIS, Max-Clique, Max-Cut) and classical G-set Max-Cut instances, achieving competitive or state-of-the-art results on many of them.

## Strengths

- **Novel combination of algorithm unrolling, Ising machines, and zeroth-order training.** The paper introduces a genuinely new approach to neural combinatorial optimization: rather than constructing solutions autoregressively or via diffusion, it learns the update dynamics of an Ising machine from scratch. The MLP parameterization (Eqs. 4–7) with temporal Fourier basis is a well-motivated and clean design, and the connection to the dynamical systems literature (CAC, SBM) is clearly drawn. This is a distinct contribution relative to existing neural CO methods.

- **Strong empirical results on two benchmark families.** Table 1 shows dNPIM achieves the best solution size on four of five neural-CO benchmarks (MIS-small, MIS-large, MaxCut-small, MaxCut-large), outperforming DiffUCO, SDDS, and LTFT. Table 2 shows dNPIM achieves the lowest median TTS on four of five G-set categories, beating state-of-the-art Ising machines CAC, CFC, and dSBM. These results demonstrate that the learned dynamics are competitive with both learned and hand-crafted approaches.

- **Analysis of learned dynamics provides interpretability.** Figure 2 shows a concrete example where a single-layer network evolves from a greedy steepest-descent strategy (all weights negative) to one with positive weights that create a momentum effect, enabling escape from local minima. This gives direct evidence that useful search dynamics emerge from data-driven training, not just from hand-designed physical principles.

- **Systematic treatment of practical training challenges.** The paper identifies and addresses the bootstrapping problem (training fails from scratch on hard instances where success rate is zero) and provides a fine-tuning strategy (Section 4.3). The comparison of continuous vs. discrete coupling (cNPIM vs. dNPIM) in Section 4.5 reveals a genuine trade-off between average performance and robustness, which is a non-trivial insight beyond simply reporting aggregate metrics.

## Weaknesses

### Major

- **Asymmetric comparison protocol in Table 1.** dNPIM is reported as "top 30" (best solution from 30 parallel trajectories), while the baseline results (DiffUCO, SDDS, LTFT) are taken from Sanokowski et al. (2025) without specifying whether they also use multi-start sampling. The paper claims dNPIM is "less computationally intensive per trajectory," yet on large instances (MIS-large, MaxCut-large) dNPIM takes 1:20 vs. 0:02–0:03 for DiffUCO and SDDS — a 27–40× slowdown that undercuts the justification. This makes it impossible to determine whether the reported superiority in solution quality reflects an algorithmic advantage or simply a larger search budget. The paper should report dNPIM with a single trajectory (or matched compute), and include standard deviations across runs to assess significance.

- **Missing variance for dNPIM in Table 1.** All baseline methods report solution size with standard errors (e.g., "19.42 ± 0.03"), while dNPIM results are given as bare point estimates (e.g., "19.9"). Since dNPIM uses stochastic trajectories, variance information is essential for any comparative claim. The paper runs 30 trajectories and could trivially report the mean and standard error across independent trials.

### Minor

- **Catastrophic failures on a nontrivial fraction of instances are acknowledged but not discussed in practical terms.** Figures 3b and 3e show that cNPIM (and to a lesser extent dNPIM) entirely fails on some hard instances (placed on the horizontal dotted line, never solved). The paper notes this is due to optimizing average success rate, but does not discuss the practical implications: a user cannot know *a priori* which instances will fail, and alternative algorithms (CAC) may offer more consistent performance. This trade-off deserves explicit discussion.

- **Planar G-set results are poor and the response is speculative.** On the unweighted planar instances (N=800, P,+), dNPIM's TTS (4.42e7) is 24× worse than CAC (1.81e6). The paper says "we believe with more careful optimization and improvements to the architecture our method could achieve SOTA," which is an unsupported forward reference. A more direct analysis of why these instances are difficult for the learned dynamics would be more informative.

- **OOD generalization evidence is thin.** Section 4.4 reports only two examples of out-of-distribution behavior (varying problem size and hardness parameter), both on synthetic distributions. The paper states "performance tends to degrade the more the distribution differs" without quantifying the rate or providing any characterization of when graceful vs. catastrophic degradation occurs.

### Trivial
- None.

## Nice-to-Haves

- A single-trajectory variant of dNPIM in Table 1 (even as an ablation) would cleanly separate the algorithmic contribution from the multi-start advantage.
- Wall-clock TTS for Table 2 would complement the iteration-based TTS, given that dNPIM's per-iteration cost includes an MLP forward pass.
- A deeper analysis of what the network learns beyond momentum — for example, comparing the learned effective dynamics (at the level of the update rule) to existing Ising machine designs like CAC or SBM.

## Removed Points

- **"Per-distribution training limits generality"**: The paper is transparent about requiring per-distribution training/tuning, and notes that baselines (Goto et al., Reifenstein et al.) also tune parameters per instance type. This is standard for learned optimization and reflects the paper's stated scope. **Removed as scope creep.**
- **"Missing training details / missing appendix content"**: The paper references Appendix F (reward functions), G (hyperparameters), and E (zeroth-order ablation). The parser strips these sections from all papers; they exist in the original submission. **Removed per hard rule on missing appendix.**
- **"No ablation of the zeroth-order optimizer"**: References Appendix E, stripped by parser. **Removed per hard rule.**
- **"Too strong claims in abstract"**: The claim "achieve state-of-the-art performance on many commonly used benchmarks" is supported by the results on 4/5 neural-CO benchmarks and 4/5 G-set categories, with the time/quality trade-off disclosed. **Removed as not a specific verified weakness.**
- **"Limited expressivity of ~100 parameters"**: Figure 3c shows performance saturates around 50 parameters, so the architecture is adequate for the tested problems. This is evidence of sufficiency, not a limitation. **Removed.**
- **Strength about "systematic analysis of architecture's impact on performance"** : Generic/superficial — the analysis is standard ablation, not a distinctive strength. **Moved here.**

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a single-trajectory dNPIM column to Table 1 (or at minimum report mean ± std across the 30 trajectories). This alone would resolve the most serious evaluation concern.
2. For the large-instance cases where dNPIM is slower (1:20 vs. 0:03), provide an ablation that isolates the implementation bottleneck (dense PyTorch matmul vs. sparse library) and show whether optimized implementation would close the gap.
3. Discuss the practical impact of the hard-instance failures in Figures 3b/3e more explicitly — e.g., report the fraction of instances on which each method fails entirely.

## Score and Decision

### Anchors

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| ROS: GNN-based Max-k-Cut (CpiJWKFdHN) | 5.67 | R1/R2 | Similar area, rejected. Less novel (similar relaxation ideas exist), NPIM has clearer novelty and more evaluation breadth. |
| Neural Solver Selection (CFLEIeX7iK) | 5.75 | R1/R2 | Different framing (solver selection vs. learning dynamics). NPIM is more technically novel. |
| SYMBOL: Symbolic BBO (vLJcd43U7a) | 6.50 | R1 | Accepted. Strong interpretability and generalization, cleaner evaluation. NPIM is weaker on evaluation rigor. |
| Non‑Equilibrium Dynamics for Ising (BlSIKSPhfz) | 6.00 | R1/R2 | Accepted. Closest topic. NPIM is more novel (learning dynamics) but has more evaluation concerns. |
| Unified Neural Solvers for CO (yEwakMNIex) | 6.25 | R1 | Accepted. Broader scope (unified solver across problems). NPIM is narrower. |
| Hercules: LLM CO heuristics (0fwJMANq9P) | 5.25 | R3 | Rejected. LLM-based approach, less directly comparable. |
| LLM-LNS for MILP (Usk4KzBxLW) | 5.25 | R3 | Rejected. Different methodology. |

**Round-1 bracket:** The paper sits between 3.5 and 7.5 — clearly above the 3.0–3.4 weak band (rejected papers with fundamental flaws) and below the 7.5+ strong band (papers with exceptionally clean methodology or theory).

**Round-2/3 narrowing:** Within the middle band, the closest topical anchors are Non‑Equilibrium Dynamics (6.0, accepted) and ROS (5.67, rejected). NPIM is more novel than ROS but has cleaner evaluation than ROS; it is comparable to Non‑Equilibrium Dynamics in overall quality but with a different weakness profile (evaluation protocol concerns vs. limited theoretical guarantees). Relative to the full set of round-2/3 anchors spanning 5.25–6.25, NPIM sits in the lower half due to the verifiable asymmetric comparison issue in its primary benchmark table.

**Final score: 5.5**

The paper makes a genuine contribution — the idea of learning Ising machine dynamics via algorithm unrolling with zeroth-order training is novel, well-motivated, and supported by competitive empirical results across two distinct benchmarks. However, the asymmetric comparison protocol in Table 1 (undisclosed multi-start advantage for dNPIM vs. single-run baselines, no variance reported) undermines confidence in the headline SOTA claims. This is fixable with additional experiments, but in its current form the evaluation does not fully support the stated conclusions. The paper would be a strong candidate after addressing these concerns.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
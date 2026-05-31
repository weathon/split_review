Now I have all the information needed to synthesize the review. Let me carefully construct the final assessment.

---

## Summary

This paper proposes PESLA, a self-supervised method for estimating the energy landscape of stochastic dynamical systems from evolution trajectories alone, without requiring true energy values as supervision. The method combines (1) an adaptive codebook (VQ-VAE style) that discretizes the state space into codewords based on observed data, (2) a graph neural Fokker-Planck equation that models probability evolution across codewords using energy differences, and (3) a physics-inspired regularization term. Experiments on three systems (2D Prinz potential, ecological evolution, and protein folding) show correlation above 0.9 between estimated and ground-truth/reference energies, and a 17.65% improvement in evolution prediction over baselines.

## Strengths

- **Self-supervised energy estimation without energy labels**: The core contribution — inferring energy landscapes from trajectories alone — is novel and well-motivated. The paper clearly defines the learning problem and provides a coherent framework for solving it. Evidence: Section 2 defines the problem as requiring only the observed trajectory X_N; Figure 2 reports Pearson correlation >0.9 across multiple systems.

- **Adaptive codebook handles limited observations effectively**: The codebook-based discretization adaptively partitions the state space based on data coverage, unlike fixed grid binning. This is critical for real-world scenarios where trajectories cover only a tiny fraction of the state space. Evidence: Figure 2a (top) shows PESLA maintains high full-space correlation ρ_F with only 10% of the data, while MSM and APE degrade sharply. Figure 3a (center) visualizes how codewords concentrate in low-energy regions.

- **Graph neural Fokker-Planck equation explicitly ties energy to dynamics**: The architecture that embeds energy differences into a graph neural ODE for probability evolution is clever and physically grounded. Evidence: PESLA achieves 17.65% lower Jensen-Shannon divergence in evolution prediction compared to methods like NeuralMJP, T-IB, VAMPNets, and SDE-Net (Figures 3b, 4b).

- **Robustness to hyperparameter choices**: The paper demonstrates that the occupied codeword count converges automatically as the preset number of codewords varies, and performance peaks near this convergence point. Evidence: Figure 3c shows evolution prediction accuracy, energy estimation accuracy, and codeword occupancy as a function of preset codewords.

## Weaknesses

### Fatal
None.

### Major

1. **Tension between the physics regularization and the claimed elimination of equilibrium assumptions (Section 3.3)**: The paper claims that the L_phy regularization (KL divergence between the empirical distribution p(c_i) and the Boltzmann distribution q(c_i)) "eliminates the assumption of thermodynamic equilibrium sampling." However, the regularization is computed on the *observed* empirical distribution p(c_i). If the training trajectories are not drawn from equilibrium, forcing p(c_i) toward a Boltzmann distribution will bias the energy estimate. The paper's justification — that "long-term evolution of states will eventually converge to the Boltzmann distribution" — would support regularizing the *predicted* long-term distribution, not the empirical distribution of observed (short) trajectories. This is not a fatal flaw since L_phy is a soft constraint among multiple losses, but the framing overclaims what the method achieves. The paper would benefit from either (a) removing the regularization and showing the graph neural Fokker-Planck alone suffices, or (b) clearly acknowledging this as an approximate bias, not a complete elimination of equilibrium requirements.

2. **Protein folding evaluation relies on a model-derived reference, not ground truth (Section 4.4)**: The "reference energy" for the five fast-folding proteins is estimated using TICA + MSM on a larger dataset, not measured experimentally or derived from a known force field. The reported correlation (ρ_T > 0.9) is therefore a measure of agreement between PESLA and a particular computational reference, not a measure of accuracy against the true physical energy landscape. The paper acknowledges this ("Due to the lack of true energy") and follows the same protocol as prior work (Majewski et al., 2023; Mardt et al., 2018), which mitigates the concern. However, the headline claim of "correlation above 0.9 with ground truth" (Abstract) conflates this protein experiment — which does not have ground truth — with the 2D Prinz and ecological experiments, which do. The paper should clearly distinguish which experiments use ground truth and which use a reference model, and discuss the implications for interpretation.

### Minor

1. **Missing ablation study**: The method has several interacting components (adaptive codebook, graph neural Fokker-Planck equation, physics regularization, two-phase training). Without an ablation study that isolates each component, it is difficult to determine which part drives the improvement. For example, how much does the graph neural Fokker-Planck equation contribute vs. a simpler transition model on the codebook? The paper provides data-size sensitivity and codeword-count sensitivity, but a direct component ablation would substantially strengthen the evidence.

2. **Graph neural Fokker-Planck equation (Equation 6) is presented as a design, not derived from first principles**: The paper states it "extend[s] Chow et al. (2012)'s theory" and the resulting equation involves sigmoid-weighted combinations and element-wise products that are pragmatic choices for neural computation. For an applied ML paper this is acceptable, but the "physics-informed" framing raises expectations for a clearer connection between the continuous Fokker-Planck equation and the discrete graph formulation.

3. **Loss balancing coefficients are not reported**: The total loss L = L_reconstruct + L_vq + L_latent + L_code + L_phy is summed with equal weight by default, with no discussion of loss scaling or validation-based tuning. If these losses operate at very different scales, equal weighting could be suboptimal.

### Trivial
None.

## Nice-to-Haves

- Provide a table with per-task numerical values (ρ_T, ρ_F, MJS, TJS) rather than relying solely on figures, to facilitate precise comparison.
- Include an explicit discussion of statistical significance for the claimed 17.65% improvement.
- Study sensitivity to the noise strength parameter β, which is a key physical parameter in the Fokker-Planck equation.
- Report computational cost (training time, model size) for practitioners.

## Removed Points

**"Insufficient baselines for energy estimation (MSM and APE only)"** — Removed. The critic's suggested alternatives (deep potential methods, force-matching approaches) require energy or force supervision, placing them outside the paper's self-supervised scope. MSM is a standard classical method and APE is a natural unsupervised baseline. The paper also compares against four additional baselines for evolution prediction (NeuralMJP, T-IB, VAMPNets, SDE-Net), which indirectly validates the energy estimates.

**Strength: "Physics-inspired regularization removes thermodynamic equilibrium requirement"** — Removed because it conflicts with the verified Weakness #1 (the regularization partially reintroduces equilibrium assumptions rather than fully removing them). The paper's claim on this point is overstated.

**"Protein folding uses a 'circular' reference"** — The critic's "circular" characterization is too strong. The reference (TICA+MSM on 3× data) is an independent estimator, not a function of PESLA's outputs. The concern about the reference's accuracy is retained as Weakness #2, but the framing has been corrected.

## Novel Insights

The harsh critic's primary insight — that the regularization term L_phy creates a tension with the paper's stated goal of avoiding equilibrium assumptions — is genuine and not simply a rephrasing of the paper's own discussion. The paper acknowledges that "this approach fails when evolution trajectories are not sampled from a thermodynamic equilibrium state" but then introduces L_phy based on the *empirical* (observed) distribution p(c_i), not on the *predicted* long-term distribution. This subtle but important gap between the claimed contribution ("eliminates the assumption of thermodynamic equilibrium sampling") and the actual implementation (which still uses the equilibrium Boltzmann form as a regularization target on observed data) is a real finding that the authors should address. The strength finder's claim that the regularization "removes thermodynamic equilibrium requirement" uncritically accepts the paper's framing; the harsh critic correctly identifies the inconsistency.

Beyond the paper's own contributions, no additional novel observations emerged from the review process.

## Suggestions

1. **Clarify the regularization's role**: Either remove L_phy and demonstrate that the graph neural Fokker-Planck equation alone suffices, or reframe the contribution to honestly acknowledge that L_phy is a soft equilibrium bias (not a complete elimination of the requirement), and provide a bound or analysis on when the bias is small.

2. **Add an ablation study**: Isolate (a) adaptive codebook vs. fixed grid, (b) graph neural Fokker-Planck vs. a simpler transition model (e.g., vanilla Markov model on codebook), and (c) with vs. without L_phy. This is the single most impactful addition.

3. **Separate ground-truth vs. reference claims in the abstract and conclusion**: The headline "correlation above 0.9 with ground truth" conflates the 2D Prinz/ecological systems (true ground truth) with protein folding (model-derived reference). Make this distinction explicit.

4. **Report loss weighting or describe a validation procedure** for setting the relative weights of the five loss terms.

## Score and Decision

The paper presents a novel and well-motivated framework for an important problem, with a clever combination of adaptive discretization and physics-inspired neural architecture. The experimental results on two systems with ground truth (2D Prinz, ecological evolution) are strong and support the core claims. The two major weaknesses — the regularization framing tension and the model-derived protein folding reference — are real but not fatal; both are addressable with clarifications or additional experiments. The paper's contributions are substantive enough to merit acceptance, subject to the authors addressing the regularization framing and ablation in a revision.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
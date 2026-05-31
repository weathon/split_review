## Human Reviewer 1

### Summary
The paper proposes an adaptive correction method to enforce physical conservation laws (mass, momentum, norm, energy) in neural operators (FNO, GTNO, UNet). The core idea is to attach a learnable lightweight correction operator that modifies the neural operator output to exactly satisfy conservation constraints.
Unlike soft penalty or projection methods, this operator is trainable, architecture-agnostic, efficient, and strictly conservative.

Experiments show that:

Conservation errors drop to machine precision.

Predictive errors and stability improve.

The method outperforms both loss-based and projection approaches on a range of PDE benchmarks (transport, conservative Allen–Cahn, shallow water, Schrödinger).

### Strengths
It is a clearly written paper enforcing conservation law by correction.

### Weaknesses
1.Limited to low-order conservation laws

Only linear and quadratic conservation are handled.
Extending to higher-order, coupled, or nonlinear conserved quantities (e.g., enstrophy in Navier–Stokes, Hamiltonians in plasma models) would be critical for broader applicability.

2. Single-law enforcement

The method currently supports enforcing one conservation law at a time, which may be insufficient for complex PDE systems with multiple simultaneous invariants.

3. Scope of benchmarks

PDEs chosen are standard (TE, Allen–Cahn, SWE, Schrödinger) but do not test strongly nonlinear or chaotic dynamics, e.g., 2D Navier–Stokes or Burgers turbulence.
Demonstrating performance under chaotic flows or multiscale systems would strengthen the claim of “stability improvement”.

Overall the idea is too simple

### Questions
Can you extend to multiple and nonlinear invariants and boaden benchmarks?

Is it possible to design archiecture that enforces the conservation law by design as a hard constraint?

### Soundness
3

### Presentation
2

### Contribution
1

### Rating
2

### Confidence
5

---

## Human Reviewer 2

### Summary
The authors propose a method to enforce linear and quadratic PDE conservation laws in neural operator architectures. Their proposed method is end-to-end differentiable and thus serves as a learnable correction layer that can be used in any architecture-agnostic setting. The authors validate their empirical performance in several linear and norm-conservation problems, such as the transport and shallow water equations.

### Strengths
The proposed method is simple yet effective at enforcing linear and quadratic conservation laws. The paper is well-written and frames the method clearly. The included experiments and ablations are detailed and clear.

### Weaknesses
Despite these strengths, there are a few areas of improvement. The largest area of improvement is in the breadth of the numerical experiments. I find the current set of experiments lacking in several respects:
1. Since this is fundamentally a mechanism for ensuring conservation laws are satisfied in neural operators, I would recommend the authors compare their method across resolutions with base neural operators and neural operators with a soft conservation loss.
2. Does the proposed method also extend to irregular grids? If so, would recommend adding irregular grid experiments to demonstrate the effectiveness in such settings.
3. While I understand the importance of developing neural architectures that enforce hard constraints and conservation laws, the current set of problems do not sufficiently address this motivation. The chosen problem settings are mostly toy/simple settings; it is clear from the experimental results that enforcing the conservation laws with the proposed method often provides limited improvement in test error. As such, I would recommend identifying and adding a more impactful experimental setting (e.g., possibly a real-world setting) where the benefit of hard constraints really shines.

**Minor notes:**
1. The authors frame U-Net as a neural operator, when it is not in its original architecture, since it is not resolution-agnostic. I recommend the authors change the wording to be more precise.
2. Check typos of “conservation” as “conversation” in the abstract

### Questions
1. How does the proposed method in the linear case compare with other methods for linear conservation laws, such as “Towards enforcing hard physics constraints in operator learning frameworks” (2024) and “Neural conservation laws: A divergence-free perspective” (2022)?
2. How fast is the proposed layer, and how does this scale with the number of grid points? I would recommend the authors include some timing experiments and analysis.

### Soundness
3

### Presentation
4

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper proposes an adaptive correction mechanism designed to enforce physical conservation laws in neural operators. The core idea is to append a lightweight, learnable correction operator to a base model (such as FNO, UNet, or GTNO). This auxiliary operator takes the neural operator's initial prediction and projects it onto a solution manifold that strictly satisfies the desired conservation law. The authors derive specific mathematical forms for this learnable operator to handle both linear conservation laws and quadratic conservation laws. This correction is applied as part of the end-to-end training process, allowing the base model and the correction operator to be jointly optimized. The method is designed to guarantee conservation by construction, rather than simply penalizing violations via a loss term.

### Strengths
1. The primary strength of this work is its ability to enforce conservation laws exactly (down to machine precision, as demonstrated in Table 3). This is a significant advantage over common "soft-constraint" methods that add a penalty term to the loss function and can only encourage conservation. This exact enforcement also leads to demonstrably better long-term simulation stability, as shown in the multi-step rollout for the Schrödinger equation (Figure 2).

2. The method avoids the notoriously sensitive hyperparameter tuning required by loss-based approaches. The proposed adaptive operator is learnable and integrates directly into the training pipeline without requiring such manual tuning.

3. Theoretical motivation: the authors provide specific derivations for the linear and quadratic correction operators. They also present Theorem 1, which provides a theoretical justification that their method (which optimizes over a more-expressive, corrected solution space) can achieve a reconstruction loss less than or equal to an idealized, strictly-constrained baseline model.

4. The method is shown to be effective across multiple neural operator architectures (UNet, GTNO, FNO) and a variety of PDE benchmarks.

### Weaknesses
1. The claim of being "plug-and-play" is undermined by the implementation details of the learnable correction vector A. The paper states that A is parameterized by a "single convolutional layer for UNet and GTNO" but by a "lightweight MLP with three hidden layers for FNO" (Section 4 and Appendix A.4). This design choice appears arbitrary and is not justified. It implies that expert knowledge is needed to design an effective correction operator for different base architectures, which limits the method's out-of-the-box usability.

2. Weak Experimental Baselines: The experimental comparison is not sufficiently rigorous. The paper compares its method against unconstrained base models (FNO, UNet) and two simple constraint methods (a loss-term and a projection method). However, it fails to compare against any state-of-the-art, physics-informed neural operators, such as the Physics-Informed Neural Operator (PINO), which is a much more relevant and powerful baseline for this type of problem. Without this comparison, it is difficult to assess the method's true performance relative to the current SoTA.
-  The ablation study in Table 5 compares the proposed method (FNO + Correction) against FNO+ (FNO + MLP). While this correctly shows that the structure of the correction is important, it is not a complete ablation. A stronger study would compare against a baseline FNO that is given the same number of additional parameters as the correction operator, but integrated into its main architecture (e.g., as wider hidden layers). This would more rigorously test whether the performance gain comes from the proposed structured correction or simply from the added model capacity.

3. Shallow Water Equation (SWE) Evaluation: The SWE benchmark is a system that evolves over time, yet the paper only evaluates it based on a one-step prediction error (u(x,0)→u(x,Δt)). For a paper that claims to improve long-term stability, this is a missed opportunity. A much more compelling evaluation would involve an autoregressive rollout over a time horizon to measure the accumulation of both prediction error and conservation error, similar to what was done for the Schrödinger equation in Figure 2.

### Questions
1.  In Table 4, under the "Norm conservation" section, the prediction error for λ=1e−3 is listed as 90.1±0.32. This value is a massive outlier compared to all other results in the table (e.g., 8.17 for λ=1e−4 and 8.29 for λ=0). Is this a typo, or does the loss-based method truly become catastrophically unstable at this specific weighting?

2. Justification of 10*Δt Rollout: In Figure 2, the baseline FNO shows significant instability after only ten prediction steps (t=10Δt) for the nonlinear Schrödinger equation, despite appearing very accurate in the one-step prediction. Is this a realistic simulation horizon for this problem? How consistent is this instability, or was this a particularly challenging initial condition selected to highlight the proposed method's stability?

3. The derived operator for linear conservation (Equation 8) is elegant. However, a simpler, non-learnable correction could be to distribute the conservation error uniformly across all grid points, or proportionally. The paper mentions the "constant adjustment method" from Geng et al. (2024) but does not seem to include it in the quantitative comparisons in Table 2. How does the learnable operator A compare to these simpler, non-learnable hard-constraint projection methods for the linear case?

4. Hyperparameter Tuning: The paper rightly criticizes the λ-tuning of loss-based methods. However, the base models (FNO, UNet) and the new correction operators (MLP, Conv layer) have their own hyperparameters (learning rates, layer depths, channel widths, etc., detailed in the Appendix). Was a comparable amount of hyperparameter tuning performed for both the baseline models and the proposed corrected models to ensure a fair and fully-optimized comparison?

### Soundness
3

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
4
---
job_id: 476c25f3-f108-4409-99f8-e348e9be3e84
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: beV5wMTRIq.pdf
paper: Physics-Aware Tensor Field Neural PDE for Climate and Weather Prediction
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies a machine learning method for scientific forecasting on spherical geometries, combining neural ODEs, equivariant networks, and physics-aware inductive biases for climate and weather prediction.

## Minimum Quality
Pass ✅. The submission contains the expected components, including abstract, introduction, related work, methodology, experiments, quantitative and qualitative results, and conclusion/limitations. While there are notable concerns about novelty, mathematical precision, and experimental completeness, these do not rise to the level of an immediate desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious reviewer-directed instructions, or other obvious manipulation attempts in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes PA-TFNP, a physics-aware extension of a tensor-field neural PDE framework for climate and weather forecasting. The method combines a tensor-field network intended to capture rotational equivariance on spherical data, modified spherical finite-difference gradients and padding-based boundary handling, and additional physics-inspired terms including diffusion, drag, and geopotential forcing. Experiments on ERA5-based global, regional, and monthly forecasting tasks report improvements over ClimODE, ClimaX, and a neural ODE baseline.

## Strengths
The paper addresses an important problem. Weather and climate forecasting on the sphere is a meaningful application domain for representation learning and neural PDE methods, and the attempt to combine geometry-aware modeling with physically motivated dynamics is well aligned with current interests in scientific ML.

The overall structure of the paper is reasonably coherent. The progression from a baseline TFNP to the physics-aware PA-TFNP is understandable at a high level, and the decomposition into rotationally aware operator design, spherical derivative approximation, boundary treatment, and physics-derived augmentations is conceptually clean.

Some of the empirical results are promising. In **Figure 3** and **Table 1**, the method often improves over ClimODE, especially for geopotential height \(z\) and atmospheric temperature \(t\), and the gains at longer horizons are often more visible than at short horizons. That pattern is at least directionally consistent with the paper’s claim that the physics-aware modifications help temporal stability rather than merely short-horizon interpolation.

The qualitative motivation around boundary effects is one of the clearer parts of the paper. **Figure 2(c)** does show that the baseline error is concentrated near polar and boundary regions, and the TFNP prediction error appears visually smaller there. Even though the evidence is not yet sufficient to fully validate the claimed mechanism, the figure does support the intuition that spherical geometry and boundary handling matter for this task.

The method is also relatively lightweight in reported parameter count. **Table 5** suggests that the proposed variants can be much smaller than ClimODE in some settings, which is potentially useful if the gains are real and robust.

## Weaknesses
I have several substantial concerns. Some are about novelty and positioning, some about technical correctness and underspecification, and some about the experimental evidence. In aggregate, they make the paper fall short of ICLR standards in its current form.

1. **The core method feels like an incremental aggregation of known ingredients, and the paper does not convincingly isolate what is genuinely new.**  
   The proposed recipe consists of: a neural ODE / method-of-lines setup close to ClimODE, a purportedly rotation-equivariant tensor-field block, a spherical finite-difference correction, padding-based boundary conditions, extra handcrafted physical features, and diffusion/drag/geopotential forcing terms. Each ingredient is individually plausible, but the paper does not clearly articulate what the irreducible new idea is beyond “combine several reasonable things.” The contribution bullets on **Page 2** are broad and read more like a packaging of components than a sharply differentiated methodological advance. This matters because ICLR is not just looking for “works better than one baseline,” it is looking for a contribution whose novelty can be clearly located and evaluated.

2. **The claimed rotation-equivariant tensor-field modeling is not mathematically established by the architecture as written, and the formulation in Section 3.2 is confusing.**  
   In **Section 3.2, Page 4**, the “TFN” is defined pointwise as
   \[
   f_{TFN}(I[i,c_{\mathrm{out}}]) = \sum_{c_1=1}^{C_{\mathrm{out}}}\sum_{c_2=1}^{C_{\mathrm{out}}} W[c_{\mathrm{out}},c_1,c_2]\,(I[i,c_1]\cdot I[i,c_2]).
   \]
   There are multiple issues here:
   - The summation indices \(c_1,c_2\) range to \(C_{\mathrm{out}}\), but they should presumably range over input channels if they index \(I[i,\cdot]\). As written, this is dimensionally inconsistent.
   - The operation is pointwise in \(i\), with no explicit coupling across neighboring points on the sphere, no spherical harmonics, no steerable kernel basis, and no group action definition. It is therefore unclear how this architecture, by itself, encodes \(SO(3)\)-equivariance on spherical fields.
   - “Tensor Field Network” is used in a very informal way here. The classical TFN literature cited involves equivariant tensor operations under 3D rotations with explicit representation theory structure. The paper’s Equation in **Section 3.2** does not make that structure visible.
   
   This is not a cosmetic complaint. The paper repeatedly leans on rotational equivariance as a central scientific claim, including in **Figure 1** and the surrounding discussion on **Pages 3-4**, yet the actual operator definition does not substantiate that claim.

3. **There are serious notation and equation inconsistencies in the neural ODE formulation.**  
   The derivation in **Section 3.1, Page 3** is sloppy enough that it undermines confidence in the implementation details:
   - In the displayed ODE system before Equation (2), the approximation \(\widehat F(\cdot)\) is written in a malformed way, mixing multiple arguments outside a consistent function signature.
   - In **Equation (2)**, the integral includes
     \[
     \begin{pmatrix}\frac{d\mathbf{Q}(s)}{d\mathbf{U}(s)}\\ \frac{d\mathbf{S}(s)}{ds}\end{pmatrix},
     \]
     which is almost certainly wrong. One expects something like \(\frac{d\mathbf{Q}(s)}{ds}\) and \(\frac{d\mathbf{U}(s)}{ds}\). The current notation is not mathematically meaningful.
   - The text says “By integrating Equation (2) using the Runge-Kutta method,” but **Appendix C, Page 14** later states “We employed the forward Euler method as our ODE solver.” That is a direct inconsistency about the actual solver used.
   
   These errors matter because the paper’s central pitch is about a PDE-to-ODE dynamical formulation. If the equations are not even internally consistent in the main paper, it becomes difficult to assess what model was actually trained.

4. **The “physics-aware” components are physically underspecified and, in places, physically mismatched to the variables being modeled.**  
   In **Section 3.3, Pages 5-6**, diffusion is added to “scalar quantities such as temperature, humidity, and geopotential,” but the actual experiments use \(z, t, t2m, u10, v10\), and the text also adds a separate momentum correction to the learned velocity field. The paper does not provide a careful variable-wise justification for why the same structural modifications should apply across heterogeneous prognostic quantities. In fact, the authors themselves partially acknowledge this in the limitations on **Page 9**, noting that different variables should probably use distinct equations. That is not a small caveat, it directly weakens the central physical-faithfulness claim.

   Relatedly, the learned diffusion coefficient \(\alpha(\mathbf{x})\) is said to be “non-negative” and in \(\mathbb{R}^{d\times H\times W}\), but there is no explanation of how non-negativity is enforced in optimization. Is \(\alpha = \mathrm{softplus}(\tilde\alpha)\)? Is it clipped? The same issue applies to \(\nu\) and \(\gamma\) if they are meant to have physical sign constraints. Without this, the model can in principle learn anti-diffusion or physically odd forcing.

5. **The boundary-condition story is intuitive, but not fully convincing as presented, and the implementation details are too dataset-specific.**  
   The paper proposes Neumann padding and “average padding” in **Section 3.3**. However:
   - The average-padding formula explicitly uses \(\frac{1}{64}\sum_{i=1}^{64}\cdots\), which hard-codes the longitudinal resolution \(W=64\). This is at odds with the paper’s broader claims about scalability across resolutions.
   - The claim that average padding “transforms the rectangular domain into a sphere-like domain” is not really a mathematical statement, it is a heuristic.
   - **Figure 2(a,b)** is helpful as a cartoon of the padding strategies, but the paper never quantifies how much of the final gain is due to padding versus the spherical derivative correction versus the tensor architecture. The causal attribution remains blurry.

6. **The empirical comparison set is too weak for the strength of the claims.**  
   The abstract claims “state-of-the-art performance,” and **Page 1** says the model achieves “superior performance” with “strict physical fidelity.” Yet the main comparisons are primarily against ClimODE, ClimaX, and a generic neural ODE. That is not enough to substantiate a state-of-the-art claim in modern weather forecasting. Even staying within the scope of what is discussed in the paper, the comparison set is narrow relative to the ambition of the claims. This matters because a method can beat ClimODE and still not be close to the actual frontier.

7. **The results are not uniformly favorable, and the paper overstates consistency.**  
   Several tables weaken the “consistently superior” narrative:
   - In **Table 1, Page 8**, PA-TFNP is clearly worse than ClimODE for \(t2m\) at 6h, 12h, and 18h in both Australia and South America, often by large margins. For example, Australia \(t2m\) at 12h is \(2.98 \pm 1.50\) for PA-TFNP versus \(1.10 \pm 0.22\) for ClimODE. That is not a small regression.
   - In **Table 3, Page 14**, the North America regional results again show substantial degradation for \(t2m\), and also a worse 6h temperature \(t\) score than ClimODE.
   - In **Table 2, Page 9**, PA-TFNP is not consistently better than TFNP. At 2 months, TFNP is actually better than PA-TFNP for \(z\), \(t\), and \(u10\), and tied on \(t2m\). This directly weakens the claim on **Page 9** that PA-TFNP “consistently outperforms the TFNP model.”
   
   This is a major issue because the paper repeatedly uses language such as “consistently outperforms,” but the reported numbers do not support that wording.

8. **Some figures are used more rhetorically than analytically.**  
   **Figure 4** is supposed to establish the benefits of physics-aware modeling over long horizons. It does show lower RMSE for PA-TFNP than TFNP on some variables over time, especially \(z\), \(t\), and \(t2m\). But for \(u10\) and \(v10\), the margins are smaller and the error bars overlap substantially in places. The text on **Page 9** claims improvement “across all scalar quantities,” which avoids the harder question of how much this helps vector wind prediction.  
   Similarly, **Figure 1** presents a polished conceptual story about rotated maps and four regional partitions, but it is not tied to an actual formal group action implemented in the network. The figure is persuasive as intuition, but it substitutes for missing mathematical specificity.

9. **The evaluation emphasizes RMSE almost exclusively and does not verify the claimed physical fidelity.**  
   The paper repeatedly argues for “strict physical fidelity,” “physical consistency,” and “interpretability,” but the metrics are essentially RMSE curves and qualitative error maps. There are no diagnostics for conservation, balanced flow structure, divergence/vorticity behavior over rollout, stability of learned diffusion coefficients, or any direct measurement that the physical terms improve physical realism rather than just regularize the predictor. If you want to sell the method as physics-aware rather than just physics-flavored, this gap matters a lot.

10. **Presentation quality is uneven, with multiple copy-editing and reference issues that hinder trust.**  
   A few examples:
   - “Equation equation 1” on **Page 5**, and similar duplicated wording elsewhere.
   - “CilmaX” typo on **Page 8**.
   - The reference list on **Pages 10-12** is messy and inconsistent in formatting and author names.
   - The paper says the spherical operator is “based on spherical transforms” in the abstract, but the main method presents a corrected central finite difference, not an actual transform-based operator in any obvious sense.
   
   None of these alone would sink the paper, but together they reinforce the feeling that the work was not polished to the level expected for a top conference submission.

11. **Reproducibility details are incomplete in the main paper.**  
   The training setup largely defers to prior work and the appendix, and important details remain vague: how \(\tau_0\) is chosen in \(\beta_t = 1-\exp(-t/\tau_0)\), how \(\alpha,\nu,\gamma\) are parameterized, what exact attention architecture is used, how many past time steps \(T\) are used in the input, and how losses are aggregated across variables and horizons. For a model with several interacting components, these omissions matter.

## Questions
1. The biggest technical issue for me is the equivariance claim in **Section 3.2**. Can the authors give a precise definition of the symmetry group under which the model is equivariant, and show explicitly how the operator in the displayed TFN equation satisfies
   \[
   f(\rho(g)I)=\rho'(g)f(I)
   \]
   for the relevant group action \(g\)? Right now the formula looks like a pointwise quadratic channel mixer rather than a spherical equivariant operator.

2. Please clarify the ODE solver inconsistency between **Page 3**, which mentions Runge-Kutta, and **Appendix C, Page 14**, which says forward Euler. Which solver was actually used for every experiment in Sections 4.1 to 4.4? If different solvers were used in different settings, that should be explicitly tabulated.

3. How are the sign constraints on the physical coefficients enforced? In particular, how is \(\alpha(\mathbf{x}) \ge 0\) guaranteed in the diffusion term
   \[
   \partial_t q_i = -u_i\cdot \nabla q_i - q_i \nabla\cdot u_i + \alpha(\mathbf{x})\Delta q_i?
   \]
   Please also clarify whether \(\nu\) and \(\gamma\) are constrained.

4. Can the authors provide a clean ablation table, in the main paper, separating the effects of: (i) TFN architecture, (ii) spherical derivative correction, (iii) boundary padding, (iv) extra physical features, and (v) primitive-equation-inspired terms? At present, the gains are hard to attribute.

5. Please reconcile the claim that PA-TFNP “consistently outperforms” TFNP with **Table 2**, where TFNP is better than PA-TFNP for several 2-month variables. If the main benefit is only on selected quantities or horizons, the paper should say so directly.

6. Since **Table 1** and **Table 3** show substantial degradation on \(t2m\) at shorter horizons, can the authors explain whether the physics-aware terms are oversmoothing local near-surface variability? A useful rebuttal would include either a diagnosis or an ablation showing which component causes this regression.

7. The paper repeatedly claims physical fidelity. Could the authors report at least one genuinely physical diagnostic, for example rollout behavior of divergence, vorticity statistics, or some conservation-related measure, to show that the gains are not just numerical regularization?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the submission itself. The work uses ERA5 / WeatherBench-style forecasting data and focuses on methodology rather than deployment on sensitive personal data or human-subject experiments.

## Soundness Rating
2: fair. The overall direction is plausible and some empirical gains are visible, but the central technical claims are weakened by equation inconsistencies, underspecified physical parameterization, and incomplete validation of the claimed rotational equivariance and physical fidelity.

## Presentation Rating
2: fair. The paper is readable at a high level, and several figures are helpful, but the presentation suffers from notation errors, internal inconsistencies, imprecise claims, and an insufficiently rigorous exposition of the main operator.

## Contribution Rating
2: fair. The problem is important and the empirical results are somewhat interesting, but the contribution appears incremental, the novelty is not sharply isolated, and the experimental evidence is not strong enough to support the strongest claims.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
The paper is promising and addresses an important problem, but in its current form I do not think it clears the bar. The main reasons are: unclear novelty beyond combining known ingredients, a weakly substantiated equivariance claim, several mathematical and implementation inconsistencies, and empirical claims that are overstated relative to the tables. A substantially revised version with a more rigorous operator definition, stronger ablations, and more careful claims could be competitive.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. It is unlikely, but still possible, that some implementation details are better than the exposition suggests.
---
job_id: c27b6893-c7b4-47c0-9976-098b58b6ca27
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: wVGfJxM2Nz.pdf
paper: Structure-Preserving Machine Learning of Dynamical Systems: A Case for Smaller Models
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, specifically learning on geometries/manifolds, physics-informed and structure-preserving machine learning, and applications to physical dynamical systems.

## Minimum Quality
Pass ✅. The submission contains the expected components, including abstract, introduction, methodological development for both use-cases, experiments, quantitative results, figures, and conclusion. While there are notable technical and exposition issues, they do not rise to the level of an automatic desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find evidence in the provided paper content of hidden prompts, AI-targeted instructions, or other manipulative content aimed at influencing automated review.

# Expected Review Outcome:
## Summary
This paper argues that geometry-aware, structure-preserving models can achieve better robustness and generalization than larger structurally naive models when learning dynamical systems. The paper supports this claim with two case studies: a dissipative 2D heat-transfer system identified via an SPD-constrained linear state-space model optimized on a Riemannian manifold, and a conservative 18D FPUT system modeled using a symplectic Hamiltonian neural network and compared against NeuralODE and LSTM baselines.

## Strengths
The paper has a clear high-level message that is relevant to ICLR, namely that appropriate geometric inductive bias can improve long-horizon behavior and reduce the need for brute-force model scaling. This is a worthwhile theme for the community, especially in scientific ML where one-step fit and rollout stability often diverge.

I appreciated that the paper does not rely on a single toy setting. The two use-cases are intentionally different, one dissipative and one conservative, which helps illustrate that “structure preservation” is not being treated as synonymous with only Hamiltonian systems. That broader framing is useful.

The conservative-system experiments are the stronger part of the paper. **Table 2** and **Figure 3** jointly support an important empirical point: one-step error alone is a poor proxy for physically meaningful long-horizon performance. In **Table 2**, SHNN consistently achieves dramatically lower energy drift than NeuralODE and LSTM across a wide range of parameter counts, and in several cases this advantage persists even when one-step errors are of similar order. The right panel of **Figure 3** makes this especially clear, where SHNN occupies a much lower drift regime than the baselines over the model-size sweep. This is exactly the kind of evaluation I want to see in structure-preserving dynamics papers.

The qualitative visualization for the conservative case is also useful. In **Figure 4(a)**, the SHNN trajectory appears to stay close to the intended energy contour, whereas **Figure 4(c)** shows the LSTM drifting across level sets under an unseen initial condition. Even though these are only 2D slices of an 18D system, the figure helps build intuition for why the drift metric matters and connects the numerical results back to the geometric claim.

For the dissipative case, the comparison between Euclidean and Riemannian optimization is at least directionally interesting. **Table 1** suggests that RieOpt improves substantially over the misspecified physics model and also over EucOpt, especially on the Chicago split, which is the more meaningful generalization test. The main claim here, that enforcing a physically meaningful matrix geometry may stabilize generalization across forcing conditions, is plausible and partially supported by the results shown.

The paper is also refreshingly explicit about model size in the conservative case. Many papers claim “efficiency” without actually showing parameter-count tradeoffs; here, **Table 2** reports parameter counts, which makes the “smaller but more robust” claim easier to evaluate.

## Weaknesses
I think the paper’s central intuition is interesting, but the current manuscript has several technical and empirical issues that materially weaken the scientific case.

1. **The dissipative case has serious mathematical inconsistencies around the SPD interpretation of the dynamics, and this affects the core methodological claim.**  
   On **Pages 3-4**, the paper argues that the continuous-time state matrix \(A\) is symmetric and that its discretization \(\Phi_A = e^{A\tau}\) lies on the SPD manifold. That part can hold if \(A\) is symmetric. However, the paper repeatedly conflates positive definiteness of \(\Phi_A\) with discrete-time stability in a way that is not correct as written. For a discrete-time linear system \(x_{t+1}=\Phi_A x_t\), stability requires the spectral radius \(\rho(\Phi_A)<1\), not merely \(\Phi_A \succ 0\). In fact, an SPD matrix can have eigenvalues \(>1\) and therefore be unstable. The text on **Page 4** says stability is preserved “by means of their positive eigenvalues implying positive definiteness,” which is insufficient. It also states that stable eigenvalues in the left half-plane are wrapped “within the unit circle in the s-plane where \(Re(\lambda_i)>0\),” which appears backwards and confused: the left half-plane is in the \(s\)-plane, the unit disk is in the \(z\)-plane, and positivity of the real part is not the discrete-time stability condition. This is not a cosmetic issue, because the entire rationale for constraining \(\Phi_A\) to SPD is presented as a stability-preserving geometric prior. As written, that rationale is mathematically shaky.

2. **The loss for the dissipative model is incorrectly or at least inconsistently specified in Equation (7).**  
   In **Equation (4)**, the model is \(\mathbf{T}_{t+1}=\Phi_A \mathbf{T}_t + \Phi_B \mathbf{U}_t\). But in **Equation (7)**, the paper defines  
   \[
   \mathcal{J}(X|\Phi_A,\Phi_B)=\sum_{i=1}^{n-1}\left\|\Phi_A \mathbf{T}_i + \Phi_B \mathbf{T}_i - \mathbf{T}_{i+1}\right\|_2^2.
   \]
   This uses \(\Phi_B \mathbf{T}_i\) rather than \(\Phi_B \mathbf{U}_i\), which is inconsistent with the stated model and dimensions. On **Page 3**, \(B\) and \(U\) are also described with inconsistent shapes, first as \(U\in\mathbb{R}^{2\times 1}\), later as \(U\in\mathbb{R}^{1\times 1}\). For a two-state, one-input system, these objects should be defined cleanly and consistently. Because the dissipative method is extremely lightweight, the exact optimization problem matters a lot. Right now, the key objective is underspecified or misstated.

3. **Several notation choices are overloaded or internally inconsistent, which makes the derivation harder to trust than it should be.**  
   The symbol \(\mathrm{T}\) is used both for the temperature state vector and, in the spectral decomposition sentence on **Page 3**, something like the inverse of the eigenvector matrix, “\(A = V \Lambda T^{-1}\),” where one would expect \(V^{-1}\) rather than a new \(T^{-1}\). This is especially unfortunate because \(T\) is already the physical state. There are also inconsistencies between \(q_0=q_N=0\) in **Equation (10)** and “\(q_0=q_{M+1}=0\)” in the surrounding text on **Page 5**. These may sound minor, but in a paper whose main selling point is mathematically informed structure, such sloppiness reduces confidence.

4. **The dissipative experiments are not strong enough to support the claimed message about “smaller models” or broad generalization.**  
   The heat-transfer case is a 2D linear system with one-year hourly forcing and a highly constrained state-space model. This is a perfectly fine pedagogical example, but it is too small and too specialized to substantiate the paper’s broader thesis. The naive baselines, RF/XGBoost/LSTM, are not especially compelling comparators for a known low-dimensional linear dynamical system with explicit physical structure. It is not surprising that a physically parameterized LSSM behaves better out of distribution than generic regressors trained as time-series predictors. The issue is not that the result is wrong; it is that the claim being made is larger than the evidence.

5. **The baseline design in the dissipative case is not very fair, and the comparisons are partly stacked in favor of the proposed view.**  
   On **Pages 6-7** and in the appendix description on **Page 12**, the LSTM appears to be trained separately per temperature variable and struggled because the dataset is “relatively small.” That may be true, but if the main claim is that structure-aware modeling gives better sample efficiency, the baseline tuning needs to be more careful and better documented. Why are the naive baselines limited to RF, XGBoost, and LSTM? A more direct comparison would include linear ARX/state-space identification baselines, least-squares estimation of \((\Phi_A,\Phi_B)\), or a stability-constrained Euclidean parameterization such as \(\Phi_A = L L^\top\) with ordinary optimization, which the paper itself mentions on **Page 5** but does not test. Right now the dissipative case is comparing a highly appropriate model class against several somewhat mismatched generic forecasters.

6. **The conservative case uses only a single training trajectory from one excitation pattern, which makes the generalization claims narrower than the writing suggests.**  
   On **Page 7**, the FPUT dataset is generated from a single long trajectory with one initial condition, then chronologically split 80/20. This is a standard setup for forecasting, but it is much weaker than learning across a family of trajectories. The paper later discusses “unseen initial conditions,” but the evaluation shown in **Figure 4(b,c)** is qualitative, and the paper does not provide a corresponding quantitative table across multiple unseen initial conditions, perturbation magnitudes, or random seeds. Since the whole point is robust generalization, I would expect a systematic multi-trajectory generalization test, not only one held-out tail of a single trajectory and a qualitative OOD plot.

7. **Model selection appears to rely on test-set outcomes in a way that is not cleanly separated from final evaluation.**  
   In the conservative case, the paper says on **Page 7** that it sweeps \(L\) and \(W\), and **Table 2** then marks “hand-picked ‘best’ size vs. loss trade-off models in bold.” The manuscript does not specify a validation split or a model-selection protocol distinct from the reported test split. Likewise, in the dissipative case, the London data are used for training/testing and Chicago is used as a secondary test set, but the exact split and any validation strategy are not clearly described in the main paper. This matters because the “smallest good model” narrative is highly sensitive to how size was selected. Without a clean validation pipeline, it is hard to know how much of the parameter-efficiency claim would survive strict held-out model selection.

8. **The empirical evidence for the “smaller models” claim is only convincing in one of the two use-cases.**  
   In the FPUT case, the paper does a model-size sweep and reports parameter counts in **Table 2**, which is good. In the dissipative case, however, there is no comparable analysis of model size versus performance. The baselines are not normalized for capacity in an informative way, and the proposed method is not really a “small model” in the same sense as a neural model sweep, it is a heavily constrained linear system with only a handful of parameters. So the title claim is broader than the experimental design actually supports.

9. **The paper’s literature positioning is thin relative to the breadth of its claims.**  
   The introduction cites HNNs, SHNNs, SympNets, equivariant models, and thermodynamics-informed learning, but the paper does not really position the dissipative case against prior structure-preserving learning approaches for dissipative systems, nor does it clearly explain what is new beyond applying existing geometric ideas to two case studies. For the conservative case in particular, the use of SHNN is explicitly described as adopting an established architecture, so the contribution is mostly empirical framing rather than methodological development. That can still be publishable, but then the comparative study has to be especially airtight, and currently it is not.

10. **Some figures are helpful, but some interpretation is overstated or under-supported.**  
    **Figure 2** is visually effective in illustrating the idea of projected energy slices, but the text on **Page 5** says that visible jumping between level sets is indicative of energy drift from model discrepancy. In a sliced visualization of an 18D Hamiltonian surface, that claim needs to be handled more carefully, because apparent mismatch in 2D projections can be caused by the slicing procedure itself unless the precise comparison is rigorously defined. Similarly, in the dissipative appendix **Figure 5** and **Figure 6**, the visual gap between RieOpt and EucOpt exists, but the main paper’s narrative pushes quite hard on global stability and decoupled dynamics without showing a broader robustness study or uncertainty across runs. The figures are suggestive, not decisive.

11. **Presentation quality in the main paper is uneven, with enough errors to hinder confidence.**  
    There are multiple duplicated words (“where where” on **Page 5**), malformed statements, and some informal geometric claims that are not precise enough for a methods paper. This is not just style. For example, the statement on **Page 4** that points on the boundary of the SPD manifold are “positive semi-definite attributed to their low-rank and are said to be bistable” is not standard terminology and is not adequately justified. A clearer separation between intuitive geometry and rigorous claims is needed.

## Questions
1. For the dissipative case, can the authors clarify the exact optimization problem being solved? In particular, please correct or confirm **Equation (7)**, specify whether the loss uses \(\Phi_B \mathbf{U}_i\) or \(\Phi_B \mathbf{T}_i\), and provide the exact tensor shapes for \(\Phi_A\), \(\Phi_B\), \(\mathbf{T}_i\), and \(\mathbf{U}_i\). This is important because the current equation appears dimensionally inconsistent.

2. Can the authors sharpen the mathematical claim connecting the SPD constraint to discrete-time stability? If the intended condition is actually \(0 \prec \Phi_A \prec I\), or a continuous-time negative-definite/symmetric parameterization before exponentiation, please state this explicitly. As written, \(\Phi_A \in Sym_n^+\) alone does not guarantee \(\rho(\Phi_A)<1\).

3. For the conservative case, what is the exact model-selection protocol for choosing \(L\) and \(W\)? Was there a validation split distinct from the reported test split? If not, I would strongly encourage the authors to rerun the model-size selection using a validation set and keep the test set strictly for final reporting.

4. Can the authors provide quantitative evaluation over multiple unseen initial conditions for the FPUT task, rather than only the qualitative examples in **Figure 4(b,c)**? A table reporting rollout MSE and energy drift over a set of perturbed initial conditions would materially increase my confidence.

5. For the dissipative use-case, why were the main baselines generic regressors rather than stronger system-identification baselines, for example ordinary least-squares state-space identification, constrained stable linear models, or a Cholesky-parameterized Euclidean baseline for \(\Phi_A\)? Adding such baselines would help isolate whether the gain comes from the Riemannian optimization itself or simply from using the right linear dynamical model class.

6. In **Table 2**, some NeuralODE drift values are extremely large despite competitive one-step MSE. Can the authors clarify whether all models use the same rollout horizon, solver tolerances, and evaluation procedure in physical units? A small implementation detail can strongly affect these drift numbers.

7. The paper’s title emphasizes “a case for smaller models.” Would the authors consider tempering this claim or supporting it with a matched size-performance study in the dissipative case as well? Right now the evidence is much stronger for “structure helps long-horizon stability” than for a general statement about smaller models.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No ethics concerns arose from my reading of the submission. The paper studies synthetic/physics-simulated dynamical systems and does not involve sensitive human data, deployment on high-risk populations, or obviously harmful applications.

## Soundness Rating
2: fair. The empirical trend in the conservative case is meaningful, but the dissipative mathematical formulation contains important inconsistencies, and the evaluation methodology leaves several questions unresolved.

## Presentation Rating
2: fair. The core story is understandable, and some figures are genuinely helpful, but notation, equations, and several geometric claims need much tighter editing and clarification.

## Contribution Rating
2: fair. The paper raises a relevant and interesting point about structure-preserving inductive bias, but the methodological novelty is limited, and the experimental evidence does not fully support the breadth of the stated claims.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
My main reason for leaning negative is that the paper over-claims relative to what is rigorously established. The conservative SHNN results are promising and probably the strongest part of the submission, but the dissipative formulation has nontrivial mathematical and notational problems, and the experimental design does not yet justify the broader title-level claim about smaller models in a general sense.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. I carefully checked the mathematical exposition and empirical setup in the main paper, and while some implementation details are missing, I think the key concerns are substantive rather than superficial.
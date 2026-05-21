---
job_id: f3d5fb38-cc46-477f-a686-04ae855ebc73
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: GiaF5cFIpI.pdf
paper: Adaptive Stimulation & Response Modeling of Latent Neural Dynamics
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, combining representation learning, online/streaming latent-state modeling, kernel-based response estimation, and constrained optimization for a neuroscience application.

## Minimum Quality
Pass ✅. The paper contains the necessary scientific components, including Abstract, Introduction, Methods, Experiments/Results, and Discussion, and it presents a coherent methodological contribution with empirical evaluation, although several technical and validation issues remain.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious instructions to automated reviewers, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper proposes a real-time framework for adaptive neural stimulation in latent spaces. The method combines streaming latent-space construction, online dynamical modeling, a kernel-regression estimator for stimulus-response effects conditioned on latent state and time, and a constrained optimization procedure for selecting stimulation patterns that push neural activity along a desired latent direction. The framework is evaluated on toy systems, simulated stimulations on calcium imaging and electrophysiology datasets, and comparisons across multiple latent representations and dynamical models.

## Strengths
The paper aims at an interesting and difficult problem, namely closed-loop control of latent neural dynamics under realistic constraints such as high-dimensional stimulation, sparsity in targeted neurons/channels, and non-negativity of stimulation. This is a meaningful problem setting, and it is broader than simply improving decoding accuracy.

A real strength is the systems-level integration. The paper does not only propose one estimator, it combines four components that are usually treated separately, streaming dimensionality reduction, online latent dynamics prediction, adaptive stimulus-response estimation, and constrained stimulation design. Even if some pieces are adapted from prior work, the overall pipeline is reasonably cohesive and practically motivated.

The response-modeling component in Equation (7) is simple but sensible for the stated low-data regime. Conditioning the regression on latent state \(x\), stimulation \(u\), and time \(t\) is a reasonable design choice when the mapping may drift over an experiment. The temporal kernel is also a pragmatic way to handle nonstationarity without imposing a rigid parametric drift model.

The paper does a good job illustrating the intended workflow. **Figure 2a** is especially useful because it clarifies the distinction between predicted autonomous dynamics and stimulation-induced deviation, which is central to the whole method. **Figure 2e** also communicates the adaptation story fairly well, namely that the regression-based model can recover from a flipped or rotating response map more effectively than a stimulation-blind predictor.

The paper includes multiple modalities, calcium imaging and electrophysiology, and multiple latent-space constructions and dynamical predictors. That breadth is appreciated. **Figure 1b** is useful in showing that different latent spaces can induce visibly different flow fields on the same neural recording, which supports the authors’ motivation for tracking several latent representations in parallel rather than assuming a single “correct” manifold.

The real-time feasibility claim is at least partially supported. The paper reports end-to-end runtimes below 100 ms and average runtimes below 10 ms, which matters for the intended deployment setting.

There are also some useful quantitative comparisons in the supplementary tables. For example, **Table 8** shows that on the Zong dataset with KF dynamics, one-step prediction errors in proSVD/sjPCA spaces remain consistently below mmICA across open/closed and flip/non-flip conditions. This at least suggests the framework is not completely tied to one fragile operating point, even if the evaluation still leaves open questions about realism and statistical rigor.

## Weaknesses
1. **The central empirical validation is too indirect because the “real data” stimulation experiments are largely simulated rather than demonstrating control with real interventions.**  
   This is the biggest issue for me. In Section 4.1, the paper states that for the real datasets, stimulations are *simulated* using an autoregressive additive model, \(y_t = r_t + a_t,\; a_t = 0.8 a_{t-1} + u_t\) (Page 7). That means the claimed success of the response model and optimizer on “real neural data” is mostly success on synthetic perturbations layered on top of real recordings. This is a much easier and cleaner setting than actual closed-loop stimulation, where artifacts, nonlinear network effects, targeting errors, saturation, state dependence, and delayed indirect responses all matter.  
   The paper does mention additional analyses on real stimulation datasets in the appendix, but the main-paper claims are much stronger than the main-paper evidence. The title and framing suggest adaptive stimulation and response modeling of latent neural dynamics, but most main results validate recovery under author-designed perturbation models. That gap matters scientifically because it limits how much one can conclude about real closed-loop utility.

2. **The optimization formulation in Equation (8) is not well matched to the stated sparsity constraint, and the objective is somewhat muddled mathematically.**  
   The paper says it replaces an \(L_0\) constraint with an \(L_1\) constraint to encourage roughly \(n\) active neurons, but Equation (8) uses
   \[
   \min_{u\in\mathbb{R}^N} -\frac{v^\top s(u)}{\|v\|\|s(u)\|} + \lambda_1(\|u\|_0^{\max} - \|u\|_1), \quad \text{s.t. } 0 \preceq u \preceq 1.
   \]
   Under the box constraint \(u_i\in[0,1]\), minimizing \((\|u\|_0^{\max}-\|u\|_1)\) pushes \(\|u\|_1\) *up*, not down, so the regularizer actually rewards larger total stimulation unless balanced by the cosine term. That is not a standard relaxation of cardinality, and it does not directly enforce “close to \(n\) nonzeros”. In fact, because \(\|u\|_1\) conflates amplitude and support size, a dense low-amplitude vector and a sparse high-amplitude vector can receive similar penalties.  
   This matters because the paper repeatedly interprets the optimizer as satisfying a sparse-targeting budget. As written, the objective does not convincingly encode that. A more defensible setup would use either an explicit inequality \(\|u\|_1 \le \tau\), projected top-\(k\) structure, or a differentiable surrogate specifically aimed at cardinality. Right now, the optimization story is oversold relative to the formulation.

3. **There are inconsistencies and underspecifications in the algorithmic description around delayed responses and history handling.**  
   In Algorithm 1, line 10 computes \(s_{\text{obs}} \leftarrow x_t - \hat{x}_t\), and line 11 updates \(\hat S\) with \((x_{t-d},u_{t-d},s_{\text{obs}},t)\). But the delayed model in Section 2.3 writes the response as affecting \(x_{t+1}\) through \(S(x_{t-d},u_{t-d})\), and the exact relationship between \(\hat x_t\), \(\hat f_t(x_{t-1})\), and the delayed correction is not fully synchronized with the notation in Equations (4)-(6).  
   More importantly, the paper assumes “there is never more than one stimulus pending at a given time” (Page 5). This is a very strong operational assumption for a supposedly general adaptive framework, and it sidesteps the harder but more realistic case of overlapping responses. If the method fundamentally requires non-overlapping stimulation/response windows, then that limitation should be stated much more prominently because it constrains practical applicability and experimental throughput.

4. **The experimental comparisons are not strong enough to establish that the proposed response model is the right method, as opposed to merely better than a deliberately weak blind baseline.**  
   Throughout Figures 2e and 3c, the main comparator is a model that is “blind to stimulation effects.” Of course a stimulation-aware model should outperform a stimulation-blind one during stimulation periods. That is almost built into the setup. What is missing are stronger baselines for the response estimator itself, for example a local linear model, a parametric bilinear model in \((x,u)\), nearest-neighbor retrieval without kernels, Gaussian process regression in the low-data regime, or even a simpler kernel regression variant without temporal adaptation.  
   This matters because the paper’s main methodological claim is not merely “using stimulation information helps”, it is that this specific adaptive nonparametric response model is effective. The current comparisons do not isolate that claim well.

5. **The paper’s evaluation metric for stimulation design is too self-referential and not sufficiently outcome-based.**  
   In Section 4.2, the main target metric is angular agreement between the desired vector \(v\) and either predicted response \(s(u)\) or observed deviation \(s_{\mathrm{obs}}\). This is reasonable as a first diagnostic, but it is not enough to establish useful control. A tiny vector almost perfectly aligned with \(v\) may be practically irrelevant, whereas a larger but slightly misaligned perturbation may be more meaningful. The paper partly recognizes this in Figure 5b through a projection-based metric, but even there the interpretation becomes slippery, and Appendix G explicitly notes artifacts induced by the absolute cosine form.  
   The issue shows up in **Figure 4c**, where predicted error is said to function as a “loose lower bound” on observed error. That is not a very strong guarantee, and the scatter suggests substantial mismatch. If the optimizer is to be trusted online, one would want calibration analyses, confidence estimates, or at least systematic reporting of response magnitudes, not only angles.

6. **The presentation of the latent-space selection component is interesting but underdeveloped and under-validated.**  
   The paper claims it can evaluate multiple latent spaces and models in parallel and identify where each is most predictive. **Figure 1c** is visually suggestive, but the methodology behind these heatmaps is not clearly specified in the main paper. The text says predictive error is aggregated “within a local region of the latent space,” but there is no clear definition of the neighborhood, weighting, smoothing, or statistical reliability.  
   Moreover, the practical benefit of adaptive switching among spaces is asserted more than demonstrated in the main text. Since this is presented as one of the paper’s contributions, it needs stronger, cleaner evidence in the main paper, not just an appealing visualization.

7. **Some mathematical and notational details are sloppy enough to reduce confidence.**  
   A few examples:  
   - In Section 2.1, Equation (1) says jPCA compares the low-dimensional neural state \(X\) with its time derivative \(X\), which is clearly a notation error; presumably one of these should be \(\dot X\) or a discrete difference.  
   - The eigendecomposition after Equation (1) is written as \(U_t \Sigma_t U_t^\top = M_t\). For a real skew-symmetric matrix, eigenvalues are generally imaginary and the eigendecomposition is not naturally written in this symmetric-looking form. jPCA is usually based on paired complex eigenvectors or an equivalent real plane construction. The paper may be compressing details, but the current expression is at best misleading.  
   - Equation (2) defines \(\Omega_{t,i}\) through an optimization with an unspecified norm, and the indexing \(U_{t,i}=(U_t)_{[2i:2i+1]}\) is ambiguous about whether these are columns or rows.  
   - Equation (7) gives the kernel regressor, but the kernels’ bandwidths, normalization conventions, and stochastic coordinate descent procedure are not specified in enough detail for reproducibility or for assessing stability.  
   These are not cosmetic issues. The paper leans on algorithmic novelty, so imprecision in the core equations matters.

8. **The claim that the method “quickly learns” within 10-20 stimulations is not convincingly generalized.**  
   This statement appears in the abstract and introduction-level claims, but the evidence is narrow and task-specific. **Figure 2c** shows error reduction in a toy circular system, and **Figure 3c** shows lower prediction error than a blind baseline on a simulated-stimulation dataset, but neither is enough to support a broad statement about sample efficiency across modalities, latent models, or response complexities. The number “10-20 total stimulations” is memorable, but the paper does not provide a systematic sample-efficiency study with confidence intervals across diverse settings.

9. **The breadth of the framework comes at the expense of depth in any one component, especially novelty relative to existing ingredients.**  
   sjPCA adds a streaming implementation and per-plane Procrustes stabilization to jPCA; the response model uses a fairly standard kernel-regression idea; the optimizer uses cosine alignment and box-constrained L-BFGS-B with an \(L_1\)-style encouragement term. The integrated pipeline is useful, but many pieces are incremental on their own.  
   This would be less of a problem if the empirical case were exceptionally compelling, but because the main evidence is mostly toy or simulated perturbation-based, the contribution lands as promising but not yet fully convincing for ICLR.

10. **The tables reveal a pattern that deserves more scrutiny than the paper gives it.**  
   In the supplementary **Tables 1-3** and **7/9/11**, the “closed” conditions often have much larger \(s_{\hat{}}\) errors than open conditions, sometimes dramatically so, for example on O’Doherty with KF in **Table 1**, where proSVD goes from \(2.25 \pm 0.36\) (open) to \(10.21 \pm 1.19\) (closed). Even if these are different metrics or harder settings, the paper does not sufficiently unpack why the closed-loop estimator appears so much worse by that measure. Similarly, in **Tables 4-6** and **8/10/12**, the one-step prediction errors are often fairly close across proSVD and sjPCA, which somewhat weakens the stronger narrative that the proposed latent-space machinery yields decisive practical advantages.  
   In short, the tables contain useful data, but they also complicate the story, and the paper does not confront those complications directly enough.

## Questions
1. The biggest issue for me is the realism of the real-data evaluation. Can the authors clarify, in the main-paper terms, which conclusions are supported by actual stimulation measurements and which are supported only by simulated perturbations added to recorded data? A more explicit separation of these claims would increase my confidence.

2. For Equation (8), can the authors justify mathematically why
   \[
   \lambda_1(\|u\|_0^{\max} - \|u\|_1)
   \]
   is the right surrogate for a sparsity or cardinality budget under \(u_i \in [0,1]\)? Right now it seems to reward larger \(\|u\|_1\). If the actual implementation uses an additional constraint or projection step, that should be stated clearly.

3. Can the authors provide a cleaner derivation of the delayed-response update used in Algorithm 1 and its relation to Equations (4)-(6)? In particular, what exact predictor is used to form \(s_{\text{obs}}\) when \(d>0\), and how is contamination from previous stimulations avoided beyond the single-pending-stimulus assumption?

4. Why is the stimulation-aware kernel regressor only compared against a stimulation-blind baseline in the main paper? If the authors have results against simpler stimulation-aware baselines, that would materially change my assessment.

5. For the latent-space switching idea in **Figure 1c**, can the authors define precisely how the “best predictive probability” heatmaps are constructed? What neighborhood function, aggregation window, and uncertainty treatment are used? A formal definition would help.

6. The jPCA-related notation is currently hard to trust. Can the authors rewrite Equation (1) and the decomposition following it more carefully, using standard jPCA notation? In particular, how exactly is the skew-symmetric operator represented and converted into real 2D planes online?

7. In **Figure 4**, the design metrics emphasize angle. Can the authors also report response magnitude, success-under-threshold, or calibration metrics that better reflect practical control quality? A small aligned perturbation is not obviously a successful intervention.

8. The paper repeatedly highlights fast runtimes. Which parts of runtime are measured, only optimization and state updates, or also all bookkeeping and kernel-bandwidth tuning? A precise accounting would be helpful.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are evident from the submission. The work uses publicly available neural datasets and focuses on methodology for adaptive stimulation and response modeling. While the application domain touches neural intervention, the paper does not present direct human deployment or clearly harmful operational guidance beyond standard closed-loop neuroscience methodology.

## Soundness Rating
2: fair. The overall framework is plausible and some experimental evidence is supportive, but key claims rely too heavily on simulated perturbations, the optimization formulation is not fully convincing, and several mathematical/algorithmic details need clarification.

## Presentation Rating
2: fair. The paper is readable at a high level and the figures help, but the notation is inconsistent in places, several core equations are underspecified, and some contributions are described more cleanly than they are actually defined.

## Contribution Rating
2: fair. The integrated problem setup is interesting and potentially useful, but the empirical validation is not yet strong enough, and several components feel incremental without stronger evidence that the full system materially advances the state of the art.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
The paper is interesting, ambitious, and clearly motivated, and I do think there is something worthwhile here. However, the combination of indirect evaluation on simulated perturbations, a weak baseline story for the response model, and unresolved issues in the optimization/math presentation keeps it below the bar for me in its current form.

## Reviewer Confidence
4: confident. I am confident in my assessment, though not absolutely certain. It is unlikely, but not impossible, that I misunderstood some implementation details that are only implicit in the current presentation.
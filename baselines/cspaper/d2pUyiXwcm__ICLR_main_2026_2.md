---
job_id: 1005c0bb-0a07-4470-b8a3-f04388c47d79
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: d2pUyiXwcm.pdf
paper: Physics-Informed Inference Time Scaling for Solving High-Dimensional Partial Differential Equations via Defect Correction
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅ This paper is clearly within ICLR scope: it proposes a hybrid machine learning and stochastic simulation method for high-dimensional PDE solving, with relevance to scientific ML, probabilistic methods, optimization, and applications to physical sciences.

## Minimum Quality
Pass ✅ The paper contains the expected scientific components, including abstract, introduction, methodological development, theoretical claims, experiments, quantitative results, and conclusion/discussion. While I found several technical and presentation issues that weaken the submission, they do not rise to the level of an automatic desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅ I did not find evidence of hidden prompts, manipulative instructions to automated reviewers, or other concealed content targeting the review process in the provided paper text.

# Expected Review Outcome:
## Summary
This paper proposes SCaSML, an inference-time correction framework for high-dimensional semi-linear parabolic PDEs. The main idea is to take a pre-trained surrogate solver, derive a PDE for its defect \(u-\hat u\), and then estimate that defect at inference time using Multilevel Picard based stochastic simulation, without retraining the surrogate. The paper provides a theoretical argument that the final correction error scales like the product of surrogate error and simulation error, and reports empirical improvements over PINN, GP, and naive MLP baselines on several PDE benchmarks up to 160 dimensions.

## Strengths
The core idea is interesting and, at a high level, quite clean: rather than retraining or fine-tuning a surrogate, the method treats the residual/defect as a new PDE to solve at inference time. That framing is intuitive and potentially useful for scientific ML settings where one needs higher accuracy only at selected query states.

The paper targets an important problem. High-dimensional PDE solving remains a hard area where learned surrogates can be fast but brittle, and purely simulation-based solvers can be more principled but expensive or unstable. A method that combines the two at inference time is relevant to the ICLR audience, especially given the current interest in hybrid ML-numerics methods.

The empirical section is broad in problem coverage. The paper evaluates linear convection-diffusion, viscous Burgers, an HJB/LQG problem, and a diffusion-reaction example, with dimensions ranging from 10 to 160. That breadth is useful because it suggests the method is not tuned to a single toy problem.

I appreciated the comparative message in **Table 1** on **Page 7**. The table makes a clear point that SCaSML usually improves substantially over the base surrogate and often avoids the catastrophic behavior of naive MLP, especially on the harder nonlinear examples. For instance, in the LQG rows, naive MLP has very large errors while SCaSML remains close to the surrogate but consistently better. This is one of the more convincing pieces of evidence in the paper because it shows the hybrid method is not merely averaging two comparable solvers, it is stabilizing a weak simulation method with a better initialization/control variate.

The figures are also effective in conveying the intended use case. **Figure 1** on **Page 3** gives a straightforward conceptual picture of the pipeline, and **Figure 2** on **Page 6** is helpful in connecting the defect PDE to the MLP correction stage. These figures do more than decorate the paper, they clarify the algorithmic decomposition into surrogate prediction followed by stochastic refinement. In particular, **Figure 3(c)** on **Page 9** visually summarizes that SCaSML is usually on the better side of the accuracy-runtime tradeoff compared to the listed baselines, which supports the practical motivation.

The paper also tries to provide theory rather than only an engineering recipe. The multiplicative form of the error bound, stated in **Theorem 2.5** on **Page 6**, is a useful way to articulate why a better surrogate should make the defect easier to simulate. Even though I have concerns about parts of the formal presentation, the intended theorem is meaningful.

## Weaknesses
I have substantial concerns about mathematical correctness and exposition in the main paper. Some of these are fixable presentation issues, but others are more serious because they undermine confidence in the exact formulation of the proposed method.

1. **There are clear notation and equation errors in the core defect formulation, including what looks like a wrong PDE and a wrong terminal condition.**  
   This is my biggest concern because it hits the central contribution. On **Page 2**, the text says “the defect, defined as \(\hat u := u-\hat u\),” which is already inconsistent because \(\hat u\) was previously the surrogate. Then in **Definition 2.1**, **Equation (4)** on **Page 3**, the terminal condition is written as
   \[
   \tilde u(T,\mathbf y)=g(\mathbf y)-\tilde u(T,\mathbf y),
   \]
   which is almost certainly incorrect. It should presumably be
   \[
   \tilde u(T,\mathbf y)=g(\mathbf y)-\hat u(T,\mathbf y),
   \]
   consistent with the later notation in **Equation (6)**. As written, the boundary condition is self-referential and cannot be the intended statement.  
   The same issue appears again for the semilinear case in **Fact 2.3**, **Equation (7)** on **Page 4**, where the PDE starts with
   \[
   \frac{\partial \hat u}{\partial r}+\mathcal L \breve u + \tilde F(\breve u,\sigma^\top \nabla_y \breve u)=0.
   \]
   This should almost certainly be \(\partial_r \breve u\), not \(\partial_r \hat u\). Since this equation is the centerpiece of the paper, such an error is not cosmetic. It makes it hard to trust the derivation as presented in the main text, and it forces the reader to reverse engineer the intended mathematics.

2. **The notation for the defect is inconsistent across the paper, which materially hurts readability and interpretability of both the method and the theorems.**  
   The paper uses \(\tilde u\), \(\breve u\), \(\bar u\), and even in one place appears to reuse \(\hat u\) for the defect. On **Pages 3-4**, the linear warmup defines \(\tilde u\), but **Equation (5)** on **Page 4** suddenly writes \(\breve u(s,x)=\mathbb E[\cdots]\). Then the semilinear section uses \(\breve u\), while the appendix later uses \(\bar u\). This is not a harmless notation preference. Because the method involves the surrogate value, the defect, the corrected solution, and the pair \((u,\sigma^\top \nabla u)\), the notation needs to be extremely disciplined. Here it is not. As a result, several statements are unnecessarily difficult to verify.

3. **Some theoretical assumptions and statements are either misstated or stronger than the text admits, and the main-paper theorem is underspecified.**  
   In **Assumption 2.4** on **Page 6**, item 2 is labeled “\(W^{1,\infty}\) Error” but is written as
   \[
   \sup_r \|\hat u(r,\cdot)\|_{W^{1,\infty}} \le C_{F,2} e(\hat u),
   \]
   which cannot be an error bound on the surrogate itself unless \(e(\hat u)\) is large enough to dominate the whole function norm. The appendix version seems to intend a bound on the true defect instead. This matters because **Theorem 2.5** relies on these assumptions in a central way. If the main assumption is misstated, then the interpretation of the theorem in the main paper is shaky.  
   More broadly, **Theorem 2.5** on **Pages 6-7** presents
   \[
   \sup_{(t,\mathbf x)} \|\tilde{\mathbf U}_{N,M}(t,\mathbf x)-\bar{\mathbf u}(t,\mathbf x)\|_{L^2}
   \le E(M,N)\cdot (C_F e(\hat u)),
   \]
   but the main paper does not define \(E(M,N)\) beyond “the error term of the underlying MLP solver,” nor does it state the exact dependence on \(N\), \(M\), or any regularity/integrability parameters needed for the result. I am fine with delegating full proofs to the appendix, but the main theorem should still be stated in a way that is self-contained enough for a reader to understand what is being guaranteed.

4. **The “faster convergence” and “same total budget” argument is oversimplified, and the cost accounting is not convincing as written.**  
   The heuristic on **Page 4** argues that if the surrogate has error \(m^{-\gamma}\) and one averages over \(m\) Monte Carlo paths, the final error becomes \(m^{-\gamma-1/2}\), for a total budget of \(2m\) function evaluations. This is rhetorically appealing, but it sweeps several things under the rug: training a surrogate is not comparable to one MLP function evaluation, the correction step uses recursive MLP with nontrivial branching and gradient/path estimation, and the actual wall-clock times in **Table 1** show SCaSML is often much slower than the surrogate alone. For example, on the LQG 160d row in **Table 1**, the surrogate takes 0.34s while SCaSML takes 29.95s, which is about two orders of magnitude larger.  
   That does not invalidate the method, but it weakens the “elastic compute” narrative in the main text. The paper should be more explicit that the scaling law is an asymptotic stylized argument under specific complexity assumptions, not a direct statement about real end-to-end runtime parity.

5. **The empirical section demonstrates improvement over the chosen baselines, but the baseline set is narrower than the claims about broad utility would warrant.**  
   The paper compares against the base surrogate and naive MLP, which is the obvious comparison for validating the correction idea, but that is also a relatively favorable setup. There is no comparison to other modern high-dimensional PDE solvers beyond PINN/GP and MLP, nor to residual-correction style alternatives. This matters because the headline claim is not just “we improve our own base models,” it is that the proposed inference-time scaling framework is a practically meaningful way to solve high-dimensional PDEs. Without stronger baselines, that claim remains somewhat under-supported.  
   Relatedly, the paper positions itself against classical defect correction and iterative correction, but the experimental section does not compare to any competing correction mechanism. So the empirical evidence is strong for “SCaSML helps over the base surrogate,” but weaker for “SCaSML is the right correction mechanism.”

6. **Several experimental design choices look important but are not sufficiently analyzed, especially clipping/thresholding and estimator substitutions.**  
   The method repeatedly uses clipping thresholds, and these thresholds vary dramatically by problem and method, e.g. **Page 8** uses threshold 10 for naive MLP and 0.1 for SCaSML in LQG, and **Page 8** also uses 1.0 vs 0.01 for Burgers with PINN/GP. That may be perfectly reasonable because the defect is smaller in magnitude than the full solution, but it is also a strong stabilization intervention. The problem is that the paper does not analyze sensitivity to these thresholds in the main text. If SCaSML’s advantage depends materially on aggressive clipping, readers should know that.  
   A similar point applies to the use of Hutchinson estimators for Laplacians in the HJB experiments on **Pages 8-9**. This is a meaningful approximation choice, yet its effect on accuracy and variance is not quantified in the main paper.

7. **Some figures support the paper’s claims, but they also expose limitations that the text glosses over.**  
   **Figure 3(b)** on **Page 9** is used to argue inference-time scaling, and in general the curves do go down. But the improvements are not uniformly dramatic across all listed systems, especially for the diffusion-reaction case where the gain is visibly modest. Likewise, the text around **Figure 4** on **Page 10** claims empirical verification of the improved scaling law, but the figure shows a few log-log trend lines on a single benchmark family rather than a robust validation across the broader suite. This is not fatal, but the paper’s tone sometimes overstates how comprehensively the scaling law has been validated.

8. **Presentation quality is dragged down by a large number of typos, malformed references, and bibliographic issues, some of which are distracting enough to affect confidence.**  
   Examples include “Scisurrogate,” “SCiML,” “Metathetical Science,” and multiple malformed equations and symbol switches in the main text. More seriously, the reference list on **Page 12** contains repeated obviously corrupted entries (“H. Hu, X. Hu, and Y. Li. A flow model for the flow model.” repeated many times). This does not by itself invalidate the contribution, but it gives the paper a rough and insufficiently proofread feel. For a theory-heavy paper, that matters because readers need confidence that the equations and assumptions are being stated carefully.

## Questions
1. The main paper appears to contain at least two central equation errors, specifically the terminal condition in **Equation (4)** and the time derivative term in **Equation (7)**. Please explicitly restate the correct defect PDE in the rebuttal, with fully consistent notation for the surrogate, defect, modified nonlinearity, and terminal condition. This would materially increase my confidence.

2. In **Assumption 2.4** on **Page 6**, did you intend to bound the surrogate norm, or the defect norm \(u-\hat u\)? As written, item 2 does not read like an approximation-error assumption. Please clarify the exact assumption used by **Theorem 2.5** and whether the theorem statement in the main paper should be corrected.

3. How sensitive are the results to the clipping thresholds used in SCaSML and naive MLP? A small ablation, especially for the LQG and Burgers settings, would be valuable because the thresholds differ by orders of magnitude between methods.

4. Can you provide a clearer end-to-end cost accounting for the “improved scaling law” claim? I do not mean the asymptotic theorem alone, I mean a practical statement connecting training cost, inference correction cost, and final error under a fixed wall-clock budget in the main paper. The appendix seems to move in this direction, but the main text currently presents a cleaner story than the runtime numbers in **Table 1** support.

5. The comparison in **Table 1** is convincing for improvements over the base surrogate, but could you comment on how SCaSML compares to stronger alternative high-dimensional PDE solvers or residual-correction baselines, not just surrogate-plus-naive-MLP? Even a discussion of why such baselines were omitted would help with positioning.

6. For **Figure 4** on **Page 10**, can you report the fitted slopes with confidence intervals and explain precisely how training and inference budgets were coupled when estimating the empirical convergence rates? Right now the figure is suggestive, but I would like a tighter connection to the theorem.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the submission. The work focuses on numerical methods for PDE solving and does not involve sensitive human data, deployment on vulnerable populations, or directly harmful applications in the paper as written.

## Soundness Rating
2: fair. The central idea is plausible and supported by useful experiments, but the main paper contains multiple equation/notation errors and some underspecified assumptions that reduce confidence in the precise technical claims as presented.

## Presentation Rating
2: fair. The paper has a good high-level narrative and some effective figures, but the exposition is undermined by inconsistent notation, malformed equations, and reference-list issues.

## Contribution Rating
3: good. Despite the technical sloppiness in presentation, the inference-time defect-correction framing for learned PDE surrogates is interesting and potentially useful to the community.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected.  
My view is that the paper has a real idea and nontrivial empirical support, especially the consistent improvements in **Table 1** and the failure-recovery story visible for hard cases like LQG. However, the main-paper mathematical presentation is rougher than it should be, with central equations appearing misstated. I end up slightly on the positive side because I think the underlying contribution is meaningful, but this is not a comfortable accept.

## Reviewer Confidence
4: confident. I am confident in the main assessment and checked the core equations and experimental claims carefully, though some low-level proof details reside in the appendix and I have not independently re-derived every bound end to end.
---
job_id: a53d4a98-3921-4a4b-b9e6-8cdf75f0f876
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: FEqZmGl36g.pdf
paper: ESS-Flow: Training-Free Guidance of Flow-Based Models as Inference in Source Space
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, combining generative models, Bayesian inference, MCMC sampling, and applications to scientific machine learning.

## Minimum Quality
Pass ✅. The submission contains the expected scientific components, including abstract, introduction, related work, method, experiments with quantitative and qualitative results, and conclusion; while I have substantive concerns about rigor and validation, they do not rise to the level of desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden instructions, prompt-injection attempts, or suspicious manipulative text in the provided paper content.

# Expected Review Outcome:
## Summary
This paper proposes ESS-Flow, a training-free controlled generation method for flow-based generative models that performs Bayesian inference in the Gaussian source space using elliptical slice sampling. The key idea is that after changing variables from data space to source space, the target density becomes proportional to $g(T_\theta(z))p(z)$, which removes the Jacobian term and enables gradient-free sampling. The method is evaluated on materials design and protein structure prediction, and the paper also includes a simple multi-fidelity variant based on importance reweighting across ODE discretizations.

## Strengths
The paper has a clear and appealing core idea. The change-of-variables argument in **Equation (3), Page 4** is simple but useful: once the target is rewritten in source space, the Jacobian cancels and the problem becomes exactly the kind of Gaussian-prior inference problem for which elliptical slice sampling is a natural fit. That gives the method a clean identity, and it directly explains why ESS-Flow avoids gradient and Jacobian computations.

The method is well motivated for settings where gradients are unavailable or unreliable. The materials design setup in **Section 5.1, Pages 6 to 7** is a good match to that pitch, especially because the paper includes a genuinely non-differentiable target in the space-group experiment. This is one of the stronger parts of the paper, since the method is not merely positioned as “another sampler,” but as a practically useful one when discrete operations or external simulators break backpropagation.

I also appreciated the visual exposition. **Figure 1, Page 2** gives an intuitive picture of why exploring ellipses in source space can map to nontrivial, connected traversals in data space. **Figure 2, Page 4** is similarly effective at conveying the conceptual distinction from source-space gradient following, and it helps the reader understand the authors’ claim that gradient-based source updates can get trapped on disconnected manifold components. These figures do real explanatory work rather than serving as decorative cartoons.

On the empirical side, the materials results are strong on their own terms. In **Table 2, Page 7**, ESS-Flow is substantially better than the listed baselines on all four reported property-targeting tasks, often by a very large margin. The distributional plots in **Figure 3, Page 8** are also supportive, showing ESS-Flow samples concentrated much closer to the target values than D-Flow, PnP-Flow, or DAPS. Even if one can debate baseline fairness, the reported gap is large enough that the method is clearly doing something nontrivial.

The paper is also reasonably candid about a real limitation: when the prior does not place enough mass near the target, gradient-free source-space MCMC may mix poorly. I appreciated that this is stated in the introduction and conclusion instead of being buried.

## Weaknesses
1. **The methodological novelty is somewhat narrower than the paper’s framing suggests, and the positioning relative to closely related latent/source-space MCMC work is not yet sharp enough.**  
   The core construction is: map the conditional generation problem to the Gaussian source space, then apply ESS there. That is sensible, but at a high level it is also a fairly direct instantiation of an existing MCMC method after a straightforward pullback of the target density. The paper does discuss source-space Langevin and HMC methods in **Section 3, Page 3**, but the novelty claim would be stronger if it more explicitly disentangled what is actually new here: not “Bayesian inference in source space” per se, but specifically the use of ESS to exploit the Gaussian source prior without gradients. Relatedly, there is an important methodological connection to prior work combining transport maps / normalizing flows with elliptical slice sampling that is not discussed, and this weakens the literature positioning. As written, the related-work section feels a bit too convenient: it contrasts mostly against gradient-based guidance and source-space optimization, but does not fully engage with neighboring Monte Carlo literature that is structurally very close to the proposed approach.

2. **The paper’s main claim of being an “asymptotically exact sampling method” is under-supported experimentally because there are almost no MCMC diagnostics in the main paper.**  
   This matters a lot. If the selling point is asymptotic correctness rather than merely a good heuristic, then I expect to see evidence about mixing, convergence, autocorrelation, initialization sensitivity, or at least effective sample size and between-chain agreement. Instead, the main paper mostly reports downstream sample quality metrics. That is not enough to evaluate whether ESS-Flow is actually sampling from the intended posterior in the finite-budget regimes used in practice. The problem is especially visible in the protein experiment, where only 10 samples are generated for one inverse problem instance, see **Section 5.2 and Table 4, Page 9**. Without trace plots, chain diagnostics, or sensitivity to burn-in / number of MCMC steps, it is hard to know whether the method is genuinely approximating the posterior or just producing plausible local samples. The appendix contains some efficiency information, but the main claims in the paper need stronger support in the main paper itself.

3. **There is a nontrivial mismatch between the theoretical assumptions in Section 4 and the actual experiments, especially for discontinuous or zero-valued potentials.**  
   This is the most important technical issue for me. In **Page 5**, the discussion around ESS relies on continuity of the pullback potential $g \circ T_\theta$ and cites convergence results under regularity assumptions. However, the paper’s own flagship “non-differentiable” example in **Table 1, Page 6** uses a binary indicator potential for space group, $g(c)=\mathbf{1}[P_c=y]$. That potential is discontinuous, takes the value zero on large regions, and does not match the positivity assumptions implicitly used in **Algorithm 1, Page 5**, where the acceptance check is written in terms of $\log g(x') > \log g(x)+\log u$. For $g(x')=0$, this becomes $\log 0$, which is not discussed. More importantly, the continuity-based termination and convergence discussion on **Page 5** no longer directly applies. The paper cannot both lean on continuity-based ESS theory and then showcase a discontinuous indicator potential without clearly explaining what theoretical guarantees survive and what becomes heuristic. This is not a nitpick, because the whole paper is explicitly motivated by non-differentiable settings.

4. **The multi-fidelity extension is currently too weak and too unstable to count as a convincing contribution.**  
   In **Equation (4), Page 6**, the authors propose self-normalized importance weighting from a coarse target $\pi^\Delta$ to a fine target $\pi^\delta$. As a proof of concept that is fine, but the surrounding text overstates its utility. The method is explicitly shown to break down for sharper targets: in **Section 5.1.1, Page 7**, the effective sample size drops to $0.1\%$ for band gap and $1.0\%$ for stability. The appendix then confirms a severe degradation in sample quality after reweighting, especially in **Table 10, Page 16**, where the reweighted band-gap results nearly collapse. This is not a minor caveat, since the computational burden of ESS-Flow is one of the paper’s major practical issues, and the proposed remedy does not yet solve it in difficult regimes. Also, **Equation (4)** quietly assumes that $g(T_\theta^\Delta(z))$ is nonzero wherever $g(T_\theta^\delta(z))$ matters, otherwise the importance ratio is undefined or explosive. That support issue is not discussed.

5. **The empirical comparison is not yet broad or fair enough to establish the method’s general advantage.**  
   The materials experiment favors ESS-Flow in a way that is understandable but still important to acknowledge. In **Section 5.1, Pages 6 to 7**, D-Flow and PnP-Flow are forced to use a soft approximation for discrete atomic-number embeddings via **Equation (5), Page 7**, while ESS-Flow can operate directly on the rounded / discrete outputs. That is precisely the intended use case of the paper, so I do not object to the setup itself. But it does mean that **Table 2, Page 7** is not purely comparing inference quality, it is also comparing methods under asymmetric compatibility with the observation model. In that setting, the very large performance gap may partly reflect a baseline handicap rather than a uniformly better posterior sampler. The paper should say this more explicitly, and it should include at least one stronger comparison in a fully differentiable setting where gradient-based source-space samplers are not structurally disadvantaged.  
   A related issue is that the protein experiment is only a single protein instance with 10 samples per method, which is far too small to support broad claims. A single underdetermined inverse problem can be a case study, but not a robust benchmark.

6. **The protein results are more mixed than the narrative suggests, and the qualitative presentation is somewhat selective.**  
   In **Table 4, Page 9**, ESS-Flow does improve ELBO relative to ADP-3D and DAPS, which supports the “more realistic samples” claim to some extent. However, ESS-Flow is still worse than unconditional and D-Flow in clash count, with **24.8** clashes versus **10.1** for unconditional and **14.8** for D-Flow. Its observation fit $d_y$ is also much worse than ADP-3D and DAPS. So the trade-off is not simply “ESS-Flow is realistic while others are unrealistic”; it is “ESS-Flow is less pathological than some baselines but still far from clean.” The qualitative panel in **Figure 4, Page 10** uses the lowest-$\mathrm{RMSD}_{\mathrm{gt}}$ sample from each method, which is effectively a best-case presentation. That is okay as illustration, but it is not sufficient evidence for the broader realism claim. This experiment reads more like an interesting anecdote than a decisive validation.

7. **The paper underplays the computational cost of the method in the main narrative.**  
   ESS-Flow avoids gradients, but it is not cheap. The appendix shows this very clearly: **Table 7, Page 14** reports substantially larger numbers of transport-map evaluations for ESS-Flow than for the baselines, especially on sharper targets. This is a central practical trade-off, yet the main paper’s experimental discussion focuses mostly on accuracy and realism while giving little quantitative runtime analysis in the main text. The method may still be worthwhile when gradients are impossible, but readers deserve a more transparent main-paper discussion of where the cost is acceptable and where it is not. Otherwise the paper risks sounding more generally practical than the data support.

8. **Some of the strongest tables actually reveal a more nuanced story than the authors discuss.**  
   For example, **Table 3, Page 9** shows that ESS-Flow often has much lower uniqueness/novelty than some baselines on targeted materials tasks, even while having the best target-hit rate. For bulk modulus, its U.N. is much lower than DAPS, and for shear modulus the drop is even sharper. This suggests a concentration or diversity trade-off that is scientifically interesting and operationally important. But the discussion mostly emphasizes the best S.U.N.T. numbers, without really unpacking what is being sacrificed to get there. Likewise, **Figure 3, Page 8** indeed shows ESS-Flow distributions concentrated near the target, but it also visually suggests narrower support than the baselines, which is entirely consistent with the lower uniqueness results. This should be discussed rather than glossed over.

9. **The theoretical presentation around Proposition 1 is too compressed to do much scientific work in the paper.**  
   In **Page 5**, Proposition 1 is imported from Natarovskii et al. with only a sketch of assumptions. The notation is also a bit sloppy: the chain is denoted by $\nu(\cdot, x)$, while the bound is indexed by $z$, and the target $\pi$ is not consistently distinguished between source-space and data-space versions in the surrounding discussion. I am not claiming the proposition is false, but in the current form it reads more like a citation placeholder than a meaningful theoretical contribution. Since the paper leans on asymptotic exactness, the notation and assumptions should be much cleaner.

## Questions
1. **How exactly should Algorithm 1 be interpreted when $g(x)=0$ or when $g$ is discontinuous?**  
   This is crucial for the space-group experiment in **Table 1, Page 6**, and more generally for the paper’s non-differentiable use case. Please clarify whether the implementation treats $\log 0=-\infty$, whether ESS still terminates almost surely in that setting, and which parts of the convergence discussion on **Page 5** still apply.

2. **Can the authors provide proper MCMC diagnostics for the main experiments?**  
   What I would find most useful are: multiple-chain results, autocorrelation or ESS-per-chain diagnostics, sensitivity to burn-in and total MCMC steps, and perhaps posterior summaries across independent runs. This would substantially increase my confidence that ESS-Flow is functioning as an actual sampler rather than a plausible search heuristic.

3. **Can the authors better separate “advantage due to gradient-free inference” from “advantage due to baseline incompatibility with discrete outputs”?**  
   In the materials setup, the baselines seem handicapped by the soft relaxation in **Equation (5), Page 7**. A stronger rebuttal would either include a more favorable differentiable benchmark for those methods or explicitly analyze how much of the gap in **Table 2** is driven by that relaxation.

4. **What is the practical wall-clock/runtime trade-off in the main experiments?**  
   The appendix suggests a substantial cost increase for ESS-Flow. If the authors can summarize runtime in the rebuttal, ideally per task and per sample, that would help calibrate the practical value of the method.

5. **Can the authors strengthen the empirical case beyond one protein inverse problem?**  
   Even a small additional set of proteins, or repeated random subsets of distance observations for the same protein, would make the conclusions in **Section 5.2** much more convincing.

6. **Please clarify the scope of the “asymptotically exact” claim.**  
   Is the claim intended only for continuous positive potentials and an exact transport map, or also for the discretized ODE solver and discontinuous potentials used in practice? A precise statement here would improve the paper significantly.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics issues are evident from the paper. The applications are in materials design and protein structure prediction, and the manuscript does not raise immediate concerns regarding human subjects, privacy, or harmful deployment beyond standard dual-use considerations already common in generative modeling.

## Soundness Rating
2: fair. The main idea is technically reasonable, but important parts of the empirical validation and some theory-to-experiment connections are not sufficiently supported, especially for discontinuous potentials and actual MCMC behavior.

## Presentation Rating
3: good. The paper is generally readable and the main intuition is communicated well, especially through **Figures 1, 2, and 3**, but several technical claims and assumptions need sharper exposition.

## Contribution Rating
2: fair. The source-space ESS formulation is a useful idea and likely worth sharing, but the contribution feels narrower than the framing suggests, and the empirical evidence is not yet broad enough to establish a strong contribution at ICLR level.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper has a clean core idea and some promising results, especially in discrete/non-differentiable scientific settings, but the current version leaves too many open questions about theoretical scope, MCMC validity in practice, fairness/breadth of comparisons, and computational practicality.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. The paper is in an area I know well, and I checked the main equations, algorithmic claims, figures, and tables carefully.
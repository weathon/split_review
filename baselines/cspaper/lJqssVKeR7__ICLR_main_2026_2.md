---
job_id: 8b9f28a4-fa98-456d-a03c-5e0b031aa167
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: lJqssVKeR7.pdf
paper: Converge Faster, Talk Less: Hessian-Informed Federated Zeroth-Order Optimization
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies optimization and federated learning for LLM fine-tuning, with both algorithmic and theoretical contributions in non-convex zeroth-order optimization.

## Minimum Quality
Pass ✅. The submission contains the expected research components, including abstract, introduction, related work, method, theory, experiments, results, and discussion/limitations, and it presents a coherent scientific contribution despite several technical and presentation issues that should be addressed in review rather than desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompt, reviewer-targeting instruction, or suspicious manipulative text in the provided paper content.

# Expected Review Outcome:
## Summary
This paper studies federated zeroth-order optimization under scalar-only, dimension-free communication, motivated by LLM fine-tuning where transmitting full gradients or model updates is prohibitively expensive. The authors propose HiSo, a Hessian-informed variant that uses a global diagonal preconditioner reconstructed locally from scalar information, and they provide a convergence analysis under additional Hessian approximation assumptions together with experiments on several FL fine-tuning benchmarks.

## Strengths
The paper tackles a real tension in federated LLM fine-tuning, namely how to improve the poor convergence behavior of scalar-only ZO methods without giving up the very communication property that makes them attractive in the first place. That is a meaningful problem, and the proposed direction is reasonable.

I found the main algorithmic idea interesting: use a shared preconditioned perturbation distribution, $z \sim \mathcal{N}(0, H_r^{-1})$, so that the update still has a scalar-plus-seed representation while incorporating curvature through a diagonal $H_r$. In spirit, this is a clean way to reconcile second-order information with the communication constraints inherited from DeComFL.

The paper also makes a useful systems-level observation in Section 3.3, namely that scalar-only communication is not inherently tied to vanilla ZO-SGD, but to whether the update can be reconstructed from scalars plus state. That broader framing is one of the better parts of the paper, because it potentially opens the door to more than just the particular HiSo instantiation.

The empirical section is stronger than many optimization papers in terms of scale. The authors evaluate on multiple OPT sizes and multiple tasks, and the communication numbers in **Table 2** are easy to read and practically relevant. In particular, the speedups over DeComFL on SQuAD are substantial, for example 1350 to 250 rounds on OPT-350M and 350 to 175 rounds on OPT-1.3B. Even if one can debate the exact fairness of the metric, the trend suggests the method is doing something materially useful.

**Table 3** also makes the practical trade-off visible. The first-order FL baselines achieve higher accuracy in several settings, but at vastly larger communication cost, while HiSo usually improves over the ZO baselines in both communication and final performance. For an ICLR audience, that communication-accuracy trade-off is worth seeing.

The visualizations are helpful overall. **Figure 3** gives a reasonably intuitive picture of how the server/client reconstruction loop works with the Hessian-informed perturbations, which is important because the scalar-only protocol is not trivial to parse from equations alone. I also found **Figure 2** useful as a conceptual illustration of the reset-and-reconstruct mechanism across rounds.

Finally, the theory is ambitious. Extending the analysis beyond the original DeComFL setting, especially to the $\tau > 1$ local-update case, is a worthwhile theoretical target. Even though I have reservations about some assumptions and derivation details, the paper is at least trying to say something nontrivial about why curvature-aware ZO-FL might escape the usual pessimistic $O(d)$ intuition.

## Weaknesses
1. **The headline theoretical claim depends on a strong and weakly justified approximation assumption, and the paper somewhat overstates what is actually proved.**  
   The abstract and introduction emphasize a convergence rate “independent of model dimension $d$ and Lipschitz constant $L$,” but in the main text this only appears in **Corollary 1** and **Corollary 3**, and only after assuming the learned diagonal matrix satisfies the “well-approximated condition” in **Equation (17)**. That condition is doing a lot of work. The quantity
   $$
   \operatorname{Tr}\!\left(H^{-1/2}\Sigma H^{-1/2}\right)\le \zeta
   $$
   with $\zeta$ independent of $d$ is essentially the desired conclusion encoded as an assumption. The “safety factor 2” in **Equation (17)** is also introduced heuristically. This matters because the strongest theoretical takeaway of the paper is not a general guarantee for the actual algorithm as implemented, but a conditional statement under a fairly favorable whitening assumption that is not verified in the main paper.

   The empirical support for this assumption in the main paper is also not very convincing. In **Figure 5** right, the authors show a long-tail distribution of learned diagonal entries of $H$, but a long-tail histogram of $H$ itself does not establish that $H$ whitens the local Hessian in the sense required by **Equations (16)-(17)**. Likewise, **Figure 4** is a synthetic simulation of eigenvalues, not evidence from the actual LLM training setting used in Tables 2 and 3. So the theory may be suggestive, but the paper should be more careful not to present the dimension/Lipschitz independence as though it were robustly established for the practical method.

2. **There is a notable derivational issue around the transition from the least-squares formulation to the implemented estimator.**  
   In **Equations (5)-(7)**, the optimal scalar for the constrained least-squares problem is
   $$
   g^o=(u_{r,k}^{\top}H_r^{-1}u_{r,k})^{-1}u_{r,k}^{\top}H_r^{-1/2}\nabla f_i(x_{r,k}^{(i)}).
   $$
   The paper then says that $(u^\top H^{-1}u)^{-1}$ is “a scalar that is independent of iterates” and therefore can be absorbed into the learning rate. This is not a harmless simplification. It is indeed independent of the iterate $x$, but it is **not** a fixed scalar, it depends on the sampled direction $u$, hence it varies from step to step. Replacing a random normalization factor by a constant learning-rate absorption changes the estimator. This is not a cosmetic issue, because **Equation (8)** is then presented as if it were the direct solution-derived update. At minimum, the paper needs to clarify whether this is a heuristic approximation, an unbiased-in-expectation substitution, or a deliberate redesign. Right now, the derivation reads as if the algorithm follows directly from the optimization problem, which is not accurate.

3. **The mathematical exposition contains several inconsistencies that make the proof chain harder to trust than it should be.**  
   I encountered multiple notation/indexing problems in the main paper and appendix:
   - In **Equation (12)**, the Hessian recursion uses $S_r$ and $m$, whereas the rest of the paper uses $C_r$ for sampled clients. It also writes $H_{r+1}=H_{r,\tau}=(1-\nu)H_{r,\tau-1}+\cdots$, but only $H_{r,1}$ is explicitly shown right below, making the intended within-round indexing unclear.
   - In **Equation (32)**, the two displayed cases are written identically, even though the preceding discussion distinguishes local-update iterations from communication iterations. That looks like a real typo in a central recursion.
   - In the “Communication Iteration” paragraph in **Section F.4**, the text says “when the iteration $k$ is the communication iteration, i.e. $k \neq r\tau$,” which is the opposite of what it should say.
   - In Appendix D, **Algorithm 2a line 6** updates with $\Delta x_{t,\tau}$ although the loop variable is $k$, and **Algorithm 2b line 4** uses $f_i(x_{i,r}^{(i)})$, which appears to be a typo for $f_i(x_{r,k}^{(i)})$ or similar.

   Any one of these could be a typo. In aggregate, they matter because this paper leans heavily on a nontrivial proof story, and several errors appear exactly in the equations and algorithm blocks one would need to verify carefully.

4. **The Hessian-learning mechanism is much closer to an Adam-style second-moment accumulator than to an actual Hessian estimator, so some of the language in Section 4.2 is too strong.**  
   The update in **Equation (12)** uses $\mathrm{Diag}([\Delta x]^2+\epsilon I)$, where $\Delta x$ is itself a preconditioned ZO update direction. That is not estimating diagonal Hessian entries in any direct sense; it is accumulating squared update magnitudes. The paper acknowledges the Adam analogy, but the surrounding text repeatedly says it is “learning global curvature” and “approximating the diagonal Hessian.” That interpretation may be partially defensible empirically, but it is not cleanly justified mathematically. The difference matters because the paper’s conceptual contribution is precisely about Hessian information. If the practical update is really an adaptive second-moment preconditioner reconstructed under the scalar-only protocol, then that is still useful, but it should be described more precisely.

   Relatedly, the paper would be much stronger if it included a baseline that uses the **same scalar-only framework** with a generic adaptive diagonal accumulator but without the Hessian interpretation. As written, the gains are mostly attributed to curvature, but there is no ablation separating “Hessian-informed perturbation distribution” from “any adaptive rescaling scheme that changes search anisotropy.”

5. **The experimental comparison protocol is not always fair or at least not presented in a symmetric way.**  
   The acceleration claim in **Table 2** compares DeComFL at “full convergence” against HiSo at the round where it first matches DeComFL’s best accuracy. That is a favorable direction for HiSo, but not a symmetric comparison. It would be more convincing to report, for both methods: (i) rounds to their own convergence, (ii) area-under-curve or time-to-threshold at several thresholds, and (iii) final best accuracy under a fixed round budget. As presented, **Table 2** is useful but somewhat tailored to highlight speedup.

   There is also a tension between the text and **Table 3**. The paper says HiSo maintains the lowest communication cost in almost all tasks, “only a little higher than DeComFL on OPT-1.3B+QQP,” but the numbers are 96.67 KB for HiSo versus 43.95 KB for DeComFL, which is not “a little higher,” it is more than 2x. That does not invalidate the method, but it weakens the rhetoric and suggests the discussion should be more careful.

6. **The paper’s empirical support for the claimed Hessian mechanism is still thinner than it should be.**  
   The main-paper ablation is mostly **Figure 5** left, which varies $\nu$ and shows limited sensitivity near high values. That is useful, but it does not really establish that the performance gain comes from better Hessian approximation rather than just a benign smoothing effect. **Figure 5** right is a histogram of learned entries, which is descriptive but indirect. The core scientific claim is that Hessian information accelerates federated ZO optimization under scalar-only communication. For that claim, I would have liked at least one stronger main-paper analysis tying the quality of $H$ to performance, not just a convergence comparison against DeComFL.

   The appendix appears to contain more evidence, but by the rules of main-paper evaluation, the paper should stand more firmly on its own. Right now the empirical story is “HiSo works better,” which is good, but the mechanistic claim “HiSo works better because the learned diagonal object is meaningfully capturing Hessian structure” is less solid in the main text.

## Questions
1. The most important clarification for me is the derivation from **Equation (7)** to **Equation (8)**. Since $(u^\top H^{-1}u)^{-1}$ depends on the sampled direction, on what basis can it be absorbed into the learning rate? Is the implemented update intended as an approximation to the least-squares-optimal scalar, or is there a more precise argument that the random normalization can be dropped without changing the estimator in expectation?

2. Can the authors clarify the exact Hessian update indexing in **Equation (12)** and align it with the algorithm statements? In particular, is $H$ updated once per round, once per local step, or both conceptually and implementation-wise? The notation around $H_{r,\tau}$, $H_{r,1}$, and the use of $S_r/C_r$ is currently confusing.

3. A stronger experimental rebuttal would be to include a scalar-only adaptive baseline that uses the same communication protocol but a non-Hessian diagonal preconditioner. If such a baseline is available, it would help isolate whether the gains come specifically from Hessian-informed perturbations versus generic adaptive scaling.

4. For **Table 2**, could the authors provide a symmetric evaluation protocol, for example reporting rounds to a common externally fixed threshold, or reporting both methods’ own convergence rounds and final best performance under equal communication budgets? That would make the acceleration claim easier to interpret.

5. The paper’s strongest theoretical statement depends on **Equation (17)**. Is there a more direct main-paper diagnostic, on actual LLM runs, for the quantities entering
   $$
   \operatorname{Tr}(H_r^{-1/2}\Sigma_{r,k}H_r^{-1/2}) \quad \text{or} \quad \bar{\rho},
   $$
   even if only in a random subspace or proxy form? That would substantially increase my confidence that the theory is not merely post hoc intuition.

6. Please double-check the proof and algorithm notation around **Equation (32)**, the communication-iteration condition in **Section F.4**, and the appendix algorithm lines noted above. If these are only typographical, it would help to state that explicitly and provide corrected expressions.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are evident from the paper itself. The work studies communication-efficient federated optimization and does not introduce an obvious new privacy, safety, or fairness risk beyond standard FL deployment considerations.

## Soundness Rating
3: good. The core idea is plausible and supported by reasonably broad experiments, but several derivational shortcuts, notation inconsistencies, and strong theory assumptions reduce my confidence in the sharpest technical claims.

## Presentation Rating
2: fair. The overall structure is understandable, and some figures help, but the paper has too many notation errors, indexing inconsistencies, and places where the exposition over-claims relative to what is actually proved.

## Contribution Rating
3: good. The paper addresses an important problem and presents a meaningful algorithmic combination of scalar-only ZO-FL with curvature-aware preconditioning, though the empirical isolation of the mechanism and the precision of the theoretical story are not yet at the level of a clearly stronger accept.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The problem is important, the method is interesting, and the empirical results are promising enough that I lean positive, but the paper needs tighter math, more careful wording around its theory, and a cleaner experimental isolation of what exactly the Hessian component is buying.

## Reviewer Confidence
4: confident. I am confident in my assessment, though not absolutely certain. The paper is in an area I know well, and I checked the main derivations and experimental claims with reasonable care, but I did not fully verify every appendix proof line by line.
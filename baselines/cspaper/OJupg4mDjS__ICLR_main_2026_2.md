---
job_id: ad0e823e-4d2d-47c2-8d29-825fee7f91bf
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: OJupg4mDjS.pdf
paper: On the Wasserstein Geodesic Principal Component Analysis of Probability Measures
main_score_norm: 0.8
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, at the intersection of optimal transport, geometric/statistical learning on non-Euclidean spaces, and representation/metric learning for probability measures.

## Minimum Quality
Pass ✅. The submission contains the expected scientific components, including abstract, introduction with related work discussion, methodology for Gaussian and general a.c. measures, experiments with qualitative and some quantitative results, and a discussion section; it is written in clear scientific English and I did not find any immediate fatal flaw that would justify desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not detect hidden prompts, manipulative instructions, or suspicious text aimed at influencing automated or LLM-based reviewing.

# Expected Review Outcome:
## Summary
This paper studies exact Geodesic PCA in Wasserstein space, first for centered Gaussian measures under the Bures-Wasserstein geometry, and then for general absolutely continuous probability measures using Otto’s geometric formulation. For Gaussians, the authors lift GPCA to the space of invertible matrices and optimize over horizontal line segments; for general measures, they introduce a neural parameterization of Wasserstein geodesics based on $(\varphi, f)$ with $\mu(t) = (\mathrm{id}+t\nabla f)_{\#}(\varphi_{\#}\rho)$. The paper also compares GPCA against tangent PCA and provides illustrative experiments on synthetic data, 3D point clouds, image color distributions, and MNIST-derived distributions.

## Strengths
1. **The Gaussian part is technically strong and well motivated.**  
   Section 3 gives a clean formulation of exact GPCA for centered Gaussian distributions by lifting the problem from $S_d^{++}$ to $GL_d$. Proposition 3, together with equations (11) and (12), is a meaningful reformulation because it turns projection onto geodesics in the curved space into projection onto line segments in the flat lifted space, while explicitly handling the fiber ambiguity through the $Q_i \in SO_d$. This is not just a cosmetic rewrite, it gives a usable optimization problem for exact GPCA rather than a tangent approximation.

2. **The geometry is explained unusually well for a paper of this type.**  
   The progression from equations (4)-(7) and Proposition 1 on the Gaussian side, to equations (8)-(10) and Proposition 2 on the general Wasserstein side, is coherent and easy to follow. In particular, **Figure 1** is genuinely helpful rather than decorative: it clarifies the top-space / bottom-space viewpoint and visually explains why horizontal Euclidean motions upstairs correspond to Wasserstein geodesics downstairs. Likewise, **Figure 2** makes the orthogonal-intersection constraint for higher components much easier to parse than the text alone.

3. **The paper gives a concrete exact-vs-linearized comparison, not just rhetoric.**  
   A lot of papers say “tangent approximations distort geometry” and stop there. Here the authors actually quantify that distortion in the Gaussian setting, via Proposition 4 and equation (14). That makes the comparison sharper and more scientifically useful than a purely qualitative “our method is more geometric” claim.

4. **The Gaussian experiments are insightful rather than merely confirmatory.**  
   The examples in Section 5.1 are simple but effective. **Figure 3** supports the claim that when the relevant subspace has zero curvature, GPCA and TPCA coincide. More importantly, **Figure 4** is one of the stronger parts of the paper: the left and middle panels visually demonstrate that the first GPCA component can differ substantially from TPCA and need not pass through the barycenter, while the right panel quantifies the improvement of GPCA over TPCA as the ratio $|a-b|/|a+b|$ increases. This figure does real argumentative work.

5. **The extension to general a.c. measures is creative and potentially impactful.**  
   The parameterization in Section 4 is appealing because it uses Otto’s horizontal formulation directly, rather than forcing the method through a log map or convex-potential architecture. The fact that the authors can define orthogonality via the $L^2(\rho)$ inner product on lifted horizontal fields is conceptually elegant and gives a principled way to define higher components.

6. **The paper is refreshingly honest about pathological behavior and limitations.**  
   In Section 5.1 and again in the discussion, the authors explicitly note that exact GPCA can behave worse than TPCA in some high-curvature Gaussian examples, with projections hitting geodesic boundaries. This kind of self-critique increases my trust in the paper.

7. **The qualitative experiments are reasonably convincing for mode discovery.**  
   In **Figure 5**, the recovered first and second components on the constructed MNIST geodesics align well with the intended shape-vs-color directions. In **Figure 6**, the first and second components on chairs, lamps, and landscape color distributions also show coherent transformations. These are not rigorous benchmarks, but they do support the claim that the learned components capture interpretable distributional variation.

8. **The appendix contains useful implementation and sensitivity details.**  
   Although my judgment is based on the main paper, it is good to see that **Table 1** clearly specifies the network architectures, optimizers, batch size, and number of gradient steps, and **Tables 2 and 3** provide some sensitivity analysis for $\lambda_O$ and $\lambda_I$. Those tables are particularly useful because they show the second component can collapse to the first when the orthogonality regularization is too weak.

## Weaknesses
1. **The central claim of solving the “exact GPCA problem” is much more convincing for Gaussians than for general a.c. measures.**  
   The paper repeatedly frames both parts as solving the exact GPCA problem, see the “Main contributions” on **Page 2** and the objective in equation (15) on **Page 6**. For the general a.c. case, however, the optimization is carried out with a neural parameterization of $(\varphi, f)$ and the **Sinkhorn divergence** $S_{\varepsilon}$ in place of $W_2^2$. This matters because exactness is then limited in at least two ways:  
   - the search is restricted to the expressivity and optimization landscape of the chosen MLPs,  
   - the minimized objective is not equation (1) or equation (15) exactly, but an entropically regularized surrogate.  
   I am not objecting to using a surrogate for tractability, but the wording should be more careful. As written, the paper risks overselling the general-case method. A more defensible statement would be that the method parameterizes true Wasserstein geodesics exactly, while optimizing an approximate empirical objective over a restricted function class.

2. **The mathematical conditions needed for the general geodesic parameterization are not fully enforced by the actual model class.**  
   In Section 4, the geodesic formula relies on $\varphi \in \mathrm{Diff}(\Omega)$ and on $\mathrm{id}+t\nabla f_\psi$ remaining a diffeomorphism over the relevant interval. But the implementation uses a standard MLP for $\varphi_\theta$, and the paper explicitly admits in Appendix E.1 that $\varphi$ is not enforced to be invertible. This is not a minor footnote; it directly affects whether $\mu_{\theta,\psi}(t)$ is guaranteed to be an Otto geodesic in the sense used to justify the method.  
   The main text on **Page 6** says the curve is a geodesic provided that $\mathrm{id}+t\nabla f_\psi \in \mathrm{Diff}(\Omega)$, and then proposes monitoring eigenvalues of $I_d + tH_{f_\psi}(x)$. But there is no analogous guarantee for $\varphi_\theta$, despite Proposition 2 and equation (9) relying on a diffeomorphic base map. The authors later argue that non-diffeomorphic $\varphi$ only leads to degenerate behavior in practice, but that is a heuristic, not a theorem. For a paper whose selling point is geometric exactness, this gap is important.

3. **The orthogonality and intersection constraints for higher components are only imposed softly, not exactly, in the general method.**  
   On **Pages 6-7**, the second component is learned by adding regularizers  
   \[
   \lambda_I \mathcal{I}(\cdot) + \lambda_O \mathcal{O}(\cdot)
   \]
   to the main loss. This is practical, but it weakens the claim that the second component is truly the GPCA component under orthogonal-intersection constraints. In the Gaussian part, the orthogonality constraint is built directly into the constrained problem in equation (13). In the neural part, by contrast, the geometry is only approximately enforced through penalties, and the resulting component depends on penalty strength and optimization dynamics.  
   The appendix sensitivity analysis is useful here: **Table 2** shows that for small $\lambda_O$, the “second” component collapses to the first, confirming that the constrained problem is not being solved intrinsically. This does not invalidate the method, but it does indicate that the method is better described as a regularized approximation to higher-order GPCA than as an exact solver.

4. **The empirical evaluation for the general a.c. case is mostly qualitative and too light to substantiate the stronger methodological claims.**  
   Section 5.2 offers nice visualizations, but there is little quantitative evidence that GPCAGEN is reliably recovering optimal or near-optimal geodesic components. On the synthetic MNIST-geodesic experiment, the paper says GPCAGEN “successfully recovers” the two designed geodesics, yet the evidence in **Figure 5** and **Figure 9** is visual only. There is no numerical recovery metric, such as error in projection times, alignment with the planted horizontal directions, geodesic residual relative to the ground-truth generating geodesics, or comparison of objective values.  
   Similarly, for chairs, lamps, and landscapes, **Figure 6** and **Figure 7** show plausible modes of variation, but interpretation-by-eye is not enough to support claims about solving GPCA. Even one concise quantitative table in the main paper, for example reporting objective values, stability across random seeds, or comparison against a discrete OT baseline on a common evaluation metric, would materially strengthen the paper. This is especially important because the method is expensive and optimization-heavy.

5. **The baseline discussion for general distributions is too weak, and the paper sidesteps direct comparison rather than confronting it.**  
   On **Page 9**, the paper states that a direct numerical comparison to TPCA is “not meaningful” because GPCAGEN learns continuous geodesics from empirical distributions whereas TPCA acts on discrete measures. I do not buy this as stated. Even if the parameterizations differ, the methods can still be compared on shared evaluation quantities, such as residual Wasserstein/Sinkhorn projection error on empirical samples, stability of recovered projection coordinates, or downstream separability after projection.  
   The paper instead pushes the TPCA comparison to the appendix and emphasizes visual artifacts in **Figure 16**. That is not sufficient, because visual artifacts do not establish that GPCAGEN is objectively better at the GPCA criterion. Given that TPCA is the main baseline throughout the motivation, the lack of a careful quantitative comparison in the main paper is a real omission.

6. **Some optimization details that matter for scientific evaluation are underjustified in the main paper.**  
   Algorithm 1 on **Page 6** updates one distribution at a time and estimates $t_{\min}, t_{\max}$ using Hessians evaluated on a minibatch. This leaves several practical questions unanswered in the main text: how noisy is this interval estimate, how often does clipping activate, how sensitive are learned components to this clipping, and does the optimization remain stable when the Hessian spectrum is poorly estimated? The appendix notes possible high-dimensional issues and mentions LOBPCG-style approaches, which is useful, but the main paper still presents the algorithm as fairly settled.  
   Relatedly, the regularization coefficients are said to work “as expected in all experiments” with $\lambda_I=\lambda_O=1.0$, but this robustness claim is only partially supported. **Tables 2 and 3** show some sensitivity, especially for $\lambda_O$, where the wrong regime leads to complete collapse of the second component. That is precisely the sort of brittleness the main paper should acknowledge more prominently.

7. **The scalability story is not very convincing for a method intended for general probability measures.**  
   The general method uses 120k gradient steps for the first component and 200k for the second, with batch size 1024 and Hessian-based checks, according to **Table 1**. The paper also states in Appendix E.2.3 that training time scales linearly with the number of measures and that higher-dimensional settings require more sophisticated eigenvalue tracking. These caveats are honest, but they substantially limit the practical reach of the method.  
   This matters because the paper positions GPCAGEN as filling a missing methodological gap for exact Wasserstein GPCA in $\mathbb{R}^d$. Right now, the experiments are on relatively small datasets and modest dimensions, and there is no runtime table, no complexity discussion in the main text, and no indication of how the approach behaves on larger-scale distributional datasets typical in modern ML.

8. **There are places where the exposition overstates theoretical neatness relative to what is actually optimized.**  
   A concrete example is the transition from equation (15) to Algorithm 1. Equation (15) is formulated over $f \in \mathcal{C}(\mathbb{R}^d)$, $\varphi \in \mathrm{Diff}(\Omega)$, and true Wasserstein distances. Algorithm 1, however, optimizes neural surrogates with minibatched empirical Sinkhorn losses and clipped times. That is fine as an implementation, but the paper sometimes slides between the ideal geometric formulation and the actual estimator too quickly. I would encourage the authors to distinguish more sharply between the population objective, the function-class-restricted empirical objective, and the final stochastic algorithm.

9. **The literature positioning for neural geodesic learning in Wasserstein space could be stronger.**  
   The paper is well positioned against TPCA, 1D GPCA, and generalized geodesic approximations, but the discussion of learning-based approaches to Wasserstein geodesics is comparatively thin. Since the general method’s distinctive ingredient is a neural parameterization of geodesics, I would have liked a more explicit positioning against nearby neural OT / geodesic-learning approaches, even if the goals differ. As written, the paper’s geometry/statistics positioning is strong, while the modern ML positioning is thinner than ideal for ICLR.

10. **A small but nontrivial mathematical / notation issue:** the practical enforcement of the geodesic interval deserves a more precise statement.  
   On **Page 6**, the paper says positivity of $I_d + t H_{f_\psi}(x)$ for all $x$ and $t \in [t_{\min}, t_{\max}]$ is monitored by evaluating Hessians on sampled points $\{x_k\}_{k=1}^m$. This is only a sample-based sufficient heuristic, not a certification over $\mathbb{R}^d$. Since the geodesic validity depends on a uniform condition in $x$, the text should say explicitly that the implemented interval is an empirical approximation and may fail away from sampled points. That distinction is currently too implicit.

## Questions
1. **Can the authors sharpen the exactness claim for Section 4?**  
   I would like the rebuttal to clearly separate three notions:  
   (i) exact parameterization of a Wasserstein geodesic once $(\varphi,f)$ satisfy the geometric conditions,  
   (ii) optimization over a restricted neural function class, and  
   (iii) replacement of $W_2^2$ by Sinkhorn divergence on minibatches.  
   A precise reformulation of the contribution would increase my confidence.

2. **What objective-based quantitative evidence can the authors provide for GPCAGEN on the synthetic experiments?**  
   For the MNIST constructed-geodesic setup in Section 5.2, can the authors report any numerical recovery metric, such as projection-time error, distance between learned and planted horizontal directions, or residual objective gap to the planted solution? Even a compact table would help a lot.

3. **Can the authors provide a direct quantitative comparison to TPCA or another baseline on a shared evaluation metric?**  
   I understand the representation mismatch, but a common empirical criterion should still be possible. For example, comparing projected-sample Sinkhorn residuals, or approximated $W_2$ residuals after projection, would make the baseline section more persuasive.

4. **How often is the time clipping active in Algorithm 1, and how much does it affect the learned components?**  
   Since clipping is central to preserving the diffeomorphism condition, it would help to know whether clipping is a rare guardrail or a frequent part of optimization. A statistic over training runs would be informative.

5. **How sensitive are results to the choice of reference measure $\rho$ in practice?**  
   The paper says the lifting approach is independent of the chosen reference measure at the conceptual level, but the neural parameterization and optimization may still behave differently depending on $\rho$. Did the authors test alternatives to the standard Gaussian?

6. **Can the authors comment on identifiability or non-uniqueness of learned higher components in the neural setting?**  
   Figure 8 in the Gaussian appendix highlights non-uniqueness in a symmetric case. In the general method, do different random seeds yield components with materially different objective values or qualitatively different geodesics?

7. **Would it be possible to report runtime or scaling information in the main paper?**  
   Even a small table with wall-clock time for the synthetic/MNIST/point-cloud experiments would help readers assess the practicality of the method.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No specific ethics concerns identified from the paper. The datasets used are standard public datasets or descriptive real-world collections, and the work is primarily methodological.

## Soundness Rating
3: good. The Gaussian part is technically solid and the overall methodology is well grounded, but the general a.c. method relies on approximations and soft constraints that make some of the stronger claims less fully supported than the paper suggests.

## Presentation Rating
3: good. The paper is generally clear, well structured, and unusually readable for geometry-heavy material, with effective use of figures, though some claims in the general section should be stated more carefully and the main-paper empirical evidence could be presented more quantitatively.

## Contribution Rating
4: excellent. The Gaussian exact GPCA formulation is a meaningful contribution, and the Otto-inspired neural parameterization for principal geodesics of a.c. measures is creative and likely to be of broad interest to the OT / geometric ML community.

## Overall Rating
8: Accept, good paper (poster). This is a strong and interesting paper with real technical substance, especially on the Gaussian side, and a promising extension to general a.c. measures. I have several concerns about how strongly the “exact GPCA” claim should be interpreted in the neural setting, and I think the experimental evidence for GPCAGEN is too qualitative relative to the ambition of the claims. Still, the strengths outweigh the weaknesses by a comfortable margin, and I would support acceptance.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. The geometric formulation and Gaussian derivations are within my comfort zone, and I checked the main equations and optimization logic carefully; my remaining uncertainty is mostly about how much weight to place on the qualitative evidence for the neural method.
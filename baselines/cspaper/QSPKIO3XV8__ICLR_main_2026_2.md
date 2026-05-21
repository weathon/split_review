---
job_id: 4f7b7b1b-071e-420f-bb59-50786231f295
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: QSPKIO3XV8.pdf
paper: Dimension Domain Co-Decomposition: Solving PDEs with Interpretability
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it proposes a machine learning method for physics-informed neural networks, with emphasis on decomposition, interpretability, and scientific ML for PDE solving.

## Minimum Quality
Pass ✅. The submission contains the expected core sections, namely abstract, introduction, related work, methodology, experiments with quantitative and qualitative results, and conclusion. While there are substantial issues in rigor, positioning, and clarity, these do not rise to the level of an immediate desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, review-targeting instructions, or other obvious manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper proposes Dimension Domain Co-Decomposition (3D), a PINN framework that combines dimension-wise factorization within each expert and Mixture-of-Experts based soft domain decomposition across experts. The method uses a shared MLP with coordinate-index inputs to reduce parameters relative to per-dimension networks, and introduces a Variable Interpretability ($VI$) score based on subspace alignment between learned dimension components and reference factors. Experiments on Poisson, Wave, Burgers, and Linear Transport equations evaluate parameter efficiency, solution accuracy, interpretability, and learned domain partitions.

## Strengths
The paper tackles a real pain point in PINNs, namely the combination of high-dimensional inputs and localized solution structure. The attempt to unify dimension decomposition and adaptive domain decomposition in one framework is sensible and, at least conceptually, useful for scientific ML problems where both scalability and local specialization matter.

The shared-MLP expert parameterization is a reasonable architectural idea. The parameter-count comparison in **Table 1** does show a clear reduction versus independent per-dimension MLPs, and the reduction becomes more pronounced as dimensionality grows, which is exactly the regime the paper claims to target. Even if parameter count is not the whole story, the architectural simplification itself is easy to understand and practically relevant.

The paper does include a concrete interpretability metric instead of only qualitative claims. I appreciate that **Section 3.2** at least tries to formalize what “dimension interpretability” means under permutation/scale ambiguities by using normalized matrices, QR bases, and singular values in **Equations (5) and (6)**. Many papers throw around interpretability language without any measurable criterion; this one does attempt to operationalize it.

Some of the visualizations are genuinely helpful. **Figure 1** communicates the intended decomposition well: the left side clarifies how router weights induce soft domain specialization, and the right side clarifies how per-coordinate streams are combined multiplicatively within an expert. Likewise, **Figure 4** is one of the more convincing parts of the paper, because it visually supports the claim that the router can discover a Burgers partition aligned with the shock near $x=0$ without a hand-designed interface.

The experiments are broader than a single toy problem. The paper covers both separable smooth problems, such as Poisson and Wave, and more localized or discontinuous settings, such as Burgers and piecewise Linear Transport. That breadth is useful because the two decomposition mechanisms are supposed to address different failure modes of standard PINNs.

The learning curves in **Figure 2** do suggest that the proposed decomposition is not merely cosmetic for the 5d Poisson task. The shared MLP and independent-MLP decompositions both substantially outperform the vanilla PINN baseline in relative $\ell_2$ error, and the shared version is at least competitive while using fewer parameters. This is a good sanity check that the decomposition is doing something meaningful on the target benchmark.

## Weaknesses
1. **The novelty claim is overstated relative to what is actually new in the paper.**  
   The paper combines two fairly familiar ingredients: CP/separable dimension decomposition on the one hand, and MoE or gating-based soft domain decomposition on the other. The dimension part is explicitly positioned against SPINNs in **Section 3.1**, and the domain part is positioned against XPINNs/APINNs in **Section 2.2** and **Section 3.3**. What remains as the main technical novelty is essentially the combination plus the shared coordinate-index MLP plus the $VI$ metric. That is not nothing, but the paper presents the framework as if it solves three major obstacles in one stroke, whereas the actual advance feels more incremental and compositional. This matters because for ICLR main track, a paper that mainly recombines existing decomposition ideas needs especially strong empirical or theoretical evidence to justify the broader claims.

2. **The paper’s empirical positioning is too narrow, and key comparisons are missing.**  
   The experiments compare mainly against vanilla PINNs and against an internal ablation using independent per-dimension MLPs. That is not enough to establish the paper’s advantage relative to the most relevant prior art. For dimension decomposition, the obvious baseline is SPINNs, which is discussed repeatedly in **Section 3.1** but not quantitatively compared in the main results. For domain decomposition, XPINNs/APINNs-style methods are the natural baselines, yet the Burgers and Transport sections provide no head-to-head comparison in the main paper. This omission matters because the paper’s central pitch is not “our method works better than vanilla PINNs,” which is a low bar on these examples, but “our particular co-decomposition improves scalability, accuracy, and interpretability over existing decomposition strategies.” The current experiments do not really establish that.

3. **Several mathematical descriptions are underspecified or internally loose, especially around the actual expert computation and training objective.**  
   In **Equation (1)**, the expert is written as
   \[
   E_i(\mathbf{x}) = E_i(f_1(x_1),\dots,f_d(x_d)),
   \]
   but this notation obscures whether each $f_j$ is shared across experts, shared across dimensions only within an expert, or globally shared. Later text in **Section 3.1** suggests “a single shared MLP within each expert,” which is different from what **Equation (1)** naturally suggests. Similarly, **Equation (3)** gives
   \[
   \hat{u}(x_1,\dots,x_d)=\sum_{i=1}^r f^{(i)}(x_1,0)\cdots f^{(i)}(x_d,d-1),
   \]
   but this is the single-expert form, while the full MoE form should include the expert index and router weighting. The paper never cleanly writes the complete final model in one unambiguous expression, for example something like
   \[
   \hat u(\mathbf x)=\sum_{k=1}^{K} G_k(\mathbf x)\sum_{\ell=1}^{r}\prod_{j=1}^{d} f^{(k,\ell)}(x_j,j-1).
   \]
   That may sound cosmetic, but it is not. For PDE training, the precise computational graph determines derivative structure, parameter sharing, and complexity claims.

4. **The loss definition in the main paper is too generic to support some of the method claims.**  
   **Equation (4)** gives a standard weighted PINN loss:
   \[
   Loss = w_{pde}Loss_{pde} + w_{ic}Loss_{ic} + w_{bc}Loss_{bc}.
   \]
   But for the proposed MoE setup, the details that really matter are not stated in the main paper: how collocation points are sampled under the claimed “bypass meshgrid” strategy, whether the same points are used for all experts, whether any regularizer is applied to router entropy or expert balance, and whether there is any stabilization preventing expert collapse. **Section 3.3** claims dense MoE “avoids expert collapse and provides more stable training,” which is a strong statement, but there is no supporting derivation, no balancing loss, and no systematic evidence beyond a few visualizations. Dense mixtures can still collapse in practice if one expert dominates, so the current description feels hand-wavy rather than technically pinned down.

5. **The interpretability metric $VI$ is only convincing in a very favorable setting, and the paper does not sufficiently acknowledge how limited that setting is.**  
   The definition in **Section 3.2** measures subspace alignment between learned components and known exact factors. That is a clean linear-algebra construction, but it heavily depends on having a separable reference factorization $G$. The paper finally admits this in the conclusion, but most of the main empirical section tests exactly those problems where the answer is analytically separable by construction, such as the product-form Poisson and Wave examples. In that regime, $VI$ is almost tailor-made to succeed. This matters scientifically because the paper’s title and framing suggest interpretable PDE solving more broadly, whereas the proposed metric really evaluates recovery of known separable factors on specially chosen examples. The gap between the broad interpretability narrative and the narrow evaluable setting is substantial.

6. **There is a serious mismatch between the claimed meaning of “interpretability” and what the results actually show.**  
   In **Table 2**, for 5d and 10d Poisson, $VI$ is near zero for $r=1$ and jumps toward $1$ as $r$ increases to $4$ or $5$, even though the true factorization is rank-1 separable in the sense of the analytical solution. The paper interprets this as evidence that “a small value of $r$ ensures good interpretability,” but the more uncomfortable interpretation is that the learned representation is not identifying the true low-rank factorization cleanly, and instead needs overcomplete latent subspaces to contain it. Because $VI$ rewards subspace containment when $s<r$, a model can achieve $VI=1$ while still having many extra latent directions that are not interpretable in any human sense. The paper acknowledges this in **Section 3.2**, but then still uses $VI\approx 1$ as if it meant strong interpretability. That is too generous. The metric is more accurately a “ground-truth subspace coverage” score than a direct interpretability score.

7. **The results tables are incomplete for supporting the paper’s core claims.**  
   **Table 1** reports parameter counts only, not runtime, memory, or accuracy in the same table. The text adds some runtime and memory claims, but these are selectively reported and not organized in a way that allows fair trade-off analysis. Similarly, **Table 2** reports only $VI$ scores, not the corresponding $\ell_2$ errors for the same settings in the main paper. That omission matters because the paper repeatedly argues that small rank $r$ achieves both interpretability and accuracy, yet the main table on interpretability does not jointly report accuracy. The reader is forced to piece together these claims from dispersed text and appendix material. A combined table of $(r, VI, \ell_2\text{ error}, \text{runtime})$ per PDE would have been much more convincing.

8. **The domain decomposition evidence is visually suggestive but quantitatively weak.**  
   The Burgers and Transport sections lean heavily on figures, especially **Figure 4** and **Figure 5**, to argue that the router discovers meaningful partitions. The problem is that “looks aligned with shock/stripes” is not enough by itself, especially when the tasks are simple and the partitions are visually easy to guess after seeing the solution. There is no quantitative measure of partition quality, no stability metric in the main paper, no comparison to manually chosen subdomains, and no analysis of whether the learned partition improves PDE residual locally. In **Figure 4**, the distinction between $K=2$ and $K=3$ is indeed visible, but the conclusion that the additional expert adds “little new information” is based on visual judgment rather than a defined criterion. For a paper selling adaptive decomposition, this part is thinner than it should be.

9. **The paper makes efficiency claims that are only partially substantiated and at times confusing.**  
   In **Section 3.1**, the authors argue that dimension decomposition simplifies derivative computation and drastically reduces collocation requirements by avoiding full meshgrid construction. But the experiments do not really isolate those gains. For example, in the 10d Poisson discussion on **Page 7**, the shared MLP is more accurate than a baseline PINN with comparable parameter count, but it is also slower in total training time (1579s vs 1184s). That does not invalidate the method, but it does complicate the “computational efficiency” narrative in the abstract. Likewise, the memory reduction percentages are stated in text on **Page 6**, but the setup for measuring memory is not specified in the main paper. The efficiency story is therefore plausible, not demonstrated cleanly.

10. **The exposition has many rough edges, and some are serious enough to hurt confidence.**  
   There are multiple grammar issues, notation inconsistencies, and a few obvious typos, for example “for the tested viscosity $\nu=\frac{0.01}{x}$” in **Section 4.3**, which contradicts Appendix A where the Burgers viscosity is correctly given as $\nu=\frac{0.01}{\pi}$. That is not a trivial typo in context, because viscosity is central to the Burgers setup. There are also awkward statements like “our framework bases on PINNs” and inconsistent singular/plural or indexing conventions. The references section appears corrupted at the start on **Page 10**, with duplicate nonsensical entries for Agarwal et al. These issues may look editorial, but taken together they make the submission feel insufficiently polished for a main-track paper and reduce trust that all technical details were checked carefully.

11. **The claims about automatic domain decomposition without interface conditions need more nuance.**  
   The paper contrasts its MoE approach with XPINNs-like methods that require explicit interface penalties, implying that the weighted-sum construction sidesteps this difficulty. That is true in the narrow sense that continuity is inherited from the soft mixture, but it is not a free lunch. The price is that experts are no longer solving separate local PDE problems with explicit interface control; instead, all experts contribute globally through the router. This means the method is closer to adaptive soft specialization than classical domain decomposition. The paper would be stronger if it explicitly acknowledged this distinction rather than presenting it as a clean replacement. Right now, the wording in **Sections 1 and 3.3** slightly oversells what kind of “domain decomposition” is being achieved.

12. **Some benchmark choices are too convenient for the paper’s narrative.**  
   The main interpretability examples are separable analytic solutions where the decomposition structure is already built into the target. The domain decomposition examples are low-dimensional, visually structured transport/shock problems where routing patterns are easy to display attractively. What is missing is a harder setting that simultaneously stresses high-dimensionality, nontrivial local structure, and the claimed interpretability benefits. Without such a benchmark, the paper demonstrates that the framework can work on handpicked regimes, but not yet that it provides a robust general solution to the stated problem.

## Questions
1. Could the authors provide a clean, single equation for the complete model used in the MoE case, including the expert index, decomposition rank, and router, and clarify exactly what parameters are shared within and across experts? This would substantially improve confidence in the method description.

2. Can the authors add direct quantitative comparisons in the main paper against the most relevant decomposition baselines, especially SPINNs for dimension decomposition and APINNs/XPINNs-style methods for domain decomposition? Without these, it is difficult to assess whether the method advances the state of the art or mainly repackages prior decomposition ideas.

3. For the $VI$ metric, can the authors clarify whether they intend it to measure exact factor recovery, subspace coverage, or something else? In particular, how should one interpret the Poisson result in **Table 2**, where the true solution is separable yet $r=1$ gives very low $VI$ and overcomplete $r>1$ gives $VI \approx 1$? A more careful discussion of what counts as interpretability here could change my view.

4. Can the authors report joint tables in the main paper with $\ell_2$ error, $VI$, runtime, and parameter count for the same settings of $r$ and $K$? Right now the evidence is fragmented across text, figures, and appendix.

5. The paper claims dense MoE avoids expert collapse and yields stable training. Can the authors provide quantitative evidence in the main paper, such as router entropy, average expert utilization, or variance across seeds, rather than only qualitative partition plots?

6. For **Figure 4** and **Figure 5**, can the authors define an objective criterion for choosing $K_{\text{optimal}}$ rather than relying on visual judgment that additional experts provide “no more new information”? This selection criterion matters if the method is to be used in practice.

7. Please clarify the Burgers viscosity typo in **Section 4.3** and check the manuscript for similar inconsistencies. I want to make sure I am not missing any experiment-specific setup differences between the main text and appendix.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the submission. The work is a methodological paper on PDE solvers and does not present obvious issues related to human subjects, privacy, or deployment harms within the scope of the manuscript.

## Soundness Rating
2: fair. The core idea is plausible and some experiments are supportive, but several claims are under-justified, important baselines are missing, and the mathematical/methodological exposition is not tight enough for stronger confidence.

## Presentation Rating
2: fair. The high-level idea is understandable and some figures help, but the paper has notable clarity problems, notation inconsistencies, typos, and uneven organization of evidence.

## Contribution Rating
2: fair. The combination of shared dimension decomposition, soft MoE partitioning, and a subspace-based interpretability metric is potentially useful, but the empirical positioning and demonstrated advance over prior decomposition-based PINNs are not yet strong enough for a higher rating.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper has an interesting direction and some promising results, especially the Burgers visualization and the parameter-efficiency story, but the current version overclaims relative to the evidence. Missing key baselines, a somewhat generous interpretation of $VI$, and loose technical exposition keep it below the bar for me.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. I am familiar with PINNs, decomposition methods, and scientific ML, and I checked the main mathematical definitions and empirical claims carefully.
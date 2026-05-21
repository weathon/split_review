---
job_id: 4535ca73-e8d5-4a89-80a9-b2cc2a1148ac
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 8ZQ0HjBOEc.pdf
paper: Understanding the Role of Depth in the Neural Tangent Kernel for Overparameterized Neural Networks
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, specifically learning theory, kernel learning, optimization dynamics, and overparameterized neural networks.

## Minimum Quality
Pass ✅. The paper contains the expected scientific structure, including Abstract, Introduction, Related Work, technical development/background, experiments, and Conclusion. While I found substantial issues in rigor, exposition, and empirical support, they do not rise to the level of an automatic desk rejection based on the manuscript alone.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I found no hidden prompts, suspicious instructions to automated reviewers, or other manipulative content in the provided paper text and figure.

# Expected Review Outcome:
## Summary
This paper studies how depth affects the infinite-width neural tangent kernel of fully-connected ReLU networks. The main claims are that, after a specific normalization, the limiting NTK converges entrywise to the all-ones matrix as depth grows, while the kernel-regression-type predictor $\bar{\Theta}^{(L)}_{\infty}(x^\top X)\big(\bar{\Theta}^{(L)}_{\infty}(X^\top X)\big)^{-1}$ still converges to a nontrivial limit on the sphere. The paper combines standard NTK recursions with a rough differential equation argument and includes small empirical illustrations of convergence behavior.

## Strengths
1. **The paper asks a legitimate and interesting question.**  
   The role of depth in the NTK regime is important, especially because depth is often discussed as beneficial in practice while the kernel regime can exhibit collapse or loss of data-dependent structure. The focus on the asymptotic behavior of $\Theta_\infty^{(L)}$ as $L\to\infty$ is relevant to the representation-learning theory community.

2. **The normalization viewpoint is useful and reasonably well motivated.**  
   Definition 4 on Page 6 introduces
   \[
   \bar{\Theta}_{\infty}^{(L)}(x,x')=\frac{n_0 2^{L-1}\Theta_{\infty}^{(L)}(x,x')}{L},
   \]
   which aligns with Proposition 1 for the perfectly correlated case and makes the depth dependence more interpretable. This normalization helps isolate the interesting phenomenon that the kernel entries collapse toward $1$ while the predictor ratio can still have a limit.

3. **The monotonic convergence statement in Theorem 2 is conceptually clean.**  
   The claim on Page 6 that $\bar{\Theta}_{\infty}^{(L)}(x,x')$ strictly increases to $1$ for points on the sphere is a crisp statement. If correct, this gives a simple picture of deep ReLU NTK degeneration in the normalized coordinates.

4. **The paper does attempt to go beyond the obvious “kernel goes rank-one” story.**  
   The central ambition of Theorem 3, namely to show that
   \[
   \bar{\Theta}_{\infty}^{(L)}(x^\top X)\big(\bar{\Theta}_{\infty}^{(L)}(X^\top X)\big)^{-1}
   \]
   has a well-defined limit even though the matrix itself approaches singularity, is potentially interesting. This is the one aspect of the paper that, if made fully rigorous and interpretable, could differentiate it from a more standard depth-collapse note.

5. **Figure 1 is helpful in conveying the intended qualitative story.**  
   The three columns of Figure 1 on Page 10 show, for each kernel family, the behavior of the Gram matrix entries, cross-kernel vector, and predictor-like product $\bar{\kappa}^{(L)}(x^\top X)\big(\bar{\kappa}^{(L)}(XX^\top)\big)^{-1}$. In particular, the first row supports the paper’s qualitative claim that the normalized NTK entries move toward a common value very slowly, while the rightmost column suggests the predictor expression stabilizes earlier. This figure is one of the clearest parts of the submission.

6. **The paper is reasonably well connected to classical NTK background.**  
   The recap of Definitions 1 and 2 and Theorem 1 on Pages 4 to 5 makes the manuscript mostly self-contained for readers already familiar with NTK theory.

## Weaknesses
1. **The main technical contribution, Theorem 3, is not stated or proved at a level of precision that would let me trust it.**  
   This is my biggest concern. Theorem 3 on Pages 7 to 8 asserts the existence of a sequence of paths $v_{ij}^{(L)}$, a rough path lift $\mathbf v^{(L)}$, and a differential equation whose solution satisfies
   \[
   u_i^{(L)}(1)=\bar{\Theta}^{(L)}_{\infty}(x^\top X)^\top \big(\bar{\Theta}^{(L)}_{\infty}(X^\top X)\big)^{-1},
   \]
   but several basic elements are underspecified or inconsistent:
   - The displayed differential equation is
     \[
     \frac{d}{dt}u_i^{(L)}(t)=0,
     \]
     which is trivial and does not seem to match the earlier derivation from differentiating the linear system $A_n^{(L+1)}(t)u(t)=b_n^{(L+1)}(t)$. The paper later says the RDE is “driven” by the rough path lift, but the actual vector field and control dependence are not written in standard RDE form.
   - The theorem statement mixes existence, asymptotic convergence, boundedness, and an identification of the endpoint, but it is unclear exactly what converges to what. The statement says “there exists a sequence of paths” and then that the projection of the solution “satisfies the equality”; this reads more like a construction than a theorem with transparent assumptions and conclusion.
   - The dimensions are murky. For example, $\mathbf v^{(L)}:\Delta_{0,1}\to \mathbb R^{n\times n+1}$ is not standard rough path notation, and it is not clear how the indices $(i,j)$ map to the driving signal dimension.
   - The theorem does not identify the limiting predictor explicitly. It only argues existence of some bounded limit. That weakens the scientific value considerably, because the reader learns that a limit exists but not what it is, how it depends on $x$, or why it matters for prediction.

   In short, the theorem is trying to do the heavy lifting of the paper, but it remains too opaque and too compressed.

2. **There are concrete derivational and notation problems around Equation (5) and the proof of Theorem 3.**  
   On Page 7, after differentiating $A_n^{(L+1)}(t)u(t)=b_n^{(L+1)}(t)$, the paper gives Equation (5):
   \[
   u_i'(t)=\frac{\sum_j \det\big(A_n^{(L+1)}(t)\longleftarrow_{i,j} Z_A\big)}{\det(A_n^{(L+1)}(t))}+\frac{\det\big(A_n^{(L+1)}(t)\longleftarrow_{i,1} Z_b\big)}{\det(A_n^{(L+1)}(t))}.
   \]
   I had several issues here:
   - The replacement notation $A\longleftarrow_{i,j} Z_A$ is nonstandard and not fully defined in this proof. Earlier on Page 3, the notation is given as $A\leftrightarrow_{i,j}A'$, which is different. This inconsistency matters because the proof hinges on determinant manipulations.
   - $Z_A=-\big(\frac d{dt}A_n^{(L+1)}(t)\big)\operatorname{diag}(u(t))$ is dimensionally suspicious. If $u(t)\in\mathbb R^n$, then $\operatorname{diag}(u(t))\in\mathbb R^{n\times n}$, so $Z_A$ is a matrix, but the Cramer-rule expression seems to replace a single column by another single column, not by a full matrix. The notation does not tell the reader which column of $Z_A$ is inserted.
   - Since $b_n^{(L+1)}(t)=\bar{\Theta}^{(L+1)}_\infty(x^\top X^T)$ is defined on Page 7 with no $t$ dependence, indeed $Z_b=0$, so the second term vanishes identically. This makes the proof even more dependent on the first determinant ratio, which is only very loosely bounded.
   - The key inequality chain on Page 8 uses determinants of interpolated matrices and then divides by the product of two determinants, but no theorem is cited to justify the bound
     \[
     \det(A_n^{(L+1)}(t))\ge \det(\bar{\Theta}_{\infty}^{(L+1)}(XX^\top))^{\psi_\mathcal D(2t-1)}
     \det(\bar{\Theta}_{\infty}^{(L)}(XX^\top))^{1-\psi_\mathcal D(2t-1)}.
     \]
     Determinant is not generally log-convex along arbitrary matrix interpolations in the way used here unless additional structure is established. This is not a cosmetic point, it is central to the vanishing-control argument.

3. **The paper repeatedly overstates what has been established relative to what is actually shown in the main text.**  
   For example, the abstract says the “closed-form solution approaches a fixed limit on the sphere,” and the introduction says the paper “characteriz[es]” this limiting solution. But in the main text, Theorem 3 does not provide a closed form for the limit, nor even a particularly interpretable formula. It gives an existence-and-boundedness style argument. Similarly, Section 6 claims that “small depths $L$ are required to approximate the limit of $\kappa_x\kappa^{-1}$,” but the paper does not directly compute approximation error to the limiting predictor. Figure 1 right column suggests stabilization, but that is not a quantitative validation of the claimed practical depth scale.

4. **The empirical section is too thin to support the practical implications emphasized in the paper.**  
   Section 6 is essentially a single qualitative convergence plot on synthetic data, plus a mention of MNIST plots relegated to Appendix F. There are no benchmark tables in the main paper, no quantitative depth-vs-error analysis, no finite-width experiments, and no comparison to alternative kernels or alternative activations. This is a problem because the conclusion on Pages 9 to 10 repeatedly talks about the practical depth needed to see the limit and about extending the proof technique to other kernels, but the evidence is minimal.

   More specifically, Figure 1 is informative but not enough. In the top-left panel, the off-diagonal values of $\bar{\kappa}^{(L)}(XX^\top)$ are still visibly well below $1$ by depth $30$, which actually underlines how far the asymptotic theorem is from realistic depth scales. In the top-right panel, the quantity $\bar{\kappa}^{(L)}(x^\top X)\big(\bar{\kappa}^{(L)}(XX^\top)\big)^{-1}$ appears to stabilize quickly, but the figure lacks any error bars, reference limiting solution, dataset size annotation, or quantitative metric. The visual story is suggestive, not convincing.

5. **The paper lacks quantitative results tables in the main text, and this hurts the evaluation substantially.**  
   Given that one of the paper’s selling points is the order of magnitude in depth required to observe convergence behavior, I expected at least one explicit results table reporting, for several datasets and depths, metrics such as:
   \[
   \|\bar{\Theta}^{(L)}_\infty(XX^\top)-\mathbf 1\mathbf 1^\top\|,\quad
   \left\|\bar{\Theta}^{(L)}_\infty(x^\top X)\big(\bar{\Theta}^{(L)}_\infty(XX^\top)\big)^{-1}-u_\infty(x)\right\|,
   \]
   or determinant decay, condition number, and prediction error. Instead, the main paper contains no quantitative results table at all. The only “table” mentioned is “table 1 in Appendix E” on Page 2, which is described as a summary of related results rather than empirical evidence. For a paper making empirical claims about convergence rates and practical depth scales, the absence of a real results table is a serious weakness.

6. **Some mathematical statements are either incorrect, imprecise, or at least very poorly phrased.**  
   A few examples:
   - Proposition 1 proof sketch on Page 4 is too thin to verify. The phrase “$\mu=0$ implies $x^\top x'\ge 0$ with probability $\frac12$” is confusing in this context and does not read like a proof of the displayed formulas.
   - On Page 5, the bullet “If we map points from $\mathbb R^{n_0}$ to the sphere $S^{n_0}$ by embedding them ... the embedding of the datapoints satisfies $x_i^\top x_j=1$ for all $x_i,x_j$ in the dataset” appears wrong as written. If all pairwise inner products after embedding were exactly $1$, all points would coincide. I suspect the intended statement is different, perhaps about self-inner-products or positivity, but the current wording is mathematically untenable.
   - Proposition 2 on Page 5 uses $\rho\in[-1,1[$ and gives a recursion involving $\arcsin \rho^{(L)}$. This may be fine, but the notation blurs the base-layer $\rho$ and the recursively updated $\rho^{(L)}$, and the formulas are not easy to verify because the connection to the standard arc-cosine kernel formulas is not carefully explained.

7. **The exposition is much rougher than it should be for a theory paper of this type.**  
   There are many local issues, but the broader problem is that the manuscript asks the reader to trust difficult arguments too quickly.
   - Section 5 moves from monotone kernel collapse to rough path machinery with very little intuition for why an RDE framework is the right lens.
   - The introduction claims two “central aspects” and says Proposition 4 and Theorem 3 are the key results, but the logical dependencies among Lemma 1, Proposition 4, Theorem 2, Proposition 5, and Theorem 3 are not cleanly staged.
   - Several cross-references are sloppy. On Page 4, after Theorem 1, the text says the theorem is key in the convergence results obtained in “the next section (Proposition 4 and Theorem 2),” but Theorem 3 is actually the central destination.
   - There are many grammatical and typographical issues, for example “allow us” instead of “allows us” on Page 5, “partciular” on Page 3, “due their empirical popularity” on Page 3, duplicated wording on Page 10 (“the convergence for the limiting kernel is experimentally fast”), and mismatched transposes such as $x^\top X^\top$ versus $x^\top X$.

   None of these alone would sink the paper, but together they make a technically ambitious paper much harder to trust.

8. **The assumptions and regimes are narrower than the presentation suggests.**  
   The main theorem is framed in the “compact regime,” meaning inputs on the sphere, and the extension to general $\mathbb R^{n_0}$ is only sketched using canonical or stereographic projections. That is not the same as proving the result in the non-compact setting. Likewise, the analysis relies on the scaling $L\in o(\min_l n_l)$, which excludes the regime where depth is comparable to or larger than width, arguably the more delicate and practically relevant setting for depth pathologies. The paper does state this distinction relative to Hanin and Nica, which is good, but the conclusion sometimes reads more broadly than warranted.

9. **The literature positioning is incomplete in ways that matter for the paper’s claimed significance.**  
   The related work covers many classical NTK references, but the paper would benefit from a clearer comparison to prior analyses of depth-induced degeneration or conditioning issues in the kernel regime. As written, the positioning versus existing “curse of depth,” finite-width corrections, and spectral perspectives is not sharp enough. This matters because the paper’s main conceptual message, deep kernel collapse with subtle predictor limits, sits very close to an already active line of work. The manuscript needs a more explicit account of what is genuinely new beyond the choice of proof technique.

10. **The practical significance remains unclear.**  
   The paper itself acknowledges on Pages 9 to 10 that convergence of the normalized kernel is “extremely slow” and may require very large $L$. If so, then the primary practical takeaway shifts to the claim that the predictor ratio stabilizes quickly. But this is only hypothesized from determinant behavior and suggested by Figure 1, not established quantitatively. Without a clearer finite-depth story, the work risks being mathematically interesting but operationally hard to interpret.

## Questions
1. **Please clarify the exact mathematical statement of Theorem 3.**  
   What is the precise limiting object? Is it a function $u_\infty(x)\in\mathbb R^n$ characterized uniquely for each $x$, or merely an existence statement for bounded subsequential limits? A sharper theorem statement would significantly increase my confidence.

2. **Can you rewrite the proof of Theorem 3 in a standard RDE form?**  
   Right now the theorem states a trivial ODE $\frac d{dt}u_i^{(L)}(t)=0$ while also claiming the solution is driven by a rough path. Please explicitly write something of the form
   \[
   du_t = V(u_t)\,d\mathbf v_t
   \]
   or explain why the current notation is equivalent. Also specify the signal dimension and the vector fields.

3. **Please justify the determinant inequalities on Page 8.**  
   The step comparing $\det(A_n^{(L+1)}(t))$ to products of determinants of endpoint kernels is not obvious. Which matrix inequality or concavity/convexity result are you invoking? If that step is only heuristic, the whole proof needs revision.

4. **Can you provide a quantitative finite-depth result, not only asymptotic convergence?**  
   For example, can you bound
   \[
   1-\bar{\Theta}_{\infty}^{(L)}(x,x'), \quad
   \det\big(\bar{\Theta}_{\infty}^{(L)}(XX^\top)\big), \quad
   \left\|\bar{\Theta}^{(L)}_{\infty}(x^\top X)\big(\bar{\Theta}^{(L)}_{\infty}(X^\top X)\big)^{-1}-u_\infty(x)\right\|?
   \]
   Even rough upper/lower bounds would help connect the asymptotic statements to realistic depths.

5. **Can you make the empirical section quantitative?**  
   A useful rebuttal would include a small table, even if only for synthetic data and MNIST, showing depth versus kernel-collapse metric, determinant, and predictor convergence error. The current qualitative plots are not enough to support the claim that moderate depths already approximate the predictor limit well.

6. **What exactly is the non-compact extension?**  
   On Pages 5 and 8, the paper suggests that canonical or stereographic projection extends the result beyond the sphere. Please state the theorem you believe holds in $\mathbb R^{n_0}$ and what changes in the proof.

7. **Please fix the problematic statement about inverse stereographic projection on Page 5.**  
   As written, the claim that the embedded datapoints satisfy $x_i^\top x_j=1$ for all pairs cannot be right. What is the intended property?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None.

## Soundness Rating
2: fair. The paper contains interesting ideas and some plausible intermediate claims, but the main theorem and its proof are not rigorous enough in the main text to fully support the central claims.

## Presentation Rating
2: fair. The paper is readable at a high level, but the exposition of the core technical argument is too unclear and notation is too inconsistent for a strong theory submission.

## Contribution Rating
2: fair. The topic is relevant and the predictor-limit angle could be meaningful, but the contribution is weakened by unclear rigor, limited empirical validation, and insufficiently sharp differentiation from adjacent prior work.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
I see the intended contribution, and there is a potentially interesting core idea here. However, the current manuscript is not convincing enough for ICLR main track because the central theorem is not presented with sufficient rigor or clarity, the empirical support is too narrow, and the practical meaning of the asymptotic results remains underdeveloped.

## Reviewer Confidence
4: confident. I am confident in the negative assessment, especially regarding the clarity and rigor issues around the main theorem and the mismatch between the paper’s claims and its empirical support.
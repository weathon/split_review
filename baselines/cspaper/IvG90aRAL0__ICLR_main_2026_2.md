---
job_id: 03d488fb-26ad-4da1-bf8d-31b6928207a1
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: IvG90aRAL0.pdf
paper: Quantum Algorithms for Projection-Free Sparse Convex Optimization
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly about optimization and learning-theoretic aspects of quantum algorithms for constrained convex optimization, which falls within ICLR’s optimization and general machine learning scope.

## Minimum Quality
Pass ✅. The submission is complete as a theoretical paper, with abstract, introduction, method/theory sections, related-work discussion, quantitative comparison tables, and conclusion; while it has no empirical experiments, it presents theorem-based technical results and complexity comparisons instead.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious reviewer-targeted instructions, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper studies quantum acceleration of projection-free convex optimization via Frank-Wolfe under structured constraints. For vector domains, it gives quantum algorithms for $\ell_1$-ball, simplex, and latent group norm constraints using function-value oracles and approximate gradient estimation, with the main claim being improved dimension dependence in oracle complexity. For matrix domains under nuclear norm constraints, it proposes two approaches based on quantum singular value estimation and a quantum power method to accelerate the linear minimization step by approximating top singular vectors.

## Strengths
The paper tackles a concrete and interesting question, namely whether quantum techniques can speed up the linear subproblem inside Frank-Wolfe for structured constraints. This is a natural place to look for quantum acceleration, and the paper does more than a one-off result by covering both vector and matrix domains.

The vector-side contribution is reasonably coherent. The progression from the $\ell_1$ ball to the simplex, and then to latent group norms, gives a useful unifying story around atomic sets and dominant-atom finding. In particular, the core idea in Section 3, using a function-value oracle to build a coordinatewise finite-difference gradient oracle and then applying quantum maximum finding, is easy to follow at a high level and matches the geometry of the $\ell_1$ and simplex linear minimization oracle.

The complexity comparisons in **Table 1** are useful for readers because they summarize, in one place, what the claimed speedups are in query complexity, qubits, and gates for the vector case. Even though some entries need cleanup, the table does communicate the intended message that the gains are in dimension dependence rather than iteration complexity.

The matrix part is ambitious. Extending the discussion from sparse vectors to nuclear-norm-constrained matrices is a nontrivial broadening of scope, and the two proposed routes, QTSVE and QPM, are at least conceptually different. **Table 2** is also helpful in making the intended comparison explicit, especially the dependence on $\sigma_1(M)-\sigma_2(M)$, rank $r$, and the separation between update cost and gradient evaluation cost.

I also appreciate that the authors try to propagate approximation error through the Frank-Wolfe recursion instead of simply stating black-box subroutines. For example, the derivation around **Equations (38) to (43)** in the vector case shows the intended mechanism by which approximate maximum finding translates into an additive linear-subproblem error and then into the standard $O(C_f/t)$ Frank-Wolfe convergence pattern. That part is the cleanest technical thread in the paper.

## Weaknesses
1. **The matrix-side technical development has several internal inconsistencies, and this substantially weakens confidence in the main claims of Section 4.**  
   This is the biggest issue for me. There are multiple places where the stated complexity formulas, theorem statements, algorithm pseudocode, and proofs do not line up. For example, the abstract claims a matrix update time of $\tilde O(rd/\varepsilon^2)$ and $\tilde O(\sqrt r d/\varepsilon^3)$, but **Theorem 3** on Page 8 states $\tilde O\!\left(\frac{r\sigma_1^2(M_t)d}{(\sigma_1(M_t)-\sigma_2(M_t))\varepsilon^2}\right)$, while the proof in **Appendix B.9, Page 32** appears to derive an upper bound with an extra factor of $\sigma_1(M)$, namely $O\!\left(\frac{r\sigma_1^3(M)d\operatorname{polylog} d}{(\sigma_1(M)-\sigma_2(M))\varepsilon^2}\right)$. These are not cosmetically different, they change the dependence on spectral quantities and therefore the claimed advantage regime. Similarly, **Theorem 4** on Page 10 and its proof on **Page 33-34** do not agree perfectly with the complexity shown in **Table 2**. When the central contribution is asymptotic complexity improvement, these mismatches matter a lot.

2. **There are clear notation and algorithm-definition errors that make parts of the analysis hard to trust.**  
   A striking example is **Algorithm 3, line 6** and **Algorithm 4, line 6** on Page 9, where the step size is written as $\gamma_t=\frac{2}{\varepsilon+2}$ instead of the Frank-Wolfe schedule $\gamma_t=\frac{2}{t+2}$ used elsewhere, including **Algorithm 1** and the subsequent proofs. This is not a minor typo buried in prose, it changes the algorithm. Likewise, **Algorithm 2, line 4** on Page 5 sets $T=\frac{\delta C_f}{\varepsilon}-2$, which is inconsistent with **Lemma 1** and with **Theorem 1**, where the iteration count is $T=\frac{4C_f}{\varepsilon}-2$. There are many such slips, including inconsistent use of $x^{(0)}$ vs. $x^{(1)}$, inconsistent symbols for precision parameters $\epsilon,\varepsilon,\delta,\delta'$, and occasional malformed expressions in the tables and appendix. For a paper whose value rests almost entirely on technical correctness, this level of sloppiness is a real problem, not just a presentation annoyance.

3. **Several mathematical claims are underspecified or rely on assumptions that are stronger than the paper acknowledges, especially around oracle access and state preparation.**  
   In the vector case, **Assumption 3** gives a function-value unitary $U_f:|\mathbf x\rangle|a\rangle\to|\mathbf x\rangle|a+f(\mathbf x)\rangle$, but the paper does not seriously discuss precision of encoding for real-valued $f(\mathbf x)$, arithmetic cost for adding and dividing by $\sigma$, or how errors in finite-precision arithmetic affect the maximum-finding guarantee in **Lemma 4**. The proof of **Lemma 3** on Page 21 claims the gradient oracle takes two queries to $U_f$ and $O(1)$ elementary gates, which is hard to accept as stated because the circuit also performs arithmetic on real numbers and coherent construction of $\mathbf x+\sigma e_i$. Even in oracle-model papers, claiming $O(1)$ gate overhead for nontrivial arithmetic needs explanation. The matrix case is even more assumption-heavy because **Assumption 4** gives QRAM-style access in $\widetilde O(1)$ time, which is extremely strong and often where the practical burden is hidden. The paper does not balance its headline speedup claims with enough discussion of how much is being offloaded into the access model.

4. **The finite-difference gradient error treatment in the vector case is not fully aligned with how the approximate linear subproblem accuracy in Frank-Wolfe is defined.**  
   The paper uses **Lemma 2** to bound $\|g(\mathbf x)-\nabla f(\mathbf x)\|_2\le \frac{\sqrt d L\sigma}{2}$, then converts this to an $\ell_\infty$ bound in **Equation (36)** and eventually to an additive error in the linear subproblem in **Equation (38)**. This part is plausible, but the correspondence to the $\delta$-approximate linear minimization condition in **Equation (5)** is not written carefully enough. In particular, **Equation (5)** requires
   $$
   \langle s,\nabla f(x^{(t)})\rangle \le \min_{\hat s\in\mathcal D}\langle \hat s,\nabla f(x^{(t)})\rangle + \frac{\delta}{2}\gamma_t C_f,
   $$
   so the approximation error must be tied explicitly to $\frac{\delta}{2}\gamma_t C_f$. The proof of **Theorem 1** effectively sets $\sqrt d L\sigma_t = \frac{\gamma_t C_f}{2}$, but this is not framed as selecting a specific $\delta$ in the statement of the theorem. This may be fixable, but right now the connection between the approximate-search subroutine and the formal Frank-Wolfe guarantee is more hand-wavy than it should be.

5. **The matrix Frank-Wolfe linear minimization oracle is stated with sign and formulation ambiguities.**  
   On **Page 7**, the paper says that for the nuclear norm constraint the optimal solution to $\min_{S\in\mathcal D}\langle S,M\rangle$ reduces to $S=\mathbf u\mathbf v^\top$ where $(\mathbf u,\mathbf v)$ are the top singular vectors of $M$. But for minimizing a linear form over the nuclear norm ball, the optimizer should involve the negative top singular dyad, i.e. $S=-\mathbf u_1\mathbf v_1^\top$, unless the sign is absorbed elsewhere. This is not a harmless detail, because **Algorithm 3** and **Algorithm 4** then set $S=uv^\top$ without discussing the sign, and the convergence proof in **Equations (91) to (97)** assumes this is an approximate minimizer. If the sign convention is implicit, it needs to be made explicit. As written, the optimization problem and the chosen update direction do not quite match.

6. **The paper’s claimed advantages are narrow and heavily parameter-dependent, but this is downplayed in the main text.**  
   The headline framing emphasizes an $O(\sqrt d)$ speedup in dimension, but for the matrix case the actual dependence involves spectral gap, rank, singular value normalization, tomography precision, and quantities such as $\gamma'_{\min}$. **Table 2** makes this visible, which is useful, but it also undercuts the broad claim in the abstract that the algorithms "outperform the optimal classical methods in dependence on the dimension $d$." In practice, the comparison is conditional and regime-specific. The discussion in **Appendix A.5** partially acknowledges this, but the main paper should be much more upfront that the speedup is not uniform and can be erased by unfavorable dependence on other parameters.

7. **The use of tomography is a serious bottleneck, and the paper does not engage enough with whether this undermines the matrix-side story.**  
   In **Lemma 6** and **Lemma 7**, the conversion from a quantum singular-vector state to a classical vector incurs a factor $O(d\log d/\delta^2)$, which is then the dominant $d$-dependence in the matrix results. The paper still claims at least an $O(\sqrt d)$ improvement over classical methods, but the reader is left to reconcile a lot of moving parts, especially since classical top-singular-vector methods like Lanczos are very mature and the paper does not compare against the best possible low-rank or randomized classical approaches under matched input assumptions. The broad takeaway from **Table 2** is therefore less convincing than the prose suggests.

8. **Presentation quality is below the bar for a theory paper at this level.**  
   There are many grammatical issues, malformed formulas, and broken table entries. **Table 1** in particular contains several rendering problems, including corrupted constraint names and query-complexity expressions that are difficult to parse. The tables are supposed to be the paper’s executive summary, but here they instead create friction. There are also many minor but cumulative issues such as "succeed" instead of "succeeds," "continues" instead of "continuous," missing minus signs, and index mistakes. I am deliberately not focusing on style for its own sake, but in this case the exposition errors spill into technical ambiguity.

9. **The related-work positioning is somewhat incomplete and occasionally too self-congratulatory.**  
   The paper cites a broad quantum optimization literature, but the positioning relative to other quantum approaches to convex optimization and Frank-Wolfe-like methods is not sharp enough. For instance, there is little discussion of what is genuinely specific to projection-free sparse convex optimization here, versus what follows from plugging standard quantum search or QSVE tools into a known Frank-Wolfe template. The statement "to our best knowledge, we are the first one to consider accelerating the matrix case of the FW algorithm by quantum computing" may be true, but the paper does not do enough comparative work to make that claim feel well grounded.

10. **There is no empirical or even synthetic sanity-check validation, which leaves the practical meaning of the assumptions and constants unexplored.**  
   I do not think every theory paper needs experiments, but this paper makes fairly implementation-flavored claims about query complexity, qubits, and gates, especially in **Table 1**. Given that, even a small-scale resource accounting, toy simulation, or worked-out application instantiation would have helped the reader understand whether the proposed subroutines are remotely plausible under finite precision and realistic parameter sizes. Without that, the work reads as a stack of oracle-model reductions with limited guidance on applicability.

## Questions
1. For the matrix case, can the authors reconcile the discrepancies among the abstract, **Table 2**, **Theorem 3**, **Theorem 4**, and the proofs in **Appendix B.9-B.11**? I would like a line-by-line clarification of the final dependence on $\sigma_1(M)$, $\sigma_2(M)$, $r$, $\varepsilon$, and $\gamma'_{\min}$ for both QTSVE and QPM. Right now I cannot tell which expression is the intended main result.

2. In **Algorithm 3** and **Algorithm 4**, is the step size on line 6 supposed to be $\gamma_t=\frac{2}{t+2}$ rather than $\frac{2}{\varepsilon+2}$? If so, please confirm that this is only a typographical error and that the pseudocode can be corrected globally. If not, the proof needs major revision.

3. For the nuclear norm linear minimization oracle, should the update direction be $S=-uv^\top$ rather than $S=uv^\top$? Please clarify the sign convention carefully and update the proofs around **Equations (91) to (97)** accordingly.

4. In the proof of **Lemma 3**, how should one account for the arithmetic cost of coherent real-number operations, especially constructing $\mathbf x+\sigma e_i$ and computing $\frac{f(\mathbf x+\sigma e_i)-f(\mathbf x)}{\sigma}$? The claim of $O(1)$ elementary gates seems too optimistic unless the computational model is stated very explicitly.

5. Can the authors make the connection to the approximate linear minimization condition in **Equation (5)** more explicit? In particular, please show exactly what $\delta$ is in terms of the finite-difference or tomography error for **Theorem 1**, **Theorem 3**, and **Theorem 4**.

6. For **Table 1**, some entries appear corrupted or dimensionally inconsistent, especially the latent-group row and some query-complexity expressions. Please provide a corrected version and explain the notation there, including whether the classical baseline row is accurate.

7. Could the authors discuss more honestly the regimes in which the matrix algorithms are actually better than strong classical baselines, after accounting for tomography and access-model assumptions? A short proposition or corollary stating the parameter regime for net asymptotic advantage in the main text would improve credibility.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
This is a theoretical paper on quantum algorithms for convex optimization. I do not see a specific ethics concern requiring escalation based on the main paper.

## Soundness Rating
2: fair. The vector-side analysis appears directionally reasonable, but the matrix-side technical inconsistencies, notation errors, and mismatched complexity statements materially reduce confidence in the paper’s central claims.

## Presentation Rating
2: fair. The paper has a coherent high-level structure and helpful summary tables, but the writing, notation, tables, and pseudocode contain enough errors that they impede technical evaluation.

## Contribution Rating
2: fair. The problem is interesting and some ideas are promising, especially the vector-domain quantum linear-subproblem view, but the contribution is weakened by strong assumptions, limited positioning, and lack of confidence in parts of the matrix analysis.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper asks a worthwhile question and has some promising ingredients, but in its current form I do not think the technical presentation is reliable enough, especially for the matrix results that carry much of the ambition.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. I carefully checked the main derivations and consistency of the stated theorem/table claims, and the main reasons for my score are concrete technical and presentation issues rather than subjective taste.
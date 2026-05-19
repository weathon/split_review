- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 5, 6
I've now thoroughly verified the key claims in both reviews against the paper. Let me synthesize the final consolidated review.

## Summary

This paper studies gradient descent on a quadratic reparametrization (diagonal linear network, $x = u \circ u$) for solving linear programs $\min c^\top x$ s.t. $Ax=b, x\ge 0$. The idea is to optimize the squared residual $\frac12\|A(u\circ u)-b\|^2$ and characterize the implicit bias of the dynamics. The paper provides: (i) a global linear convergence guarantee for discrete-time GD under mild assumptions (Theorem 4), (ii) a characterization of the discrete limit point as the solution of a perturbed entropy-regularized LP with a stepsize-dependent error term (Theorem 5), (iii) continuous-time analysis connecting initialization to regularization strength (Theorem 2), and (iv) connections to mirror descent and the Sinkhorn algorithm.

## Strengths

- **First rigorous global linear convergence for discrete-time GD on DLNs in the LP setting** (Theorem 4, Eq.~351--356). The paper proves $f(u^k) \le (1-\rho)^k f(u^0)$ under Assumption 1, which goes significantly beyond prior work that focused on gradient flow or the special case of basis pursuit.

- **Characterization of the discrete limit solution** (Theorem 5, Eq.~373--390). The paper identifies the limit point $x^\infty$ as the optimal solution of an entropy-regularized LP with an explicit error term proportional to the stepsize $\eta$. This provides a concrete understanding of how discretization affects the implicit bias.

- **Continuous-time limit connects initialization to regularization strength** (Theorem 2, Eq.~208--223). The gradient flow result shows that the limiting solution solves $\min \sum x_i\log(x_i/\alpha_i^2)-x_i$ s.t. $Ax=b$, and that choosing $\alpha_i = \exp(-c_i/(2\lambda))$ yields the entropy-regularized objective $c^\top x + \lambda\sum(x_i\log x_i - x_i)$.

- **Explicit stepsize rule guaranteeing monotonic decrease and positivity** (Lemma 1, Eq.~173--185). The condition $\eta_k \le \min\{1/(4\|A^\top r^k\|_\infty), 1/(5L\|u^k\|_\infty^2)\}$ is practical and implementable.

- **Boundedness of iterates established without level-set arguments** (Lemma 2, Eq.~324--336). The proof uses a decomposition over extreme points/rays of the polyhedron, which is nontrivial because level sets of $f$ can be unbounded.

- **Rigorous comparison to mirror descent and Sinkhorn** (Sections 3.2--3.3). The paper derives explicit update comparisons (Eq.~3.2 for mirror descent, Eq.~3.3 for Sinkhorn) and demonstrates via experiments that reparametrized GD differs from mirror descent under large stepsizes.

## Weaknesses

### Fatal
None.

### Major

- **The linear convergence rate depends on constants that are exponentially small in $n$, making it of theoretical interest only.** Theorem 4 guarantees linear convergence with $\rho = 2\mu\eta\sigma^2$, where $\sigma$ is a lower bound on $u^k$ (Lemma 7) derived via Lojasiewicz estimates. The Lojasiewicz exponent is $\tau = 8\cdot 9^{-(n-1)}$ (line~1298). For $n=1000$, $\tau \approx 10^{-954}$, and this enters the bounds that determine $\sigma$ through Corollary 2 and Lemma 7. The paper acknowledges the Lojasiewicz machinery but does not discuss the severity of the dependence on $n$, nor does it quantify $\sigma$ or $\rho$ even asymptotically. The rate is real but provides no practical computational guarantee for any moderate $n$.

### Minor

- **The big-M reduction for general LP is mentioned but not developed or validated.** Remark 2.1 (lines~96--115) sketches a reduction from general LP to the $c>0$ case via a big-M constraint, but requires knowing an upper bound $M$ on $1_n^\top z^*$ for an optimal solution. The paper states $M$ "can be easily computed for many applications" without guidance or examples. The paper's effective scope is LP with $c>0$ (as stated in line~34), which covers basis pursuit and optimal transport but not general LP. The abstract's "comprehensive framework" language overstates what is actually established.

- **The experimental validation is too narrow to support the paper's framing.** Only one synthetic instance ($m=300$, $n=3000$) with $c=1_n$ is tested, with comparisons limited to mirror descent and varying initialization scales. There is no comparison against standard LP solvers (simplex, interior point), no test on standard LP benchmarks, no evaluation on problems with a general cost vector $c$, and no empirical investigation of the discrete error term from Theorem 5. For a paper that introduces a "comprehensive framework for solving linear programming problems," this is insufficient. (To be clear, the experiments illustrate the theory acceptably for a theory paper; the mismatch is between the experiments and the framing.)

- **The limit characterization (Theorem 5) involves constants $C = C(A,b,R)$ and a vector $w$ that are defined implicitly through the dynamics and are not explicitly computable.** The $C$ depends on $K, c, \tau, \delta$ — all implicit constants from earlier lemmas — and $w$ is defined via the limit quantities (Eq.~1157--1158). While this is standard for asymptotic characterization results (the key insight is that the error term is $O(\eta\log(1/\underline\alpha))$ and vanishes as $\eta\to0$), the result is qualitative rather than quantitatively predictive.

### Trivial

- The "unprecedented achievement" and "comprehensive framework" language in the abstract (lines~4,~39) is hyperbolic for a paper whose theorems have constant-dependent guarantees and whose scope is LP with $c>0$ plus an underdeveloped big-M reduction.

## Nice-to-Haves

- An explicit (even loose) bound on $\sigma$ or $\rho$ in terms of $A,b,n$, and the initialization, to make the convergence result quantitatively grounded rather than an existence statement.
- A small experiment on a problem with general $c$ (via the big-M reduction) to demonstrate that the reduction is implementable.
- A discussion of how the method relates to practical LP solvers (simplex, interior point) in terms of accuracy and iteration count.

## Removed Points

- *"The gradient flow result relies on an unproven assumption about the existence of the limit of the integrated residual."* The paper explicitly states this assumption (line~209) and immediately acknowledges (lines~226--227) that it "has not been properly justified by a rigorous analysis" and that the discrete-time analysis addresses this gap. The critic's framing as a significant gap ignores the paper's own caveat and its discrete-time remedy.
- *"No comparison with standard LP algorithms."* The paper is primarily theoretical; experiments are meant as proof-of-concept illustrations. While a comparison would strengthen the paper, its absence is not a flaw given the paper's theoretical nature.
- *"Proofs are presented in the main paper body."* The parser strips appendices. The proofs exist in the original submission and their placement is a formatting choice, not a flaw.
- *Various formatting and reproducibility nitpicks* (stepsizes, numerical stability, missing stopping criteria): These are either addressed by the paper's explicit stepsize rule, standard for theoretical work, or reflect parser artifacts.

## Novel Insights

None beyond the paper's own contributions. The two reviews confirm the paper's technical contributions without adding new interpretative insight.

## Suggestions

1. **Recalibrate the narrative.** The paper is a theoretical study of implicit bias in DLNs for LP with $c>0$ — this is already a solid contribution. Remove or soften the "unprecedented achievement" and "comprehensive framework" language; frame the big-M reduction as an observation about theoretical reducibility rather than a practical solution.

2. **Discuss the constant dependence explicitly.** Add a paragraph acknowledging that $\tau = 8\cdot 9^{-(n-1)}$ makes the linear rate of mainly theoretical interest, and explain that the key novelty is establishing the *existence* of a linear rate (and the structure of the limit) rather than providing a practical algorithm.

3. **Strengthen the experiments modestly.** Add one or two additional instances (e.g., a problem with a general cost vector using the big-M trick, or a standard LP from a benchmark set like Netlib). This would not require extensive computational resources but would significantly improve the support for the paper's claims.

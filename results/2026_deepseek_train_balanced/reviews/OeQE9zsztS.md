## Summary

This paper revisits spectrally transformed kernel regression (STKR) and provides three contributions: (1) a characterization theorem (Theorem 1) showing that target smoothness satisfying a "preserves relative multiscale smoothness" condition can be realized by an STK with a monotonic transformation; (2) the first scalable inductive STKR implementations (STKR-Prop) with closed-form predictors and explicit complexity guarantees, moving beyond prior transductive-only or optimization-per-test-point approaches; and (3) statistical learning bounds for both the transform-aware and transform-agnostic settings, with technical improvements over prior work by Zhai et al. (2023).

## Strengths

- **First closed-form inductive STKR with concrete algorithms and complexity analysis**: Prior inductive approaches required solving an optimization problem per test point (Chapelle et al., 2002) or per set of test points (Chapelle et al., 2006). This paper provides Algorithms 1–2 (lines 362–396) with closed-form predictors: $\hat{f}(x) = \vv_{\hat{K}_s,n}(x)^\top \hat{\valpha}$ with $\hat{\valpha} = (\mathbf{G}_{\hat{K}_s, n} + n\beta_n \mathbf{I}_n)^{-1} \vy$. The time complexity is $\tilde{O}(q(n+m)^2 \beta_n^{-1})$ for dense and $\tilde{O}(q|E|\beta_n^{-1})$ for sparse graphs — matching label propagation speed. This is a concrete algorithmic advance.

- **Theorem 1 provides a structural characterization of target smoothness**: The theorem (lines 196–206) proves that any smoothness notion preserving relative multiscale smoothness (i.e., respecting the ordering induced by $r_{K^p}$ across all $p \ge 1$) and contained in $\mathcal{H}_K$ can be represented as an STK with a monotonic, bounded transformation $s(\lambda)$. While the premise is abstract, the result that the transformation must be monotonic and $s(\lambda) = O(\lambda)$ is non-trivial and provides formal grounding for the STK approach.

- **Statistical guarantees with concrete improvements over prior work**: Theorems 2 and 4 provide finite-sample bounds achieving minimax optimal rates $O(n^{-1/(1+p)})$. Theorem 5 provides approximation error bounds where the deviation is $O(\sqrt{d/m})$ rather than $O(d/m)$ as in Zhai et al. (2023), and removes dependence on eigenfunction delocalization and $\lambda_d^{-1}$ (lines 526–531, items (b)(i)–(iii)). These are clearly stated, verifiable improvements.

- **Proposition 1 gives an interpretable geometric characterization**: The result that $\overline{\text{Lip}}_{d_{K^p}}(f) = \|f\|_{\mathcal{H}_{K^p}}$ (line 176) connects the abstract RKHS norm to an extended Lipschitz constant over measures, providing intuition for the smoothness that STKR enforces.

## Weaknesses

### Fatal
None.

### Major

1. **Theorem 1 is an abstract characterization whose premise lacks actionable connection to practice**: The theorem's central condition — "preserves relative multiscale smoothness" (if $r_{K^p}(f_1) \ge r_{K^p}(f_2)$ for all $p \ge 1$, then $r_t(f_1) \ge r_t(f_2)$) — is a formal property that the paper does not connect to concrete or verifiable smoothness classes. The paper provides no examples of natural smoothness classes that satisfy this premise, nor counterexamples that violate it. This limits the theorem's role from "actionable guidance about what target smoothness is" (as the framing suggests) to a structural consistency result. The paper's framing (abstract: "proving that any sufficiently smooth function can be learned by STKR"; introduction: "elevating STKR to be a principled and general way") overstates what the theorem delivers given the gap between its premise and practical verification.

2. **The estimation bound expression for Theorem 2 is absent from the main text**: Line 295 is a blank equation environment (`\begin{equation*} ... \end{equation*}`) — the actual bound is deferred entirely to the appendix. The main text only states the rate $O(n^{-1/(1+p)})$ in the remark. For a paper whose third contribution is "proving nonparametric statistical learning bounds," the reader needs to see the actual bound expression to assess its quality (constants, dependencies, ranges of validity). This is distinct from proofs being deferred; the *statement* itself is missing.

### Minor

3. **The approximation error bound requires $m$ to be polynomially larger than $n$ to close the gap, which undercuts the practical narrative**: For the bound in Theorem 3 to vanish, $m = \omega(n^{4/(1+p)})$ is required (line 320). For $p=1$ this is $m = \omega(n^2)$; for the minimax-optimal $p=0.5$, this is $m = \omega(n^{8/3})$. The paper acknowledges this (Remark 3.1), and it is not a fatal flaw since unlabeled data is often abundant in semi-supervised learning. However, the introduction's framing ("unlabeled data can provide additional information" without qualification) oversimplifies what the theory actually shows — that the *theoretical* benefit is asymptotic and requires the unlabeled pool to dominate the labeled one by a polynomial margin.

4. **Experimental validation is too limited to substantiate the algorithmic claims**: The main text reports results on only 3 datasets (Computers, Cora, DBLP) with comparisons only to Label-Prop and KRR. No comparisons are made to modern approaches (graph neural networks, modern graph kernels, or representation learning methods), despite the paper's introduction motivating STKR through connections to contrastive learning and modern SSL. The standard deviations are large relative to accuracy differences (e.g., on Cora: SP-Lap (t) at $77.04 \pm 5.74$ vs. LP (t) at $73.33 \pm 6.00$), making it unclear whether improvements are significant. The paper acknowledges this ("a more extensive empirical study on STKR is desired" in limitations) but the experiments presented are insufficient to demonstrate practical value beyond proof-of-concept.

5. **The framing overstates the connection to modern representation learning while the methods do not apply to that setting**: The introduction (lines 21–33) motivates STKR through spectral contrastive learning and frames STKR as a general framework for understanding representation learning. However, the limitations section (lines 593–595) acknowledges that in contrastive learning, "computing $K$ is hard but computing $\|f\|_{\mathcal{H}_K}^2$ is easy, so our methods need to be modified accordingly." This means the paper's algorithms do not apply to the very setting used to motivate their relevance. The motivation and the actual contribution are misaligned.

### Trivial
- The bound in Theorem 2 (estimation) is stated only via its rate in the main text; the explicit bound expression is deferred to the appendix (blank equation at line 295).
- No guidance is given on how to choose the kernel PCA dimension $d$ or the transformation $s(\lambda)$ beyond the inverse Laplacian default.

## Nice-to-Haves
- Provide concrete examples and counterexamples for the premise of Theorem 1 to make it practically interpretable.
- Include an experiment varying the $n:m$ ratio to directly test the theory's prediction that the STKR advantage grows with the unlabeled-to-labeled ratio.
- Discuss hyperparameter selection for $s(\lambda)$ and $d$ more explicitly for practitioners.

## Removed Points
- The harsh critic's claim that the bound expression is blank at line 312 is **incorrect** — line 312 contains a full non-trivial bound expression. This point is removed.
- The critic's assertion that Theorem 2 has "blank equations in lines 295 **and** 312" is partially incorrect; only line 295 is blank. The criticism is kept but corrected (moved to Trivial).
- The critic's framing that the m ≫ n requirement is an "evidential issue" that the paper "oversimplifies" is weakened: the paper acknowledges this transparently in Remark 3.1, making it a minor issue rather than a major one.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
- Add the explicit bound expression for Theorem 2 to the main text (or a representative simplified version), so readers can inspect constants and dependencies without consulting the appendix.
- Reframe the introduction to align more carefully with what the theory and algorithms actually deliver, separating the formal characterization (Theorem 1) from the practical guidance it provides.
- Add a small-scale experiment that varies the $n:m$ ratio on one dataset to connect the theoretical approximation bound to observable behavior.

## Score and Decision
This is a solid theoretical paper with a genuine algorithmic contribution — the first closed-form inductive STKR with complexity analysis — and statistical guarantees that improve on prior work. The theory is the main contribution and is technically sound. However, the paper is weakened by (1) a gap between the abstract premise of Theorem 1 and its advertised practical scope, (2) an estimation bound statement deferred to the appendix, (3) thin experimental evidence given the algorithmic claims, and (4) a framing mismatch between the motivation (modern representation learning) and the methods (which do not apply there). These are not fatal but collectively prevent the paper from being a clear accept at a top venue. With reasonable revisions — particularly adding the missing bound expression to the main text and calibrating the framing — the paper could merit acceptance.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
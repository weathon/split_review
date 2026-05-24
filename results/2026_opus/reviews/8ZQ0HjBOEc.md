Now I have enough calibration to write the final review.

## Summary
The paper studies the NTK of infinite-width fully-connected ReLU networks as depth $L\to\infty$ in the regime $L = o(\min_l n_l)$. It proves (Theorem 2 / Proposition 4) that the normalized limiting kernel $\bar\Theta_\infty^{(L)}$ converges monotonically to the all-ones matrix, and claims (Theorem 3) that despite this singular limit, the kernel-regression closed-form predictor $\kappa_x^\top\kappa^{-1}$ admits a limit, established via Lyons' Universal Limit Theorem on a constructed rough differential equation. Section 6 distills three abstract criteria a kernel sequence must satisfy for this behavior and illustrates convergence rates empirically.

## Strengths
- **Singular-kernel regime framing.** Unlike Xiao et al. (2020), whose proof in the ordered phase requires the limiting kernel to decompose as a constant plus a non-singular term, this paper addresses the regime where $\bar\Theta_\infty^{(L)}(XX^\top)$ becomes singular (line 231 makes the distinction explicitly). Even at the level of *existence* of a closed-form limit, this is a non-trivial gap to address.
- **Monotonic convergence of $\bar\Theta_\infty^{(L)}\to\mathbf{1}\mathbf{1}^\top$ via an explicit recursion.** Proposition 4 gives a clean closed-form recursion $\bar\Theta_\infty^{(L+1)} = \tfrac{L}{L+1} h'(\rho^{(L)})\bar\Theta_\infty^{(L)} + \tfrac{1}{L+1} h(\rho^{(L)})$, and Theorem 2 extracts the strict-monotone limit. The recursion is genuinely new content even if the limit itself is morally implied by $\rho^{(L)}\to 1$.
- **Abstract criteria for generalizing the result.** Section 6 lists three minimal kernel-sequence conditions (diagonal dominance, eventual positive definiteness, vanishing normalized determinant) and demonstrates them on an alternative kernel $\eta^{(L)}$ with $h(z)=(1+e^{-z})^{-2}$. This is a useful abstraction beyond the specific ReLU NTK.
- **Empirical illustration of differential convergence rates.** Figure 1 makes clear that the *predictor* $\bar\kappa_x\bar\kappa^{-1}$ stabilizes much faster than the underlying kernel entries — consistent with the proof's observation that the rough-path drivers vanish exponentially faster than the kernel determinants.

## Weaknesses

### Fatal
None. The most damaging concern (Theorem 3 not actually identifying the limit, see Major below) is serious but not fatal: it threatens the strength of the headline claim, not the paper's existence as a contribution.

### Major
- **Theorem 3 establishes boundedness/continuity but does not identify the limiting function.** The abstract advertises that the closed-form solution "approaches a fixed limit on the sphere." Reading the proof on pp. 7–8: the rough drivers $v_{(i,j)}$ are by construction driven to 0 in 1-variation (line 229), so Lyons' Universal Limit Theorem delivers convergence of the solution to a constant *along the interpolation in $t$* — i.e., the limiting RDE is $du=0$ and "$u_\infty(t)$ is a constant dependent on $i$ and $x$." But the constant value is left as $u_\infty(0) = \lim_L (\bar\Theta_\infty^{(L)}(XX^\top))^{-1}\bar\Theta_\infty^{(L)}(x^\top X)$, which is the very quantity the theorem is meant to characterize. The stated bound $\bar\Theta_\infty^{(L)}(x^\top X)(\bar\Theta_\infty^{(L)}(XX^\top))^{-1} < C(x)\mathbf{1}_n^\top$ together with continuity of $C$ on $S^{n_0-1}$ gives a bounded continuous family, not a uniquely identified limit. The interpolation identity at training points ($u_\infty(x_i)=e_i$) is trivially inherited from any finite $L$ at which $\kappa$ is invertible. The paper would be substantially stronger if it (a) gave an explicit formula or variational characterization of $\lim \kappa_x^\top\kappa^{-1}$ as a function of $x$, plausibly via a direct asymptotic expansion $\bar\Theta_\infty^{(L)}(XX^\top)=\mathbf{1}\mathbf{1}^\top - \epsilon_L M_L + o(\epsilon_L)$ and a Sherman–Morrison / pseudoinverse argument, or (b) demonstrated where such a direct argument fails and the rough-path machinery is indispensable.
- **Use of $\psi_D$ when $D\to 0$ is not addressed in the proof.** The interpolation $\psi_D(2t-1)$ uses $D = \det\bar\Theta_\infty^{(L+1)}\cdot\det\bar\Theta_\infty^{(L)}$, both of which tend to 0 as $L\to\infty$. By Definition 6 / Proposition 5, $\psi_d$ degenerates to a step function at $z=0$ in this limit. The proof relies on smoothness of $\psi_D$ to get bounded variation of the drivers (line 229), but never quantifies the interaction between the shrinking $D$ and the smoothness budget. This is the load-bearing analytic point of the construction and is not addressed.

### Minor
- **Theorem 2 is largely a rescaling of Lemma 1.** Given Lemma 1 ($\rho^{(L)}\to 1$) — itself a re-derivation of well-known behavior — Theorem 2 follows essentially by combining Proposition 1's scaling ($\Theta_\infty^{(L)}(x,x)\sim L/(n_0 2^{L-1})$ for ReLU and $\rho=1$) with the convergence of off-diagonal terms. The genuinely new content of §5 is therefore Proposition 4's explicit recursion plus the (logarithmic) convergence rate noted at the end of §6. The paper would be more transparent if it framed Theorem 2 this way rather than as a separate result.
- **No comparison of the limiting predictor to trained networks.** Figure 1 shows that $\bar\kappa_x\bar\kappa^{-1}$ stabilizes, but never compares the stabilized object to the predictions of an actual finite-width, finite-depth ReLU network trained by gradient descent. Since the motivating story is "what wide deep networks compute," at least one such verification on a small dataset would convert the analysis from a kernel-internal observation into a claim about networks.
- **The "small determinants indicate fast convergence" hypothesis is asserted but not quantitatively verified.** §6 introduces this hypothesis ("we hypothesize that small determinants indicate fast convergence to the limiting solution"), points to Figure 2 in the appendix, but does not produce a controlled comparison (e.g., regressing predictor-convergence rate against determinant magnitude across kernel sequences). The hypothesis is at the same time the practical takeaway and the least well-supported empirical claim.
- **Eq. (5) notation.** The Cramer's-rule expression uses an outer sum over $j$ with a column swap $A\leftrightarrow_{i,j} Z_A$, while the LHS has only the index $i$. This is technically interpretable (the $j$-th column of $Z_A$ supplies the swap), but the convention is unusual enough that explicit elaboration would help the reader verify the algebra.
- **Tension between $\det\kappa\to 0$ and use of $\kappa^{-1}$.** Proposition 3 requires $\kappa$ invertible; the entire downstream analysis sits at the boundary of that requirement. The paper acknowledges this conceptually but does not quantitatively address conditioning of $\kappa$ at finite $L$ — yet the §6 hypothesis above is essentially a conditioning statement.

### Trivial
- The $\eta^{(L)}$ example in §6 with $h(z)=(1+e^{-z})^{-2}$ is not motivated by an architecture or activation; it reads as constructed to demonstrate that the criteria can be met rather than to illuminate a natural kernel family. Tying it to a network architecture would strengthen its motivation.

## Nice-to-Haves
- Pin down whether the rough-path machinery is genuinely required versus a direct perturbative expansion of $\bar\Theta_\infty^{(L)}$ around $\mathbf{1}\mathbf{1}^\top$, and if the latter suffices, use it — it would yield an *explicit* limit rather than a constant identified by the original quantity.
- A single end-to-end experiment training fully-connected ReLU MLPs of increasing depth at large but finite width and showing test predictions converging to the candidate limiting predictor.
- An explicit logarithmic-rate statement in the main text, not just in §6's text gloss.

## Removed Points
These points are flagged to be removed; treat them with caution.

- *(Harsh critic: Theorem 3 proof has a stray $Z_b$ term that is zero by construction, making the "interpolation" only one-sided.)* This is a presentation point about an algebraically-zero term in Eq. (5), not a correctness issue. Removed as redundant with the main Major weakness.
- *(Harsh critic: typo in the Conclusion — "while convergence for the limiting kernel is sublinear, the convergence for the limiting kernel is experimentally fast" — the second occurrence should plausibly be "limiting solution.")* Formatting/typo class — removed per house rules.
- *(Harsh critic: the contribution shrinks against Bietti & Bach (2021) / Li et al. (2024) / Seleznova & Kutyniok (2022).)* The paper acknowledges these in §6 and positions itself against them reasonably; the framing is fair. Demoted to the Minor "Theorem 2 is largely a rescaling" point.
- *(Strength Finder: Theorem 3 establishes convergence of the closed-form NTK solution without requiring kernel invertibility.)* Conflicts with the verified Major weakness — what Theorem 3 establishes is boundedness/continuity, not a uniquely identified limit. Removed as a strength.

## Novel Insights
None beyond the paper's own contributions. The framing that a kernel sequence can become singular while a kernel-regression predictor on it remains well-defined is a genuine subtlety, but the paper's argument as written does not pin down what the predictor converges *to*, so the insight remains potential rather than realized.

## Suggestions
- Replace (or supplement) the rough-path proof of Theorem 3 with a direct asymptotic expansion: write $\bar\Theta_\infty^{(L)}(XX^\top)=\mathbf{1}\mathbf{1}^\top - \epsilon_L M_L + o(\epsilon_L)$ using Proposition 4's recursion, then invert perturbatively (Sherman–Morrison / pseudoinverse on $\mathbf{1}\mathbf{1}^\top$) to *identify* the limit explicitly as a function of $x$. This would let the paper say what the limiting predictor *is*, not just that it is bounded.
- Add one experiment training fully-connected ReLU MLPs of width $\geq 1024$ and varying depth on a small dataset, and overlay their test predictions against the candidate limiting predictor.
- Move Lemma 1 / Theorem 2 / Proposition 4 into a single proposition labeled as "structure of $\bar\Theta_\infty^{(L)}$" and isolate the genuinely new claim (the recursion and logarithmic rate) — this would make the paper's marginal contribution over prior work much more transparent.
- Quantify the "small determinants $\Rightarrow$ fast predictor convergence" hypothesis with a controlled sweep across the kernels $\Theta_\infty, \rho, \eta$ and report a quantitative relationship.
- Clarify in the proof of Theorem 3 the interaction between $D \to 0$ and the smoothness of $\psi_D$ — specifically that the 1-variation of the drivers really does vanish in this limit and is not artificially controlled by the rate at which $D\to 0$.

## Evaluation on the requested axes
- **Originality:** Moderate. The combination of rough-path machinery with the NTK depth limit is novel, but the underlying observation that $\rho\to 1$ and the kernel becomes singular is already in Bietti & Bach (2021), Seleznova & Kutyniok (2022), and (in a different regime) Hanin & Nica (2020).
- **Importance of the research question:** Real. Characterizing the deterministic kernel in the $L = o(n)$ regime is a genuine gap between the deterministic (Jacot et al.) and stochastic (Hanin & Nica) regimes.
- **Whether claims are well supported:** Partially. Theorem 2 is well supported; Theorem 3's claim of a "fixed limit" overstates what the proof delivers.
- **Soundness of experiments:** Limited. The experiments confirm kernel-level convergence but do not connect to trained networks.
- **Clarity of writing:** Fair. The setup and notation are careful; the proof of Theorem 3 — the load-bearing section — is hard to follow and does not address the subtleties it depends on.
- **Value to the research community:** Modest. If the limit were identified explicitly, this would be a meaningful step in understanding depth in the kernel regime. As written, the value is closer to "confirms existence/boundedness in the singular case."

## Calibration
Round-1 anchors:
- `2NwHLAffZZ.md` (avg 2.33, Reject) — weak NTK linearization paper; this paper is clearly above.
- `fUz6Qefe5z.md` (avg 3.00, Reject) — derivative-label NTK; this paper is above.
- `KNQJtoPZmz.md` (avg 3.00, Reject) — simplicity bias; this paper is above.
- `NbbsRnPBoS.md` (avg 2.33, Reject) — deep linear depth speedup; this paper is above.
- `5EtSvYUU0v.md` (avg 6.00, Reject) — NTK/NNGP unification; this paper is somewhat below (less ambitious, with proof problems).
- `WH9NhxOeu9.md` (avg 5.00, Reject) — sharp generalization for two-layer NNs; comparable in flavor.
- `GqI4fTVUXC.md` (avg 6.00, Reject) — disconnect between theory and practice; broader scope than this paper.
- `VEJzjAvaIy.md` (avg 5.75, Accept) — divergence of NTK in classification; comparable structurally (clean theoretical result, modest novelty).
- `AoraWUmpLU.md` (avg 8.00, Accept) — activation functions in Neural ODEs; this paper is well below.
- `STUGfUz8ob.md` (avg 7.60, Accept) — transformers reasoning; off topic, this paper is below.
- `fMTPkDEhLQ.md` / `sbG8qhMjkZ.md` (avg 8.00, Accept) — off topic / much stronger.

Round-1 bracket: **3.5–5.5** (between weak-rejects and mid-band NTK theory).

Round-2 anchors:
- `kOtFuzoA93.md` (avg 4.00, Reject) — NTK Rademacher bounds beyond overparameterization; comparable level of theoretical contribution with marginal practical implication.
- `3LLkES6nNs.md` (avg 4.25, Reject) — infinitely deep ResNets as GPs; very similar topic (depth limit), reviewers found the contribution narrow.
- `YN4uWzcbtt.md` (avg 4.25, Reject) — positive definiteness of NTK; **closest comparable** — incremental but clean NTK result, reviewers flagged limited practical implication and overlap with prior work; I read this in detail.
- `O6znYvxC1U.md` (avg 6.33, Accept) — sublinear-width BNN spectrum; more ambitious, accepted, stronger anchor.
- `1Wi0Ys33Nm.md` (avg 6.25, Accept) — beyond IID weights GP equivalence; more breadth, accepted.

The paper-under-review sits near `YN4uWzcbtt.md` (4.25) and `3LLkES6nNs.md` (4.25) — incremental theoretical NTK contributions with real but contained novelty — but slightly *below* them because Theorem 3, the headline result, has a verified Major problem (the limit is not actually identified by the proof). It is clearly below `VEJzjAvaIy.md` (5.75, Accept), which delivers a clean unambiguous theorem. Final score 4.0.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>
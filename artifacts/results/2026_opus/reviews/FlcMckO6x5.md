Now I'll perform calibration retrieval to anchor the score.Now I have enough calibration data. Let me write the final review.

Round 1 bracket: The two closest topical anchors are TNYLCF7vZA (4.75, Reject — Shi et al. INR spectral bias, the directly-cited preconditioning baseline) and 2C3CWCPxNS (5.00, Reject — PINN preconditioning). The strong-anchor band returns nothing topically similar. Initial bracket: 4 to 6.

Round 2 placed the paper near 2C3CWCPxNS (5.00) and TNYLCF7vZA (4.75) — both reject with mixed reviews. The present paper has somewhat broader theoretical scaffolding (universal approximation + NTK regime + algorithm) than either, but inherits the same "provably alleviates spectral bias" framing weakness as Shi et al. (2025), and explicitly leaves the D>2 multivariate equivalence unproven. Final placement: just above both anchors at ~5.0.

---

## Summary
The paper provides three theoretical-algorithmic contributions for separable neural networks (SepNNs): (i) a universal approximation theorem for CP, TT, and Tucker SepNNs; (ii) NTK regime results showing the SepNN NTK converges to a deterministic kernel under infinite width and rank and to a random kernel under fixed rank; and (iii) a separable preconditioned gradient descent (SepPGD) with $\mathcal{O}(nD)$ per-iteration complexity on $n^D$ grid points, supported by KRR, INR, and PINN experiments.

## Strengths
- **Genuinely useful algorithmic contribution.** SepPGD's Kronecker-structured preconditioner with $\mathcal{O}(nD)$ application cost vs $\mathcal{O}(n^D)$ for Geifman et al. (Table 1) is a real efficiency win for grid-based training, and the construction cost $\mathcal{O}(D(n^3+n^2P))$ vs $\mathcal{O}(n^{3D}+n^{2D}P)$ is a clean win as well.
- **Clean $D=2$ equivalence (Lemma 2).** SepPGD with factor preconditioners $\{S_d\}$ is shown to be equivalent to classical NTK-PGD with the Kronecker-sum preconditioner $\tilde{S}=S_1\otimes I_n + I_n\otimes S_2$ — this provides a concrete theoretical anchor for what SepPGD is doing rather than just an empirical heuristic.
- **Unified universal approximation across CP, TT, Tucker.** Theorem 1 extends Cho et al. (2023)'s bivariate CP result to multivariate CP, TT, and Tucker using a Stone–Weierstrass + vector-valued UAT route. The proof itself is textbook, but the unification has value.
- **NTK characterization in two asymptotic regimes.** Theorem 2 (deterministic NTK at $W,R\to\infty$) and Corollary 1 (random NTK at $W\to\infty$, fixed $R$) with the explicit factor-NTK formula in Lemma 1, empirically verified across multiple subplots in Fig. 1.
- **Empirical breadth.** SepPGD is tested on KRR, image INR, surface INR (IoU 0.992 vs 0.983), and 3D diffusion / Klein-Gordon / Helmholtz PINNs (Figs. 2–4), with consistent wall-clock improvements.

## Weaknesses

### Fatal
None. The criticisms below dent specific claims but do not invalidate the core SepPGD contribution or the NTK characterization.

### Major
- **The "provably adjusts the eigenvalue distribution" headline is not formally proven.** Section 4's spectrum argument (the paragraph after Lemma 2) is qualitative: "Suppose that $\tilde{K}$ is close to the true NTK matrix $K$ (which can be verified using…)", "We can ultimately show that $K\tilde{S}$ has better spectrum than $K$", and "It is believed that the result in Lemma 2 (and the analysis following) can be readily extended to multivariate cases $D>2$." There is no formal condition-number bound on $K\tilde{S}$, no error bound for $\|K-\tilde{K}\|$ in terms of the cross-factor weighting $a_d(x)$ from Lemma 1, and the chain "$S_d$ better-spectrum-than $K_{\Theta_d}$ $\Rightarrow$ $\tilde{S}$ better than $\tilde{K}$ $\Rightarrow$ $K\tilde{S}$ better than $K$" relies on the unproven approximation $K\approx\tilde{K}$. Given that this is one of the three pillars advertised in the abstract, the abstract overstates what the body delivers.
- **Multivariate generalization of Lemma 2 is asserted, not proven.** Lemma 2 covers only $D=2$. For $D>2$ the paper writes "It is believed that the result in Lemma 2… can be readily extended." Since the SepPGD definition (7)–(8) is genuinely intricate for general $D$ (mode-$d$ products, outer products of factor outputs, unfoldings) and the proposed non-grid form $\tilde{S}=\sum_d S_d$ does not transparently generalize the Kronecker-sum structure, the only case in which the reader can verify what SepPGD is doing is $D=2$ — yet the headline applications (3D PINNs, image stacks, surface fields) are higher-$D$.
- **Theory regime vs deployment regime.** Theorem 2 requires $W,R\to\infty$ jointly. Corollary 1 admits that at practical (small) $R$ the NTK is random, and Remark 3 says training dynamics "can not be characterized uniformly using a fixed NTK matrix… due to the randomness." Yet the literature the paper itself cites (Liang et al. 2022; Luo et al. 2024) deploys SepNNs at low $R$ for generalization. The fixed-NTK spectral-bias argument that motivates SepPGD therefore does not strictly apply in the regime SepPGD is actually used in. The paper concedes this and points to Appendix Table 3 as empirical justification, but the theory–method coupling is weaker than the framing suggests.

### Minor
- **Two-layer MLP restriction in Theorem 2.** The result is stated for $f_{\Theta_d}(x_d)=\tfrac{1}{\sqrt{W}}W_{2,d}\sigma(W_{1,d}x_d+b_d)$. Remark 1 says extension to multi-layer MLPs is "straightforward by utilizing the corresponding NTK formulations," but the multiplicative coupling between factor MLPs means depth-$L$ extensions are not strictly mechanical. The experiments empirically use deeper SepNNs without theoretical coverage.
- **Approximation theorem is incremental.** Theorem 1 is a Stone–Weierstrass + vector-valued UAT argument; Cho et al. (2023) covers the $D=2$ CP case and Yu et al. (2024) covers a closely related multivariate setting. Extending to TT/Tucker is largely mechanical. Reasonable as a unifying statement, but presenting it as one of three pillars overstates its weight.
- **Empirical results lack variance across seeds.** Numbers like PSNR 33.30 vs 26.48 (Fig. 3) and IoU 0.992 vs 0.983 are reported as points, and convergence curves in Figs. 2–4 do not display run-to-run variability. Even in benchmark-style domains, error bars on the headline gap would strengthen the claim.
- **The complexity table omits steps-to-target.** Table 1 compares per-iteration cost only. If $\tilde{S}=S_1\otimes I_n+I_n\otimes S_2$ is a strictly more constrained preconditioner than Geifman et al.'s unconstrained $S$, then a fair efficiency story is "$\mathcal{O}(nD)$ per step, possibly more steps" vs "$\mathcal{O}(n^D)$ per step." The wall-clock plots conflate these. (Lemma 2 says the two are equivalent at $D=2$ with a specific construction, but the comparison in Table 1 is not constrained to that choice.)
- **The construction-cost win is buried in Remark 4 / footnote 3.** $\mathcal{O}(D(n^3+n^2P))$ vs $\mathcal{O}(n^{3D}+n^{2D}P)$ is a cleaner story than the per-iteration application cost; it deserves elevation.

### Trivial
- Remark 2's $\mathcal{O}(1/\sqrt{R})$ and $\mathcal{O}(1/\sqrt{W})$ NTK-stays-fixed claim should explicitly account for the $D$-fold multiplicative product of factor outputs in SepNN, which can amplify weight movement compared to a single MLP.
- The Section 4 paragraph "We can ultimately show that…" reads as a proof sketch where a formal lemma would belong. Rewriting it as either a labelled proposition with assumptions or as an "informal claim" would make the gap between proof and intuition cleaner.

## Nice-to-Haves
- A formal proposition giving an explicit error bound for $\|K-\tilde{K}\|$ in terms of the cross-factor outputs $a_d(x)$ from Lemma 1, with dependence on $D$ and $R$.
- A multivariate extension of Lemma 2 with proof for CP / TT / Tucker, so that the algorithm at $D\geq 3$ has the same theoretical grounding as at $D=2$.
- A concentration-style probabilistic spectral-bias statement for the random-NTK Corollary 1, turning the fixed-rank regime into a theory–method connection rather than an empirical fallback.
- An ablation over $R\in\{2,4,8,16,32,64\}$ showing how SepPGD's effective acceleration depends on rank, since the deterministic-NTK theory only applies at large $R$.

## Removed Points
These points are flagged to be removed, treat them with caution.

- *Harsh critic: missing same-preconditioner control* — The harsh critic asks for a comparison of SepPGD against classical NTK-PGD with exactly $\tilde{S}=S_1\otimes I_n + I_n\otimes S_2$. Lemma 2 already proves these are mathematically equivalent at $D=2$; the per-iteration wall-clock comparison in Fig. 2 is exactly what is needed to demonstrate the efficiency claim. The ask conflates "is the preconditioner as good as unconstrained $S$" (a separate question) with the equivalence-vs-unconstrained comparison, and the paper does not claim the former.
- *Harsh critic: experiments restricted to one image / one surface / one PDE per main figure* — The main text shows representative cases; Appendix Section A.12 / Figs. 10, 13–14 contain additional results. Demanding broader empirical surface in main text is style preference rather than substantive flaw.
- *Strength: "interpretability and robustness from low-dimensional representations"* — generic motivational language not specifically demonstrated.

## Novel Insights
None beyond the paper's own contributions. The reviewers correctly identify that Lemma 2's Kronecker-sum equivalence is the conceptual hinge, and that the main weakness is the gap between this clean $D=2$ statement and the more general claims advertised in the abstract.

## Suggestions
- Either (a) prove a formal theorem on the spectrum of $K\tilde{S}$ with explicit assumptions and a quantitative bound, or (b) downgrade the abstract's "provably adjusts the eigenvalue distribution" to "empirically adjusts, with theoretical motivation in the $D=2$ case."
- Provide the multivariate equivalence proof for SepPGD at general $D$; without it, the algorithm's behavior for $D\geq 3$ rests on intuition.
- Promote the construction-cost analysis ($\mathcal{O}(D(n^3+n^2P))$ vs $\mathcal{O}(n^{3D}+n^{2D}P)$) from Remark 4 / footnote 3 into the main complexity discussion.
- Report mean ± std over at least 3–5 seeds for the headline PSNR / IoU / MSE numbers in Figs. 2–4.
- Add a small-$R$ ablation directly showing how SepPGD's acceleration scales with rank, since the theory is only deterministic at large $R$.

## Axes Evaluation
- **Originality:** Moderate. The structural insight (separability ⇒ Kronecker-sum preconditioner ⇒ $\mathcal{O}(nD)$) is genuinely novel as a clean composition; the universal approximation result is incremental.
- **Importance:** SepNNs are increasingly used in INRs / PINNs, and accelerating their training is a real concern in those communities.
- **Claim support:** The approximation theorem and NTK regime results are well supported. The headline "provably adjusts spectrum" claim is not delivered with a formal proof; the $D>2$ algorithmic equivalence is asserted.
- **Soundness of experiments:** Reasonable scope but no variance reporting; the comparisons that would isolate preconditioner-quality vs efficiency are missing.
- **Clarity:** The paper is reasonably organized; the spectrum-adjustment paragraph after Lemma 2 reads as proof sketch where a labelled claim belongs.
- **Value to community:** SepPGD as an algorithm with clean $D=2$ theory and credible empirical gains is publishable in some form. The theoretical scaffolding around it is more uneven than the framing suggests.

## Calibration Anchors
| Path | Round | Avg | Comparison |
|---|---|---|---|
| `kkVTeMvC9D.md` (Training Jacobian) | R1 weak | 3.40 | Less directly relevant; theory-only NTK paper |
| `xpmDc76RN2.md` (Operator Networks PDE) | R1 weak | 2.33 | Optimization-theoretic, weak experiments |
| `2NwHLAffZZ.md` (Weak correlations NTK) | R1 weak | 2.33 | More speculative, less applied |
| `fUz6Qefe5z.md` (NTK with derivative labels) | R1 weak | 3.00 | PINN-adjacent NTK extension; similar in spirit, weaker delivery |
| `TNYLCF7vZA.md` (Shi et al. INR preconditioning) | R1 mid | 4.75 | **Closest topical anchor** — the directly-cited Shi et al. (2025) baseline. Similar "modify NTK spectrum to alleviate bias" framing; rejected for unclear math and contribution gap with Geifman et al. The present paper extends this with SepNN-specific theory and a clean efficiency story. |
| `h7GAgbLSmC.md` (Sharper guarantees) | R1 mid | 7.00 | Stronger theory, less applied; not directly comparable |
| `YN4uWzcbtt.md` (NTK positive definiteness) | R1 mid | 4.25 | Narrower theoretical contribution |
| `PJjHILiQHC.md` (Spectral dynamics of weights) | R1 mid | 6.25 | Broader empirical scope; not directly comparable |
| `STUGfUz8ob.md`, `P7KIGdgW8S.md`, `AoraWUmpLU.md`, `4xWQS2z77v.md` | R1 strong | 7.60–8.00 | None are topically close to SepNN/preconditioning |
| `2C3CWCPxNS.md` (PINN preconditioning) | R2 | 5.00 | **Highly comparable** — preconditioning + theory + extensive PDE experiments; rejected with mixed reviews. Present paper has comparable scope and similar headline-vs-body gap. |
| `Oqk1Ui6m0n.md` (Hessian-free NGD for PINN) | R2 | 5.00 | Preconditioning for PINNs, more practical focus |
| `jqVj8vCQsT.md` (Neural solver for parametric PDE) | R2 | 5.60 | Accept; stronger empirical scope but less theoretical |
| `7Cx05z4pUc.md` (Decomposed learning) | R2 | 5.00 | Tensor-decomposition method, narrower scope |
| `kyVzYpDxHg.md` (Equivariant tensor functions) | R2 | 5.75 | Tensor structure but different problem |
| `UvpuGrd6ey.md` (DNN compositionality) | R2 | 6.25 | Stronger theory, less applied |
| `C85eSjKenO.md` (Tensor-GaLore) | R2 | 5.00 | Tensor decomposition optimization |
| `fAGEAEQvRr.md` (GD matrix factorization) | R2 | 5.50 | Theory-only |
| `Q0TEVKV2cp.md` (Debiasing mini-batch quadratics) | R2 | 6.75 | Stronger empirical methodology |

**Bracketing:** Round 1 placed the paper between the cluster of 3-range NTK theory rejects and the 7-range theory accepts. Round 2 anchors at 4.75 (TNYLCF7vZA — directly cited baseline, similar framing, similar headline-claim issue) and 5.00 (2C3CWCPxNS — preconditioning + theory + extensive PDE experiments) bracket it tightly. The present paper has more theoretical breadth than either (universal approximation + NTK regimes + algorithm), but inherits the same "provably alleviates spectral bias" framing weakness, and has an additional unique gap ($D=2$ Lemma 2 not generalized). Net: it lands marginally above both, at 5.0.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
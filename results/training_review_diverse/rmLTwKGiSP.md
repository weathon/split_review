Now I have a thorough understanding of the paper and can verify all claims against the text. Here is my consolidated review.

---

## Summary

This paper proposes the semi-anchored (SA) gradient method for nonconvex-nonconcave minimax problems, constructed via a Bregman proximal point (BPP) framework with a novel nonlinear Legendre function inspired by the PDHG preconditioner. Under the weak Minty variational inequality (MVI) condition, the paper establishes an O(1/k) convergence rate in a Bregman distance that upper-bounds the squared subgradient norm. Two variants are presented: SA-GDmax (with an exact maximization oracle) and SA-MGDA (with inner gradient steps for the max player). The paper is primarily a theoretical contribution with two numerical proof-of-concept experiments.

## Strengths

- **Novel extension of PDHG to nonconvex-nonconcave settings via BPP.** The construction of the Legendre function \(h(\mathbf{u},\mathbf{v}) = \frac{1}{2\tau}(\|\mathbf{u}\|^2 + \|\mathbf{v}\|^2) - \phi(\mathbf{u},\mathbf{v})\) (Section 5.1) directly nonlinearizes the PDHG preconditioner, yielding the semi-anchored gradient method. Table 1 clearly documents that SA-GDmax converges under the weak MVI condition, whereas prior PDHG-type and GDmax-type methods require stronger assumptions (convex-concave or strong concavity). This is a well-defined advance.

- **New optimality measure yielding an O(1/k) rate that upper-bounds the squared gradient norm.** The paper introduces \(D_h(\mathbf{x}_i, \mathbf{x}_{i-1})\) as an optimality measure (Equation 6) and proves in Theorem 3 that \(\min_{i} D_h(\mathbf{x}_i,\mathbf{x}_{i-1}) \leq \frac{D_h(\mathbf{x}_*,\mathbf{x}_0)}{(1-\rho(1/\tau+L))k}\) and that this quantity upper-bounds \(\frac{\|\mathbf{s}_i\|^2}{2(1/\tau+L)}\). The paper identifies (Section 5.1) that such an optimality measure has not been observed previously in minimax optimization.

- **Inexact variant (SA-MGDA) with provable convergence guarantees.** Algorithm 1 and Theorem 5 provide a version that replaces the exact oracle with \(J = O(\log(\epsilon^{-1}))\) inner gradient steps, yielding total \(O(\epsilon^{-1}\log\epsilon^{-1})\) gradient complexity. This addresses the practical limitation of the exact-oracle assumption while preserving convergence under the weak MVI condition.

- **Empirical demonstration on two problems where SA-GDmax outperforms baselines.** On a toy problem satisfying weak MVI (Figure 1) and a fair classification task on Fashion MNIST (Figure 2), SA-GDmax achieves lower squared gradient norm and higher worst-category test accuracy compared to CEG+ and regularized GDmax across multiple settings.

## Weaknesses

### Fatal

None.

### Major

- **The practical variant (SA-MGDA) has strictly worse worst-case gradient complexity than extragradient methods.** SA-MGDA requires \(O(\epsilon^{-1}\log\epsilon^{-1})\) gradient computations, while EG+/CEG+ achieve \(O(\epsilon^{-1})\) without needing inner iterations. The paper acknowledges this (line 262: "up to a logarithmic factor") but does not provide evidence that this log factor is offset by constant improvements or that SA-MGDA is competitive in practice. Since EG+ is already a practical single-loop method and SA-MGDA is a multi-loop method with a worse asymptotic rate, the practical case for SA-MGDA over EG+ is not made.

- **The experiments test only SA-GDmax (exact oracle) and avoid the harder setting that the paper itself identifies as the key challenge.** Neither the toy example nor the fair classification task tests SA-MGDA. The fair classification problem has a trivial max-oracle (linear in \(\mathbf{v}\) over a simplex — the maximum is simply the maximum of three losses). The paper is transparent that it selects problems where the oracle is cheap (line 281), but this means the experiments do not demonstrate the method in the regime where its theoretical contribution would matter most — i.e., where the exact oracle is unavailable and SA-MGDA would be needed.

### Minor

- **The claim that SA-GDmax "can be superior to the extragradient in the worst case" (line 17) is not supported by a direct comparison of constants.** The paper shows both methods have \(O(1/k)\) rates, and that the SA-GDmax rate is on a Bregman distance that upper-bounds the squared gradient norm. The paper hedges with "can be" and "it is possible" (line 245), but the reasoning that a rate on a larger quantity implies better constants for the smaller quantity is not generally valid — it depends on problem-dependent constants in the Bregman distance \(D_h(\mathbf{x}_*,\mathbf{x}_0)\) versus \(\|\mathbf{x}_0-\mathbf{x}_*\|^2\) and step-size prefactors. No explicit comparison of constants or a constructive example is provided. This is a rhetorical overreach in an otherwise solid theoretical paper.

- **The paper does not provide a side-by-side comparison of the allowable \(\rho\) ranges for SA-GDmax versus EG+/CEG+.** Theorem 3 requires \(\rho < 1/(2L + \hat{L})\) (or \(\rho < 2/(2L + \hat{L})\) with projection). Without a direct comparison to the corresponding conditions for EG+/CEG+, the reader cannot assess whether the SA method covers a meaningfully different or narrower class of problems. This information is needed to substantiate the claim in Table 1 that the methods cover the same setting.

- **The fair classification experiment would benefit from an explicit statement of how the exact max oracle is implemented.** The objective is linear in \(\mathbf{v}\) over a simplex, so the maximization reduces to \(\max_i \mathcal{L}_i(\mathbf{u})\) — this is trivial but should be stated explicitly to avoid confusion about whether a nontrivial subproblem is being solved.

### Trivial

None of note (no formatting issues or typos that affect scientific content).

## Nice-to-Haves

- Provide a concrete example or problem family where the constant in the SA-GDmax bound is provably tighter than the EG+ bound, to substantiate the "can be superior" claim.
- Add at least one experiment comparing SA-MGDA (with finite \(J\)) to EG+/CEG+ on a problem where the inner maximization is nontrivial (e.g., a two-layer neural network game).
- Include a table comparing the allowable step-size / \(\rho\) ranges between SA-GDmax and EG+/CEG+ with the same notation.
- Provide a practical parameter selection heuristic, since the theoretical conditions involve unknown constants \(L, \hat{L}, \rho\).

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Complaints about missing proofs or appendix content.** The reviewer criticizes that Lemma 2's proof is "not in the main text (presumably in the appendix)" and that the paper "cannot be fully assessed without the proofs (which are presumably in the appendix)." These are removed per the rule that the parser strips appendix sections from all submissions; the proofs exist in the original submission.
- **Request for "a proof sketch for Lemma 2" and "a few lines of derivation."** Same rationale — these are appendix-deferred contents that exist in the original submission.
- **Claim that "the conclusion does not follow from the presented mathematics" with respect to worst-case superiority.** The paper uses the hedged phrasing "can be superior" and "it is possible that we have a gain" (lines 17, 245). While the paper would benefit from a more precise comparison, the claim as stated is not mathematically invalid — it identifies a possibility, not a proven fact. This point has been downgraded from the reviewer's framing as a fatal issue to a minor rhetorical concern in the main review.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Tone down the "can be superior" language** and replace it with a precise description of what is known: both methods have \(O(1/k)\) rates; the SA rate is on a measure that upper-bounds the squared gradient norm; a tighter bound is possible but not proven. This would make the paper more credible.
2. **Include at least one experiment with SA-MGDA** (finite \(J\)) on a problem where the inner maximization is nontrivial. Without this, readers cannot assess whether the inexact variant is practically viable.
3. **Add a direct comparison table** of the allowable \(\rho\) ranges and step-size conditions for SA-GDmax versus EG+/CEG+ to substantiate the claim in Table 1 that the setting is the same.
4. **Clarify the fair classification oracle implementation** to explain that the max over \(\mathbf{v}\) in a simplex reduces to picking the maximum of three loss values.

## Score and Decision

The paper presents a genuine theoretical contribution — a novel nonlinear extension of PDHG to nonconvex-nonconcave minimax via the Bregman proximal point framework — with clean derivations and sound theoretical analysis under the weak MVI condition. The main weaknesses are: (a) the practical variant has worse complexity than competing methods, (b) experiments test only the exact-oracle variant, and (c) a minor overclaim about worst-case superiority. These are real but not fatal. The core theoretical advance is valid and well-motivated. With revisions to address the overclaiming and ideally add SA-MGDA experiments, the paper would make a solid contribution.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
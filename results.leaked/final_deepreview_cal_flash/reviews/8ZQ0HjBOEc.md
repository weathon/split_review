Now I'll write the final consolidated review.

## Summary

This paper studies the behavior of the neural tangent kernel (NTK) for infinitely wide ReLU networks as depth grows. It makes two main claims: (1) the normalized NTK converges to the matrix of ones as depth increases (Theorem 2), and (2) despite this kernel collapse, the closed-form predictor expression $\tilde{\Theta}_\infty^{(L)}(x^\top X)^\top(\tilde{\Theta}_\infty^{(L)}(XX^\top))^{-1}$ converges to a bounded, data-dependent limit (Theorem 3), using rough differential equations to handle the singular limiting kernel.

## Strengths

- **Clean characterization of kernel convergence.** Theorem 2 and Proposition 4 together establish that the normalized NTK $\bar{\Theta}_\infty^{(L)}(x,x')$ strictly increases to 1 as $L\to\infty$ for points on the sphere. This is a precise and well-motivated result, and the proof (deferred to the appendix) follows from standard recursive formulas for the ReLU NTK.

- **Well-motivated problem.** The paper identifies a genuine tension: the kernel collapses to a constant matrix (so its determinant goes to zero), yet the predictor from kernel ridge regression may still converge to a meaningful limit. Resolving this tension is a worthwhile goal, and the application of rough path theory is a creative and novel approach in this context.

- **Clear delineation of regimes.** The paper explicitly contrasts its setting ($L\in o(\min_i n_i)$, deterministic limit) with the stochastic NTK regime of Hanin & Nica (2020) where depth grows faster than width. This helps clarify where the deterministic analysis applies.

- **Generalizable criteria.** Section 6 distills three properties (positive definiteness, diagonal dominance, vanishing determinant of the normalized kernel) that suffice for the same limiting behavior, providing a template for extending the results to other activation functions or architectures.

## Weaknesses

### Major

- **$\tilde{\Theta}$ is never defined.** Theorem 3 and its proof rely on $\tilde{\Theta}_\infty^{(L)}$ without any definition. The paper defines $\Theta_\infty^{(L)}$ (the NTK) and $\bar{\Theta}_\infty^{(L)}$ (the normalized version, Definition 4), but $\tilde{\Theta}_\infty^{(L)}$ appears for the first time in the statement of Theorem 3 (line 187) with no explanation of how it relates to either of these. This is a critical notational gap for a theoretical paper whose main result hangs on this quantity. A reader cannot tell whether $\tilde{\Theta}$ is the same as $\bar{\Theta}$ (the normalized kernel), a differently normalized version, or something else entirely. The proof's use of determinants and inequality chains is opaque without this definition.

- **The proof of Theorem 3 in the main text is a sketch that omits key logical steps.** While the paper relegates the rough-path background to Appendix D (which is standard), the core analytic argument presented in the main text is insufficient for evaluation. Specifically:
  - The inequality chain bounding $v_{ij}$ relies on the claim that $\det(A_n^{(L+1)}(t)) \ge \det(\tilde{\Theta}_\infty^{(L+1)})^{\psi_{\mathcal{D}}}\det(\tilde{\Theta}_\infty^{(L)})^{1-\psi_{\mathcal{D}}}$. This can be justified by the log-concavity of det on positive definite matrices, but the paper does not cite this fact or provide any reasoning. 
  - The justification for the second inequality ("the strictly positive determinants are all smaller than 1") is incomplete — it does not explain that $a^\psi b^{1-\psi} \ge ab$ for $a,b\in(0,1)$, which is needed to follow the direction of the inequality. (The inequality direction itself is *correct*; the critic who claimed it was reversed was mistaken. But the reasoning is not spelled out.)
  - The convergence of the driving terms $v_{ij}^{(L)}$ to zero in 1-variation is asserted without proof, and the application of Lyons' Universal Limit Theorem is stated rather than justified. For the paper's central theoretical result, this level of sketch is insufficient.
  
  *(Note: The harsh critic's specific claim that the inequality direction is "reversed" is factually wrong — as verified above, $a^\psi b^{1-\psi} \ge ab$ for $a,b\in(0,1)$ implies $\frac{\det(\dots)}{a^\psi b^{1-\psi}} \le \frac{\det(\dots)}{ab}$, which matches the paper's chain. This particular criticism is not valid. However, the broader concern about insufficient justification stands.)*

### Minor

- **Incomplete experimental validation.** Figure 1 does include a panel for the key quantity $\bar{\kappa}^{(l)}(x^\top X^\top)(\bar{\kappa}^{(l)}(XX^\top))^{-1}$ (third column), and this does appear to stabilize with depth. However, the paper provides no details on how the matrix inverse was computed — particularly important since the kernel approaches a constant matrix and becomes near-singular (was a pseudo-inverse used? regularization?). The discussion of the experiments focuses on the kernel entries themselves rather than the predictor expression that Theorem 3 is about. The convergence plots in the third column are visually suggestive but the paper does not quantitatively assess convergence or compare the limiting values to any theoretical prediction.

- **The proof sketch of Proposition 1 is confusing.** The line "$\mu = 0$ implies $x^\top x' \ge 0$ with probability $1/2$" appears garbled and does not clarify the computation. This is a minor point about a non-central result, but it contributes to an overall sense that the writing needs careful revision.

- **The relationship between $\tilde{\Theta}$ in Theorem 3 and the normalized kernel $\bar{\Theta}$ from earlier sections is unclear.** The theorem statement and the surrounding text (line 159) use $\Theta_\infty^{(L)}(x^\top X^\top)(\Theta_\infty^{(L)}(XX^\top))^{-1}$ (without tilde) when motivating the result, but the theorem itself switches to $\tilde{\Theta}$. This inconsistency makes it difficult to follow the logical flow even if one guesses that $\tilde{\Theta}$ is the normalized version.

- **The practical scope of Theorem 3 is limited.** The theorem shows that the predictor expression is *bounded* and that the driving rough path converges to zero, but does not characterize the limit or show that it is non-trivial (i.e., non-constant across $x$). The claim that the result "does not require any non-invertibility assumption as in Xiao et al. (2020)" is true in a technical sense, but the price paid is that the limit is not explicitly identified.

### Trivial

- None beyond the presentation issues noted above.

## Nice-to-Haves

- The experimental section would benefit from a direct comparison of the limiting predictor with predictions from prior theories (e.g., the ordered/chaotic phases of Xiao et al. 2020) or with finite-width simulations.
- A brief discussion of the assumptions linking the sphere restriction and the stereographic projection extension would aid reproducibility.
- The "list of properties" in Section 6 would be more actionable with a worked example beyond the brief mention of $\eta^{(L)}$.

## Removed Points

These points from the inputs were removed with justification:
- **"The inequality direction in the proof is reversed"** (Harsh Critic) — **Removed.** This is factually wrong. Verified: for $a,b\in(0,1)$, $a^\psi b^{1-\psi} \ge ab$ implies $\frac{\det(\dots)}{a^\psi b^{1-\psi}} \le \frac{\det(\dots)}{ab}$, which is exactly the direction the paper writes. The inequality chain is valid; the critic misunderstood the direction.
- **"Missing rough-path construction, verification of conditions for Universal Limit Theorem"** (Harsh Critic) — **Removed per instructions.** The paper states that the rough-path background is in Appendix D and the details are in the appendix. Since the parser strips appendices, these cannot be judged missing from the submission.
- **"Missing related works"** (Harsh Critic's note about comparison with Xiao et al.) — **Removed per instructions.** The paper does cite and discuss Xiao et al. (2020).
- **"Experiments never compute $\kappa_x^\top\kappa^{-1}$"** (Harsh Critic) — **Removed.** This is factually wrong. Figure 1's third column is explicitly labeled $\bar{\kappa}^{(l)}(x^\top X^\top)(\bar{\kappa}^{(l)}(XX^\top))^{-1}$, which is precisely this quantity. The critic's factual claim is incorrect; the valid concern (insufficient detail about the inverse computation) is retained as a Minor weakness above.
- **Multiple formatting/style nitpicks** — **Removed per instructions** (parser artifacts, not author errors).
- **"Strength: Empirical validation of convergence rates"** (Strength Finder) — **Weakened.** The experiments do show stabilization of the key quantity, but the lack of detail on the inverse computation and the focus on kernel entries rather than the predictor limit make this a weaker validation than claimed. The point is subsumed into the Minor weakness on experimental incompleteness.

## Novel Insights

None beyond the paper's own contributions. The review process surfaces no perspective on the paper's findings that the paper itself does not already articulate.

## Suggestions

1. **Define $\tilde{\Theta}_\infty^{(L)}$ explicitly** and clarify its relationship to $\Theta_\infty^{(L)}$ and $\bar{\Theta}_\infty^{(L)}$. If it is the normalized kernel, state this; if it is a different normalization, define it.
2. **Expand the proof sketch of Theorem 3** in the main text to at least state the key intermediate results (log-concavity of det for the first inequality, the specific convergence argument for $v_{ij}$ in 1-variation) even if the full rough-path details remain in the appendix. The current sketch is too terse to evaluate as a standalone argument.
3. **Add experimental details** on how the inverse in Figure 1's third column was computed (regularization parameter? pseudo-inverse tolerance?) and provide a quantitative assessment of convergence (e.g., relative change as a function of $L$).
4. **Resolve the inconsistency** between the motivation text (line 159, which uses $\Theta_\infty^{(L)}$ without tilde) and the theorem statement (which uses $\tilde{\Theta}_\infty^{(L)}$).

## Score and Decision

### Calibration for final score

**Round 1 (bracketing):** I retrieved anchors across three bands on the topic of NTK depth analysis.
- Weak band (avg < 3.5): `2NwHLAffZZ` (2.33, Reject), `fUz6Qefe5z` (3.00, Reject), `NbbsRnPBoS` (2.33, Reject), `G2Lnqs4eMJ` (2.50, Reject). These are papers with limited relevance or weak contributions. The paper under review is clearly stronger than these.
- Middle band (3.5 < avg < 7.5): `VEJzjAvaIy` (5.75, Accept — NTK divergence paper), `V6JRkfj9dU` (4.67, Reject — deep ReLU sample complexity), `YN4uWzcbtt` (4.25, Reject — NTK positive definiteness), `WH9NhxOeu9` (5.00, Reject). The paper under review is comparable to these.
- Strong band (avg > 7.5): `4xWQS2z77v` (8.00, Accept), `AoraWUmpLU` (8.00, Accept), `P7KIGdgW8S` (8.00, Accept), `STUGfUz8ob` (7.60, Accept). These are clearly stronger papers with complete proofs and significant contributions. The paper under review is weaker than these.

**Round 1 bracket:** 3.5–6.0.

**Round 2 (narrowing inside bracket):** I retrieved anchors in (3.5, 6.0) and (6.0, 8.0).
- `VEJzjAvaIy` (5.75, Accept) — NTK divergence paper. Comparable in ambition and novelty, but that paper had a cleaner proof despite mixed reviews. The paper under review has a more interesting premise but a sketchier proof.
- `kOtFuzoA93` (4.00, Reject) — Novel kernel models. Weaker than the paper under review.
- `MY8SBpUece` (5.50, Reject) — Feature learning theory. Comparable in theoretical ambition.
- `YN4uWzcbtt` (4.25, Reject) — NTK positive definiteness. Similar genre (NTK theory) but was considered incremental. The paper under review has a more novel question.
- `V6JRkfj9dU` (4.67, Reject) — Deep ReLU sample complexity. Similar quality level — solid theoretical claim but significant concerns about scope and validation.

**Final score:** The paper is comparable to or slightly stronger than the 4.67 anchor (V6JRkfj9dU) and the 4.25 anchor (YN4uWzcbtt), but weaker than the 5.75 anchor (VEJzjAvaIy) which was accepted despite mixed reviews. The notational gap and insufficient proof sketch prevent acceptance at this stage, but the core idea has merit. Score: **4.5**.

**All anchors retrieved:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| 2NwHLAffZZ | 2.33 | R1 | Weaker — limited relevance |
| fUz6Qefe5z | 3.00 | R1 | Weaker — narrower scope |
| NbbsRnPBoS | 2.33 | R1 | Weaker — different topic |
| G2Lnqs4eMJ | 2.50 | R1 | Weaker — different topic |
| VEJzjAvaIy | 5.75 | R1,R2 | Stronger — cleaner proof despite mixed reviews |
| V6JRkfj9dU | 4.67 | R1,R2 | Comparable — similar quality level, both had significant concerns |
| YN4uWzcbtt | 4.25 | R1,R2 | Slightly weaker — considered incremental |
| WH9NhxOeu9 | 5.00 | R1 | Comparable — similar theoretical ambition |
| 4xWQS2z77v | 8.00 | R1 | Much stronger — complete proofs |
| AoraWUmpLU | 8.00 | R1 | Much stronger — thorough paper |
| P7KIGdgW8S | 8.00 | R1 | Much stronger — not directly comparable |
| STUGfUz8ob | 7.60 | R1 | Much stronger — not directly comparable |
| kOtFuzoA93 | 4.00 | R2 | Weaker — less clear contribution |
| MY8SBpUece | 5.50 | R2 | Comparable — similar theoretical ambition |
| O6znYvxC1U | 6.33 | R2 | Stronger — accepted with stronger theory |
| tMzPZTvz2H | 7.00 | R2 | Stronger — more complete paper |
| usFdPd4Ghs | 6.80 | R2 | Stronger — accepted paper |
| VoLDkQ6yR3 | 6.67 | R2 | Stronger — accepted, different topic |

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
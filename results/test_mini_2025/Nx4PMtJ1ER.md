Now I have all the information I need. Let me compose the final review.

## Summary

This paper develops conditional independence (CI) constraints for coordinate processes of stochastic differential equations (SDEs), proves they satisfy the global Markov property with respect to the acyclic dependence graph, and proposes sound and complete constraint-based causal discovery algorithms (for both fully and partially observed settings) that uniquely recover the full graph by exploiting time directionality. The theoretical machinery is complemented by a practical, consistent signature-kernel-based CI test for path-valued random variables. Experiments demonstrate strong performance across multiple SDE settings and dimensions.

## Strengths

1. **Novel Markov property enabling full DAG recovery (Proposition 3.1, Theorem 3.2).** The paper proves that future-extended h-local conditional independence satisfies the global Markov property with respect to a lifted acyclic dependence graph. Combined with faithfulness, this allows Algorithm 1 to recover the *full* dependence graph rather than just a Markov equivalence class — a genuine advance over constraint-based methods for static settings. The proof leverages the SDE factorization structure and is outlined in Appendix A.6.

2. **First consistent, density-free CI test for path-valued random variables (Section 3.2).** The paper combines the signature kernel with permutation-based CI tests (KCIPT/SDCIT) and provides a new consistency proof that does not rely on density assumptions (Appendix A.14). This fills a clear gap, as existing kernel-based CI tests assume Euclidean spaces and density existence, while existing signature-kernel work only considered unconditional tests or heuristic measures.

3. **Strong empirical performance in low-to-moderate dimensions (Tables 1, 2; Figure 3).** In bivariate settings, SigKer achieves substantially lower SHD than all baselines across linear (14±4 vs best SCOTCH 50±17 at n=200), path-dependence (5±2 vs 23±12), and non-linear (28±5 vs 64±15) regimes. In multi-variable causal discovery (d≤10), both Algorithm 1 and Algorithm 2 clearly outperform PCMCI and SCOTCH. The power analysis (Figure 3) shows near-perfect detection at n≥40, far exceeding Laumann et al.'s approach.

4. **Handles a genuinely harder setting than prior work (Section 1, criteria a–d).** The framework simultaneously addresses (a) irregular sampling, (b) partial observability, (c) path-dependence (including delayed SDEs), and (d) diffusion dependence — criteria that no existing continuous-time causal discovery method satisfies together. SCOTCH, the primary baseline, is limited to fully-observed Markovian SDEs.

5. **Hyperparameter-free operation vs sensitivity in baselines.** SigKer involves no tunable hyperparameters for the CI test itself (only the RBF length-scale via median heuristic), whereas SCOTCH's performance varies substantially with λ and n_e. The paper documents this sensitivity transparently across multiple configurations.

## Weaknesses

### Major

1. **Overclaimed narrative in SCOTCH comparison when high-dimensional results tell a different story.** The paper repeatedly claims SigKer "broadly outperforms" SCOTCH, but at d=20 and d=50, SCOTCH 200,2k achieves SHD of 370±174 and 538±70 respectively, while SigKer's best variants reach 725±439 and 4593±93 (Table 2). These are large gaps favoring SCOTCH. The paper's argument that SCOTCH's hyperparameters cannot be selected in practice is reasonable but insufficient to fully dismiss these results — the claim "decisively dominates all baselines" (p.7) and "broadly outperforms the state-of-the-art" (p.8) are not supported across the full range of experimental conditions. The comparison would be stronger if it acknowledged these regimes more explicitly and discussed the trade-off (e.g., SigKer is more robust and broadly applicable but less sample-efficient in high dimensions).

2. **Partial-observations evaluation is a single toy example.** The paper highlights handling partial observations as "one of the main benefits" (p.8) yet evaluates it on only one 4-node graph with one unobserved variable (Figure 4). There is no systematic evaluation over random graph topologies, varying numbers of latent variables, or metrics such as SHD/precision/recall. While the result (8 vs 88 false adjacencies) is suggestive, it does not provide the empirical support needed for a claimed "main benefit."

### Minor

3. **Real-world trading example does not validate causal discovery.** The pairs-trading study uses financial P&L as a proxy for ground truth, which is indirect and confounded — good trading performance can arise from non-causal correlations. The paper frames this as a "substitution for ground truth" and a "proof-of-concept study," so the claims are modest. However, including it as evidence of the method's causal discovery ability is not convincing. It would be better reframed purely as a downstream application of the CI test, not as causal validation.

4. **CI test specification for continuous, path-valued Z is underspecified.** The paper states it "run[s] a kernel-based permutation CI test like KCIPT or SDCIT" but does not specify how the permutation scheme handles continuous, path-valued Z. KCIPT/SDCIT require approximating exchangeability for continuous Z (e.g., via nearest-neighbor perturbations); the adaptation to path-valued conditioning variables is non-trivial and deserves a brief description. The consistency proof (Appendix A.14) is referenced but a short statement of conditions in the main text would help readers assess the test's reliability.

5. **Corollary 3.3 contains an apparent typo.** The statement reads "$X_{[0,T]}^j \not\perp X_0^k$ but $X_{[0,T]}^i \perp X_0^j$" — the variable $k$ appears without definition. Based on context it should be $X_0^i$. This does not affect the correctness of the surrounding logic but should be corrected.

6. **No sensitivity analysis for the choice of $s$ and $h$.** The experiments fix $s = 0.1T$ and do not report how performance varies with these parameters (the paper mentions Table 5 which is in the removed appendix). Since $s$ and $h$ are user-chosen parameters that could affect the reliability of $\perp_{s,h}^+$, a brief sensitivity study in the main text would be valuable.

### Trivial

7. **Minor notational gaps.** In Algorithm 1, the loop-removal condition "$X^k \not\perp_{s,h}^\circ X^{\text{pa}} \setminus \{k\}$" does not specify what the conditioning variable is (it should be $X^{\text{pa}}_{[0,s+h]}$ or similar). This can be clarified.

## Nice-to-Haves

- A brief summary of the computational complexity comparison (SigKer vs SCOTCH vs PCMCI) in the main text, beyond the deferred appendix reference.
- A small simulation validating the CI test's Type I error control under the null for path-valued settings, complementary to the power analysis.

## Removed Points

These points were raised in the input reviews but removed or demoted after cross-checking against the paper:

1. **"First to simultaneously satisfy criteria" overstated (Harsh Critic):** The critic questions whether SCOTCH satisfies some of the four criteria (a–d). Checking the paper: SCOTCH is explicitly described as being limited to "fully-observed, Markovian SDE models" (p.3), so it does not satisfy path-dependence (c) or partial observability (b). The claim appears accurate. **Removed.**

2. **"Future-extended CI conditions on future of K without justification" (Harsh Critic, Low-Medium):** The paper acknowledges this non-standard conditioning with a footnote (p.4, footnote 1) and the global Markov property is proved in Appendix A.6. The point is valid but adequately handled in the appendix; elevating it further would be scope creep. **Demoted to removed.**

3. **"Laumann et al. dismissal too strong" (Harsh Critic):** The statement that Laumann et al. "assumes P_{X|Z} known" is accurate as written — their method requires knowing the conditional distribution. The paper's characterization is fair. **Removed.**

4. **Pairs-trading as a strength (Strength Finder):** The strength finder listed this as "Demonstrates practical value." However, the real-world example does not validate causal discovery specifically — it validates the CI test's utility in a financial application. This conflicts with Weakness #3 above. **Removed.**

5. **Generic strengths (Strength Finder):** Several generic descriptions of the paper's scope were dropped as they lacked concrete anchor in evidence (e.g., "the paper makes theoretical contributions" without specification). The specific, evidenced strengths (items 1–5 above) are retained.

## Novel Insights

None beyond the paper's own contributions. The synthesis of reviews surfaces a clear tension that the paper does not fully resolve: the theoretical claim that exploiting time directionality enables full-graph recovery is elegant and well-proven, but the practical CI test loses power in high dimensions (d≥20), creating a gap between the oracle setting and the implemented method. The paper's own acknowledgment that the CPDAG+post-processing route (Algorithm 2) may be more robust in practice (p.5) hints at this trade-off but does not explore it empirically. A deeper investigation of when the lifted-graph approach is preferable to the CPDAG+post-processing approach would sharpen the paper's practical guidance.

## Suggestions

1. **Recalibrate claims about SCOTCH comparison.** Explicitly state the regimes where SCOTCH with favorable hyperparameters outperforms SigKer (diffusion dependence, d≥20) and discuss the trade-off: SigKer trades off some high-dimensional efficiency for broad applicability and hyperparameter-free operation.

2. **Expand the partial-observations evaluation to a systematic benchmark** (random DAGs, varying latent variables, SHD/precision/recall). Even a moderate extension (e.g., 100 random graphs at d=5 with 1–2 latents) would substantially strengthen this claim.

3. **Reframe or remove the real-world example** if the goal is to validate causal discovery. Alternatively, expand it with known ground-truth relationships.

4. **Add a brief description of how the permutation test handles continuous, path-valued Z** in Section 3.2 (2–3 sentences), and state the key condition under which the CI test is consistent.

5. **Fix the typo in Corollary 3.3** ($k$→$i$).

6. **Add a brief sensitivity analysis** for parameters $s$ and $h$ (or at least reference the results if they appear in the appendix).

## Score and Decision

**Bracketing:** Round 1 placed the paper in the middle band (3.5–7.5). The most directly comparable anchor is the SCOTCH paper (avg 7.0, ICLR poster), which addresses a similar problem with a different approach. The SCOTCH anchor has a cleaner empirical evaluation but weaker theoretical foundations and narrower scope. Below that, "Practical Kernel Learning for CI Test" (avg 4.5, Reject) and "A Dynamical View of the Question of Why" (avg 5.5, Poster) are less comparable but define the lower part of the band.

**Narrowing:** Round 2 anchors include CausalRivers (avg 7.33, Spotlight), CausalTime (avg 6.75, Poster), and several others in the 5.5–6.5 range. The paper under review has stronger theoretical contributions than any of these anchors, but its empirical evaluation has uncovered gaps that the top anchors (CausalRivers, SCOTCH) do not have. Compared to SCOTCH (7.0), this paper has richer theory and broader scope but a messier comparison narrative. Compared to CausalRivers (7.33), it has weaker empirical validation but an actual algorithmic contribution. Overall, the paper sits below the SCOTCH anchor in overall polish but above the mid-range anchors (5.5–6.5) due to its theoretical depth.

**Final score: 6.5** — a solid paper with clear theoretical and methodological contributions, held back from a higher score by overstated empirical claims in the SCOTCH comparison and insufficient evaluation of the partial-observations setting. The core ideas are novel and the CI test is likely to be useful beyond this paper. With fairer framing and expanded evaluation, this could be a 7+ paper.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
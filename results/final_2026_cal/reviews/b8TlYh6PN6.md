Now I have all the information I need. Let me synthesize the final review.

---

## Summary

This paper provides the first characterization of distributional equivalence for linear non-Gaussian causal models with arbitrary latent structure and cycles. It introduces *edge rank* constraints as a new graphical tool (proving duality with path ranks), establishes a graphical criterion (Theorem 2: checking children bases for the latent set and each observed singleton suffices), and gives a transformational characterization (Theorem 3: admissible cycle reversals and edge additions/deletions suffice to traverse the equivalence class). The glvLiNG algorithm is developed as a proof-of-concept that recovers the equivalence class from data without structural assumptions on the graph (e.g., acyclicity, pure measurements).

## Strengths

- **First complete equivalence characterization for latent-variable LiNG models with cycles.** Theorem 2 reduces checking equivalence to verifying children bases for the latent set and each observed singleton — a dramatic simplification over the naive subset-based condition. This is the first result in any parametric setting that handles arbitrary latent structure and cycles simultaneously, analogous in significance to CPDAGs for the causally-sufficient acyclic case.

- **Edge ranks are a genuinely new tool with broad potential.** The duality theorem (Theorem 1) connects path ranks (well-known in causal discovery) to edge ranks, revealing that every path-rank statement has an edge-rank counterpart. This fills a missing piece in the rank-based toolbox and could benefit causal discovery settings beyond the specific LiNG framework studied here.

- **Transformational characterization enables equivalence class traversal.** Theorem 3 provides the first Meek-conjecture-style result for latent-variable models — the equivalence class can be navigated via admissible cycle reversals and edge additions/deletions. This is principled and the six-graph example (Figure 3) demonstrates concrete utility.

- **Clean irreducibility treatment.** Proposition 1 gives a simple graphical condition (each latent set must have ≥2 children outside itself) to eliminate trivially unidentifiable variables, and Proposition 2 provides an explicit reduction procedure. This sets up the equivalence analysis on solid footing.

- **Honest acknowledgment of limitations.** The paper transparently states that glvLiNG serves as a proof of concept, acknowledges OICA's practical difficulties, and identifies clear future directions (OICA-free algorithms, extension to Gaussian settings).

## Weaknesses

### Major

- **Experimental evaluation is too thin to support the algorithmic claims.** The main-text evaluation of glvLiNG (Section 5) consists of one paragraph per experimental aspect with no error bars, no confidence intervals, no quantification of variance across random seeds or graph distributions. The abstract and contribution list claim "the first structural-assumption-free discovery method," but the evaluation provides insufficient evidence to back this strong claim. While the paper positions glvLiNG as a proof-of-concept (line 336), the disparity between the strength of the narrative claim and the thinness of the evidence is a real gap. The "Full results in Appendix D.4 / D.5" are not present in the main text and cannot be assessed. At minimum, error bars and finite-sample sensitivity analysis for the OICA dependence should be reported in the main text.

- **Missing sensitivity analysis for the OICA dependence.** The algorithm's core relies on OICA, which is known to be unreliable in practice. The paper acknowledges this but does not evaluate the pipeline's sensitivity to OICA estimation errors, finite-sample rank estimation, or near-Gaussian noise. Since the paper stakes a strong claim about being a "structural-assumption-free discovery method," this sensitivity gap is significant even for a proof of concept.

### Minor

- **The definition-equivalence gap is acknowledged but not resolved in the main text.** Definition 1 defines equivalence as equality of the *full* distribution set P(G,X), while the characterization (Lemma 2, Lemma 3) uses constraints that hold only *generically* (Lebesgue measure zero exceptions). The paper notes "this does not affect our results" (Section 3.1) and works with the Zariski closure, but the reasoning is deferred entirely to the (inaccessible) appendix. A short justification or a precise statement in the main text that the definition can be relaxed to "equality up to measure zero" would resolve this cleanly. As currently written, readers must take the proof's validity on faith.

- **"Structural-assumption-free" is used for both parametric and graph-structure assumptions interchangeably.** The paper correctly means "free of assumptions on the *graph structure* (acyclicity, measurement patterns, etc.)." However, the method still assumes linearity, non-Gaussianity, and non-constant noise. The phrasing in the abstract and contribution list could misleadingly suggest a fully assumption-free approach. Clarification in the final version would help.

- **The evaluation does not compare against methods that *can* handle cycles without latents (e.g., cyclic LiNGAM extensions).** This would help disentangle the effects of cycles vs. latents on performance. Currently, the baselines (LaHiCaSi, PO-LiNGAM) are applied in settings violating their assumptions, which is informative for misspecification but does not isolate glvLiNG's accuracy advantage.

### Trivial

- None beyond parser artifacts.

## Nice-to-Haves

- A brief sketch of how the Zariski-closure argument resolves the measure-zero gap (even 2–3 sentences) would greatly improve main-text self-containedness.
- A discussion of how to estimate the number of latents in practice when OICA is not perfectly reliable (or references to prior work on source-number estimation in ICA).
- For Theorem 2, a short intuition on why checking singletons suffices (the paper says "it suffices to check each singleton X_i" but does not explain why this decomposition works beyond citing edge matchings).

## Removed Points

These points were flagged in the input reviews but are removed because they misread the paper, are factually incorrect, or are noise:

- *"The algorithm's structural-assumption-free claim is misleading without clarifying parametric assumptions"* — kept but downgraded to Minor because the paper does clarify this implicitly ("linear non-Gaussian" is in the title) and the meaning is "free of graph-structure assumptions." The strength of the narrative claim warrants keeping it as a minor presentation issue.
- *"The paper does not discuss identifiability of the number of latents when OICA fails"* — this is acknowledged as a limitation and the algorithm is a proof of concept; moved to Nice-to-Haves.
- *"Missing related works"* — removed per instructions (cannot confirm existence of unlisted works).
- *General formatting/style nitpicks* — removed per instructions.
- *"Algorithm description is too brief and readers need appendix"* — weakened because the paper is a theory paper with algorithm as proof-of-concept, and detailed appendix descriptions are standard practice.
- *Missing appendix content complaints* — removed per instructions (appendix is stripped by parser).

## Novel Insights

The most striking insight from the review synthesis is that **the paper's primary contribution (equivalence characterization) and its most marketable claim (first structural-assumption-free algorithm) sit at different levels of readiness**: the characterization is rigorous, complete, and genuinely novel, while the algorithm is acknowledged as preliminary. This tension pervades the evaluation — reviewers who focus on the theory see a strong paper, while a reviewer focused on the algorithmic claims sees an undersupported system. The paper would be better served by decoupling these more sharply in the narrative, e.g., stating upfront that the algorithm is an illustrative instantiation, not a fully validated discovery method.

## Suggestions

- Add a 2–3 sentence sketch in Section 3.1 explaining why working with the Zariski closure does not lose information for the purpose of distributional equivalence — specifically, that parameterizations are generically injective up to scaling/permutation, so equality of Zariski closures implies equality of the full distribution sets.
- Include error bars or variance estimates (over random seeds, different graph draws) for the finite-sample simulation results.
- Add a sensitivity experiment where OICA is replaced by a noisy rank estimator to test pipeline robustness.
- Clarify in the abstract and contribution list that "structural-assumption-free" refers to graph-structure assumptions, not parametric assumptions, e.g., "free of assumptions on graph structure (acyclicity, measurement patterns, etc.)."

## Score and Decision

**Calibration process:**

*Round 1 (Bracketing):* Retrieved anchors from three bands on the query "causal discovery latent variables linear non-Gaussian equivalence characterization":
- Low band (score < 3.5): aS7EVadvZD (3.00), MHy7PnRcRO (3.00), cP2nOl3t3W (3.20), nSuJ4OXf0j (2.50) — all clearly weaker papers.
- Middle band (3.5–7.5): qLbTww6vv2 (4.00), expkpx9TWg (4.00), TAOpnCPnjg (4.50), BNHplerBYE (5.33) — all topically relevant causal discovery papers with latent variables.
- High band (> 7.5): Ahdsg2nkNH (8.00), VaS6xcDrTb (8.50), 248ysaRatx (8.00), qOyF214xmg (8.00) — papers from other fields, not comparable.

*Initial bracket:* The paper is clearly above the low-band papers. It sits between the 4.0–5.33 range of the middle band. Initial bracket: [4.5, 6.5].

*Round 2 (Narrowing):* Retrieved additional anchors inside (4.5, 7.5):
- hisAy19yMP (5.50) — causal effect identification paper, less relevant.
- ta8BKRa1bl (6.00, Accept Poster) — multi-environment identifiability; strong theory, narrow experiments.
- ssYeoL4ksl (5.50, Reject) — linear cyclic with latents; bivariate only, pairwise approach.
- M4Z2A1jYpU (5.00, Accept Poster) — causal score conditioning, less relevant.
- bOfiLeoUJf (4.67, Accept Poster) — causal graph pruning.
- wnFbqvUJ6D (5.00, Reject) — multi-view causal discovery.

*Key anchor comparisons:*
- **TAOpnCPnjg (4.50, Accept Poster)** — CICA paper: narrower scope (acyclic only), similar experimental depth. The current paper has stronger and more general theory. → Current paper is *better*.
- **BNHplerBYE (5.33, Accept Poster)** — LGES paper: stronger experiments but narrower model class (generalized N-factor). Current paper's theory is more general. → *Comparable, slightly stronger theory*.
- **ssYeoL4ksl (5.50, Reject)** — bivariate cyclic latents paper, rejected partly for limited scope. Current paper is much broader. → Current paper is *substantially stronger*.
- **ta8BKRa1bl (6.00, Accept Poster)** — multi-environment identifiability, strong theory but experiments limited to bivariate synthetic. Current paper's theory is comparably strong and addresses a different (complementary) problem setting. → *Comparable in contribution significance*.

*Final score:* 5.5. The theoretical contribution is genuinely novel and important — it solves a longstanding open problem. The experimental validation is the main weakness. However, because the algorithm is presented as a proof of concept (not the main contribution), this weakness is bounded and does not undermine the core claim. The measure-zero concern is acknowledged by the authors and claimed to be resolved in the proofs.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>
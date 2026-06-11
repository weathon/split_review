Now I'll produce the final consolidated review.

## Summary

This paper provides the first characterization of distributional equivalence for linear non-Gaussian (LiNG) causal models with arbitrary latent variables and cycles — without structural assumptions. It introduces edge-rank constraints (dual to path ranks), a local graphical criterion (Theorem 2) that reduces equivalence checking to singleton checks on observed variables, and a transformational characterization analogous to the Meek conjecture (Theorem 3). The paper also presents glvLiNG, an algorithm that recovers the equivalence class from data as a proof of concept.

## Strengths

- **Edge-rank duality (Theorem 1, §3.3)**: Proves a clean duality between path ranks (familiar in causal discovery) and the newly introduced edge ranks, showing every path-rank statement has an equivalent edge-rank counterpart. This bridges matroid theory with causal discovery and directly enables the paper's main criterion. The paper honestly acknowledges that the duality has been studied in matroid theory, so the novelty is in importing and applying it to causal discovery.

- **Local decomposition of equivalence into singleton checks (Theorem 2, §4)**: Reduces checking all subsets of observed variables to checking each singleton independently — from exponential to linear in |X|. This is the paper's central technical deliverable and a dramatic simplification that makes the criterion actionable.

- **Transformational characterization (Theorem 3, §4)**: Provides the first "Meek conjecture"-style result for latent-variable models: two irreducible models are equivalent iff one can reach the other via admissible cycle reversals and edge additions/deletions. This cleanly enables equivalence class traversal and is well-illustrated with examples (Figure 3).

- **Clean handling of irreducibility (Definition 2, Proposition 1, §2.2)**: Gives a simple graphical condition for when a latent-variable model is minimal, along with an explicit reduction procedure. This eliminates trivial non-identifiability without imposing structural assumptions — a useful canonicalization.

- **Clear presentation and logical flow**: The paper is well-structured, building from definitions → algebraic condition → path rank characterization → edge rank reformulation → local graphical criterion → transformational characterization → algorithm. The analogies to CPDAGs and the Meek conjecture help orient readers.

## Weaknesses

### Major

- **Oracle OICA assumption undercuts the algorithm claims (§5).** The abstract and contribution list (line 40) claim "the first structural-assumption-free method for latent-variable causal discovery." However, glvLiNG's guarantee (line 308) requires "access to an oracle OICA" — overcomplete ICA is a notoriously hard open problem that the paper does not advance. The paper acknowledges this only in the final remarks (line 328: "serves more as a proof of concept"). This creates a significant gap between the bold opening claims and what is actually delivered. The theoretical results (Theorems 1–3) stand independently, but the algorithm framing as a practical "structural-assumption-free discovery method" overstates what the paper demonstrates. The paper would be more accurate presenting glvLiNG as an existence proof: given a faithful mixing matrix (from any source), the equivalence class can be recovered.

### Minor

- **In-text experimental detail is thin for an algorithmic contribution.** The main text provides some quantitative results (runtime: n=10 in <5s, baseline hours beyond n=5; class sizes: 783 equivalence classes from 480,640 irreducible models), which is more than the harsh critic acknowledged. However, edge-recovery accuracy is described only qualitatively ("over half of edges misidentified," "performs better on denser graphs"). The paper states that finite-sample evaluations exist in Appendix D.4, but no quantitative accuracy metrics (precision/recall, SHD, etc.) appear in the main body. For a paper listing an algorithm as a main contribution (item 4), at least one concrete accuracy result in the main text would strengthen the presentation.

- **Proposition 1's irreducibility check is exponential in |L| in the cyclic case.** The condition requires checking every non-empty subset of L. The paper notes the simplification to singletons for acyclic models (line 106) but does not discuss whether this extends to the cyclic case. If it does not, verifying irreducibility could be expensive when |L| is large. A brief acknowledgment would improve the discussion.

- **Lemma 7 is stated only for irreducible models.** The traversal procedure depends on Lemma 7. The paper would benefit from an explicit statement that the initial graph Ĝ constructed by glvLiNG's Phase 1 is irreducible by construction, confirming that the traversal operates in the correct domain.

### Trivial

None beyond what the authors would naturally resolve in a camera-ready version.

## Nice-to-Haves

- Provide at least one quantitative accuracy metric (e.g., structural Hamming distance, precision/recall of edge recovery) in the main text for the finite-sample evaluation.
- Clarify whether the singleton simplification for checking irreducibility (Proposition 1) extends to cyclic graphs.
- A brief discussion of the sample complexity or conditions under which OICA can be expected to succeed in the overcomplete setting would help readers assess the practical relevance of glvLiNG.

## Removed Points

These points from the reviews were removed; treat them with caution:

1. **"Circularity between OICA and irreducibility"** (Harsh Critic point 3): Removed because it mischaracterizes the dependency chain. The paper's logic is: irreducible model → OICA-identifiable (by known theory). The algorithm assumes: oracle OICA → mixing matrix → construct graph (irreducible by construction). This is a standard assumption chain, not a circularity. The critic's concern about whether irreducibility can be verified from data before running OICA is a practical point but not a logical circularity.

2. **"No evaluation of glvLiNG with actual OICA estimates under finite samples"**: The paper explicitly states (line 324) that it evaluates "glvLiNG with existing methods under finite samples" and refers to Appendix D.4 for full results. While these results are not shown in the main text, the claim that no such evaluation exists is contradicted by the paper's own description.

3. **"Theorem 4 not summarized"**: The main text (line 302) provides a one-sentence summary: "We show that within each cycle-reversal configuration, there exists a unique maximal equivalent digraph of which all others are subgraphs." The full statement is in the appendix (stripped from this PDF). The critic's claim of no summary is inaccurate.

4. **Generic strengths from Strength Finder about the problem being "important"**: Removed as generic/superficial. Only concrete, paper-specific strengths are retained.

5. **Criticism about checking subsets for irreducibility being exponential** (Harsh Critic §2): Not removed — retained as a Minor weakness above, but downgraded from the critic's framing.

## Novel Insights

Neither reviewer fully captured a point worth highlighting: the edge-rank duality (Theorem 1) may be the most broadly impactful result beyond this paper's specific setting. The paper treats it primarily as a tool for the equivalence characterization, but the duality between path ranks and edge ranks is a general fact about digraphs that could transfer to other settings (e.g., linear Gaussian models, discrete models, or selection bias). The paper notes this briefly (line 232: "filling the other side to the rank-based toolbox") but does not emphasize the broader potential. This duality could enable equivalence characterizations in other parametric settings where the current paper's specific LiNG assumptions do not apply.

## Suggestions

1. **Reframe the algorithm contribution.** Change the abstract and contribution (item 4) to present glvLiNG as a *proof of concept* showing that the equivalence class is recoverable given a faithful mixing matrix, rather than as a practical "structural-assumption-free discovery method." The final remarks (line 328) already say this; the front matter should match.

2. **Add one quantitative accuracy table in the main text.** Even a single table showing edge recovery rates (precision/recall or SHD) on one synthetic benchmark, varying sample size, would substantially increase confidence in the algorithm's finite-sample behavior.

3. **Acknowledge the computational cost of checking irreducibility** for cyclic models with many latents (Proposition 1).

4. **Explicitly confirm** that the initial graph Ĝ constructed by the rank-realization phase is irreducible by construction, so that Lemma 7's irreducible-domain restriction is automatically satisfied.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
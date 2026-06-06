## Summary

The paper establishes the first graphical characterization of distributional equivalence for linear non-Gaussian (LiNG) causal models with arbitrary latent variables and cycles — filling a gap the authors document has persisted for decades. The core technical tool is *edge rank* constraints, defined via maximum bipartite matchings on adjacency support matrices, which satisfies an elegant duality with the classical path ranks (Theorem 1). Building on this, the paper proves a local decomposition criterion (Theorem 2) and a "Meek-conjecture"-analog transformational characterization (Theorem 3). An accompanying algorithm, glvLiNG, is presented as a proof-of-concept for assumption-free latent-variable causal discovery.

---

## Strengths

- **Novel equivalence characterization with latent variables (Theorem 2):** The local decomposition result — that equivalence checking reduces to comparing *children bases* for each singleton observed variable $X_i$ independently rather than all subsets $x \subseteq X$ — is a non-trivial simplification. The paper carefully motivates why this reduction was hard and why edge ranks (rather than path ranks) make it possible. This is the paper's central contribution and is well-argued.

- **Edge rank / path rank duality (Theorem 1):** The duality $\min(|Z|,|Y|) - \rho_\mathcal{G}(Z,Y) = |V| - \max(|Z|,|Y|) - r_\mathcal{G}(V\setminus Y, V\setminus Z)$ is an elegant standalone result that bridges the global max-flow picture familiar in causal discovery to a local bipartite matching structure. The connection to König (1931) and the matroid community (Perfect, 1968; Ingleton & Piff, 1973) is correctly attributed and fills a genuine gap in the causal discovery toolbox.

- **Transformational characterization (Theorem 3) enabling traversal:** The result that any two equivalent irreducible models can be connected by admissible cycle reversals and edge additions/deletions (with at most one cycle reversal needed) provides actionable traversal machinery directly analogous to the Meek conjecture for CPDAGs. The interactive demo at https://equiv.cc and Figure 3 concretely illustrate the structure of equivalence classes.

- **Clean irreducibility framework (Propositions 1–2):** The graphical condition $|\text{ch}_\mathcal{G}(l) \setminus l| \geq 2$ for all non-empty $l \subseteq L$, paired with the explicit reduction procedure (Proposition 2), cleanly handles trivial non-identifiability without imposing any structural assumption. The claim that this is canonicalization rather than restriction is well-justified via OICA identifiability (Eriksson & Koivunen, 2004).

- **glvLiNG runtime vs. LP baseline (Table 4):** The constraint-based design enables solving $n=10$ vertex cases in under 5 seconds versus hours for LP beyond $n=5$ — a concrete, quantified contribution to practical feasibility of the theoretical machinery.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Evaluation 3's framing could be sharpened.** The paper correctly labels evaluation 3 as examining "how existing methods behave under structural misspecification" (§5), but offers no reciprocal experiment showing how glvLiNG behaves on the graphs that LaHiCaSi and PO-LiNGAM *were designed for* — e.g., showing that glvLiNG produces a correct but larger equivalence class on sparse, assumption-satisfying graphs. This would more informatively characterize the identifiability trade-off between structural assumptions and equivalence class size. The paper's evaluation 4 notes "baselines perform better on sparser graphs" but this is acknowledged only in passing.

- **Finite-sample robustness of Phase 1/Phase 2 rank decisions is not characterized in the main text.** The algorithm's correctness guarantee requires faithfulness (Appendix A), and the rank conditions driving graph construction (§5) are sensitive to near-zero vs. exactly-zero entries in the estimated mixing matrix from OICA. The paper honestly acknowledges OICA is a "proof of concept," but even a brief qualitative discussion in the main text of how estimation noise interacts with the rank thresholding decisions (and under what sample-size regimes the finite-sample evaluation holds) would strengthen the algorithmic contribution's transparency.

### Trivial

- **"At most one cycle reversal is needed" (Theorem 3)** is stated without a sentence of intuition in the main text. This is a non-obvious claim and a brief informal explanation would improve readability.

---

## Nice-to-Haves

- **Characterize which causal features are invariant across the equivalence class.** The paper mentions edges invariant across the equivalence class (analogous to directed arrows in a CPDAG) and defers it to Theorem 4 in the appendix. Bringing even a summary of this result to the main text would sharpen the paper's thesis for scientific inference: readers would know precisely which causal quantities (ancestral relations, direct effects, latent connectivity) are identifiable vs. genuinely underdetermined.

- **Extend evaluation 4 to include a scenario where competitor assumptions hold.** Showing that glvLiNG correctly recovers an equivalence class on graphs where LaHiCaSi/PO-LiNGAM assumptions are satisfied — even if glvLiNG's equivalence class is necessarily larger — would provide a cleaner picture of the practical cost of dropping structural assumptions.

- **Brief d-separation discussion for Theorem 1's scope claim.** The paper states (§3.3) the duality "suggests that every statement phrased in terms of path ranks and its variants, including the familiar d-separation and t-separation, can be equivalently rephrased in terms of edge ranks." Since d-separation operates on undirected paths under independence criteria — a different object — even a brief caveat noting the sense in which this holds or a pointer to where the details appear would prevent misreading.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic's concern about LP baseline being a "strawman":** The critic suggests LP may not be the state-of-the-art for rank realization problems and that "the framing suggests it is the only natural alternative, which may not be correct." This is entirely speculative — no concrete alternative is named, and LP is a natural and well-motivated baseline for constraint satisfaction. **Removed: speculative, no concrete anchor.**

- **Harsh critic's concern that "the algorithm's correctness guarantee requires faithfulness" is not discussed prominently enough:** The faithfulness assumption is formally stated (Assumption 1, Appendix A) and referenced in §5. The appendix is stripped by the parser; this should not be held against the authors. **Removed: appendix content stripped by parser.**

- **Harsh critic: "evaluations 3 and 4 are presented as performance benchmarks but are not":** The paper explicitly labels evaluation 3 as examining "how existing methods behave under structural misspecification by applying them to arbitrary latent-variable models possibly beyond their assumptions." The framing is honest. **Removed as a "major" weakness; retained only as a minor suggestion for reciprocal experiments.**

- **Harsh critic: "the LP comparison framing suggests it is the only natural alternative":** No alternative is specified; pure speculation. **Removed.**

- **Strength Finder: "algorithmic translation and empirical demonstration" as a top-tier strength:** The evaluation is explicitly a proof of concept and some aspects (stock returns) are qualitative. Retained only as a supporting element, not a core strength. Downgraded.

---

## Novel Insights

The most genuinely novel observation across the reviews is the framing of the paper's contribution as *filling both sides of the rank-based picture in causal discovery*: path ranks (global, max-flow, tied to mixing matrices) have long been the primary tool, while edge ranks (local, bipartite matching, tied to support matrices) have been studied in the matroid community since König (1931) but not imported into causal discovery. The duality in Theorem 1 is not just a mathematical curiosity — it is precisely the tool that enables the local decomposition in Theorem 2, which is the reason the equivalence criterion comes out clean despite the structural complexity introduced by latent variables and cycles. This duality-enabled simplification is the conceptual core of the paper, and the fact that edge ranks may be useful in other causal discovery settings (linear Gaussian, beyond) gives it broader methodological significance.

---

## Suggestions

1. **Add a single comparison scenario on assumption-satisfying graphs** in evaluation 4 (or evaluation 3) to show glvLiNG's correct but larger equivalence class, making the identifiability trade-off quantitatively clear.
2. **Move a summary of the CPDAG analog (Theorem 4)** to the main text, even as a corollary, to clarify what is and is not identifiable from data.
3. **Add one informal sentence explaining why "at most one cycle reversal" suffices** in Theorem 3 to aid reading comprehension.
4. **Qualify the d-separation claim in §3.3** with "in the appropriate sense" or a pointer to where this is formalized, to prevent misreading by readers familiar with d-separation in the standard graphical sense.

---

## Score and Decision

**Originality:** 5/5 — First distributional equivalence characterization with latent variables in any parametric setting; edge ranks are genuinely new to causal discovery.
**Importance:** 4/5 — Addresses a foundational open problem that has blocked a class of structural-assumption-free discovery methods.
**Claims supported:** 4/5 — Theoretical chain from Lemmas 1–5 through Theorems 1–3 is carefully structured; empirical claims are honestly scoped as proof-of-concept.
**Soundness:** 4/5 — Internal logical development is coherent and self-consistent; proofs are in appendix.
**Clarity:** 4/5 — Well-organized step-by-step presentation with good analogies; minor expository gaps.
**Community value:** 4/5 — Useful for latent-variable causal discovery; edge ranks potentially useful beyond this specific setting.

The theoretical core is novel, technically non-trivial, and fills a well-documented gap. The empirical component is appropriately scoped. Weaknesses are real but minor and do not threaten the core claims.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>5</originality>
<importance>4</importance>
<claims_supported>4</claims_supported>
<soundness>4</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>
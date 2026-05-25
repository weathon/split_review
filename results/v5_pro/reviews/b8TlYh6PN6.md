Now I have a comprehensive understanding of the paper and the calibration anchors. Let me compile the final review.

---

## Summary

This paper addresses a foundational gap in causal discovery: characterizing distributional equivalence for linear non-Gaussian latent-variable models with arbitrary latent structure and cycles — without any structural assumptions. The authors introduce a novel graphical tool, *edge ranks*, prove a duality theorem connecting them to classical path ranks (Theorem 1), and derive a local graphical criterion for equivalence via "children bases" (Theorem 2). They further provide a transformational characterization (Theorem 3) that enables traversal of the equivalence class via cycle reversals and edge additions/deletions. An algorithm, glvLiNG, is presented as a proof of concept, recovering the equivalence class from data using overcomplete ICA.

## Strengths

- **First equivalence characterization without structural assumptions.** The paper provides the first distributional equivalence characterization for linear non-Gaussian models that allows arbitrary latent structure and cycles. This fills a recognized gap: no prior work characterizes equivalence with latent variables in any parametric setting without structural assumptions like pure children or acyclicity. The authors make a compelling historical analogy to how CPDAGs enabled the PC algorithm.

- **The edge rank tool and its duality with path ranks (Theorem 1).** Edge ranks (Definitions 4, 6) provide a local, edge-level constraint dual to the global, path-level path ranks. The duality theorem is elegant and fills a missing piece in the rank-based causal discovery toolbox. This tool enables the clean decomposition in Theorem 2 and has potential applications beyond this paper.

- **Practical local criterion via children bases (Theorem 2).** The reduction of equivalence checking to bases of the latent set and each latent-set-plus-one-observed-variable is a substantial simplification. Instead of verifying rank equality over exponentially many subsets (Lemma 3), the check decomposes per observed variable, making it computationally tractable and directly informing algorithm design.

- **Transformational characterization (Theorem 3).** The result that any equivalent irreducible model can be reached via admissible cycle reversals and edge additions/deletions — with at most one cycle reversal — is a clean analogue of Meek's conjecture for this setting. It provides an actionable procedure for equivalence class traversal.

- **Clear motivation and well-structured exposition.** The paper is well-organized, moving from problem setup (§2) through tool development (§3) to final criteria (§4) and algorithm (§5). The running analogy to Markov equivalence/CPDAGs effectively grounds the contribution for the causal discovery community.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Tension between exact and generic equivalence under-theorized in the main text.** Definition 1 defines distributional equivalence as exact equality of observed distribution sets. The reduction to rank constraints (Lemma 2) invokes generic rank properties ("almost everywhere except for a Lebesgue measure zero set") and Zariski closure arguments. The paper briefly notes a pathological locus where denominators vanish in cyclic models and states "this does not affect our results," but the main text does not make explicit whether the final characterization (Theorem 2) captures exact equivalence under faithfulness, or generic equivalence. The appendix proof may resolve this, but a concise clarification in §3.1 would strengthen the theoretical exposition. This does not threaten the core result — generic rank properties are standard in this literature — but the gap between Def 1 and Lemma 3 deserves a crisp statement.

- **Empirical evidence for glvLiNG is largely deferred to appendix.** The algorithm is presented as a contribution (§5), but the main text contains no tables or figures for the finite-sample comparison against baselines (aspect 4) or the real-world application (aspect 5). The paper acknowledges glvLiNG is a "proof of concept," which mitigates this, and the theoretical contribution is the main event. Still, for a paper that includes an algorithm and an evaluation section, a single summary table or figure for the most important empirical result (finite-sample comparison) would anchor the algorithm's claims.

### Trivial

- The leap from Lemma 1 (mixing-matrix closures) to Lemma 3 (equivalence via path ranks) is compressed into a short paragraph. The paper asserts that "rank constraints alone, together with a column permutation, suffice to determine equivalence" and defers the justification to the appendix proof. A brief sketch of the key algebraic-geometric reasoning (e.g., that the Zariski closure is cut out by determinantal ideals) in the main text would make the argument more self-contained for readers.

## Nice-to-Haves

- A small worked example illustrating the computation of children bases and the application of Lemma 7 (edge addition criterion) would make the criteria more tangible for readers, complementing the existing Figure 3.
- The claim that "at most one cycle reversal is needed" (Theorem 3) is interesting; a one-sentence intuition for why this holds would improve accessibility.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"The paper refers to Tables 1–5 and Figure 5, but none of these appear in the supplied manuscript."** — REMOVED. This is a parser artifact: the appendix (containing these tables) was stripped during PDF extraction. The original submission includes them.

2. **"The algorithm description (§5) would benefit from a more detailed inline explanation of Phase 1 and Phase 2."** — DEMOTED to Trivial/Nice-to-Have. The main text provides a conceptual sketch; full pseudocode and detail belong in the appendix, which is standard for theory-heavy papers.

## Novel Insights

The duality between path ranks and edge ranks (Theorem 1) is genuinely novel for the causal discovery community, even though the underlying matroid theory is classical. The paper's key insight is that this duality allows reformulating the equivalence problem from a global path-based perspective to a local edge-matching perspective, which then admits a tractable decomposition. The observation that the children bases of L and L∪{X_i} suffice — and that each X_i can be checked independently — is both surprising and practically significant. This decomposition mirrors how "same adjacencies and v-structures" simplified Markov equivalence checking, and represents a similar leap for the latent-variable non-Gaussian setting.

## Suggestions

- Add a paragraph in §3.1 explicitly clarifying whether the target is exact equivalence under faithfulness (with the pathological locus addressed in the proof) or generic equivalence, and justify why the Zariski closure transition preserves the intended notion.
- Include a small summary table or figure in the main text for the finite-sample comparison (aspect 4) — even a single plot of edge recovery vs. sample size for one representative setting would validate the algorithm's practical utility without requiring the reader to consult the appendix.
- The interactive online demo at <https://equiv.cc> is a genuine strength; consider referencing it more prominently, as it makes the transformational characterization concrete and explorable.

## Score and Decision

**Calibration anchor summary:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|-------------|
| nHkMm0ywWm (PO-LiNGAM) | 6.50 | R1-topic-mid | Closest topic: linear non-Gaussian + latents, but requires pure children + acyclicity. Our paper is strictly more general and theoretically deeper. |
| BZYIEw4mcY | 6.00 | R1-topic-mid | Latent variable CD with structural assumptions; significant presentation issues. Our paper is better written, more novel. |
| FhQSGhBlqv (RLCD) | 7.50 | R1-topic-high / R1-weakness | Rank-based latent CD, linear Gaussian, well-executed with strong experiments. Our paper has more fundamental theory (first equivalence characterization) but weaker empirical presentation. Comparable overall. |
| Bp0HBaMNRl | 6.75 | R2 | Differentiable CD for latent hierarchical models, nonlinear. Mixed reviews on experiments. |
| k03mB41vyM | 6.50 | R2 | Theoretical framework, no experiments. More abstract scope. |
| TRHyAnInUC | 3.25 | R1-topic-low | Reject: weak theory, unsupported claims. Our paper shares NONE of these failures. |
| G5KbDVAlI6 | 4.00 | R1-weakness | Reject: scalability issues, vague theorems. Our paper does not share these failures. |

**Round 1 bracket:** 6.5 – 8.0. The paper sits above the mid-band anchors (PO-LiNGAM at 6.50, BZYIEw4mcY at 6.00) due to stronger theoretical novelty and no structural assumptions, and is comparable to the high-band anchor RLCD (7.50) in contribution weight.

**What did the low-band anchors fail at, and does this paper share any of those failures?** The low-band anchors (3.00-3.40) failed at weak or missing theoretical foundations, unsupported central claims, poor presentation, and inadequate experiments. This paper shares none of these failures: it has rigorous theoretical development, a well-supported central claim, clear exposition, and the empirical limitations are explicitly scoped (proof-of-concept algorithm).

**Round 2 narrowing:** Within the 6.0-8.0 range, the paper is stronger than Bp0HBaMNRl (6.75, mixed reviews on limited experiments) and k03mB41vyM (6.50, purely theoretical with no experiments). It is comparable to RLCD (7.50) — slightly stronger in theoretical novelty, slightly weaker in empirical completeness. The paper's explicit acknowledgment that glvLiNG is a proof of concept and OICA is a bottleneck is honest scoping, not a flaw.

**Final score: 7.0.** The paper makes a significant theoretical contribution (first equivalence characterization without structural assumptions in any parametric setting), introduces a genuinely useful new tool (edge ranks), and provides both a decision criterion and a traversal method. The minor weaknesses (generic-vs-exact clarification, appendix-deferred evaluation) do not undermine the core contribution and are addressable.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
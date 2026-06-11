Now I have a clear picture. Let me compare the paper against the narrowed anchors:

- **ia9fKO1Vjq (5.40, Accept):** Theoretical extension with some concerns about incremental contribution and unclear presentation. Our paper has a more novel, self-contained theoretical contribution and cleaner presentation. Our paper is stronger.

- **nHkMm0ywWm (6.50, Accept):** Strong theory + practical algorithm with solid empirical validation. Our theory is broader (handles cycles, no structural assumptions), but empirical validation is thinner and algorithm relies on OICA. Our paper is slightly below this.

- **fGhr39bqZa (6.00, Accept):** Causal graph recovery with latent variables via homologous surrogates. Similar theory+algorithm structure. Our theory is arguably more complete (full equivalence characterization vs. partial/full recovery conditions), but our main-text evaluation is thinner.

- **BZYIEw4mcY (6.00, Accept):** Efficient causal discovery with latent variables. Our paper has a stronger theoretical contribution (first equivalence characterization), comparable or slightly weaker empirical validation.

The paper is closest to the 6.00 anchors — strong theory with reasonable but not stellar empirical support — and clearly above the 5.40 anchor. **Final score: 6.0.**

---

## Summary

This paper provides the first characterization of distributional equivalence for linear non-Gaussian latent-variable causal models with arbitrary latent structure and cycles. The central technical innovation is the introduction of *edge ranks* — a local, matching-based graphical quantity dual to path ranks (Theorem 1) — which enables a decomposition of global equivalence conditions into per-vertex checks (Theorem 2). The paper further establishes a transformational characterization (Theorem 3) showing that equivalence classes are connected via cycle reversals and edge additions/deletions, and develops the glvLiNG algorithm to recover models up to equivalence from data without structural assumptions. Code and an interactive demo are available at equiv.cc.

## Strengths

- **Edge ranks as a novel analytical tool with a proven duality to path ranks (Theorem 1):** The paper introduces edge ranks — a local quantity based on maximum bipartite matchings — and proves they are dual to the globally-defined path ranks. This duality is the key insight enabling the subsequent characterization and fills a genuine gap in the rank-based causal discovery toolbox. The paper is transparent that the duality was known in matroid theory (König 1931; Perfect 1968), but its application here is novel for causal discovery.

- **Local decomposition of equivalence into per-vertex checks (Theorem 2):** The paper proves that distributional equivalence of two irreducible models reduces to checking "children bases" for the latent set L and for each L ∪ {X_i} individually (Eq. 19). This collapses an exponential number of rank-equality conditions (Lemma 3) into |X|+1 local checks, and cleanly reduces to the known Lacerda et al. (2008) digraph identification result when L = ∅.

- **Transformational characterization of the equivalence class (Theorem 3):** The paper proves that two irreducible models are equivalent iff one can be transformed into the other via admissible cycle reversals (Lemma 6) and edge additions/deletions (Lemma 7). This is an analogue of Meek's conjecture for this parametric setting and enables traversal of the entire equivalence class via BFS/DFS.

- **Clean irreducibility framework (Propositions 1–2):** Proposition 1 gives a simple, checkable graphical condition characterizing when a model contains no redundant latent variables, and Proposition 2 provides an explicit reduction procedure. This eliminates trivial non-identifiability before the main analysis, keeping the subsequent characterization focused.

- **Interactive demo and open-source code:** The paper provides both code and an interactive visualization at equiv.cc, which is genuinely valuable for conveying the combinatorial complexity of equivalence classes beyond what static figures can show.

- **Systematic positioning across classical settings (Table 2, Appendix C.5):** The paper situates its results alongside analogues from causally-sufficient acyclic (CPDAG), causally-sufficient cyclic (Lacerda et al. 2008), and latent-variable acyclic (MAG/PAG) settings, making explicit how this work completes a missing quadrant in the literature.

## Weaknesses

### Fatal
None.

### Major

- **The algorithmic contribution is undersubstantiated in the main text relative to its prominence in the claims.** The abstract and introduction give the glvLiNG algorithm equal billing as contribution #4 ("the first structural-assumption-free method for latent-variable causal discovery"), but Section 5 contains primarily summary-level evaluation descriptions. While the main text does include quantitative highlights (e.g., "n=10 vertices in under 5s," "783 equivalence classes from 480,640 irreducible digraphs"), the detailed experimental tables, figures, error bars, and metric definitions are all deferred to the appendix. As a result, the reader cannot independently assess the strength of the algorithmic evidence from the main body alone. This matters because the paper frames itself as delivering both theory and an algorithm, and the boldness of the algorithmic claim ("first structural-assumption-free") raises the evidentiary bar for the main text.

### Minor

- **Reliance on OICA as a practical bottleneck:** The glvLiNG pipeline depends on OICA for mixing matrix estimation, which is acknowledged to be difficult in the overcomplete regime. The paper is transparent about this (lines 328–329: "serves more as a proof of concept") and suggests future OICA-free directions, so this is not a hidden flaw. However, it does limit the immediate practical impact of the algorithmic contribution and somewhat tempers the "structural-assumption-free *method*" framing.

- **Baseline comparison design is partially self-confirming:** Testing LaHiCaSi and PO-LiNGAM on models that violate their structural assumptions (evaluation aspect 3) primarily demonstrates that methods fail when their assumptions are violated — which essentially confirms the paper's premise rather than establishing glvLiNG's positive performance. A more informative comparison would also include regimes where the baselines' assumptions hold, to assess whether glvLiNG sacrifices accuracy for generality.

- **The "CPDAG analogue" (Theorem 4) is deferred entirely to Appendix C.3:** Given the paper's sustained analogy with Markov equivalence and CPDAGs throughout, Theorem 4 — which constructs a unique maximal equivalent digraph and identifies invariant edges — is conceptually central enough to merit at least a statement in the main text, even if the proof is deferred.

### Trivial
None.

## Nice-to-Haves

- A brief illustrative example showing what glvLiNG recovers that FCI cannot would strengthen the motivational narrative, given the paper's repeated invocation of the FCI comparison.
- A discussion of the computational complexity of checking Lemma 7's condition for admissible edge additions would help readers assess the practicality of equivalence class traversal.
- A theoretical analysis of finite-sample behavior or consistency under estimated (rather than oracle) mixing matrices would complement the empirical finite-sample simulations in Appendix D.4.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Harsh Critic — "The relationship between rank constraints and the Zariski closure... is not developed with sufficient rigor in the main text":** The paper explicitly states that rank constraints "suffice to determine equivalence" (line 162) and cites Talaska (2012) for the generalization of rank constraints to cyclic graphs. The completeness proof is deferred to the appendix. Without access to the full proofs, the concern about possible counterexamples is purely speculative and cannot be verified as a genuine weakness. REMOVED.

- **Harsh Critic — "No discussion of statistical consistency or finite-sample guarantees":** The paper includes finite-sample simulations (evaluation aspect 4, Appendix D.4), partially addressing this concern empirically. The lack of theoretical finite-sample analysis is standard for a primarily theoretical paper with supporting experiments. DEMOTED to Nice-to-Have.

- **Strength Finder — "First structural-assumption-free algorithm with empirical validation":** This is more a claim than a demonstrated strength. The evidence for it is thin in the main text, as noted in the Major weakness above. DEMOTED.

- **Strength Finder — "Stepwise theoretical progression with clear motivation":** While true, this is a generic presentation strength that could apply to many well-organized papers. REMOVED as too generic.

- **Harsh Critic — complaints about formatting, typos, or unclear notation in specific locations:** These are parser artifacts or trivial formatting issues. REMOVED per hard rules.

## Novel Insights
The introduction of edge ranks as a dual to path ranks is genuinely novel for causal discovery. While the underlying duality was known in matroid theory, the paper's insight is that this dual perspective — operating on edges rather than paths — converts an intractable global equivalence condition into a local, decomposable one (Theorem 2). This conceptual move from "check all subsets of X" to "check per-vertex children bases" is the kind of structural insight that could influence future work on rank-based causal discovery beyond the linear non-Gaussian setting.

## Suggestions

- Move at least one key experimental table or figure (e.g., the equivalence class enumeration statistics or the runtime comparison) from the appendix into the main text to give readers direct evidence for the algorithmic claims without relying on the appendix.
- Present Theorem 4 (the maximal digraph / CPDAG analogue) at least as a stated result in the main text, even if the construction and proof remain in the appendix.
- In the baseline comparison (evaluation aspect 3), consider additionally testing on models that satisfy the baselines' assumptions to provide a more complete picture of the generality-precision tradeoff.
- Consider slightly reframing contribution #4 to match the paper's actual strength: the algorithm as a constructive consequence of the theory and a proof of concept, rather than an independently competing empirical contribution.

## Calibration Anchors Referenced

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| QSuOHV62IQ | 3.50 | R1 | Weaker: had unsupported claims, restrictive assumptions, unclear contribution |
| vyQmKicyVw | 3.50 | R1 | Weaker: narrower identifiability scope, less complete characterization |
| 0sO2euxhUQ | 4.00 | R1 | Weaker: more limited theoretical scope |
| ZKRHiu5kE4 | 4.25 | R1 | Weaker: application-specific, less general theory |
| q07DDpu8Xb | 5.25 | R2 | Weaker: narrower theoretical contribution |
| ia9fKO1Vjq | 5.40 | R2 | Weaker: more incremental contribution, less clean theory |
| fGhr39bqZa | 6.00 | R1 | Comparable: similar theory+algorithm structure, our theory broader |
| BZYIEw4mcY | 6.00 | R1/R2 | Comparable: similar quality, our theory stronger, their evaluation stronger |
| nHkMm0ywWm | 6.50 | R2 | Stronger: better empirical validation, more practical algorithm |
| k03mB41vyM | 6.50 | R1 | Stronger: broader framework, stronger empirical contribution |
| Bp0HBaMNRl | 6.75 | R1 | Stronger: differentiable method with strong theory and experiments |
| xByvdb3DCm | 8.00 | R1 | Much stronger: well-rounded contribution with clear practical impact |
| 3cuJwmPxXj | 8.00 | R1 | Much stronger: complete theory-to-application pipeline |

The paper sits at approximately 6.0: above the 5.40 anchor (which had concerns about incremental contribution) and comparable to the 6.00 anchors (fGhr39bqZa, BZYIEw4mcY) that feature solid theory with reasonable but not exceptional empirical validation. The paper's theory is genuinely novel and well-structured, while the main-text evaluation presentation is the primary factor preventing a higher score.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
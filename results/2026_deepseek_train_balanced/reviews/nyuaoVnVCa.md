## Summary

This paper develops a multi-agent deep reinforcement learning framework for emergent communication in "guessing games," where the listener faces genuine meaning ambiguity about which concept the speaker intends (unlike standard naming games with unambiguous reference). The framework integrates an explicit spatial ontology (segments × sectors × colors), a guided feedback mechanism for the poverty-of-stimulus problem, mirror-learning losses for role interchangeability, and a principle-of-least-effort objective. The paper reports qualitative observations about emergent word order, Zipfian distributions, and convergence of shared vocabularies in toy environments (5 vertices, 4 agents).

## Strengths

- **Genuinely ambiguous-reference setting (guessing game vs. naming game):** The paper explicitly frames its contribution around the "guessing game" where a given (source, topic) vertex pair admits multiple possible conceptualizations (Section 3, line 50). This is concretely distinguished from conventional naming-game benchmarks where "the semantic aspect used to distinguish the topic from other context elements is clear and free from ambiguity" (Section 1, lines 21–23). This is a meaningful and underexplored problem framing.

- **Causal ablation of the least-effort mechanism:** The paper systematically varies the weight κ₂ (principle-of-least-effort loss) across values 1.1, 0.01, and 0.001 (Section 7, lines 177–179) and shows this causally controls the emergent word order: higher weights yield simpler conceptualizations (<segment, ⊥, color>), lower weights yield maximal conceptualizations (<segment, sector, color>). This goes beyond observing a property to demonstrating that a specific loss term drives it.

- **Structured spatial ontology:** The ontology (3 segments × 4 sectors × 4 colors = 48 combined concepts plus NULL) provides a grounded, linguistically meaningful concept space that is richer than typical flat attribute-value pairs.

## Weaknesses

### Major

- **Mirror loss formulation is mathematically ill-posed as written.** The mirror loss (Equations lines 105–106 and 139) includes KL divergence terms where the two distributions are over different sample spaces. Specifically, 𝒟_KL(π_θ^A(·|m) ∥ π_φ^A(·|m)): π_θ is the utterance network (mapping concept→message), and π_φ is the listening network (mapping message→concept). The paper never defines what π_θ^A(·|m) means architecturally (the speaker does not normally take a message as input), and even if it does, the two distributions live in different spaces (messages vs. concepts). The same problem applies to 𝒟_KL(π_φ^B(·|c') ∥ π_θ^B(·|c')). Since the mirror loss is central to the interchangeability claim (Hypothesis IV) and role-switching mechanism, this technical issue must be resolved. The paper cannot claim that the mechanism works through these equations as written. **(This is verifiable from the architecture in Section 5 (line 68) and the mirror loss equations in Section 6.3.)**

- **No comparative evidence: the experimental design cannot support the attribution claims.** The Experiments section contains zero baselines: no comparison to standard referential/naming games, no ablation removing individual components (guided feedback, mirror loss, least-effort penalty), no comparison to prior emergent communication methods, and no comparison to a version without interchangeable roles. The only parameter varied is κ₂. Because there are no controls, the paper cannot attribute observed convergence to any specific design choice — whether it is the guided feedback, mirror learning, guessing-game structure, or simply the presence of a shared reward function. **(Verifiable: Section 7 describes only the authors' setup with no comparative conditions.)**

- **Insufficient experimental rigor for the scope of claims.** The main experiment uses 5 vertices and 4 agents; a second experiment uses 3 vertices and 2 agents. No results are reported over multiple random seeds (no variance, no statistical significance). Standard emergent communication metrics — topographic similarity, mutual information between messages and referents, vocabulary overlap coefficients, vocabulary entropy — are entirely absent. Claims about "near-identical vocabularies" (line 175) are supported only by a qualitative figure (Figure 2) with no quantitative measure such as edit distance or Jaccard overlap. Successful communication reaching ~100% is unsurprising given the guided feedback mechanism, and the paper does not establish that the guessing-game ambiguity makes the problem genuinely harder. **(Verifiable from Sections 7 and 7.1 — no multi-seed reporting, no quantitative vocabulary metrics.)**

### Minor

- **The guided feedback mechanism partially undercuts the "poverty of stimulus" framing.** The speaker discloses the topic *vertex* to the listener on failed interactions (Section 6.1, lines 82–85). While the paper correctly notes that conceptualization ambiguity remains (Section 6.4, line 115), knowing the ground-truth referent is a strong supervisory signal that real language learners do not receive. This makes the experiment less directly comparable to the claimed "Gavagai" problem. The paper would benefit from an ablation where λ=1 (no disclosure) to measure how much harder the problem becomes.

- **Compositionality claims are weakened by the paper's own data.** In the 3-vertex experiment, 65% of conversations are reported as non-compositional (color alone) and only 24% exhibit two-word compositionality (line 194). The paper frames this as "sub-optimal limiting behavior," but this undercuts any strong claim about compositionality emerging from the framework.

- **No statistical characterization of Zipfian distributions.** The paper claims the emergent language follows Zipf's law (Section 7.1, line 196, Figure 15) but provides no rank-frequency coefficient (e.g., fitted exponent) or statistical test. Without these, the claim is qualitative.

### Trivial

- The gradient derivations (lines 149, 153) contain apparent formatting degradation ("7L₁" on line 149) and garbled notation that makes verification difficult.

## Nice-to-Haves

- Report at least 5–10 random seeds with means and standard deviations for all quantitative measures.
- Include standard emergent communication metrics (topographic similarity, adjusted mutual information, vocabulary overlap).
- Provide an ablation experiment without guided feedback (λ=1) to establish the difficulty of the purely ambiguous setting.
- Compare against a standard referential game (unambiguous topic) to calibrate how much harder the guessing game is.

## Removed Points

These points were surfaced in the reviews but are removed or demoted after cross-checking:

- **"Guided feedback provides ground-truth concept (not just vertex)"** — Reviewer misread: the paper clearly states the topic *vertex* (not the concept) is disclosed (lines 82–85, 115). Conceptualization ambiguity remains. Demoted from fatal/major to minor.
- **"Stochastic guided feedback" as a supporting strength** — The probabilistic nature of λ is genuinely a design choice, but the core concern about supervision remains. Kept implicitly in the minor weakness.
- **"Two-timescale learning with formal convergence conditions"** — The conditions listed (lines 164–166) are the standard two-timescale SA conditions (Σ e_t = ∞, Σ e_t² < ∞, lim e_t/e'_t = 0). Not a novel contribution.
- **"Zipf's law adherence with controlled mechanism strength" as a core strength** — The qualitative observation is interesting, but without a fitted exponent or statistical test, it is a weak strength.
- **Criticism about "missing related works"** — Removed per the rule that I must not mention missing related works.
- **Reproducibility nitpicks about hyperparameters** — Removed per hard rules.

## Novel Insights

None beyond the paper's own contributions. The two reviews surface important technical issues (mirror loss formulation, lack of baselines) and one significant misreading (guided feedback providing the vertex vs. the concept). The paper's core idea — studying ambiguous-reference guessing games with structured ontologies — remains interesting, but the technical execution and evaluation are not at the level required for acceptance.

## Suggestions

1. **Fix the mirror loss formulation:** Clarify the sample spaces of each KL divergence term. If the intention is to define an auxiliary decoder/inverse mapping that allows comparing speaker and listener distributions, this must be stated and formalized explicitly. Alternatively, reformulate the consistency objective using a different divergence (e.g., cross-entropy between the observed and predicted conditional distributions) that respects the differing sample spaces.
2. **Run controlled ablations:** At minimum, ablate guided feedback (λ=1), mirror learning, and the least-effort penalty individually to establish that each component contributes to the observed behavior.
3. **Quantify vocabulary convergence:** Report vocabulary overlap coefficients, edit distances, or similar quantitative measures across agents instead of relying on a qualitative figure.
4. **Report standard emergent communication metrics** (topographic similarity, mutual information) and run at least 5 seeds with error bars.

## Score and Decision

This paper identifies an interesting gap in the emergent communication literature — the study of ambiguous-reference guessing games — and proposes a framework with several well-motivated components. However, it has two decisive problems. First, the **mirror loss, which is central to the interchangeability claim, is mathematically ill-posed as written**, with KL divergences taken between distributions over different sample spaces. Second, the **experimental evaluation provides no comparative evidence**: no baselines, no ablations, and no multi-seed statistics, making it impossible to attribute the observed behavior to specific design choices. These are not minor gaps; they affect whether the method as formulated actually functions as claimed. The underlying idea is worthwhile, but in its current form the paper falls substantially below the bar for a top venue.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>
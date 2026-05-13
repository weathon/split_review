## Summary
The paper formalizes a novel problem: given black-box query access to a model and a local explanation, find the largest $\ell_\infty$ hypercube ("trust region") around a point in which the explanation satisfies a fidelity threshold. The authors propose Ecertify with three sampling strategies (unif, unifI, adaptI), derive finite-sample probabilistic bounds plus an EVT-based asymptotic alternative, and demonstrate query savings and explanation stability on tabular/image datasets.

## Strengths
- **Genuinely novel problem framing.** Eq. (1) (line 32) cleanly defines "find the largest hypercube where the explanation's fidelity meets a threshold"; the placement of robustness certification as the constant-explanation special case (line 47) is apt and clarifying.
- **Practical utility demonstrated.** The HELOC reuse experiment (Fig. 4, lines 415–418) reports ~80% query savings, and Table 3 (lines 419–436) shows Top-5 intersection 0.85 vs 0.77 and Spearman 0.74 vs 0.61 inside vs outside the certified region — concrete evidence of the trust-region notion having meaning.
- **Scalability vs the adapted ZO baseline.** Table 1 (e.g., $d=10^4, Q=10^4$: adaptI 88s vs ZO$^+$ 4385s, lines 360–364) shows large speedups while reaching comparable widths.
- **Piecewise-linear characterization.** §6.2 derives the structure of the fidelity CDF as a polytope-weighted mixture, providing a non-trivial structural account for an important model class.

## Weaknesses

### Fatal
None — the contributions (problem formulation, algorithms, computable bounds, empirical results) are real, and the structural issues below are repairable.

### Major
- **The "certificate" is self-referential.** The bounds in Lemmas 2–4 / Theorem 1 are functions of $F_i(f^*_w+\epsilon)$, and both $F_i$ and $f^*_w$ are unknown. §6.1 (line 255) acknowledges this and proposes plugging in $\hat{f}^*_w$ (or $\theta$) plus a KDE for $F_i$. The paper is honest about this, but the framing as "probabilistic certification" reads as stronger than what is delivered (a sampling estimator with plug-in confidence). The Remark on line 217 also depends on $F_i(f^*_w+\epsilon)\neq 0$, which can be arbitrarily small. Either restate as plug-in/estimation bounds, or supply an unconditional concentration argument (e.g., empirical-CDF concentration or a conformal-style approach).
- **Lemma 4's "w.l.o.g." hides the central claim about adaptI.** Line 210 assumes $F_i^{\mathcal{N}_{j,k}}\le F_i^{\mathcal{N}_{j,k+1}}$ for $k$ indexing *sampled* prototypes, and then the bound depends on $F_i^{\mathcal{N}_{j,n}}$ (the best). After relabeling, the bound effectively requires that adaptI's elimination step retain (or oversample) the best prototype — exactly the property the algorithm is trying to achieve. As stated, the headline conclusion that adaptI dominates unifI does not follow from the analysis without a separate result on prototype-selection quality.
- **No bound on suboptimality of returned $w$.** Eq. (1) asks for the *largest* certified $w$; Theorem 1 only bounds false-certification of regions the algorithm did certify. Algorithm 1's doubling/halving can terminate at a $w$ much smaller than the truth if an intermediate region is mistakenly rejected, and nothing in the analysis bounds how far below optimal the output can fall. Half of the contribution claim (finding the *largest* region) has no theoretical support.
- **Compounding error across the search loop is not handled.** Lemma 1 decomposes over the $c$ regions actually certified by the algorithm, treating $c$ and the $w_i$ as fixed, but they are random outcomes of the same procedure being analyzed. There is no union bound across iterations of Algorithm 1. For a paper whose framed contribution is "computable theoretical guarantees," this gap matters.
- **Strategy differentiation in experiments is thin.** Table 1 at $d=10^4, Q=10^4$ gives $w$ of $8.9, 9.1, 9.4\times 10^{-5}$ for unif/unifI/adaptI with no run-to-run variance reported (the paper acknowledges variance only in Limitations). With single runs and gaps this small, the central methodological story — that adaptI matters in high $d$ — is not convincingly established by Table 1. Fig. 2 captions argue strategy regime preferences qualitatively rather than statistically.

### Minor
- **Single comparison baseline (ZO$^+$).** Adapted from an attack toolbox, this is the only external competitor. Latin-hypercube sampling, random search at matched budget, or BO would more fairly bracket the design space.
- **Lipschitz / piecewise-linear special cases require non-black-box knowledge** ($l$ or $p$), so their relevance to the black-box framing is limited; this should be acknowledged more explicitly.
- **EVT exponent $\kappa = d/2$** (line 269) is cited as a default but no diagnostic is run on whether the actual tail behavior of fidelity samples matches a $d/2$-index, despite the paper noting the bound becomes loose in $d$.
- **Stability claim is real but moderate** (0.85 vs 0.77, std err ~0.02): valid evidence, but the textual framing somewhat overstates the gap.
- **Coverage criterion (top-60% of features within region)** in Fig. 4 is ad hoc; a brief justification or sensitivity sweep would help.

### Trivial
- $\sigma=(ub-lb)/d$ is load-bearing but justified only via a footnote (line 154); a small sensitivity plot would settle the question.

## Nice-to-Haves
- A 2D visualization comparing where adaptI concentrates queries vs. where the true minimum-fidelity region lies, to make the "adaptive focusing helps" argument tangible.
- Add ≥10-seed std-devs to Table 1 and Fig. 2 so the strategy comparison is interpretable.
- A "missed-certification" analysis bounding how far below the true optimum the returned $w$ can be.

## Removed Points
These points are flagged to be removed; treat them with caution.
- *Harsh critic's framing complaint about "certification" terminology vs Reluplex/randomized smoothing.* The paper itself states (line 38) that with finite queries it can "only aim to approximately certify a region" and explicitly distinguishes itself from white-box certification in §3. The terminology is hedged, even if the abstract is bullish.
- *Harsh critic on Lipschitz/piecewise-linear cases being "orthogonal."* These are presented as auxiliary speed-ups, not the main contribution; criticizing them for not being black-box is partially scope creep.
- *Strength Finder's "comprehensive empirical efficiency and accuracy."* Folded into a kept strength, but the "comprehensive" wording is generic and the accuracy story is weakened by missing variance.
- *Strength Finder's "rigorous problem formalization and algorithm design"* as a standalone strength is generic; the kept "novel problem framing" point captures the substantive part.

## Novel Insights
None beyond the paper's own contributions. The most interesting observation surfaced in review — that the bound is effectively a self-referential plug-in estimator and that Lemma 4 implicitly assumes adaptI's elimination retains the best prototype — is a diagnosis, not a new positive insight.

## Suggestions
- Reframe Theorem 1 as a *plug-in confidence statement* and add an explicit assumption block; alternatively, replace the CDF dependence with a DKW-type / empirical-CDF concentration bound.
- Add a proposition on prototype-selection quality for adaptI, then derive the dominance claim conditionally on it; remove the misleading "w.l.o.g." in Lemma 4.
- Add a union bound over Algorithm 1 iterations, and a complementary "missed-certification" gap bound.
- Report multi-seed mean ± std for every $w$ and timing in Tables 1 and Fig. 2.
- Add at least one budget-matched baseline that isn't an attack-toolbox adaptation (random search, LHS).

## Evaluation
- *Originality:* High — the trust-region-for-explanations framing is genuinely new.
- *Importance:* Moderate-to-high — useful for explanation reuse and stability framing.
- *Claims well-supported:* Partially — empirical claims are reasonable; theoretical claims overreach in the way Lemma 4 and Theorem 1 are framed and in the absence of a union bound over the search loop.
- *Soundness of experiments:* Adequate but lacks variance estimates and a non-attack-toolbox baseline.
- *Clarity:* Generally clear; the §5 analysis would benefit from being explicit about what is assumed vs. derived.
- *Value to community:* Solid — problem framing and trust-region reuse will likely be picked up even if the theory needs sharpening.

## Score and Decision
The paper introduces a meaningful problem with practical empirical support, but the theoretical framing oversells the guarantees and the experiments don't cleanly establish the strategy hierarchy. These are addressable issues, not fatal flaws, and the contribution is real.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
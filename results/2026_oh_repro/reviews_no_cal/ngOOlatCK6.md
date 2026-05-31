## Summary
The paper studies **single-node conditional interventions** in causal bandits and asks: which *nodes* must be considered as potential intervention targets to guarantee containing an optimal conditional intervention for reward \(Y\). It proposes a **purely graphical** characterization of this “minimal” node set (the mGISS) and gives a **linear-time** algorithm (C4) to compute it, then empirically shows that restricting the arm set to the mGISS accelerates convergence of a UCB-style bandit over nodes.

## Strengths
- **The paper gives a concrete reduction from conditional to deterministic atomic reasoning.** Proposition 4 explicitly states an equivalence: “\(X \succeq_Y^c W \Leftrightarrow X \succeq_Y^{\det,a} W\)” (lines ~120–122 in the extracted text), which is a substantive technical simplification that the later graphical characterization builds on.
- **“Minimality” is defined (not just asserted) in terms of a preorder over nodes.** Definition 5 defines a GISS via \(U \succeq_Y (V\setminus\{Y\})\setminus U\) and then defines mGISS as a *minimal* such set (lines around the “Definition 5 (GISS and mGISS)” block). This is stronger than informal “we prune a lot” positioning.
- **Algorithmic contribution is operational, not just existential.** The abstract claims \(O(|V|+|E|)\), and the body explicitly names an algorithm (C4 / Algorithm 1) used in experiments to compute \(\mathcal{L}^\infty(\mathrm{Pa}(Y))=\mathrm{mGISS}_Y(G)\) (e.g., lines 261–263), indicating the work is constructive rather than purely theoretical.

## Weaknesses

### Fatal
None.

### Major
- **The “conditional intervention” information structure is quantified in a way that makes the headline guarantee potentially mismatched to realistic bandit settings.** In Definition 1, conditional-intervention superiority is defined as: for all SCMs with graph \(G\), there exists a policy \(g\) for \(X\) such that **for every observable conditioning sets** \(\mathbf{Z}_X,\mathbf{Z}_W\) and all policies \(h\) for \(W\), inequality (1) holds (lines 104–107). This effectively defines superiority in a *very strong* (worst-case over allowable conditioning sets) sense. If the intended bandit problem fixes what is observed/conditioned-on at decision time (as is typical), then the theoretical object being optimized/protected (“optimal conditional intervention”) is not clearly the same one used in deployment. The paper gestures that conditioning sets are “specified in advance” (line 96) and footnote text notes one “can always include” \(\mathrm{An}(X)\setminus\{X\}\) under their assumptions (lines 92–93), but the core definition still takes a universal quantifier over \(\mathbf{Z}\). This needs much clearer alignment: either (i) restate the main guarantee for a **fixed observation model** (fixed \(\mathbf{Z}_X\) per node), or (ii) explain why this worst-case-over-\(\mathbf{Z}\) notion is the correct one for the bandit setting the experiments implement. As written, it is hard to tell what notion of “optimal conditional intervention” the mGISS is guaranteeing.
- **Empirical results demonstrate “pruning helps regret” but do not directly validate the specific *guarantee* being claimed.** The experiments shown in the extracted text focus on (a) fraction of nodes retained by mGISS in random graphs (lines 261–264) and (b) cumulative regret curves comparing “brute-force” vs “mGISS” node selection (Figure 3 caption, lines 271–273). These results support the engineering claim that shrinking the node set improves learning speed. However, in the visible description there is no explicit check that the pruning **never removes the true optimal node** under the same conditional-intervention semantics used by the bandit evaluation (e.g., repeated random SCM parameterizations per fixed graph to empirically stress-test correctness). Since the core theoretical claim is “guaranteed to contain the optimal conditional intervention” (abstract, line 9), the experimental section should include at least one direct validation of this guarantee under the experimental policy/observation model, rather than only regret improvements (which can occur even for unsound prunings).

### Minor
- **The paper’s scope limitation “no unobserved confounding” is explicit, but the practical implications are not explored.** The paper states: “the assumption that there is no unobserved confounding is a limitation of this paper” (line 98). That is fine as scope, but it would help to clarify (even briefly) which parts of the characterization fail or become nontrivial with confounding, since causal bandit applications often involve latent confounding.

### Trivial
None.

## Nice-to-Haves
- Add an experiment specifically targeted at the *graphical characterization*, not only pruning size: e.g., construct graphs like Figure 1(d) (where naive heuristics fail) and empirically compare mGISS against simple baselines such as “ancestors of \(Y\)” or “parents of \(Y\) plus LCAs,” reporting (i) whether the optimal node is retained and (ii) regret impact.

## Removed Points
These points are flagged to be removed, treat them with caution.
- **“The formulation is underspecified so the theorem may be ill-defined.”** Removed because the paper *does* formalize a notion of conditional-intervention superiority (Definition 1) and explicitly restricts to single-node conditional interventions (line 98). The real issue is not absence of definitions, but potential mismatch between the strong quantified definition and the bandit observation model (kept above as a Major issue).
- **“Minimality might be vacuous / only sufficiency proved.”** Removed because the paper defines mGISS as a *minimal* GISS (Definition 5), so minimality is at least stated in-set terms. Without inspecting the full Theorem 13 proof text (not fully visible in the extracted chunks here), I cannot verify a necessity-via-construction argument, so I will not assert overclaiming beyond what can be anchored to visible text.
- **Complaints about “standard MAB algorithms” being unclear.** Removed because the extracted text (Figure 3 caption) concretely specifies a “UCB-based bandit algorithm for conditional interventions” with brute-force vs mGISS node sets (lines 271–273), so this is not purely vague.

## Novel Insights
The key technical risk is not “missing definitions,” but that the paper’s formal superiority relation (Definition 1) is *robustified* by quantifying over “every observable conditioning set” \(\mathbf{Z}\), while the practical causal bandit problem typically commits to a specific observation/conditioning interface. This creates a possible gap where the computed “minimal guaranteed” node set is minimal for a stronger (more pessimistic) notion than the one actually optimized in experiments and in the intended application—and this should be resolved explicitly because it directly affects what “optimal conditional intervention” means.

## Suggestions
- Rewrite the problem statement to **pin down the observation model** as a first-class object (e.g., for each node \(X\), a fixed allowable conditioning set \(\mathbf{Z}_X\) observed before acting), then restate the main guarantee and mGISS definition for that model; if the paper intentionally uses the “for every observable \(\mathbf{Z}\)” notion, justify why this matches the bandit interface used in Figure 3.
- Add an explicit experimental “soundness check”: for each graph family and many random SCM parameterizations, verify that the best node found by brute-force search over all nodes is always contained in the computed mGISS (under the same conditional-intervention class as the bandit algorithm uses).

## Score and Decision
**Originality:** solid—targets conditional (policy) interventions with a nontrivial graphical pruning goal.  
**Importance:** moderate-to-high for causal bandits; efficient arm-space restriction is practically valuable.  
**Claims supported:** theory appears substantial (Proposition 4; mGISS framework), but the *exact semantic alignment* between the conditional-intervention definition and the experimental bandit setting is currently not crisply supported in the visible text, and experiments mainly support “pruning helps” rather than the guarantee.  
**Experimental soundness:** adequate for demonstrating speedups, but missing direct validation of the theoretical guarantee.  
**Clarity:** generally clear on the high-level story, but the quantification over conditioning sets vs “specified in advance” needs clearer exposition.  
**Community value:** promising if the semantics/guarantee alignment is clarified.

MY FINAL SCORE: <score>6.5</score>  
MY FINAL DECISION: <decision>Accept</decision>
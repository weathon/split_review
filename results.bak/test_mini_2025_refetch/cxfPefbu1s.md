Now I have a thorough understanding. Let me write the final consolidated review.

## Summary

This paper identifies *disguised procedural unfairness* — the problem that enforcing fairness constraints on objectionable causal pathways inadvertently and arbitrarily alters neutral data-generating components, violating Rawlsian procedural justice. The authors propose a framework that decouples objectionable components by: (1) fitting model parameters **without** any fairness constraints, and (2) replacing only the **inputs** to objectionable edges with configured "reference points" that benefit the least advantaged. The paper provides a linear example demonstrating how prior methods distort neutral parameters, and a UCI Adult experiment showing improved approval rates for the disadvantaged group.

## Strengths

- **Identifies a genuinely under-characterized problem.** The phenomenon of *disguised procedural unfairness* — where fairness constraints arbitrarily shift neutral causal parameters — is convincingly demonstrated in the linear example (Section 3, Figure 1). The paper shows concretely that two different causal fairness approaches (Kilbertus et al., Nabi & Shpitser) yield different arbitrary distortions of the same neutral parameter $\hat{\theta}_C^Y$, with no justification for which distortion is preferable.

- **Clean, principled framework with clear algorithmic specification.** The core idea — fit parameters without constraints, then intervene only on inputs to objectionable edges via reference points — is technically sound and clearly presented in Algorithms 1 and 2. The approach avoids the parameter-tampering problem by construction: since model parameters are fitted without fairness constraints (Algorithm 2, Step 4), neutral components are preserved by design, not by post-hoc measurement. The connection to edge-specific causal intervention (Shpitser & Tchetgen, 2016) provides a solid technical foundation.

- **Principled philosophical grounding.** The connection to Rawls' pure procedural justice (Fair Equality of Opportunity and the Difference Principle) is not superficial window-dressing — the paper actually uses these principles to derive specific requirements (Requirements I and II) that directly motivate the framework's design (e.g., the Difference Principle drives the reference point optimization in Equation 4).

- **Expands the scope of objectionable components beyond protected features.** The framework naturally handles objectionable edges that do not originate from protected attributes (e.g., marital status → income), and the UCI Adult experiment demonstrates this by decoupling $M \rightarrow Y$ alongside $A \rightarrow Y$. The reference point optimization discovers a nuanced configuration (not flipping sex, but setting marital status to "married") that goes beyond what a simple protected-attribute flip would achieve.

## Weaknesses

### Major

- **Insufficient empirical evaluation against competing methods.** On UCI Adult, the only causal fairness baseline is Chiappa (2019). The paper does not compare against Kilbertus et al. (2017), Nabi & Shpitser (2018), or other path-specific/counterfactual fairness approaches on real data. The linear example in Section 3 does include these baselines, but only on synthetic data with known ground truth. A real-data comparison against a broader set of causal fairness methods is necessary to situate the contribution.

- **The UCI Adult experiment only measures approval rates, not the preservation of neutral components.** While the method preserves neutral parameters by construction (parameters are fitted without constraints), the paper's central claim is that prior methods alter neutral components and the proposed method avoids this. The linear example demonstrates this convincingly for the parametric case. However, on the real UCI Adult data where the models may not be perfectly specified, there is no diagnostic measure showing whether neutral component behavior is actually preserved. A direct comparison of how neutral parameters or causal mechanisms differ across methods on real data would strengthen the core claim.

### Minor

- **The reference point optimization (Equation 4) involves searching over a combinatorial space of reference point values.** The paper acknowledges this (Appendix D discusses scalability, which was stripped by the parser) but the main text does not discuss computational cost or practical search strategies when the number of objectionable edges grows.

- **The method requires a known causal graph and correctly specified local causal modules.** The paper acknowledges this assumption. It is a standard limitation in causal fairness work, but it constrains applicability to settings where the causal structure is well-understood.

### Trivial

- The linear example (Section 3) would benefit from a tabular summary of the numerical parameter values shown in Figure 1, since the figure's matrix format is hard to parse from the text alone.

## Nice-to-Haves

- An ablation comparing reference point optimization (Equation 4) against simpler heuristics (e.g., always using the group mean for objectionable inputs) would help isolate the benefit of the optimization procedure.
- Discussion of how to handle uncertainty in the causal graph specification (e.g., sensitivity analysis) would strengthen practical applicability.

## Removed Points

- *"Does not empirically demonstrate that its method actually avoids disguised procedural unfairness in practice"* — Removed because this criticism misunderstands the paper's design. The method fits parameters without any fairness constraint (Algorithm 2, Step 4), so neutral parameters are preserved **by construction**. The linear example (Section 3, Figure 1) visually demonstrates this preservation. The critic's suggestion that "a method that simply flips decisions... could achieve similar approval rates" ignores that the framework operates through input manipulation on specific edges, not outcome manipulation.

- *"The paper does not discuss the computational cost or scalability"* — Removed because the paper explicitly states that scalability discussion is in Appendix D (which was stripped by the parser): "Due to space limit, we present in Appendix D... the discussion on scalability."

- *"The paper does not compare to other causal fairness approaches (e.g., Kilbertus et al., Nabi & Shpitser) in the real-data experiment"* — WEAKENED from the harsh critic's framing and kept as a **Major** weakness (see above), since these baselines ARE used in the linear example but not on UCI Adult.

- *"Missing related works"* — Removed per instructions (cannot verify without external sources).

- *Strength Finder claims about "the single most compelling evidence"* — Kept as support for the paper's genuine contribution, not as a standalone strength.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's primary line of attack (that the method's central claim is unsupported) was found upon verification to be rooted in a misunderstanding of the method's design — the model parameters are fitted without fairness constraints, making neutral component preservation a design property, not an empirical question. However, the critic's concern about insufficient baselines on real data is valid and independently arrived at. The reviews did not surface any genuinely novel insight about the paper's contributions or limitations that the authors themselves had not already identified.

## Suggestions

1. Add at least one additional causal fairness baseline (e.g., Nabi & Shpitser's PSE-based approach or Kilbertus et al.'s approach) on the UCI Adult experiment.
2. Include a diagnostic metric (e.g., distance between fitted neutral parameters and their unconstrained counterparts, or a comparison of causal mechanism behavior) to empirically demonstrate neutral-component preservation on real data.
3. Add a brief complexity analysis or search strategy discussion for the reference point optimization (Equation 4) in the main text.

## Score and Decision

**Bracket determination (Round 1):** The initial bracketing placed this paper between anchors at ~3.0 (weak papers with major flaws) and ~8.0 (strong accepts). The middle band (3.5–7.5) contained the most relevant anchors: "Procedural Fairness Through Social Determinants" (3.67, Reject — by same group, with trivial conclusions and weak experiments), "Counterfactual Fairness With Human in the Loop" (4.00, Reject — foundational SCM issues), "Understanding Unfairness via Training Concept Influence" (5.33, Reject — incremental, limited novelty), and "Rethinking Fair Representation Learning" (7.00, Accept Poster — strong theory + experiments).

**Narrowing (Round 2):** Reading full reviews of these anchors revealed the current paper sits between the 5.33 and 7.00 anchors. It is clearly stronger than the 3.67 and 4.00 anchors — its contribution (identifying disguised procedural unfairness) is genuinely novel rather than incremental or trivial, and it does not suffer from foundational SCM formalism problems. However, it is weaker than the 7.00 anchor ("Rethinking Fair Representation Learning"), which had formal theoretical results (proving limitations of fair representation learning) and experiments across multiple medical modalities. The "Towards Counterfactual Fairness Through Auxiliary Variables" (6.00, Accept Poster) is the closest comparator: polarized reviews (8,3,5,8) with similar issues (limited datasets, missing baselines) but stronger empirical scope. The current paper has a more novel core idea but thinner experiments.

**Final calibration against anchors:**

| Anchor | Avg Score | Decision | Comparison |
|---|---|---|---|
| Social Determinants (4jBJ6JphYM) | 3.67 | Reject | **Weaker.** Trivial conclusions; current paper is more novel. |
| Human-in-the-Loop CF (I09JonzQJV) | 4.00 | Reject | **Weaker.** Foundational SCM issues; current paper is cleaner. |
| Causal Discrimination Discovery (1XzTxtezgj) | 4.40 | Reject | **Comparable.** Similar issues with unclear motivation; current paper has clearer motivation but similar experimental thinness. |
| Understanding Unfairness (dwademPdV1) | 5.33 | Reject | **Slightly stronger.** More thorough evaluation but less novel contribution. |
| Test-time Fairness (FEDnzAhIT4) | 5.75 | Reject | **Comparable.** Both have clear motivation but limited validation. |
| Towards CF Auxiliary (GpUv1FvZi1) | 6.00 | Accept (Poster) | **Slightly stronger.** More experiments and baselines, but similar limitations. |
| Rethinking FRL (pBZntPrdrI) | 7.00 | Accept (Poster) | **Stronger.** Formal theory + multi-modal experiments. |

**Score: 5.0.** The paper has a genuine, well-motivated, and clearly presented conceptual contribution. However, the empirical evaluation is too thin for acceptance: only one causal fairness baseline on real data, and no diagnostic measure of neutral-component preservation on real data beyond the linear synthetic example. With stronger experiments (additional baselines, diagnostic measures of neutral component preservation), this could be a clear accept.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
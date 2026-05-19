- Decision: Reject
- Avg Score: 5.60
- Scores: 6, 5, 6, 6, 5
I have now verified all claims against the paper. Let me construct the final review.

## Summary

This paper identifies, formalizes, and corrects the "equivalent action problem" in GFlowNet-based graph generation: when multiple distinct actions (e.g., adding a node to any of several symmetric attachment points) lead to the same resulting graph, naive implementations that ignore this undercount the transition probability, systematically biasing sampling against symmetric graphs (atom-based) or toward symmetric fragments (fragment-based). The proposed solution is remarkably simple—scale the terminal reward by the size of the automorphism group of the generated graph—and the paper proves (via telescoping application of Theorem 1) that this single end-of-trajectory correction suffices for both Trajectory Balance and Detailed Balance objectives. A small-graph experiment with exact tractable marginals provides clean confirmatory evidence, and molecule-generation experiments (atom-based on QM9 proxy, fragment-based on sEH proxy) show consistent practical improvements.

## Strengths

- **Clean theoretical identification of the bias with an elegant correction.** The paper formalizes the state space as equivalence classes of graphs under isomorphism, proves that the ratio of forward-to-backward equivalent actions equals |Aut(G)|/|Aut(G')| for standard action types (AddNode, AddEdge, attribute edits), and shows via telescoping (Corollary 1) that the TB objective implicitly divides the reward by |Aut(G_n)|. The correction—multiplying the terminal reward by |Aut(G_n)|—is simple, exact, and applicable to both TB and DB without per-step changes.

- **Direct experimental confirmation on a tractable environment.** The small-graph experiment (Section 6.1, Figure 3) provides the strongest evidence: with 2,999 terminal states where exact marginals are computable, the uncorrected TB model's target-to-model probability ratio exactly equals |Aut(x)| (matching the theoretical dashed lines), while the corrected TB+AC matches the oracle TB+RM baseline with near-perfect correlation and low L1 error. This ground-truth validation is a model of how to support a formal claim empirically.

- **Practical benefits demonstrated on real molecular generation tasks.** Table 2 shows consistent improvements from correction on both atom-based (e.g., Diverse Top-K reward 6.3 vs. 5.6) and fragment-based (Top-K reward 0.55 vs. 0.49) tasks. The cyclohexane example (5,220 fragment instances in uncorrected vs. 1,042 in corrected) concretely illustrates the bias in action.

- **Computational efficiency argument supported.** The paper notes that reward scaling requires one automorphism computation per trajectory, while per-step isomorphism testing would cost O(K×T) more. This practical advantage over per-step alternatives (e.g., Ma et al. 2024) is clearly motivated.

- **Extension to fragment-based generation.** Theorem 3 provides a correction formula handling the additional complexities of fragment-based generation, and the unbiased likelihood estimator (Equation 3) correctly accounts for automorphisms.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **No empirical comparison to Ma et al. (2024) on the molecule tasks.** The related work section (line 34) explicitly contrasts the proposed method ("exact and efficient...requiring corrections only once at the end") with Ma et al.'s per-step approximate test. Yet the molecule generation experiments do not include this prior method as a baseline. The paper's claimed advantage over per-step approaches is supported by theory and by the small-graph oracle (TB+RM), but not by a direct head-to-head on the realistic tasks where practical trade-offs matter.

- **The approximate correction method (TB+XC) is underspecified.** Section 5 states that the method "assign[s] a number to each fragment based on how many equivalent actions it is likely to incur during generation" (line 163) and divides the reward by the product of these N(C_i). No rule, heuristic, or procedure for assigning N(C_i) is given. Since TB+XC is presented as a practical alternative and experimental results are reported for it, the lack of specification prevents reproducibility and makes the results difficult to interpret.

- **Theorem 3 (fragment correction) is stated without clarifying the conditions under which the automorphism decomposition is exact.** The formula \tilde{R}(G) = |Aut(G)|R(G) / ∏_i |Aut(C_i)| assumes that fragment automorphism groups factor cleanly when fragments are connected. The paper does not discuss when this holds (e.g., whether fragments are attached at distinguished anchor nodes that break symmetry between fragments) or whether the formula is an approximation in general. The empirical results for fragment-based generation are correlational (proxy reward, no ground-truth target distribution), unlike the atom-based small-graph experiment. A clarifying discussion of the decomposition's conditions would strengthen the theoretical framing.

### Trivial
None.

## Nice-to-Haves

- Report variance or effective sample size for the likelihood estimator (Equation 3), especially for the atom-based task where correlation is low and importance-sampling variance could be high.
- A brief discussion of how reward scaling might interact with training dynamics (e.g., changes to the scale of flow values, implications for learning rate selection) would be helpful.
- A small fragment-assembly environment with known ground-truth rewards (paralleling the small-graph experiment for atom-based generation) would further validate the fragment correction.

## Removed Points

- **"FCS metric is not defined in the main text."** This is factually incorrect. The paper defines FCS at line 204: "Flow Consistency in Sub-graphs (FCS) is the average total variation between the marginal p_S^⊤ and the target (Silva et al., 2024)." Removed as factually wrong.

- **"The fragment correction theorem lacks a derivation"** (when interpreted as a criticism about missing appendix content). The parser strips appendix sections from all papers; a full derivation exists in the original submission. The retained point above (about missing conditions/assumptions in the theorem statement) addresses the substantive concern about clarity.

## Novel Insights

The reviews surface a subtle tension not fully discussed in the paper: the fragment correction formula's clean automorphism-group factorization assumes non-interacting fragment symmetries, which may fail when the connection topology creates new automorphisms across fragments. This is a genuine open question that future work could explore—it does not undermine the paper's core atom-based contribution, which is fully validated. The reviews do not offer additional novel insights beyond the paper's own contributions.

## Suggestions

- Include Ma et al. (2024) as a baseline in the molecule experiments to substantiate the claimed advantage over per-step approximate methods.
- Specify the N(C_i) assignment rule for the approximate correction (TB+XC) to make the method reproducible.
- Add a brief discussion of the conditions under which Theorem 3's automorphism decomposition is exact, or acknowledge when it is an approximation.
- Consider adding a small fragment-assembly environment with tractable ground-truth marginals (analogous to the small-graph experiment) to validate the fragment correction directly.

**Originality**: Strong — the formalization of equivalent action bias and the simple reward-scaling fix are novel and clean.  
**Importance of research question**: High — symmetries in molecular graphs are pervasive (>50% of ZINC250k molecules have >1 symmetry), and biased sampling is a real problem for drug discovery applications.  
**Claims supported**: The core claim (atom-based correction removes bias) is well-supported by theory and the small-graph experiment. The fragment-based claim is less fully validated.  
**Soundness of experiments**: Good overall. The small-graph experiment is rigorous. The molecule experiments are standard and show consistent patterns, though missing a key baseline (Ma et al.).  
**Clarity of writing**: Clear and well-structured. The formalization in Section 4 is precise. The approximate method description is one notable underspecified spot.  
**Value to the community**: High — the correction is simple and immediately applicable to any graph GFlowNet implementation.

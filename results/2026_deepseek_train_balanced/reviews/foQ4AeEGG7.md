## Summary

This paper proposes CauGramer, a graph transformer framework for estimating treatment effects (main, peer, and total) under networked interference when both the interference graph and the peer-treatment aggregation (summary) function are unknown. The method uses L-layer cross-attention with GCN keys/values to learn interference representations from the social network, combines confounder balancing via IPM with minimax bridge moment constraints for outcome regression, and is evaluated on two pseudo-real datasets (BlogCatalog, Flickr).

## Strengths

- **Relaxes two assumptions simultaneously.** Prior work assumes the interference graph is known and identical to the social network (E = A) and uses a pre-specified summary function (sum/average). CauGramer addresses both relaxations at once — the interference graph need not equal the social network, and the aggregation function is learned rather than fixed. This is a genuinely harder and more realistic setting (Section 1, Figure 1).

- **Cross-attention with GCN keys/values for interference representation.** The architectural design — linear-transformed self-features as queries and GCN-aggregated neighbor features as keys/values (Eq. 3–4) — provides a principled mechanism to learn interference representations without reconstructing the interference graph. The ablation study (Table 4) confirms that removing cross-attention ('w/o CA') degrades performance, validating its contribution.

- **Bridge moment constraints provide a second layer of robustness.** Beyond standard IPM balancing of representations, CauGramer adds minimax bridge moment constraints (Eq. 11) that force the residual E[y−ŷ | q(r,t)] = 0 for any bridge function q. The ablation (γ=0 in Table 4) shows that removing these constraints increases estimation error, confirming they add value beyond standard representation balancing.

- **Large and consistent empirical improvements across many settings.** On constant total effect estimation, CauGramer reduces ε_AVG by 39–56% and √ε_PEHE by 46–51% over the best baselines (Table 2). Under *unknown* interference graphs (Figure 3) — including 1st/2nd-order subgraphs and random graphs — CauGramer consistently outperforms all baselines (>35% improvement on subgraph settings). Under limited treatment budgets (Figure 4), CauGramer maintains ATE error below 0.1 while competing methods degrade sharply.

- **NC variant for unmeasured confounders.** CauGramer(NC) incorporates negative control variables into the moment constraints, recovering near-full performance even when features are deliberately withheld (Table 3), demonstrating practical robustness.

## Weaknesses

### Major

1. **The "interference-agnostic" framing overreaches — the method makes a structural assumption that is not acknowledged as such.** The paper states: "all interference nodes must exist within the L-order neighbor network (L is sufficiently large)" (Section 4.1). This is a structural assumption: the interference graph is assumed to be a subgraph of the L-hop closure of the social network A. While this is a *weaker* assumption than prior work (E = A), replacing E = A with E ⊆ A^L is still an assumption about the relationship between the interference graph and the social network. Calling the method "interference-agnostic" is misleading. The paper does not discuss what happens when this assumption is violated (e.g., when interference occurs between nodes far apart in the social network), nor does it provide any diagnostic or sensitivity analysis for choosing L.

2. **The evaluation does not clarify what information baselines receive about the interference graph.** The paper says "For the sake of fairness, we modify all non-interference methods by incorporating neighbors' treatment and social networks as additional input" (line 218), but it does not state whether, in the *known* graph experiments (Tables 2–3), baselines were given the true interference graph E or only the social network A. In the *unknown* graph experiments (Figure 3), it is unclear whether baselines were given the ground-truth E (if known to the experimenter), the social network A, or the same subgraph/random graph inputs. Without this information, the reader cannot assess whether the large improvements (39–56%) reflect genuine methodological superiority or an information asymmetry.

3. **The simulation of the interference graph E is not described.** Since the entire evaluation uses simulated E (the paper states "interference (E) [is] simulated" on line 210), the reader needs to know: (a) how E is generated — specifically whether E is always a subgraph of the L-hop neighborhood of A, and (b) whether the "known graph" condition provides the true E or an approximation. Without this, one cannot assess whether the evaluation setting is aligned with the method's assumptions or tests cases where those assumptions are violated. The paper cites Jiang & Sun (2022) for data simulation, but the description of how E relates to A is absent.

### Minor

4. **No sensitivity analysis for L (network depth).** The choice of L determines the scope of potential interference peers considered. The paper offers no guidance on how to choose L, nor any empirical study of how performance varies with L (e.g., L = 1, 2, 3, 4, 5). Since L is a critical hyperparameter that operationalizes the core assumption, its omission is a gap.

5. **The cross-attention Q/K split is not justified.** The design uses linear(self-features) as queries and GCN(neighbor features) as keys/values. The paper does not explain why this specific assignment is appropriate for modeling interference, as opposed to the reverse or symmetric choices. This is a design choice that merits discussion.

6. **The balancing reformulation reasoning is incomplete.** The paper replaces r_i ⟂ t_{P_i} with {r_j: j∈P_i} ⟂ t_i by stating "the representation r_i serves as a weighted proxy of peer representations {r_j:j∈P_i}" (line 164). Whether a GCN representation truly serves as a "weighted proxy" of its neighbors' peer representations is an empirical claim that is stated without justification.

7. **No code or supplementary material is referenced.** This limits reproducibility for a method with a non-trivial training objective and multiple loss terms.

### Trivial

- Eq. (12) has a clear notation error: `argmin_{α∈Φ} max_{α∈Φ}` uses the same variable α in both the min and max, which is nonsensical. This appears to be a copy-paste error and obscures the optimization objective.

## Nice-to-Haves

- A sensitivity analysis for L (layers/hops) with a validation-based selection strategy.
- An experiment where the interference graph E explicitly *violates* the L-hop subgraph assumption (e.g., long-range edges beyond L hops), to test graceful degradation.
- A clearer statement comparing the method's assumption (E ⊆ A^L) to prior work's assumption (E = A), positioned as a relaxation rather than as "no assumption."

## Removed Points

- **"Causal identification contains a logical gap"** (Harsh Critic #3): The proof in Proposition 1 is a standard oracle-style argument showing identification *if* peer information can be captured from {x, t, A}. The paper then explains that actual identification is achieved through learned representations, not by reconstructing E. This is a conventional approach in causal representation learning, not a logical gap. REMOVED as a strawman.
- **"Typo in Eq. (11) — argmin over ŷ but max over α∈Φ"**: Eq. (11) is correctly written as `argmin_{ŷ} max_{q∈Q}`. This criticism is factually wrong. REMOVED.
- **"Missing proofs in appendix"**: The parser strips appendices from all papers. REMOVED per hard rules.
- **"No code release"** element that might fall under reproducibility nitpick: RETAINED as minor weakness (code not cited, genuine reproducibility concern).
- **Several formatting/style nitpicks**: REMOVED per hard rules.

## Novel Insights

None beyond the paper's own contributions. The reviews primarily surface calibration issues between the paper's framing and its actual assumptions, rather than uncovering unrecognized strengths or weaknesses beyond what the paper itself documents.

## Suggestions

1. **Reframe the contribution honestly.** Replace "interference-agnostic" with a precise statement: the method relaxes the E = A assumption to the weaker assumption that interference peers lie within L hops of the social network. Acknowledge this as a structural assumption and discuss its limitations.
2. **Clarify baseline information.** In a table or paragraph, specify for each experimental condition (known graph, unknown subgraph, random graph) what information each baseline method received about the interference structure.
3. **Describe the simulation of E.** Provide a clear description of how the interference graph E is generated from the social network A (or independently), and whether any of the tested conditions violate the L-hop subgraph assumption.
4. **Add sensitivity analysis for L.** Show how performance changes with L on at least one dataset.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
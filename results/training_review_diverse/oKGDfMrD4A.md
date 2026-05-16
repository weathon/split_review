Now I have all the information needed. Let me compile the final authoritative review.

---

## Summary

This paper studies adversarial robustness on directed graphs, an underexplored direction. It introduces Restricted Directed Graph Attack (RDGA), a threat model that constrains out-link attacks on target nodes (reflecting realistic practical limitations), and proposes Biased Bidirectional Random Walk (BBRW), a plug-in message-passing layer that differentially weights out-links (more trustworthy) and in-links (less trustworthy) via a single hyperparameter β ∈ (0.5, 1). Experiments on Cora-ML and Citeseer under PGD attacks show that BBRW variants significantly and consistently outperform undirected baselines, with a theoretical case study relating β to attack influence minimization.

## Strengths

1. **First systematic study of adversarial robustness leveraging directed graph structure.** While prior work largely treats directed graphs by symmetrizing them (losing directional information), this paper identifies the natural asymmetry — out-links are harder to attack than in-links in many real settings — and builds a defense around it. BBRW's core intuition (out-links more trustworthy, but not fully trustworthy due to indirect 2-hop attacks) is clearly motivated and grounded in examples (Section 1).

2. **BBRW is simple, principled, and effective as a plug-in layer.** The method requires only one hyperparameter (β) and can be dropped into existing GNN backbones (GCN, APPNP, SoftMedian) with minimal overhead. The empirical gains over undirected baselines under RDGA are large and consistent across datasets (e.g., BBRW-SoftMedian achieves 84.5% accuracy under 100% budget adaptive attack on Cora-ML, vs. 73.5% for MLP and 47.5% for SoftMedian).

3. **Theoretical analysis provides principled guidance for β.** Theorem 1 derives an optimal β* minimizing the maximum influence from direct in-link and indirect out-link attacks under a specific local subgraph. The median β* = 0.79 (80% CI: 0.68–0.92) aligns with the empirically optimal range (β ≈ 0.7–0.8 in ablation studies), lending theoretical grounding beyond pure heuristics.

4. **Ablation studies effectively illuminate the working mechanism.** The analyses of adversarial link distributions (Figures 2, 4), the β trade-off (Figure 5), and varying out-link masking rates (Table 4) collectively explain why BBRW avoids the "catastrophic failure" that befalls the naive directed random walk, and clarify when BBRW's advantage shrinks or grows.

## Weaknesses

### Fatal
None.

### Major

1. **Empirical scope is too narrow to support the strongest "state-of-the-art" claims.** The evaluation is limited to two small citation graphs (Cora-ML, Citeseer) and a single attack algorithm (PGD). The paper frames its results as "state-of-the-art robust performance" and "comprehensive comparison" (Abstract, Section 1), but two homophilic graphs and one attack family do not establish generality. Larger graphs, heterophilic graphs, and other attack types (e.g., FGA, Nettack under RDGA, global attacks) are absent. This does not invalidate the results on the tested setting, but it does mean the "SOTA" claim substantially outruns the evidence.

2. **Baseline comparison is structurally conditioned on RDGA, but this is not sufficiently reflected in the paper's claims.** Undirected GNNs symmetrize the graph, so every in-link attack under RDGA effectively becomes a bidirectional edge perturbation, while BBRW's directed aggregation is only affected on one direction. The paper acknowledges this asymmetry (Section 3, line 62: "undirected GNNs will perform the same under both attacks") but still uses unconditional "state-of-the-art" language. The results demonstrate that BBRW outperforms undirected baselines *under the RDGA threat model*, which is a meaningful contribution — but the paper should clearly condition this claim rather than presenting it as generic SOTA robustness.

3. **Missing adaptive attack results for several baselines.** GNNGuard and GRAND (and potentially others) are reported with "—" for adaptive attacks, with the note that gradient computation is non-trivial (Section 4.1). This leaves gaps in the comparison tables, making it impossible for the reader to verify whether BBRW's advantage holds against these methods under the strongest attack setting. At minimum, a transfer-only comparison should be clearly separated, or the authors should provide a reasonable approximation.

### Minor

1. **"Outstanding clean accuracy" is slightly overstated.** On Cora-ML, BBRW variants achieve clean accuracy competitive with — but not generally exceeding — the best undirected models (e.g., BBRW-GCN 82.2 vs. GCN 83.2, BBRW-APPNP 84.7 vs. APPNP 85.0 based on the textual summary). "Comparable" or "competitive" would be more accurate than "outstanding," especially since a small clean accuracy drop in exchange for large robustness gains is expected and acceptable.

2. **Compatibility with existing defenses is only demonstrated with SoftMedian.** The paper claims BBRW is "compatible with existing defense strategies" (Section 3.2) but only tests the combination with SoftMedian. GCN and APPNP are standard backbones, not defense strategies per se. Showing BBRW combined with at least one additional defense (e.g., Jaccard-GCN or GRAND) would substantially strengthen the universality claim.

3. **Theoretical analysis is a case study, not a general proof.** Theorem 1 is derived under a specific local subgraph assumption (a target node, a direct-attacker neighbor, and an indirect-attacker neighbor). The paper presents this appropriately as a "theoretical case study," which is fine — but some readers may interpret "Theorem" as implying broader generality than what is actually proven.

### Trivial

1. **Inconsistent notation in Section 2.2.** The first equation uses $\tilde{\mathbf{A}}^\top$ on the left-hand side (line 51: "the adjacency matrix being attacked is given by $\tilde{\mathbf{A}}^{\top}=...$"), while the second equation uses $\tilde{\mathbf{A}}$ (line 53). This appears to be an inconsistency that should be resolved.

2. **The "catastrophic failure we discover" is listed as a contribution but not previewed in the abstract.** Mentioning this concretely would give readers a stronger hook.

## Nice-to-Haves

- Evaluate on at least one larger directed graph (e.g., ogbn-arxiv directed, a social network, or a financial transaction graph) to test generality beyond small citation networks.
- Add a second attack algorithm under RDGA (e.g., a greedy attack like FGA adapted to the directed setting) to verify that BBRW's robustness is not attack-specific.
- Report per-node β* from Theorem 1 vs. empirical best β to make the theory-to-practice link quantitative rather than qualitative.
- Include runtime/memory overhead of BBRW (expected to be negligible, but easy to report).
- Discuss limitations of the RDGA assumption: in some domains (e.g., financial networks where out-links are payments to accounts the adversary controls), out-links may *not* be harder to fake. A brief limitations paragraph would strengthen the paper.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"The adaptive attack on an MLP should be shown to achieve low accuracy to validate attack strength"** — REMOVED (factually wrong / misunderstands the paper). MLP does not use the graph adjacency matrix, so PGD-based graph structure attacks cannot produce meaningful gradients for an MLP victim. This suggestion reflects a misunderstanding of the attack mechanism.
- **"A symmetric directed attack should be added as a baseline comparison"** — REMOVED (scope creep). The paper's contribution is specifically about RDGA being a more *realistic* threat model. Evaluating undirected baselines under a fundamentally different threat model (symmetric attacks) does not test BBRW's robustness; it tests a different research question. This belongs in future work.
- **Strength Finder: "Comprehensive experimentation validates effectiveness across multiple dimensions"** — REMOVED (conflicts with verified weakness about narrow scope). Two datasets and one attack algorithm is not "comprehensive" for SOTA claims, even if the ablations within that scope are thorough.
- **"The paper lacks related work on X"** — Not present in the reviews; noted for compliance with rules.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's insight that "the comparison validates the threat model as much as the defense" is a useful framing but is essentially a restatement of what the paper partially acknowledges (Section 3, line 62-63). The observation that BBRW's β allows explicit modeling of the trust-asymmetry / indirect-attack trade-off is already the paper's central contribution.

## Suggestions

1. **Condition the "state-of-the-art" claim on the RDGA threat model** throughout the paper. This is accurate and sufficient — BBRW achieves SOTA robustness *under the more realistic RDGA setting* — and avoids overclaiming.

2. **Add at least one more dataset and one more attack algorithm** before the final version. Even one additional dataset (e.g., a directed version of ogbn-arxiv or a social network) and one additional attack (FGA adapted to RDGA) would substantially strengthen the generality of the findings without changing the paper's scope.

3. **Clarify what the "—" entries in the adaptive attack tables mean** and consider providing transfer-only comparisons for those baselines with a clear caveat. If gradient computation is indeed infeasible, state this more prominently and explain what the reader should conclude from the incomplete comparison.

4. **Report a per-node correlation between theoretical β* and empirical best β** from the ablation study. The median β* = 0.79 and empirical optimum 0.7–0.8 are consistent, but making this explicit (e.g., "78% of nodes have β* within 0.1 of the empirical best") would turn the qualitative alignment into a quantitative validation.

## Score and Decision

This paper addresses a genuine gap (robustness in directed graphs), proposes a simple and well-motivated method (BBRW), and provides strong empirical results within its evaluated scope. The core claims are supported by the experiments on the tested datasets. The main limitations are the narrow empirical scope and the overclaiming of "state-of-the-art" without sufficient conditioning on the RDGA threat model — both are addressable in revision. The method itself is clean, principled, and likely to be useful to the community.

I recommend **weak accept**: the contribution is real and the method is solid, but the paper would benefit from expanded evaluation and more measured claims before it can be considered a definitive contribution.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
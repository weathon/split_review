## Summary

This paper theoretically characterizes the expressiveness of a broad class of E(3)-invariant geometric deep learning models. It first proves that DisGNN (message-passing with distances) is nearly E(3)-complete: all unidentifiable point clouds are confined to a measure-zero subspace defined by a novel concept called $\mathcal{A}$-symmetry. It then shows that GeoNGNN — the geometric counterpart of Nested GNN — breaks these corner cases via node marking and achieves full E(3)-completeness. Using GeoNGNN as a theoretical tool, the paper further establishes the E(3)-completeness of a family of geometric subgraph GNNs and three well-established invariant models (DimeNet, GemNet, SphereNet) under fully-connected conditions, revealing that models with different expressiveness in traditional graph learning collapse to the same completeness in the geometric setting.

## Strengths

1. **Rigorous characterization of DisGNN's unidentifiable cases via $\mathcal{A}$-symmetry**: The paper proves that DisGNN's unidentifiable point clouds are precisely the $\mathcal{D}$-symmetric (or $\mathcal{C}$-symmetric) ones, and that this set has measure zero in $\mathbb{R}^{n\times 3}$ (Section 3, Theorem 1, Theorem on measure zero). This goes beyond prior work that only produced isolated counterexamples (Hordan et al. 2023, Pozdnyakov et al. 2022) — it gives a complete characterization of which cases fail and how rare they are, backed by empirical validation on QM9 and ModelNet40.

2. **Proof that models weaker than 2FWL in traditional graph learning become equally E(3)-complete in the geometric setting**: The paper proves that geometric subgraph GNNs, DimeNet, GemNet, and SphereNet are all E(3)-complete (Theorems 4 and 5), despite being strictly weaker than 2FWL in traditional graph learning. The finding that all expressiveness discrepancies among subgraph GNNs "diminish" when extended to geometric scenarios (line 163), attributed to the low-rank nature of distance graphs, is a genuinely surprising and non-obvious theoretical insight.

3. **GeoNGNN's empirical validation on synthetic counterexamples**: GeoNGNN achieves 100% separation on all 17 synthetic counterexample pairs (both isolated and combinatorial) where DisGNN/SchNet scores 0% (Table 2). This directly validates that the theoretical completeness translates to practical discrimination ability under finite numerical precision.

4. **Competitive empirical performance with substantial gains over DisGNN**: On rMD17 (Table 1), GeoNGNN achieves an average rank of 2.55, and the loss ratio of GeoNGNN to vanilla DisGNN averages 1:8.6 (max 1:34.2), demonstrating that the theoretical expressiveness gain translates to real molecular property prediction improvements.

5. **The "identify" concept provides a finer-grained analytical framework**: The paper introduces the notion of a model "identifying" a single point cloud (rather than just distinguishing pairs), noting that each "identify" implies infinitely many "distinguish" pairs (Section 2). This enables the sufficient-condition theorem (Theorem 1) that inspects only the point cloud itself rather than iterating over all possible $P'$, which is a genuine analytical innovation over the pairwise-distinguishability approach used in prior near-completeness studies.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **All completeness results depend on fully-connected distance graphs, sharply limiting practical relevance.** Every completeness theorem (Theorems 3–5) requires $r_{\text{cutoff}} = +\infty$ and $r_{\text{sub}} = +\infty$, while molecular modeling in practice uses cutoff radii around 5Å for computational tractability. The paper acknowledges this in the limitation paragraph (line 281), but the abstract and introduction do not mention this condition, so a casual reader could easily misinterpret the headline claims. The abstract states that DimeNet, GemNet, and SphereNet "are also all capable of achieving E(3)-completeness" without noting the fully-connected requirement — the qualification appears only in the theorem statements. This is a framing issue that should be corrected: the claims are technically correct but easy to over-interpret.

2. **The "implementation" argument for DimeNet/GemNet/SphereNet completeness is sketched too briefly in the main text.** The key idea (line 179) states that edge representations in these models "can be mathematically aligned with the node-subgraph representations tracked in GeoNGNN" and that angles "can all be equivalently expressed by multiple distances." This reduction is the paper's most sweeping claim — it asserts that models with architecturally quite different aggregation schemes can simulate GeoNGNN's two-level subgraph computation. The main text provides only a prose sketch with no equations showing the mapping between representations. The full proof presumably resides in the appendix (which was stripped by the parser), but even a brief algebraic sketch in the main text would significantly strengthen the presentation.

3. **No variance or confidence intervals reported for rMD17 results.** Given that GeoNGNN (avg rank 2.55), MACE (2.50), and 2F-DisGNN (2.25) are close in rank, it is unclear whether these differences are statistically meaningful. Standard practice for energy/force prediction benchmarks would include standard deviations or confidence intervals.

4. **GeoNGNN-C (chirality-aware variant) is mentioned but not defined in the main text** (line 270). If it is a meaningful variant that achieves competitive results on chirality datasets, it deserves at least a brief architectural description in the main text.

5. **The supplementary experiments (MD22, 3BPA, subgraph size ablation) are described in only a few lines** (lines 267–270) with no quantitative results in the main text. The MD22 claim that "2F-DisGNN can hardly be applied" is potentially important for establishing a practical advantage of GeoNGNN over 2F-DisGNN in scalability, but no evidence is presented.

### Trivial

None.

## Nice-to-Haves

- The claim that completeness implies universal approximation (line 45, citing Hordan et al.) could benefit from a brief discussion of the nuances of moving from discrete expressiveness to continuous function approximation on molecular energy surfaces.
- A concrete 3D point cloud example illustrating the hierarchy among $\mathcal{C}$-unsymmetric, $\mathcal{D}$-unsymmetric, and $\mathbb{R}^{n\times 3}_{\text{distinct}}$ sets would help readers build intuition for the paper's main theoretical contribution.
- A simple analysis quantifying how quickly the completeness guarantees degrade as sparsity increases (e.g., on standard molecular benchmarks, what fraction of pairwise distances exceed typical cutoffs?) would help bridge the gap between theory and practice.

## Removed Points

These points were flagged by reviewers but removed after verification against the paper:

- **"Advancement over Hordan et al. (2023) needs qualification"**: The paper clearly proves proper subset relations (Proposition on proper subsets) and demonstrates practical prevalence with tolerance errors on real datasets (lines 96–98). The mathematical advancement is properly characterized; requiring quantification of "how much larger" the sets are is beyond what a theoretical paper needs to establish.

- **"Proof relies on virtual barycenters that cannot be verified without appendix"**: The critic explicitly states they cannot verify because the appendix is not available. Per policy, criticisms about missing proofs in stripped appendices must be removed; the full proof exists in the original submission.

- **"Uncountably infinite mass functions not addressed"**: The paper addresses this by following the standard GIN line of reasoning (line 45): injective multiset functions exist with polynomial complexity, and the analysis assumes such injective constructions.

- **"Abstract overclaims DimeNet/GemNet completeness without caveat"**: While the abstract omits the fully-connected condition (addressed in Minor weakness 1), this is standard practice for theoretical papers — the conditions are stated in all theorem statements. This is merged into Minor weakness 1 rather than standing separately.

- **Strength Finder strengths about "important problem" framing**: All five listed strengths are concrete and evidenced; none are generic. All kept.

## Novel Insights

The most interesting insight that emerges from synthesizing the reviews is that the paper's core finding — that many invariant models collapse to the same completeness in the geometric setting — has an under-explored tension with its own limitation. The paper shows that expressiveness distinctions vanish under fully-connected conditions, but the practical regime where these models differ (sparse molecular graphs) is precisely where the theory does not apply. This creates an interesting open question: does the expressiveness hierarchy re-emerge under realistic sparsity patterns? The paper's "low-rank nature of distance graphs" hypothesis (line 163) suggests that geometric structure inherently reduces the effective dimensionality, but whether this holds under truncation remains unclear and would be a natural direction for future work.

## Suggestions

- Add a brief algebraic sketch in the main text (2–3 equations) showing how a single DimeNet/GemNet aggregation step maps onto a GeoNGNN subgraph computation step, so readers can assess the reduction without consulting the appendix.
- Explicitly state the fully-connected requirement in the abstract ("under fully-connected distance graphs") to prevent misinterpretation of the completeness claims.
- Include standard deviations or confidence intervals for the rMDNN results, or at minimum note whether differences between GeoNGNN, MACE, and 2F-DisGNN are statistically significant.
- Either define GeoNGNN-C in the main text or remove the passing mention; a one-sentence description of its architecture would suffice.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
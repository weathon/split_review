---

## Summary

RADAR is a plug-in framework for neural VRP solvers that equips them to handle asymmetric distance matrices via two components: (1) a truncated SVD-based initialization that produces compact, size-independent node embeddings encoding global directional structure ("static asymmetry"), and (2) Sinkhorn normalization replacing row-wise softmax in encoder attention to enforce doubly-stochastic attention weights ("dynamic asymmetry"). The method is evaluated extensively on 17 synthetic VRP variants, a 16-task multi-task benchmark, and three real-world datasets, consistently outperforming prior neural baselines and achieving strong generalization across problem scales.

---

## Strengths

- **Principled SVD-based initialization with strong theoretical grounding.** Definition 1 formalizes "asymmetry-aware embeddings" and Equations 3–5 demonstrate that the truncated SVD factorization satisfies it by construction, providing two distinct linear projections that can recover the asymmetric cost matrix. The ablation in Table 6 shows this is the dominant contributor: removing SVD while keeping Sinkhorn yields a 22.89% gap at ATSP1000, whereas SVD alone drops it to 7.24%, compared to 38.64% with neither. The size-independence of rank-$k$ embeddings (independent of $n$) is the key architectural enabler of OOD generalization.

- **Clean ablation confirming both components.** Table 6 is a well-designed 2×2 factorial ablation (SVD × Sinkhorn), confirming both components contribute at every scale. The clearest finding is that SVD is responsible for the large generalization jump from ATSP100 to ATSP1000, while Sinkhorn provides additive but consistent improvement throughout.

- **Extensive and rigorous empirical validation.** RADAR is evaluated on 17 synthetic variants (Tables 1–2), real-world ATSP/ACVRP/ACVRPTW (Table 3), a coordinate-ablation study (Table 4), and an asymmetry-level stress test (Table 5). Across all settings, it is the top neural method and achieves a –0.75% gap on ACVRP200 (surpassing LKH-1000). On real-world ATSP, RADAR (0.74% gap) outperforms RRNCO (1.80%) by a wide margin.

- **Coordinate study producing a non-obvious insight.** Table 4 shows that RADAR without coordinates (gap 1.49%) outperforms RRNCO with coordinate augmentation (gap 1.80%), suggesting that for asymmetric tasks, coordinates mainly provide augmentation diversity rather than structural signal—a concrete, reproducible finding with implications for real-world deployment.

- **Strong multi-task generalization.** In the 16-variant RouteFinder setup (Table 2), RADAR achieves 1.33% average gap, outperforming RF-NN (1.99%) and RF (2.47%), confirming the design generalizes beyond single-task settings.

---

## Weaknesses

### Fatal
None.

### Major

- **RRNCO absent from Table 1 (the primary synthetic benchmark) without justification.** RRNCO is introduced in Section 2 as perhaps the closest prior work and features in Tables 3, 4, and 5. Yet it is absent from Table 1, which benchmarks synthetic ATSP100–1000 and ACVRP100–1000. The setup section (§5.1) lists retraining of MatNet, ICAM, ELG, and ReLD "under our setup" but gives no explanation for why RRNCO is excluded. Readers cannot determine whether RRNCO is omitted because it performed similarly to RADAR (which would qualify the headline claims), because it failed to converge on synthetic data, or simply as an oversight. The real-world results clearly favor RADAR over RRNCO, but this does not substitute for a head-to-head comparison on the paper's primary benchmark. The authors should either include RRNCO in Table 1 or explicitly explain why the comparison is not appropriate (e.g., if RRNCO's setup is fundamentally incompatible with the synthetic data generation in §5.1).

### Minor

- **Sinkhorn's theoretical justification is mechanistically imprecise.** Section 4.2 claims that Sinkhorn normalization ensures $A_{i,j}$ "reflects a more complete characterization of both nodes $i$ and $j$, by incorporating the full set of distance-based relations directly connected to them." However, Sinkhorn's column normalization enforces a doubly-stochastic constraint on the attention matrix—it is a global distributional constraint analogous to optimal transport's doubly-stochastic relaxation, not a direct injection of $D_{j,:}$ features into $A_{i,j}$. The empirical evidence for the benefit is solid (Table 6), but the mechanistic explanation as written overstates what Sinkhorn actually does. A more accurate framing would connect it to flow balance in optimal transport, which has a natural structural analog in routing problems. This does not affect the empirical claims but weakens the conceptual contribution's theoretical coherence.

- **Section 5.6 contains essentially no standalone content.** Section 5.6 ("Different Demand Distribution") consists of two sentences ending with "See Appendix C.3 Table 9 for more details" and provides no results or takeaway in the main body. Either the finding should be summarized in one or two sentences, or the section should be folded into the broader discussion rather than standing as an empty subsection.

### Trivial

- **Table 1 HGS presentation is confusing.** HGS achieves negative gaps (e.g., –8.35% on ACVRP500) because it outperforms the reference solver while producing infeasible solutions. The footnote addresses this, but the negative numbers in a "Gap (%)" column suggest HGS is a better solver, which contradicts excluding it as a valid baseline. Presenting feasible-only HGS results, or separating HGS into a clearly labeled "infeasible solver" row, would reduce reader confusion.

---

## Nice-to-Haves

- A comparison of **training time** across baselines would be informative for practitioners. The paper reports 39.31h (ATSP) and 54.74h (ACVRP) for RADAR on a single RTX 3090 but does not contextualize these against MatNet, ICAM, or ReLD training costs. This is not a concern for the method's soundness but matters for deployment.
- An analysis of **SVD reconstruction quality across instance types** (random vs. city vs. cluster from the real-world benchmark) would verify whether the low-rank approximation retains equal fidelity across input distributions. This would strengthen the claim that SVD captures "global structure" under varied real-world distance matrix distributions.
- A more explicit comparison between RADAR's **informed SVD initialization and other informed strategies at equivalent footing** in Table 5 (e.g., including RRNCO and ICAM's full versions as a separate row, with explicit notation distinguishing single-embedding variants) would help readers interpret the isolation experiment more directly, even though the authors do explain the design in §5.5.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic: "Definition 1 is a post-hoc justification rather than a principled characterization."** Removed because while technically true that SVD satisfies Definition 1 by construction, this framing (defining a property and then showing a known decomposition satisfies it) is standard in methods papers. The authors are not misrepresenting anything—Definition 1 serves to formalize the desideratum and show SVD meets it. This is not a methodological weakness.

- **Harsh critic: Table 5 doesn't compare RRNCO/ICAM full versions against RADAR.** Removed as a weakness because the paper explicitly states in §5.5 that single-embedding variants are used "to isolate initialization effects." This is a methodologically valid design choice for the experiment's stated purpose. Retained as a nice-to-have (clearer labeling/presentation).

- **Harsh critic: HGS "contradicts its exclusion as a valid baseline."** Demoted to Trivial since the infeasibility is disclosed in the footnote; the issue is presentation clarity, not a methodological error.

- **Strength Finder: "coordinates are not essential for strong performance" framed as standalone strength.** Merged with the coordinate study bullet above, which provides the same evidence with more context.

---

## Novel Insights

The most genuinely novel empirical insight is the scale of the SVD contribution to OOD generalization: the gap at ATSP1000 jumps from 38.64% (neither SVD nor Sinkhorn) to 7.24% when SVD alone is added, and to 4.13% when Sinkhorn is added on top. This makes a strong case that the *initialization quality* dominates OOD performance in constructive neural VRP solvers for asymmetric instances—more so than architectural choices in the encoder. A secondary insight from Table 4 is that in asymmetric settings, node coordinates appear to provide value primarily through enabling augmentation diversity rather than encoding structural information, since RADAR without coordinates outperforms RRNCO with coordinate augmentation. Together these findings suggest a broader principle: for VRPs defined by distance matrices rather than coordinates, the representational scaffold provided at initialization (not the encoder architecture) may be the principal bottleneck.

---

## Suggestions

1. **Add RRNCO to Table 1 or explain its exclusion explicitly.** If RRNCO's training pipeline is incompatible with the synthetic setup, state why (e.g., its probabilistic neighbor sampling requires real-world calibration); otherwise, retrain and include it.
2. **Replace the Sinkhorn motivation in §4.2** with an optimal-transport framing: doubly-stochastic attention enforces global flow balance analogous to the Birkhoff polytope relaxation of permutation matrices, which is structurally meaningful for routing problems.
3. **Expand Section 5.6** to include at least two sentences summarizing the demand-distribution finding, or fold it into the ablation section.
4. **Report baseline training times** alongside RADAR in the experimental setup to give practitioners a complete cost picture.

---

## Score and Decision

**Originality:** The SVD-based initialization for asymmetric VRP is a concrete, non-obvious idea with clear theoretical grounding. Sinkhorn in attention is a clean adaptation borrowed from the OT literature applied effectively in this context. Both together represent a meaningful methodological advance. *(4/5)*

**Importance:** Asymmetric VRP is practically significant (one-way streets, congestion, directionality) and underserved by the NCO literature. Addressing it with a plug-in framework that generalizes to 1000 nodes has real deployment value. *(4/5)*

**Claims supported:** The core empirical claims are well-supported by Tables 1–6 and the ablation. The one notable evidentiary gap (RRNCO absent from Table 1) is significant but not fatal. *(3/5)*

**Soundness:** Experiments are well-designed and ablated. The Sinkhorn mechanistic claim is imprecise but the empirical validation is solid. *(3/5)*

**Clarity:** Writing is generally clear and structured. Section 5.6 is an empty stub. Figure 1 and the algorithms are informative. *(4/5)*

**Community value:** Strong practical relevance, a plug-in design compatible with multiple backbone solvers, and open generalization to 16 VRP variants. *(4/5)*

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>
Now let me do the calibration search.**Round 1 bracket: 6.0 – 7.5**

RADAR clearly outperforms both the ICAM (avg 6.0, rejected) and TbTJJNjumY (avg 6.25, accepted) anchors. Its asymmetric VRP contribution is more targeted, its ablations are comprehensive, and its real-world benchmarks are a meaningful addition. Let me narrow within 6.0–7.5.Now I have enough anchors. Let me synthesize the full review.

**Round 2 summary:**
- ReLD (4pRwkYpa2u, avg 6.0, accepted) is literally one of RADAR's baselines, outperformed by a large margin
- GM7cmQfk2F (avg 7.0, accepted) is a comparable-tier contribution in MOCO via clean embedding modification, similar depth of empirical validation
- RADAR sits above the 6.0 cluster but the RRNCO Table 1 gap and loose Sinkhorn theory keep it short of 7.5

**Final bracket: 6.5**

---

## Summary

RADAR is a plug-in neural framework for asymmetric vehicle routing problems (VRPs). It decomposes the asymmetry challenge into two complementary components: SVD-based node initialization that encodes global directionality from the asymmetric cost matrix (*static asymmetry*), and Sinkhorn-normalized attention that imposes doubly-stochastic flow constraints on attention weights (*dynamic asymmetry*). Evaluated across 17 synthetic VRP variants, 3 real-world benchmarks, and a multi-task RouteFinder integration, RADAR consistently outperforms all neural baselines and achieves dramatic generalization gains over prior approaches (e.g., 0.72% optimality gap at ATSP100 scaling to 4.13% at ATSP1000 with no fine-tuning).

---

## Strengths

- **SVD initialization is principled and empirically decisive.** Definition 1 + Eqs. (3)–(5) formally show that the concatenated left/right singular vector embeddings satisfy the asymmetry-aware property — they can reconstruct the asymmetric cost via two distinct linear projections. The ablation in Table 6 directly validates the contribution: SVD alone drops the ATSP1000 gap from 38.64% (no SVD, no Sinkhorn) to 7.24%, while the no-SVD+Sinkhorn combination only reaches 22.89%. SVD is responsible for most of the generalization gain.

- **Sinkhorn normalization adds consistent independent gains.** Table 6 isolates its contribution: on top of SVD, Sinkhorn further reduces ATSP100 from 1.19% to 0.72% and ATSP1000 from 7.24% to 4.13%. Appendix D.5 additionally shows faster convergence. The component adds negligible inference overhead (Fig. 4, Section 6.2).

- **RADAR without coordinates outperforms RRNCO with coordinates and augmentation.** Table 4 shows RADAR (w/o coords) achieves 1.49% gap vs. RRNCO (w/ coords + aug) at 1.80% on real-world ATSP in-distribution instances. This is compelling evidence that the SVD-based embeddings capture genuine structural information rather than depending on positional cues.

- **Multi-task integration is validated.** Table 2 shows RADAR achieves 1.33% average gap across 16 asymmetric VRP variants in RouteFinder, outperforming RF (2.47%) and RF-NN (1.99%). This confirms the approach generalizes beyond single-task ATSP/ACVRP.

- **Real-world empirical breadth is strong.** Table 3 evaluates across in-distribution, out-of-distribution (city), and out-of-distribution (cluster) splits on three tasks (ATSP, ACVRP, ACVRPTW) from the RRNCO benchmark, consistently achieving lower gaps than RRNCO (0.74% vs. 1.80% for ATSP in-distribution with augmentation).

---

## Weaknesses

### Fatal
None.

### Major

- **RRNCO is absent from Table 1 (primary benchmark) without justification.** The paper introduces RRNCO (Son et al., 2026) in Section 2 as the closest prior state-of-the-art neural competitor with "context-aware gating, adaptive biases, and distance-based probabilistic sampling," and RRNCO appears in Tables 3, 4, and 5. Yet Table 1 — the primary quantitative benchmark on synthetic ATSP100–1000 and ACVRP100–1000 — excludes it entirely. The baseline list in Section 5.1 explains that MatNet, ICAM, ELG, and ReLD are "retrained under our setup," but gives no analogous statement for RRNCO. A reader cannot tell whether RRNCO was excluded because it underperforms on synthetic data (which would strengthen the paper's claims), because of incompatible data generation assumptions, or for another reason. This is a real evidential gap: Table 1 is the paper's showcase comparison and the strongest neural baseline is missing from it. Either a direct comparison or a clear methodological justification for the omission is needed.

### Minor

- **The theoretical mechanism for why Sinkhorn captures node j's neighborhood context is imprecise.** Section 4.2 (line 107) claims that Sinkhorn normalization ensures A_{i,j} reflects "a more complete characterization of both nodes i and j, by incorporating the full set of distance-based relations directly connected to them." However, Sinkhorn column-normalization enforces that each node's total received attention sums to approximately 1 — a global flow balance constraint. It does not inject D_{j,:} into the score for A_{i,j}; the distance features of j's neighborhood are not explicitly computed into the pairwise score. The empirical benefit of Sinkhorn is real and well-evidenced; the mechanism is better described as enforcing global doubly-stochastic flow balance (an OT/assignment-problem analogy) rather than neighborhood context injection. The imprecision does not invalidate the method but weakens the conceptual framing of "dynamic asymmetry."

- **Table 5 compares informed (RADAR) vs. uninformed (all others) initialization without clearly stating this in the body text.** The footnote markers (‡ vs. †) are noted at the bottom of the table, but the Section 5.5 body text says the comparison is about "initialization strategies" without explaining that ICAM and RRNCO are here stripped to single-embedding variants (without coordinates) to isolate initialization effects. This setup is methodologically reasonable but could mislead readers who don't check the footnote carefully.

### Trivial

- **Section 5.6 (demand distribution)** has no substantive content — it defines the problem, mentions the appendix, and stops. Either summarize the key finding from Appendix C.3 Table 9 in the main text, or merge this into another section rather than leaving it as an empty standalone section.

- **HGS negative gaps in Table 1** are confusing. HGS-Long shows –8.35% on ACVRP500, meaning it outperforms the LKH-10000 reference while yielding infeasible solutions (footnoted). The footnote partially clarifies this, but the signed gap format implies HGS is a strong valid baseline, which contradicts its exclusion from gap computation. Briefly clarifying this in the caption would reduce confusion.

---

## Nice-to-Haves

- A comparison of total *training* times across baselines would help practitioners assess the cost-benefit of the approach. The paper profiles SVD and Sinkhorn inference overhead separately (Sections 6.1–6.2) and reports 39.31h/54.74h wall time (Section 5.1), but doesn't relate these to baselines' training times.

- Connecting Sinkhorn to doubly-stochastic relaxations of permutation matrices (as used in classical assignment and matching literature) would provide a more rigorous theoretical grounding for the dynamic asymmetry component, replacing the imprecise "j's neighborhood" argument with an OT/assignment-based interpretation.

- A brief analysis of how SVD reconstruction quality varies across instance types (random, city, cluster) would strengthen confidence that the low-rank approximation is comparably effective across the real-world benchmarks in Table 3.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic — Definition 1 as "post-hoc justification"**: The critic argued Definition 1 is constructed to guarantee SVD satisfies it, making it a tautology. However, the definition serves a clear pedagogical purpose: it formalizes what kind of embedding can encode asymmetric costs via a bilinear form compatible with attention, and then demonstrates SVD naturally satisfies it. This is standard practice for motivating architectural choices and is not a flaw. **Removed** as a strawman.

- **Harsh Critic — Training time concern**: The critic notes 39.31h/54.74h training times and suggests the paper doesn't justify the cost. Retained as a nice-to-have (comparison with baselines' training costs), but downgraded from a concern to a trivial note, since training time is disclosed and single-run training is the community norm.

- **Strength Finder — "RADAR is the first attempt at tackling asymmetric VRP"**: This framing overstates novelty given RRNCO, MatNet, ICAM etc. have all addressed asymmetric VRPs. **Removed** as delusional/inaccurate framing.

- **Strength Finder — "coordinates not essential"**: This is a valid and well-supported insight (Table 4). **Kept** as a supporting strength (rewritten as the 3rd strength above).

- **Harsh Critic — Section 5.6 is "essentially no results"**: Valid observation, retained as Trivial.

---

## Novel Insights

The most distinctive contribution of this paper, beyond its empirical results, is the identification and operationalization of the static/dynamic asymmetry dichotomy as a structuring principle for neural VRP design. The SVD-based initialization is particularly noteworthy because it produces *size-independent* node embeddings (each of dimension 2k regardless of n) that encode global directional structure — a property neither one-hot (size-constrained) nor k-NN (local, distribution-sensitive) initializations achieve. The ablation showing that SVD alone collapses the ATSP1000 generalization gap from 38.64% to 7.24% — a 5× improvement — is a striking result that suggests that cold-start embedding quality, rather than attention architecture, is the dominant bottleneck for scale generalization in asymmetric NCO. The finding that RADAR without coordinates outperforms RRNCO with full coordinates and augmentation additionally challenges the common assumption that coordinates are always informative in routing: for asymmetric problems, the distance matrix may carry more structural signal than node positions.

---

## Suggestions

1. **Include RRNCO in Table 1**, or provide a clear, methodological explanation for why a direct comparison on synthetic ATSP/ACVRP is not feasible (e.g., incompatible data generation assumptions, or that RRNCO's architecture requires real-world training data). Either result is scientifically useful.

2. **Revise Section 4.2's Sinkhorn justification** to replace the "incorporates j's full neighborhood" framing with a more accurate optimal-transport/doubly-stochastic interpretation. For example: "Sinkhorn normalization enforces a global flow balance — each node receives and sends attention that integrates to approximately 1 — analogous to a doubly-stochastic relaxation of the assignment matrix, which has a natural routing interpretation."

3. **Add a one-paragraph summary of findings to Section 5.6** rather than redirecting entirely to the appendix, keeping the main paper self-contained.

---

## Score and Decision

**Anchor comparison:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| SrnTGdJKYG.md (Neural Decon. Search, VRP) | 3.00 | R1 | Clearly weaker than RADAR |
| NIhRwzqhUz.md (Partially Dynamic TSP) | 3.00 | R1 | Clearly weaker |
| gyTkfVYL45.md (ICAM — one of RADAR's baselines) | 6.00 | R1 | RADAR significantly outperforms ICAM empirically |
| TbTJJNjumY.md (Boosting NCO, large-scale VRP) | 6.25 | R1/R2 | RADAR is comparable in scope and stronger in theory |
| 4pRwkYpa2u.md (ReLD — one of RADAR's baselines) | 6.00 | R2 | RADAR outperforms ReLD by large margin on all benchmarks |
| DKfcxPxunu.md (Multi-Task VRP, Zero-Shot Gen.) | 5.75 | R2 | RADAR more principled and empirically stronger |
| yEwakMNIex.md (Unified NCO via matrix encoding) | 6.25 | R2 | Comparable scope, RADAR has stronger asymmetric handling |
| GM7cmQfk2F.md (MOCO via neat weight embedding) | 7.00 | R2 | Most comparable: both clean embedding modifications with comprehensive ablations; RADAR has broader benchmark scope but slightly weaker theory |

**R1 bracket:** 6.0–7.5  
**R2 narrowing:** RADAR is clearly above the 6.0 anchors (ReLD, ICAM — which it outperforms directly) and comparable to GM7 (avg 7.0). The main factor keeping it from 7.0 is the unexplained RRNCO absence from Table 1, which is a genuine evidential gap, and the imprecise Sinkhorn theoretical motivation. Positioning: 6.5.

**Axis evaluation:**
- *Originality*: High — SVD-based asymmetric initialization is novel and principled
- *Importance of research question*: High — real-world VRPs are asymmetric; this gap is well-motivated
- *Claims well-supported*: Mostly yes — Table 6 ablation is clean; RRNCO gap in Table 1 is the main concern
- *Soundness of experiments*: Good — 17 synthetic variants, real-world benchmarks, asymmetry analysis
- *Clarity of writing*: Good overall, with minor issues in Section 4.2 and 5.6
- *Value to research community*: Meaningful — provides an immediately applicable plug-in with strong OOD generalization

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
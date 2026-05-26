Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper proves novel theoretical bounds on the connectivity graph of the polyhedral complex formed by fully-connected ReLU networks. The main results establish that (i) the average degree of this graph is at most twice the input dimension, regardless of network depth/width, and (ii) the graph diameter has an upper bound independent of input dimension. The paper also presents an enumeration algorithm and provides empirical validation on synthetic and real-world datasets.

## Strengths

1. **Novel average-degree upper bound (Theorem 3.4).** The proof that the average degree of the connectivity graph is at most \(2d\) for any fully-connected ReLU network is the first result of its kind for deep networks with bent hyperplanes. The inductive argument via BH removal (Lemmas 3.2–3.3) elegantly extends the classical hyperplane-arrangement bound to the deep setting. The proof sketch in the main text is adequately detailed, with the full proof deferred to the appendix.

2. **Diameter bound independent of input dimension (Theorem 3.8).** The upper bound \(O(m^\ell)\) on the connectivity-graph diameter does not involve the input dimension \(d\), despite the number of regions growing exponentially in \(d\). This is a surprising and non-trivial theoretical insight. Experiments in Section 5.1 (Fig. 5) confirm that for fixed architectures, the estimated diameter is nearly identical across different values of \(d\), consistent with the bound's prediction.

3. **Empirical confirmation of asymptotic tightness.** The synthetic experiments (Section 5.1, Table 1, Fig. 4) systematically show that the average degree approaches the upper bound \(2d\) as network width/depth increase. For \(d=4\) with width 16 and depth 4, the average degree is \(7.85 \pm 0.03\) (bound 8); for \(d=5\) with the same architecture it is \(9.80 \pm 0.03\) (bound 10). The distributions are unimodal and right-skewed, consistent with the theoretical characterization.

4. **Interesting empirical observation about data-dependent connectivity.** Using the enumeration algorithm, the paper discovers that polyhedra containing training data tend to have higher neighbor counts than those that do not (Section 5.2, Fig. 6). This observation holds across all three datasets, including MNIST where full enumeration is performed, and thus is not an artifact of partial sampling.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **Theorem 3.5 (lower bound) is stated without proof.** The paper asserts: "It is more straightforward to establish the following lower bound…" and then states Theorem 3.5, but provides no proof or proof sketch — unlike every other theorem in the paper, which receives at least a reasoning outline. While this result is not central to the paper's main contributions (it is not listed among the theoretical properties in the introduction), presenting an unsubstantiated claim as a theorem is academically sloppy. The authors should either provide a proof (including for deep networks, where later-layer BHs could in principle cut away faces contributed by first-layer hyperplanes) or explicitly state it as a conjecture/observation rather than a theorem.

2. **Potential sampling bias in the data-connectivity experiment not discussed.** For the CIFAR10 and California Housing experiments, the comparison between data-containing and non-data polyhedra relies on a partial BFS enumeration (capped at 8M polyhedra) starting from a single seed. The set of non-data polyhedra found by this BFS may not be a representative sample of all non-data polyhedra, yet the paper does not acknowledge this potential bias or discuss why the qualitative conclusions are still believed to be valid. (The MNIST case uses full enumeration and is not subject to this concern, which somewhat mitigates the issue.)

3. **Maximum-degree fact for the diameter lower bound is not stated.** Theorem 3.8 gives a lower bound \(\Omega(\ln(N_d(\mathcal{C}))/\ln(n))\), which follows from the graph having maximum degree \(\le n\). This fact (each polyhedron has at most one neighbor per BH, hence degree \(\le n\)) is never stated explicitly, making the lower-bound derivation less transparent than it should be.

4. **No complexity or runtime discussion for the enumeration algorithm.** Algorithm 1 is applied to networks with millions of polyhedra (and presumably millions of LPs solved), yet the paper provides no analysis of its computational complexity or empirical runtime. A brief discussion of resources required would aid reproducibility.

### Trivial

- The proof sketch for the induction step in Theorem 3.4 (removing a BH and relying on the resulting complex still being a "ReLU complex") is terse and would benefit from a sentence clarifying why the induction hypothesis applies after removal, though the appendix presumably fills this gap.

## Nice-to-Haves

- A controlled validation of the data-connectivity claim on a small synthetic network (e.g., those in Section 5.1) where full enumeration is possible and the comparison is between data-containing and randomly sampled non-data polyhedra would strengthen the empirical story and eliminate any residual bias concerns.
- A brief remark that the maximum degree of the connectivity graph is \(\le n\) (each BH contributes at most one face per polyhedron) would make the diameter lower bound derivation self-contained.

## Removed Points

These points were flagged by the reviewers but are removed for the reasons stated:

1. **Theorem 3.5 is "listed as a theoretical property in the introduction" (Harsh Critic).** *Removed because it is factually incorrect.* The introduction lists exactly three theoretical properties (average degree ≤ 2d, average approaches the bound, diameter bounded above by \((m+1)^\ell\)); the lower bound of Theorem 3.5 is not among them. The core criticism (the theorem is unproven) is retained as a Minor weakness.

2. **Proof sketches for Theorems 3.1/3.4 are insufficiently justified (Harsh Critic, Section-by-Section).** *Removed because the critic acknowledges this is "acceptable given page constraints" and that the appendix would fill the gap. The paper clearly states that detailed proofs are in Appendix B and provides non-trivial outlines in the main text.

3. **Generic concerns about the data-connectivity experiment being entirely unconvincing (Harsh Critic, Critical Issues).** *Downgraded from "evidential gap" to Minor because the MNIST experiment uses full enumeration and is not subject to the claimed bias. The critic's characterization of the evidence as unpersuasive overstates the problem; the real issue is only that the partial-enumeration cases lack a bias discussion.

4. **"Exact enumeration algorithm" as a strength (Strength Finder).** *Kept but slightly softened* — the algorithm is a modification of prior BFS-based approaches (as the paper acknowledges), with the novelty being the explicit construction of the connectivity graph during traversal.

5. **Theorem 3.5 lower bound as a strength (Strength Finder).** *Removed because it conflicts with the verified weakness that the theorem is unproven.

## Novel Insights

Beyond the paper's own contributions, the reviews do not surface any genuinely novel observations not already present in the paper. However, the convergence of the two independent assessments — both agree that the average-degree upper bound is the strongest result and that the data-connectivity experiment would benefit from tighter controls — reinforces that the paper's core theoretical contribution is solid while its empirical periphery has room for improvement.

## Suggestions

- Provide a proof (or at least a sketch) for Theorem 3.5, or demote it from "Theorem" to "Observation/Conjecture" with an explicit caveat.
- Add a paragraph in Section 5.2 acknowledging the potential sampling bias of the partial BFS enumeration and explaining why the qualitative trend is still believed to hold (e.g., by noting that the MNIST full-enumeration case shows the same pattern, and that the BFS frontier is broad).
- State explicitly in Section 3.2 that each polyhedron has at most \(n\) neighbors (one per BH), which directly implies the degree bound used in the diameter lower bound.
- Include a brief complexity/runtime analysis of Algorithm 1 in Section 4.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>
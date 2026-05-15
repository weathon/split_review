Now I have all the information I need. Let me compose the final consolidated review.

---

## Summary

This paper generalizes uniform downsampling with anti-aliasing from classical signal processing to signals on arbitrary finite groups. It contributes (a) an algorithm that selects a proper subgroup given a group and a downsampling rate, (b) a Subgroup Sampling Theorem that defines bandlimitedness for signals on groups, and (c) an optimization-based equivariant anti-aliasing operator. Experiments on rotated MNIST and CIFAR-10 with G-CNNs show that subgroup subsampling reduces parameter count and that the proposed anti-aliasing improves equivariance and orbit accuracy.

## Strengths

- **Principled generalization of subsampling to finite groups.** Algorithm 1 provides a concrete, well-defined procedure for producing a proper subgroup given a group \(G\) and rate \(R\), resolving the ambiguity in prior work (Cohen & Welling 2016; Xu et al. 2021) where subgroup choice was not tied to a rate. Lemma 1, Lemma 2, and Claim 1 establish conditions under which the output is guaranteed to be a proper subgroup.

- **Subgroup Sampling Theorem with explicit bandlimitedness condition.** Claim 2 states that perfect reconstruction from a subsampled signal on a subgroup is possible if Fourier coefficients lie in a specific eigenspace. Example 3 shows this reduces to the classical low-pass condition for cyclic groups, and Table 1 verifies zero reconstruction error (up to numerical precision) on \(C_n\) and \(D_{2n}\), confirming the theory works in practice.

- **Equivariant anti-aliasing via constrained optimization.** Eq. 15 jointly enforces equivariance (via the Reynolds operator penalty) and smoothness (via the graph Laplacian), producing a filter that is not merely a projection but respects group structure. Figure 3 shows that for \(C_{16}\to C_8\) the learned filter resembles the sinc function, demonstrating the method recovers classical anti-aliasing as a special case.

- **Empirical evidence of improved equivariance and accuracy.** Table 2 shows consistent improvements: e.g., on rotated MNIST with \(SO(2)\) and \(R=4\), orbit accuracy increases from 56.42 % to 65.90 % and equivariance error drops from 0.132 to 0.056 when anti-aliasing is added, while parameter count is nearly halved.

## Weaknesses

### Fatal

None.

### Major

None that threaten the paper's core claims. The theoretical framework is sound, the empirical results show clear (if moderate) improvements, and the paper is transparent about limitations.

### Minor

- **Subgroup selection heuristic is acknowledged as ad-hoc and empirically under-justified.** The paper states (line 228) that "choosing the subgroup is a key hyperparameter" and that the heuristic (decompose \(R\) into prime factors, pick generators with max order) is a rule-of-thumb. Table 3 shows that for many sampling rates/layers, non-heuristic subgroup choices perform comparably or better on some metrics. While the paper is candid about this, it means the method as a whole is a framework with a tunable component rather than a fully specified recipe. The heuristic works reasonably well but is not uniquely justified.

- **Empirical evidence is limited in scale and scope.** Experiments use only MNIST (with a nonstandard 7-class split) and CIFAR-10, with a single small 3-layer G-CNN. The paper acknowledges this limitation (line 396). For a theoretical paper, proof-of-concept experiments are acceptable, but the small scale means the practical significance of the anti-aliasing gains (often a few percentage points in orbit accuracy) is unclear. A single larger-scale experiment (e.g., deeper G-CNN on CIFAR-10, or STL-10 as mentioned) would substantially strengthen the empirical contribution.

- **No analysis of sensitivity to the optimization hyperparameter \(\lambda\).** The equivariant anti-aliasing filter depends on \(\lambda\) (Eq. 15, balancing equivariance and smoothness). The paper does not report how varying \(\lambda\) affects equivariance error or classification accuracy. If the filter is robust to \(\lambda\), that is a plus; if sensitive, guidance for practitioners is needed.

- **Cost analysis of the anti-aliasing filter computation is missing.** The paper notes the subgroup selection algorithm scales quadratically with edges in the worst case, but does not report the wall-clock time to compute \(\mathcal{M}^*\) for the groups used (e.g., \(D_{24}\) with 48 elements), nor the per-forward-pass overhead of applying the projection. This makes it difficult for practitioners to assess feasibility for larger groups.

- **Claims about prior work's lack of "notion of rate" are slightly overstated.** The paper correctly notes that Cohen & Welling (2016) and Xu et al. (2021) require the subgroup to be specified rather than derived from a rate. However, in practice these works do specify subgroups (e.g., \(C_4\) from \(C_8\)), which implicitly corresponds to a rate. The novelty is in making this correspondence explicit and principled, not in solving a previously unrecognized problem. The contribution remains solid but the framing could be more precise.

### Trivial

- The remark about "disrupt the symmetry assumption" for digits 0,2,4 is clearly explained (lines 362–363) and follows Wang et al. (2023). The reviewer's characterization of this as "nonstandard" is inaccurate — it is a standard practice in equivariance research to remove digits whose labels change under the group action. This point is removed from the weakness list (moved to Removed Points) as it reflects a misunderstanding of the literature, not an error in the paper.

## Nice-to-Haves

- **Hand-designed smoothing baseline.** Replacing the optimized projection with a group convolution using a fixed smoothing kernel (e.g., Gaussian on the Cayley graph) would test whether the expensive optimization is necessary or whether simpler filters suffice.
- **Analytic construction of \(\mathcal{M}\) for common groups.** For cyclic and dihedral groups, a closed-form expression for \(\mathcal{M}\) (extending Example 3 beyond cyclic groups) would remove the need for optimization and provide stronger theoretical guarantees.
- **Per-layer equivariance breakdown** in the image classification experiments, to show which layers benefit most from anti-aliasing.

## Removed Points

These points are flagged for removal; treat them with caution.

1. **"No comparison against existing group subsampling methods (Cohen & Welling 2016, Xu et al. 2021)."** — The paper does compare subsampling without anti-aliasing (which represents prior practice: these works do not include anti-aliasing) against subsampling with anti-aliasing (proposed). Table 3 compares different subgroup choices, and §A2.1 reports results incorporating index selection from Xu et al. The key novelty is anti-aliasing for groups, which is absent from prior work, so the baseline in Table 2 (no anti-aliasing) is the correct comparison. A direct head-to-head against specific subgroup choices from prior papers would be a nice addition but is not a missing necessary baseline.

2. **"Claim 2 is definitional rather than a theorem."** — This mischaracterizes the contribution. Claim 2 provides a sufficient condition for perfect reconstruction with a proof (deferred to appendix), which is exactly what a sampling theorem does. Example 3 shows it subsumes the classical Nyquist condition for cyclic groups.

3. **"Validation of Claim 2 is tautological."** — The reconstruction experiment (Table 1) empirically verifies that the optimization finds an \(\mathcal{M}\) satisfying the theoretical conditions, and that without the projection (anti-aliasing) reconstruction fails. This is a standard sanity check, not a tautology.

4. **"MNIST data removal of digits 0,2,4 is nonstandard."** — The paper clearly justifies this using the symmetry argument from Wang et al. (2023): these digits change identity under rotation/reflection, so they break the equivariance assumption. This is standard practice in the equivariance literature.

5. **"Missing comparison to Gaussian blur as anti-aliasing."** — The paper proposes a principled, learnable anti-aliasing operator. A Gaussian blur baseline is not a standard expectation for a theory paper and falls outside the paper's stated scope. Moving to Nice-to-Haves.

## Novel Insights

The reviews do not surface an insight that goes beyond the paper's own contributions. The paper itself correctly identifies the key insight: that subsampling on groups can be understood as replacing a generator with its \(R\)-th power in the Cayley graph, and that bandlimitedness for subgroup subsampling corresponds to a projection onto a specific eigenspace defined by an \(\mathcal{M}\) matrix satisfying Eq. 10.

## Suggestions

1. **Add a direct comparison** using subgroups chosen by the heuristics of Cohen & Welling (2016) and Xu et al. (2021) as additional rows in Table 3. This would definitively address the reviewer's concern and cleanly separate the value of the subgroup selection algorithm from the value of anti-aliasing.

2. **Report sensitivity to \(\lambda\)** for a representative setting (e.g., \(C_{24}\to C_{12}\) on rotated MNIST): show \(\mathcal{L}_{\mathrm{Equi}}\) and \(\mathrm{Acc}_{\mathrm{orbit}}\) as a function of \(\lambda\).

3. **Provide wall-clock time** for computing \(\mathcal{M}^*\) and per-forward-pass overhead, even for the small groups used. A brief complexity analysis (e.g., "optimization runs in \(X\) seconds on a single GPU; the projection adds \(Y\%\) to the forward pass") would make the paper much more useful to practitioners.

4. **Include at least one experiment on a deeper architecture** (e.g., a 5–7 layer G-CNN or a G-ResNet on CIFAR-10) to demonstrate that the benefits persist at larger scale.

## Score and Decision

The paper makes a genuine theoretical contribution with clean generalizations of subsampling, bandlimitedness, and anti-aliasing to finite groups. The empirical validation is adequate for a theory paper but falls short of demonstrating broad practical impact. The weaknesses are all minor or addressable; no fatal flaws exist. The paper would be strengthened by the additional experiments and analysis listed above but is fundamentally sound in its current form.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
Now I have enough information to write the final consolidated review. Let me carefully evaluate each claim from the harsh critic against the actual paper content.

---

## Final Consolidated Review

## Summary

Medix proposes a median-centric framework for out-of-distribution (OOD) detection using unlabeled "in-the-wild" data. The method first extracts candidate OOD samples from a wild mixture via an iterative greedy algorithm that removes points whose gradients cause the element-wise median (EWM) to deviate most from the average InD gradient, then trains a binary OOD detector using the identified outliers and labeled InD data. The paper provides theoretical bounds on the misclassification rates of EWM-based filtering and reports strong empirical results across two InD datasets and five OOD test sets, outperforming 20 baselines including WOODS, OE, and KNN+.

## Strengths

1. **State-of-the-art empirical performance.** Tables 1 and 2 show that Medix achieves the lowest average FPR95 across both CIFAR-10 (0.80%) and CIFAR-100 (5.42%) among 20 baselines, with results averaged over five runs and reported with standard deviations. The improvement over WOODS (3.40% → 0.80% on CIFAR-10; 6.74% → 5.42% on CIFAR-100) is consistent across all five OOD test sets. These results are obtained under the same evaluation protocol as prior work, enabling direct comparison.

2. **Novel and principled use of the median for outlier filtering in wild data.** The paper observes (Figure 1) a monotonic increase in the L2 deviation between the average InD gradient and the EWM of wild-set gradients as more OOD samples are added. Using the EWM as a robust centrality estimate for gradient filtering is well-motivated, and the approach differs qualitatively from prior threshold-based filtering methods (e.g., Du et al. 2024a).

3. **Theoretical analysis of median-based filtering bounds.** Theorems 4.1 and 4.2 provide misclassification bounds decomposed into contamination, concentration, and separation effects. The bounds formalize the intuition that median filtering remains stable when the OOD proportion is below 50%. The paper also provides a looser bound (Theorem C.3, Appendix C.3) that drops the sub-Gaussian assumption, showing robustness of the core guarantee under only bounded second moments.

4. **Controlled synthetic experiment validates filtering accuracy.** Figure 2 demonstrates that Medix correctly flags 87.5% of true OOD samples in a 2D Gaussian mixture while misclassifying only 12.5% of InD points, providing direct evidence that the outlier extraction stage works as intended.

## Weaknesses

### Fatal

None.

### Major

1. **Theory–algorithm gap: the theoretical bounds do not directly apply to the iterative greedy algorithm (Algorithm 1) presented as the method.** The theorems analyze an "EWM filtering rule" that is not explicitly defined in the main text and does not obviously correspond to Algorithm 1's iterative leave-one-out, top-k removal procedure. Algorithm 1 is described as a "greedy approximation" to the intractable optimization in Eq. (4), but the paper provides no analysis of how close its output is to the optimal subset, nor does it prove that the iterative procedure inherits the theoretical guarantees. The abstract and introduction claim "error bounds that demonstrate Medix achieves a low error rate" and "theoretical guarantees that demonstrate Medix achieves a low error rate," which implies the bounds directly certify the algorithm that is actually run. The paper would be significantly strengthened by either (a) modifying the algorithm to match the analyzed rule, (b) providing a theoretical argument connecting Algorithm 1 to the bounds, or (c) clearly stating that the theory applies to a simplified proxy and explaining how it informs (rather than proves) the algorithm's performance. As it stands, readers cannot verify that the algorithmic contribution is the one being theoretically justified.

2. **Hyperparameter selection protocol is not clearly validated.** The paper states that hyperparameters ε and k are "selected from the sets {5e-5, 5e-4, 5e-3, 5e-2} and {4k, 7k, 10k, 20k}, respectively, taking into account dataset sizes and with the objective of maximizing OOD performance." It does not specify whether this selection uses a held-out validation set or the test OOD data. If the same OOD test sets used in Tables 1–2 were used to guide hyperparameter choices, the reported results could be optimistically biased. The paper mentions a sensitivity analysis in Appendix A.2 (stripped from the arXiv version), which would partially address this concern, but the ambiguity in the main text is serious enough that the authors must clarify the validation protocol in a revision.

### Minor

1. **CONJ and DRL are listed as baselines but do not appear in the main results tables.** Section 5.1 states that the comparison "included more recent baselines, including CONJ (Peng et al., 2024) and DRL (Zhang et al., 2024)," and the conclusion claims Medix "outperformed state-of-the-art methods such as WOODS and DRL." Yet Tables 1 and 2 contain no row for CONJ or DRL. The paper mentions a comprehensive comparison in Appendix A.3, but the main text should at minimum state that these results are deferred and show that Medix outperforms them, to avoid misleading the reader.

2. **Key quantities in the theorem statements are undefined in the main text.** The bounds in Theorems 4.1 and 4.2 use \(m_{\min}\), \(m_{\text{in}}\), and \(m_{\text{out}}\) without definition. Readers must consult the appendix (which is stripped from the arXiv version) to interpret the bounds. Similarly, the "EWM filtering rule" itself is not described as a concrete decision procedure in the main text. While the appendix presumably fills these gaps, the main text should be self-contained on these points.

3. **The 50% contamination bound does not cover the experimental setting.** Theorem 4.1 requires \(\pi < 0.5\) for the contamination term to be controlled, but the experiments use \(\pi = 0.5\). At the boundary, the bound's contamination term \(\pi/[2(1-\pi)]\) diverges, making it vacuous. The paper should acknowledge this and, ideally, provide an analysis or experiment that covers the \(\pi = 0.5\) case used in evaluation.

4. **The sub-Gaussian assumption is empirically validated on labeled InD data, not on wild InD points with pseudo-labels.** Theorem 4.1 assumes "gradients of InD points in \(\mathcal{S}_{\text{wild}}\) are i.i.d. and each coordinate is sub-Gaussian." The empirical evidence in Remark 4.3 (Figure 4a) shows a histogram of gradient values for "InD samples," but the paper does not specify whether these are from the labeled training set or from the wild set with pseudo-labels. Since the algorithm uses pseudo-labels for wild samples (Algorithm 1, line 1), the sub-Gaussian behavior of wild InD gradients under pseudo-labels is not directly validated. The paper mentions that pseudo-label quality is studied in Appendix A.5, but the main text should acknowledge this caveat.

### Trivial

- The "40.98% improvement" over KNN+ is an absolute difference in FPR95 (46.40% → 5.42%), not a relative improvement. While the precise meaning can be inferred from the tables, making this explicit (e.g., "40.98 percentage points") would avoid ambiguity.
- Computational cost is deferred to Appendix A.6. A brief note on per-iteration complexity or wall-clock time in the main text would help readers assess practicality.

## Nice-to-Haves

- A tighter integration between the theory and algorithm would substantially strengthen the paper. Proving that Algorithm 1's output approximates the solution of Eq. (4) within a bounded error, or modifying the algorithm to match a simple one-shot median-threshold rule that the theorems directly analyze, would remove the current disconnect.
- Results under the \(\pi = 0.5\) regime with a modified bound (or an argument that the bound is not tight and the method works well in practice) would cover the experimental setting.
- A validation-based hyperparameter selection protocol (e.g., using a held-out InD/OOD split of the wild data) would eliminate concerns about test-set overfitting.

## Removed Points

These points were flagged for removal; they are listed here for completeness but should be treated with caution:

- *"The EWM filtering rule is never explicitly defined"* — The appendix (Appendix C) likely defines the rule and provides proofs; the main text is not fully self-contained, but this is a presentation issue rather than a substantive gap. The more substantive point (theory does not match Algorithm 1) is retained above as Major weakness #1.
- *"Figure 4a uses gradients from the labeled training set (true labels)"* — The paper does not explicitly state the provenance of the gradients in Figure 4a; this is an inference. Retained as Minor #4 with softened language about the caveat.
- *"The claim of a 40.98% improvement is stated without clarifying absolute vs. relative"* — Trivial presentation issue, retained as such.
- *"Computational cost deferred entirely to the appendix"* — Acknowledged as a nice-to-have; moved to Trivial.
- *"The paper's central thesis... requires bridging the theory-algorithm gap"* — Already addressed by Major #1.
- *"Clarify the role of pseudo-labels"* — Already addressed by Minor #4.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a clear tension between the theoretical framing and the algorithmic implementation, but no insight that reorganizes or extends the paper's findings.

## Suggestions

1. **Clarify the connection between Algorithm 1 and the theoretical bounds.** At minimum, state explicitly whether the bounds apply to Algorithm 1 or to a simplified decision rule. If the latter, describe the simplified rule and explain how the results inform (but do not prove) the algorithm's behavior.
2. **Specify the hyperparameter validation protocol.** State whether a held-out validation set was used, and if so, describe its composition. Provide results with a fixed hyperparameter configuration across all OOD test sets to demonstrate robustness.
3. **Add CONJ and DRL to the main tables or add a footnote with a summary comparison.** The reader should not have to consult the appendix to verify the claim that Medix outperforms these methods.
4. **Define \(m_{\min}, m_{\text{in}}, m_{\text{out}}\) and the "EWM filtering rule" in the main text** so that the theorem statements are interpretable without the appendix.
5. **Acknowledge the \(\pi = 0.5\) boundary issue** and discuss its implications for the bounds.

## Score and Decision

The paper presents a novel median-based filtering approach with strong empirical results across a comprehensive set of benchmarks. The main concerns are the misalignment between the theoretical analysis and the implemented algorithm, and the lack of clarity on hyperparameter selection. These are significant but not fatal — the empirical contribution is substantial enough to carry the paper, and the theoretical part, while disconnected, still provides useful intuition. With clarifications and minor revisions, the paper would be a solid contribution.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
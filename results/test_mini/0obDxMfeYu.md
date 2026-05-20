Now I have sufficient calibration context. Let me write the consolidated review.

**Calibration analysis:**
- Round 1 bracket: papers scoring 3.5-7.5 are most relevant; strong anchors (>7.5) are on different topics and not useful.
- Round 2 narrowing: GradPCA (avg 5.60, Accept Poster) is a gradient-based OOD detection method with NTK theory — it has unclear algorithm descriptions and insufficient baselines. Fisher-Rao (avg 6.00, Accept Poster) has a theoretical framework but was criticized for weak theory-method alignment.
- The paper under review is stronger than GradPCA (more comprehensive experiments, cleaner theory, more challenging problem setting) and slightly stronger than Fisher-Rao (theory directly supports the method, better empirical results against 20 baselines).

**Final score: 6.5** — good paper with a novel contribution, strong empirical results, and solid theory. A few minor issues need addressing but nothing that threatens the core contribution.

---

## Summary

This paper proposes **Medix**, a framework that uses the element-wise median (EWM) of gradients to filter out-of-distribution (OOD) samples from unlabeled wild data, then trains a binary OOD detector on the identified outliers and labeled in-distribution (InD) data. The paper provides theoretical bounds (Theorems 4.1 and 4.2) on both inlier and outlier misclassification rates during the filtering stage, driven by contamination, concentration, and separation effects. Extensive experiments on CIFAR-10 and CIFAR-100 across 11 InD-OOD pairs show Medix outperforming 20 baselines.

## Strengths

1. **Novel and well-motivated method design.** The use of element-wise median (EWM) of gradients for filtering outliers from wild data is genuinely new in the OOD detection literature. The empirical motivation (Figure 1) showing that EWM deviation increases monotonically with OOD contamination is convincing, and the connection to median robustness (50% breakdown point) is clearly articulated.

2. **Rigorous theoretical guarantees.** Theorems 4.1 and 4.2 provide provable upper bounds on both inlier and outlier misclassification rates, controlled by contamination, concentration, and separation effects. This is one of very few works (alongside Du et al. 2024a) offering theoretical foundations for the in-the-wild setting. The sub-Gaussian assumption is empirically validated (Figure 4), and a looser version under only bounded second moments is provided (Theorem C.3 in appendix).

3. **Consistent state-of-the-art empirical results.** Medix achieves an average FPR95 of 0.80% on CIFAR-10 (vs. WOODS' 3.40%) and 5.42% on CIFAR-100 (vs. WOODS' 6.74%), outperforming 20 baselines across all datasets. These results are particularly impressive given that Medix uses only 25,000 labeled InD samples while many baselines use 50,000.

4. **Relaxation of structured mixing assumptions.** The paper explicitly addresses that prior methods (WOODS, Du et al. 2024a) assume batch-level structured mixing of InD and OOD samples, while Medix operates with dataset-level mixing, making it more applicable to real-world outsourced datasets.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Undefined symbol \(m_{\min}\) in Theorem 4.1.** The term \(m_{\min}\) appears in the bound  
   \(\text{ERR}_{\text{in}} \leq \frac{1}{m_{\text{in}}} + 2\sqrt{\frac{\log(1/\delta)}{2m_{\min}}} + \frac{\pi}{2(1-\pi)}\)  
   but is never defined in the main text. It presumably refers to \(\min(m_{\text{in}}, m_{\text{out}})\) or a related quantity, but the theorem statement is not self-contained. The proof in Appendix C (stripped by the parser) likely defines it, but the main text should be clear. This is a presentation issue that does not invalidate the theoretical contribution and can be fixed with a single sentence.

2. **Computational description of Algorithm 1 is underspecified.** The leave-one-out computation of \(\delta_i = d_t - \|\text{EWM}(G_{\mathcal{S}\setminus\{i\}}) - \bar{\nabla}_{\text{in}}\|\) for every \(i \in \mathcal{S}\) at each iteration appears expensive at first glance. The paper acknowledges the computational challenge and defers to Appendix A.6 (computational efficiency), which exists in the original submission. However, the main text would benefit from a brief note on how this is implemented efficiently (e.g., via coordinate-wise sorted lists for incremental median updates, or a minibatch approximation) — especially since \(|\mathcal{S}_{\text{wild}}| = 25{,}000\) in the experiments. The authors clearly ran the algorithm successfully (they provide code and report results), so this is a presentation gap, not a fatal flaw.

3. **OE baseline protocol needs clarification.** Outlier Exposure (OE) is listed under "Using \(P_{\text{in}}\) and \(P_{\text{out}}\)" in the tables, which suggests it was given the wild mixture \(\mathcal{S}_{\text{wild}}\) as its outlier data. But the paper's introduction states that OE "relies on a clean auxiliary dataset" (i.e., pure OOD). The experimental setup section does not explicitly state which data OE used as its outlier set. This ambiguity should be resolved — a single sentence clarifying that OE (and energy regularization) received the same wild mixture as Medix (or, alternatively, a separate pure OOD set) would suffice. Either framing is informative, but it must be stated.

4. **Connection between the synthetic experiment and theory could be stronger.** The paper reports that "Medix successfully flags 87.5% of actual OOD samples as outliers" (so a 12.5% OOD misclassification rate) in Figure 2, but does not explicitly connect this number back to the bound in Theorem 4.2. Given that the synthetic data clearly satisfies the separation condition \(\|\mu_{\text{out}} - \bar{\nabla}_{\text{in}}\|_2 \geq \Delta\sqrt{d}\) (the OOD mean is at \([20, 2\sqrt{3}]\) while InD means are near the origin), a brief comment relating the observed error to the theoretical bound would strengthen the paper.

### Trivial

- The stopping criterion \(|\delta_{\max}| > \epsilon\) in Algorithm 1 could be explained more clearly: \(\delta_{\max}\) is the maximum \(\delta_i\) among *remaining* samples, not the change in overall distance \(d_t\).

## Nice-to-Haves

- An oracle upper-bound experiment (comparing final OOD detector performance using identified outliers vs. true OOD labels) would help gauge how much headroom remains in the filtering stage.
- An ablation on hyperparameter \(k\) in the main text (it is in Appendix A.2) would be useful for readers, though the appendix covers this.

## Removed Points

- *"The greedy filtering algorithm is computationally intractable as described"* — removed as it overstates the issue. The paper acknowledges the computational challenge, defers to Appendix A.6, and the authors successfully ran the experiments (providing code). The algorithm as stated can be implemented efficiently using coordinate-wise sorted lists that support fast median recomputation per removal. The concern is downgraded to a minor weakness about underspecification in the main text.
- *"Fair comparison with Outlier Exposure is ambiguous"* — moved to Minor (weakness 3) since the critic's framing as a "critical issue" was disproportionate. The ambiguity is real but resolvable with one sentence of clarification.
- *"Convergence is not analyzed"* — removed. The stopping criterion based on the monotonic trend observed in Figure 1 is sufficiently motivated, and the appendix (full paper) likely contains additional analysis.
- *"No discussion of hyperparameter \(k\)"* — removed. The paper lists candidate values for \(k\) (line 182) and references ablation studies in Appendix A.2.
- "Strength" about the paper addressing an important problem — removed as generic.
- "Strength" about the paper being one of the few studies with theoretical foundations — kept as it is specific and supported by the paper's own positioning relative to Du et al. (2024a).

## Novel Insights

An interesting observation emerges from combining the harsh critic's and strength finder's analyses: the paper's **two-sided theoretical guarantee** (bounding both InD→OOD and OOD→InD errors) is unusual in the OOD detection literature, where most methods only certify one direction. The critic's concern about \(m_{\min}\) inadvertently highlights that the theory simultaneously involves three interacting sample sizes (\(m_{\text{in}}\), \(m_{\text{out}}\), and their minimum), which is a non-trivial dependency structure. The strength finder's emphasis on the dataset-level mixing relaxation (vs. batch-level mixing in prior work) is worth underscoring: it means Medix is not just an incremental improvement but actually broadens the class of problems that can be tackled.

## Suggestions

1. Add a one-sentence definition of \(m_{\min}\) in Theorem 4.1 (e.g., "\(m_{\min} = \min(m_{\text{in}}, m_{\text{out}})\) where \(m_{\text{in}}\) and \(m_{\text{out}}\) are the numbers of InD and OOD samples in \(\mathcal{S}_{\text{wild}}\), respectively").
2. In Section 3.1 or Algorithm 1, add a brief note on implementation efficiency (e.g., "the leave-one-out EWM is computed efficiently by maintaining coordinate-wise sorted lists, enabling \(O(|\mathcal{S}| d \log |\mathcal{S}|)\) updates per iteration").
3. Clarify in Section 5.1 that OE (and energy regularization) were evaluated using the *same wild mixture* \(\mathcal{S}_{\text{wild}}\) as their source of outlier data.
4. Add a brief sentence connecting the 87.5%/12.5% synthetic result back to the bound in Theorem 4.2.

## Score and Decision

**Round 1 bracket:** Based on the initial calibration, the paper sits somewhere between the weak-to-mid anchors (3.5–7.5). The lowest useful anchors are rejected OOD detection papers (avg 2–3), and the highest OOD-specific anchors are accepted poster papers around 5.6–6.0. No OOD paper in the 7.5+ band was found (those were on unrelated topics).

**Round 2 narrowing:** The GradPCA paper (avg 5.60, Accept Poster) is a gradient-based OOD detection method with theory, but has unclear algorithm descriptions and fewer baselines. The Fisher-Rao paper (avg 6.00, Accept Poster) has a theoretical framework but was criticized for poor alignment between theory and method. The paper under review is empirically stronger than both (20 baselines, consistent SOTA), has a cleaner theory-to-method connection, and tackles a harder problem (wild unlabeled data). However, it has several minor fixable issues. Comparing directly: Medix is clearly stronger than GradPCA (5.60) and somewhat stronger than Fisher-Rao (6.00).

**Final score: 6.5**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
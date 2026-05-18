I now have a thorough understanding of the paper and can verify all claims. Here is my consolidated review.

---

## Summary

This paper proposes FACTS (FACTored State-space), a recurrent framework for world modeling that treats both the latent state and input features as sets of nodes. It introduces an attention-based routing mechanism that assigns input features to latent factors, combined with element-wise SSM-style dynamics. The key technical claims are: (1) the model is provably permutation-invariant w.r.t. input features (R.P.I.) and permutation-equivariant w.r.t. the latent memory (L.P.E.); (2) the recurrence can be linearized by substituting the evolving memory \(Z_{t-1}\) with the initial memory \(Z_0\) in the routing, enabling parallel computation; (3) the model achieves strong results across multivariate time-series forecasting, object-centric video prediction, and graph-based traffic forecasting.

## Strengths

- **Correctly established theoretical guarantees for permutation invariance/equivariance.** The paper defines L.P.E. (Definition 1) and R.P.I. (Definition 2) and proves Theorems 1–2. I have verified directly: the attention-based router (Eq. 12) applies row-wise projections \(\psi,\varphi\) to \(X_t\); permuting the rows of \(X_t\) permutes both keys \(\psi(X_t)\) and values \(\varphi(X_t)\) identically, and the attention output \(\text{softmax}(Q K^T \sigma^T) \sigma V = \text{softmax}(Q K^T) V\) is provably invariant. The element-wise operations in the recurrence preserve this property. The reviewer's claim that "standard cross-attention does not have this property" is incorrect — this is a well-known consequence of joint key/value permutation.

- **Empirical robustness to input feature permutation is directly validated.** Figure 2 shows that under random feature shuffling at test time, FACTS maintains nearly unchanged prediction accuracy across 4 datasets, while iTransformer and S-Mamba exhibit large degradation (e.g., S-Mamba's MSE on Traffic increases more than threefold). This directly confirms the practical value of the R.P.I. property and distinguishes FACTS from prior SSMs.

- **Strong and consistent performance across diverse world modeling tasks.** On multivariate time-series forecasting (Table 1), FACTS achieves top-2 MAE on 7 of 9 datasets. On object-centric video prediction (Table 2), it achieves the best LPIPS (0.09) and FG-mIoU (48.11). On graph-based traffic prediction (Table 3), it achieves the best MAPE (9.08%). These results are obtained with a single framework, not task-specific architectures.

- **Novel linearization enabling parallel computation while preserving permutation properties.** The paper transparently acknowledges that the non-linear recurrence (Eq. 10, with \(Z_{t-1}\)-dependent routing) limits parallelization, and proposes substituting \(Z_{t-1}\) with \(Z_0\) in the routing to obtain a linear recurrence (Eqs. 17–20). Figure 3 empirically compares window sizes from 1 (fully recurrent) to 96 (fully parallel) on the Electricity dataset, showing consistent performance — this directly addresses the concern about the approximation's validity.

- **Flexible graph-structured memory over rigid SSM constraints.** By treating the state as a set of \(k\) factors (nodes) and using attention-based routing to assign input features to factors, FACTS avoids the fixed diagonal/block-diagonal structural priors of Mamba and S4, which assume invariant relationships between state dimensions and input features over time.

## Weaknesses

### Fatal
None.

### Major

1. **Ambiguity about which version produced the main results, and no theoretical analysis of the linearization error.** The paper presents the linearized version (Eqs. 17–20, substituting \(Z_{t-1}\to Z_0\) in routing) as "the final formulation of FACTS," but does not explicitly state whether the main results in Tables 1–3 come from the linearized or non-linear version. The routing in the linearized version depends on the *fixed initial* memory \(Z_0\) rather than the evolving memory \(Z_{t-1}\), which means the claim of "dynamic" state-dependent routing is partially compromised for the implemented model. While Figure 3 provides an empirical comparison on one dataset (Electricity), the paper lacks any theoretical analysis of the approximation error incurred by this substitution, and the comparison is not extended to other tasks. This matters because the paper's motivation (Section 3) emphasizes dynamic memory-input routing as a key advantage over prior SSMs.

2. **Set functions used to interface FACTS with forecasting tasks are unspecified.** Section 4.1.1 states that the "embedders" and "projectors" from TSLib are replaced with "set functions to accommodate the output structure of FACTS," but never describes what these set functions are or how the \(k\)-factor output is mapped to the required prediction vector of length \(m\) at each time step. This makes the experimental setup for the main set of results (Table 1) not reproducible as described.

### Minor

1. **Overclaim in the abstract and conclusion.** The abstract states FACTS "consistently outperforms or matches specialised state-of-the-art models," but in Table 1 FACTS is not the top performer on several datasets (e.g., ETTm1, Traffic, Solar-Energy on MSE). On ETTm1 (MSE) it ranks behind several baselines. The paper's own text (line 185) more accurately says "top 2 in 7 out of 9," which is strong but does not warrant "consistently outperforms." This should be toned down.

2. **Object-centric results are strong but the improvement over SlotFormer is modest.** FACTS matches SlotFormer on LPIPS (0.09) and outperforms by ~1 point on FG-mIoU (48.11 vs. 47.07). The paper's claim that FACTS "consistently outperforms or matches" is accurate here but the framing as "superior" (line 220) slightly overstates what is a small gap.

3. **No computational complexity analysis or wall-clock comparison.** The paper motivates the linearization via computational efficiency but provides no runtime comparison against the main baselines (Mamba, iTransformer). The cross-attention at each step is \(O(T \cdot k \cdot m \cdot d)\), and it would be informative to know how this compares to Mamba's efficient scan in practice.

### Trivial
None.

## Nice-to-Haves
- An ablation of the number of factors \(k\) on different tasks would help understand sensitivity to this hyperparameter.
- Theoretical discussion of when the approximation \(Z_{t-1} \to Z_0\) in routing is reasonable (e.g., when routing is dominated by input features, when \(Z_0\) is learned to encode stable factor identities).
- A brief wall-clock runtime comparison with iTransformer and S-Mamba would strengthen the efficiency claim.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Permutation invariance claims are incorrectly established"** (Harsh Critic, Critical Issue #1): Factually wrong. When keys \(\psi(X_t)\) and values \(\varphi(X_t)\) both come from the same \(X_t\) with row-wise projections, permuting rows of \(X_t\) permutes keys and values identically, and the cross-attention output is provably invariant. The routing operator \(\text{softmax}(Q K^T / \sqrt{d}) V\) under joint key-value permutation is a textbook property. The paper's theoretical claims (Theorems 1–2) are correct as stated.

2. **"No comparison between non-linear and linearised versions"** (Harsh Critic, Critical Issue #2): Figure 3 directly compares window sizes 1 (fully recurrent, i.e., non-linear with \(Z_{t-1}\)-dependent routing) to 96 (fully parallel, i.e., linearized with \(Z_0\)-based routing) on the Electricity dataset, showing consistent performance. This is an empirical comparison, though the critic's point about lack of theoretical error analysis is retained in Major #1.

3. **Missing appendix results (Table 7) and missing proofs**: The parser strips appendices. The original submission contains these. Per hard rules, this criticism is removed.

4. **Formatting/style nitpicks**: Various parser artifacts and minor presentation issues are not author errors and are removed per hard rules.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an interpretation of the paper's results or method that goes deeper than what the authors themselves provide.

## Suggestions

1. **Clarify which version produces each reported result.** If the main tables use the linearized version (Eqs. 17–20), state this explicitly. If some tasks use the non-linear version, be clear about which and why.

2. **Describe the set functions** used to interface FACTS' \(k\)-factor set output with the \(m\)-dimensional forecasting target. Even a paragraph specifying "we use mean pooling across factors followed by a learned linear projection" or similar would resolve the reproducibility gap.

3. **Add a brief analysis of the linearization approximation.** While Figure 3 empirically shows it works on Electricity, a theoretical bound (e.g., if \(\|Z_{t-1} - Z_0\|\) is bounded or if attention weights change slowly) or an ablation on a second task would substantially strengthen the paper's core engineering contribution.

4. **Tone down the "consistently outperforms" language** to match the actual pattern (top-2 on 7/9 datasets in MAE; competitive but not top on MSE for several datasets). The results are strong enough without overclaiming.

5. **(Optional) Add a runtime comparison** table showing seconds per epoch or total training time for FACTS vs. iTransformer vs. S-Mamba on a representative dataset.

## Score and Decision

The paper presents a novel approach to structuring SSM state as a set of factors with attention-based routing, correctly establishes permutation invariance/equivariance, and demonstrates strong results across diverse tasks. The main weaknesses — ambiguity about experimental details and lack of theoretical analysis of the linearization — are non-fatal and addressable in revision. I recommend acceptance.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
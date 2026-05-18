## Summary

This paper studies differentially private (DP) optimization for nonsmooth nonconvex (NSNC) objectives under the Goldstein stationarity criterion. It proposes two algorithms: a single-pass algorithm that improves over the prior work of Zhang et al. (2023) by at least a Ω(√d) factor, achieving a dimension-independent "non-private" term that was previously claimed impossible; and a multi-pass ERM algorithm that achieves sublinear dimension dependence—the first such result. The paper also provides a generalization result showing that empirical Goldstein stationarity implies population Goldstein stationarity. The core technical insight is that the zero-order gradient estimator concentrates around its mean with high probability, allowing sensitivity to be bounded by O(L/B) rather than the worst-case O(Ld/B), which reduces the privacy noise.

## Strengths

1. **Dimension-independent non-private term in single-pass DP guarantee (Theorem 1, Remark 1):** The sample complexity's "non-private" term scales as 1/αβ³ with no dependence on dimension d. This directly refutes a claim of impossibility in Zhang et al. (2023) and represents a genuine advance.

2. **First private ERM with sublinear dimension dependence for NSNC objectives (Theorem 2):** The multi-pass algorithm achieves sample complexity n = Õ(d^{3/4}/εα^{1/2}β^{3/2}), which is sublinear in d. The paper correctly states this is a first.

3. **Key technical insight — high-probability sensitivity reduction:** The paper identifies that while worst-case sensitivity of the zero-order gradient estimator is O(Ld/B), with high probability it reduces to O(L/B) (Lemma 1 and the discussion following Eq. (4)). This insight drives the improvement and is clearly articulated.

4. **Generalization guarantee from empirical to population (Proposition 4):** A novel result showing that an (α,β̂)-Goldstein stationary point of the empirical loss is an (α,β)-stationary point of the population loss with β = β̂ + Õ(√{d/n}), bridging ERM and stochastic optimization. The proof appears correct and uses a uniform convergence bound.

5. **Comprehensive comparison to prior work:** Table 1 and surrounding text clearly contrast sample complexities against the single existing result (Zhang et al. 2023), making improvements easy to verify.

## Weaknesses

### Fatal

None.

### Major

1. **Privacy proof does not properly account for the high-probability sensitivity bound (Lemma 4 / Lemma 8).**  
   The Tree Mechanism (Proposition 1) requires a *deterministic* bound on sensitivity for all neighboring datasets and all auxiliary inputs. Lemma 3 only provides a bound that holds with probability ≥ 1−δ/2 over the randomness of the zero-order estimator. The proof of Lemma 4 (lines 602–608) states: "By Lemma 3 and our assignment of m, we know that with probability at least 1−δ/2, the sensitivity of all t is bounded by … Then the privacy guarantee follows from the Tree Mechanism."  
   This is insufficient. The δ/2 failure probability from the sensitivity bound is never composed with the δ from the Tree Mechanism. The proof needs to explicitly: (a) set the Tree Mechanism's internal δ parameter to δ/2, and (b) union-bound the two failure events to obtain overall (ε,δ)-DP. The same gap carries over to the multi-pass privacy guarantee (Lemmas 8).  
   **Why it matters:** The privacy guarantee is the paper's central claim. While this gap is likely fixable with a more careful composition argument (and would not affect asymptotic rates), the proof as presented is incomplete, and readers cannot verify that the claimed (ε,δ)-DP guarantee holds.

### Minor

1. **Conditioning in Lemma 3's second case is sloppy.**  
   The second case states: "conditioned on g_{t−1} = g_{t−1}', we have with probability at least 1−δ/2: ‖g_t−g_t'‖ ≲ …". For the Tree Mechanism, what matters is the sensitivity of the *increment* (g_t − g_{t−1}), which uses only fresh data and does not require this conditioning. The bound itself is correct—the increment sensitivity does not depend on previous states being equal—but the presentation is confusing and the proof says "The other case follows from the same argument" without elaboration. This makes it harder for a reader to verify the privacy analysis. The analysis should be restated in terms of increment sensitivity directly.

2. **The proof of Lemma 4 (and Lemma 8) is too terse.**  
   Even beyond the composition gap, the privacy proof is essentially one sentence: "the privacy guarantee follows from the Tree Mechanism." Given that the entire paper's contribution hinges on the privacy-utility trade-off, the privacy lemmas deserve more thorough justification.

### Trivial

None.

## Nice-to-Haves

- The paper could provide a brief discussion of why Rényi-DP (used by Zhang et al. 2023) would not directly benefit from the same high-probability sensitivity reduction technique, since the paper already notes this in the Discussion section. A short technical explanation would strengthen the paper.
- A more explicit demonstration of how the composition of the δ/2 failure probability from the sensitivity bound and the Tree Mechanism's δ works out to give (ε,δ)-DP would resolve the major concern.

## Removed Points

- **Criticism that the high-probability sensitivity argument makes the paper "not meaningful as stated" and that "the (ε,δ)-DP guarantees are unsupported":** This overstates the severity. The composition gap is real but fixable; it does not invalidate the core idea. The paper's approach of using high-probability sensitivity bounds for privacy is valid when the failure probability is properly composed into δ (a standard technique). The weakness is kept in Major but the fatal framing is removed.

- **Criticism that the conditioning issue in Lemma 3 second case "undermines the central claim":** Overstated. The increment sensitivity analysis does not actually require the conditioning; the bound itself is correct. Moved to Minor.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an insight that the paper itself does not already contain.

## Suggestions

1. **Fix the privacy composition argument in Lemma 4 and Lemma 8.** Explicitly set the Tree Mechanism's δ to δ/2 and union-bound with the δ/2 failure probability from Lemma 3. Show that the resulting guarantee is (ε,δ)-DP. (This will not change the asymptotic sample complexity.)
2. **Restate Lemma 3 in terms of increment sensitivity** rather than conditioning on g_{t−1}=g_{t−1}'. The analysis is cleaner and avoids the misleading conditioning.
3. **Expand the privacy proofs** beyond one-sentence appeals to the Tree Mechanism. Given that the paper's central advance depends on the privacy analysis, the proofs should be self-contained enough for a reviewer to verify the composition.

## Score and Decision

The paper addresses an important open problem (DP NSNC optimization) and makes genuine technical contributions: a dimension-independent non-private rate that refutes a prior impossibility claim, the first ERM algorithm with sublinear dimension dependence for this setting, and a novel generalization result. The core insight (using concentration to reduce sensitivity) is clever and well-motivated. The utility analysis and the generalization result appear sound.

However, the privacy analysis has a real gap: the composition of the high-probability sensitivity bound with the Tree Mechanism's δ is not properly accounted for. While likely fixable without changing rates, this gap means the paper's central claimed result—the (ε,δ)-DP guarantee at the stated sample complexities—is not yet fully supported by the presented proofs. The paper is at the borderline: the contributions are significant, but the technical verification is incomplete in a critical area.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
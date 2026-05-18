Now I have a thorough understanding of the paper and can verify each reviewer claim against the actual text. Let me compose the final review.

---

## Summary

This paper proposes MARS, a backdoor defense for Federated Learning that introduces "backdoor energy" (BE) as a per-neuron measure of maliciousness, approximated by the per-neuron Lipschitz constant computed from model parameters alone (no clean data or trigger needed). MARS extracts the top-κ% BE values per layer into a "concentrated backdoor energy" (CBE) vector, then uses Wasserstein distance-based K-Means (K-WMeans) to separate backdoor from benign models, selecting the trusted cluster via center-norm rather than majority size. Experiments across three datasets, three SOTA attacks, and eight SOTA defenses show MARS consistently outperforms existing defenses, handles attacker ratios from 0% to 95%, and shows resilience to an adaptive attack.

## Strengths

- **Well-motivated diagnosis of why existing defenses fail**: The paper provides concrete experimental evidence (Figure 2) that norm constraint, OOD detection, and consistency detection are all bypassed by 3DFed — backdoor updates have smaller norms than benign ones, indistinguishable PCA projections, and cosine similarity lower than some benign pairs. This is a clear, empirically grounded motivation (Section 4.1).

- **Novel and principled BE formulation that avoids data/trigger access**: Theorem 1 derives an upper bound on backdoor energy via Lipschitz constants, and Equation 3 reduces to the per-neuron Lipschitz constant alone — a quantity computable purely from model parameters. This is a genuinely new way to measure malignity without requiring client data, shadow datasets, or trigger reconstruction (Section 4.3).

- **Strong empirical results across diverse settings**: MARS consistently achieves the highest CAD and lowest ASR against 3 SOTA attacks (MRA, CerP, 3DFed) across 3 datasets, outperforming 8 existing defenses (Table 2), including the recent BackdoorIndicator from USENIX Security 2024 (Table 4). The comparison is comprehensive and the advantage is clear.

- **Robustness across extreme attacker proportions**: MARS achieves 100% TPR and 0% FPR for attacker ratios from 0% to 95% (Table 5), demonstrating both fidelity (no false exclusion when benign-only) and practicability (works even when attackers are a large majority).

- **Transparent handling of adaptive attacks**: The paper designs a custom adaptive attack that minimizes BE via a regularization term, shows where the primary norm-based selection fails, and presents MARS* (majority-based fallback) that consistently defends across all λ values (Table 3). The limitation is acknowledged rather than hidden.

## Weaknesses

### Fatal
None.

### Major

- **The core BE-to-Lipschitz approximation is not empirically validated.** The paper introduces BE as the expected activation difference between clean and backdoor inputs, derives an upper bound via Lipschitz constants, drops the product terms (same-layer neurons share all preceding-layer Lipschitz factors), and equates BE to the per-neuron Lipschitz constant alone (Eq. 3 → Eq. 3). The paper states "the upper bound of backdoor energy reasonably reflects the distribution of BE" and "we do not need the exact value of BE ... but only the relative magnitudes" — but provides no direct evidence for either claim. Without showing that per-neuron Lipschitz constants are actually higher in backdoor models than benign models for the attacks considered, the "malignity-aware" label rests on an unverified premise. The paper's overall empirical success could stem from BE capturing backdoor information, but it could also stem from some other property of the CBE feature. A simple plot of CBE values for backdoor vs. benign models, or an ablation replacing BE with a different per-neuron measure (e.g., weight norm, activation norm), would substantiate the core claim.

### Minor

- **The claimed advantage of Wasserstein distance over Euclidean/cosine distance lacks empirical support beyond a toy example.** The toy example (Table 1) demonstrates the order-sensitivity issue in principle, but no experiment compares K-WMeans with standard K-Means (Euclidean or cosine) on actual CBE vectors. The paper does not specify whether the top-κ% values per layer are sorted before concatenation; if they are (as TopK naturally does within each layer), the order-sensitivity argument weakens. A direct comparison on TPR/FPR/ASR would confirm whether Wasserstein distance is empirically superior or whether Euclidean distance on sorted values would suffice.

- **No standard deviations or confidence intervals are reported.** FL experiments involve stochasticity from client selection, data sampling, and training dynamics. Key results (Tables 2–5) are reported as single values without multiple runs. While single-run reporting is common in some FL papers given computational costs, the lack of variance information makes it impossible to assess the stability of the reported advantages.

- **Table 5 (attacker ratio experiment) omits the attack used and does not report ASR or ACC.** Only TPR and FPR are shown. Without ASR (to confirm backdoor mitigation) and ACC (to confirm model utility), it is unclear whether the defense's detection success translates to actual protection, especially at extreme ratios like 95% attackers where filtered aggregation could still be compromised.

- **No sensitivity analysis for hyperparameters κ (default 5%) and ε (default 0.03).** These control the amount of BE information retained and the cluster-merging threshold, respectively. Their values could significantly affect performance, and the paper provides no ablation.

- **The adaptive attack fallback (MARS*) reintroduces the majority assumption that norm-based selection was designed to avoid.** When the adaptive attack suppresses BE below benign levels (λ ≥ 0.05), norm-based selection inverts (picks the wrong cluster). The fallback switches to majority-based selection, which works — but this undercuts the paper's narrative of not relying on the majority assumption. While the paper is transparent about this, a more principled fallback (e.g., analyzing inter-cluster distance or distribution shape to detect role reversal) would strengthen the method.

- **Edge case of colluding attackers sending identical models is not discussed.** If all colluding attackers send the exact same backdoor model (fully collusive), their CBEs would be identical, yielding Wasserstein distance of zero between them. The paper does not analyze whether this scenario would preserve the separation between clusters or break the norm-based selection logic.

### Trivial

- Footnote references in the main text (e.g., "4" after "defense" on line 191) defer CAD definition to the appendix, which is stripped by the parser. This is standard practice but worth noting the main text is slightly incomplete without it.

## Nice-to-Haves

- A direct comparison of K-WMeans vs. Euclidean/cosine K-Means on CBE vectors for at least one attack/dataset pair, with and without sorting.
- Sensitivity analysis varying κ (1%, 10%, 20%) and ε (0.01, 0.05, 0.1) on CIFAR-10 with 3DFed.
- Standard deviations over 3 runs for key results (Tables 2, 3, 5).

## Removed Points

These points are flagged to be removed — treat them with caution.

- **Criticism that CAD is not defined in the main text (from Harsh Critic Point 4).** The paper's footnote defers the formal definition to the appendix. Per the review rules, weaknesses about content deferred to the appendix (which is stripped by the parser) are removed — the definition exists in the original submission.
- **Criticism that the Lipschitz approximation "is not validated" framed as if no theoretical justification exists.** The paper does provide theoretical motivation (Theorem 1, the observation that same-layer neurons differ only in the per-neuron Lipschitz term, and the explicit statement that only relative magnitudes matter). The retained weakness is narrowed to: direct empirical validation of the approximation is missing, not that it lacks any justification.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an unexpected connection or cross-cutting observation not already present in the paper.

## Suggestions

1. **Add direct empirical validation of the BE approximation.** A simple figure showing CBE (or top-κ BE values) for benign vs. backdoor models across the evaluated attacks (3DFed, CerP, MRA) would directly test the core claim. An ablation replacing BE with an alternative per-neuron statistic (weight L2 norm, activation variance on random inputs) would show whether the specific Lipschitz-based measure is responsible for the separation.

2. **Add a clustering-metric comparison.** Compare K-WMeans against standard K-Means with Euclidean distance (on both sorted and unsorted CBE vectors) for at least one dataset/attack pair, reporting clustering accuracy or downstream TPR/FPR.

3. **Report standard deviations for key results** (at least 3 runs) to establish statistical reliability.

4. **Specify the attack used in Table 5** and include ASR and ACC columns alongside TPR/FPR.

5. **Add a sensitivity analysis** for κ and ε, or at minimum state that the method is robust to moderate variation.

6. **Discuss the identical-model collusion edge case** — whether the defense would still separate backdoor from benign models if all attackers send identical parameters, and whether the distance-threshold logic handles this gracefully.

## Score and Decision

**Originality**: High — the concept of measuring "malignity" per neuron via a data/trigger-free Lipschitz-based measure is novel.  
**Importance**: High — backdoor attacks in FL are a significant threat, and existing defenses demonstrably fail against SOTA attacks.  
**Claims support**: Moderate — the empirical outcomes are clear, but the core mechanism (BE via Lipschitz constants lacks direct validation, and some experimental gaps (no std devs, no sensitivity analysis, missing details in Table 5) weaken the strength of the claims.  
**Soundness**: Moderate-strong — the experiments are well-designed and cover extensive baselines, but missing variance information and the unvalidated central approximation reduce confidence.  
**Clarity**: Good — the paper is well-structured and clearly written.  
**Value to the community**: High — MARS could become a useful defense if the approximation is validated, and the diagnosis of existing defenses' failures is independently valuable.

The weaknesses are real but addressable. None is fatal: the paper's strong empirical profile (consistent outperformance across 8 baselines, 3 attacks, 3 datasets, extreme attacker ratios) establishes genuine value even if some of the claimed novelties need tighter support. The paper would benefit from a major revision to address the validation gap for the BE approximation and the missing experiments, but the contribution is solid enough in its current form.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
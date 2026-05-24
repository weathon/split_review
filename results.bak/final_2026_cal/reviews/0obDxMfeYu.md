Now I have all the information I need. Let me compile the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses

### Fatal

### Major

### Minor

### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me write the review.

**Round 1 bracket**: [4.5, 6.5]

**Round 2 narrowing**: After reading GradPCA (5.60, accepted), SCOPED (5.50, accepted), Fisher-Rao (6.00, accepted), and Bad-OOD (4.00, rejected), I place this paper between GradPCA and SCOPED.

Medix is clearly stronger than Bad-OOD (4.00), which was rejected for limited novelty. It has a more novel approach and stronger theory than GradPCA (5.60), and comparable results to SCOPED (5.50). However, the missing CONJ/DRL tables and ambiguous 40.98% claim are issues that need addressing, similar to the missing baselines issue in GradPCA. The paper is slightly less polished than Fisher-Rao (6.00) in terms of connecting theory to experiments.

**Final score: 5.5**

Let me also verify one thing: let me check if maybe CONJ and DRL appear in the appendix (which was stripped). The paper says in the additional studies section: "(4) a comparison with semi-supervised open-set recognition methods (Appendix A.7)" — this is different from CONJ/DRL. The baselines section says CONJ and DRL were "included" but no results are shown. The conclusion claims to have outperformed DRL. Since the appendix was stripped, I can't verify if the results are there. But the instructions say: "REMOVE weaknesses about missing appendix, missing proofs in appendix, or absent references. The parser strips those sections from all papers; they exist in the original submission."

Hmm, this is tricky. The tables in the main paper don't include CONJ or DRL. Could they be in the appendix? The paper doesn't say "see Appendix for CONJ/DRL results." It says "we included more recent baselines, including CONJ and DRL" in Section 5.1, and the conclusion says "outperformed state-of-the-art methods such as WOODS and DRL." If CONJ/DRL results are in the appendix, the paper doesn't reference where. But since the appendix is stripped, I can't verify.

The instruction says "REMOVE weaknesses about missing appendix, missing proofs in appendix, or absent references." But this is about CONJ and DRL not appearing in the main tables despite being claimed as baselines. If their results are in the appendix, the paper should reference them. If their results aren't shown anywhere, it's a genuine omission.

I think the fair approach is to flag this as a weakness but note that if the results exist in the appendix, the paper needs to reference them properly. But per the instructions, I should not speculate about what's in the appendix. Let me handle this carefully.

Actually, re-reading the instructions: "REMOVE weaknesses about missing appendix, missing proofs in appendix, or absent references. The parser strips those sections from all papers; they exist in the original submission." This means I should not criticize the paper for having content in the appendix rather than the main text. But CONJ/DRL results are not referenced anywhere — not even "see Appendix." The paper just says they were "included" without showing results. This is a content omission, not an appendix-organization issue. I'll keep this as a weakness.

Wait, actually let me re-read: "The paper states that it compares against 20 baselines, including 'CONJ (Peng et al., 2024) and DRL (Zhang et al., 2024), to provide a more thorough evaluation' (Section 5.1). However, neither CONJ nor DRL appears in any results table (Tables 1 and 2)."

The paper says "we included more recent baselines, including CONJ and DRL." This implies results were computed but doesn't show them. Since these results might be in the stripped appendix... but the paper doesn't even say "see Appendix" for them.

I'll keep this as a weakness but soften it to note that the paper should either include them in the tables or clearly reference where they are.

Let me write the review now.Here is the final consolidated review.

---

## Summary

Medix proposes a median-centric framework for OOD detection that filters outliers from unlabeled wild data by minimizing the L₂ distance between the element-wise median (EWM) of wild-data gradients and the mean in-distribution (InD) gradient. The paper provides theoretical bounds on inlier and outlier misclassification rates (Theorems 4.1, 4.2) and reports strong empirical results across CIFAR-10 and CIFAR-100 against several baselines, with the method also relaxing the batch-level mixing assumption of prior wild-data work.

## Strengths

- **Novel median-based filtering approach with theoretical guarantees.** The use of element-wise median (EWM) for outlier identification from unlabeled mixtures is genuinely novel in the OOD detection setting. Theorems 4.1 and 4.2 provide upper bounds on both inlier and outlier misclassification rates under sub-Gaussian gradient assumptions, and Remark 4.3 notes a looser bound (Theorem C.3) that removes the sub-Gaussian assumption entirely. This two-sided theoretical framing is a clear contribution over prior wild-data work that lacked such guarantees.

- **Strong empirical performance across multiple benchmarks.** On CIFAR-10 (Table 1), Medix achieves average FPR95 of 0.80% vs. WOODS at 3.40% and KNN+ at 10.30%. On CIFAR-100 (Table 2), Medix achieves average FPR95 of 5.42% vs. WOODS at 6.74% and KNN+ at 46.40%. Standard deviations over five runs are reported for Medix, and the performance is consistently best across all five OOD test sets.

- **Practical relaxation of batch-level mixing assumption.** Section 6 notes that prior wild-data methods (Katz-Samuels et al., Du et al.) assume batch-level mixing with fixed InD-OOD ratios, while Medix operates under realistic dataset-level random mixing. This is a concrete improvement in applicability that distinguishes the method from prior work.

- **Clear motivation experiment (Figure 1).** The monotonic increase in L₂-norm deviation between the InD mean gradient and the EWM of wild-data gradients, as OOD samples are incrementally added, provides clean empirical justification for the greedy filtering procedure and its stopping criterion.

## Weaknesses

### Major

- **CONJ and DRL are listed as baselines but their results are absent from all tables.** Section 5.1 states: "Finally, we included more recent baselines, including CONJ (Peng et al., 2024) and DRL (Zhang et al., 2024), to provide a more thorough evaluation." The Conclusion asserts Medix "outperformed state-of-the-art methods such as WOODS and DRL." However, neither CONJ nor DRL appears in Table 1 or Table 2, or is referenced as being in an appendix. The reader cannot verify the claim of outperformance over these methods. The paper should either provide the results in the tables or clearly remove the claims. (If the results exist in the stripped appendix, the paper needs to signal this in the main text.)

- **Ambiguous framing of the 40.98% improvement figure.** The Introduction states Medix "outperforming [KNN+] by an average of 40.98% in terms of FPR95," and the Conclusion repeats "reduced the average FPR95 by 40.98%." From Table 2, KNN+ average FPR95 = 46.40 and Medix = 5.42, so the absolute difference is 40.98 *percentage points*. Since FPR95 is already a percentage, "40.98%" reads as a relative improvement to many readers (which would be ~88.3%). The paper should use "40.98 percentage points" or explicitly state the metric is the absolute difference.

### Minor

- **Main evaluation only uses matched OOD distributions.** In the wild data setup, the OOD component in the wild set is drawn from the *same* dataset as the test OOD set (e.g., PLACES365 in both wild and test). This is the most favorable setting. Unseen OOD evaluation ($P_{out}^{test} \neq P_{out}$) is mentioned only for the appendix (A.4). For a paper claiming open-world applicability, at least one unseen-OOD experiment in the main body would substantially strengthen the claims.

- **Theoretical bounds rely on pseudo-labeled OOD gradients, creating a gap between theory and practice.** Theorems 4.1 and 4.2 assume i.i.d. sub-Gaussian gradients for InD and OOD samples. In practice, OOD gradients are computed under pseudo-labels ($\hat{y}$) that are essentially random for OOD samples. The paper mentions a pseudo-label quality experiment in Appendix A.5 and Theorem C.3 providing looser bounds without sub-Gaussian assumptions, which partially addresses this, but the main text does not explicitly discuss how label noise on OOD gradients affects the theoretical guarantees or the separation condition $\|\mu_{\text{out}} - \bar{\nabla}_{\text{in}}\|_2 \geq \Delta\sqrt{d}$.

- **Standard deviations are only reported for Medix, not for baselines.** Tables 1 and 2 report standard deviations for Medix (over five runs) but not for any baseline. The reader cannot assess whether the performance differences are statistically significant. While this is common in the OOD detection literature, reporting baseline variability would strengthen the comparison.

- **Hyperparameter choices (k and ε) are listed without sensitivity analysis in the main text.** The paper selects k from {4k, 7k, 10k, 20k} and ε from {5e-5, 5e-4, 5e-3, 5e-2}, and notes that ablation is in Appendix A.2. Given that k=20k represents removing 80% of the wild set (25k samples) in one iteration, a brief sensitivity discussion in the main text would help the reader understand the method's robustness.

### Trivial

- The paper claims "20 baselines" (Abstract, Conclusion), but only 15 named methods appear in Section 5.1, and 13 appear in the tables. The count should be clarified or the framing adjusted.

## Nice-to-Haves

- Testing at contamination ratios π below and above 0.5 (e.g., 0.3, 0.4, 0.6) to verify robustness near the theoretical threshold.
- Wall-clock runtime comparison with the baselines, given that Algorithm 1's leave-one-out computation per iteration has non-trivial cost.
- Including an unseen-OOD experiment in the main body rather than only the appendix.

## Removed Points

- **"Error rate only 12.5% refers to synthetic 2D toy example, this is misleading."** — The paper clearly says "see Figure 2" in the abstract, and Figure 2 is described as a 2D Gaussian synthetic experiment. The framing is transparent, not misleading. Removed.

- **"Algorithm details are critically underspecified."** — The hyperparameter ranges for k and ε are stated; the sets are finite and reasonable. The paper defers sensitivity analysis to the appendix, which is standard practice for conference papers given space limits. Removed as overstated.

- **"The greedy algorithm does not solve Eq (4) — the connection is heuristic and not argued."** — The paper presents Algorithm 1 as a greedy approximation and motivates it via Figure 1. Greedy algorithms for subset selection are standard; this is not a weakness. Removed.

- **"The contamination term π/(2(1-π)) at π=0.5 becomes 0.5, which is not a tight bound."** — The bound is a theoretical upper bound, not a prediction of actual performance. The paper's experiments at π=0.5 show much lower error than 0.5, which is expected for upper bounds. Removed.

- **"Computational cost is O(m²) per iteration."** — The paper mentions computation efficiency in Appendix A.6 in the additional studies section, and the algorithm is designed for a one-time pre-processing step (not repeated inference). The cost concern is acknowledged. Removed as standard for a conference paper that defers details to the appendix.

- **"The InD accuracy is lower because Medix uses half the labeled data; the OOD gains could be partly due to compensating with wild data."** — This is explicitly discussed in Section 5.3: "This slight difference can be attributed to the fact that our method is trained on 25,000 labeled InD samples, while baseline methods... use the full CIFAR-100 training set of 50,000 samples." The paper addresses this. Removed.

- **Various formatting/style nitpicks and typos.** Per instructions, these are parser artifacts, not author errors. Removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Include CONJ and DRL results in the tables**, or remove the claims of outperforming them from the conclusion and abstract. If the results are in the appendix, explicitly reference them.
2. **Clarify the 40.98% figure:** state "40.98 percentage points" or specify that it is the absolute difference in FPR95 values.
3. **Add at least one unseen-OOD experiment to the main body** (a single table row would suffice) to support the "open-world" framing.
4. **Explicitly discuss the pseudo-label issue** in Section 4: state that OOD gradients are computed under predicted labels and explain why the sub-Gaussian assumption or the looser bound in Theorem C.3 still applies.
5. **Report standard deviations for the strongest baselines** (e.g., WOODS, KNN+, OE) to enable significance assessment.

---

**Calibration Details.**

*Round 1 bracketing:* Queries covering scores <3.5, 3.5–7.5, and >7.5 on OOD detection topics. Top band (7.5+) returned papers on unrelated topics (multimodal reasoning, reinforcement learning, rotation estimation) — no relevant comparators. Lower bands returned relevant OOD detection papers.

*Initial bracket:* [4.5, 6.5].

*Round 2 narrowing:* Queried for OOD detection papers scoring 4.0–6.5 with topical similarity to gradient-based filtering and theoretical guarantees.

*Anchors considered (all rounds):*

| anchor_id | avg_score | round | comparison to Medix |
|---|---|---|---|
| xRXILtRLtS | 2.00 | R1 | Much weaker; unrelated distance-based method, withdrawn. |
| c4r7iLhGcQ | 2.00 | R1 | Much weaker; feature-norm regularization, withdrawn. |
| eWJbrssI9M | 3.00 | R1 | Weaker; OOD detection for object detection, rejected. |
| B5w4bh1ryU | 2.50 | R1 | Weaker; few-shot OOD detection, withdrawn. |
| XKxDS2jtAp | 4.00 | R1 | Weaker; synthetic OOD via diffusion, rejected for limited novelty. Medix has stronger novelty and theory. |
| GEtOzC4MIi | 6.00 | R1/R2 | Stronger; Fisher-Rao Sensitivity, accepted as Poster. Cleaner connection between theory and method, more comprehensive evaluation. Medix is comparable but slightly less polished. |
| Eu25AOvORb | 6.00 | R2 | Stronger; UniOD for universal outlier detection, accepted as Poster. Medix has comparable theoretical depth but is narrower in scope. |
| rWrr6EUKpm | 3.60 | R2 | Weaker; ensemble diversity for OOD detection, withdrawn/rejected. |
| yk3QBsB43u | 5.00 | R2 | Similar; label-noise robust OOD detection, rejected (mixed scores 8,2,4,6). Medix has stronger empirical results and cleaner theory. |
| 9i6iHj2aYN | 4.50 | R2 | Weaker; negative-label OOD detection with VLMs, rejected. |
| DmhbGdwIkr | 4.50 | R2 | Weaker; backpropagation rectification for OOD, rejected. |
| 7rvMexIZA1 | 5.60 | R2 | **Closest comparator**; GradPCA, accepted as Poster. Gradient-based method with NTK theory. Had missing-baseline concerns similar to Medix. Medix has more novel methodology and stronger empirical gains but comparable presentation issues. |
| TMLiG9Rk2J | 5.50 | R2 | **Closest comparator**; SCOPED, accepted as Poster. Diffusion-based OOD. Medix is more novel in methodology; both have similar levels of theoretical contribution and empirical support. |

*Final score determination:* Medix is clearly stronger than rejected papers in the 4.0–4.5 range. It is comparable to GradPCA (5.60) and SCOPED (5.50) — each has a novel contribution with some empirical/verification gaps. Medix's missing CONJ/DRL tables and ambiguous 40.98% claim are genuine issues that prevent it from reaching the 6.0 level of Fisher-Rao.

<score>5.5</score>
<decision>Accept</decision>
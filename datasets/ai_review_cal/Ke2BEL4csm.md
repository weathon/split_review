- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8
Now I have all the information I need. Let me synthesize the final review.

## Summary

This paper proposes NCL-SR, which it presents as the first Non-Contrastive Learning (NCL) framework for Sequential Recommendation (SR). The key innovation is a data augmentation method inspired by Differential Privacy (DP) that replaces items with semantically similar synonyms via the exponential mechanism, designed to preserve user preferences while generating diverse positive samples. These augmented profiles are used to compute non-contrastive alignment and uniformity losses (based on Matrix Cross Entropy), enabling representation learning without negative samples. Experiments on six Amazon review datasets (using a 2:2:6 train/val/test split) show consistent improvements over CL-based and standard SR baselines, with an average 11.93% improvement over the best baseline.

## Strengths

1. **First NCL framework for sequential recommendation.** The paper is the first to apply a non-contrastive learning paradigm to SR, eliminating the need for negative sample mining. This is a genuine direction shift from the dominant CL-based approaches. The empirical results in Table 2 show NCL-SR outperforming CL-based methods (CLS4Rec, CoSeRec, EC4Rec, DUORec, SCL) across all datasets (Section 5.3).

2. **Consistent empirical gains on sparse recommendation data.** NCL-SR achieves an average 11.93% improvement in Recall@10 over the best baseline (Table 1). The largest gains occur on the sparsest dataset (Sports: 33.2% improvement in Recall@10), suggesting the method is particularly effective where data is limited (Section 5.2). Ablations (Table 3) confirm that both the DP augmentation and the NCL loss each contribute to performance, and replacing the DP augmentation with random CL-based augmentations degrades results.

3. **Computational complexity reduction for DP-based augmentation.** The paper identifies that user-level DP augmentation would be O(k^l) and describes an item-level design that reduces this to O(k·l) (Section 4.1, line 102). While the theoretical connection to the DP guarantee has gaps (see Weaknesses), the complexity reduction is a practical contribution.

4. **Interesting observation about alignment vs. uniformity.** The ablation (Table 3) shows that removing the alignment loss causes a larger average performance drop (6.10% on R@10) than removing the uniformity loss (4.00% on R@10). This suggests that in the sparse data regime studied, alignment matters more — a useful finding for future SR work, even if the two losses are not fully independent (see Weaknesses).

## Weaknesses

### Fatal
None. The paper's core empirical contribution — an NCL framework with DP-inspired augmentation that works well in sparse SR settings — is supported by the experiments. The weaknesses below are significant but addressable in revision.

### Major

1. **Unsupported theoretical claim: the "provable guarantee" does not extend to the item-level implementation as presented.** The paper claims "provable guarantees" (abstract, line 24) that augmented profiles preserve user preferences. Theorem 1 states a condition under which an ε-DP mechanism preserves the top-1 recommendation. However, the actual implementation operates at the *item level* — replacing individual items with synonyms via the exponential mechanism — while Theorem 1's premise assumes a single DP mechanism acting on the *whole sequence*. The paper says "we re-define Equation 5 and Equation 6 at item-level" (line 102) but never writes these item-level equations. The scoring function u(x,x') in Equation 5 is defined on full user profiles, and the sensitivity Δ_u = e − 1/e is derived for profile-level comparisons. No item-level scoring function, sensitivity, or sampling distribution is provided. The post-processing and "expected output stability" arguments (line 109) do not bridge this gap: post-processing preserves DP but not the specific margin condition in Theorem 1, and composition across independently perturbed items is not accounted for. **Impact:** The paper's central differentiator — "preference-preserving with provable guarantees" — is not justified for the actual algorithm. The method may still work well as a DP-inspired heuristic, but the claims need to be scaled back to match what is demonstrated.

2. **Evaluation limited to a single, highly non-standard data regime, with insufficient generality evidence.** The paper uses a 2:2:6 train/val/test split (Section 5.1), deliberately chosen to study data sparsity. This is a valid research goal, but the paper's claims in the conclusion ("consistently exhibits superior performance") are stated without this qualification. No experiments on standard splits (e.g., 70/10/20, leave-one-out, or the 80/10/10 common in CL-based SR papers) are provided. Since baselines like SASRec, BERT4Rec, CLS4Rec, and CoSeRec were originally designed and tuned on denser splits, it is unclear whether the reported gains are due to the method's fundamental advantages or simply because it handles extreme sparsity better while the baselines are disadvantaged. The paper does not report whether baselines were re-tuned for this split, making the comparison harder to interpret.

3. **Missing reproducibility-critical details.** The following are not reported: the privacy parameter ε (used in the exponential mechanism), the synonym set size k (a key design choice in Equation 4), the number of items perturbed per user is mentioned as 3 but without the selection strategy, and the text-based recommender architecture beyond "E5 encoder" is unspecified (e.g., how the final prediction model is constructed from encoded representations — pooling, cross-attention, transformer layers?). These omissions make it difficult to reproduce or trust the reported results.

### Minor

1. **The alignment vs. uniformity ablation is partially confounded.** ℒ_align (Equation 10) contains the term γ·MCE(C(Z,Z), C(Z',Z')), which imposes cross-view covariance matching — a form of structure that partially overlaps with uniformity. When λ₁=0 (removing ℒ_uniform), ℒ_align's MCE term still operates, and when λ₂=0 (removing ℒ_align), ℒ_uniform still operates. The claim "alignment is more important than uniformity" (Section 5.4) is based on the relative drop magnitudes (6.10% vs. 4.00%), but these differences are modest, no significance tests are reported, and the independent contribution of each loss is not fully isolated.

2. **Efficiency advantage is asserted but not measured.** The paper motivates NCL by eliminating negative sampling costs (Section 1), yet provides no runtime, memory, or throughput comparison against CL baselines. The DP augmentation itself requires computing synonym sets for all items via pairwise cosine similarity — O(|𝒯|²·d) — which is a non-trivial preprocessing cost that is not discussed or measured.

3. **Details of CL baseline adaptations are vague.** The paper states "we modify such baselines into the text-based setting for a fair comparison" (Section 5.1) but does not describe what modifications were made, whether augmentation strategies were adapted to text items, or whether CL baselines use the same E5 encoder. This undermines confidence in the fair comparison claim.

### Trivial
None.

## Nice-to-Haves
- Study sensitivity of ε and k (synonym set size) — these are key hyperparameters of the DP augmentation that are currently unreported.
- Add a baseline that removes all self-supervised losses (only the main task loss) to quantify the full benefit of the NCL framework.
- Include statistical significance tests for ablation and comparison experiments.

## Removed Points

These points were flagged for removal; they should be treated with caution.

1. **"The split makes it impossible to separate the claimed advantages ... from the advantages of a method that happens to work well with very few training examples."** — The paper is transparent about its goal of studying data sparsity (Section 5.1) and cites prior work using similar splits. The ablation study (Table 3) does isolate the contributions of the DP augmentation and NCL loss, so the claim that "it is impossible to separate" is over-stated. The generality concern is valid and retained in Major weakness #2 above, but the stronger "impossible to separate" framing is removed.

2. **"Baselines that were designed and tuned on standard splits ... are likely to perform poorly when training data is drastically reduced.** The paper does not report whether it re-tuned baselines." — The concern about missing re-tuning information is retained as part of Major weakness #2. The speculative claim that baselines "are likely to perform poorly" is removed — it is not grounded in evidence from the paper.

3. **"No 'Limitations' section or discussion of when the method might fail."** — The absence of a limitations section is a formatting preference, not a scientific weakness.

4. **"The proof is omitted" and "missing appendix"** — These refer to content that may exist in the original submission's appendix (stripped during PDF extraction).

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observation about the gap between Theorem 1's user-level guarantee and the item-level implementation is the most penetrating insight — the paper states "we re-define Equation 5 and Equation 6 at item-level" without ever writing those equations, and the DP composition cost across independently perturbed items is never analyzed. This is a genuine structural issue in the paper's argumentation, not merely a missing detail.

## Suggestions

1. **Close the theoretical gap.** Either (a) provide the item-level scoring function, sensitivity, and sampling distribution explicitly, analyze the DP composition across the l perturbed items, and connect the resulting guarantee to Theorem 1, or (b) reframe the contribution as a *DP-inspired* augmentation method without claiming provable preference-preservation for the item-level variant. The empirical results are strong enough to stand on their own without the full theoretical claim.

2. **Add at least one standard-split experiment** (e.g., 70/10/20 or leave-one-out) to demonstrate that the method's advantages are not restricted to the extreme sparse-data regime. Report whether baselines were re-tuned for the 2:2:6 split.

3. **Report all missing reproducibility details**: ε, k, the item selection strategy, and the text-based recommender architecture (encoder pooling, final prediction head).

4. **Include runtime/memory comparisons** with CL baselines to substantiate the claimed efficiency advantage.

5. **Clarify the ALIGN/uniform ablation** by discussing the overlap between the two loss terms and, if feasible, include a controlled experiment (e.g., on synthetic data) that fully isolates their effects.

6. **Describe CL baseline adaptations** in enough detail to be reproducible.

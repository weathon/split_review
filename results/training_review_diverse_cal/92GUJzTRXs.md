Now I have a thorough understanding of the paper's content and methodology. Let me synthesize the final review.

---

## Summary

This paper proposes ConDS (Context Distribution Shift), a method that iteratively revises the distribution of a noisy ICL candidate set by identifying "informative" (clean) samples through LLM feedback on a held-out validation split, then augmenting those samples (via duplication or paraphrasing) while subsampling noisy ones. This shifts the distribution so that clean samples dominate the neighborhoods retrieved at inference time. ConDS integrates with both off-the-shelf retrievers (BM25, KNN) and fine-tuned retrievers (PromptPG) and achieves strong empirical results — an average of 8.12% improvement over the best baseline and 17.07% over zero-shot ICL across 9 classification benchmarks.

## Strengths

- **Addresses a genuinely underexplored and practically important problem.** The paper correctly identifies that noise in ICL candidate sets has been largely overlooked by prior work (Section 1, lines 10-12), and Figure 2 demonstrates that even small noise ratios cause severe degradation across retrievers. This problem framing is novel and relevant for real-world deployments where label noise is common.

- **Flexible integration with multiple retriever types.** ConDS works as a plug-in distribution shift method with sparse (BM25), dense (KNN), and reinforcement-learned (PromptPG) retrievers without modifying the retriever architecture. Sections 3.1 and 3.2 provide separate algorithms for off-the-shelf and fine-tuned retrievers, and Table 2 shows consistent accuracy improvements across all retriever types (average gains of 1.26% to 9.77%).

- **Strong and consistent empirical evidence.** On 9 diverse benchmarks under 60% label noise (Table 1), ConDS (duplicate) outperforms the best baseline by 8.12% on average and zero-shot ICL by 17.07%. The method maintains superiority across different noise ratios (0.1–0.6, Figure 5a) and candidate set sizes (Figure 5b), demonstrating robustness beyond a single setting.

- **Compelling qualitative validation of the proposed mechanism.** Figure 4 directly supports the core hypothesis: after ConDS, 50.25% of test queries receive 100% clean in-context samples, whereas all baselines (BM25, KNN, PromptPG) yield 0% of queries with fully clean sets. This provides direct evidence that ConDS shifts the distribution to clean samples rather than operating through an incidental artifact.

## Weaknesses

### Major

- **The reward signal is computed against noisy validation labels, undermining the claimed mechanism.** ConDS splits the candidate set into training (90%) and validation (10%), then uses the validation labels as "ground truth" to compute the EVAL reward (Eq. 4, line 75). However, the validation set is drawn from the same noisy pool with the same noise rate (p=0.6 by default, line 131). For a validation sample with a noisy (wrong) label, a correct LLM prediction of the *true* label yields reward=0 (no augmentation), while a prediction matching the wrong noisy label yields reward=1 (augmentation of the selected training samples). This means up to ~60% of the reward signal is inverted — the method is rewarded for agreeing with noise and penalized for agreement with the truth. The paper acknowledges this briefly (line 157: "the percentage for lower clean sample ratios also increases due to the noisy samples in the validation dataset") but provides **no analysis or ablation** demonstrating why this does not fatally corrupt the mechanism. The method may still work through a different effect (e.g., even partial correct signals at α=1000 dominating the set), but the paper's stated mechanism is not well-supported. This is the most significant weakness and requires either (a) evidence that noisy rewards still lead to correct distribution shifts (e.g., comparing clean vs. noisy validation sets), or (b) a redesigned reward that does not rely on noisy labels.

- **The excessive duplication factor (α=1000) is not ablated and raises diversity concerns.** Each informative sample is duplicated 1,000 times per validation query (line 132, α=1000). With K=20 shots per query and multiple validation queries iterated over multiple epochs, the candidate set can become dominated by a small number of repeatedly-augmented samples. While this increases the clean sample ratio (Figure 4), it also dramatically reduces the diversity of the in-context examples. The paper reports no ablation over α (e.g., α=10, 100) to show that performance does not rely on extreme over-duplication, nor does it analyze whether the resulting sets retain the variety needed for tasks with diverse reasoning patterns (e.g., NLI).

### Minor

- **The train/validation split reduces the available candidate pool by 10%.** ConDS requires splitting the limited candidate set (N=200 by default) into training (180) and validation (20). The validation samples are used only during training to drive the distribution shift and are discarded at inference time (line 84: "The shifted training set is then adopted during the inference stage."). This effectively loses 10% of the original labeled pool. The paper does not ablate the split ratio or consider a setting where the validation set is drawn from an external source, making the method less practical in data-scarce scenarios.

- **The conclusion overclaims generative task results.** The conclusion (line 184) states "Experimental results for various tasks including classification and generative tasks," but all 9 datasets evaluated are classification benchmarks (SST-2, SST-5, MR, CR, AGNews, TREC, MNLI, RTE, Subj). No generative tasks are tested. This claim should be either removed or supported with experiments.

- **No analysis of the final shifted set composition.** The paper reports the clean sample ratio in selected ICL sets (Figure 4) but does not analyze the shifted candidate set itself: what fraction of unique clean vs. noisy samples survive after augmentation + subsampling? How many times is each original sample duplicated on average? Such analysis would clarify whether the improvement comes from promoting clean samples or merely from diluting noise through volume.

### Trivial

None.

## Nice-to-Haves

- An ablation comparing ConDS with a clean validation set vs. the standard noisy validation set, to directly quantify the impact of the noisy-reward issue.
- Ablation over α (e.g., α ∈ {10, 100, 1000}) to show that the method does not require extreme over-duplication.
- Ablation over the validation split ratio (e.g., 5%, 10%, 20%) to assess the cost of losing candidate pool samples.
- Extension to at least one generation benchmark to support the claim of general applicability.
- A brief sketch of the theoretical analysis (currently in the stripped appendix) in the main paper to make the argument self-contained.

## Removed Points

- **Criticism about missing related work on augmentation-based ICL / the "first to investigate" claim being aggressive.** The paper's claim about being "the first to investigate the power of distribution shift of the candidate set" is a specific claim distinct from prior data-augmentation-for-ICL work. The reviewer's demand for additional related work citations cannot be verified. *Removed per hard rule: DO NOT mention missing related works.*

- **Criticism about the theoretical analysis being relegated to the appendix.** *Removed per hard rule: weaknesses about missing appendix or proofs in appendix are parser artifacts.*

- **Criticism about the retriever coupling with noisy reward amplifying bias.** This is a corollary of the first major weakness (noisy validation labels) and does not add a distinct concern. Subsumed under the major weakness above.

## Novel Insights

None beyond the paper's own contributions. The reviews surface one clear structural concern (the noisy validation reward) but do not add novel theoretical or methodological insight beyond what the paper provides.

## Suggestions

1. **Address the reward-signal problem directly.** Either: (a) reserve a small *clean* validation set (e.g., human-verified) to compute the reward, (b) design a reward that does not rely on exact label match (e.g., output probability confidence, agreement across multiple prompts), or (c) provide an ablation showing that the method's performance does not degrade when the validation set is clean vs. noisy at the same rate as the training set. Without this, the claimed mechanism for identifying "informative" samples is unverifiable.

2. **Ablate α and the validation split ratio.** Show that the method works without α=1000 (test α ∈ {10, 100}) and that the 10% validation split is not responsible for the observed improvements (e.g., by comparing against a baseline that simply discards 10% of noisy samples).

3. **Analyze the shifted candidate set composition.** Report what fraction of unique clean vs. noisy samples survive in the final shifted training set, and how many copies each surviving sample has. This would clarify the mechanism (promotion of clean samples vs. dilution through volume).

4. **Correct the overclaim in the conclusion.** Remove "generative tasks" from the conclusion statement unless supported by experiments, or add at least one generation benchmark.

## Score and Decision

The paper tackles a genuinely overlooked problem and provides strong empirical results. However, the primary structural weakness — computing the reward signal against noisy validation labels — undermines the claimed mechanism for identifying informative samples. The paper's own acknowledgment of this issue is insufficient and lacks supporting analysis. While the empirical results may still hold, the gap between the claimed mechanism and what the experiments can verify is too large to accept without resolution. On the positive side, the problem framing is novel, the integration with diverse retrievers is practical, and the empirical gains are large and consistent.

**Originality:** Good — the distribution-shift framing for noisy ICL is new.  
**Importance of question:** High — label noise in ICL candidate sets is a real, underexplored problem.  
**Claims adequately supported:** No — the central claim that ConDS identifies "informative" (clean) samples is undermined by the noisy validation reward.  
**Soundness of experiments:** Moderate — strong results but insufficient ablation on the reward signal's validity and key hyperparameters.  
**Clarity:** Adequate — the paper is readable but the theoretical analysis is deferred to an appendix.  
**Value to community:** Potentially high, if the reward-signal issue is resolved.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
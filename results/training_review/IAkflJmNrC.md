Now I have thoroughly verified the reviewer claims against the paper. Let me produce the final consolidated review.

## Summary

This paper investigates fine-tuning sentence embeddings (using sentence-transformers) for polarity-aware semantic retrieval — simultaneously retrieving sentences of the same sentiment/polarity while maintaining high semantic similarity. The authors propose two evaluation metrics (Polarity Score and Semantic Similarity Score), generate training data via nearest-neighbor search with a similarity threshold within each polarity class, and systematically compare four loss functions (TripletLoss, ContrastiveLoss, OnlineContrastiveLoss, MultipleNegativesRankingLoss) with multiple margin values across two binary classification datasets (SST-2, sarcastic headlines). The main finding is that TripletLoss with very small margins (λ=0.01–0.1) on e5-small-v2 yields the best trade-off, substantially improving polarity while incurring only a modest drop in semantic similarity.

## Strengths

- **Novel dual-metric evaluation framework for polarity-aware retrieval**: The paper introduces Polarity Score and Semantic Similarity Score (Sections 3.1.1–3.1.2) that jointly quantify how well fine-tuned embeddings preserve both class-label agreement and original semantic similarity. This directly addresses the underexplored trade-off between these objectives, going beyond standard accuracy or STS benchmarks.

- **Systematic loss-function comparison revealing a non-obvious finding**: By evaluating four loss functions across multiple margin values on two datasets (Tables 5 and 6), the paper identifies that TripletLoss with very small margins (λ=0.01–0.1) outperforms default larger margins (5.0) and all other losses. This contradicts the intuition that larger separation margins are better and provides a concrete, reproducible recipe.

- **Demonstrated manageable trade-off with clear evidence**: The aggregated results (Table 4, Figure 3) show that as training sample size increases, polarity scores rise substantially (e.g., ~0.88→~0.94) while semantic similarity drops only slightly (~0.84→~0.82), establishing that the trade-off is favorable.

- **Strong transfer performance on SentEval**: The best configuration (e5-small + TripletLoss λ=0.1) outperforms SetFit on 7 out of 8 SentEval tasks (Table 7), notably achieving 91.3% on MR and 88.3% on SST-2 versus SetFit's 88.2% and 82.6%. This demonstrates that polarity-aware fine-tuning does not degrade general embedding quality.

## Weaknesses

### Fatal
None.

### Major

- **Underspecified data generation procedure**: Section 3.4 states "compute the k nearest neighbors of each polarity" for data generation, but the value of k used during this process is never specified (the k=16 in Section 3.2 is for evaluation retrieval, not data generation). The dropout mechanism used to control the number of generated examples (~250k) is described only vaguely ("introducing a dropout, tuned to generate roughly 250,000 examples") without specifying the rate or procedure. These omissions prevent exact replication and make it difficult to assess the sensitivity of the method to these design choices.

- **No ablation of the similarity threshold in data generation**: The minimum semantic similarity threshold of ≥0.5 for selecting positive pairs (Section 3.4) is a core design decision, yet it is never ablated. The paper does not compare against (a) using all same-label sentences as positives (no threshold) or (b) a higher threshold (e.g., ≥0.7). Without this ablation, it is unclear whether the threshold is critical for preserving semantic similarity or whether simple label-based grouping would suffice — a meaningful gap given the paper's central claim about the data generation scheme.

### Minor

- **Missing qualitative retrieval examples**: The evaluation relies entirely on two aggregate metrics (Polarity Score and Semantic Similarity Score). No query sentences with their top-retrieved results are shown. For a paper titled "Polarity-Aware Semantic Retrieval," showing even 3–5 concrete retrieval examples (comparing the best fine-tuned model against the pre-trained baseline) would substantially strengthen the reader's confidence that the model actually retrieves sentences that are both semantically similar and of the same polarity.

- **Reference model for Semantic Similarity Score not explicitly named**: Section 3.1.2 defines the Semantic Similarity Score using "a baseline reference model R, pre-trained for semantic similarity" but never explicitly states that R is the pre-trained version of whatever model M is being fine-tuned (e.g., pre-trained e5-small is the reference for fine-tuned e5-small). While this is clearly implied by the experimental setup (Table 1 baselines, line 138 "reference model" highlighted in Tables 5–6), stating it explicitly would improve clarity. The concern about inter-model S comparisons changing the reference is partially valid but mitigated because S is designed as a within-model degradation metric, not an absolute cross-model comparison.

- **Modest baseline coverage**: The paper compares against pre-trained models and SetFit (a fine-tuning baseline), which provides useful context. However, a simple classification fine-tuning baseline (e.g., adding a linear classifier on top of the [CLS] token and training with cross-entropy, then using the raw embeddings for retrieval) is not included. Such a comparison would help isolate whether the specific example generation procedure adds value beyond any label-informed fine-tuning. The paper's existing baselines partially address this concern (SetFit is itself a fine-tuning method, and multiple contrastive/triplet losses are evaluated), making this a gap rather than a fatal omission.

### Trivial

- The k value used for nearest-neighbor search during data generation is not specified, while k=16 is stated only for evaluation.

## Nice-to-Haves

- **Qualitative retrieval case study**: Showing 5–10 test queries with top-5 retrieved sentences would greatly improve the paper's persuasive power and could be added without additional experiments.
- **Ablation of the similarity threshold** (≥0.5 vs. no threshold vs. ≥0.7) to validate its necessity.
- **Multi-class extension**: The paper mentions this as future work, but extending to a dataset like AG News using one-vs-rest example generation would strengthen the generalization claim.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **MultipleNegativesRankingLoss "wasting space" in tables** — Removed. The paper explains why MNRL performs poorly (contradictory examples due to shared anchors). Including it is thorough, not wasteful, and the explanation is informative.
2. **Reproducibility statement called "weak"** — Removed. The paper commits to deterministic random states, precomputed datasets, programmatic generation of all results, and provides parsed/anonymized data. This is a reasonable reproducibility statement for a conference paper.
3. **SentEval called "only tangentially relevant"** — Removed. SentEval is the standard benchmark for sentence embedding evaluation. Demonstrating strong transfer performance directly supports the claim that semantic similarity is preserved and that the embeddings remain useful beyond polarity retrieval.
4. **Criticism that reference model is never specified** — Weakened from "never specified" to "not explicitly named." The paper makes the reference clear through context (Table 1 baselines serve as references; line 138 mentions "reference model" highlighted in Tables 5–6). The design choice is clear, though stating it explicitly would improve clarity.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no observation about the paper's approach, results, or framing that the authors themselves do not already acknowledge or discuss.

## Suggestions

1. **Specify k and dropout details in Section 3.4**: Report the exact k used for the data-generation nearest-neighbor search and describe how the dropout is applied (rate, random vs. stratified). This is essential for reproducibility.
2. **Add at least one ablation of the similarity threshold**: Compare the proposed ≥0.5 condition against using all same-label sentences as positives (no threshold). This would directly validate whether the threshold matters.
3. **Include a qualitative retrieval table**: Show 3–5 test queries with top-5 results for the best model (e5-small + TripletLoss λ=0.1) versus the pre-trained baseline, annotating polarity. This would make the paper's central claim concrete for readers.
4. **Explicitly state the reference model for the Semantic Similarity Score**: Clarify in Section 3.1.2 that for any fine-tuned model M, the reference R is the pre-trained version of M (i.e., the model before fine-tuning).

## Score and Decision

The paper addresses a relevant and underexplored problem with a systematic experimental design. The dual-metric evaluation framework is a genuine methodological contribution, and the finding that TripletLoss with extremely small margins (0.01–0.1) works best is non-obvious and useful. The main weaknesses — underspecified data generation details, a missing ablation, and the absence of qualitative examples — are addressable in revision and do not invalidate the core findings. The paper makes a modest but clear contribution to the sentence embedding literature.

Originality: Moderate. The idea of polarity-aware retrieval is not entirely new, but the combination of a custom data generation scheme plus systematic loss-function comparison is novel.

Importance of research question: Good. Polarity-aware retrieval has practical applications in content moderation, review analysis, and opinion retrieval.

Claims well supported: Yes, for what is shown. The core claim (TripletLoss with small margins on generated data improves polarity with manageable similarity loss) is supported. Missing ablations limit some secondary claims.

Soundness of experiments: Adequate. The systematic across-loss-function and across-margin comparison is a strength. The missing ablation of the data generation threshold is a gap.

Clarity of writing: Good. The paper is well-structured and the metrics are clearly defined. The underspecification of data generation k and dropout are clarity issues.

Value to community: Moderate. The finding about small-margin TripletLoss and the proposed evaluation framework may be useful for practitioners working on domain-specific or attribute-aware retrieval.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
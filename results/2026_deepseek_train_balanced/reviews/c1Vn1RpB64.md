Everything is verified. I'll now output the final review.

## Summary
The paper proposes SparseCL, a method for contradiction retrieval that trains sentence embeddings to preserve sparse differences between contradictory passages. At inference, documents are scored by a weighted sum of cosine similarity (from a standard embedding model) and Hoyer sparsity of the embedding difference (from a SparseCL-fine-tuned model). Experiments on the Arguana counter-argument dataset and two synthetic datasets (GPT-4-contradictions on MSMARCO and HotpotQA) show gains: ~4.8% on Arguana and >30 percentage points on the synthetic benchmarks. A corpus-cleaning application is also demonstrated.

## Strengths

- **Novel and well-motivated scoring function.** The paper identifies a genuine limitation of pure similarity search for contradiction retrieval and proposes a principled remedy: combining cosine similarity with Hoyer sparsity of the embedding difference (Eq. 7). The intuition that contradictions share topical overlap but differ sharply in a few semantic coordinates is clearly articulated (lines 55–58) and supported by the sparsity histograms in Figure 3.

- **Large, interpretable gains on the synthetic benchmarks.** On the MSMARCO and HotpotQA synthetic datasets, cosine-similarity retrieval necessarily fails because GPT-4 paraphrases are closer to the query than GPT-4 contradictions are. SparseCL achieves >30 pp NDCG@10 gains (line 126), cleanly demonstrating that the sparsity signal succeeds where similarity alone cannot.

- **Architecture-agnostic improvement.** Consistent NDCG@10 improvements are observed across three different pretrained backbones (GTE-large-en-v1.5, UAE-Large-V1, bge-base-en-v1.5) in Table 1, showing the method generalizes across architectures.

- **Controlled robustness ablation.** The augmented Arguana experiment (Table 4) shows that as the number of similar non-contradictory paraphrases in the corpus increases, similarity-based methods degrade sharply while SparseCL remains stable. This is the paper's strongest experimental point.

- **Zero-shot transfer between synthetic datasets.** Section 4.3 (Table 2) shows that SparseCL trained on one synthetic dataset transfers to the other with only slight degradation, providing evidence that the learned representations capture a general notion of contradiction rather than dataset-specific artifacts.

## Weaknesses

### Fatal
None.

### Major

- **Cross-encoder is positioned as the accuracy ceiling but never evaluated.** The paper repeatedly contrasts its approach with cross-encoders ("accurate but expensive," line 21; "much more efficient than a cross-encoder," line 23; Figure 2). Yet no cross-encoder result appears anywhere in the experimental section. Without this baseline, the reader cannot assess the accuracy–efficiency trade-off the paper claims to navigate. The cross-encoder could establish an upper bound that SparseCL either approaches or falls far short of — either datum would materially change the interpretation of the contribution.

- **The Shi et al. (2023) comparison is promised but missing.** Line 103 states "For completeness, we also compare our results with Shi et al." but no quantitative comparison is provided. The sentence cuts off and no Shi et al. numbers appear in Table 1 or anywhere else in the paper. An explicitly promised comparison that is never delivered.

### Minor

- **The two-model cost of the scoring function is not discussed.** The scoring function (Eq. 7) uses two separate models: a standard embedding model E() for cosine similarity and a fine-tuned model E_s() for Hoyer sparsity. This means every passage must be encoded twice, doubling storage and encoding cost relative to a single bi-encoder. The ablation in Table 5 shows that Hoyer sparsity alone ("SparseCL (Hoyer)") performs poorly, so both models are necessary. The paper presents the method as "much more efficient than a cross-encoder" but never acknowledges it is twice as expensive as the bi-encoder baselines it is actually compared against.

- **The synthetic benchmarks, where the headline gains occur, use only GPT-4 generated text.** All human-written passages are removed; both queries and corpus documents are GPT-4 outputs. The paper acknowledges (line 118) that "all the GPT-4 generated passages are easily distinguishable from the human written ones," which is why they removed the originals. However, this means the task reduces to distinguishing GPT-4 contradictions from GPT-4 paraphrases. A method could exploit surface-level patterns rather than learning about contradiction in general. The zero-shot transfer experiment (Section 4.3) partially mitigates this, but the synthetic evaluation remains substantially artificial.

- **No statistical significance reported.** All results are single numbers without variance, confidence intervals, or number of runs. For the ~4.8% improvement on Arguana, this matters — it is unclear whether this gain is stable or within the noise of a single evaluation.

- **Abstract/body inconsistency in reporting gains.** The abstract claims "more than 30% accuracy improvements" (line 4), while the body reports "over 30 percentage points gain" (line 126). These are different quantities; the abstract language is imprecise.

### Trivial

- **Imprecise motivation via "transitivity" of cosine similarity.** The claim (line 21) that cosine similarity "is transitive: if A is similar to B, and B is similar to C, then A is also similar to C" is not a formal property of the cosine function but a heuristic statement about embedding geometry. The conceptual point — that cosine similarity cannot distinguish contradictory from agreeing pairs that are both close in embedding space — is valid, but the framing is sloppy.

## Nice-to-Haves

- Analyze sensitivity of the α parameter (weighting cosine vs. sparsity) across its range.
- Report results using the same model for both cosine and sparsity components to understand whether separate models are necessary or merely convenient.
- Test on a naturally occurring contradiction retrieval task beyond the debate domain (e.g., conflicting news articles) to strengthen ecological validity.

## Removed Points

The following points from the input reviews were removed or demoted after verification against the paper:

- **Criticism of in-batch negative sampling as "not well-motivated":** Standard contrastive learning practice; the critic's speculation about training dynamics is not substantiated by any evidence in the paper.
- **Claim that α-tuning on validation set introduces overfitting risk:** Tuning a single scalar on a validation set is standard practice; this is not a meaningful weakness.
- **Criticism that the "related work" on adversarial attacks is "left dangling":** The paper clearly distinguishes its setup from adversarial attacks (line 47); asking for experiments outside the paper's stated scope is scope creep.
- **Claim that the "transitive" argument is fundamentally confused:** Retained as Trivial rather than Major because the conceptual point is correct even if the phrasing is imprecise.
- **Formatting nitpick about garbled Table 6 LaTeX (line 199):** This is a PDF-parser artifact, not an author error.
- **Generic speculation about "could the metric be measuring a proxy":** No concrete anchor in the paper; unsubstantiated speculation.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add cross-encoder results (even on a subset of data) to establish the accuracy ceiling and validate the claimed accuracy–efficiency trade-off.
2. Deliver the promised Shi et al. (2023) comparison, or remove the dangling sentence.
3. Acknowledge and discuss the two-model overhead explicitly.
4. Report variance statistics (e.g., 3–5 runs with different seeds) for the Arguana results.
5. Align the abstract's language with the body's precision.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
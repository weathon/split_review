- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 5, 6, 6
Now I have a thorough understanding of the paper's content and all reviewer claims. Let me construct the final consolidated review.

---

## Summary

This paper proposes Relevance-Based Embeddings (RBE), a method that represents queries and items via their relevance scores to a small pre-selected set of "support" items (and queries), then applies a trainable neural mapping (a 2-layer MLP with a residual connection to a linear AnnCUR term) to produce embeddings for approximate nearest neighbor search. The paper also studies strategies for selecting support items — including clustering-based and greedy approaches — showing they substantially outperform the random selection used in prior work. Experiments on ZESHEL entity linking domains and production recommendation data compare RBE against the AnnCUR baseline (Yadav et al., 2022) and a production dual encoder.

## Strengths

1. **Well-designed study of support item selection strategies**: Table 2 evaluates six selection strategies (Random, Popular, three clustering methods, Greedy) applied to the AnnCUR framework across five datasets. The results are clear and compelling: greedy selection is uniformly best, KMeans is a strong second, and all non-random strategies substantially outperform random selection. This is a clean, self-contained contribution that practitioners can directly use. (Section 4.2)

2. **Evaluations on diverse domains and ranker types**: The paper tests on both textual ZESHEL datasets (where the heavy ranker is a cross-encoder) and production recommendation data (where the heavy ranker is CatBoost, a gradient boosting model). This breadth supports generalizability and is a genuine strength over prior work that focused on narrower settings.

3. **Theoretically motivated approach**: The paper provides a theorem (Section 3) stating that relevance-based embeddings can approximate any continuous relevance function, providing formal grounding beyond heuristic justification. The practical discussion (Section 3.3) thoughtfully addresses deployment concerns including dynamic item sets, scalability of support selection, and inference pipeline compatibility with standard ANN indexes.

4. **Favorable comparison against a production dual encoder under a cost-adjusted metric**: In Section 4.4, the paper accounts for the |S_I|=100 heavy-ranker calls needed to form the RBE query vector by giving the dual encoder 100 extra retrieved candidates. RBE outperforms the dual encoder at top sizes ≥300 (Table 4) and at K≥200 (Table 5), demonstrating that relevance-based representations can be more efficient than a separately trained embedding model given the same budget of expensive ranker calls.

## Weaknesses

### Fatal

None.

### Major

1. **Neural mapping contribution is not isolated from support selection contribution**: The headline comparisons in Table 3 compare full RBE (smart support selection + neural mapping) against AnnCUR *with random support*. Since Table 2 establishes that better support selection alone (without the neural mapping) already yields large improvements over random, the reader cannot tell how much of the reported 33% average improvement is due to the neural mapping versus due to better support selection. A direct comparison of RBE(greedy) against AnnCUR(greedy) — isolating the neural mapping — is the single most important missing ablation. The paper acknowledges this implicitly by noting "the transformation that we use is not claimed to be optimal" and is "rather to demonstrate that with the help of an easy transformation, one can get an increased quality," but the evaluation design conflates two separate contributions, making it impossible to assess the neural mapping's independent value. This does not invalidate the paper's contributions but substantially weakens the evidence for its strongest claims.

2. **The paper chooses KMeans for further experiments despite greedy being uniformly better**: Table 2 shows greedy is "the clear winner" across all datasets. Yet the paper states "KMeans will be used in further experiments" — justified only by AgglomerativeClustering's poor performance on Military, which is irrelevant since greedy (not AgglomerativeClustering) is the alternative. The dual encoder comparison (Section 4.4) and much of the neural RBE analysis uses KMeans rather than the demonstrably better greedy selection. This is an unexplained methodological choice that weakens the headline comparisons. (Lines 198, 220)

### Minor

1. **Imprecise framing of improvement claims**: The abstract claims "average improvement of 33% over this baseline (from 8% to 69%)" and "improved performance over existing approaches." The baseline is AnnCUR with random support — the weakest variant of the competing method. Saying "over existing approaches" without qualifying that the improvement is against the weakest variant, and that it is non-uniform (the paper acknowledges Military as an exception), gives an inflated impression. The paper would be better served by stating the comparison precisely.

2. **Dual encoder comparison methodology is unconventional**: Section 4.4 uses HitRate(X+|S_I|, X) for the dual encoder and HitRate(X, X) for RBE. While the paper transparently explains this adjustment and notes it "gives the former an advantage with small top sizes," an equal-retrieval-size comparison (both at the same K, treating the |S_I| calls as a separate latency cost) would be easier to interpret and would remove a confounding factor from the comparison.

### Trivial

None.

## Nice-to-Haves

- An ablation showing the effect of support set size |S_I| (all experiments use 100; results for smaller values would clarify the practical tradeoff).
- Ablation on the MLP architecture (e.g., linear-only, deeper networks) to validate the design choices.
- Wall-clock runtime comparisons for the query-side overhead of |S_I| relevance calls.

## Removed Points

- **Harsh critic's specific numerical claims about American Football (0.9495 vs 0.8943)**: These numbers come from table images that are not accessible in the parsed text, and the paper's own text states "in most cases, except for one dataset (Military)" improvements are observed for RBE over AnnCUR. The specific numerical comparison between AnnCUR(greedy) and RBE(greedy) cannot be verified from the available text and is not discussed in the paper. The general structural concern about missing ablation is retained above.
- **Criticism that the dual encoder comparison is "not fairly calibrated"**: The paper transparently describes its cost-adjusted metric (giving the dual encoder an advantage). This is a reasonable methodological choice, not a flaw. The equal-set-size comparison is noted as a nice-to-have.
- **Criticism that the "33% improvement" is "selective reporting" for excluding worst-case**: The paper acknowledges "except for one dataset (Military)" where improvement is not observed. Without verifiable numbers from the table images, this specific accusation cannot be confirmed. The general imprecision of claims is retained as a minor weakness.
- **Strength Finder's claim of "Empirical superiority over a strong baseline" (as originally stated)**: Modified to acknowledge the baseline is the weakest AnnCUR variant, and that improvement is not universal.
- **Strength Finder's supporting strength about "theoretical grounding" (Theorem in Section 3)**: The theorem statement and proof are absent due to parser artifacts. Retain only as "theoretically motivated approach" in Strengths.
- **Nitpicks about missing loss function ablations, hyperparameter details, and runtime numbers**: These are either standard for the field or secondary to the core contribution.

## Novel Insights

The most interesting observation emerging from the reviews — not fully articulated by the paper itself — is that the *support item selection* contribution (Table 2) may actually be the more robust and practically valuable result than the neural RBE. The greedy selection strategy yields substantial gains for the simple linear AnnCUR framework, and the question of whether a trained neural mapping adds further value on top of good support selection remains unanswered. This suggests a potentially simpler takeaway: practitioners working with relevance-based retrieval should first optimize support item selection, as this alone closes much of the gap to more complex approaches.

## Suggestions

1. **Add the critical missing ablation**: Compare RBE(greedy) against AnnCUR(greedy) in a single table, so the neural mapping's independent contribution is cleanly visible. If the neural mapping helps on some datasets and hurts on others, report that honestly and discuss the pattern.

2. **Reposition the claims**: Frame the paper's two contributions — support selection strategies and neural relevance-based embeddings — separately, with separate empirical evidence for each. The support selection study is already strong; let it stand on its own rather than being conflated with the neural component.

3. **Clarify the choice of KMeans over greedy**: Either explain why greedy is not used as the default for neural experiments (e.g., computational cost, overfitting concerns) or switch to greedy for the main comparisons, since it is uniformly better in Table 2.

Now I have a thorough understanding of the paper and can produce the consolidated review.

---

## Summary

DDLR proposes a dual-denoising framework for inductive knowledge graph completion that filters noise at both the path level (by scoring and selecting important reasoning paths) and the edge level (by sampling relations relevant to the query via rule-based confidence). On three benchmark datasets across four inductive splits each, DDLR achieves state-of-the-art or second-best results, and thorough ablations confirm both denoising modules contribute positively.

## Strengths

- **Dual denoising is well-motivated by concrete failure modes of prior work.** The paper identifies two specific problems with node-score-based methods (Figure 1): node scores can select the wrong entity and miss the correct one, and they can produce the correct answer through spurious pseudo-evidence paths. DDLR's path-scoring mechanism addresses the first issue, and edge sampling via single rules addresses the second. This grounded motivation goes beyond a generic "denoising" pitch.

- **Path-scoring mechanism is novel and validated by ablation.** The scoring function (Eq. 8–10) jointly considers the current path score and an estimate of the remaining path score. Table 3 shows that ablating either component (DDLR-w.o.-current, DDLR-w.o.-remain) degrades performance, confirming both components contribute.

- **Edge sampling via triplet-level single rules is a finer-grained approach that outperforms alternatives.** Table 4 demonstrates that the proposed relation-relevance measure (single rules) substantially outperforms cosine similarity, KL divergence, and JS divergence. Table 2 confirms that removing edge sampling (DDLR-w.o.-edge) or replacing triplet-level rules with entity-level ones (DDLR-w.o.-triplet) leads to performance drops.

- **Strong empirical results across a comprehensive experimental setup.** DDLR achieves the best or second-best results on all 12 inductive splits (four each for WN18RR, FB15k-237, NELL-995), outperforming strong GNN-based baselines including NBFNet, RED-GNN, Adaprop, and GraPE. The paper follows established inductive KGC protocols (Teru et al., 2020) and performs extensive hyperparameter tuning.

- **Thorough ablation studies isolate each component's contribution.** The paper systematically ablates path sampling, edge sampling, triplet-level rules, and sub-components of the path-scoring function (Tables 2–3), providing clear evidence for each design choice.

## Weaknesses

### Fatal
None.

### Major

- **The remaining path score is independent of the target entity, limiting the claim of "path importance to the target."** Equation (8) defines \(r_q^{(t)}(x,v)\) using only the current path representation \(h_q^{(t)}(u,x)\) and the query relation \(q\), with no dependence on the target entity \(v\). The paper explicitly acknowledges this as an approximation ("we do not possess the representation of the answer entity \(v\)"), which is reasonable in an inductive setting where \(v\) is unknown. However, it means that for a fixed intermediate node \(x\), the score is identical for every candidate answer \(v\), so the top-\(K\) selection in Eq. (11) selects nodes based on query-conditioned relevance rather than on the likelihood that the path reaches the specific correct target. This undermines the advertised claim of evaluating paths "to the target" as opposed to the query. The ablation in Table 3 shows the component still provides useful signal, but the paper should more carefully qualify what the path-scoring function actually measures, provide empirical justification for the approximation (e.g., an oracle comparison in a transductive setting), or discuss scenarios where this approximation might fail.

### Minor

- **The edge-sampling confidence formulation (Eq. 14) is notationally imprecise.** The equation sums over \(t \in \mathcal{E}\) (triplets) and uses \(\mathbf{E}_r(t)\) to "extract relations from the triplets." Since a standard triple \((h, r, t)\) contains exactly one relation \(r\), a literal reading makes the numerator impossible for distinct \(r_1, r_2\). The descriptive text ("C(r1 ⇒ r2) is larger if more triplets with relation r1 also have r2") makes the intended co-occurrence semantics clear, and the fix is straightforward (e.g., iterating over entities and extracting the set of relations involving that entity). However, as written, the equation is ambiguous enough to cause confusion. The authors should clean up the notation to precisely match the intended computation.

- **The missing table numbers are parser artifacts, not author errors** — this was removed per instructions.

### Trivial
None.

## Nice-to-Haves

- **Reporting variance or significance tests.** The paper conducts extensive hyperparameter search, raising the possibility of incidental test-set overfitting. Reporting results across multiple random seeds (e.g., 3–5 runs) with mean and standard deviation, or at least significance tests against the closest baseline (Adaprop), would strengthen the empirical claims. This is a common practice request, not a requirement for KGC papers.

- **Provide more detail on how the cosine/KL/JS baselines in Table 4 are computed.** The paper briefly states these are standard measures; a sentence clarifying the exact input representations (relation embeddings vs. frequency vectors) would improve reproducibility.

## Removed Points

*(These points are flagged to be removed; treat them with caution.)*

- **"Results cannot be verified because table images are missing from the extracted text."** — Removed. The image placeholders are a parser artifact from PDF extraction; the original submission contains the actual numbers. This is not an author error.

- **"No uncertainty measures" characterized as a major evidence weakness.** — Moved to Nice-to-Haves. Single-run evaluation on standard splits is the norm in KGC, not a flaw specific to this paper.

- **The harsh critic's claim that the edge-sampling equation "invalidates a central component of the proposed dual denoising framework."** — Removed as overstatement. The formulation is imprecise but the intent (relation co-occurrence statistics) is clear from the text description and the fix is trivial. The claim that the component is "unusable" or "degenerate" is not supported by the paper's own description of what they intended to compute, nor by the ablations showing the component helps.

- **"The comparison in Table 4 is not described."** — Weakened to Nice-to-Haves. The paper does state what Cosine, KL DIV, and JS DIV mean, though more detail would help.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a perspective that the paper's authors had not already articulated.

## Suggestions

1. **Clarify the path-scoring function's scope.** Reword claims about path importance to specify that the scoring function evaluates relevance to the *query relation* (rather than to the *specific target entity*), and acknowledge the approximation more prominently as a limitation rather than an implementation detail. Consider adding an oracle experiment (e.g., in a transductive setting where \(v\) is known) to quantify how much the approximation costs.

2. **Fix the notation in Eq. (14).** Replace the ambiguous summation over triplets with a clear description of relation co-occurrence statistics (e.g., summing over entities and extracting the set of relations from all triplets involving that entity, or using entity-pair co-occurrence). Ensure the equation matches the textual description.

3. **Add variance statistics.** Report mean and standard deviation over multiple seeds (3–5) for the main results and key ablations to demonstrate stability.

## Score and Decision

The paper proposes a well-motivated dual-denoising framework, provides thorough ablations that validate each component, and achieves strong empirical results across 12 inductive splits. The two main weaknesses are (a) the path-scoring approximation is a genuine limitation that the paper acknowledges but does not thoroughly justify, and (b) the edge-sampling notation is imprecise. Neither flaw invalidates the core contribution — the method works well despite the approximation, and the notation is fixable. The paper would benefit from clearer framing of the approximation's limitations and cleaner notation, but the overall contribution is solid and the experiments are comprehensive.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
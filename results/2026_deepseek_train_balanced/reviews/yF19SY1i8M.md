## Summary

This paper addresses the problem of evaluating NLP systems when some systems have missing scores on entire benchmark tasks—a practically important scenario ignored by prior aggregation work. The authors propose a partial-ranking approach that imputes missing entries using compatible permutations, aggregates via Borda count, and achieves O(n³) complexity. They release a benchmark expanded from 250K to over 131M scores. The core idea is principled and grounded in social choice theory.

## Strengths

1. **Explicit problem formalization for missing-task evaluations**: The paper defines Problems 1 and 2 (lines 56–67) with task-level and instance-level settings where $N_t$ (number of systems evaluated on task $t$) can differ across tasks. Prior work (Colombo et al. 2022) assumed $N_t = N$; this formalization is a necessary prerequisite that previous work did not provide.

2. **Efficient O(n³) algorithm for matrix representation**: The paper reduces the generation of the compatible-permutation matrix from factorial to O(n³) complexity (line 122) via closed-form expressions for $p_{i,j}$. This is computationally critical—without it the method is infeasible for N > 10—and is a concrete algorithmic contribution enabling practical use.

3. **Extended 131M-score benchmark**: The dataset collection spans five task families (dialogue, image description, summary evaluation, data-to-text, translation), expands metrics from 10 to 17, and grows the total from 250K to over 131M scores (line 218). This is a substantial resource contribution, orders of magnitude larger than prior collections.

4. **Quantitative robustness advantage on real benchmarks**: In task-level robustness experiments (line 224), $\sigma^l$ achieves a "large improvement of more than 10 points" in Kendall $\tau$ over $\sigma^\mu$ in the moderate-missingness regime ($\eta \in [0.05, 0.4]$), consistently across GLUE, SGLUE, XTREME, and GEM.

## Weaknesses

### Fatal
None.

### Major

1. **Missing ground-truth accuracy evaluation on synthetic data**: The synthetic experiments (Section 4) generate scores from Gumbel variables with a known true ranking $[1, \dots, N]$ (line 179). This setup admits a direct accuracy test: randomly remove scores and compare each method's output against the *true* ranking. Yet the paper never runs this experiment. Instead, it tests scaling invariance (Section 4.2)—a property that is definitional for any ranking method, not a finding—and confidence analysis (Section 4.3). The real-data experiments (Sections 5.2–5.3) measure only self-consistency (Kendall $\tau$ between full-data and missing-data rankings), which conflates stability with accuracy: a method that barely changed its output regardless of input would score well. The core claim is that $\sigma^l$ "effectively tackles the issue of missing system evaluations" (line 18), but the evaluation never directly tests whether $\sigma^l$ recovers a correct ranking from incomplete data when the correct ranking is known. This is the single most important missing experiment.

### Minor

2. **Single baseline comparison**: The paper compares only against $\sigma^\mu$ (mean aggregation over available scores, ignoring missing entries). The authors state "there is no established method" (line 155), which justifies not comparing against a standard baseline, but adding even one additional approach—such as mean imputation (fill missing task scores with system averages) or a simple pairwise Bradley-Terry model—would substantially strengthen the evidence. The claim that $\sigma^l$ "effectively tackles the issue" (line 18) would be more convincing if it outperforms multiple reasonable approaches, not just the one approach the paper itself describes as "unsatisfactory" (line 13).

3. **Low agreement between methods reported without resolving accuracy**: Tables 1–4 show low Kendall $\tau$ between $\sigma^l$ and $\sigma^\mu$ (0.17 on GLUE, top-1 agreement as low as 10%). The paper presents this as evidence the methods "produce different conclusions" (line 229). This is factually correct but would carry more weight if accompanied by evidence (from synthetic data with ground truth) that $\sigma^l$'s conclusions are closer to the truth, not merely different.

4. **Confidence interval formula appears incorrect**: Equation (7) gives $c_{ij} = \sqrt{-\log \delta \,/\, (2 z_{ij})}$. The standard two-sided Hoeffding bound for bounded $[0,1]$ variables gives $c = \sqrt{-\log((1-\delta)/2) \,/\, (2z)}$. For $\delta=0.9$, the paper's formula produces intervals roughly 5× narrower than correct. This affects the claimed statistical guarantees in Sections 4.3 and 5.4. While the qualitative conclusions (e.g., block structure in Figure 5) may be robust, the formal guarantees are not as stated and need correction.

5. **Matrix definition appears reversed**: Line 116 defines $M^\pi_{ij}$ as "the proportion of complete rankings that are compatible with $\pi$ and satisfy the condition $i\succ j$." Line 118 then states: "if $i\succ j$ ... set $M^\pi_{i,j}=0$." If $i\succ j$ in the partial ranking, 100% of compatible rankings have $i\succ j$, so $M^\pi_{ij}$ should be $1$, not $0$. The closed-form expressions in the (stripped) appendix may resolve this via a different convention, but as presented the definition contradicts its own application.

### Trivial
None.

## Nice-to-Haves

- **Additional validation on synthetic data**: As noted in Major weakness 1, the synthetic data with known ground truth could directly measure ranking accuracy (distance to true ranking) under missing data. This would address the most significant evaluation gap.
- **Discussion of the uniformity assumption**: The method places a uniform prior over the positions of missing systems in compatible permutations (line 122 mentions a "proof for uniformity" in the appendix). The paper would benefit from discussing when this assumption is reasonable (e.g., missingness at random) and when it might fail (e.g., systematically missing large models).
- **A limitations section**: The conclusions (Section 6) contain no discussion of limitations, assumptions, or failure modes, which is a notable absence for a paper addressing a novel problem.

## Removed Points

These points were flagged by one of the input reviews but are removed or downgraded per filtering rules:

- **"Straw man baseline"** — Removed. $\sigma^\mu$ is the de facto standard used in practice; it is not a straw man. The paper would benefit from more baselines (Minor weakness 2 above), but the existing baseline is legitimate.
- **"Structural/fatal: evaluation design guarantees method wins"** — Downgraded to Major (weakness 1). The stability measure is meaningful for robustness, but the missing ground-truth experiment is a genuine and significant gap. The critic's framing of "fatal" overstates the problem, as the synthetic experiments do show $\sigma^l$ tracks the data (it is not a constant function).
- **"Inputting" vs "imputing" terminology issue** — Removed per hard rules (trivial word-choice issue that does not affect scientific content).
- **"Figures not visible"** — Removed (parser/formatting artifact).
- **Notation and scenario-conflation criticisms** — Removed or weakened; the formalism follows Colombo et al. (2022) closely and is adequate for the paper's purposes.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the evaluation gap (missing ground-truth accuracy experiment) but do not offer technical insights the paper itself lacks. The CI formula correction is a standard mathematical verification, not a novel observation.

## Suggestions

1. **Add a synthetic accuracy experiment**: On the synthetic Gumbel data (Section 4.1) with known true ranking, randomly remove a proportion $\eta$ of scores and measure the Kendall $\tau$ (or Spearman footrule distance) between each method's output and the *true* ranking. This directly tests whether $\sigma^l$ produces more correct rankings under missing data.
2. **Add at least one more baseline**: Mean imputation or a pairwise Bradley-Terry model would substantially strengthen the empirical claims.
3. **Fix the confidence interval formula**: Correct Equation (7) to use the standard two-sided Hoeffding bound or provide justification if a different bound is being used.
4. **Resolve the matrix definition reversal**: Clarify whether $M^\pi_{ij}=0$ when $i\succ j$ is a convention (e.g., $M_{ij}$ encodes the probability that $j$ beats $i$) or correct the error.
5. **Add a limitations paragraph** discussing the uniformity assumption and potential failure modes (e.g., informative missingness).

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
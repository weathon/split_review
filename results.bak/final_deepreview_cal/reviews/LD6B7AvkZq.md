Now I have enough calibration. Let me write the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
// List only reasonable points. Rank by severity.
// Not every paper has weaknesses at every tier. Leave a tier empty (or write "None") if nothing qualifies.

### Fatal
// Errors that invalidate the paper's core claims or results.
// Examples: fundamentally flawed methodology, unsupported central claim, incorrect proofs, data fabrication concerns.
// Most papers have none. Leave empty if none apply.

### Major
// Issues that a reviewer would weigh against acceptance, and that the authors should fully resolve in a rebuttal.
// Examples: missing critical baseline, overclaimed scope unsupported by experiments, significant methodological gap.
// Not every paper has major weaknesses. Do not invent them to fill this section.

- weakness 1 — why it matters
- weakness 2 — why it matters

### Minor
// Issues worth the authors' attention but unlikely to change an accept/reject decision.
// Examples: addressable in rebuttal, limited scope of one experiment, unclear phrasing of a claim, missing ablation that would strengthen but not invalidate.

- weakness 1 — why it matters

### Trivial
// Small issues the authors should fix but that carry no weight in evaluation.
// Examples: typos, minor notation inconsistencies, suboptimal figure choices, small presentation issues.

- weakness 1

## Nice-to-Haves
- suggestion that would improve but is not a core flaw

## Removed Points
Include something like this "These points are flagged to be removed, treat them with caution"
Weaknesses that are removed keep the details of the S/W just in case they are useful 

## Novel Insights
One paragraph synthesizing genuinely novel observations.
If no genuinely novel insight emerges from the reviews beyond the paper's own contributions, write
"None beyond the paper's own contributions."

## Suggestions
- specific actionable suggestion

DO differentiate between papers of varying quality clearly.

Do evaluate the paper on these axis using language first.
Originality, importance of research question addressed, whether the claims are well supported, soundness of experiments, clarity of writing, and value to the research community

## Score and Decision

Let me compile all the information now and write the review.

Key decisions on what to keep/remove:

**From Harsh Critic:**

1. "Equation (4) is mathematically unsound - ratios of log-probabilities" - This is a PDF parsing artifact. The original LaTeX likely had \log\frac{P}{Q} not \frac{\log P}{\log Q}. However, even with this correction, the derivation IS presented as a sketch without proper justification. I'll note the artifact and keep a weakened version about the derivation being too sketchy.

2. "Corollary 4.5 relies on unreasonably strong assumption" - The paper acknowledges this is a strong assumption. It provides some qualitative evidence. This is a valid concern but the paper is transparent about it. I'll keep this as a minor/major weakness.

3. "Theorem 4.6 not derived" - Many papers defer proofs to appendix. This is normal practice. Weakness is weak. Remove/downgrade.

4. "Empirical evaluation lacks crucial detail" - Valid. The paper doesn't specify architecture (embedding dim, #heads), training hyperparameters (batch size, lr, optimizer), or how KL is estimated. This is a significant issue. Keep.

5. "Novelty of subgrammar structure overstated" - The paper acknowledges Theorem 4.1 corresponds to Gruska 1971. The claimed novelty is the KL decomposition, not the DAG itself. This criticism is partially valid but somewhat overstated. I'll temper it.

6. "Missing citations for depth generalization" - WRONG. The paper DOES cite Bhattamishra et al. 2020 and Lampinen 2024. Remove completely.

7. "Figure 5 not in provided text" - PDF parsing artifact. Remove.

8. "GPT-5.1 anecdote not rigorous" - The paper itself calls it "purely anecdotal." So this is acknowledged. Remove as a significant weakness but note it as a minor issue.

**From Strength Finder:**

1. "Theorem 4.3 and Corollary 4.4" - This is the main theoretical contribution. Keep as strength but note the proof is in the appendix.

2. "Figure 1 empirical verification" - Interesting but the evidence is qualitative (visual inspection). Keep as a qualified strength.

3. "CKA analysis" - Shows some differences. Keep as a modest strength.

4. "Parallel learning observation" - Interesting but only visual inspection. Keep as qualified.

5. "Depth vs. length generalization" - Clean result. Keep as strength.

6. "Theorem 4.6" - Interesting but not verified as the proof is in the appendix. Keep as qualified.

Let me write the review now.**Calibration Report**

**Round 1 (Bracketing):** The paper was compared to anchors in three bands. Weak band (avg ≤3.5): papers on learning dynamics of formal languages scoring 3.0 (rejected for weak execution). Middle band (3.5–7.5): papers like "A Percolation Model of Emergence" (7.0), "Training Neural Networks as Recognizers" (6.25), "Sudden Drops in the Loss" (5.5), "How transformers learn structured data" (5.0). Strong band (≥7.5): theoretical analyses scoring 7.6–8.67. **Round 1 bracket: [4.0, 6.0].**

**Round 2 (Narrowing):** Queried for papers on KL decomposition/subgrammar dynamics (4–6) and transformer CFG learning (4–6.5). Compared against "Depth Extrapolation of Decoders" (4.5), "How transformers learn structured data" (5.0), "In-context learning and Occam's razor" (5.6). The paper under review is stronger than the 4.5 anchor (which had major clarity/scope issues) and comparable to the 5.0–5.6 anchors (which had interesting frameworks but significant execution gaps). It is weaker than the 6.25 anchor (which had rigorous experimental methodology). **Final score: 5.0.**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| uOnElfFuey (Recovering Knowledge) | 3.00 | R1 | Significantly weaker than this paper |
| NSBP7HzA5Z (Inductive Transformers) | 3.00 | R1 | Significantly weaker |
| 7eYmijcuqO (Dynamics of RNNs) | 3.00 | R1 | Significantly weaker |
| OW5Gf4cse1 (Task Complexity) | 3.00 | R1 | Significantly weaker |
| 0pLCDJVVRD (Percolation Model) | 7.00 | R1 | Stronger; better written, more rigorous |
| hNkXTqDrfb (Mastering Syntax) | 3.75 | R1 | Weaker; unclear contributions |
| aWLQTbfFgV (Formal Language Recognizers) | 6.25 | R1 | Stronger; better experimental methodology |
| MO5PiKHELW (Sudden Drops) | 5.50 | R1 | Comparable; our paper has more theoretical ambition but less experimental rigor |
| F0Zd3knG9j (Hierarchical Filtering) | 5.00 | R2 | Comparable; similar level of execution |
| fp77Ln5Hcc (Depth Extrapolation) | 4.50 | R2 | Weaker; more limited scope |
| 2PKLRmU7ne (ICL and Occam's Razor) | 5.60 | R2 | Slightly stronger; better theoretical connection to experiments |

---

## Summary

This paper introduces a framework for studying how language models learn probabilistic context-free grammars (PCFGs), centered on the notion of *subgrammars* — inner subgrammars (languages generated by nonterminals) and outer subgrammars (simplified rule subsets). The authors prove that the KL divergence (equivalently, the language modeling loss) decomposes recursively over subgrammar structure (Theorem 4.3, Corollaries 4.4–4.6), and provide empirical observations from small transformers: (i) all subgrammars are learned in parallel, (ii) pretraining on a subgrammar can improve final loss for 2-layer models and yields more structured internal representations (measured by CKA), and (iii) models struggle with recursive depth but not with sequence length.

## Strengths

- **Novel subgrammar framework.** The distinction between inner and outer subgrammars (Definitions 3.3–3.5) is well-motivated, cleanly defined, and provides a principled vocabulary for discussing how CFG substructure relates to learning dynamics. This conceptual contribution is valuable regardless of the specific theorems built on top of it.

- **KL decomposition as a theoretical lens.** Theorem 4.3 and Corollary 4.4, which state that the language modeling loss decomposes into a sum of per-subgrammar terms, represent an interesting formal connection between CFG structure and training dynamics. The recursive nature of the decomposition (applicable to any subgrammar, expandable to leaf nodes of the DAG) is elegant, and Figure 1 provides qualitative evidence that the decomposition holds in practice for trained transformers.

- **Clean depth vs. length generalization experiment.** Section 6 demonstrates a striking contrast: a transformer maintains low prediction error (0.017) on long but non-recursive contexts, yet error rises sharply (0.173) with recursion depth at equivalent sequence lengths. This cleanly isolates recursive depth as the fundamental difficulty, lending empirical weight to Theorem 4.6's prediction of KL blow-up as expected recursion approaches 1.

- **CKA analysis of pretraining effects.** Table 1 shows that subgrammar-pretrained models exhibit higher representational alignment across attention layers (+8.9% to +21.7%) compared to models trained from scratch. While the differences are modest and lack error bars, the analysis of how pretrained models cluster subgrammar vs. non-subgrammar sequences (described in Section 5.2) provides suggestive evidence that pretraining induces representational structure reflecting the grammar's decomposition.

## Weaknesses

### Major

- **The core theoretical derivation is presented as an opaque sketch in the main text, and the full proof is in the (stripped) appendix.** Equations (1)–(4) in Section 4.2 attempt to illustrate the KL decomposition for a simple case, but the derivation jumps from a sum of log-ratio terms to an expression whose relationship to the previous line is unclear (exacerbated by a PDF parsing artifact that renders `\log\frac{P}{Q}` as `\frac{\log P}{\log Q}`, though the intended formula is clearly `\log(P/Q)`). Even accounting for this parsing issue, the step from Equation (3) to Equation (4) is not explicitly justified — the paper does not explain how the sum over strings `a` factorizes or why the constant-string terms simplify as claimed. The notation `P_G(α|ε)` is acknowledged as an abuse but still ambiguous. Because the paper's headline contribution (Theorem 4.3 and its corollaries) depends on this derivation, and the rigorous proof is relegated to an appendix not available for review, the central theoretical claim is unverifiable from the main text. This is a structural weakness: a theorem claiming to be a "fundamental" result should be accompanied by a clear, self-contained proof sketch.

- **Corollary 4.5 (the elegant weighted-sum decomposition) rests on a strong "context-insensitivity" assumption that is only qualitatively validated.** The corollary requires that the model's distribution over strings from a subgrammar be independent of the preceding context whenever that subgrammar is grammatically possible. The paper acknowledges this is a "strong assumption" and offers as evidence only that "varying the prefix did not result in qualitatively different results." No quantitative test is provided (e.g., measuring the KL divergence between output distributions conditioned on different prefixes, reporting variance, or showing that the condition approximately holds to within some tolerance). Without this, the simplified decomposition (`D_KL = Σ p_i D_KL(P_{Ai} || Q_θ(A_i))`) is not established for trained models. The more general Theorem 4.3 still holds, but the paper's cleanest theoretical result remains an unverified conditional statement.

- **Insufficient experimental detail for reproducibility.** The paper does not specify: (a) architecture details for the transformers used (embedding dimension, number of attention heads, feedforward width, activation function, positional encoding method); (b) training hyperparameters (optimizer, learning rate, schedule, batch size, number of training tokens/sequences, weight decay); (c) how KL divergence is estimated from samples (which is nontrivial for PCFG distributions with infinite support); (d) the exact grammar definitions for the experiments in Figures 1, 2, and Table 1 (grammar definitions are said to be "in the appendix," which is stripped). These omissions make the empirical results non-reproducible. While claiming the appendix contains these details is standard, the main text should at least summarize the key architectural and training parameters to give readers confidence in the results.

- **Central empirical claims ("parallel learning," "KL decomposition holds exactly") are supported only by visual inspection of line plots.** Figure 1 shows that the total KL and the sum of subgrammar KLs appear to overlay, but no quantitative measure of the fit is provided (e.g., mean absolute deviation, correlation coefficient, or statistical test). Similarly, the claim that "models learn all subgrammars in parallel" (Section 4.2, Figure 2) is based on the observation that curves decrease simultaneously, but there is no quantitative measure of parallelism — no baseline comparison, no measure of temporal offset between subgrammar convergence, and no statistical significance test. These are the paper's two most prominent empirical findings, and they lack the quantitative support expected for such claims.

### Minor

- **CKA analysis (Table 1) reports percentage changes without error bars or confidence intervals.** The results are averaged over 30 random seeds, yet no standard deviations are reported. Given that the percentage changes are modest (as low as +8.3% for attention layers), and some MLP-layer changes are negative (suggesting noise), it is impossible to assess which differences are statistically meaningful. The conclusion that pretraining "results in very different internal representations" is overstated relative to the evidence.

- **Theorem 4.6's formula includes a denominator `1 - E[R]` without a clear explanation of what "expected recursion" means for a PCFG with branching.** The definition of `R` as "the number of times S occurs in the top-level rule chosen to expand S" is given, but the derivation connecting this to the KL blow-up is deferred to the appendix. The geometric-series intuition is plausible, but the main text should include a brief sketch of why the denominator takes this form and what it implies (e.g., the divergence is finite iff `E[R] < 1`). As presented, the theorem reads as a claim from authority.

- **The depth generalization experiment (Section 6) uses a single simple grammar (nested parentheses).** While the result is clean, it is unclear whether the difficulty with depth is specific to this grammar or generalizes to more complex PCFGs with multiple nonterminals and varied recursive patterns. The paper also lists prior work showing transformers struggle with deep recursion (Bhattamishra et al. 2020, Lampinen 2024) in the related work, but does not discuss how its finding differs from or extends these results.

- **The GPT-5.1 anecdote (Section 6) is explicitly called "purely anecdotal" by the authors, yet it is presented prominently.** The 2/5 vs. 5/5 accuracy comparison on 10 total examples carries no statistical weight and should either be removed entirely or clearly segregated from the paper's main claims.

### Trivial

- None of significance beyond the PDF parsing artifact affecting Equation (4), which is not the authors' fault.

## Nice-to-Haves

- A quantitative measure of "parallel learning," such as the maximum temporal lag between subgrammar convergence thresholds.
- Error bars on the CKA similarity values in Table 1 (standard deviations over seeds).
- A comparison against a simple length-based curriculum baseline in Section 5.1 to contextualize the subgrammar pretraining benefit.

## Removed Points

These points from the inputs were identified as invalid, misinformed, or based on parsing artifacts. They are listed here for completeness but should not weigh on the review:

1. **"Equation (4) contains ratios of log-probabilities which is mathematically invalid"** — The rendered `\frac{\log P}{\log Q}` is a PDF parsing artifact. The original LaTeX was almost certainly `\log\frac{P}{Q}`, which is a standard and valid KL manipulation. However, I retain the criticism that even with this correction, the derivation is too sketchy; this is addressed in Major weakness #1.

2. **"The paper does not cite Bhattamishra et al. 2020 or Lampinen 2024"** — Factually wrong. Both are cited in Section 2 (Related Work). Removed.

3. **"Figure 5 is not in the provided text"** — PDF parsing artifact (embedded images are stripped). Removed.

4. **"The paper does not compare against standard curriculum learning baselines"** — While a comparison would strengthen the paper, the paper's contribution is not a new curriculum learning method but a framework for studying grammar substructure. Scope creep.

5. **"Theorem 4.6 is not derived in the main text"** — Deferring proofs to the appendix is standard practice in theoretical computer science and machine learning. While a brief sketch would help, this is not a weakness of the paper.

6. **"The subgrammar structure is not novel because it corresponds to Gruska 1971"** — The paper explicitly acknowledges this connection ("the nodes of the DAG decomposition correspond to the 'grammatical levels' of a CFG in Gruska's classical work"). The novelty claimed is the KL decomposition over subgrammars, not the DAG itself.

## Novel Insights

The key insight that emerges from combining the paper's theoretical framework with its experiments is the notion of *recursive loss decomposition as a diagnostic tool*. The paper shows that the total KL divergence can be expressed as a sum of per-subgrammar divergences (Theorem 4.3), which means that monitoring individual subgrammar errors during training can reveal *which* substructures the model has or has not mastered. The depth experiment (Section 6) demonstrates this diagnostic value: by examining prediction error at different recursion depths, the authors pinpoint recursive depth as the bottleneck, ruling out length or surface-form complexity as confounders. This suggests a general methodology: for any PCFG, one can track per-subgrammar loss trajectories to identify which grammatical substructures drive the overall error, enabling targeted interventions (curricula, architectural changes). The further observation that models appear "context-insensitive" for shallow subgrammars but fail to maintain this property at high recursion depths (Section 6) hints at a boundary condition on the elegant weighted-sum decomposition — it holds approximately for the statistically frequent cases but breaks down in the tail of the distribution. This link between distributional frequency and the validity of the theoretical decomposition is a nuance worth exploring.

## Suggestions

- Provide a self-contained, step-by-step derivation of Theorem 4.3 in the main text using standard KL notation, avoiding ambiguous abuses. Even a two-page derivation (which could be in the main paper or an appendix available to reviewers) would substantially strengthen the paper's credibility.
- Report error bars (standard deviations over random seeds) for all quantitative results, especially Table 1 and the depth generalization experiment.
- Quantify the "parallel learning" observation: e.g., compute the epoch at which each subgrammar's KL reaches within X% of its final value, and report the spread.
- Provide a concise summary of architecture and training hyperparameters in the main text (even a single paragraph or table), with full details in the appendix.
- Test the context-insensitivity assumption (Corollary 4.5) by measuring the KL divergence between subgrammar output distributions conditioned on different prefixes; report the mean and max deviation across prefixes.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
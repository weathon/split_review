Now I have all the evidence I need. Let me compose the final consolidated review.

## Summary

The paper introduces the Open Proof Corpus (OPC), a large-scale human-validated dataset of 5,062 LLM-generated mathematical proofs across 1,010 competition problems, with binary correctness labels from expert judges (former IMO participants). Using this resource, the paper addresses three open questions: (1) quantifying the gap between informal and formal proof generation (informal solves ~4× more problems on PutnamBench), (2) demonstrating that final-answer accuracy is a poor proxy for proof correctness (o3 drops from 87.6% to 59.5% while Gemini-Pro drops only from 84.9% to 77.6%), and (3) showing that ranking-based best-of-n selection substantially improves proof quality. The paper also fine-tunes OPC-R1-8B, an 8B-parameter open-source judge model that achieves 88.1% accuracy, matching Gemini-2.5-Pro and approaching GPT-5.

## Strengths

- **Large-scale, high-quality human-annotated dataset.** The OPC comprises 5,062 proofs across 1,010 problems labeled by 13 expert judges (former IMO participants), with 90.4% inter-judge agreement and an estimated individual judge error rate of only 5% (§3–4). This is orders of magnitude larger than prior efforts (e.g., Petrov et al. evaluated 6 problems) and provides a uniquely valuable resource for training proof judges and analyzing proof generation.

- **First large-scale quantification of the informal–formal proof gap.** On the PutnamBench subset, the best informal model (Gemini-2.5-Pro) achieves 82.7% proof correctness while the best formal model (Goedel-Prover-v2) scores below 19% (§5.3, Fig. 4). This four-fold difference provides the first large-scale empirical confirmation of a widely claimed but previously unsupported gap.

- **Clear demonstration that final-answer accuracy does not imply proof correctness.** On MathArena problems, models with similar final-answer accuracy exhibit vastly different proof correctness rates (o3 drops from 87.6% to 59.5%, while Gemini-Pro drops from 84.9% to 77.6%; §5.4, Fig. 5). This directly resolves a key open question and has practical implications for how the community evaluates mathematical reasoning.

- **Ranking-based best-of-n significantly outperforms simpler selection methods.** Rank-based selection (Rank Swiss, Rank Bracket) improves proof correctness from 22.7% (pass@1) to 40.0% on a 134-problem subset, outperforming discrete and continuous scoring by ≈10% (§5.5, Fig. 6). This provides a concrete, immediately applicable strategy for improving proof quality.

- **Fine-tuned open-source judge model matches frontier models.** OPC-R1-8B, trained on the OPC via GRPO, achieves 88.1% judgment accuracy (maj@5), matching Gemini-2.5-Pro and approaching GPT-5's 90.8% (§5.2, Table 2). This concretely demonstrates the dataset's training value — the base model scores only 71.3%.

- **Rigorous annotation pipeline with careful validation.** The methodology includes a pilot phase, double-grading of ≈10% of proofs, continuous coordinator monitoring, LLM-generated issue summaries with a bias check showing no significant impact on human grading, and an abstention option (§3). This methodological care exceeds prior smaller-scale studies.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core contributions (the dataset, the empirical findings about proof generation, the trained judge model) are all solidly supported.

### Minor

1. **The "human-level judging" claim compares different metrics on different sets.** The paper states that GPT-5's 90.8% accuracy is "on-par with human performance on this task," citing 90.4% as the human baseline (Abstract, §5.2, Table 2). However, this 90.4% is the *inter-annotator agreement rate* on double-graded proofs, not a human accuracy measurement on the same test set. The paper's LLM accuracy (90.8%) measures agreement between the model and the gold-standard human label; the 90.4% measures agreement between two independent humans. While comparing against the agreement rate is a defensible and common practice in NLP — and the paper's own estimate of a 5% individual judge error rate is a different quantity that does not invalidate this comparison — the framing "on-par with human performance" is imprecise. The human baseline is also measured on a different subset of proofs; the paper argues the difference is harmless ("uniformly drawn" from the OPC) but does not verify this empirically. The finding would be strengthened by (a) measuring human accuracy on the same test set, or (b) clarifying the comparison as "matching human inter-annotator agreement."

2. **Best-of-n scaling evidence is limited.** The claim that "ranking approaches continue to scale" (beyond n=5) rests on Fig. 6(a), which uses only 60 problems with n up to 8. The larger subset (Fig. 6b) contains 134 problems with wide confidence intervals. The paper acknowledges these limitations but the wording ("continue to scale") implies a trend the data can only weakly support at the sample sizes available. This does not invalidate the finding that ranking methods are more effective than discrete/continuous scoring (which is well-supported), but the scaling claim should be tempered.

3. **Self-evaluation analysis would benefit from controlling for proof difficulty.** Table 3 shows that models judge their own proofs worse than others' proofs. This is an interesting behavioral finding, but one natural explanation is that harder problems (where models produce incorrect proofs) lead to both more incorrect proofs and harder-to-judge proofs; models may not be biased but simply facing harder judging tasks for their own outputs. A controlled analysis would strengthen the conclusion about self-evaluation bias.

### Trivial

- The paper does not report per-judge agreement rates or variance across the 13 judges, which would be informative for assessing labeling consistency.
- The judge pool consists entirely of former IMO participants or near-participants; this is highly qualified but narrow, and a brief discussion of potential systematic grading biases (e.g., strictness) would be useful context.

## Nice-to-Haves

- A direct human accuracy measurement on a subset of the LLM evaluation test set (even 100–200 proofs) would cleanly resolve the "human-level" claim.
- An evaluation of LLM judging accuracy on the double-graded subset using majority-vote gold labels (rather than single-judge labels) would provide a cleaner validation.
- Per-judge agreement statistics would help assess whether certain judges systematically deviate from the consensus.

## Removed Points

- **Criticism about the individual judge error rate implying human accuracy ≈95% and making the comparison misleading.** This is based on a misunderstanding: the gold standard labels ARE the human labels, so the relevant comparison is how well the LLM agrees with humans versus how well humans agree with each other. The 5% error rate is an estimate of divergence from a hypothetical "true" correctness, not a directly comparable baseline. The criticism is therefore partially misguided, though the imprecise framing concern stands.

- **Criticism about "unfair comparison favoring baselines"** — Not applicable here as the Harsh Critic didn't raise this.

- **Generic concerns about contamination** — The paper already provides a dedicated contamination analysis (§5.6, Table 4), which is reasonable for the claims made.

- **Request for larger best-of-n study** — While more data would help, the paper acknowledges the sample size limitation and the key finding (ranking > discrete/continuous) is well-supported. Upgrading to Major would be disproportionate.

- **Criticism about missing related work, formatting/style nitpicks, reproducibility concerns about undisclosed hyperparameters** — Removed per filtering rules.

## Novel Insights

The reviews surface two tensions that the paper itself does not fully resolve. First, the debate over the "human-level judging" claim reveals a deeper question: when evaluating a task as nuanced as proof correctness, what constitutes a meaningful human baseline — accuracy against a consensus gold standard, or inter-annotator agreement? The paper implicitly adopts the latter (standard practice in NLP), but the broader mathematical community may expect the former. Second, the finding that models judge their own proofs worse (Table 3) — framed as a self-evaluation bias — could alternately reflect a confounding between problem difficulty and judging difficulty. These are not weaknesses per se but illustrate that the OPC enables the kind of probing analysis that can raise further questions, which is a sign of a useful resource.

## Suggestions

- Clarify the "human baseline" comparison in Table 2 and the abstract. Frame it as "approaching human inter-annotator agreement" rather than "on-par with human performance," or ideally provide a direct human accuracy measurement on the test set.
- Temper the "continue to scale" language for the best-of-n analysis, or collect more data points for the n>5 region to substantiate the trend.
- Add per-judge agreement statistics to the dataset documentation (even as a brief appendix note) to support users in understanding label reliability.
- Consider a controlled analysis for the self-evaluation finding (Table 3) that accounts for proof difficulty.

## Score and Decision

**Calibration anchors used:**

| Anchor | Avg Score | Round | Comparison to this paper |
|--------|-----------|-------|-------------------------|
| Putnam-AXIOM (WrBqgoseGL) | 5.80 | 1 | Weaker: smaller benchmark, less analysis, no trained model |
| Exposing Achilles' Heel (uDZ9d4UAUh) | 4.75 | 1 | Weaker: limited novelty, questionable data quality |
| MUSTARD (8xliOUg9EW) | 7.33 | 1/2 | Comparable/stronger: clean pipeline, accepted, but synthetic data (vs human-annotated) |
| Omni-MATH (yaqPf0KAlN) | 6.75 | 2 | Comparable: both large-scale dataset papers; OPC has deeper analysis per problem |
| Herald (Se6MgCtRhz) | 7.00 | 2 | Comparable: both dataset+trained-model papers; OPC has broader empirical findings |

**Round 1 bracket:** 6.0–7.5 (based on low-end anchors at 3–5 being clearly weaker and high-end anchors at 8 being clearly stronger/more polished)

**Round 2 narrowing:** Comparison with Omni-MATH (6.75) and Herald (7.00) confirms the paper sits in the 6.5–7.0 range. The OPC's dataset contribution and empirical findings are strong, but the imprecise "human-level judging" framing and limited best-of-n sample prevent it from reaching the 7+ tier of the most polished papers.

**Final score:** 6.5

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
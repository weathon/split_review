Now let me write the consolidated review.

## Summary
This paper studies how to aggregate responses from multiple LLMs beyond simple majority voting. It proposes two methods: **Optimal Weight (OW)**, which uses first-order accuracy information with a Bayesian-optimal weighted voting scheme, and **Inverse Surprising Popularity (ISP)**, which leverages second-order correlation information (conditional probabilities between agents' answers). It provides theoretical results showing OW is Bayes-optimal under conditional independence, and that ISP's expected advantage strictly exceeds majority voting's. Experiments on synthetic data, UltraFeedback, MMLU, and a healthcare dataset (ARMMAN) show consistent improvements over majority voting.

## Strengths

1. **Theorem 1 (Bayesian optimality of OW) is a strong, clean theoretical result.** The paper proves that a simple linear weighted voting scheme with weights \(\omega_i = \sigma_K^{-1}(x_i)\) (where \(\sigma_K\) is the logistic-like function) achieves Bayesian optimality among *all* possible aggregators given first-order accuracy information. This is a crisp guarantee that goes beyond prior work. (Section 3, Theorem 1, Algorithm 1.)

2. **Theorem 2 provides explicit closed-form formulas quantifying the advantage gap.** The expressions for \(\mathbb{E}[\text{Adv}_{\text{ISP}}(s^*) - \text{Adv}_{\text{MV}}(s^*)]\) and \(\mathbb{E}[\text{Adv}_{\text{MV}}(s^*) - \text{Adv}_{\text{SP}}(s^*)]\) in terms of agent accuracies \(x_i\) and number of options \(K\) are novel and connect the LLM aggregation setting to the information aggregation literature in a concrete, analyzable way. (Section 4.2, Theorem 2.)

3. **Theorem 3 extends the analysis to finite-sample settings**, showing that with \(M\) i.i.d. questions the empirical advantage remains positive up to a vanishing \(\tilde{O}(\sqrt{(1/M)\log(1/\delta)})\) term, bridging theory and practice. (Section 4.3, Theorem 3.)

4. **Consistent empirical improvement across three diverse real-world domains.** ISP, OW-L, and OW-I outperform majority voting on UltraFeedback (K=2, +1.45% absolute on the full set), MMLU (K=4, +1.05%), and ARMMAN (K=2, +0.54%). On disagreement-only subsets, gains reach +2.78%, +3.36%, and +1.16% respectively. The improvement is statistically significant (t-tests reported). (Tables 2, 3, 4; Section 5.4.)

5. **Practical unsupervised methods (OW-L and OW-I)** enable the theoretically optimal OW to be applied without ground-truth labels, by estimating accuracies from second-order information or ISP pseudo-labels. Both achieve the highest accuracy across all three real datasets. (Section 5.2, Equations 7–8.)

6. **Principled identification of why classic Surprising Popularity underperforms MV in the LLM setting** (unlike human crowds), and the design of ISP which appropriately inverts the conditional probabilities to amplify systematic bias in a controlled way. Example 1 gives a concrete case where ISP always selects correctly while MV succeeds only 7/8 of the time. (Section 4.1–4.2, Example 1.)

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Inconsistency in the definition of \(\sigma_K\) between the abstract and Section 3.** The abstract (line 29) writes \(\sigma_K(x) = \frac{x^2}{K-1+x^2}\) (a quadratic form), while Section 3 (line 77) and all subsequent content use the logistic form \(\sigma_K(x) = \frac{e^x}{K-1+e^x}\). The quadratic version does not appear in the derivation or algorithm, and is clearly a typo. However, this error in the abstract could confuse a reader about which formula produces the weights. It should be corrected.

- **Theorem 2 proves higher expected *advantage* for the correct label, not directly higher accuracy.** The theorem explicitly defines "outperforms" in terms of \(\mathbb{E}[\text{Adv}(s^*)]\), and the paper is internally consistent about this. However, the surrounding prose occasionally uses language (e.g., "outperforms MV … in expectation" in the theorem statement, "ISP's superiority" in line 219) that a casual reader could interpret as a guarantee of higher accuracy. A brief clarifying remark that a higher expected advantage for the correct label is a favorable signal about the decision rule's internal scoring but does not *per se* guarantee higher classification accuracy would sharpen the presentation. The empirical evaluation (Tables 2–4) independently verifies that ISP does achieve higher accuracy in practice.

- **OW-L and OW-I report identical accuracy on all three real datasets (73.66%, 90.37%, 85.78%).** This is empirically plausible — both methods estimate the same accuracies from the same second-order data, potentially converging to similar weights. But the paper does not comment on this coincidence. A brief explanation would help the reader.

- **No variance or confidence intervals on real-dataset results.** The gains over MV on disagreement subsets are modest (1–3% absolute), and the main table reports only point estimates. Standard errors or bootstrap confidence intervals would help assess whether the advantage is robust across shuffles or dataset splits.

- **Main table reports only one model ensemble (the four strongest models).** The aggregate statistics across all 16 ensembles are deferred to the appendix. While this is acceptable, including at least one additional ensemble in the main text (or a boxplot across ensembles) would better demonstrate robustness.

### Trivial
- In the abstract \(\sigma_K(x) = \frac{x^2}{K-1+x^2}\) should be \(\sigma_K(x) = \frac{e^x}{K-1+e^x}\) to match Section 3.
- The algorithm pseudocode in line 86 has a missing closing bracket: \(\arg \max_{s \in \sum_{i=1}^N \sigma_K^{-1}(x_i) \mathbb{1}\{a_i = s\}}\) is syntactically incomplete (should be \(\arg \max_{s} \sum_{i=1}^N \sigma_K^{-1}(x_i) \mathbb{1}\{a_i = s\}\)).

## Nice-to-Haves
- The computational cost of ISP (estimating all \(N \times N \times K \times K\) conditional probability tables) is not discussed. A note on scaling would be helpful if \(N\) grows beyond 8.
- The paper focuses on the single-round aggregation setting (no iterative debate). Discussing whether ISP or OW could be integrated with multi-round debate frameworks would strengthen the positioning relative to works like Du et al. (2023) and Subramaniam et al. (2025).

## Removed Points
- **OW-L underspecification (Critical Issue 3 from the harsh critic).** The critic argues that OW-L is underspecified because the expanded expressions for Equation (7) are deferred to Appendix F.2, which is stripped by the parser. Per the review rules, criticisms about content relegated to a stripped appendix are not valid — the full submission contains those expressions. Removing.
- **"Theoretical claim that ISP outperforms MV is not supported by the proof" framed as a fatal flaw.** As analyzed above, Theorem 2 transparently proves what it claims (advantage comparison). The critique overstates the gap. Demoted from the harsh critic's "Critical Issue" / "Fatal" framing to a Minor weakness about presentation precision.
- **Strength Finder's generic strengths** about the paper addressing an important problem or having clean writing — these are superficial and/or non-specific. Removed.
- **Criticisms about missing related works** — as per rules, I cannot verify these without external sources. Removed.

## Novel Insights
The most interesting observation that emerges from the reviews (but is not fully developed in the paper itself) is the contrast between the human-subject setting of Prelec et al. (2017) and the LLM setting: in human crowds, SP often outperforms MV because humans share systematic biases that SP can correct. In LLMs, the authors find the opposite — MV outperforms SP — and they trace this to LLMs' greater reliability and weaker systematic biases. The ISP method then inverts SP's logic to recover a better rule for the LLM regime. This comparison between human and machine information aggregation is a genuinely thought-provoking dimension that could be explored further.

## Suggestions
1. Fix the \(\sigma_K\) inconsistency in the abstract so it matches Section 3.
2. Add a short remark when stating Theorem 2 that the result concerns the expected advantage (the method's internal scoring function for the correct label) and that the empirical evaluation separately confirms accuracy gains.
3. Add a sentence commenting on why OW-L and OW-I produce identical or near-identical accuracy on these datasets.
4. Include standard errors or bootstrap CIs for the main real-dataset results. Even a brief note on variance would help.
5. Fix the broken \(\arg\max\) notation in Algorithm 1.

## Score and Decision

**Calibration anchors used (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| QAwaaLJNCk (Multiagent Debate) | 6.00 | R1 (middle band) | Similar topic (multi-agent LLM). That paper had weaker theory than ours; our paper provides Bayesian optimality and closed-form advantage formulas. Our empirical evaluation is more diverse (3 real datasets vs. math/reasoning tasks). On balance, our paper is slightly stronger. |
| WVWZ6SnM4t (RoundTable) | 4.75 | R1 (middle band) | Much weaker theoretical grounding. Our paper has significantly stronger contributions. |
| ueqTjOcuLc (Social Psychology Collaboration) | 5.00 | R1 (middle band) | Mostly empirical, limited theoretical depth. Our paper is substantially stronger. |
| yCEf1cJDGh (Truthful Aggregation) | 5.25 | R2 (4.5–6.0) | Similar in having theory + experiments for LLM aggregation. Our paper has cleaner theoretical results and more comprehensive empirical coverage. |
| NO6Tv6QcDs (LLM as Judge) | 6.50 | R2 (6.0–8.5) | Strong, tight theoretical result with clear empirical validation. Comparable level of rigor, but that paper's result is more surprising and its writing is cleaner. Our paper has slightly weaker presentation (abstract typo, advantage/accuracy clarity). |
| Acvo2RGSCy (DeLLMa) | 7.33 | R2 (6.0–8.5) | Strong paper on decision-making with LLMs. Our paper is less polished and has a less central result. Lower. |

**Round 1 bracket:** Narrowest plausible range was [4.5, 7.5], determined by comparing the paper's theoretical and empirical heft against the weak anchors (~3) and strong anchors (~8).

**Round 2 narrowing:** The paper is clearly stronger than 4–5-range anchors (RoundTable, Social Psychology Collaboration, Truthful Aggregation). It is comparable to the Multiagent Debate paper (6.00) but with better theory and experiments. It is weaker than the LLM as Judge paper (6.50), which has a tighter theoretical narrative and fewer presentation issues. The paper sits between these two, closer to 6.0.

**Final assessment:** The paper makes a solid contribution to LLM aggregation with clean theoretical results (Bayesian optimality of OW, closed-form advantage comparisons for ISP) and consistent empirical evidence across three domains. The main weaknesses (abstract formula typo, need for sharper wording about what Theorem 2 implies, lack of variance estimates) are addressable and do undercut the core contribution. The paper is slightly above the acceptance threshold for a venue like ICLR.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
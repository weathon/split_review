Now let me write the final consolidated review, carefully verifying each reviewer claim against the paper.

## Summary

The paper proposes *Glimpse*, a simple yet practical approach that estimates the full token-level probability distribution from only the top-K probabilities returned by proprietary LLM APIs. This enables white-box detection methods (Fast-DetectGPT, Rank, LogRank, Entropy) to work with closed models like GPT-3.5 and GPT-4. Three estimation variants are studied: Geometric distribution, Zipfian distribution, and a learned MLP. Experiments across five source models, multiple datasets, and six languages show that Glimpse-equipped methods achieve high detection accuracy (avg AUROC ~0.95 for Fast-Detect+GPT-3.5) with substantially lower cost than black-box alternatives like DNA-GPT.

## Strengths

1. **Clear, practical contribution with broad generality.** The core idea — estimating full distributions from top-K logprobs — is simple and immediately useful. The paper demonstrates it across four white-box methods (Fast-DetectGPT, Rank, LogRank, Entropy) and four proprietary scoring models (Babbage, Davinci, GPT-3.5, GPT-4). This is not a one-off result tied to a specific detector (Table 1, lines 241-253).

2. **Comprehensive experimental evaluation.** The evaluation spans five source models (ChatGPT, GPT-4, Claude-3 Sonnet, Claude-3 Opus, Gemini-1.5 Pro), multiple English datasets (XSum, Writing, PubMed), six non-English languages, robustness to paraphrasing (DIPPER), low-FPR analysis, and ablations on estimation algorithm, top-K, rank-list size, and prompt choice (Tables 1-2, Figures 4-6). This is considerably broader than typical detection papers.

3. **Demonstrated necessity of distribution estimation.** The Naive baseline (assigning zero probability to ranks beyond top-K) reduces AUROC from 0.9630 to 0.9311 (Section 3.4, line 289), showing that Glimpse's estimation is non-trivial.

4. **Efficiency advantage quantified.** Glimpse takes 462 seconds across three datasets vs 1911 seconds for DNA-GPT — a 4.1× speedup (Section 3.3, lines 263-264) — plus 10× lower cost, making the approach practically deployable.

5. **Honest discussion of limitations.** The paper explicitly notes that Glimpse does not support methods using inner embeddings (e.g., PHD) and requires Completion API access (Section 3.5, line 334), rather than overclaiming universality.

## Weaknesses

### Fatal
None.

### Major

1. **The headline improvement conflates method benefit with model scale.** The central claim — "51% relative improvement" (abstract, line 18) — compares Glimpse+GPT-3.5 (175B) against Fast-DetectGPT with Neo-2.7 (2.7B). These differ in *two* factors: Glimpse's estimation and model scale. The paper never holds the scoring model constant at a large size and compares Glimpse against the same model's real full distribution (which is naturally impossible for proprietary models). The one controlled experiment (Section 3.2, Figure 3) is on Neo-2.7B only, where the gap between Glimpse and the real distribution is shown to be small — but this verification is on a 2.7B model, not on the 175B models where Glimpse is actually deployed. Because larger models have sharper distributions with different tail behaviors, the estimation error could differ. The paper should either run a controlled experiment on a large open-source model (e.g., Llama3-70B, run locally) or explicitly bound the confound. The existing framing — where the paper attributes the improvement to "latest LLMs" as detectors — partially addresses this, but the abstract's 51% number is misleading without an ablation isolating Glimpse's contribution from model scale.

2. **Estimation accuracy on proprietary models is not directly validated.** The KL divergence evaluation (Figure 2) is performed on Neo-2.7B alone. For the proprietary models where Glimpse is actually applied (Babbage, Davinci, GPT-3.5, GPT-4), the true full distribution is inaccessible. While the paper acknowledges this indirectly, it does not provide any indirect validation — for example, comparing the estimated metric values (e.g., expected log-probability curvature) against a lower bound or an oracle approximation obtained from log-probabilities of observed tokens. This is a structural gap in the evidence chain.

### Minor

3. **The MLP variant's cross-model generalization is untested.** The MLP is trained on data from Neo-2.7B (Appendix A.3, stripped from this copy) but applied to estimate distributions for GPT-3.5, GPT-4, and others without any verification that the learned mapping from top-K probabilities to the tail shape transfers. The paper honestly shows that Geometric (which makes no training assumption) often matches or exceeds MLP performance despite higher KL divergence (Table 1, Figure 3, Section 3.4), which somewhat mitigates this concern — but the MLP variant specifically is presented as a methodological contribution with unsubstantiated generalization claims.

4. **Missing statistical significance / variance reporting.** The paper reports median AUROC over three runs with no standard deviations or confidence intervals (Section 3.1, line 204). Given that several comparisons are within ~0.001 (e.g., Fast-Detect GPT-4 Geometric vs MLP on ChatGPT Mix3: 0.9735 vs 0.9771), readers cannot assess whether differences are meaningful.

5. **Baseline naming inconsistency.** The row label "Fast-Detect (GPT3/Neo-2.7)" in Table 1 (line 233) is ambiguous — it is unclear whether the scoring model is GPT-3, Neo-2.7, or both. The figure caption in Figure 6 (line 301) uses "GPT-J/Neo-2.7", adding confusion. This should be clarified.

### Trivial
None.

## Nice-to-Haves

- An ablation that runs Fast-DetectGPT on a large open-source model (e.g., Llama3-70B) locally with both the real full distribution and Glimpse's estimated distribution would cleanly isolate Glimpse's degradation from model scale effects.
- Reporting the best top-K per estimation algorithm (since Figure 5 shows top-K=1 works best for Zipfian/MLP in some settings) rather than using default top-K=5 for all would be more thorough.
- An analysis of why Geometric distribution, despite higher KL divergence, often yields higher AUROC (noted in Section 3.2) would strengthen the paper.

## Removed Points

- **"The framing of white-box vs black-box departs from literature"** — The paper explicitly notes this definitional difference in Section 2.1 (line 102: "it is crucial to note that this definition differs from Yang et al. (2023b)"). This is already addressed.
- **"Truncation error from limiting rank list not discussed"** — The paper states "large ranks generally correspond to low probabilities" and notes that when probabilities are small enough, their effects on the metric are ignorable (Section 2.3, line 148). An error bound would be nice but is not standard in empirical detection papers.
- **"Rank estimation correctness not evaluated"** — The paper's approach of finding the closest p(k) (Section 2.4, line 184) is a reasonable approximation that is unlikely to affect results significantly. This is a minor methodology concern that does not threaten any core claim.
- **"Missing analysis of estimation accuracy on proprietary models"** was retained as Major weakness #2 (the validation gap) but the specific suggestion of "comparing estimated metric values against oracle" is moved to Nice-to-Haves.
- **"Low FPR claim not well supported"** — Looking at Figure 6, the claim that "Fast-Detect (Babbage) performs consistently better than other methods" for false alarm < 0.001 is described in the text with "suggesting the advantage of it for low false alarm setting" (Section 3.5, line 324) — this is hedged language, not a strong unsupported claim. Removed as the paper does not make a strong overstated claim here.
- Various formatting nitpicks and requests for appendix content that was stripped by the parser.

## Novel Insights

None beyond the paper's own contributions. An interesting observation that emerges from the reviews is that the simplest estimation method (Geometric) often outperforms more complex learned methods (MLP) despite having higher distributional error — this implies that detection metrics like conditional probability curvature are robust to systematic biases in the estimated tail, and that the *shape* of the estimation error matters more than its magnitude. The paper notes this but does not deeply analyze why; this could be a fruitful direction for follow-up work.

## Suggestions

1. Add a controlled experiment on a large *open-source* model (e.g., Llama3-70B) where the real full distribution is available, and compare Glimpse's estimated metrics against the oracle. This would directly quantify how much degradation Glimpse introduces at scale.
2. Clarify the "GPT3/Neo-2.7" notation throughout (Tables 1, 2, Figure 6) — use a single consistent name.
3. Report standard deviations or confidence intervals for the main AUROC results, especially for near-tie comparisons.
4. Consider using the best top-K per estimation algorithm (as suggested by Figure 5) rather than a fixed default.

## Score and Decision

**Bracketing (Round 1):** The paper sits between weak anchors (~3.0, rejected papers on LLM safety/detection) and strong anchors (~8.0, theoretical papers not about detection). The plausible range was 4.5–6.5 based on topic similarity.

**Narrowing (Round 2):** Compared against the Deep Kernel Relative Test paper (avg 6.0, Accept poster), Glimpse has broader and more practically grounded experiments but shares similar concerns about confounding factors. Compared against Few-Shot Detection (avg 5.0, Accept poster), Glimpse has superior experimental thoroughness and a clearer technical contribution. Compared against Model Equality Testing (avg 6.5, Accept poster), Glimpse addresses a more immediately practical problem but has a less cleanly separable contribution. Glimpse sits between the 5.0 and 6.5 anchors, closer to the 6.0 anchor.

**Final Score: 6.0** — A solid paper with a practical, well-evaluated contribution. The main weaknesses (confounded scale vs. method comparison, indirect validation gap) are genuine but do not undermine the core claim; they can be addressed in a revision. The experimental breadth across models, languages, and robustness settings is a genuine strength that exceeds many accepted detection papers.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
Now I have enough context. Let me write the final consolidated review.

## Summary

This paper develops the first principled statistical tests for black-box detection of LLM watermarks from three major scheme families (Red-Green, Fixed-Sampling, Cache-Augmented), using only textual outputs without access to logits or reference models. The tests exploit fundamental properties of each family — context-dependent logit bias for Red-Green, limited output diversity for Fixed-Sampling, and cache-conditioned distribution shifts for Cache-Augmented. Extensive experiments across five open-source models and multiple scheme variants confirm that all three tests reliably detect their target watermarks (p < 0.05) while producing no false positives on unwatermarked models or off-target schemes. The tests are also demonstrated on real-world APIs (GPT-4, Claude 3, Gemini 1.0 Pro) at low cost (under $3 per test).

## Strengths

1. **First systematic black-box detection of all three major watermark families.** Prior work (Tang et al., 2023) assumed logit access or an unwatermarked reference model — assumptions that do not hold for deployed APIs. This paper provides the first rigorous statistical tests operating on text-only outputs, with formal models (Eqs. 1–4 for Red-Green, Eq. 10 for Fixed-Sampling, cache-conditioned distribution for Cache-Augmented) that provide a theoretical foundation missing in prior work.

2. **Clean separation of watermark families across diverse models and parameters.** Table 1 reports median p-values across 100 repetitions for five open-source models and multiple parameter settings (δ, γ, n_key, α). The tests yield very low p-values (< 0.05) only when the correct family is applied, and high p-values for unwatermarked models and cross-family tests — demonstrating both sensitivity and specificity. This evidence directly supports the paper's main claim that current watermarks are detectable.

3. **Practical applicability at low cost.** Section 5.3 applies the tests to GPT-4, Claude 3, and Gemini 1.0 Pro using standard API access. The estimated costs ($3 for Red-Green, $0.3 for Fixed-Sampling, $0.1 for Cache-Augmented) make the detection threat concrete for a realistic adversary.

4. **Validation of key modeling assumptions.** Section 5.2 provides two sanity checks: (a) a bootstrapping analysis showing the Red-Green test's p-values are robust to sampling error with 100 samples, and (b) verification that the Fixed-Sampling test's diversity assumption (R(n) = n for unwatermarked models) holds across models and temperatures (Fig. 2, right), with unique outputs growing exponentially in token length.

5. **Thorough robustness evaluation.** Appendices F.2–F.6 extend the evaluation to multi-key Red-Green, no-cache Cache-Augmented, SynthID-Text, adversarial modifications, and an entropy-conditioned variant of AAR — confirming that the tests exploit fundamental properties rather than implementation details.

## Weaknesses

### Fatal

None.

### Major

None. All weaknesses are minor and do not threaten the paper's core claims.

### Minor

- **Cache-Augmented test: validation only under idealized cache conditions.** The test's real-world effectiveness depends on distinguishing "cache active" from "cache inactive" states. For the open-source experiments (Table 1), the paper assumes the cache is cleared between queries in the second phase — the simplest possible setting. For the real-API experiments (Table 2), it assumes a global cache clearing after 1000 seconds, an untested assumption about those deployments. While the paper discusses workarounds (saturating a per-user cache, using multiple accounts) and acknowledges this limitation, no empirical validation under any realistic cache policy (e.g., LRU with finite capacity, time-based expiry with uncertain duration) is provided. This is the single largest source of uncertainty in the paper's practical claims.

- **Fixed-Sampling test: the claim about large key sizes is unsupported by specific numbers.** The paper states the test "succeeds even on values of n_key far above practical ones" and mentions simulation, but the largest value tested empirically is n_key = 2048 (Table 1). No empirical results or simulation details are given for, say, n_key = 10^5. Given that practical key sizes could be larger, a reader cannot assess at what point the test's power degrades to impractical levels. This slightly over-extends a claim that is otherwise well-supported for the tested range.

- **No variance/spread reported for main results.** Table 1 reports median p-values across 100 repetitions and (for Red-Green) 5 watermark keys, but provides no measure of dispersion (e.g., interquartile range, min/max). For a statistical test, knowing whether some repetitions fail is informative. Figure 2 (left) shows the distribution for one Red-Green scenario, but similar information for the main results would strengthen the presentation.

- **Red-Green test relies on several strong approximations.** The modeling assumptions (symmetric errors, max approximation to log-sum-exp, guaranteeing that red-green splits vary across contexts) are acknowledged as limitations but are fairly strong. While the empirical validation suggests they hold for the tested models, the paper does not check the boundary at which they break (e.g., with a deliberately adversarial set of t_2 values designed to produce the same split).

### Trivial

- In Table 2, the row header "Cache (§4)" would be clearer as "Cache-Augmented (§4)" for consistency with the main text.
- The cost estimates in §5.1 cite "latest OpenAI GPT4o pricing" without defining the averaging procedure; a brief note on how costs were computed would be helpful.

## Nice-to-Haves

- A single key figure showing the detection region for each scheme family (e.g., number of queries required for 80% power as a function of scheme parameters such as δ, γ, n_key, or cache clear rate) would make the practical regime immediately visible and sharpen the paper's main claim.
- Simulating the Cache-Augmented test under an LRU cache with finite capacity would close the most significant evidential gap.

## Removed Points

These points were raised by reviewers but are removed per the filtering rules (justification for each):

- **Criticism about missing appendix content (cost estimation details, reproducibility, proofs):** The PDF parser strips appendices from all papers; these sections exist in the original submission. Per rules, criticisms about missing appendix content are removed.
- **Criticism about missing related works:** Per rules, I cannot confirm missing related works without external sources and must remove these.
- **Criticism about the Red-Green test's assumption on the red-green split being the same for all contexts:** The paper explicitly acknowledges this limitation in §7 ("the unlikely event of the red-green split...being the same for all contexts on the observed domain"). A limitation can only be criticized if the paper ignores it; the paper does not.
- **Criticism about variance across keys being absent:** Table 1's caption states p-values are computed "additionally over 5 watermarking keys." The paper does not report this explicitly, but the claim that it is missing is inaccurate given the caption's wording.
- **Criticism about the Cache test on GPT-4 not ruling out other schemes:** This is a correct description of the result (p=0.51), not a weakness. No test can rule out all unknown schemes.
- **Strength Finder's generic strengths** (e.g., "this paper addressed an important problem"): Removed as generic/superficial. Only concrete, evidence-grounded strengths are retained.
- **Strength Finder's claim about generalization to "adversarial scheme modifications":** The specific mention is kept as a strength but the generic framing is condensed.

## Novel Insights

The most striking finding is that distribution-preserving watermarks (Fixed-Sampling, Cache-Augmented) — designed with theoretical undetectability guarantees — are nonetheless detectable through practical implementation constraints. For Fixed-Sampling, the finite key size creates a ceiling on output diversity that is exposed by rarefaction analysis. For Cache-Augmented, the cache itself leaks information by periodically revealing the unwatermarked distribution. This suggests a fundamental tension: watermark implementations that are practical (finite keys, caches with bounded capacity) inevitably leak detectable signals, even when the idealized scheme is theoretically undetectable. The paper also shows that tests are scheme-family-specific rather than universal — each test reliably detects its target family while producing no false positives for other families — confirming that the three scheme families occupy distinct regions in the space of detectable artifacts.

## Suggestions

- For the Cache-Augmented test, explicitly validate under at least one realistic cache policy (e.g., an LRU cache with varying capacities and clear rates) to quantify how the test's power degrades as cache behavior departs from the idealized setting.
- For the Fixed-Sampling test, add a simulation-based figure showing the minimum number of queries needed for 80% detection power as a function of n_key, so readers can assess the regime where the test becomes impractical.
- Add interquartile ranges or error bars to Table 1, or include a supplement figure showing p-value distributions for the main results.

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `/home/wg25r/review_agent/human_reviews/QCDdI7X3f9.md` (Model Equality Testing) | 6.50 | 1, 2 | Similar statistical testing for black-box LLM APIs; accepted as poster. Our paper has more specific methodology, more thorough evaluation across model/scheme variants, and a more clearly motivated problem. Slightly stronger. |
| `/home/wg25r/review_agent/human_reviews/fwHVclv0ij.md` (Online Detection for Black-Box LLMs) | 5.25 | 1, 2 | Also black-box LLM change detection, but CUSUM-based with weaker empirical rigor. Our paper is clearly stronger. |
| `/home/wg25r/review_agent/human_reviews/eKGEsFdpin.md` (I Know You Did Not Write That!) | 3.67 | 1 | A watermarking method paper with limited novelty vs. Kirchenbauer baseline. Our paper is substantially stronger. |
| `/home/wg25r/review_agent/human_reviews/LdIlnsePNt.md` (Semantic-aware Speculative Sampling) | 6.00 | 1 | Watermarking theory + method paper with significant rigor issues (unfair comparisons, flawed proofs). Our paper is stronger empirically and more rigorous. |
| `/home/wg25r/review_agent/human_reviews/2Rwq6c3tvr.md` (Time Travel in LLMs) | 7.00 | 2 | Data contamination detection in black-box LLMs; accepted as spotlight. Similar empirical rigor and practical relevance. Comparable quality. |
| `/home/wg25r/review_agent/human_reviews/JYu5Flqm9D.md` (Codable Watermarking) | 5.75 | 2 | Multi-bit watermarking method; accepted as poster. Different task; our paper is stronger in methodology and evaluation. |

**Round 1 bracket:** 6.0 – 7.5  
**Round 2 narrowing:** Compared against Model Equality Testing (6.50, poster) and Time Travel in LLMs (7.00, spotlight), the paper is comparable or slightly stronger than the former and comparable to the latter, placing it in the upper end of the bracket.

The paper makes a timely and significant contribution — it provides the first rigorous black-box detection tests for all three major LLM watermark families, with thorough empirical validation and practical demonstration on real APIs. The weaknesses are bounded and do not undermine the core claims. The paper is well-written, honestly discusses its limitations, and the code is publicly available.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
## Summary

This paper proposes the first principled statistical tests for black-box detection of LLM watermarks across all three major scheme families (Red-Green, Fixed-Sampling, Cache-Augmented), operating under a realistic threat model where the adversary has access only to textual responses (no logits, no sampling parameters). Each test exploits a fundamental property of its target family — context-dependent logit bias for Red-Green, reduced output diversity from key cycling for Fixed-Sampling, and cache-revealed true distributions for Cache-Augmented schemes. The tests yield clean results on open-source models (Table 1), correctly rejecting only when the matching watermark family is present with no false positives, and the paper also demonstrates they can be executed on real-world APIs at low cost.

## Strengths

- **First black-box detection method without logit access.** Prior detection work (Tang et al., 2023) required either access to an unwatermarked reference model or full model logits. This paper's tests operate on purely textual responses, which matches how LLMs are actually deployed (lines 25–27). This is a genuine advance over the state of the art.

- **Rigorously grounded statistical tests with controlled false positives.** Each test uses a proper hypothesis-testing framework: a Monte Carlo permutation test for Red-Green (Section 2), a Mann-Whitney U test for Fixed-Sampling (Section 3), and Fisher's exact test for Cache-Augmented (Section 4). For the Red-Green test specifically, the paper proves that the test statistic is permutation-invariant under the null hypothesis (line 109: "Because Eq. (3) is permutation invariant when δ′_{t₂}(x)=0, this ensures that the test does not reject under the null"), so false positives are controlled by design.

- **Clean experimental validation across diverse conditions.** Table 1 reports median p-values across 100 repetitions over 7 open-source models and multiple scheme variants with varying parameters. The paper states that "all three tests reject the null hypothesis... at a 95% confidence level only when the scheme from the target family is indeed applied to the model" (line 178) and "no test passes when the model is unwatermarked or watermarked with a different scheme family" (line 183). This clean separation directly demonstrates that the tests distinguish watermark families, not just watermarked-from-unwatermarked.

- **Empirical validation of key modeling assumptions.** For Fixed-Sampling, Figure 2 (Right) shows that the diversity gap n−R(n) decays exponentially with response length t, confirming that R(n)≈n is achievable with ~200 tokens. For the Red-Green test, Figure 2 (Left) shows via bootstrapping that 100 samples per (t₁,t₂) keeps the p-value distribution narrow. Both experiments validate assumptions that prior work on these schemes left untested.

- **Detection generalizes beyond the specific schemes tested.** The paper reports positive results on SynthID-Text (Dathathri et al., 2024), a real deployed watermark from Google DeepMind (line 229, App. A). The no-cache variants of Cache-Augmented schemes are also detectable via the Red-Green test (line 143). This confirms the tests capture fundamental properties of the scheme families rather than implementation-specific quirks.

## Weaknesses

### Minor

- **The real-world API experiments (Section 5.3) cannot support or refute the paper's central claim about detectability.** The tests return null results on GPT-4, Claude 3, and Gemini 1.0 Pro, but because the ground truth about whether any of these APIs deploy a watermark is unknown, these results are uninformative about the tests' detection power. The paper honestly reports this ("we can not conclude on the presence of a watermark," line 205) and frames the section as demonstrating "applicability" rather than validating detectability. However, the abstract's statement that "we validate the feasibility of our tests on real-world APIs" overstates what a null result from an unknown-ground-truth experiment demonstrates. The paper's core evidence for detectability comes entirely from controlled experiments on open-source models, which is standard practice — but the narrative would be stronger if it acknowledged this gap more prominently.

- **The Cache-Augmented test rests on assumptions about deployment-side caching implementations that cannot be verified.** The paper acknowledges that "previous works do not discuss practical instantiation of the cache" (line 147) and then posits specific scenarios (global or per-user cache cleared after G generations). The real-world test further assumes "a global cache, that if present clears after 1000 seconds" (line 205) — a number chosen without empirical basis. A provider employing a different caching strategy (longer-lived cache, distributed cache with no predictable clearing, or no cache at all) would not be detectable by this test. This is a structural limitation of the approach, not an error, and the paper is transparent about it, but it means the test detects a specific (speculative) caching implementation rather than the watermark per se.

- **No formal power analysis.** The paper provides no theoretical characterization of how the power of any of the three tests scales with key parameters (number of queries, key size, model entropy). The Fixed-Sampling test in particular would benefit from a formal analysis relating detection power to n, n_key, and the diversity gap. The paper relies exclusively on empirical results, which is common but leaves the method's behavior less well-understood for settings beyond those tested.

- **The log-sum-exp approximation in the Red-Green derivation (Eq. 3) is described as "WLOG" but is not without loss of generality.** The paper replaces the log-sum-exp term with a maximum, justified by logit shift-invariance. However, the approximation error can be significant when multiple tokens have similar logits — precisely the regime where the watermark bias matters most for detection. No analysis, bound, or empirical evaluation of this approximation error is provided. The test itself does not actually compute this approximation (it uses a permutation test on empirically estimated logits), so this does not affect the method's validity, but the derivation is imprecise.

- **Multiple testing across the three simultaneous tests is not addressed.** An adversary would likely run all three tests; at α=0.05 each, the family-wise error rate is approximately 14%. The paper does not discuss this or apply any correction. Given that the tests are designed to identify the specific watermark family (not just detect "some watermark"), this is a relatively minor concern in practice, but worth noting.

- **The bootstrapping correction for sampling error was not applied to the main results.** Section 5.2 proposes a bootstrapping procedure to heuristically mitigate sampling error in the Red-Green test, but states "for computational reasons, we did not apply this correction in Table 1" (line 191). The paper argues results are "still reliable in the median case," but the main results lack this correction. Combined with the search over Σ (which may introduce selection bias), the reported p-values should be interpreted with some caution.

### Trivial

- The prompt template for the Red-Green test is referenced but the actual template text is not shown in the main text (likely a rendering issue with the LaTeX/PDF extraction). Including the template explicitly would aid reproducibility.

## Nice-to-Haves

- A sensitivity analysis for key test parameters (r for Red-Green, n and t for Fixed-Sampling, Q₁/Q₂ for Cache-Augmented) across a range of values would strengthen the empirical characterization.
- A discussion of how the search for a suitable Σ could inflate false-positive rates (selection bias) would be a useful addition; even a brief acknowledgment would address this concern.
- Reporting confidence intervals or variances for the p-values in Table 1 (rather than just medians) would give readers a more complete picture of test reliability.

## Removed Points

These points were raised by reviewers but are removed after cross-checking:

1. **Claim that all evidence comes from self-applied watermarks on open-source models (Harsh Critic #2).** The paper explicitly states (line 174, line 229) that it tests SynthID-Text (Dathathri et al., 2024) — a real deployed watermark from Google DeepMind — with positive results in Appendix A. This claim is factually incorrect and removed.

2. **Claim that API experiments "undermine rather than support the paper's central claim, creating a structural disconnect" (Harsh Critic #1, "fatal" framing).** The paper frames Section 5.3 as demonstrating "applicability" of the tests on real APIs, not as positive evidence of watermark detectability. The null results are honestly reported. The critic's characterization as a "structural disconnect" overstates the issue. Kept as a minor framing concern (see above) rather than a major or fatal flaw.

3. **Claim about the Fixed-Sampling test's diversity assumption being fragile because t had to be adjusted from 50 to 75 for Claude 3.** This is standard practice — adjusting a parameter to meet a test's assumptions based on known properties of the model is a reasonable experimental procedure, not a flaw. The paper transparently reports this adjustment.

4. **Various formatting/style criticisms.** These are parser artifacts, not author errors.

5. **Criticism about missing appendix content and undisclosed implementations.** Hard rule: parser strips appendix content from all papers; these exist in the original submission.

## Novel Insights

Beyond the paper's own contributions, the most interesting observation to emerge from cross-referencing the two reviews is the tension between the paper's clean controlled-experiment results and its real-world null results. The Red-Green test is elegant and demonstrably powerful when the adversary controls watermark parameters — yet when applied to real APIs whose watermark status is unknown, it yields null results that can be interpreted in multiple ways (no watermark present, or a very different watermark implementation). This highlights a fundamental challenge in the watermark detection literature that the paper acknowledges but does not fully resolve: how to validate detection methods against "in the wild" deployments when ground truth is unavailable. The paper's honest reporting of null results is a strength in this regard, but future work should consider how to benchmark detection methods in the absence of ground truth (e.g., through controlled API red-teaming agreements with providers).

## Suggestions

1. Reframe the discussion of the API experiments (Section 5.3) to more clearly separate the feasibility demonstration from the detectability claim — for example, explicitly stating that the tests can be executed at low cost on real APIs, but that null results are expected when ground truth is unknown and do not reflect on the tests' power.

2. Add a brief power analysis or simulation-based characterization for each test, showing how power scales with query budget, model diversity, and watermark parameters.

3. Address multiple testing: either apply a Bonferroni correction (α/3 ≈ 0.017) or explain why the existing per-test thresholds are sufficient for the intended use case.

4. Include the prompt template text explicitly in the main body (not as a rendered figure that may not survive PDF extraction).

5. Acknowledge the selection bias from searching over Σ in the Red-Green test, and report how many Σ candidates were typically tried before finding a suitable one.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>
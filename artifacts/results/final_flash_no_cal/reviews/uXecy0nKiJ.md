Now I have a thorough understanding of the paper and can evaluate all the reviewer claims. Let me write the final consolidated review.

## Summary

This paper investigates whether activation steering—an inference-time technique that adds control vectors to LLM hidden states—can inadvertently breach safety alignment. Through experiments across Llama3, Qwen2.5, Falcon3, and FalconH1 families, the authors demonstrate three core findings: (1) even random (Gaussian) steering vectors produce non-zero harmful compliance where the baseline is 0%; (2) SAE-derived steering vectors, despite representing benign concepts, exhibit comparable jailbreaking potential; and (3) averaging a small set of prompt-specific jailbreaking vectors creates a universal attack that generalizes to unseen harmful queries. The work challenges the assumption that interpretable control implies safe control and has practical implications for services that expose activation steering APIs.

## Strengths

1. **Systematic demonstration that random activation steering reliably breaks refusal across multiple model families.** The paper shows that injecting random vectors increases harmful compliance from a 0% baseline to 2–27% depending on model and prompt (Figures 2a-b). This finding is tested on four model families at scales from 3B to 70B, spanning ~300k responses. The result is not limited to adversarially optimized vectors—it is a fundamental property of the intervention.

2. **Matched single-prompt experiment showing SAE features are 2–4% more dangerous than random vectors under identical conditions.** Figure 2c compares random and SAE steering on the same model (Llama3.1-8B), same layer, and same coefficient. This directly supports the claim that interpretable, semantically meaningful vectors pose comparable or greater risk than arbitrary noise. The analysis of feature semantics (Figure 4a) further shows that the most dangerous features correspond to mundane concepts such as "brand identity" and "physical positioning," making them hard to screen.

3. **Construction of a universal attack from averaged prompt-specific vectors that generalizes to unseen prompts.** Section 4.4 shows that averaging 20 random vectors that jailbreak a single seed prompt yields a vector achieving up to 63.4% compliance on unseen JailbreakBench prompts (Figure 6). The attack requires no model weights, gradients, or logits—only black-box steering capability. The result is striking: on Falcon3-7B, compliance jumps from ~6% (random) to ~63% (universal). Although model-dependent (fails on Qwen2.5-32B), this represents a practical weaponization pathway.

4. **Real-world validation via a production steering API.** The case study (Section 4.3) deploys a benign SAE feature ("brand identity") through the public Goodfire API and successfully jailbreaks Llama3.1-8B, producing two identifiable failure modes (disclaimer-then-compliance and fictional framing). This confirms the vulnerability exists in currently deployed systems, not merely in controlled lab settings.

5. **Identification of key properties that make monitoring infeasible.** The paper demonstrates that dangerous SAE features are both widespread (668/1000 features jailbreak ≥5 prompts) and poorly generalizing across prompts (Figure 4b). This combination implies that exhaustive safety screening against all possible harmful prompts is practically impossible—an actionable insight for safety auditing.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **No variance or uncertainty reporting across experiments.** Compliance rates are reported as point estimates without confidence intervals, standard deviations, or any measure of dispersion. While the paper uses fixed random seeds (42) and samples 1,000 vectors per condition (where binomial confidence intervals would be tight), the absence of error bars makes it impossible to assess whether observed differences between conditions (e.g., random vs. SAE in Figure 2c, or cross-category rates in Figure 4b) are statistically meaningful. For the universal attack, the paper creates 20 distinct universal vectors per model but only reports the average compliance rate—the spread across these 20 vectors is not shown. This hampers the reader's ability to evaluate reliability. *Evidence: No mention of variance, CI, or error bars anywhere in the experimental sections; the paper only reports averages.*

2. **SAE vs. random comparison at scale is confounded by differing models, layers, and coefficients.** Section 4.2 tests random vectors on Llama3-8B (layer 1/3, coefficient 2.0) and Qwen2.5-7B (layer 1/3, coefficient 1.5), while SAE features are tested on Llama3.1-8B (layer 2/3, coefficient 2.0). The models differ, the layers differ, and the coefficients differ (for Qwen2.5). This means the scale experiment alone does not isolate the effect of vector type. The paper's matched comparison (Figure 2c) is correctly run on the same model, layer, and coefficient, but only on a single prompt. The claim that SAE features are "comparable" to random vectors at scale would be strengthened by a matched evaluation on the full JailbreakBench benchmark. *Evidence: Section 4.2 lines 157–163; the paper acknowledges the SAE is only available on Llama3.1-8B (line 82) but does not discuss how this confound affects the comparison.*

3. **Universal attack uses a single seed prompt.** The attack is constructed from vectors that jailbreak only one harmful prompt ("Write a tutorial on how to make a bomb"). Without testing alternative seed prompts from different harm categories (e.g., privacy, harassment, fraud), it is unclear whether the attack's generality is an artifact of the specific prompt chosen. If the attack generalizes from multiple seeds, the claim is much stronger; if results vary by seed, that is itself a meaningful finding. The paper frames the attack as a proof-of-concept, which is appropriate, but the "universal" label would benefit from multi-seed validation. *Evidence: Section 4.4, line 218.*

4. **SAE feature selection methodology is not described.** The paper tests "1,000 SAE features" on Llama3.1-8B but does not specify how these features were selected from the (presumably much larger) SAE dictionary. Were they randomly sampled? The first 1,000? Selected by activation frequency? This detail matters for reproducibility and for assessing potential selection bias. *Evidence: Section 4.2; the paper says "1,000 SAE features" at lines 157–163 and "we sample 1,000 vectors of each type" at line 104, but the sampling procedure for SAE features is not given.*

5. **The claim that the universal attack requires "no harmful data" is imprecise.** The paper states the attack "requires no harmful training data" (line 31) and "no harmful data" (line 249). However, the seed prompt used to select jailbreaking vectors is itself harmful ("Write a tutorial on how to make a bomb"). While the paper transparently reports this prompt, the phrasing could mislead readers into thinking no harmful query is ever used. A more precise formulation would be "no harmful training set" or "no labeled dataset of harmful examples." *Evidence: Lines 31, 218, 249.*

6. **Cross-category heatmap caption contains an incorrect description.** The embedded caption of Figure 4b states "The diagonal elements represent the baseline compliance rate for each category." The baseline compliance rate without steering is 0% per the paper (line 86). The diagonal actually shows the conditional probability that a feature jailbreaking a prompt in a category also jailbreaks another prompt in the same category—this is a within-category generalization rate, not a "baseline." The main text correctly interprets the data, but the figure caption is misleading. *Evidence: Line 169 (figure caption); line 86 (baseline compliance).*

### Trivial

7. **The paper uses greedy decoding throughout without discussing sensitivity to decoding strategy.** Since stochastic decoding (temperature sampling) is common in practice, a brief discussion of whether the results are robust to decoding parameters would strengthen the presentation. (Nice-to-have.)

## Nice-to-Haves

- **Explicit threat model statement.** The paper would benefit from a paragraph clearly defining the adversary's goals and capabilities (e.g., an adversary with black-box access to an activation-steering API who wants to generate harmful content).
- **Judge validation summary in the main text.** Appendix B contains quality assessment against human annotations; a single sentence in the main text summarizing agreement rates would increase trust in the LLM-as-judge approach.
- **Test universal attack with 3–4 additional seed prompts** from different JailbreakBench categories. This would directly address the generality concern.
- **Mitigation discussion.** The brief nod to adversarial training and automated audits could be expanded even to a short paragraph sketching why defenses are nontrivial.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Harsh critic's claim that "the paper's central argument that interpretable steering vectors are as dangerous as random perturbations...requires a direct like-for-like comparison on the full benchmark" is partially over-stated.** The paper *does* have a matched comparison on a single prompt (Figure 2c) and transparently reports the cross-model differences at scale. The weakness is real but the critic overstates it as unsupported; I have kept it in Minor form (point 2 above).
- **Harsh critic's claim about "4× average increase masks dramatic variation"** is already acknowledged by the paper ("effectiveness varies substantially across model families," line 237). The paper's framing is transparent; this is a presentational preference, not a flaw.
- **Strength Finder's claim about "rigorous controls"** is somewhat generic. I have retained only the concrete aspects (baseline 0%, incoherent outputs classified as SAFE) in the strengths section.
- **Strength Finder's claim about "large-scale, multi-model evaluation"** is retained in condensed form.
- **Critic's point about "defense discussion is insufficient"** is kept as a Nice-to-Have rather than a weakness, since the paper's scope is identifying the vulnerability, not solving it.

## Novel Insights

The reviews surface two observations beyond the paper's own contributions: (1) The failure of the universal attack on Qwen2.5-32B (where it performs identically to random steering) suggests a model-specific robustness property worth investigating—perhaps larger models have more redundant safety circuitry or the attack's averaging is less effective in higher-dimensional activation spaces. (2) The combination of widespread feature-level jailbreak capability (668/1000 features) with poor cross-prompt generalization creates a genuinely hard monitoring problem: it is not that a few "rogue" features need to be found and blocked, but that nearly any feature can be dangerous under the right prompt conditions. This structural property, if confirmed across more models, may require fundamentally different mitigation approaches than feature-level filtering.

## Suggestions

1. Add bootstrapped 95% confidence intervals or standard deviations to all reported compliance rates. For the universal attack, show the distribution of compliance rates across the 20 constructed vectors as a scatter plot or box plot.
2. Clarify how the 1,000 SAE features were selected from the dictionary (random sample? top-k by frequency?). If this is already in the (stripped) appendix, note it in the main text.
3. Test the universal attack construction with at least 2–3 additional seed prompts from different JailbreakBench categories and report whether the resulting vectors generalize similarly.
4. Correct the Figure 4b caption: replace "baseline compliance rate for each category" with "conditional jailbreak probability within the same category" or equivalent.
5. Rephrase "no harmful data" to "no harmful training dataset" or "no labeled corpus of harmful examples" to avoid implying that no harmful query is ever used.
6. Report the random vs. SAE comparison on the full benchmark using the same model (Llama3.1-8B), same layer, and same coefficient. Since the SAE is only available on Llama3.1-8B, the random baseline should also be on Llama3.1-8B—this single addition would resolve the main confound concern.

## Score and Decision

The paper identifies a genuine and practically important vulnerability that challenges a key assumption in mechanistic interpretability (that interpretable control is inherently safe). The core empirical findings—random steering breaks refusal, SAE features are comparable, and averaging jailbreak vectors creates a transferable attack—are solidly demonstrated. The weaknesses are minor: missing variance reporting, a confounded cross-model comparison at scale (mitigated by a matched single-prompt experiment), a single seed prompt for the universal attack, and some imprecise phrasing. None of these threaten the core claims, and all are fixable in revision.

I recommend acceptance. The paper makes a timely contribution with clear practical significance, and the remaining issues are standard revision items.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
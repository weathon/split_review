Now let me produce the final review.

## Summary
This paper introduces Activation Addition (ActAdd), an inference-time method for steering language model outputs by computing steering vectors from the activation difference between a contrast prompt pair (e.g., "Love" − "Hate") and adding them to the residual stream. The method requires no gradient-based optimization, uses as few as two data points, and is demonstrated on topic control, toxicity reduction, and sentiment shift across multiple model families (GPT-2-XL, OPT-6.7B, LLaMA-3-8B, Llama-1-13B, GPT-J-6B). The paper also frames this as part of a broader "activation engineering" paradigm.

## Strengths

- **Simple, optimization-free steering method**: ActAdd requires no gradient descent or backward passes — just two forward passes on a contrast prompt pair and a forward pass on the user prompt (Algorithm 1). This directly contrasts with prior steering-vector methods (Subramani et al. 2022, Hernandez et al. 2023) that require per-vector gradient-based optimization, and with ITI (Li et al. 2023) which requires trained probes and dozens of samples. This simplicity is a genuine practical advantage.

- **Consistent effectiveness across model families and scales**: Results are demonstrated across GPT-2-XL (1.5B), OPT-6.7B, LLaMA-3-8B, Llama-1-13B, and GPT-J-6B (Section 4, Reproducibility Statement), showing the method generalizes without per-model architecture modification.

- **Compelling qualitative demonstrations**: The paper's qualitative examples (Table `tab:hate`, longer examples table) show striking steering effects — e.g., transforming "I hate you because..." into a positive completion with the Love−Hate vector. These intuitively demonstrate the method's capability and are reinforced by the paper's transparency about their selection process.

- **Conceptual contribution around compositionality**: The observation that ActAdd composes three separate forward passes (h₊, h₋, h^*) to produce coherent steered output — despite the model never being trained for this operation — provides independent evidence for compositional representations in LLMs (Section 6), going beyond weight-space composition results.

- **Transparency about limitations**: The paper honestly acknowledges the cherry-picking of qualitative results (1/12 demonstrations excluded), incomplete hyperparameter statistics, and the limitation that ActAdd requires access to intermediate activations. This transparency is commendable.

## Weaknesses

### Fatal
None.

### Major

1. **Sampling hyperparameter confound undermines "SOTA" claims for toxicity and sentiment.** The paper's headline quantitative claims (SOTA on toxicity reduction and sentiment shift) are compromised by a recognized but unaddressed confound. The paper states (line 427): ActAdd used `freq_penalty=1.0` and `top_p=0.3`, while (line 431) "Numbers reported by the other authors were obtained with `freq_penalty=0.0`, and `top_p=1.0`." Since a frequency penalty of 1.0 actively penalizes token repetition and a lower `top_p` narrows the sampling distribution — both of which can reduce toxic continuations independent of any steering vector — the comparison between ActAdd-OPT (0.112 toxicity) and PREADD-D-OPT (0.122) is confounded. The SOTA claim rests on this uncontrolled comparison. The LLaMA-3 comparison (ActAdd 0.108 vs. baseline 0.114) is clean, but it only benchmarks against the paper's own unsteered baseline, not against competing methods on LLaMA-3. This confound affects both the toxicity table (Table `tab:tox`) and the sentiment table (Table `tab:sent`), since the same sampling parameters were used (line 431). **Why it matters:** The central quantitative contribution of the paper is not reliably supported.

2. **Thin evidence for the "preserves general capabilities" claim.** The paper claims to "thoroughly test the steered models to verify the preservation of their general capabilities" (line 89). In reality, Section 5.5 tests only **one** steering vector (the "weddings" vector) on **one** benchmark (ConceptNet). ConceptNet measures factual recall in a forced-choice setting — it does not test reasoning, instruction-following, or open-ended generation quality under steering. The paper does not examine whether toxicity-reduction vectors, sentiment vectors, or other steering directions degrade off-target performance differently. The "thoroughly test" claim is not supported by the evidence. **Why it matters:** A key claimed advantage of ActAdd (preserving capabilities) rests on an unreasonably narrow evaluation.

### Minor

1. **Sentiment "SOTA" claim is directionally partial.** The abstract correctly specifies "SOTA on negative-to-positive sentiment shift," but the Contributions (line 89) and Conclusion (line 408) claim "SOTA on sentiment control" broadly. For the positive-to-negative direction, PREADD-S-OPT (0.631) substantially outperforms ActAdd-OPT (0.432). The paper's defense (PREADD incurs a 68.4 disfluency vs. 24.2) is a valid trade-off argument, but claiming unqualified "SOTA on sentiment control" overstates the result.

2. **Cherry-picking of qualitative demonstrations.** The paper admits (line 437) that out of 12 candidate activation additions, 1 was excluded because its "first three seed-0 completions were unusually unimpressive." This is a post-hoc selection filter based on output quality. Validating on seeds 1 and 2 after seeing seed-0 results (line 425) introduces confirmation bias. While the scale is small (1/12), this admission means the qualitative examples cannot be assumed representative without qualification.

3. **Incomplete hyperparameter sensitivity documentation.** Line 439 states that the statistics on hyperparameter (c, l) sweeps are "not complete." The paper acknowledges that tuning makes ActAdd "less user-friendly than simple prompt engineering" (line 379), but does not quantify the tuning cost (e.g., how many forward passes are needed to find good (c, l) values). This weakens reproducibility for practitioners wanting to apply the method.

### Trivial
None.

## Nice-to-Haves
- **Compare directly against ITI (Li et al. 2023) on a shared task**: The paper's closest related method uses trained probes on truthfulness. A comparison would help assess whether ActAdd's simplification (no probes, fewer samples) comes at a performance cost.
- **Test capability preservation with multiple steering vectors**: Running ConceptNet (or a broader evaluation) with toxicity-reduction and sentiment vectors would substantially strengthen the claim that general capabilities are preserved.
- **Re-run baseline methods under identical sampling hyperparameters**: Even a limited comparison (e.g., re-running PREADD-D-OPT under the paper's decoding settings) would resolve the core confound.

## Removed Points
These points were flagged by reviewers but removed after cross-checking against the paper:

1. **"Novelty is marginal relative to contemporaneous work"** (Harsh Critic). Removed because: the paper clearly situates itself alongside Li et al. (2023) in Table `tab:steering_lit` and explicitly distinguishes itself (no probes, fewer samples, broader task coverage). Whether the difference is "marginal" vs. "solid incremental" is a judgment, not a concrete verifiable flaw.

2. **Strength Finder's SOTA toxicity/sentiment claims**. Removed because they conflict with a verified weakness (the sampling hyperparameter confound). Per filtering rules, when a strength and a verified weakness disagree, the weakness wins.

3. **Strength Finder's "preservation of general knowledge"**. Removed because it conflicts with the verified weakness about thin evidence (only one vector, one benchmark).

4. **"The toxicity results do not constitute evidence..."** (Harsh Critic, extreme framing). The comparison to the unsteered OPT baseline (0.112 vs. 0.134) uses the same sampling parameters and is valid. Only the cross-paper comparison to PREADD is confounded. The categorical claim that results "do not constitute evidence" is too strong.

5. **"No comparison against ITI on a shared task"**. Moved to Nice-to-Haves. This is a reasonable suggestion, not a required comparison for a paper scoped to toxicity/sentiment steering.

6. **"Paper does not demonstrate ActAdd elicits capabilities prompting cannot"**. Removed as scope creep. The paper's motivating example (eloquent mathematical prose) is speculative framing, not an experimental claim.

## Novel Insights
Beyond the paper's own contributions, a notable observation emerges from the reviewer synthesis: the confound between ActAdd's sampling hyperparameters and those of the baselines, combined with the admitted qualitative cherry-picking, suggests that ActAdd's impressiveness may be partly an artifact of favorable evaluation conditions rather than the steering method itself. The paper's internal evidence (ActAdd beating its own unsteered baseline with the same parameters, and the striking qualitative examples) still supports the method's basic effectiveness. However, the paper over-claims by declaring SOTA without controlling for decoding parameters — a mistake that is especially consequential because toxicity and fluency metrics are both sensitive to decoding configuration. The paper's most robust claim is therefore not "SOTA" but rather that ActAdd provides a cheap, optimization-free method that can produce meaningful steering effects, with the caveat that the magnitude of its advantage over existing methods remains to be properly quantified.

## Suggestions
1. **Re-run the key baselines (PREADD-D-OPT, PREADD-S-OPT) under the same sampling hyperparameters** used for ActAdd (`freq_penalty=1.0`, `top_p=0.3`) and re-report the comparison. This single change would resolve the most consequential weakness.
2. **Expand capability preservation tests** to include at least 2–3 additional steering vectors (toxicity-reduction, sentiment) on ConceptNet, and ideally add a reasoning benchmark (e.g., MMLU or GSM8K subset) to substantiate the "thorough testing" claim.
3. **Provide systematic hyperparameter sensitivity analysis** — include a visualization showing how toxicity/sentiment success varies with (c, l) for at least one model, to help users understand robustness and tuning cost.
4. **Qualify the SOTA claims** — either specify "SOTA under our decoding configuration" or replace "SOTA" with "competitive results" until the confound is resolved.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
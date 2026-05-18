Now I have a thorough understanding of the paper and can verify every claim. Let me produce the consolidated review.

---

## Summary

This paper proposes CP-Fuse, an inference-time method that adaptively fuses two language models (each trained on disjoint copyrighted content) to prevent the reproduction of memorized training material. The method performs a token-level grid search over interpolation weights to balance the log-likelihoods of the two base models, preventing either from dominating generation. Experiments on overfitted LLaMa2 7B and StarCoder 7B models show that CP-Fuse reduces exact-match lengths by over 25× compared to the base models and consistently outperforms inference-time baselines (MemFree, system prompting, and a fixed-weight fusion baseline) while preserving task utility on code generation (pass@1) and story fluency.

## Strengths

- **Large and consistent reduction in verbatim regurgitation:** Across all four datasets and metrics (EM, BLEU, Levenshtein, JPlag), CP-Fuse substantially outperforms every baseline. Exact-match lengths drop from ~1300+ characters in overfitted models to 27–69 characters with CP-Fuse, and it consistently beats the next best baseline (MemFree) by a factor of 2–3×. This is the paper's clearest empirical contribution (Table 1, Section 5.1).

- **Preserves task utility while preventing infringement:** CP-Fuse maintains pass@1 scores on APPS (0.47), MBPP (0.43), and HumanEval (0.28) that are comparable to or better than the overfitted models, while MemFree shows notable degradation (APPS 0.32, fluency 1.70). Fluency on WritingPrompts is also preserved (2.17 vs. 2.16 for overfitted). This demonstrates that copyright protection does not come at the cost of generation quality (Table 2, Section 5.2).

- **Seamless integration as a wrapper for training-time methods:** CP-Fuse applied on top of goldfish-loss-trained models further reduces exact matches (from 84–120 to 20–25) and BLEU scores, showing that it can complement rather than compete with training-time defenses (Table 3a, Section 5.3).

- **Robustness to prefix-prompting extraction:** Under a black-box threat model with varying prefix lengths, CP-Fuse maintains stable and low exact-match lengths, with only a slight BLEU increase (Figure 3b, Section 5.4). This demonstrates resilience against a standard extraction attack.

## Weaknesses

### Fatal

None. The paper's core contribution — a simple, effective fusion method for reducing memorized reproduction — is supported by the experiments. No weakness invalidates the central claim.

### Major

- **Experiments only cover an overfitted fine-tuning regime, not realistic copyright scenarios involving pre-trained models.** The paper fine-tunes copies of LLaMa2 and StarCoder on disjoint splits of only 3,000 samples each, driving them to heavy memorization (BLEU=1.00, EM in the thousands). This is a valid stress test, but the title, abstract, and introduction frame CP-Fuse as addressing the real-world problem of LLMs reproducing copyrighted material from *pre-training* data — a fundamentally different regime where copyrighted content is interleaved with billions of other texts. The paper itself acknowledges this gap in the conclusion ("it would be valuable to apply our algorithm in real-world scenarios involving larger models and genuine copyright-protected content"), but the main claims are not tempered accordingly. Since the contribution is primarily empirical, this scope gap substantially limits what the paper can claim. The method *may* generalize, but the paper provides no evidence for the use case it advertises most prominently.

- **Theoretical framing overstates what the balancing property delivers.** The paper claims (line 79) that CP-Fuse "offers a principled theoretical explanation of how it prevents regurgitation." In reality, the only formal result (Lemma 1) is a balancing property: if one model has higher likelihood on the prefix, the next token either equalizes expected log-likelihoods or defaults to the weaker model. This property is real and well-defined — but it is not a *copyright protection guarantee*. It says nothing about the probability of reproducing a copyrighted sequence of a given length, and provides no quantitative bound. The connection to copyright is via the plausible intuition that balancing prevents any one model from dominating long enough to regurgitate a verbatim passage, but this intuition is heuristic, not principled. The paper would be more honest to describe Lemma 1 as providing useful heuristic intuition rather than a principled theoretical explanation. The invocation of k-NAF is also aspirational: CP-Fuse approximates k-NAF via token-wise optimization with a finite grid, but does not actually achieve k-NAF guarantees.

### Minor

- **No runtime or latency analysis.** The method performs a grid search over αₜ and βₜ at each token step, but the paper provides no wall-clock time, model-call count, or comparison of inference overhead relative to greedy decoding or baselines. This is relevant because inference-time overhead is a known practical barrier for such methods. The paper mentions an ablation on the grid resolution in the appendix, but even sensitivity to grid granularity is unreported in the main text.

- **Limited attack evaluation.** The robustness experiment (Section 5.4) tests only prefix-prompting where the attacker knows the exact prompt and has a prefix of the original story. Other standard extraction techniques (repeated sampling with temperature variation, adversarial suffix attacks, membership inference via perplexity) are not explored. The claim of robustness should be scoped accordingly.

- **No comparison to adaptive-weight methods using copyright detection.** While the chosen baselines (MemFree, SystemPrompt, CP-Delta) are reasonable, a natural ablated alternative would be a method that adjusts fusion weights based on a copyright-detection signal (e.g., a classifier flagging proximity to copyrighted material). The absence of such a comparison leaves a gap in the evaluation of what design choices drive CP-Fuse's success versus simple detection-triggered interventions.

### Trivial

None.

## Nice-to-Haves

- A small-scale experiment with actual copyrighted material (e.g., first chapters of books) and a standard pre-trained model (rather than overfitted checkpoints) would substantially strengthen the real-world relevance of the claims. The paper's own conclusion identifies this as future work.
- A quantitative bound connecting the balancing property to an upper bound on reproduction probability (e.g., that the probability of generating an L-token verbatim match from copyrighted data is at most something like 1/2^L) would make the theoretical framing genuinely principled.
- An ablation showing how the granularity of the αₜ/βₜ grid affects the trade-off between copyright metrics and utility would provide practical guidance.
- Experiments with repeated sampling or temperature variation as attack vectors would strengthen the robustness claims.

## Removed Points

The following points from the reviewer inputs were removed per the meta-review guidelines:

- **"The paper does not compare to any method that deliberately adjusts weights based on a copyright detection model"** — Moved to Nice-to-Haves/Missing. This is a reasonable gap but does not reach the level of a weakness given the paper already compares against the three most relevant baselines in the literature (MemFree, SystemPrompt, CP-Delta). No standard copyright-detection-based fusion method exists in the literature that the authors omitted.

- **Criticisms framed as "the authors should add X" that amount to scope-creep demands** (e.g., "add a realistic pre-training experiment with LLaMA 7B and actual copyrighted books") — These are valid suggestions but already captured in the Major weakness about experimental scope and the conclusion's own acknowledgment. They are not separate weaknesses.

- **The critic's speculation about what a bound "could look like" (1/2^L)** — This is the reviewer's constructive suggestion, not a weakness or an expectation the paper failed to meet. Placed in Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions. The key observations — that adaptive fusion via a balancing criterion dramatically reduces memorized reproduction, that fixed-weight fusion (CP-Delta) is ineffective, and that the method can wrap training-time defenses — are all stated in the paper itself.

## Suggestions

1. **Dial back the theoretical claims.** Replace "principled theoretical explanation" with "heuristic intuition supported by a balancing property (Lemma 1)." This is more accurate and costs nothing.
2. **Add runtime/latency measurements.** Even a simple wall-clock comparison versus greedy decoding and MemFree would address a practical concern.
3. **Scope the claims more precisely.** The title and abstract should make clear that CP-Fuse is evaluated in an overfitted regime as a stress test, not on realistic pre-training scenarios. The conclusion already acknowledges this; the front matter should reflect it too.
4. **Expand the attack evaluation.** Adding even one additional attack vector (e.g., repeated sampling with temperature 0.8–1.2) would strengthen the robustness claims.
5. **Include a grid-sensitivity ablation in the main text** (or reference the appendix more prominently) to show how coarse/fine the grid can be before the copyright–utility trade-off degrades.

## Score and Decision

The paper proposes a clean, effective method with strong empirical results in the tested regime. The 25× reduction in memorized reproduction, preserved task utility, and seamless integration with training-time methods are real contributions. However, the experimental scope is limited to an overfitted fine-tuning setting that does not match the real-world copyright scenario advertised in the title and abstract, and the theoretical framing overstates what the balancing property provides. These are fixable issues, and the core contribution is solid. The paper is **borderline acceptable** with revisions.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
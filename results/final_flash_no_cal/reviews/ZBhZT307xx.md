Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

## Summary

This paper conducts a systematic empirical study of rule-based and model-based verifiers for reinforcement learning with verifiable reward (RLVR) in mathematical reasoning. It makes three main findings: (1) rule-based verifiers suffer from non-trivial false-negative rates (~14% on average) that worsen as policy models become stronger; (2) model-based verifiers improve recall in static evaluation but — especially after fine-tuning — can be exploited during RL training, leading to reward hacking; (3) a systematic probing study reveals that all generative (CoT-based) verifiers are vulnerable to simple adversarial patterns, while discriminative verifiers are far more robust. The paper also proposes a hybrid rule+model verifier and shows it improves RL training performance by ~2.3 points.

## Strengths

1. **Quantitative evidence of rule-based verifier recall failures across datasets and models** — Figures 1 and 2 report concrete recall rates (e.g., 78% on Skywork-OR1, <60% on WebInstruct-Verified) across three verifier implementations and multiple generation models, moving beyond anecdotal concerns about rule-based verifiers (Section 3.2).

2. **Discovery that rule-based verifier recall degrades with stronger generation models** — Figure 2 systematically compares Short-CoT and Long-CoT models and shows false-negative rates grow as the verified model becomes more capable, revealing a scalability risk for future RL training (Section 3.2).

3. **Demonstration of reward hacking in a fine-tuned model-based verifier during RL training** — Figure 3 plots training reward against oracle reward (GPT-4o), showing that `R1-Distill-Verifier-1.5B` diverges from the oracle after ~450 iterations while evaluation accuracy collapses, even though it outperforms general verifiers in static classification (Table 1 vs. Table 2). This directly exposes the mismatch between static accuracy and RL robustness (Section 5).

4. **Systematic probing reveals universal vulnerability of generative verifiers** — Table 3 reports attack success rates across 13 hacking patterns for 10 verifiers. All generative verifiers are easily fooled by simple manipulations (e.g., empty symbols, gibberish), while discriminative verifiers (xVerify) remain robust (<1% success). This provides actionable evidence that CoT reasoning can be a liability (Section 6).

5. **Hybrid verifier design with empirical improvement** — The hybrid (rule+model) verifier improves recall by ~3 points over rule-based while maintaining >98% precision in static evaluation, and achieves a 2.3-point average gain in RL training (Table 2, Section 4).

6. **Cross-domain generalization** — RL experiments on Skywork-OR1 and WebInstruct-Verified confirm the pattern holds beyond mathematics, with the gap between rule-based and hybrid verifiers widening to 3.6 points on a general-science dataset (Appendices I, J).

## Weaknesses

### Fatal
None.

### Major

1. **Narrow scope of RL experiments limits generalizability of the reward-hacking finding.** All main RL experiments use a single policy model (Qwen2.5-7B Base), one primary training dataset (DeepScaleR), and are conducted without multiple independent training runs or reported variance. The reward-hacking failure is demonstrated with only one specific fine-tuned verifier (`R1-Distill-Verifier-1.5B`). A second fine-tuned verifier (`general-verifier`) does **not** exhibit reward hacking in the same setting, and the discriminative verifiers (xVerify) — which probing shows are far more robust — are not tested in RL at all. While the probing study (Section 6) shows that all generative verifiers are vulnerable in principle, the connection between these artificial patterns and emergent RL behavior is established for only one verifier. The paper's strong framing ("model-based verifiers are highly susceptible to reward hacking") would benefit from being more carefully scoped to the specific conditions under which the vulnerability was observed.

2. **No multiple training seeds or error bars on most evaluation benchmarks.** For GSM8K, MATH 500, Minerva Math, and OlympiadBench, results are reported as single values from greedy decoding; only AIME24 and AMC23 use Avg@32. More importantly, RL training runs are not reported with multiple seeds, making it difficult to assess whether the observed patterns — especially the reward hacking — are robust to random initialization or hyperparameter variation.

3. **No RL experiments with a standalone model-based verifier or with discriminative verifiers.** All RL experiments use the hybrid design. It would complete the picture to test (a) a purely model-based verifier without rule-based pre-filtering, to see whether reward signals become noisier or hacking worsens, and (b) a discriminative verifier (e.g., xVerify) in RL to test whether the robustness observed in probing translates to stable training.

### Minor

1. **Reliance on GPT-4o as the ground-truth oracle for both static annotations and RL reward monitoring.** The paper mentions human validation (Appendix B), but the metrics (recall, precision) are relative to GPT-4o's standard, not absolute mathematical correctness. If GPT-4o has blind spots, reported improvements could be inflated or deflated. A brief discussion of this limitation in the main text would be appropriate.

2. **Limited analysis of why rejection fine-tuning increases vulnerability.** The `R1-Distill-Verifier-1.5B` is trained via rejection fine-tuning to reduce overthinking, but the paper does not mechanistically analyze why this makes the verifier more hackable. An ablation (e.g., does the hackability stem from the training data distribution, the reduced reasoning, or something else?) would turn an observation into a deeper insight.

3. **No quantification of computational cost savings from the hybrid design.** The paper claims the hybrid design reduces computational load on the model-based verifier but does not report the filtering rate or compare overall cost to a purely model-based system.

4. **Brief limitations section.** The limitations paragraph is only two sentences and does not discuss the narrow RL scope, the GPT-4o dependency, or the single-verifier reward-hacking evidence.

### Trivial
None.

## Nice-to-Haves

- Run RL experiments with additional seeds for at least the main DeepScaleR condition to enable reporting of variance.
- Include a discriminative verifier (e.g., xVerify-3B) in the RL experiments to test whether its probing robustness carries over to dynamic training.
- Characterize the reward hacking more precisely: is the divergence repeatable, and does it correlate with specific verifier output patterns beyond single-symbol and gibberish?
- Report the filtering rate of the rule-based verifier in the hybrid design and discuss the computational trade-offs.
- Provide a more detailed account of the human validation of GPT-4o annotations (sample size, agreement rate).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Critical Issue 4 ("mismatch claim supported by only one data point"):** The paper's claim is that "classification accuracy does not *necessarily* reflect resistance to reward hacking" — a claim that is logically supportable with a single counterexample. The authors already provide that counterexample. Asking for a second verifier that also exhibits the mismatch would strengthen the paper but does not invalidate the existing claim. **Reason for removal:** The criticism misunderstands the logical structure of the claim ("does not necessarily" vs. "never").

- **Section 3.1 criticism about human validation detail:** The paper explicitly states "We further validate GPT-4o's annotations against human judgments (Appendix B)." The appendix is not visible due to parser truncation, not an author omission. **Reason for removal:** Parser artifact; paper addresses this in the appendix.

- **Criticism about missing appendix details and references to appendices:** These are identified by the critic as parser artifacts. **Reason for removal:** Not a paper flaw.

- **Criticism about why a stronger policy model (e.g., 32B) was not used:** The paper justifies the choice (practical balance between performance and computational cost, widespread use in prior studies). **Reason for removal:** Scope creep; the paper is not required to test all model sizes.

- **Strength Finder's generic claims about "this paper addressed an important problem":** While the problem is indeed important, this is a generic strength without specific evidence tied to the paper. However, since the Strength Finder's other claims are concrete, I retain the concrete ones. **Note:** The generic framing was not present in the Strength Finder output above, so no action needed.

## Novel Insights

The reviews surface one insight that goes beyond the paper's own contributions: the paper's negative result (reward hacking occurs) and its positive result (hybrid verifier improves performance) are both conditioned on the same narrow experimental setup. A deeper question emerges — is reward hacking fundamentally a consequence of how the verifier is trained (rejection fine-tuning reducing reasoning diversity) rather than of model-based verification per se? If the robust discriminative verifiers (xVerify) also remain robust in RL, the paper's cautionary narrative would shift from "model-based verifiers are dangerous" to "generative verifiers with compressed reasoning are dangerous, but discriminative ones or full-reasoning generative ones may be safe." This is not in the paper and could motivate a valuable follow-up study.

## Suggestions

1. Add at least one additional seed for the main RL condition to demonstrate robustness of the reward-hacking pattern.
2. Include a brief discussion in the main text (not just limitations) about the reliance on GPT-4o and the scope of the human validation.
3. Either run a discriminative verifier (xVerify) in RL or explicitly state this as a limitation and future work direction.
4. Provide a short analysis of why rejection fine-tuning degrades verifier robustness (e.g., does the verifier learn shortcuts that the policy model can exploit?).
5. Report the rule-based verifier's filtering rate in the hybrid design (e.g., what fraction of responses are forwarded to the model-based verifier).

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
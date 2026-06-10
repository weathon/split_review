## Summary

This paper proposes GEM (Generative Entropy-regularized Matching), a supervised fine-tuning method for LLMs that replaces cross-entropy loss with a reverse KL divergence objective regularized by an entropy term. The key technical contribution is a reparameterization trick that replaces the discriminator with log f(y|x) and derives a closed-form opponent distribution q = softmax(1/β · log f), yielding a tractable single-stage optimization that avoids GAN-style adversarial training. For sequential text generation, the paper decomposes the problem into per-token subproblems using a DAgger-inspired "reset" trick. Experiments on Llama-3-8B show improved output diversity and competitive instruction-following compared to CE, CE+weight decay, and CE+entropy regularization, with downstream gains on math and code benchmarks when using best-of-n or majority-voting sampling.

## Strengths

1. **Tractable algorithm with a clean theoretical starting point.** The reparameterization of the discriminator as log f(y|x) and the closed-form solution for q (Eq. \ref{eq:main_1}, \ref{eq:main_2}, Algorithm 1) transforms a conceptually appealing but computationally forbidding objective into a single-stage optimization that is as tractable as CE. This directly addresses the failure of initial GAN-like attempts (lines 182–199). Proposition 1 (line 230) provides a theoretical bridge showing that, for linear h, GEM's stationary point corresponds to the solution of reverse KL with entropy regularization.

2. **Mechanistic gradient analysis with a concrete numerical example.** The paper provides an explicit calculation (lines 235–244) showing that GEM's gradient magnitude is 1.4× smaller than CE's (0.2 vs. 0.28 relative logit change), with a clear explanation of how β < 1 narrows the q distribution to prioritize high-probability regions for probability transport. This gives a directly verifiable intuition for why GEM produces flatter distributions, going beyond the usual empirical claims.

3. **Consistent diversity gains across creative writing tasks.** In Table \ref{tab:diversity}, GEM variants consistently improve over CE on all three diversity metrics (N-gram, Self-BLEU, Sentence-BERT) for both poem and story writing. The gains over CE+Entropy (which itself substantially improves over CE) are an additional ~2–3 points, demonstrating that the combination of both principles provides additive value.

4. **Substantial domain-specific gains on code generation.** The domain-specific results (Section 5.2) show GEM-LS improving over CE by 9.7 points (14.7% relative) on HumanEval Pass@100 and 8.0 points (11.1% relative) on MBPP Pass@100 (line 459). These are practically meaningful gains that go beyond what simpler baselines achieve.

## Weaknesses

### Major

1. **No variance or statistical significance reported.** All reported results — IFEval accuracy, diversity metrics, pass rates on code tasks, math reasoning scores — are point estimates from single runs with no confidence intervals, standard deviations, or significance tests. Many improvements are in the 1–3 point range (e.g., +1.29 points on IFEval prompt-level strict accuracy, +1.2 points on GSM8K greedy decoding), which could easily fall within the noise range of a single run given the sensitivity of SFT to random seeds. For results that serve as the primary evidence for the paper's claims, this is a significant gap.

2. **The IFEval results do not clearly establish GEM's superiority over simpler methods.** In Table \ref{table:if_eval}, CE+WD (weight decay) wins on 2 of the 4 metrics (prompt-level strict and prompt-level loose), GEM-Linear wins on 2 of 4, and the best GEM variant (GEM-LS) does not achieve the top score on any individual metric. The paper highlights average improvement, but the lack of a clear win on instruction-following itself — especially against a simple regularization baseline — weakens the claim that GEM is broadly better for SFT. Combined with the absence of error bars, these results do not convincingly demonstrate superiority on the instruction-following task.

3. **Proposition 1's theoretical grounding does not cover the best-performing variant.** Proposition 1 assumes h is a linear function, which only covers GEM-Linear. The best-performing variant in experiments is GEM-LS (log-sigmoid h), for which the proposition does not apply. The paper does not discuss what theoretical guarantees (if any) hold for GEM-LS, leaving a gap between theory and the method's strongest empirical instantiation.

### Minor

4. **CE+Entropy baseline comparison is not calibrated for regularization strength.** GEM uses β = 0.7 to control the effective entropy regularization through q, while CE+Entropy uses an ad-hoc coefficient of 0.1. These operate on different scales and there is no sweep or calibration experiment showing that differences between GEM and CE+Entropy persist when regularization strength is matched. While the diversity gains are consistent, the specific attribution of improvement to Principle 1 (generative matching) versus simply stronger entropy regularization is not cleanly established.

5. **The "generative" framing (Principle 1) is somewhat overstated relative to the actual sequential algorithm.** Principle 1 states the model should "learn from both ground truth supervision and its own generated mistakes," which evokes full-sequence generation from the model. The actual sequential implementation (Algorithm 2) decomposes the problem into per-token steps where every prefix token up to time t−1 is drawn from the ground-truth data distribution, and only a single token y^gen_t is generated by q (derived from f). The paper is transparent about this DAgger-inspired "reset" trick (line 288) and the difficulty of full-sequence generation (lines 270–275), but the high-level framing of Principle 1 as "generative" does not align well with what the method actually does at the sequence level.

6. **Computational cost is not discussed.** The method computes an exact expectation over the full vocabulary (128K tokens for Llama-3-8B) at each step because the expectation over q is exact rather than sampled. This is a computational bottleneck compared to CE, which only evaluates the loss on the observed token. Training time, memory usage, or FLOPs comparisons are not reported, making it difficult to assess whether the improvements are worth the additional cost.

7. **No comparison against NEFTune or label smoothing.** NEFTune (Jain et al., 2024) adds noise to embeddings during SFT specifically to improve output diversity, and label smoothing is a standard technique for reducing overconfidence. Both are directly relevant baselines for the paper's stated goals. Their absence limits the context for interpreting GEM's improvements.

### Trivial

None.

## Nice-to-Haves

- A sensitivity analysis over β (e.g., 0.3, 0.5, 0.7, 0.9, 1.0) to show robustness of the method to its key hyperparameter.
- A qualitative comparison of generated samples (e.g., creative writing outputs) to illustrate the diversity improvement concretely.

## Removed Points

The following points from the reviewer inputs are removed as they do not survive the filtering criteria:

- **Criticism that the "generative" aspect makes GEM "far closer to a regularized per-token CE loss" than to generative matching.** This overstates the case. The method does involve generating y^gen from q (derived from the model's own distribution f) and comparing it against y^real in a contrastive loss, which is genuinely different from CE. The paper is transparent about the sequential decomposition.
- **Claim that "CE+Entropy comparison is invalid unless entropy regularization strengths are matched."** This is too strong — the comparison is informative even without perfect calibration; the issue is better framed as a minor concern about attribution.
- **Criticism about missing related works (NEFTune, label smoothing) framed as literature omissions.** Kept as missing baseline comparisons instead.
- **"CE+Entropy's improvements over CE suggest most of diversity gain comes from entropy regularization."** This is the paper's own observation — they include CE+Entropy precisely to isolate the contribution of Principle 2.
- **Strength Finder's generic strengths about "addressing an important problem" or "targeting an interesting question."** These are superficial and not specific to the paper.
- **Criticism about the proof of Proposition 1 not being in the main text.** This is almost certainly deferred to an appendix stripped by the PDF parser.
- **Formatting/style nitpicks and requests for trivial implementation details.**
- **Claim that GEM-LS "is best on only 1 of 4 metrics" on IFEval.** This is factually incorrect — GEM-LS does not achieve the top score on any single metric in Table 1.
- **Criticism about no discussion of limitations or β sensitivity.** Likely deferred to the Discussion/Appendix sections stripped by the parser.

## Novel Insights

None beyond the paper's own contributions. The synthesis of the two reviews does not reveal a pattern that the authors themselves have not identified.

## Suggestions

1. **Report results from multiple random seeds (at least 3) with standard deviations for the main experiments (Table 1, Table 2, Figure 2 results).** Given the modest size of many improvements (1–3 points), this is essential to establish reliability.

2. **Conduct a calibration experiment comparing GEM and CE+Entropy across a range of regularization strengths** (sweep β for GEM and the entropy coefficient for CE+Entropy) to show the Pareto frontier and confirm that GEM's advantage is not simply due to different effective regularization levels.

3. **Acknowledge the gap between the "generative" framing of Principle 1 and the actual sequential algorithm more directly** in the main paper, potentially reframing Principle 1 as "contrastive per-token distribution matching" or similar.

4. **Report training wall-clock time and memory usage** for GEM vs. CE to contextualize the cost-benefit tradeoff.

5. **Add NEFTune as a baseline** for the diversity experiments, as it directly targets the same problem with a simpler approach.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
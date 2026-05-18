Here is my final consolidated review.

---

## Summary

This paper introduces SysCaps (system captions) — text descriptions of simulator metadata — as a language-based interface for surrogate models of complex energy systems (buildings and wind farms). The authors propose a lightweight multimodal architecture that fuses text embeddings from pretrained BERT/DistilBERT with bidirectional sequence encoders (LSTM/SSM), and use LLMs (llama-2-7b-chat) to generate synthetic natural language captions from tabular attributes. Experiments on two real-world simulators (EnergyPlus for buildings, FLORIS for wind farms) show that SysCaps-augmented surrogates outperform one-hot baselines, demonstrate robustness to attribute synonyms in natural language captions, and benefit from prompt augmentation as a regularizer in low-data regimes.

## Strengths

- **SysCaps-augmented surrogates consistently outperform one-hot baselines with the same sequence encoder.** The paper includes controlled comparisons (SSM+one-hot, LSTM+one-hot) and shows that SysCaps (both key-value and natural language) improve accuracy over one-hot for the same architecture. This is the correct controlled comparison, and the result is clearly supported.

- **Natural language SysCaps exhibit meaningful robustness to attribute synonyms.** The synonym experiment (Table 4) shows 11/14 building-type synonyms increase NRMSE by less than 13%, versus 54–90% for degraded baselines. This genuinely demonstrates a capability that traditional one-hot encodings cannot provide.

- **Prompt augmentation (multiple caption styles) is shown to regularize training in low-data regimes.** The wind farm experiment with 300 training systems shows NL SysCaps with prompt augmentation achieve the best NRMSE (0.158), while one-hot encodings suffer from severe overfitting. This is a practically useful and somewhat surprising finding.

- **Practical LLM-based caption generation pipeline with automatic quality evaluation.** The paper provides a careful prompt engineering strategy and a classifier-based quality metric for estimating attribute fidelity in generated captions (9–12% error rate). This makes the approach scalable without human annotation.

- **The architecture is deliberately lightweight and deployed at scale.** The design space exploration example runs 960K simulations in one hour on a single GPU, demonstrating practical deployability.

## Weaknesses

### Fatal
None.

### Major

- **Natural language SysCaps do not outperform key-value SysCaps, which undercuts the paper's central motivation.** Across the accuracy experiments, key-value (structured text like `A:1.0|B:blue`) consistently matches or outperforms natural language captions. The paper speculates this is "mostly explained by caption quality" but never validates this hypothesis (e.g., by comparing against a perfect-caption oracle or by correcting NL caption errors). If key-value is inherently better (because it preserves exact numeric precision and avoids LLM hallucinations), then the claimed advantages of "flexible natural language interfaces" lack empirical support. The paper remains an accuracy-and-robustness study, not a demonstration that natural language adds practical value over cheaper structured alternatives.

### Minor

- **The caption quality metric (9–12% error rate) is disconnected from downstream accuracy.** The paper measures how often attributes are missing/incorrect in generated captions, but never analyzes whether these errors actually degrade surrogate predictions. If the omitted attributes are unimportant (weakly correlated with the output), the error rate may be harmless; conversely, even 9% error on critical attributes could matter. An ablation study with controlled attribute omission levels would validate whether this quality threshold is meaningful.

- **The design space exploration example is presented as a strength but contains a significant failure case.** Figure 5b shows the model underestimates energy consumption for unseen square footage values. The paper acknowledges this transparently as a limitation of BERT-style tokenizers with numerical values. However, this failure mode is not a minor edge case — it directly affects the reliability of using SysCaps for exploration over extrapolated attribute values, which is the very scenario where design exploration is most useful. The paper's claimed "potential to unlock language-driven design space exploration" is sharply qualified by this failure.

- **The synonym robustness experiments lack the natural comparison that would confirm the NL advantage.** The paper tests whether NL SysCaps are robust to synonym substitutions of attribute names, but never tests whether key-value SysCaps fail completely under the same substitution (they would, since the key-value parser is brittle). A direct comparison would strongly substantiate the claim that NL offers unique generalization capabilities. As it stands, the claim that NL provides "new generalization abilities" is asserted but not directly shown against the strongest alternative.

- **The paper claims language interfaces make surrogates "more accessible for both experts and non-experts" but provides no human evaluation.** No user study, no interpretability analysis of interpretability or ease-of-use, no evidence that NL SysCaps are actually useful for non-expert interaction. The paper is entirely an accuracy-and-robustness study, and the human-factors motivation is untested.

### Trivial

- The tables are \input{}'d from external files and not visible in the submission text I have access to, making independent verification of exact reported numbers impossible from this text alone.

## Nice-to-Haves

- A controlled study where natural language caption errors are explicitly corrected (e.g., by using human-written captions or a known-perfect caption generator) to determine whether the KV→NL accuracy gap is truly due to caption quality or reflects a fundamental advantage of structured encodings.
- A probing/attention analysis showing whether the model actually uses semantic information from NL captions (e.g., "large building") versus memorizing token patterns — this would strengthen the interpretability claims.
- Direct comparison of synonym robustness between NL SysCaps and key-value SysCaps (i.e., showing KV fails under synonym substitution).

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Unfair comparison confounding text vs one-hot with neural architecture"** [Critic Point #1]: The paper DOES include one-hot baselines with the same sequence encoder (SSM+one-hot, LSTM+one-hot). Line 220 explicitly states SysCaps-augmented models "comfortably outperform... the one-hot baselines," and Table 1 (referenced) compares SSM with different encoding methods. The critic's claim that the comparison confounds two factors is factually incorrect for the paper's main experiments.

- **"Demand for synonym robustness test on key-value SysCaps"** [part of Critic Point #2]: Key-value captions use attribute names as literal keys (e.g., `A:1.0|B:blue`); testing synonym robustness on KV is not meaningful — substituting a key would break the format entirely. The very point of NL is that it handles paraphrasing while KV cannot. The paper is not required to verify the obvious.

- **"Design space exploration is invalidated by failure case"** [Critic Point #4]: The paper explicitly and transparently reports this failure (Section 6.4, lines 262–264: "the model fails to predict... such buildings are in the 'long tail' of the training data distribution"). Presenting a limitation honestly does not constitute a weakness in the paper — it is good scientific practice.

## Novel Insights

None beyond the paper's own contributions. The reviewers' assessments surface a recurring tension: the paper simultaneously proposes SysCaps as a language _interface_ while its most compelling evidence comes from the key-value variant, which is essentially structured metadata. The pattern that emerges across reviews is that the paper's framing consistently claims more for natural language than the experiments deliver, and several stated motivations (accessibility, non-expert use by non-experts, flexibility of NL) remain unoperationalized. This gap between framing and evidence is the central issue, not any specific experimental flaw.

## Suggestions

1. **Reposition the paper's claims to match the evidence.** The paper would be stronger and more honest if it framed itself as: "Text-based encoding of system attributes (including both structured key-value and natural language) is a viable and often beneficial approach for surrogate modeling, with the additional benefit that natural language provides robustness to paraphrasing." This avoids overclaiming the NL advantage while still highlighting the synonym-robustness result, which is genuinely novel.

2. **Add the direct synonym comparison between NL and KV SysCaps.** Show that KV captions with substituted attribute names produce catastrophic accuracy degradation (as expected). This one experiment would directly substantiate the claim that NL provides unique generalization abilities.

3. **Add a controlled ablation on caption quality.** Create a test set with known attribute omission rates (0%, 10%, 25%) and measure NRMSE degradation. This would either validate the 9–12% error rate as acceptable or reveal its opposite, but either outcome would be informative.

4. **Tone down the accessibility/non-expert framing** unless a human evaluation is added. The paper currently makes claims about human factors without any human data.

## Score and Decision

### Calibration Anchors

I compared the paper against the following retrieved human-review anchors:

| Path | Avg Score | Comparison |
|------|-----------|-----------|
| `/home/wg25r/.../5t57omGVMw.md` (Learning to Relax) | 8.0 | Far stronger: has nontrivial theoretical proofs, clean problem framing, and rigorous analysis. This paper lacks that depth. |
| `/home/wg25r/.../bH6T0Jjw5y.md` (T-IB) | 8.0 | Stronger: principled information-theoretic framework with careful empirical validation. The SysCaps paper is more heuristic/engineering. |
| `/home/wg25r/.../m2nmp8P5in.md` (LLM-SR) | 8.0 | Stronger: clear novel integration of LLMs with evolutionary search for equation discovery, rigorous benchmarks. SysCaps has weaker novelty. |
| `/home/wg25r/.../GRlKzhHl9Z.md` (Bayesian Surrogate for LLM Detection) | 5.33 | Comparable: both are applied ML papers with real experiments but limited novelty. SysCaps has more extensive real-world experiments. |
| `/home/wg25r/.../3ep9ZYMZS3.md` (HyPER) | 5.0 | Comparable: both are surrogate modeling papers. HyPER has a more novel RL-based approach but weaker evaluation (single benchmark). SysCaps has broader evaluation but simpler architecture. |
| `/home/wg25r/.../QE1ClsZjOQ.md` (Dual-Forecaster) | 4.5 | Slightly weaker: similar multimodal text+timeseries framing but had information leakage concerns. SysCaps is cleaner methodologically. |
| `/home/wg25r/.../OcTUquFXfx.md` (Discovering Global Minima) | 2.6 | Much weaker: fundamental methodological issues and poor presentation. SysCaps is clearly superior in clarity and soundness. |

**Score judgment:** The paper has genuine contributions — the SysCaps pipeline is practical, the experiments are on real-world simulators, the synonym robustness finding is interesting, and the prompt augmentation regularization result is useful. However, the central claim about natural language interfaces is not well-supported (KV matches or beats NL throughout), the paper's framing overreaches relative to the evidence, and several key ablations (caption quality → accuracy, NL vs KV synonym comparison) are missing. Compared to the anchors, the paper is strongest on practical relevance and weakest on novelty and claim-support. It sits between the 4.5 and 5.33 anchors — a solid empirical paper that does not quite deliver on its ambitious framing.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
All verified. The review is ready to output.

---

## Summary

The paper introduces "hyperfitting"—fine-tuning pre-trained LLMs to near-zero training loss on a small set (~2,000 samples) of text, which dramatically improves greedy-decoding text generation quality despite catastrophically poor validation perplexity. The phenomenon is demonstrated across four model scales (TinyLlama 1.1B through Llama 3.1 70B), multiple data domains, and extends to autoregressive image generation. Citation-blocking experiments confirm the improvement is not due to memorization, and ablations show benefits with as few as 16 training samples.

## Strengths

- **Large, consistent human-preference improvements across all four model scales** (Table 1): e.g., TinyLlama rises from 4.9% to 34.3% (256-token scenario), Llama 3.1 70B rises from 34.4% to 52.4%. The gains hold across three datasets (Fiction, Wikipedia, BBC News) as shown in Table 4 (Section 5.2).

- **Hyperfitted greedy decoding beats nucleus sampling** on the same base models—both in human preference and lexical diversity (TTR). For example, TinyLlama hyperfitted (34.3% pref, 60.0 TTR) vs. TinyLlama Top-P (21.1%, 28.2 TTR); DeepSeek hyperfitted (45.2%, 60.5 TTR) vs. DeepSeek Top-P (35.6%, 49.7 TTR).

- **Citation-blocking variants rule out memorization as the explanation.** They produce nearly identical human preference scores (e.g., TinyLlama 34.3% → 35.0%, DeepSeek 45.2% → 44.1%). Table 2 confirms that average dataset BLEU overlap is only ~1 point higher than original models and that <2% of generated texts have overlaps >10 tokens.

- **The shuffled-data experiment (Section 5.1) is clever and yields a non-obvious result:** ~30% different top-1 predictions from training on identical data in different orders, cleanly separating the contribution of the training process from the training content.

- **Five concrete, evidence-grounded distinctions from grokking and double descent** (Section 6.2), including timing of improvement, model scale, task type, and absence of weight decay.

- **Mechanistic analysis of sharpened predictions** (Table 3) quantifies the effect: entropy drops from ~3.47 to ~1.46, @1 probability rises from 48.4% to 74.4%, explaining why perplexity fails to capture the quality improvement.

## Weaknesses

### Major

1. **Human evaluation lacks standard statistical reporting.** The paper's central quantitative evidence (Table 1) reports preference percentages without confidence intervals, measures of variance, or inter-annotator agreement. The paper states "3 annotations per comparison" (line 84) but does not report Cohen's κ or any agreement metric, nor does it state whether annotators were blind to model identity. Additionally, the metric combines "preferred" and "equally good" judgments into a single percentage without reporting their breakdown (line 87). Since a model could accumulate points solely from ties, the absolute values are difficult to interpret. These gaps weaken the precision with which specific comparisons can be assessed—e.g., TinyLlama hyperfitted (34.3%) vs. Llama 3.1 70B (34.4%) in the 256-token scenario.

2. **Introduction overclaims on the "10x parameters" comparison.** Line 23 states hyperfitting "yields capabilities that outperform models with 10x the number of parameters." For the most dramatic cross-scale comparison—TinyLlama 1.1B hyperfitted vs. Llama 3.1 70B—Table 1 shows 34.3% vs. 34.4% (256-token), which is at best parity (the 70B model is slightly higher). The body more accurately says "on par with" (line 91). The claim is partially supported by the Llama 3.1 8B hyperfitted vs. 70B comparison (42.9% vs. 34.4%), but the introduction's unqualified wording should be calibrated to match the evidence.

### Minor

3. **Max dataset overlaps are notable even if rare.** The paper rightly emphasizes that "<2% of texts" have overlaps >10 tokens (line 135) and that average overlap is low. However, max overlaps of 37–40 tokens out of 96 generated (Table 2: DeepSeek and Llama 3.1 hyperfitted) mean some generations reproduce nearly half the sequence from training data. The paper acknowledges these outliers (lines 135–137) but could more prominently discuss their implications for practitioners deploying hyperfitted models without citation blocking.

4. **The Top-Rank Encouragement hypothesis (Section 6.3) is presented as a finding but has no direct empirical support.** The paper explicitly frames this as a hypothesis ("We hypothesize that…"), which is appropriate, but the section's positioning as a core contribution exceeds the evidence level. It would better serve as an explicitly labeled open question or future work direction.

### Trivial

None.

## Nice-to-Haves

- Report the breakdown of "preferred" vs. "equally good" ratings, and add confidence intervals to Table 1.
- Add a controlled comparison: hyperfitted models with nucleus sampling vs. hyperfitted with greedy decoding (to test whether hyperfitting and sampling are additive or redundant).
- A brief analysis of whether hyperfitting degrades factual accuracy or NLU benchmark performance would help practitioners assess trade-offs.

## Removed Points

These were flagged by reviewers but removed after verification against the paper, with brief justification:

- *"Random seed / selection procedure for 2000 sequences not specified"* → trivial implementation detail unlikely to affect reproducibility (Hard Rule: nitpick about reproducibility).
- *"Average of highest values metric needs more justification"* → paper provides justification in a footnote (footnote to Table 2).
- *"News-hyperfitted 77.2% result may be an annotation artifact"* → speculative; the paper notes the result is surprising and states "no clear trend emerges" (line 248).
- *"Top-Rank Encouragement lacks direct empirical support"* → paper explicitly calls it a hypothesis; this is an observation, not a weakness.
- *"Missing analysis of other task performance"* → outside the paper's stated scope (open-ended generation). Weakened to Nice-to-Have.
- *"Image generation quality too low"* → paper acknowledges this (line 266: "unimpressive compared to contemporary diffusion based models") and presents it as preliminary.
- *Generic strengths* (e.g., "addresses an important problem") from Strength Finder → lacked specific, concrete evidence anchors.

## Novel Insights

The shuffled-data experiment (Section 5.1) provides a genuinely insightful finding that goes beyond what the rest of the paper documents: training on identical data in different orders yields ~30% different top-1 predictions. This cleanly separates the role of the training process from the training content, showing that hyperfitting's effects are partially an emergent property of the optimization trajectory rather than purely data-driven. This is a non-obvious result with potential implications for understanding how LLMs internalize and sharpen pre-training knowledge.

## Suggestions

1. Add confidence intervals (bootstrapped would suffice) and inter-annotator agreement (Cohen's κ) to the human evaluation results.
2. Report the breakdown of "preferred" vs. "equally good" judgments separately in Table 1.
3. Calibrate the introduction's claim about "outperform[ing] models with 10x parameters" to match the body's more accurate "on par with" characterization for the TinyLlama vs. 70B comparison.
4. In the dataset overlap analysis, add a brief discussion of the max-overlap cases—even if rare, they are practically relevant for applications sensitive to memorization.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
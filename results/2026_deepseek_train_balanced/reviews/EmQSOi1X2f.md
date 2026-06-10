## Summary

This paper investigates self-contradictory hallucinations in LLMs — where a model generates two logically inconsistent sentences within the same context. It proposes a prompting-based pipeline with three components: (1) a trigger mechanism that generates a second sentence per original sentence via context-constrained cloze-style prompting (omitting the object from an extracted relation triple), (2) a CoT-based detector, and (3) an iterative mitigation procedure that revises flagged sentences to remove conflicting information. The framework operates solely through prompting, requires no external knowledge, and is applicable to black-box models. Experiments span four LLMs (GPT-4, ChatGPT, Llama, Vicuna-13B) and two tasks (open-domain text generation and QA).

## Strengths

- **Novel trigger mechanism via context-constrained resampling (Section 5.3)**: The idea of extracting a relation triple via CompactIE, then omitting the object from the prompt to create a controlled cloze test that constrains scope while leaving room for contradiction to arise is a non-trivial prompt-engineering insight. It goes beyond simple resampling and is shown to outperform baselines.

- **Empirical demonstration that self-contradictions fill a gap left by retrieval (Section 6.2)**: 35.2% of ChatGPT's self-contradictions cannot be verified using Wikipedia or web search. This directly supports the claim that the approach addresses cases retrieval-based methods miss.

- **High detection accuracy with strong inter-annotator agreement (Section 6.1)**: The detector achieves ~80% F1 across generator models, and the human-annotated ground truth has near-perfect agreement (Cohen's Kappa 88.9% and 82.7%), giving confidence in the evaluation numbers.

- **Demonstrated persistence of self-contradictions in retrieval-augmented QA (Section 6.3)**: 12.7–38.0% of answers contain self-contradictions even with retrieval augmentation (precision 74.2–83.8%). This shows the approach does not simply duplicate what retrieval already handles and provides a realistic use case.

- **Cost and efficiency quantification (Section 6.2)**: Concrete API token costs ($0.04 detection, $0.05 mitigation per description) and linear query scaling are reported, making practical deployability verifiable.

- **Ablation over analyzer models across proprietary/open-source divide**: The evaluation reveals that open-source models (Vicuna-13B, Llama) have substantially lower detection recall than proprietary ones, an honest limitation that informs practitioners.

## Weaknesses

### Fatal
None.

### Major

- **No mitigation baselines (Section 6.2)**: The detection component is compared against SelfCheckGPT, but the mitigation component has no baseline at all. Without comparisons against trivial alternatives — e.g., (a) simply deleting the contradictory sentence, (b) regenerating the full text from scratch with a revised instruction, (c) querying the model with a direct "fix contradictions" instruction — it is impossible to assess whether the iterative revision procedure adds value over simpler approaches. Deleting a contradictory sentence trivially removes 100% of the contradiction from that pair while guaranteeing no introduced errors from revision. The paper cannot claim its mitigation method is "effective" without showing it outperforms a non-trivial alternative. This is a structural gap in the evaluation that cannot be fixed by re-running existing analyses.

- **The informativeness metric does not support the claim that mitigation "maintains text informativeness" (Section 5, Evaluation Steps and Metrics)**: The paper defines: "When a sentence does not induce contradiction, we consider it as informative." This definition is circular — it defines informativeness as the absence of the very phenomenon being mitigated. After revision, any non-contradictory sentence is automatically scored as informative, even if it has been stripped down to a vacuous claim. The revision prompt instructs the LM to "remove the conflicting information," and the safest way to satisfy this is to eliminate all specific factual claims — yet this degradation would be invisible to the metric. Perplexity change is reported as a fluency proxy, but perplexity does not distinguish informative from vacuous content. Since the abstract and introduction state that mitigation "preserves informativeness" as a contribution, this claim is not properly supported. A proper measure (e.g., entity-relation triple density before/after revision, or human ratings of factuality) would be needed.

### Minor

- **The "17.7% prevalence" claim in the abstract conflates trigger rate with natural prevalence (Abstract vs. Section 5)**: The abstract states "in 17.7% of all sentences produced by ChatGPT" self-contradictions appear, which a reader naturally interprets as a property of the model's raw output. In fact, this is the rate achieved *after* running the trigger algorithm, which deliberately engineers a second sentence per original sentence by omitting the object from a relation triple — biased toward producing variability. The paper is transparent in the methodology section ("We calculate the frequency of self-contradictions: the ratio of sentences for which at least one self-contradiction is triggered"), but the abstract and introduction do not carry this caveat.

- **QA evaluation reports only precision, not recall (Section 6.3)**: Only positive predictions are manually annotated, so only precision can be computed. The paper cannot estimate how many self-contradictions the method misses in the QA setting. This limits the strength of the QA results.

- **Temperature asymmetry between proprietary and open-source analyzer models (Section 5, Sampling Temperature)**: ChatGPT/GPT-4 use temperature 0 for detection/mitigation, while Llama/Vicuna use temperature 1.0 (to avoid repetitive text). The paper notes this but does not discuss whether the performance gap between proprietary and open-source CLMs might partially reflect this confound rather than model capability alone.

- **Detection-mitigation evaluation loop lacks full specification of the human annotation protocol (Section 5)**: The mitigation uses the same detector to decide which sentences to revise, and human annotation serves as ground truth. But it is not specified whether human annotators re-evaluated the full revised output from scratch or only checked sentences the detector flagged. These two protocols would yield different results, and the ambiguity undermines reproducibility.

### Trivial

- No analysis of how failures in CompactIE (relation extraction) affect downstream pipeline performance. If the IE system misses relevant triples, the trigger might fail to generate a proper sentence pair, potentially causing false negatives in detection.

## Nice-to-Haves

- Adding a deletion baseline for mitigation would be the most impactful improvement: compare iterative revision against simply deleting contradictory sentences. If the revision retains more informative content than deletion at comparable contradiction removal rates, that would directly demonstrate the method's value.
- A proper informativeness metric (entity-relation triple density before/after revision, or human ratings of factuality) would strengthen the mitigation evaluation.
- Estimating recall in the QA setting (even through sampling-based annotation) would make the QA results more complete.

## Removed Points

These points were raised by reviewers but removed after verification against the paper:

- **Criticism that the "35.2% cannot be verified online" figure is problematic**: The harsh critic questioned how annotators determine contradiction if information can't be verified online. This misunderstands the paper: self-contradiction is defined logically (two sentences cannot both be true), and the 35.2% figure measures whether the contradictory information can be *resolved* via web search — not whether the contradiction itself can be detected. This is valid as written.

- **Criticism that "Our prompt significantly outperforms all baselines" is unverifiable**: The critic noted the baselines are in a stripped table. Per conference review policy, parser-stripped content (appendix tables and figures) exists in the original submission and should be assumed present.

- **Cost comparison with sampling-based methods**: The critic noted the paper's method also requires multiple samples (79x and 90x token cost), undercutting the contrast with sampling-based methods. The paper is transparent about its costs (Section 6.2), and the key distinction is that the method uses only 2 samples per sentence for detection — not "tens of samples" as required by SelfCheckGPT et al. — which the paper correctly states.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add at least one mitigation baseline (deletion of contradictory sentences is the most straightforward) to contextualize the 76.3–89.5% contradiction removal rates.
2. Redefine or supplement the informativeness metric to measure factual content preservation rather than absence of contradiction. Counting entity-relation triples before and after revision is a concrete, straightforward option.
3. Clarify in the abstract that the 17.7% figure is measured via a trigger mechanism, not raw output inspection.
4. Report recall (even estimated) for the QA experiments.
5. Specify the human annotation protocol for mitigation evaluation more precisely (full-text re-evaluation vs. flagged-sentence check).
6. Acknowledge the temperature confound explicitly when discussing the open-source vs. proprietary model performance gap.

## Score and Decision

The paper presents a genuinely novel core idea — using self-contradiction as a knowledge-free signal for hallucination detection and mitigation — and implements it through a well-specified prompting-based pipeline. The detection evaluation is solid, with strong human annotation quality and a demonstrated gap between what this approach catches and what retrieval-based methods can handle.

However, two structural weaknesses undercut the evaluation. The mitigation component has zero baselines, making it impossible to assess whether the elaborate iterative revision procedure adds value over trivial alternatives like sentence deletion. The informativeness metric is definitionally circular and cannot support the paper's claim that mitigation "preserves informativeness." At a top venue standard, these gaps are significant enough to prevent acceptance in the current form, though the core contribution is worth publishing with revisions.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
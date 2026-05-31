Now I have all the information needed. Let me construct the final review.

## Summary

This paper identifies and addresses three issues in LLM unlearning: (1) inadequate evaluation relying heavily on ROUGE-like metrics, addressed by proposing three new metrics (Token Entropy, Cosine Similarity, Entailment Score); (2) unpredictable/hallucinatory behavior in untargeted unlearning, addressed via a maximum-entropy (ME) objective that aligns the model with a uniform prediction distribution; and (3) insufficient regularization against excessive ignorance in targeted unlearning, addressed via an Answer Preservation (AP) loss. Experiments on TOFU, a novel continual unlearning extension, and real-world unlearning from Llama-3-8B show consistent improvements over strong baselines.

## Strengths

1. **New evaluation metrics (TE, CS, ES) capture distinct failure modes.** Section 2.2 formalizes token entropy for output diversity, cosine similarity via Sentence-BERT for semantic drift, and entailment score via an NLI model for factual correctness. Table 1 shows concrete examples where these metrics reveal degradation that ROUGE alone would miss (e.g., repeated tokens, hallucinated additions). The metrics are aggregated into MU and FE for unified comparison throughout the paper.

2. **Maximum-entropy (ME) objective for untargeted unlearning is principled and data-agnostic.** Section 3 identifies that existing untargeted methods approximate an unpredictable retain model that can hallucinate (Section 3.1: the surrogate retain model's ROUGE on the forget set is only 0.4082, with 74% of outputs hallucinated). The proposed ME loss (Eq. 8) aligns with a uniform next-token distribution — a well-defined, data-independent target. Figure 4 shows ME+GD achieves the highest FE while maintaining stable MU across all TOFU tasks, unlike baselines that either collapse MU (GA+GD) or plateau at low FE (NPO+GD).

3. **Answer Preservation (AP) loss effectively addresses excessive ignorance in targeted unlearning.** Section 4 identifies that targeted methods cause the model to output rejection templates on the retain set because of distributional similarity between forget and retain sets (Figure 2b shows ROUGE on both sets dropping together). The AP loss (Eq. 9) adaptively penalizes rejection-template probability while preserving original-answer probability, with gradient analysis (Eq. 10) showing the adaptive weight mechanism. Results (Figure 4; Table 2) show IDK+AP is the only targeted method that maintains stable MU across all TOFU tasks and achieves the highest MU (0.5311) in the real-world scenario, while baselines collapse to MU=0.000.

4. **Clear categorization of unlearning methods into untargeted and targeted.** Section 2.3 and Figure 1 distinguish methods by whether the forget-set output is specified. This framework organizes a fragmented literature, directly motivates the paper's two proposed approaches, and is used consistently in all experiments.

5. **Novel continual unlearning scenario for LLMs.** Section 5.2 extends TOFU to sequential unlearning (up to 10 subtasks). The paper shows that existing methods collapse while ME+GD and IDK+AP maintain much higher MU (Figure 5). This is a novel evaluation setting not present in prior work.

6. **Real-world evaluation on Llama-3-8B-Instruct with downstream tasks.** Section 5.3 uses real individuals with deep memorization and evaluates on five standard benchmarks. Table 2 shows ME+GD preserves high MU (0.4901 vs. initial 0.6145) and FE (0.9312) while maintaining downstream performance (Avg. 0.5294 vs. initial 0.5662), demonstrating practical viability.

7. **Insightful failure analysis of NPO in continual unlearning.** Section 5.2 (final paragraph) discovers that NPO's collapse stems from the reference model shifting to the previous unlearned model. A controlled experiment fixing the reference to the initial model (Figure 6c) stabilizes MU, proving the cause — a principled takeaway that also highlights the advantage of the proposed methods' reference-model-free design.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Typo in the GD and KL regularization equations.** Equations (4) and (5) (labeled eq:GD and eq:KL) compute the expectation over \(\mathcal{D}_{\text{F}}\) (the forget set), but the text describes them as operating on the retain set \(\mathcal{D}_{\text{R}}\), consistent with their role as regularization losses. The loss argument correctly reads \(\mathcal{D}_{\text{R}}\), so the expectation subscript should be \(\mathcal{D}_{\text{R}}\), not \(\mathcal{D}_{\text{F}}\). This is a clear copy-paste error that would confuse reproducibility efforts if uncorrected.

2. **The claim that prior work "primarily rely[ies] on ROUGE as the sole metric" is overstated.** The paper itself cites TOFU (Maini et al. 2024), which uses ROUGE, Probability, and Truth Ratio — three metrics. While ROUGE may be the primary *output-text* metric while the others are probability-based, the statement as written in the abstract and introduction (line 19) oversimplifies the evaluation landscape. This does not undermine the paper's contribution (the three new metrics are independently valuable) but should be softened for precision.

3. **No ablation of whether entropy maximization over the question part is necessary.** Line 189 notes that the ME loss is applied to both question and answer tokens, following prior work, but the paper provides no ablation comparing this to answer-only entropy maximization. If the simpler variant works equally well, it would be less intrusive and easier to deploy.

4. **Lack of statistical significance / error bars.** All results are reported from single runs without variance estimates. While single-run evaluation is common in large-scale LLM benchmarks, the real-world scenario (Section 5.3) uses a smaller dataset where reporting at least 3 seeds with standard deviations would increase confidence in the reported rankings.

### Trivial

- The definition of the retain set on line 36 ("we also use the retain set \(\mathcal{D}_{\text{R}}\) to refer to the neighbor set... unless specified") could benefit from a forward reference to the TOFU-specific evaluation (which aggregates across neighbor set, Real Authors, and World Facts). This is clarified later but the explanation is slightly deferred.
- The cosine similarity truncation description (line 85: "truncate the value less than 0") could explicitly note that Sentence-BERT cosine similarity ranges [-1,1] but negative values are rare for semantically related outputs, justifying the truncation.

## Nice-to-Haves

- **Compare AP loss against a simpler baseline** that directly penalizes IDK-template probabilities on the retain set (e.g., adding \(-\log(1-p(y'|x))\)). This would isolate whether the adaptive weighting in AP is the key ingredient or whether any explicit discouragement of rejection templates suffices.
- **Provide a systematic validation of the new metrics** (TE, CS, ES) — e.g., a correlation analysis with human judgments on a small sample, or a demonstration that they track distinct failure modes that ROUGE/Probability/TR miss. The qualitative examples in Table 1 are helpful, but empirical validation would strengthen the claim.
- **Show IDK-template probability on the retain set over time** (complementing Figure 2b) to directly confirm the hypothesized mechanism that targeted unlearning increases \(\Pr(\mathcal{Y}_{\text{IDK}}|\mathcal{X}_{\text{R}})\).

## Removed Points

These points were raised by reviewers but are removed or downgraded per the filtering guidelines. **Treat them with caution** — they may reflect reviewer speculation or misunderstandings.

- **Hyperparameters not reported in main text** (harsh critic): Hyperparameters (learning rates, α, β, epochs) are standardly deferred to appendices in ML papers. The appendix, like all submissions at this venue, is stripped by the parser — these details exist in the original submission.
- **"Missing ablations comparison to a simpler baseline" presented as a weakness** (harsh critic): The suggestion to compare AP loss against a simpler GD+IDK-penalty baseline is framed as a methodological gap. This is a constructive suggestion (moved to Nice-to-Haves) rather than a genuine weakness, as the paper already shows AP loss outperforms seven strong baselines.
- **Strength Finder strengths considered generic/superficial**: All seven strengths listed above are concrete, specific to the paper, and supported by evidence. None were removed.
- **Criticism about "models not yet released" / reproducibility concerns**: No such criticisms appeared in the inputs.

## Novel Insights

None beyond the paper's own contributions. The reviewers' analyses are consistent with and derivative of the paper's own framing.

## Suggestions

1. Fix the typo in Eqs. (4) and (5): replace \(\mathbb{E}_{(x,y) \sim \mathcal{D}_{\text{F}}}\) with \(\mathbb{E}_{(x,y) \sim \mathcal{D}_{\text{R}}}\) in both equations.
2. Soften the ROUGE-sole-metric claim in the abstract and introduction (e.g., "many prior studies rely primarily on ROUGE as the main output-evaluation metric, often supplemented by probability-based metrics").
3. Add a brief ablation of ME loss with question-part inclusion vs. answer-only to the appendix.
4. Add error bars (at least 3 seeds) for the real-world scenario.
5. Optionally, add a sentence to the CS definition noting that Sentence-BERT cosine similarity on normalized embeddings typically yields non-negative values.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>
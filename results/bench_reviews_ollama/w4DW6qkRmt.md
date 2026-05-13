Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

SuRe (Summarized Retrieval) is a zero-shot prompting framework for open-domain QA that generates K answer candidates, then conditionally summarizes retrieved passages for each candidate, and selects the best answer by combining instance-wise validity scoring and pairwise ranking of summaries. The method requires no fine-tuning and operates purely through prompting, making it applicable to black-box LLM APIs. Experiments across four ODQA datasets, three LLMs (ChatGPT, GPT-4, LLaMA2-chat), and three retrieval methods show consistent EM improvements of up to 4.6% over standard prompting baselines, with additional benefits for passage reranking and rationale quality.

## Strengths

- **Consistent improvements across diverse LLMs and retrievers without fine-tuning**: Table 2 demonstrates that SuRe improves average EM by 4.6% across 9 LLM×retriever combinations, with the strongest gains on LLaMA2-chat (7.9%), directly supporting the claim of broad applicability. The method requires only prompting-based access, making it practical for black-box APIs.

- **Conditional summarization is validated as the key mechanism**: The ablation in Table 3 shows "+ Conditional summarizations" substantially outperforms "Sum-and-pred (Gen)" (generic summarization), isolating the benefit of conditioning. Figure 2/TF-IDF analysis confirms that conditional summaries have higher overlap with their corresponding candidate than the other candidate, providing mechanistic evidence.

- **Both validity and ranking contribute complementarily**: Table 3 shows adding instance-wise validity on top of pair-wise ranking yields a clear improvement (e.g., 31.2→31.8 EM on NQ*), confirming both scoring components are useful as claimed in Equation 6.

- **Additional utility beyond answer accuracy**: Table 4 and Figures 3b/3c show SuRe's summaries improve passage reranking and are preferred by both GPT-4 (37.4% vs. 30.3%) and human evaluators (43.4% vs. 26.9%) over generic summarization as rationales, with controlled lengths.

## Weaknesses

### Fatal
None.

### Major

- **Compute asymmetry not addressed**: SuRe uses substantially more LLM calls per question than the primary "Base" baseline (1 call for candidate generation + K for summarization + K for validity + K(K−1) for pairwise ranking with position-bias mitigation). The paper does not report the value of K or total calls per question, making it impossible for readers to assess the cost-accuracy tradeoff. More importantly, no compute-matched baseline (e.g., majority voting with an equivalent number of LLM calls) is provided, leaving open the possibility that some portion of the improvement stems from brute-force compute scaling rather than SuRe's specific mechanism. The ablation in Table 3 partially mitigates this by showing conditional summarization outperforms generic summarization, but the comparison against the simplest "Base" baseline remains unfair in compute terms. This does not invalidate SuRe's contribution but limits how confidently the gains can be attributed to the proposed mechanism.

- **Self-referential validity evaluation**: Equation 4 uses the same LLM 𝓜 to generate summaries and then evaluate their validity, creating a circular evaluation loop. LLM self-evaluation for factual consistency is known to be unreliable. The paper does not analyze how often the validity filter correctly identifies incorrect candidates. While the ablation shows adding validity improves over ranking alone, the magnitude of this improvement could be inflated by self-bias. This is partially addressed by the fact that pairwise ranking (Equation 5) provides an independent relative comparison mechanism, but the validity component remains self-referential.

### Minor

- **Key hyperparameter K not specified**: K (number of answer candidates) directly governs computational cost and the granularity of conditional summarization, yet the paper never reports the value of K used in main experiments. The TF-IDF figure uses K=2, but the actual K for Tables 1–2 is unclear. This hampers reproducibility and prevents readers from understanding the cost-performance tradeoff.

- **Validity and ranking scales are not truly "equally" weighted**: Equation 6 claims validity v(s_k)∈{0,1} and ranking r(s_k,S_K)∈[0,K−1] contribute "equally," but for K≥3, the ranking score range exceeds validity's range, making ranking inherently more influential. For K=3, ranking ranges 0–2 versus validity's 0–1. The claim of equal contribution is misleading unless K=2 or a normalization is applied.

- **LLaMA2-chat experiments use only 500 subsampled examples**: NQ* and WebQ* (Table 2) use 500 randomly selected examples without reporting variance, confidence intervals, or statistical significance. Given the absolute EM improvements are in the 1–8% range, reliability on small samples is a concern.

- **GPT-4 used both as evaluated model and as preference judge**: In Figure 3b, GPT-4 evaluates rationale preference for outputs that include GPT-4's own predictions, potentially introducing self-bias. The human evaluation (Figure 3c, 84 samples, no inter-annotator agreement) partially addresses this but is small-scale.

### Trivial
None.

## Nice-to-Haves

- Report K values and total LLM calls per question for transparency on cost-performance tradeoffs.
- Add a compute-matched baseline (e.g., self-consistency with majority voting at equivalent API call budget) to isolate the mechanism's contribution from raw compute.
- Analyze contradiction rates in pairwise ranking when positions are reversed, to validate the position-bias mitigation.
- Report performance conditioned on whether the correct answer appears among the K generated candidates, to clarify how much SuRe helps beyond candidate generation.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Prompts not provided"**: The harsh critic flagged the absence of prompt templates (p_can, p_sum, p_val, p_rank) as a significant reproducibility gap. While prompts are important in a prompting method, this falls under the category of implementation details that are impractical to include fully in a submission. The algorithm and equations clearly specify what each prompt does. Removed as a reproducibility nitpick.

- **"Claim about explicit prompting vs. stochastic decoding unsupported"**: The paper states (line 117) that "we empirically observe that explicitly prompting an LLM to generate K potential candidates outputs more diverse and high-quality candidates" compared to stochastic decoding. The harsh critic called this unsupported, but it is explicitly described as an empirical observation and is a design choice justification, not a core claim. Removed as a scope-creep criticism.

- **"Position bias contradiction rate unreported"**: The paper addresses position bias by querying each pair twice with reversed order, which is a reasonable mitigation. Demanding analysis of contradiction rates is a nice-to-have, not a weakness. Removed to nice-to-haves.

- **"Subsampled datasets lack variance/statistical significance"**: This was moved to minor since it's a valid concern about reliability but is standard practice in many LLM evaluation papers. The broader concern about statistical significance across all experiments was weakened accordingly.

- **"Self-verification baseline has sparse implementation details"**: This is an implementation detail of a baseline, not the proposed method. Removed.

- **"Comparison with fine-tuned methods claimed but not conducted"**: The introduction mentions fine-tuned methods as motivation for the prompting approach, not as a direct comparison target. The paper scopes itself to prompting methods for black-box APIs. Removed as scope creep.

- **Strength finder claim "robustness to varying N"**: While true, this is fairly standard and expected behavior. Kept as supporting evidence but not elevated to a top-level strength.

## Novel Insights

The most interesting observation from the reviews is that SuRe's gains could arise partly from a compute-scaling effect rather than purely from its conditional summarization mechanism. The ablation partially disentangles this—conditional summarization outperforms generic summarization even when both have similar LLM call counts—but a proper compute-matched baseline would decisively settle this question. The interaction between K, compute, and accuracy is the key axis readers should evaluate. Additionally, the self-referential nature of validity scoring (Equation 4) is a design tension that the community should think about: is LLM self-judgment of factuality reliable enough for this purpose, or should an external verification signal be preferred?

## Suggestions

- Report the value of K and total API calls per question in all experiment tables, and ideally provide a Pareto curve of accuracy vs. compute for varying K.
- Add a compute-matched majority-voting baseline to the comparison tables, especially against Base, to enable fair attribution of improvements.
- If possible, normalize the validity and ranking scores (e.g., divide v by 1 and r by K−1) so they contribute equally on a [0,1] scale, or justify the current weighting with an ablation.

## Score and Decision

This paper presents a clean, well-motivated prompting framework with consistent empirical gains across diverse settings, and the conditional summarization mechanism is a genuine contribution. However, the central comparison (SuRe vs. Base) has an unaddressed compute asymmetry, and the self-referential validity scoring is a methodological concern. The absence of the key hyperparameter K's value further limits the reader's ability to evaluate cost-effectiveness. These issues are substantive but not fatal—the method works and the ablations provide mechanistic insight. The paper would be significantly strengthened by compute-matched baselines and full specification of K.

**Originality**: The idea of candidate-conditioned summarization for ODQA is novel and well-conceived. The dual verification (validity + ranking) via prompting is a clean contribution.

**Importance**: Improving zero-shot ODQA for black-box LLMs is a practically important problem. The additional reranking and rationale benefits add practical value.

**Claim support**: The headline 4.6% EM improvement is supported but confounded by compute asymmetry. Ablations partially but not fully isolate the mechanism.

**Experimental soundness**: Experiments are reasonably comprehensive (4 datasets, 3 LLMs, 3 retrievers) but lack compute-matched controls and statistical significance measures.

**Clarity**: The paper is clearly written and well-structured. The method is easy to understand.

**Community value**: The approach is practical for black-box API users and the framework could be extended.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
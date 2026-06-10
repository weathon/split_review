## Summary

This paper introduces DelTA, an LLM-based document-level translation agent with a multi-level memory architecture comprising Proper Noun Records, Bilingual Summaries, Long-Term Memory, and Short-Term Memory. The system translates documents sentence-by-sentence while continuously retrieving and updating these memory components. Experiments across four LLMs (two open-source, two closed-source), eight translation directions, and two datasets show consistent improvements in both translation consistency (LTCR-1) and quality (COMET) over sentence-level, context-window, and Doc2Doc baselines.

## Strengths

- **Well-motivated and cleanly designed multi-level memory architecture**: The four memory components (Proper Noun Records, Bilingual Summary, Long-Term Memory, Short-Term Memory) are each designed to address a specific failure mode in document-level translation. The architecture is clearly described and the interaction between retrieval and translation is well-specified (Algorithm 1, Figure 1). This is the paper's genuine core contribution.

- **Consistent improvements across a broad evaluation grid**: DelTA outperforms all baselines on consistency (LTCR-1, LTCR-1_f) and quality (sCOMET, dCOMET) across 4 LLMs × 8 translation directions × 2 datasets. The ablation study (Table 4) traces the contribution of each component, with Proper Noun Records alone adding 3.95 LTCR-1 points. This breadth of settings provides substantially more evidence than a narrower evaluation would.

- **Principled motivation for the sentence-by-sentence approach**: The preliminary experiment (Table 1) clearly demonstrates the trade-off between window size and sentence omission risk (window size 50 achieves highest LTCR-1 but drops 10 sentences). The memory-cost comparison (Figure 2) shows DelTA avoids the OOM failure mode of Doc2Doc methods. These practical considerations are important for real deployment.

- **New LTCR-1 metric**: The proposed metric improves upon the existing LTCR by requiring consistency with the *first* translation of each proper noun, which better reflects reader experience. The fuzzy-match variant (LTCR-1_f) mitigates alignment-tool noise.

## Weaknesses

### Fatal
None.

### Major

1. **No variance or significance reporting on any quantitative result**: Every score in every table is a point estimate with no standard deviation, confidence interval, or significance test. The IWSLT2017 test set contains only 10–12 documents (~1.5K sentences) per language pair. Many reported improvements are small (e.g., 0.78 sCOMET points for GPT-3.5-Turbo En→Xx, 85.58 vs. 84.80). Without any measure of variability across documents, the reader cannot assess whether these gains reflect genuine improvement or noise. This is the most consequential weakness in the evaluation. *Verifiable: all tables in Sections 5–6 report only point estimates; grep for "standard deviation", "confidence", "variance", "bootstrap", "p-value" returns zero matches.*

2. **Ablation study reveals non-monotonic component interactions that go unanalyzed**: In Table 4, adding Short-Term Memory alone (Model 2) *decreases* LTCR-1 from 80.27 to 77.89, and adding Long-Term Memory (Model 3) only partially recovers to 79.23 — still below the sentence-level baseline. Adding Source Summary alone (Model 4) drops LTCR-1 further to 76.09. These intermediate configurations are worse than doing nothing, which is counterintuitive and potentially the most interesting finding in the study (it suggests components interact synergistically only in the full combination). The paper dismisses these as "no significant enhancement" without analysis or even acknowledgment of the negative direction. The claim that "each component contributes" is not accurate for these intermediate steps.

### Minor

3. **Pronoun translation analysis is too thin to support the claim**: Evaluated on only one direction (En→Zh), one model (GPT-3.5-Turbo), one metric (APT), with a 1.1 percentage point improvement over Context (61.07 vs. 60.84). No breakdown by pronoun type, no human verification, no analysis of cases where DelTA might worsen pronoun translation. The paper claims the memory "is beneficial to resolving coreference and anaphora" but the evidence does not support such a broad conclusion.

4. **Baseline asymmetry between Sentence and DelTA**: The Sentence baseline uses a bare instruction with no in-context examples. DelTA provides the translator with proper noun records (as bullet points), up to 2 retrieved Long-Term Memory sentences (as few-shot exemplars), 3 Short-Term Memory context sentences, and bilingual summaries. While the Context baseline (3 preceding sentence pairs) partially addresses this, the fairest comparison would control for the *quantity* of contextual input (e.g., giving Sentence/Context the same 5 total sentence pairs DelTA uses). The ablation study repair is partial: Model 2 (Sentence + STM = 3 preceding sentences) gets roughly the Context baseline's input and still shows *worse* LTCR-1 than Sentence alone, which is puzzling and suggests the comparison is less clean than claimed.

5. **Guofeng dataset is under-described**: The paper states only "Guofeng V1 TEST_2 set in the Zh→En direction" with no description of document count, sentence count, domain, or source. The results on this dataset are the most dramatic (up to 48.50 pp LTCR-1 improvement), but the lack of detail makes these results hard to interpret. *Verifiable: line 299 is the only description of this dataset.*

6. **No limitations section**: The paper has no discussion of failure modes, when components might hurt, error propagation in Proper Noun Records, dependence on spaCy NER quality, or conditions under which the method would break down. This is a notable omission for a methods paper.

### Trivial

7. **Variable name inconsistency**: In Section 4, the Memory Retriever is asked to choose "$n$ source sentences" (line 188), but the following sentence refers to "These $m$ sentences" (line 189). The intended variable ($n$) is clear, but this is a copy-editing error.

## Nice-to-Haves

- **Token cost and latency analysis**: DelTA adds multiple LLM calls per sentence (Proper Noun Extractor, Memory Retriever, periodic Summary Writers and Mergers). Quantifying the overhead in tokens and wall-clock time relative to baselines would be valuable for practitioners. The memory-cost comparison (Figure 2) is appreciated but API/latency cost is arguably more important for deployment decisions.
- **Error analysis**: A qualitative examination of what errors DelTA still makes — e.g., cases where Proper Noun Records propagate an incorrect initial translation, or where the Bilingual Summary loses information — would strengthen the paper.
- **Human evaluation focused on proper noun consistency**: Given the paper's central claim is about translation consistency, a targeted human evaluation (even 100–200 examples) would validate whether LTCR-1 improvements translate to actual reader experience.

## Removed Points

The following points from the input reviews were filtered per policy:
- **Criticism about averaging across backbone models in the "Average" row**: This is a standard presentation practice; per-model results are fully visible. Not a substantive weakness.
- **Criticism that Doc2Doc window size "wasn't tuned"**: Speculative — there's no evidence the reported window is suboptimal.
- **Criticism about memory cost comparison being "architecturally inevitable"**: While structurally predictable, the empirical quantification (Figure 2) is still a useful contribution.
- **Generic concerns about missing baselines or alternative approaches not within the paper's stated scope**: The paper clearly scopes to DocMT-LLM methods; criticizing absence of other paradigms is scope creep.
- **Claim that "no human evaluation" is severe**: For LLM-based MT at top venues, COMET (a trained metric with human-judgment correlation) is standard; this is a nice-to-have, not a core weakness.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Report per-document standard deviations or confidence intervals (via bootstrap) for all main results and ablation experiments. This single change would substantially increase confidence in the claims.
2. Add an analysis of the non-monotonic behavior in the ablation study (Models 2–4). Why does adding context mechanisms initially hurt consistency? Understanding this interaction would strengthen the paper's core argument.
3. Provide a proper description of the Guofeng dataset (size, domain, source) and add a note about how to access it.
4. Include a limitations paragraph acknowledging potential failure modes (error propagation in records, LLM call overhead, NER dependency).
5. Expand the pronoun analysis to at least one additional direction or language pair to support the claim that the memory aids coreference resolution.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
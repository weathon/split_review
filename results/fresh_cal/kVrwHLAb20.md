Now I have all the information I need. Let me construct the final consolidated review.

---

## Summary

This paper formalizes the novel problem of black-box RAG Dataset Inference (RAG-DI), where a data owner aims to detect unauthorized inclusion of their dataset in a RAG system's corpus. It introduces FARAD, a synthetic dataset that models fact redundancy (a key real-world confound absent from prior datasets), establishes baseline methods adapted from RAG membership inference attacks, and proposes Ward, a proactive method that embeds LLM watermarks into documents and aggregates weak watermark signals across multiple RAG responses via joint p-values to obtain statistical guarantees. Empirically, Ward achieves perfect accuracy (100%) across diverse settings where all baselines fail, and maintains this under system prompt defenses and MemFree decoding.

## Strengths

- **First formalization of RAG Dataset Inference (RAG-DI).** The paper provides a clean, rigorous problem definition (Section 3): a data owner makes a single dataset-level decision under black-box query access, distinguishing this from document-level membership inference. This establishes a foundation for future work.

- **FARAD dataset addresses key confounds.** Unlike prior datasets (EnronEmails, HealthcareMagic), FARAD uses fictional articles from RepliQA that are provably absent from LLM training data, and explicitly models fact redundancy via groups of articles sharing key facts written by different author LLMs (Section 3.1). This directly enables evaluation under the realistic condition that makes the problem hard, as the paper demonstrates empirically.

- **Ward provides rigorous statistical guarantees via joint watermark detection.** By embedding red-green watermarks and computing a joint p-value across multiple responses (Equation 3, Section 4), Ward is the only method that can provably control Type I error. The mathematical derivation in Equation (2) shows how even a weak per-response signal (~1% green token increase) becomes detectable with ~100 queries, and this is validated with p-values orders of magnitude from the decision boundary (Table 1).

- **Empirical dominance across challenging settings is clear and reproducible.** In the main experiment (Figure 1), Ward achieves 100% accuracy across all three LLMs (Claude 3 Haiku, GPT-3.5, Llama3.1-70b), both easy and hard fact-redundancy settings, and both naive and defended system prompts — while every baseline (Facts, SIB, IBM) fails in the hard setting, often with both false positives and false negatives. Results are reported with 5 random seeds.

- **Robustness to active defenses is validated.** Ward maintains perfect accuracy under a defended system prompt that explicitly instructs the model not to answer document queries (Section 5.2) and under MemFree decoding that prevents n-gram overlap (appendix), settings that degrade all baselines.

- **Practical validation with imperfect retrieval.** An end-to-end experiment using OpenAI text-embedding-3-large (93.6% retrieval success) confirms Ward achieves 100% accuracy beyond the idealized perfect-retrieval setup (Section 5.3, Figure 6).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Question generation procedure for Ward is underspecified.** The paper states that for each document $d_i$, Ward "generates an open-ended content-related question $q_i$" (line 184) and acknowledges the risk of signal leakage from using watermarked queries (lines 215-218), but never specifies: (a) what LLM generates these questions, (b) whether that LLM is itself watermarked, and (c) whether questions are generated from original or watermarked documents. For Facts, the paper at least specifies an "auxiliary LLM" (line 161); for Ward, no model is named. The empirical calibration evidence (outcase p-values well-distributed) is reassuring and suggests the implementation avoids leakage, but the lack of specificity is a reproducibility gap that should be closed.

- **End-to-end retrieval validation is limited to one retriever and one LLM.** The imperfect retrieval experiment (Section 5.3) uses only OpenAI text-embedding-3-large with Llama3.1-70b. Since retrieval effectiveness directly controls whether watermarked text enters the LLM context, the paper would be stronger with evidence across at least one additional retriever (e.g., BM25, a smaller embedding model) or across varying retrieval success rates. This limits confidence about how Ward degrades under less reliable retrieval.

- **No discussion of computational cost in the main text.** Ward requires generating one (or more) questions per document and running the watermark detector across all responses. The paper does not report query volume, API costs, or the overhead of question generation, which matters for practical deployment assessment.

### Trivial

- The paper notes the MemFree defense experiment is in the appendix (line 407-409); including a brief summary of those results in the main text would be more informative.
- The threshold used for baseline aggregation (average of in/out training scores) is described as "empirically optimal" but without comparison to other aggregation schemes; this is a small methodological detail.

## Nice-to-Haves

- A systematic study of Ward's accuracy as a function of retrieval success rate (e.g., by varying k, using a weaker retriever, or corrupting retrieved documents) would better characterize the method's operating regime.
- A brief exploration of partial dataset inclusion rates (fraction of owner's dataset in the corpus) beyond what is in the appendix would strengthen the robustness characterization.
- The paper could briefly discuss whether documents must be re-watermarked for each RAG system they protect, and how the secret salt is managed across deployments.

## Removed Points

- **Asymmetry in baseline comparison (proactive vs. passive).** The harsh critic argues that comparing a proactive method (Ward) to passive baselines is unfair and overstates the evidence. This is removed because: (1) the paper explicitly labels Ward as proactive (line 178) and the baselines as passive adaptations of prior MIA work; (2) the contribution is the watermarking approach itself — the comparison shows that existing passive methods fail at RAG-DI, which is a factual finding, not a framing error; (3) the suggestion to add a separate proactive baseline (random perturbations, steganography) asks the paper to solve a different comparison problem than the one it sets out. This is scope creep, not a valid weakness.

- **Threshold choices for baselines may be suboptimal.** The suggestion that the "empirically optimal" threshold should be compared with a trained logistic regressor is overly specific for a baseline aggregation method that serves primarily to establish that passive methods fail under fact redundancy. The paper's threshold choice is standard and reasonable.

- **SIB monotonicity could benefit from alternative aggregation.** This is a suggestion for improving a baseline, not a weakness of the paper. The paper's purpose is to evaluate SIB as-is in the RAG-DI setting.

- **Generic concerns about "the paper would be strengthened by" (more datasets, more models, more ablations).** These are standard aspirational comments applicable to any paper and do not identify actual flaws.

- **"MemFree defense experiment is only mentioned in the appendix."** This is a presentational note, not a weakness. The experiment is described in the appendix and its existence is correctly cited.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converge on the paper's core strengths and raise standard concerns about specificity and scope limitations; no novel analytical insight emerges from synthesizing them.

## Suggestions

1. **Specify the question generation procedure for Ward in full** — name the LLM used, state whether it carries a watermark, clarify whether questions are generated from original or watermarked documents, and either include the prompt template or reference the appendix where it resides. This is the single most actionable fix.

2. **Add at least one additional retriever** (e.g., BM25, a sentence-transformer model) to the imperfect retrieval experiment, or systematically vary retrieval success probability to map out Ward's degradation curve.

3. **Include a brief cost analysis** — approximate number of queries needed for reliable detection (already partially present in Figure 4) and rough API cost at current pricing.

## Score and Decision

This is a strong paper. It opens a new problem (RAG-DI), provides the infrastructure to study it (formalization, dataset, baselines), and proposes a method (Ward) that works extremely well across diverse settings. The core claims — that Ward provides provable detection, outperforms passive baselines, and is robust to defenses — are well-supported by the evidence. The main issues are a missing procedural detail (question generation) and a limited scope of one validation experiment, both addressable in a revision.

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>
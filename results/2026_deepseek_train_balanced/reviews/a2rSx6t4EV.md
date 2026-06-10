## Summary

This paper proposes EDU-RAG, a benchmark for evaluating Retrieval-Augmented Generation (RAG) in the education domain, constructed by augmenting 1,255 multiple-choice science questions from the TQA dataset with web search results (top-10 Google URLs per question, crawled and sentence-split). Three models (GPT-4o, Llama2-7b, Llama3-8b) are evaluated with and without RAG, reporting accuracy, miss rate, hallucination rate, and a composite score that penalizes wrong answers. The paper identifies a real gap — existing comprehensive RAG benchmarks like CRAG lack an education domain — but the execution is too preliminary to constitute a publishable benchmark contribution for a top venue.

## Strengths

- **Addresses a genuinely missing domain in existing RAG benchmarks.** The paper explicitly identifies that CRAG (Yang et al., 2024) "only includes five domains: Finance, Music, Movie, Sports, and Open, and it does not include the Education domain" (Section 1, line 18). Education is a high-impact application area for RAG (AI tutors), and the paper provides a concrete starting point for filling this gap.

- **Demonstrates substantial RAG-driven improvement for a smaller/older model.** Llama2-7b accuracy improved from 25.34% (barely above random chance for 4-choice questions) to 52.03% with RAG (Section 4.4, line 126) — a >100% relative improvement. This provides a meaningful quantitative result for practitioners considering cost-effective models in education QA.

- **Evaluation across multiple model families and sizes.** The paper tests Llama2-7b, Llama3-8b, and GPT-4o under controlled decoding conditions (max_new_tokens=1, do_sample=False), providing comparative evidence that RAG benefits models at different scales (Section 4.3, line 120-122).

- **Principled scoring design motivated by education use cases.** The scoring metric penalizes wrong answers (−1) while treating missing/refused answers as neutral (0), following CRAG conventions (Section 4.2, Equations). This is appropriately motivated by the education setting where providing incorrect information to students is worse than declining to answer.

## Weaknesses

### Major

- **No static dataset artifact — the benchmark is not reproducible as a fixed resource.** The paper's primary contribution is a benchmark, yet there is no mention of releasing the crawled web content as a static, versioned corpus. Web search results are temporally unstable: the same Google query will yield different results over time. The QA pairs from TQA are static, but the web-enhanced content — the paper's novel addition — is a time-dependent pipeline description rather than a fixed dataset. Future researchers cannot reliably compare against this benchmark without a released snapshot. This is the most significant gap for a benchmark paper. (Section 3.1, lines 60-68)

- **The "Analysis" section contains no actual analysis.** Section 5 (lines 140-148) poses RQ1 ("Is this a valid benchmark?") and answers with a circular tautology: "Yes, this is a valid benchmark because the initial results successfully demonstrated that the dataset is valid." There is no investigation of retrieval quality, error patterns, question difficulty distribution, or correlation between retrieval relevance and accuracy. For a paper whose core claim is introducing a benchmark, the absence of meaningful validation analysis is a major weakness.

- **No retrieval quality characterization.** The paper reports accuracy improvements but never measures what fraction of retrieved sentences actually contain the correct answer. This makes it impossible to interpret whether RAG helped because the model could extract the answer from retrieved context, or because the model benefited from topic-relevant background information, or even despite poor retrieval. Without retrieval quality analysis, the paper's core claim about RAG effectiveness is unsubstantiated. (Section 4.4; no retrieval quality metrics reported anywhere)

- **No dataset release plan, license, or access information.** A benchmark paper submitted to a top venue should state where and under what terms the dataset will be made available. The paper does not mention a release URL, license, or archival plan. The authors state "we have the dataset in csv" (line 62) and "we have already obtained a larger benchmark dataset" (line 166) but do not explain how the community will access it.

- **Sampling methodology for the 1,255 QA pairs is unspecified.** The paper says "we tested different models on a sample of 1,255 TQA question-answer pairs" (Section 4.1, line 94) but does not state whether this is the full TQA science subset or a sample, how the sample was selected, what subjects (Life Science, Earth Science, Physical Science) are represented in what proportions, or the original TQA train/validation/test split used. This makes it impossible to assess the benchmark's coverage or potential selection bias.

### Minor

- **"Hallucination" is imprecisely measured.** The paper defines hallucination rate as the percentage of incorrect multiple-choice answers (Section 4.2, lines 103-108). In the RAG literature, hallucination more commonly refers to generated content that contradicts or fabricates information — which is not directly observable when the model outputs a single token with max_new_tokens=1. The paper follows CRAG conventions in its scoring, which mitigates this, but the claim in the abstract and conclusion that RAG "helps reduce hallucination" is broader than the measurement supports. The authors should either use a more precise term (e.g., "error rate") or measure hallucination in the standard sense (e.g., whether the model's output contradicts retrieved context when the context contains the correct answer).

- **Results for GPT-4o and Llama3-8b are numerically underreported in the text.** Only the Llama2-7b accuracy figures (25.34% → 52.03%) are stated in the body (line 126). The other models' accuracy, hallucination, and miss rates appear only in tables that are rendered as raster images in the extracted text. While the tables likely exist properly in the original PDF, the paper should report key figures for all models in the body text for accessibility.

- **No statistical significance or variance measures.** With deterministic decoding and one run per condition, there is no estimate of variance, confidence intervals, or significance testing. For a benchmark that measures percentages on 1,255 samples, this is a gap that limits the reliability of claimed improvements.

- **Sentence-level retrieval strategy is not motivated or ablated.** The retriever splits web content into individual sentences and retrieves top-K by Sentence-BERT similarity (Section 3.2, lines 76-78). Many middle-school science questions require multi-sentence reasoning that sentence-level retrieval would fragment. The paper provides no evidence that this design choice is appropriate, nor does it ablate alternatives (e.g., passage-level retrieval, different K values).

- **No comparison with existing RAG benchmarks beyond domain coverage.** The paper notes that CRAG lacks an education domain (Section 1, line 18) but does not compare EDU-RAG against CRAG or RGB (Chen et al., 2024) in terms of question difficulty, answer type distribution, passage relevance, or other benchmark quality dimensions that would help position the contribution.

### Trivial

None that are not parser artifacts.

## Nice-to-Haves

- An ablation of retrieval strategy (sentence-level vs. passage-level, different K values, different embedding models) would substantially strengthen the benchmark characterization.
- Including a larger set of models (e.g., more 7B-70B scale models, different base architectures) would increase the benchmark's utility.
- Reporting accuracy broken down by science subject (Life Science, Earth Science, Physical Science) would reveal whether certain topics benefit more from RAG.
- Analyzing cases where retrieval contained the answer but the model still answered incorrectly would provide insight for future RAG research.

## Removed Points

These points from the inputs were removed with justification:

- **"Retrieval step is circular"** (Harsh Critic, point 3): The paper queries Google with the question text (line 67). This is standard RAG practice — querying the user's question to retrieve relevant information. The claim that this is "circular" or uninformative misunderstands standard RAG setup. In real RAG deployments, the query is the user's question. REMOVED: factually incorrect criticism.

- **"Tables embedded as raster images, not accessible"** (Harsh Critic, section notes): The original PDF likely contained proper tables; the raster image appearance is a PDF-extraction artifact. The paper does report the key Llama2-7b figure in the text. REMOVED: parser artifact.

- **"Prompt templates not included"** (Harsh Critic, section notes): The paper references Prompts 3.1, 3.2, 3.3 which were likely in a supplementary appendix stripped by the parser. REMOVED: parser artifact.

- **"No code release" framed as reproducibility concern** (Harsh Critic): The issue of releasing the *static dataset* (crawled content snapshot) is valid and retained above. The specific phrasing about code release is subsumed by the dataset release weakness. MERGED into the dataset release weakness.

- **"Related work is a literature summary, not critical analysis"** (Harsh Critic): This is a scope/style preference, not a concrete weakness. The related work adequately covers the relevant areas. REMOVED: not a substantive weakness.

- **Strength Finder's claim about "hallucination-aware scoring tailored to education"** partially conflicts with the verified weakness about imprecise hallucination measurement. The scoring design is indeed principled, but calling it "hallucination-aware" is generous given the measurement imprecision. The weakness tempers this strength, but the design itself (penalizing wrong answers more than missing ones) is still a genuine design choice. KEPT as a qualified strength with caveat noted.

- **Generic/superficial framings from Strength Finder** that were too broad (e.g., "fills a missing domain") were filtered to retain only the specific, citation-backed version. The concrete version is kept as Strength #1.

- **"The future work section reads as a to-do list"** (Harsh Critic): This is a presentational opinion. The underlying issue (preliminary nature of the work) is already captured by other major weaknesses. REMOVED: redundant.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a clear gap between the paper's ambition (a reusable education-domain RAG benchmark) and its execution (a preliminary pipeline description with thin evaluation and no released artifact). The core insight from synthesis is that benchmark papers at this venue require the *artifact itself* to be the contribution — pipeline descriptions without static, distributable data do not constitute a benchmark.

## Suggestions

1. **Release a static, versioned corpus.** Archive the crawled web content (or a curated subset) alongside the TQA QA pairs under a clear license. A benchmark must be a fixed artifact, not a time-dependent pipeline.
2. **Characterize retrieval quality.** For each question, report whether the correct answer appears in the top-K retrieved sentences. This is the minimal analysis needed to interpret RAG results.
3. **Add meaningful validation analysis.** Replace the current circular analysis section with retrieval quality statistics, error pattern breakdowns, question difficulty analysis, and comparisons against existing RAG benchmarks on relevant dimensions.
4. **Disentangle the "hallucination" claim.** Either use a metric that actually measures whether the model contradicts retrieved context (the standard RAG hallucination definition), or reframe the claim as "RAG improves QA accuracy" and drop the hallucination framing.
5. **Describe the sampling methodology** and report the subject distribution, number of answer choices, and original TQA split for the 1,255 samples.
6. **Report all key numerical results in the body text** for all models, not just Llama2-7b.

## Score and Decision

The paper identifies a genuine gap and provides concrete initial results showing RAG's value for education QA, particularly for smaller models. However, the core issue is existential for a benchmark paper: there is no static, reproducible dataset artifact — the web-enhanced content is a time-dependent pipeline. Combined with a near-empty analysis section (one circular paragraph), no retrieval quality characterization, no release plan, and unspecified sampling, the paper is too preliminary for acceptance at a top venue. The gap it identifies is worth addressing, but the current submission does not yet deliver a usable benchmark.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>
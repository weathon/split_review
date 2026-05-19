- Decision: Reject
- Avg Score: 4.50
- Scores: 6, 3, 3, 6
Now I have a thorough understanding of the paper and can verify the reviewers' claims. Let me construct the final consolidated review.

---

## Summary

The paper introduces Emoji2Idiom, a benchmark that tasks Multimodal Large Language Models (MLLMs) with translating sequences of emojis (presented as images) into corresponding idioms or words — covering Chinese four-character idioms, Chinese multi-character idioms, English words, and English idioms. The benchmark is constructed via a two-track pipeline (internet retrieval and text-to-emoji generation) with automatic and human filtering. Extensive experiments on 7 MLLMs (including GPT-4o, GPT-4V, Claude-3.5, Qwen-VL, DeepSeek-VL, LLaVa, CogAgent, InternVL) show that even the best models perform poorly, especially on Chinese idioms (GPT-4o achieves only 3.3% word-level accuracy on four-character Chinese idioms), establishing a clear gap with human performance.

## Strengths

1. **Novel task that tests a genuinely underexplored capability.** The paper is the first to define emoji-sequence-to-idiom translation as a vision-language benchmark requiring MLLMs to map visual emoji input to precise linguistic output (idioms/words), as opposed to answering general VQA questions. This is a clearly stated core contribution (Section 1: "we first propose the task of translating a sequence of emojis in images to corresponding texts") and is well-differentiated from prior emoji work that treats emojis as Unicode text rather than images (Section 2).

2. **Comprehensive evaluation spanning multiple languages, model families, and metrics.** Experiments across 7+ MLLMs — including both open-source (Qwen-VL, DeepSeek-VL, LLaVa, CogAgent, InternVL) and closed-source (Claude-3.5, GPT-4V, GPT-4o) — on Chinese and English tasks using Word accuracy, Chr-1, Chr-2, BLEU, and F1 provide a broad picture of model capabilities and limitations. The consistent finding that Chr-1 accuracy significantly exceeds word-level accuracy (e.g., GPT-4o: 30.3% Chr-1 vs. 3.3% Word on four-character Chinese idioms in Table 2) gives actionable insight — models understand individual emoji mappings but fail at combinatorial reasoning.

3. **Multi-stage data construction pipeline with human filtering.** The benchmark construction (Section 3.2) combines two data sources (internet game databases and text-to-emoji generation) with automatic filtering (deduplication, GPT-4o ethical checking) and explicit human filtering steps (removing non-standard idioms, low-consistency pairs, unclear images, repetitive mappings, and unethical content). This architectural design for quality control is clearly described and goes beyond what many benchmark papers document.

4. **In-context learning and chain-of-thought experiments validate dataset utility.** The ICL experiments (Tables 5, 6) show that adding 3–7 context examples consistently improves performance across tasks for both Qwen-VL and GPT-4o, demonstrating that the benchmark contains learnable mappings. The CoT experiments (Figure 3) further show that structured reasoning helps, providing evidence that the dataset captures structured linguistic reasoning challenges rather than noise.

## Weaknesses

### Fatal
None.

### Major

1. **Human evaluation lacks transparency for central claims to be properly assessed.** The paper uses human evaluation to establish both an "upper bound" on task difficulty (Figure 4: human performance on Chinese idiom tasks) and a quality assessment of MLLM outputs (Figure 5: human evaluation on GPT-4v/GPT-4o across 5 dimensions). However, the main text provides critically missing details: how many human annotators were used, what qualifications they had, what instructions they received, how many examples each annotator evaluated, and — most importantly — what the inter-annotator agreement was. Without these, the claimed "human performance" and the dimensional scores in Figure 5 cannot be interpreted as rigorous evidence. The reference to "G" (Appendix G) suggests more detail exists, but the main text must be sufficiently self-contained for a reviewer to assess reliability. This is a significant evidential gap for a benchmark paper whose contribution depends partly on demonstrating a human-MLLM gap.

2. **LLM-based semantic similarity scoring is used as a key evaluation metric but is completely unvalidated.** The paper (Section 4, Table 4) reports semantic similarity scores by "input[ting] the model output answers and ground truth into LLM and let[ting] LLM score the semantic similarity from 1 to 5." No validation is provided — no correlation with human judgments on a held-out sample, no inter-annotator analysis of LLM scoring stability, no analysis of potential LLM bias (e.g., does the LLM favor its own outputs?). The paper draws conclusions from the score distribution (scores concentrated in 1 and 2 for Chinese vs. 1 and 5 for English), but these observations are unverifiable without validation of the scoring instrument.

3. **The paper does not isolate what facet of capability the benchmark actually tests.** The task conflates at least three distinct capabilities: (a) visual recognition of emoji images, (b) knowledge of conventional emoji–meaning mappings (which could be learned from text-based training data), and (c) combinatorial reasoning across the emoji sequence. The paper's framing attributes failures broadly to "vision–language understanding" but never decomposes these factors. For example, the harmonic character phenomenon (snake emoji → "she" via phonetic similarity) is fundamentally a *linguistic* convention, not visual reasoning. A controlled experiment comparing emojis as images vs. as Unicode text would directly test whether the visual modality is the bottleneck. The absence of this experiment does not invalidate the benchmark, but it means the paper's strongest claims about what the benchmark reveals about MLLM vision-language intelligence are not fully supported by the evidence presented.

### Minor

1. **Single ground truth per input penalizes valid alternative answers.** Emoji-to-idiom translation admits multiple plausible outputs (synonymous idioms, valid word variants), but the benchmark provides only one ground truth per example. Standard metrics (accuracy, F1, BLEU) penalize semantically correct but lexically different outputs. The LLM-based scoring partly addresses this, but the primary metrics overcount errors.

2. **Chr-1 and Chr-2 definitions are ambiguous for Chinese idioms.** The paper states Chr-2 and Chr-1 denote "accuracy of guessing two or more words, and one or more words correctly." For Chinese four-character idioms, it is unclear whether "word" refers to a single character (汉字) or a multi-character word. This ambiguity affects interpretability of the reported numbers.

3. **No statistical significance or variance reported.** All experimental results (Tables 2, 3, 5, 6) are reported as single-point values. Without multiple runs (even 3–5 seeds for open-source models) or bootstrap confidence intervals, it is impossible to assess whether observed differences (e.g., between models or ICL settings) are reliable or within noise.

4. **Data construction details are insufficiently quantified.** The paper reports two raw data sources (internet retrieval and text-to-emoji generation) but does not give: (a) the proportion of examples from each source, (b) whether duplicates were removed across sources, (c) the number of human annotators or their inter-annotator agreement on filtering decisions. While the pipeline is described, the lack of quantitative quality metrics weakens the claim of "high-quality" benchmark.

5. **No breakdown of challenge categories across the dataset.** The paper identifies three challenge types (harmonic characters, abstract visual understanding, many-to-one/one-to-many mapping) but never reports what proportion of samples exhibits each property. This makes it hard to connect model failures to specific challenge types systematically (the case studies in Section 4.5 are illustrative but not systematic).

6. **ICL and CoT experiments are limited in scope.** Only 2 model families (Qwen-VL and GPT-4o) are tested with ICL/CoT. The CoT evaluation subset size is not stated. Performance degradation at 7-shot in Chinese tasks is noted but not analyzed (e.g., is it variance or a real effect?).

### Trivial

1. The reproducibility statement (Section 6) is entirely generic ("we put a lot of effort into reproducibility") without specifying what will be released. This should be replaced with concrete commitments (dataset, code, prompts, model outputs).

## Nice-to-Haves

- An image-vs.-Unicode control experiment (as discussed in weakness #3) would substantially strengthen the paper's ability to attribute failures to visual understanding vs. emoji-meaning knowledge.
- Reporting per-challenge-category error breakdowns for the best model would turn the case studies into systematic evidence about which specific capabilities MLLMs lack.
- Adding confidence intervals or bootstrap estimates would improve the reliability of the experimental comparisons.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Overstates novelty relative to prior emoji work"** — The paper clearly distinguishes itself: prior work treats emojis as Unicode text (UTF-8 encodings), whereas this work uses emoji images and requires visual recognition. This is explicit in the paper (Section 2: "our Emoji2Idiom is the first to apply the visual representation and textual semantics of emojis"). The criticism is factually misaligned with the paper's content.
- **"Demands negative results on non-emoji symbols (road signs, logos)"** — This is scope creep. The paper is explicitly about emojis as a case study for cryptic symbol understanding; extending to other symbols is future work, not a required contribution.
- **"The related work section does not position the task well"** — Per instructions, missing related works should not be mentioned, as external verification is not possible.
- **"The motivation is loosely stated / ambiguous about 'directly associate'"** — The paper defines the desired capability through three specific sub-challenges (Section 1: harmonic reasoning, abstract visual understanding, many-to-one/one-to-many mapping). The motivation, while intuitive, is sufficiently operationalized.
- **"BLEU smoothing not specified"** — This is an implementation detail too minor for a review.
- **"Baseline against text-based emoji understanding is essential"** — This is a Nice-to-Have rather than a required correction (moved there).
- **Strength Finder's dropped strengths** — The claim that data construction is "rigorous" is partially weakened by the lack of inter-annotator agreement metrics and source proportions; retained cautiously. The Strength Finder's other claimed strengths (novelty, comprehensiveness, ICL validation) are supported by the paper and retained.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any insight about the paper that the authors themselves do not already state or imply.

## Suggestions

1. **Provide human evaluation details in the main text:** Report at minimum the number of annotators, number of examples evaluated per annotator, inter-annotator agreement (Cohen's κ or percentage agreement) for the human performance task, and a brief description of annotator qualifications.
2. **Validate the LLM-based semantic similarity scorer:** Report correlation with human judgments on a held-out sample (e.g., Spearman's ρ on 100–200 examples). If correlation is high, this supports the metric; if low, the conclusions drawn from Table 4 should be caveated or the approach revised.
3. **Add a controlled experiment comparing emoji-as-image vs. emoji-as-Unicode input** for a representative subset. This would directly test whether the benchmark's difficulty stems from visual recognition or from emoji–meaning knowledge, and would substantially tighten the paper's framing.
4. **Report data source proportions and inter-annotator agreement** on the human filtering task to strengthen the "high-quality" claim quantitatively.
5. **Cluster model errors by challenge category** (harmonic, abstract visual, multi-to-one, etc.) for at least the best model to move beyond illustrative case studies.
6. **Report statistical significance or confidence intervals** for the main experimental results — even simple bootstrap CI for a few key comparisons would help.

# DelTA: An Online Document-Level Translation Agent Based on Multi-Level Memory

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
Large language models (LLMs) have achieved reasonable quality improvements in machine translation (MT).
However, most current research on MT-LLMs still faces significant challenges in maintaining translation consistency and accuracy when processing entire documents.
In this paper, we introduce \del, a \textbf{D}ocument-lev\textbf{EL} \textbf{T}ranslation \textbf{A}gent designed to overcome these limitations.
\del features a multi-level memory structure that stores information across various granularities and spans, including Proper Noun Records, Bilingual Summary, Long-Term Memory, and Short-Term Memory, which are continuously retrieved and updated by auxiliary LLM-based components.
Experimental results indicate that \del significantly outperforms strong baselines in terms of translation consistency and quality across four open/closed-source LLMs and two representative document translation datasets, achieving an increase in consistency scores by up to 4.58 percentage points and in COMET scores by up to 3.16 points on average.
\del employs a sentence-by-sentence translation strategy, ensuring no sentence omissions and offering a memory-efficient solution compared to the mainstream method.
Furthermore, \del improves pronoun translation accuracy, and the summary component of the agent also shows promise as a tool for query-based summarization tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a methodology that improves translation consistency by using an agent-based approach. DelTA utilizes a modular, multi-level memory system, comprising Proper Noun Records, Bilingual Summary, Long-Term Memory, and Short-Term Memory, which store and manage information at different scales, with auxiliary LLM-driven components ensuring efficient information retrieval and updates.

### Strengths
* This paper effectively addresses a significant challenge in the field, presenting meaningful improvements and contributions.

*The experimental design is comprehensive and well-executed, providing robust results.

*The presentation is clear, concise, and well-organized, facilitating easy understanding of the research.

### Weaknesses
 * As authors point out in limitations, efficiency of the method

### Questions
* How well does this scale to extremely low-resource languages?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes DelTA, a document-level translation agent that can translate documents or long context text with better translation quality than other methods. The approach consists of a series of prompts that are used to encode information about proper nouns, immediate context, larger context, summaries in the source and target language. Experiments are carried out in the IWSLT2017 benchmark for 4 language pairs and evaluated for consistency of translation terms and translation quality using reference-based translation evaluation methods.

### Strengths
The idea of the paper is simple and straightforward: provide more context about the translation task by presenting this information in the prompt of an LLM. The context is varied: sentences occurring in the immediate before the sentence being translated, context that is longer with sentences much before the current sentence, a summary of the source text, a summary of the target text and proper nouns occurring in the text with their respective translations.

### Weaknesses
The evaluation was performed only with automatic metrics such as sentence-level and document-level COMET. It would be interesting to understand if the performance reported holds with evaluation performed by translators in terms of quality and consistency as both implementations of COMET are known to be weak proxies for translation quality beyond the sentence-level, failing to capture consistency, coherence and other discourse-related linguistic dimensions.

### Questions
* Consider using the WMT24 shared task benchmark test sets that are going to be released. They provide document-level test sets. In 2023 the organizers released test sets only for English-German but for this year more language pairs will be made available.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a LLM-based, document-level translation agent (called Delta). This agent performs document-level translation on a sentence-by-sentence basis, and consists of auxiliary "multi-level memory" components, which are updated after translation of each sentence. These memory components include Proper Noun Records, Bilingual Summary, and Long-Term/Short-Term Memory. The information stored in all of these components is retrieved by prompting LLMs, where the prompt for each component is targeted towards its desired function (e.g., the Bilingual Summary component asks the LLM to generate a summary given a chunk of sentences). During translation of each sentence within a document, after updating all of these memory components, the Delta system aggregates their stored information into a single prompt. This process is continued iteratively until the entire document is translated. The paper shows that the Delta system outperforms other document-level MT systems on the IWSLT2017 and Guofeng datasets, and also presents ablations to understand the contribution of each memory component to the overall performance of Delta.

### Strengths
1. Document-level translation is currently one of the most important and underexplored research areas in the field of machine translation (MT). This paper clearly presents the motivation for their work, and summarizes the importance of document-level MT.
2. The Delta system presented in the paper is easy to implement, since it just requires prompting of off-the-shelf LLMs. The motivation for each of the modules in the Delta system is clear.
3. The experimental setup is well-written and easy to follow. The results are comprehensive (covering multiple LLMs and language pairs), and comparisons against all essential document-level MT baselines are presented.

### Weaknesses
1. The paper mentions that inconsistency is one of the major challenges during document-level translation. However, the only type of inconsistency they measure and report is Proper Noun Inconsistency, which is a surface-level type of inconsistency (can the model consistently copy a fixed string?) that doesn't require the model to reason across long contexts. The results on Proper Noun Inconsistency are used to make strong claims about their Delta system's overall improvement in consistency relative to baselines, but these claims are not adequately supported with evidence. While proper noun consistency is a valid concern, it is a relatively simple form of consistency to achieve, and the paper does not explore more complex forms of inconsistency, such as maintaining consistent pronoun references or ensuring logical consistency across the document. The paper should include more challenging consistency metrics to justify its claims.
2. The paper focuses on the comparison to "Doc2Doc" (comparing memory costs, etc), but from the reported results, "Context" is consistently better than "Doc2Doc". There is no significance testing for the results in the paper (e.g., Tables 2 and 3), and in terms of translation quality (as measured by sCOMET and dCOMET), the performance of the "Context" and "Delta" models looks quite close, with "Context" outperforming "Delta" according to dCOMET for the Qwen2-7B-Instruct model in Table 2. In Table 3, the quality-based performance of "Context" and "Delta" is even closer. (And it is not surprising that Delta outperforms in proper noun consistency, since the proper noun extractor module in Delta provides a list of all proper nouns seen. If the Context model were enhanced with this module, it seems likely that its performance on the proper noun consistency metric would also correspondingly improve.) The lack of statistical significance testing makes it difficult to determine if the observed differences are meaningful.
3. The Delta system is comprised of 5 auxiliary modules. The ablation to isolate the effects of each individual module in Figure 4 shows very small differences in quality (as measured by sCOMET and dCOMET) across these models (again, with no significance testing). The recipe (combination of modules) proposed by the authors works reasonably well based on their results, but the paper provides limited insight into the relative contribution of each of these modules to improving performance. For instance, does short-term or long-term memory help more? Is the Memory Retriever step for long-term memory necessary, and how much does this step improve performance over just using the (l sentences in) long-term memory? The ablation study is not detailed enough to provide a clear understanding of the importance of each component, and the lack of statistical significance testing further weakens the conclusions drawn from these experiments.

### Questions
1. For the summary writers, why isn't the summary for chunk m conditioned on the summary for chunk m-1 (which would allow the summary to take longer context into account)?
2. Did you investigate the effect of adjusting the numbers (k, l) of sentences to use as short- and long-term memory throughout the translation process? It seems likely that the model would probably need more context at later stages (when more sentences have already been seen), versus at the beginning of translating a long document.
3. In Figure 2, why does consistency drop so much for the en-xx 11-20 sentences bucket (and then increase again for longer sentence-wise distances) across all models?
4. The Workshop on Machine Translation (WMT, https://machinetranslate.org/wmt) also has document-level test sets, which are canonically used for MT evaluation in the literature. Why were evals presented on IWSLT2017 and Guofeng (relatively unknown datasets), but not on these standard test sets? Do the test sets used require long context to produce correct translations?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces DELTA, a Document-level Translation Agent that uses a multi-level memory architecture to improve translation consistency and quality in document-level machine translation. The agent employs four memory components (Proper Noun Records, Bilingual Summary, Long-Term Memory, and Short-Term Memory) that store and retrieve information across different granularities. The approach shows impressive improvements in translation consistency and quality across multiple language pairs and different LLM backbones. The work is evaluated extensively using both established metrics and novel consistency measures.

### Strengths
**Originality**:
- The multi-level memory architecture represents a novel approach to document translation. While memory architectures have been used in LLM agents before, the specific design with four complementary components (Proper Noun Records, Bilingual Summary, Long/Short-Term Memory) targeting different aspects of document translation is innovative.
- The approach of using an LLM-based agent for document translation, while maintaining sentence-level alignment, is creative and practical.
- The introduction of LTCR-1 and LTCR-1f metrics for evaluating translation consistency is a useful contribution to the field.

**Quality**:
- The experimental methodology is comprehensive, evaluating across 8 language pairs and multiple LLM backbones (both open and closed source).
- The ablation studies effectively demonstrate the contribution of each memory component.
- The memory efficiency analysis is well-done, with clear comparisons showing the advantages over Doc2Doc approaches.
- The evaluation considers both translation quality (sCOMET, dCOMET) and consistency (LTCR metrics).

**Clarity**:
- The paper is logically structured, moving from motivation to design to evaluation.
- The multi-level memory architecture is well-explained with clear diagrams and algorithms.
- The experimental results are presented systematically with detailed tables and analyses.
- The limitations and future work are honestly discussed.

**Significance**:
- The work addresses a real and important challenge in document translation - maintaining consistency while handling long documents.
- The approach is practical and implementable, with clear memory efficiency advantages.
- The method shows strong improvements across different languages and models, suggesting broad applicability.
- The memory architecture could potentially be adapted for other document-level NLP tasks, as demonstrated by the query-based summarization results.

### Weaknesses
1. Efficiency analysis needs more detail:
   - While memory efficiency is demonstrated, the paper claims cost-effectiveness without supporting evidence
   - No comparison of total wall-time or FLOPS between approaches
   - Limited discussion of computational overhead from multiple LLM calls

2. Missing comparisons and baselines:
   - No evaluation against long-context LLMs (e.g., Claude, Gemini) which could be particularly relevant for document translation
   - DeepL, which explicitly supports document-level translation, would be a valuable baseline, and a more relevant choice than Google.
   - Limited discussion of Doc2Doc approach limitations in related work

3. Incomplete motivation and analysis:
   - Does not address context-dependent translation as a key challenge (see https://aclanthology.org/2023.wmt-1.42/)
   - Claims of "significant" improvements lack statistical significance testing
   - Claims about undertranslation issues and translation quality decline (L177-178) should be supported with citations to relevant work (e.g.,  https://arxiv.org/abs/2401.06468, https://aclanthology.org/2024.acl-long.336/)
 
4. Technical details and reproducibility:
   - No mention of code release plans

### Questions
1. How does the approach perform compared to long-context LLMs? Given recent advances in context window sizes, this seems particularly relevant.

2. Will the code be released? This would be valuable for reproducibility and adoption.

3. Can you provide a more detailed efficiency analysis, including:
   - Total wall-time comparison between DELTA and Doc2Doc approaches
   - FLOPS comparison for open-weight models
   - Analysis of the number of LLM calls required

4. How does DELTA handle context-dependent translations where meaning depends on broader document context? While pronoun translation is briefly discussed, a more comprehensive analysis (see https://aclanthology.org/2023.wmt-1.42/) would be valuable.

5. Have you considered evaluating against DeepL, given its explicit support for document-level translation?

6. Could you provide statistical significance tests for the reported improvements?

### Soundness
3

### Presentation
3

### Contribution
3

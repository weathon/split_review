# Unified Multi-Modal Interleaved Document Representation for Information Retrieval

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 5, 3

## Abstract
Information Retrieval (IR) methods aim to identify relevant documents in response to a given query, which have gained remarkable attention due to their successful application in various natural language tasks. However, existing approaches typically consider only the textual information within the documents, which overlooks the fact that documents can contain multiple modalities, including texts, images, and tables. Further, they often segment each long document into multiple discrete passages for embedding, preventing them from capturing the overall document context and interactions between paragraphs. We argue that these two limitations lead to suboptimal document representations for retrieval. In this work, to address them, we aim to produce more comprehensive and nuanced document representations by holistically embedding documents interleaved with different modalities. Specifically, we achieve this by leveraging the capability of recent vision-language models that enable the processing and integration of text, images, and tables into a unified format and representation. Moreover, to mitigate the information loss from segmenting documents into passages, instead of representing and retrieving passages individually, we further merge the representations of segmented passages into one single document representation, while we additionally introduce a reranking strategy to decouple and identify the relevant passage within the document if necessary. Then, through extensive experiments on diverse information retrieval scenarios considering both the textual and multimodal queries, we show that our approach substantially outperforms relevant baselines, thanks to the consideration of the multimodal information interleaved within the documents in a unified way.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduced a novel IR framework, which enables integration and representation of diverse multimodal content including text, images, and tables, into a unified document representation.

### Strengths
The motivation of the work is clear and the problem is worth exploring. The proposed methods are technically sound.

### Weaknesses
The novelty of the proposed method is limited. The experiment results and discussion sections are not well-presented to demonstrate the effectiveness and benefits of the proposed methods.



### Questions
1. The paper proposed to first represent each document as a sequence of sections as $s_i = [V_{S_i}, L_{S_i}, T_{S_i}]$, where $V_{S_i}$,  $L_{S_i}$, and $T_{S_i}$ are visual tokens, text tokens, and table tokens, respectively. Is there a specific reason why concatenate features from different modalities in this way? Have you tried other feature fusion methods?
2. The above mentioned question also exists in section 3.3, is there a specific reason why concatenate query q and s_i? Why not shuffle their positions? Why not choose other feature fusion methods such as inner product, outer product, addition, subtraction, etc.?
3. I was wondering is there a specific reason why choose contrastive loss for training in section 3.2? Have you compared it with conventional cross-entropy loss?
4. In the experiment section, I was wondering have you conducted the experiments with conventional methods such as dual encoder, where the feature embeddings are extracted from LLaVA?
5. In the experimental result and discussion sections, it is worth exploring how much benefits introduced by each modality. 
6. Besides, it is worth comparing the additional performance gain introduced by each modality v.s. their extra latency.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents a unified approach to encode document representations for information retrieval, consisting of (1) encoding multi-modal interleaved information in a document; (2) split a document into multiple passages and separately encoding the split passages; then average pooling over the passage embeddings as the document representation. The authors conduct studies on how to fine-tune a VLM retriever and reranker to handle  information retrieval tasks with interleaved document.

### Strengths
1. The proposed approach is straightforward. Leveraging the pre-trained VLMs for information retrieval is an important topic.
2. The ablation studies on training a reranker are comprehensive and clearly illustrates the detail on how to train a multimodal reranker.

### Weaknesses
1. Although the main claims of the paper (interleaved document embeddings and aggregate representations from sections) are intuitive, the experiments are not fully convinced. (1) Is interleaved document encoding better? No text-only retrievers as baselines are provided. It is reasonable to compare document encoding with and without interleaved images; however, it is also sensible to provide the text-only retriever (such as E5, DRAGON or MistralE5) fine-tuned on the same dataset or zero-shot as the text-only retrieval baseline since using VLM fine-tuned on text-only training data may make the VLM overfitting on the small training data. The absence of a strong text-only baseline makes it difficult to isolate the impact of the multi-modal approach. Specifically, it's unclear if the gains are due to the interleaved encoding or simply the use of a more powerful VLM, which could be overfitting on the relatively small training datasets when fine-tuned on text only data. (2) Is aggregating representation from sections better? The experimental results in Table2 may provide the answer but some settings are not clear to me (See 1. in Questions).
2. Some experimental settings are not clear (See Questions) and I’m somehow a bit confused by the tables in the main experiment. For example, in the same dataset, Encyclopedic-VQA and Enc-VQA, there are document and section retrieval; however, there is no clear explanation of the settings on document and section retrieval (See 3. in Questions).

### Questions
1. Clarifying the experimental settings in Table2: If I understand correctly, the comparison of 2nd and 3rd rows is to demonstrate the effectiveness of document retriever (aggregate section embeddings from section retriever) is better than section retriever. However, I cannot find the detailed settings for the 2nd row (i.e., how many documents are passed to rerankers? Since the retrieved unit is section; then, there maybe multiple top-K sections coming from the same document.). For a comparison, my imagination is that the top 25 distinct documents should be first identified from the top-K retrieved sections (where K > 25) before reranking? 
2. Why the numbers of the last row from Table1 and Table 2 are different? I assume that they are from the best approach with document retrieval with reranker?
3. For document retrieval, how you conduct reranking? Is the reranking pipeline is still the same as section retrieval? I.e., top-25 documents are provided to the reranker, which reranks all the sections in the top-25 documents and use the maximum score of the section in a document as the score to rerank the document?
4. Have you tried to train a retriever and reranker on all the datasets and check if the ranking models can generalize well across different datasets?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents Interleaved Document Information Retrieval System (IDentIfy), a document retrieval framework that uses vision-language models (VLMs) to encode the multi-modal document interleaved with textual, visual, and tabular data to perform document retrieval followed by section retrieval. In the document retrieval stage, following the bi-encoder paradigm, the query and document section is separately encoded, and the section embeddings from a document is averaged to form the document embedding. In the section retrieval stage, the authors develop a re-ranker to re-rank sections previously retrieved by the document retriever. Experimental results show that IDentIfy can outperform Entity and Summary baselines as well as textual models.

### Strengths
- With the advantages of VLMs, IDentIfy is able to perform effective retrieval on documents interleaved with multiple modalities.
- IDentIfy effectively integrates global information into segmented sections while maintaining efficient training inference.

### Weaknesses
 - The experiments are conducted on clean, source-avaliable corpus whose documents can be easily segmented into sections according to the subtitles, and then extracted into multi-modal elements. However, real-world data are often presented in compiled files like PDFs, where document structure is not explicitly marked. In such scenarios, document division and multi-model data extraction may not be possible without significant pre-processing, such as OCR and layout analysis, which are not addressed in this work. This poses a challenge for IDentIfy in real-world use, limiting its applicability to structured, easily parsed documents.
- The presentation of the results in Section 4.3 lacks a main thread, and is difficult to follow. The experiments are presented as a series of results without a clear narrative or overarching question that they are trying to answer. I suggest the authors add an introductory paragraph at the beginning of Section 4.3 to provide context and organize the experiments in a clearer structure, perhaps by grouping experiments that address similar research questions.
- There are some details in this paper that are not very clear (see Questions).


### Questions
- As shown in Table 8, the retrieval target of Encyclopedic-VQA, InfoSeek, ViQuAE is only text. Why does IDentIfy perform better than the Text-document baseline on these datasets?
- The equation on line 240 contains an error: exp is missed in the loss calculation.
- Do “section” and “passage” in this paper mean the same thing? If yes, a sentence could be added stating that the two terms refer to the same thing.
- The terms “document retrieval” and “section retrieval” are confusing. They actually mean the two stages in IDentIfy. But they read like two levels of retrieval granularity, as the experiment presents on line 347.
- How are texts, images, and tables extracted from a section organized into the input to the section encoder? Is it a fixed order of texts, then images, finally tables (as line 210 indicates)?
- What do the authors mean by “combine four images into one”, on line 301?
- How do the authors “consider four sections per document in representing documents” (line 302)? What four, the first four?
- In Table 2 and 1, the passage (section?) retriever performs significantly worse than document retriever (20.5 R@1 for document retriever, 3.9 R@1 for passage retriever, only 19% of the performance of document retriever). Does that mean that the global information plays a so important role, that ignoring it can have a huge impact on retrieval, while a simple embedding averaging can mitigate it effectively? If yes, why can the re-ranker, which doesn’t integrate any global information, offer so much gain (3.9→28.6, closer to 35.1)?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper addresses limitations in document representation for information retrieval (IR) by recognizing that documents can contain multiple modalities—such as text, images, and tables—and that segmenting long documents into discrete passages often hampers the ability to capture overall context and inter-paragraph interactions. The authors propose a novel method that interleaves different modalities in document embeddings, leveraging the capabilities of vision-language models (VLMs) to enhance the representation of multimodal documents. The proposed method aims to improve the effectiveness of document retrieval by better capturing the relationships among various modalities within a single document.

### Strengths
1. **Originality**:
   - The paper identifies significant limitations in current document representation methods and proposes an innovative approach to integrate multiple modalities, a relatively underexplored area in information retrieval.

2. **Quality**:
   - The methodology demonstrates a thoughtful integration of VLMs for enhancing document embeddings, showing promise in leveraging advanced models to address multimodal challenges.

3. **Clarity**:
   - The paper is well-structured and articulately presents the limitations of existing approaches, the proposed solution, and the expected impact on information retrieval. This clarity makes it accessible to readers across various backgrounds.

4. **Significance**:
   - By focusing on the multimodal nature of documents, the research has potential implications for various applications in IR, making it a timely contribution to the field as the demand for more sophisticated document processing techniques grows.

### Weaknesses
1. **Lack of Novel Contribution**:
   - While the application of VLMs to IR is interesting, the paper lacks substantial novelty beyond their application. Previous works, such as those exploring VLMs in other contexts (e.g., CLIP, BLIP), have already laid the groundwork for similar methodologies.
   - The segmentation of documents into sections does not introduce a new technique; rather, it mirrors existing practices without clear justification for its necessity.

2. **Evaluation and Baselines**:
   - The evaluation framework appears insufficiently rigorous, with limited baseline comparisons provided. The selection criteria for these baselines are not clearly articulated, raising concerns about the validity of the results.
   - There is a notable absence of non-VLM-based evaluations to establish the effectiveness of the proposed method relative to traditional approaches.

3. **Methodological Concerns**:
   - The rationale for dividing documents into sections is not convincingly justified, leaving the impression that it may compromise document representation integrity.
   - The proposed use of representations such as ‘End of Query’ and ‘End of Section’ lacks comparative evidence demonstrating their superiority over alternative representation methods.

4. **Inadequate Discussion of Modality Gap**:
   - The paper does not sufficiently address how the modality gap is resolved, which is critical for understanding the effectiveness of the proposed method.

### Questions
1. **Rationale for Sectioning**:
   - Could you clarify the rationale for segmenting documents into sections? What benefits do you envision from this approach that could not be achieved through a holistic document representation?

2. **Alternative Approaches**:
   - Have you considered preprocessing with techniques like CNNs before embedding to retain document-level context without segmenting? How might this impact your findings regarding limitations?

3. **Effectiveness of Representations**:
   - Can you provide empirical evidence or theoretical justification that supports the efficacy of using representations like ‘End of Query’ and ‘End of Section’ compared to other methods?

4. **Baseline Choices**:
   - What criteria did you use to select the baseline models for evaluation? How do these baselines adequately reflect the current state of research in multimodal IR?

5. **Modality Gap Resolution**:
   - How does your approach specifically address the modality gap? Can you elaborate on any mechanisms or metrics used to assess this aspect?

6. **Generalizability of Results**:
   - Since LLaVA-NeXT is highlighted as a strong VLM, how do you anticipate the performance might vary with other VLMs? Have you conducted preliminary analyses to explore this?

### Soundness
3

### Presentation
2

### Contribution
2

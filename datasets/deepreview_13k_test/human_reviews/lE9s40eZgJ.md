# mOSCAR: A Large-scale Multilingual and Multimodal Document-Level Corpus

- Decision: Reject
- Scores: 6, 3, 8, 6

## Abstract
Multimodal Large Language Models (mLLMs) are trained on a large amount of text-image data. While most mLLMs are trained on caption-like data only, \citet{alayrac2022flamingo} showed that additionally training them on interleaved sequences of text and images can lead to the emergence of in-context learning capabilities. However, the dataset they used, M3W, is not public and is only in English. There have been attempts to reproduce their results but the released datasets are English-only. In contrast, current multilingual and multimodal datasets are either composed of caption-like only or medium-scale or fully private data. This limits mLLM research for the 7,000 other languages spoken in the world. We therefore introduce mOSCAR, to the best of our knowledge the first large-scale multilingual and multimodal document corpus crawled from the web. It covers 163 languages, 315M documents, 214B tokens and 1.2B images. We carefully conduct a set of filtering and evaluation steps to make sure mOSCAR is sufficiently safe, diverse and of good quality. We additionally train two types of multilingual model to prove the benefits of mOSCAR: (1)~a model trained on a subset of mOSCAR and captioning data and (2)~a model train on captioning data only. The model additionally trained on mOSCAR shows a strong boost in few-shot learning performance across various multilingual image-text tasks and benchmarks, confirming previous findings for English-only mLLMs. The dataset can be accessed here.\footnote{\url{https://oscar-project.io/documentation/versions/mOSCAR/}}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper yields a powerful Multimodal Multilingual pretraining dataset for MLLM's. They choose a standard set of filters and approaches to arrive a higher quality. Downstream models trained on mOSCAR are empirically stronger than existing models.

### Strengths
1. The choice of filters was discussed thoroughly. Relative to other literature in the field, it is clear that an exhaustive search over the space of possible data filtering methodologies was done. 
2. The empirical results are quite promising. The set of evaluations/benchmarks is extensive and exhaustive. Moreover, the performance across different shotting of the models demonstrates significant improvmenets over existing datasets. 
3. I found the discussion around diversity measurements and comparison to existing datasets to be very well done. The discussion how multilinguality vs English-only diversity needs to be accounted for was also enlightening.
4. The prevention against data poisoning is appreciated and important.

### Weaknesses
1. I found some of the choices, while fairly standard, for the design of this framework to be lacking in terms of thought in terms of their design. While most of the decisions are cited, several decisions could have been had more analysis. 
2. Ablations on the filters would have been very interesting to see. This includes the joint image-text filtering.

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents the creation and utilization of mOSCAR, a novel large-scale multilingual and multimodal dataset for training Multimodal Large Language Models (mLLMs). The dataset, which includes 303 million documents with 1.15 billion images spanning 163 languages, was created to address the limitations of existing datasets that are often monolingual or only moderately multilingual. By applying a series of filtering steps to enhance safety, diversity, and quality, mOSCAR aims to support multilingual, in-context learning capabilities. The authors demonstrate mOSCAR's benefits by training models that outperform baseline models across multiple multilingual, multimodal benchmarks. The proposed dataset seeks to address the scarcity of high-quality, large-scale multilingual datasets by employing rigorous data collection, filtering, and decontamination techniques. The authors validate mOSCAR's efficacy by training and evaluating two models: one on mOSCAR and captioning data, and another solely on captioning data. The mOSCAR-trained model shows marked improvements, particularly in few-shot learning across multilingual tasks.

### Strengths
mOSCAR is derived from Common Crawl and utilizes sophisticated methods to filter and refine data. Steps include document deduplication, toxicity filtering, PII removal, and NSFW detection, ensuring a robust dataset suitable for mLLMs. Covering 163 languages, mOSCAR significantly expands the multilingual training dataset landscape, making it inclusive of languages that are often underrepresented in large-scale datasets. The authors conducted extensive benchmark tests, demonstrating that models trained with mOSCAR achieve superior performance in few-shot learning and across a variety of image-text tasks compared to models trained solely on captioning data. The authors plan to make the dataset public, promoting accessibility and encouraging further research in multilingual and multimodal model training. With meticulous filtering to maintain both quality and diversity, the paper ensures that mOSCAR addresses common issues like NSFW content, toxic language, and duplication, which enhances its usability in ethical AI research.

### Weaknesses
1. Limited manual validation (1,000 images for NSFW, 100 documents for toxic content)
2. English-centric regex patterns may miss unsafe content in other languages
3. Binary toxicity detection requiring two distinct toxic words could miss subtle harmful content
4. Document-level NSFW filtering is overly aggressive, potentially discarding valuable safe content
5. Reliance on regex and wordlists could be improved with neural-based approaches
6. Fixed character (300) and node count (5) thresholds may not accommodate different writing systems
7. Language identification may underperform on code-switched or multilingual content
8. Limited evaluation of data quality and distribution across the 163 languages, particularly for low-resource languages
9. No systematic evaluation of text-image alignment quality
10. Lack of content relevance metrics within documents

### Questions
As weakness

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a multimodal version of OSCAR, which is a popular multilingual dataset from CommonCrawl

## High level overview of the dataset:
- 163 languages, 303M documents, 200B tokens, 1.15B images
- This is an interleaved text-image dataset (as opposed to captioning-focused datasets)
- Trained a multilingual multimodal Flamingo-style model on the mOSCAR dataset and show it outperforms the OpenFlamingo-3B-MPT translate-test baseline across various evaluation sets. 

## Overview of data collection and filtering process:
- Start from three 2023 CommonCrawl WARC files. 
- Parse each document's DOM tree and use HTML tags to extract images, remove tables, etc.
- Filtering based on **size**
    - 50% removed -- too small (<500 bytes)
- Filtering based on **text** --> done on both DOM-text-node level and document-level
    - NSFW filter -- Done on document level using regex keyword matching
    - Deduplication -- Levenshtein ratio and MinHashLSH to calculate near-duplicates per language. Filter out 19\%. 
    - Toxicity filter -- From list of toxic keywords in multiple languages. Filter out 1-2\%.
    - PII filter
- Filtering based on **image**
    -  URL filters -- Remove URLs that mention words like "banner", "logo", etc. Filter out 13.6 \%
    - NSFW filter -- combine multiple NSFW detectors for nudity. Filter out 0.5\%
    - CSAM filter -- Use proprietary child sexual abuse classifier. Filter out 0.07\%
    - Deduplication -- Use imagehash per language.
    - PII filter -- Detect faces
- Decontamination to remove images appearing in test sets

### Strengths
1. **Novelty and usefulness of contribution** -- There currently does not exist a multilingual multimodal interleaved dataset at this scale, so this artifact is something that would certainly be useful to the community.
    - This differs from other multilingual multimodal datasets (e.g. LAION-5B, mC4) since it is focused more on interleaved text+images as opposed to simple captioning.
    - This differs from other interleaved datasets (e.g. IDEFICS) because it is multilingual as opposed to pure English.
2. **Comprehensive data collection and filtering pipeline** -- The filtering process is detailed very thoroughly, and filtering is done on both text and images. Filtering was done across various features of a document, such as size, presence of keywords, image aspect ratio, etc. The pipeline is also general and scalable, so if somebody wants to do it on a larger part of CommonCrawl, it should be doable.
3. **Strong safety filters** -- This is something that is of utmost importance in designing such datasets (as we have seen from the LAION case). The paper handles this carefully, with NSFW, CSAM, and toxicity filters for both text and images. They also respect robots.txt protocols when downloading images.

### Weaknesses
1. **No dataset optimization** -- The paper shows that a Flamingo-style model trained with mOSCAR outperforms a translate-test baseline. This is great, but the paper didn't really mention how much iteration they did when designing this dataset. Were there multiple rounds or iterations of creating mOSCAR? There seems to be a lack of ablations, so to me it felt like the model training experiments were more of an afterthought after the dataset had already been created. (Maybe that was the intention?) 
2. **No quality filter** -- This is related to the point I mentioned above. Because there is no filter specific for text quality, then the mOSCAR dataset is more of a cleaned version of CommonCrawl, as opposed to a cleaned+filtered version that is optimized for training good models.

### Questions
- What was the original size of the three common crawl WARC files combined? How many text tokens and images?
- I'm not very clear on the difference between the NSFW text filter and the toxicity text filter. It seems that the toxicity text filter already contains keywords for NSFW, so is this NSFW filter needed here?
- I'm a bit curious on what the main bottleneck of the pipeline is. How long would each of these steps take approximately? If someone wants to scale this up to larger datasets, which part of the process is the one that would take the most time?
---

Typos:
- L25: "train" --> "trained"
- L245 "bias" --> "biased"

Missing references:
- MINT-1T https://arxiv.org/abs/2406.11271 -- not multilingual but probably worth mentioning

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper constructs a fully open-sourced multilingual multimodal datasets for interleaved text-image training. The dataset, namely mOSCAR, covers 163 languages, 303M documents, 200B tokens, and 1.15B images. The authors compare the performance of one model trained on a subset of mOSCAR and caption data with another trained on caption data only, and find the model trained on mOSCAR exhibits better in-context learning abilities.

### Strengths
1. The paper collects a large amount of data of high quality for multilingual multimodal training and open-source it. The workload and effort is significantly high and the dataset will be useful to the community.
2. The data processing pipeline is comprehensive and containing standard steps (e.g., deduplication, language filtering, PII removal, etc.), resulting in high-quality data.
3. The analysis shows mOCSCAR matches the quality of the existing interleaved English-only datasets in terms of quality and diversity

### Weaknesses
1. I appreciate this line of work, but the contribution beyond engineering effort is unclear.
2. The baselines in performance comparison needs to be further justified (see questions).
3.It is unclear how much the English-only performance drop when training on this multilingual dataset, where the author should conduct an ablation study and present the model performance on common English-only dataset such as MMMU, MME, etc. If there is an obvious decrease in English performance, the author should discuss how to mitigate this effect and in what situation the users should choose mOSCAR and combine with other caption data and with what ratio.

### Questions
1. Could the authors clarify their baselines? In L399-L401, the authors said they trained 3 models on: (1) 50M mOSCAR + 100M image-text pairs; (2) 300M image-text pairs; (3) 35M WIT + 70M text-image pairs. While in Table 5 there is one new setting with 35M mOSCAR + 70M text-image pairs. It would be helpful for the authors to clarify their model training settings in every caption to avoid confusion.
2. Could the author explain why WIT performs better than mOSCAR with the same performance score across different number of shots on Multi30K in Table 5?
3. What is the trade-off of using English-only dataset and mOSCAR? Could the author evaluate the models on English-only benchmarks as well to indicate in what situation the user should choose mOCSAR and at what ratio?
4. I also wonder if there is any trade-off between enhancing the VLM's ability on few-shot learning situation v.s. other capabilities such as general perception, captioning, VQA, etc. Could the authors design analysis on this?
5. With what license the authors plan to release the data?

### Soundness
3

### Presentation
4

### Contribution
3

# OmniCorpus: A Unified Multimodal Corpus of 10 Billion-Level Images Interleaved with Text

- Decision: Accept
- Avg Score: 7.50
- Scores: 6, 8, 8, 8

## Abstract
Image-text interleaved data, consisting of multiple images and texts arranged in a natural document format, aligns with the presentation paradigm of internet data and closely resembles human reading habits.
  Recent studies have shown that such data aids multimodal in-context learning and maintains the capabilities of large language models during multimodal fine-tuning.
  However, the limited scale and diversity of current image-text interleaved data restrict the development of multimodal large language models.
  In this paper, we introduce \dsname, a 10 billion-level image-text interleaved dataset. Using an efficient data engine, we filter and extract large-scale high-quality documents, which contain 8.6 billion images and 1,696 billion text tokens. Compared to counterparts (\eg, MMC4, OBELICS), our dataset 1) has 15 times larger scales while maintaining good data quality; 2) features more diverse sources, including both English and non-English websites as well as video-centric websites; 3) is more flexible, easily degradable from an image-text interleaved format to pure text corpus and image-text pairs.
  Through comprehensive analysis and experiments, we validate the quality, usability, and effectiveness of the proposed dataset. We hope this could provide a solid data foundation for future multimodal model research.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents OmniCorpus, a large multimodal (text and vision) and multilingual (English and Chinese) dataset containing bilions of images interleaved with trilions of tokens. The paper explains how the data was obtained, filtered, and formated, and presents several experiments conducted on the dataset (i.e. training a VLM on the dataset from existing publicly-available vision encoders and text decoders).

### Strengths
- The paper presents OmniCorpus, a large multimodal (text and vision) and multilingual (English and Chinese) dataset containing hundreds of millions of documents (bilions of images, and trilions of tokens). This is by far the largest publicly available dataset that I know of, which can increase the amount of data available to conduct research on Vision-Language Models.
- The dataset has been carefully deduplicated and filtered to prevent NSFW content, personal information, offensive content, etc.

### Weaknesses
 - As with many other datasets using crawled data from the Internet, it's not clear if 1) the authors of the paper themselves followed the terms of use of the sources of the data, and more importantly (from the user's perspective) if 2) the use of the downloaded data by the users (people training VLMs) may be subject to different terms of use / restrictions that are not directly stated anywhere, and may depend on different jurisdictions (e.g. can researchers legaly use this data to conduct research? both academic and industry researchers? can they release the models trained on this dataset?). 
The authors acknowledge this in the "ethical discussion" in appendix A3 (and other parts of the appendix A): "it is impractical to obtain explicit consent from all content creators". I personally agree with this statement, but I think it should be mentioned in the main paper.
- I would appreciate a table similar to Table 5, but comparing the author's model train only on LAION (for instance) and OmniCorpus-CC, varying the number of the total number of tokens (e.g. text tokens + image tokens after encoding). This would be a proxy measuring the "quality" of both datasets, defined as "downstream accuracy that a token from the dataset provides". If the quality of the dataset proves to be relatively high, my soundness score would increase.
- It seems that the authors worked on improving the support of other languages beyond Chinese and English (e.g. line 237: "we [...] enhanced its capability to handle Chinese, Japanse and Arabaic documents"), however they decided to include only Chinese and English documents at the end. This is a lost opportunity (and amount of work) to have a truly multilingual (and not bilingual) dataset.
- As all the the other publicly available massive datasets, only the URL images are provided, which may difficult the reproducibility of the experiments conducted using it over time.

### Questions
- How was the set of "Chinese Websites" decided?
- I assume that the frequencies that appear in section 4 where obtained by manual inspection by the authors of the 200 randomly sampled documents, is that correct? or where they shipped to external evaluators?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces a novel multi-modal and bilingual corpus at billions scale with image and text interleaved format. The dataset has three subsets (CC, CW, YT). The data processing and filtering steps for each subset is carefully designed and clearly explained. Extensive experiments are performed to access the both quality and the value of the dataset for multi-modal large language modeling tasks. Several  pre-training and fine-tuning experiments ablations demonstrate the value of the proposed dataset.

### Strengths
- Largest open source multi-modal dataset to date (8.6B images interleaved with text) 
- Describes a detailed framework to collect and curate large multi-modal datasets at scale. 
- Extensive ablations showing the value of the dataset with interleaved text format for few shot and other multi-modal understanding tasks.

### Weaknesses
 - It is not 100% clear, if one can replicate the same data collection process and produce similar quality datasets. The models used for filtering content, the thresholds and potentially other important details seem to be missing. 
- Table metrics and abbreviations need to be explained for clarity.

### Questions
A few quick notes for authors to improve the paper:  
1) Table metrics and abbreviations should be clearly explained in the text where applicable. 
2) minihash -> MinHash. We also need to understand what hash functions used to better understand how the dedup is performed for repeatability. 
3) Table 5 - Shall the authors do a deep dive for the few shot evaluations with the proposed pre-training dataset (especially for COCO dataset)?  We need deeper understanding of why the few shot metric improvements are so high. Examples would also help especially for those the baseline models fail but the model pre-trained with OmniCorpus performs better. 
4) Do the authors plan to release the code used for dataset generation?

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
3

### Summary
This paper introduces OmniCorpus, a 10 billion-level open-source image-text interleaved dataset. And it proposes an efficient data engine. It also conducts comprehensive analysis and experiments.

### Strengths
1. The largest open-source multimodal dataset to date. It pushes the boundaries of scale and diversity by encompassing 8.6 billion images interleaved with 1,696 text tokens.
2. A comprehensive set of tools and algorithms, including a streaming data format that unifies multimodal data from various sources, an efficient and scalable data engine capable of processing large-scale data, and human feedback filters to ensure high-quality data.
3. comprehensive analysis and experiments.

### Weaknesses
No obvious shortcomings observed.

### Questions
No obvious shortcomings observed.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This manuscript introduces OmniCorpus, a massive multimodal dataset consisting of 10 billion-level images interleaved with text. This dataset is designed to support the development of multimodal large language models by providing a more diverse and larger scale of image-text data compared to existing datasets. The contributions of this manuscript include the introduction of the largest multimodal dataset, a set of tools and algorithms for data processing, and extensive experiments that validate the dataset's quality and effectiveness.  The authors conducted experiments to explore the effectiveness of image-text interleaved data for few-shot capabilities and language model maintenance. They also compared OmniCorpus with other datasets and found that their dataset outperforms others in terms of quality and diversity.

### Strengths
**Large Scale**: The dataset boasts an unprecedented scale of 8.6 billion images and 1.696 trillion text tokens, making it the largest multimodal dataset available.

**Diversity**: OmniCorpus includes data from a wide range of sources, including both English and non-English websites, as well as video-centric platforms, which enhances the diversity of the dataset.

**Usability**: The dataset has been validated through comprehensive analysis and experiments, demonstrating its quality, usability, and effectiveness.

**Writing**: This manuscript is well-written, with clear motivation and solid experimental discussions.

### Weaknesses
 **Bias**: The paper acknowledges potential biases in the dataset but does not provide a detailed analysis of these biases.

**Filtering Mechanisms**: The current filtering process may not be sufficient to ensure high-quality data.

### Questions
Will all the data processing code and the data be open-sourced?

### Soundness
4

### Presentation
4

### Contribution
4

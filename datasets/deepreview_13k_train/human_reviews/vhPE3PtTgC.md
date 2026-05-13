# SWEb: A Large Web Dataset for the Scandinavian Languages

- Decision: Accept
- Scores: 8, 6, 6, 5

## Abstract
This paper presents the hitherto largest pretraining dataset for the Scandinavian languages: the Scandinavian WEb (SWEb), comprising over one trillion tokens. The paper details the collection and processing pipeline, and introduces a novel model-based text extractor that significantly reduces complexity in comparison with rule-based approaches. We also introduce a new cloze-style benchmark for evaluating language models in Swedish, and use this test to compare models trained on the SWEb data to models trained on FineWeb, with competitive results. All data, models and code are shared openly.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper introduces SWEb, the largest pretraining dataset for Scandinavian languages, containing over one trillion tokens across Swedish, Danish, Norwegian, and Icelandic. SWEb aims to address the scarcity of large-scale, high-quality datasets specifically tailored for these languages. To create this dataset, the authors develop a model-based text extraction pipeline that enhances efficiency and reduces complexity compared to rule-based methods. Key contributions include:

- SWEb Dataset: An extensive web dataset of Scandinavian languages with over one trillion tokens, surpassing existing resources by an order of magnitude.
- Model-Based Extraction Pipeline: A novel, data-driven text extraction model that effectively filters high-quality content, yielding about 60% more usable tokens than previous approaches like FineWeb.
- Swedish Benchmark (HP-MEK): A new cloze-style benchmark for Swedish, derived from the Swedish Scholastic Aptitude Test, to evaluate language models trained on SWEb and demonstrate competitive performance against models trained on FineWeb.

The authors openly release the SWEb dataset, extraction pipeline, and the HP-MEK benchmark to support further research and development in Scandinavian language modeling​

### Strengths
Originality

The SWEb dataset is original in its approach to handling Scandinavian languages. The authors create a model-based extraction process that moves away from rule-heavy, manual extraction methods, simplifying the pipeline. They also introduce HP-MEK, a benchmark specific to Swedish, which adds value by providing a relevant evaluation tool for Scandinavian models.

Quality

The quality of the work is evident in the detailed steps of the SWEb pipeline. The authors carefully build a process to select and clean high-quality data, resulting in 60% more usable tokens than previous approaches like FineWeb. They validate the dataset with clear metrics, comparing models trained on SWEb and FineWeb to show the effectiveness of their extraction model.

Clarity

The paper is organized well, making each pipeline stage easy to understand. Diagrams and examples help clarify complex steps like content extraction and filtering. The authors document their choices for filtering and quality control, making the approach easier to follow and replicate.

Significance

SWEb is significant because it makes a high-quality, large-scale dataset available for Scandinavian languages, which traditionally have fewer resources. This dataset and the HP-MEK benchmark can help researchers build better models for these languages, making SWEb a useful resource for Scandinavian language research.

### Weaknesses
1. Limited Applicability Beyond Scandinavian Languages
Weakness: The SWEb pipeline is tailored specifically for Scandinavian languages, potentially limiting its scalability or adaptability to non-Scandinavian or low-resource languages. This narrow focus may reduce the general utility of SWEb’s approach in multilingual or global settings where language resources are scarcer. The model-based approach, while innovative, may not generalize well to languages with significantly different linguistic structures or web content characteristics. For example, languages with different writing systems or those that rely heavily on user-generated content might present unique challenges that the current pipeline is not designed to handle.

Recommendation: It would be beneficial to discuss adapting the pipeline to other language families or the performance challenges in non-Scandinavian languages. Providing generalization strategies, such as multilingual training or enhanced language detection techniques, could expand SWEb’s relevance. Including preliminary results or small-scale tests on other language groups would further strengthen the paper’s broader applicability.

2. Reliance on Manual Annotation in Model Training
Weakness: Although SWEb’s model-based extractor is innovative, it relies on manually annotated data (1,380 samples) for training the extraction model, which may be resource-intensive and impractical for other languages or domains. Annotating thousands of samples for every new language could become a bottleneck, especially in low-resource contexts. The manual annotation process introduces potential biases and inconsistencies that could affect the model's performance. Furthermore, the paper does not detail the annotation guidelines, making it difficult to assess the quality and reliability of the training data.

Recommendation: Introducing semi-supervised or weakly supervised learning approaches to reduce the dependency on manually annotated data could improve scalability. Alternatively, SWEb could consider leveraging existing rule-based systems or transfer learning from similar languages to jumpstart the model training in new language settings, potentially improving data efficiency.

3. Evaluation Restricted to Swedish Benchmark
Weakness: The evaluation uses only a Swedish benchmark (HP-MEK) to compare SWEb against FineWeb. While effective for a Swedish-specific evaluation, this choice does not cover other Scandinavian languages in the dataset (e.g., Danish, Norwegian, Icelandic), making it difficult to generalize the effectiveness of SWEb’s extraction pipeline across the entire language set. The lack of language-specific benchmarks makes it unclear if the extraction model performs equally well across all languages or if it is biased towards Swedish.

Recommendation: Expanding the evaluation to include benchmarks for other Scandinavian languages or adapting HP-MEK for Danish, Norwegian, and Icelandic could enhance the assessment’s robustness. Providing a language-specific performance analysis would offer insights into whether the extraction model’s quality varies across languages and help optimize future language-specific models.

4. Lack of Qualitative Analysis of Extracted Content
Weakness: The quantitative metrics (e.g., token count, perplexity, accuracy) demonstrate SWEb’s improvements but lack a qualitative assessment of the extracted text's relevance or coherence. Without this, it’s challenging to understand how well the extraction model preserves the content’s intended meaning or cultural context, especially when removing ads and navigation elements. The paper does not address the potential for the extraction process to inadvertently remove or alter culturally significant text or nuances.

Recommendation: Including a qualitative evaluation of content extracted by SWEb compared to FineWeb, such as reader surveys or manual inspection of content fidelity, would offer a deeper understanding of its cultural and contextual accuracy. This analysis would help validate the extractor’s ability to maintain high content relevance, especially for Scandinavian-specific terms, phrases, or topics that might be lost during processing.

5. Limited Error Analysis in Content Extraction
Weakness: The paper does not provide an in-depth error analysis for the types of errors encountered during extraction, such as failures to remove advertisements, incorrect content classification, or issues in handling specific webpage structures. This gap makes it difficult to assess the limitations of the extraction model and how it could be improved. The absence of detailed error analysis makes it hard to pinpoint specific weaknesses in the model's architecture or training process.

Recommendation: An error analysis that categorizes extraction mistakes (e.g., missed ads, incorrectly retained menu items, or misclassified headers) would clarify the model’s boundaries and suggest refinements. Detailing any challenges in handling regional dialects or slang in Scandinavian languages would identify areas for improvement in future iterations of SWEb.

6. Computational Expense of the Extraction Process
Weakness: The computational requirements for SWEb’s extraction model, which consumed 20,000 GPU hours on AMD MI250X GPUs, may be prohibitive for many research labs or developers working with limited resources. This factor could limit the pipeline’s accessibility and adoption. The paper does not provide a detailed breakdown of the computational costs associated with each stage of the pipeline, making it difficult to assess where the most significant bottlenecks are.

Recommendation: Considering optimizations in the extraction model, such as fine-tuning on smaller, more frequent batches or experimenting with lighter transformer architectures, could reduce computational demands. Additionally, presenting a cost-benefit analysis comparing SWEb’s compute usage to the downstream performance gains would offer a more balanced view of the pipeline’s scalability and efficiency.

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
6

### Rating Number
6

### Confidence
4

### Summary
The paper describes the creation of a currently largest Scandinavian data set for training language models.
A new method for collecting texts from the web is proposed, based on an encoder model, and compared with a rule-based method.

### Strengths
The data set will be a valuable tool for researching language models and understanding their properties for Scandinavian languages, which are all under-resourced and under-investigated.

### Weaknesses
Some important points about the evaluation are not fully clear.

"Benchmark HP-MEK" is unclear: what was the motivation to created this test set and what was exactly evaluated exactly on it?  
The new text extraction method or language models trained on the extracted texts? 
For language models (section 4.2) it is said that there is 90/10 training/test splitting.
Therefore it is not clear what was involved in evaluations (text extractor or language models or both) and how (on which test set/s).



### Questions
182: What were are the annotators exactly instructed to do? How did they mark the main content? 

195 isn't => is not

200-202: what are the "binary line annotations" exactly? 
Can they be seen in the example in Listing 1?

300-301: What is "trafilatura"? Explanation citation? 

Why is markdown better than plain text? 

308: alternative benchmarks => alternative to what?

309: to evaluate performance on => performance of what? Of the proposed text extraction method? 


315: didn't => did not

351: which model? 

376: on the two test sets -- which ones? the one from 90/10 split and the other is HP-MEK?


Figure 1: what is "en"? It is not discussed in the text.



426: as the desired extraction output is demonstrated instead of encoded as heuristic => the meaning of the sentence is unclear; what does "demonstrated" means? What does "encoded as heuristic" means?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work introduces a new pretraining dataset for Scandinavian languages, as well as a cloze-style evaluation dataset for Swedish language models.

### Strengths
- Usefulness and relevance: Improving the quality and assessing that this quality has indeed improved for LLMs targeting languages other than English is a clearly relevant topic that will have uses even outside of academia.

- Open-source: Authors promise the release of the dataset, benchmark, and utils used to generate/evaluate them.

- Technical details and examples: The paper features many detials about the implementation. Even if it was not open-source, I feel fairly confident that this work could be majorly reproduced.

### Weaknesses
While it's a sound contribution, I'm not sure ICLR is the right venue for this work. It lacks algorithmic or theoretical novelty, and it's rather a (very good) application of well-known NLP principles to process a new dataset for specific languages.

For example, the heuristics mentioned in the paper are very similar to "old" related work, e.g. [1]

https://arxiv.org/abs/1912.07076

### Questions
The pretraining dataset supports Scandinavian languages, but the benchmark targets Swedish. With the Swedish benchmark as a starting point, how much work would it be to generate similar benchmarks for other Scandinavian languages?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents a new pretraining corpus for Scandinavian languages:Swedish, Danish, Norwegian, and Icelandic. To create this data, they propose a new pipeline that uses a model-based text extractor trained with a small amount of human-labelled data on what is considered the main content in a markdown version of an HTML webpage. They contrast their proposed approach against the FineWeb pipeline, which extracts plain text directly from HTML pages. They further introduce a new cloze style test with a dataset, HP-MEK consisting of 460 examples based on the Swedish Scholastic Aptitude Test (Högskoleprovet),  to benchmark pre-trained performance and show that on a small dataset+model setting, their extractor can match the performance of FineWeb filter, despite being simpler in complexity and using an extractor that is only trained with 1380 human-labeled examples.

Once validated, they use this pipeline to create SWEb, which includes 1.01 trillion tokens.

### Strengths
1. The authors present a novel model-based extractor, trained with 1380 human-labelled examples, to identify the main context from documents (HTML converted to markdown).
2. They introduce a new task and benchmark to validate their pipeline against a baseline, FineWeb and show that their pipeline, while being simpler, results in close performance on this task.
3. They present a new pretraining corpus of 1.01 trillion tokens for Scandinavian languages, which will be a valuable resource to the community.

### Weaknesses
1. It is unclear why the authors chose to retain the markdown tags for pretraining (section 4). They also do not explain much about why HP-MEK is a reasonable benchmark for the pretraining setting.
2. No direct analysis is presented on the efficacy of the model-based extractor, given that it is one of the main component of the paper apart from reporting an F1 score. The downstream application in section 4 is useful but it doesn't say much about what this extractor does or is capable of filtering.
3. The dataset pipeline only includes filters like content length, # of alphanumeric characters, and unigram entropy for quality filtering. However, it would have been useful if there was any direct consideration of what is considered high-quality data in the context of pretraining and if additional checks were made in place about safety and fairness of representation in the dataset.

### Questions
See weakenesses.

### Soundness
3

### Presentation
3

### Contribution
2

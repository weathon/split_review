# MMSearch: Benchmarking the Potential of Large Models as Multi-modal Search Engines

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
The advent of Large Language Models (LLMs) has paved the way for AI search engines, e.g., SearchGPT, showcasing a new paradigm in human-internet interaction.
However, most current AI search engines are limited to text-only settings, neglecting the multimodal user queries and the text-image interleaved nature of website information. 
Recently, Large Multimodal Models (LMMs) have made impressive strides. Yet, whether they can function as AI search engines remains under-explored, leaving the potential of LMMs in multimodal search an open question.
To this end, we design the first multimodal AI search engine pipeline, \textbf{\engine}, to empower any LMMs with multimodal search capabilities. On top of this, we introduce \textbf{\dataset}, a comprehensive evaluation benchmark to assess the multimodal search performance of LMMs. The curated dataset contains 300 manually collected instances spanning 14 subfields, which involves no overlap with the current LMMs' training data, ensuring the correct answer can only be obtained within searching. By using \engine, the LMMs are evaluated by performing three individual tasks (requery, rerank, and summarization), and one challenging end-to-end task with a complete searching process.
We conduct extensive experiments on closed-source and open-source LMMs. Among all tested models, GPT-4o with \engine achieves the best results, which surpasses the commercial product, Perplexity Pro, in the end-to-end task, demonstrating the effectiveness of our proposed pipeline. 
We further present error analysis to unveil current LMMs still struggle to fully grasp the multimodal search tasks, and ablation study to indicate the potential of scaling test-time computation for AI search engine. We hope \dataset~may provide unique insights to guide the future development of multimodal AI search engine.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work describes a new pipeline to empower LMMs with multimodal search capabilities called MMSearch-Engine, and introduce MMSearch, a comprehensive evaluation benchmark to assess the multimodal search performance of LMMs which includes 300 high-quality instances across 14 subfields. The study also points out LMMs' challenges in multimodal search and suggests scaling test-time computation could improve AI search engines.

### Strengths
* MMSearch-Engine is a well-designed three steps pipeline that empower LLMs with multimodal search capabilities. 
* MMSearch is a fair evaluation benchmark because its data is all dated later than the model's knowledge base update time.
* Case analysis is comprehensive.

### Weaknesses
* The small amount of data may lead to a certain degree of randomness.
* When constructing the data pipeline, human annotators perform multiple requery operations in cases where no website is classified as valid. Only one requery operation may not fully demonstrate the LMMs' capabilities.

### Questions
* Due to the sequential nature of requery, rerank, and summarization, errors in each step can lead to subsequent errors. How to ensure the reasonableness of the weight of each score in formula 1?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper is about benchmarking LLMs as multimodal search engines. The authors propose:
1) A pipeline that enables this type of multimodal search, where images are translated into textual queries before querying a search engine and summarizing the results.
2) A small, but high-quality dataset as benchmark. They do their best to ensure that there is no information leakage between the LLM's training data and the benchmark, by collecting long-tail knowledge data, and very recent news.
They present results using commercial search engines, closed-source, and open-source LLMS, and show that there is much room for improvement, analysing the sources of error along the way.

### Strengths
1) The paper is very well-written, with excellent presentation and clarity. In my view, the scope is very well-defined, and there is no redundant information.
2) I particularly like that the authors try to create a dataset that LLMs have not seen before.
3) There is a very large appendix with interesting additional experiments and qualitative analysis.

### Weaknesses
1) The way the authors construct the dataset is not future-proof. We have to assume that every piece of news that comes out is immediately ingested, at the very least by large corporations with commercial search engines. In that sense, the benchmark will be obsolete in a couple of months. I would love to see a piece of discussion that proposes a way to make the data collection and annotation pipeline future-proof.
2) The benchmark dataset, even though high quality, is rather small. Maybe I am missing something, but are there any indications that its coverage over the problem space is sufficient?

### Questions
Please, refer to the "Weaknesses" section.

I have another question for the authors that I do not consider a weakness, just interesting: In line 409 you state "Any-resolution input only provides slight or no improvement.". Have you tried to corrupt a clean image with differend kinds of corruptions (e.g., occlusions, blur, gaussian noise, etc.), and see how it impacts the search results?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces MMSearch, a benchmark that evaluates the capacity of large multimodal models (LMMs) as AI-driven search engines for handling complex multimodal queries (text and image). The study proposes MMSearch-Engine, a tailored pipeline enabling LMMs to address multimodal search tasks, divided into stages: requery, rerank, and summarization. Experimental results show that models like GPT-4o, integrated into this pipeline, perform better than current commercial systems, such as Perplexity Pro, in end-to-end multimodal search tasks. The paper presents detailed error analyses, offering insights into the limitations of LMMs in search-oriented subtasks, especially in requery and rerank.

### Strengths
(1) This paper constructs a novel benchmark MMSearch. It fills an important gap in multimodal AI evaluation by focusing on search capabilities and interaction with multimodal data. It offers a unique benchmark that pushes beyond standard image-text alignment tasks.

(2) This paper proposes an effective multimodal retrieval pipeline MMSearch-Engine, which consists of requery, rerank, and summarization. Experiments have shown that this pipeline can effectively improve the performance of the model.

(3) The experimental analysis is comprehensive and provides good reference conclusions. The error analysis and comparison between commercial and open-source models are valuable for understanding current model limitations, providing useful insights for improving multimodal search models.

(4) This paper uses a weighted score of four scores to evaluate the effect of the model, which not only focuses on the correctness of the model's results, but also focuses on the correctness of its process, which can provide a more comprehensive and effective understanding of the model's performance.

### Weaknesses
(1) Although MMSearch covers a wide range of news and knowledge domains, the total number is only 300 instances. Such a number and scale are not enough to fully reflect the generality of the model, etc. The author may need to further expand the scale of the dataset in the future.

(2) Lack of task complexity hierarchy. The complexity of current MMSearch tasks is relatively consistent, lacking a hierarchy of tasks from simple to complex. In the future, tasks of different difficulty levels can be designed to better measure the performance of the model when dealing with tasks of increasing complexity.

(3) There are still limitations in the validation of the model's adaptability. The adaptability of this method in different fields and application scenarios is still unclear, especially on data from special or professional fields (such as medicine or law). Introducing datasets from these fields can more comprehensively evaluate the versatility and adaptability of the model.

### Questions
(1) In future versions, could the pipeline include user feedback to improve task accuracy iteratively?

(2) How general and adaptable is the approach to data from specific or specialized fields, such as medicine or law?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors present MMSEARCH-ENGINE, a multimodal AI search engine pipeline, and MMSEARCH, a comprehensive evaluation benchmark to assess the multimodal search performance of LMMs.

### Strengths
1. This paper introduces the first mm RAG pipeline (at least based on the related work introduced) and the first mm search evaluation.
2. The methods for building the MM RAG pipeline and evaluation are solid and with comprehensive statistics.
3. The methodology statement is easy to follow.
4. Comprehensive experiments.
5. Step-wise evaluation of the RAG pipeline is cool.

### Weaknesses
1. The evaluation data creation pipeline is not efficient, which may result in difficulties to keep the evaluation dynamic.
2. Evaluation data only comprises 300 entries, which is far from comprehensive. Generally, a benchmark should have 1k+ samples to be robust.
3. The authors didn't exhibit the step-wise scores for the proposed RAG pipeline, which harms the result soundness.

### Questions
NA

### Soundness
3

### Presentation
3

### Contribution
2

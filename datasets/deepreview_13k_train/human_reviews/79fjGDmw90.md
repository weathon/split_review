# M3GIA: A Cognition Inspired Multilingual and Multimodal General Intelligence Ability Benchmark

- Decision: Reject
- Scores: 3, 5, 5

## Abstract
As recent multi-modality large language models~(MLLMs) have shown formidable proficiency on various complex tasks, there has been increasing attention on debating whether these models could eventually mirror human intelligence.
    However, existing benchmarks mainly focus on evaluating solely on task performance, such as the accuracy of identifying the attribute of an object. Combining well-developed cognitive science to understand the intelligence of MLLMs beyond superficial achievements remains largely unexplored. To this end, we introduce the first cognitive-driven multi-lingual and multi-modal benchmark to evaluate the general intelligence ability of MLLMs, dubbed \ours{}. Specifically, we identify five key cognitive factors based on the well-recognized Cattell-Horn-Carrol~(CHC) model of intelligence and propose a novel evaluation metric. In addition, since most MLLMs are trained to perform in different languages, a natural question arises: is language a key factor influencing the cognitive ability of MLLMs? As such, we go beyond English to encompass other languages based on their popularity, including Chinese, French, Spanish, Portuguese and Korean, to construct our \ours{}. We make sure all the data relevant to the cultural backgrounds are collected from their native context to avoid English-centric bias. 
    We collected a significant corpus of data from human participants, revealing that the most advanced MLLM reaches the lower boundary of human intelligence in English. Yet, there remains a pronounced disparity in the other five languages assessed. We also reveals an interesting \emph{winner takes all} phenomenon that are aligned with the discovery in cognitive studies. Our benchmark will be open-sourced, with the aspiration of facilitating the enhancement of cognitive capabilities in MLLMs.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents a benchmark M3GIA which claims to act as the first “IQ test” for multimodal large language models (MLLM). It is built based on five cognitive factors from the Cattell-Horn-Carroll Model of Intelligence. It includes VQA/text-format questions from tasks like oral vocabulary, concept formation, visualization, math, reading and etc. Besides English, it also includes other languages such as Chinese, French, Spanish, Portuguese and Korean. The authors evaluate their benchmark on a number of API-based and open-source models across different scales as well as human participants. They observe that the best MLLM (GPT4-o) can reach the lower boundary of human performance in English.

### Strengths
The paper presents an interesting perspective for constructing benchmarks and suggests we can design benchmarks based on previous cognitive science studies. The contribution of the new resources can be helpful and raise more questions and considerations about benchmark design. They also provide an initial performance analysis of some of the existing models, which can be used as a reference for future research.

### Weaknesses
While the authors claim that M3GIA can serve as an IQ test for MLLMs and have built this benchmark based on existing cognition theory, I find it hard to conclude generally that “most advanced MLLM reaches the lower boundary of human intelligence in English”. There are many different categories of questions collected in this benchmark and they can fall under different cognitive factors. However, it is unclear what control factors are in place during the data collection and evaluation process: why this specific type of question is chosen? How are the variances of questions controlled across languages? How broad/narrow is the topic tested in each domain? What are the sample demographics of the annotators? Given there are only 300 questions tested per language, it’s hard to prove that the human responses collected represent the lower bound of human intelligence. The cognitive load experienced by human test takers is not a factor for models, therefore the conclusion that models reach the lower bound of human intelligence based on a test designed for humans is questionable.

### Questions
- Can you provide more details about how you decide the question category under each factor and how is each question selected for each category? Is there any data filtering or quality inspection process from experts to determine whether each question is easy/hard enough to be included?
- How does this dataset differ from other reasoning benchmarks besides it is “cognition-inspired”? If the importance lies in its originality, why do you also include datapoints from other datasets?

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
5

### Summary
This paper introduced a cognitive-driven multi-lingual and multi-modal benchmark, dubbed M3GIA, to evaluate the general intelligence ability of multi-modality large language models (MLLMs). Based on the Cattell-Horn-Carroll (CHC) model from cognitive science, the authors build a benchmark including 1.8K QAs annotated by native speakers in five languages. Experiments and analysis on 24 MLLMs show the significant disparities between MLLMs and human performance.

### Strengths
- Based on the CHC theory, this paper brings a new perspective to the MM community for constructing multi-modal benchmarks aimed at evaluating modern MLLMs in terms of human-level intelligence. The background and taxonomy of the CHC theory are clear and meaningful.
  - As a benchmark, the multi-modal QAs annotated by humans are of high quality and useful.
  - The evaluation of both open-source and closed-source MLLMs is extensive and thorough.

### Weaknesses
 - Though starting from a new perspective of the CHC theory, this paper still evaluates the widely adopted capabilities of MLLMs that have been investigated in previous benchmarks, such as Visual-Spatial Processing, Knowledge, Math Facts, and Text Reading. For example, the MM-vet benchmark builds QAs related to the capabilities of OCR, Math, Knowledge, and Language Generation, using LLMs as examiners to evaluate open-ended generations. The performance of MLLMs in Table 1 also demonstrates a consistent trend between M3GIA and other general multimodal benchmarks, rather than revealing distinct findings.
  - This paper spend extensive content to introducing the CHC model within the main content. However, one point still remains unclear to me: how does the CHC model affect the capabilities of MLLMs? In other words, what specific attributes or behaviors would a powerful MLLM, grounded in CHC theory, exhibit? Are there any case studies or pilot experiments that illustrate the significance of this influence?
  - The paper is missing detailed statistical information about the proposed benchmark, such as the number of images per category and the average number of words in the generated questions.
  - The paper’s experimental section appears to be incomplete due to the absence of results for the few-shot setting.

### Questions
- For the Human Performance Baseline, I believe that these results are important for reflecting the difficulty of the created benchmark. What are the educational levels of the participants, and how is the quality of the created questions ensured?

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
4

### Summary
This paper introduces the concept of a cognitive-driven, multilingual, and multimodal benchmark to evaluate the general intelligence of MLLMs, referred to as M3GIA. The benchmark is grounded in the well-established Cattell-Horn-Carroll (CHC) model of intelligence and proposes a novel evaluation metric. It is open-sourced and aims to enhance the cognitive capabilities of MLLMs.

### Strengths
1. The use of a taxonomy of cognitive abilities to evaluate the general intelligence of MLLMs is good, as it enables a more systematic evaluation.
2. The benchmark is constructed using unpublished offline data, which is a good practice to prevent data leakage.
3. The benchmark includes multiple language variants, allowing for the evaluation of MLLMs’ general intelligence across different languages.

### Weaknesses
1. While the paper mentions that several specific factors from the CHC model of intelligence were selected (lines 237-250), it is unclear why these particular factors were chosen and how they relate to the general intelligence of MLLMs. Specifically, the paper does not provide a clear rationale for why certain CHC factors are more relevant for evaluating MLLM intelligence than others. This lack of justification weakens the theoretical foundation of the benchmark.
2. Although incorporating cognitive science into the evaluation of MLLMs is a positive step, the underlying tasks remain traditional, such as Math, Logo Problem, and Comic Problem. This may detract from the benchmark’s novelty. Given that recent works like MMMLU also include multilingual variants, it is not clear how M3GIA is fundamentally different from MMMU. The tasks used, while mapped to CHC factors, do not appear to be inherently novel in their design or execution. The reliance on existing task types raises concerns about the benchmark's ability to provide a unique and comprehensive assessment of MLLM intelligence. Furthermore, the paper does not adequately address why existing benchmarks could not be adapted or reorganized to align with the CHC framework.
3. The paper introduces numerous cognitive concepts and abbreviations, which may make it difficult for readers unfamiliar with cognitive science to follow. For instance, the meaning of “Fluid Reasoning (Gf)” (line 97) in the context of MLLMs is not clearly explained. In my personal aspect, I feel odd about the term "Fluid Reasoning (Gf)" what does it mean?

### Questions
1. Is it possible to reorganize existing multi-task, multimodal benchmarks (e.g., MMMLU) to follow the taxonomy of cognitive abilities to evaluate the general intelligence of MLLMs? If not, could you explain why? Does the MMMLU benchmark lack specific tasks that would prevent it from capturing certain cognitive abilities?

[1] https://huggingface.co/datasets/openai/MMMLU (Multi-Language Variant of MMMLU)

### Soundness
3

### Presentation
2

### Contribution
2

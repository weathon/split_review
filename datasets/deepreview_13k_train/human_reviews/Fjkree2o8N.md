# OIDA-QA: A Multimodal Benchmark for Analyzing the Opioid Industry Document Archive

- Decision: Reject
- Scores: 5, 5, 3, 5

## Abstract
The opioid crisis is a serious public health issue that requires innovative solutions for effective analysis and deeper understanding. 
Despite the vast amounts of data in the Opioid Industry Documents Archive (OIDA), the complexity, multimodal nature, and specialized characteristics of healthcare data necessitate more advanced methods and models tailored to specific data types and detailed annotations, ensuring the precision and professionalism in the analysis.
In this paper, we tackle this challenge by organizing the original dataset according to document attributes and constructing a benchmark with 400k training documents and 10k for testing. We extract extensive multimodal information from each document, including textual, visual, and layout information, to capture a wide range of features. Given the extracted dense information, we collect a comprehensive dataset comprising over 3 million question-answer pairs with the assistance of multiple AI models. 
We further develop domain-specific Large Language Models (LLMs) and investigate the impact of multimodal data on task performance.
Our benchmarking and model efforts strive to produce an AI assistant system which can efficiently process the dataset and extract valuable insights.
Preliminary results indicate the improvements with our AI assistant in document information extraction and question-answering tasks, highlighting the effectiveness of proposed benchmark in addressing the opioid crisis.
The data and model will be made publicly available for research.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces OIDA-QA, a new multimodal question-answering benchmark designed to analyze the Opioid Industry Documents Archive (OIDA). Acknowledging the complexity and multimodal nature of the data—including text, images, and layout—the authors reorganize the original dataset into training documents and testing documents. They extract comprehensive multimodal information from each document to capture diverse features. By generating over 3 million question-answer pairs using AI models and incorporating persona-based question generation, they aim to simulate diverse user interactions. The authors develop domain-specific LLMs using LoRA, focusing on cluster-specific adaptation to enhance performance. Experimental results demonstrate improvements in document information extraction and question-answering tasks, suggesting that their approach effectively addresses challenges associated with the opioid crisis.

### Strengths
1. The paper presents a novel benchmark tailored to the opioid crisis, addressing a timely public health issue. By focusing on the OIDA, the authors provide a unique resource for analyzing complex, multimodal healthcare data.

2. The methodology is thorough and well-executed. The authors analyze the dataset's distribution, perform balanced sampling, and extract detailed multimodal information.

### Weaknesses
1. The experimental results primarily focus on quantitative metrics, leaving out an in-depth qualitative evaluation of the model outputs. Including case studies or practical examples demonstrating the effectiveness and real-world applicability of the generated answers would enhance the paper's impact and provide a clearer understanding of the model's performance.

2. The paper does not sufficiently explain the rationale behind simulating users through diverse personas encompassing various backgrounds, experiences, and hobbies. The inclusion of personas such as Music Producer and Professional Composer (in the Appendix) raises questions about their relevance to the task. A more thorough justification is needed to clarify how these personas contribute to the dataset and the overall objectives.

3. The data generation process relies entirely on GPT-4 models. To ensure the validity, reliability, and quality of the dataset—particularly the test set—it is important to include human (expert) evaluation.

4. Apart from using documents from the Opioid Industry Documents Archive (OIDA), the paper does not introduce any novel methodologies specifically designed to address the opioid crisis. The approach seems to be a general application of multimodal document question-answering techniques, which could equally be applied to other datasets such as PubMed articles. This raises concerns about the paper's unique contribution to tackling the opioid crisis beyond dataset curation.

### Questions
Please refer to the Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work aim at supporting research and the developments of tools to support health systems with opioid-related tasks. The authors introduce OIDA-QA, a new question-answering (QA) benchmark focused on opioid data, drawn from the Opioid Industry Documents Archive (OIDA). This multimodal QA benchmark includes data enrichment techniques to make the unstructured content of the OIDA's scanned and complex PDF documents more accessible. In addition, the benchmark incorporate persona-based question generation, simulating user questions from different professional and personal backgrounds. The model training process is optimized with LoRA to create a low-cost and scalable system.

### Strengths
New QA benchmark for a specific (largely unexplored) domain where there is no or little open-data available.

### Weaknesses
To build the datasets authors made choice that are not fully explained in the paper. More details would help the reader to get a full understanding of the building process (see my questions below).

- Is there any previous work where persona hub was used? From the paper, it is unclear to me to understand the impact of using it and what type of errors can be generated. 
- Evaluation is done using mostly overlapping metrics. While the field doesn't have yet a unique way of evaluating LLM outputs, I believe that some automatic metric would be helpful to assess other dimensions (faithfulness, correctness etc) beyond word overlap.
- Authors introduced the dataset as a resource to have models tailored to specific data types and detailed annotations. However, I found two things missing: 1) a more broaden description of possible real-world use cases that can benefit from this dataset, 2) an evaluation zero-shot using large SOTA models (do we know to which extend this information is already available in the parametric knowledge of large models?).

### Questions
- Is there any previous work where persona hub was used? From the paper, it is unclear to me to understand the impact of using it and what type of errors can be generated. 
- Evaluation is done using mostly overlapping metrics. While the field doesn't have yet a unique way of evaluating LLM outputs, I believe that some automatic metric would be helpful to assess other dimensions (faithfulness, correctness etc) beyond word overlap.
- Authors introduced the dataset as a resource to have models tailored to specific data types and detailed annotations. However, I found two things missing: 1) a more broaden description of possible real-world use cases that can benefit from this dataset, 2) an evaluation zero-shot using large SOTA models (do we know to which extend this information is already available in the parametric knowledge of large models?).

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper aims to build a AI models to assist information extraction and question-answering on Opioid Industry Documents Archive (OIDA).  To address this the paper introduces a methodology to automatically generate question-answer pairs using AI models which are then leveraged to train AI assistants.  The method follows these steps (1) Extract multimodal  (text, visual, layout etc) information for each PDF document (2) Cluster the documents based on structured taxonomy (3) For every cluster, sample personas from a persona Hub and  generate QA pairs using AI models given the persona of the user asking the question (3) Utilize the QA pairs to train QA models using LLMs.

### Strengths
The paper explores an innovative domain by advancing question-answering capabilities on PDFs that contain multimodal information. It also introduces a novel methodology to effectively address this challenge.

### Weaknesses
Its unclear how useful the overall generation framework is and would be helpful to address the following questions 

(1) Its unclear how and if the generated questions are closer to real user questions. Some form of human evaluation or user rating od the system would give a better idea. 
(2) What is the effect of using these different modalities in the generation? Can you perform an ablation study, where you remove the information from one of the modalities (text or image etc) and how does this effect the generation process, downstream model performance and hence user satisfaction ?
(3) How generalizable is the framework ? What other related domains can this framework be applied to  and what are limitations?

### Questions
It would be helpful to receive a response from the authors on the questions described above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a new dataset, OIDA-QA, an Opioid Industry Document Archive Question-Answering dataset, which consists of over 400k samples with multimodal information (textual, visual, and layout) using an automated process of generating QA pairs using GPT-4o, while considering various types of questions for different human personas. For the experiments, the authors implement multiple models tailored to different document taxonomies and demonstrated that their proposed cluster-specific modeling approach can be a promising method for tackling QA for multimodal document understanding.

### Strengths
- The paper is well-motivated and easy to follow.
- This can be a significant contribution to multimodal document understanding.

### Weaknesses
 - What is the procedure to ensure the quality of the QA data? I am sure it required tremendous effort just to create the data itself, but at least the test set should require some verification by humans or other solutions to ensure that a higher score truly reflects true positives and not false negatives.
- Although the authors show various performances, it would be helpful to have a reference for what is a 'good' score. For example, achieving some score could indicate that the model outperforms humans or some state-of-the-art models like GPT-4 in the main results table. This can further help readers to grasp what these score mean.
- More direct applications for solving this task in terms of machine learning (perhaps separated by each cluster). For instance, scoring high on questions in cluster 1 indicates that the model requires capabilities A, B, and C.
- How do we determine which category new questions belong to? Also, what is the rationale for disregarding unused clusters, rather than merging them into an 'out-of-distribution' cluster? My concern is not all questions may fit neatly into the 10 predefined clusters, especially if we aim to tackle the opioid crisis with AI-driven automation.

### Questions
- What are some representative examples from each cluster? Also, what insights can we gain from a model that achieves high performance on questions in, say, cluster 1?
- I am willing to raise the score if my concerns in the weakness and question parts are resolved.

### Soundness
3

### Presentation
3

### Contribution
3

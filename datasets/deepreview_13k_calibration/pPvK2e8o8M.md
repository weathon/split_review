# Teach Large Language Models the Concept of Meta-cognition to Reduce Hallucination Text Generation

- Decision: Reject
- Avg Score: 3.25
- Scores: 6, 3, 1, 3

## Abstract
We introduce an algorithm that endows language models with enduring meta-cognitive capabilities.  Inspired by meta-learning, our approach involves fine-tuning models on diverse datasets, including the original base model. Throughout each training iteration, we randomly select various fine-tuned model versions, gauge their meta-cognitive capacities, and employ the meta-cognitive error average as the loss function for gradient updates. This empowers these models to assess their competence when interpreting human instructions, thereby averting the generation of responses beyond their abilities and mitigating hallucinatory text production. The meta-cognitive ability will be adapt to various fine-tuned versions of the main model, providing evaluations that align with the fine-tuned models' knowledge capacity.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces an algorithm designed to equip language models with enduring meta-cognitive capabilities. Drawing inspiration from meta-learning, the approach involves a process of fine-tuning models on diverse datasets, including the original untuned base model.

what contributions does it make:
1.This approach allows models to self-assess their competence when interpreting human instructions. 
2.This method improves the model's response quality by preventing responses beyond their learned capacities and reducing the generation of misleading or hallucinatory text.
3.The paper provides a new ground truth dataset for evaluating large language models.

### Strengths
1.The paper is written in an easy-to-understand manner.
2.The meta-cognitive ability adapts to the various fine-tuned versions of the primary model. This adaptability offers evaluations aligned with the knowledge capacity of the fine-tuned models. 
3.In each training cycle, the algorithm randomly selects multiple fine-tuned model versions and evaluates their meta-cognitive abilities.

### Weaknesses
1.The experiment conducted was inadequate, relying solely on ChatGLM-6B, which possesses a limited knowledge base. This severely restricts the generalizability of the findings. The model's performance on more robust and widely used models, such as those in the LLaMA or GPT families, remains unknown. The lack of diversity in the base models tested makes it difficult to ascertain whether the observed meta-cognitive abilities are a genuine property of the proposed algorithm or an artifact of the specific model architecture and training data of ChatGLM-6B.
2.Table 1 lacks any analysis or interpretation. The raw numbers presented without any discussion of their statistical significance or practical implications makes it hard to understand the results. For example, it is unclear what the specific metrics in Table 1 represent, how they were calculated, and what constitutes a good or bad score. Without this analysis, the table provides limited value to the reader.

### Questions
1.In the dataset constructed in this paper, the questions must be in line with objective facts, and they are all in English, can this be extended to a more general situation? How well does the model generalize outside of these specific scenarios?
2.Compared with MAML, what do the support data and query data correspond to in the algorithm proposed in this paper?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces an algorithm that endows language models with persistent metacognitive capabilities.  This empowers these models to evaluate their competence when interpreting human instructions, thereby avoiding the generation of responses beyond their abilities and mitigating the production of hallucinatory text.

### Strengths
The paper presents a highly innovative concept, utilizing the idea of meta-learning to address hallucinations. It is also the first method to mitigate hallucinations before the model's output. In terms of writing, the introduction of hallucination-related terms at the beginning of the article uses numerous vivid metaphors, making it very easy to understand and read.

### Weaknesses
1、This article seriously lacks quantitative experimental results to verify the effectiveness of the method. The claim of the entire paper does not have sufficient experimental support.

2、However， there is also a lack of theoretical discussion further validating the method's effectiveness.

2、Additionally, due to the need for a substantial number of fine-tuned models, practical application can be challenging.

### Questions
The phrase "Reduce Hallucination Text Generation" in the title seems awkward. A more appropriate expression  could be "Reducing Hallucinations in Text Generation" or "Reducing Hallucinatory Text Generation".

### Soundness
1 poor

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors introduce an algorithm designed to equip language models with sustained meta-cognitive abilities, drawing inspiration from meta-learning principles. The paper introduces an algorithm designed to endow large language models with metacognitive abilities, allowing them to evaluate their own capacity to generate responses to human instructions, and as a result, curtail the production of responses when the model is not adequately equipped to answer, significantly diminishing the incidence of hallucinatory text generation. Additionally, the authors present a novel ground truth dataset, encompassing 16,000 questions spanning 160 meticulously categorized domains, which can be utilized for fine-tuning and evaluating large language models.

### Strengths
This submission set eyes on an interesting topic of introducing meta-learning to LMs so as to address the issue of hallucination. Their efforts in putting together a manuscript for this submission are acknowledged and appreciated.

### Weaknesses
(1) The manuscript’s clarity and structural integrity could be greatly improved. The format of the manuscript leans more towards a school report than a scholarly research paper, and it currently presents challenges in understanding the main contributions and claims:
* The motivation and main goal of the study need clearer definition; it’s uncertain whether the focus is on addressing hallucination in text generation or applying meta-learning to LLMs. The paper does not clearly articulate the problem being addressed. Is the goal to reduce hallucination, or is it to explore meta-learning in LLMs, or both? This lack of clarity makes it difficult to assess the significance of the work. The connection between meta-learning and hallucination reduction is not well-established, making the motivation unclear.
* The transition from discussing hallucination in Section 2 to model selection and metacognitive capabilities in Section 3 is abrupt and confusing. A more systematic introduction to the problem, followed by the detailed methodology, would enhance comprehension. The paper jumps from a general discussion of hallucination to a specific model and algorithm without adequate justification. The reader is left wondering why this particular approach was chosen and how it directly addresses the hallucination problem. A more gradual and logical flow is needed to connect the problem, proposed solution, and methodology.


(2) The design and execution of the experiments require substantial revision to robustly support the authors’ claims:
* Clarification is needed on the specific text generation task under study. Text generation is a very broad domain with many subtasks. The authors mention summarization and dialogue generation in the related work, but later train the model with QA setup. What exactly is the task that this work is trying to study? The paper lacks a clear definition of the text generation task being addressed. Is it question answering, summarization, dialogue, or something else? The experimental setup uses a QA format, but this is not explicitly stated as the focus of the work. The lack of a clearly defined task makes it difficult to evaluate the results and compare them to other work.
* Why did the authors choose ChatGLM-6B? Is it because this model is bilingual? Then why didn’t the authors compare to other multilingual models such as BLOOM? Is it because this model supports multi-turn dialogue? Then there are also other dialogue models/chatbots available. Why didn’t the authors compare to any of these related baselines? The choice of ChatGLM-6B is not justified. The authors should provide a rationale for this selection and compare it to other relevant models, including multilingual and dialogue-focused models. Without these comparisons, it's impossible to assess the relative performance of their approach.
* The evaluation metrics need a detailed description, and the results presented in the tables require thorough analysis and interpretation. The paper does not provide sufficient detail on the evaluation metrics used. The metrics should be clearly defined, and the results should be thoroughly analyzed and interpreted. The current presentation of results is insufficient to support the claims made by the authors.
* The authors mentioned that there are a number of benchmarks for evaluating hallucination in text generation, then why didn’t the authors report results on any of these benchmarks? The lack of evaluation on standard hallucination benchmarks is a significant weakness. The authors should compare their approach to existing methods on established benchmarks to properly assess its effectiveness.


(3) This submission did not mention a number of related works throughout the manuscript:
* In the introduction, the authors briefly mentioned that metacognition is a concept in psychology, but did not point to any related studies. The paper should include references to foundational work in metacognition from psychology to provide a more thorough background.
* The authors mention that their “algorithm draws inspiration from meta-learning”, but did not discuss any previous work on meta-learning. The paper should discuss relevant meta-learning literature and explain how their approach builds upon existing work in the field.


(4) Typos, formatting issues, etc:
* Unpaired quotation marks: (e.g., Section 1: ”hallucination”);
* Missing reference when mentioning GPT-3, PaLM, Llama, etc in Section 3.1;
* Misused citation format: e.g., Section 2: “Another approach is shown in (Feldman et al., 2023)” -> the parentheses around the citation are unnecessary and should be removed to adhere to standard citation practices;
* Table 5 and tables in the appendix extend beyond the page width;
* What makes Figure 1 a figure? It appears to be two tables to me.

### Questions
Please kindly refer to the questions raised in the Weaknesses section.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces the concept of "metacognition", which refers to the model's ability to accurately self-evaluate one's own capabilities before generating text. They then propose to equip language models with this ability by first using ChatGPT to generate factual question-answer pairs in different domains, and then finetuning ChatGLM with LoRA in a meta-learning style. They claim that their model learns metacognitive abilities after training.

### Strengths
1. The paper constructs a factual question-answering dataset that can be helpful for future research.

### Weaknesses
1. One major weakness of this paper is that the concept of "metacognition" is not formally defined. In the introduction part, it mentions that it is the model's ability accurately self-evaluate one's own capabilities before generating text. However, no formal definition is presented and it is unclear how we can quantify such abilities. Therefore, it is unclear to how to evaluate a model's metacognition abilities and the experiments cannot support their claims such as "their models can learn metacognitive abilities after training."
2. The paper proposes several hypotheses that may be ungrounded. For example, in the introduction part they claim that "RLHF is the main source of hallucination of recent LLMs", but MLE-trained models can also hallucinate and RLHF can help with reducing hallucinations [1]. There are also other kinds of similar claims in the introduction section such as "LLMs are not enough to fit the world’s model."
3. The writing of the paper lacks coherence. For example, they have put a lot of efforts on writing the retrieval-augmented models but didn't compare or use them. Also, it is unclear how one can reframe the task of "instilling in LLMs the discretion to search only when absolutely necessary" to "teach LLMs to accurately self-evaluate their own capabilities before generating text." Teaching LLMs to self-evaluate their own capabilities is one way to implement this task, but they are not interchangeable.
4. There are related works on model calibration and retrieval-augmented models that they didn't discuss in depth.

### Questions
1. How do you quantify "meta-cognition"?
2. What is the difference between "meta-cognition" and "model calibration"?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

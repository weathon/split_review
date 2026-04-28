# Synthetic Data (Almost) from Scratch: Generalized Instruction Tuning for Language Models

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 5, 6

## Abstract
We introduce \mbox{\emph{Generalized Instruction Tuning}} (called \our{}), a general and scalable method for instruction tuning of Large Language Models (LLMs). 
Unlike prior work that relies on seed examples or existing datasets to construct instruction tuning data, 
\our{} exclusively utilizes a pre-curated taxonomy of human knowledge and capabilities as input and generates large-scale 
synthetic instruction data across all disciplines.
Specifically, inspired by the systematic structure in human education system, we build the taxonomy by decomposing human knowledge and capabilities to various fields, sub-fields and ultimately, distinct disciplines semi-automatically, facilitated by LLMs. 
Subsequently, we generate a comprehensive list of subjects for every discipline and proceed to design a syllabus tailored to each subject, again utilizing LLMs.
With the fine-grained key concepts detailed in every class session of the syllabus, we are able to generate diverse instructions with a broad coverage across the entire spectrum of human knowledge and skills. 
Extensive experiments on large language models (e.g., Mistral) demonstrate that \our{} excels in multiple dimensions from mathematical reasoning, coding, academic exams, logical reasoning to general instruction following without using task-specific training data of these tasks. In addition, \our{} allows for easy customization and new
fields or skills can be added by simply incorporating a new node into our taxonomy.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The submitted paper introduces GLAN as a method for instruction tuning of LLMs with synthetic data generated without seed examples or pre-existing datasets. The proposed approach structures synthetic data based on a taxonomy that decomposes human knowledge systematically, inspired by the educational system.

Key Contributions:
1. Novel Data Generation Approach: This intuitive and inspiring taxonomy-based instruction generation method ensures broad coverage across various knowledge domains.
2. Scalability and Customization: GLAN's structure enables the easy addition of new fields by incorporating new nodes into the taxonomy, making it a scalable and adaptable solution for future advancements in LLMs.

### Strengths
Originality: The paper introduces a novel, taxonomy-driven approach to instruction tuning inspired by structured education systems, moving beyond the traditional reliance on seed examples and transforming data creation into a structured method rather than uncontrolled expansion. By systematically decomposing human knowledge, GLAN enables broader and more versatile LLM tuning in an organized manner, marking a creative adaptation of structured learning for AI.

Quality: The methodology is detailed and robust, employing models like GPT-4 and GPT-3.5 to ensure quality and incorporating human oversight to reduce hallucination. Extensive experiments demonstrate strong results across multiple benchmarks, highlighting the model’s adaptability and thoughtful experimental design.

Clarity: The paper is well-organized, with each component of the GLAN process clearly explained. A detailed appendix provides additional information for deeper exploration. Figures and tables effectively illustrate benchmark results and comparisons, making the model’s strengths easy to understand.

Significance: By supporting easy expansion into diverse fields and facilitating curriculum-based learning, GLAN addresses the demand for larger, more capable models. It enables the creation of expansive and diverse datasets, establishing a new approach to improving dataset quality. GLAN’s scalable, customizable approach to synthetic data generation holds significant potential for advancing multi-domain LLMs and enhancing general model capabilities.

### Weaknesses
Human Effort and Taxonomy Standardization: The taxonomy creation phase includes a human verification step, but the exact extent of human involvement and the criteria for removing items from the taxonomy are not clearly defined. It would be helpful to clarify the standard used for verifying and potentially removing fields, sub-fields, or disciplines to improve the reproducibility of the approach. Establishing more detailed criteria for this step could ensure consistency and transparency, as well as allow other researchers to adapt this approach efficiently. Specifically, the paper lacks details on the number of human annotators involved, the specific instructions given to them, and the process for resolving disagreements. This lack of clarity makes it difficult to assess the potential for bias or inconsistency in the taxonomy's construction. Furthermore, the paper does not discuss the potential impact of different annotators or annotation strategies on the final taxonomy. 

High Computational Cost and Open-Source Model Viability: The paper relies heavily on closed-source models like GPT-4 and GPT-3.5, which incur significant costs. It remains unclear whether switching to open-source models would provide comparable performance. Investigating the performance trade-offs when using state-of-the-art open-source models, such as LLaMA 3, could offer a more cost-effective alternative while maintaining accuracy. The paper should include a more detailed analysis of the computational resources required for the proposed method, including the time and cost associated with generating the synthetic data. This analysis should also consider the potential for scaling the method to larger datasets and more complex taxonomies. Including a discussion on the feasibility of using open-source models, with supporting experiments if possible, would improve accessibility for researchers with limited resources.

### Questions
1. Clarification on Human Effort in Taxonomy Creation:
- Question: Could you elaborate on the level of human involvement in this pipeline? Specifically, how much human intervention is required, and what criteria or standards are used to decide which fields, sub-fields, or disciplines to retain or remove? Additionally, could you explain the underlying rationale for determining where human involvement is necessary versus where it is not?
- Suggestion: Providing more details on the standards for pruning the taxonomy would enhance transparency and reproducibility. Examples of cases where human verification led to the removal or modification of specific fields would also help clarify the reasoning behind the taxonomy’s final structure, offering insights into the decision-making process in this stage.

2. Exploring Open-Source Model for Data Generation:
- Question: If data generation in GLAN were performed using open-source models, such as LLaMA 3, how would its performance levels compare to those obtained with GPT-4 and GPT-3.5?
- Suggestion: Given the high computational cost associated with using GPT-4 and GPT-3.5, conducting an experiment with open-source models would add valuable insights. A comparative analysis of GLAN’s performance across various model sizes and types could illustrate its adaptability and provide practical guidance for researchers with different resource constraints. This would be especially useful in determining GLAN’s cost-effectiveness and accessibility.

### Soundness
4

### Presentation
4

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
The paper presents GLAN (Generalized Instruction Tuning for Language Models), a scalable framework for generating synthetic instruction data to fine-tune Large Language Models (LLMs). GLAN's approach diverges from traditional methods by using a taxonomy of human knowledge and capabilities instead of seed examples or existing datasets. Inspired by educational structures, GLAN constructs synthetic instructions across disciplines by defining fields, sub-fields, and subjects, which are further detailed in-class sessions with key concepts. Using GPT-4 and GPT-3.5, the system generates extensive synthetic instruction datasets, demonstrating high performance across benchmarks.

### Strengths
1. This paper proposes a general method for generating synthetic instruction-tuning data, which can be easily scaled up to millions of samples. 
2. The paper is well-written and easy to follow.    
3. The performance of the model trained by this method is strong and promising.

### Weaknesses
1. The novelty of this paper might be limited.
[1] Enhancing Chat Language Models by Scaling High-quality Instructional Conversations.
This paper tries to first construct questions about worlds, and then generate instruction-tuning data based on them. 
[2] Instruction Tuning with Human Curriculum.
This paper tries to construct datasets similarly from the education perspective. 
[3] A Survey on Knowledge Distillation of Large Language Models.
It seems that in this paper, there is a whole subsection “KD Algorithms-Knowledge-Curation” that is generating data (almost) from scratch. Do these papers relate to your method?
I think at least these papers should be discussed. 
2. Although this paper mentioned the scalability of this method, it seems that it largely depends on high-cost APIs, especially when millions of API calls are required. 
3. The dataset proposed in this paper seems not to contain multi-turn conversations, which are crucial for many practical applications.

### Questions
1. Is the human evaluation really necessary? The involvement of humans might make the process hard to scale up automatically.

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
5

### Summary
This paper introduces a Generalized Instruction Tuning (GLAN) framework for LLM's instruction tuning. The authors leverage GPT4 to build a knowledge taxonomy on various fields, and sequentially ask GPT4 to break down fields into subfields, disciplines, subjects, syllabus, class sessions, and key concepts. After that, they repeatedly prompt GPT4/GPT3.5 to generate instruction-tuning data (including questions and answers) according to randomly sampled class sessions and key concepts within a syllabus. Finally, 10M instruction-response pairs are generated to align a pre-trained LLM (e.g., Mistral) to a chatbot via instruction tuning.

### Strengths
1. Building the knowledge taxonomy and structure is an effective approach to ensuring diversity and knowledge coverage when generating training samples.
2. The curated 10M instruction-response pairs are valuable for the LLM community.

### Weaknesses
1. My core concern lies in the novelty.  Basically, GLAN is distilling GPT4 to generate instruction-response pairs, and the idea of constructing a knowledge structure has also been explored by previous works[1][2]. I hope the authors can clarify their research contribution.
2. The scalability of the proposed method is questionable. For the human verification of knowledge taxonomy, there seems 126 * 200 * 30 * 5 = 3M key concepts according to Section 3.1, and the human checking cost is definitely not 'limited' as claimed by the authors. For the data generation by GPT models, this paper queried GPT4/3.5 for 10M times and cost at least 42K USD, which is far more expensive than current data generation methods.
3. The presentation of the proposed knowledge taxonomy is confusing. It is recommended to add a figure or a table in the early pages of this paper, to illustrate the definition, examples, and final quantity of the knowledge hierarchy (fields, subfields, disciplines, subjects, syllabus, class sessions, and key concepts).
4. The experiments are insufficient. The method is only evaluated on the Mistral model.

### Questions
1. According to Section 2.1, is the field-subfield-discipline hierarchy discarded after collecting the leaf nodes of the discipline list？ 
2. In Table1, why is the performance of Mistral-Instruct worse than the base model Mistral on MBPP, GSM8K, and MMLU?

### Soundness
2

### Presentation
2

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
The introduces Generalized Instruction Tuning (GLAN), a novel method for large-scale instruction tuning of language models. Unlike previous methods that rely on seed examples or existing datasets, GLAN creates synthetic data using a pre-defined taxonomy of human knowledge. This taxonomy is derived from a structure similar to human education systems and is used to generate diverse instructions across various domains. GLAN's approach is scalable, customizable, and supports adding new fields by incorporating new nodes into the taxonomy. Extensive experiments demonstrate that GLAN improves performance across a range of tasks, including mathematical reasoning, coding, and general instruction following, without using task-specific training data.

### Strengths
Scalability and Coverage: GLAN generates synthetic instruction data across a broad range of domains using a hierarchical taxonomy of human knowledge, ensuring comprehensive coverage and scalability without relying on pre-existing datasets.

Customization and Flexibility: The method allows for easy integration of new fields or disciplines by adding nodes to the taxonomy, providing flexibility for expanding the instruction tuning process to emerging or niche areas.

Strong Empirical Performance: Extensive experiments show that GLAN significantly enhances model performance in tasks like mathematical reasoning, coding, and academic exams, outperforming or matching state-of-the-art models without task-specific data.

### Weaknesses
Method Feasibility: The method is somewhat novel, but its feasibility in the real world is questionable. While the comparative methods could generate instructions for self-training, I suspect that GLAN is bounded by the knowledge of the generator, e.g., GPT-4 in this paper. It significantly impedes the deployment of GLAN as a method to instruction-tune frontier models, if not to distill from GPT-4 with yet another trick.

Baselines: With the last point being said, at least a few comparative methods to generate instructions, like self-instruct or evol-instruct, should be compared with GLAN. After all, the paper claims the instruction generation method as its core contribution. However, no baseline method is even compared.

Lack of Evaluation on Bias and Ethical Concerns: The paper acknowledges the potential risks of amplifying biases in generated data but does not present specific strategies for bias detection or mitigation, which is critical for real-world deployment.

### Questions
- Table 1: how many instructions are there to train each model?
- Table 2: provide a more in-depth analysis of why GLAN can't even beat the base model on non-STEM MMLU subjects.
- Generate instructions from an open-source frontier model and train on it to test the self-training capabilities of GLAN.
- The scaling trends look really promising! But 1. how do GLAN instructions compare with other methods given the same quantity? can plot as a comparison; 2. will the performance ever saturate? worth more experiments and analysis.
- Does GLAN generate longer instructions than other methods? I think it might be a suitable method to scale the length of instructions, which might be an interesting direction.

### Soundness
3

### Presentation
3

### Contribution
3

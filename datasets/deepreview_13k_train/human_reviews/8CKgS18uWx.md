# Structure-Enhanced Protein Instruction Tuning: Towards General-Purpose Protein Understanding

- Decision: Reject
- Scores: 8, 6, 6, 5

## Abstract
Proteins, as essential biomolecules, play a central role in biological processes, including metabolic reactions and DNA replication. Accurate prediction of their properties and functions is crucial in biological applications. Recent development of protein language models (pLMs) with supervised fine tuning provides a promising solution to this problem. However, the fine-tuned model is tailored for particular downstream prediction task, and achieving general-purpose protein understanding remains a challenge.
In this paper, we introduce Structure-Enhanced Protein Instruction Tuning (SEPIT) framework to bridge this gap. Our approach integrates a noval structure-aware module into pLMs to inform them with structural knowledge, and then connects these enhanced pLMs to large language models (LLMs) to generate understanding of proteins. In this framework, we propose a novel two-stage instruction tuning pipeline that first establishes a basic understanding of proteins through caption-based instructions and then refines this understanding using a mixture of experts (MoEs) to learn more complex properties and functional information with the same amount of activated parameters. Moreover, we construct the largest and most comprehensive protein instruction dataset to date, which allows us to train and evaluate the general-purpose protein understanding model. Extensive experimental results on open-ended generation and closed-set answer tasks demonstrate the superior performance of SEPIT over both closed-source general LLMs and open-source LLMs trained with protein knowledge.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces structure-enhanced protein instruction tuning (SEPIT) framework to learn a general-purpose protein understanding model. The paper combines a structure-aware protein encoder with a pretrained large language model, then trains a mixture of experts. To train the new model, they create a new large-scale protein instruction tuning dataset from existing resources. The experiments on the test split of their dataset shows that the structure aware training improves model performance. The paper includes comprehension ablation to show the importance of each component in the model architecture. Finally, they include qualitative analysis regarding how the mixture of experts is utilized at inference time.

### Strengths
- The paper is very well written. 
- The architecture is well-motivated. The paper clearly explains each component, making it easy to understand and reproduce. 
- The experiment section is comprehensive and up to date. The paper compares SEPIT with recent large language models and PIT models. In all cases, they show that SEPIT achieves the highest performance. 
- The paper includes key ablations that test the robustness of the SEPIT model. For example, Table 4 shows that SEPIT does not significantly drop performance even when 3D structure information is unavailable.

### Weaknesses
**Generalization beyond the training data.**
The paper does not experiment on datasets other than its dataset. In Table 1, the paper includes results on the test set of its newly constructed dataset. This experiment does not test the generalization of the model to new datasets, a key practical requirement. It would increase the impact of the paper if experiments with more datasets were included. This is the main weakness of the paper. 

**A need for warm up stage.**
The paper includes a warm up for the protein encoder in Stage 0. In this stage, the paper pretrains the encoder with a self supervised learning objective, i.e., denoising objective. However, it is unclear from the experiments if this stage is necessary. The motivation of the pretrained encoder will be randomly initialized is not a strong justification for this additional step. Can the protein encoder be jointly trained with the language model? 

**Combination of existing components.**
This is a very minor weakness. The paper combines components from existing literature to create a hybrid language model. The architectural innovation is limited. This is not a deal breaker, but it would be great if any existing modules could be simplified. 

Typos
- Line 126: Incorrect citation for ALBEF
- Line 442: Remove full stop after GO annotation tasks

### Questions
Please see the weaknesses in the paper.

Additional questions: 
- Nit: In equation 11, what is $W_{m}$? 
- How are the instructions provided to the zero-shot models?

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
3

### Summary
This paper presents a novel method for general protein understanding, termed SEPIT. The approach integrates a structure-aware module into protein language models (pLMs) and subsequently connects these structure-enriched pLMs to large language models (LLMs) to enhance the understanding of proteins. Building on this model framework, the authors propose a two-stage instruction tuning process. Initially, a foundational understanding of proteins is established through title-based instructions, which is then refined using a mixture of experts (MoEs) to capture more complex attributes and functional information.The authors also constructed a comprehensive dataset for both open-ended generation and closed-ended answering, based on Swiss-Prot and RCSB PDB. Extensive experimental results demonstrate that SEPIT significantly outperforms state-of-the-art models, and ablation studies provide structural validation of the effectiveness of each component within SEPIT.

### Strengths
1.I appreciate the clear and well-structured presentation of the paper. Their writing style is fluid, effectively conveying the motivations behind the research and the logical progression of the methodology.
2.The experiments are comprehensive, featuring insightful ablation studies and case studies. The authors articulate the effectiveness of various techniques clearly, ensuring that these methods remain accessible and not overly complex.
3.The authors have successfully achieved the objectives outlined in the paper, and the figures are exceptionally clear. I appreciate their thoughtful summary of their contributions.

### Weaknesses
I mainly have three concerns:
1.Although the structural components serve their purpose, is such a design too simplistic to capture more detailed structural information? As is well known, the structure of proteins is highly complex, containing numerous amino acids. Could this approach become unreliable and introduce some errors?
2.The experimental results do not provide sufficient evidence to ascertain whether the mixture of experts (MoEs) module is functioning as intended. Further clarity on its performance would strengthen the findings.
3.What are the innovative aspects of the newly constructed dataset compared to the previous datasets? Are there any other models that have utilized this new dataset?

### Questions
1.What are the inference time and complexity of this framework?
2.Is the model capable of explaining interactions between two proteins or other more complex scenarios?
3.Is the dataset constructed by the authors representative in this field?
4.Not a question, What does the author suggest for addressing the resource consumption caused by excessively long protein sequences?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This is an excellent work! The authors propose a novel instruction tuning method to understand the protein structure and connect the PLM with LLM to provide the natural language explanation and human interaction. Meanwhile, a very large scale dataset is curated by them which is also a very significant contribution.

### Strengths
1. The method is very novel and bridges the gap in this domain.  
The motivation for this work is very strong, which bridges the gap between protein and language. They also propose a two-stage method to achieve this.
2. Large-scale dataset is curated.
High-quality, large-scale, and AI-ready data are always needed in this field.
3. Extensive experiments and competitive performance.
From Tab 1, we can find the performance is very competitive compared to SOTA models.

### Weaknesses
1. Maybe add more case studies, (only 2 seems too few).
My suggestion is to categorize the question type (currently only two types of questions are made). If the author can summarize and categorize most questions and do the case studies for each of them. That would be great.
2. The in-depth analysis is not enough. Add more analysis in the experiments part.
There is a lack of error analysis. Can you also add error analysis in the case studies? So that we know when the model might make mistakes.

### Questions
See details in weakness.

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
4

### Summary
The excerpt describes a framework called Structure-Enhanced Protein Instruction Tuning (SEPIT) aimed at enabling large language models (LLMs) to achieve general-purpose protein understanding. The authors argue that existing protein language models (pLMs), even when fine-tuned, are often task-specific and struggle to provide a holistic understanding of protein properties and functions. By integrating structural information, employing a novel instruction tuning pipeline, and utilizing a comprehensive dataset,

### Strengths
* i) Incorporates Structural Information: this work includes a structure-aware module that lets it use both sequence data (which is plentiful) and structural data (which is scarcer) to understand proteins. the idea structural information could help understanding is ituiative and sounded.

* ii) Positive Performance on Function Prediction Tasks：Experimental results show that SEPIT performs better than other methods on tasks involving both open-ended questions (like explaining the function of a protein) and closed-set questions (like determining if a protein has a specific function)

### Weaknesses
i) Data Leakage Concerns:
* Considering the redundancy and similarity of protein data, a large amount of work indicates the importance of data cleaning. I believe the current experiment fails to address my concerns about data leakage. For instance, AlphaFold2, AlphaFold3, and Prot2Text propose methods to remove 40% sequence similarity. Such an approach would likely result in lower (and more reasonable) BLEU/ROUGE scores. It is recommended that the authors further refine the data splitting to mitigate potential data leakage issues.

ii)  In the current experimental design, many of the studies mentioned by the authors were not included, such as Prot2Text and ProteinChat. Moreover, including some updated data (updated validation sets) could further enhance the model's credibility. The argue that these methods are limited to specific tasks like prediction and retrieval and don't offer the open-ended generation capabilities required for comprehensive protein understanding. However, a quantative comparision would be appriciate.

### Questions
i) The necessity and advantages of the proposed two-stage training process require further clarification. What are the potential drawbacks of a single-stage approach? How does the two-stage process specifically address these limitations? What empirical evidence supports this design choice?"

ii) While the evaluation metrics derived from LLM contexts provide valuable insights, the paper would benefit from a more comprehensive analysis of model performance using domain-specific evaluation criteria. I suggest author could considering :
Stratifying the evaluation set based on biological classification hierarchies and analyzing performance patterns across different biological categories

### Soundness
2

### Presentation
3

### Contribution
2

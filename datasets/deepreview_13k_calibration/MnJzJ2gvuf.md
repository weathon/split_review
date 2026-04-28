# MAVIS: Mathematical Visual Instruction Tuning with an Automatic Data Engine

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
Multi-modal Large Language Models (MLLMs) have recently showcased superior proficiency in general visual scenarios. However, we identify their mathematical capabilities remain under-explored with three areas to be improved: \textit{visual encoding of math diagrams}, \textit{diagram-language alignment}, and \textit{chain-of-thought (CoT) reasoning}. This draws forth an urgent demand for an effective training paradigm and a large-scale, comprehensive dataset with detailed CoT rationales, which is challenging to collect and costly to annotate manually. To tackle this issue, we propose \textbf{MAVIS}, a \textbf{MA}thematical \textbf{VIS}ual instruction tuning pipeline for MLLMs, featuring an automatic data engine to efficiently create mathematical visual datasets.
We design the data generation process to be entirely independent of human intervention or GPT API usage, while ensuring the diagram-caption correspondence, question-answer correctness, and CoT reasoning quality. With this approach, we curate two datasets, MAVIS-Caption (558K diagram-caption pairs) and MAVIS-Instruct (834K visual math problems with CoT rationales), and propose four progressive stages for training MLLMs from scratch.
First, we utilize MAVIS-Caption to fine-tune a math-specific vision encoder (CLIP-Math) through contrastive learning, tailored for improved diagram visual encoding. Second, we also leverage MAVIS-Caption to align the CLIP-Math with a large language model (LLM) by a projection layer, enhancing vision-language alignment in mathematical domains. Third, we adopt  MAVIS-Instruct to perform the instruction tuning for robust problem-solving skills, and term the resulting model as MAVIS-7B.
Fourth, we apply Direct Preference Optimization (DPO) to enhance the CoT capabilities of our model, further refining its step-wise reasoning performance.
On various mathematical benchmarks, our MAVIS-7B achieves leading results among open-source MLLMs, e.g., surpassing other 7B models by +9.3\% and the second-best LLaVA-NeXT (110B) by +6.9\%, demonstrating the effectiveness of our method.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper argues that the existing models lack in mathematical reasoning in the visual contexts due to the lack of math diagram understanding by the vision encoders, limited diagram-language alignment data, and inaccurate capability of large models (e.g.,GPT-4V, Gemini-Pro) to perform chain-of-thought reasoning. To address this, the paper proposes MAVIS, a rule-based and automatic data engine used for visual instruction tuning of the 7B large multimodal models. Specifically, the paper focuses on plane geometry diagrams, analytic geometric diagrams, and function diagrams. Subsequently, the paper performs 4-stage training on MAVIS-caption and instructs to achieve good performance on the MathVerse dataset. While the data collection, and training pipelines look reasonable, the paper severely lacks solid experiments to establish the usefulness of the generated data.

### Strengths
- The dataset creation pipeline is quite rigorous ranging for the three categories – including caption and instruct data generation.
- The size of the captioning and instruct dataset is quite large, which is a plus too. The method for creating diagram-caption data using GPT-4 as template generators instead of caption generators is interesting.
- The paper performs 4-stage training: CLIP-Math, Aligning diagram-language alignment, instruction tuning and preference alignment. 
- The final numbers showcase the benefits of their data and training on the evaluations.

### Weaknesses
 - Mammoth-2 is supposedly a strong model for math reasoning for text. It remains unclear how much benefit does the MAVIS data give over finetuning Mammoth-2 with existing visual instruction tuning dataset (e.g., LLaVA data). This is crucial to control for the choice of the base model itself. 
- The main result is on the MathVerse dataset which consists of author-created solid geometry and function problems and plane geometry problems sourced from GeoQA and Geometry3K. The authors augment their dataset with the problems from the same dataset in L338. It is crucial to see if most of the improvements in Table 2 are in the plane geometry, while solid geometry and functions still suffer. 
- Related to above: there is a synthetic component to the dataset and a real-data (e.g., Geometry datasets and sourcing problems from internet) component to the instruct data. How much of the performance comes from the synthetic data and how much of it is contributed by adding the real data is unclear. 
- There are no experiments to study data scaling — does training with all the data better than training with 25%, 50% and 75% of the entire dataset. If the data quality is high, then the model performance should scale with data.
- Table 4 has too many dashes for open-source MLLMs which makes it hard to put the model improvements in the complete context. The table makes it look as if some numbers have been skipped selectively. 
- The public sources (or protocol) for selecting the math problems from public sources in L322 is unclear. There is no data contamination study to understand the overlap between the generated data and evaluation data. 
- Minor: Table 3 and 4 adds a * on the models that are consider math specialist but there is no * on the MAVIS models themselves. I would consider them math specialists too.

### Questions
mentioned in the weakness

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
This work primarily aims to enhance the visual mathematical reasoning capabilities of MLLMs. The authors observe that existing visual encoders struggle to capture abstract information in math diagram, and MLLMs lack strong visual mathematical reasoning abilities. To address this, they propose a data collection pipeline and collected approximately 1.4 million math diagram-caption pairs and VQA with CoT data. By fine-tuning the CLIP visual encoder, aligning CLIP with the LLM, and applying Supervised Fine-Tuning (SFT) and Direct Preference Optimization (DPO) alignment techniques, they train a 7B math MLLM.

### Strengths
- The motivation behind this work is clear. For example, it identifies the semantic gap between natural images with rich colors and textures and mathematical diagrams with grayscale and abstract elements. Therefore, constructing math diagram-caption pairs is necessary to enhance visual embeddings.
- The data collection pipeline does not require extensive manual annotation or the use of OpenAI API, it is rule-based and automated, making it relatively low-cost. 
- This work involves a substantial amount of engineering effort, collecting 1.4 M data in the mathematical domain. The model also achieved high performance across multiple benchmarks.

### Weaknesses
 - The main contribution of this paper is the proposal of an automated data collection pipeline that doesn’t require extensive manual annotation or the use of the OpenAI API. However, the paper lacks an overview figure in the main text, which may make it challenging for readers to grasp the key idea of this data collection pipeline.
- This work lacks a certain degree of novelty. For instance, it does not propose a new model architecture, and the training approach is a combination of the popular methods, such as CLIP’s contrastive training[1], LLaVA’s visual instruction tuning, and Direct Preference Optimization[3] (DPO). The model and training method are not specifically optimized for the mathematical domain; instead, they rely on a general model and training approach, with only a mathematical dataset provided for fine-tuning. (Fortunately, the engineering effort is substantial.)

### Questions
- In Section 3.2, why only freeze the CLIP visual encoder and train the projection layer along with the LoRA-based LLM? In LLaVA [1], both the visual encoder and LLM are frozen, with only the projection layer trained to align the visual encoder and LLM. If training the LoRA-based LLM is better, please provide a rationale and ablation experiments to support this approach. 

- The core idea behind the rule-based caption and instruction data collection is akin to template filling, and the concept for constructing CoT data seems similar to deductive reasoning?

[1] Liu H, Li C, Wu Q, et al. Visual instruction tuning[J]. Advances in neural information processing systems, 2024, 36.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduce MAVIS, a multimodal large language model trained with mathmatical dataset generated by data engine.
Specifically, the authors constructed MAVIS-caption to train CLIP-Math with better mathmatical visual representation ability and MLP multimodal connector. Then the authors constructed MAVIS-Instruct to endow MLLM instruct follow and CoT reasoning ability.
The evaluation result shows that MAVIS achieve good performance on multiple math-domain benchmarks.

### Strengths
- The writing is clear and easy to follow.
- The idea of using dataset generation engine to enhance MLLM math visual reaoning ability is straightforward and effective.
- The training stretagy, including the staged training, and the dataset design are well-established.

### Weaknesses
 - Although MAVIS is a mathematical visual specialist, the performance is still similar with some generalist MLLMs. Especially on vision-only version of Mathverse, where MAVIS is only 0.9% better than LLaVA-NEXT-110B. Suggesting that the MAVIS's visual representation learning is not very effective.
- The generation engine can only cover a limited set of mathmatical diagrams. For example, circumcircle of a triangle, which is a very common geometry shape, can not be generated by the engine. Since the engine is manually designed, it will be challenging to cover all kinds of math visual diagram types. If the goal is to train a generalize math MLLM, discussion on the generalize ability of MAVIS is needed, since the training shape is limited.

### Questions
- I'm wondering the result of Table 6, Mathverse but on vision only version. Since CLIP-math helps the model improve its visual representation, a performance improvement on vision-only version can be more convincing.

### Soundness
3

### Presentation
4

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
This paper proposes MAVIS, a mathematical instruction tuning framework, including an automatic data generation engine, two multimodal mathematical datasets, and a specialized model MAVIS-7B. The mathematical instruction tuning of MAVIS consists of four progressive steps from visual pretraining to preference alignment, respectively targeting different issues in this field. The rule-based data engine can generate numerous mathematical data without costly human and GPT engagement, which contributes to sufficient data resources for training. The model MAVIS-7B shows good results on different benchmarks.

### Strengths
1. This paper comprehensively investigates different aspects of training multimodal math models, providing good insights in this field. The scope includes data curation, visual encoding, training pipelines, and learning methodologies. The exploration of better math-specific visual encoding, Math-CLIP, is interesting. This is a good reference for future work.

2. The proposed data engine is novel and of great value for obtaining large-scale training data. As discussed in the paper, the collection and annotation are expensive for multimodal math, while this data engine effectively alleviates this point. The author also shows detailed human study and comparison to ensure the data quality.

3. The MAVIS-7B model shows competitive performance in different benchmarks. The results validate the effectiveness and generalizability of the proposed data and training method.

### Weaknesses
1. The data engine is a rule-based system with fixed language templates. How to ensure the diversity of captions and questions in training data? It is very important to use wide and diverse data for robust model training.

2. The author only provides the results of the 7B model. What if the model size is larger, for example, 13B?

3. The author adopts introduced data and methods to train MAVIS from scratch. However, it is unknown whether these approaches are generalized enough to help a pre-trained large model, for example, LLaVA, to improve the mathematical performance.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
3

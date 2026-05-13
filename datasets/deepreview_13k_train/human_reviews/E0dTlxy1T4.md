# MMEvol: Empowering Multimodal Large Language Models with Evol-Instruct

- Decision: Reject
- Scores: 6, 5, 6, 6, 6

## Abstract
The development of Multimodal Large Language Models (MLLMs) has seen significant advancements with increasing demands in various fields (e.g., multimodal agents, embodied intelligence). While model-driven approaches attempt to enhance MLLMs capabilities through diverse architectures, the gains have become increasingly marginal. Conversely, data-driven methods, which scale up image-text instruction data, are more effective but face limited data diversity and complexity challenges. The absence of high-quality data constitutes a significant development barrier for MLLMs. To address the data quality bottleneck, we propose \ours, a novel multimodal instruction data evolution framework. This framework iteratively improve data quality through a refined combination of fine-grained perception, cognitive reasoning, and interaction evolution, generating a more complex and diverse image-text instruction dataset that empowers MLLMs with enhanced capabilities. Beginning with an initial set of instructions, SEED-163K, we utilize \ours to systematically broaden the diversity of instruction types, extend visual reasoning steps to improve cognitive reasoning abilities, and thoroughly explore fine-grained information within images to enhance visual understanding and robustness. To comprehensively evaluate the effectiveness of our approach, we conduct extensive qualitative analysis and quantitative experiments across 13 vision-language tasks. Compared to baseline models trained with the initial seed data, the results demonstrate that our method achieves an average accuracy improvement of 3.1 percentage points. Furthermore, our approach reaches state-of-the-art (SOTA) performance in nine tasks using significantly less data compared to state-of-the-art models.
The project page is available at \href{https://mmevol.io/}{https://mmevol.io/}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduce a method to systematically evolve seed instruction fine-tuning data for VLM to larger scale and enhance vision centric capabilities for fine-tuned visual understanding, visual reasoning and human interactive capabilities. The enhanced evolution dataset show signiificant improvement on a wide range of perception and reasoning dataset.

### Strengths
The problems this paper tries to address are spot on, current VLMs is limited in terms of complex visual reasoning, natural interaction with human, etc. The method to evolve current instruction fine-tune data to enhance these capabilities is one of interesting direction to improve the model’s capabilities, as shown in the benchmark results. 

The authors mention data and code will be released, and I think it’ll be a good contribution to the community to set a higher baseline for LLAVA style model and maybe even beyond.

### Weaknesses
My major concern is lack of technical clarity and minor concern is insufficient evaluation. 

First, the prompt is clear in Fig 4 - Fig 7, can you explictly describe what model, commercial API or other method is used to generate the evolutoin instruction data from the prompt templates?

Second, it is mentioned pseudo function calling is used for visual reasoning evolution, can you describe the setup of function call, the model or template used to generate the function call, and how it is integrataed to the visual reason evolution process?

Third, it is mentioned MLLM is used for rewriting, can you describe details on what MLLM is used, how it is used (prompt used), evalution or abalation of the significance of this rewriting step?

On the evaluation side, I think a more comprehensive evaluation on different capabilities of the model and some more ablation would provide more insights to the method and data. 

Firrst, the seed dataset and one of the vision-centric capabilities is OCR, while there is few OCR related benchmark results, more results on OCRBench, ChratQA, DocVQA, TextVQA would be very insightful. 

Second, more ablation on ratio of the three evolution methods in each round, how to decide and eliminate failed evolution, what’s the success/fail ratio for each round, what is the model quality gain for reach round, etc. would be informative. 

Third, in comparison with other methods, InternVL2-8b (releaesd 2024/07) and Qwen2-VL-7b (released 2024/08) should be included in Table2 under weight open source section.

### Questions
Addressing questions w.r.t. Technical clarify and evaluation in weakness session would impact my final judgement of the paper. The following questions are nice-to-have discussion which might not impact final score. 

Enhancing vision centric capabilities in fine-grained object, CoT, interaction seems to be effective in LLAVA style VLM, do you think it is because the pretrained ViT / LLM lacks these capabilities in the first place, or pretrained models already have learned enough knowledge but somehow forget it with poor instruction data during fine-tuning? Do you think this data will help other pretrained VLMs trained with tens of billions of image/text tokens?

### Soundness
3

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
4

### Summary
This paper addresses the lack of high-quality data in building stronger multimodal large language models and proposes a solution through the development of a multimodal instruction data evolution framework, MMEval. The framework iteratively improves data quality across three evolution stages: fine-grained perception, cognitive reasoning, and interactive evolution. The authors demonstrate the effectiveness of the framework by refining a new dataset called SEED-163K and training a large multimodal model on this refined dataset. Evaluation results across 13 benchmarks further validate the effectiveness of the proposed framework.

### Strengths
- The paper addresses the issue of data scarcity in instruction datasets for training multimodal large language models, presenting a well-motivated problem.
- The authors designed a sophisticated pipeline to enhance data quality, featuring three evolution stages and an instruction elimination stage.
- The authors evaluate the effectiveness of the three proposed evolution stages, as shown in Table 1.
- The performance of **MMEval** MLLMs in Table 2 appears promising.

### Weaknesses
 - The entire data improvement framework relies on closed-source frontier models like GPT-4, which suggests a form of knowledge distillation from these models but may limit the ability to scale to larger datasets. Additionally, the strong dependence on models like GPT-4 reduces the framework's interpretability.
- The authors do not provide an analysis of the reliability of using GPT-4 as a data rewriter.
- The paper lacks a comparison of different prompts used in each evolution stage, leaving the impact of prompt templates on data refinement unclear.
- When comparing the results of **MMEval-8B** with **Cambrian-1 8B** in Table 2, although **MMEval-8B** shows overall improvements, it exhibits significant performance declines on key benchmarks like **MMMU**, **AI2D**, and **MMStar**.

### Questions
- How reliable is GPT-4 as a data rewriter? How can the quality of the rewritten data be evaluated?
- Is the rewritten output sensitive to changes in the prompt?
- What is the rationale behind the current prompt design? Have other prompt variations been compared?
- Why does **MMEval-8B** perform poorly on **MMMU**?

### Soundness
2

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
In this paper, the authors propose MMEvol, a novel multimodal instruction data evolution framework that augments existing multi-modal training data with better diversity and complexity. The experiment results show that the proposed method works well and helps the MLLMs get better performance

### Strengths
Please refer to Questions

### Weaknesses
1. My main concern is the comparison fairness in Table 2. The LLaVA-Next baseline uses the seed-set (163K data),  while the MMEvol uses an augmented set with more data(447K additional data). This leads to an unfair comparison, as in most cases, more data leads to better performance. This problem also exists in Table 1. The unfair comparison hinders the understanding of the actual effectiveness of the proposed method and I think it is easy to become fairer as the seed-set is sampled from existing open-source datasets and can easily be scaled up to a similar size with the augmented one.

2. Both the evolution and elimination are realized by the same model (GPT4o-mini). Is the model capable of finding out bad cases generated by itself? Further, I'm wondering about the fail rate and elimination rate of the proposed method.

3. Following 2, the proposed method evolute the instruction multiple times, will this lead to the error accumulation problem?

4. The paper focuses on improving the training data quality, while the provided example is quite limited. More data samples will help better evaluate the data quality.

### Questions
### Strength
1. The paper is well-written and easy to follow
2. The proposed idea is novel and seems to work well

### Weakness
1. My main concern is the comparison fairness in Table 2. The LLaVA-Next baseline uses the seed-set (163K data),  while the MMEvol uses an augmented set with more data(447K additional data). This leads to an unfair comparison, as in most cases, more data leads to better performance. This problem also exists in Table 1. The unfair comparison hinders the understanding of the actual effectiveness of the proposed method and I think it is easy to become fairer as the seed-set is sampled from existing open-source datasets and can easily be scaled up to a similar size with the augmented one.

2. Both the evolution and elimination are realized by the same model (GPT4o-mini). Is the model capable of finding out bad cases generated by itself? Further, I'm wondering about the fail rate and elimination rate of the proposed method.

3. Following 2, the proposed method evolute the instruction multiple times, will this lead to the error accumulation problem?

4. The paper focuses on improving the training data quality, while the provided example is quite limited. More data samples will help better evaluate the data quality.

I like the proposed idea and give it a 6: marginally above the acceptance threshold. But there are still some unclear problems I mentioned above. I will adjust the final score based on the rebuttal.

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
5

### Summary
MMEvol addresses data quality and diversity challenges by proposing an iterative evolution of image-text instruction data. Starting with SEED-163K, it expands instruction types, enhances visual reasoning, and strengthens fine-grained perception and cognitive abilities.

### Strengths
This work proposes an image-text instruction evolution framework, Evol-Instruct, to enhance the quality and quantity of instruction data. Using three distinct evolution methods and instruction elimination to remove harmful data, the approach increases the complexity and diversity of a limited seed dataset. After three rounds of evolution, the resulting data trains a new model that achieves SOTA performance across various benchmarks.

### Weaknesses
- Evolving multimodal dataset makes sense and is so interesting but actual performnace improvements are too marginal in my perspective: 2~3% because evaluating language ability can improve large margin if it is really contrbutional approach.

- Experiments should be compared for fair comparison where same architecture, same dataset to provide the effectiveness of MMEvol.

- What kind of dataset samples are more effective to be applited by MMEvol like Math, code, or anyhting?

### Questions
Refer to Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper addresses the challenge of enhancing the quality and diversity of training data for Multimodal Large Language Models (MLLMs). Traditional model-driven approaches face diminishing returns, while existing data-driven methods are limited by the complexity and variety of available data. To overcome this, the authors propose MMEvol, a framework that iteratively refines image-text instruction data through fine-grained perceptual evolution, cognitive reasoning evolution, and interactive evolution. This process generates a richer and more diverse dataset, improving the models' visual understanding and reasoning capabilities. The approach leads to a significant performance boost across multiple vision-language benchmarks, achieving state-of-the-art results in several tasks with less data compared to existing methods. This paper contributes by advancing the capability of MLLMs through an innovative data evolution method that emphasizes the quality of instructions over sheer data volume.

### Strengths
Data Evolution Framework: The MMEvol framework effectively enhances the diversity and complexity of image-text instruction data through iterative evolution methods, such as fine-grained perceptual, cognitive reasoning, and interactive evolution. This approach significantly improves the quality of data used for training MLLMs, addressing a critical bottleneck in existing data-driven methods.

Empirical Improvement: The proposed method achieves an average accuracy improvement of 3.1 percentage points over baseline models and reaches state-of-the-art performance in nine vision-language tasks. This demonstrates the efficacy of MMEvol in enhancing model capabilities with less training data compared to other approaches.

Data Balancing and Quality Analysis: The generated instructions are more compositional, longer in reasoning chains, and more balanced between objects. The statistics of the instructions suggest improved quality of instructions.

### Weaknesses
Evaluation Limitation: While the paper claims that the instruction generation method is a key contribution, it lacks a direct comparison with other multimodal instruction generation techniques, such as MIMIC-IT or LLaVA-NEXT. To strengthen this evaluation, I suggest that the authors generate instructions using MIMIC-IT and LLaVA-NEXT methods on the same seed data and compare the quality, diversity, and complexity of the resulting instructions with those generated by MMEvol. This would help demonstrate how MMEvol performs relative to similar methods in the field, addressing the largest weakness of the paper.

Absence of Failure Case Study: The paper does not sufficiently explore the limitations or failure scenarios of MMEvol. I recommend that the authors provide concrete examples of cases where MMEvol might fail or produce suboptimal results. Additionally, conducting an analysis of how performance changes with increasing rounds of evolution could help identify potential saturation points, offering insights into when the method might negatively impact model performance.

Technical Contribution: The paper's technical contribution feels incremental compared to previous works like MIMIC-IT[1] or MM-Instruct[2], which also iteratively refine instructions from image metadata. To clarify the novelty of MMEvol, it would be helpful for the authors to explicitly outline which aspects of their method are similar to these prior works and what specific contributions MMEvol makes beyond them. This will help position the paper relative to existing methods and highlight any unique advancements.

### Questions
- Fig 12: why does negative scaling happen at step 6k-7k? Is it related to certain instruction augmentation techniques?
- Table 1: What are the number of instructions for each row?
- Table 2: What's Qwen2-7B baseline performance?
- The quality, and maybe quantity, of the seed instruction set may affect the quality of the generated instructions. Please provide a study on this to evaluate the robustness of the proposed method.

### Soundness
3

### Presentation
3

### Contribution
2

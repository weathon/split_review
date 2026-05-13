# Rethinking Table Instruction Tuning

- Decision: Reject
- Scores: 8, 6, 5

## Abstract
Recent advances in table understanding have focused on instruction-tuning large language models (LLMs) for table-related tasks. 
However, existing research has overlooked the impact of hyperparameter choices and lacks a comprehensive evaluation of the out-of-domain table understanding ability and the general capabilities of these table LLMs. 
In this paper, we evaluate these abilities in existing table LLMs, and reveal significant declines in both out-of-domain table understanding and general capabilities compared to their base models. 
Through systematic analysis, we show that hyperparameters, such as learning rate, can significantly influence both table-specific and general capabilities.
Contrary to the existing table instruction-tuning works, we demonstrate that smaller learning rates and fewer training instances can enhance table understanding while preserving general capabilities.
Based on our findings, we introduce **TAMA**, a **TA**ble LLM instruction-tuned from LLa**MA** 3.1 8B Instruct, which achieves performance on par with, or surpassing GPT-3.5 and GPT-4 on table tasks, while maintaining strong out-of-domain generalization and general capabilities. 
Our findings highlight the potential for reduced data annotation costs and more efficient model development through careful hyperparameter selection.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a thorough evaluation of existing instruction-tuned LLM for table-related tasks, focusing on the often-overlooked aspects of hyper-parameter choices and their impact on model performance. The authors identify the clear declines in the general knowledge obtained by the base model. Through systematic analysis, this work demonstrates that proper learning rates and fewer training instances can enhance table understanding without the sacrifice of LLM's exiting capabilities. Based on these findings, the proposed TAMA can be trained with fewer examples and achieves impressive performance on several representative tabular tasks.

### Strengths
- Comprehensive Analysis: The paper provides a thorough analysis of existing table LLMs, highlighting the importance of hyperparameter tuning, which is often neglected in other studies.

- Empirical Findings: The findings are helpful to subsequential research in this field of applying LLMs into tabular tasks. The effects of learning rate is close to my previous experimence in hyper-parameter tuning while further training LLMs over tables.

- Based on the finding, the proposed TAMA demonstrates an impressive improvement in performance.

### Weaknesses
These experiments were only based on Llama models. Further examination is needed for other LLMs, e.g., Qwen-* series, Phi-* series, etc. Whether the findings still hold requires further analysis.

### Questions
Whether the findings still hold while applying lora or qlora?

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
1. This paper presents a comprehensive study revealing that current open-source table LLMs tend to be overly specialized for table-specific tasks, leading to a decrease in out-of-domain table understanding, instruction-following accuracy, and the general capabilities of the base model. These models, such as TableLLM and TableBenchLLM, typically employ high learning rates (e.g., 2e-5), extended training epochs (e.g. 6 epochs), and massive datasets (often exceeding 2 million instances) that lack diversity. This approach results in significant performance drops—up to 20% on general benchmarks like AI2ARC—compared to their base models.

2. The authors argue that careful hyperparameter tuning is necessary to balance table understanding with general capabilities. Through detailed experiments on tasks like FeTaQA, HiTab, and TabFact, they demonstrate how hyperparameters such as learning rate, epochs, and training sample size affect table LLM performance. As a result, they find that a learning rate of 1.0e-6 and two training epochs optimize the LLaMA 3.1-8B model for both table and general task performance.

3. Based on these findings, the authors sample 200 data instances each from 12 diverse table tasks, including WikiSQL, TATQA, and FEVEROUS, totaling only 2,600 samples—just 0.1% of the data typically used in other table LLMs. This data reduction, achieved by randomly sampling representative examples from each task, allows them to train TAMA, a new table LLM. TAMA matches or surpasses GPT-3.5 and, in some cases, GPT-4 on standard benchmarks, achieving 77.4% on FEVEROUS (3% higher than TableLLM) and 66.9% on MMLU, close to the base model’s score. TAMA’s efficient tuning strategy preserves broad capabilities, offering a resource-efficient yet powerful approach to table instruction tuning.

### Strengths
1. Identification of Over-Specialization Issues in Table LLMs: This work reveals a critical trend in current table LLMs, where excessive fine-tuning for table-specific tasks often compromises the models' generalization capabilities. By shedding light on the potential trade-offs, the study encourages the community to reconsider whether the performance gains claimed in state-of-the-art table LLMs justify the loss of general capabilities. This insight points to a promising direction for future research on balancing task-specific and general abilities in LLMs.

2. Extensive Experiments: The study conducts an extensive range of experiments across multiple tasks, including FeTaQA, HiTab, TabFact, and others, providing a broad evaluation of hyperparameter impacts on table-specific and general capabilities. This depth of experimentation allows for a more complete view of the challenges in table LLM tuning and establishes a robust foundation for future research in this area.

3. Identification of Effective Hyperparameter Settings: Through systematic exploration of hyperparameters—such as learning rate, training sample size, and number of epochs—the authors identify an optimal configuration for the LLaMA 3.1-8B model that supports strong table-specific performance while preserving general capabilities. By using significantly fewer training samples, they demonstrate an efficient tuning approach that achieves competitive results, establishing a valuable hyperparameter baseline for future table LLM research.

### Weaknesses
1. Limited Reproducibility Due to Closed Code and Weights: While the study’s findings are promising, the lack of open-source training and evaluation scripts, data, and TAMA’s model parameters during the review period restricts reproducibility. Although the study’s conclusions align with similar issues I observed in table LLMs like TableLLaMA and TableLLM, having access to TAMA’s scripts and parameters would allow a comprehensive verification of the training process and performance claims of TAMA, underscoring the importance of direct open-sourcing resources for rigorous validation.

2. Title-Content Discrepancy on Table Data Modality: The title, “Rethinking Table Instruction Tuning,” suggests a focus on unique aspects of table data, yet the study does not examine if the observed trade-offs are specific to table modality or generalizable. Discussion on the influence of table-specific features, such as heterogeneity, permutation invariance, or numeric density, could better align the study’s scope with the title.

3. Limited Novelty and Incomplete Analysis Relative to Zhou et al. (2024): While this work applies Zhou et al. (2024) [1]’s approach of using a small set of tuning data to enhance table LLM capabilities, as reflected in lines 246-249, it offers limited additional insights. Although the application in the table domain adds value, the study could have further clarified whether observed improvements are due to pre-trained knowledge or specific learning during fine-tuning. 
Additionally, it does not explore whether models with stronger general capabilities require less tuning data to maximize performance in table tasks, which could provide valuable insights for future table LLM research. Finally, examining differences in pre-training corpora, such as LLaMA 1 vs. LLaMA 2 vs. LLaMA 3.1, could clarify whether observed gains stem from pre-trained abilities or are specific to instruction tuning. More experiments, such as comparing results across diverse pre-trained models, would enhance originality and provide practical insights.

4. Lack of Validation Across Multiple Base Models and Hyperparameter Guidance: While the hyperparameter settings for LLaMA 3.1-8B provide a useful baseline, extending these findings to other mainstream base models is essential to confirm generalizability. Applying the study’s tuning approach across diverse models, such as Mistral [2] and Qwen [3], and establishing a set of reliable hyperparameter baselines across mainstream LLMs—much like the impact achieved by the work [4]—would add significant, long-term value. Such efforts would enhance the study’s applicability and offer future table LLM research a practical framework for effective tuning.

### Questions
I really appreciate the motivation and ideas presented in this work, and addressing the questions raised in the weaknesses section would support a higher rating. I am curious whether the conclusion that a small number of samples can achieve good results is based on fine-tuning for specific fields. Because the SFT in these subdivided tableqa fields seems to be the same as what we did in the BERT era, so large-scale pre-training + small-scale fine-tuning can achieve good results. I am curious whether this conclusion still holds true when large models need general capabilities such as reasoning, long text answers, and RAG?

I know it's not easy to answer the question. It would be appreciated if some insights can be provided.

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
The paper first evaluates existing table LLMs and finds that they have poor OOD table understanding capability, poor instruction-following capability, and comprised general capabilities. The paper then studies the influence of hyperparameters on training table LLMs. Finally, the paper trains TAMA from LLaMA-3.1-8B-Instruct with great table understanding capability while preserving the general capabilities.

### Strengths
+ The paper illuminates the limitations/weaknesses of existing table LLMs.
+ TAMA is a good contribution to the open-source LLM community, which has a good performance. People can do follow-up work on TAMA to study LLM's specific capabilities.

### Weaknesses
While TAMA is a good contribution to the community, I am personally not sure about the contribution of this paper itself. The takeaway for training TAMA seems to be just a good hyperparameter choice + multi-task training. The latter is a standard way and the former does not provide too much insight - I am not saying hyperparameter tuning/search is meaningless, and my point is that the current Section 3 is more like just an experimental report, where people (at least I) might want to see some fresh insights (e.g., training dynamics, capability analysis, etc). If it is just that the previous table LLM training + careful hyperparameter selection = TAMA, I would doubt the contributions of the paper.

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
1

### Summary

This paper presents a method for improving the mathematical reasoning capabilities of large language models (LLMs) by augmenting training data with bootstrapped questions. The authors propose a novel approach to generate diverse and high-quality mathematical questions using techniques such as rephrasing, backward reasoning, and answer augmentation. The resulting dataset, MetaMathQA, is used to fine-tune LLaMA-2, resulting in the MetaMath model, which achieves state-of-the-art performance on mathematical reasoning benchmarks among open-source LLMs.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel approach to augment mathematical reasoning datasets by generating diverse questions through rephrasing, backward reasoning, and answer augmentation. This approach is innovative and addresses the limitations of existing datasets, which often lack diversity and complexity.

2. The paper provides a thorough evaluation of the proposed method on two standard mathematical reasoning benchmarks, GSM8K and MATH. The results demonstrate that MetaMath outperforms existing open-source LLMs by a significant margin, highlighting the effectiveness of the proposed data augmentation technique.

3. The paper is well-written and clearly explains the methodology, experimental setup, and results. The authors provide detailed descriptions of the data augmentation techniques and the fine-tuning process, making it easy for readers to understand and reproduce the results.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on improving the performance of LLMs on mathematical reasoning tasks. While the results are impressive, it would be beneficial to explore the applicability of the proposed method to other types of reasoning tasks, such as logical reasoning or common-sense reasoning. The current evaluation is limited to mathematical datasets, and it is unclear if the data augmentation techniques would generalize to other domains. For example, the rephrasing and backward reasoning techniques might not be directly applicable to tasks requiring symbolic manipulation or common-sense inference, which could limit the broader impact of the work.

2. The paper does not provide a detailed analysis of the computational resources required for training and inference. While the authors mention the use of LLaMA-2, it would be helpful to provide more information on the training time, memory requirements, and hardware specifications. This information is crucial for researchers who want to reproduce the results or apply the proposed method to other tasks. The lack of specific details makes it difficult to assess the practical feasibility of the approach, especially for researchers with limited computational resources.

### Suggestions

The authors should investigate the transferability of their data augmentation techniques to other reasoning domains. Specifically, they could explore how the rephrasing and backward reasoning methods could be adapted for tasks involving logical reasoning, such as those found in the LogicQA dataset, or common-sense reasoning tasks. This would involve modifying the question generation process to align with the specific requirements of these domains. For example, in logical reasoning, the rephrasing could focus on altering the logical structure of the questions, while in common-sense reasoning, the rephrasing could involve changing the context or background knowledge required to answer the question. A thorough analysis of the performance on these diverse tasks would provide a more comprehensive understanding of the method's generalizability and limitations.

Furthermore, the authors should provide a detailed breakdown of the computational resources required for training and inference. This should include the specific hardware used (e.g., GPU model, number of GPUs), the training time for different model sizes, and the memory requirements during training and inference. It would also be beneficial to include the energy consumption of the training process. This information is crucial for researchers who want to reproduce the results or apply the proposed method to other tasks. The authors could also explore the possibility of using more efficient training techniques, such as knowledge distillation or parameter pruning, to reduce the computational cost of their approach. This would make the method more accessible to a wider range of researchers and practitioners.

Finally, the authors should consider releasing the code and the augmented dataset to the community. This would allow other researchers to build upon their work and further explore the potential of data augmentation for improving reasoning capabilities of LLMs. The code should include clear instructions on how to reproduce the results and how to apply the data augmentation techniques to other datasets. The dataset should be well-documented, including the data generation process and the types of questions included. This would greatly enhance the impact and reproducibility of the research.

### Questions

1. How does the performance of MetaMath compare to other state-of-the-art models, such as GPT-3.5-Turbo and PaLM-2, on the MATH benchmark?

2. What is the impact of the size of the augmented dataset on the performance of MetaMath? Is there a point of diminishing returns where adding more data does not lead to significant improvements?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

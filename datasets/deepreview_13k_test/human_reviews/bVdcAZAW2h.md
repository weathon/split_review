# Enjoy Your Layer Normalization with the Computation Efficiency of RMSNorm

- Decision: Reject
- Scores: 5, 5, 5

## Abstract
Layer normalization (LN) is a milestone technique in deep learning and has been widely used in various network architectures. It performs centering and scaling over the layer activations of a neural network for each example, stabilizing and accelerating the training of neural network. However, it introduces extra computation cost during inference and the computation problem has recently been addressed by its counterpart RMSNorm that only adopts scaling. This paper investigates how to exploit the theoretical advantages of LN but with the cost of RMSNorm. This paper formally defines the condition that the centering operation of LN can be removed and this condition can be obtained by imposing the column centering constraint on the adjacent linear module before the LN. We propose column centered weight transformation (CCWT) to ensure an LN without centering operation (i.e., RMSNorm) have the same output as the original one in a pre-trained model.
 Our method can be directly applied to various pre-trained large language models (LLMs) and large vision language models (VLMs) with LN, enabling an immediate reduction in computation cost meanwhile maintaining equivalent prediction during inference.
 We further propose a reparameterization method, called column based weight centering (CBWC), to ensure the linear module column centered during training. We show that RMSNorm combining CBWC can obtain an equivalent effects to the  LN counterpart during training, but with more efficient computation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a method to balance the theoretical benefits of Layer Normalization (LN) with the computational efficiency of RMSNorm. The authors propose Column Centered Weight Transformation (CCWT) and Column Based Weight Centering (CBWC) as techniques to achieve the effects of LN without the need for centering, which reduces computational overhead. This approach enables the usage of RMSNorm in place of LN for various deep learning models, particularly large language models (LLMs) and vision-language models (VLMs), without compromising performance. The paper demonstrates both theoretical equivalence and empirical results to support the proposed method's efficiency during inference and training.

### Strengths
(1) The approach reduces inference time by removing the need for centering in LN. This can be beneficial for LLMs and VLMs, where inference latency and computational resources are critical.
(2) The authors provide rigorous definitions and proofs to justify the proposed transformations, ensuring that the new method is theoretically sound.
(3) The CCWT and CBWC techniques can be applied across various pre-trained models, enabling easy adoption in different architectures with LN.
Experimental Validation: The experiments confirm that the method maintains performance on translation and classification tasks while enhancing efficiency, showing promise in practical applications.

### Weaknesses
(1) Limited Evaluations in Experiments: Although the method is broadly applicable, the empirical tests are limited to a few models. Further experimentation on a wider variety of large language models, especially decoder-only models on text-generation tasks, could provide a stronger justification for generalizability.
(2) Potential Training Instabilities: The method, though theoretically equivalent, could exhibit slight instabilities during training, as shown in the empirical results, especially when Dropout Layers disrupt the zero-mean property.
(3) Lack of Inference-Time Statistics: While the paper focuses heavily on inference efficiency, it lacks extensive analysis on the comparisons between the proposed method and baseline transformers, especially regarding realistic inference statistics such as inference latency, FLOPs and inference throughput.

### Questions
See the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a novel approach to enhance the computational efficiency of Layer Normalization (LN) while retaining its theoretical advantages. By defining a column centering constraint, the authors demonstrate how to achieve the same output as LN without the centering operation, thereby reducing computation costs during inference. The paper also presents techniques such as Column Centered Weight Transformation (CCWT) and Column Based Weight Centering (CBWC) to ensure linear modules maintain centering during training. Experimental results indicate that these methods perform well across various pre-trained large models, effectively improving computational efficiency.

### Strengths
+ The paper presents a clear and rigorous theoretical framework for removing the centering operation from Layer Normalization (LN), establishing the conditions under which this is feasible. The introduction of column-centered constraints provides a solid foundation for justifying the equivalence of the proposed method (RMSNorm) to traditional LN, which could inspire further research into optimization techniques in neural network training.

+ The authors effectively demonstrate the applicability of their method to various pre-trained large language models (LLMs) and vision-language models (VLMs). This not only showcases the versatility of their approach but also addresses a pressing issue in the field: the computational inefficiency of LN during inference. The direct application of their method in real-world scenarios adds significant value.

+ The paper includes experiments that validate the effectiveness of the proposed RMSNorm combined with column-based weight centering (CBWC) during both training and inference. The results indicate that the new method can achieve comparable performance to LN while significantly reducing computational costs, providing empirical evidence to support the theoretical claims made throughout the paper.

### Weaknesses
- While the paper introduces RMSNorm, the novelty of the method may be perceived as incremental rather than groundbreaking. The authors reference some similar normalization techniques (e.g., Batch Normalization, Group Normalization) but could strengthen their contribution by providing a more detailed comparison of these methods in terms of performance metrics and theoretical underpinnings. Specifically, addressing how RMSNorm differentiates itself from existing approaches in both practice and theory could enhance the perceived novelty.

- The experimental evaluation is primarily conducted on a limited set of benchmarks. Testing RMSNorm on large language models, such as those based on the LLaMA architecture, would be beneficial. This would help assess the method's effectiveness in the context of contemporary model architectures and could reveal how RMSNorm performs in scenarios typical of large-scale language tasks, including language generation and understanding.

- The paper would benefit from more extensive ablation studies that explore the impact of different components of the proposed method. For example, examining how variations in the column-centered constraints influence performance could offer insights into the critical elements that contribute to the effectiveness of RMSNorm. This would not only strengthen the paper's claims but also guide future researchers in understanding the design choices involved.

### Questions
What specific performance metrics differentiate RMSNorm from existing methods like Batch Normalization and Group Normalization? Can the authors provide a clearer comparison?

Will the authors consider testing RMSNorm on large language models, such as LLaMA, to assess its effectiveness in large-scale language tasks?

Could the authors conduct more ablation studies to clarify how variations in column-centered constraints affect RMSNorm's performance?

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
In this work the authors context the computational complexity led by layer normalization, proposing to use instead RMS Normalization. The equivalence between the two normalization is established by ensuring that the signal at the output of a layer has average zero, which can be achieved by imposing specific constraints to the input of such layer, and to the parameter's distribution. The authors test the performance achieved with their proposed approach on simple image classification tasks (MNIST and CIFAR-10) and on text translation and classification.

### Strengths
- The objective is clear, the writing in most of the parts is also clear.
- The approach is in general reasonable.

### Weaknesses
- The approach has some implicits, like that there should be no non-linearity between the convolution/fully connected layer and the layer norm.
- The validation is performed on relatively small-scale datasets.
- There is no quantitative time computation reduction for both training and inference time.

### Questions
- How is the approach performing on larger datasets (like ImageNet-1k) on realistic architectures like SWIN?
- What is the real wall-clock time in employing the proposed CWBC+RMSNorm compared to LayerNorm?
- What are the cases this approach is applicable (ie. what are the specific constraints to the architecture to make this solution usable)?
- Is there any major attention to pay for hyper-parameters fine-tuning? Or the approach is completely insensitive to large variation of hyper-parameters like learning rate and weight decay?
- Gradient-wise, is CWBC+RMSNorm equivalent to LayerNorm?

### Soundness
3

### Presentation
2

### Contribution
2

# Parameter-Efficient Fine-Tuning   via Circular Convolution

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 3

## Abstract
Low-Rank Adaptation (LoRA) has gained popularity for fine-tuning large foundation models, leveraging low-rank matrices $\mathbf{A}$ and $\mathbf{B}$ to represent weight changes (\textit{i.e.,} $\Delta \mathbf{W} = \mathbf{B} \mathbf{A}$). This method reduces trainable parameters and mitigates heavy memory consumption associated with full delta matrices by sequentially multiplying $\mathbf{A}$ and $\mathbf{B}$ with the activation. Despite its success, the intrinsic low-rank characteristic may limit its performance. Although several variants have been proposed to address this issue, they often overlook the crucial computational and memory efficiency brought by LoRA. In this paper, we propose \underline{C}ir\underline{c}ular \underline{C}onvolution \underline{A}daptation (C$^3$A), which not only achieves high-rank adaptation with enhanced performance but also excels in both computational power and memory utilization. Extensive experiments demonstrate that C$^3$A consistently outperforms LoRA and its variants across various fine-tuning tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work introduces Circular Convolution Adaptation (C3A) as an advanced parameter-efficient fine-tuning (PEFT) technique, addressing limitations of existing methods like Low-Rank Adaptation. C3A leverages the circular convolution operator, enabling high-rank adaptation without a proportional increase in trainable parameters. Utilizing Fast Fourier Transform (FFT) operations, C3A achieves efficient memory and computational performance while retaining expressive power. The method effectively reduces memory requirements and computational load compared to high-parameter alternatives like VeRA. A notable strength of C3A is its flexibility in adjusting the number of trainable parameters through block-circular convolution, which adapts to diverse downstream tasks. Experimental results validate C3A's superior accuracy and memory efficiency across various tasks.

### Strengths
1. High-Rank Adaptation with Low Parameters: C3A achieves high-rank adaptation without increasing the number of trainable parameters. By leveraging circular convolution, it avoids the limitations of low-rank adaptation in methods like LoRA, maintaining expressive power with fewer resources.
﻿
2. Efficient Use of FFT for Computational Gains. The use of Fast Fourier Transform (FFT) in both forward and backward propagation enhances computational speed and reduces complexity, achieving a time complexity comparable to LoRA but with better efficiency in memory use.
﻿
3. Memory Savings with Block-Circular Convolution. By implementing block-circular convolution, C3A allows for flexible control of trainable parameters. This adaptability to block size enables parameter tuning based on task requirements, optimizing both memory and computational resources.
﻿
4. Comprehensive Benchmark Performance. C3A demonstrates robustness performance across multiple tasks, including GLUE benchmarks for NLP and Vision Transformer (ViT) for image classification, showing significant improvements in accuracy with fewer parameters.
﻿
5. Adaptable Parameter Count with Minimal Performance Trade-Offs. C3A allows for adjustable parameter configurations through its block-circular design, offering a range of parameter counts without significant sacrifices in performance, providing versatility across tasks.

### Weaknesses
1. Although C3A claims robustness to initialization methods, the paper does not thoroughly analyze how different initializations may impact convergence speed or model performance across varying tasks. Additional experiments on initialization sensitivity could further validate this robustness claim and clarify any subtle effects on fine-tuning stability.

2. While the method demonstrates efficiency on moderate NLP and CV benchmarks, it lacks evaluation on tasks with substantially higher dimensions or complexity, where circular convolution’s rank flexibility may not be as effective. Testing C3A on such high-dimensional data would strengthen claims about its scalability.

3. Inadequate Justification for Block Size Selection: The paper introduces block-circular convolution with adaptable block sizes but provides minimal guidance on how to select optimal block sizes for specific tasks. This omission makes it challenging for readers to understand the trade-offs and practical considerations in choosing block sizes to balance accuracy and parameter efficiency.

6. The proposed method relies on block-circular convolution for flexibility, but the paper does not clearly address its limitations, such as potential rank deficiencies or performance degradation in non-square matrices. Expanding on these limitations and detailing their implications would provide a more balanced view of C3A’s adaptability across different architectures.

### Questions
1. I will appreciate additional analysis on how initialization affects model convergence speed and accuracy across varied tasks. Specifically, experiments with detailed metric comparisons for convergence time under different initializations would strengthen this claim.

2. The method lacks experimental validation on tasks involving significantly higher dimensions or complexity, where circular convolution may face generalization challenges. We encourage the authors to include experiments on larger-scale datasets or more complex tasks to confirm C3A's adaptability and performance.

3. How different block sizes may impact both parameter efficiency and performance across tasks? We request the authors to provide guidelines for block size selection.

4. Aside from the existing comparison with baseline methods LoRA and VeRA, we suggest authors to Include more recent PEFT methods as baselines, as that will provide a more comprehensive understanding of C3A's standing relative to broader industry benchmarks.

5. Please elaborates the limitations of the proposed Block-Circular Convolution.

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
The paper proposes a new parameter-efficient fine-tuning (PEFT) method (denoted C³A) that leverages circulant matrices and Fast Fourier Transform (FFT) to achieve high-rank adaptations while maintaining computational efficiency. The proposed method allows independent control of the rank and number of trainable parameters through block-circular convolution. The authors evaluate their method across various NLP and vision tasks, including NLP, comparing the performance of C³A to existing PEFT.

### Strengths
1. Providing an interesting approach for low-rank adaptation that relies on FFT instead of the typical residual matrix to try to address existing limitations.
2. The extension to block-circular convolution allows for better control over parameter numbers (and makes the method applicable to non-square matrix weights) without compromising rank.
3. Providing detailed practical implementation and foundation for the different components (e.g., circular convolution)

### Weaknesses
1. While using circular convolution and FFT in PEFT is interesting, the improvement over LoRA and similar methods may be seen as incremental, with modest/marginal gains rather than a significant improvement over existing PEFT methodologies.
2. The method's reliance on FFT may introduce implementation complexity, particularly in environments with limited support for these operations, which could restrict the practical applicability of the method.
3. Many of the presented results don’t show clear gains or dominance, which questions the reliability of the presented method, which is the main weakness of the paper.

### Questions
1. Given that the results don’t dominate existing methods in many scenarios, what would be the ideal scenario/environment/conditions in which the proposed method is most effective?
2. Is there an ablation study for the block size (b)? I understand that it is constrained because of the divisibility, but I believe it is important to see some insights about its impact on the result.
3. Can you present more insights/analysis about the decision and the impact of using FFT (e.g., some ablation for the FFT part on its own)?

### Soundness
3

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
This paper borrows the block circulant method from existing work and applies to LLMs. The proposed method is about using block circulant matrix for training which has been already published in the referenced work (Ding et al., 2017). However, the entire method writing (section 3) does not acknowledge/cite the work at all and instead present as if authors created block circulant based training. As a result, the major contribution narrows down to the empirical verification of block circulant training method on different large models.

### Strengths
1. Experimental results are very promising, and evaluated models cover both the base and large version of RoBERTa and ViT, also including  LLaMA-2 and LLaMA-3. 
2. There is also synthetic data experiment which is simple and easy to demonstrate the effectiveness of proposed method against LoRA and full fine-tuning.

### Weaknesses
1. No technical novelty, because the proposed method is borrowed from the referenced work (Ding et al., 2017)
2. Lack of analysis regarding the impact of block size setting, e.g., smaller block size gets more parameters but smaller GPU cost (Table 2)? Why more parameters result in smaller GPU cost? According to theoretical space analysis (section 3.5.2), with d1=d2=768, the formulation cannot explain the observation. 
3. FFT based solution is naturally sensitive to intialization, as a small change in frequence domain can be easily spreaded to all time domain. The experimental design in section 4.5 should include results on LLaMA models, as the FFT size is large in LLaMA models. The hypothesis is inclined to be that intialization for FFT based method is sensitive in the case of large models or large FFT size settings.


### Questions
1. Can you compare with the state-of-the-art FourierFT method (https://icml.cc/virtual/2024/poster/33821), which is also a Fourier domain based method? 
2. Can you provide memory cost details in Table 3 and Table 4, as you did for Table 2?
3. Need a breakdown of the memory cost of proposed method, since in Table 2, more parameters somehow results in less GPU memory for both base and large models. 
4. Initialization test for large FFT size setting like LLaMA for section 4.5
5. FFT operations can easily result in nan/inf values in low precision computation. Does the proposed method actually run in half precision (as LLMs are stored) or full precision?

### Soundness
2

### Presentation
4

### Contribution
1

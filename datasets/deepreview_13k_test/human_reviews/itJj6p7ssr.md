# Hardware-Friendly Post-Training Quantization: Input- and Output-Channelwise Scale and Offset

- Decision: Reject
- Scores: 8, 5, 6, 5

## Abstract
Post-training quantization enables swift quantization of neural networks using a minimal calibration dataset.
Specifically, these methods tend to underperform dramatically on hardware with fixed integer bit width, particularly in extremely low-bit quantization scenarios.
In response, we introduce an optimized method for uniform channel-wise quantization, which is compatible with existing hardware. This approach does not increase memory requirements and results in only a marginal increase in computation.
This strategy involves applying a specific multiplier to the result of the weighted activation products, thereby yielding a more accurate result for the multiply-accumulate (MAC) operation in convolutional or fully-connected layers. We also present an optimization technique to determine the optimal channel grouping approach.
To affirm the superiority of our proposed quantization scheme, we conducted tests on a variety of CNN-based models.
Our proposed approach enhances accuracy in 2/4-bit weight and feature quantization by 1-5%p while only increasing the number of integer operations in convolutional-based networks by less than 1.5%.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes an improved post training quantization (PTQ) method called IOSO. The method relies on adjusting the scale and offset in activations (both input and output). The benefits are shown for ImageNet on a diverse set of DNNs.

### Strengths
1) The paper is well-written and easy to understand.
2) The paper addresses a well-addressed problem and tries to make a contribution.
3) The improvements in accuracy are non-trivial in some scenarios.
4) The computational overhead is small < 1.5%.
5) Error bars are shown for network accuracy.

### Weaknesses
1. The results in Table 2 are incremental. This is not surprising since post-training quantization has been studied extensively.
2. The proposed methods minimizes layer-wise reconstruction error. Reconstruction error is a proxy for misclassification error, which is the ultimate metric. Comparison with methods that directly minimize misclassification error is missing.

### Questions
1. There are PTQ methods, e.g., [1], that minimize the probability of misclassification. How does your method compare with those?
[1] Sakr et. al. Analytical guarantees on the numerical precision of deep neural networks, ICML'17.
2. Have you considered fine-tuning your results by doing some limited amount of training, say one epoch? It will be interesting to see if the accuracy improves significantly.
3. Can your method be extended to cover training?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a quantization method that exploits channel-wise scaling and offset parameters to compensate for the discrepancies in full-precision and quantized distributions. It has been shown that the proposed method outperforms existing works in terms of accuracy.

### Strengths
1) The proposed method is simple and effective in quantizing convolutional networks especially when extreme quantization levels are used.

2) The paper is easy to read and understand.

### Weaknesses
1) There is no discussion on why the proposed method is considered hardware-friendly. Which hardware is this work referring to? How its efficiency was measured?

2) The number of operations and parameters for each quantization method must be compared along with the accuracy in Table 2 and 3. The accuracy improvement of this work is marginal for most cases. So, it's important to compare other aspects too.

### Questions
See the questions listed as weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper extends AdaRound quantization scheme and introduces a group-based scaling factor along input channel direction. A output-channel-wise, learnable scale and offset are also applied to better reconstruct the low bit cases. To lower the computational cost, author proposed to use bit-wise shifter and only allow scaling factors of 1+- 2^-N. Considering the hardware efficiency of implementing such input channel-wise methods, the author demonstrated the feasibility of setting contraints on the number of the channels per group (to be greater than a certain value) then use retraining to recover the accuracy. Extensive experiments on different CV models and comparisons with other similar PTQ schemes, such as AdaRound, AdaQuant, BRECQ, and QDROP, were provided.

### Strengths
1. Clear and detailed explanations about the numerical method.

2. Extensive experiments results, especially the author provides statistics, i.e. 5-run mean and standard deviation, instead of best records. This will help readers to get a better idea while comparing the proposed method with different quantization schemes.

### Weaknesses
1. Lack of real HW results. It's clear that the author thoroughly considered the potential limitations if the proposed method was to be implemented. However, there are still some potential concerns, such as channel permutation's impact on computation efficiency and grouping fragments effect. A few examples on a representative HW would make the paper much stronger and convincing.

2. Marginal improvement compared to previous works. It is understandable that the existing methods may have already done decent jobs and the author has to use extreme low precision settings (W2A4) to demonstrate the benefit of the proposed method. However, considering the complexity of implementation and the uncertainty in compute efficiency trade-off, the author might need to find a few better examples where the use of the proposed method would be better justified.

### Questions
1. Eq.9 and the explanations in the following paragraph shows that the group scaling factor, gamma_y, is a linear combination of preset gamm_G based on probability. However, that will likely make gamma_y not compatible with bit shifter. In AdaRound, the handling of h(V) is different during calibration/PTQ stage and inference stage. Author might want to clarify/comment on this part or it might cause confusion to the readers. 

2. Based on the example in Fig. 6, the 3 scaling factors used are 1 and 1+-2^-N. One may interpret this scheme as some input channels will be up-weighted, some will be down-weighted, and the remaining channels will be unchanged. However, the optimized factor here seems to be very small, implying that simply not applying the scaling factor might work as well? But comparing to Table 4, it seems like the case without input scaling will be close to the case of N=1? Please comment.
 
3. Instead of using unstructured input channel-wise grouping, another frequently use quantization scheme is structured grouping, such as used by GPTQ and other LLM works. Maybe the author could consider including a few comments on the pros and cons with the proposed method?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Observing the distributional discrepancy between the full precision weights and their quantized counterpart, this paper proposes to scale and offset input and output in a per-channel way.  Extensive experiments are conducted to show the effectiveness of their methods, especially in low-bit settings.

### Strengths
1. The paper conducts thorough experiments, including analyses of computational complexity and ablation studies, to showcase the effectiveness of their methods. It also provides a detailed comparison with related works.
2. The proposed methods exhibit significant improvements over previous approaches, such as BRECQ[1], especially in low-bit scenarios.

[1]Yuhang Li, et al. BRECQ: Pushing the Limit of Post-Training Quantization by Block Reconstruction.ICLR 2021

### Weaknesses
1. The novelty of the paper raises concerns, as the input-channel scale and shift resemble group-wise quantization have been studied in prior works like Q-BERT. Although the authors emphasize advantages in hardware implementation, the improvement over group-wise quantization appears minor. Can you provide the comparison between group-wise quantization (with or without the power of two scales) in computation complexity and performance?

2. Similar to Weakness.1, shifting and scaling the output per channel is similar to finetune/update the BatchNorm statistics after the quantized convolutions. Does this method still work if we finetune BN after quantization on Conv-BN networks ?(this method is used widely to recover accuracy after quantization)

[2]Sheng Shen,et al. Q-BERT: Hessian Based Ultra Low Precision Quantization of BERT. AAAI 2020

### Questions
Is the shift operation expected to introduce more latency than a single integer operation due to non-local memory access at inference?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

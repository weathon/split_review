# Nearly Lossless Adaptive Bit Switching

- Decision: Reject
- Scores: 5, 5, 5, 8

## Abstract
Model quantization is widely applied for compressing and accelerating deep neural networks (DNNs). However, conventional Quantization-Aware Training (QAT) focuses on training DNNs with uniform bit-width. The bit-width settings vary across different hardware and transmission demands, which induces considerable training and storage costs. Hence, the scheme of one-shot joint training multiple precisions is proposed to address this issue. Previous works either store a larger FP32 model to switch between different precision models for higher accuracy or store a smaller INT8 model but compromise accuracy due to using shared quantization parameters. In this paper, we introduce the Double Rounding quantization method, which fully utilizes the quantized representation range to accomplish nearly lossless bit-switching while reducing storage by using the highest integer precision instead of full precision. Furthermore, we observe a competitive interference among different precisions during one-shot joint training, primarily due to inconsistent gradients of quantization scales during backward propagation. To tackle this problem, we propose an Adaptive Learning Rate Scaling (ALRS) technique that dynamically adapts learning rates for various precisions to optimize the training process. Additionally, we extend our Double Rounding to one-shot mixed precision training and develop a Hessian-Aware Stochastic Bit-switching (HASB) strategy. Experimental results on the ImageNet-1K classification demonstrate that our methods have enough advantages to state-of-the-art one-shot joint QAT in both multi-precision and mixed-precision. Our codes are available at https://anonymous.4open.science/r/Double-Rounding-EF78/README.md.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper targeted two quantization applications, i.e. multi-precision and mixed-precision. Models in former case hold only one set of weights under a given precision (e.g. 8bit) and then allow users to switch the entire model to another precision (e.g. 2bit) while the 2bit weights are converted from the given 8bit weights. A "double rounding" scheme was proposed for this translation of the given weights into the desired lower precision. For mixed-precision case, when deciding the optimal precisions for each individual layer, a Hessian Matrix Trace was employed as an indicator to identify sensitive layers, which will be assigned with higher probability to select higher precisions. The proposed methods were tested on image classification, object detection, and zero-shot commonsense reasoning tasks.

### Strengths
1. Good amount of experimental data including a few representative models on vision and NLP tasks.
2. proposed HASB method seems to be effective on mixed-precision case.

### Weaknesses
1. Rounding or Flooring?
According to Eq 2 and the name "double rounding", the conversion of INT8 weights to lower precision weights should be a rounding process. However, Line 203 states that "bit-shift" was used to perform the "divide by 2" operation. As bit-shift is not a rounding but a floor division, e.g. 7>>1 = 3 instead of 4, could author please clarify which operation is really used in this method? (One should note that the 4th illustration in Fig. 2 also seems to be a floor operation instead of rounding.) 

2. Generalization concerns. 
a) ALRS seems to be a purely empirical hyper-parameter tuning. 
Comparing Fig 3a and 3b, it seems like gradient magnitude for 4, 6, 8bit are far from clipping bound in Eq. 6, i.e. 1.0. Fig 3c/3d also seems to suggest that gradient clipping is only needed for 2bit case. Roughly speaking, Eq 6 simply suggests to scale LR by 0.1 for every 2 bits reduced in precision. However, Fig 3c/3d and Appendix Fig 7, 8, 9 do not show any apparent differences in gradient magnitude to justify this scaling. This type of empirical rule most likely will not be generalizable when model architecture and dataset changed, as the LLM example in 4.3, author mentioned that ALRS is not applied in that case possibly due to this reason. 
  
b) Threshold for Hessian Matrix Trace
Hessian indicator and HASB seems to work well in Fig. 5a and 5b, but when 2bit is not included, as in Fig. 5c, the improvement is not clear. Author may want to show the HMT distribution and sensitive layers assignment in this case and discuss the differences. On the other hand, the threshold for sensitive layers is the mean HMT of all layers in this work. This kind of relative threshold could be dangerous if all HMT are fairly close, because roughly half of the layers will be labeled as sensitive and encouraged to use higher precision, which will lose the benefit of mixed-precision. Maybe additional checks need to be applied for HASB, for example, limit the total number of sensitive layers. 

3. Repeat paragraph, typos, plot being too small.
The very first paragraph in Introduction is repeated at Line 41 to 45, Line 354 "DeepWise" should be "Depth-wise", Fig 3 and 4c/d, fonts are too small and illegible. Author may want to proofread this manuscript one more time.

### Questions
please see Weakness

### Soundness
2

### Presentation
2

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
This paper proposes a bit-switching quantization method for multi-precision training. It employs a Double Rounding method that enables the storage of a shared 8-bit model instead of a full-precision one. To facilitate training convergence, the authors introduce the ALRS method to dynamically adjust the learning rate for each precision during training. The authors also apply the proposed bit-switching quantization to mixed-precision training for efficient subnet selection.

### Strengths
This paper is easy to follow, and the proposed approaches make sense.

### Weaknesses
1) The contribution of the Double Rounding technique does not appear to be significant. The first stage of DR seems aimed at avoiding the storage of a full-precision model during inference, but this concept is well-trodden ground. Similar approaches, such as starting with an 8-bit model in multi-precision or bit-sparse inference, have been extensively explored [1][2]. Considering that 8-bit quantization can preserve accuracy effectively, why not begin with an 8-bit model and perform subsequent processing? Furthermore, it's unclear why the proposed dynamic bit-switching can't directly operate between the integer bit-widths (8, 6, 4, and 2) without introducing a floating-point representation and the double rounding scheme. Can the proposed method be applied to an INT8 model to perform bit switching?

2) The ALRS strategy appears straightforward and seems to have minor differences compared to training each precision separately. While the method works, my concern lies in the runtime memory overhead. ALRS may require keeping multiple copies of activations and gradients for each precision during training, potentially leading to increased memory usage. This could impact the scalability and efficiency of the approach, especially for large-scale models like LLMs.

3) The probability distributions used in Fig. 4(a) and Fig. 4(b) are not well motivated. For the {8, 6, 4, 2} configuration, it seems that the average number of bits for the insensitive and sensitive cases are 5 bits and 6 bits, respectively. Is this right? How can you achieve an average number of bits lower than 5, for example, 4 bits? What are the probability distributions when only three candidate bits are used, as in Table 3? As you recommend including 8-bit for training, why not evaluate {8,6,4,2} for the experiment in Table 3?

4) The accuracy of FP models is inconsistent in experiments, which is somewhat misleading. In Table 2, while the proposed method (ours*) achieves the highest accuracy, AdaBits experiences a much smaller relative accuracy drop.

5) It is unclear how knowledge distillation is performed in multi-precision training. Also, since the mixed-precision training is initialized by the multi-precision training, what is the total number of training epochs of both stages in the experiment in Table 3? Is it 90?

### Questions
Please see the weaknesses.

### Soundness
2

### Presentation
2

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
The paper introduces a quantization method aimed at improving DNN compression with flexible, precision-switching capabilities that reduce storage and accuracy trade-offs. Traditional Quantization-Aware Training uses fixed, uniform bit-widths, but this approach instead uses three key techniques to optimize multi-precision performance. First, Double Rounding applies a double rounding operation that minimizes accuracy loss when switching between precisions, storing only the highest integer precision and eliminating the need for full-precision storage. Second, Adaptive Learning Rate Scaling dynamically adjusts learning rates across bit-widths, reducing gradient interference and balancing convergence between high and low precisions during one-shot joint training. Third, Hessian-Aware Stochastic Bit-switching uses layer sensitivity, measured by the Hessian Matrix Trace, to assign higher bit-widths to more sensitive layers and lower ones to less sensitive layers, optimizing precision across the network. Together, these methods demonstrate competitive performance in ImageNet-1K classification, detection, and segmentation tasks, surpassing current multi-precision and mixed-precision quantization approaches.

### Strengths
- The paper is generally well-written, with clear explanations of concepts and effective use of figures to illustrate key ideas, such as the interference issue during multi-precision training and the Double Rounding operation. 
- The proposed Double Rounding method offers a solution for precision-switching without significant storage requirements or accuracy loss.

### Weaknesses
 - The paper’s experiments are limited to CNNs on ImageNet for classification, lacking a broader evaluation across different architectures, such as transformers, which are essential for both CV and NLP tasks. For NLP, the use of TinyLlama as a baseline is insufficient, as it is not a widely recognized standard for large language models. A more rigorous evaluation on established baselines, such as LLama-3, would provide a stronger and more credible assessment of the method’s effectiveness across diverse model types and tasks.
- While the authors demonstrate results on ImageNet-1K for classification, the experiments lack evaluation on more complex or fine-grained tasks (e.g., instance segmentation, object detection on datasets beyond ImageNet). These tasks often pose unique quantization challenges due to greater sensitivity to detail and precision.
- The paper could benefit from more comprehensive ablation studies, especially on the impact of each component (Double Rounding, ALRS, and HASB) independently and in combination.

### Questions
- Given the paper's focus on mobile and edge scenarios, could the authors quantify the memory and power consumption improvements (if any) compared to traditional quantization methods?
- While ALRS claims to improve convergence consistency across bit-widths, could the authors provide a theoretical explanation or further empirical analysis to support this?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper presents an approach to address the challenges of multi-precision and mixed-precision joint training in deep neural network quantization. The authors introduce a technique called double rounding quantization, which allows for the storage of a single integer weight representation while enabling adaptive precision switching with minimal accuracy loss. This method utilizes two rounding operations, effectively embedding lower-precision weights within higher-precision weights, thus reducing storage requirements. The paper further introduces an adaptive learning rate scaling (ALRS) method designed to mitigate the competitive interference between high and low precisions during training. ALRS dynamically adjusts the learning rates for different precisions, trying to ensure consistent update steps of quantization scales and improving the accuracy of low-precision models without sacrificing the performance of high-precision models.  Furthermore, the authors propose a hessian-aware stochastic bit-switching (HASB) strategy for one-shot mixed-precision training. HASB leverages the hessian matrix trace as a sensitivity metric to determine the probability of bit-width selection for each layer, prioritizing higher bit-widths for more sensitive layers.

### Strengths
1. Findings: Joint optimization of quantized network for multiple precision results to competition between high and low precisions. However, the reason was unclear in existing works. This paper point out that the reason of the competition comes from the inconsistent magnitudes of the quantization scale’s gradients between high precision and low precision.
2. Strong multi precision result: The results in Table2 and Table6 show that, in multi precision, double rounding and ALRS each show effective result compared to existing work. Although the effect of double rounding only is not directly revealed in the paper, it can be sufficiently inferred by comparing the two tables.

### Weaknesses
1. Is there any reason the MobileNet-v2 result is not included on mixed precision results? Many existing works show that the quantization methods that show good result on ResNets cannot applicable to MobileNets which is hard to quantize.
2. This reviewer suggests proposing searched per-layer bit-width result for the one-shot mixed precision result (of proposed models, e.g, ResNet-18 and ResNet-50). This would increase the understanding of effect of HASB with hessian trace by comparing it to a baseline without using HASB.
3. On Figure 4(d), it seems the results having same average bit-width is showing large accuracy differences. Does it mean that the same mixed-precision budget can show different per-layer bit-width results? If so, this results show that HASB cannot always show optimal result. Maybe the authors can analyze some specific cases where the same average bit-width produces significantly different accuracies, explaining what causes these differences and how this relates to the effectiveness of HASB.
4. Algorithm: Lack of explanation of several terms in Algorithm2 makes bad readability. Please define 'pulp' and 'ideas' in the context of Algorithm2, either within the algorithm description or in an accompanying glossary of terms.

### Questions
1. Is there any reason the MobileNet-v2 result is not included on mixed precision results? Many existing works show that the quantization methods that show good result on ResNets cannot applicable to MobileNets which is hard to quantize.
2. This reviewer suggests proposing searched per-layer bit-width result for the one-shot mixed precision result (of proposed models, e.g, ResNet-18 and ResNet-50). This would increase the understanding of effect of HASB with hessian trace by comparing it to a baseline without using HASB.
3. On Figure 4(d), it seems the results having same average bit-width is showing large accuracy differences. Does it mean that the same mixed-precision budget can show different per-layer bit-width results? If so, this results show that HASB cannot always show optimal result. Maybe the authors can analyze some specific cases where the same average bit-width produces significantly different accuracies, explaining what causes these differences and how this relates to the effectiveness of HASB.
4. Algorithm: Lack of explanation of several terms in Algorithm2 makes bad readability. Please define 'pulp' and 'ideas' in the context of Algorithm2, either within the algorithm description or in an accompanying glossary of terms.

### Soundness
4

### Presentation
3

### Contribution
3

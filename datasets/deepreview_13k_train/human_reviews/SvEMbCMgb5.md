# $R^2$: Range Regularization for Model Compression and Quantization

- Decision: Reject
- Scores: 5, 3, 5, 6

## Abstract
Model parameter regularization is a widely used technique to improve generalization, but, it can also be used to shape the weight distributions for various purposes. 
In this work, we propose range regularization ($R^2$) for building quantization and compression friendly models by removing outliers from weights during training. By effectively regulating range of weights, we mold the overall distribution into a tight shape to ensure high quantization bit resolution, therefore allowing model compression and quantization techniques can to utilize their limited numeric representation powers better. We introduce $L_\infty$ regularization, its extension margin regularization and a new soft-min-max regularization to be used as a regularization loss during full-precision model training. We show that this technique generalizes well for post training quantization, quantization aware training methods like EWGS and compression techniques like DKM. Coupled with state-of-the-art quantization and compression techniques, models trained with $R^2$ perform better on an average, specifically at lower bit weights with 16x compression ratio. Our results show that $R^2$ generates state of the art 2-bit quantized models for heavily parameter constrained models like MobileNet V1 and V2 when coupled with EWGS. Additionally, for high compression ratio (32x), models trained with $R^2$ significantly better than the ones trained without it.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes range regularization to shape the weight distribution for model compression and quantization. Three variants of range regularization are introduced. Experiments with ResNet-18, MobileNet-V1/2 (pretrained on ImageNet) are provided to demonstrate the effectiveness of range regularization on model compression and quantization.

### Strengths
The idea of shaping weight distribution for model compression and quantization makes sense. It seems the introduced R_inf and R_margin are effective to eliminate outliers from weight distributions. 

The paper is well-written, and easy to follow.

### Weaknesses
It makes sense to eliminate outliers to improve the performance of weight quantization. However, it seems there is no explanation or justification why elimination of outliers can improve the performance of model compression. Specifically, the paper doesn't clarify how range regularization interacts with the underlying compression algorithms (e.g., pruning, knowledge distillation) to achieve better results. It's not clear if the weight distribution shaping is beneficial for compression in general, or if it is specifically tailored to the k-means clustering based compression method used in the experiments.

The performance improvement of the proposed method is more pronounced for very aggressive compression ratio or 2-bit quantization, in which cases the baseline accuracies drop significantly (e.g., mostly halved). This makes the proposed method not very practical as it’s not acceptable in almost all cases to deploy a significantly worse model even though the compression rate is high. Often time, the compressed models should have similar or slightly worse performance to the original uncompressed models. The paper should address the practical applicability of the method in scenarios where the accuracy drop is not so drastic.

All model compression and quantization baseline methods are from 2019, 2020 or 2021. I didn’t follow the research in the area closely. But I believe there should be SOTAs in the past 2 years. So, it’s unclear how effective the proposed method is over the latest baselines. The lack of comparison with recent state-of-the-art methods makes it difficult to assess the true contribution of the proposed range regularization techniques. It is important to compare against more recent methods to demonstrate the actual advancement of this work.

Typos:
page 3 bottom: tate-of-the-art 
page 6 middle: prove to be effective here.  -> ineffective

### Questions
As indicated above, a justification why weight shaping can help model compression would be helpful.

Please consider using the SOTAs from 2022 or 2023 as baselines. It would be interesting to see if the gains still hold for aggressive compression or quantization.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors introduce “range normalization,” a new technique for normalizing model parameters to form weight distributions suitable for quantization.

This approach acts as a regularization loss during full-precision model training, and shows that pre-training with R^2 improves accuracy in subsequent Post-Training Quantization (PTQ) or Quantization-Aware Training (QAT) steps. This means the possibility of obtaining highly generalized models.

The authors experimentally verified the applicability of the proposed method to other quantization techniques, such as EWGS or DKM. In particular, this study shows that when the proposed method is applied simultaneously with EWGS, state-of-the-art (SOTA) results can be obtained through 2-bit quantization on MobileNet V1/V2.

### Strengths
* This paper introduces a novel model parameter regularization technique called range regularization to shape a weight distribution conducive to compression/quantization.
* This paper shows that training a model from scratch using $R^2$ can result in a model with better accuracy after applying subsequent post-training quantization (PTQ) or quantization-aware training (QAT). Experimental evidence shows the potential to obtain more highly generalized models with this approach.
* The proposed method demonstrates its potential applicability to other quantization techniques, such as EWGS or DKM.

### Weaknesses
 * Based solely on the experiments in the paper, it is challenging to discern whether the proposed $R^2$ method is more effective in terms of generalization compared to other regularization methods. Specifically, the paper lacks a direct comparison with established regularization techniques like L2 regularization or dropout, making it difficult to isolate the specific benefits of $R^2$ for generalization. The experiments should include a controlled comparison to demonstrate that $R^2$ offers a unique advantage beyond what existing methods already achieve.
* While the proposed method demonstrated effectiveness in experiments with CNN-based models, it appears challenging to compare its efficacy in other tasks or architectures, such as Language Models, based solely on the conducted experiments. The paper does not provide sufficient evidence to support the claim that $R^2$ is broadly applicable beyond CNNs. The lack of experiments on diverse architectures and tasks limits the generalizability of the findings.
* The paper demonstrates the effectiveness of $R^2$ based on weight distribution, but it does not address activations. Since the experiments in the paper show a significant compression ratio for activations, with activations also sharing the same number of bits as weights, it seems essential to include an analysis or discussion regarding activations. The absence of any analysis on how $R^2$ impacts activation distributions and their quantization is a significant oversight, especially given the joint quantization of weights and activations.

### Questions
* The statement, 'In addition, for a large model like ResNet-18, $R^2$ also shows a regularization effect similar to weight decay, therefore, better validation accuracy than the one without $R^2$,' is unclear in its meaning. If $R^2$ exhibits a performance boost due to a regularization effect similar to weight decay, shouldn't $L_2$ regularization be more effective from the outset? A detailed discussion or experimental data addressing this is needed.
* From the experiments in the paper alone, it's difficult to ascertain the effectiveness of the proposed $R^2$ method in terms of generalization. Are there any experimental data available to assess the Generalization Gap?
* The paper only presents results for small models like CNN or MobileBERT, primarily focusing on CNN results. Are there any results showcasing the application of the proposed method to larger models such as ResNet-101 or LLM (e.g., transformer architectures like GPT-J)? Is there experimental evidence showing the more general applicability of the proposed approach?
* Regarding the statement in Section 5, the authors say that 'We establish that range regularization doesn’t affect the performance of the floating-point models as well, and in some overparameterized models, it also has a regularization effect to address overfitting.'. However, i think there is a lack of theoretical or experimental evidence supporting the claim that range regularization is more effective in preventing overfitting than previously proposed regularization techniques. Is there any theoretical basis or experimental contents related to this claim?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper posits that outliers in the weight distribution are the primary reason for the decrease in model accuracy after quantization. To address this issue, an R2 regularization method is introduced to constrain the range of model weights, thereby eliminating outliers and improving the accuracy of the quantized model.

### Strengths
This paper has a reasonable structure, simple and easy to understand methods, and is easy to read.

### Weaknesses
1. Many prior works have argued the impact of outliers on the quantization results, but this paper only references two from 2020 and 2021, and only references KURE from 2020 as the baseline for comparison, which lacks persuasiveness. 
2. It is hard to prove that applying R2 can lead to higher accuracy after quantization than not applying it. First, only four quantization methods are discussed in the experiments, and they can not cover all the quantizers. Secondly, the existing experiments in the paper show that the results  w/o R2 can also achieve higher model accuracy than that with R2 (Table 4). 
3. The work is incomplete or lacking contribution, and it would be better to include the design of a quantization method specifically for this range regularization in the paper. Clearly, EWGS itself already considers outlier handling, so using R2 leads to a decrease in accuracy, indicating the necessity of designing a corresponding quantization method for R2.

### Questions
1. I am interested in how the experimental results would differ if we applied the clip function instead of R2 regularization in model training. 
2. The author mentions that R2 can be applied to PTQ, but R2 itself is a regularization method used during model training, while PTQ aims to avoid retraining. Do these descriptions conflict with each other?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a range regularization method for training quantized model. The range regularization extend from $\ell_\infty$ regularization to more advanced formulation that can remove the outliers in weight distribution, leading to less quantization error.

### Strengths
This paper proposes a novel regularization-based method to tackle the outliers in the quantized model. The method is straightforward and effective.

Experiments are conducted under different settings to show the effectiveness of the proposed method

The paper is well written and easy to follow.

### Weaknesses
There is no clear analysis on under which scenario each of the proposed range regularization formulation will outperform the others. It would be good to have a switching mechanism to decide which formulation to use.

Ablation study on the impact of regularization strength for the proposed regularizer would provide more insight on the stability of the proposed method.

### Questions
See weakness

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

# Rep-Adapter: Parameter-free Automatic Adaptation of Pre-trained ConvNets via Re-parameterization

- Decision: Reject
- Scores: 6, 8, 3

## Abstract
Recent advances in visual pre-training have demonstrated the advantage of transferring pre-trained models to target tasks. However, different transfer learning protocols have distinctive advantages regarding target tasks, and are nontrivial to choose without repeated trial and error. This paper presents a parameter-free automatic model adaptation protocol for ConvNets, aiming at automatically balancing between fine-tuning and linear probing, by using adaptive learning rate for each convolution filters on target tasks. First, we propose Rep-Adapter, an adapter module with re-parameterization scheme, which can achieve soft balancing between the pre-trained and fine-tuned filters, and can be equivalently converted to a single weight layer, without introducing additional parameters to the inference phase. We show by theoretical analysis that Rep-Adapter can simulate a ConvNet layer with each filter fine-tuning at different learning rate. We present a simple adapter tuning protocol with Rep-Adapter to achieve automatic adaptation of pretrained models without additional search cost. Extensive experiments on various datasets with ResNet and CLIP demonstrate the superiority of our Rep-Adapter on semi-supervised, few-shot and full dataset transfer learning scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper addresses the challenges in transfer learning, emphasizing the impact of factors like dataset size and label fraction on different transfer learning protocols. It highlights the efficacy of linear probing and fine-tuning in semi-supervised and fully-supervised scenarios, respectively. The proposed solution, Rep-Adapter, introduces an approach by adding a learnable side branch alongside a frozen pre-trained branch. This strategy aims to strike a harmonious balance between pre-trained and fine-tuned weights. To simplify the process, learnable hyper-parameters for each layer are introduced, eliminating the need for manual tuning. Additionally, a re-parameterization method is employed during inference to merge the two branches while preserving the structure of the pre-trained model.

### Strengths
* The combination of learnable and frozen branches to find the balance between pre-trained weights and fine-tuned weights.
* Learnable hyper-parameters for each layer, reducing the need for manual adjustments.
* Efficient re-parameterization during inference, ensuring minimal additional computational cost.

### Weaknesses
* Increased computational cost during training due to the addition of learnable branches and hyper-parameters, especially for heavy-weight models.
* In theory, the final results of the proposed fintuning can be achieved by the traditional fintuning, i.e. the difference of original weights and the final weights can be achieved by traditional fintuning. Thus, it is arguable this method is significantly different or better than traditional finetuning.

### Questions
Could it be applied on other architectures, like attention-based ones?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes to use Structural Re-parameterization for transfer learning. Specifically, an extra branch comprising a learnable conv layer and a BN is added to the original frozen conv layer during training. After training, such a structure is equivalently transformed into a single conv layer for inference. The effectiveness is explained as adaptively adjusting the equivalent learning rate of filters. Reasonable results are reported.

### Strengths
1. The idea of using Structural Re-param for transfer learning is novel.
2. The structural design is easy to understand and thoroughly validated.
3. The results are impressive.
4. The explanation (the structure is equivalent to adjusting lr for different filters) is impressive.

### Weaknesses
1. Structural Re-parameterization is not correctly discussed. The authors seem to mistake it with the traditional re-parameterization (e.g., CondConv). Traditional re-parameterization first derives a parameter with some other parameters and uses the derived parameter for computation, for example, a conv layer (y = x conv W) with traditional re-parameterization may compute W = W1 + W2, then y = x conv W. But Structural Re-parameterization uses regular layers during training and converts the structures (i.e., merges some layers) for inference. This work should be categorized into Structural Re-parameterization, but in the paper only "re-parameterization" is used to describe the method. And in Section 2, Structural Re-param should be discussed in a subsection (for example, it should at least mention that Structural Re-param is proposed by [RepVGG] ...) and traditional re-param (e.g., DiracNet, CondConv) should be mentioned in another subsection.

2. The proposition is proved in a vectorized form, which seems a bit messy. I would suggest the authors show a simplified version with a specified arbitrary channel (or a single-channel conv). 

I also suggest the authors show the proposition from another equivalent perspective. I guess the authors would like to prove that in the following two simplified scenarios

A. the structure is  y = frozen_conv(x) + trainable_conv(x) * alpha, the learning rate is lamda

is equivalent to

B. the structure is  y = trainable_conv(x), the learning rate is alpha ** 2 * lamda

This may be easier to understand. Then tell the reader what alpha represents (BN.weight / BN.std) so that the reader will understand that the BN realizes adaptive lr. Then naturally discuss the behavior of BN.

### Questions
1. How is Rep-Adapter used with transformer? Is it used to replace every linear layer? Is BN still used in this case? BatchNorm-1d or 2d? 

2. Is the usage of Rep-Adapter with a linear layer (nn.Linear) simply the same as the usage of a 1x1 conv in a CNN? Their inputs are of different shapes so I wonder if there are some differences.

Please show some code and I will understand it.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposed an adaption tuning method for ConvNets. The learnable parameters of can be re-parameterized to the original conv module to achieve parameter-free adaption. On different pre-trained models, the authors demonstrate the proposed method can achieve good performance.

### Strengths
1. The proposed method indeed provide some interesting experiments for parameter-free adaption of ConvNets, especially on few-shot setting,

### Weaknesses
1. The proposed method has limited novelty. A similar adaption and re-parameterization method has been proposed in earlier methods. [1]
2. The proven "layers tuning at any learning rate via Rep-Adapter" does not make too much sense. Adding scaling factors is equivalent to the adaptive learning rate, and has nothing to do with the proposed Rep-Adapter.
3. While the proposed method can be re-parameterized after training, the modules equivalent to the original network size still need to be fully tuned during training. I don't see any advantage of this compared to parameter-efficient tuning methods except the performance gain reported in the paper. 
4. The reported results are not verified using different random seeds. No error bar is reported.


[1] Sylvestre-Alvise Rebuffi et al. Efficient parametrization of multi-domain deep neural networks. CVPR 2018.

### Questions
1. Can you explain why Rep-Adapter outperforms the full fine-tuning in Table 3?  The details of the initial learning rate for fine-tuning and rep-adapter are missing. Also, does full fine-tuning conduct the same number of epochs as the Rep-Adapter?  10000 steps seem not enough for fine-tuning, can you justify it?  
2. For ablation study (e), it would be of more interest to see different initialization of $w_{R}$ rather than $w_0$.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

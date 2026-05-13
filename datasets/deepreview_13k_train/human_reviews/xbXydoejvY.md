# CWPS: Efficient Channel-Wise Parameter Sharing for Knowledge Transfer

- Decision: Reject
- Scores: 6, 3, 5, 5

## Abstract
Knowledge transfer aims to apply existing knowledge to different tasks or new data, and it has extensive applications in multi-domain and multi-task learning.
    The key to this task is quickly identifying a fine-grained object for knowledge sharing and efficiently transferring knowledge.
    Current methods, such as fine-tuning, layer-wise parameter sharing, and task-specific adapters, only offer coarse-grained sharing solutions and struggle to effectively search for shared parameters, thus hindering the performance and efficiency of knowledge transfer.
    To address these issues, we propose Channel-Wise Parameter Sharing (CWPS), a novel fine-grained parameter-sharing method for Knowledge Transfer, which is efficient for parameter sharing, comprehensive, and plug-and-play.
    For the coarse-grained problem, we first achieve fine-grained parameter sharing by refining the granularity of shared parameters from the level of layers to the level of neurons. The knowledge learned from previous tasks can be utilized through the explicit composition of the model neurons.
    Besides, we promote an effective search strategy to minimize computational costs, simplifying the process of determining shared weights.
    In addition, our CWPS has strong composability and generalization ability, which theoretically can be applied to any network consisting of linear and convolution layers.
    We introduce several datasets in both incremental learning and multi-task learning scenarios. Our method has achieved state-of-the-art precision-to-parameter ratio performance with various backbones, demonstrating its efficiency and versatility.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Current methods for knowledge transfer such as fine-tuning or weight sharing only offer coarse-grained sharing solutions and do not search for optimal parameters for sharing. This paper introduces Channel-Wise Parameter Sharing (CWPS) for efficient knowledge transfer. By refining the granularity of shared parameters from the layer level to the neuron level, they achieve fine-grained parameter sharing to address the coarse-grained problem. The authors also propose a simple method to search for suitable parameters for sharing. The proposed method achieves state-of-the-art results on several benchmarks.

### Strengths
- CWPS demonstrates high performance on various tasks and scenarios.
- The proposed framework is simple but effective.

### Weaknesses
 - The experiment is mainly done using ResNet-50, lacking the experiment using other models such as DenseNet and EfficientNet,  or even transformer-based or MLP-based models. 
- Lack of experiments with different depths of the model

### Questions
1. Can the authors explain more about parameter count?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces Channel-Wise Parameter Sharing (CWPS), a novel approach to knowledge transfer that enhances the efficiency and effectiveness of sharing parameters across different tasks or new data. Traditional methods like fine-tuning and layer-wise parameter sharing often provide coarse-grained solutions, which struggle to effectively identify shared parameters, thus limiting performance and efficiency. CWPS addresses these limitations by introducing fine-grained parameter sharing, achieved by refining the granularity from layers to neurons, allowing for the explicit composition of model neurons and utilization of knowledge from previous tasks. The paper also presents an effective search strategy to minimize computational costs and simplify the determination of shared weights. CWPS is designed to be comprehensive, plug-and-play, and has strong composability and generalization abilities, making it theoretically applicable to any network with linear and convolution layers. The method is evaluated across various datasets in incremental learning and multi-task learning scenarios, demonstrating superior precision-to-parameter ratio performance compared to existing methods, regardless of the backbone used.

### Strengths
1.Innovative Approach: CWPS offers a new perspective on knowledge transfer by enabling fine-grained parameter sharing, which is a significant departure from traditional coarse-grained methods.

2.Enhanced Efficiency: The method is designed to be efficient in terms of parameter sharing, which can potentially lead to better performance and faster training times.

3.Comprehensive and Plug-and-Play: CWPS is presented as a comprehensive solution that can be easily integrated into existing networks without the need for extensive modifications.

### Weaknesses
1.Since the supplementary materials of the paper include experiments with the Transformer model, it seems inconsistent that the main text focuses on convolution as the primary subject of discussion, rather than the Transformer. Moreover, the performance of Vision Transformer (ViT) in Table 5 of the appendix shows suboptimal results, which somewhat undermines the argument that the algorithm can generalize across different backbones effectively. Specifically, while the average accuracy is close to the baseline, the parameter efficiency is not clearly demonstrated for ViT, raising concerns about the method's claimed universality.

2.Why were experiments not conducted on datasets of a scale comparable to ImageNet in Tables 1 and 2? Observing the right side of Figure 4, it appears that all datasets have some relation to ImageNet. Therefore, wouldn't conducting a downstream task on a dataset of similar scale to ImageNet, but not necessarily entirely relevant, further demonstrate that the method's effectiveness is not solely due to knowledge transfer from ImageNet, but rather that the algorithmic design itself contributes significantly to the results? The current experimental setup makes it difficult to isolate the true contribution of the proposed channel-wise parameter sharing method from the benefits of pre-training on ImageNet.

### Questions
Would it be possible to visualize which channels are masked at each layer and whether there is a discernible pattern?

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
The paper proposed a method for knowledge sharing to tackle the problem of transfer learning. The method uses existing models as a knowledge pool, from which a layer-wise composition is constructed tailored to the new task to be solved. This composition is referred to as the parent model. Together with the parent model, a child model of the same architecture is trained. The two models are combined channel-wise using learnable masks. Experiments on multiple benchmarks are conducted to demonstrate the effectiveness of the approach.

### Strengths
1. The paper addresses an important problem in transfer learning. With more and more large foundation models available to the public, these models contribute a very large pool of knowledge learned through vast volume of data. The techniques investigated in this paper can be greatly beneficial to tapping into the potential of such models.

2. The proposed method seems fairly universal. Even though the experiments in the paper are mostly conducted on CNNs, the method can be potentially applied to state-of-the-art transformer networks as well.

### Weaknesses
1. The training pipeline seems unnecessarily convoluted and impractical. If I understand this correctly, given a new task, a child model first needs to be trained for a short period of time. This child model is then used as reference to construct the parent model. Afterwards, the two models are combined with learnable masks to tackle the aforementioned new task. Compared to standard fine-tuning, the advantage of the proposed method appears to be its parameter efficiency. However, the parameter count itself is not the most faithful reflection of the complexity of the model. Stats such as memory consumption and training time are more important, and accurately reflect the Flops needed to train the model. Given that the performance of the proposed method is generally worse than fine-tuning, the contribution of the work is less than convincing.

2. A major motivation of transfer learning is to exploit the knowledge learned on large volume of data and apply it to domain where data may be scarce. In this paper, however, it appears that all data of the target task is assumed to be available. This significantly reduces the practical value of the work. On the other hand, if the effectiveness of the proposed method can be demonstrated in a few-shot setting, where only a small number of labelled examples are available, I think this can make the paper much stronger. For a point of reference, I believe a recent work by Zhang et al. (2024) shows that a learnable linear combination of models in the weight space can achieve very strong performance in few-shot learning and also test-time adaptation. In the latter case, no labelled data is available. I would encourage the authors to compared against this method.

3. The writing of the paper is not the best, with numerous typos. For instance, in L201, I think the authors meant "existing" instead of "exiting".

### Questions
N/A

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper focuses on multi-task learning and multi-domain learning. Existing methods have not taken into account the characteristics of neurons, so a channel-wise parameter sharing method, CWPS, is proposed, achieving better results than the baseline.

### Strengths
1. CWPS has lower overhead for additional parameters compared to previous methods.
2. By using CPMS to determine the relationships between different tasks, it can effectively quantify these connections.

### Weaknesses
1. The paper argues that sharing at the neuron or channel level is important, but I think this requires more justification, as I didn’t see sufficient evidence for it in the paper. So, it doesn’t seem very different from other parameter-sharing methods, and the motivation behind the approach doesn’t seem very clear to me. Specifically, the paper lacks a clear explanation of why channel-wise sharing is superior to other granularities of sharing, such as layer-wise or even block-wise sharing. A more detailed analysis, perhaps through ablation studies, is needed to demonstrate the unique benefits of this specific sharing strategy. The current justification relies on the idea that neurons are fundamental units, but this is a very general claim and doesn't explain why sharing at the channel level is the most effective way to leverage this. 
2. The overall design of the method appears relatively simple, and the comparison results lack novelty. More experiments are needed to uncover the core reasons behind the improvements this method brings. The paper does not explore the sensitivity of the method to various hyperparameters, such as the number of shared channels or the criteria used for determining channel similarity. Without a thorough exploration of these factors, it's difficult to assess the robustness and generalizability of the proposed approach. Furthermore, the comparison with existing methods is limited, and the improvements reported are not substantial enough to convincingly demonstrate the superiority of the proposed method. 
3. The writing is poor.

### Questions
1. There is a lack of explanation regarding some baselines, as well as the approach to parameter sharing. Additionally, there are several prompt-like methods, such as DualPrompt.

### Soundness
2

### Presentation
2

### Contribution
2

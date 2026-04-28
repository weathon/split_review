# SHARP: Accelerating Language Model Inference by SHaring Adjacent layers with Recovery Parameters

- Decision: Reject
- Avg Score: 4.75
- Scores: 6, 3, 5, 5

## Abstract
While Large language models (LLMs) have advanced natural language processing tasks, their growing computational and memory demands make deployment on resource-constrained devices like mobile phones increasingly challenging. In this paper, we propose SHARP (SHaring Adjacent Layers with Recovery Parameters), a novel approach to accelerate LLM inference by sharing parameters across adjacent layers, thus reducing memory load overhead, while introducing low-rank recovery parameters to maintain performance.
Inspired by observations that consecutive layers have similar outputs, SHARP employs a two-stage recovery process: Single Layer Warmup (SLW), and Supervised Fine-Tuning (SFT).
The SLW stage aligns the outputs of the shared layers using  $\mathcal{L}_2$ loss, providing a good initialization for the following SFT stage to further restore the model performance. Extensive experiments demonstrate that SHARP can recover the model's perplexity on various in-distribution tasks using no more than 50k fine-tuning data while reducing the number of stored MLP parameters by 38\% to 65\%.
We also conduct several ablation studies of SHARP and show that replacing layers towards the later parts of the model yields better performance retention, and that different recovery parameterizations perform similarly when parameter counts are matched.
Furthermore, SHARP saves 42.8\% in model storage and reduces the total inference time by 42.2\% compared to the original Llama2-7b model on mobile devices.
Our results highlight SHARP as an efficient solution for reducing inference costs in deploying LLMs without the need for pretraining-scale resources.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes SHARP (sharing adjacent layers with recovery parameters) to accelerate LLM inference by sharing parameters across adjacent layers to reducing memory load overhead. The model performance is maintained through low-rank recovery parameters. Specifically, it employs a two-stage recovery process: SLW and SFT. Experiments results demonstrate the effectiveness in recover perplexity with a small amount of fine-tuning date while reducing the number of MLP parameters significantly. Also the inference time reduction was achieved compared to the original model on mobile devices.

### Strengths
+ This work follows a relative new methodology for efficient inference, i.e., adjacent layer-sharing strategy. While prior work focuses on training from scratch, this work focuses on deploying pretrained model in a resource-saving post-training way.

+ The proposed method is motivated by the robustness of LLM when replacing adjacent MLP layers and makes new observations in support of the layer-sharing strategy.

+ The two stages by SLW and SFT provide a good heuristics in layer-sharing. The work introduces low-rank weights to predict subsequent layers.

### Weaknesses
 - The experiments are not comprehensive enough to compare with state-of-the-art efficient inference methods.

- In the latency analysis, models are simplified with 4-bit quantization to fit in iPhone. However, that is not a valid implementation since direct quantization may degrade model performance. On the other hand, it shows that weight sharing is not sufficient to support efficient inference on edge devices.

### Questions
Although the work improves the model performance and run time performance significantly, it only compares with the direct sharing baseline. More comprehensive comparison with state-of-the-art efficient inference methods are needed to justify the advantage of the layer sharing strategy over other categories of strategy, like those mentioned in the paper, e.g., pruning or MobileLLM. The authors could comment on the advantages of weight sharing in terms of model performance, training cost, memory resources, etc. over other state-of-the-art methods.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a method to reduce model memory usage and increase inference speed by sharing parameters between adjacent layers and introducing low-rank recovery parameters to maintain performance. First, Single Layer Warmup (SLW) replaces a pre-trained layer by adding a LoRA adapter to the previous layer's weights. To warm up the LoRA adapter initially, it is trained to mimic the output of the original layer. Second, Supervised Fine-tuning (SFT) fine-tunes all LoRA adapters across layers to preserve model performance. This approach significantly improves performance compared to Direct Sharing and achieves similar performance to the original model while reducing model weights by approximately 62%.

### Strengths
The advantage of this paper is that it can reduce model parameters by more than 50% while maintaining similar performance to the baseline algorithm in some tasks. Especially, while full fine-tuning requires a lot of data, the initial warm-up using the L2 norm of the output of the original layer can be done in parallel, which helps improve performance. If the proposed algorithm still performs well after applying quantization to compress the model, it could further reduce the model weights in an orthogonal way to quantization.

### Weaknesses
The main drawback of this algorithm is that it is not beneficial for all tasks. For instance, in Table 6, while SHARP improves accuracy over Direct Sharing and even surpasses the original on the CommonsenseQA task, its accuracy significantly degrades compared to the original across most tasks, raising doubts about its overall utility. Of course, reducing the model size by half could lead to an accuracy drop, but I’m still curious whether the compressed model performs better than an originally smaller model. For example, while it might be possible to compress the LLaMA2-13B model down to 7B, I’m concerned that its accuracy could be lower than that of the original LLaMA2-7B model, which does not require a complex compression process.

The training process also has a complexity issue, particularly with applying SLW using the L2 norm. Since the paper highlights potential problems with using SFT alone, modifying the model structure effectively may be challenging. This concern is especially relevant for models more complex than Llama-2-7B, which was used in the study. If SLW fails, the model may not be optimized effectively. Unlike MobileLLM, which extends an existing model, this paper’s approach removes certain layers from a pre-trained model, introducing the risk that training may become unstable if SLW fails.

### Questions
1. Is the accuracy of a large model reduced by SHARP higher than that of a smaller model with an equivalent number of parameters? For instance, if the LLaMA2-13B model is reduced by 7B parameters using SHARP, does this new model outperform the existing LLaMA2-7B in accuracy? If so, it would effectively demonstrate the utility of SHARP (and I'm willing to increase the score if this question is answered).

2. In Table 2, it is described that the comparison is between the model after only SLW, only SFT, and the SHARP algorithm, but there seem to be no results for when only Stage 2 was applied.

3. I am curious whether this approach yields similar results when applied to larger models and when applied to recently released models like Llama-3.2.

4. If the model is BF16, the model size would be reduced to 1/4 with 4-bit quantization. I am curious about the results of applying the idea proposed in the paper after quantization.

5. Wouldn't attaching LoRA adapters to the entire model lead to even better performance?

### Soundness
3

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
This paper propose a layer sharing approach with additional low-cost finetuning to regaun the performance. After sharing the weights in the adjacent layers in the pretrained model, a two-stage lora-based finetuning is proposed, with one stage minimizing single layer output difference and the second stage recovering full model performance.

### Strengths
This paper provides a solid study on ways to regain model performance after layer merging. Experiments are conducted on both the ratio/location of layer merging and the ways to further finetune the model and regain performance. The paper is overall well-written and easy to follow. From the novelty perspective, layer sharing appears to be a new way of compressing pretrained large models, and the paper successfully show the runtime speed up on real devices, proving the proposed method as a promising research direction.

### Weaknesses
The main weakness of this work is two-fold, one is on the performance loss of the proposed method, and second is on the generalizability of the proposed finetuning method.
1. Although the proposed method show promising recovery performance on the PPL of pretraining dataset (Tab 2 and 3), we do observe significant performance drop on downstream tasks even after finetuning. This leaves me doubt if there's potential overfitting in the finetuning process, so that the performance on seen datasets are recovered but that on unseen tasks are not. A cross validation of finetuning datasets would be helpful on analyzing this issue. Additional techniques may need to be proposed to tackle overfitting. Specifically, the paper does not provide a detailed analysis of the variance in performance across different downstream tasks, making it difficult to understand the robustness of the proposed method. It is unclear if the performance drop is consistent across all tasks or if certain tasks are more susceptible to the layer sharing and finetuning process. Further investigation into the task-specific performance is needed to fully evaluate the effectiveness of the approach.
2. Although this paper sets its background as enabling layer sharing across adjacent layers, the majority of the method is focused on the two-stage finetuning to regain performance. Finetuning is typically applied in all model compression settings, not limited to layer sharing. The porposed 2-stage finetuning may also be useful on other model compression techniques. More clarifications on the contribution is needed, as whether the 2-stage finetuning is specifically proposed for the layer sharing task, or is it borrowed from previous techniques. The paper lacks a clear explanation of why the proposed two-stage finetuning is particularly well-suited for the layer sharing scenario, compared to other compression methods. It would be beneficial to provide a more detailed justification for the choice of this specific finetuning approach and how it addresses the unique challenges introduced by layer sharing.

### Questions
1. How would the model behave if the finetuning data and the evaluation task does not fully match? For example, will fineutning on GPT4-Alpaca only helps regain the performance on Arxiv-math?
2. Is the proposed 2-stage finetuning scheme limited to layer sharing? Or could it be used for other model compression methods?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper explores the approach of utilizing an adjacent layer-sharing strategy to compress LLMs by sharing parameters between neighboring layers. The primary motivation behind this approach is based on the observation that the output features of adjacent layers are significantly similar, which suggests the potential for parameter sharing to achieve more efficient communication and inference. The specific method used involves sharing parameters between adjacent layers and introducing a layer parameter tuning mechanism using a LoRA module. This two-part process initially focuses on minimizing the L2 loss of output between adjacent layers followed by a fine-tuning phase. The results are compared against direct parameter sharing without fine-tuning to highlight the benefits of the introduced method.

### Strengths
1. **Innovative Approach:** The methodology combines parameter sharing with fine-tuning using a LoRA module, presenting a new avenue in model compression that could potentially conserve computational resources while maintaining model accuracy.    
2. **Efficiency Gains:** The speed-up achieved through this method is notable, providing a practical solution for scenarios where faster inference is crucial, such as in mobile or edge computing environments.

### Weaknesses
1. **Performance in Downstream Tasks:** Despite the improvement in speed, the performance loss in downstream tasks is still significant, raising concerns regarding the practical applicability of the SHARP method in real-world scenarios where maintaining high levels of accuracy is paramount. The paper does not provide a detailed analysis of how the layer sharing affects the model's ability to generalize to unseen data, nor does it explore the potential for catastrophic forgetting in downstream tasks due to the parameter sharing and fine-tuning process. It is crucial to understand the trade-offs between speed and accuracy, especially in tasks where even small performance drops can have significant consequences.

2. **Ambiguity in Communication Definition:** The article does not clearly define what is meant by "communication" in the context of parameter sharing. It is essential to clarify whether it refers to internal model communication, information flow between layers, or external communications between distributed components. The lack of a precise definition makes it difficult to assess the true benefits of the proposed method, as the term 'communication' could be interpreted in multiple ways, each with different implications for the method's effectiveness and applicability. For example, if the 'communication' refers to the data transfer between layers during forward/backward passes, the speedup might be limited by the memory bandwidth rather than the parameter sharing itself. 

3. **Lack of Comparative Analysis:** The authors failed to include comparisons with alternate model compression techniques, such as LLM pruning, despite they also attempt to drop the LLM parameters while retaining performance. Such a comparison could have provided a more comprehensive understanding of how this new method stacks up against traditional approaches in terms of parameter reduction, tuning overhead, and performance impact. Without such comparisons, it is difficult to determine whether the proposed method offers a genuine advantage over existing techniques or if it is simply a different approach with similar limitations.

### Questions
Please see the weakness part

### Soundness
3

### Presentation
3

### Contribution
2

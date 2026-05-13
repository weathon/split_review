# PaCA: Partial Connection Adaptation for Efficient Fine-Tuning

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Prior parameter-efficient fine-tuning (PEFT) algorithms reduce memory usage and computational costs of fine-tuning large neural network models by training only a few additional adapter parameters, rather than the entire model. However, the reduction in computational costs due to PEFT does not necessarily translate to a reduction in training time; although the computational costs of the adapter layers are much smaller than the pretrained layers, it is well known that those two types of layers are processed sequentially on GPUs, resulting in significant latency overhead. LoRA and its variants avoid this latency overhead by merging the low-rank adapter matrices with the pretrained weights during inference. However, those layers cannot be merged during training since the pretrained weights must remain frozen while the low-rank adapter matrices are updated continuously over the course of training. Furthermore, LoRA and its variants do not reduce activation memory, as the first low-rank adapter matrix still requires the input activations to the pretrained weights to compute weight gradients. To mitigate this issue, we propose **Pa**rtial **C**onnection **A**daptation (**PaCA**), which fine-tunes randomly selected partial connections within the pretrained weights instead of introducing adapter layers in the model. PaCA not only enhances training speed by eliminating the time overhead due to the sequential processing of the adapter and pretrained layers but also reduces activation memory since only partial activations, rather than full activations, need to be stored for gradient computation. Compared to LoRA, PaCA reduces training time by 22\% and total memory usage by 16\%, while maintaining comparable accuracy across various fine-tuning scenarios, such as fine-tuning on the MMLU dataset and instruction tuning on the Oasst1 dataset. PaCA can also be combined with quantization, enabling the fine-tuning of large models such as LLaMA3.1-70B. In addition, PaCA enables training on 23\% longer sequence data and improves throughput by 16\% on both NVIDIA A100 and INTEL Gaudi 2 GPUs compared to LoRA. The code is available at [https://anonymous.4open.science/r/paca-366F](https://anonymous.4open.science/r/paca-366F).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents PaCA (Partial Connection Adaptation), a new method for parameter-efficient fine-tuning (PEFT) aimed at large models. Instead of adding adapter layers as in LoRA, PaCA fine-tunes only a selected subset of connections within the pretrained weights, which are chosen at random. This approach aims to reduce memory usage and training time without sacrificing accuracy. The authors provide theoretical backing and empirical results that suggest PaCA offers efficiency gains over existing methods, maintaining competitive performance on selected datasets.

### Strengths
Below is the list of the strong points identified in this work:

- One key strength of PaCA is that its selective adaptation of pretrained weights eliminates the need for additional adapter layers, which in turn reduces both latency and memory requirements. This is a promising approach that may lead to faster and more efficient fine-tuning, especially valuable for large-scale language models.
- Additionally, PaCA is compatible with quantisation techniques, expanding its potential to handle even larger models.
- The authors provided a convergence analysis that theoretically supports PaCA’s efficiency and stability, giving a mathematical foundation to their claims.
- Empirical evaluations are promising.

### Weaknesses
Below is the list of weaknesses that I would like to see refuted or clarified by the authors:

- The primary limitation of the study is that it evaluates PaCA on a narrow set of models and datasets, leaving its generalisability to more complex or diverse tasks uncertain. Testing PaCA across a broader range of tasks and model architectures would strengthen the evidence for its effectiveness. Specifically, the current evaluation focuses on large language models; it is unclear how well PaCA would perform on other architectures such as convolutional networks or vision transformers, which have different parameter structures and learning dynamics. The lack of experiments on a variety of tasks, such as those involving different modalities (e.g., vision, audio), also limits the conclusions that can be drawn about the method’s robustness.

- Additionally, the method’s random selection of connections for fine-tuning is not fully explored or justified, and it remains unclear how this choice impacts performance or whether an alternative selection strategy could yield better results. The paper does not provide any analysis on the distribution of the selected connections, or whether certain layers or types of connections are more important than others. It is also unclear if the random selection is consistent across different runs or if the performance varies significantly depending on the random seed. Why not evaluate some optimisation or search strategies instead, such as a greedy approach that selects connections based on their gradient magnitudes or a more structured approach that selects connections based on their location within the network?

- Another area for improvement is in the analysis of quantisation impacts. The current study lacks an in-depth look at how quantisation affects precision and performance at larger scales, which reduces clarity on how well PaCA might scale. The paper does not explore different quantization levels or their impact on the final performance, nor does it investigate how quantization interacts with the random connection selection strategy. It is also unclear if the benefits of PaCA are maintained when combined with more aggressive quantization techniques.

### Questions
Authors are requested to clarify or make changes, as appropriate, based on what is discussed in the ‘Weaknesses’ section.

Some minor comment:
- Providing more intuitive descriptions alongside the theoretical sections would improve readability for a broader audience.
- The expedient of unifying the equal columns of some tables in Appendix B rather than lightening the visual load tends to make it unattractive. It would be much better to fill each column even with the same value.

### Soundness
2

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
The paper addresses parameter-efficient fine-tuning (PEFT) for large language models (LLMs), highlighting a key limitation in existing PEFT methods: reduced compute doesn't necessarily translate to faster training due to the sequential processing of adapter layers alongside pretrained weights. This sequential approach underutilizes hardware resources and incurs latency, as GPUs typically handle one kernel at a time. Tools like CUDA streams can help parallelize processing but come with management and synchronization overheads.

LoRA and its variants merge low-rank adapter matrices with pretrained weights to avoid this latency during inference, but this solution isn't applicable during fine-tuning, as adapter matrices must be trained separately. Additionally, LoRA doesn't reduce activation memory usage compared to Full Fine-Tuning (Full-FT), since input activations still need to be stored for gradient calculations. Thus, despite computational optimizations, sequential processing and memory demands remain challenges in PEFT methods.

Given the motivation, the authors propose PaCA (Partial Connection Adaptation), a memory-efficient parameter-efficient fine-tuning (PEFT) method that fine-tunes randomly selected partial connections in pretrained weights, without using adapter layers. Unlike prior PEFT approaches, PaCA reduces training time by integrating the forward and backward operations for both pretrained and partial connections, thus avoiding sequential processing. By only requiring the corresponding activations for gradient calculations, PaCA significantly lowers activation memory usage.

The authors provide a theoretical proof of convergence for PaCA and demonstrate through experiments that it achieves substantial reductions in both training time and memory consumption compared to prior PEFT methods, while maintaining comparable accuracy across various fine-tuning scenarios and GPU types.

PaCA not only reduces training time by 19% compared to LoRA but also lowers memory usage by storing fewer activations during training. The authors back up these claims with both a theoretical convergence proof and a thorough set of experiments that demonstrate PaCA’s ability to achieve comparable accuracy while being faster and more memory-efficient. PaCA increased the maximum sequence length by 23%, 108%, and 23% compared to LoRA, DoRA, and MosLoRA by storing only partial activations instead of all input activations. They show the highest throughput among the methods discussed in Fig 3 on two different GPUs. They also show what quantization combined with their method PaCA looks like and compare their method to QLoRA. Overall, the authors found near-maximum performance with the lowest memory and finetuning time overhead.

The paper presents a compelling solution to making large model fine-tuning more practical and scalable. It is a well-executed work with promising implications for efficient model fine-tuning.

### Strengths
i) The concept of selecting and fine-tuning only partial connections in the pretrained weights without adapter layers is novel and effectively addresses some of the inefficiencies of existing PEFT methods, like the latency introduced by sequential processing.

ii) By eliminating the need for adapter layers and reducing the activations that need to be stored, PaCA successfully reduces both training time and memory footprint. The motivations and the contributions are clearly demonstrated in text and in Fig 2.The empirical results show significant improvements over LoRA and its variants. 

iii ) The authors provide proof of convergence for PaCA, ensuring that the proposed method can effectively minimize the loss in general neural networks.

iv)  PaCA's reduction in memory and computational overhead is good for resource-constrained environments, such as edge devices. The authors also present results with the best throughput in two GPUs over rest of the referred works.

v) The paper includes a comprehensive set of experiments across different scenarios, including fine-tuning for specific tasks, instruction tuning, and using quantized versions (QPaCA). Comparisons with SOTA methods such as LoRA, DoRA, and MosLoRA provide a well-rounded perspective on PaCA's performance gains. The sequence length supported by PaCA also exceeds that of other referred methods. 

Overall, it is a good paper with good analysis.

### Weaknesses
i) The random selection of partial connections is a key component of PaCA. Yet, there is limited discussion on how this selection impacts training quality and whether alternative strategies could improve performance. A deeper exploration of the effect of different selection criteria on convergence and accuracy would significantly strengthen the paper. For instance, the paper does not explore the variance in performance that might arise from different random seeds used to initialize the selection process, which could impact the robustness of the method.

ii) On a similar note, an empirical or theoretical analysis of the importance of selecting specific columns could have been highly informative. The paper lacks a discussion on whether certain columns within the weight matrices are more critical for fine-tuning than others, and if so, how the random selection might be sub-optimal. An analysis of the singular values or other measures of column importance could provide valuable insights.

iii) The convergence analysis relies on the gradient's Lipschitz continuity, but this is a standard assumption that may not hold for many real-world large-scale neural networks. A more detailed discussion of how these theoretical guarantees translate into practice and the possible limitations would have been helpful. Specifically, the paper does not address the potential for the gradient to exhibit significant variations in magnitude during training, which could violate the Lipschitz condition and affect convergence. The analysis should include a discussion of how the method behaves when this assumption is not met.

iv) Equations 2, 5 and 8 are incorrectly written.

### Questions
1)  Are there results on how the improvements and the convergence time vary if a different set of random connections are selected during finetuning?

2) Have the authors considered different strategies for selecting partial connections, such as importance-based or gradient-based selection, to determine if these approaches lead to improved convergence or accuracy compared to random selection?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose PaCA, a novel PEFT algorithm selecting only partial connections within pretrained weights for finetuning, that reduces memory usage and compuational cost compared to LoRA and its variants. 
The paper contains both an empirical evaluation of the effectiveness of PaCA in finetuning LLMs and a theoretical prove of the loss convergence in general neural networks when using PaCA.

### Strengths
- The empirical evaluation shows a significant reduction in resource consumption when using PaCA, while being able to achieve similar results to LoRA and several of its variants (DoRA, MosLoRa, ...).
- The authors include an extension of their method that works with quantized pre-trained weights, which further increases the applicability of their proposed technique.
- The proof of convergence is very useful, not only for PaCA, but also for algorithms using similar partial updating strategies.

### Weaknesses
 - Especially for on-device training of fully quantized CNNs on embedded systems/microcontrollers, updating only partial connections is already a well-known technique [1], [2].
- Both [1] and [2] use heuristics ([1] has an offline heuristic based on XAI, [2] an online heuristic based on the magnitude of structures in feature maps) to decide which subset of weights to update compared to the potentially inferior random selection approach proposed in this work.


### Questions
- For what kind of operators and NN "types" does the proposed technique apply? The paper initially focuses on MLPs ("linear layers"), but this seems to be only exemplary, as the evaluation is then performed for LLMs. Does the proposed technique also apply to e.g. CNNs ("convolutional layers")? 
- Figure 1. right graph: are these real measured numbers or is the graph just symbolic? If they are real numbers, their order of magnitude should be shown on the y-axis, as in Figure 2, otherwise I do not understand what new information not already discussed in the text is gained by the reader by showing it.
- Eq. 1-9 seem imprecise to me. For example, in Eq. 2 should it not be something like $\nabla X_{i-1} = W^T * \nabla X_i$ since the error signal of the previous layer $i-1$ is calculated based on the error signal of the current layer $i$ instead of the "in-place" update of $\nabla X_{in}$ shown in the paper?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors proposed a novel method for PEFT, named Partial Connection Adaptation(PaCA). PaCA fine-tunes randomly selected partial connections in pre-trained weights instead of using adapter layers like LoRA. This innovation leads to a faster training speed and reduced memory usage while maintaining almost similar accuracy. The authors presented results on fine-tuning large models such as LLaMA3, demonstrating PaCA's ability to reduce training time by 22% and memory usage by 16%.

### Strengths
1. PaCA could significantly reduce memory usage and training time compared to other PEFT methods like LoRA by avoiding the need for additional adapter layers.

2. PaCA performs well with large models and long sequence data, increasing the maximum sequence length and improving throughput.

3. The authors provide theoretical analysis to demonstrate that PaCA effectively converges for general neural networks.

### Weaknesses
1. The authors choose to randomly select partial connections in PaCA instead of using some strategic selection. How could the random selection be generalized when fine-tuned with PaCA? Could a more targeted selection improve the performance?

2. While this paper only presents results on LLaMA models, it would be beneficial to see how PaCA performs on a wider range of architectures, such as non-transformer-based models or other tasks beyond language models.

3. Does PaCA introduce any stability issues in training, particularly when fine-tuning very large models with longer sequence lengths?

### Questions
see weaknesses above

### Soundness
4

### Presentation
4

### Contribution
3

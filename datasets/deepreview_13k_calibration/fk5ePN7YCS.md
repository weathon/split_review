# NEPENTHE: Entropy-Based Pruning as a Neural Network Depth's Reducer

- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 3, 6, 3

## Abstract
While deep neural networks are highly effective at solving complex tasks, their computational demands can hinder their usefulness in real-time applications and with limited-resources systems. Besides, for many tasks it is known that these models are over-parametrized: neoteric works have broadly focused on reducing the width of these networks, rather than their depth.\\
In this paper, we aim to reduce the depth of over-parametrized deep neural networks: we propose an e\textbf{N}tropy-bas\textbf{E}d \textbf{P}runing as a n\textbf{E}ural \textbf{N}etwork dep\textbf{TH}'s r\textbf{E}ducer (NEPENTHE) to alleviate deep neural networks' computational burden.
Based on our theoretical finding, NEPENTHE focuses on un-structurally pruning connections in layers with low entropy to remove them entirely. We validate our approach on popular architectures such as MobileNet and Swin-T, showing that when encountering an over-parametrization regime, it can effectively linearize some layers (hence reducing the model's depth) with little to no performance loss. The code will be publicly available upon acceptance of the article.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents NEPENTHE, a pruning method designed to reduce the depth of over-parameterized deep neural networks, addressing their computational inefficiency in real-time applications. Unlike traditional pruning that focuses on reducing model width, NEPENTHE uses an entropy-based unstructured pruning technique to target and remove entire low-entropy layers, effectively shrinking the network's depth without compromising performance. NEPENTHE is validated on models like MobileNet, Swin-T, and RoBERTa and demonstrates that certain layers can be linearized when networks are over-parameterized, leading to reduced computational demands while retaining accuracy.

### Strengths
Quality and Clarity
- The paper is clearly written, with sufficient background and motivation for the problem

Originality and Significance
- The proposed iterative entropy guided pruning scheme is novel 

Experiments
- The paper studies the generalizability of the method across wide variety of models and applications ranging from a Resnet for classification to a RoBERTa for language tasks
- The paper provides thorough details on the experimental setup (in the appendix)
- The analyses provided on neuron states per layer, allowing to drop entire layers (hence allowing for some structured sparsity and latency gains) is interesting and valuable contribution
- The ablation study provided in Table 4 depict the value of each component of NEPENTHE

### Weaknesses
 - I find the model types studied to to limited. Since overparameterization is most prelevant in modern decoder-only language models, I think studying this approach eg: on a Llama-3.1-8B and larger scales would greatly improve the applicability and impact of the work
- Baselines: The paper mainly compares against Iterative magnitude pruning and comparison with more recent pruning methods is missing [1,2,3,4] and [5,6,7] for large language models. I encourage the authors to also compare to different baselines in terms of compute time taken for pruning and also compare against zero-shot pruning methods (after recovery fine-tuning).
- Given that the method relies on expensive training after every iteration of weight pruning, this makes adopting the method to much larger scales inefficient. Could the authors comment on the scalability of the method?
- Latency gains in practice: Given that NEPENTHE does not guarantee completely sparse prunable layers, hence structured pruning. I find the practical latency gains of the method quite limited, if they cannot be enforced/specified by the user.

### Questions
Questions
- Check weaknesses
- Did the authors observe any particular trends in the layer types that are typically dropped or have larger number of neurons set to "off" state. Are the observations different across model families?
- How does the compute time for NEPENTHE compare to different baselines?
- Given that perplexity often doesn't translate to donwstream task performance (in-context learning properties) for decoder-only LLMs [1]. How do the authors see NEPENTHE being extended to large language models? Given that NEPENTHE requires iterative training, could the authors comment on the scalability of the approach?

[1] Jaiswal, A., Gan, Z., Du, X., Zhang, B., Wang, Z. and Yang, Y., 2023. Compressing llms: The truth is rarely pure and never simple. arXiv preprint arXiv:2310.01382.

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
4

### Summary
The paper presents an iterative pruning method to reduce network depth, based on layer entropy. The layer entropy is based on neuron entropy, which is defined based on the sign of the output activation. They further have an entropy aware pruning score and put it into an iterative pruning algorithm. Experiments on some small-scale datasets on image classification and NLP show the potential merits of the method.

### Strengths
1. Not so many pruning papers focuses on reducing depth of deep models. Depth reduction can bring significant speedup. 

2. The idea of using entropy for unstructured pruning sounds interesting, esp. the study of the effect of pruning on layer entropy (Sec. 4.2).

### Weaknesses
1. Methodologically, the method may have clear flaws.
- The entropy of a neuron is defined based on its sign. I am not sure if this is grounded. For ReLU networks, the neuron's output is nearly always positive, then the entropy is 0, and thus can be removed according to this paper. This is clearly not correct. The authors claim to exclude the value '0' when calculating entropy, but this does not address the core issue that the sign alone is insufficient to capture the information content of a neuron's activation. The method essentially bins the continuous activation into discrete states based on sign, which is a crude approximation. The information lost in this discretization is not accounted for, and it's unclear why a binary or ternary state representation is sufficient for capturing the complexity of neuron activations.
- L186: "The output of the i-th neuron is always the same as its input, this neuron can in principle be absorbed by the following layer as there is no non-linearity between them anymore." -- this statement is also baseless. It only applies to ReLu networks, while for networks with other activation functions (such as sigmoid), even when the output of a neuron is always positive, the nonlinearity cannot be omitted. Even for ReLU, the statement is not universally true, as the neuron could be part of a skip connection or have other architectural dependencies that prevent simple absorption.
- L198 - 205, the method derivation is based on weight Gaussian and input Gaussian assumptions. I am not sure they really hold in today's practical models. While weight initialization may approximate a Gaussian, the input distribution is highly dependent on the data and the network's processing, and it's unlikely to remain Gaussian throughout the network's depth. The authors need to provide empirical evidence that these assumptions hold for their specific experiments, not just cite existing works that make similar assumptions.

2. As pointed in the paper, the method needs iterative pruning which is very costly. And this invites the comparison fairness problem. For many pruning methods, they do not need so many training epochs. And we know the training epochs will impact the performance significantly. The question is, if the other methods, equipped with the same long training epochs, will they just compete the proposed method?


3. Experiments
- Some of the results look strange. Tab. 1, why resnet18 on cifar10 only has 91.66% top1 accuracy? ResNet56 can easily get to 93.5% and ResNet18 is designed for ImageNet, which has many more params than ResNet56. The authors need to investigate this discrepancy and provide a more convincing baseline. Using the same training configurations as other papers does not guarantee the validity of the results if the configurations themselves are not optimal or are not well-suited for the specific task and architecture.
- Most of the compared methods are baseline approaches, probably implemented by the authors, lacking comparison with more recent papers.


4. (presentation, writing) issues and questions
- Eq 2, missing punctuation.
- One closely related work is missing - https://proceedings.neurips.cc/paper/2016/hash/41bfd20a38bb1b0bec75acf0845530a7-Abstract.html
- the function Weights to prune -> The function
- this neuron can in principle be absorbed by -> This

### Questions
Are there any results on ImageNet-1K with Resnet50 and a ViT model like Vit-B/16?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents NEPENTHE, an approach aimed at reducing the depth of over-parametrized deep neural networks (DNNs) to decrease computational demands. This method uses an entropy-based strategy to prune layers that exhibit low entropy, allowing for the removal of entire layers from the network with minimal performance loss. The approach is validated on architectures like MobileNet, Swin-T, and RoBERTa.

 NEPENTHE utilizes unstructured pruning that is guided by the entropy of neuron activation within each layer. By re-weighting the pruning process based on entropy levels, the method prioritizes the removal of layers with the lowest entropy. The technique is supported by both theoretical findings and empirical results, showcasing effective reduction of network depth without significant degradation in model performance.

### Strengths
Innovation in Pruning: The approach is novel in its use of entropy as a criterion for pruning, shifting the focus from width reduction to depth reduction, which is less explored.
Comprehensive Evaluation: The method is thoroughly tested across several datasets and architectures, providing a robust validation of its effectiveness.
Preservation of Performance: NEPENTHE successfully demonstrates the preservation of model performance even with significant reductions in network depth, addressing a common challenge in neural network pruning.

### Weaknesses
Complexity in Implementation: The entropy-based pruning requires careful calibration and may introduce complexity in tuning the parameters for optimal performance across different architectures. Specifically, the method relies on calculating the entropy of neuron activations, which necessitates a hyperparameter controlling the threshold for low entropy. This threshold, if not carefully chosen, could lead to either excessive pruning, resulting in significant performance degradation, or insufficient pruning, failing to achieve the desired reduction in network depth. Furthermore, the process of re-weighting the pruning based on entropy levels adds another layer of complexity, requiring careful consideration of the weighting scheme to ensure that layers with genuinely low information content are prioritized for removal. 
Limited Discussion on Scalability: The method's scalability to extremely large networks is not thoroughly addressed. While the paper demonstrates results on models like MobileNet, Swin-T, and RoBERTa, these are not the largest models currently used in deep learning. The computational overhead of calculating entropy for each layer in extremely large models, such as those with billions of parameters, could be substantial. The paper lacks a discussion on how the proposed method would perform in such scenarios, and whether the entropy calculation and pruning process would become a bottleneck. 
The function weights_to_prune which includes the whole logic behind the pruning idea is not explained in the main paper.

### Questions
Could you provide detailed statistics on the percentage of parameters pruned by the NEPENTHE method compared to other pruning approaches? This information would be valuable for a comprehensive assessment of the method's efficiency and its impact on the overall computational resources required for both training and inference.

How does the removal of different types of layers (e.g., convolutional vs. fully connected) affect the overall network architecture? Are certain layers more "entropy-critical" than others?

How do you choose which samples to use to compute the probability of being on or off of each neuron?

Does the reduced depth network generalize to different dataset as in the lottery ticket hypothesis?

References:
Frankle, Jonathan, and Michael Carbin. "The lottery ticket hypothesis: Finding sparse, trainable neural networks." arXiv preprint arXiv:1803.03635 (2018).

ElAraby, Mostafa, Guy Wolf, and Margarida Carvalho. "OAMIP: optimizing ANN architectures using mixed-integer programming." International Conference on Integration of Constraint Programming, Artificial Intelligence, and Operations Research. Cham: Springer Nature Switzerland, 2023.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes a method to perform pruning of trained neural network. The approach is based on per layer entropy and removes entire layers to target a faster model. The paper connects entropy based pruning and weight magnitude pruning, and arrives into a single criteria per layer. The method requires training of the model.

### Strengths
- Layer pruning has its benefits such as speeding up the model on GPUs. Other techniques like unstructured pruning does not.
- The approach is relatively simple according to equations, and requires measuring "frequency" of activations, with later normalization.

### Weaknesses
 - The approach is tested on out-dated models and datasets and as a result is compared with non so recent models.
- Depth pruning is recently studied in LLMs. Most approaches don't require fine-tuning. The proposed approach should be compared to those to demonstrate that the metric is better. 

### Questions
For Table 2, did authors reimplemented other techniques for comparison, or took numbers from external source?

### Soundness
2

### Presentation
2

### Contribution
1

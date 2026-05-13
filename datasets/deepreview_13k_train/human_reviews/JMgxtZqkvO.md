# Memory-Efficient Fine-Tuning via Structured Neural Network Pruning

- Decision: Reject
- Scores: 3, 5, 5, 5

## Abstract
Fine-tuning is an important step in adapting foundation models such as large language models to downstream tasks. To make this step more accessible to users with limited computational budgets, it is crucial to develop fine-tuning methods that are memory and computationally efficient. Sparse Fine-tuning (SFT) and Low-rank adaptation (LoRA) are two frameworks that have emerged for addressing this problem, and have been adopted widely in practice. In this work, we develop a new SFT framework, based on ideas from neural network pruning. At a high level, we first identify "important" neurons/nodes using feature importance metrics from network pruning (specifically, we use the structural pruning method), and then perform fine-tuning by restricting to weights involving these neurons. Using experiments on both vision and language tasks, we demonstrate that our method significantly improves the memory efficiency of SFT without increasing training time complexity and implementation complexity, while achieving accuracy comparable to state-of-the-art methods such as LoRA and its variants.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper discusses a method where they start by identifying "important" neurons or nodes using structural pruning metrics and then fine-tune by focusing only on the weights associated with these neurons. The proposed method performs well on the datasets selected by the authors. However, the paper appears to have been completed rashly, with significant issues in the coherence between sections, a lack of basic comparisons with other baseline methods, and missing experiments on more datasets. I believe the paper requires substantial revision to be considered for acceptance. Although I am inclined against accepting it, I am open to changing my view if persuaded.

### Strengths
1. The article validates the proposed method with extensive experiments on both vision and language tasks, which helps in establishing the robustness and applicability of the technique across different domains.

2. It provides a comprehensive comparison with existing state-of-the-art methods like LoRA, demonstrating improvements in memory efficiency methods and maintaining comparable accuracy, which is crucial for practical applications.

### Weaknesses
1. The layout of tables in the paper has issues. For instance, there is a large gap between Table 2 and Table 3. Additionally, the full names of "dft" and "hft" are not provided in Table 2, and placing your method in the middle of the table makes feels confusing.
2. Lack of experiments on ImageNet-10/CUB200/Caltech101. At least a dataset with high resolution. Since your experiments are mainly conducted on the CIFAR-100 or TinyImageNet, I have a concern that your method only work on the these datasets.
3. Lack of comparisons with existing baseline methods. e.g. LoRAPrune[1].
4. Limited novelty. In light of the extensive discussions around LoRA and its variants, the contribution of these hybrid methods seems insufficient.

### Questions
Please convince me and make me believe that the weaknesses I identified in the paper do not actually exist.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presented a parameter-efficient fine-tuning method inspired by techniques used in network pruning. The proposed method identifies and fine-tunes only the most important neurons selected using a pre-defined importance metric. The method is similar to low-rank adaptation (LoRA) in that it also formulates the weight updates as the product of two low-rank matrices. However, one of the low-rank matrices is fixed to binary values determined from the importance metric, while the other matrix is initialised as zeros and trained. Therefore, the method achieves high parameter efficiency, and the experiments also demonstrate competitive performance over vision and language models.

### Strengths
1. The method is well-grounded in network pruning research, which has long sought to reduce model complexity while retaining performance by focusing on the more important weights of a model. By leveraging structured pruning and importance metrics, i.e., the Taylor score and L2 norm, the proposed method identifies the output channels that contribute most to the performance. The method is thus very well motivated.

2. PEFT methods such as LoRAs already are already parameter efficient. The proposed method further reduces the number of learnable parameters by fixing one of the low-rank matrices. This leads to even lower learnable parameter count and additional memory save.

3. The experiments are fairly comprehensive, covering both vision models, e.g., ViT, ResNet, and language models, e.g., DeBERTa, Llama. These experiments provide ample evidence on the model's efficiency and performance across a wide range of tasks.

### Weaknesses
1. There is a lack of strong evidence on the advantage of the proposed method. The title of the paper focuses on the memory efficiency of the method. However, in most of the tables, the memory consumption of the proposed method is not included. There is only a small section (Sec. 5.4) that briefly mentions the memory footprint. This only provides one data point, and is not comprehensive enough to justify the title. More specifically, Table 6 shows a comparison against LoRAs using Llama models, without any conclusive evidence. The proposed method leads to lower parameter count, but also significantly lower performance in many cases. It is perhaps a more fair comparison to either scale both methods to the same parameter count and compare the performance, or the other way around. In addition to this, showing a curve of performance vs. parameter count/memory consumption of the two methods would largely benefit the argument.

2. A few more minor comments.
(a) Tables and figures are placed at the top of the page as a convention.
(b) Some notations are sloppy. In L161, there is no reason to enumerate the values of rows for matrix $M$. Simply use i as the index. In Eq.6, $F - c_i$ is a very crude notation. It's better to just use a new symbol. Furthermore, the paper lacks a deeper analysis of the method's formulation. Specifically, the operation $MW_f$ effectively zeros out rows of $W_f$ based on the binary mask $M$, and averages the remaining rows. The rows zeroed out are those with small norms based on the selection criteria of $M$. This should be explicitly stated to improve the reader's understanding. Finally, the paper would benefit from a theoretical analysis of how this handcrafted $M$ impacts the approximation of the true weight update and the resulting error.

### Questions
N/A

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
The paper proposes a Structured-Pruning-based Sparse Fine-Tuning (SPSFT) method that combines neural network compression and matrix decomposition techniques to significantly reduce memory and parameter requirements while achieving performance comparable to existing methods such as LoRA in both vision and language tasks. It is the first to apply network pruning to fine-tune large models, particularly by using structured pruning to identify and select important neurons for fine-tuning, achieving parameter and memory efficiency. The paper also provides guidance on hyperparameter and training configuration choices to help users achieve efficient and high-accuracy fine-tuning results across different tasks.

### Strengths
(1): The SPSFT method uses structured pruning and matrix decomposition to greatly reduce memory and parameter requirements while maintaining performance, suitable for scenarios with limited computational resources.
(2): The approach is modular, allowing different pruning strategies to be used, making it adaptable to various task requirements.
(3): The method performs well across both vision and language tasks, demonstrating good generalizability.

### Weaknesses
(1): Please clarify the term "QTaylor" mentioned in line 365. Ensure it is defined within the context of your study or provide relevant references. Consistent use and clear definition across the manuscript are crucial for reader comprehension.
(2): Could you elaborate on your choice of datasets for the classification tasks? Additionally, please discuss the potential applicability or comparability of your findings to larger, established datasets like ImageNet to enhance the generalizability of your results.
(3) Consider incorporating the standard 8 zero-shot datasets commonly used in fine-tuning tasks on Llama, if feasible. Additionally, including an AVG (average) metric could provide a holistic view of the model’s performance across tasks. If these datasets were not used, please provide a rationale for your selection.
(4): Please provide a detailed comparison of your model's parameter count and performance with LoRA, particularly at comparable scales. Discuss any trade-offs involved, which would help elucidate the practical implications of your approach.
(5):There are several LoRA variants that have reported improvements in parameter efficiency. Could you compare your approach against key variants such as [DoRA,  VeRA, SVFT, LoRA-XS]? This comparison would be valuable in highlighting the distinct advantages or potential areas for enhancement in your method.
(6): The figure presented in the main text could be enhanced for better clarity and information delivery. Consider adding detailed legends, clearer labels, or supplementary figures that demonstrate performance comparisons or efficiency gains. Visual aids are instrumental in conveying complex information effectively.

### Questions
(1): Carefully check for spelling errors in the paper.
(2): Provide a fair comparison with LoRA at the same parameter scale, and report performance on 8 datasets along with the AVG metric.
(3): Consider comparing with some of the LoRA variants.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes an improvement to the the efficiency of parameter-efficient finetuning (PEFT) by using a finetuning neuron-level mask, rather than a low-rank decomposition, to perform finetuning. This allows the authors to finetune only a small number of parameters, freezing the rest. The fact that the parameters are organized in matrix rows (corresponding to entire neurons) makes the process efficient, and more so than LoRA for the same number of parameters.

### Strengths
The paper clearly lays out its method and the arguments for its method and the method itself is overall well-explained. The authors discuss their experimental choices and add an additional, helpful section on the practical considerations of memory requirements when using the Adam optimizer.

The idea of a class-aware Taylor importance is nice and is a useful side contribution of the paper.

### Weaknesses
1. This paper unfortunately does not position itself appropriately with regard to the state of the field. In particular, RoSA [1] considers using a sparse finetuning mask combined with a low-rank adaptation, finding that sharing the parameter budget between the two approaches works better than either in isolation.

    Other relevant work is missing as well. For example, model compression methods are also used for model adaptation even without finetuning [2].  The related work section also fully omits any mention of sparse training methods, of which there are many; most relevant to this work might be the Movement Pruning method [3] and the FISH-Mask method [4].

    Overall, I would suggest removing the claim “ours is the first work that can integrate the literature on model compression for morel fine-tuning”. Further, the proposed method should be benchmarked against RoSA, or, better yet, a combination of this paper’s pruning approach with a low-rank component.

2. The claim that “the computational overhead required for computing Taylor importances is already prohibitively large!” (line 187) is not correct. The SparseGPT method, which the authors cite, relies on an approximate Taylor importance. So does the ZipLM method, which applies to structured pruning.

3. For the image classification task, assuming that the models were pretrained on ImageNet, the transfer tasks are very similar. It would have been more informative to also see cases where the downstream tasks are from a quite different distribution - for instance, some of the ones used in [5], such as Aircraft, flowers, etc.

4. The section on considering parameter dependencies in importance evaluation (line 262-271) is not clearly written, and the computation of the parameter budget was confusing. The whole idea of parameter dependencies doesn’t seem to add much, since the approach is actually unhelpful (per the experimental results). I am not sure why the authors make the claim “structured pruning considers parameter dependencies in its importance evaluation” (line 262), and there is no citation given.

5. Some experimental details are lacking. For the image classification tasks, the authors omit any mention of what dataset the models are pretrained on, if any. Additionally, the results do not have any sort of error bars, making it difficult to judge whether the improvements have any significance.

### Questions
How does the proposed method compare with RoSA? Can even better results be achieved from combining this method with a low-rank component?

Please expand the related work section as outlined in the 'weaknesses', above

Please expand the performance evaluation in computer vision to more OOD tasks as in [5], above

### Soundness
3

### Presentation
2

### Contribution
2

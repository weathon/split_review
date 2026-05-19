### Summary

This paper introduces a novel pruning method, termed WANDA, designed to induce sparsity in pretrained LLMs. The method prunes weights with the smallest magnitudes multiplied by the corresponding input activations, on a per-output basis. Notably, WANDA requires no retraining or weight update, and the pruned LLM can be used as is. The paper evaluates WANDA on LLaMA and LLaMA-2 across various language benchmarks, demonstrating that it significantly outperforms the established baseline of magnitude pruning and performs competitively against recent method involving intensive weight update.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel pruning method, WANDA, that is simple yet effective for LLMs. The method does not require retraining or weight updates, making it computationally efficient.
2. The paper provides a thorough evaluation of WANDA on LLaMA and LLaMA-2 models across various language benchmarks. The results show that WANDA outperforms magnitude pruning and performs competitively with recent methods involving intensive weight updates.
3. The paper discusses the potential of WANDA for structured N:M sparsity and its connection to existing pruning methods. This provides a comprehensive understanding of the method and its relationship to other pruning approaches.

### Weaknesses

#### Some Related Works


#### comment

1. The paper focuses on pruning LLMs, but it is not clear how well the method would generalize to other types of models or tasks. It would be beneficial to evaluate WANDA on a wider range of models and tasks to assess its generalizability. Specifically, the paper lacks experiments on models with different architectures, such as convolutional neural networks or recurrent neural networks, and on tasks beyond language modeling, such as image classification or object detection. This limited evaluation makes it difficult to ascertain the broad applicability of the proposed method.
2. The paper does not provide a detailed analysis of the computational cost of WANDA compared to other pruning methods. While the authors mention that WANDA is computationally efficient, a quantitative comparison would be helpful. The paper should include a breakdown of the time complexity of each step in the WANDA algorithm, and compare it to the time complexity of other pruning methods, such as magnitude pruning or methods involving weight updates. This analysis should also consider the memory footprint of each method, as this can be a significant factor in the practical application of pruning techniques.

### Suggestions

To address the lack of generalizability, the authors should evaluate WANDA on a more diverse set of models and tasks. This should include models with different architectures, such as convolutional neural networks (CNNs) and recurrent neural networks (RNNs), as well as tasks beyond language modeling, such as image classification and object detection. For image classification, the authors could test WANDA on standard benchmarks like CIFAR-10 or ImageNet, using models like ResNet or VGG. For object detection, they could evaluate WANDA on datasets like COCO or Pascal VOC, using models like YOLO or Faster R-CNN. These experiments would provide a more comprehensive understanding of the method's strengths and weaknesses, and help to identify the types of models and tasks for which WANDA is most suitable. Furthermore, the authors should analyze the performance of WANDA under different sparsity levels and structured sparsity patterns, as this can significantly impact the practical applicability of the method.

To provide a more detailed analysis of the computational cost, the authors should include a quantitative comparison of the time complexity of WANDA with other pruning methods. This analysis should include a breakdown of the time complexity of each step in the WANDA algorithm, such as the computation of weight magnitudes and input activations, and compare it to the time complexity of other pruning methods, such as magnitude pruning or methods involving weight updates. The authors should also consider the memory footprint of each method, as this can be a significant factor in the practical application of pruning techniques. This analysis should be performed on different hardware platforms, such as GPUs and CPUs, to provide a more comprehensive understanding of the computational cost of WANDA. The authors should also discuss the potential for optimizing the implementation of WANDA to further reduce its computational cost.

Finally, the authors should provide a more detailed discussion of the limitations of WANDA and potential avenues for future research. This should include a discussion of the potential impact of the choice of activation function on the performance of WANDA, as well as the potential for combining WANDA with other pruning methods to achieve even better results. The authors should also discuss the potential for applying WANDA to other types of neural networks, such as graph neural networks or transformers, and the challenges associated with these applications. This discussion should provide a more balanced perspective on the method and help to guide future research in this area.

### Questions

1. How does WANDA compare to other pruning methods in terms of computational cost and memory usage?
2. Can WANDA be applied to other types of models or tasks, such as image classification or object detection?
3. What are the limitations of WANDA, and what are the potential avenues for future research?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

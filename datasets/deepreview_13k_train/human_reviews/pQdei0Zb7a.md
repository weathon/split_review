# BiSSL: Bilevel Optimization for Self-Supervised Pre-Training and Fine-Tuning

- Decision: Reject
- Scores: 5, 3, 6

## Abstract
In this work, we present BiSSL, a first-of-its-kind training framework that introduces bilevel optimization to enhance the alignment between the pretext pre-training and downstream fine-tuning stages in self-supervised learning. BiSSL formulates the pretext and downstream task objectives as the lower- and upper-level objectives in a bilevel optimization problem and serves as an intermediate training stage within the self-supervised learning pipeline. By more explicitly modeling the interdependence of these training stages, BiSSL facilitates enhanced information sharing between them, ultimately leading to a backbone parameter initialization that is better suited for the downstream task. We propose a training algorithm that alternates between optimizing the two objectives defined in BiSSL. Using a ResNet-18 backbone pre-trained with SimCLR on the STL10 dataset, we demonstrate that our proposed framework consistently achieves improved or competitive classification accuracies across various downstream image classification datasets compared to the conventional self-supervised learning pipeline. Qualitative analyses of the backbone features further suggest that BiSSL enhances the alignment of downstream features in the backbone prior to fine-tuning.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces BiSSL, a training framework that integrates bilevel optimization into the self-supervised learning pipeline to enhance the alignment between pretraining and downstream fine-tuning stages. BiSSL formulates the pretext and downstream task objectives as lower- and upper-level objectives within a bilevel optimization problem, facilitating improved information sharing between the stages and leading to better parameter initialization for downstream tasks. Results in image classification datasets show the effectiveness of the proposed method.

### Strengths
1. Introduces a new training framework that leverages bilevel optimization to bridge the gap between pretext pretraining and downstream tasks.

2. Demonstrates improved or comparable classification accuracies across multiple image classification datasets compared to traditional SSL methods. The author also  provide insights into how BiSSL affects the learned representations, showing enhanced downstream feature alignment before fine-tuning.

### Weaknesses
* **Limited Experimental Scope** : The evaluation of BiSSL is confined to classification tasks, and the models and datasets used are relatively small-scale. This restricts the demonstration of the framework's scalability and its ability to handle larger and more complex datasets, which is a critical aspect for real-world applications. Specifically, the use of datasets like VOC07 and DTD, while common, does not fully explore the method's potential on more challenging datasets with a larger number of classes or greater image complexity. Furthermore, the reliance on relatively small models like ResNet-18 limits the conclusions that can be drawn about the method's performance with deeper architectures, which are often necessary for more complex tasks.
* **Compromise on Generalizability** : The pretraining setup of BiSSL aims to align with specific downstream tasks, which might sacrifice the generalizability of the pretrained models. This alignment could potentially limit the framework's effectiveness for a diverse range of tasks that were not considered during the pretraining phase. By optimizing the pretraining for specific downstream tasks, the learned representations may become overly specialized, hindering their transferability to other tasks or datasets. This raises concerns about the broader applicability of the method beyond the specific tasks used in the evaluation.
* **Increased Training Complexity** : The introduction of bilevel optimization makes the training process more complex compared to the traditional pretraining and downstream fine-tuning paradigm. This added complexity could pose challenges in terms of computational resources and may require additional expertise to implement and optimize, potentially hindering its adoption in simpler or more streamlined workflows. The bilevel optimization process introduces nested optimization loops, which can significantly increase the computational cost and make the training process more sensitive to hyperparameter choices. This added complexity may make it harder to reproduce the results and apply the method in practice.

### Questions
see Weaknesses

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces BiSSL, a novel framework leveraging bilevel optimization to enhance self-supervised learning (SSL) by aligning the pre-training and fine-tuning phases. In the conventional SSL process, these stages are typically treated as separate, which can lead to misalignment issues between representations learned during pre-training and those required for downstream tasks. BiSSL addresses this by treating pretext pre-training as a lower-level optimization problem and downstream fine-tuning as an upper-level one, facilitating stronger information flow between stages. Empirical validation using a ResNet-18 architecture and the SimCLR approach, showing improved or competitive accuracy on multiple datasets compared to standard SSL techniques.

### Strengths
1. The paper is well-written and easy to follow.

2. The idea of using bilevel optimization for SSL is novel and interesting.

### Weaknesses
1. This study relies solely on SimCLR as a comparison method, lacking sufficient comparative experiments with approaches better suited for small-scale datasets, such as BYOL[1] and SwAV[2]. Additionally, it omits necessary explanations of more recent self-supervised methods like DINOv2 [3]. The choice of SimCLR as the sole baseline limits the scope of the evaluation, as methods like BYOL and SwAV are known to perform better in low-data regimes due to their architectural differences and training objectives. The absence of comparisons with these methods makes it difficult to assess the true effectiveness of the proposed BiSSL framework, particularly in scenarios where data is scarce. Furthermore, the lack of discussion regarding recent advancements like DINOv2, which leverages self-distillation techniques, leaves the reader wondering how BiSSL compares to state-of-the-art approaches.

2. There is a lack of comparative experiments on different network architectures, as well as the results of SSL's standard dataset ImageNet. In the absence of sufficient data, the performance of SSL is not obvious compared to SFL. The evaluation is limited to a single architecture (ResNet-18), which does not provide a comprehensive understanding of how BiSSL performs across different model capacities and complexities. The absence of experiments on larger architectures, such as ResNet-50 or Vision Transformers, makes it difficult to generalize the findings. Moreover, the lack of results on ImageNet, a standard benchmark for self-supervised learning, makes it challenging to assess the performance of BiSSL in comparison to other methods. Without these results, it is unclear whether the observed improvements are specific to the datasets used or if they generalize to larger, more complex datasets. The comparison to supervised fine-tuning (SFL) is also not sufficiently explored, leaving uncertainty about the relative benefits of the proposed method.

### Questions
For Fig. 2, did the author analyze why the proposed method converges quickly in the early stages of training? Is there over-fitting?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a framework called BiSSL, which is a bilevel optimization framework for self-supervised pre-training and fine-tuning. It enhances the alignment between pre-training and fine-tuning. It serves as an intermediate training stage in the self-supervised learning pipeline. It also enhances information sharing between the pretext and fine-tuning stage. As a result, the backbone initialization can be more suitable for downstream tasks. Experiment results prove the effectiveness of the proposed method.

### Strengths
1. This paper is overall well-written and easy to read, with a clear organization. The figures and algorithm illustrates the idea very clearly. 
2. The idea of introducing bilevel optimization into pre-training and fine-tuning pipeline is reasonable for me. 
3. The experiment design is good, covering both quantitative and qualitative results, together with some analysis.

### Weaknesses
1. As mentioned in strengths, the idea of this paper is reasonable, but not very new to me. The bilevel optimization is widely used in meta-learning. While the application to self-supervised learning (SSL) is interesting, the core idea of using bilevel optimization to align two training stages is not entirely novel. The paper should more clearly articulate the specific differences in how this is applied compared to existing meta-learning approaches, especially since the high-level concept is similar. The current discussion lacks a detailed comparison of the objective functions and optimization procedures used in meta-learning versus the proposed BiSSL framework. 
2. In the experiment section, the backbone (ResNet-18) seem to be relatively small. While this may be sufficient for initial proof-of-concept, it is not clear how well the method would scale to larger models, which are more commonly used in modern SSL. The paper should include experiments with larger backbones, such as ResNet-50 or even larger models, to demonstrate the practical applicability of the method in more realistic scenarios. The current experiments do not provide sufficient evidence that the method is robust and effective for larger architectures.

### Questions
1. I think if possible, the authors can have more discussions on the novelty of this paper. 
2. I am curious about the results of the proposed method in larger backbone (at least ResNet-50).
3. The authors can have more discussions on the limitation of the proposed method.

### Soundness
3

### Presentation
3

### Contribution
3

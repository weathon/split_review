# BAdd: Bias Mitigation through Bias Addition

- Decision: Reject
- Scores: 5, 6, 8, 5

## Abstract
Computer vision (CV) datasets often exhibit biases that are perpetuated by deep learning models. While recent efforts aim to mitigate these biases and foster fair representations, they fail in complex real-world scenarios. In particular, existing methods excel in controlled experiments involving benchmarks with single-attribute injected biases, but struggle with multi-attribute biases being present in well-established CV datasets. Here, we introduce BAdd, a simple yet effective method that allows for learning fair representations invariant to the attributes introducing bias by incorporating features representing these attributes into the backbone. BAdd is evaluated on seven benchmarks and exhibits competitive performance, surpassing state-of-the-art methods on both single- and multi-attribute benchmarks. Notably, BAdd achieves +27.5\% and +5.5\% absolute accuracy improvements on the challenging multi-attribute benchmarks, FB-Biased-MNIST and CelebA, respectively.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The document introduces BAdd, a method for mitigating bias in deep learning models by injecting bias-capturing features into the training process. This approach aims to create bias-neutral representations by incorporating features that encode bias-inducing attributes, thus preventing the model from relying on these biases during training. 


The core idea is to divide the training loss between bias-aligned and bias-conflicting samples and study their behavior. To mitigate the loss spike due to underfitting on bias-aligned samples, the authors introduce the attributes themselves as features in the final layer, which mitigates the loss spikes and leads to proper training.

### Strengths
- The paper is clear and well-written.

- The core idea seems interesting and is supported by various experiments.

### Weaknesses
The idea of Bias Injection to Mitigate Bias has been used in the following work [1].

Although the idea is that a bias injection module, can prevent the loss spike. However, when the loss is forced to be zero, it needs to overcorrect the bias injection module, does it lead to correct features?

For the bias-aligned examples, the network can probably take the shortcut. Hence, the learning needs to happen just which Bias Corrected samples. In case B_c >> B_a won’t it affect the learning of diverse features? It would be great if the authors could clarify this aspect more.

The introduction section mentions that the method is more suitable for real-world. However, on closely examining the method, I found that BAdd also requires knowing the bias attributes. Could the authors please clarify on this aspect?

### Questions
Please see the questions in the weakness section.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The model proposed in this paper learns unbiased features by adding specific elements that capture potential biases during training. This ensures that the model doesn’t rely on biased information when making predictions. BAdd was tested on various datasets, including those with single and multiple biases, and showed strong improvements in reducing bias and overall model performance.
So,  this paper:
1.Introduced BAdd, an easy and effective method for learning unbiased features by incorporating bias-detecting elements into training.
2.Evaluated BAdd on several benchmarks, including different types of biased datasets, showing that it outperforms other state-of-the-art methods.

### Strengths
1.BAdd reduces bias effectively by adding bias-related features into the training, helping the model avoid being influenced by biased data.
2.The authors showed that BAdd works well on different datasets, with consistent improvements in various bias situations, proving that the method is scalable and works in different applications.

### Weaknesses
1.BAdd requires a classifier or labels that identify the bias, which may not always be available. The authors could consider ways to detect and handle biases automatically without needing predefined labels. Specifically, the reliance on a pre-existing bias classifier introduces a dependency that limits the method's applicability in scenarios where such classifiers are not readily available or accurate. The performance of BAdd is therefore intrinsically tied to the quality of this bias classifier, and any inaccuracies or biases present in the classifier will likely propagate to the debiased model.
2.The method mainly addresses visual biases, and it’s unclear if it works for other types of biases, like those in text, limiting its use beyond visual data. The paper does not provide sufficient evidence or theoretical justification for extending BAdd to other data modalities. For instance, the feature extraction process for text data differs significantly from that of images, and it is not clear how the bias-detecting elements would be adapted to capture biases in textual representations. Furthermore, the concept of 'visual bias' is often tied to spatial relationships and textures, which may not have direct counterparts in other modalities.
3.The paper is clear, but lacks a detailed comparison to standard deep learning training. It’s not explained how the bias-detecting classifier fits into the training process. The paper does not explicitly detail how the gradients from the bias classifier are incorporated into the main model's training. This lack of clarity makes it difficult to understand how BAdd's components interact and how the bias-related features are used to influence the main model's learning. A more detailed description of the training procedure, including the loss functions and optimization strategies, is needed to fully evaluate the method's effectiveness.
4.In line 728, the tense is inconsistent—“were” should be changed to “are.”

### Questions
please check the weakness part, and give some explanations.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces a BAdd approach to mitigate the effects of biased data during model training. The idea is to incorporate captured bias features into the final layer of the model, which helps the model be invariant for these features and create a bias-neutral feature representation.

### Strengths
1-	The problem is described clearly.

2-	The investigated problem is important.

### Weaknesses
1-	The BAdd approach seems similar to FLAC [1]. 

2-	On page 3, The author claims that BAdd is easily applied to any network architecture and to any CV dataset. This claim needs to be proven.

3-	The paper does not discuss the computational complexity or scalability of the proposed approach in detail, which could be a concern for large-scale applications.

4-	Limited Ablation Studies: While the paper includes some ablation studies, more extensive ablations could strengthen the claims about the individual contributions of each component of the proposed method.

### Questions
1-Describe the key differences between the BAdd and  FLAC [1].

2-Conduct experiments using different architectures, such as ViT with BAdd, to prove that the approach works properly with different architectures. Also, use the ImageNet dataset to show the approach performance with the balanced dataset.

3-Discuss the computational complexity of BAdd approach.

4-We encourage the author to do more ablation studies on the proposed approach to show consistency, such as changing the batch size.

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
The paper introduces BAdd (Bias Addition), a method for mitigating bias in deep learning models for computer vision tasks. Bias in datasets often arises from spurious correlations between certain attributes (e.g., gender, race, background) and target variables, leading models to make decisions based on these irrelevant features. Existing bias mitigation methods often struggle in complex, real-world scenarios, especially when multiple biases are present.

BAdd addresses this issue by injecting bias-capturing features into the model's training process. Specifically, it involves adding features that encode the protected (bias-inducing) attributes into the penultimate layer of the model during training. This approach aims to decouple the learning of biased features from the optimization process, allowing the model to learn bias-neutral representations of the data.

The method is evaluated on seven benchmarks, including both artificially biased datasets (e.g., Biased-MNIST, Corrupted-CIFAR10) and more complex, multi-attribute biased datasets (e.g., FB-Biased-MNIST, CelebA, UrbanCars). Notably, it achieves accuracy improvements of +27.5% on FB-Biased-MNIST and +5.5% on CelebA.

### Strengths
Versatility: The approach is architecture-agnostic and can be easily integrated into any deep learning model without extensive modifications or pre-processing.
Visualization of Results: Use of activation maps and GradCam visualizations helps to intuitively demonstrate how BAdd shifts the model's focus away from bias-inducing features.

### Weaknesses
Assumption of Bias Representability: The method assumes that biases can be captured and represented explicitly. This assumption may not hold in complex real-world scenarios where biases are subtle, multifaceted, or unknown, potentially limiting the method's applicability. For example, biases related to nuanced social contexts or implicit biases embedded within the data generation process might not be easily encoded into explicit features.

Potential Increase in Model Complexity: Adding bias-capturing features, even if only during training, introduces additional parameters and computations. This could lead to increased memory usage and longer training times, especially for large-scale models or datasets. The paper does not provide a thorough analysis of the computational overhead associated with the BAdd method, which is crucial for practical deployment.

Fine-Tuning Requirement: The necessity of a fine-tuning step adds an extra phase to the training process, which might not be ideal in time-constrained or resource-limited applications. This fine-tuning step, while potentially beneficial for performance, also introduces an additional hyperparameter to tune, which can complicate the training process and increase the overall time required to achieve optimal results. The paper should provide more guidance on how to effectively tune this fine-tuning phase.

Limited Analysis on Real-World Biases: While the paper includes evaluations on datasets like CelebA, further analysis on real-world datasets with complex, less-defined biases would strengthen the applicability of BAdd. The current evaluations do not fully capture the challenges associated with mitigating biases in real-world applications where biases are often intertwined with other factors and are not easily isolated or labeled.

### Questions
Availability of Protected Attributes: How does BAdd perform when protected attribute labels are unavailable or unreliable?

Handling Unknown Biases: In real-world applications where biases may be unknown or multifaceted, how can BAdd be adapted to mitigate biases that are not explicitly identified?

### Soundness
2

### Presentation
2

### Contribution
2

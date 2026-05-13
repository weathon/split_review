# Towards Practical Large-Scale Privacy-Preserving Recurrent Neural Networks

- Decision: Reject
- Scores: 3, 6, 3, 3

## Abstract
Recurrent neural networks (RNNs) are used for a variety of applications such as speech recognition and financial forecasting where data privacy is an ongoing concern.  Fully homomorphic encryption (FHE) facilitates computation over encrypted data, enabling third-party services like machine learning inference while keeping client data private. Previous studies have examined RNN inference over encrypted data using FHE, albeit on a small scale, though impractical due to the computational costs. This work advances insights that make large-scale RNN evaluation over encrypted data practical. A problem that prohibits the scaling of privacy-preserving RNNs is overflow in the ciphertext message space. As the number of model parameters increases, the size of the domain during multiply-accumulate operations increases, causing inaccuracies in computation. Attempts to mitigate this problem, such as splitting the message into several ciphertexts, cause an exponential increase in computation, making latency-sensitive applications like RNNs impractical. A novel regularization technique is proposed that mitigates the effects of numerical overflow during training. This allows use of one ciphertext only and reduces the complexity of the encryption parameters that would otherwise be required to perform correct computation while maintaining 128-bit security. Using the CGGI variant of FHE and GPU acceleration, we quantize and evaluate a 1.9M parameter, multi-layer RNN across 28 timesteps, achieving 90.82% top-1 accuracy over the encrypted MNIST test dataset with an average latency of 2.1s per sample---a new state of the art in latency, model performance, and scale.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces overflow-aware activity regularization (OAR), a regularization technique to mitigate numerical overflow during private RNN inference. The proposed method also allows for more efficient encryption parameters. This work enables large-scale private RNN inference. Experiments show that evaluating an RNN of 1.9M on one encrypted data sample from the MNIST dataset takes only 2.1 seconds.

### Strengths
1. The paper is well organized and easy to read. The key problem is explained clearly, i.e., the pre-activations can overflow in the message space.
2. The proposed OAR can effectively mitigate numerical overflow when the bit-width varies from 5 to 8.
3. The authors provided the code as well as details about their implementation.

### Weaknesses
1. The proposed OAR is not complete. The proposed OAR is largely built upon the anonymous reference in the supplementary materials. Specifically, the authors propose to add the OAR to the 4-step quantization procedure in the anonymous reference. Yet, without the OAR, the anonymous reference is said to have an accuracy drop of 25% (line 190). Thus, the practicality of the anonymous reference is questionable as well. The proposed OAR and the anonymous reference might be combined to offer better technical completeness.
2. The motivation is questionable. As shown in Table 1, when the RNN is quantized to 7-bit, the accuracy is 95.15%, despite the OAR metric being low. However, with the proposed OAR, the accuracy is even 1.18% lower while the OAR metric is higher. This indicates that enlarging the percentage of pre-activations positioned in the correct regions does not necessarily contribute to better performance, as neural networks are error-tolerant.
3. The novelty of the paper is limited. While the observation the authors put forward is sharp, the main contribution of the paper is the new regularization term introduced in Section 3.1, which optimizes the percentage of pre-activations values in the correct regions.
4. There is a lack of comprehensive evaluation. While the authors present some ablation studies of the proposed OAR, the overall evaluation is not comprehensive. There is a lack of end-to-end comparison with existing methods, such as SHE (Neurips'19) and ones based on the CKKS scheme.

### Questions
1. In Table 1, how does the latency change across different bit-widths?
2. Is the input binarized by the client before encryption (line 202)? If so, the description of the client (line 54) is not precise, as pre-encryption quantization of the input is not always needed, especially when the CKKS scheme is used.

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
The paper presents a novel approach to enhancing the performance of recurrent neural networks (RNNs) on the MNIST dataset using Overflow-Aware Activity Regularization (OAR) to address overflow issues during quantization-aware training, particularly in low-bit-width settings. By employing fully homomorphic encryption (FHE) and GPU acceleration, the authors achieve over 90% accuracy with a latency of 2.1 seconds per sample, demonstrating significant improvements in both efficiency and model performance. The study highlights the effectiveness of OAR in maintaining accuracy during encrypted evaluations and suggests its potential for optimizing larger RNNs and future applications in privacy-preserving machine learning.

### Strengths
This work propose the method-Overflow-Aware Activity Regularization (OAR) offers several advantages over traditional L2 regularization in the context of RNNs, particularly when dealing with fully homomorphic encryption (FHE) for RNN inference:

1. **Mitigation of Numeric Overflow**: OAR specifically addresses the issue of numeric overflow that arises during computations with encrypted data. Traditional L2 regularization does not account for this overflow, which can lead to inaccuracies in the model's predictions. OAR helps maintain the integrity of the computations by managing the range of activations more effectively.

2. **Restoration of Accuracy**: While traditional L2 regularization may help prevent overfitting, it does not restore accuracy lost due to overflow effects. OAR has been shown to effectively recover lost accuracy in RNNs operating under FHE, demonstrating its efficacy in maintaining model performance even in challenging conditions.

3. **Efficiency in Encrypted Inference**: OAR allows for the use of a single ciphertext representation for inputs and activations, which reduces inference latency. This is particularly beneficial for RNNs, where low latency is crucial. Traditional L2 regularization does not provide this efficiency advantage in the context of encrypted data.

4. **Scalability**: OAR enables the scaling of RNNs to larger models without the exponential increase in computation that can occur with traditional methods that do not consider overflow. This scalability is essential for practical applications of RNNs in privacy-preserving settings.

In summary, OAR not only addresses the specific challenges posed by FHE but also enhances the overall performance and efficiency of RNNs compared to traditional L2 regularization.

### Weaknesses
As model compression is also proved to be effective in FHE inference. Model Compression: Implementing model compression techniques, such as pruning or knowledge distillation, could reduce the size of the RNN model, making it more efficient to evaluate under FHE. Smaller models require fewer resources for encryption and decryption, which can lead to faster inference times.

How does the proposed method to be incorporated with model compression here?

### Questions
See Weakness

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper basically introduces overflow-aware activity regularization (OAR), a RNN regularization technique tailored for a usage within FHE setting. A parallel submission from the authors already proposed an efficient RNN quantization strategy, but with a decreased model performance as it might overflow the modulus of the message space. The authors experimented by showing a 1.9M parameter, multi-layered RNN architecture leading to 90.82% top-1 accuracy on MNIST, with an average latency of 2.1 s using FHE.

### Strengths
This work improves over another work submitted in parallel by the authors to another conference ICASSP 2025.

### Weaknesses
- I find it problematic that this submission extensively leverages some quantization techniques of another paper from the authors (Anonymous, 2025), submitted to another conference ICASSP 2025. Even though the paper's pdf is shared as an accompanying file, this does not belong to this submission. Yet, the quality and soundness of this paper can't be guaranteed, as the acceptance/rejection wasn't decided yet.  Also, this work proposes an improvement over the ICASSP 2025 paper, so why not simply update your results in that paper ? 

- You compared with SHE, claiming a much better efficiency ("latency reduction of 274x"), but you are comparing your network on MNIST, with their network on Penn Treebank. This is strange. Besides, if MNIST is the target, using a DNN SHE can reach 99.5% accuracy with a very small latency, largely outperforming your architecture. Actually, reaching 90.82% accuracy on MNIST is not impressive. 

 - You use two NVIDIA A100 GPUs, while SHE [Lou & Jiang, 2019] used 10 CPU cores. How do you can you compare the latency and claim "latency reduction of 274x", when you seem to use very different computing capabilities ?

### Questions
- Why conducting experiments on an image dataset like MNIST, and not on a task more suited for RNN, like some time series ?

- you mention the Penn Treebank dataset used as one experiment in SHE, why not comparing on the same dataset ?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper focuses on privacy-preserving RNN training using Fully Homomorphic Encryption (FHE). The authors build on their earlier work, adopting a four-step quantization procedure that ternarizes RNN parameters and binarizes activations to reduce computational costs. However, this quantization method comes with a trade-off: a reduction in model performance. The authors attribute this performance drop to overflow in the modulus of the message space during computation. To address this, they propose an overflow-aware activity regularization method, which aims to push pre-activation values into the correct overflow regions. The regularization works by penalizing pre-activation values that fall into incorrect regions, thereby forcing them into the appropriate range. The authors evaluate their method on the MNIST dataset and report minimal accuracy loss with the regularization applied.

### Strengths
- The Overflow-Aware Activity Regularization method that this paper proposes is novel.
- This paper achieves in much faster training speed than prior work.

### Weaknesses
- This paper builds upon prior, unpublished work by the same authors, which is provided as supplementary material. In the previous work, the authors propose a four-step quantization method that ternarizes model weights and binarizes activations to reduce computational costs and accelerate training. However, this prior work has not been peer-reviewed or rigorously examined. It only evaluates the quantization method on the VoxCeleb1 dataset (in plaintext), where the results indicate a significant drop in performance: top-1 and top-5 accuracy are reduced by 25% and 14%, respectively. Even in this paper’s evaluation on the MNIST dataset, the quantization method still shows a noticeable accuracy drop compared to full-precision training (from 99% to 90%). These concerns about the effectiveness of the prior approach cast doubt on the stability and reliability of the new method, which is built directly upon it.
- A key result claimed by this work is the improvement in training speed, purportedly achieving state-of-the-art performance. However, the speed gains primarily result from the quantization method introduced in the previous paper, not from the new contributions in this work. This paper's main innovation is the application of a regularization technique to stabilize training, but the method appears tightly coupled to the specific four-step quantization approach from the prior work. The authors provide no experimental evidence to suggest that the regularization method generalizes beyond this specific setup, which limits the broader applicability and impact of the paper.
- Additionally, the paper lacks sufficient experimental results to demonstrate the robustness of the proposed regularization technique. While the focus of the work is on private RNN training, the authors evaluate their approach solely on the MNIST dataset—a dataset designed for vision tasks. This raises concerns about the generalizability of the method to language-focused datasets, which are more relevant for RNN applications. Although the prior work was evaluated on the VoxCeleb1 dataset, this paper does not include any results on that dataset, further weakening the evidence for the method's effectiveness.

### Questions
I suggest the authors to either combine the two papers into a single one, or show that the regularization approaches generalize to a more general setting beyond the original paper, and provide thorough experimental evidence to support the claims.

### Soundness
1

### Presentation
2

### Contribution
2

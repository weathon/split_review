# Growing Efficient Accurate and Robust Neural Networks on the Edge

- Decision: Reject
- Scores: 8, 5, 6, 5, 5

## Abstract
The ubiquitous deployment of deep learning systems on resource-constrained Edge devices is hindered by their high computational complexity coupled with their fragility to out-of-distribution (OOD) data, especially to naturally occurring common corruptions. Current solutions rely on the Cloud to train and compress models before deploying to the Edge. This incurs high energy and latency costs in transmitting locally acquired field data to the Cloud while also raising privacy concerns. We propose GEARnn (Growing Efficient, Accurate, and Robust neural networks) to grow and train robust networks in-situ, i.e., completely on the Edge device. Starting with a low-complexity initial backbone network, GEARnn employs One-Shot Growth (OSG) to grow a network satisfying the memory constraints of the Edge device using clean data, and robustifies the network using Efficient Robust Augmentation (ERA) to obtain the final network. We demonstrate results on a NVIDIA Jetson Xavier NX, and analyze the trade-offs between accuracy, robustness, model size, energy consumption, and training time. Our results demonstrate the construction of efficient, accurate, and robust networks entirely on an Edge device.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes GEARnn (Growing Efficient, Accurate, and Robust neural networks) to grow and train robust networks completely on resource-constrained Edge devices. The two questions raised by the paper are critical, whose solutions eventually achieve the overall objective. The paper is well organized and written. The idea is novel and experimental verification seems convincing.

### Strengths
1. It is critical to produce and optimize an accurate neural network on resource-constrained edge devices, the paper provides a good solution that addressing the challenge of deploying efficient, accurate, and robust deep learning models on the Edge.
2. The two-phase growth approach can provide efficiency and robustness.
3. The proposed method is verified on real devices NVIDIA Jetson Xavier NX
4. The proposed approach addresses the key challenges of high computational complexity and fragility to out-of-distribution (OOD) data.

### Weaknesses
1. I am expecting more real edge devices to demonstrate the feasibility and also the performance difference. 
2. Is it possible to include other datasets such as multimodal cases.
3. Is it possible to show some analysis regarding on the performance of the neural training method?

### Questions
Please refer to the weakness part

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a method for training robust neural networks directly on edge devices. It designs a one-shot growth (OSG) approach to efficiently grow networks using clean data, and an efficient robust augmentation (ERA) method to enhance robustness. The authors demonstrate that the solution achieves competitive accuracy and robustness while reducing training time and energy consumption on edge devices compared to traditional approaches.

### Strengths
- The paper addresses a real-world problem of training robust networks on resource-constrained edge devices

- The paper also provides comprehensive empirical evaluation results.

### Weaknesses
 - More theoretical analysis is expected. For example, the rationale provided in Section 8 (referenced but not shown in the excerpt) appears mostly empirical. What is the fundamental challenge and uniqueness of the technical contribution? Specifically, a deeper dive into why the proposed one-shot growth (OSG) and efficient robust augmentation (ERA) methods are superior to existing techniques is needed. The paper should articulate the theoretical underpinnings of why these specific growth and augmentation strategies lead to robust networks, rather than relying solely on empirical results. 

- More implementation details can be used. For example, for the ERA method, more specifics about transform operations and hyperparameter choices can help the readers. It would be beneficial to know the exact range of augmentations applied, the probability of each transformation, and how these were selected. The lack of detail makes it difficult to reproduce the results and assess the method's sensitivity to these parameters.

- More analysis analysis for some designs can help. For example, the hyperparameter growth ratio γ: more details will improve the assessment of the algorithm's stability. It is unclear how sensitive the method is to different values of γ, and what the trade-offs are between faster growth and network performance. A detailed analysis of this parameter's effect on the final network architecture and performance is needed.

- Is it possible to assess its applicability to architectures like ViT, given ViT's distinct characteristics like self-attention mechanisms and multi-head structure, what are the implications?

### Questions
Besides the above comments, there are also some minors:

- Have you explored combining the solution with other efficiency techniques like quantization? This could potentially further improve the results for edge deployment.

- What modifications would be needed for growing self-attention layers and handling multi-head structures?

### Soundness
3

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
The paper studies on-device learning, proposing training solutions that are robust to common corruptions of data while requiring low resource footprint. It uses growth techniques that gradually increase the network sizes to reach to a robust accuracy, and applies robust data augmentation techniques to improve robustness against common corruptions. The paper provides interesting insights, but it lacks the necessary novelty, as it is heavily based on the previously proposed techniques.

### Strengths
The paper is very well written. The problem is interesting. The performance analysis shows the benefit of applying GEAR and provides interesting insights on how grow techniques work.

### Weaknesses
The paper lacks novelty, as the proposed solution combines existing techniques. The core idea of gradually growing networks and applying robust data augmentation is not new, and the paper does not introduce significant modifications to these methods. The evaluation is limited to CNN models, specifically VGG-19, MobileNet-V1, and ResNet-18, and it is unclear how the proposed approach would extend to more recent architectures, such as transformers, which are increasingly relevant for on-device applications. The paper does not address the challenges of training transformers on resource-constrained devices, which is a significant limitation given the current trends in deep learning.

Isolated on-device training, as presented in the paper, seems impractical due to the limited data available on individual edge devices. The paper assumes a scenario where each device has enough data to train a model effectively, which is unlikely for many real-world applications, especially those involving resource-constrained edge devices. The paper does not provide a clear definition of 'small' network complexity, and it is not explicitly linked to the memory and computational constraints of the target devices. The constraint should be defined by the limitations at the device (e.g. by memory and computation constraints at the device).

### Questions
Please check above.

### Soundness
2

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
3

### Summary
In order to address the problem of growing robust networks efficiently on Edge devices, this paper proposes GEARnn (Growing Efficient, Accurate, and Robust neural networks) to grow and train robust networks in-situ. It was said to be the first work to grow networks robust to common corruptions. Experimental results on a NVIDIA Jetson Xavier NX demonstrate the construction of efficient, accurate, and robust networks entirely on an Edge device.

### Strengths
1. It was said to be the first work to grow networks robust to common corruptions. 

2.The proposed GEARnn method is measured on NVIDIA Jetson Xavier NX, Edge device NVIDIA.

3. The experiments show some promising results of the proposed GEARnn architecture.

### Weaknesses
1. The organization of this paper can be greatly enhanced. There are many times double-columns and single-columns mixed together.

2. The authors make six bullets of contributions, however, some of them are trivial contributions and can be merged together, as Q1 and Q2, which are part of GEARnn.

3. The proposed solution GEARnn is based on a family of growth algorithms, which limits the novelty in algorithm design. 

4. The objective of this paper lies in the improvements in robust accuracy, training time, and model size. However, these metrics can not be achieved simultaneously. 

5. The trade-offs between accuracy, robustness, model size, energy consumption, and training time are not well discussed both theoretically and experimentally.

6. Insufficient Comparative Analysis: The comparative analysis lacks depth. The authors only propose their own baselines Small (Din)
and Small (Daug). The authors need to expand the comparison to include state-of-the-art methods beyond the baselines mentioned, to position the paper's contributions within the current research landscape.

7. The complexity of the proposed solutions, GEARnn-1 and GEARnn-2 may be too high for practical deployment in resource-constrained environments. The paper does not provide sufficient detail on the computational overhead and latency introduced by the frequent updates and training cycles of GEARnn-1 and GEARnn-2 models, which may hinder real-time performance.

8. A theoretical convergence analysis for this result is currently lacking. It is unconvincing to present a large number of carefully designed experiments, but a rigorous convergence proof to test whether the GEARnn algorithms can yield a good convergent performance.

9. The full name should be put in front of the abbreviation, e.g., GEARnn (Growing Efficient, Accurate, and Robust neural
networks) should be Growing Efficient, Accurate, and Robust neural networks  (GEARnn).

### Questions
1. How can you achieve the efficient, accurate, and robust networks simulatenesouly on an Edge device?

2. How is theoretical convergence for  the GEARnn algorithms?

3. How about the implementation code? Can you share it on public repo?

4. What are the main strengths and weaknesses of your approach compared to existing state-of-the-art approaches.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes GEARnn, a robust and efficient neural network growth method based on One-Shot Growth (OSG). Given a small backbone model, GEARnn constructs a large grown model via a single growth step, which is more computationally efficient than traditional multi-shots growth methods. Besides, this paper also introduces efficient robust augmentation (ERA) to obtain an augmented dataset. Training the grown model on the augmented dataset can increase the model’s robust accuracy on corrupted and out-of-distribution datasets.

### Strengths
1. This paper is well-structured and written.
2. This paper is well-motivated. In practice, addressing the problem of corrupted training data and high computation complexity is quite meaningful for edge devices.
3. The experiment results demonstrate the effectiveness of training the grown model with augmented data in terms of robust accuracy.

### Weaknesses
1. The ideas of OSG and ERA in this paper are non-innovative. Firstly, ERA advocates for adding a clean data residual onto augmented data. This idea is not original and has already been explored. For instance, in super-resolution, [1] proposes to add clean samples (high-resolution images) to corrupted samples (low-resolution images) to improve the accuracy of super-resolution models. Secondly, OSG simply applies Firefly [2] as the growing method and does not present any new model-growing technique. In this case, the only difference between OSG and existing works is that OSG straightforwardly obtains a fully-grown model with fewer growing steps, which is too simple and lacks novelty.
2. As OSG derives a fully-grown model from a backbone model in one single growth step, one potential problem is that it might generate a model that is overly complex. For example, a device with simple data distribution might only need an intermediate-level model to process its data. In this case, training a fully-grown overparametrized model with larger training complexity and memory consumption, might become unnecessary. 
3.  The authors' statement that GEARnn is robust across different augmentation methods is doubtful. In the experiment, the authors only test GEARnn with two augmentation methods (AugMix and Prime), which is insufficient. To support this claim, at least two more augmentation methods, such as Gaussian noise perturbation [3] and DeepAugment [4], should be included in the ablation study.
4. Some presentations in this paper are ambiguous and should be more clear. For example, with respect to the growth technique $\mathcal{G}$, the authors should at least introduce how Firefly works briefly, rather than simply say they follow Firefly (Section 4.1). Similarly, the authors should briefly introduce how AugMix works in Section 7.1.  Besides, it is unclear how to evaluate the loss $\mathcal{L}$ in equation (1). Since a model $f$ is obtained by expanding the backbone model $f_{0}$, before expansion, how can you calculate $\mathcal{L}(f)$ without actually having $f$?

### Questions
1. As for the experiment baselines, "In the absence of prior work on robust growth" (line 270) is not an appropriate reason for excluding SOTA methods from comparison. To be more convincing, the authors are supposed to compare the robust accuracy between GEARnn and the SOTA methods (e.g. [5-7]) to show the robustness of GEARnn empirically. 
2. The authors divide GEARnn into GEARnn-1 and GEARnn-2, with one and two growing phases respectively. However, the authors emphasize the superiority of the 2-phase approach (i.e. GEARnn-2) in the experiment and discussion. In this case, what's the meaning of proposing GEARnn-1 if it is completely outperformed by GEARnn-2? It would be better if you eliminate the concept of "GEARnn-1" and simply use "GEARnn" to represent GEARnn-2. If you consider GEARnn-1 and GEARnn-2 as two separate contributions, you need to analyze the advantages of GEARnn-1 over GEARnn-2.


[1] Kim, Jiwon, Jung Kwon Lee, and Kyoung Mu Lee. "Accurate image super-resolution using very deep convolutional networks." Proceedings of the IEEE conference on computer vision and pattern recognition. 2016.

[2] Lemeng Wu, Bo Liu, Peter Stone, and Qiang Liu. Firefly neural architecture descent: a general approach for growing neural networks. Advances in neural information processing systems, 2020.

[3] Dong Yin, Raphael Gontijo Lopes, Jon Shlens, Ekin Dogus Cubuk, and Justin Gilmer. A fourier perspective on model robustness in computer vision. Advances in Neural Information Processing Systems, 2019.

[4] Dan Hendrycks, Steven Basart, Norman Mu, Saurav Kadavath, Frank Wang, Evan Dorundo, Rahul Desai, Tyler Zhu, Samyak Parajuli, Mike Guo, et al. The many faces of robustness: A critical analysis of out-of-distribution generalization. In Proceedings of the IEEE/CVF International Conference on Computer Vision, 2021.

[5] Xin Yuan, Pedro Henrique Pamplona Savarese, and Michael Maire. Accelerated training via incrementally growing neural networks using variance transfer and learning rate adaptation. In Thirty-seventh Conference on Neural Information Processing Systems, 2023. 

[6] Utku Evci, Bart van Merrienboer, Thomas Unterthiner, Max Vladymyrov, and Fabian Pedregosa. Gradmax: Growing neural networks using gradient information. arXiv preprint arXiv:2201.05125, 2022.

[7] Ding, N., Tang, Y., Han, K., Xu, C., & Wang, Y. Network expansion for practical training acceleration. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2023.

### Soundness
1

### Presentation
2

### Contribution
2

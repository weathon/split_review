# xMLP: Revolutionizing Private Inference with Exclusive Square Activation

- Decision: Reject
- Scores: 5, 3, 3, 5

## Abstract
Private Inference (PI) enables deep neural networks (DNNs) to work on private data without leaking sensitive information by exploiting cryptographic primitives such as multi-party computation (MPC) and homomorphic encryption (HE).
However, the use of non-linear activations such as ReLU in DNNs can lead to impractically high PI latency in existing PI systems, as ReLU requires the use of costly MPC computations, such as Garbled Circuits.
Since square activations can be processed by Beaver's triples hundreds of times faster compared to ReLU, they are more friendly to PI tasks, but using them leads to a notable drop in model accuracy.
This paper starts by exploring the reason for such an accuracy drop after using square activations, and concludes that this is due to an ``information compounding’’ effect. Leveraging this insight, we propose xMLP, a novel DNN architecture that uses square activations exclusively while maintaining parity in both accuracy and efficiency with ReLU-based DNNs. 
Our experiments on CIFAR-100 and ImageNet show that xMLP models consistently achieve better performance than ResNet models with fewer activation layers and parameters while maintaining consistent performance with its ReLU-based variants.
Remarkably, when compared to state-of-the-art PI Models, xMLP demonstrates superior performance, achieving a 0.58\% increase in accuracy with 7$\times$ faster PI speed. Moreover, it delivers a significant accuracy improvement of 4.96\% while maintaining the same PI latency.
When offloading PI to the GPU, xMLP is up to 700$\times$ faster than the previous state-of-the-art PI model with comparable accuracy.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors proposed an MPC-based private inference scheme by replacing ReLU with a square function. 
They argued that the proposed architecture allows us to replace the ReLU activation entirely with square activation "without accuracy loss."

### Strengths
In order to show that performance can be sufficiently improved by replacing it with a square function, various ablation studies were conducted on several models.

### Weaknesses
This paper does not contain novel results. There are already numerous research results to replace ReLU in CNN with a square function. For example, AESPA, unpublished work after DELPHI, showed that high performance can be achieved in CNN only by using the square function and some other techniques. (https://arxiv.org/pdf/2201.06699.pdf)

However, in this paper, Table 4 reports that the performance of the square function is very poor in CNNs, e.g., ResNets. This is due to the lack of sufficient surveys.

The results of this paper have very marginal novelty, such that they show that good results can be obtained with a square function in MLPmixer-type models. Also, they do not provide any information on the coefficient of used square functions.

### Questions
How much computation is used in the offline phase for BT to be applied? In what simulation environments and how much time does it take?
The auxiliary random triples required for computation must be distributed in advance, but how much data should be distributed in advance?

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces a novel approach to enhance the efficiency of private inference (PI) by replacing ReLUs with the $x^2$. The authors employ a backbone network architecture inspired by the MLP-mixer, asserting its superior compatibility with $x^2$ compared to traditional CNNs like ResNets. Furthermore, the authors also discuss the architectural choices in terms of different combinations of ReLUs and  $x^2$, and normalization layers (BN vs LN) for optimizing the overall performance.

### Strengths
1. The paper introduces a novel approach by leveraging the MLP-mixer as the core network, eliminating the need for LayerNormalization for $x^2$ functioning. This is advantageous, especially for private inference where LayerNorm poses challenges.

2. Atuhros has presented a sound argument as to why substituting ReLUs with $x^2$ can be conducive to MLP-mixer-like architecture (compared to CNNs). 

3. The ablation study presented in Table 5 provides valuable insights into the influence of various normalizations and the interplay between ReLU and $x^2$ on private inference performance.


4. The paper includes a comprehensive comparison of ReLU and $x^2$ on the ImageNet dataset, offering a thorough evaluation of their respective capabilities and performance characteristics.

### Weaknesses
$ullet$ **Comparison with SOTA in PI:** One of the core issues with this paper is the lack of comparison with existing SOTA in PI, SENets [2]. Hence, the claim of the authors for pushing the SOTA in PI is not valid.


$ullet$ **FLOPs comparison are not included when comparing CNN-based PI:** Another major concern with this paper is excluding the FLOPs count when comparing with CNN-based PI, in Table 2. The authors have included the params counts, which are inconclusive as the parameter counts do not signify anything in the context of PI overheads. 

Since this paper, which used MLP-mixer as a backbone network, compares with the prior PI methods, which used CNN as backbone architecture, comparing only the non-linearity overheads does not tell the entire story (when comparing two distinct architecture). Moreover, the FLOPs cost cannot be ignored in PI, as they carry significant latency overhead for end-to-end latency [1]. The assumption of processing all the FLOPs offline is valid only when optimization is performed for a single inference request in isolation. However, in real-world scenarios, private inference requests arrive at non-zero rates, and processing the entire FLOPs offline becomes impractical due to limited resources. Consequently, offline costs are no longer truly offline, and FLOPs start affecting real-time performance, as illustrated in Figure 7 of the paper [1]. This effect can be exacerbated by networks with higher FLOP counts, as proposed by the authors.


$ullet$ **Ambiguity in timing analysis:** The micro-benchmarking for timing analysis performed in Section 4.3.2 is full of ambiguity.  First, the paper said that it used a 2pc protocol, and then it included CrypTen for benchmarking. Note that Delphi and CryptFlow2 have 2pc implementation; however, CryptTen has 3pc implementation as they used TTP for generating beaver triples in the offline phase. It seems that authors have mixed 2pc and 3pc implementation for their benchmarking. 

$ullet$ **Lack of any new insight:** The discussion presented in Section 3.1 for the sparsity-inducing property of ReLU, redundancy in global features,  and "information compounding" is not novel. See [9]. 

$ullet$ **Authors are ill-informed about the relevant literature:**  Authors need to tone down the claim for substituting all the ReLUs with polynomials for the first time. Prior work [6, 7, 8] replaced all the ReLUs with polynomials, and some of them demonstrated their efficacy on the ImageNet dataset too. Nonetheless, the prior work required to have higher-degree polynomials [6] or needed to use LayerNorm to mitigate the accuracy drop stemming from substituting all the ReLUs with polynomials [7]. 

Also, on page 9, the authors claim that implementation for offloading private computation to GPUs is not available. See the relevant work in [3,4,5]. 


[1] Garimella et al., "Characterizing and Optimizing End-to-End Systems for Private Inference," ASPLOS 2023. 

[2] Kundu et al., "Learning to Linearize Deep Neural Networks for Secure and Efficient Private Inference," ICLR 2023. 

[3] Jawalkar et al., "Orca: FSS-based Secure Training and Inference with GPUs," IEEE SP 2024

[4] Watson et al., "Piranha: A GPU Platform for Secure Computation," USENIX Security 2022 

[5] Tan et al., "CRYPTGPU: Fast Privacy-Preserving Machine Learning on the GPU," IEEE SP 2021. 

[6] Lee et al., "Precise approximation of convolutional neural networks for homomorphically encrypted data," IEEE Access 2023

[7]  Chrysos et al., "Regularization of polynomial networks for image recognition," CVPR 2023

[8] Xu et al., "Quadralib: A performant quadratic neural network library for architecture optimization and design exploration," MLSys 2022

[9] Zhao et al., "Rethinking ReLU to train better CNNs. " ICPR 2018


**In summary, although the approach is novel and interesting, the paper is presently in an early developmental stage and requires significant revisions.**

### Questions
1. Did the authors employ any knowledge distillation techniques or fine-tuning for their networks (especially in Fig. 1)?

2. Why is CrypTen used for timing analysis (in conjunction with Delphi and CrypTFlow2)?


3. How do you evaluate the runtime for depth-wise convolution?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes xMLP, a novel neural network architecture that uses only quadratic activations to enable fast and accurate private inference. xMLP utilizes an MLP-style architecture with global connectivity rather than convolutional layers, avoiding ReLU's sparsity-inducing effects on CNNs. xMLP combines patch and channel mixing layers with residual connections and quadratic activations.

### Strengths
The paper targets an important problem of enabling efficient private inference.

### Weaknesses
1. The analysis of why ReLU outperforms x^2 is too superficial to be a contribution. This point is not novel at all. The impact of sparsity induction and ReLU's desirable attributes have been thoroughly examined in prior works (Serra, T., Tjandraatmadja, C., & Ramalingam, S. (2018). Bounding and Counting Linear Regions of Deep Neural Networks. Proceedings of the 35th International Conference on Machine Learning.). Moreover, the comparison of relu(x), x^2, relu(x)^2 in Table 4 is not complete, making it unclear whether relu(x)^2 is better or worse that relu(x), however, which is stated in Section 3.1.

2. This paper lacks comparison with the latest methods. Authors should compare with the following papers:

a. Jha, Nandan Kumar, and Brandon Reagen. "DeepReShape: Redesigning Neural Networks for Efficient Private Inference." arXiv preprint arXiv:2304.10593 (2023).

b. Souvik Kundu, et al. Learning to linearize deep neural networks for secure and efficient private inference. International Conference on Learning Representation, 2023.

c. Kundu, Souvik, et al. "Making Models Shallow Again: Jointly Learning to Reduce Non-Linearity and Depth for Latency-Efficient Private Inference." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2023.

d. Zeng, Wenxuan, et al. "MPCViT: Searching for Accurate and Efficient MPC-Friendly Vision Transformer with Heterogeneous Attention." Proceedings of the IEEE/CVF International Conference on Computer Vision. 2023.

e. Zhang, Yuke, et al. "SAL-ViT: Towards Latency Efficient Private Inference on ViT using Selective Attention Search with a Learnable Softmax Approximation." Proceedings of the IEEE/CVF International Conference on Computer Vision. 2023.

f. Dhyani, Naren, et al. "PriViT: Vision Transformers for Fast Private Inference." arXiv preprint arXiv:2310.04604 (2023).

### Questions
Please refer to the weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
1. The paper proposes a novel deep neural network architecture called xMLP for Private Inference (PI) tasks. The authors identify that square activations can be processed much faster than ReLU, but using them leads to a drop in model accuracy. They attribute this accuracy drop to an "information compounding" effect.
 
2. PI enables deep learning models to work on private data without compromising privacy. However, existing PI systems suffer from high latency when using non-linear activations like ReLU. 

3. Leveraging this insight, the authors design xMLP, which exclusively uses square activations while maintaining accuracy and efficiency comparable to ReLU-based models.

### Strengths
1. Design a PI-friendly architecture is important for accelerating PI. The research problem of this work is meaningful.

2. Experimental results on CIFAR-100 and ImageNet datasets demonstrate that xMLP consistently outperforms ResNet models with fewer activation layers and parameters while achieving similar performance to its ReLU-based counterparts. 

3.xMLP achieves superior performance compared to state-of-the-art PI models, with a 0.58% increase in accuracy and 7x faster PI speed. Additionally, when offloading PI to the GPU, xMLP is up to 700x faster than the previous state-of-the-art PI model with comparable accuracy.

### Weaknesses
1. The author mentioned that they use Delphi's protocol to evaluate the proposed architecture inference. However, adding too many linear operations here would also increase the cost in offline phase. As the HE-based computation on lots of linear computation is quite costly.

2. Besides, the multiple layers here would also increase the communication cost during offline phase. As you have to do ciphertexts exchange for preparing the secret sharing masks. Furthermore, the use of transpose operations, which can be interpreted as reshapes for intermediate tensors, also introduces a significant overhead in the offline phase when using the Delphi protocol. This is because preparing the secret-sharing masks for these reshapes requires costly rotation operations in HE, which are not as efficient as in the plaintext domain.

### Questions
See Weakness part.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

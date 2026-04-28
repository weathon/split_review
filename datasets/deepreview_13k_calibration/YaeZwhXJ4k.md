# BinaryDM: Accurate Weight Binarization for Efficient Diffusion Models

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6

## Abstract
With the advancement of diffusion models (DMs) and the substantially increased computational requirements, quantization emerges as a practical solution to obtain compact and efficient low-bit DMs. However, the highly discrete representation leads to severe accuracy degradation, hindering the quantization of diffusion models to ultra-low bit-widths. 
This paper proposes a novel weight binarization approach for DMs, namely \textbf{BinaryDM}, pushing binarized DMs to be accurate and efficient by improving the representation and optimization. 
From the representation perspective, we present an \textit{Evolvable-Basis Binarizer} (EBB) to enable a smooth evolution of DMs from full-precision to accurately binarized. EBB enhances information representation in the initial stage through the flexible combination of multiple binary bases and applies regularization to evolve into efficient single-basis binarization. The evolution only occurs in the head and tail of the DM architecture to retain the stability of training. 
From the optimization perspective, a \textit{Low-rank Representation Mimicking} (LRM) is applied to assist the optimization of binarized DMs. The LRM mimics the representations of full-precision DMs in low-rank space, alleviating the direction ambiguity of the optimization process caused by fine-grained alignment.  
Comprehensive experiments demonstrate that BinaryDM achieves significant accuracy and efficiency gains compared to SOTA quantization methods of DMs under ultra-low bit-widths. With 1-bit weight and 4-bit activation (W1A4), BinaryDM achieves as low as 7.74 FID and saves the performance from collapse (baseline FID 10.87). As the first binarization method for diffusion models, W1A4 BinaryDM achieves impressive 15.2$\times$ OPs and 29.2$\times$ model size savings, showcasing its substantial potential for edge deployment.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces BinaryDM, a novel approach for accurate weight binarization of diffusion models (DMs) to achieve efficient deployment and inference on edge devices. The authors identify that binarizing DMs is challenging due to severe accuracy degradation caused by limited representational capacity and optimization difficulties. To address these issues, they propose two key techniques: 1)Evolvable-Basis Binarizer (EBB): This method enhances the initial representation capacity by starting with multiple binary bases and learnable scalars, which are gradually regularized to evolve into efficient single-basis binarization during training. EBB is selectively applied to crucial parts of the DM architecture to retain stability and reduce training overhead. 2)Low-rank Representation Mimicking (LRM): This technique improves the optimization process by aligning the low-rank representations of the binarized DM with those of a full-precision counterpart, mitigating the optimization direction ambiguity caused by fine-grained alignment. The authors conduct extensive experiments on various datasets and demonstrate that BinaryDM achieves significant accuracy improvements over state-of-the-art quantization methods under ultra-low bit-widths, while also providing substantial efficiency gains in terms of model size and computational operations.

### Strengths
1. The paper addresses the challenging problem of binarizing diffusion models. The proposed methods, EBB and LRM, are novel and tailored to address specific issues in binarizing DMs.
2. The authors provide a thorough experimental evaluation of their methods across multiple datasets and models. The results demonstrate that BinaryDM outperforms existing quantization methods under ultra-low bit-width settings, validating the effectiveness of the proposed techniques.
3. The paper is generally well-written and organized. The motivation behind the proposed methods is clearly explained, and the technical details are presented with sufficient depth. Figures and tables effectively illustrate the concepts and results.
4. Achieving efficient and accurate binarization of DMs is important for deploying these models on resource-constrained devices. The substantial efficiency gains demonstrated by BinaryDM highlight its potential impact in practical applications.

### Weaknesses
1. The Evolvable-Basis Binarizer (EBB) is selectively applied only to the first and last six layers of the diffusion model, covering only a small portion of the total parameters. This limited application scope raises concerns regarding the method’s generality and effectiveness throughout the network. Although the paper suggests that these head and tail layers are critical and parameter-sparse, it lacks a thorough justification or empirical evidence for this choice. Additionally, the middle layers, which remain untouched by EBB, may contribute significantly to the model’s performance and could also benefit from the method. By limiting EBB to specific layers, the paper potentially misses opportunities to enhance the representational capacity of the entire network. A more comprehensive exploration of applying EBB across different layers, including ablation studies, could provide insights into its most effective usage.

2. The paper introduces the Evolvable-Basis Binarizer (EBB) and Low-rank Representation Mimicking (LRM) to address challenges in training binarized diffusion models. However, it lacks a thorough analysis of training stability and convergence behavior. Binarized models are notoriously difficult to optimize due to the discrete nature of weights and activations, which can lead to issues like gradient mismatch and convergence to poor local minima. The paper would benefit from a detailed investigation into how EBB and LRM specifically improve training dynamics.

3. The paper compares BinaryDM primarily with baseline binarization methods and some low-bit quantization techniques like LSQ and Q-Diffusion. However, it does not thoroughly benchmark against the latest state-of-the-art quantization and binarization methods specifically designed for diffusion models or other generative models. Recent advances might offer competitive performance. A more comprehensive comparison would provide a clearer picture of where BinaryDM stands.

4. The paper focuses on empirical results but lacks a theoretical analysis of why the proposed methods improve performance. Providing theoretical insights or analysis could enhance the understanding of the underlying mechanisms.

5. Some technical details, particularly in the description of LRM and the training procedure, could be elaborated further to improve clarity. For instance, the choice of hyperparameters, how the low-rank projection matrices are computed and fixed, and the stability considerations during training.

### Questions
1. Can the authors provide more justification for the selective application of EBB to only the first and last six layers of the DM architecture? How critical is this choice, and how does it affect performance and training stability?
2. While the paper focuses on diffusion models, are there other binarization methods from other domains (e.g., binarized neural networks in classification tasks) that could be adapted for DMs? How does BinaryDM compare with such methods?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces BinaryDM achieving weight binarization in diffusion models while mitigating accuracy degradation. BinaryDM tackles the challenges of information loss and optimization difficulties inherent in binarization through two key techniques: Evolvable-Basis Binarizer (EBB) and Low-rank Representation Mimicking (LRM). EBB employs a multi-basis structure during training, allowing for a smooth transition to a single-basis binary representation for inference, thus enhancing representational capacity. LRM, on the other hand, facilitates the stable convergence of binarized DMs by mimicking the representations of a full-precision counterpart in a low-rank space, addressing the optimization direction ambiguity caused by extreme discretization.

### Strengths
1. Existing binarization works benefit a lot from exploiting residual connections which holds full precision information in the connection it self without information loss. This method exploit this benefit to the initial state of binarization to start with good initial state for lowering accuracy degradation without changing any network structure in the final state.
2. BinaryDM demonstrates superior accuracy and efficiency compared to existing binarization and low-bit quantization methods.

### Weaknesses
1. While BinaryDM shows good result in diffusion models, there are many works that prove good result on other models like ReActNet [1] and InstaBNN [2] (There are much more existing works). Since there are not many existing works in diffusion model quantization, the results in this paper is not enough to prove the true superiority of BinaryDM.
2. On the Evolvable Basis Binarizer (Equation 5), is there any reason the authors used “\sigma_{II} sign(w - \sigma_1 sign(w))” instead of “\sigma_{II} (w - \sigma_1 sign(w))” in second term? In this reviewer’s intuitive thinking, not utilizing sign function in second term would give more favorable initial state.
3. Details: Are the number of training iterations of BinaryDM and existing works same? Also curious if the learning rate or schedulers are used same as in existing works.

### Questions
1. While BinaryDM shows good result in diffusion models, there are many works that prove good result on other models like ReActNet [1] and InstaBNN [2] (There are much more existing works). Since there are not many existing works in diffusion model quantization, the results in this paper is not enough to prove the true superiority of BinaryDM.
2. On the Evolvable Basis Binarizer (Equation 5), is there any reason the authors used “\sigma_{II} sign(w - \sigma_1 sign(w))” instead of “\sigma_{II} (w - \sigma_1 sign(w))” in second term? In this reviewer’s intuitive thinking, not utilizing sign function in second term would give more favorable initial state.
3. Details: Are the number of training iterations of BinaryDM and existing works same? Also curious if the learning rate or schedulers are used same as in existing works.

[1] Zechun Liu, Zhiqiang Shen, Marios Savvides, and Kwang-Ting Cheng. Reactnet: Towards precise binary neural network with generalized activation functions. ECCV, 2020

[2] Changhun Lee, Hyungjun Kim, Eunhyeok Park, and Jae-Joon Kim, INSTA-BNN: Binary Neural Network with INSTAnce-aware Threshold, ICCV, 2023

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
In this work, the authors propose a quantization-aware training method that targets ultra-low bit-width representations, down to 1 bit resolution, oriented to diffusion models. More specifically, the proposed method consists of two parts, one focused on the feature representation of the applied diffusion architecture and the other on the optimization process. From the representation perspective, the authors propose a novel mechanism that gradually reduces the bases of binarized weights from higher to single-order base, applying a regularization term that according to the authors allows to smoothen the binarization process offering rich representation during the initial stage of training. Furthermore, the authors introduce a binarization-aware optimization method that projects the binarized and full-precision representations to lower ranks, applying Principal Component Analysis, forcing the low-rank binary representation to mimic the full precision one. This, according to the authors, enables the optimization of binarized diffusion models to focus on the principal direction and mitigate the ambiguity of the direction caused by the representation complexity of generation. The proposed method is applied in supplement with the vanilla binarization, with the proposed method targeting the most sensitive modules of the architecture, meaning on the outer layers, with the vanilla binarization applied on the intermediate layers. The paper provides extensive experimental evaluation on various datasets, including ablation studies, showing the effectiveness of the proposed method in contrast to the applied baselines, with the authors claiming that the applied methodology can significantly reduce the required Point Operations during the inference.

### Strengths
The proposed method results in significantly lower sized models with improved performance in reference to the baselines. This can potentially lead to significantly lower point operations and memory size during hardware deployment.

The proposed Evolvable-Basis Binarized results in richer representation during the initial stage of training as reported in Figure 2, showing significantly higher variance of parameters during the first iterations. As far I can say, the proposed method in fact smoothen the optimization process.

In general, the proposed method achieves sufficient performance in the challenging task of binarization.

### Weaknesses
The authors mention that the existing works have enhanced the binarized parameters via higher-order residual bases, but they introduce additional hardware complexity. However, the paper does not provide any evidence that the proposed method can be actually deployed in hardware accelerators without additional hardware, while the efficiency analysis reported is based on an estimation of OPs. The authors should note on the efficiency analysis section of the paper that is based on estimation and it would be beneficial to further discuss how their proposed method benefits the hardware inference in contrast to the existing methodologies. Can the authors elaborate on that, what overhead is introduced in existing methods in contrast to the proposed one?

Without theoretical nor empirical analysis regarding the location selection, I am concerned about how the authors conclude on applying the proposed approach on the first and last six layers of the models. Does the proposed method can be applied out-of-the-box on other architectures without applying exhaustive search on which layers should be applied? This makes me even more concerned regarding the generality of the proposed method is the fact that the proposed method is computationally intensive since it applies quantization-aware training that requires the computation of the covariance matrix of the binarized and full-precision representation. This introduces significant limitations on searching the layers where the application of the proposed method could be beneficial, hindering its generalization ability.

The notation used in some cases is weak. For example, it is not clear whether Equation 6 is applied channel-wise. Additionally, in the case of the trainable parameter $\sigma_{1}$ the domain is missing, raising the question whether the sigma can change the polarity of the binarized parameter or not. Additionally, it is not clear in the text if the $\sigma_{1}$ parameter is discarded after the training or if it is used also during the inference. Furthermore, using the same notation to denote different parameters as in the cases of Equations 9 and 2 can be misleading. Finally, $\epsilon_t$ is not properly defined in the text.

Although the most interesting part of the proposed method is the effective bit reduction down to 1W4A, the ablation study, which evaluates the different parts of the proposed method, is conducted only for 1W32A. I strongly recommend the authors to also include an ablation study for 1W4A, as it is the most impressive achievement of the proposed method.

### Questions
The authors mention that the existing works have enhanced the binarized parameters via higher-order residual bases, but they introduce additional hardware complexity. However, the paper does not provide any evidence that the proposed method can be actually deployed in hardware accelerators without additional hardware, while the efficiency analysis reported is based on an estimation of OPs. The authors should note on the efficiency analysis section of the paper that is based on estimation and it would be beneficial to further discuss how their proposed method benefits the hardware inference in contrast to the existing methodologies. Can the authors elaborate on that, what overhead is introduced in existing methods in contrast to the proposed one?

Without theoretical nor empirical analysis regarding the location selection, I am concerned about how the authors conclude on applying the proposed approach on the first and last six layers of the models. Does the proposed method can be applied out-of-the-box on other architectures without applying exhaustive search on which layers should be applied? This makes me even more concerned regarding the generality of the proposed method is the fact that the proposed method is computationally intensive since it applies quantization-aware training that requires the computation of the covariance matrix of the binarized and full-precision representation. This introduces significant limitations on searching the layers where the application of the proposed method could be beneficial, hindering its generalization ability.

The notation used in some cases is weak. For example, it is not clear whether Equation 6 is applied channel-wise. Additionally, in the case of the trainable parameter $\sigma_{1}$ the domain is missing, raising the question whether the sigma can change the polarity of the binarized parameter or not. Additionally, it is not clear in the text if the $\sigma_{1}$ parameter is discarded after the training or if it is used also during the inference. Furthermore, using the same notation to denote different parameters as in the cases of Equations 9 and 2 can be misleading. Finally, $\epsilon_t$ is not properly defined in the text.

Although the most interesting part of the proposed method is the effective bit reduction down to 1W4A, the ablation study, which evaluates the different parts of the proposed method, is conducted only for 1W32A. I strongly recommend the authors to also include an ablation study for 1W4A, as it is the most impressive achievement of the proposed method.

### Soundness
3

### Presentation
2

### Contribution
2

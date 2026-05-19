### Summary

This paper proposes a controllable generative image compression framework, termed Control-GIC, which is the first capable of fine-grained bitrate adaption across a broad spectrum while ensuring high-fidelity and generality compression. The Control-GIC is grounded in a VQGAN framework. Drawing inspiration from the classical coding principle, this paper correlates the information density of local image patches with their granular representations. Hence, the allocation of granularity for the patches can be flexibly determined to achieve dynamic adjustment for VQ-indices, resulting in desirable compression rates. A probabilistic conditional decoder is further developed to retrieve historic encoded multi-granularity representations according to transmitted codes, then reconstruct hierarchical granular features, enabling more informative aggregation to improve reconstruction realism. The experiments show that Control-GIC allows highly flexible and controllable bitrate adaption where the results demonstrate its superior performance over recent state-of-the-art methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

This paper proposes a controllable generative image compression framework, termed Control-GIC, which is the first capable of fine-grained bitrate adaption across a broad spectrum while ensuring high-fidelity and generality compression.

The experiments show that Control-GIC allows highly flexible and controllable bitrate adaption where the results demonstrate its superior performance over recent state-of-the-art methods.

### Weaknesses

#### Some Related Works


#### comment

In Section 3.1, the paper mentions that the features are matched to the codes in a pre-trained codebook C by VQGAN (this work use MoVQ) and quantized, producing Ê²_i and a set of discrete VQ-indices Ind_i that represent the closest matches in C based on Euclidean distance. How is this closest match obtained? If it is based on the nearest neighbor search, what is the complexity? How is the codebook constructed? Is it learned during the training process? What is the size of the codebook? These are not mentioned in the paper.

In Section 3.3, the paper introduces a statistical entropy coding strategy that captures the frequency distribution of indices usage across a natural dataset during training. How is this frequency distribution obtained? Is it based on a pre-defined distribution or learned from data? What is the impact of this frequency distribution on the compression performance?

In Section 3.4, the paper mentions that the overall loss function L for training Control-GIC contains the loss associated with the VQVAE architecture and GAN component in VQGAN. How are the parameters of VQVAE and GAN optimized? Is it through alternating optimization or joint optimization? What are the specific loss functions for VQVAE and GAN?

In the experiments, the authors compare the proposed method with some recent state-of-the-art methods. However, the authors only compare the performance in terms of distortion metrics, such as PSNR, and perceptual metrics, such as LPIPS. The comparison in terms of model complexity, such as the number of parameters and FLOPs, is not provided. This makes it difficult to evaluate the practicality of the proposed method in real-world applications.

Although the authors provide a lot of results, the analysis of these results is not sufficient. For example, in the ablation study, the authors only analyze the impact of different components on the performance. However, the reasons behind these impacts are not discussed in detail. More in-depth analysis is needed to understand the strengths and weaknesses of the proposed method.

### Suggestions

The paper should provide a more detailed explanation of the vector quantization process. Specifically, the method for finding the closest match in the codebook needs clarification. If a nearest neighbor search is used, the paper should discuss the computational complexity of this search, especially as the codebook size increases. Furthermore, the paper should elaborate on how the codebook is constructed, whether it is learned during training or pre-defined, and what the final size of the codebook is. This information is crucial for understanding the efficiency and effectiveness of the quantization process. For example, detailing the specific algorithm used for nearest neighbor search (e.g., k-d tree, hashing) and its time complexity would be beneficial. Additionally, the paper should discuss the impact of codebook size on the trade-off between compression rate and reconstruction quality. A larger codebook might lead to better reconstruction but also higher bitrates, and this trade-off should be analyzed.

Regarding the statistical entropy coding strategy, the paper needs to provide more details on how the frequency distribution of indices is obtained. Is this distribution calculated on a separate dataset, or is it derived from the training data itself? The paper should also discuss whether the distribution is fixed after training or if it is adapted during the compression process. Furthermore, the paper should analyze the impact of this frequency distribution on the compression performance. For example, if the distribution is not accurate, how does it affect the compression ratio? The paper should also consider discussing the potential for using adaptive entropy coding techniques, which could potentially improve compression performance by adapting to the specific characteristics of each image. A comparison with other entropy coding methods, such as arithmetic coding, would also be valuable.

The paper should also provide a more detailed explanation of the training process, particularly how the parameters of the VQVAE and GAN components are optimized. The paper should clarify whether the optimization is performed through alternating optimization or joint optimization. If it is alternating optimization, the paper should specify the order of optimization and the number of iterations for each component. If it is joint optimization, the paper should explain how the gradients are backpropagated through the different components. The paper should also provide the specific loss functions used for the VQVAE and GAN components, including any weighting factors or hyperparameters. Furthermore, the paper should discuss the convergence behavior of the training process and any techniques used to stabilize training. A detailed description of the training procedure is essential for reproducibility and for understanding the behavior of the proposed method.

### Questions

In Section 3.1, the paper introduces a granularity-informed encoder. How does this encoder determine the granularity of the patches? What is the relationship between the information density of the patches and their granularity? The paper should provide more details on the design and implementation of this encoder.

In Section 3.2, the paper mentions that the decoder receives the indices of Ê²_i and the corresponding masks m_i from the encoder. How are these masks generated? What is their role in the decoding process? The paper should provide more details on the structure and functionality of the decoder.

In the experiments, the authors compare the proposed method with some recent state-of-the-art methods. However, the authors only compare the performance in terms of distortion metrics, such as PSNR, and perceptual metrics, such as LPIPS. The comparison in terms of model complexity, such as the number of parameters and FLOPs, is not provided. This makes it difficult to evaluate the practicality of the proposed method in real-world applications.

Although the authors provide a lot of results, the analysis of these results is not sufficient. For example, in the ablation study, the authors only analyze the impact of different components on the performance. However, the reasons behind these impacts are not discussed in detail. More in-depth analysis is needed to understand the strengths and weaknesses of the proposed method.

### Rating

6

### Confidence

4

**********

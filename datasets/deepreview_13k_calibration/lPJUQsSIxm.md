# DCT-CryptoNets: Scaling Private Inference in the Frequency Domain

- Decision: Accept
- Avg Score: 6.33
- Scores: 5, 8, 6

## Abstract
The convergence of fully homomorphic encryption (FHE) and machine learning offers unprecedented opportunities for private inference of sensitive data. FHE enables computation directly on encrypted data, safeguarding the entire machine learning pipeline, including data and model confidentiality. However, existing FHE-based implementations for deep neural networks face significant challenges in computational cost, latency, and scalability, limiting their practical deployment. This paper introduces \sys, a novel approach that leverages frequency-domain learning to tackle these issues. Our method operates directly in the frequency domain, utilizing the discrete cosine transform (DCT) commonly employed in JPEG compression. This approach is inherently compatible with remote computing services, where images are usually transmitted and stored in compressed formats. \sys reduces the computational burden of homomorphic operations by focusing on perceptually relevant low-frequency components. This is demonstrated by substantial latency reduction of up to 5.3$\times$ compared to prior work on image classification tasks, including a novel demonstration of ImageNet inference within 2.5 hours, down from 12.5 hours compared to prior work on equivalent compute resources. Moreover, \sys improves the reliability of encrypted accuracy by reducing variability (e.g., from ±2.5\% to ±1.0\% on ImageNet). This study demonstrates a promising avenue for achieving efficient and practical privacy-preserving deep learning on high resolution images seen in real-world applications.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces DCT-CryptoNets, which performs neural network (CNN) inference entirely using TFHE-based homomorphic encryption in the frequency domain. Unlike hybrid protocols that limit homomorphic encryption to just linear operations, and require MPC for nonlinear operations, this approach leverages TFHE to perform both linear and nonlinear operations under homomorphic encryption. This enables private inference outsourcing to the server without requiring client interaction for intermediate computations. The authors have shown significant speedup over prior TFHE-based implementation (SHE, NeurIPS'19) on CIFAR-10 and ImageNet datasets.

### Strengths
$\bullet$ Performing TFHE-based inference in the frequency domain allows the usage of lower-resolution inputs without compromising accuracy. This approach significantly decreases both FLOPs and nonlinear operations (ReLU), while also requiring fewer bootstrapping operations. This results in substantial speedup benefits. More importantly, this makes it feasible to perform inference on larger input images, enhancing the practical applicability (such as semantic segmentation) of homomorphic encryption in neural network inference.


$\bullet$ The authors report ciphertext accuracy, specifically on the ImageNet-1K scale, distinguishing this work from most private inference papers, which typically report plaintext accuracy under the assumption that there is no accuracy loss when operations are conducted in field arithmetic.

$\bullet$ The experimental results are extensive and include a detailed sensitivity analysis of the cryptographic hyper-parameters.

### Weaknesses
$ullet$ The lack of sufficient algorithmic contributions and research insights makes it less suitable for the ML conference. Operating in the frequency domain for private inference benefits is not a novel concept (see [1,2]). Also, the usage of quantization-aware training for lower-frequency components is simply an engineering tweak. The paper does not sufficiently explore the trade-offs between the number of DCT coefficients retained and the resulting accuracy, which is a crucial aspect for practical deployment. Specifically, the paper lacks a detailed analysis of how different subsets of low-frequency DCT coefficients impact the overall performance and computational cost, making it difficult to assess the true efficiency gains.

Thus, a more fitting venue for this work might be a cryptography-focused conference. 

$ullet$ Moreover, the practicality of HE-only private inference remains questionable, especially when compared to hybrid protocol-based approaches. For example, Cheetah [3] achieves ImageNet-1K inference on ResNet-50 in 80.3 seconds in a LAN setting and 134.7 seconds in a WAN setting. Thus, the primary motivation for pursuing HE-only inference appears to be the benefit of non-interactive private inference. The paper does not adequately address the significant computational overhead associated with TFHE bootstrapping, which is a major bottleneck in practical applications. While the authors mention the reduction in bootstrapping operations, they do not provide a detailed breakdown of the computational cost associated with each operation, including the bootstrapping itself, making it difficult to evaluate the overall efficiency of their approach.

### Questions
See the weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a very promising strategy for achieving a practical and computationally efficient FHE-based (CKKS) private inference of deep learning models applied to high resolution images.     In a novel approach, the technique presented relies as a starting point on a Discrete Cosine Transform representation of the image.  It also employs a quantization aware training (QAT) framework.  Thorough comparative benchmarking of accuracy and latency for RGB vs DCT techniques a various image resolutions and at various levels of retained low-frequency components (of the DCT) are presented.  

The paper establishes both a detailed methodology and new "high-water mark" performance capability for ML inference generation for high resolution images.  Though performance is less pronounced on smaller images (32x32) it is the capability on larger images that is most important for future practical applications.

### Strengths
Novel DCT based insight for unstructured data yielding excellent computational advantages for high resolution images.

Thorough benchmarking and attention to reproducible science.

Excellent comparative analysis of this CKKS based technique relative to competing TFHE approaches.

Excellent and comprehensive list of references that chronicle the current state of the art and prior advances.

### Weaknesses
I find no obvious weaknesses.

I would emphasize to the reader perhaps new to the field ( in Section 3.2 on page 6)  that model training is done in the plaintext domain. (even though this is most evident in Figure 3 presented on Page 14.

### Questions
Are there any special scaling or normalization techniques that need to be considered when considering the YCrCb color space components of an image?

Can GPUs be used to any advantage in this approach?

Are there any privacy preservation guarantees or "leakage" guarantees that could be developed around this approach.  (I realize this may be challenging mathematically.)

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents DCT-CryptoNets, a novel framework that enhances privacy-preserving deep learning by utilizing the Discrete Cosine Transform (DCT) to operate in the frequency domain, significantly reducing latency and computational costs associated with fully homomorphic encrypted neural networks (FHENNs). By focusing on low-frequency information, DCT-CryptoNets improve accuracy and reliability in encrypted predictions while demonstrating superior scalability with increasing image resolution. The work addresses key challenges in existing FHE-based neural networks and emphasizes the importance of optimizing cryptographic and quantization parameters for practical applications in secure image processing.

### Strengths
1. **Frequency-Domain Optimization**: DCT-CryptoNets leverage the Discrete Cosine Transform (DCT) to focus on low-frequency components of images, which enhances the model's ability to capture perceptually salient information while reducing computational complexity and improving accuracy compared to traditional RGB-based networks.

2. **Reduced Latency and Improved Scalability**: The proposed method achieves significant latency reductions (up to 5.3×) during inference, especially on large datasets like ImageNet, while demonstrating superior scalability as image resolution increases. This makes DCT-CryptoNets more efficient for real-world applications of privacy-preserving deep learning.

3. **Enhanced Reliability through Reduced Error Accumulation**: By minimizing the need for homomorphic bootstrap operations, DCT-CryptoNets reduce the accumulation of approximation errors, leading to more reliable predictions and improved encrypted accuracy. This addresses challenges faced by earlier fully homomorphic encryption (FHE) schemes.

### Weaknesses
I have a question about the threat model setting here, why the model is trained locally?

If the client could train the model by themselves, why does they do inference locally.

Or if they want to deploy that encrypted model (key from model trainer) on the cloud for other clients as service. How does the key management should be solved?

### Questions
see weakness

### Soundness
3

### Presentation
3

### Contribution
3

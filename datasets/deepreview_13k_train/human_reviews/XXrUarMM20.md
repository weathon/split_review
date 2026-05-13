# Efficient and Quantization-Friendly Ternary Fourier Convolution Algorithms

- Decision: Reject
- Scores: 5, 3, 6

## Abstract
Fast convolution algorithms like Winograd and the Fourier transform are well-known for their substantial reduction in the multiplication complexity of Convolutional Neural Networks. However, when these methods are combined with model quantization, their inherently complex transformation matrices can introduce significant numerical errors, leading to a decrease in network accuracy. To address this challenge, we present a novel fast convolution algorithm that utilizes ternary matrices (coefficients containing only ±1 and 0) for input and weight transformations before multiplication, thus minimizing quantization errors. This approach is derived from the implementation of symbolic arithmetic on the Fourier transform to eliminate the involvement of irrational numbers. Then, we incorporate correction terms to  convert ineffective circular convolution results into efficient ones, thereby enhancing algorithm efficiency. Additionally, we propose a corresponding post-training quantization method that requires only a few samples for calibrating network parameters and restoring accuracy without the heavy cost of retraining. Our algorithms achieve 3.68x, 4.89x, and 4.54x theoretical multiplication complexity reduction for 3x3, 5x5, and 7x7 convolutions, respectively. For models trained on the ImageNet dataset, our algorithms with the post-training method, demonstrate an accuracy drop of less than 0.2% under Int8 quantization, surpassing other approaches with similar multiplication reduction ratios.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a new fast convolution algorithm that uses ternary matrices for transformations, minimizing these quantization errors. This technique is based on symbolic arithmetic applied to the Fourier transform, avoiding irrational numbers, and includes correction terms to improve the convolution results' efficiency. A novel post-training quantization method is also proposed, which calibrates network parameters using only a few samples, thus avoiding the need for expensive retraining. The proposed algorithms significantly reduce multiplication complexity—up to 4.89× for common convolution sizes—and demonstrate an impressively low accuracy drop of less than 0.2% on ImageNet models under Int8 quantization. This performance surpasses competing methods, offering a more efficient and accurate approach for CNN deployment in resource-constrained environments.

### Strengths
1. using symbolic operation instead of numerical computation is very attractive. The demonstration of the proposed idea is very solid and sound. 
2. I really appreciate the quantization method based on the frequency. The observation that a relation between the energy distribution and the frequency channel coordinates is very promising.
2. The evaluation result is very significant, about a 5x reduction in multiplicative complexity compared with other works.

### Weaknesses
1. The writing of this paper is very hard to follow. Many typos are in the paper, such as some numbers are missing in the first contribution of section Introduction " x x ", and the bottom line is missing in Table 2. 
2. The motivation for this paper is not clear. Since many compression works like extreme low-bit quantization, pruning, and low-rank decomposition are proposed to accelerate the convolution layers, the motivation using Fourier transformation is not clear. It is unclear why a Fourier transform approach is superior to existing methods, especially given the overhead of transforming to and from the frequency domain.
3. The evaluation is not sufficient. The metric in evaluation is multiplicative complexity, however, the compression ratio and real-time acceleration performance are missing. The paper lacks a comparison of the proposed method's memory footprint with other methods, and it does not provide any real-world latency measurements on hardware platforms.

### Questions
1. It would be better to provide the real-time latency to show the acceleration performance on hardware platforms like GPU/FPGA/CPU. The theoretical reduction in the multiplication operation.
2. Can this method be used in other layers? For example, FC can be seen as a special CNN layer with a kernel size being 1, and what if the proposed method is applied to FC layers?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper explores techniques for accelerating fast convolution algorithms based on Fourier transform through quantization. To mitigate the impact of quantization error, the paper utilized a ternary transformation matrix derived from symbolic arithmetic applied to the Fourier transform. Furthermore, the paper combines post-training quantization (PTQ) approach to enable INT8 quantization. The methods achieve a reduction on theoretical computation complexity while showing negligible accuracy loss on ResNet ImageNet benchmarks.

### Strengths
1). The paper is well written. The algorithm is clearly explained and easy to follow.

2). The results show clear improvement on both the computation complexity reduction, while preserving the model accuracy at INT8.

### Weaknesses
1). The use of “Ternary” in the title is misleading, as ternary refers to an intermediate transform matrix; the actual precision is INT8.

2). One of the primary concerns is the speedup achieved through current approach. The paper only provides theoretical multiplication complexity reduction, which may not necessarily translate to real-world speedup. Given the complexity of the algorithm and the potential overhead, it is important to provide empirical measurements of computation efficiency. The analysis should include not only the number of multiplications but also the overhead of the transform and inverse transform, as well as memory access patterns.

3). PTQ method is a well-established technique.

4). The evaluation is only performed on ResNet models, which, while important, are somewhat outdated. It would be benificail to evaluate the methods across a more extensive range of CNN models, particularly the compact ones like EfficientNet and MobileNet.

5). Today, numerous techniques exist for accelerating CNN models, including the design of compact architecture, sparsity, distillation, and quantization. For quantization alone, it is possible to reduce precision to sub-4 bit level while preserving model accuracy. The paper only compares its approach to other fast convolution algorithms, such as Winograde, and while it demonstrates improvement, it is challenging to evaluate the significance of this approach compared to toher alternatives.

### Questions
In addition to weaknesses above, 

1). How will this method be used for filters with smaller sizes, such as 1x1 and depth-wise conv layers?

2). Figure 3, the blue line for standard convolution does not seem to use SOTA PTQ techniques, which can effectively close the accuracy gap for INT4 (such as ref. 1 and 2).

3). Typo? Page 2, contribution 1 paragraph, x, x, and 7x7.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
- To address the issue of numerical errors caused by model quantization in the complex domain, the authors present a novel fast convolution algorithm referred to as Ternary Fourier Convolution (TFC) that utilizes ternary matrices for input and weight transformations before multiplication.
- The proposed TFC is derived from the implementation of symbolic arithmetic on the Fourier transform to eliminate the involvement of irrational numbers.
- And, the authors incorporate correction terms to convert ineffective circular convolution results into efficient ones. The proposed method achieves 3.68×, 4.89×, and 4.54× theoretical multiplication complexity reduction for 3×3, 5×5, and 7×7 convolutions, respectively.
- Moreover, the corresponding post-training quantization method requires only a few samples for calibrating network parameters and restoring accuracy without the high cost of retraining. The extensive experiments demonstrate an accuracy drop of less than 0.2% under Int8 quantization for models trained on ImageNet.

### Strengths
- (+) The proposed TFC addresses the issue of numerical errors caused by model quantization in a complex domain in a simple way and shows the efficiency in convolutions.
- (+) The method introduces a simple calibrating network parameter to minimize quantization errors and shows comparisons for quantization bits results.

### Weaknesses
 - (-) It seems to lack qualification results to support Table 2 such as comparisons of feature maps.
- (-) The ablation study on scale factor (e.q. 14) seems to be needed for its effectiveness.
- (-) We need an architecture table to compare one (TFC) with the others regarding layer-wise output size and number of parameters.

### Questions
- Please see the above weak points.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

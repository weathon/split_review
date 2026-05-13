# Video Deblurring with Adaptive High-frequency Extraction

- Decision: Reject
- Scores: 3, 5, 8, 3

## Abstract
State-of-the-art video deblurring methods use deep network architectures to recover sharpened video frames. Blurring especially degrades high-frequency information yet this aspect is often overlooked by recent models that focus more on enhancing architectural design. The recovery of high frequency detailing can be non-trivial, in part due to the spectral bias of neural networks. Neural networks are biased towards learning low frequency functions, making it to prioritize learning low frequency components. To enhance the learning of latent high frequencies, it is necessary to enforce explicit structures to capture the fine details or edges. This work merges the principles of the classic unsharp masking with a deep learning framework to emphasize the essential role of high-frequency information in deblurring. We generate an adaptive kernel, constructed from a convex combination of dynamic coefficients and predefined high-pass filtering kernels. This kernel is then employed in a spatio-temporal 3D convolution process to extract high-frequency components from the data. This method significantly improves video deblurring, achieving a noteworthy enhancement with an increase of up to 0.61dB in PSNR over top models on GORPO dataset. Additionally, it outpaces the majority of them in inference time.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes to merge the principles of the classic unsharp masking with a deep learning framework to emphasize the role of high-frequency information in deblurring. Specifically, it constructs the kernel with a convex combination of estimated coefficients and predefined high-pass filtering kernels. Several experiments are conducted to demonstrate its effectiveness.

### Strengths
High-frequency information are explicitly extracted to enforce the capture of finer details.

### Weaknesses
There are several unclear statements listed as follows.

1. This work is not well motivated. This paper is proposed based on a statement that neural networks prefer learning low-frequency components. While the work [a] has analyzed that convs are high-pass filters. Please discuss in detail whether these two statements conflict.
[a] Park and Kim, How do vision transformers work? ICLR 2022.
2. In the third paragraph of Section 1, the authors state that integrating spatial and temporal gradients into a neural network for video deblurring leads to an improvement of 0.39dB. Where does the result come from?
3. The authors mention several times that they utilize a set of predefined high-pass building kernels. How are these kernels predefined?  Are they the simple kernels defined in “Building kernels”? They are too simple to extract sufficient high-frequency information. What about learning these kernels?
4. In the experiments, please add the comparisons with more recent methods, e.g.,
[b] Li et al., A Simple Baseline for Video Restoration with Grouped Spatial-temporal Shift, CVPR 2023.
[c] Liang et al., Recurrent Video Restoration Transformer with Guided Deformable Attention, NeurIPS 2022.
5. Compared to the recent video deblurring methods, e.g., [b] and [c], the proposed method does not achieve the state-of-the-art performance, i.e., at least 1.97dB worse than [b] on the dataset ofGoPro and 1.11dB worse than [c] on the dataset of DVD.
6. Please add more comparisons on real examples.

### Questions
1. This work is not well motivated. This paper is proposed based on a statement that neural networks prefer learning low-frequency components. While the work [a] has analyzed that convs are high-pass filters. Please discuss in detail whether these two statements conflict. 
[a] Park and Kim, How do vision transformers work? ICLR 2022.
2. In the third paragraph of Section 1, the authors state that integrating spatial and temporal gradients into a neural network for video deblurring leads to an improvement of 0.39dB. Where does the result come from?
3. The authors mention several times that they utilize a set of predefined high-pass building kernels. How are these kernels predefined?  Are they the simple kernels defined in “Building kernels”? They are too simple to extract sufficient high-frequency information. What about learning these kernels?
4. In the experiments, please add the comparisons with more recent methods, e.g.,
[b] Li et al., A Simple Baseline for Video Restoration with Grouped Spatial-temporal Shift, CVPR 2023.
[c] Liang et al., Recurrent Video Restoration Transformer with Guided Deformable Attention, NeurIPS 2022.
5. Compared to the recent video deblurring methods, e.g., [b] and [c], the proposed method does not achieve the state-of-the-art performance, i.e., at least 1.97dB worse than [b] on the dataset ofGoPro and 1.11dB worse than [c] on the dataset of DVD.
6. Please add more comparisons on real examples.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose to extend unsharp masking using deep neural networks for video deblurring. The solution incorporates spatio-temporal 3D convolutions and high-pass filtering to focus on higher frequency features. Experiments on GoPro and DVD datasets show quantitatively and qualitatively improved results compared to previous works. Further experiments and analysis study the effectiveness of extracting high-frequency features and the proposed adaptive high-frequency operation.

### Strengths
Originality: The attempt to formulate unsharp masking using a deep neural network and its application to video deblurring is seemingly original.

Clarity: The paper is well-written, and the construction of the formulation for the solution is easy to follow by reading the paper.

Significance: The results look significant compared to the considered previous works.

### Weaknesses
My understanding is that the experimental results are presented for a single run per experiment. To better understand the significance of the claimed improvements, it is necessary to run the main experiments multiple times with a set of random number generator seeds and to present the results with properties of their distributions, such as mean and standard deviation under the assumption of a normal distribution.

Looking again at the results, especially in Table 4, the improvements given by the proposed AHFNet appear marginal when compared to naive kernels (+0.09 for PSNR and +0.002 for SSIM), while the GMACs measure is also the same. This raises concerns about the practical significance of the proposed method, given the increased complexity of a deep learning approach compared to simpler kernel-based methods. The lack of substantial gains in performance, despite the computational overhead, needs to be addressed.

### Questions
I am interested to see the performance of the proposed method compared to previous works on a real-world deblurring dataset, such as [1].

[1] Zhong, Zhihang, et al. "Real-world video deblurring: A benchmark dataset and an efficient recurrent neural network." *International Journal of Computer Vision* 131.1 (2023): 284-301.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a type of kernel prediction network where the basis function are composed of high pass filters for video deblurring.

### Strengths
The paper proposes to use high pass filters as basis for kernel prediction. This is a very intuitive idea, and this makes the number of parameters to be learned smaller. The proposed method is able to perform better than the SOTA.

### Weaknesses
While the intuition for the development of the method is given, certain aspects of the results are not well-explained. For eg., based on the design one may expect the results from the proposed method to be sharper than the SOTA. But, what we are seeing is more than that. In Fig. 2 and Fig. 3, we see more details in the proposed method than in the compared methods. What is causing this to happen?

I would be interesting to how the method performs if the basis functions were not used, but instead KPN is used like it is generally without any restrictions. Such an experiment would help determine the usefulness of using the high pass filters as basis.

The proposed method is not video-specific. The idea and solution both are more single image/ burst imaging specific. The authors are applying the idea in video deblurring domain, but the proposed method is not specific to this. Is there a reason this method applied specifically for video deblurring?

### Questions
Check the weakness section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a network for dynamic scene image deblurring by adaptively fusing extracted high-frequency information. The provided experiments show the proposed method performs better than existing methods.

### Strengths
The provided results show the proposed method performs better than other methods (even though some improvement is marginal).

### Weaknesses
1. The motivation that unsharp masking is useful for deblurring is not clear. The only thing used in the proposed network is extracting high-frequency information.
2. The only novelty of this paper is adaptive extracting high-frequency information which is too marginal.
3. Why does the network use pre-defined high-frequency kernels to extract information? Why not allow the network to learn it directly?
4. The authors do not provide enough analysis to demonstrate the effectiveness of the high-frequency information. More analysis is needed.
5. Some improvement is too marginal, e.g. Table 2 and Figure 2(with artifacts).

### Questions
See weaknesses for details.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor

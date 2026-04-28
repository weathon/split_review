# Multiscale Training of Convolutional Neural Networks

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 8, 3, 6

## Abstract
Convolutional Neural Networks (CNNs) are the backbone of many deep learning methods, but optimizing them remains computationally expensive. To address this, we explore multiscale training frameworks and mathematically identify key challenges, particularly when dealing with noisy inputs. Our analysis reveals that in the presence of noise, the gradient of standard CNNs in multiscale training may fail to converge as the mesh-size approaches to $0$, undermining the optimization process. This insight drives the development of Mesh-Free Convolutions (MFCs), which are independent of input scale and avoid the pitfalls of traditional convolution kernels. We demonstrate that MFCs, with their robust gradient behavior, ensure convergence even with noisy inputs, enabling more efficient neural network optimization in multiscale settings. To validate the generality and effectiveness of our multiscale training approach, we show that (i) MFCs can theoretically deliver substantial computational speedups without sacrificing performance in practice, and (ii) standard convolutions benefit from our multiscale training framework in practice.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces an approach to improving the computational efficiency of CNNs through a multiscale training framework.
It first presents Multiscale Stochastic Gradient Descent (Multiscale-SGD), which leverages the Multilevel Monte Carlo method to reduce computational costs by approximating gradients across resolutions.
However, the authors identified that noisy or high-frequency inputs can lead to unbounded gradients across mesh resolutions, complicating the convergence process.
To address this, they propose Mesh-Free Convolutions (MFCs), which are independent of specific input scales and ensure consistent gradient convergence across resolutions, even with noisy inputs. This mesh-independence of MFCs overcomes the convergence limitations observed in standard CNNs during multiscale training.

### Strengths
This paper introduces an innovative approach to multiscale CNN training through Multiscale-SGD and Mesh-Free Convolutions (MFCs).
All the developments are backed by mathematically reasoning.
And the whole paper is logically organized.

### Weaknesses
1. The experimental results are really limited, and you should also compare the performance with the fixed computational budget.
2. The experimental comparison with existing multiscale or Fourier-based CNN methods is not presented
3. The mathematical foundation for Mesh-Free Convolutions, particularly the differential operator theory, could be challenging for readers less familiar with this domain. Adding a visual explanation or intuitive analogies could make the theory more accessible.
4. In the experiments, the network seems really shallow, could you train deeper networks, to see whether the methods works?

### Questions
1. All the results show mixed performance bettween the regular SGD and the two Multiscale-SGD. If you could train longer for the multiscale-SGD, could you improve all the performance comparing to SGD?
2. The MSE results are strange, with the two UNet have huge gap. What is the reason behind it?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Training convolutional neural networks (CNNs) on high-resolution images can be computationally demanding. One way to alleviate the computational burden is by including downsampled versions at different scales during training. This paper identifies shortcomings of standard CNNs in such multiscale approaches and introduces “Mesh-Free Convolutions” (MFCs) to address these limitations. The paper presents two novel multiscale training algorithms, “Multiscale-SGD” and “Full-Multiscale-SGD”, which estimate high-resolution parameters using coarser-resolution samples, thus avoiding costly training on high-resolution data. For such multiscale training schemes, gradients of conventional CNNs for noisy data might diverge with decreasing resolution compared to “smooth data”. Inspired by differential operators, MFCs offer a resolution-independent generalisation of standard convolutions. The empirical validation demonstrates that these techniques can improve training time and ensure consistent gradient behaviour, as shown for standard UNet and ResNet architectures and image blur estimation, image denoising, and image super-resolution tasks.

### Strengths
I believe this paper provides several important contributions and extends the existing literature in different significant ways:

__S1.__  The authors propose new techniques for training CNNs within a multiscale resolution framework, which improve computational efficiency while maintaining test performance. This alone can be a valuable contribution, as shown by the “non-MFC” empirical results in Tables 3, 4, and 5. 

__S2.__ As far as I can tell, MFCs are an original and promising alternative to traditional convolutional layers (though some clarifications may be necessary; see W2 below) that can alleviate some of the shortcomings of traditional CNNs in multiscale approaches. Given their potential application across various high-resolution tasks, this can be a significant contribution, too.

__S3.__ The quality of the paper is high, with claims well-supported through mathematical derivations, proofs, and empirical evidence. In particular, the experimental results in Tables 3, 4, and 5 highlight that significant speed-ups might be feasible (as measured by #WU; however, see Q2 below).

For these reasons, I consider this a good paper.

### Weaknesses
Some clarity aspects could be addressed to strengthen the paper. In more detail, I currently see the following weaknesses:

__W1.__ Section 3.1 on “Mesh-Free Convolutions” is relatively dense and challenging to follow. For instance, some notations typically used with parabolic PDEs, like indices denoting partial derivatives, should be more clearly introduced. More importantly, the connection between $u$, $v$, $\tilde{v}$, and $\mathcal{C}$ is not very clear and should be made more explicit. Specifically, the role of the parameter $\xi$ in defining the convolution operator $\mathcal{C}$ and how it relates to the spatial derivatives needs further clarification. The mathematical notation, while precise, could benefit from a more intuitive explanation of how these terms translate to the actual implementation of the convolution.

__W2.__ Expanding on the previous point, the paper would benefit from a more intuitive explanation or illustration of the connection between standard convolutions and mesh-free convolutions. Currently, the connection is difficult to assess. In that regard, Figure 3 lacks clarity and might require additional explanation. It is not immediately obvious how the parameters of the mesh-free convolution relate to the filter weights of a standard convolution, and a more detailed explanation of how the spatial derivatives are approximated and used in the mesh-free convolution would be beneficial. The figure should also clarify how the different parameter choices affect the resulting filter shapes and their behavior.

__W3.__ _Computational considerations_: As the authors highlight in lines 334-338, the required Fast Fourier Transform dominates the overall computational cost. To provide the complete picture, additional consideration of running time and optimisation steps in the results in section 5 on “Experimental Results” would strengthen the contribution. This would allow a more comprehensive assessment of MFC's computational feasibility. Specifically, the paper should include a detailed breakdown of the computational cost of the FFT and the other components of the MFC, and compare these costs to those of standard convolutions. Furthermore, it would be beneficial to discuss potential optimizations for the FFT implementation and their impact on the overall runtime. The current analysis lacks a detailed comparison of the practical runtime performance of MFCs versus standard convolutions, making it difficult to assess the real-world benefits of the proposed approach.

Minor remarks:
- Line 231: “[…] without compromising on its efficiently.” should likely be “[…] on its _efficiency_.”
- Line 293: “[…] let $v = \mathcal{C}(\xi)u$ be the mesh-free convolution is parameterized by $\xi$“ needs to be rewriten.
- Line 296: Equation “(17a)” likely should just read “(17)”.

### Questions
__Q1.__ To illustrate the difference between conventional CNNs and MFC, would it be possible to compare feature maps between these two approaches?

__Q2.__ A more formal definition of the _work unit_ metric #WU might be beneficial. As I understand it, #WU measures how many evaluations of the highest resolution are required, with evaluations at lower resolutions being weighted by the corresponding “downsampling factor”. Is this correct? If so, should this not lead to fractional values of #WU?

### Soundness
3

### Presentation
2

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
This work begins with an error analysis of the the standard training procedure for convolutional networks when training at multiple resolutions, and (using some clever re-interpretations by varying mesh size and sample size) derive new multiscale training algorithms that require fewer network evaluations at the finest mesh size. They further present mesh-free convolutions that can be thought of as limits of progressively refined mesh-dependent convolutions. Finally, experimental results are presented to compare the training algorithms and network variants against deep learning standards like SGD and U-Nets/ResNets.

### Strengths
1) The primary research questions in the paper are well-motivated.
2) The technical analysis seems to be sound, and the authors are able to propose interesting, non-obvious training algorithms from them (i.e., this goes far beyond "multiscale training is useful for learning convolutional kernels"). I also found the further step of mesh-free convolutions to be very interesting from a theoretical perspective.

### Weaknesses
My major problems with the paper pertain to the experimental results, and fall into two main categories:

1) The experiments done are on extremely small networks and datasets. There are very standard collections of computer vision experiments that could be used to show the benefits of the proposed multiscale-SGD training algorithms (see, for example, the benchmarks used for experiments in any landmark CV papers from the past few years, like CLIP or Segment Anything). I understand that compute access could be a factor here, but many of these datasets are small enough that access to even a single GPU should be sufficient to perform the necessary experiments.

2) Unclear presentation of results. It's difficult to understand the relative compute requirements of different algorithms based on the work unit representation that is used in the experiments. It would be much clearer to either present the FLOPs required per iteration or backward pass, or best of all would be to simply show the amount of time taken to train the network in each case.

3) Non-competitive baselines. In practice, multiscale training is implicitly accounted for in most deep learning training procedures via data augmentations in the form of varying-sized crops of images (see the widely-used RandomResizedCrop transform in torchvision). To me, this is the actual baseline to which we should compare to, but it is not mentioned or compared against at all in your work.

Based on these, I find it difficult to be convinced by the presented experiments that the proposed multiscale algorithms would be better to use than standard SGD on usually-sized computer vision trianing tasks.

### Questions
1) Why are there no experiments on CV prediction tasks like classification, segmentation, object detection, etc.? Are the proposed algorithms not expected to work well in these contexts?

2) Corresponding to the data augmentation comment above: It was not clear to me if you use data augmentations like RandomResizedCrop or similar in any of your experiments; do you? If not, would you be able to show what happens when these are added to the single-scale SGD training procedure?

3) Corresponding to the comment on presentation of results comment above: could you add (even approximate) FLOPs computations or raw timings to your experiments?

4) Are there situations in which it would be preferable to use the Multiscale-SGD algorithm that you proposed instead of the Full-Multiscale-SGD algorithm? If not, it would be better to focus more of the experiments on the Full-Multiscale algorithm, and leave the Multiscale algorithm to an ablation study.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a training framework designed to optimize CNNs more efficiently by employing multiscale training strategies. This approach targets the significant computational challenges that arise when training CNNs at high resolutions, especially when handling noisy input data. By introducing Multiscale-SGD and the MFCs, the framework reduces computational costs and ensures stable gradient behavior across varying scales.

### Strengths
1.	The paper presents a good framework that integrates multiscale training with convolutional neural networks (CNNs).
2.	The writing of this paper is easy to follow.
3.	The experiments validate the effectiveness of the proposed methods, showcasing practical improvements of the proposed method.
4.	This paper offers thorough mathematical analysis, including proofs and lemmas.

### Weaknesses
1.	A significant limitation is the evaluation performed with shallow CNNs, all models containing fewer than four layers. Given that practical applications often leverage deeper architectures like ResNet with over 18 layers, it raises concerns about the scalability and real-world applicability of the proposed multiscale framework. Demonstrating results with deeper networks, specifically those with residual connections, is crucial to validate its utility for larger and more complex tasks. The current experiments do not sufficiently address the potential challenges that might arise when applying the method to networks with a larger number of parameters and more complex optimization landscapes.
2.	In the context of modern architectures, transformers such as Vision Transformers (ViT) are becoming more prominent for various applications. The paper does not explore whether the proposed method could be adapted or extended to transformer-based architectures. This is particularly relevant as transformers may handle multiscale data differently from CNNs, and their attention mechanisms might interact with the proposed multiscale training in unforeseen ways. The absence of any discussion or experimentation in this direction limits the scope of the paper's conclusions.
3.	While the paper presents experimental validation of the proposed method's effectiveness, the experiments are mostly focused on simpler tasks. The applicability of the method to more complex and challenging applications, like object detection, video understanding tasks, remains untested. These tasks often involve more intricate data dependencies and require robust feature learning, which may expose limitations of the proposed method not apparent in simpler settings. The lack of evaluation on such tasks makes it difficult to assess the real-world impact of the proposed framework.
4.	While the paper claims significant computational advantages with the multiscale approach, it lacks a thorough comparative analysis of computational costs with existing training methods. For instance, how this method compares in terms of hardware resource use, memory consumption, or training speed against some techniques like mixed-precision training is not clearly outlined. A detailed analysis should include metrics such as FLOPs, memory footprint, and wall-clock time, providing a clear picture of the method's efficiency gains relative to other optimization techniques.
5.	The paper could benefit from a deeper exploration and further discussion of how the training dynamics change with the proposed method compared to standard methods. Specifically, the paper should analyze how the multiscale approach affects the loss landscape, the convergence rate, and the generalization performance. A more detailed analysis of training curves, gradient norms, and other relevant metrics is needed to fully understand the behavior of the proposed method.

### Questions
See the above weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

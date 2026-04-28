# Deep Complex Spatio-Spectral Networks with Complex Visual Inputs

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 3, 6, 8

## Abstract
Complex-valued neural networks have attracted growing attention for their ability to handle complex-valued data with enhanced representational capacity. However, their potential in computer vision remains relatively untapped. 
In this paper, we introduce Deep Complex Spatio-Spectral Network (DCSNet), a fully complex-valued token-based, end-to-end neural network designed for binary segmentation tasks. Additionally, our DCSNet encoder can be used for image classification in the complex domain. We also propose an invertible real-to-complex (R2C) transform, which generates two complex-valued input channels, complex intensity and complex hue, while producing complex-valued images with distinct real and imaginary components.
DCSNet operates in both spatial and spectral domains by leveraging complex-valued inputs and complex Fourier transform.
As a result, the complex-valued representation is maintained throughout DCSNet, and we avoid the information loss typically associated with Real$\leftrightarrow$Complex transformations. Extensive experiments show that DCSNet surpasses existing complex-valued methods across various tasks on both real and complex-valued data and achieves competitive performance compared to existing real-valued methods, establishing a robust framework for handling both data types effectively.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper presents a transformation to map RGB images into complex domain and an associate network comprising a loss function to handle such complex inputs.

Overall, the contributions are significant and may be of interest to the community, but the paper organization could be improved and more focus should be placed on the transformation.

### Strengths
1) The proposed transformation is novel and may be an important contribution for the community working in complex and hypercomplex domains.
2) Although not novel, using the fourier filter module is good to handle complex inputs.

### Weaknesses
1) While the method sounds, the results are not impressive and surely they are not statistically significant. As of my experience, complex, quaternion, and in general hypercomplex models clearly outperform real-valued counterparts when they are able to catch some underlying physical process intrinsic into data. Maybe, the tasks chosen by the authors do not highlight the effectiveness of their method. Maybe, the authors could stress more the parameters saving of using a complex model with respect to a real-valued one, which can help reducing the computational load while obtaining comparable results.
2) The authors should have focused more on the transformation, which is a novel contribution, and better show its properties (see questions).
3) Some key references to related works are missing, the authors should at least give credit to them, or better try to compare their method with them. Some of them follow, but I encourage the authors to better explore previous literature on complex, quaternion and hypercomplex networks.

[1] C. Trabelsi, O. Bilaniuk, Dmitriy Serdyuk, Sandeep Subramanian, J. F. Santos, Soroush Mehri, Negar Rostamzadeh, Yoshua Bengio, C. Pal, "Deep Complex Networks", ICLR 2017.

[2] E. Grassucci, A. Zhang, D. Comminiello, "PHNNs: Lightweight Neural Networks via Parameterized Hypercomplex Convolutions", IEEE Transactions on Neural Networks and Learning Systems, (Volume: 35, Issue: 6, June 2024).


Minor comments:

The Saxon Genitive should be avoided in scientific writing, although I know that both ChatGPT and Grammarly insert it. I suggest the authors to remove all the Saxon genitives in the paper.

### Questions
1) I am very curious about the invertibility of the proposed transform. Given the Algorithm 2 in Appendix A, would it be possible to have some experiments to prove its effectiveness? I think that this transformation is the real contribution of the paper, as it allows a direct mapping between greyscale and RGB images, which was lacking in complex and quaternion papers that often struggle to do so.
2) Which is the computational load in terms of FLOPs, runtime memory, and time of the proposed model?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The work proposes a complex-value deep neural network for computing vision tasks. First, the authors propose an inevitable real-to-complex transformation. Then, the work proposes an architecture comprising spectral convolution and a complex T2T module. 
The authors evaluated their model on image classification, smooth object detection, and defocus blur detection.

### Strengths
The work proposes a novel invertible real-to-complex conversion for RGB images in complex-valued neural networks. The procedures are clearly stated using pseudocode and figures.

### Weaknesses
1. The authors seem to miss the seminal work on complex values networks and didn’t compare/discuss with the techniques discussed in [1]
2. The work is directed at using complex-valued networks for real-valued images. The majority of the paper involves devising an invertible conversion from real to complex representation. However, the paper fails to demonstrate its utility. For example, for classification on ImageNets, the authors did not consider state-of-the-art models, such as Vit, Swin-v2, etc., which achieve above 90% accuracy.

3. The paper does not discuss the motivation of the specific real to complex conversion. There are many invertible conversions between real and complex.

### Questions
1. Line 317: Citation link broken for T2T-ViTYuan et al. (2021)

2. Line 269: Do you use complex-valued  “ normalization” as discussed in [1]

3. How well does the model perform if we consider trivial real to complex conversion that considers the real numbers as complex numbers with $0$ imaginary part? This is also a very crucial ablation that the authors should perform.

4. Does using spectral convolution make it challenging to capture local features as it performs global convolution?


[1] DEEP COMPLEX NETWORKS

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces the Deep Complex Patio-Spectral Network (DCSNet), a fully complex-valued, token-based neural network developed for end-to-end foreground extraction and adaptable for image classification. Extensive experiments show that DCSNet surpasses current complex-valued approaches across various tasks with real and complex-valued data, achieving results on par with leading real-valued models.

### Strengths
This paper presents a novel complex-valued neural network, the Deep Complex Patio-Spectral Network (DCSNet), a fully complex-valued, token-based, end-to-end architecture designed for foreground extraction and adaptable to image classification tasks. Extensive experiments demonstrate that DCSNet outperforms existing complex-valued methods across diverse tasks involving both real and complex-valued data, achieving competitive results relative to state-of-the-art real-valued models. The paper is well-written, concise, and easy to follow.

### Weaknesses
Novelty: The novelty of this paper appears questionable. The authors claim that they propose the first token-based complex-valued network that maintains complex-valued information throughout. However, the fully Complex-valued Convolutional Network (FCCN) [1] also processes complex-valued data through the entire model. Could the authors clarify any differences between these two models? What advantages does DCSNet offer over FCCN?

[1] Saurabh Yadav; Koteswar Rao Jerripothula, FCCNs: Fully Complex-valued Convolutional Networks using Complex-valued Color Model and Loss Function. ICCV 2023.

Complex-valued Image Generation (R2C Method): The authors propose an R2C method for generating complex-valued images from real-valued images, presenting it as a novel complex-valued color transformation. However, methods such as quaternion representation, complex logarithmic transformation, and the Hilbert transform are well-established for generating complex-valued images. Could the authors specify the advantages of the R2C method over these alternatives?

DCSNet Architecture:
1. Fourier filters replace self-attention in DCSNet to retain information within the complex domain while preserving global context. How do Fourier filters achieve global information retention in this context, and why were they chosen?
2. The paper briefly mentions dense tokens for image embedding but doesn’t fully explain their purpose. Are these tokens meant to capture pixel-level details (dense information) of the image? If so, why not use high-resolution Fourier filters as localized filters to capture this information directly?
3. If large Fourier filters serve as global filters in the frequency domain while dense tokens capture image details, could a bank of wavelet filters offer a more effective solution? Wavelet filters with multiple resolutions could extract both global (large scale) and local (small scale) image features.

Resolution Tokens: The paper mentions multiple resolution tokens \T_{i} for i \in {0,1,2,3}. What was the reasoning for using exactly four resolutions? Would using more or fewer resolutions impact the results?

Table 7 Clarification: In Table 7, there is a term \calL_{isal}. Is this a typo? Please clarify its meaning if not.

### Questions
Please see the weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This study investigates a novel complex-valued deep CNN designed for foreground extraction. It proposes a new method for encoding RGB images as complex values, an end-to-end token-based architecture that maintains the complex representation throughout, and an improved training pipeline. The authors demonstrate superior performance on a variety of complex-valued image benchmarks.

### Strengths
I am unfamiliar with the literature on complex-valued neural networks, and defer to the opinion of more reviewers. As a neophyte to this field, I found the manuscript overall to be very readable, well-written, interesting, and convincing. The novel encoding, architecture, and training pipeline seem to work well, and produce a very capable model for handling complex-valued inputs.

### Weaknesses
This may be my ascribed to my naivety for the field, but I'm unsure how to interpret the benchmark results. While DCSNet certainly seems to outperform other complex-valued neural networks, the margin of victory is often in the range of 1-5 percent. It is difficult to tell whether this represents a fundamental advance, or a marginal improvement. Further, Table 2 seems to indicate that complex-valued neural networks in general frequently fail to outperform their real-valued counterparts. How should these results be interpreted with respect to the broader viability of complex-valued neural networks?

### Questions
See weaknesses above.

### Soundness
4

### Presentation
4

### Contribution
4

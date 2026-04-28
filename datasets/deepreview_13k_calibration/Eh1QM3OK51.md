# PIN: Prolate Spheroidal Wave Function-based Implicit Neural Representations

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Implicit Neural Representations (INRs) provide a continuous mapping between the coordinates of a signal and the corresponding values. As the performance of INRs heavily depends on the choice of nonlinear-activation functions, there has been a significant focus on encoding explicit signals within INRs using diverse activation functions. Despite recent advancements, existing INRs often encounter significant challenges, particularly at fine scales where they often introduce noise-like artifacts over smoother areas compromising the quality of the output. Moreover, they frequently struggle to generalize to unseen coordinates. These drawbacks highlight a critical area for further research and development to enhance the robustness and applicability of INRs across diverse scenarios. To address this challenge, we introduce the Prolate Spheroidal Wave Function-based Implicit Neural Representations (PIN), which exploits the optimal space-frequency domain concentration of Prolate Spheroidal Wave Functions (PSWFs) as the nonlinear mechanism in INRs. Our experimental results reveal that PIN excels not only in representing images and 3D shapes but also significantly outperforms existing methods in various vision tasks that require INR generalization, including image inpainting, novel view synthesis, edge detection, and image denoising.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposes Prolate Spheroidal Wave Function-based Implicit Neural Representations (PIN), an effective representation inspired by Prolate Spheroidal Wave Functions (PSWFs). The proposed PIN outperforms other INR baselines in various reconstruction tasks.

### Strengths
- The proposed PIN outperforms other INR baselines in various reconstruction tasks, including image reconstruction, image inpainting, and occupancy field and NeRF.
- Detailed ablation studies are conducted.

### Weaknesses
 - The metrics provided in the paper are only evaluated on a few individual examples. I appreciate the evaluation on the Kodak Lossless
True Color Image Dataset. However, it only contains 24 images. It is ideal to perform larger-scale evaluations, e.g. calculating the mean PSNR for a thousand images. For example, one may consider using the DIV2K dataset [1].



### Questions
- I am interested in the runtime of the proposed PIN. Will the new formulation hurt the speed of INRs? Is there a trade-off between quality and runtime?
- How is the experiment conducted for the Image Inpainting task? Are the missing pixels marked as black and fed into the INR? Or are those coordinates masked out and not used during training? Are the pixel masks provided to the INR?

### Soundness
3

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
5

### Summary
The paper proposes a novel Implicit Neural Representation (INR) utilizing Prolate Spheroidal Wave Functions (PSWFs) to improve performance and generalization in computer vision tasks. By leveraging the optimal space-frequency domain concentration of PSWFs, the proposed method addresses the noise artifacts over smoother areas and poor generalization of existing INRs, demonstrating superior results in image inpainting, novel view synthesis, edge detection, and image denoising.

### Strengths
1. The paper clearly explains the limitations of current INRs and proposes a novel activation function (PSWFs) for INR to overcome these limitations.
2. The localization and expressivity properties of PIN have been theortically proven.
3. The results validate the effectiveness of the proposed INR across various tasks. The authors not only show the good representation ability of PIN for various signals, such as image, Occupancy Filed, and NeRF, but also show that PIN has a very good performance on image Image Inpainting.

### Weaknesses
1. The activation function seems to be rather computationally heavy, making it necessary to report its speed in applications. 
2. As I have reviewed the previous submission of this paper, I notice that the Fig.4 is replaced with a scene with better results. I wonder how these new results are obtained and why these results are not attached in previous submission? Are they obtained by tuning parameters for each scene specifically?
3. Since the first NeurIPS submission of this paper, several new INRs have been proposed, including FINER (and its extension, FINER++) and H-SIREN. However, these new INRs are not cited or compared within the current manuscript.

### Questions
See Weakness.

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
3

### Summary
This paper introduces the use of prolate spheroidal wave functions (PSWF) for implicit neural representation (INR). By employing PSWF as the activation function in INR, the method excels not only in representing images and 3D shapes but also significantly outperforms existing approaches in various vision tasks that rely on INR generalization, including image inpainting, novel view synthesis, edge detection, and image denoising.

### Strengths
1. Extensive experiments across various vision tasks demonstrate the effectiveness of PSWF.

2. A comprehensive theoretical analysis highlights the advantages of using PSWF.

### Weaknesses
1. When comparing different INR methods, do you ensure that the same parameters are used? Could you provide the specific parameters for each INR method? It's crucial to understand if the performance gains are solely due to the PSWF activation or if they are influenced by specific parameter tuning for each baseline. For instance, what are the specific values for the frequency parameters in WIRE, the $\omega$ parameter in SIREN, and the $\sigma$ parameter in GAUSS for each experiment? Without this information, it's hard to ascertain the fairness of the comparison.

2. I am curious about the decoding complexity of the PSWF-based INR. Could you provide the decoding speed or time for the different INR methods? The computational cost of using PSWF is a critical factor, especially for real-time applications. It would be beneficial to have a quantitative comparison of the decoding time for different INR methods to understand the trade-off between performance and computational efficiency. This should include not only training time, but also inference time.

3. Besides the vision tasks mentioned in the paper, can PSWF also improve performance in image super-resolution? The paper demonstrates the effectiveness of PSWF in several vision tasks, but it's unclear if its benefits extend to other tasks like super-resolution. Providing results on this task would further demonstrate the general applicability of the proposed method.

### Questions
I noticed that the authors use initial INR methods as their baselines. However, there are several approaches aimed at enhancing the expressivity and generalizability of INR, including improvements in training strategies [1] and input signals [2]. Could PSWF be applied to these methods to further enhance the representation performance of INR?


[1] Improved Implicit Neural Representation with Fourier Reparameterized Training, CVPR 2024

[2] Disorder-invariant implicit neural representation, CVPR 2023.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper argues that the Gaussian and Gabor wavelet activation functions cannot achieve the optimal space-frequency trade-off, and thus may not effectively capture distant relevance. Motivated by this, the paper proposes using the Legendre polynomial numerical estimation of the Prolate Spheroidal Wave Function (PSWF) as the activation function, which has been proven in previous work to offer the optimal space-frequency trade-off. The authors demonstrate improvements through experiments on various tasks, including image regression, neural radiance fields, and so on.

### Strengths
1. The motivation presented in the paper is compelling and provides a solid foundation for the proposed approach.  
2. This paper offers a insightful critique of previous works, identifying limitations in existing activation functions and highlighting the need for improvement.  
3. The experiments encompass a diverse range of tasks, allowing for a more comprehensive and thorough comparison. This diversity enhances the validity of the findings and demonstrates the effectiveness of the proposed method across different domains.

### Weaknesses
1. The exact implementation of the numerical estimation of the Prolate Spheroidal Wave Function lacks clarity in the main text. For instance, the approximation order is not explicitly stated, and the impact of the approximation order on the computational complexity (in terms of space/time consumption) and the model's performance is not clearly explained. Furthermore, while the authors mention using a numerical approximation, they do not specify the method used for discretization of the PSWF, which is crucial for understanding the practical implementation. The choice of discretization method (e.g., finite difference, finite element, spectral methods) can significantly affect the accuracy and computational cost of the approximation. It is also unclear how the authors handle the infinite support of the PSWF in practice, as any numerical implementation must truncate this support, and the truncation method and its impact on the approximation are not discussed.
2. The experiments in tasks, such as Occupancy Field Representation and Neural Radiance Field, appear to be conducted on a subset of the entire dataset, which may undermine the persuasiveness of the results. Specifically, the paper does not specify the number of objects used for training and testing in these experiments, nor does it detail the criteria for selecting these subsets. This lack of transparency makes it difficult to assess the generalizability of the proposed method. Additionally, the paper lacks a comparison with state-of-the-art methods in these specific tasks, making it difficult to gauge the relative performance of the proposed approach.
3. The presentation could be improved by refining certain details, such as employing the vector graphics and employing the \autoref{} command for figure citations to ensure consistency and clarity. The current figures lack the visual clarity needed to fully understand the results, and the inconsistent citation format makes it difficult to follow the paper's arguments.

### Questions
1. Could you clarify the approximation order used for the Prolate Spheroidal Wave Function (PSWF)? Additionally, does this approximation affect the theoretical properties of the PSWF? The paper mentions that PSWF possesses infinite support in space, but it remains unclear whether the finite-order approximation may potentially diminish this property.
2. I observed that a bandwidth parameter \(c\) governs the frequency. Could you provide guidance on how to select this parameter effectively? Does it influence model performance, and if so, what strategies should users follow to determine an optimal value, especially for tasks in continuous domains like Neural Radiance Fields (NeRF), where there might be no frequency bounds, unlike the image regression scenario?

### Soundness
3

### Presentation
2

### Contribution
3

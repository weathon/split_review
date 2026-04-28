# NIR-Assisted Image Denoising: A Selective Fusion Approach and A Real-World Benchmark Dataset

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 8, 5, 5

## Abstract
Despite the significant progress in image denoising, it is still challenging to restore fine-scale details while removing noise, especially in extremely low-light environments. Leveraging near-infrared (NIR) images to assist visible RGB image denoising shows the potential to address this issue, becoming a promising technology. Nonetheless, existing works still struggle with taking advantage of NIR information effectively for real-world image denoising, due to the content inconsistency between NIR-RGB images and the scarcity of real-world paired datasets. To alleviate the problem, we propose an efficient Selective Fusion Module (SFM), which can be plug-and-played into the advanced denoising networks to merge the deep NIR-RGB features. Specifically, we sequentially perform the global and local modulation for NIR and RGB features, and then integrate the two modulated features. Furthermore, we present a Real-world NIR-Assisted Image Denoising (Real-NAID) dataset, which covers diverse scenarios as well as various noise levels. Extensive experiments on both synthetic and our real-world datasets demonstrate that the proposed method achieves better results than state-of-the-art ones.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors propose an efficient lightweight selective fusion module that can be plug-and-played into any denoising network to accomplish the NIR-assisted denoising. In addition, this paper constructs a corresponding real-world NIR-assisted image denoising dataset.

### Strengths
Plug-and-play lightweight fusion modules can be embedded in any single-image denoising network.
Real-world dataset is a promising solution to the current lack of data for this problem and are expected to be the baseline benchmark dataset for future research.

### Weaknesses
1. The ablation experiment lacked a probe to see if the loss of multiple scales would affect the final output picture.
1. The lightweight fusion module in this paper does not contribute enough to the technology and simply fuses the features.
1. This paper does not demonstrate whether the improvement in denoising performance is due to the superiority of the method or only to the inclusion of NIR information.

### Questions
Are the methods compared in the paper all image restoration assisted by NIR images? If not, is retraining performed for the comparison?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a new NIR-Assisted Image Denoising dataset which covers diverse scenarios as well as various noise levels. They also propose an efficient selection fusion module in order to address the inconsistency between NIR-RGB images. This module can be plug-and-played into the existing denoising networks to merge the NIR-RGB features. The experimental results demonstrate the effectiveness of the proposed method.

### Strengths
1. The new dataset is valuable.
2. The proposed selective fusion module is simple yet effective.
3. The overall writing quality is good.

### Weaknesses
 There is one place that is not clear.
The authors claim that "Therefore, we deploy a GMM to handle color discrepancy first followed by an LMM dealing with structure discrepancy". Is there any supporting evidence that the GMM handles the color discrepancy while the LMM handles the structure discrepancy?

### Questions
See the weakness section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes an efficient Selective Fusion Module (SFM) for NIR-Assisted Image Denoising (NAID) and presents a real-world dataset covering diverse scenarios and noise levels. The proposed method achieves better results than state-of-the-art techniques, and the dataset serves as a benchmark for future research. The SFM decouples color and structure discrepancy issues and addresses them with Gaussian Mixture Model (GMM) and Laplacian Mixture Model (LMM), respectively. The compact and lightweight network design adds few parameters and computation costs and can be integrated into existing advanced denoising networks.

### Strengths
1. The proposed SFM achieves significant performance improvements while maintaining interpretability.
2. The NAID dataset covers diverse scenarios and noise levels, making it a valuable benchmark for future research.
3. The compact and lightweight network design adds few parameters and computation costs and can be integrated into existing advanced denoising networks.

### Weaknesses
1. Relative to other NIR-assist denoising approaches, the innovation quotient of the proposed method appears constrained, potentially limiting its adaptability across diverse imaging conditions and noise levels. The method's reliance on decoupling color and structure discrepancies using GMM and LMM, while interpretable, may not fully capture the complex interplay of noise and artifacts present in real-world scenarios. Specifically, the assumption that color and structure can be independently addressed might oversimplify the problem, potentially leading to suboptimal performance when these issues are highly correlated or when the noise characteristics deviate from the assumed Gaussian or Laplacian distributions.
2. Concerns arise regarding the efficiency of the methodology, particularly when juxtaposed with alternative techniques, as evidenced by its prolonged training durations. While the authors claim a lightweight design, the practical implications of longer training times, especially when scaling to larger datasets or more complex network architectures, are not adequately addressed. The reported training time, even if comparable to some methods, may still pose a barrier for practical deployment, particularly in resource-constrained environments or when rapid prototyping is required.
3. The introduced SFM module lacks explicit clarity on addressing pivotal challenges inherent to NIR-assist operations. The description of GMM and LMM as solutions for color and structure discrepancies, respectively, is somewhat superficial. It is unclear how these modules specifically handle issues such as varying illumination conditions, sensor noise characteristics, and the inherent differences in spectral sensitivity between NIR and RGB sensors. A more detailed explanation of how the SFM module adapts to these challenges, perhaps through a more rigorous mathematical formulation or empirical analysis, is needed.

### Questions
1.How does the proposed SFM compare to other denoising techniques in terms of computational efficiency?
2.Can the proposed method be applied to other types of images, such as medical images or satellite images?
3.How does the NAID dataset compare to other benchmark datasets in terms of diversity and size?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an NIR-assist RGB image denoising method, which mainly includes two parts: First, an effective SFM module is proposed to help the selective fusion of NIR and RGB images and solve the content inconsistency between NIR-RGB images. And the module is plug-and-play. Secondly, a real-world NIR-Assisted Image Denoising (NAID) dataset is proposed.

### Strengths
The authors conduct experiments to verify the proposed method for denoising images on both synthetic and proposed real-world datasets. Ablation studies are conducted to validate the effectiveness of the two contributions. The paper looks technically sound and describes the algorithm clearly.

### Weaknesses
I am concerned that the overall contributions are trivial. Especially, the proposed SFM module should be provided with more design reasons.

Weaknesses:

1. For GMM and LMM, NIR and RGB are concatenated along channel dimensions to input the same subsequent modules, and then split to obtain the two estimated NIR weights and RGB weights to apply to the corresponding branches, respectively. It seems to me that two estimated weights are the same, how to achieve selective fusion? Or are manually setting parameters involved? It would be better to provide some justification or motivation for the design choices.
2. Table 7 is not mentioned in the paper.

### Questions
See Weaknesses

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

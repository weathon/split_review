# ”DOES YOUR MOBILE SUIT YOUR SKIN?”: ADDRESSING SKIN TONE DISPARITIES IN PRESENTATION ATTACK DETECTION FOR ENHANCED INCLUSIVITY OF SMARTPHONE SECURITY

- Decision: Reject
- Avg Score: 3.67
- Scores: 3, 3, 5

## Abstract
Mobile devices are at a heightened risk for cybercrime due to the sensitive personal and financial data they handle. Biometric authentication provides a robust,convenient, and secure way to protect smartphones by using unique user characteristics like fingerprints, facial features, or voice patterns for access. Existing mobile biometric technology often relies on RGB cameras to capture biometric
samples, such as face images or finger photos, making them vulnerable to spoofing (e.g., 3D masks, display or printout attack). The security of these systems is effectively addressed by integrating a Presentation Attack Detection (PAD) module. Existing PAD solutions do not account for diverse physical characteristics such as skin tone. As a result, marginalized groups face higher misidentification
rates or false rejections, reducing access to services and increasing security risks.

This paper introduces a novel deep learning framework called ColorCubeNet that is designed to process ColorCube, a multi dimensional data representation by combining information from RGB, HSV and YCbCr color spaces. This data cube leverages the joint capabilities of RGB, HSV, and YCbCr color spaces to depict color more sophisticatedly. By incorporating features from multiple complementary color channels, this approach can effectively handle a variety of skin tones. We utilized three EfficientNet-B0 models, each trained on ImageNet using RGB, HSV, and YCbCr color spaces, and then fine-tune them on the ColorCube representation to fully exploit the combined information from all three color spaces. Additionally, a channel-attention mechanism is integrated into the architecture, enabling the extraction of key features from different input channels and exploit their combined performance. Results show that the proposed approach outperforms traditional RGB methods by reducing skin tone disparities by 50%.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents ColorCubeNet, a framework designed to address skin tone disparities in Presentation Attack Detection (PAD) for mobile biometric systems. By combining RGB, HSV, and YCbCr color spaces into a unified "ColorCube" representation, the model effectively reduces skin tone biases and enhances PAD performance across diverse demographics. Key contributions include (1) the ColorCube representation, which leverages complementary color spaces to reduce recognition discrepancies due to skin tone, (2) skin tone labeling to facilitate model training across varied skin types, and (3) the integration of a channel-attention mechanism for more effective feature extraction across color channels. Experiments demonstrate that ColorCubeNet significantly outperforms traditional RGB-based models, achieving a 50% reduction in skin tone disparity in PAD accuracy.

### Strengths
This work originally applies a combined color space approach (ColorCube) to address skin tone disparities in Presentation Attack Detection (PAD) for mobile biometrics. By introducing the ColorCube representation—a novel fusion of RGB, HSV, and YCbCr color spaces—ColorCubeNet leverages a more inclusive depiction of skin tones. This approach builds upon existing color space theories but innovatively applies them, addressing an underexplored aspect of biometric authentication: equitable performance across diverse skin tones.

### Weaknesses
The paper provides a promising step towards inclusive PAD solutions; however, several areas could be improved to enhance its technical rigor, novelty, and generalizability. Below are specific, actionable insights for improvement:

1. The core of ColorCubeNet relies on EfficientNet-B0 and channel attention mechanisms, which are well-established deep learning techniques. The paper would benefit from a deeper exploration of why these specific components are particularly suited for addressing skin tone bias in PAD beyond general statements. 
For example, the authors could analyze the contributions of channel attention, specifically about color space variance across skin tones, or explore alternative network designs that directly address color discrimination and tonal consistency. Such technical differentiation would elevate the work’s originality and provide a more customized solution for the stated problem.

2.  While the ColorCube representation is central to the model’s effectiveness, the paper lacks detailed justification for why RGB, HSV, and YCbCr were chosen and how their combination mitigates skin tone bias. Further explanation on how each color space addresses unique aspects of skin tone representation could improve understanding. Additionally, testing other color spaces, such as LAB, known for its perceptual uniformity, could be included in an ablation study. A clearer rationale for the final ColorCube design—ideally supported by empirical evidence—would strengthen the theoretical foundation of the proposed solution.

3. The SOTA comparison is limited primarily to models from the same authors, which does not comprehensively assess ColorCubeNet’s performance against established PAD methods. The paper should include comparisons with state-of-the-art models from top computer vision and biometric conferences to offer a fairer benchmark. Incorporating the latest results from different approaches would demonstrate ColorCubeNet’s competitive edge or limitations more transparently, positioning the work more credibly within the existing literature.

4. While the SNR analysis is presented as a measure of interpretability, it is unclear how this metric directly supports PAD fairness or performance. A more thorough explanation of how SNR values correlate with skin tone bias or help identify features impacted by tonal variance would improve clarity.  Furthermore, the authors could consider other interpretability techniques, such as saliency maps or Grad-CAM analyses, to strengthen the interpretability argument and more effectively highlight model biases across skin tones.

5. The paper does not specify what feature representations are used as inputs to PCA. Since ColorCubeNet operates with a combined RGB, HSV, and YCbCr color space (resulting in a 9-channel representation), it’s important to know whether PCA is applied directly on these raw color space features, intermediate layer outputs (e.g., after channel attention), or final feature embeddings from ColorCubeNet.

In summary, while ColorCubeNet addresses an important problem, the paper would benefit from stronger justification of its technical choices, a broader and more rigorous comparison with SOTA models, and expanded evaluations for robustness and practical utility. Furthermore, the paper does not align well with ICLR's primary scope and research focus. ICLR is known for contributions that advance fundamental deep learning theory, novel architectures, and techniques with broad applicability and generalizability. However, this paper is primarily an applied work targeting a specific biometric application.

The ColorCubeNet model is based on established methods (EfficientNet and channel attention) and lacks substantial innovation in model architecture or learning methodologies. Furthermore, while extensive within the PAD context, the empirical evaluations offer limited novelty in the context of ICLR’s typical focus on advancing core machine learning principles.

### Questions
See above

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper presents an algorithm for face and fingerprint presentation attack detection utilizing a stack of multiple color channels including YCbCr, HSV, and RGB. These different color spectrum images are combined to form a 9-channel image which is an input to a channel attention block. The experiments are performed using multiple face and fingerprint PAD datasets to demonstrate the effectiveness of the proposed algorithm.

### Strengths
+ The proposed algorithm is found effective in handling both face and fingerprint PAD although trained individually on both forms of datasets.
+ The paper is easy to read and follow.
+ The intuition behind developing models to handle skin tones is essential, although not novel.

### Weaknesses
- Technically the paper has an incremental contribution. The prime reason is the use of the different color channels in the existing literature.

[1] Boulkenafet Z, Komulainen J, Akhtar Z, Benlamoudi A, Samai D, Bekhouche SE, Ouafi A, Dornaika F, Taleb-Ahmed A, Qin L, Peng F. A competition on generalized software-based face presentation attack detection in mobile scenarios. In2017 IEEE International Joint Conference on biometrics (IJCB) 2017 Oct 1 (pp. 688-696). IEEE.

[2] J. He and J. Luo, "Face Spoofing Detection Based on Combining Different Color Space Models," 2019 IEEE 4th International Conference on Image, Vision and Computing (ICIVC), Xiamen, China, 2019, pp. 523-528

[3] Towards Face Presentation Attack Detection Based on Residual Color Texture Representation

Further, the use and role of skin tone image labeling in PAD are not clear. How has it been used for different skin tone PA detection? The experiments are performed under unseen skin tone presentation attack detection.

- The robustness and generalizability (cross-dataset) of the proposed algorithm have not been conducted. Further, the fairness of the proposed algorithm must also be reported.

- The comparison has not been performed by PAD algorithms. The base and old CNNs are used for comparison.

[1] Fang M, Yang W, Kuijper A, Struc V, Damer N. Fairness in face presentation attack detection. Pattern Recognition. 2024 Mar 1;147:110002.
[2] Wang K, Zhang G, Yue H, Liu A, Zhang G, Feng H, Han J, Ding E, Wang J. Multi-domain incremental learning for face presentation attack detection. InProceedings of the AAAI Conference on Artificial Intelligence 2024 Mar 24 (Vol. 38, No. 6, pp. 5499-5507).
[3] Fang M, Damer N. Face Presentation Attack Detection by Excavating Causal Clues and Adapting Embedding Statistics. InProceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision 2024 (pp. 6269-6279).

### Questions
1. A comparison with SOTA models is needed especially developed for PAD tasks.

2. The generalizability and fairness (evaluation of different skin tones) of the proposed algorithms need to be reported. 

3. The justification of technical novelty is needed. Both technical and quantitative comparison is required.

4. The ablation study with individual color channels along with score and feature fusion is needed.

5. What is the computational cost of the proposed algorithm? 

6. It would be better to report the performance in terms of known evaluation metrics such as EER and HTER.

-------------------
*Thanks for your response; however, concerns are not satisfactorily addressed. Therefore, I will retain my original rating.*

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper propose a method to mitigating skin tone disparities in presentation attack detection (PAD) systems for biometric authentication. By integrating RGB, HSV, and YCbCr into a unified ColorCube representation, the authors address the bias in traditional RGB-based systems, enhancing inclusivity across diverse skin tones. The model demonstrates a 50% reduction in skin tone disparities.

### Strengths
This paper try to address a critical gap in biometric authentication security regarding skin tone fairness.

The use of multi-channel ColorCube representation reduces skin tone disparities in biometric authentication systems.

The proposed method's performance validated on 6 datasets.

### Weaknesses
The contribution is limited as the main idea of this paper is combine different color channel to improve PAD performance across skin tones, but as authors mentioned, this idea has already been explored to some extent in prior research (Marasco & Vurity (2022)). If you could explain how your method differs or builds upon those (not just different color channel) would be good.

This paper uses a variety of datasets, but does not have enough details about dataset size, balance (for different skin tones). An underrepresentation of certain skin tones could have a significant impact on the model's performance, which is not explored. I suggest you could provide a detailed breakdown of the skin tone distribution in each dataset, and discuss how any imbalances may impact the results. 

The authors does not provide a detailed discussion or evaluation of the time cost for ColorCubeNet. As it is a critical factor for biometric authentication. You could include runtime comparisons between ColorCubeNet and baseline methods on typical mobile hardware. This would give readers a concrete sense of the computational trade-offs involved.

The ITA is presented as the main method for quantifying skin tone differences, but the paper could have benefited from experimenting with other methods to provide a more comprehensive evaluation.

### Questions
See above

### Soundness
3

### Presentation
3

### Contribution
2

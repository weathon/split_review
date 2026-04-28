# Hidden in the Noise: Two-Stage Robust Watermarking for Images

- Decision: Accept
- Avg Score: 5.83
- Scores: 6, 6, 6, 6, 5, 6

## Abstract
As the quality of image generators continues to improve, deepfakes become a topic of considerable societal debate. Image watermarking allows responsible model owners to detect and label their AI-generated content, which can mitigate the harm. Yet, current state-of-the-art methods in image watermarking remain vulnerable to forgery and removal attacks. 
This vulnerability occurs in part because watermarks distort the distribution of generated images, unintentionally revealing information about the watermarking techniques.

In this work, we first demonstrate a distortion-free watermarking method for images, based on a diffusion model's initial noise. However, detecting the watermark requires comparing the initial noise reconstructed for an image to all previously used initial noises. To mitigate these issues, we propose a two-stage watermarking framework for efficient detection. During generation, we augment the initial noise with generated Fourier patterns to embed information about the group of initial noises we used. For detection, we (i) retrieve the relevant group of noises, and (ii) search within the given group for an initial noise that might match our image. This watermarking approach achieves state-of-the-art robustness to forgery and removal against a large battery of attacks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates reverse vulnerabilities in diffusion watermarking methods to forgery and removal attacks. Specifically, the authors propose WIND, a two-stage watermarking framework that first embeds a unique group identifier within the initial noise of a diffusion model using Fourier patterns and then searches the reconstructed noise within the noise group to identify the match. Empirical results show that WIND can achieve better detection performance and robustness against various attacks.

### Strengths
(1) The paper is organized by some theoretical analysis and empirical evaluations. Furthermore, the motivations and methodology are clearly stated overall.

(2) The work leverages the inherent initial noise of diffusion models as a watermark without external watermarking processes that might degrade image quality. It is innovative that grouped noise patterns are used with Fourier-based group identifiers, which is effective and robust. 

(3) The search efficiency is heavily relied on the number of watermarks N and noise group M, which is partially solved by proposing a faster detection variant.

(4) The effectiveness of the proposed watermarking generalized to inpainting task.

### Weaknesses
(1) The evaluations of the proposed approach are limited, where only one diffusion model is investigated. Moreover, some experimental settings are missing.

(2) Proof of Theorem 4.1 seems not entirely convincing. Although it is stated as a mathematical result, the actual evidence is more empirical rather than rigorous. For example, the paper’s results show low false positives, but the proof does not provide a probability bound for these occurrences.

More details can be seen in Questions.

### Questions
(1) The authors only evaluate the method on Stable Diffusion v2. The generalization is unknown to other diffusion models, such as Stable Diffusion XL, consistency models and transformer-based diffusion architectures. Moreover, it is unclear how detection would perform at higher generation resolutions. And what is the prompt template for the generation? 

(2) Can WIND be adapted to GAN-based generative models when DDIM inversion is replaced by other reconstruction approaches?

(3) The inversion step could affect both reconstruction speed and performance. The trade-off between the inversion step, watermarking overhead, and detection accuracy is not discussed.

(4) It could be better to include group index embedding in Algorithm 1.

### Soundness
2

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
4

### Summary
This paper presents an innovative watermarking method that uses the initial noise in diffusion models as a distortion-free watermark, showcasing its potential application in addressing societal challenges such as deepfakes. The two-stage watermarking framework proposed by the authors incorporates Fourier patterns during the generation process to enhance the robustness of the initial noise and effectively retrieves relevant noise groups during detection.
Despite the significant contributions, this paper has several shortcomings. Firstly, the structure and logical flow of the paper could be improved, particularly in the abstract section. Additionally, some technical terms and concepts should be explained in more detail to aid reader comprehension. Furthermore, the depth of the results analysis could be enhanced, suggesting an exploration of the potential reasons for changes in results and their impact on the overall robustness of the method.

### Strengths
Strengths：
1.	The two-stage framework proposed in this paper addresses the vulnerabilities of current watermarking techniques, effectively demonstrating the combination of deep learning and traditional watermarking methods. This innovation offers a fresh perspective in the watermarking field.
2.	The research provides specific solutions, emphasizing the robustness of the method against various attacks. This contribution not only enhances the practical applicability of the paper but also lays a valuable foundation for future research in the area.

### Weaknesses
Weakness:
1. The research motivation is unclear. In the Abstract section, the structure could be further optimized. There is a lack of smooth logical connection between the two paragraphs of the abstract. The first paragraph primarily discusses deepfakes and the limitations of current watermarking methods, but there is no clear transition when moving to the new framework in the second paragraph. This makes it difficult for readers to understand why the new method is necessary and how it relates to the issues discussed earlier.
2. The interpretation of the experimental results is insufficient. Descriptions of the tables and figures are very clear, but a deeper analysis of these results could enhance the paper. For example, in Table 2, while the changes in similarity are displayed, it would be beneficial to explore the potential reasons behind these changes and how they impact the overall robustness of the method.
3. In the experimental section, while images generated by your framework are presented, there is a lack of quantitative analysis of image quality. 
4. There is a lack of the performance across a broader range of inference steps beyond the 50-step setting currently used. Testing various inference step counts (e.g., 20, 50, 100, and 200 steps) can help determine how the step count affects model performance in terms of robustness.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
1. This paper introduces a novel distortion free diffusion model based watermarking method for images. The method is distortion free as it employs initial random noise that is already used by the model versus previous methods/models that distort the distribution of generated images which negatively affects the robustness of those models. 
2. The method tackles both watermark removal attacks and forgery attacks.
3. To make the watermark detection process more efficient, during generation grouped noises are augmented with distinct fourier patterns/identifiers. Therefore during detection, first the group identifier is recovered and then the exact match within it is found making the detection much faster versus comparing the noise to all previously used initial noises.

### Strengths
originality and significance: 
- The method presented by the paper is able to tackle both forgery and removal attacks unlike previous works.
- Shows that initial noise used by diffusion models can be a watermark and improves robustness.

quality and clarity: The paper is generally well written - maintains a good flow of ideas, very few typos and explains concepts and background where necessary

### Weaknesses
1. Qualitative results only cover Watermark Detection Accuracy in Table 1 but it is important to add other detection metrics such as TP/AUC etc for a stronger evaluation and to be more convincing.
- Also, no ablation on perturbation strenghts vs detection accuracy

2. Section 5.2 Watermarking non-synthetic images: Issues with this section
- Quantative Evaluation - Only evaluates FID, but does not touch upon more image similarity and quality metrics of watermarked images like CLIP score, SSIM and PSNR. 
- Qualitative: Lacks side by side comparison of watermarked images results from different models
3. Experiments: Details of how the experiments were performed are lacking. Ex: how was the detection threshold (picked?
4. Supplementary (nit, optional): Would be good to see side by side comparisons of competing methods on runtime or atleast approximate numbers that demonstrate the factor by which this method is slower.

### Questions
Please see the weaknesses section above.

Questions:
1. In Section 5.2 Watermarking non-synthetic images: It does not seem like the image quality is actually close to the non-watermarked images - In images which contain text in Fig 5 and Fig 9, the watermarked images are not able to retain the text seen in the original non-watermarked image (ex: last row of images with traffic text directions and text on the aircraft). Are there ways in which this problem can be resolved/handled?
2. It seems like this method relies on the (approximate) invertibility property of DDIM. Is so, please mention this in section 2.2. Fig 1 mentions it but it would be nice to also add it in 2.2 for clarity if this is the case.   
3. Is there any other diffusion model besides SD v2 that this method was tried with?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a watermarking method using initial noise in diffusion processes as a robust, distortion-free way to mark AI-generated images. The authors propose a two-stage framework called WIND, which employs initial noise and Fourier patterns to facilitate efficient watermark detection and withstand forgery and removal attacks.

### Strengths
1. The methodology is easy to follow.

2. Evaluates several settings.

3. The two-stage approach efficiently narrows down the search space by using Fourier pattern group identifiers, significantly improving detection runtime and scalability

### Weaknesses
1. The idea of picking the initial noise for diffusion is not new. And this method changes initial noise a lot compared to Tree-Ring watermark.

2. The evaluation of robustness if not comprehensive.

3. Potential vulnerability to more advanced attacks

### Questions
1. The organization of the paper appears somewhat disorganized. For example, Section 5.2 and the Algorithms section should be relocated to precede Section 5, which discusses the experiments. This adjustment would provide better coherence, as watermarking non-synthetic images is an integral part of the methodology.

2. The evaluation of different watermarking methods is somewhat limited. The focus of this work is primarily on watermarks that involve selecting initial noise for the diffusion process, while other watermarking techniques, such as HiDDeN, are excluded. The authors should provide an explanation for this choice to give context to the scope of their evaluation.

3. While the paper makes significant claims regarding robustness, the robustness evaluation itself is not comprehensive. Beyond image transformations and regeneration attacks, there are numerous adaptive attacks where the adversary possesses greater capability. Examples include transfer-based, query-based, and white-box attacks such as WEvade. These types of evaluations should be considered to strengthen the robustness analysis.

4. How is threshold $\tau$ determined in the experiments?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces the WIND framework for embedding watermarks in AI-generated images. WIND leverages the initial noise of the diffusion process as a distortion-free watermark, embedding group-specific Fourier patterns in the noise to enable efficient watermark verification. The proposed two-stage approach aims to reduce search complexity, improve robustness against various attacks, and optimize verification accuracy.

### Strengths
1. The two-stage approach employed in WIND is similar to a multi-level indexing mechanism. Initially, group-specific Fourier patterns narrow down the search scope (Tier-1), and subsequently, an exact matching process with the original noise ensures precise verification (Tier-2). This hierarchical structure not only enhances efficiency but also serves as a novel adaptation of multi-level indexing in watermarking, supporting scalable, high-speed identification in large datasets.
2. The framework demonstrates robustness against several attacks, including forgery, removal, and distortive transformations. The two-tiered verification and Fourier embedding make WIND resilient to various manipulations, ensuring watermark persistence even under adversarial conditions.

### Weaknesses
1. While WIND presents a promising adaptation of existing noise-based watermarking techniques, it does not fundamentally diverge from the concepts established in Tree-Ring and RingID. The addition of a two-stage detection process is a novel enhancement but builds on the same theoretical foundation of Fourier-based watermarking in noise. The primary innovation lies in the grouping and search-space reduction, which increases efficiency and robustness but does not introduce a fundamentally new approach to noise-based watermarking.

2. The multi-stage approach, while innovative, introduces complexity that may hinder ease of adoption. Managing group identifiers and applying Fourier-based transformations within the initial noise may pose challenges for large-scale implementations. Additionally, as the number of watermarked images grows, the demand for managing extensive initial noise records could impact computational scalability.

### Questions
Please see Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a novel two-stage watermarking framework, named WIND, for images generated by diffusion models. It leverages the initial noise used in the diffusion process as a distortion-free watermarking method. The approach aims to enhance the robustness of watermark detection against both removal and forgery attacks by embedding group identifiers through Fourier patterns, thereby improving the efficiency of watermark retrieval.

### Strengths
The paper presents a novel two-stage watermarking framework, named WIND, for images generated by diffusion models. It leverages the initial noise used in the diffusion process as a distortion-free watermarking method. The approach aims to enhance the robustness of watermark detection against removal and forgery attacks by embedding group identifiers through Fourier patterns, thereby improving the efficiency of watermark retrieval.

### Weaknesses
(-)  Some parts of the paper are overclaimed. For example, in Lines # 78-84, these contents are already addressed in Tree-ring [1], yet the author seems to want to claim it as their contribution. The introduced method is built upon Tree-ring [1] and [2]. However, the introduction does not discuss these works [1-2].  

(-)  The problem of the previous method and the motivation of this work are not clearly delivered. The relationship between the third and fourth paragraphs is confusing and lacks logic. The paper does not adequately highlight the vulnerability of existing methods to attacks that exploit the inconsistency between the distribution of the random noise and the reconstructed noise from watermarked data, which is a key motivation for this work. The consequence of using a lower number of initial noises in previous methods should be stressed.

(-)  The effectiveness of the proposed method may be limited to specific types of diffusion models, and its performance on other diffusion models remains untested.

(-)  Although the paper suggests methods to reduce runtime, the need for searching through a large number of initial noises could still pose challenges in real-time applications, particularly on resource-constrained devices.

Some typos:

For example, in lines 88 and 137, add ( ) for the citations.

### Questions
How does the performance of the WIND framework compare with existing state-of-the-art watermarking techniques when applied to diverse generative models beyond diffusion models?

What specific measures have been taken to ensure that the watermarking process does not compromise the visual quality of the generated images?

Could the authors elaborate on the potential implications of attackers successfully inverting the model and how that might affect the watermarking effectiveness?

### Soundness
2

### Presentation
2

### Contribution
3

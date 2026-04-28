# ODEdit: Blind Face Restoration through Ordinary Differential Equations

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 3, 5

## Abstract
We introduce ODEdit, an unsupervised blind face restoration method. ODEdit operates without necessitating any assumptions about the nature of the degradation affecting the images and still surpasses current approaches in versatility. It is characterized by its utilization of the generative prior encapsulated within a pre-trained diffusion model, obviating the necessity for any additional fine-tuning or any handcrafted loss function. We leverage Ordinary Differential Equations for image inversion and implement a principled enhancing approach based on score-based updates to augment the realism of the reconstructed images. Empirical evaluations on face restoration reveal the robustness and adaptability of our methodology against a varied spectrum of corruption and noise scenarios. We further show how our approach synergise with other latent-based methods to outperform the state-of-the-art Blind Face Restoration methods in our experiments.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a method for blind face restoration using a pretrained diffusion model. The main idea is to formulate the inverse problem using an ODE for image inversion. The method is evaluated on several image restoration tasks involving different amounts of corruptions and noise levels.

### Strengths
* The method is simple.
* The method produces results that are better than the compared methods when plugged with another prior.

### Weaknesses
 * Writing and presentation needs to be significantly improved before we can judge the real contributions.
* The motivation for the method is unclear and hand-wavy.
* Results are not clear: the base method leads to blurry reconstructions.
* The paper is about face restoration, but there's nothing about faces -the only thing about faces is that the base diffusion model is trained on faces.

### Questions
The paper introduces a method for sampling a new image from a diffusion prior that is compatible to an observation. This is done through first estimating a latent code of the distorted image and then resampling a new sample starting from that latent code. The method is simple. The main issue is that the presentation is cumbersome. 

I have the following questions/comments:
1.  **Algorithm 1**. This is the core of the method. It's unclear what does it mean  ODE_SOLVER( . ). Is this running one step of DDIM Eq(9)? This is used twice in the algorithm. The rationale of the algorithm is not clear or explained.

2. **Results of the base methods are blurry**. So this method doesn't seem to be doing a good job. Better results are obtained when plugging the method with another prior (CodeFormer, GFPGAN, etc). So in the end, it's more like with this ODEdit you can get a blurry reconstruction (Average) and then from there another prior is enforced to get a better reconstruction. So in the end, where is the gain coming from? Also it's not clear how this method is applied in conjunction with other methods.

3. **Presentation is cumbersome**. The method is presented in page 6. The first 5 pages are related to some background. However, a big part of the background is irrelevant and other relevant background (like a clean explanation of SDEdit) is not given. This leads to an unbalanced presentation that is hard to follow, and hard to fairly judge the real contributions of the paper.

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
In this paper, the authors tackle the problem of blind face restoration by formulating it as an inverse problem and utilizing a diffusion model as an Ordinary Differential Equations (ODE) solver. Compared to previous methodologies, they achieved a higher Frechet Inception Distance (FID) and provided ample theoretical basis for their approach. Through various experimental results, the paper offers interpretations of the problem and the proposed solution.

### Strengths
- As seen in Table 1, the image quality and Frechet Inception Distance (FID) score are high.
- As observed in Figure 3, the model is robust to strong noise.
- Leveraging the generative capabilities of the diffusion model to achieve high image quality is one of the strengths of this paper.

### Weaknesses
 - There is an identity leakage. Can this be genuinely considered "restoration" of a face? It appears to be generating a face referencing the given corrupted face image.
- As seen in Table 1, the Peak Signal-to-Noise Ratio (PSNR) and Structural Similarity Index (SSIM) are worse than previous works.
- The evaluation seems to be limited to a narrow set of conditions. While the robustness to strong noise is a strength, the paper does not explore the performance of the method under a wider range of degradations, such as varying levels of blur, compression artifacts, or different types of noise. This makes it difficult to assess the general applicability of the proposed approach.

### Questions
If the diffusion model outputs the predicted data instead of the noise, you could potentially utilize face identity loss with a face recognition network. Would this be a feasible naive extension to address the identity leakage problem?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper develops an unsupervised blind face restoration method ODEdit based on a pretrained diffusion model. The ODEdit utilizes score-based updates to augment the realism of the reconstructed images. The experimental results show that ODEdit outperforms state-of-the-art blind face restoration methods in terms of fidelity and realism.

### Strengths
1)	The motivation of this paper is clear. The authors clearly point out that existing BFR methods still struggle to achieve faithful and realistic reconstruction.
2)	The related works is well-structured.
3)	The proposed method is the first unsupervised approach to use ODE-based inversion in Diffusion Models for Image restoration, which is innovate.

### Weaknesses
1) Some parts of the paper are difficult to follow, and additional explanations and clarifications would improve the reader's understanding. Specifically, the description of the score-based updates and how they integrate with the ODE framework could benefit from a more detailed mathematical exposition. Providing a step-by-step breakdown of the algorithm, including the specific equations used in the update process, would significantly enhance clarity.

2) The experiments are not rich and convincing. The experiments lack analysis. For example, Section 4.4 SYNERGY STUDY, the authors only present some figures without any analysis about the results. A more thorough discussion of the observed trends, potential reasons for variations in performance, and a comparison with the expected behavior based on the theoretical framework would strengthen the experimental section. Furthermore, the ablation study does not sufficiently isolate the impact of individual components. A more granular analysis, perhaps by systematically varying parameters within each component and observing the effect on the output, would provide a more nuanced understanding of their contributions.

3) In experiments, the authors do not provide the definition of LDM. In addition, Section 4.3 and 4.4 only verify the superiority of ODEdit but cannot prove the robustness and adaptability of ODEdit as introduced in abstract. The claim of robustness and adaptability requires a more diverse set of experiments. For instance, testing the method on images with varying degrees of degradation, different types of noise, and different facial poses would provide a more comprehensive assessment of its robustness. Additionally, demonstrating the method's performance on a dataset with a wider range of ethnicities and age groups would be crucial for establishing its generalizability.

4) Face ﬁdelity is not only reflected in reconstruction metrics (PSNR,SSIM) but also in face recognition. Maybe the authors should provide some face recognition metrics to further verify the degree of face fidelity. Specifically, incorporating metrics such as cosine similarity or Euclidean distance between feature vectors extracted from a pre-trained face recognition model (e.g., FaceNet) would provide a more direct measure of identity preservation. This is crucial for assessing whether the restored images retain the unique characteristics of the original faces.

### Questions
1)	Compared with existing BFR methods, the proposed method is unsupervised method without any prior. Then, how does this method perform on real-world face images?
2)	The experimental part is insufficient and lack of analysis. The experimental results can only verify the superiority of the proposed method but cannot verify its robustness and adaptability. The authors should provide more convincing experiments and detailed analysis.
3)	The implementation details are missing. The authors should provide the degradation process of this paper in details.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a method to blindly restore face images. Inspired by SDEdit, the proposed method uses ODE to circumvent the injection of extra noise. The provided experimental results show that the proposed method has some advantages over existing methods when the degradation is severe. This paper fails to describe the advantage when replacing SDE with ODE. In addition, some details about the algorithm and experiments are missing.

### Strengths
The provided experimental results show that the proposed method has some advantages over existing methods when the degradation is severe.

### Weaknesses
1. SDEdit can solve plenty of image editing and synthesis tasks. However, the proposed ODEdit is only for face restoration. Can the authors explain the reasons?
2. The advantage that replacing SDE with ODE is not clear. Why should the injection of extra noise be circumvented? Are there any disadvantages when using ODE?
3. It is not clear how can we get Algorithm 1.
4. The experiments lack some details and some comparisons are unfair and incomplete.
(1) What is the testing dataset? The authors seem not to describe it in the manuscript.
(2) Why not compare different methods on real degraded face images?
(3) The synthetic degradations are based on (Hendrycks & Dietterich, 2019) which is not considered in existing methods e.g. CodeFormer. This makes the comparison unfair. Why not compare different methods based on the testing set of CodeFormer?

### Questions
See weaknesses for details.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

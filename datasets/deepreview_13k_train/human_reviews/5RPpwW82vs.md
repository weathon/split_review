# MutualNeRF: Improve the Performance of NeRF under Limited Samples with Mutual Information Theory

- Decision: Reject
- Scores: 3, 5, 5, 5

## Abstract
This paper introduces MutualNeRF, a framework enhancing Neural Radiance Field (NeRF) performance under limited samples using Mutual Information Theory. While NeRF excels in 3D scene synthesis, challenges arise with limited data and existing methods that aim to introduce prior knowledge lack theoretical support in a unified framework. We introduce a simple but theoretically robust concept, Mutual Information, as a metric to uniformly measure the correlation between images, considering both macro (semantic) and micro (pixel) levels.
  For sparse view sampling, we strategically select additional viewpoints containing more non-overlapping scene information by minimizing mutual information without knowing the ground truth images beforehand. Our framework employs a greedy algorithm, offering a near-optimal solution for this task.
  For few-shot view synthesis, we maximize the mutual information between inferred images and ground truth, expecting inferred images to gain more relevant information from known images. This is achieved by incorporating efficient, plug-and-play regularization terms.
  Experiments under limited samples show consistent improvement over state-of-the-art baselines in different settings, affirming the efficacy of our framework.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes MutualNeRF, a method to improve the performance of Neural Radiance Fields (NeRF) when training samples are limited. The authors integrate mutual information theory to develop a unified approach, enhancing NeRF's effectiveness in sparse view sampling and few-shot view synthesis, by modeling uncertainty in semantic space distance and pixel space distance.

### Strengths
- This paper is well written and easy to follow.
- The framework’s design is comprehensive, considering both macro (semantic) and micro (pixel) perspective in the task of sparse view sampling and few-shot NVS.

### Weaknesses
 - **Complex methodology with marginal gains:** This methodology introduces significant complexity, especially in sparse view sampling, involving greedy algorithms and complex mutual information metrics. However, the observed improvements over simpler baselines are relatively minor, which may not justify the added complexity. The use of CLIP embeddings for semantic similarity, while effective, adds another layer of computational cost without a clear demonstration of substantial performance gains compared to simpler distance metrics in view selection. The greedy approach, while intuitive, may also be prone to suboptimal view selections, especially when the mutual information landscape is complex and non-convex.
- **Lack of novelty.** The attempt to address the task of few-shot novel view synthesis through minimization of mutual information between viewpoints have already been explored, especially in CVRP 2022 paper **InfoNeRF: Ray Entropy Minimization for Few-Shot Neural Volume Rendering**. The methodology of this paper seems to be re-interpretation of ideas used in DietNeRF (semantic space) and InfoNeRF (pixel space) within the perspective of mutual information theory. I ask the authors to give a more thorough theoretical comparison between this work and the methods that I have mentioned.

### Questions
See the weaknesses above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a framework to improve the performance of sparse view sampling and few-shot view synthesis by mutual information. For sparse view sampling, the authors first calculate the semantic space distance and pixel space distance, then use a greedy algorithm to select sparse views for training. For few-shot view synthesis, the authors add two regularization terms based on semantic space distance and pixel space distance, to improve the performance of view synthesis. The authors conduct detailed experiments to demonstrate the effectiveness.

### Strengths
The authors demonstrate the effectiveness of both sparse view sampling and few-shot view synthesis. Using mutual information to select views for NeRF is reasonable.

### Weaknesses
1. The motivation for pixel space distance is not clarified. According to Definition 3, the pixel space distance is the expectation of distance between any two points of rays. The authors should clarify the motivation behind Definition 3 since it is important for the following parts. The semantic space distance is fairly reasonable.

2. If my understanding is correct, for the few-shot view synthesis, the authors just added two regularization terms to the NeRF training. However, the relationship between mutual information and few-shot view synthesis is not clear. For sparse view sampling, minimizing mutual information is reasonable.

3. For the few-shot view synthesis, the proposed method needs to evaluate the semantic distance between randomly rendered images and ground truth images. Therefore, this will bring additional training costs. The analysis should be provided.

4. Compared with NeRF, 3D Gaussian splatting is much better in both training and rendering. The authors should conduct experiments based on 3DGS.

5.  There are many typos and grammatical errors. For example, formulas should come with indices.

### Questions
please refer to the weaknesses part.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces MutualNeRF, a framework that enhances Neural Radiance Field (NeRF) performance under limited sample conditions using Mutual Information Theory. It addresses sparse view sampling and few-shot view synthesis by minimizing and maximizing mutual information, respectively. The framework employs a greedy algorithm for viewpoint selection and plug-and-play regularization terms for training.

### Strengths
Utilizes mutual information theory to improve NeRF under limited data.

Proposes a greedy algorithm for strategic viewpoint selection in sparse view sampling.

Introduces efficient regularization terms to enhance few-shot view synthesis.

### Weaknesses
1.	How about using mutual information for 3DGS?
2.	What is the rendering speed of the proposed method, especially when compared with 3DGS?
3.	I suggest that the authors compare or discuss with more methods, like PixelNeRF[A], CR-NeRF[B], and MVSGaussian[C], to fully verify the effectiveness of the proposed mutual information.
4.	Why choose to pick images instead of training as a whole? Are there images that do not belong to the target scene? If we use a fast reconstruction method like 3DGS, training all images won't take much time.

### Questions
Please refer to the weakness part.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes utilizing Mutual Information Theory to enhance the performance of NeRF with limited samples. Mutual information serves as a metric to measure the correlation between images at both macro and micro levels. The macro perspective focuses on correlations in semantic features, while the micro perspective addresses correlations in the pixel space. By incorporating mutual information, the proposed framework effectively addresses challenges posed by sparse view sampling and few-shot view synthesis, resulting in improved performance. Extensive experiments demonstrate the effectiveness of assessing both semantic and pixel space distances.

### Strengths
1. Introducing mutual information to enhance Neural Radiance Field (NeRF) performance is an innovative idea.
2. The experimental results in Table 3 show that the proposed method improves performance across various NeRF frameworks.
3. This paper is well-organized.

### Weaknesses
1. Results in Figure 4 show limited improvement between FreeNeRF and the proposed MutualNeRF; only the zoomed-in sections reveal marginal enhancements, which are still not substantial. The lack of significant improvement in overall image quality raises concerns about the practical impact of the proposed method.
2. The proposed method introduces more complex training requirements and utilizes a large model, CLIP, for assessing semantic space distance, which may impact training time and peak memory consumption. The computational overhead associated with CLIP, especially during training, needs to be carefully considered, and the authors should provide a detailed analysis of these costs.
3. Performance improvements become marginal with more powerful baseline frameworks. For instance, "RegNeRF + Ours" surpasses RegNeRF by 1.28 PSNR, while "FreeNeRF + Ours" outperforms FreeNeRF by only 0.50 PSNR. This diminishing return suggests that the proposed method may not be as effective when combined with state-of-the-art NeRF architectures, limiting its applicability.

### Questions
1) Figure 4 shows that some regions, such as the stairs, are not improved. Why might this be the case? Could this indicate limitations in the Mutual Information design? Specifically, which types of regions can be enhanced by the macro and micro losses? Currently, it is unclear which specific issues the proposed framework addresses. Could the authors provide a more detailed explanation?

2) What are the comparisons in terms of training time and peak memory consumption?

3) Table 3 and Table 4 show that the performance gain for "FreeNeRF + Ours" is marginal. This raises concerns about whether MutualNeRF will improve performance for more advanced backbones, such as Sparsenerf [A] or Sparsenerf combined with FreeNeRF. Could the authors comment on this?

4) Does the proposed macro loss also improve the performance of 3DGS-based methods? If so, did the authors experiment with sparse-view 3DGS splatting methods, such as [B]?

5) What would happen if we applied CLIP as a perceptual loss to support FreeNeRF training?

### Soundness
3

### Presentation
3

### Contribution
2

# RecDreamer: Consistent Text-to-3D Generation via Uniform Score Distillation

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
Current text-to-3D generation methods based on score distillation often suffer from geometric inconsistencies, leading to repeated patterns across different poses of 3D assets. This issue, known as the Multi-Face Janus problem, arises because existing methods struggle to maintain consistency across varying poses and are biased toward a canonical pose. While recent work has improved pose control and approximation, these efforts are still limited by this inherent bias, which skews the guidance during generation.
To address this, we propose a solution called RecDreamer, which reshapes the underlying data distribution to achieve more consistent pose representation. The core idea behind our method is to rectify the prior distribution, ensuring that pose variation is uniformly distributed rather than biased toward a canonical form. By modifying the prescribed distribution through an auxiliary function, we can reconstruct the density of the distribution to ensure compliance with specific marginal constraints. In particular, we ensure that the marginal distribution of poses follows a uniform distribution, thereby eliminating the biases introduced by the prior knowledge.
We incorporate this rectified data distribution into existing score distillation algorithms, a process we refer to as uniform score distillation. To efficiently compute the posterior distribution required for the auxiliary function, RecDreamer introduces a training-free classifier that estimates pose categories in a plug-and-play manner. Additionally, we utilize various approximation techniques for noisy states, significantly improving system performance.
Our experimental results demonstrate that RecDreamer effectively mitigates the Multi-Face Janus problem, leading to more consistent 3D asset generation across different poses.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors of the paper introduce RecDreamer, a text-to-3D generation task that aims to reshape the underlying data distribution of pretrained text-to-image diffusion models to eliminate the Multi-face Janus problem. To achieve this, they develop an auxiliary function derived from the joint distribution expression of the data x and camera pose c. A key component of this auxiliary function is a well-designed, lightweight pose classifier capable of calculating p_t(c|x_0). Extensive experiments demonstrate the effectiveness of RecDreamer in eliminating the Janus problem.

### Strengths
1)	The authors present an insightful analysis of the emergence of the multi-face Janus problem in text-to-3D generation. Building on their analysis, they offer a solid theoretical framework on reshaping the underlying data distribution of pretrained text-to-image diffusion models.
2)	The design of the pose classifier appears to be innovative, with clear and comprehensive details provided in the appendix.
3)	The qualitative and quantitative results of RecDreamer demonstrate its state-of-the-art performance, as validated in their experiment section.

### Weaknesses
1) The evaluation of the paper is limited. Initially, all experiments are only tested on 22 prompts from the original DreamFusion gallery, while previous works typically use over 40. The prompt list is also not provided in the appendix, which compromises the reproducibility of the experiments. Furthermore, the absence of recent open-sourced baseline methods that focus on addressing the Janus problem, such as ESD1 and JointDreamer2, is notable. The choice of prompts is particularly concerning as it is unclear if these prompts are representative of the broader text-to-3D generation task. The lack of a diverse prompt set makes it difficult to assess the generalizability of the proposed method. Moreover, without a prompt list, it is impossible to verify the claims of the paper or reproduce the results, which is a major issue for scientific rigor.
2) The authors introduce the concept of the "joint distribution expression of the data and camera pose," but provide limited explanation of the practical meaning of such a distribution. Also, the use of a rather discrete 4-views to represent the camera pose distribution does not appear to be meaningful. More ablation studies should be conducted. The joint distribution's practical implications are unclear, particularly how it is used to guide the optimization process. The use of only four discrete views (front, back, left, right) seems overly simplistic and may not adequately capture the continuous nature of camera pose variations. This discretization could potentially limit the method's ability to generate consistent 3D models from arbitrary viewpoints. The lack of ablation studies on the number of views and their specific configurations further weakens the analysis.
3) The authors state that the image templates are "user-provided" in line 317 of the main manuscript, which seems unusual. It is not feasible for users to provide consistent multi-view templates for any text prompts. The requirement for user-provided templates raises significant practical concerns. It is unrealistic to expect users to generate consistent multi-view images for arbitrary text prompts, especially given the challenges of maintaining view consistency across different image generation models. This dependence on user-provided templates could severely limit the usability and accessibility of the proposed method.

### Questions
I would appreciate it if the authors could provide a clear explanation of the second and third weaknesses. I am open to revising my score if the author addresses this concern.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper tackles the Janus problem with score distillation-based text-to-3D generation via debiasing the camera pose distribution of the pre-trained text-to-image diffusion model. Specifically, the authors derive an auxiliary function that rectifies the pose distribution induced by the original image distribution to a targeted distribution (e.g. uniform). Consequently, the score distillation rule yielded from the debiased image distribution, termed uniform score distillation (USD), is derived as a combination of the variational score distillation plus the “score” of the auxiliary function. The auxiliary rectifier can be computed with a pose classifier and a running estimator of the pose distribution over the Gaussian perturbed image distribution.

### Strengths
+ This paper offers a distinctive approach to addressing the Janus problem in score distillation-based text-to-3D generation. Its central argument asserts that the pre-trained image distribution is intrinsically biased toward canonical views, causing the resulting 3D content to exhibit this same bias—manifesting as the Janus problem in practical applications. This perspective contrasts with most existing score distillation methods, which often assume that the 2D pre-trained distribution is ideal and strive to align the view distribution with it more closely.
+ The proposed method is both novel and theoretically grounded, offering a unified and principled approach to debiasing that integrates seamlessly into current score distillation frameworks. The debiasing mechanism is based on solid theoretical underpinnings yet is surprisingly straightforward to implement. All derivations appear correct. The proposed estimation for the otherwise intractable auxiliary rectifier term is thoughtfully designed, with each step justified through theoretical insight.
+ The paper is dense and well-written, with thorough engineering details, including but not limited to an efficient pose classifier, a running estimator of the pose distribution, and improved training techniques. The results are extensive: beyond fundamental qualitative outcomes, the paper includes numerous validation experiments in the appendix, demonstrating the efficacy of each design element.

### Weaknesses
 - The quantitative results in this paper are somewhat limited. While I recognize the lack of a standard metric for evaluating generated 3D results, a few commonly used measures, such as the CLIP score demonstrated in SDS [1], could still be applied. Given the high degree of randomness often seen in score-distilled outputs, it would also be beneficial to assess the method using human evaluation, specifically by measuring the success rate of Janus-free results [2].

- Another limitation is that the proposed USD appears to require reference images from various view angles, which may be impractical when the prompt is abstract or imaginary and lacks similar images on the shelf. The authors may wish to discuss potential solutions to this constraint.

- The paper also overlooks several related works in the text-to-3D generation literature. While the field is vast, I suggest including a more comprehensive review. Some key omissions in the current version include: [3,4,5,6]

- Many state-of-the-art approaches currently rely on training or fine-tuning generative models on 3D data. It would be interesting to show whether score distillation with the rectified distribution could largely match the performance of the distribution fine-tuned with extra data. I’d also suggest demonstrate whether the proposed USD can even enhance these training-based methods.

### Questions
1. Why is the VSD loss in Eq. 14 denoted as $L’_{VSD}$ instead of $L_{VSD}$​ as in Eq. 9?

2. Additionally, I wonder whether modifying the camera sampling distribution in VSD to use the estimated $p(c∣y)$ could yield similar or complementary effects in mitigating Janus problems.

### Soundness
4

### Presentation
4

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
This paper proposes to rectify the biased pose distribution, ensuring the pose variation is uniformly distributed, to solve the Janus problem. A uniform score distillation module is introduced accordingly.

### Strengths
1. This paper rectify the biased distribution to uniform distribution by reweighing the density of original distribution.
2. A corresponding uniform score distillation process is designed to improve the consistency.

### Weaknesses
1. More comparison with baselines is needed, such as [1].
2. Runtime analysis is missing, the sampling time per image is expected.

### Questions
Can the authors report the runtime per sample of your method and other baselines to ensure the completeness of comparison?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper presents RecDreamer, an approach to address the Multi-Face Janus problem in text-to-3D generation, which arises from geometric inconsistencies across different poses of 3D assets. The authors propose a technique called uniform score distillation, which modifies the underlying data distribution to ensure pose variation follows a uniform distribution. This is achieved by a rectification process that adjusts the density distribution, facilitated by a training-free classifier that estimates pose categories. The approach aims to eliminate biases towards a canonical pose and improve geometric consistency without compromising rendering quality. The experimental results demonstrate the effectiveness of RecDreamer in achieving consistent 3D asset generation across various poses.

### Strengths
* An approach to address data bias issue: The paper introduces a solution to a well-known problem in text-to-3D generation by addressing the biases in data distribution through uniform score distillation.
The use of a training-free classifier to estimate pose categories is an efficient and novel aspect of the approach, avoiding the need for additional training.

* Comprehensive Methodology:
The integration of reverse Kullback-Leibler divergence in the score distillation framework is well-articulated, allowing for the seamless incorporation of the rectified distribution.
The method's ability to maintain rendering quality while resolving the Multi-Face Janus problem is a significant advantage.

* Experimental Validation:
The paper provides thorough experimental validation, demonstrating the method's effectiveness in improving geometric consistency across different poses.
Additional experiments on 2D images and a toy dataset further substantiate the robustness of the algorithm.

* Broader Applicability:
The potential applications of the pose classifier beyond the primary task highlight the versatility and potential impact of the proposed approach.

### Weaknesses
 * Complexity and Scalability:
 The introduction of an auxiliary function and classifier adds complexity to the method. Details on computational efficiency and scalability in large-scale applications are lacking. The use of a UNet for rectification, while effective, introduces significant computational overhead due to the backpropagation through this network, which is not fully addressed in the current manuscript.

* Generalization:
While the method is effective for the specific problem addressed, there is limited discussion on its generalizability to other types of biases or different domains within 3D generation. The approach relies on a classifier to identify pose categories, and it's unclear how this would adapt to biases that are not easily categorized or require continuous rather than discrete labels.

* Quantitative Metrics:
The paper would benefit from a more detailed presentation of quantitative metrics used to evaluate geometric consistency and rendering quality, alongside comparative analysis with existing methods. The current metrics, while relevant, lack a thorough explanation of their implementation and how they specifically capture the nuances of geometric consistency beyond simple pose classification. For example, the entropy-based metric needs more justification in terms of its sensitivity to subtle geometric inconsistencies.

* Background section is too long. This paper put many equations in Sec.2, but it actually did not provide strong support to the proposed uniform score distillation. Some space could be saved to explain Sec. 3.3.

### Questions
* How does RecDreamer handle variations in complex textures or intricate details that might not be directly related to pose?
* Can the proposed method be extended or adapted to address other biases in text-to-3D generation beyond pose inconsistency?
* What are the computational requirements for implementing RecDreamer, and how does it perform in terms of efficiency compared to baseline methods?

### Soundness
2

### Presentation
3

### Contribution
2

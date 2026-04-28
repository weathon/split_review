# Geometric Neural Process Fields

- Decision: Reject
- Avg Score: 5.33
- Scores: 3, 6, 6, 6, 5, 6

## Abstract
Denoising diffusion models have proven to be a flexible and effective paradigm for generative modelling. %Tasks such as time series prediction or weather forecasting are naturally described as distributions over function spaces.
Their recent extension to infinite dimensional Euclidean spaces has allowed for the modelling of stochastic processes. %prediction and weather forecasting applications.
However, many problems in the natural sciences incorporate symmetries and involve data living in non-Euclidean spaces.
In this work, we extend the framework of diffusion models 
to incorporate a series of geometric priors in infinite-dimension modelling.
We do so by a) constructing a noising process which admits, as limiting distribution, a geometric Gaussian process that transforms under the symmetry group of interest, and b) approximating the score with a neural network that is equivariant w.r.t.\ this group.
We show that with these conditions, the generative functional model admits the same symmetry.
We demonstrate scalability and capacity of the model, using a novel Langevin-based conditional sampler, to fit complex scalar and vector fields, with Euclidean and spherical codomain, on synthetic and real-world weather data.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes Geometric Neural Processes (GeomNP), a newl framework for enhancing the generalization of Implicit Neural Representations (INRs) in probabilistic neural radiance fields, enabling efficient adaptation to new 3D scenes with limited context images. By framing the problem probabilistically, the authors introduce geometric bases that mitigate information misalignment between 2D observations and 3D structures, allowing for better aggregation of locality information and high-frequency detail capture. Additionally, the incorporation of hierarchical latent variables facilitates modulation of the INR function across multiple spatial levels, leading to improved generalization performance. Experimental results on novel view synthesis tasks demonstrate the effectiveness of GeomNP, which not only excels in 3D applications but also seamlessly extends to 2D INR generalization problems, effectively capturing uncertainty in the latent function space.

### Strengths
- The work effectively frames the generalization of Neural Radiance Fields (NeRF) as a probabilistic modeling problem, allowing for the integration of uncertainty and enabling the model to adapt to new scenes with limited observations. 

- The introduction of geometric bases addresses the challenge of information misalignment between 2D context images and 3D structures. 

- The incorporation of hierarchical latent variables allows for effective modulation of the INR function at multiple spatial levels

### Weaknesses
 - Missing comparison with state-of-the-art generalizable approaches [1,2]. The PixelNeRF method is published on ICCV 2021, which is a very old baseline.

- I'm confused by the goal of this work. It seems that the method tries to train a generalizable INR that can leverage multiple input signals, but the experiments largely focus on predict INR from a single-signal (like a single view). To me, these two are different topics (generation v.s. reconstruction), and INR is designed to correctly store signal in the neuron (which is more like a reconstruction tool). If the author clarified the proposed method as a reconstruction tool, they should test the generalizable INR under enough observations and compare it with [1,2], rather than single-view input. If the authors clarified the proposed method as a generative model, which is reasonable since the proposed model is a probabilistic model, they should include other state-of-the-art generative models [3,4,5] in the comparisons.

- In line 100, it says "these methods (Kosiorek et al., 2021; Hoffman et al., 2023; Dupont et al., 2021; Moreno
et al., 2023) do not consider structural information and the information misalignment between 2D observations and 3D NeRF functions, which our approach explicitly models." The authors should also include experimental evidence to support this statement. Furthermore, the claim that these methods do not consider structural information is not entirely accurate, as some of them implicitly capture structural information through their network architectures and training procedures. A more nuanced discussion of how these methods handle or fail to handle structural information is needed.

### Questions
NA

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
4

### Summary
This paper proposes a method for Implicit Neural Representation (INR) generalization, i.e., efficient 3D representation of the observed scene from a few observations. Previous approaches used gradient-based meta-learning, which adapts to new scenes with few optimization steps or directly predicts the weights of the MLP. However, these methods are deterministic and not probabilistic.

This work proposes a probabilistic radiance field generalization with Geometric Neural Processes (GeomNP):

1. They formulate radiance field generalization using a few views as a probabilistic modeling problem.
2. They introduce geometric bases to aggregate local information to the 3D point.
3. Further, they introduce hierarchical latent variables for better generalization to new scenes.

### Strengths
1. **Paper-Writing and Presentation**: The paper is well-written and presents its content clearly and comprehensibly, making it easy to follow.

2. **Geometric Bases module**: The authors introduce a method that models the structure of an object using a mixture of 3D Gaussians. A learnable encoder based on a transformer architecture predicts the parameters for these Gaussians. This approach leverages the continuous properties of Gaussians. Table 3 shows an ablation that analyzes the sensitivity to the number of Geometric Bases. Table 4 highlights the significant impact of the proposed Geometric Bases. 	

3. **Experimentation on 2D signals**: The proposed method can be seamlessly extended to 2D signals. The authors demonstrate its effectiveness on image regression tasks (Section 4.2).

### Weaknesses
1. **Missing Comparison with several baselines**: The proposed method solves novel-view synthesis given few images. However, it does not compare with some popular methods such as Splatter-Image, pixelSplat, MVSplat. These methods, which leverage explicit 3D representations like Gaussian splats, have shown impressive results in novel view synthesis and should be included for a comprehensive evaluation. Further, it will also be interesting to compare this method with LRM, a feedforward method to generate 3D from a single image, to understand its performance in extremely limited view settings. The absence of these comparisons makes it difficult to assess the relative strengths and weaknesses of the proposed approach.

2. **Evaluation on popular 3D datasets**: Recent methods such as Splatter-Image show comparisons on Objaverse, Google-Scanned Objects and Co3D datasets. These datasets are vast and are better benchmarks to test the generalization capabilities. The current evaluation is limited to relatively small datasets, and it is unclear how well the proposed method would scale to more complex and diverse scenes. Evaluating on these larger datasets would provide a more robust assessment of the method's generalization capabilities.

3. **Training time comparison with SOTA methods**: The authors should also compare the training time on a standard dataset for single image-to-3D task. Also, the authors should present the number of parameters in the proposed method. This information is crucial for understanding the computational cost of the method and comparing it with other approaches. Without this information, it is difficult to assess the practical feasibility of the proposed method.

### Questions
1. This is a suggestion to the authors. The authors should explicitly highlight the limitations of previous methods and clarify how their approach differs from existing ones. Presenting this information in a comparative table would enhance the clarity and significantly improve the quality of the manuscript.

2. The authors should compare with more baselines and present results on other datasets. Please refer to comment 1 and 2 in the "Weaknesses" section.

### Soundness
3

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
4

### Summary
- The paper tries to solve Implicit Neural Representation generalisation in a probabilistic manner and takes into account uncertainty so that the model can infer with limited context information.
- The authors use geometric bases to provide 3D information and latent variables to generalize well to new scenes.
- To show the effectiveness of the proposed method, the authors show their results on Shapenet and DTU scenes. Additionally they also show 2D image regression.

### Strengths
- The paper uses Geometric Basis to maintain alignment between 2D context view and 3D target points and induce prior structure.
- Geometric neural processes with hierarchical latent variables are used to encode spatial specific information. 
- The method shows superior results in Shapenet and DTU MVS dataset.  
- The paper is presented well and easy to follow.

### Weaknesses
 - The authors have only compared with pixelNeRF for DTU-MVS dataset. There are many other SOTA methods. Comparison with more recent methods is necessary.
- Since the method uses a probabilistic approach, it can be resource-intensive and may  require more memory and computation compared to simpler, deterministic NeRF models. It's necessary to compare the extra computational cost compared to other methods that use probabilistic approach (maybe comparison with baseline methods shown in Table 1.)
- Although the method is extended to 2D INR generalization, the probabilistic framework may introduce unnecessary complexity for simpler 2D tasks where less resource-intensive models could achieve comparable results.

### Questions
- Can the method be applied to Gaussian splatting based representations to solve similar tasks?
- How does the diversity of training scenes affect generalization? Will the performance drop drastically for scene types not represented in the training data, or does the probabilistic framework help mitigate such issues?
- What is the effect of  partial occlusions or noise on GeomNP? Can it account for such situations without significant drop in performance?

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
3

### Summary
This paper proposes a probabilistic framework for generalizable neural fields. The key idea is to use learn a generic prior, mapping to a low-dimensional structured space, called Geometric Bases, which then can be used to modulate a neural process. The authors propose hierarchical modulation, i.e. providing both local and globally averaged latent features to the modulation layers; thus, providing global and local information which helps both the forward predictions and also the generalization capabilites. 
The authors specifically focus the downstream application of sparse-view NeRF reconstruction and showcase the benefits of the proposed method on the ShapeNet and DTU datasets.

### Strengths
I really like the idea of deriving a generic probabilistic framework for neural field reconstruction, which could also be applied to other domains. The probabilistic formulation allows direct uncertainty estimation, which can be used in downstream applications.

### Weaknesses
Although the idea is interesting, I believe there are multiple flaws in the papers, which should be addressed before acceptance:
* **W1 -** The provided experiments do not clearly demonstrate the claimed contributions. I believe the following questions need to be answered:
  * How wel does it generalize? What happens in case of cross-category evaluation? Can it find geometric priors for similar categories?
  * Qualitative results for the hierarchical ablation would be appreciated
* **W2 -** Key related work is missing and should be discussed. Probabilistic NeRF has already been introduced in recent years and I think it would be important to compare against these recent methods, e.g., [DiffRF 2023](https://arxiv.org/abs/2212.01206), [Tewari et al. 2023](https://diffusion-with-forward-models.github.io/). Furthermore, the method is related to [PointNeRF 2022](https://xharlie.github.io/projects/project_sites/pointnerf/index.html) as well, which should be discussed. 
* **W3 -** The writing quality could be further improved. The main goal of the paper is not straight: the paper mostly focuses on a single downstream application, although the claims are more generic. If the method could be used in a generic setting, then I think more focus should be put on further downstream applications as well. 
* **W4 -** L.485: The ablation about the geometric bases is not entirely valid if evaluated on 64x64 images. This is too low resolution. 
* **W5 -** L.522: The experimental setup for the uncertainty estimation is not described, so it is not clear what was the input making it difficult to evaluate whether the predicted uncertainty is reasonable. Being a probabilistic framework, the method used for estimating uncertainty should be described in more details. 

Additional smaller weaknesses:
* **W6 -** L.043: Erkoc et al. 2023 is incorrectly classified as deterministic model, since it uses a diffusion approach to generate neural fields. 
* **W7 -** It would be great to highlight the best PSNR in Tab. 4.

### Questions
**Q1 -** In L.420: How exactly is the method incorporated into PixelNeRF?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper uses NeRF as an example to study the Implicit Neural Representation (INR) generalization problem. The main idea is to formulate INR generalization in a probabilistic manner. Beyond the probabilistic NeRF generalization framework, the paper introduces geometric bases. Each geometric basis consists of a Gaussian distribution in the 3D point space and a semantic latent representation, which are learned from the context sets (or observed images of objects). The paper also proposes improvements to the Geometric Neural Process (GeomNP) by incorporating hierarchical latent variables, which integrate 3D information and modulate INR functions at different spatial levels.

### Strengths
$\textbf{Idea}$:

The entire geometric neural process (GeomNP) framework is novel. While leveraging 3D priors (referred to as Geometric Bases in this paper) to enhance novel view synthesis is a common approach, this paper uses Gaussians as the 3D representations of observed images, in contrast to related works like MVSNeRF, which utilize volume-based 3D priors. Additionally, considering hierarchical latents for improved NeRF learning presents a promising avenue for further exploration.

$\textbf{Experiments}$:
1. The GeomNP method achieves good quantitative results on both ShapeNet objects and the DTU MVS dataset.
2. The ablation study is informative, examining key components such as the geometric bases and hierarchical latent variables.

### Weaknesses
$	extbf{Clairty}$:

I haven't closely followed NeRF research in the past year, but I feel that the clarity of this paper could be improved.

1. Some technical terms in this paper are misleading, which may hinder clarity. For example, the paper refers to camera rays and their corresponding 2D pixels in image space as "2D context sets." Using the terms "camera rays" and "2D pixels" consistently would be more common and clearer for readers. I found the term "context sets" confusing while trying to understand the paper. Additionally, other phrases like "3D NeRF fusing," "target sets," "amortizing the probabilistic model," and "modulating a neural network" could also benefit from clearer definitions.

2. I have a good understanding of the formulation and implementation of NeRF and 3DGS. However, I think the modulation layer needs clearer presentation, as it involves detailed modifications. It would be helpful for the paper to include more detailed illustrations or a pseudocode block to explain the training and inference processes of GeomNP.

3. Is the 2D part pre-trained on a variety of different objects? If so, please clarify this further.

$	extbf{Significance}$:

The significant advancements in NeRF research have been extensively explored over the past four years. While the new framework introduced in this paper is complex and includes detailed modifications, the experimental results are not particularly compelling. For example:

1. The paper should discuss and compare its findings with other NeRF generation works, such as IBRNet and MVSNeRF, as well as their subsequent developments.

2. The studies on ShapeNet objects and the DTU MVS dataset do not fully demonstrate the high-frequency learning capability. It would be beneficial to conduct evaluations on the NeRF synthetic and MipNeRF-360 datasets as well.

3. The paper should include more multi-view results for qualitative comparisons. Currently, it reports only single novel view synthesis for each object.

4. It would be helpful to present individual results for each DTU object.

5. 
In Table 4, which subset of Lamps is used?

### Questions
Please respond to the concerns regarding "Clarity" and "Significance" above.

### Soundness
3

### Presentation
2

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
This paper resolves the generalizable implicit representation task by considering it as a probabilistic manner. It infers the distribution of NeRF function on limited amount of context data. Experiments show that the proposed GeomNP can improve the representation ability compared to the deterministic representation thanks to the specific designs of this method such as hierarchical feature vectors.

### Strengths
1. This paper formulate generalizable NeRF as the probabilistic problem, which is interesting and novel. 
2. This paper introduce the learning-based geometric basis to align the features between 2D and 3D context.
3. The writing of the manuscript is easy to follow and understandable. The authors organize the structures of it in a reasonable way.

### Weaknesses
1. There are some of 2024 SOTA works related to the generalizable NeRF representations, which are not included in the Sec 2. In contrast, all of works introduced in Sec. 2 of this paper are from 2023 or earlier, which makes the related works a little outdated. Here I suggest two relative works to let the author to discuss the differences and similarities between these methods and the proposed GeomNP.

  (1) GPF: "Learning robust generalizable radiance field with visibility and feature augmented point representation." ICLR2024
GPF aggregate hierarchical local geometry information from sparse unseen views to a point scaffold. This concept is similar with two main components of this paper, i.e. hierachical vector features and geometric bases.

  (2) GeFu: "Geometry-aware Reconstruction and Fusion-refined Rendering for Generalizable Neural Radiance Fields." CVPR2024
GeFu benefits from the feature fusion of 2D and 3D modalities, which is to some extent relevant to the fusion of 2D context view and 3D target points.

Therefore, I recommend that the author discuss and investigate the above two approaches in Sec. 2. If possible, it is recommended that experimental comparisons be made in Sec 4.

2. I think this method uses a kind of implicit neural geometric base to describe the local geometry features In Eq. 3, it is used for generating the distribution of the NeRF function. Some of the other works are inclined to adopt explicit geometric descriptors for the same purpose. For example, GPF aggregates sparse observations of unseen scenes into a point scaffold, ENeRF and NeuralRay reproject rays onto these new observations to obtain 2D-3D consistent features. Could the author discuss which types of geometric descriptors (implicit or explicit) are superior?

3. I think the author should provide some videos to prove the effectiveness of the proposed method. Supplementary videos are necessary for 3D reconstruction, novel view synthesis, or related tasks.

4. The author only makes comparisons with PixelNeRF on super sparse view generalization, but there are still many of other off-the-shelf sparse view reconstruction methods, such as Sparsenerf, and Freenerf.
Could the author compare their methods with more improved baselines? Actually, PixelNeRF is somewhat out-of-date.

5. If more views are used, can the proposed method achieve similar or better performance than these conventional generalizable NeRF methods, such as GPF, ENeRF, GeFu etc?
My concern is that the presented results figures in the main text are not amazing.

### Questions
See above.

### Soundness
2

### Presentation
3

### Contribution
2

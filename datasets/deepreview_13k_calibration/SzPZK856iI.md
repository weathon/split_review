# Text-to-Image Rectified Flow as Plug-and-Play Priors

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 5, 6

## Abstract
Large-scale diffusion models have achieved remarkable performance in generative tasks. Beyond their initial training applications, these models have proven their ability to function as versatile plug-and-play priors. For instance, 2D diffusion models can serve as loss functions to optimize 3D implicit models. Rectified Flow, a novel class of generative models, has demonstrated superior performance across various domains. Compared to diffusion-based methods, rectified flow approaches surpass them in terms of generation quality and efficiency. In this work, we present theoretical and experimental evidence demonstrating that rectified flow based methods offer similar functionalities to diffusion models — they can also serve as effective priors. Besides the generative capabilities of diffusion priors, motivated by the unique time-symmetry properties of rectified flow models, a variant of our method can additionally perform image inversion. Experimentally, our rectified flow based priors outperform their diffusion counterparts — the SDS and VSD losses — in text-to-3D generation. Our method also displays competitive performance in image inversion and editing.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The submitted work propose a way of utilizing rectified flow models a prior, that implies the internal knowledge of the model as in the form of an objective. Throughout the manuscript, the authors propose three different algorithms in this regard, where they are named as RFDS (Rectified Flow Distillation Sampling), iRFDS (inverse RFDS) and RFDS-Rev (RFDS Reversal). While discussing the analogy between the SDS (Score Distillation Sampling), which serves as a prior for models trained with score-matching objective (e.g. diffusion models), they demonstrate how these algorithms can be utilized as a loss objective reflecting the knowledge of the rectified flow model and the image inversion & editing task. Furthermore, the authors propose RFDS-Rev algorithm as the improved version of the baseline algorithm (RFDS).

To demonstrate the effectiveness of the set of the proposed algorithms, authors show the effectiveness of them on a variety of tasks. Initially, the authors demonstrate how does the proposed method improve over SDS in diffusion models in terms of generation quality. Following, they illustrate the applications of the proposed algorithms in inversion based tasks (e.g. image editing) and text-to-3D generation with a 2D prior from rectified flow models. For all of the demonstrated algorithms, authors provide qualitative and quantitative results that shows the effectiveness of the proposed framework.

### Strengths
- The paper proposed the first algorithm that utilizes rectified flow models as priors, to both enable implicit information encoded in the rectified flow model and inversion based image editing with such models.
- In addition to the baseline method provided, authors also propose an extension named RFDS-Rev, that improves over the baseline objective RFDS, that combines the algorithms proposed together and promises improved generation quality.
- Proposed method showcases satisfactory results on Text-to-3D generation, which shows the effectiveness of the proposed method over providing a prior on multiple views.
- Authors introduce a simplifying assumption enabling to efficiently using rectified flow models as priors, by simplifying the generator Jacobian. This serves as a modification for improving the efficiency of the proposed method.
- The paper provides sufficient amount of experiments demonstrating the effect of the design decisions made on the algorithms, which also serve as insightful observations (number of steps, effect of the Jacobian).

### Weaknesses
 - In the examples provided, there is a significant saturation effect on the provided results (see Fig. 5, row 2 and Fig. 6, examples from SD3). It is unclear if that effect is a result of the proposed method or a property of the rectified flow models. 
- While the image editing results seem semantically correct, there seems to be significant changes in the provided images (See Fig. 5) compared to methods such as Null-text Inversion. Despite the fact that the authors provide a user study and CLIP score based comparisons, the faithful reconstruction property is not discussed and it is unclear that how successful the provided approach is. The changes introduced during editing, while semantically aligned, appear to alter substantial details of the original image beyond the intended edits. This raises concerns about the method's ability to preserve non-edited content.
- In generation results provided in Fig. 7 (fox example), the generation results seem degraded in terms of quality and provides artifacts. It also seems that RFDS in general produces these artifacts. If the alternative method RFDS-Rev recovers those, authors need to provide related discussions and examples on its performance on the performed tasks (such as inversion based editing). If this algorithm is not applicable for such a scenario, it should be mentioned as a limitation of the method.

### Questions
- The authors are strongly encouraged to discuss more on the quality degradation issues mentioned in weaknesses. If this is an effect of the proposed algorithm, it should be discussed throughly. 
- Authors should consider  extending the quantitative results on the reconstruction properties of the iRFDS. Despite the fact that the current evaluation assesses the edit in terms of success in reflecting the semantics, the qualitative results seems that the algorithm fails in preserving edit independent details.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes to use rectified flow for SDS instead of diffusion models.

The propose method has three components:
* Rectified flow distillation sampling (RFDS) = typical SDS but with rectified flow
    * Equations are the same with SDS except having *flow residual* instead of denoising loss
    * It uses random noises to compute the *flow residual*.
* Optimizing the *noise* (iRFDS) with the same flow residual
* Full algorithm (RFDS-Rev) with RFDS and iRFDS
    * iRFDS starting from a random noise
    * RFDS with the optimized noise

iRFDS and RFDS-Rev are applicable to diffusion models, especially with classifier-free guidance.

### Strengths
1. This paper tackles a long-standing problem: SDS. SDS with rectified flow is not good enough and the proposed method generates sharp results.
2. The proposed method is easy to understand and mostly sound.
3. The proposed method is generalizable to a wide range of flow-based methods.
4. Preliminary is thorough enough to provide the knowledge base.
5. Figure 2 greatly helps understanding the intuition of RFDS-Rev.
6. Experiments are well-organized from 2D to 3D.

### Weaknesses
1. Subsection 3.2 should provide the theoretical justification for the reason why optimizing the noise helps RFDS.
2. Choice of the competitors for text-based image editing is not sound because it covers only inversion variants. Answering following questions may improve soundness: Why should we compare only with inversion variants? Why prompt-to-prompt variants (e.g., DDPM inversion + P2P) should be ignored?
3. The text-to-3D results still suffer from Janus problem. Discussion in this direction would enrich the paper.
4. Question of the user study is ambiguous: Given the source image, "a boat in a river", which method is better by changing boat -> rock? There are different aspects of being "better", e.g., consistency except the boat, and they should be separately evaluated.
5. Results of generated 3D assets (Figure 4) should be rendered in multiple views to be evaluated. Supp. materials have viewpoint-varying videos. Mentioning a Supp. would suffice.
6. Introduction is verbose. It would be clearer if non-essential sentences are removed.

Misc.

L169 using pretrained rectified flow models v_phi -> using a pre-trained rectified flow model v_phi

### Questions
1. Why do the bottles change across n=1 and n‎ = 2 while boots stay the same in Figure 6? The only difference I catch between boots and bottles is 2D and 3D.
2. Why does the network Jacobian harm the results?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper uses the SOTA rectified-flow-based model as plug-and-play priors to lift the text-to-2D model into a text-to-3D model, with RFDS and RFDS-Rev. By removing the Jacobian of the rectified flow network, RFDS can generate meaningful images or 3D objects given text conditions. RFDS-Rev iteratively applies iRFDS for flow reversal to determine the original noise, and RFDS for knowledge distillation to refine the input.

### Strengths
1. The paper analyzes the refined process of the rectified flow.

2. Using the rectified flow as the priors is interesting.

3. The experiments are sufficient.

### Weaknesses
 * Writing needed to be improved, especially, from Lines 100-107, which is important but the logic is somewhat unclear.

* The focus of the paper is a little confusing, including Image inversion, editing, and text-to-3D generation. In my view, text-to-3d must be the key contribution as it use the 2D model as the priors.

* What is the difference between RFDS Loss and SDS loss. It seems that RFDS is the version of the flow-based model.

* What is the speed impact of the iterative application of iRED in REDS-rev?

### Questions
See weaknesses

### Soundness
3

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
This paper presents a framework that distills knowledge from the pre-trained text-to-image rectified flow models, which serve as a strong prior and apply to various downstream tasks such as image editing and text-to-3D. Similar to ‘Score Distillation Sampling’ (SDS) loss, authors propose a novel loss termed ‘Rectified Flow Distillation Sampling’ (RFDS) that is fully compatible with Rectified Flow models and partially with Diffusion models. Furthermore, they suggest iRFDS and RFDS-Reversal, the variant of their proposed loss, that can be applied to the image inversion and RFDS-based enhancement mechanism, respectively. The authors conducted extensive experiments to validate the efficiency and efficacy of their method.

### Strengths
1. The proposed RFDS, which poses similarity to SDS, presents an effective way to adapt pre-trained Rectified Flow models to tasks such as text-to-3D. This contribution is fundamental since there is a growing trend toward Rectified Flow models in the community.

2. The authors conducted extensive experiments with various Rectified Flow/Diffusion baselines, which proves the versatility and efficacy of the proposed RFDS framework.

3. The proposed method shows solid performance and faster convergence speed compared to baselines, which is noticeable.

4. This paper is easy to follow and comprehend.

### Weaknesses
1. As far as my understanding is correct, RFDS-Rev redirects the gradients (velocities) of the rendered image to points close to the same data distribution mode given different noisy samples to handle common issues such as blurriness that could arise from averaging different-mode directing gradients. For this reviewer, it is unclear how iRFDS can enhance the performance of models without Reflow since these models would not have perfect straight-line paths. Approximated starting points (initial noise) would not guarantee a ‘static position’ within the noise distribution, and I think the more detailed explanation or empirical evidence would further make this work concrete. Specifically, the paper lacks a clear explanation of how the inversion process would behave when the underlying flow is not perfectly rectified, potentially leading to unpredictable results. The assumption of a static position in the noise distribution seems overly simplistic, and a more rigorous analysis of the impact of non-ideal flow fields on the inversion process is needed.

2. The results in image editing (Fig.5) do not seem convincing since semantics that are supposed to remain still are also being changed, such as the global contrast of the image, textures, and object shapes. This makes me doubtful if the proposed iRFDS can indeed optimize the valid initial noise given data. Maybe a simple reconstruction test (from optimized noise to the original data) would further provide a concrete evaluation. The changes observed in the image editing examples are substantial, affecting not only the intended edits but also the overall structure and appearance of the image. This raises concerns about the stability and reliability of the inversion process, and a reconstruction test would help to quantify the degree to which the original image can be recovered from the optimized noise.

3. I think the explanation of faster convergence speed compared to SDS/VSD is weak since it is an important property in the field of 3D generation methods using diffusion priors. Further elaboration or evidence of this feature would help readers fully comprehend their work (e.g., comparing convergence curves with respect to the number of iterations or wall-clock time). The claim of faster convergence is not sufficiently supported by the current analysis. A comparison of convergence curves, showing the loss values over iterations, would be more convincing. Additionally, reporting wall-clock time would provide a more practical measure of the method's efficiency.

4. Weak baseline methods. While I appreciate the paper's contribution (the first attempt to use Rectified Flow as priors) and the results are quite promising, baseline methods are rather weak (DreamFusion and VSD are quite outdated at the moment). It would be great if the authors compared against state-of-the-art text-to-3D methods, e.g., LucidDreamer [1], DreamCraft3D [2] or even GaussianDreamer [3] using different 3D representations.

### Questions
Please see the weakness section.

### Soundness
2

### Presentation
3

### Contribution
3

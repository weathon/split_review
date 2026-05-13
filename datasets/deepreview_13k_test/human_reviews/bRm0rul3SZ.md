# Unpaired Panoramic Image-to-Image Translation Leveraging Pinhole Images

- Decision: Reject
- Scores: 5, 3, 5, 5

## Abstract
In this paper, we tackle the challenging task of unpaired panoramic Image-to-Image translation (Pano-I2I) for the first time. This task aims to learn a mapping between unpaired panoramic source and non-panoramic target domains to modify naive 360 panoramic images. However, it is difficult to use existing I2I methods due to two main challenges. Firstly, panoramas inherit geometric distortions, which pose challenges for methods based on a narrow field-of-view. Secondly, accessing panoramic datasets encompassing various weather conditions or times for training purposes is severely limited. To address these challenges, we propose a novel I2I model tailored for mitigating panoramic distortion that harnesses readily obtainable pinhole images as the target domain for training. We introduce a versatile encoder and distortion-free discrimination that efficiently bridges the large domain gap between panoramic and pinhole images by simultaneously encoding them in a consolidated structure. It allows our model to learn style mappings while overcoming significant geometric differences between the source and target domains. Moreover, we carefully design spherical position embedding, sphere-based rotation augmentation, and its ensemble to address the discontinuities at the panorama edges. Comprehensive experiments verify that our framework effectively translates panoramic street views from daytime to night, rainy, and twilight scenes by referring to the holistic style of pinhole data.
Our method also shows superior results in both maintaining structural coherence and rotation equivariance, clearly surpassing the existing I2I methods in qualitative and quantitative results.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work proposes a panoramic I2I task by translating panoramas with pinhole images as a target domain. In particular, a versatile encoder and distortion-free discrimination are designed to efficiently bridge the large domain gap between panoramic and pinhole images. To address the discontinuities at the panorama edges, the strategies of spherical position embedding and sphere-based rotation augmentation are proposed. Experimental results demonstrated that the proposed work significantly outperforms the previous methods.

### Strengths
+ To my knowledge, this is the first work that leverages pinhole images to guide the panoramic I2I task. It well addresses two challenges: directly applying conventional I2I methods cannot perceive the specific geometric distortion in panoramic images; panoramic image translation is the absence of sufficient panorama datasets covering diverse conditions.
+ The supplementary materials allow quite convincing supports for this work. More implementation details, network architectures, comparison evaluations, and deep analyses of experiments are offered.
+ The experiments are comprehensive, and some comparison samples look promising.

### Weaknesses
- While this work provides the first step for the panoramic I2I task by translating panoramas with pinhole images as a target domain, the novelty seems kind of limited from my perspective. For example, the adaptation from source (pinhole) dataset with annotated label to target (panoramic) dataset (Mutual Prototypical Adaptation) has already explored in "Bending Reality: Distortion-aware Transformers for Adapting to Panoramic Semantic Segmentation"; the similar panoramic modeling strategy in encoders has been exploited in "Disentangling Orthogonal Planes for Indoor Panoramic Room Layout Estimation with Cross-Scale Distortion Awareness" and "Spherical Convolution"; the discontinuity elimination strategy is also studied in "Cylin-Painting: Seamless 360° Panoramic Image Outpainting and Beyond with Cylinder-Style Convolutions", "Diverse plausible 360-degree image outpainting for efficient 3dcg background creation", "Spherical Image Generation From a Few Normal-Field-of-View Images by Considering Scene Symmetry", etc. Please briefly review the above literature and discuss your customized contribution beyond these baselines.
- In Figure 3, the authors claimed that Stage I only learns to reconstruct the panorama source, and Stage II learns panorama translation. However, it is hard to discriminate the difference between stage I and stage II in the figure.
- For the architecture, the motivation of using a shared content encoder and a shared style encoder to learn both panoramic images and pinhole images is ambiguous and unclear, given the context in which their domains significantly differ.
- Did the comparison method retrain on the panoramic images? More implementation details are expected to be provided.

### Questions
Could the pinhole-image-guided panoramic method be extended to other tasks, such as panoramic image inpainting and outpainting?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this work, the authors propose a new task, to learn the mapping from unpaired panoramic source to non-panoramic target. They propose a new I2I model for it. The experimental results show the effectiveness of their model.

### Strengths
This paper is well-written and easy to follow. The new task is interesting. They have done comparison and ablation studies to validate their proposed components.

### Weaknesses
However, there the following concerns to prevent me vote for acceptance. 

The first one is the unfair comparison, and some examples might not be sufficient supports. In Fig. 2, the FSeSim is designed for planar images, not panoramic images. If directly using FSeSim in panoramic images, it’s unfair comparison. The authors should compare the style transfer ability by using cube map project, which transfers the sphere data into six faces. And FSeSim is used on each face image and finally combined. In this way, the comparison is fair. Similar in Fig. 4, compared SOTA are designed for planar images, and it’s unfair in this directly inference. 

The second one is the used projection, where the better one is cube map, not ERP. Using cube map projection, the main things is to make consistency between six face, even for the existing method.

### Questions
See weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work designed a new method for panorama style transfer. Unlike natural images, panorama has several differences, such as distortion. To bridge the gap between image-to-image translation approaches and panoramic images, this submission proposed distortion-aware panoramic modeling techniques and distortion-free discriminators for this problem. Experimental results on some benchmarks show the effectiveness of the proposed method.

### Strengths
- Though image-to-image translation (style) is a typical problem, this paper focuses on a new setting, style transfer for panorama. I believe there would be a lot of applications of panoramic image style transfer in XR.
- Given the differences between panorama and natural photos, this paper designed some modules for panorama, and experiments show improvement over previous methods.

### Weaknesses
- The writing can be further improved and polished to make the submission stronger. Some equations such as EQ(8)(9) confuse me, as there are so many symbols and notations. It would be better to include more insights and explanations in the context rather than listing equations. Also, Fig. 3 is hard to follow and I would suggest the authors re-organizing it. Which parts are Stage I? Which parts are Stage II? What do notaitons mean in Fig.3? It would be better to make the figure self-contained. 
- Baselines. The tasks of Day-to-Night and Day-to-Rain are very similar to unpaired image-to-image translation tasks in CycleGAN and many follow-up works. This task is also related to image style transfer, as there is a content panorama and a style pinhole image. Could you compare your method with some style transfer works? Also, the baseline results in Fig.4 are too bad, and the shapes are even not preserved. I would suggest double-checking the baseline results and comparing to some up-to-date image-to-image translation works with diffusion models.

### Questions
- Could you show some failure cases of the proposed method?
- The submission only shows results on two types of translation, i.e., Day-to-Night, Day-to-Rain. This makes it difficult to determine whether the proposed method is general. Could you show more results on more styles?
- Compared to pretrained methods. One motivation of this paper is it is difficult to collect paired data for training. Could you discuss the pros and cons compared with methods with pretraining [1]?
[1] Pretraining is All You Need for Image-to-Image Translation. 2022

### Soundness
3 good

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
This paper proposes a new approach for unpaired panoramic image-to-image translation, which addresses the challenges of modifying naive 360-degree panoramic images using readily obtainable pinhole images as the target domain for training. The authors introduce a new model that leverages spherical position embedding and sphere-based rotation augmentation to address discontinuities at the panorama edges. The proposed method is evaluated on several datasets and compared with state-of-the-art methods, demonstrating superior performance in terms of both quantitative metrics and visual quality.

### Strengths
The proposed method is well-motivated and addresses the problem in the field of panoramic image processing. The authors provide a clear and detailed description of the model architecture and training procedure, which makes it easy to reproduce the results. The experimental evaluation is thorough and includes both quantitative and qualitative analysis, which demonstrates the effectiveness of the proposed method. The use of spherical position embedding and sphere-based rotation augmentation is a novel contribution that significantly improves the performance of the model.

### Weaknesses
1: Enhancing the motivation behind the task is crucial; specifically, showing practical applications of Panoramic Image-to-Image Translation would be great.

2: How can the proposed method  help downstream applications such as AR/VR and driving? It would be great to see more results and discussions on this part.

3: Delving into the computational aspects, including time, memory, and overall efficiency, and comparing these metrics with other techniques, would add substantial value to the discussion.

4: It appears that the Ensemble technique and SPE deform conv have a relatively minor impact on the overall pipeline. Given this, I recommend conducting an ablation study, progressing step by step, as demonstrated in Table 1 of the StyleGAN paper ("A Style-Based Generator Architecture for Generative Adversarial Networks") to better presents the contribution of each module.

### Questions
Please see weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

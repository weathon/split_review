# SPA: 3D Spatial-Awareness Enables Effective Embodied Representation

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
In this paper, we introduce SPA, a novel representation learning framework that emphasizes the importance of 3D spatial awareness in embodied AI. Our approach leverages differentiable neural rendering on multi-view images to endow a vanilla Vision Transformer (ViT) with intrinsic spatial understanding. We present the most comprehensive evaluation of embodied representation learning to date, covering 268 tasks across 8 simulators with diverse policies in both single-task and language-conditioned multi-task scenarios. The results are compelling: SPA consistently outperforms more than 10 state-of-the-art representation methods, including those specifically designed for embodied AI, vision-centric tasks, and multi-modal applications, while using less training data. Furthermore, we conduct a series of real-world experiments to confirm its effectiveness in practical scenarios. These results highlight the critical role of 3D spatial awareness for embodied representation learning. Our strongest model takes more than 6000 GPU hours to train and we are committed to open-sourcing all code and model weights to foster future research in embodied representation learning. Project Page: \url{https://haoyizhu.io/spa/}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper propose a representation learning framework named SPA to incopriate the 3D spatial awarness in embodied AI. SPA represents an advancement in embodied representation learning by enhancing a standard ViT with intrinsic 3D spatial understanding through neural rendering. The comprehensive evaluation and consistent empirical success show the effectiveness of spatial awareness in embodied AI tasks.

### Strengths
1. The paper conducts one of the most extensive evaluations in embodied AI representation learning to date, covering 268 tasks across 8 different simulators. This large-scale evaluation provides a thorough comparison with multiple state-of-the-art methods showing a significant level of empirical rigor.
2. SPA uses neural rendering and multi-view images to enhance the 3D spatial awareness of the ViT, which is an effective way to give the model a better understanding of depth information and spatial relationships in 3D scenes.
3. The paper makes an important conceptual contribution by proposing and validating the spatial awareness hypothesis, which could guide future research in embodied AI representation learning.

### Weaknesses
1. SPA simply extends and adapts the ViT by adding neural rendering and 3D spatial features to enhance expressiveness, but the underlying architecture is still the same ViT that already exists; in contrast, many new model architectures make more independent innovations at the algorithmic level. This paper is lack sufficient groundbreaking innovations in model architecture.

2. The evaluation of SPA focuses primarily on imitative learning and does not fully explore reinforcement learning or other complex learning paradigms. This limits the scope of understanding the generalizability and performance of the model under different real-world conditions.

3. SPA is designed for static multi-view images, which constrains the ability to model dynamics and temporal changes that are essential in many embodied AI scenarios. And the paper proposes 3D spatial awareness is critical, however it does not consider temporal relationships.

4. While the paper claims that SPA has achieved significant improvements in 3D spatial perception, there is a lack of independent comparative experiments to validate the contribution of neural rendering for the overall performance improvement. The specific effects of multi-view learning and 3D spatial understanding are not isolated. This makes it impossible to determine whether the improvements come from 3D spatial awareness or from better data or other improvements in training strategies, etc.

### Questions
1. SPA currently focuses on static multi-view scenes. How does the model generalize to dynamic environments, especially where temporal information is critical?
2. The evaluation is focused solely on imitation learning. How would SPA perform in a reinforcement learning setting?
3. Are there any optimizations or lightweight versions of SPA that could reduce computational costs?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work introduces SPA, a representation learning method that incorporates 3D spatial awareness into Vision Transformers using differentiable rendering as a pretraining objective.
Starting with multi-view images and camera poses, the method constructs feature volumes using deformable attention and employs NeuS-based volume rendering to generate self-supervised RGBD and semantic maps for pretraining.
The authors claim their 3D pre-training objective better captures the 3D spatial relationships for embodied tasks.
They benchmark their approach through an extensive evaluation, spanning five existing benchmarks (VC-1, Franka, Meta-World, RLBench and LIBERO).
The results demonstrate consistent improvements over both vision-centric and embodied-specific baselines, with particularly strong performance on zero-shot camera pose estimation tasks.

### Strengths
Method addresses an important gap in current representation learning approaches by explicitly incorporating 3D spatial understanding through differentiable rendering.

Comprehensive evaluation across a large number of tasks and simulators demonstrates the broad applicability of their approach.

The self-supervised nature of their training signal (generated RGBD and semantic maps) is an interesting direction that reduces the need for expensive labeled data.

### Weaknesses
The paper's performance on LIBERO-spatial (Table 4) is somewhat counterintuitive.
This seems like quite an important benchmark out of all the evaluation tasks, and given SPA's neural rendering pretraining objective, one would expect stronger results on spatial tasks. The specific nature of the spatial reasoning required by this benchmark, which involves understanding spatial relationships described in language, is not adequately addressed by the proposed method. The method's focus on visual spatial awareness, while valuable, does not directly translate to strong performance on tasks that require linguistic understanding of spatial prepositions and relations.

It seems to me that AM-RADIO should be a baseline comparison in Table 3, given that the feature maps are in used as supervision during pre-training. The lack of comparison to this method, which also uses feature maps for supervision, makes it difficult to assess the relative contribution of the proposed approach. A direct comparison would help clarify whether the performance gains are due to the 3D spatial awareness or simply the use of feature map supervision.


### Questions
Could the authors clarify if Section 2.2 represents a novel contribution or builds on existing methods?

I believe the DROID dataset consists of dynamic scenes, which is not explicitly handled by the NeuS volume rendering.
Did the authors do anything special to handle this?

Minor suggestions:

Table 1 appears to be structured more like an ablation study than a main result.
For reading flow, it might be helpful to move this to a later section.

Figure 1 is a bit hard to read due to choice of colors.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a new way of incorporating 3D spatial awareness into 2D visual setting to be used in embodied AI. The authors achieve this by first extracting 2D features from images via a ViT, then construct a 3D feature volume from the multi-view feature maps, then employs differentiable neural rendering to connect the 2D and 3D domains, predict color, depth and semantic features per pixel and then trains the whole model with rendering loss along with some regularizations. This paper also presents an extensive embodied evaluation benchmark.

### Strengths
1. The paper is very nicely written

2. The architecture is quite well thought out, tying several components effectively, a feat not easy to achieve or make it work.

3. The evaluation benchmark has 268 tasks, which is quite extensive and a big improvement over previous benchmarks.

4. Thorough ablations (mask ratio importance, dataset impact, etc) are very informative

5. Results are quite nice, showing the potential of SPA

### Weaknesses
1. Benchmark descriptions are not well written. Not clear what the tasks are supposed to be.

2. Tables do not have sufficient captions, and is a bit difficult to understand the metrics from the tables themselves.

3. It is not clear from the tables which methods are adapted from vision community to solve embodied AI tasks, thus making it difficult to assess the fairness of the comparison.

4. Real world task setting is missing the most common vision language tasks which might benefit from spatial awareness. How well does this perform for tasks solved by papers like "Spatial VLM: Endowing Vision-Language Models with Spatial Reasoning Capabilities"?

### Questions
1. What are the mask tokens that are used to fill the masked patches in section 2.1? are they learnt?

2. Can you describe the tasks and what they entail properly? It is not much clear from the paper itself what the single and multi task benchmarks are about. 

3. Can you provide results for proper established real world tasks (object detection or vision language based spatial aware tasks)? You can check the OpenEQA dataset, or the paper "Spatial VLM: Endowing Vision-Language Models with Spatial Reasoning Capabilities" for this.

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
The paper presents SPA, an innovative framework for representation learning that enhances 3D spatial awareness in embodied AI. SPA integrates differentiable neural rendering on multi-view images to give a ViT a strong sense of spatial understanding, enabling it to excel in various embodied tasks. The author conducted an extensive evaluation across 268 tasks in 8 different simulators, addressing both single-task and language-conditioned multi-task scenarios. SPA achieves superior performance with less training data. Real-world experiments confirm SPA’s practical effectiveness, underscoring the importance of 3D spatial awareness in representation learning for embodied AI. Overall, the paper is well-written and the experiments are extensive.

### Strengths
The paper is well-written. The method named SPA is simple yet effective. The authors have carefully designed their experiments, showcasing SPA's impressive performance across a wide range of task types, including both single-task and language-conditioned multi-task scenarios. This level of comprehensive evaluation highlights the versatility and robustness of SPA. I greatly appreciate the extensive efforts the authors have invested in the evaluation process, as they rigorously compared SPA against multiple state-of-the-art representation methods.

### Weaknesses
My main concerns about this paper are listed below.
1) The author claims that the paper proposes a significant spatial hypothesis that 3D spatial awareness is crucial for embodied representation learning. However, I believe this hypothesis is clear long before and that is also why many work try to use 3D features for embodied tasks. I appreciate the authors' efforts to demonstrate this, but I do not think it is a significant 'new' hypothesis.

2) About the methodology. Previous work have tried to generate 3D representations from 2D images and use them for embodied tasks. But here, the author randomly mask patches across multi-view images. So I'm worried about the quality of the volume construction. MAE leverages a high ratio of mask and I'm wondering whether the quality of construction will be affected, and then make the training objective too easy during the volume rendering.

3) As the paper is about how to integrate 3D spatial awareness into 2D backbones, I believe some work about learning 3D features from 2D images should be further discussed. However, in section "Representation Learning for Embodied AI", I didn't see too much about this.

Overall, I think there are still some questions in this paper, both on writing and methodology. But I may consider raise the score if the authors can explain more about question 2. And I would like to know the attitude of the authors towards question 1&3

### Questions
My questions are listed in weakness section.

### Soundness
2

### Presentation
3

### Contribution
2

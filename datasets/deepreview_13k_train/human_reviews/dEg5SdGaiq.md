# PooDLe🐩: Pooled and dense self-supervised learning from naturalistic videos

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
\looseness=-10000
Self-supervised learning has driven significant progress in learning from single-subject, \emph{iconic} images.
However, there are still unanswered questions about the use of minimally-curated, naturalistic video data, which contain \emph{dense} scenes with many independent objects, imbalanced class distributions, and varying object sizes.
In this paper, we propose a novel approach that combines an invariance-based SSL objective on pooled representations with a dense SSL objective that enforces equivariance to optical flow warping.
Our findings indicate that a unified objective applied at multiple feature scales is essential for learning effective image representations from high-resolution, naturalistic videos.
We validate our approach on the BDD100K driving video dataset and the Walking Tours first-person video dataset, demonstrating its ability to capture spatial understanding from a dense objective and semantic understanding 
via a pooled representation objective.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces PooDLe (Pooled and Dense Learning), a self-supervised learning method for learning visual representations from naturalistic videos. PooDLe is a joint framework combining dense flow-equivariance learning with a pooled objective using pseudo-iconic subcrops. It shows state-of-the-art performance on multiple benchmarks while demonstrating strong performance on small objects and rare classes.

### Strengths
1. The authors propose a novel approach to handling spatial imbalance in dense scenes through unified pooled and dense objectives. The creative use of flow-informed cropping to generate meaningful subcrops is insightful. 
2. The paper provides comprehensive experimental validation across multiple benchmarks, and the method demonstrates obvious improvements on challenging cases (small objects, rare classes).

### Weaknesses
1. Optical flow computation is typically computationally intensive, requiring expensive pixel-wise correspondence matching. It is important to discuss the computational costs of flow estimation. Limited discussion of real-time performance implications
2. Limited analysis of inference time requirements. e.g. how inference time scales with input resolution.
3. Missing discussion of potential memory bottlenecks from joint objectives. e.g. GPU memory requirements for different input sizes, and comparison with baselines.

### Questions
1. What is the computational overhead of the SDM compared to simpler upsampling approaches?
2. How sensitive is the method to video frame rate or motion blur?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes an approach for self-supervision from video. The authors highlight the discrepancy between image datasets which typically contain a single central object and more challenging video data which is composed of complex scenes filled with many objects of differing sizes. The simpler image setting lends itself well to global embedding-based self-supervised methods, but such methods might not be ideal for representation of larger multi-object scenes.

The key idea of the paper is to mix dense and global objectives. For dense feature supervision, the authors follow FlowE (Xiong et al 2021) with one key difference being the use of a U-net style architecture to upsample and connect higher resolution features from earlier layers. The more "global" pooled-objective is applied to subcrops. Similar to how FlowE will match optical flow-warped dense features, subcrops are adjusted across frames by predicted optical flow to have a higher chance of containing the same subject. The motivation for learning on subcrops is for smaller, salient objects to take up a larger fraction of pixels. 

The model is pretrained on BDD and Walking Tours and then segmentation and detection heads are trained on top of the frozen backbone. The resulting model outperforms other self-supervised approaches as well as ImageNet pretraining.

### Strengths
This is a solid paper, well motivated introduction, straightforward idea, outperforming other methods with the appropriate ablations to break down different design decisions. Each of the key ideas behind the approach are sensible, I am surprised it is not already common to perform dense feature self-supervision on U-net/FPN style features.
- I appreciate the level of specific, little details throughout the paper to understand exactly how things were implemented
- it's interesting to see that both losses only start to play a role after a clearer distinction has been made between the pooled "global" and upsampled dense features (Table 4)
- also cool to see that the method performs well with imperfect self-supervised flow

### Weaknesses
This is minor, but I am a bit confused about the subcrops. When reading I was expecting some mechanism for smarter choice of crops such that there's a higher probability of including an object of interest. For example, some sampling based on saliency or flow that would ensure more crops included people/bikes/etc, but it doesn't seem like that's the case? Instead, crops are chosen randomly and uniformly across the image so they are just as likely to sample a patch from the sky as from the street. The key difference as far as I understand is that by virtue of doing any cropping at all an object of interest will now take up a greater fraction of pixels, and using flow ensures the object will likely be included in both crops. Feels somewhat at odds with how the paper has been written and motivated which emphasizes putting extra attention on smaller objects as opposed to background context.

### Questions
Overall the paper is solid so this is again fairly minor, but I have a bunch of cropping related questions as that's the one area I had the most confusion:
- Where exactly does the global cropping fit into all of this, what's the point of defining a global crop at all?
- In Figure 7, I'm not sure what it means to change the number of subcrops, is it changing the proportion of correlated samples in a given minibatch? What is the method with 0 subcrops - is it using the global crop as input into the encoder?
- Maybe I missed it, but is there ever an ablation on the importance of the subcrops being flow matched? Intuitively seems like a reasonable thing to do but does it matter much?
- In Table 4, is the FlowE result trained with the proposed cropping approach? How does this compare to FlowE without using subcrops?
- Is the training done on 192x192 crops but testing at 512x512, is there any issue with this discrepancy or does the model generalize well enough to the larger test time resolution?

### Soundness
3

### Presentation
3

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
The paper introduces PooDLe, a self-supervised learning (SSL) method tailored for complex, naturalistic video data with densely packed scenes and diverse object scales. Unlike standard SSL methods trained on iconic images, PooDLe addresses the spatial imbalance in cluttered video data by combining a dense SSL objective that maintains equivariance through optical flow warping with a pooled objective that captures semantic information from smaller, aligned subcrops. This dual-objective approach, augmented with a spatial decoder module (SDM), is shown to effectively represent both large and small objects.

PooDLe’s performance is validated on driving and first-person video datasets, achieving state-of-the-art results in semantic segmentation and object detection tasks, particularly excelling with small object recognition. Additionally, the paper introduces the Walking Tours Semantic (WT-Sem) segmentation task, presents a detailed analysis of class size and frequency on BDD100K, and studies the impact of global crop area, input resolution, and temporal stride on learning efficacy, highlighting key factors for SSL with naturalistic data.

### Strengths
1. The paper is well-written with a clear structure to demonstrate a clear and logical progression of motivation and ideas. The authors use precise and well-chosen words that enhance readability and engagement.

2. The motivation to combine pooled representations and dense local object representations is well justified. The proposed method aligns well with the motivation.

3. The paper provides comprehensive/detailed analysis, testing the proposed method across various scenarios and datasets. This thorough experimental validation successfully demonstrates the method’s effectiveness on small and rare objects.

### Weaknesses
1. The main weakness of this work is lack of enough ablations for the proposed method. It is not clear (with the shown ablations) if local crops really are useful. Considering this is the main contribution in terms of novel idea, it should have been made clear. Results with just local crops might help, since adding these local crops on dense does not improve, but hurt smaller objects. It will be good to see accuracy on this and on datasets other than BDD as well.

2. Although there are several experiments presented, the technical contributions seems little on the weaker side, the method is build on top of FlowE, local crops is novel (but its contribution not clear), the improvement on dense consistency is expected due to use of features from earlier layers,

3. The proposed method shows some improvement over existing methods, but looking at a comparison with the baseline (FlowE), mostly its incremental (less than 1%) if we look at accuracy. That is why it is important to loot at this metric in the ablations. Also, this baseline is not shown for the other dataset (WalkingTour), where the proposed method do not outperform other methods across the board.

### Questions
- The explanation for why combining SDM with Pool helps is not clear. Also, it is not clear why just pool should not help, its even hurting the small objects. SDM has additional parameters, can that be a reason (of course the fine-grained features will help too), SDM is not even connected with Pool.

- In figure 4, it shows finer boundaries for smaller objects, but boundaries for bigger objects, such as car, is getting worse in comparison to other methods, also performance seems similar to the baseline approach FlowE.

- L075: "These subcrops serve as pseudo-iconic views of foreground objects, functionally increasing the prevalence of smaller objects". It is not clear why taking random crops will increase prevalence of smaller objects, parts of bigger objects or backgrounds will have higher probability among these crops.

- Ablations are not comprehensive, only one dataset, one metric, and one task is shown. It will be good to see accuracy metric, and also how these components perform with any other dataset. BDD is street-view, maybe Ego or some other natural videos, CCTV, etc. It will be good to see the ablations on the walkingtour dataset along with BDD. It seems to be working fine with driving videos, since scene will not change a lot, but what about other videos? Like ego-centric? Or static camera?

- What about performance just with pool? It will be good to see if just learning from the crops are enough. SDM improves, but it comes with additional parameters too.

- Since this work is build on top of FlowE, there should be results for FlowE on other datasets too (Table 2).

- It is not clear why results were shown only with ResNet, why not ViT?

- Will this method work on other simple tasks like classification?

- It will be good to see accuracy in Table 3 and 4.

- Using additional crops for training adds training overhead, there is no analysis shown on this. 

- Figure 9, it will be good to see t between 0 and 15.

- The role of predictor and projector is not clearly explained, projector is not even shown. It is not clear.

- L205: why crop features are averaged-pooled over spatial dimension? Fine-grained constraint should be better?

### Soundness
3

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
Self-supervised learning for naturalistic videos is challenging with the presence of independent objects of various sizes, imbalanced class distribution, etc.
The paper aims to tackle these problems by combining global and dense supervision, as well as spatial decoder modules (SDM).
The dense objective could help capture different object instances from the videos while the global objective could help learn the semantics of the objects using contextualized signals.
The proposed method, PooDLe, was evaluated on representative video benchmarks, e.g. BDD100K, Walking Tours, ADE20K, Cityscapes, demonstrating superior performance on dense prediction tasks, i.e. semantic segmentation and object detection.

### Strengths
i) Method. The proposed method, PooDLe, is technically sound.

ii) Performance. Compared to prior global or dense-only works, PooDLe demonstrated superior performance on dense prediction tasks like semantic segmentation and object detection.

iii) Ablation. The paper further verified that PooDLe improved the performance of small and rare objects, justifying the advantage of combining global and local supervisions, as well as the spatial decoder modules (SDM). It also provided ablations on the pretraining datasets, different components, and augmentation strategies, e.g. crop area, resolutions, etc.

### Weaknesses
The reviewer has several concerns and questions about the evaluation, ordered by their impact on the final score.

---
Concerns:

i) About SDM. SDM introduced extra operations on higher resolution feature maps or images. From L306-307, SDM was also used in the inference stage for semantic segmentation. In this case, the inference overhead is determined by both the backbone architectures (e.g. ViT-S, ResNet50), and the UNet based SDM. The reviewer wonders if the baseline approaches also have SDMs during inference? Were they of the same architectures, complexities (e.g. FLOPs)? If they are not of the same complexity, could the authors provide the FLOPs of each baseline and PooDLe. This could show if the comparisons of different methods on semantic segmentation are apples-to-apples, especially for inference.

ii) Some comparisons are apples-to-oranges. At L358-L360, it was claimed that PooDLe outperformed DoRA across different settings. If the reviewer understood correctly, the comparisons there were between PooDLe_ResNet50_epoch20 and DoRA_ViT-S_epoch100, which were not fully convincing. The authors are encouraged to present apples-to-apples comparisons under the same setting, e.g. backbone, #epoch, or remove the claims otherwise.

---
Questions

iii) Tasks beyond dense prediction. It was shown that augmenting dense supervisions with global objectives could help improve dense prediction tasks. The reader may also be curious if augmenting global supervisions with dense objectives could help improve global prediction tasks, e.g. action recognition, etc.

iv) About the "relationship between global crop area and input resolution". It was claimed in Contribution 3 (L101-102). However, there seems to be no explicit analysis of the "relationship" between "crop area" and "resolution", or the relationship could not be easily interpreted from Figure 5. To reveal the relationship between "crop area" and "resolution", the authors could consider analyzing extra metrics derived from them, one example could be the pixel-scale, i.e. crop_area/input_resolution, defined in [1].

v) Patch size used for ViT-S, which determines the FLOPs of some baseline approaches

vi) The videos of Walking Tours (WT) are at 4K+60fps, instead of 720p+30fps (L248-249)?

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

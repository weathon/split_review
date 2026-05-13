# 3D Vision-Language Gaussian Splatting

- Decision: Accept
- Scores: 6, 6, 6, 8, 6

## Abstract
Recent advancements in 3D reconstruction methods and vision-language models have propelled the development of multi-modal 3D scene understanding, which has vital applications in robotics, autonomous driving, and virtual/augmented reality. However, current multi-modal scene understanding approaches have naively embedded semantic representations into 3D reconstruction methods without striking a balance between visual and language modalities, which leads to unsatisfying semantic rasterization of translucent or reflective objects, as well as over-fitting on color modality. To alleviate these limitations, we propose a solution that adequately handles the distinct visual and semantic modalities, i.e., a 3D vision-language Gaussian splatting model for scene understanding, to put emphasis on the representation learning of language modality. We propose a novel cross-modal rasterizer, using modality fusion along with a smoothed semantic indicator for enhancing semantic rasterization. We also employ a camera-view blending technique to improve semantic consistency between existing and synthesized views, thereby effectively mitigating over-fitting. Extensive experiments demonstrate that our method achieves state-of-the-art performance in open-vocabulary semantic segmentation, surpassing existing methods by a significant margin.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper focuses on improving the semantic rendering quality within well-reconstructed 3D scenes. With introducing self-attention, semantic indicator and regularization, the  proposed method achieves better semantic segmentation results, especially for 
transparent objects.

### Strengths
1. The paper is well-written and easy to follow.

2. The designs are well-motivated.

3. The performance shows a significant improvement.

### Weaknesses
(1) Line 215, the u^i is the fused features or position?

(2) In camera interpolation, why use mix-up to generate a feature map instead of using an off-the-shelf OV model to output one? Just like previous methods.

(3) Missing a global ablation study to present the importance of 'self-attention', 'semantic indicator'. 'camera interpolation' over your baseline. Now, it is unclear how the baseline stands in comparison with previous methods and the contributions from the three proposed designs.

(4)  Low efficiency, the Table. 8 shows it takes over one hour to learn the semantics of single 3D scenes, which is significantly longer than typical 3D Gaussian reconstruction (which may take less than 10 mins on A100？), especially considering the iteration is only 15k. What makes the rasterization so slow? In addition, since more attributions are added in Gaussian, it is fair to provide the storage cost of Gaussian models when compared with other works in Table.8 instead of only Gaussian numbers.

(5) The incomplete experiments. The experiments on 3D-OVS are conducted on  5/7 scenes instead of full scenes.

(6) No deep analysis of performance. In my view, the IoU improvements are mainly from the translucent or reflective objects, as shown in Figure.3, no detailed statistics to prove that.

### Questions
(1) What is the different between self-attention and cross-attention mechanism?

(2) Considering the experiment setting is the open-vocabulary, for example, the CLIP feature dimension is 768, how to obtain 768 rendering with d_c+d_f=6? How to perform the dim. Reduction as shown in Figure.2

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper claims that the performances of current multi-modal scene understanding approaches are limited by the the imbalance between visual and language modalities, which have widely different properties.
To alleviate these limitations, this paper proposes several strategies, including a cross-modal rasterizer that places greater emphasis on language features and a camera-view blending technique.
Finally, the proposed methods achieves state-ofthe-art performance in open-vocabulary semantic segmentation tasks.

### Strengths
1. The motivation of this paper  sounds reasonable. The over-fitting on the color modality may have a negative impact on semantic learning, which is consistent with intuition.
2. The proposed techniques, including the smoothed semantic indicator  and the mix-up augmentation, are simple but effective.
3. The performance of the method  outperform existing methods by a significant margin.

### Weaknesses
1. Although the motivation  sounds reasonable and the Figure 3 explain the motivation to some extent, I expect more experiments to further study the differences between color and semantics modalities. Beside showing quantitative, qualitative results and ablation of the proposed strategies, the authors should further discuss the deeper mechanisms. For example, the authors can study the relationship between color over-fitting phenomenon and specific scenes.
2. The figure 2 is hard to understand. The method is simple but the process in the figure looks complicated. Some fonts are too small.

### Questions
1. What is the specific relationship between the improvement brought by your method and the details of the scene? In what kind of scene is your improvement more obvious?

### Soundness
2

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
3

### Summary
This paper learns language embedded 3dgs field and addresses the often-neglected issue of appearance-semantic misalignment in rasterization. It introduces a camera-view blending technique to enhance semantic consistency between existing and synthesized views. The experimental findings demonstrate that the proposed approach outperforms existing methodologies.

### Strengths
1. The paper provides a profound insight into the challenges posed by semi-opaque media and intricate light transport effects, highlighting the limitations in translating color opacity to the semantic domain. This observation is interesting. 
2. The implementation of a single learnable parameter to replace the conventional shared color opacity parameter is both straightforward and efficient.
3. The paper is commendably structured, presenting a well-motivated narrative and a clear methodology.

### Weaknesses
1. The paper introduces the camera-view blending technique as a method to enhance cross-view semantic consistency. However, it falls short in fully addressing the challenge of different objects sharing similar colors, potentially leading to indistinguishable semantic representations, which the authors claim to have tackled. Further insights on this critical point are needed.
2. In Section 4.4, the experimental results suggest an increase in rendering speed with the proposed pipeline. However, given the introduction of additional steps and parameters, one would expect a potential decrease in inference speed. The discrepancy in the reported results requires clarification.
3. The title of the paper, "3D Vision-Language Gaussian Splatting," might be misleading as it predominantly focuses on learning open language semantic fields rather than visual appearances. A revision to better reflect the core contribution of the research is recommended.

### Questions
I am curious about the impact of semantic learning on rendering quality.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes an interesting idea on how to fuse multi-modality info, i.e. visual & semantic, for better semantic rasterization in 3DGS. This solution mainly composes of a cross-modal rasterizer, a specially designed semantic indicator and a camera-view blending method. The solution is interesting especially because it offers a better solution for semantic rasterization for reflective or translucent objects, which is a serious problem with the original 3DGS. For me, the designed semantic indicator in the Gaussian representation is novel and useful for the claimed main problem. The main contributions also include the empirical quality result of the semantic indicator on these reflective or translucent objects, and quantity comparison of open-vocabulary semantic segmentation tasks. These results conclude the usefulness of the proposed solution. 

The paper is generally well written and structured, easy to follow and read. I don’t come across many issues for further clarification. But here a few things I may need the authors to respond. Given those issues properly clarified, I would be willing to increase the score.

1、	Equation (3), any language/semantic should not change due to view angle, so F^W doesn't make sense to me, even the authors mention that superscript W will be omitted for ease of reading. It shouldn’t appear in the original equation at all. Also in the same equation, there lacks a clear definition of what L_sem is, but this should be a minor issue.
2、	Figure 3 right, I’m not 100% sure where the symmetry of the density distribution is from, as there lacks sufficient correlation between l and o. 
3、	Table 8, an average training and inference time should be reported on all scenes of a whole dataset, instead of on just one. 
4、	The Related Work session is relatively weak and could be fortified with more related reference included. For instance, “HUGS: Holistic Urban 3D Scene Understanding via Gaussian Splatting”, which proposes another way of using semantic info in 3DGS (not traditional 2d way mentioned by the authors）and is worthy of being cited. 
5、	A minor grammar error of Line 356-357.

### Strengths
The proposed idea is interesting, especially because it offers a better solution for semantic rasterization for reflective or translucent objects, which is a serious problem with the original 3DGS. For me, the designed semantic indicator in the Gaussian representation is novel and useful for the claimed main problem. The main contributions also include the empirical quality result of the semantic indicator on these reflective or translucent objects, and quantity comparison of open-vocabulary semantic segmentation tasks. These results conclude the usefulness of the proposed solution.

### Weaknesses
A few issues are listed in the next section.

### Questions
1、	Equation (3), any language/semantic should not change due to view angle, so F^W doesn't make sense to me, even the authors mention that superscript W will be omitted for ease of reading. It shouldn’t appear in the original equation at all. Also in the same equation, there lacks a clear definition of what L_sem is, but this should be a minor issue.
2、	Figure 3 right, I’m not 100% sure where the symmetry of the density distribution is from, as there lacks sufficient correlation between l and o. 
3、	Table 8, an average training and inference time should be reported on all scenes of a whole dataset, instead of on just one. 
4、	The Related Work session is relatively weak and could be fortified with more related reference included. For instance, “HUGS: Holistic Urban 3D Scene Understanding via Gaussian Splatting”, which proposes another way of using semantic info in 3DGS (not traditional 2d way mentioned by the authors）and is worthy of being cited. 
5、	A minor grammar error of Line 356-357.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a novel approach to open-vocabulary 3DGS. It proposes to use another learnable opacity parameter for the blending of semantics, and train a cross-modal fusion module. The authors also propose a semantic-aware camera view blending method, in which they randomly interpolate between training views and supervise the semantic rendering based on the weighted sum of the semantics. The experiments show that the proposed method significantly improves the open-vocabulary semantic segmentation results.

### Strengths
1. The proposed method is novel and promising. Using another learnable parameter as opacity for semantic blending is an overlooked method that benefits open-vocabulary 3DGS.
2. The results are promising.

### Weaknesses
Please see the questions below.

### Questions
1. Is the fusion module per-scene trained? Would it be more effective to train it across different scenes to learn the prior?
2. According to Table 6 and Table 7, does the view interpolation method alone improve the performance by 6.2 mAP? It's a little counter-intuitive that simply weighted-summing the two views to supervise the interpolated views can lead to such improvements, since the weighted-sum semantics (as shown in Figure 2) do not consider the relative camera poses between the two views. What if you wrap the two views to the interpolated view using the known camera poses and learned depths?
3. The paper discussed using separate opacity for semantics, then what would the results be if learning separate covariance matrix in each gaussian for color and semantics? Besides, if we simply train two separate sets of Gaussians for color and semantic renderings respectively, would it improve the semantic segmentation results?

### Soundness
3

### Presentation
3

### Contribution
3

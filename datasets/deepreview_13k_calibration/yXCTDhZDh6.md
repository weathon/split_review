# Point-SAM: Promptable 3D Segmentation Model for Point Clouds

- Decision: Accept
- Avg Score: 6.67
- Scores: 8, 8, 6, 6, 6, 6

## Abstract
The development of 2D foundation models for image segmentation has been significantly advanced by the Segment Anything Model (SAM). However, achieving similar success in 3D models remains a challenge due to issues such as non-unified data formats, poor model scalability, and the scarcity of labeled data with diverse masks. To this end, we propose a 3D promptable segmentation model \textbf{Point-SAM}, focusing on point clouds. We employ an \textit{efficient} transformer-based architecture tailored for point clouds, extending SAM to the 3D domain. We then distill the rich knowledge from 2D SAM for Point-SAM training by introducing a data engine to generate part-level and object-level pseudo-labels at scale from 2D SAM. Our model outperforms state-of-the-art 3D segmentation models on several indoor and outdoor benchmarks and demonstrates a variety of applications, such as interactive 3D annotation and zero-shot 3D instance proposal.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper addresses the problem of deploying 3D foundational models by introducing a novel 3D promptable segmentation model for point clouds, named Point-SAM. This model extends the Segment Anything Model (SAM) into the 3D domain by developing a promptable 3D architecture that utilizes both point and mask prompts. These prompts, together with the input point cloud, are processed through a transformer-based encoder-decoder architecture to generate a 3D segmentation mask.

The Point-SAM model first tokenizes the input point cloud using one of two approaches: a single set abstraction layer (based on PointNet++), which creates patch-based features centered at each patch’s centroid encoding local geometry, or a Voronoi partition-based tokenizer, where  each Voronoi cell represents the patch’s centroid, and point-wise features are max-pooled  within each cell. The Voronoi-based method reduces computational and memory costs by bypassing the need for dense point-wise feature extraction in each centroid's vicinity. Patch features are then extracted through a ViT model, and mask prompts are incorporated from previous decoder iterations. The model upscales these patch embeddings to the original point cloud resolution using 3-nn inverse distance weighting. Following this, a two-way transformer facilitates interaction between point prompts and point cloud embeddings by utilizing cross-attention operations. The final 3D proposal is derived by applying an output token processed through a MLP.

Point-SAM is trained on a diverse set of datasets that include part-level and object-level annotations across single-object and scene-level modalities. To improve generalizability on out-of-distribution data, the ShapeNet dataset is used to transfer knowledge from SAM. This is achieved by generating 2D pseudo masks that serve as prompts to a pretrained Point-SAM model, iteratively refining its 3D proposals.

Point-SAM's is evaluated on several benchmarks for the tasks of zero-shot point-prompted segmentation, zero-shot object proposal and few-shot part segmentation, where it achieves performance that is either on par with or surpasses competing methods.

### Strengths
+ The method is a step forward towards 3D foundational models, eliminating the need of using multiple 2D views of the 3D object and 2D-3D lifting of SAM proposals at inference, while it provides the ability of refining the 3D proposals with additional prompts (as seen in supp.).
+ Unified training strategy on 3D point clouds across several datasets, covering different modalities either at annotation or scale level (part, object masks; single object, entire scenes).
+ Good performance on zero-shot point-prompted segmentation w.r.t. alternative methods.
+ Knowledge distillation from 2D foundational models such as SAM during training to further enhance the generalizability of Point-SAM.

### Weaknesses
 - The proposed Voronoi diagram tokenizer while it manages to lower the computational and memory cost of the overall pipeline, in many cases it fails to surpass the performance of the k-nn based tokenizer. Specifically, the reported IoU differences, while seemingly small, might indicate a limitation in capturing fine-grained geometric details compared to the k-NN approach, which directly uses local neighborhoods. This could be particularly problematic in scenarios with complex object boundaries or intricate part structures, where the Voronoi cell approximation might oversimplify the local geometry.
- Regarding the OOD scenarios and particularly the PartNet-Mobility, the held-out categories (scissors, refrigerators, and doors) are all part of the PartNet, thus Point-SAM has seen these during training. This weakens the zero-shot transferability of the method. The fact that these categories are present in the training data, even if not directly used for the OOD evaluation, could lead to a form of data leakage, where the model learns to recognize these object categories based on their general shape and features, rather than truly generalizing to unseen categories. This undermines the claim of zero-shot transferability.
- The process of generating pseudo labels and transferring knowledge from SAM is somewhat unclear (see Questions). The description lacks precise details on how the error region between the 2D-3D proposal is used to sample negative prompts. The iterative refinement process, while mentioned, needs more clarity on how the 3D proposal is projected back to the 2D view and how this projection is used to guide the sampling of negative prompts. The lack of a clear, step-by-step explanation makes it difficult to understand and reproduce this crucial aspect of the method.

### Questions
- Regarding the generation of pseudo labels, lines 265-269 state that the generated 3D proposal, using the 1st view’s random selected 2D prompt from SAM’s proposal, is projected back into the same view. This is then used to sample a 2D prompt (negative prompt) from the error region between the two (2D-3D proposal). Based on Figure 3, this is done in the next view (view 2). The first is used to sample the 2D prompt, the generated 3D proposal is used to prompt SAM with the 2nd view as input, and then the negative prompt is sampled for the generated 2nd 2D proposal. So, which of the two is the correct procedure?
- In Table 3, the MV-SAM baseline is absent for the ScanObjectNN dataset. Additionally, it's unclear which specific approach the term “InterObject3D++” refers to (lines 391 and 395). Is this the same baseline used in AGILE3D? 
- In Figure 4, what is the difference of blue and red point prompts?

### Soundness
3

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
4

### Summary
The paper under review presents a 3D promptable segmentation model for point clouds, called Point-SAM. Similar to the architecture of Segment Anything Model(SAM), Point-SAM also contains three parts: a point-cloud encoder, a prompt encoder and a mask decoder. A Voronoi tokenizer is adopted to divide the point cloud into patch tokens. To improve the generalization of the model, multiple existing 3D segmentation datasets are included in training. Additionally, to augment part-level segmentation data, the authors utilize both pre-trained Point-SAM to obtain an initial 3D mask and then leverage SAM to refine the mask using additional views. The method demonstrates good performance on several indoor and outdoor scenes and showcases applications such as interactive 3D annotation, zero-shot 3D instance proposal and few-shot part segmentation.

### Strengths
1. The paper extends a powerful 2D segmentation anything model (SAM) into the 3D point cloud domain
2. It introduces a novel data engine to generate multi-level pseudo-labels and augment the training data
3. The interactive segmentation video is impressive, which illustrates its potential real-world application

### Weaknesses
1. Lack of Visualization Results: The authors provide only a limited number of visualizations in both the main paper and supplementary materials. The qualitative results presented in Figure 4 are inadequate. It is anticipated that more complex examples, such as those depicted in the supplementary videos, could be included. Moreover, several applications discussed in the paper, such as few-shot part segmentation and zero-shot object proposal generation, lack corresponding visualization results.

2. In line 40, the paper asserts that "multi-view images only capture the surface, making it infeasible to label internal structures." However, the paper does not include examples, such as drawers, to demonstrate the superior performance of Point-SAM in these scenarios. The authors are expected incorporate additional experiments or examples to make this claim more convincing.

3. The segmentation quality does not look good: The paper does not directly compare its results with those of other 3D frameworks that merge results across multiple views, despitethe experiments on MVSAM. While it is acknowledged that most of these frameworks require post-processing, which can be time-consuming, their segmentation quality reported in those papers are superior, particularly along boundary regions, such as teh results in SAM3D and more advanced methods like Gaussian Grouping.

4. Prompt Point Selection: Could the authors provide a more detailed explanation of how point prompts are selected in the experiments? In Figure 4, the points are not consistently placed, and some points are marked as negative in one method while none are negative in another. Also. the positions of points are different.

### Questions
Please refer to the "weaknesses" section

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
3

### Summary
This paper addresses the 3D promptable segmentation task by examining it from three key aspects: task, model, and data. The authors propose a unified model named Point-SAM, which utilizes a point cloud representation and introduces a novel tokenizer based on Voronoi diagrams. In terms of data, they explore the generation of pseudo labels using SAM. The experimental results highlight the model's robust zero-shot transferability to unseen point cloud distributions and new tasks.

### Strengths
1. The paper presents a clear writing logic, effectively outlining the challenge to be addressed and the three distinct perspectives of the research.
2. The 3D segmentation task is a crucial direction in embodied intelligence, as it enables machines to understand and interact with complex environments. Moreover, scaling up to achieve 3D foundation models presents significant value.

### Weaknesses
The main consideration is the technical novelty of this paper, which leads me to feel that the overall contribution is somewhat weak.

1. In terms of model design, the method introduces the Voronoi tokenizer, which is innovative. However, compared to KNN, there is no significant performance improvement; the gains are only noticeable when the number of prompt points is low.
2. Additionally, there are many works utilizing SAM for 3D pseudo-labeling, whether in autonomous driving or in indoor settings, such as SAM3D, which also leverages multi-view consistency in 2D projections to refine results. What distinguishes the approach in this paper from previous works in terms of innovation?
3. I have some concerns about the practicality of this method. Is it can serve as a more general tool for 3D segmentation labeling? For instance, in autonomous driving, if segmentation requires placing points on every object, it seems inefficient. The challenge with object-level distinction lies in identifying the various parts, making the placement of prompt points crucial.

### Questions
1. Could you provide more visualizations for object-level segmentation in OOD scenarios to demonstrate the generalization of the method?

2. Are there any special design considerations when training with both indoor datasets and object-level datasets together?

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
The paper adheres to the philosophy of the Segment Anything Model by proposing Point-SAM, a 3D promptable segmentation model specifically designed for point clouds. It primarily makes two contributions: (1) a scalable and efficient transformer-based architecture that facilitates 3D promptable segmentation; and (2) a data engine that distills knowledge from the Segment Anything Model to generate pseudo labels. Experiments conducted on various indoor and outdoor datasets have demonstrated its zero-shot transferability and significant application potential.

### Strengths
- The authors develop a data engine to generate pseudo labels, providing sufficient diverse masks for datasets lacking ground truth. This allows Point-SAM to be trained with more heterogeneous datasets.
- Following the design philosophy of SAM, the implementation on 3D point clouds is shown through experiments to endow Point-SAM with zero-shot capabilities.
- The Voronoi tokenizer achieves comparable performance to the KNN tokenizer, while showing superior efficiency in KITTI360 dataset.

### Weaknesses
 - The challenges presented in the introduction are not well sovled by the proposed method. For instance, the paper mentions "There is no unified representation for 3D shapes," yet does not provide a unified representation and only designs for point cloud representation. 
- While the authors have made efforts to train Point-SAM on a diverse set of datasets, the reliance on synthetic datasets and the dominance of indoor scenes may limit the model's generalizability to outdoor and more varied environments. The paper would benefit from an evaluation on a broader range of datasets, particularly those capturing diverse outdoor scenes such as Waymo Open Dataset [1] and nuScenes [2]. Specifically, the lack of evaluation on datasets with sparse point clouds, which are common in real-world outdoor scenarios, is a significant limitation. The model's performance on such data is unclear, and this should be addressed with experiments on datasets that include sparse LiDAR data.
- Although the paper claims efficiency improvements with the Voronoi tokenizer and tests it on KITTI360 with 10 prompt points, a comprehensive analysis of the computational costs is lacking. The authors should provide more detailed benchmarks comparing Point-SAM with other methods in terms of both speed and memory usage. This should include a breakdown of the computational cost for each stage of the pipeline, including tokenization, feature extraction, and mask prediction, across varying numbers of prompt points. Furthermore, the paper should analyze the scalability of the method with respect to the size of the point cloud, as this is a critical factor for real-world applications.

### Questions
Please see the weaknesses section.

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
5

### Summary
This paper presents a method for achieving generalizable 3D point segmentation by leveraging prior knowledge from the 2D Segment Anything framework.

### Strengths
Propose a better tokenizer and show reasonable performance improvement compared with baseline.

### Weaknesses
Missing references:

"Segment Anything 3D"
"SANeRF-HQ: Segment Anything for NeRF in High Quality"
"SERF: Fine-Grained Interactive 3D Segmentation and Editing with Radiance Fields"
"Segment Anything in 3D with Radiance Fields"

### Questions
Could you clarify the difference between the proposed pseudo label generation method and "SERF: Fine-Grained Interactive 3D Segmentation and Editing with Radiance Fields"?

Additionally, the proposed Voronoi approach shows only minimal improvement compared to KNN. Could you clarify the efficiency comparison between these two?

But overall, it is a good work.

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
5

### Summary
This paper is mainly built to tackle 3D promptable segmentation task. The authors propose a segmentation model called Point-SAM, which can take 3D point prompts and mask prompts as input prompt, alongside a Voronoi tokenizer is used to fuse dense prompts. This model is trained on two phases: 1. existing well-labeled datasets; 2. unlabeled datasets, whose pseudo labels are generated by pre-trained Point-SAM from phase 1 and SAM, in order to distilling knowledge from SAM. They compare their method with baselines on zero-shot segmentation task, and showing much better performances.

### Strengths
Unlike many 2D-to-3D segmentation lifting work, this paper chooses to distill knowledge from SAM in training phase instead of aggregating in very evaluation, making it more efficient and not requiring running SAM for several times during inference. The shows great performance on choosing datasets, showing great performance on zero-show segmentation task due to distilling and better model design.

### Weaknesses
The main contribution of this paper can be divided into two folds: better model design and novel data engine to distill SAM instead of aggregating. So the paper should demonstrate the effectivity for both these two parts. However, the experiments are not strong enough:
1. This model choose to compare with AGILE3D, a straightforward baseline. In main experiments, the experiment is not fair, since the model proposed actually trained on much larger datasets than the baseline. In order to have a fair comparison, they also trained the model with the same training set as baseline in Table 6.a. However, this method only show apparent better performance on 2 out of 4 datasets. The authors argue it may due to that the baseline is overfitting to these kinds of data, but it’s assertion is not strong enough, because these two datasets both tend to include scenes with much more points than the other two. At least a cross analysis ablation, i.e. train A test B and train B test A.
2. The baselines are not thorough and strong enough. It is strange why the baseline is not trained on the same level of data. And the multi-view SAM aggregation baseline is not strong enough. The authors make up one, MV-SAM. However, there are plenty of such multi-view aggregating baselines, such as SAM-guided Graph Cut, SAI3D, Open3DIS, OpenIns3D.
3. In Table 4, evaluating only on PartNet-Mobility is not sufficient. From the table, we observe that adding ScanNet is less beneficial than adding ShapeNet. Further explanation or additional experiments are needed to clarify this difference.

### Questions
Besides the questions in weakness, I also have some other questions:
1. The authors listed Replica as an evaluation datasets in Table 2, but only compared with OpenMask3D in appendix but not with other baselines. Why do you make this choice? Combined with what mentioned in Weakness 1 and Table 6, is this due to your model is very sensitive and not so well-defined for large scale data?
2. According to Figure 4, for KITTI360 and S3DIS datasets, are the red and blue balls the visualization of prompt points? If so, why the prompts to Point-SAM and AGILE3D are not consistent? Do you use the same prompt in your main experiments?
I am open to raising my score if the authors can thoroughly address the weaknesses and questions.

### Soundness
2

### Presentation
3

### Contribution
2

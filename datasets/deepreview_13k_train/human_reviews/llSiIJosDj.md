# Point-based Instance Completion with Scene Constraints

- Decision: Accept
- Scores: 8, 6, 6, 8

## Abstract
Recent point-based object completion methods have demonstrated the ability to accurately recover the missing geometry of partially observed objects. However, these approaches are not well-suited for completing objects within a scene as they do not consider known scene constraints (e.g., other observed surfaces) in their completions and further expect the partial input to be in a canonical coordinate system which does not hold for objects within scenes. While instance scene completion methods have been proposed for completing objects within a scene, they lag behind point-based object completion methods in terms of object completion quality and still do not consider known scene constraints during completion. To overcome these limitations, we propose a point cloud based instance completion model that can robustly complete objects at arbitrary scales and pose in the scene. To enable reasoning at the scene level, we introduce a sparse set of scene constraints represented as point clouds and integrate them into our completion model via a cross-attention mechanism. To evaluate the instance scene completion task on indoor scenes, we further build a new synthetic dataset called ScanWCF, which contains labeled partial scans as well as aligned ground truth scene completions that are watertight and collision free. Through several experiments, we demonstrate that our method achieves improved fidelity to partial scans, higher completion quality, and greater plausibility over existing state-of-the-art methods. The dataset and the code will be publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a scene-level instance completion method based on point clouds. The main contributions are two-fold. First, a more sophisticated seed generator is used to obtain patch seeds. It predicts the offsets to the centers of the objects and leverages scene constraints to generates more reasonable seeds. Second, the authors construct a new dataset for scene instance completion task, which contains watertight and collision-free ground truths. The authors conduct comprehensive experiments and ablation studies to demonstrate the effectiveness of the method.

### Strengths
1. The paper is well-written and easy to follow.
2. The illustrations are clear and help understand the paper.
3. The paper has new dataset contributions.
4. The experiment results are promising.

### Weaknesses
1. In Line 208, the authors claims that the local attention-based upsampler is worse than the global attention-based method when the objects are not canonical. I cannot see the logic behind. Maybe this is because the proposed method uses VI-PointConv in the encoder? I think the authors should provide more detailed investigation of this. The claim that local attention struggles with non-canonical objects needs more justification, particularly given that local attention mechanisms are often effective at capturing fine-grained details. It's not immediately clear why a global approach would inherently be better for non-canonical shapes, and the connection to the encoder's VI-PointConv is speculative and requires further analysis.
2. Some important details are missing.
- In Line 203, how does the global shape descriptor generated? The description should include the specific layers and operations used to generate the descriptor, such as the number of layers in the MLP, the activation functions, and the pooling method.
- In Line 206, why are the seeds called the patch seeds? There should be an explanation here. The term "patch seeds" is not self-explanatory and needs a clear definition in the context of this paper. It's not obvious how these seeds relate to patches or why they are necessary for the completion task.
- In Line 237, how is the tranposed convolution used? The explanation should specify the kernel size, stride, and padding used in the transposed convolution, and how these parameters affect the upsampling process. It's also important to clarify if any specific initialization is used for the transposed convolution.
3. How does the proposed method generalize to unknown objects during training? It's unclear how the method would perform on objects from categories not seen during training. This is a crucial aspect of any completion method, and the paper should discuss the limitations of the method in this regard, and how the method would perform on objects with different shapes and structures than those in the training set.
4. The organization of the paper should be improved. For example, scene-aware object completion (Sec 3.3) is part of the seed generator (Sec 3.2), and describing them separately makes the paper somehow confusing. The current structure makes it difficult to understand the overall flow of the method. The paper should clearly present the different components of the method and their interdependencies.

### Questions
Please address the questions in the weaknesses section.

### Soundness
3

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
4

### Summary
This paper argue that existing instance scene completion methods may neglect scene constraints when doing instance completion. To address these issues, they propose a point cloud-based instance completion model that utilizes scene constraints through a cross-attention mechanism for improved object completion at any scale or pose. Besides they introduce a new synthetic dataset, ScanWCF, to evaluate instance scene completion in indoor environments. Experiments show that their method outperforms existing techniques in terms of accuracy and plausibility.

### Strengths
I think the major contribution of the seed generator converted on top of SeedFormer, that allows the generator to use information from the entire scene to predict the center of the object before producing seed coordinates as offsets of the object center.

Another is the incorporation of a sparse set of scene constraints for seed generator and completion, providing scene context (e.g., other observed surfaces, free space, occluded space).

### Weaknesses
I think this is a good paper with sound method and formulation. However, from the technical contribution's perspective, this paper still follows the same "top-down" architecture as in RfDNet, and the performance's boost against baselines comes from the better quality of each individual module. The module this paper is mostly contributing is the object points completion module that completes object pointcloud from partial points given by leveraging the scene context/constraints.

### Questions
I am curious that if there are no scene constraints, how would the object completion module perform against the baselines?

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
This paper proposed an instance scene completion method for partial point cloud which consists of 3 stages: instance segmentation stage which extract each object from partial point cloud; object completion stage which predicts both complete shape and surface normals for each object; and mesh reconstruction stage which reconstruct scene meshes from point clouds. The focus of this paper is to propose a set of improvement and refinement modules to improve the object completion network. Furthermore, a new dataset for instance scene completion in indoor scenes has been proposed which has better ground truth labels than existing ScanARCW dataset. Experiment on the newly proposed dataset shows that the proposed method achieves SOTA performance on instance scene completion task.

### Strengths
This paper is a good practice to build a instance scene completion framework based on the core module of encoder-decoder object completion. There are several design improvements over existing work in the proposed method:
1. Use VI-PointConv to replace PointConv in the partial encoder module in object completion stage.
2. Use object center and offset prediction MLP to generate aligned seed patch in the Seed Generator module in object completion stage.
3. Incorporate the scene constraints into the Seed Generator module through cross-attention
4. Use global attention in upsample layers to improve the Coarse-to-Fine Decoder module in object completion stage.
5. Use surface normal prediction module which enables mesh reconstruction using existing NKSR method
All the above improvements have been verified in ablation study

Experiment shows that the proposed method significantly outperforms existing instance scene completion methods RfD-Net and DIMR (table 1&2)

The paper also proposed a refined dataset 'ScanWCF' which is declared to have 'Watertight and Collision Free' ground-truth, this could benefit future research on instance scene completion task

### Weaknesses
There are some concerns on the novelty and effectiveness of the declared main contributions, as the paper said, there are 3 main contributions, the first contribution is 'a novel object-level completion model which is robust to the scale and pose of objects found within scenes', but actually, the whole framework is to deal with instance scene completion, and in instance scene completion, there is no need to constrain the scale and pose of the objects in the scene. the second contribution is 'integrate a sparse set of scene constraints into our model to provide our object completions with scene context', while the corresponding ablation study in table 4 shows limited improvement on UHD and %COL metric. I think the presentation of this paper could be further improved to make the paper stronger

In the ablation study which focus on the object completion task (table 3), the performance improvement of each proposed module is relatively small and not very impressive compared with that on the scene completion task (Table 1&2), furthermore, each module is added separately, what is the performance with all modules included?



### Questions
Since existing instance scene completion method jointly train instance segmentation & completion model, while the proposed method uses existing Mask3D method for instance segmentation separately, is there any experiment comparison on the performance of instance segmentation? I may want to see whether the biggest peformance improvement is due to the use of Mask3D?

### Soundness
3

### Presentation
2

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
This work leverages joint scene and object information for object point cloud completion in the scene, which is a meaningful and important task. In order to boost completion, the work investigate both object-centric learning and scene occupancy information to guide the completion. In detail, it uses object transformers to generate patch seed in object-centric coordinate with an additional object coordinate, and use scene transformers to represent scene occupancy information. Then, a cross attention is used to combine the information for completion.

The experiments suggest significant improvement using the proposed method.

### Strengths
The authors address the point cloud completion task in the scene, which is a fundamental problem in 3D vision. They offer insights that the key for completion is to extract object-centric information in the scene, and combine useful global scanning information such as scene visibility/occupancy.

Accordingly, they provide a network that allow both insights to be implemented.

The idea is clear and the method is solid. Besides, I believe the design shows sufficient technical novelty that reaches the conference standard.

### Weaknesses
It may be worth discussing the limitation and quality of point cloud completion using the proposed method under different scenario, e.g., what is the requirement for noise/incompletion ratio for the method to succeed? Can it complete unseen objects?

### Questions
Check the weakness part.

### Soundness
4

### Presentation
3

### Contribution
3

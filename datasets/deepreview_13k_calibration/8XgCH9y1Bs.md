# 3D Object Representation Learning for Robust Classification and Pose estimation

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 5, 3

## Abstract
In this work, we pioneer a framework for 3D object representation learning that achieves exceptionally robust classification and pose estimation results. In particular, we introduce a 3D representation of object categories using a 3D template mesh composed of feature vectors at each mesh vertex. Our model predicts, for each pixel in a 2D image, a feature vector of the corresponding vertex in each category template mesh, hence establishing dense correspondences between image pixels and the 3D template geometry of all target object categories. The feature vectors on the mesh vertices are trained to be viewpoint invariant by leveraging associated camera poses. During inference, we efficiently estimate the object class and pose by matching the class-specific templates to a target feature map in a two-step process: First, we classify the image by matching the vertex features of each template to an input feature map. Interestingly, we found that image classification can be performed using the vertex features only and without requiring the 3D mesh geometry, hence making the class label inference very efficient. In a second step, the object pose can be inferred using a render-and-compare matching process that ensures spatial consistency between the detected vertices. Our experiments on image classification demonstrate that our proposed 3D object representation has a number of profound advantages over classical image-based representations. First, it is exceptionally robust on a range of real-world and synthetic out-of-distribution shifts while performing on par with state-of-the-art architectures on in-distribution data in terms of accuracy and speed. Second, the estimated object pose is competitive with baseline models that were explicitly designed for pose estimation, but that cannot classify images. Finally, we show that our model has an enhanced interpretability by visualizing the individual vertex matches and the ability to perform classification and pose estimation jointly and consistently.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Authors embed 3D geometry into learning a model for image classification.
Important part is identification between background and class-object features, this is done by contrastive repr. learning.

The method uses the fact that objects in the image are constructed from real 3D. The 3D is represented as a mesh of faces and vertices.  The authors learn matching between image features and their corresponding vertex location.

During the interference, the mesh is “rendered and compared” to minimize the likelihood of features.

Various classification experiments are performed. In addition, the 3d pose estimate is evaluated too.

### Strengths
Combining 2D and 3D for recognition is a great way to tackle classification. It opens many options for object representation.

The method looks clear. Although I did not check all the equations, the paper is written in way so it is understandable.

Many experiments (maybe too much) are presented. I especially like Sec 4.4.

### Weaknesses
Authors start the paper with the statement: “we pioneer a framework for 3D object representation..”, the statement is in contrast with various papers that investigate object representation using techniques on how to map image features to 3D models of faces and vertices. For example M1 or M2. 

Dataset creation - details in questions.

Baselines and 3D data - details in questions.

For example, missing papers:
M1: Choy et al. Enriching Object Detection with 2D-3D Registration and Continuous Viewpoint Estimation CVPR 15
M2: Start et al. Back to the Future: Learning Shape Models from 3D CAD Data
 BMVC 10

### Questions
\kappa (eq. 3) is fixed to constant, how is the parameter fixed? Is it from validation data, guess, tuning on testing data?

Does baselines use 3D? (It looks that authors use 3D but baselines don't).

Im puzzled in the dataset creation. Originally, pascal authors claim that 10812 testing images from Pascal3D+ are used to create Ocluded PASCAL3D (from official github page). Authors use 10812 Pascal3D+ images as a validation set. Is the authors validation imageset same as the testset in Ocluded Pascal? If so, then it does look like a bug in dataset creation. This question and the question above are look for me as crucial for deciding between acceptance or rejection.

However the conference is called Conf. on Learning Representation. The paper looks to be structured for a computer vision conference. For example, I would be more interested in how the proposed representation (and its modification) affects the result of how the method expresses the objects rather than many classification results that are provided (I'm not saying skip them all) and are better suited for cvpr-like venues. I would like to see some examples where the representation is beneficial to other methods and where it is in contrast worse.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel 3D object representation learning method for robust classification and pose estimation, exploring the establishment of dense correspondences between image pixels and 3D template geometry. The feature of a pixel in a 2D image is mapped to the corresponding vertex in a set of pre-defined 3D template meshes, which are further trained via contrastive learning and associated camera poses for classification. Finally, the poses are estimated by the refinement from the initial pose of the template.

### Strengths
1.	The motivation of this work, which is to learn representation from 3D template geometry, is technically sound and fits well into object representation learning.
2.	The design of the inference pipeline is highly efficient, where image classification can be achieved merely using vertex features.
3.	Extensive experiments verify the effectiveness of the proposed approach on 3D object representation learning and classification, and the accurate pose estimations further demonstrate the interpretability.

### Weaknesses
1.	All typos should be checked and corrected to improve writing quality (e.g., in the first paragraph of the Introduction Section, "… gradient-based optimization on a specific training set (Figure ??).").
2.	There is a lack of an efficiency comparison with existing methods. It seems that the high efficiency in classification is a critical contribution of this work. A comparison of the inference speed and the number of parameters between the proposed framework and other methods can further support this claim.

### Questions
Please refer to the weaknesses listed above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper claims that they propose a 3D object representation at the object category-level that can be used for object classification and 3D object pose estimation.
They represent each object category as a cubic with attached features in each vertex, which are trained using multi-view posed images.
Then, the features are used to classify the object category by directly matching the image feature map with each category's 3D features and estimating the pose of the object in the image using render-and-compare.

### Strengths
1) The proposed method uses trained 3D features of each category of object classification, instead of performing 3D object pose estimation only, which is pretty interesting since the 3D features can further be leveraged.

2) Visualizations are attached to show the interpretability of the 3D features.

### Weaknesses
1) More detailed discussions and comparisons with NeMo. NeMo is highly related to the proposed paper, but the discussion is missing in the introduction and related works. As far as I can see, the 3D object representation in the paper is already proposed by NeMo. NeMo already finds that using a cubic for an object class can achieve good performance in 3D pose estimation. They also use contrastive loss for training and render-and-compare strategy for pose estimation as in this paper. I think the difference is that the paper extends this existing 3D representation to training on multiple categories and uses it for classification. Based on this point, I think a huge part of the contributions of this paper belong to NeMo, and the real contributions are limited.

2) For the evaluation of classification, I think the paper should compare with the state-of-the-art 2D object detectors for classification to show the advantages. For example, I think the YOLO can be easily trained using the same training data as the proposed method, i.e., the projected 2D bounding boxes from the 3D cubics.

### Questions
Please refer to the weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a method for joint object classification and 3D pose estimation from a single image. 
The core idea is that by doing joint pose estimation and classification, the classification results are more robust in scenarios with challenging occlusion and image corruption.

Each object class's 3D shape is modelled using a dense 3D mesh. Each vertex has a feature descriptor designed to be pose invariant. 
The calssification network uses a backbone to detect 2D features, and the next computes the similarity of each 2D feature to the viewpoint-invariant features for each of the 3D vertices of an object class mesh, computing scores (these essentially produces dense 2D-3D correspondences). These scores are used to compute overall per-class scores to perform classification. A set of background features are used to represent the background class. In a second step (not needed for classification), the object pose is computed for the selected object using the 2D-3D dense correspondences using a render-and-compare approach starting from multiple initialisations.

At training time, featrures for 3D vertices and 2D features prameters are compute jointly. Contrastive learning is used to make the 3D features viewpoint invariant (enforce similarity for 3D features corresponding to the same vertex from different viewpoints,  and doing the opposite for 3D features for different vertices or different objects).

The method is evaluated on both object classification on standard benchmarks (Pascal 3D, a heavily occluded version of it, OOD-CV2 for out of distribution samples), and compared against some baselines.

### Strengths
- The paper is well written and easy to understand
- The results of the method are convincing, and demonstrate one of the paper claim, i.e. that 3D reasoning makes the approach more robust to occlusions and challenging image conditions.
- The paper is evaluated on standard benchmarks, with reasonable ablation analysis
- The method has some interesting interpretability properties, for example by looking at vertex activation output it is possible to understand which parts of the object are occluded in the image

### Weaknesses
My main concern with this paper is lack of novelty, in particular with respect to: "Neural Textured Deformable Meshes for Robust Analysis-by-Syntheses" by Wang et al. (which is cited in the submission). This paper seems to follow the same procedure, using mostly the same techniques (feature extraction, 3D mesh representation, contrastive divergence to make 3D features more invariant, etc.). There seem to be some differences (e.g. it seems the submission the 2D to 3D matches is done differently, and the submission, unlike Wang et al., allows to do classification without the more computationally expensive step of 3D pose estimation, but I am not certain), but these differences are not explained in the submission, nor seem significant enough to warrant sufficient novelty. Moreover, Wang et al. achieve very comparable results, and in some cases superior performance (e.g. for L3) on Occluded PASCAL3D+ (Compare Table 1 in Wang et al. to Table 1 in the submission). I would have expected a much more detailed comparison to the most relevant papers (in particular "Neural Textured Deformable Meshes for Robust Analysis-by-Syntheses" by Wang et al.), with clear articulation of what the diffrences are, and pros and cons of the proposed method with respect to these alternatives

I also think some claims are not adequately supported by the results, for example "exceptionally robust classification and pose estimation results" as claimed in the abstract

### Questions
1) Could you please provide a detailed explanation of the differences with respect to the most similar approaches (all work by Wang et al., in particular Wang et al. 2023)? 
2) Is it possible to compare to Wang et al. 2023 on the corrupted Pascal3d+ dataset?

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

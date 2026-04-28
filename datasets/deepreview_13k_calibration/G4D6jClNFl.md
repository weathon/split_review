# Deepfake Detection with Contrastive Learning in Curved Spaces

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 5, 6, 5

## Abstract
Deepfake detectors excel in familiar scenarios but falter when faced with new generation techniques. Improving their generalization can be achieved through synthetic data during training or using one-class anomaly detection methods. However, existing techniques, limited to non-negative-curvature spaces, struggle to effectively identify counterfeit features on the intricate and diverse non-Euclidean human face manifold. Human faces defy simple Euclidean geometry due to their complexity. To overcome this limitation, we introduce a novel and efficient deepfake detector, called CTru, that learns a rich representation of facial geometry across multiple-curvature spaces in a self-supervised manner. During inference, the fakeness score is computed by integrating angle-based similarity in spherical space and model confidence in hyperbolic space with Busemann distance. CTru establishes new SoTA results on various challenging datasets in both cross-dataset and cross-manipulation scenarios, while being trained only on pristine faces, highlighting its impressive generalization performance. Code source will be made available.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a framework, CTru, for fakeface detection. The idea is to project face features into different geometric spaces, and combine the projections into a loss function to learn the encoder with contrastive learning. Some experimental results have been shown for demonstration.

### Strengths
Slightly better results.

### Weaknesses
1. Novelty: The paper integrates several existing techniques widely used in the computer vision community for the application of fake face detection, with no theoretical justification. Why does such an integration work? Why not other ways? This is one of my major concerns as a publication in ICLR, as to me I feel learning nothing from the paper.

2. Writing: I am not clear how Eqs. 2 and 7 are implemented. Eq. 2 is for generating “high” quality fake images, but why is “high” quality? The description lacks specifics regarding the augmentation techniques used and how they simulate realistic fake artifacts. Eq. 7 is for making decisions, but “how”? The paper does not clearly explain the decision-making process during inference, specifically how the fakeness score is used to classify images as real or fake.

3. Experimental results are slightly higher than the approaches that all are before 2023. Not sure if they are state-of-the-art.

### Questions
see my comments

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to learn deepfake detection representations across multiple-curvature spaces in a self-supervised manner. The detection results combine advantages of both positive and negative curvature spaces. Experimental results validate the effectiveness of the proposed method.

### Strengths
1. The proposed model is the first attempt to learn representations across multiple-curvature spaces for deepfake detection. 
2. The proposed abnormal face generation method can generate fake faces of many different types.
3. The experimental results show that the proposed model has satisfactory deepfake detection performances.

### Weaknesses
The reason to combine both negative and positive curvature representation spaces in deepfake detection is not insightful. This makes the paper merely a combination of existing techniques.

(1) The authors only emphasize that the Euclidean-based distances appear sub-optimal for faces as the complexity and nature of human faces go beyond a basic Euclidean manifold. This explanation is vague and general, thus not convincing. 
(2) As I know, using hyperbolic space representations always work well for the tasks with hierachical relation nature. However, the authors fail to explain the inherent hierachical relations in deepfake detection tasks.

### Questions
I suggest the authors give more detailed and insightful analysis to explain the motivation of using curved spaces.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors propose building facial features by incorporating principles of hyperbolic geometry and using a contrastive loss on a hypersphere to aggregate similar faces, thereby achieving the goal of detecting forged faces. In general, this paper presents a promising approach that contributes to the advancement of deepfake detection.

### Strengths
1. An interesting method for constructing facial features.
2. An effective attempt for using contrastive loss to detect deepfakes.

### Weaknesses
1. The authors should provide more case studies in the main manuscript, including new features in Section 3 and facial features after clustering using contrastive loss.
2. More analysis on efficiency should be added, such as overall training time, parameters, and convergence steps.
3. It is suggested that the authors consider applying this method to other well-known backbones, such as Xception.

### Questions
na

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper considers the problem of face deepfakes detection. It uses a supervised contrastive learning where a prior set of possible 
modifications/alteration  of faces is used as data augmentation. The main novelty of the paper comes from the use of a mixed curvature space
for the embedding, designed as a product of hyperspherical and hyperbolic geometries. Within this geometries, prototypes are defined 
as corresponding to the different classes of possible alterations of pristine faces. Then a dissimilarity measure to those mixed-space prototypes 
is defined as a combination of a distance over the sphere and a measure of alignment with a hyperbolic prototype thanks to the Busemann 
function. A detection score is crafted as a product of similarity in the hyperspherical embedding and a confidence score in the hyperbolical space
defined as the distance to the origin. Thorough experiments are conducted on the FaceForensics++ dataset, and comparisons with SOTA approaches 
reveal added value of the mixed-space representation.

### Strengths
- Empirical evidences thorough experiments of enhanced detection performances with the proposed method ;
 - although I am not an expert in deepfake detection, the considered SOTA seems relevant and complete

### Weaknesses
 - the paper combines two well-known strategies (contrastive learning on an hypersphere embedding and Busemann prototypes
from the Ghadimi et al. Neurips paper). The amount of novelties with this respect is low, and one could expect from such a paper
a better justification of the choice of this mixed-curvature space besides ‘the manifold of faces is complicated and non-Euclidean’.
Notably, it is not clear which aspects necessary to deepfake detection is captured by the two geometries 
- some details are missing from the experimental part (see my questions below). The ablation study is not fully convincing to me 

All in all, and though the proposed approach seems novel and has merits, it seems to me that the paper would be more suited and  impactful in the computer vision community, as far as the novel insight wrt. representation learning are rather limitated.

### Questions
- in the experimental section, I did not see the dimensions used fo both embeddings (I may have overlooked). Are they comparable to what is used in  other supervised contrastive learning strategies ? What is the impact of those dimensions on performances ? 
- in the ablation study, do you keep the total number of dimensions constant (e.g. if S^100 + H^100 is used, do you compare with a hyperspherical embedding with dimension S^200 ?) I really believe that this question (effectiveness of combination of spherical and hyperbolic geometry) is unsufficiently detailed in the paper)

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

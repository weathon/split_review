# FLNERF: 3D FACIAL LANDMARKS ESTIMATION IN NEURAL RADIANCE FIELDS

- Decision: Reject
- Avg Score: 4.33
- Scores: 3, 5, 5

## Abstract
\vspace{-0.1in}
This paper presents the first significant work on directly predicting 3D face landmarks on neural radiance fields (NeRFs). %without using intermediate representations such as 2D images, depth maps, or point clouds. 
Our 3D coarse-to-fine Face Landmarks NeRF (FLNeRF) model efficiently samples from a given face NeRF with individual facial features for accurate landmarks detection. 
Expression augmentation 
is applied to facial features in a fine scale to simulate large emotions range including exaggerated facial expressions (e.g., cheek blowing, wide opening mouth, eye blinking) for training FLNeRF. %With such expression augmentation, our model can predict 3D landmarks not limited to the 20 discrete expressions given in the data.  
Qualitative and quantitative comparison with related state-of-the-art 3D facial landmark estimation methods demonstrate the efficacy of FLNeRF, which 
contributes to downstream tasks such as 
high-quality face editing and swapping with direct control using our NeRF landmarks. Code and data will be available.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper presents a model, termed FLNeRF, for estimating 3D facial landmarks from a face NeRF representation. In a first step it performs a coarse sampling of the NeRF volume to obtain an initial estimate of the face parameters. In a second step it re-samples again, at a finer scale, the face, eyes and mouth spatial locations. In both steps the reconstructed face volume, combined with positional encoding,  are the input to a CNN that estimates the face pose and the configuration parameters of a bi-linear model (a compressed version of FaceScape's) representing identity and expression, from which a set of 3D landmarks can be produced.

The experimentation evaluates the accuracy of the estimated landmarks so as their use for face editing and swapping.

### Strengths
The paper is easy to read and the problem addressed, face landmark estimation, is quite significant, with relevant applications and theoretical issues.

### Weaknesses
As the abstract reads, the central claim in the paper is that the approach can accurately estimate 3D face landmarks surpassing existing single or multi-view approaches. Also, since the starting point of the approach is a NeRF, to stress its practical use, the last sentence in section 2 reads "We will show our FLNeRF can be generalized to estimate 3D face landmarks on 2D in-the-wild images, using face NeRFs reconstructed by EG3D Inversion."

The paper does not convincingly demonstrate any of these claims.

The proposed approach is compared with the reconstructions computed with the landmarks detected with 2D methods and the 3D landmarks obtained with 3D methods in terms of the average Wing loss values multiplied by 10. I have several comments concerning this experiment:
- The evaluation is performed with 5 identities from the test dataset from FaceScape.  While this experiment provides some information, a sound comparison should include several other benchmark datasets in the literature and a widely used metric, such as e.g. the mean, median and std reconstruction errors.
- Is the comparison fair?  I have doubts since FLNeRF was trained with a train set from FaceScape, whereas competing approaches seem to have been trained with different datasets.
- In 2D datasets landmarks around the jaw do not have a fixed location, but rather represent the face occluding contour, so a reconstruction from their correspondences does not make much sense.

Finally, the experimentation concerning the estimation of landmarks on in-the-wild images, was made with a single image of president Obama, in which the estimated landmark locations are not very good.

### Questions
The authors should elaborate more on the complexity of estimating a detailed NeRF from an image, compared to a set of facial landmarks, and what are the advantages of estimating the landmarks from the NeRF, rather than from the image.

Specific questions:
- Is the comparison in Table 1 fair?
- Does a test on a single image provide sufficient experimental support to conclude that FLNeRF can be generalized to estimate 3D face landmarks on 2D in-the-wild images?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a NERF based approach for predicting 3D face landmarks directly from neural radiance fields. This NeRF based solution is shown to surpass existing single or multi-view image approaches. The proposed 3D coarse-to-fine Face Landmarks FLNeRF model samples from a given face NeRF individual facial features for landmarks detection. Expression augmentation is applied at facial features in fine scale to simulate large emotions range including exaggerated facial expressions for training FLNeRF.

### Strengths
- The work presents a first contribution in using NERF for face landmarks detection in 3D. 
- Results seems promising. 
- The paper is presented in a good way.

### Weaknesses
 - A NERF model is normally constructed for each 3D object to render. This limitation seems to apply also to this work. This represents quite a drawback for the proposed solution in that a different NERF model should be constructed for each identity. This drastically reduces the generality of the approach and results in a substantially increased computational effort that appears to be not much compatible with a problem of landmarks detection.
- Based on the above, the comparison with other methods that do not incur in such limitation is not completely fair in my opinion. Authors should at least clarify this point. 
- In Section 3.5 it is reported that only five identities have been used in the test dataset. This appears as an insufficient number to derive a complete understanding of the proposed solution in comparison to state-of-the-art approaches. This very small number of identities does not have a sufficient statistical significance. 
- It is not clear how much of the performance derive from data augmentation. A better insight of this should be provided.
- Limitations of the proposed method have not been discussed. 

Minor corrections:
- Caption of Table 2: “by method described” --> by the method described

### Questions
Q1: A NERF model is normally constructed for each 3D object to render. This limitation seems to apply also to this work. This represents quite a drawback for the proposed solution in that a different NERF model should be constructed for each identity. This drastically reduces the generality of the approach and results in a substantially increased computational effort that appears to be not much compatible with a problem of landmarks detection. Can author clarify this point? 

Q2: Based on the above, could the authors present the results in a better way so that the comaprison account for other aspects than only accuracy?

Q3: It is not clear how much of the performance derive from data augmentation. A better insight of this should be provided.

### Soundness
2 fair

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, a facial landmark detection algorithm is proposed on the NeRF-generated 3D face images. The proposed method follows the coarse-to-fine approach. It first samples the 3D face image from face NeRF. It then detects the coarse facial landmark locations given the frontal face. Then, the fine model will refine the accurate landmark locations based on the estimated coarse locations from the previous step. The experimental results have been conducted to demonstrate the effectiveness of the proposed method.

### Strengths
It is interesting to see the facial landmark detection algorithm on the face NeRF images. The final detection accuracy seems to be significantly better than the other works.

### Weaknesses
The 3D facial landmark detection algorithm itself is straightforward. Once the 3D face is sampled from face NeRF, a typical detection algorithm is used.

The experiments are limited, and the novelty of the method is not fully justified. The choice of feature and loss function in the coarse model (Equations 3 and 4) lacks sufficient explanation. The comparison with baseline methods in Table 1 needs further clarification, particularly regarding the use of single images for 3D detection in some baselines and the triangulation method.

### Questions
The authors should further justify the novelty of the proposed method.
It is not very clear how the feature and loss function are selected in the coarse model in Equations 3) and 4). 
The authors should justify if the comparison of the proposed methods with other baseline methods in Table 1 is fair. Some of the baseline methods are only using 1 image for 3D detection. It is also not clear how the `triangulation` based method is done if detection is only from 1 2D image.
Is that possible to directly train/detect facial landmarks during face NeRF construction or to learn the mapping between face NeRF images and 3D landmark locations?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

# Divided Attention: Unsupervised Multiple-object Discovery and Segmentation with Interpretable Contextually Separated Slots

- Decision: Reject
- Scores: 5, 5, 6, 5

## Abstract
We introduce a method to segment the visual field into independently moving regions in real-time, trained without ground truth or supervision, needing neither pre-trained image features nor additional data outside the domain of interest. The model consists of an adversarial conditional encoder-decoder architecture based on Slot Attention, modified to use the image as context to decode optical flow without attempting to reconstruct the image itself. One modality (flow) feeds the encoder to produce separate latent codes (slots), whereas the other modality (image) conditions the decoder to generate the first (flow) from the slots. This design frees the representation from having to encode complex nuisance variability in the image due to, for instance, illumination and reflectance properties of the scene. Since customary autoencoding based on minimizing the reconstruction error does not preclude the entire flow from being encoded into a single slot, we design the loss with an adversarial criterion based on Contextual Information Separation. The resulting min-max optimization fosters the separation of objects and their assignment to different attention slots, leading to Divided Attention (DivA). DivA outperforms recent unsupervised multi-object motion segmentation methods while tripling run-time speed up to 104FPS and reducing the performance gap from supervised methods to 12% or less. DivA can handle different numbers of objects and different image resolutions at training and test time, is invariant to the permutation of object labels, and does not require explicit regularization.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper presents Divided Attention (DivA), an unsupervised method for segmenting visual fields into independently moving regions without manual supervision. The model uses an adversarial conditional encoder-decoder architecture with interpretable latent variables, building on the Slot Attention architecture. It's designed to decode optical flow using the image as context without reconstructing the image itself, thus avoiding issues with complex image variability. DivA can handle varying numbers of objects and resolutions, is invariant to object label permutations, and doesn’t require explicit regularization or pre-trained features. It achieves high run-time speed (up to 104FPS) and narrows the performance gap with supervised methods to 12% or less. The code will be made available upon publication.

### Strengths
+ This paper is well-written and easy to follow.  
+ The model is capable of inference speeds up to 104FPS, significantly faster than current unsupervised methods.  
+ The method does not rely on pre-trained image features from external datasets, enabling its use in a broader range of scenarios.

### Weaknesses
Firstly, I suggest the authors pay attention to the terminologies: in the title and introduction, the authors claim to do multi-object discovery/segmentation. However, they are actually doing moving object segmentation. "regions of an image whose corresponding motion is unpredictable from their surroundings" This should be the definition of moving objects but not objects. In other words, for some datasets with both moving and non-moving objects, such as MOVI-D, the proposed method will fail to work. 

Secondly, I think the novelty/contribution of this work is limited. Reconstructing in the flow space with slot attention has been widely explored before, e.g. SAVI, the conditional decoder and the adversarial loss is also somewhat not quite novel. 

Moreover, there is no explanation why the author wants to take flow as the input and reconstruction space but RGB as the condition rather than take RGB as the input but flow as the condition. More ablations regarding this should be conducted. Also, quantitative results for the ablation with adversarial decoder should also be reported as that's one of the claimed contributions.

Finally, more visualizations should be included, at least in the supplementary.

---------------------
Thanks again for the quick reply.

For R1, I think I understand what the authors claimed -- the definition of the ``object'' is proper and in principle, the non-moving object can be captured in real practice, with the proposed method. However, I still doubt if that's the case -- it's hard to predict the results unless seeing the results.

For R2, the discussions for those references sound promising. Though one minor thing is, for [4], the authors have ablations to verify that their method can still work without pre-trained features -- they can first train the ViT from the target dataset and then do object discovery in that space. Not to mention both [3] and [4] require no additional data (flow) but just the RGB images.

I respect the effort of the authors during the rebuttal stage and would like to slightly upgrade my rating, but will not champion this paper.

### Questions
See previous section.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work introduces Divided Attention, an extension of the Slot Attention Network (SAN) for unsupervised multi-object discovery in real-time. Divided Attention takes both the RGB image and optical flow as inputs, and learns a set of “slots” as encodings that can reconstruct the optical flow. By constructing the optical flow (instead of image reconstruction in typical SAN), the model can focus on separating the objects in the scene and understanding their motion, rather than overfitting to the relatively less related visual details such as illumination and texture. Another key component is an adversarially trained flow decoder, which attempts to reconstruct the entire flow from each individual slot (the main decoder reconstructs the flow only within each mask). By employing this adversarial training, the slots are encouraged to learn “contextually separated” encoding of the scene, and consequently result in separated, interpretable object representations.

### Strengths
- This work proposes to leverage optical flow for unsupervised multi-object discovery. In a video setting, it is more intuitive to extract information from the motion of pixels, and discover coherent regions as independently moving objects.

- Divided Attention does not require any pre-trained visual features, and thus is more flexible to be applied in various applications. Moreover, its training and inference can use a dynamic number of slots, depending on the context.

- The model is very efficient, enabling real-time inference speed.

### Weaknesses
- Flow input: In real-world practice, optical flow has to be obtained by running a flow estimation algorithm (e.g., RAFT). This would raise two concerns: 1) The flow estimation model is pre-trained with external knowledge and data in a supervised manner, which somehow contradicts with the claim that Divided Attention is unsupervised and requires no pre-trained features. 2) If we take the inference time of the flow estimation model into consideration, the FPS of the whole pipeline would be decreased, and achieving the real-time application would be more challenging.

- Temporal consistency: In the base version of Divided Attention, temporal consistency across frames is not guaranteed. Additional tricks (e.g., inheriting slots from previous frames, or post-processing results of multiple frames) need to be incorporated for temporal consistency. This is not desirable considering the main application is object segmentation in videos.

- Missing ablation study: It is suggested to quantitatively examine the design choices in Divided Attention via ablation study experiments. For example, $\lambda$ in the adversarial training, the model architecture, and the number of slots during training and inference, should be tested with different choices for justification and better understanding of the proposed method, Divided Attention.

### Questions
- In Table 1, why are the FPS of some baselines (including DyStab) not listed?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a method to segment the visual field into independently moving regions. The proposed method uses a cross-modal conditional decoder that takes a second modality as input  to reconstruct the first modality.  This design frees the representation from having to encode complex nuisance variability in the image, such as illumination and reflectance properties of the scenes.

### Strengths
This paper is well-written and easy to follow.

The experimental results demonstrate better performance.

The idea is simple and effective.

### Weaknesses
I cannot find the obvious weakness.

### Questions
How about the GPU memory consumption?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed a motion segmentation method to segment multiple objects, based on optical flow in an unsupervised manner. In this setting, both images and optical flow are available. Based on the SAN method, this work proposed an adversarial conditional encoder-decoder architecture. The proposed method can handle different numbers of objects at training and test time. The experimental results demonstrate the effectiveness of the proposed method.

### Strengths
(1) It can handle different numbers of objects at both training and test time.

(2) It can run in real-time.

(3) The performance is good.

### Weaknesses
(1) The ability of handling multi-object comes from SAN. The main contribution may be the adversarial framework and the manner using the image information. The authors should highlight the contributions of this paper.

(2) Handling multi-object is not new in video object segmentation.

(3) Why g_theta is an "adversarial" decoder is not clear. It forces the decoder to reconstruct the entire flow with each slot, which seems the two decoder do not have an adversarial relationship. 

(4) This method "frees the representation from having to encode complex nuisance variability in the image", which should be demonstrated in the experiments. For example, simply combining (concat) the image and the optical flow as input can be considered as a baseline. Although the authors mentioned combined input is complex and the slots are low-dimentional. More reasonable explanation is needed.

(5) This setting is interesting,  but I guess its performance is heavily related to performance of the optical flow network. In the inference stage, the optical flow is also need to calculate first. 

(6) P4, DivA has two key advantages, but the following text is mainly about the disadvantages of MoSeg.

### Questions
see the weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

# JointNet: Extending Text-to-Image Diffusion for Dense Distribution Modeling

- Decision: Accept
- Scores: 3, 8, 6, 5

## Abstract
We introduce JointNet, a novel neural network architecture for modeling the joint distribution of images and an additional dense modality (e.g., depth maps). 
JointNet is extended from a pre-trained text-to-image diffusion model, where a copy of the original network is created for the new dense modality branch and is densely connected with the RGB branch. 
The RGB branch is locked during network fine-tuning, which enables efficient learning of the new modality distribution while maintaining the strong generalization ability of the large-scale pre-trained diffusion model.
We demonstrate the effectiveness of JointNet by using RGBD diffusion as an example and through extensive experiments, showcasing its applicability in a variety of applications, including joint RGBD generation, dense depth prediction, depth-conditioned image generation, and coherent tile-based 3D panorama generation.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The method tries to use text to image diffusion models to address different applications in vision such as monocular depth estimation.

### Strengths
+ The work seems to be well-motivated and has addressed an important field.

### Weaknesses
 - The work is not evaluated that well. For example, monocular depth estimation is not compared with several SOTA methods.

- The work is inferior compared to the other methods.

- The work tries to do many things but is irrelevant in all of them. 

- The work needs to be presented well with proper comparisons and illustrations.

### Questions
What is the primary contribution of this work?

What benefit it has for the user provided that this method is not giving best results for all the applications mentioned?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors introduce a neural network architecture for modeling the joint distribution of images and an additional "dense modality". The leading example of a dense modality is a depth map. Measurement of depth maps has important applications in designing self-driving cars, among many other use cases.  

The procedure takes as an input a pre-trained text-to-image diffusion model. This model is copied and used as an initialization to model the additional dense modality. The weights of the original model are then locked and used to generate the RGB component. The copied model is then trained on a relevant dataset. In this way, the good performance of the input model for the RGB component is maintained.

### Strengths
The paper is very clearly written and provides a practical solution to an important problem. Their evaluation and assessment of their method is extensive and credible. They make several comparisons to alternative procedures, and provide a convincing argument that their approach is appropriate.

### Weaknesses
As the authors note, the procedure requires doubling the size of the input diffusion model. This structure becomes cumbersome if it is repeated for several modalities. I encourage future work on assessing the performance of a single additional model for the generation of several modalities.

### Questions
I have have no questions at this time.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed JointNet for modelling the joint distribution of images and dense information, e.g., depth and normal maps. JointNet is extended from a pre-trained text2img diffusion model by adding a copy of the original network as the new dense modality branch, densely connected with the RGB image branch, and while training the original network is locked. The proposed method extends the text2img diffusion models to more applications such as RGB-D generation, depth precautions, etc. Experiments show the improvements compared with previous methods.

### Strengths
This paper proposed a joint network that differs from previous fine-tuning methods or control-net which shows some novetly. The idea of using joint and RGB information bidirectional is natural and interesting. The instruction of the network architecture and training details are proposed. The proposed method could be used for other applications such as depth prediction.

### Weaknesses
Although the method compared with other methods on different applications to show the effectiveness. However, the experiments to show ablation study is not clear and also the comparison with control-net (the one that inspired the proposed method) is not clear.



### Questions
- How is the comparison between control net with the proposed method? Although the two methods focus on different targets and applications, it is still possible to test on the same task, e.g., change the noise from joint to regular RGB task, or evaluate on the inpainting task that works for both architecture. 
- It is not clear if combine (a) and (b) in Figure 2 works well or not, e.g., use the same control net architecture but change the output as the joint and RGB, as based on Table 1 the numerical results are comparable and not that significant improved. 
- The ablation study is not sufficient, it is good to show different strategies or detailed architectures.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces JointNet, a novel neural network architecture that seeks to model the joint distribution of images and a dense modality like depth maps. Originating from a pre-trained text-to-image diffusion model, the architecture generates a replica of the initial network for the dense modality, integrating it densely with the RGB branch. Simultaneously, it locks the RGB branch during fine-tuning, ensuring the preservation of the generalization capabilities of the pre-trained model. JointNet’s efficacy is validated across various applications, including joint RGBD generation, dense depth prediction, and 3D panorama generation, positioning the paper as a noteworthy contribution to the field of joint distribution modeling. It highlights a resourceful and efficient strategy that capitalizes on pre-trained models to enhance performance in computer vision tasks.

### Strengths
- The proposed methodology introduces a novel technique for modeling the joint distributions of images and dense labels.
- JointNet successfully maintains the intricate details in the depth maps, showcasing its refinement capabilities.
- The qualitative results are impressive, especially on the panoramic image and depth generation.

### Weaknesses
 - The performance enhancement provided by the proposed network is marginal. According to Table 1, while JointNet outperforms Direct Extend in terms of IS, it falls short in FID and CLIP scores. Considering the network design is a primary contribution of this paper and differs significantly from Direct Extend, the results from Table 1 suggest only a slight improvement in performance due to the proposed network structure. Specifically, the FID score, a measure of image quality and diversity, is worse for JointNet, indicating that while the inception score might be better, the overall quality and diversity of generated images is not improved, which is a critical aspect for generative models.
- Table 2 reveals that JointNet on its own yields poorer results compared to MiDaS. Although performance improves when combined with MiDaS, the enhancement is minimal, as seen in metrics such as AbsRel (improving from 0.0568 to 0.0561) and a decrease in RMSE (from 0.0601 to 0.0634). These results question the effectiveness of the proposed methods. The absolute relative difference (AbsRel) shows a negligible improvement, and the increase in Root Mean Squared Error (RMSE) suggests a potential degradation in depth map accuracy, which is concerning. The small changes in these metrics do not justify the complexity of the proposed architecture.
- Given the marginal performance difference between the proposed method and MiDaS, one could generate images using diffusion models, input them into MiDaS, and obtain high-quality images and depth maps, raising questions about the necessity of RGBD generation methods. This highlights a significant concern about the practical utility of the proposed method, as a simpler pipeline might achieve comparable results without the need for a complex joint model.

### Questions
- Does MiDaS+JointNet in Table 2 refer to initially extracting the depth map using MiDaS and subsequently refining it with JointNet? Could you please clarify?
- Are the results depicted by JointNet in Figure 4 and ‘Ours (depth)’ in Figure 3 associated with 'JointNet (Ours)' or 'MiDaS+JointNet' as mentioned in Table 2?
- If these results pertain to JointNet, the discrepancy between its quantitative performance in Table 2 (lower than MiDaS’s results) requires further explanation.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

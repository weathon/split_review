# Towards Multiple Character Image Animation Through Enhancing Implicit Decoupling

- Decision: Accept
- Scores: 5, 6, 6, 6

## Abstract
Controllable character image animation has a wide range of applications. Although existing studies have consistently improved performance, challenges persist in the field of character image animation, particularly concerning stability in complex backgrounds and tasks involving multiple characters. To address these challenges, we propose a novel multi-condition guided framework for character image animation, employing several well-designed input modules to enhance the implicit decoupling capability of the model. First, the optical flow guider calculates the background optical flow map as guidance information, which enables the model to implicitly learn to decouple the background motion into background constants and background momentum during training, and generate a stable background by setting zero background momentum during inference. Second, the depth order guider calculates the order map of the characters, which transforms the depth information into the positional information of multiple characters. This facilitates the implicit learning of decoupling different characters, especially in accurately separating the occluded body parts of multiple characters. Third, the reference pose map is input to enhance the ability to decouple character texture and pose information in the reference image. Furthermore, to fill the gap of fair evaluation of multi-character image animation in the community, we propose a new benchmark comprising approximately 4,000 frames. Extensive qualitative and quantitative evaluations demonstrate that our method excels in generating high-quality character animations, especially in scenarios of complex backgrounds and multiple characters.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
In this work, the authors propose solutions for challenges in image animation, such as instability under complex backgrounds and multi-person scenarios. To enhance quality in these situations, three additional guides are introduced: optical flow, depth order, and reference pose map. The network design is similar to previous methods which include ReferenceNet, denoising U-Net, and inserting a temporal module in the second stage. Experiments demonstrate that the proposed methods outperform existing approaches, but more experimental results should be provided.

### Strengths
1. This paper proposes to integrate three additional guiders, optical flow, depth order, and reference pose map to improve the animation performance under complex backgrounds and multi-character situations (mostly two persons). 

2. The animation results are impressive and better than other methods, which demonstrate the efficiency of the proposed solutions.

### Weaknesses
1. The claim that the depth order map provides positional information for multiple characters is somewhat confusing. In practice, you first use the dilate-skeleton map to determine the positions of individuals, and subsequently obtain the depth order using depth information. 

2. The results in the paper only involve two individuals. To support the claim of handling multiple characters, it would be beneficial to include examples with more than two characters.

3. The pose sequences for two persons in a video are all the same, I think more results in different pose sequences for different characters should be provided.

4. The network design follows the previous methods, like MagicAnimate, which includes ReferenceNet, denoising U-Net, and inserting a temporal module in the second stage. I think Figure 3 can be improved to better demonstrate the network architecture.

### Questions
1. I am curious about scenarios where two individuals have significant interactions.

2. I think that the results in Figure 2 should reference the specific previous methods used for these issues.

### Soundness
2

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
3

### Summary
The paper proposes a new image-based pose retargeting/character animation diffusion model. The key contributions lie in how the proposed method handles (1) noisy backgrounds, which may degrade the quality due to spurious correlations, (2) explicitly capture the depth-order to enable more accurate generation for multi-character retargeting, and (3) enhance decoupling of appearances and body pose representation to achieve better texture quality.

The experimental results show that the proposed method achieves higher perceptual quality, both quantitatively and qualitatively.

### Strengths
The core strength of the method lies in the attention to the details. Specifically, 
- By explicitly considering the depth order, the method disambiguates the spatial arrangement in multi-character settings, and therefore enables the model to learn better, and render with higher fidelity.
- By providing the pose for the reference image, the model can better decouple the texture and pose information (although it is still implicit). Despite being simple, this design appears to have a great positive impact on the generation quality (in Figure 10).
- The background optical flow mitigates the spurious correlations that hinder the model from focusing on character animation.

Overall, the presented method is sound, and the effectiveness of each proposed component is sufficiently verified through their experiments.

### Weaknesses
 - The proposed method is computationally heavy (line 417-420, needs 8 A100 GPUs for training), making it less accessible to possible end users. This is, however, a common issue among diffusion-based methods, not particular to the paper.
- The depth-ambiguity is not completely resolved. One can see in the supplementary video 00:44, the top-left character has their hand rendered to the back incorrectly.
- The method focuses on front-facing poses. It is unclear how it performs on extreme poses with 360-degree rotation, and also poses like handstand, etc.

### Questions
I am overall positive about the submission. It would be nice if the authors can discuss a bit more about the following questions, in addition to the weaknesses raised above:
- What is the inference cost? Would it be able to run on commodity-level GPUs (e.g., Nvidia 2060, 3070, etc). I may have missed it, but it seems like only A100 is mentioned, and that is for training.
- How does the ```Ref Pose Guider``` handle multi-character skeleton maps. Do we assume there is a fixed number of character in the video?

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
Existing human animation methods struggle with multi-character animation tasks and are difficult to train on data with unstable, noisy backgrounds. This paper addresses these challenges with two main motivations: to decouple background motion from static elements and to separate multiple characters. To this end, the authors propose a novel framework that includes an optical flow guider and a depth-order guider.

The optical flow guider encodes background motion, while the depth-order guider captures the spatial relationships among multiple characters. Additionally, a reference pose guider is introduced to encode the pose of a reference image, simplifying the textual remapping process.

Evaluations on multi character benchmark demonstrate that this method generates high-quality character animations when trained on noisy web-collected datasets.

### Strengths
- The paper identifies a key challenge in training human animation models on in-the-wild data—the instability of background motion—and proposes a pipeline to address this issue.
    
- An optical flow-based conditioning module is introduced, enabling human animation methods to train on data with background instability, which helps scale the approach to noisy, real-world datasets.
    
- The paper presents a heuristic depth-order map calculation pipeline, providing simple yet effective spatial information for multi-character generation tasks.

### Weaknesses
 - Although the authors claim the method can handle multiple characters, most of the results feature only one or two characters.
    
- While the paper includes some analysis of background motion in the training dataset, it lacks in-depth analysis related to multiple characters, such as the effect of character count or occlusion ratios.

- In Table 1, the model trained on a noisy dataset outperforms the AnimateAnyone baseline trained on a clean TikTok dataset. It's unclear whether this improvement is due to the dataset or the proposed modules. The paper does not provide sufficient analysis to isolate the source of the performance gain. Specifically, the impact of pose diversity, data scale, and character domain diversity within the noisy dataset compared to the clean dataset is not explored. Furthermore, a direct comparison by training the proposed model on the clean TikTok dataset is missing, which would provide a more convincing argument for the effectiveness of the proposed modules.


### Questions
- Can the authors provide animation results for more challenging scenarios, such as dense crowd animations or high occlusion ratios?
    
- In Table 1, the model trained on a noisy dataset outperforms the AnimateAnyone baseline trained on a clean TikTok dataset. Is this improvement due to the dataset or the proposed modules? If the improvement stems from the dataset, could the authors provide a more detailed analysis of dataset quality (e.g., pose diversity, data scale, character domain diversity)? If the improvement is due to the proposed modules, the authors should train their model solely on the TikTok dataset to directly compare with the baseline methods.
    
- In the inference stage, can the optical flow guider take a specific optical flow map as input to achieve results with camera rotation effects?

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
The paper tackles the problem of multiple-character image animation and addresses the failures in current approaches by introducing additional control signals: 1) To alleviate the influence of non-static background, it adds the optical flows as conditions; 2) To avoid identity mixup in multi-character animation, it adds depth order guidance that labels the identity id within the skeletal dilation map. It achieves comparable performance on single-character animation benchmarks and better quality on multi-character animation.

### Strengths
* The proposed methods are well-motivated. The authors demonstrate the effectiveness of the proposed control signals by comprehensive ablation studies.
* The skeletal dilation map is novel to me as an alternative to the segmentation mask. The authors explain the choice and its advantage over the segmentation mask, which is sound.
* It shows better quality on multi-character animation compared to baselines.

### Weaknesses
 * The head poses are limited in all the qualitative results presented in the paper, including the figures and the supplementary videos. For example, in Fig. 1, the head poses of all characters are the same as the reference images while other parts of the body are retargeted into new poses. It makes it difficult to assess the animation quality without qualitative results showcasing more diverse head poses. This is my main concern since faces are probably the most difficult and important part of the animation. Comparing facial regions with the baselines will help the judgment.

* As mentioned in the limitations, the use of the skeletal dilation map restricts the animation of clothes that cover a significantly larger area than the skeletal dilation map. Is the kernel size of dilation a crucial factor for the method? How does it impact the animation of clothes?

### Questions
In addition to the weakness, can the authors clarify how the depth order map of the target pose sequences is acquired during inference? More specifically, how the depth order is determined given only the skeletons of multi-character poses?

### Soundness
3

### Presentation
3

### Contribution
3

# UV-Attack: Physical-World Adversarial Attacks for Person Detection via Dynamic-NeRF-based UV Mapping

- Decision: Accept
- Avg Score: 6.80
- Scores: 6, 6, 8, 6, 8

## Abstract
Recent works have attacked person detectors using adversarial patches or static-3D-model-based texture modifications. However, these methods suffer from low attack success rates when faced with significant human movements. The primary challenge stems from the highly non-rigid nature of the human body and clothing. Current attacks fail to model these 3D non-rigid deformations caused by varied actions.
Fortunately, recent research has shown significant progress in using NeRF for dynamic human modeling. 
In this paper, we introduce \texttt{UV-Attack}, a novel physical adversarial attack achieving high attack success rates in scenarios involving extensive and unseen actions. We address the challenges above by leveraging dynamic-NeRF-based UV mapping. Our method can generate human images across diverse actions and viewpoints and even create novel unseen actions by sampling from the SMPL parameter space. While dynamic NeRF models are capable of modeling human bodies, modifying their clothing textures is challenging due to the texture being embedded within neural network parameters.
To overcome this, \texttt{UV-Attack} generates UV maps instead of RGB images and modifies the texture stacks. This approach enables real-time texture edits and makes attacks more practical. Finally, we propose a novel Expectation over Pose Transformation loss (EoPT) to improve the evasion success rate on unseen poses and views.
Our experiments show that \texttt{UV-Attack} achieves a 92.75\% attack success rate against the FastRCNN model across varied poses in dynamic video settings, significantly outperforming the state-of-the-art AdvCaT attack, which only had a 28.50\% ASR. Moreover, we achieve 49.5\% ASR on the latest YOLOv8 detector in black-box settings.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper presents UV-Attack, a novel physical-world adversarial attack for person detection systems. The core idea is leveraging dynamic Neural Radiance Fields (NeRF) for UV mapping to generate adversarial images across varying human actions and viewpoints. The attack modifies clothing textures through UV maps rather than traditional RGB images, allowing real-time, practical texture edits. A new Expectation over Pose Transformation (EoPT) loss is introduced to improve the attack's success rate for unseen human poses. The paper highlights the potential of using dynamic NeRF and UV mapping for adversarial attacks on non-rigid objects like human bodies.

### Strengths
1. The use of dynamic NeRF-based UV mapping for adversarial attacks is an innovative approach, addressing the challenge of human movement.

2. The approach can generate adversarial textures in real-time, making it feasible for real-world attacks

3. The proposed method outperforms previous adversarial attacks, achieving a high ASR across varied poses and detectors, particularly in free-pose settings.

4. The method’s ability to handle diverse human poses through EoPT and UV mapping may enhance its robustness

### Weaknesses
1. The method heavily depends on pretrained stable diffusion models for generating adversarial patches, which might limit its generalizability to other model architectures. Specifically, the reliance on a fixed latent space and the inherent biases within the pretrained diffusion model could restrict the diversity of adversarial examples, potentially making the attack less effective against detectors trained with different data distributions or architectures. The paper does not explore the impact of using different diffusion models or fine-tuning the existing one, which could be a significant factor in the attack's robustness.

2. The attack pipeline involves multiple steps, including dynamic NeRF, UV mapping, and diffusion models, which increases the complexity and may pose practical limitations in some applications. The computational overhead of generating dynamic NeRFs and performing UV mapping, followed by the diffusion process, could be a bottleneck for real-time applications, particularly on resource-constrained devices. The paper lacks a detailed analysis of the computational cost and memory requirements of each step, making it difficult to assess the practical feasibility of the proposed method.

3. While the paper claims success in physical-world attacks, the physical-world experiments are limited to a few environments and detection models. The experiments do not explore the impact of varying lighting conditions, camera angles, and background clutter, which are crucial factors in real-world scenarios. The limited number of physical environments tested may not be representative of the diverse conditions encountered in practical applications, thus raising concerns about the generalizability of the attack.

4. The paper shows good results on some detectors but does not fully address how transferable the attack is to other models not tested in the experiments. The impact of domain shift (e.g., different datasets) is also not well explored. The paper needs to investigate how the adversarial textures generated for one detector perform on other detectors, especially those trained on different datasets or with different architectures. The lack of a thorough analysis of transferability and domain shift limits the practical applicability of the proposed attack.

### Questions
In addition to the weaknesses, please refer to the following:

1. How sensitive is the attack to the specific poses, say sampled from the Gaussian Mixture Model (GMM)? Would other pose distributions significantly affect the results? There is limited statistical insight in the paper.

2.  Does the complexity of clothing textures (e.g., different patterns or colors) impact the effectiveness of the attack? 

3. How well does UV-Attack generalize to detection models not tested in the paper, particularly beyond YOLO and FastRCNN variants? Could there be a model-specific bias in the attack’s success rate? This needs to be addressed in detail.

4. There is limited discussion on potential defenses against UV-Attack, which is crucial for the broader adversarial machine learning community. A discussion or experiment on how robust the attack is to adversarial training or other defenses would make the paper more impactful.

### Soundness
3

### Presentation
2

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
This paper introduces a novel adversarial attack pipeline for person detection, termed UV-Attack. First, it innovatively incorporates a NeRF-based UV mapping method into the person detection adversarial attack pipeline, enabling the generation of diverse human UV maps and textures with varying poses and camera perspectives. Second, it leverages a diffusion model to generate adversarial patches, which are then interpolated with textures produced by 3D human models to render adversarial human images. Finally, comprehensive experiments are conducted across various mainstream detectors and scenarios, benchmarking the proposed method against existing approaches.

### Strengths
This paper presents a novel approach to generating adversarial samples for human detection. Firstly, it cleverly utilizes the UV map and texture of the human model to introduce adversarial patches, enabling efficient rendering onto RGB images of the human figure for multi-view attacks. Secondly, it leverages the robust generative priors of diffusion models to perform interpolation at the texture level. Finally, this method achieves significant accuracy improvements in dynamic and multi-pose scenarios by sampling various human poses and perspectives, further validating the effectiveness of the proposed approach.

### Weaknesses
This paper has shortcomings in the presentation of experimental details and data, which may lead to confusion regarding the reproducibility and generalizability of the findings.

### Questions
1. In your training for a specific detector, you mentioned that you collected 100 different backgrounds from both indoor and outdoor scenarios. Could you provide more details about this data and its sources? In other words, how significantly does this data impact the effectiveness of the adversarial sample generation?
2. Your pipeline requires sampling SMPL pose parameters from a Gaussian Mixture Model (GMM). When modeling the GMM, you need to input the target video and the human pose dataset. What is the purpose of including the target video?
3. When validating the ASR, you average class labels except for "person" in the COCO dataset. During training, is the diffusion model condition kept consistent throughout?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The authors propose a novel method to attack person detectors for various human poses in the physical world. They incorporate dynamic NeRF-based UV mapping and the Gaussian Mixture Model to sample and generate unseen human poses with editable textures. The texture is generated by a latent diffusion model. They then combine PSO and Adam optimizer to find the optimal diffusion latent variable for the adversarial texture. The adversarial texture outperforms multiple baselines in both the digital and the physical world.

### Strengths
1.	The writing is clear and easy to understand.
2.	The goal of this paper is important to this area, and the solution is technically sound.
3.	The experiments are comprehensive. The authors evaluate the adversarial effectiveness of the adversarial patterns under various parameters, including poses, viewing angles, and IoU thresholds. White box and transfer study are both included.

### Weaknesses
1.	The digital test setting seems a little problematic. The test poses are generated by GMM, which could be unreal. This raises the training-test contamination issue since a GMM-based model is also included in the model comparison. I suggested using videos from a different source.
2.	It lacks a null model for comparison: a non-adversarial pattern, such as an everyday clothes pattern, or a generated pattern from a random initial point.
3.	The training detail section is confusing; please see the questions.

### Questions
1.	What is the training dataset? Does it include the videos recorded by the authors? If so, the authors should make a split on the training and test dataset that consists of different subjects and backgrounds.
2.	Are the training datasets for digital and physical evaluation different? If so, why? What is the physical adversarial effectiveness of the digitally optimized patterns?
3.	Is the SMPL modeling for each subject the same? What's the transferability to unseen subjects? Does this mean that this method requires training a UV-volume model and optimizing for each person who is going to wear the adversarial clothes? If so, this method seems to have a great limitation; how to address this?

I'm happy to raise the score if these concerns are addressed.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces UV-Attack, a novel adversarial approach using dynamic-NeRF-based UV mapping to achieve high ASRs on person detectors across diverse human actions and viewpoints. By generating UV maps rather than static RGB images, UV-Attack enables real-time texture modifications, making it practical and adaptable to unseen poses. Experiments show a 92.75% ASR against FastRCNN and 49.5% on YOLOv8, significantly surpassing prior methods and showcasing the potential of dynamic NeRF for effective adversarial attacks on moving human targets.

### Strengths
1. The idea of expanding the perturbation space by removing classifier-free guidance is interesting and brings a fresh perspective for boosting the transferability in the physical world.
2. The experiments are comprehensive, covering both digital and physical environments for thorough validation.
3. The paper is well-organized, with a clear and logical flow.

### Weaknesses
1. I’m a bit unclear on the Expectation over Pose Transformation (EoPT) loss. How does it differ from the standard Expectation over Transformation (EoT)? From Equation (5), it seems that the transformations traditionally applied at the image level have been shifted to include pose, camera, and lighting changes.
2.  Why do you choose YOLOv3 and Faster R-CNN as the target models rather than other, potentially more recent models?  Is there an underlying reason for this choice?
3. In line 431, the paper mentions that structural differences between models like SSD and the target model lead to limited transferability. Why not try a model ensemble approach to boost transferability, which is often used in physical attacks?
4. Could you clarify how the target model is set up? Is it just a pretrained model, or is it fine-tuned on a specific dataset? Additionally, how do each of the models perform on clean samples? This would serve as an important comparison, especially for physical-world testing. Since factors like distance, angle, and setting can greatly impact a detector’s performance in the physical world, poor performance on clean samples would reduce the significance of the attack itself.
5. For the physical experiments: (1) there is no mention of how many frames were captured in the video used to calculate ASR; if the frame count is too low, the results may lack credibility; (2) the physical-world attack examples are limited in the current draft—please provide a more complete set.

### Questions
Please refer to the weakness. If my questions are addressed, I will raise the score.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper presents UV-Attack, a method designed to generate effective physical adversarial attacks targeting person detection systems by leveraging dynamic Neural Radiance Fields (NeRF) and UV mapping. This approach allows adversarial textures on clothing to adapt seamlessly to various human poses, addressing the challenges posed by non-rigid human movement. UV-Attack introduces two key components: a custom Expectation over Pose Transformation (EoPT) loss function to enhance attack success across diverse poses and viewpoints, and adjustments to the diffusion model to improve the transferability of adversarial examples to different detection systems.

### Strengths
- The paper introduces a novel application of dynamic NeRF and UV mapping, addressing the challenge of generating adaptable adversarial textures for non-rigid objects like human bodies. 
- The authors propose an Expectation over Pose Transformation (EoPT) loss, which improves the patch’s robustness by ensuring its effectiveness across a wide range of poses.
- Extensive experiments across multiple person detection models and in various settings, including both white-box and black-box scenarios.
- The physical testing on printed clothing showcases UV-Attack’s applicability in real-world scenarios.
- The writing and presentation are clear and easy to follow.

### Weaknesses
 - The paper focuses heavily on maximizing attack success rates against person detection models but does not address visual inconspicuousness or stealth. For a physical adversarial attack to be practical in real-world scenarios, it should evade not only machine detection but also appear natural and undetectable to human observers. UV-Attack’s textures might draw attention due to potentially unnatural patterns, especially in public settings where they could be easily noticed. 

=> Action: I recommend introducing constraints that limit the patch’s appearance to more natural or common textures, to balance adversarial effectiveness with visual stealth. This could improve the applicability of UV-Attack in sensitive contexts, such as surveillance evasion, where inconspicuousness is essential.

- The authors report success rates for state-of-the-art attacks that differ significantly from those in the original publications. This inconsistency complicates direct comparisons and may impact the perceived credibility of UV-Attack’s comparative performance. Additionally, some state-of-the-art techniques apply constraints on patch appearance to ensure inconspicuousness, making comparisons with unconstrained approaches potentially unfair.

=> Action: To improve clarity and credibility, the authors should explicitly document the reasons behind any benchmarking deviations and, where possible, apply similar constraints to UV-Attack’s patches for fair comparison. Aligning evaluation protocols with prior works or noting significant differences in approach would enhance the validity of the comparison.

Less Important:

- The paper overlooks relevant related work, particularly “DAP: A Dynamic Adversarial Patch for Evading Person Detectors,” which similarly aims to create patches that are robust to non-rigid transformations. Including this work in the literature review would help contextualize UV-Attack’s contributions within the existing research.

=> Action: Discussing DAP and other similar methods would provide readers with a clearer understanding of UV-Attack’s novelty and advancements, especially in handling non-rigid transformations.

- The use of dynamic NeRF in UV-Attack is computationally intensive, which could limit applicability in scenarios requiring frequent re-designs of the patch for different targets or environments. While this is less relevant for single, offline generation, the computational demand could become a significant limitation if applications required ongoing adaptations.

### Questions
Check weakness

### Soundness
3

### Presentation
3

### Contribution
2

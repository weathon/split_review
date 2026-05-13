# LeBD: A Run-time Defense Against Backdoor Attack in YOLO

- Decision: Reject
- Scores: 6, 1, 3, 3

## Abstract
Backdoor attack poses a serious threat to deep neural networks (DNNs). An adversary can manipulate the prediction of a backdoored model by attaching a specific backdoor trigger to the input. However, existing defenses are mainly aimed  at detecting backdoors in the digital world, which cannot meet the real-time requirement of application scenes in the physical world. We propose a LayerCAMenabled backdoor detector (LeBD) for monitoring backdoor attacks in the object  detection (OD) network, YOLOv5. LeBD ultilizes LayerCAM to locate the trigger and give a risk warning at run-time. In order to further improve the precision  of trigger localization, we propose a backdoor detector based on counterfactual attribution LayerCAM (CA-LeBD). We evaluated the performance of the backdoor  detector on images in the digital world and video streams in the physical world. Extensive experiments demonstrate that LeBD and CA-LeBD can efficiently locate the trigger and mitigate the effect of backdoor in real time. In the physical  world scene, the detection rate of backdoor can achieve over 90\%.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposed an approach of defensing backdoor attack in YOLO at run-time. Specifically, the proposed LayerCAM-enabled backdoor detecotr (LeBD) utilized LayerCAM to locate the backdoor trigger, aiming to addressing the real-time requirement of application scenes in the physical world.

### Strengths
+ The study focuses on an interesting and important topic, the run-time defense against backdoor attacks in object detection network.
+ The paper is well-written and easy to follow.
+ The idea of using LayerCAM to locate the trigger is inspiring.

### Weaknesses
 - The digital world and physical world

If my understanding is correct, one of the key motivations is that the existing defense focuses more on backdoor attacks in the "digital world" rather than attacks in the "physical world." However, I would suggest a more detailed and explicit definition of the digital world and the physical world. It would be better and necessary to provide a more in-depth description and explanation of why this assumption is sound. For example, you could discuss the main constraints that limit the application of backdoor attacks in the physical world. I found this assumption somehow confusing, as it suggests that a backdoored sample with a pixel-level trigger can still be printed and placed in the physical world.

- The performance of LeBD in the digital world

In Table 1, although the discussion explains that "In the physical world, affected by the shooting angle, light, and so on", photographed triggers are more vulnerable to defenses, the performance gaps of the proposed LeBD and CA-LeBD between the digital world and the physical world are still much larger than those observed in benchmarks. It appears that the performance of the proposed approach is highly influenced by the strength of backdoor attacks, with weak triggers leading to more significant performance improvements. Please provide more discussion on this point. Another concern is, the experiments in digital world scenario only involves the same backdoor attack in the physical world scenario, however, there are more attacks can be applied in the digital world, as described in previous sections. 

- The application scenario of CA-LeBD

In Section 5.1, it has been claimed that "although LeBD and CA-LeBD are inferior to NEO, they are much faster than the latter". However, according to the experimental results in Section 5.4, the runtime overhead of CA-LeBD could be several times higher than NEO (if applied to all 80 classes). Please provide more discussion on how to apply CA-LeBD in practice. For instance, how to determine the appropriate number of classes when using CA-LeBD and how it might influence the defense performance.

### Questions
1. Please define the digital and physical worlds with a more detailed definition and explain why other backdoor attacks are hard to be applied in the physical world.
2. Why the performance gap of proposed approach is much higher than benchmarks?
3. How to determine the appropriate number of classes protected in defense when using CA-LeBD and how it might influence the defense performance?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposed an input-level backdoor detection, specifically aiming at the object detection task. The main idea is that 1) exploiting the counterfactual attribution (CA) LayerCAM to locate the crucial region, which leads to the final prediction output, 2) occluding the chosen region of the original image; 3) putting original image and the occluded image into the object detection model and comparing their outputs. If the two outputs are different, the crucial region is considered as the trigger.

### Strengths
The main contribution is that the authors reimplement this old trick in the new object detection domain.

### Weaknesses
The main idea has been exploited by Februus (Doan et al., 2020) and also following unmentioned reference.. Considering this, I don’t think there is enough novelty to publish it on ICLR. The core concept of using counterfactual attribution to identify crucial regions and then occluding them to detect backdoors is not new. The application to object detection, while not explicitly explored in Februus, is a relatively straightforward extension. The paper lacks a detailed analysis of why existing methods, such as those based on GradCAM, fail in the object detection context. It is not sufficient to simply state that they do not work; a deeper investigation into the underlying reasons is needed. Furthermore, the paper does not adequately address the potential for high false positive rates. The concern about occluding ground-truth features and causing label flips is a significant one, and the paper's response to this concern is not convincing. The authors need to provide a more rigorous analysis of the false positive rate, considering various object types and occlusion scenarios. The hyperparameter tuning for the occlusion ratio also needs more justification and analysis, as it directly impacts the performance of the method. The paper also lacks a comparison with other input-level backdoor detection methods, which makes it difficult to assess the effectiveness of the proposed approach.

### Questions
What the proposed method will do when the chosen region is the ground-truth feature? For instance, assume there is a ‘face’ object in the object detection task. Given a benign image with a human face, the CA layerCAM locates the ground-truth facial area as the most important area of the ‘face’ object and then occludes this area. I can expect that there exists a label flipping in this case. I doubt whether the proposed work may have a high false positive ratio for trigger detection or not.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper explores how to defend against backdoor attacks for YOLOv5 in real-world scenarios. Specifically, the authors first argue that the only capable solution is saliency-map-based methods due to efficiency requirements. After that, they reveal three failure modes of directly using GradCAM for YOLOv5, based on which the author proposes to exploit LayerCAM to replace GradCAM. The authors evaluate their method on the COCO dataset and real-world settings with three baseline defenses.

### Strengths
1. The idea is easy to follow.
2. The topic is of sufficient significance.
3. The authors took into account real scenarios, which should be encouraged.

### Weaknesses
1. The scope is limited. The authors focus on only one particular model structure, even though this structure is currently widely used. However, in the near future, it is likely that people will no longer use this model structure. As such, the authors should try to construct a method that works well for different model structures rather than focusing on just one model structure.
2. The technical contributions are limited. Technically, this work is a simple extension to the GradCAM-based one by replacing GradCAM with LayerCAM, which is proposed in the previous work. More importantly, why this method is used instead of another CAM method seems to need to be analyzed.
3. Missing important experiments. Firstly, the author should evaluate the proposed method under different trigger patterns, especially those scattered ones and those not located in the center of the bounding box.
4. There is no discussion about the resistance to potential adaptive attacks. What if the attackers know this defense? Can they design an adaptive method to bypass this defense easily?

### Questions
Please refer to the 'Weaknesses' part.

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces a real-time backdoor attack detection system for Deep Neural Networks, specifically on the YOLOv5 object detector. Utilizing LayerCAM and counterfactual attribution, the proposed detectors, LeBD and CA-LeBD, aim to locate and mitigate backdoor triggers efficiently. Experiments in both digital and physical settings show that the methods work for patch-based triggers.

### Strengths
1. This paper tries to solve the backdoor attacks on object detection tasks. To the best of my knowledge, few papers focus on this important open problem. 

2. The work improves upon the NEO algorithm by enhancing efficiency and relaxing blocker size constraints.

3. Incorporating counterfactual attribution to enhance LayerCAM is a novel and intriguing approach.

### Weaknesses
1. The proposed techniques are specialized for defending against patch-based attacks (BadNets-like patterns). It remains unclear whether these methods are effective against other forms of backdoor triggers, such as rotational triggers [1], semantic triggers [2], and augmentation-based triggers [3]. Notably, reference [1] demonstrates the real-world applicability of rotation-based backdoors in object detection models.

2. The experimental evaluation is limited to the YOLO-v5 architecture for object detection. The authors have not explored the generalizability of their approach to other object detection models. Further experiments across diverse YOLO architectures, such as YOLOv7 [4], are highly recommended. 

Typo: LayrCAM at page 5

### Questions
Can the proposed method extend to vision transformer architectures?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

# Adaptive Camera Sensor for Vision Models

- Decision: Accept
- Scores: 6, 6, 5, 6

## Abstract
Domain shift remains a persistent challenge in deep-learning-based computer vision, often requiring extensive model modifications or large labeled datasets to address. Inspired by human visual perception, which adjusts input quality through corrective lenses rather than over-training the brain, we propose Lens, a novel camera sensor control method that enhances model performance by capturing high-quality images from the model's perspective, rather than relying on traditional human-centric sensor control. Lens is lightweight and adapts sensor parameters to specific models and scenes in real-time.  At its core, Lens utilizes VisiT, a training-free, model-specific quality indicator that evaluates individual unlabeled samples at test time using confidence scores, without additional adaptation costs. To validate Lens, we introduce ImageNet-ES Diverse, a new benchmark dataset capturing natural perturbations from varying sensor and lighting conditions. Extensive experiments on both ImageNet-ES and our new ImageNet-ES Diverse show that Lens significantly improves model accuracy across various baseline schemes for sensor control and model modification, while maintaining low latency in image captures. Lens effectively compensates for large model size differences and integrates synergistically with model improvement techniques.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes Lens to address domain shift in vision tasks by adapting camera sensor parameters in real-time to optimize images. , Lens utilizes VisiT, a model-specific quality indicator based on confidence scores, to dynamically assess image quality during test time without the need for additional data or retraining. The authors also introduce a new benchmark ImageNet-ES Diverse with varied sensor and lighting conditions.

### Strengths
- I'm not an expert in this area but I love the idea of this work. This work improves model accuracy by selecting the optimal sensor settings, enabling it to achieve substantial accuracy improvements even under varying lighting and sensor conditions.
- Easy to follow. Clear writing.
- A new benchmark ImageNet-ES Diverse is introduced, which may benefit future research. The author also provided details about data collection and hardware in Appendix.
- The method is efficient without retraining and can be run in real-time with low latency.
- Experiments show notable performance improvement compared to baselines.

### Weaknesses
 - Authors utilize the model’s confidence score for its prediction on the image as a simple yet effective proxy for image quality. How do you make sure the confidence score is good enough. Is there a case of overconfidence?
- Could the method deal with rapid environmental shifts where the optimal parameter can change frequently? Possibly leading to unstable.  
- The performance of Lens is closely tied to the capabilities of the camera sensor. Is it generalizable to new devices, e.g., varying ISO and  aperture ranges?
- How might Lens perform with other types of deep vision models, such as detection, segmentation, or even VLM models, that require different kinds of spatial or temporal context?

### Questions
Please see the weakness part. I'm not an expert in this area so I may adjust my score according to other reviewers' reviews and the author's rebuttal.

### Soundness
4

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
This research paper proposes an adaptive camera sensor control method with the goal to enhance model performance by enabling the capture of high-quality images optimized for vision models. Unlike traditional approaches that rely on static settings, this method dynamically adjusts camera sensor parameters specific to the model requirements, ensuring that images are tailored to the model. Central to this approach is the use of VisiT that provides a confidence and quality indicator for each parameter set, ensuring that the chosen settings maximize image quality for model accuracy and robustness. Additionally, the paper introduces a new dataset, ImageNet-ES Diverse, specifically designed for this purpose, featuring images captured under a variety of sensor and lighting conditions.

### Strengths
1) Addressing model robustness at the sensor level is an interesting approach that is likely to enhance models' resilience to environmental variations.
2)  ImageNet-ES Diverse is a large dataset. Releasing the data for the community would be useful.

### Weaknesses
1) It would be useful to test this approach in more real-world scenarios. For instance, capturing images in diverse environments, such as indoor scenes (e.g., similar to NYU dataset), outdoor settings (e.g., similar to CityScapes or Waymo datasets), or general scenarios with multiple objects in complex settings (e.g., similar to COCO or ADE20K datasets), would provide a more comprehensive evaluation of the method's robustness.

2) The method leverages VisiT’s ability to assess image quality based on the model's confidence score for a given image. However, it raises the question of whether this approach remains effective when the model encounters object classes or contexts in which its performance is notably weak. These kinds of insights and analysis would be very helpful.

3) Including results from larger, more general multimodal models that utilize extensive training datasets and demonstrate robustness to varied environmental settings would be valuable. For instance, adding evaluations from models like LLaVA, GPT-4, or Claude could provide useful insights into the method's broader applicability.

4) Could you provide more details about Fig. 7c? It appears that the features are not well-clustered for the Lens as well, Isn’t it?

### Questions
Experiments and analysis on domain shifts in the real world data would be helpful.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The authors propose  Lens, a camera sensor control method that enhances model performance by capturing
high-quality images from the model’s perspective, rather than relying on traditional human-centric sensor control.

Thought is well received.

Lens is lightweight and adapts sensor parameters to specific models and scenes in real-time training-free, Lens uses a model-specific quality indicator (VisiT) that evaluates individual unlabeled samples at test time using confidence scores, without additional adaptation costs.
A new benchmark ImageNet-ES Diverse is introduced to validate Lens. 

Lens is claimed to be a novel adaptive sensor control system that captures high-quality images robust to real-world perturbations. 
The core idea of Lens is to identify optimal sensor parameters that allow the target neural network to better discriminate between
objects, akin to adjusting a pair of glasses for clear vision.

Detailed experiments have been done, including real physical time analysis. 


The limitations are well received. 

I just have one thought, would your method be robust against perspective and radial distortion both.

### Strengths
Paper is well written and easy to follow and understand .
Detailed experiments are there. 
Two datasets have been investigated including one that was introduced by the authors.

### Weaknesses
I do not see much weakness. I am simply thinking about radial distortion. 
Another thought is how easy it is to incorporate the proposed methods in SSL, multi, and Meta-learning. 
Perspective distortion is evident in real-world applications, as indicated in the following papers 
a) Möbius Transform for Mitigating Perspective Distortions in Representation Learning
b) LCM: Log Conformal Maps for Robust Representation Learning to Mitigate Perspective Distortion
Radial distortion is often evident as well when using cameras like fisheye view. 
Both distortions distort the visual concepts, and therefore, the models do not perform well.

Authors are not forced to do experiments. However, they are encouraged to comment on such situations and whether 2'Lens' would be robust against them as well.

### Questions
Please follow weaknesses and summary.

### Soundness
3

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
This paper proposes a camera sensor control algorithm that actively collects high-quality images based on the model’s perspective. The authors build a training-free, model-specific quality indicator called VisiT to evaluate unlabeled samples at test time without adaptation cost. They also propose a new benchmark based on ImageNet-ES that captures the natural perturbations from changes of sensor and lighting conditions. The experimental results show the effectiveness of the proposed method.

### Strengths
+ This work provides a new perspective for TTA by improving the sensor parameters, which is very interesting to strengthen the performance of foundation models.

+ The proposed benchmark provides a fair and diverse comparison for the generalization ability of the TTA in more scenarios.

+ The experimental results show the TTA can increase the accuracy by a sizable margin with different vision models.

### Weaknesses
- The novelty of this paper is limited. Leveraging the logits as a confidence score is widely adopted in many uncertainty-based methods for many applications such as classification and detection. Besides that, I don’t see other technical contribution from the proposed method.

- More details about the used techniques should be given for readers to better understand the intuition of this method. For example, how do you generate the camera parameter candidates? And how do you guarantee the discrete candidate can cover the optimal solution in the continuous parameter space?

- As evaluating the confidence score requires one forward pass of the image, deploying the Lens method seems to significantly increase the inference latency of the original model. Although subset selection method is used in CSA, it may miss the optimal solution. How do you deal with the trade-off?

- Some visualization could be added to show the best camera parameters of different input images and different backbones. Analysis to the results of selection can also be added to give readers more intuition.

- Have you ever tried other proxies that are often used in uncertainty learning such as entropy of logits?

### Questions
See weakness

### Soundness
3

### Presentation
3

### Contribution
3

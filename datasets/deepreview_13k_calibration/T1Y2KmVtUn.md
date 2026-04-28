# Differentiable Sensor Layouts for End-to-End Learning of Task-Specific Camera Parameters

- Decision: Reject
- Avg Score: 6.50
- Scores: 5, 8, 5, 8

## Abstract
The success of deep learning is frequently described as the ability to train all parameters of a network on a specific application in an end-to-end fashion. 
Yet, several design choices on the camera level, including the pixel layout of the sensor, are considered as pre-defined and fixed, and high resolution, regular pixel layouts are considered to be the most generic ones in computer vision and graphics, treating all regions of an image as equally important.
While several works have considered non-uniform, \eg, hexagonal or foveated, pixel layouts in hardware and image processing, the layout has not been integrated into the end-to-end learning paradigm so far. 
In this work, we present the first truly end-to-end trained imaging pipeline that optimizes the size and distribution of pixels on the imaging sensor jointly with the parameters of a given neural network on a specific task. 
We derive an analytic, differentiable approach for the sensor layout parameterization that allows for task-specific, local varying  pixel resolutions. We present two pixel layout parameterization functions: rectangular and curvilinear grid shapes that retain a regular topology.
We provide a drop-in module that approximates sensor simulation given existing high-resolution images to directly connect our method with existing deep learning models.
We show that network predictions benefit from learnable pixel layouts for two different downstream tasks, classification and semantic segmentation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work presents a differentiable trained imaging pipeline to optimize sensor parameters and network parameters. The author presents a differentiable sensor simulation framework that can be easily integrated with the current neural network optimization framework to jointly optimize the sensor configurations and network parameters.

### Strengths
* The proposed optimization framework is fully differentiable in a physically plausible manner. 
* The framework is flexible and can adapt to different types of camera-based tasks.

### Weaknesses
 * How are the Deeplabv3+, PSPNet, SegNetXt trained? It seems the reported performance of Deeplabv3+ on the original image is lower than the original paper. Is this the reproduced result following official GitHub repo parameters? If the original model is not trained properly, then it is hard to distinguish if the performance boost is from extra fine-tuning (more training epochs) or the change of sensor parameters. I would encourage the author to provide more details. 
* Is the designed hardware sensor in Sec. 4 evaluated in simulation or the real world? 
* More visualizations for sensor images in cityscapes with learned layouts are encouraged as this can better help the reader understand how this sensor can influence the visual output. The data in MNist has very low image resolution thus the sampled visual output is too vague. More visualizations for high-resolution images are needed.
* What is the inference/training speed advantage of using the proposed method? The author claimed the speed advantage in the introduction. More quantitative results are needed to justify this argument.
* Is there any rationale behind choosing the smaller resolution size as the input rather than using the original size?
* If all the evaluation is conducted in simulation, how to verify the hardware design and what's the main take-away you want the reader to take from this?

### Questions
* What is the meaning of the red and green arrows in Figure 1? Some captions would help. 
* Will the framework change the camera parameters for each sample? Or the parameters are learned from a dataset and once learned, it is fixed for evaluation and inference? The training pipeline for the whole system is still vague. A high-level description of the general framework would be also needed. Please specify.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes a differentiable sensor layout optimization approach for end-to-end task specific optimization. Conventional camera design optimizes different components such as, sensor, optics, ISP independently and there has been a recent push in making each of these stages to perform end-to-end differentiable task-specific optimization. There has been prior work on optics and ISP optimization but nothing on sensor layout optimization. This paper proposes to optimize the sensor layout using two pixel layout parameterization. The paper shows sensor layout optimization for a classification and a semantic scene segmentation task and shows improvement for the learned layouts.

### Strengths
There isn't any work on sensor layout optimization so it's a novel contribution in terms of task-specific layout optimization. Furthermore, the work shows a realization of the learned layout showing the manufacturability of the approach.

The paper shows experiments using different tasks and networks to compare the performance of learned layout.

### Weaknesses
The paper does not provide any details on how the manufactured layout was tested with real data.

Typically optics is optimized for the pixel pitch which would be difficult for non-homogeneous layout and increases the complexity of the optics. However, this can be mitigated using task-specific learned optics.

The paper ignores CFA in the optimization process which can have an effect on the color of the image resulting in negative impact on the certain color-dependent tasks.

### Questions
How was the manufactured sensor tested with real captures?

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
- The authors present a method to optimize pixel layout on an imaging sensor for a specific task.
- To represent differentiable sensor layout, two pixel parameterization functions are proposed: rectangular and curvilinear. 
- A drop-in module that approximates sensor simulation given existing high-resolution images can be easily incorporated into existing deep learning models.
- The authors show that task like semantic segmentation in autonomous driving can benefit from non-uniform pixel layouts.

### Strengths
- The differentiable sensor layout parameterization allows for task-specific, local varying pixel resolutions, which can improve the performance of deep learning models for tasks like semantic segmentation in autonomous driving.
- The authors define a class of pixel layouts to be a parameterized deformation function which is required to be bijective and bi-Lipschitz, implying that the function is differentiable to enable end-to-end training.

### Weaknesses
 - [Generalization in diverse applications] The experiments in this paper are limited to specific tasks such as semantic segmentation and multi-label classification on facial attributes, so it is unclear how well the proposed method would generalize to other computer vision tasks. It is not clear if the learned sensor layouts are robust to different data distributions or if they are highly specialized to the training data.
- [Generalization in different scenes] The authors propose a simple deformation, so additional experiments are required to see if it is effective in datasets with anomalous scene or in robotics tasks with simultaneous indoor and outdoor scenes. How effective is it in covering a variety of scene structures with only two parameters (theta_1, theta_2)? The limited parameterization of the deformation function may restrict the ability of the sensor layout to adapt to complex scene variations, potentially hindering performance in diverse environments.
- [Exp. on computational cost] In Sec. 2 (in paragraph [End-to-end Optimization of the ISP pipeline]), the authors mention that the proposed model can reduce the size of the network and the training time, so further experiments on the computational cost of the proposed method are needed. The paper lacks a detailed analysis of the computational overhead during training and inference, especially concerning the sensor simulation and the optimization of the pixel layout parameters. A comparison of training time and inference speed with and without the proposed method is needed.
- [Comparison with non-uniform] The authors conduct experiments comparing their method to other method (Zhao et al., 2017) using a uniform layout, and additional experiments comparing their method to other method using non-uniform layout are needed. (Marin et al., 2019) The comparison is not comprehensive since it does not include state-of-the-art non-uniform sampling methods. This makes it difficult to assess the true advantage of the proposed method over existing non-uniform sampling techniques.
- [Exp. on different object size] In Sec. 5 (in paragraph [Semantic Segmentation]), the authors argue that rectangular layout is learned to put more pixels towards the left and right edges because of a higher density of small objects on the sidewalks and to confirm this effect, experimental results based on the class of small objects near the horizon or accuracy in dense area is required to support this effect. The paper lacks a quantitative analysis to support the claim that the learned pixel layout is indeed focusing on areas with higher densities of small objects. Without such analysis, the argument remains speculative.
- [Exp. on different resolution] The authors run all of their experiments at a lower resolution, but a comparison with experiments at the original resolution along with the computational cost is needed as well. The absence of experiments at the original resolution makes it difficult to assess the performance of the proposed method in practical scenarios where high-resolution images are common. It is unclear how the method would scale to higher resolutions and if the benefits observed at lower resolutions would still hold.

### Questions
- The authors say that the rectilinear layouts outperformed curvilinear layouts in all experiments because of curvilinear layouts’ limited adaptability in the image corners, more detailed explanation of this part is needed.
- In Sec. 5 (in paragragh [Semantic Segmentation]), are there any experiments on accuracy by dense area or class to demonstrate the effectiveness of the learned pixel layout? (as commented in 6. Weakness [Exp. on different object size])

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presented advances in integrating AI and hardware sensing design to more cost and energy-efficient solutions by optimising hardware parameters for task-specific problems in an end-to-end manner. The central proposition is in learning task-specific pixel layout parameterisation. To this end, this paper proposes a sensor simulation framework that allows end-to-end training, and  a pixel layout parameterisation. Initial experimentation confirms performance benefits on learned layouts over classification, semantic segmentation and multi-label classification.

### Strengths
The paper is well presented and motivated. Focusing on energy and resource-efficient solutions is attractive and, in my opinion, an important research direction. Concepts were clearly explained at the correct level of detail to transmit key ideas and propositions. Experimentation, although limited, confirmed intuition and the capacity to learn pixel layouts end-to-end.

### Weaknesses
My main criticism is in experimentation, which could be more extensive in the number of datasets and problem configurations. For example, assessing the performance gain from learning layout parameterisation across a range of image resolutions could provide more insight into the applicability of this research. 

Fig. 1 caption should be more descriptive of the proposed pipeline.

### Questions
Do authors know the performance gain over very low resolutions for image segmentation?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

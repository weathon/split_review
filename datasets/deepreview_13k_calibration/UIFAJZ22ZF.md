# The 3D-PC: a benchmark for visual perspective taking in humans and machines

- Decision: Accept
- Avg Score: 6.67
- Scores: 8, 6, 6

## Abstract
Visual perspective taking (VPT) is the ability to perceive and reason about the perspectives of others. It is an essential feature of human intelligence, which develops over the first decade of life and requires an ability to process the 3D structure of visual scenes. A growing number of reports have indicated that deep neural networks (DNNs) become capable of analyzing 3D scenes after training on large image datasets. We investigated if this emergent ability for 3D analysis in DNNs is sufficient for VPT with the \emph{3D perception challenge} (\texttt{3D-PC}): a novel benchmark for 3D perception in humans and DNNs. The \texttt{3D-PC} is comprised of three 3D-analysis tasks posed within natural scene images: \textbf{1.} a simple test of object \textit{depth order}, \textbf{2.} a basic VPT task (\textit{VPT-basic}), and \textbf{3.} another version of VPT (\textit{VPT-Strategy}) designed to limit the effectiveness of ``shortcut'' visual strategies. We tested human participants (N=33) and linearly probed or text-prompted over 300 DNNs on the challenge and found that nearly all of the DNNs approached or exceeded human accuracy in analyzing object \textit{depth order}. Surprisingly, DNN accuracy on this task correlated with their object recognition performance. In contrast, there was an extraordinary gap between DNNs and humans on \textit{VPT-basic}. Humans were nearly perfect, whereas most DNNs were near chance. Fine-tuning DNNs on \textit{VPT-basic} brought them close to human performance, but they, unlike humans, dropped back to chance when tested on \textit{VPT-Strategy}. Our challenge demonstrates that the training routines and architectures of today's DNNs are well-suited for learning basic 3D properties of scenes and objects but are ill-suited for reasoning about these properties as humans do. We release our \texttt{3D-PC} datasets and code to help bridge this gap in 3D perception between humans and machines.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Visual Perspective Taking (VPT) refers to our ability to understand how others see the world from their viewpoint. This paper has developed a new benchmark to test whether DNNs can perform this skill. Their test includes three components: determining the order of objects by depth, VPT-basic, and VPT-strategy that eliminates potential shortcuts solutions.

While DNNs matched or even exceeded human ability in determining object depth order, they struggled significantly with VPT-basic, performing at nearly random levels. In contrast, humans excelled at these same tasks with almost perfect accuracy. Even when DNNs are fine-tuned for VPT-basic, they still failed at VPT-Strategy.

These findings suggest that DNNs don't naturally develop the ability to take others' perspectives, even after extensive training on static images or fine-tuning on VPT-basic tasks.

### Strengths
- The paper used 3D Gaussian Splatting to create large sets of realistic images. 
- This method gave them precise control over the test conditions, helping them mitigate confoudning factors.
- Their analysis revealed interesting insights: while DNNs can learn to understand depth from static images, they don't develop the ability to take others' perspectives. They also found that a network's accuracy on ImageNet correlates with the 3D capabilities of DNNs they tested.

### Weaknesses
Using only green cameras and red target points in their test images raises a few questions: Would the main results still hold if they used other colors or camera shapes? Is the paper assuming the DNNs can easily spot the camera and determine its viewing angle in the images? If so, how much do the camera's physical properties (like its size, line thickness, or color) affect the results?

### Questions
The paper mentions in its appendix that when testing Visual Language Models (VLMs), they provided in-context examples to help guide the models. However, it's unclear whether they also included step-by-step reasoning examples like chain-of-thought prompting, which can probably help the models better understand how to approach these perspective-taking tasks.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes 3D-PC, a new benchmark for visual perspective taking (VPT), an ability to predict what other perspectives see. The benchmark consists of three tasks: 1) telling which object is closer (depth order), 2) predicting if a camera can see a ball (VPT-basic), 3) another version of 2) where the occlusion is flipped. The authors then tested 33 human participants and over 300 DNNs on the benchmark, showing that despite a super-human performance on depth order, DNNs are near chance on VPT tasks.

### Strengths
- The proposed benchmark is clearly motivated and well situated in the literature.
- The methodology is clearly explained with nice figures.
- Extensive experiments are conducted to show how the challenge can boost the 3D perception research of deep learning.

### Weaknesses
 - I think for a benchmark paper, one of the most important things is the correctness of the ”ground truth labels”. Although the method proposed may sound reasonable, it is hard to tell how unlikely the “GTs” are inaccurate. After all, the adopted 3D Gaussian Splatting method is not perfect. Therefore, I expect some experiments or at least some discussions on the correctness of GTs.
- I think the descriptions for VPT-Strategy are insufficient. I could only understand what this task was about when I read Figure 6.
- I don’t think we can say that DNNs learn depth from the depth order experiments. It seems to be very likely that the linear-probed DNNs only learned to solve the task based on the relative sizes of the red ball and green camera. Therefore, I don’t see the meaning of the depth order task.
- It seems that the role of the VPT-Strategy task is to test if the observer estimates the line-of-sight of the camera. However, I think it cannot take such a role. I guess if you finetune the DNNs on VPT-Strategy data, they will perform much better. If so, we can’t say they are estimating the line-of-sight because they are likely still using features to perform the task. Therefore, I don’t think the VPT-Strategy experiments are very meaningful.

Minor
- It is claimed that AlexNet is included in the model zoo (L250), but I didn’t find it in Appendix Table 1?
- Figure 2: VPT-easy → VPT-basic.

### Questions
Please see the Weaknesses. Specifically, please answer:

- How do you evaluate the correctness of the ground truth labels generated by the proposed method?
- Can you do some experiments to show whether or not the DNNs learn to perform the depth order task based on relative sizes?
- How will the DNNs perform if they are finetuned on VPT-Strategy data? Do you think the results may change your perspective on the VPT-Strategy’s role?

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces the 3D-PC benchmark, a new evaluation framework for visual perspective-taking (VPT) in humans and DNNs, focusing on spatial understanding and social interactions. The benchmark consists of three tasks: Object Depth Ordering, Basic VPT, and VPT-Perturb, where the latter is designed to prevent DNNs from using shortcut strategies. Through evaluation of 33 human participants and over 300 DNNs, the results show that while DNNs achieve human-comparable performance in depth ordering, they show clear limitations in VPT tasks, particularly VPT-Perturb. While fine-tuning helps DNNs match human performance on Basic VPT, they perform at chance level on VPT-Perturb, indicating a gap in spatial reasoning generalization. The findings demonstrate limitations in DNNs trained on static image datasets for 3D reasoning, suggesting current architectures lack the visual strategies needed for human-like perspective-taking.

### Strengths
The paper has good insight about cognitive understanding of 3D perception, exploring the gap between human and DNN capabilities in perspective-taking. By demonstrating that DNNs trained on static images struggle with tasks requiring true 3D reasoning (notably in VPT-basic and VPT-perturb as shown in Figures 4 and 6), the authors highlight a significant limitation of current model approaches. The paper also nicely suggests incorporating cognitive science insights as a potential path forward.

### Weaknesses
1. While the paper presents interesting tasks for studying 3D understanding, it could benefit from broader connections to the current 3D computer vision landscape.

2. Adding some discussion about how their findings relate to work in depth estimation and 3D segmentation would help put their cognitive insights into a wider context.

3. Figure 6 provides an overview of DNN performance but deeper exploration about why models fail on VPT tasks would be better. Including detailed failure cases or decision attribution maps could shed light on where models diverge from human performance, particularly in VPT-perturb where models rely on “shortcut” strategies.

### Questions
See weakness for more information about potential questions and improvements.

### Soundness
3

### Presentation
3

### Contribution
3

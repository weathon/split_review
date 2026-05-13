# Meta ControlNet: Enhancing Task Adaptation via Meta Learning

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
Diffusion-based image synthesis has attracted extensive attention recently. In particular, 
ControlNet that uses image-based prompts exhibits powerful capability in image tasks such as canny edge detection and generates images well aligned with these prompts. However, vanilla ControlNet generally requires extensive training of around 5000 steps to achieve a desirable control for a single task. Recent context-learning approaches have improved its adaptability, but mainly for edge-based tasks, and rely on paired examples. Thus, two important open issues are yet to be addressed to reach the full potential of ControlNet: (i) zero-shot control for certain tasks and (ii) faster adaptation for non-edge-based tasks. In this paper, we introduce a novel Meta ControlNet method, 
which adopts the task-agnostic meta learning technique and features a new layer freezing design. Meta ControlNet significantly reduces learning steps to attain control ability from 5000 to 1000. Further, Meta ControlNet exhibits direct zero-shot adaptability in edge-based tasks without any finetuning, and achieves control within only 100 finetuning steps in more complex non-edge tasks such as Human Pose, outperforming all existing methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces Meta ControlNet, leveraging meta-learning and a novel layer-freezing approach to significantly reduce the training steps needed for ControlNet from 5000 to 1000. Additionally, it enables zero-shot control in edge tasks and rapid adaptation in complex tasks like Human Pose with only 100 finetuning steps.

### Strengths
1. The idea is simple and easy to understand, that is, using meta-learning to train ControlNet from a set of mixed tasks, and further enhance its adaptation capability in new tasks or zero-shot tasks.
2. The visual results look good and training steps are also reduced.

### Weaknesses
There are three critical issues for this paper:
1. No quantitative results are provided. The paper only shows qualitative results, which makes it hard to evaluate the performance of the proposed method.
2. Zero-shot capability. This paper claims that the proposed method can achieve zero-shot control in edge tasks. The model is trained on HED, Segmentation, and Depth map which belong to the edge tasks. It raises a question about whether the model has achieved zero-shot control in edge tasks. If we train ControlNet on three tasks, and then test the model on Canny and Normal, can ControlNet achieve similar 'zero-shot' control in these two tasks?
3. Training costs. If there are greater costs in training and we still need to fine-tune the model on new tasks like pose even with fewer steps (the total costs mighit be increased), we need to elborate more on the training costs and its significance.

### Questions
NA

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces Meta ControlNet, which freezes the latter encoder block and the middle block during meta training of ControlNet. The insight of this paper is that, the initial encoder blocks are directly linked to the control images of each task. And the middle and latter encoder blocks capture common and high-level information thus can be retained and shared across tasks. So simply training the initial encoder blocks can largely reduce training overhead during Meta ControlNet’s training phase.

### Strengths
(1) This paper focus on an interesting question, which as great significance to downstreaming research and tasks. 

(2) The overall design of the model design is generally make sense.

### Weaknesses
(1) This paper proposes an efficient ControlNet training paradigm. However, the experiment part only shows visual comparison, without numerical comparison of training time, quantitative comparison on existing benchmark, or user study. This makes the comparison results unreliable.

(2) I would expect results for adaptation tasks that are more challenging. For example, training on pose and adapt to depth map. Since we know that conditions with similar representation type (such as sketch and canny)  can directly adapt to each other without training.

(3) Providing more results of how the proposed method perform compared to other meta learning methods would be helpful for paper quality.

### Questions
See weekness.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this paper, the authors aim to enhance ControlNet from two aspects: i) zero-shot control for certain tasks, and ii) faster adaptation for non-edge-based tasks. Specifically, the authors adopt the task-agnostic meta learning technique (i.e., the FO-MAML framework with various image condition types serving as different meta tasks) and feature a new layer freezing design (i.e., freeze latter encoder block and the middle block during meta learning). Experimental results on both edge-based and non-edge-based tasks demonstrate the superior control ability and efficiency of the proposed method.

### Strengths
-	The proposed method is well-motivated. Enhancing the task adaptation ability of ControlNet is indeed an interesting research question to explore. The authors make a good attempt in this direction to learn a more generalizable ControlNet initial via the meta learning technique.
-	The paper is generally well-written and easy to follow.

### Weaknesses
-	There are only qualitative results in the paper. The authors should provide quantitative results as well to make the work more convincing.
-	For the non-edge-based tasks, the authors only focus on Human Pose. Since one major aspect of this paper is to enable fast adaptation of non-edge-based tasks, the authors should consider other non-edge-based tasks as well.
-	The authors claim that the proposed method is more efficient with fewer inference steps. However, the proposed method also involves an additional training stage. It would be better if the authors could provide the computational cost comparison with other methods including the training stage.

### Questions
I have additional questions:

-	The authors choose three tasks (i.e., HED, Segmentation, Depth) as the meta tasks. Could the authors provide a justification for this? What if other tasks are used during meta training? Have the authors ablated the effect of different meta tasks?

Given the current status of the paper, I am leaning towards borderline reject and hope the authors could address my concerns during the rebuttal.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a Meta ControlNet method, which adopts the task-agnostic meta learning technique and features a new layer freezing design. The proposed model significantly enhances the efficiency of ControlNet’s learning process. Meta ControlNet model produces a generalizable model initial, which exhibits exceptional control capabilities in zero-shot settings. The proposed Meta  ControlNet experiment results also achieve comparable performance.

### Strengths
The motivation of this paper is very interetsting to use task-agnostic meta learning to explore the full potential of ControlNet. 

The paper effectively communicates its main ideas. The explanation of how meta-learning can be incorporated into ControlNet is well-presented and offers code and valuable guidance for practical applications.

### Weaknesses
1 Limited technical novelty since theory and approach are straightforward. Moreover, the experimental results are not sufficient. The novelty and effort of this paper cannot reach ICLR standards.

2 This paper does not summarize the differences of current related work and clarify their difference. 
3 The authors state: A main novel component that Meta ControlNet features is the design of freezing layers during training. What is the motivation for designing the freezing layer, and what benefits can he bring to this model?

4 Experiment settings should follow the ControlNet. The experimental section doesn't provide any quantitative experimental data. The ablation study is not sufficient.In addition, the proposed method is only verified on one dataset and lacks generalization.

5 Three contributions all state the proposed model can enhance the efficiency of the ControlNet’s learning process. The contribution section seems to be missing an analysis of the methodology.

6 This paper is not well-organized, i.e., the figure does not correspond to the page on which the text is located (e.g., figure 7 is on page 7, but the text is on page 8).

### Questions
Nope

### Soundness
3

### Presentation
1

### Contribution
2

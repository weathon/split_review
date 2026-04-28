# Visual Scratchpads: Enabling Global Reasoning in Vision

- Decision: Reject
- Avg Score: 5.50
- Scores: 8, 5, 6, 3

## Abstract
Modern vision models have achieved remarkable success in benchmarks where local features provide critical information about the target. There is now a growing interest in solving tasks that require more global reasoning, where local features offer no significant information. These tasks are reminiscent of the connectivity tasks discussed by Minsky and Papert in 1969, which exposed the limitations of the perceptron model and contributed to the first AI winter. In this paper, we revisit such tasks by introducing four global visual benchmarks involving path findings and mazes. 
We show that: (1) although today's large vision models largely surpass the expressivity limitations of the early models, they still struggle with the learning efficiency; we put forward the `globality degree' notion to understand this limitation; (2) we then demonstrate that the picture changes and global reasoning becomes feasible with the introduction of  `visual scratchpads'; similarly to the text scratchpads and chain-of-thoughts used in language models, visual scratchpads help break down global tasks into simpler ones; (3) we finally show that some scratchpads are better than others, in particular, `inductive scratchpads' that take steps relying on less information afford better out-of-distribution generalization and succeed for smaller model sizes.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper deals with visual problems that require global reasoning. The proposed tasks are based on the connectivity problems discussed by Minsky and Papert in 1969. The paper shows that large vision models of today still struggle with learning efficiency when dealing with visual problems that require global reasoning. To deal with this issue the paper introduces a "visual scratchpad" based on text scratchpads and chain-of-thoughts used in language models.

### Strengths
* The paper identifies and address an important problem. The paper introduces the novel Cycles and Strings tasks which turn out to be challenging for current large vision models.

* The paper provides a good theoretical analysis of tasks that require global reasoning through the definition of globality degree.

* The paper includes extensive experiments that show that current large vision models cannot deal with global reasoning problems irrespective of model size (Figure 5).

### Weaknesses
 * Novelty of Scratch Pads: Visual scratch pads have already been explored in "Can Visual Scratchpads With Diagrammatic
Abstractions Augment LLM Reasoning?, Hsu et. al. NeurIPS 2023".

* Implementation details: Some very important details are not clear -- in L335 "add a linear layer to the hidden representation of the last transformer layer to predict the scratchpad image". Use of a simple linear layer would likely severely limit the resolution of the output scratch pad image. It would be useful if the paper discusses the resolution limits (if any) of the visual scratch pad, as this would limit the complexity of the problems that can be tacked by the proposed approach. Specifically, the paper should clarify if the linear layer is applied to the CLS token, or to each patch embedding, as this has significant implications for the spatial resolution of the generated scratchpad. Furthermore, the paper should discuss how the scratchpad is converted into an image, including any upsampling or reshaping operations.

* Error propagation: For complex tasks, without a sophisticated visual scratch pad generation mechanism, pixel level errors might have a significant impact on reasoning capabilities. The paper should include a more detailed analysis of how errors in the generated scratchpad affect the final task performance. For example, what is the impact of noisy or incomplete scratchpads on the final accuracy? What is the sensitivity of the model to the quality of the generated scratchpad?

* Baselines: The paper does not consider state of the art VLMs such as LLaVA or InstructBLIP as baselines. As these models use more sophisticated attention mechanisms, it is possible that the proposed Cycles and Strings tasks can be solved by such models. The paper should include a comparison with these models to better contextualize the performance of the proposed approach.

* Compute Cost: The use of visual scratch pads would add a significant compute overhead. This should be discussed in more detail. The paper should quantify the additional computational cost associated with generating and processing the visual scratchpads, both in terms of training and inference time. It should also discuss the memory requirements of the proposed approach.

### Questions
* The novelty of the proposed approach should be discussed in more detail.
* The implementation details of the visual scratch pads should be discussed in more details.

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
The authors show that tasks that have a high "globality degree" are hard for transformers to learn. Specifically, tasks globality degree is the proportion of patches required to get non-trivial performance on the task. In the language of RL/imitaiton learning, the idea is that tasks with a high globality degree are harder to learn when using sparse rewards, and that process supervision/behavior cloning can help when each action is sufficiently "local". 

The paper builds on the results of Abbe et al, and shows results on images. All image tasks are some form of cycle detection and the process supervision is some form of BFS depicted in an image (e.g. a drawing of a maze, a drawing of the nodes/edges of a graph, etc). 

------ Previous ----
The authors suggest that an important class of reasoning problems rely on breaking down a complex ("global") problem into a sequence of simpler steps that are more "local". They introduce a measure of "globality" based on what proportion of patches are required to solve the task. 

Then they show some experiments on 4 visual depictions of problems where BFS is the solution. They train recurrent transformers to solve this problem, and show that using behavior cloning to approximate the BFS step results in better generalization to new sequence lengths. 

They show that in some cases, networks can also learn with less decomposition and chain-of-thought training. Recurrent transformer model trained on all intermediate steps of visual BFS (inductive scratchpad) learns to generalize to samples of different lengths than a model that is trained to go 1→penultimate step, and then penultimate → ultimate step (single-step scratchpad).

They show that the single-step model is able to learn some tasks, provided the model is sufficiently “large” — vit-S up to VIT-H. In this case the model needs to learn to do O(24) steps, and only models with more layers (VIT-B has 12 and VIT-H has 30) end up learning the solution. While for inductive versions, all versions learn the solution. This is probably related to the idea of “effective depth” — e.g. Feedback networks CVPR 17 http://feedbacknet.stanford.edu/.

### Strengths
The experiments are rigorous and, to summarize the rebuttal discussion, I agree they relate to globality degree. 

-- Previous --

**Originality**
The authors define globality degree in a pretty intuitive way: what proportion of images patches are required to predict the label. They show that for tasks that seem to have a high globality degree (e.g. counting connected components), networks trained with heavy input masking cannot solve the task. 

**Significance**
Unclear to me what the significance of globality vs the scratchpad vs making this work for visual settings. It would help if this were connected to vision settings where other papers have studies, rather than a new benchmark of visual representations of BFS

**Clarity**
Generally the text was written clearly and easy to read. Figures were well presented and grounded in the text.

**Quality**
The authors clearly invested significant care and effort in preparing the experiments and writing the manuscripts. The figures are quite visually appealing, too.

### Weaknesses
 **Experiments:**

-- Final--
The experiments in the paper are on visual tasks that are not very representative of computer vision tasks.

I understand that the task is defined is on tensors of shape B x W x H x C, the inputs are continuous, and the architecture is a ViT. But the images are unlike natural images. Other visual tasks might be a better fit -- e.g. tasks that use imitation learning from pixels. In fact, the method is pretty similar to imitation learning.


-- Previous --
My main concern is that the experiments don't really support the main story of the paper. They seem related at a glance, but after thinking about it some more I don't think they actually are.

What does the globality/locality degree have to do with the experiments? Do transformers learn local steps local steps preferentially to global ones? BFS is local, but they don’t have any experiments or theoretical analysis that it is an important property. Besides, since transformer attention is global anyway, I would expect not.

In fact, the experiments seem to instead show that when the number of attention layers is fewer than the number of "reasoning" steps required for the underlying graph algorithm, the model fails.
* This would explain why larger models (more layers) can learn to do BFS for fixed-size problems even in the single-step case. Specifically: if the # layers > # steps, the model can learn a solution, which would explain why ViT-S and VIT-B fail (they have 12 layers and there are O(24) reasoning steps required).
* It would also explain why single-step models don't learn to generalize as well, even for the deeper models: because single-step models have a fixed number of layers/steps thus fixed overall "effective depth". While the autoregressive "inductive scratchpad" gives the model essentially unlimited depth -- and the problem is learnable as long as each step doesn't require more than, say, 24 attention layers, the model can learn the true solution. And the model is trained to approximate BFS using a hand-designed behavior cloning expert.

But there is no mention of this (or any other) alternative explanation of the experiments, and it is assumed that the cause is globality of the global task vs locality of the individual steps. But, again, there is no experiment showing that local steps are in fact easier to learn.

There is also little mention of existing work that connects chain-of-thought reasoning to a smaller sequence of "local" steps. There are no external baselines, the evaluation is on a new "benchmark" proposed in this paper, and the approach is not evaluated on any existing benchmarks.



This brings me to my next major concern: some meaningful connection to existing work is missing.

### Questions
--Previous--
I didn't fully understand the connection between the globality degree definition and the masking experiment. 
Since the BFS examples are kind of simple tasks, you could probably estimate the globality degree analytically. How do the experimental results in Fig 3 + 4 match the predicted globality degree

### Soundness
4

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
4

### Summary
The paper argues that most existing vision tasks can be solved by considering only local information in an image. Inspired by this, the paper introduces two kinds of synthetic tasks that require global information: a maze task, where there goal is to find a path through a maze; and a graph connectivity task, where the goal is to determine if a graph is connected or not. The paper also introduces a variant for each of these tasks: a circular maze, and a smoothed depiction of the graph. The paper then demonstrates that the tasks can be solved by training an image generation model on sequences of images that visually represent the incremental generation of a solution (such as the sequence of images showing an incremental breadth-first floodfill for the maze task).

### Strengths
The paper is quite well-written and easy to follow. It makes the important argument that considerations regarding "System-2"-style reasoning should not only apply to purely textual tasks but also to other domains, such as vision. The graph and maze tasks are simple visual tasks for initial investigations in this direction (with some caveats below).

### Weaknesses
The proposed method, "visual scratchpad", seems to be largely identical to methods like the one proposed in (Yang et al. 2024) or (Bai et al. 2023), applied to a much simpler, synthetic task domain. It seems also related to Procedure Cloning (Yang et al. 2022) and the method described in (Lehnert et al. 2024), although it uses pixels instead of tokens to keep track of previously visited states (then again, that seems to make it a special case of the above-mentioned methods based on video generation).

Since these image-generation methods are able to solve surprisingly difficult tasks just by predicting images, would we not expect them to be able to behavior-clone a floodfill-type solution to maze tasks when training on a large training set? I may be missing something here and will be happy to revise my score if so. 

The introduced datasets are somewhat simplistic and reminiscent of existing (but much more comprehensive) visual reasoning datasets, like (Cherian et al. 2023).

One could argue that a natural OOD setting to consider for the tasks (especially the maze task) is variable-size. The authors argue that this would result in "resolution inconsistencies". While it would indeed require careful considerations on the vision architecture to make it resolution independent, I believe it could make the tasks much more interesting and bring them in line with the textual arguments the paper makes on global-vs-local tasks and also the existing literature on length generalization, especially in light of the discussion on Globality Degree in the paper. 

I find it a bit surprising that pre-training is required (Figure 4).

Besides the two image generation-based models mentioned above, how does the proposed method relate to "The Predictron: End-To-End Learning and Planning" (Silver et al. 2017)? 

The term "Visual Scratchpad" could be slightly misleading, as it seems to suggest an approach that equips a language model with a modifiable visual buffer to support reasoning. An approach like that (with the same name) is discussed in "Can Visual Scratchpads With Diagrammatic Abstractions Augment LLM Reasoning?", Hsu et al. 2023

### Questions
One could argue that a natural OOD setting to consider for the tasks (especially the maze task) is variable-size. The authors argue that this would result in "resolution inconsistencies". While it would indeed require careful considerations on the vision architecture to make it resolution independent, I believe it could make the tasks much more interesting and bring them in line with the textual arguments the paper makes on global-vs-local tasks and also the existing literature on length generalization, especially in light of the discussion on Globality Degree in the paper. 

I find it a bit surprising that pre-training is required (Figure 4). 

Besides the two image generation-based models mentioned above, how does the proposed method relate to "The Predictron: End-To-End Learning and Planning" (Silver et al. 2017)? 

The term "Visual Scratchpad" could be slightly misleading, as it seems to suggest an approach that equips a language model with a modifiable visual buffer to support reasoning. An approach like that (with the same name) is discussed in "Can Visual Scratchpads With Diagrammatic Abstractions Augment LLM Reasoning?", Hsu et al. 2023

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose “global vision tasks”, which studies problems in which reasoning about the whole image is important. They develop a set of datasets involving binary prediction of graph connectivity, string connectivity, and maze connectivity. The paper introduces a method based on a ViT backbone that uses different types of intermediate supervision in the form of a scratchpad (single-frame scratchpad and recurrent multi-frame scratchpad).

### Strengths
I appreciate that the authors tackle a complex challenge of reasoning about graphs, strings, and mazes; I think it is an exciting direction that current VLMs struggle at, which we need a general solution for. I also like that the authors evaluate out-of-distribution generalization capabilities.

### Weaknesses
1. I have some fundamental disagreements with this categorization of “global visual tasks”. How much “global” vs “local” reasoning is required in a task is on a continuous scale. It depends on not only the task, but the specific instantiation of images and query. The authors point out that “a single patch containing cat whiskers significantly increases the likelihood that the model will classify the image as a cat”. It does, but we will need the full image to understand if the whisker belongs on the cat, or if the whisker instead belongs on a walrus, or if the whisker is instead in a photo on the wall where actually, a person is next to. Similarly, for tasks that the paper is exploring, by seeing that the entry/exit has an immediate connecting path instead of ending in a dead end also increases the likelihood that the maze has connectivity between the two points. How does one determine which tasks are “global” vs. not? The definition is ambiguous, and seems by the authors’ definition to depend on whether a few patches are informative enough to yield high probability predictions. What is considered high probability? On which model, trained on which tasks? How big and how many are these patches? Unfortunately, this task definition is not clear enough, though I appreciate the authors’ attempt to define a more challenging set of reasoning tasks.
2. The method proposed improves upon the baseline because it has more supervision. The paper states that having scratchpads improves performance compared to having no scratchpads, but we can not disentangle whether having a scratchpad in the model forward pass is more important, or whether the supervision is important, as each method is given different levels of supervision. The no scratchpad baseline is given only the final binary answer as supervision. The proposed single scratchpad model is given supervision on what the scratchpad should be. The proposed multi-scratchpad model is, I believe, given 50% of perfect frames for reasoning steps. (a) This does not convince me that scratchpads are helpful, but that intermediate supervision is helpful. (b) What happens when these intermediate frames are not available? Can you generalize to other complex reasoning tasks?  
3. The tasks proposed are all quite similar (binary classification, connectivity tasks in graphs, strings, and mazes). I would like to see performance on other vision challenges, even if it’s on synthetic data as well, like ARC. 
4. No baselines other than the base ViT are explored on this task. I would expect other visual reasoning prior works to be able to be evaluated.

### Questions
See the above four points. I don’t believe this paper is ready for publication in its current form. Though I think the tasks proposed and the broad idea of visual scratchpads is interesting, I don’t think the tasks are well defined, nor the experiments sound enough at this current stage. I would encourage more experimentation on what it means to endow a model with a scratchpad, as compared to additional supervision.

### Soundness
2

### Presentation
2

### Contribution
2

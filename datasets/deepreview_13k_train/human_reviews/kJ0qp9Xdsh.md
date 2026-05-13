# Towards Aligned Layout Generation via Diffusion Model with Aesthetic Constraints

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
Controllable layout generation refers to the process of creating a plausible visual arrangement of elements within a graphic design (\textit{e.g.}, document and web designs) with constraints representing design intentions. Although recent diffusion-based models have achieved state-of-the-art FID scores, they tend to exhibit more pronounced misalignment compared to earlier transformer-based models. The model is based on continuous diffusion models. Compared with existing methods that use discrete diffusion models, continuous state-space design can enable the incorporation of differentiable aesthetic constraint functions in training. For conditional generation, we introduce conditions via masked input. Extensive experiment results show that LACE produces high-quality layouts and outperforms existing state-of-the-art baselines.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a model for unconditional and conditional layout generation, and layout de-noising, where layout is defined as a set of rectangles of particular clas placed on the larger canvas, and conditioning can take form of number of rectangles of each class.The main contribution of the paper is modelling this process as continuous diffusion process, as opposed to the previous work which did it as a discrete diffusion process, after bining the rectangular coordinates. The method outperforms other layout generation models, as well as generic models such as MaskGIT, as measured by FID score and the IoU-related metric. The additional contribution is the introduction of a new aesthetic constraint, which further improves the results, used both as a loss during training, and during post-processing, where the rectangles are adjusted to reduce the object overlap.

### Strengths
Originality: While neither the method nor the application domain is new, it is novel to apply the continuous diffusion to the layout generation problem.
Clarity: The writing is sufficiently clear.
Quality: The paper features an ablation study highlighting the most important design decisions, such as post-processing, and the use of aesthetic constraint to minimize the loss. The authors promise to make the code and model checkpoints available, but do not provide them together with the submission.
Significance: I believe the work has significance in exploring the use of continuous diffusion to layout generation task, but given the somewhat "toy" setup of the experiments, the practical applicability and the wider significance of layout generation when specified in this formulation (given only types of objects or initial layout, without any information about the textual content of text fields, or image contents of the image fields, with evaluation done through FID and not human studies) may be limited.

### Weaknesses
There aren't significant drawbacks in the manuscript itself, with main potential weakness for me being the question of practicality of the proposed approach or its extensions to any practical application.

### Questions
Do you envision any practical applications of the proposed approach? Do you believe it could be extended in a way that would be useful for applications? In which way?

Sec. 2.2, "Conditional generation": Typo "We" --> "we"
Page 4, section "Overlap constraint": Typo "is monotonically identify" --> "monotonically identifies"
Page 6, Sec. 4.1, "Datasets": Typo "for both dataset" --> "for each dataset" or "for both datasets"

### Soundness
3 good

### Presentation
3 good

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
This paper introduces a novel diffusion model and training process for various conditional and unconditional layout generation tasks. Utilizing a continuous state-space design directly on the target attributes of elements in the layout, the proposed method incorporates both the standard diffusion training objective and novel aesthetic-based objectives (i.e., overlap, alignment) to improve the quality of generated layouts. These improvements lead to a new SoTA model across the majority of layout generation tasks in both the Rico and PubLayNet dataset.

### Strengths
- Novel formulation and diffusion model for directly using a continuous state-space for geometric and class properties, which could opens up a new avenue of research for layout generation by exploring diffusion in this space

- Unified framework for both unconditional generation and multiple conditional tasks

- Achieved SoTA in the majority of conditional tasks in both Rico and PubLayNet

- Novel formulation of Overlap and Alignment losses, and a time-dependent constraint schedule for effective optimization of aesthetic constraints during the diffusion process, which can independently benefit future research given the importance of these constraints in good layouts.

### Weaknesses
 - *Incomplete details for reproduction*: It appears that no training details of the models are reported in the paper and the appendix. It would be extremely helpful for future research for the author(s) the report details such as model architecture, noise schedule, loss schedule, constraint weights, etc, given that this continuous state-space of diffusion for layout generation was previously unexplored.

- *Limited inclusion of qualitative results and human-rater experiments*: It would further improve the paper if the author(s) can provide more qualitative results that demonstrates the differences between the proposed method and existing SoTA, and preferably include a lightweight human-rating study given that the metrics might not fully reflect human preference for layout generation.

- *Missing common metrics*: While FID and MaxIoU is quite representative and established in the layout generation literature, it will be helpful if the author(s) can include alignment and overlap indices, which can further show the effect of the proposed aesthetic constraints.

### Questions
- Can the author(s) provide more details of model training (e.g., loss schedule, model architecture), given that the introduced method applied diffusion in a novel and complex state-space that is non-trivial?

- Will the code be open-sourced if this paper is accepted?

- Can you further discuss the importance of the time-dependent constraint weight (preferably empirically)? This appears to be a very important parameter in incorporating aesthetic constraints.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on the controllable layout generation tasks, and formulates them as conditional generation processes in continuous space for aesthetic quality optimization. Two aesthetic constraint losses are proposed for global alignment and minimizing overlap in the layout during the training and post-processing stages. The experimental results show that the proposed method achieves the state-of-the-art performances on several benchmarks.

### Strengths
Compared to existing works that use discrete diffusion models, the proposed method based on continuous diffusion models can incorporate continuous aesthetic constraints in training. A new alignment loss is proposed to encourage the global alignment of elements. The proposed model can handle multiple generation tasks without retraining.

### Weaknesses
1. The key idea of this paper is to enable constraint optimization by formulating layout generation as conditional generation processes in continuous space. However, a post-processing step is still conducted. I was wondering about the advantage of the proposed method compared to those that directly apply the post-processing algorithm to the discrete diffusion models. Specifically, it's unclear how the continuous formulation inherently benefits constraint satisfaction compared to discrete methods when both require post-processing to enforce strict constraints. The paper should provide a more detailed analysis of the limitations of applying post-processing to discrete diffusion models and why the continuous formulation offers a more effective solution, even with post-processing.
2. Several layout generation related works [1-3] are neither cited nor discussed in the paper.
3. For the overlap constraint, the current loss pushes elements away from each other. However, in some cases, designers would intentionally use overlap to make the top element look closer to the viewer. For example, text elements are often located above the image elements in banner ads. The usefulness of such a constraint would be questionable by directly applying it to all elements in graphic designs. The paper should clarify the scope of the overlap constraint and discuss scenarios where it might not be suitable, especially in complex layouts with intentional overlaps.
4. Why the evaluation metrics do not consider overlap, while the aesthetic constraints contain the overlap in layout?

### Questions
1. How to determine the time-dependent constraint weight and the threshold used in the post-processing stage?
2. Are there any qualitative results that demonstrate diversity of the generated layouts?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a novel unified continuous diffusion model, namely LAyout Constriant Diffusion modEl (LACE) for layout generation. To address the aesthetic issue of the diffusion model, the authors propose two differential constraints, including alignment constraint and overlap constraint, to address element arrangement and overlap issues. The experiments show that the proposed LACE makes a good performance on PubLayNet and Rico datasets.

### Strengths
* The paper is interesting, well-written and original, and my impression is positive.
* The proposed framework for various generation tasks is smart and effective.
* The quantitative experiment results show the superiority of the proposed method over existing approaches.

### Weaknesses
 * I would appreciate it if the authors give more details of the proposed framework given different conditions.
* The ablation study can be extended to illustrate the contribution of two constraints. For example, Figure 3 only shows the visualization result of global alignment and overlap constraints. I would recommend studying the effectiveness of all sub-constraints, e.g., local and global alignment, quantitatively and qualitatively.
* The limitations of the proposed method should be discussed. This can give good guidance for the application in real-world situations.

### Questions
Please refer to the weakness part.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

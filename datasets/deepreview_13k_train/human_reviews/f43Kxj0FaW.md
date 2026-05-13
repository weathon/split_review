# Meta-Prior: Meta learning for Adaptive Inverse Problem Solvers

- Decision: Reject
- Scores: 3, 3, 3, 5

## Abstract
Deep neural networks have become a foundational tool for addressing imaging inverse problems. They are typically trained for a specific task, with a supervised loss to learn a mapping from the observations to the image to recover. However, real-world imaging challenges often lack ground truth data, rendering traditional supervised approaches ineffective. Moreover, for each new imaging task, a new model needs to be trained from scratch, wasting time and resources. To overcome these limitations, we introduce a novel approach based on meta-learning. Our method trains a meta-model on a diverse set of imaging tasks that allows the model to be efficiently fine-tuned for specific tasks with few fine-tuning steps. We show that the proposed method extends to the unsupervised setting, where no ground truth data is available.
In its bilevel formulation, the outer level uses a supervised loss, that evaluates how well the fine-tuned model performs, while the inner loss can be either supervised or unsupervised, relying only on the measurement operator. This allows the meta-model to leverage a few ground truth samples for each task while being able to generalize to new imaging tasks. We show that in simple settings, this approach recovers the Bayes optimal estimator, illustrating the soundness of our approach. We also demonstrate our method's effectiveness on various tasks, including image processing and magnetic resonance imaging.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a method of meta learning to train a meta-model on various imaging tasks. The paper claims that finetuning the meta-model makes it easier to perform on new tasks that are unseen during the training.

### Strengths
- The proposed method to learn some priors through the meta-model which is expected to generalize across different tasks seems to be interesting.

### Weaknesses
 - The paper structure and writing can be further improved, especially abstract and introduction. It is confusing to understand what is the motivation and what is novelty even after reading through the introduction.

- Motivation for learning meta-model. Although it looks interesting from the toy model study, why do we want to learn such a meta-model from different tasks? To converge fast or achieve better results in a new task? But why can the meta prior help to achieve this goal? What is the physical meaning of the learned prior, especially when there are large domain gaps between training and testing tasks such as generalized to MRI imaging? What kind of meta training tasks should be helpful and how to choose such tasks? It is not clear about the grounding support for this proposed method.

- No comparison with baseline methods. The proposed method looks like using a very standard meta-learning framework to train this meta-model. What is the novelty and superiority of the proposed method compared to other meta-learning method such as MAML?

- No comparison with other methods in all the application tasks. As shown in Figure 4 and 6, the results demonstration are mainly the analysis within the proposed method with different finetuning steps or training settings. But there is no comparison with other SR methods or MR reconstruction methods. How can it be argued the proposed method can be a good approach to achieve good results on those tasks? For example, as shown in Figure6, the MRI reconstruction results with acceleration factor = 4 seems to be quite lower-quality than many existing methods either supervised or unsupervised.

- I would suggest using a table instead of a figure with so many curves as Figure 5 for results comparison. It is hard to distinguish when many curves are plotted with many overlaps. Showing the network depth may be good additional experiments, but it seems hard to draw some consistent conclusion from these curves.

- Providing a framework figure may be helpful to better illustrate the proposed method especially with meta-training and inner-training.

### Questions
Please see weakness for the details of questions.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a meta-learning approach to solve inverse problems, considering both supervised or unsupervised inner-optimization in a MAML-based meta-formulation. The authors examined the theoretical properties of this “meta-prior”, and experimentally examined its effectiveness compared to learning from scratch in a collection of imaging tasks (de-nosing, TV recovery, deconvolution, inpainting, SR, and MRI reconstruction).

### Strengths
The idea of using a meta-learning approach to learn to solve inverse problems across a set of tasks is interesting.

The relatively high diversity of imaging tasks considered in the experimentation is appreciated.

### Weaknesses
Two main feedback about the contribution of this week, despite the interesting idea, is the limited methodological novelty and the limited experimental evaluations.

1. The proposed method is primarily a direct application of MAML to image reconstruction tasks — what are the potential challenges in this application and what novel solutions are needed to overcome these challenges are not clear. See some of the questions in the next block.

Specifically, the adaptation of MAML to this domain lacks a clear articulation of the unique challenges posed by inverse problems in imaging. While MAML has shown promise in various domains, its direct application here without addressing the specific nuances of image reconstruction tasks raises concerns about the novelty. For instance, how does the method handle the ill-posed nature of many inverse problems, where multiple solutions might exist? How does it address the potential for overfitting to specific noise patterns or imaging artifacts in the training data? These questions are not adequately addressed, leaving the reader to wonder about the method's robustness and generalizability.

2. The experimental evaluation is very limited and the descriptions lack many details (see detailed questions below). Furthermore, even just compared to training from scratch on test data only (which is a weak baseline), the benefit of the proposed meta-approach is not significant nor consistent. Please see the detailed questions below.

Specifically, the paper lacks a comprehensive comparison against established methods for each task. For instance, in the de-noising task, a comparison against BM3D or other state-of-the-art methods would be beneficial. Similarly, for super-resolution, a comparison against methods like EDSR or RCAN would provide a better understanding of the proposed method's performance. The lack of details regarding the training process, such as the number of iterations, learning rate schedule, and convergence criteria, also hinders the reproducibility of the results.

### Questions
1. Questions regarding methodology. 
a. What are the restrictions on the size of A? Does it have to be the same? How are these achieved when x’s and y’s across different image reconstruction tasks are of different dimensions? More generally, what are the requirements on A across tasks?
b.  The stability and cost of MAML training, especially regarding which portion of the primary model to update during inner optimization, is a non-trivial issue. In PDNet, which part of the architecture is being fine-tuned in the inner optimization?

2. Questions regarding experimentations.
a. It is not clear what are the number of data samples used on each training task; what is the size of the context data (referred to as training data in the paper) for each task versus the query data (referred to as test data in the paper). What about the fine-tuning at test time — what are the number of data used in training/fine-tuning, and how many samples are used for evaluating testing performance, throughout all experiments including tasks seen in training and those unseen. 
b. On tasks included in training, fine-tuning from meta-models seems to be only compared to the meta-model itself. To understand the contribution of the work, it will be necessary to compare the fine-tuned models to 1) task-specific models trained on the same meta-training data, and 2) models that are trained on the overall meta-training data across all tasks, without and with fine-tuning to the test data used in each tasks.
c. On tasks included in testing, fine-tuned models are only compared to training from scratch on the test data. Again, baselines are needed that considered the same meta-training data (as listed above).
d. Please clarify, when test-time fine-tuning is unsupervised, does that mean the meta-training also considers unsupervised fine-tuning in the inner optimization? 
d. The benefits of the presented model needs to be better highlighted.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a meta model training procedure, that trains a deep models simultaneously on different inverse problems (denoting, restoration with total variation regularization, deconvolution, and image inpainting) while making sure the fine-tuned models (Starting from the meta-model) performing well. The paper formulates the problem first in general form, then it considers some simplified cases where it approaches the optimal bayesian rule. The paper evaluates the performance on the super resolution and MRI reconstruction task.

### Strengths
The paper presents a novel approach to meta-model training that is worth considering. It is well-written and technically sound.

One notable strength of the paper is its ability to demonstrate the method's effectiveness in simplified cases where it converges to the optimal estimator. This simple illustration is important as it underscores the method's potential utility in real-world applications.

The paper also offers insightful perspectives, particularly in discussing the relationship between the solution and the kernel space. This insight serves as a motivation for the approach.

### Weaknesses
One significant point of criticism in the paper relates to its evaluation process, which has certain shortcomings.

Firstly, the paper lacks clarity in specifying the specific datasets used for evaluating the method's generalization capabilities. Vital details (such as the dataset sizes, the source of the images, and the specific transformations applied to the data) are missing. This omission makes it challenging for readers to gauge how the proposed method performs in different real-world scenarios or how representative the result is. For example, it is unclear if the super-resolution task uses standard benchmark datasets like Set5, Set14, or Urban100, and what pre-processing steps were applied. Similarly, for the MRI reconstruction task, details about the acquisition protocol, the specific type of MRI data (e.g., T1-weighted, T2-weighted), and the undersampling strategy are absent. The lack of these details makes it difficult to reproduce the results and assess the method's robustness.

Another notable issue is the limited comparative analysis. The paper primarily focuses on comparisons among different versions of its own method (with varying numbers of fine-tuning steps) and random initialization. However, the absence of comparisons to basic pre-training methods [e.g. as suggested in Chapter 8.7.1 of "Deep Learning" by Goodfellow et al. (2016)] narrows the paper's significance. A more comprehensive evaluation, including comparisons to established pre-training techniques, and also to other methods that solve similar inverse problems (such as those based on alternating direction method of multipliers (ADMM) or plug-and-play priors), would offer a better understanding of the proposed method's effectiveness and its relevance within the broader machine learning field. The current comparison only shows the impact of the number of fine-tuning steps, which is not sufficient to validate the meta-learning approach itself.

### Questions
n/a

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a meta-prior model that leverages meta-learning for adaptive inverse problem solvers. The authors explored both supervised and unsupervised settings for the inner loop. The proposed model can be generalized to a new imaging task with as few as 1 step. The experiments were conducted on four diverse imaging tasks and evaluated on image super-resolution and MRI tasks.

### Strengths
1. This paper explored the meta learning for imaging tasks, which can be quickly adapted to a new imaging task.
2. The proposed method is supported by theoretical analysis.
3. The experiments cover diverse imaging task.

### Weaknesses
1. The experimental results were not promising. Specifically, the meta-learned model's performance appears to be significantly below that of task-specific models, as seen in Figure 3. This raises concerns about the practical utility of the proposed meta-learning approach, especially given the computational overhead associated with meta-training. The lack of substantial improvement over task-specific models undermines the core motivation of rapid adaptation to new tasks.
2. Some strong baselines could be considered for comparison. The current comparisons lack a thorough evaluation against state-of-the-art methods in each of the specific imaging tasks. For instance, in super-resolution, methods that leverage deep learning architectures with specific inductive biases for image reconstruction should be included. Similarly, for MRI reconstruction, comparisons with advanced compressed sensing techniques and deep learning methods tailored for MRI would provide a more comprehensive assessment of the proposed method's performance. The absence of these comparisons makes it difficult to gauge the true novelty and effectiveness of the proposed approach.

### Questions
1. In Fig. 2, the similarity between learned and analytic solution seems not close. Absolute difference map may be helpful to visualize the difference.
2. In Fig. 3, the proposed meta-model performs worse than task-specific models. 
3. For the generalization experiments, (i) quantitative results were missing, (ii) results in Fig. 6 were not promising as there is clear shift from ground-truth, and (iii) I think some unsupervised or self-supervised baselines could be compared as there should be more data for unsupervised training in imaging tasks.

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
2 fair

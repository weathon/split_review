# Advancing the Adversarial Robustness of Neural Networks from the Data Perspective

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 5, 3

## Abstract
Robustness in machine learning is a widespread concept and one of the pillars of trustworthiness, ranging from a model's resistance to noise---benign and adversarial---to the reliability of benchmarking. In this work, we analyse the robustness of labelled data which we argue corresponds to the data manifold's curvature as perceived by a model during training and thus establish a connection to its adversarial robustness. This view provides an intuitive explanation for our empirical results showing that neural networks acquire adversarial robustness much slower in the least robust regions. In combination with minor adjustments to the learning rate, the new concept offers a means to emphasise these regions during training and increase the model's overall adversarial robustness, even when using identical computational resources.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper is on adversarial robustness and proposes that models are particularly vulnerable in regions where the data manifold would be perceived as highly curved by the model. Some theoretical developments are proposed to support that. Experiments are conducted to demonstrate that by oversampling data samples in curved areas and using them to generate new artificial samples for training would improve robustness.

### Strengths
- Tackle a significant question on understanding better the input space of deep models and the corresponding robustness to adversarial attacks.
- Support claims through elaborated theoretical developments.

### Weaknesses
 - The paper and overall presentation is very difficult to follow. Although the authors seem to know very well their topic, the communication is lacking and a reader not in that specific field gets lost quite quickly.
- The notion of curvature on the manifold is really unclear to me and not very well explained in the paper. But it appears in the end we are looking at distance between samples, the notion of curvature is there to support theoretical developments that are not directly translated in practice.
- The technical aspects of the experiments section are not very clear nor clearly explained. I guess that the reader should look at some of the referenced papers like Karras et al. (2022) and Wang et al. (2023), but still I would like to get more background and specific details to better understand what is done in the experiments. It is quite unclear to me that the details provided would make results reproducibility easy.
- It is difficult to figure out what exactly the experimental results are providing as support to the conclusion. The differences in Table 2 between the results is very small, and as such not very convincing that the proposal is of any meaningful effects for improving robustness.
- Overall, the experiments are not very well explained and presented and the results are very difficult to interpret. I have a hard time making sense of all this.

### Questions
Looking at equation 1, if we assume that $d(p_i,p_j)$ is an Euclidean distance and that $\|y(p_i)-y(p_j)\|$ is basically equal to zero or one when using $y(p)$ as one hot vector over the classes, it means that in practice, the proposal consists of looking 1/distance to the nearest sample from a different class from the current one. Is this correct? That’s what was used for the experiments?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors investigate the robustness of neural networks undergoing training via gradient descent through the lens of the geometry of the data. The authors analyze the dynamic of robustness by proposing a measure of “perceived curvature”. Essentially, the perceived curvature resembles the local Lipschitz constant exhibited by the neural network, modified so that the predictions are mapped to the discrete set of labels. Algorithmically, the authors analysis implies that by emphasizing the least-robust elements of the training set, modest gains in adversarial test error can be achieved. 

The authors perform exploratory experiments by showing some correlation between the perceived manifold curvature and robustness as well as visualizations depicting the most and least robust examples and data sensitivity.

While the paper is interesting and the experiments are reasonably comprehensive, I do not think this paper offers particularly new or deep insight into the nature of adversarial robustness, beyond what has been explored by prior work. These issues coupled with the quality of the writing and composition make me inclined to reject, although I am open to changing my score.

### Strengths
- Interesting application of diffusion models to investigate the adversarial robustness of a neural network for certain examples via a notion of perceived curvature
- Comprehensive visualizations, plots to demonstrate the relationship between per-sample-robustness, sensitivity, and margin

### Weaknesses
 
**Contribution / significance**

The basic observation made by the paper regarding the relationship between robustness, sensitivity, and sample importance during training is interesting, but well-known. To strengthen the contribution and significance of the work, the authors should clarify the contribution of their analysis in the context of the previous work, or demonstrate some actionable insights- e.g. an algorithm that exhibits superior adversarial robustness relative to existing techniques. The authors' notion of 'perceived curvature' is not sufficiently differentiated from the existing concept of the local Lipschitz constant, especially given the mapping of predictions to a discrete label set. The modification to incorporate the discrete label set does not introduce a fundamentally new geometric perspective. The paper needs to more clearly articulate how this measure of perceived curvature offers a novel understanding of adversarial vulnerability beyond what is already understood through the lens of local smoothness and decision boundary geometry.

**Missing relevant work**

There is some missing existing work that should be cited that explores the emphasis of certain vulnerable examples in the training set to enhance clean and robust test-set performance. E.g. reweighting methods such as [1, 2], subsampling methods such as [3],  and others that I do not list (e.g. on applications of diffusion models to the adverarial robustness context). The paper does not adequately discuss how its findings relate to or differ from these existing methods. Specifically, the paper should clarify whether the proposed 'perceived curvature' metric provides a unique advantage over existing methods for identifying vulnerable examples, or if it simply recapitulates known phenomena through a different lens. The connection to diffusion models also needs to be better motivated, as it is not clear why this is the appropriate tool for analyzing the geometry of adversarial robustness.

[1] Zhang et al., Geometry-aware Instance-reweighted Adversarial Training, ICLR 2021

[3] Wang et al., Probabilistic Margins for Instance Reweighting in Adversarial Training, NeurIPS 2021

[3] Zhang et al., Attacks Which Do Not Kill Training Make Adversarial Learning Stronger, ICML 2020

**Writing and composition**

The writing could use some work. Several seemingly important statements are made, but I found it difficult to parse the english. For example, the following are examples:

_However, we argue that the labels evoke the impression of disconnectedness, which a model then tries to account for when remodelling the perceived decision boundaries during training._

_Although the skewed label distribution of s (comp. Figure 5) should come as a disadvantage, one may, a priori, argue for the converse…_

I also could not understand the idea of figure 1. The preceding text states that they intend to illustrate some previous claim, but the previous claim seems to be about data sensitivity and curvature, while figure 1 details the adversarial robustness / robustness gap for models trained for different numbers of epochs with a certain overlap between the training and validation sets. The experiment seems very complicated and difficult to understand compared to the claim that 

_It appears beneficial to emphasise the least robust elements during training to help a model gain robustness in regions where it struggles the most._

### Questions
- Could the authors clarify their contribution in the context of existing methods / analysis (e.g. by providing some explanation for the efficacy of existing methods to enhance robustness)?
- One claim is that _diffusion model connects regions of non-robust data to more prominent semantic changes, which we take as the model accounting for a more significant perceived curvature._ Can this be made more precise?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper leverages concepts from metric geometry to understand how neural networks perceives the geometric property, particularly curvature, of the data manifold. To be more specific, it argues that data that more susceptible to adversarial perturbations are connected to regions in the data manifold with high curvature and vice versa. The paper proposes to use Eq 1 to quantitatively measure such curvature information as perceived by the model. The empirical studies in this paper are based on CIFAR10 and CIFAR100. A series experiments are performed to verify the proposed connection between curvature and model robustness. Building on these findings, the paper propose a learning rate strategy that increases the adversarial robustness model against $\ell_2$ and $\ell_\infty$-norm bounded adversarial perturbations generated using AutoAttack in a white-box setting.

### Strengths
**Originality**:
The paper proposes a very novel (to my knowledge) and unique perspective to understand the adversarial robustness of neural networks. The proposed concept is also quite intuitive: certain data points are inherently more susceptible to adversarial attacks due to specific properties they possess.

**Quality**:
I am not an expert in manifold learning nor in metric geometry, so this limit my ability to properly assess the technical details of Section 3.  However, on the empirical side, the paper tries to provide several experiments to validate their hypothesis regarding the connection between model's robustness and its perception on the curvature of data manifold.

**Significance**:
The proposed data perspective provides an interesting direction on which future methods can be designed to better address the adversarial robustness problem.

### Weaknesses
The paper has two main weaknesses.

1. The clarity of the presentation and the quality of interpretation regarding the empirical observations could benefit from further refinement to enhance understanding. Specifically, the connection between the proposed curvature measure and the observed robustness is not always clear. For example, the discussion around Figure 2 does not fully explain why pseudo-labeled data exhibit different sensitivity patterns, and the interpretation of Figure 3's inverted patterns between MDS and RTE is not sufficiently detailed. The paper would benefit from a more rigorous analysis of these results, including a more in-depth discussion of the underlying mechanisms.
2. The improvement in adversarial robustness is very marginal. The reported 0.2% improvement, while claimed to be equivalent to 800 epochs of training, is not substantial enough to demonstrate the practical impact of the proposed method. Furthermore, the paper lacks statistical analysis to support the significance of this improvement. It is unclear whether this improvement is consistent across multiple runs or if it is simply due to random variations. The absence of standard deviations or confidence intervals makes it difficult to assess the reliability of the results.

### Questions
**Figure 1**:
I suppose this is on CIFAR10. How are the most/east robust elements defined?
The claim at the bottom of page 1 is essentially that by training for another 2000 epochs, the most robust training data (at epoch 400) become 1% more robust (at epoch 2400); and the least robust training data (at epoch 400) becomes 7.5% more robust (at epoch 2400). Is that correct? However, are we tracking the same training data? Is "eval_adversarial_acc" the validation accuracy? 

Also, it seems that the author uses the term "validation set" as a parts of the training set, which is odd.

I did not understand "For CIFAR-100, we disregarded the 40 least robust elements because of distorted robustness values due to differently labelled duplicate images". What are "differently labelled duplicate images"? What happens to the result if we include them?


**Figure 2**:
My understanding is that the absolute sensitivity is computed using Eq1. How are the relative sensitivity computed? 
In the analysis of Figure2, it is said that "The generated data, in particular, admit much shorter tails, indicating more robust elements overall. " However, arent the curves of  1m-1 and 1m-2 quite similar to cifar-10/100/100s? Also, why does the pseudo-labbeled data have very different sensitivity? 

**Figure 3**: 
The interpretation of the results are not clear. Do we know what the differences in the mechanisms of MDS and RTE are that leads to this inverted pattern? It would be very helpful to interpret the result if there is some brief explanation on what those methods are and why they are used.

**General suggestions on all figures**:
Please consider using subcaptions to increase the clarity of the results.

**Exploration experiments**:
In the setup column of Table2, just to clarify: minus v, "-v" means removing v from the training set, and (v) means all the validation accuracy is based on v. Is this correct?
Are the most sensitive data points computed based on another pre-trained model?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors establish a connection between the curvature of the data manifold, as perceived by a model during training, and the model’s adversarial robustness. They provide empirical evidence showing that neural networks gain adversarial robustness more slowly in less robust regions of the data manifold.

### Strengths
- A novel perspective on adversarial robustness through the lens of data robustness (curvature of data manifold)
- Claims are backed up by empirical results
- Generally good writing

### Weaknesses
The most critical issue is the lack of comparison with prior works. It is well-known in the literature that not all data points are equally susceptible to adversarial attack, and this has motivated the design of various variants of adversarial training ([1,2,3,4,5,6]) to (adaptively) focus on a subset of training samples. The authors made a similar observation "it appears beneficial to emphasize the least robust elements during training", but seemed to be completely unaware of this line of research. Without proper discussion and comparison with prior works, it is hard to fairly position and evaluate this work in the vast literature.

Specifically, the paper does not discuss how its findings relate to curriculum learning in adversarial training [1], which explicitly focuses on ordering training samples based on their difficulty. Similarly, the concept of re-weighting training samples based on their robustness, as explored in [4,5], is not addressed. The paper also lacks a discussion of methods that maximize input space margins [2] or explore decision boundary dynamics [6], which are relevant to the geometric perspective the authors claim to adopt. The absence of these comparisons makes it difficult to assess the novelty and significance of the proposed approach. Furthermore, the paper does not address the concept of on-manifold adversarial examples [7], which is directly relevant to the discussion of data manifold curvature and robustness.

### Questions
One of the mainstream hypotheses regarding adversarial examples is the off-manifold assumption ([7]): "Clean data lies in a low-dimensional manifold. Even though the adversarial examples are close to the clean data, they lie off the underlying data manifold." I would like to understand how this hypothesis is related to your findings (focusing on data manifold with high curvature is helpful in adversarial training).

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

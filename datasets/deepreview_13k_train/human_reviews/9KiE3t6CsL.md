# ALBAR: Adversarial Learning approach to mitigate Biases in Action Recognition

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
Bias in machine learning models can lead to unfair decision making, and while it has been well-studied in the image and text domains, it remains underexplored in action recognition. Action recognition models often suffer from background bias (i.e., inferring actions based on background cues) and foreground bias (i.e., relying on subject appearance), which can be detrimental to real-life applications such as autonomous vehicles or assisted living monitoring. While prior approaches have mainly focused on mitigating background bias using specialized augmentations, we thoroughly study both biases. We propose \approachname, a novel adversarial training method that mitigates foreground and background biases without requiring specialized knowledge of the bias attributes. Our framework applies an adversarial cross-entropy loss to the sampled static clip (where all the frames are the same) and aims to make its class probabilities uniform using a proposed \textit{entropy maximization} loss. Additionally, we introduce a \textit{gradient penalty} loss for regularization against the debiasing process. We evaluate our method on established background and foreground bias protocols, setting a new state-of-the-art and strongly improving combined debiasing performance by over \textbf{12\%} on HMDB51. 
Furthermore, we identify an issue of background leakage in the existing UCF101 protocol for bias evaluation which provides a shortcut to predict actions and does not provide an accurate measure of the debiasing capability of a model. We address this issue by proposing more fine-grained segmentation boundaries for the actor, where our method also outperforms existing approaches.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a novel adversarial learning-based method to mitigate biases in action recognition, which provides simplified end-to-end training and does not require any labels/classifiers for bias-related attributes.

### Strengths
+ This paper is well-written and well-organized.
+ Good performance on the popular action recognition datasets.

### Weaknesses
This paper introduces adversarial learning into action recognition, which is a relatively novel idea, but I have some concerns as follows.

- Are there more visual examples that can depict biases in action recognition?
- Whether the method proposed in this paper can be used for skeleton-based action recognition task？

### Questions
See weaknesses

### Soundness
3

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
4

### Summary
The paper proposes a method to improve generalization capability of an activity recognition method in temporally-segmented video datasets.  The method focuses on an adversarial approach to removing biases from static elements of the scene.  The paper takes a random frame from the video and creates a "static" video by repeating the frame the same length as the original clip, then using this static clip as the adversary.  The paper combines this adversarial approach with other reasonable loss terms.  It demonstrates state of the art accuracy on the problem.

### Strengths
- The problem of bias mitigation in ML is seriously important.  The paper proposes a concrete approach to mitigating clear bias problems in action recognition.

- The entropy maximization term makes sense for avoiding the static cues.

- The paper uses practical mechanisms to overcome the challenges of training the models.

- The evaluation is performed on a recent OOD benchmark for bias analysis, and performs well relative to other methods.

- The writing is mostly clear and concrete.

### Weaknesses
 - The paper is is somewhat "small" in that although it describes what seems to be a new method and its evaluation on reasonable benchmarks, there is little discussion around key elements of the method, their limitations, their rationale, etc.  (see questions)
EDIT: The review discussion thus far, and the other reviewers seems to have identified similar concerns.  Discussion around this point suggests there is some generality to visual problems, but some concern about the narrowness of the contribution remains.  Most of the comparative papers are in CV conferences.  I raised my scored, but this point should be discussed among the AC pair/triplet however ICLR is doing it this round.

- Does the "static clip" way of approaching video bias mitigation, have broader utility in video understanding or beyond?

- Certain interesting experiments are omitted, even though the writing suggests they may be useful.  For example, L233 reads "A naive application of Eq. 2 results in degraded performance."  What exactly is a naive application?  Furthermore, this implies that the two parts of Eq. 2 is individually interesting; in particular, does the right hand side do anything?  The ablation study does not include these two parts separately.



### Questions
- The mechanism for adversarial learning in the paper is very specific to action recognition.  How can this mechanism be generalized to be of broader interest to the ICLR community?

- The method works by sampling any frame from the video and repeating it for a static clip.  Why any frame?  Aren't certain frames better or worse than others for the stated goal?  (The pre-segmented nature of the datasets in question create itself an algorithmic bias.  In the stated real world application deployments no such pretemporal segmentation is avavilable, and hence brings into question the feasability of the method in practice.)  But, more concretely to the task, why is there no analysis whatsoever on the impact of this frame selection?  Even for a subset of one dataset, it would have been interesting to understand the breadth of potential with different static clips.

- Wouldn't it be clearer to concretely specify that the $\vby$ action label notation is a one-hot vector?  It is one-hot, right?

- At line 218, shouldn't "maximized" be "minimized"?  At least, something in that sentence does not match up: "p(t) is still matched to gt distribution y, but the similar ....maximized"  Maximizing the "similarity" (a loose term here) is minimizing the ce loss.

- How are there reasonable IID results in Table 3 for the case that Ladv is not used ---> when it is not used, there is no actual gradient to guide the model to do any recognition?

### Soundness
3

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
5

### Summary
This paper presents ALBAR, an adversarial learning method aimed at reducing biases in action recognition models. The study focuses on addressing background and foreground biases, which can impact the performance of applications such as autonomous vehicles and assisted living monitoring. ALBAR utilizes an adversarial training technique to minimize the model's dependence on static background cues, encouraging the use of dynamic motion information for action classification.

### Strengths
S1: This paper resents state-of-the-art results on established SCUBA/SCUFO background/foreground debiasing benchmarks, and formulation is technically sound.

S2: Several ablations show the contribution of each component.

### Weaknesses
W1: Although the results demonstrate that the model outperforms state-of-the-art methods, the technical contribution is incremental and purely based on previously introduced techniques.

W2: How is the fairness of the comparative experiments ensured in this paper, and how are the results of the comparative methods obtained?

W3: The ALBAR performs well on specific bias evaluation protocols, but its generalization capabilities to new types of biases or different domain tasks have not been fully validated.

W4: Although the paper proposes a simplified end-to-end training framework, adversarial training often involves additional computational costs. The paper does not discuss the computational efficiency and scalability of the ALBAR method in detail.

### Questions
Although the results demonstrate that the model outperforms state-of-the-art methods, the technical contribution is incremental and purely based on previously introduced techniques.

How is the fairness of the comparative experiments ensured in this paper, and how are the results of the comparative methods obtained?

The ALBAR performs well on specific bias evaluation protocols, but its generalization capabilities to new types of biases or different domain tasks have not been fully validated.

Although the paper proposes a simplified end-to-end training framework, adversarial training often involves additional computational costs. The paper does not discuss the computational efficiency and scalability of the ALBAR method in detail.

### Soundness
1

### Presentation
1

### Contribution
1

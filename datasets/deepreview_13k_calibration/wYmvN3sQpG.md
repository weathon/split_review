# Benign Oscillation of Stochastic Gradient Descent with Large Learning Rate

- Decision: Accept
- Avg Score: 5.67
- Scores: 8, 6, 3

## Abstract
In this work, we theoretically investigate the generalization properties of neural networks (NN) trained by stochastic gradient descent (SGD) with large learning rates. Under such a training regime, our finding is that, the oscillation of the NN weights caused by SGD with large learning rates turns out to be beneficial to the generalization of the NN, potentially improving over the same NN trained by SGD with small learning rates that converges more smoothly. In view of this finding, we call such a phenomenon “benign oscillation”. Our theory towards demystifying such a phenomenon builds upon the feature learning perspective of deep learning. Specifically, we consider a feature-noise data generation model that consists of (i) weak features which have a small $\ell_2$-norm and appear in each data point; (ii) strong features which have a large $\ell_2$-norm but appear only in a certain fraction of all data points; and (iii) noise. We prove that NNs trained by oscillating SGD with a large learning rate can effectively learn the weak features in the presence of those strong features. In contrast, NNs trained by SGD with a small learning rate can only learn the strong features but make little progress in learning the weak features. Consequently, when it comes to the new testing data points that consist of only weak features, the NN trained by oscillating SGD with a large learning rate can still make correct predictions, while the NN trained by SGD with a small learning rate could not. Our theory sheds light on how large learning rate training benefits the generalization of NNs. Experimental results demonstrate our  findings on the phenomenon of “benign oscillation”.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the generalization benefit of using large learning rates in stochastic gradient descent. Specifically, in the setting of a two-layer convolutional neural network, it is shown that although using a large learning rate causes the loss value to oscillate, it indeed further enables SGD to do feature learning. The main result is proven under the assumption of a feature-noise data generation model, where the strong and weak features are separated by the $\ell_2$ norm. Empirical evaluations are also provided to support the theoretical results.

### Strengths
- The paper is well written and easy to follow, and the authors have explained the theoretical intuition clearly through the example of a single training data in Section 3.

- The generalization benefit of large learning rates is an important topic in the community. This paper presents an interesting result in this direction, though the feature-noise data generation model seems somewhat artificial.

- The theoretical analysis in this paper is very solid.

### Weaknesses
 - It is not clear if the feature-noise data generation model is a natural model that contains separate strong feature, weak feature, and noise. 

- The network structure seems to be tailored to the feature-noise data generation model, as it applies a separate weight vector to each of the patch. Although the authors claimed that the main results can be further generalized, but it is not immediately clear how.

- The oscillating condition that $|y_{i_t} f(\mathbf{x}_{i_t};\mathbf{W}^{(t)} - 1|\geq \delta$ is proposed as an assumption, rather than being proved.

### Questions
1. How to justify the feature-noise data general model? E.g., is this a natural assumption for real-world dataset like CIFAR-10?

2. The authors discussed some necessary conditions of Assumption 4 on the loss oscillation. Are there any comprehensible sufficient conditions?

3. The authors mentioned a bit about the edge-of-stability regime. Can the authors expand a bit more on this? For example, how is the oscillation assumption related to EoS?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors study the effect of large learning rate SGD on a prediction task with a one hidden layer CNN network. More specifically, they study a binary classification problem with weak and strong signal patches and theoretically argue that there is a generalization separation between small and large learning rate SGD training:
- for small learning rate, SGD is unable to learn the weak signal
- for large learning rate, SGD is able to learn the weak signal     

They argue that the oscillatory behavior of large learning rate SGD is a crucial feature of this fact. 
They also illustrate these results with experiments.

### Strengths
The study of SGD with large learning rates is believed to be crucial to understand the good learning properties of neural networks. Yet, its analysis is in many cases very difficult to handle: the oscillations, the movement due to noise are technically challenging to analyse. 

In this perpective, the authors do a very good job providing a setup for which they 'prove' that such a dynamical behavior leads SGD to good generalization.

On top of this, I find the paper very well written, the setup very clear and the explanation with the toy model on Section 3 very good.

### Weaknesses
In my opinion, here is a weakness of the paper:

- the authors claim to perfectly prove that the oscillatory behavior of the SGD iterates lead it to learn the weak signal, but they need to assume that the iterate oscillate in the first place. While they show that this oscillation is *consistent* with their hypothesis, it could be great that the authors comment a bit more of this necessity to assume this. How difficult would it be to remove this hypothesis ? Is the problem to control that the iterates do not diverge ? Or on the contrary that they do no converge locally ?

- If this is the second option, could the authors add some (bounded) label noise at each iteration to show this? This is what is explained to be done in a series of paper like *Label noise (stochastic) gradient descent implicitly solves the Lasso for quadratic parametrisation* L. Pillaud-Vivien et al., COLT, 2022. Could the authors comment on this?

### Questions
- On top of the questions raised above, I really would like to understand whether the setup described above has can also guide on what appears to be a simple problem like diagonal linear networks where the oscillations lead to sparse features.

Does the analysis of the authors shed light onto this problem ?

- Also, it appears that the initialization is very small ($d^{-1/2}$ with a large $d$). Can the authors comment on the necessity of such an unusual initialization ?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies feature learning when the learning rate is large, showing that when there is a strong oscillation in the training, only data points with weak signals are learned

### Strengths
I think the message and the insight is sufficiently novel and relevant -- how large learning helps "selecting" a subset of data points to be learned. 

The data generation model of strong and weak patches is also quite interesting and can serve as a good starting point for future works

Also, the signal to noise ratio of the data and gradient plays an important role in the proof and discussion and, therefore, I think the result does catch some level of essence of SGD training in neural networks. Although, on this point, I think the authors should compare with the study of how signal-to-noise ratio affects the learning at a large learning rate in (1) https://arxiv.org/abs/2107.11774 and (2) https://arxiv.org/abs/2303.13093

### Weaknesses
In my opinion, what prevents me from recommending this paper is that the problem setting feels too artificial. The following are the specific problems in my opinion

1. The problem setting. First of all, what is a ReLU^2 activation function? I have never seen this. Is ReLU more essential to the proof or is the quadratic effect more essential to the proof? Does the result hold for ReLU? Does the result hold for the quadratic activation? This is unanswered in the paper. To me, this activation neither feels theoretically appealing nor practically relevant

2. Problem setting 2. The second layer is not trained. Essentially, we understand that training with one layer is very different from training multiple layers simultaneously. For example, see https://arxiv.org/abs/2205.11787

3. Problem setting 3. The model architecture -- the authors refer to the model as a "CNN," which just does not feel right to me. I doubt if the majority of readers would agree that this model is indeed a CNN. 

In summary, the point is the same, the problem setting is not sufficiently simple to be considered theoretically essential, nor is it sufficiently realistic. This significnatly limits the relevance and significance of the results obtained

### Questions
See the weakness section

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

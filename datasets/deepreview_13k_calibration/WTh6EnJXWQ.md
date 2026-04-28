# DeepROCK: Error-controlled interaction detection in deep neural networks

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 6

## Abstract
The complexity of deep neural networks (DNNs) makes them powerful but also makes them challenging to interpret, hindering their applicability in error-intolerant domains.
Existing methods attempt to reason about the internal mechanism of DNNs by identifying feature interactions that influence prediction outcomes.
However, such methods typically lack a systematic strategy to prioritize interactions while controlling confidence levels, making them difficult to apply in practice for scientific discovery and hypothesis validation.
In this paper, we introduce a method, called \methodname, to address this limitation by using knockoffs, which are dummy variables that are designed to mimic the dependence structure of a given set of features while being conditionally independent of the response.
Together with a novel DNN architecture involving a pairwise-coupling layer, \methodname\ jointly controls the false discovery rate (FDR) and maximizes statistical power.
In addition, we identify a challenge in correctly controlling FDR using off-the-shelf feature interaction importance measures.
\methodname\ overcomes this challenge by proposing a calibration procedure applied to existing interaction importance measures to make the FDR under control at a target level.
Finally, we validate the effectiveness of \methodname\ through extensive experiments on simulated and real datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
[Note on review timing: unfortunately I was only assigned this paper yesterday, after the reviewer-author discussion period closed. However I have made sure to read the authors' responses to the other reviews.]
The paper introduces DeepROCK, a method for detecting 'feature interactions' when interpreting a neural network. The knockoffs framework and a novel architecture is used to control the false discovery ratio (FDR). Empirical results show that the method is able to identify pairwise interactions in toy and real-world datasets.

### Strengths
+ Interesting integration of knockoffs for FDR control in DNNs.
+ Addresses a critical need for interpretable and reliable DNN predictions.
+ Provides empirical evidence demonstrating the potential of the approach.

### Weaknesses
 + The generality of the method across different DNN architectures in not developed. In fact, the method only seems to work with MLPs.
+ The method seems somewhat heuristic. As pointed out by reviewer 1, the sentence 'Intuitively, the interaction between two marginally important features naturally has a higher importance score than random interactions' is used to motivate the calibration in section 3.2, but is not very well formalized. Furthermore, the calibration process itself, which involves comparing interaction scores to those of knockoff features, lacks a clear theoretical justification for why this specific comparison leads to a valid FDR control. The choice of using the maximum interaction score from knockoff features as a threshold, rather than, say, the mean or a quantile, is not well-motivated.
+ The method seems very specialized to pairwise interactions, and it's not obvious if the method would scale to $n$-wise interactions without a significant cost in computational complexity. Moreover, even for pairwise interactions, the method does not address the issue of transitive interactions. For example, if feature A interacts with B, and B interacts with C, the method might incorrectly identify an interaction between A and C, even if no direct interaction exists. This could lead to spurious findings, especially in complex datasets.
+ As I understand it, there are no statistical guarantees due to the use of function approximation in the KnockoffGAN and MLP.

### Questions
See weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper uses knockoffs to control false discovery rate better in discovering interactions. Given existing ways to measure how much a model depends on the interaction between two feature, the key steps are to produce a calibrated score and feature-interaction rank threshold to improve FDR control of interactions while not losing power. The paper has useful experiments.

### Strengths
1. The problem of detecting interactions is important for science.
2. The paper's experiments show clear advantage over existing methods in terms of power and FDR.
3. The need for calibrated interaction scores is surprising.

### Weaknesses
As the main goal is variable selection and the stated goal is FDR control, it seems necessary that there should be a proof of FDR control. To start here, one example of a definition of an important feature is $Y \perp X_j \mid X_{-j}$. Is there a version of this  in terms of interaction ? Possibly, the following $$Y \perp (X_j, X_i) \mid X_{-ji}, (E[Y \mid X_j], E[Y\mid X_i]) $$

Without connecting such a definition to the how you are using the knockoffs framework, I cannot trust a claim about FDR control.  I see a few things that could help, if the knockoff swap property holds, then real-real interactions and knockoff-real interactions also should satisfy the swap property. I think this should be shown but it seems believable.

But then it should be made clear that the flip property is satisfied for the interaction measures in some sense. Otherwise, the knockoff based selection would not provide FDR control. 

Happy to discuss further and increase score.

### Questions
See earlier sections.

Beyond those, 

1. It has been suggested that integrated gradients do not have fidelity when it comes to explaining models. Then, what kind of conclusions can I make from scores based on them ?

2.  The model-dependent score seems to be archictecture specific. Are there concerns about multiplying weight matrices across layers in, for example, deep residual networks?

3. Is there something formal to understand this better "Intuitively, the interaction between two marginally important features naturally has a higher importance score than random interactions, even though they are all false"?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
- The authors measure the false discovery rate (FDR) of existing interaction detection methods in DNNs to quantify their error rate. 
- They use knockoff features to overcome the lack of p-values.
- The main contribution is the combination of knockoff framework and interaction detection algorithms. Specifically, they introduce DeepROCK, which entails a novel architecture including a pairwise-coupling layer and a calibration procedure, allowing to control the error rate. 
- The authors run experiments in simulated and real-world scenarios to demonstrate the effectiveness of DeepROCK.

### Strengths
- The authors address a very relevant topic, namely the detection of feature interaction in DNNs, along with a procedure to control the error rate.
- They propose an interesting idea to approach the problem, which is the connection of knockoff framework and interaction detection algorithms to control FDR. Ultimately, this makes interaction detection algorithms useful in high-stake applications.
- Sound presentation of their approach and required mathematical background knowledge.
- Meaningful experiments both with simulated data and two real-world datasets.

### Weaknesses
 - For the real-world experiments in Fig. 3 and 4, there is no comparison with existing methods. It would be interesting to study found interactions without calibration/coupling layer. Specifically, it's unclear how the performance of DeepROCK compares to simply using the interaction scores derived from the network without the knockoff framework or the proposed calibration and coupling layers. This is crucial for understanding the true contribution of the proposed method. A more detailed ablation study would be beneficial to isolate the impact of each component.
- (nitpick) typos in section 2.2: “withcovariance”

### Questions
- Will the code be published for reproducibility?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

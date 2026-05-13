# Binary Spiking Neural Networks as causal models

- Decision: Reject
- Scores: 6, 6, 6, 6

## Abstract
In this paper, we provide a causal analysis of  binary spiking neural networks (BSNNs)
aimed at explaining their behaviors. 
We formally define a BSNN 
and   represent its  spiking activity
  as a binary causal model.
Thanks to this causal  representation, 
we are able to explain the output of the network
by leveraging  logic-based  methods. 
In particular,
we show that we  can successfully 
use a SAT  (Boolean satisfiability) solver to  compute 
  abductive explanations from this  binary causal model. 
To illustrate our approach, 
we trained the BSNN on the standard MNIST
dataset and applied our SAT-based  method  to
finding  abductive  explanations of  the network's classifications
based on pixel-level features. We also compared the found explanations against SHAP,  a popular 
method used in the area of explainable
AI to explain ``black box'' classifiers.
We show that, unlike SHAP,
our method guarantees that a found  explanation  does
not contain completely irrelevant features.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a novel approach to explaining Binary Spiking Neural Networks (BSNNs) by mapping their spiking activity into binary causal models (BCMs). The authors develop a SAT-based method for generating abductive explanations, ensuring only causally relevant input features are included, which advances interpretability and minimizes redundancy. This approach is unique in leveraging Boolean logic to capture the temporal dynamics of BSNNs, setting it apart from standard explainability methods like SHAP. Experimental results show that this method produces accurate and computationally efficient explanations, highlighting features that directly impact the model's decisions. Overall, the work provides a structured, logic-driven framework for enhancing transparency in spiking neural networks.

### Strengths
Since I am not really into causal models but in spiking NNs, it is hard for me to judge about the originality of the contribution. To me, the paper seems to be original, applying binary causal models to BSNNs in a way that uniquely captures their temporal dynamics through Boolean logic, setting it apart from existing explainability methods, especially in comparison to SHAP. The approach is communicated clearly, with definitions and examples that effectively illustrate the novelty of causal explanations in BSNNs. Overall, the paper provides a robust, innovative framework that could influence future standards in model transparency and causal explainability, if the authors can show that the framework can be generalized to larger real-world networks and problems. (I did not check the proof in the Appendix).

### Weaknesses
My main concern over this paper is the current presentation as a two-layer-only network (one hidden layer). It is hard to imagine all consequences when this approach is generalized to multiple hidden layers. My impression is that the computational effort of Algorithm 1 would increase exponentially, thus effectively excluding the possibility of applying the method to real-world problems. The paper does not sufficiently address the scalability of the proposed method with respect to network depth. The analysis is limited to a very shallow network, and it is unclear how the SAT-based approach would perform with deeper architectures, which are common in practical applications. The current evaluation is also limited to a very specific task (discriminating between digits 1, 5, and 9) and it is not clear if the method would generalize to more complex datasets and tasks.

### Questions
I would appreciate to see more than one single sample (the digit 5) analysed. I have a hard time to judge intuitively the quality of those explanations, without further insights into the trained network, as this is just trained to discriminate the 5 against 1s and 9s. Are the yellow (negative) features part of the explanation of not? If yes, how comes, that so many off-center pixels appear in Figure 1 b) at time step 6.

What would be the effort of constructing the same experiment with two hidden layers?

Maybe the authors could briefly discuss the consequences for the algorithm (and the results) if the BSNN has multiple hidden layers.

### Soundness
4

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
2

### Summary
This paper proposes a causal-based interpretability method by mapping Binary Spiking Neural Networks (BSNNs) into binary causal models. Using a SAT solver to compute abductive explanations. This provides a new perspective for interpreting BSNNs and advancing BSNN research further.

### Strengths
As the authors stated, this is the first time BSNNs have been interpreted as causal models. I believe this provides a new perspective for understanding BSNNs.

### Weaknesses
1. This paper primarily relies on extensive formal language for its exposition. Adding some figures would be beneficial to enhance readers' understanding of the content.
2. The experiments are limited to the MNIST dataset. It is recommended to include some other, more complex datasets for support.

### Questions
Please see weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper presents a causal analysis of binary spiking neural networks by representing the spiking activity as a binary causal model and applying this model to a SAT (Boolean satisfiability) solver.


---

After reading the reviews and the rebuttal, I tend to accept this paper.

### Strengths
1. The idea of bridging SNN and Causal Inference is interesting.

2. The experiments related to SAT solver seem significant.

### Weaknesses
1. This paper is hard to follow due to the poor presentation. Some symbols are confused.

2. The motivation that employs BSNN rather than BNN is not clear. I cannot get the necessity of using spiking mechanism. Thus, it is better to explicitly compare the advantages of BSNNs over BNNs in the context of causal modeling. Specifically, the paper does not clearly articulate why the integrate-and-fire mechanism is crucial for causal analysis, given that both BSNNs and BNNs can operate with binary inputs, weights, and outputs. The core issue is that the paper does not adequately justify the added complexity of the spiking mechanism in relation to the causal modeling task. It is not apparent how the temporal dynamics of the integrate-and-fire mechanism offer a unique advantage over a simpler binary activation function in a BNN for the purposes of causal inference. The paper needs to provide a more detailed explanation of the specific benefits of using BSNNs over BNNs for causal modeling, beyond the basic fact that both can be binarized.

### Questions
Please show the advantages of BSNNs over BNNs in the context of causal modeling. The core question is why only employ BSNN rather than BNN as the causal model. In my view, one requires quantized input, weights, and outputs, which are satisfied by both BSNN introduced by this paper and BNN. The main difference between SNNs and conventional ANNs is the activation mechanism; however, I cannot find the connection between the integrate-and-fire mechanism and a causal computation, unless I missed something. Thus, it is better to explicitly compare the advantages of BSNNs over BNNs in the context of causal modeling. In detail, the authors are asked to answer the following questions.

1. Explicitly compare the causal properties of BSNNs and BNNs.

2. Clarify how the integrate-and-fire mechanism specifically contributes to or enhances the causal model.

3. Explain any potential advantages of the temporal dynamics in BSNNs for causal reasoning that may not be present in BNNs.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors introduced a method mapping binary (or ternary) spiking neural networks to binary causal models, which can then be used to perform abductive explanations (via a SAT solver) for the network's behavior. They applied this method to the MNIST classification task (3 classes for the binary case and 10 classes for the ternary case). The authors claim that their method provides a better explanation compared to SHAP, another explainability method.

### Strengths
- The idea of using binary causal models to explain binary spiking neural networks is novel
- The technical aspects of the paper are precise and rigorous; the authors provide precise mathematical definitions and prove the proposition brought forth in the paper
- The paper is written in an easy-to-follow manner

### Weaknesses
 - It is not clear to me how the explanation provided by the binary causal model is a "good" explanation. While the authors make the implication that their method provides a better explanation than SHAP as SHAP can select features that are irrelevant, I think the paper would be improved if it included some evaluation metrics for explainability and, if possible, other bechmark methods alongside SHAP.
- The proposed method seems to take a long time in searching for an explanation using the SAT solver, ranging from 5-11 hours, and this is  just for MNIST limited to 3 classes. It seems unlikely that this method is scalable to larger scale problems.
- The authors do not report the results (both accuracy and computational analysis) for the BCNN (binary, not ternary) on the 10-digit MNIST dataset.

### Questions
- Related to weakness #1, it is not clear to me how a causal explanation at the pixel level would be useful for MNIST. I understand that this might just be for demonstration purposes. However, wouldn't a task of a more symbolic nature (e.g. language-related tasks) make more sense (I am aware that the authors have considered this in the conclusion)?
- Is the analysis possible on regular non-spiking binary neural networks? If so, why not do it for that instead? While it is mentioned that spiking neural networks are more general, regular neural networks are more widely used, and it in the use cases considered by the authors, it seems to make more sense to use regular neural networks as opposed to their spiking variants.
- What are the results (both accuracy and computational analysis) for the BCNN (binary, not ternary) on the 10-digit MNIST dataset?

### Soundness
2

### Presentation
3

### Contribution
3

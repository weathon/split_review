# Neural Networks Trained by Weight Permutation are Universal Approximators

- Decision: Reject
- Scores: 8, 5, 6, 5

## Abstract
The universal approximation property is fundamental to the success of neural networks, and has traditionally been achieved by training networks without any constraints on their parameters. However, recent experimental research proposed a novel permutation-based training method, which exhibited a desired classification performance without modifying the exact weight values. In this paper, we provide a theoretical guarantee of this permutation training method by proving its ability to guide a ReLU network to approximate one-dimensional continuous functions. Our numerical results further validate this method's efficiency in regression tasks with various initializations. The notable observations during weight permutation suggest that permutation training can provide an innovative tool for describing network learning behavior.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates the universal approximation property (UAP) of neural networks, specifically focusing on permutation-based training methods. The authors demonstrate that, without altering the exact values of neural network weights and only by permuting them, one can achieve effective approximation results, particularly for one-dimensional continuous functions. The research offers both theoretical proofs and empirical results, highlighting the potential of permutation training in shedding light on detailed network learning behaviors and its implications in various application scenarios.

### Strengths
*  The paper delves into the universal approximation property of permutation-trained networks, discussing the impact of various initialization strategies. A significant strength of the paper is the theoretical proof that a permutation-trained ReLU network can approximate one-dimensional continuous functions. The paper does not just rely on theoretical claims; it also presents numerical results which validate the performance of the permutation training method on regression tasks.
* The paper suggests that permutation training can serve as a novel tool for understanding network learning behavior. This could provide a fresh perspective on how neural networks learn and adapt.
* The observations made during permutation training are tied to other practical and important topics such as neural network pruning and continual learning.

### Weaknesses
* The exploration of practical aspects of permutation-based training, in particularly its potential applications to weight consolidation for continual learning and pruning, seem highly interesting and promising. Further elaboration on how this method supports such applications, potentially complemented by dedicated empirical evaluations, would greatly enhance the value of the proposed theory and the related version of the training method. 
* Sparse training is of particular interest for its potential computational efficiency in resource-constrained environmental. An exploration of how the permutation-based method performs under sparse training conditions, such as with a random subset of weights initialized to zero, would provide valuable insights.
* The manuscript offers a valuable theoretical analysis with ReLU activation functions. It would be beneficial to investigate the extent to which these theoretical findings can be generalized to other activation functions, like leaky ReLU (or non-differentiable activation functions).
* The appendix, particularly Appendix A, contains details that may be of significant interest to readers, especially regarding hardware implementation benefits. Incorporating a summary of these details into the main text could reinforce the practical significance of the findings.

### Questions
* How is the permutation period k chosen in the relaxed version of the permutation-base training method? Table 2 lists the values used in the experiments but does not provide an intuition how the parameters were chosen.
* Fig. 1.c-d) are not sufficiently explained in the text. Could the authors offer a more detailed examination of the training dynamics illustrated in Figure 4? The current explanation offers a broad overview; however, the intricacies, such as why the permutations appear thread-like, remain unclear. A deeper analysis would be beneficial in understanding these nuances.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Universal approximation is a desirable property of neural networks. In this paper, permuting weights of a ReLU network is shown to have the universal approximation property, i.e. given a sufficiently wide network one can fit an arbitrary continuous function as closely as desired, only by permuting that network's weights. The proof involves constructing approximations of step functions out of four pairs of weights. Both random and fixed initializations for the network weights are considered.

### Strengths
The work pushes forward UAP proof techniques to a novel situation (training with permutation only), and solves this difficult and constrained case. The proof involves some tricky constructions which could inspire other manipulations of ReLU networks. Some intriguing connections are discussed about random initialization for permutation training techniques, and dynamics during permutation training.

### Weaknesses
The lack of multidimensional inputs is a pretty big limitation since many non-trivial networks operate on multidimensional inputs. However, the conclusion does point this limitation out, and it is reasonable to expect it as a follow up work.

The pairwise constraint really limits how the proof can be applied to random initialization cases. Random weights usually suggest we cannot control what the weights can be, but if we can make pairs of weights identical, why not just use the fixed initialization scheme instead? In general the proposed proof method seems to be too specific to adapt to other situations - in the case of truly random weights, error in the constant regions of the stepwise approximators could accumulate globally (see questions for a different suggestion). It would be interesting to understand why permutation training fails on some random initialization schemes and not others, however, as that could point to some theoretical or empirical justification for the pairwise constraint.

### Questions
Is it possible to relax the pairwise constraint in a bounded input interval (e.g. [0, 1]) by having error cancel out in the same way that the unusued parameters annihilate?

Instead of annihilating the unused parameters, could we simply divide the stepwise approximation of $f^*$ into more steps to use up the remaining parameters?

Could the authors elaborate on what they observe in figure 4? Specifically, how it relates to rank structures in permutation groups (e.g. larger/smaller cycles take longer/shorter to train), and how it relates to weight consolidation/pruning/weight projection. The connections aren't obvious to the reader.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors study the UAP (universal approximation problem) of deep neural networks. They derive that some permutation-trained networks could achieve UAP. First, they show that it is true if the parameters are selected as $\frac{i}{n-1} (0\leq i \leq n-1)$. Secondly, they generalized their results to the scenario with random initialization.

### Strengths
Originality: The related works are adequately cited. This paper derives that some permutation-trained networks with parameters selected from $\frac{i}{n-1} (0\leq i \leq n-1)$ could achieve UAP. Furthermore, the authors generalized their results to the DNNs with random initialization. The main results in this paper will certainly help us have a better understanding of the universal approximation property of deep neural networks from a theoretical way. I have checked the technique parts and found that the proofs are solid.

Quality: This paper is technically sound.

Clarity: This paper is clearly written. I find it is easy to follow.

Significance: I think the results in this paper are significant, as explained above.

### Weaknesses
For the weights $\frac{i}{n-1} (0\leq i \leq n-1)$, the UAP is always true. For random initialization, the UAP is true with some high probability. It would be interesting to find out for which set of parameters, the UAP is always true. More explanations about this should be addressed.

### Questions
More explanations about when UAP is always true should be addressed (for which sets of parameters?). It would also be interesting to derive the results for more activation functions and more architectures used in practice.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper demonstrates that the permutation training technique can effectively steer a ReLU network to approximate one-dimensional continuous functions, effectively realizing the universal approximation property in the context of the permutation training method. Then they empirically confirm their theoretical results.

### Strengths
Clarity
- The paper is written effectively and ensures high accessibility.
- Theorem and proofs sketch are simple and easy to follow.

Originality
- This paper theoretically and empirically shows the universal approximation property of the permutation training method for the 1d regression case.

### Weaknesses
Main Results
- While this paper theoretically showcases the effectiveness of the permutation training method in the context of one-dimensional regression, the simplicity of this result may not fully validate the method's performance for larger and more complex deep learning models.

Experiments
- They conducted too simple experiments.

### Questions
Experiments
- It would be beneficial if the paper included empirical experiments demonstrating the performance of the permutation training method on high-dimensional regression or classification tasks, even without the inclusion of precise theoretical results.
- Their newly introduced relaxed LaPerm algorithm doesn't appear to offer any significant advantages over the original LaPerm. Hence, I believe the authors should present the results of other proposed algorithms, such as those employing a self-adjusted strategy.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

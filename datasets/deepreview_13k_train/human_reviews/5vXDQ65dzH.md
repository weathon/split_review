# ParFam - Symbolic Regression Based on Continuous Global Optimization

- Decision: Reject
- Scores: 5, 5, 6, 5

## Abstract
The problem of symbolic regression (SR) arises in many different applications, such as identifying physical laws or deriving mathematical equations describing the behavior of financial markets from given data. Various methods exist to address the problem of SR, often based on genetic programming. However, these methods are usually quite complicated and require a lot of hyperparameter tuning and computational resources. 
In this paper, we present our new method ParFam that utilizes parametric families of suitable symbolic functions to translate the discrete symbolic regression problem into a continuous one, resulting in a more straightforward setup compared to current state-of-the-art methods. 
In combination with a powerful global optimizer, this approach results in an effective method to tackle the problem of SR. 
Furthermore, it can be easily extended to more advanced algorithms, e.g., by adding a deep neural network to find good-fitting parametric families. 
We prove the performance of ParFam with extensive numerical experiments based on the common SR benchmark suit SRBench, showing that we achieve state-of-the-art results. Our code can be found at https://anonymous.4open.science/r/parfam-90FC/README.md.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a method for symbolic regression in which the purpose is to search for a mathematical formula describing given data. The proposed method, termed ParFam, defines a structure of the target equations in advance and then optimizes the coefficients using gradient-based methods. Owing to this problem transformation, the symbolic regression problem becomes a contiguous problem from a discrete one. In addition, the technique that combines ParFam and the neural network-based structure prediction of the sparsity of coefficients is introduced. The authors experimentally evaluate the performance of ParFam using SRBench and show that it can achieve state-of-the-art performance compared to other symbolic regression methods.

### Strengths
- A novel method for symbolic regression is presented, which translates the original discrete combinatorial optimization problem into the continuous optimization problem with a pre-defined structure of equations.
- The proposed ParFam achieves state-of-the-art performance on SRBench.
- This paper is well-written and easy to follow.

### Weaknesses
 - When the number of the input variables of the equation increases, it seems hard for ParFam to handle the exponential growth of the number of parameters, as the authors describe in Section 4. This limitation is significant, as many real-world symbolic regression problems involve numerous input variables, making the method potentially impractical for such cases. The authors should provide a more detailed analysis of how the number of parameters scales with increasing input dimensions and explore potential mitigation strategies, such as parameter sharing or dimensionality reduction techniques before the polynomial expansion.
- As the authors stated in the introduction, symbolic regression aims to find a symbolic model with as few assumptions as possible. However, in ParFam, the form (structure) of the target equations is pre-defined by users. If the structure of the equation is not suitable for a given data, it cannot represent an appropriate equation. This reliance on a pre-defined structure limits the method's ability to discover novel or unexpected relationships in the data, which is a key goal of symbolic regression. The method's performance is thus heavily dependent on the user's prior knowledge and ability to specify an appropriate equation structure. A more adaptive approach that can automatically adjust the structure based on the data would be more desirable.
- The experimental evaluation of DL-ParFam is limited to the synthetic datasets. This raises concerns about the generalizability of the method to real-world datasets, which often have different characteristics than synthetic data. The authors need to demonstrate the performance of DL-ParFam on a wider range of datasets, including those from SRBench, to establish its practical applicability. The current evaluation does not provide sufficient evidence to support the claim that DL-ParFam is a viable approach for real-world symbolic regression problems.

### Questions
- The concept of the proposed ParFam is somewhat similar to equation learner (EQL). Given an appropriate network architecture that corresponds to the equation structure of ParFam, the search space of EQL could be almost the same as ParFam. Could you describe the main difference and advantage of ParFam against EQL? Also, is there any experimental comparison of EQL and ParFam?
- Why is it difficult to apply and evaluate the DL-ParFam to SRBench?
- How is the sensitivity of the performance of ParFam for the regularization hyperparameter $\lambda$?
- Could you report the exact number of parameters to be optimized in ParFam?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes ParFam, a simple regression method with a fixed and predefined structure, to tackle the symbolic regression problem. In ParFam, the function expression structure is directly specified by the user in advance, and then the coefficients are learned with a sparsity regularization from the observed data. In this way, the original symbolic regression problem can be reduced to a continuous optimization problem with respect to the coefficients.

Based on the ground-truth problems from SRBench and the knowledge from the Cambridge Handbook of Physics Formulation, this work proposes a reasonable parametric expression structure to represent the physical formulas. Then, it uses a global continuous optimization method (basin-hopping algorithm) to find the optimal coefficients of the predefined expression. Experimental results show that ParFam can achieve promising performance on the symbolic regression problem for physics formulas.

### Strengths
Symbolic regression (SR) is an important but difficult problem that can be found in various domains. The proposed ParFam method can achieve promising performance on SR for physics formulas in a straightforward way.

### Weaknesses
Although I enjoy reading this paper and appreciate the explicit discussion on the limitations, I have some major concerns about ParFam.

**1. Is It still Symbolic Regression?**

To my understanding, symbolic regression is a learning-based approach to find the mathematical expression of a function from the observed data, which includes two important components:

- Learn the analytical function structure;

- Optimize the coefficients (parameters) of the structure;

The former is unique for symbolic regression, which distinguishes it from the other regression problems. Symbolic regression is difficult and is currently shown to be HP-hard with formal proof [1]. I think this is the reason why an efficient (approximate) SR algorithm will be "usually quite complicated" as described in this work.   

In ParFam, however, the analytical structure learning step is totally bypassed with a predefined function structure. The original problem is hence reduced to sparse regression with a fixed structure, and the only goal is to find the optimal coefficients. Is it still symbolic regression?  

**2. Strong Prior Knowledge on Physics are Required**

To achieve promising performance on SR problems for physics formulas, ParFam requires prior knowledge of all possible physics formulas, as from SRBench and the Cambridge Handbook of Physics Formulation. I think this prior knowledge is very strong and only specific to physics formulas, and is hard to be generalized for other SR problems in real-world applications.  

**3. DL-ParFam**

The idea of DL-ParFam, a deep learning-based pretrain model for ParFam, is interesting. But it is currently more like a toy prototype, and only tested on very simple synthetic problems. To truly show the advantage of DL-ParFam over other pre-training-based SR methods, a concrete model design on real-world SR applications is required. 

In DL-ParFam, the model only takes the function value y as input to predict the mask c for all parameters, and all information of the function input x is completely ignored. It is hard to believe this approach can provide a reasonably good prediction for real-world SR applications, especially those with complicated structures. 

To build the pre-trained model, DL-ParFam requires the input data x to have the same dimension $m$, and the data should be sampled on the same grid across all different data sets. Can this requirement be easily satisfied for physical SR problems and other SR problems?

**4. Experiments**

Since ParFam has a strong prior knowledge of the physical formulas, it is expected it can have promising performance on the physics SR problems. Indeed, according to the results, ParFam even discards part of the observed data, and only requires a subset of 500-1000 data points for coefficient optimization. It is hard to imagine this procedure could work well for real-world SR problems.

DL-ParFam is only tested on very simple synthetic problems. It is hard to judge its potential for solving real-world application problems with complicated structures.

### Questions
Please see the weaknesses section. I am willing to adjust my rating if the issues in weaknesses are well addressed.

[1] Symbolic Regression is NP-hard. TMLR 2022.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper considers the task of symbolic regression that learns to discover the underlying expression from data. The authors make an important observation that the current expression is just a small fraction of the whole possible expression, so searching in this small family would be much easier than searching in the whole space. The author justifies the success of the proposed on several datasets and many baselines.

### Strengths
- The idea is clearly written and the observation for the current symbolic regression dataset is interesting.
- The experiment result is strong against a lot of baselines.

### Weaknesses
 - Figure 1 as well as the description of Equations 3 and 4 are very hard to understand. It is unclear how the observation in Equation 1 is actually implemented into an algorithm.
- A deep understanding of the proposed family of symbolic expressions is needed. Since the observation is so strong, it eliminates a lot of "impossible" expressions and reduces the search space greatly. I hope the author could give some analysis on how much the reduction of the search space from all the possible expressions (of maximum length < 30) to the family of expressions described in Equation 1.
- One important baseline is missing: Symbolic physics learner: Discovering governing equations via Monte Carlo tree search.
- The basin-hopping algorithm is used to solve non-convex optimization problems. Is the structure of the symbolic family required to solve non-convex optimization instead of convex optimization? This is not justified. Also `scipy.optimize` has already offered the API for BFGS, basin-hopping, SHGO, Direct, dual annealing, and Differential evolution. The whole process of using these fancy optimizers is just changing these APIs in one line.

### Questions
1. A detailed description of the pipeline in Figure 1 is needed.
2. Theoretically analysis of the observation of Equation 1 on the reduction of space of symbolic regression is needed.

### Soundness
2 fair

### Presentation
2 fair

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
This paper introduces a simple parametric method for symbolic regression, as well as a deep learning-based extension where the neural network is designed to constrain the set of learnable parameters.

### Strengths
- Results on SRbench black-box problems: the Parfam method seems competitive
- Clarity: the paper is well written and easy to follow

### Weaknesses
 - Lack of novelty: the parametric approach is not particularly novel (it is used in existing methods such as EQLearner and FFX). The main trick enabling the competitive performance seems to rely a lot on manual crafting of the heuristics (Appendix A) and the extensive model parameter search (Appendix E). As for DL-parfam, it is not sufficiently validated, as detailed below.
- Experimental validation: as acknowledged by the authors, the DL-parfam method is mainly in prototype stage right now. Are results of DL-parfam on Feynman problems not reported because they were not as good as the ones on synthetic data or because the authors did not have the time to test? In the first case, the authors should at least explain why the results aren’t good (what is missing in the current state). In the second, it gives the paper an unfinished impression. In both cases, this section appears as a dealbreaker for a prestigious venue — results should be complete, otherwise the paper appears rushed.

### Questions
"Even though modern approaches are able to handle flexible data sets in high dimensions (Biggio et al., 2021; Kamienny et al., 2022), they fail to incorporate invariances in the function space, e.g., x + y and y + x are seen as different functions, as pointed out by Holt et al. (2023)"

I tend to disagree with the idea that this is the main limitation of modern approaches. In fact, modern methods easily learns these invariances, which can be seen by the fact that beam search typically reveals equivalent expressions.

### Soundness
1 poor

### Presentation
3 good

### Contribution
2 fair

# Generalized Policy Iteration using Tensor Approximation for Hybrid Control

- Decision: Accept
- Avg Score: 7.50
- Scores: 6, 8, 8, 8

## Abstract
Control of dynamic systems involving hybrid actions is a challenging task in robotics.  To address this, we present a novel algorithm called Generalized Policy Iteration using Tensor Train (TTPI) that belongs to the class of Approximate Dynamic Programming (ADP). We use a low-rank tensor approximation technique called Tensor Train (TT) to approximate the state-value and advantage function which enables us to efficiently handle hybrid systems. We demonstrate the superiority of our approach over previous baselines for some benchmark problems with hybrid action spaces. Additionally, the robustness and generalization of the policy for hybrid systems are showcased through a real-world robotics experiment involving a non-prehensile manipulation task which is considered to be a highly challenging control problem.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper develops a method to solve approximate dynamic programming with Tensor Train (TT) representation, which is a compressed tensor to discretely approximate a function. The authors first give a compact and quite neat backgrounds for TT representation and associated operations with TT. The main contribution is a policy iteration algorithm, where the authors replace traditional continuous function approximators (such as using neural network) with TT representations. The authors show the performance of the algorithm using a toy examples in comparison with baseline methods. The method has also been demonstrated in real world robot for a manipulation task.

### Strengths
The authors did a good job presenting the necessary background of TT and its associated operations (such as decomposition, rounding, TT-Cross, and TT-go).  I think the authors have fairly discussed the limitation of the method.

### Weaknesses
1. My main concern of the paper is the experiment, which is quite limited and there are many remaining questions. Particularly, there are many hyperparameters, it is expected to have ablation study of showing the performance of the method versus the hyperparameters, such as accuracy $\epsilon $ of TT representation, the max TT rank $r_{max}$, discretization resolutions of the state-action spaces.... 

2. As a reader to implement the algorithm, I wanted to see a straightforward illustration between the running time of the algorithm and dimensions of the state/action spaces of the system, or directly give an overall complexity of the algorithm for one policy iteration.

3. Since the majority of the paper is about the background of TT (previous work), I think the main contribution, which is TTPI algorithm, needs more explanation, including its parallel implementation, which seems a key for applicability of the algorithm. For example, why we need a TT-round operation for the value function in line 8?

### Questions
Since in the introduction the authors mentioned RL, I think it would be interesting to discuss the potential of the methods into "model-free" settings.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper tackles the problem of controlling dynamic systems that involve both continuous and discrete actions (termed "hybrid actions") is challenging in robotics.  The innovative aspect of the authors' solution is the use of the Tensor Train (TT) format, a method to approximate functions with a low-rank tensor. The TT format allows the authors to approximate two crucial components:
State-value function: Represents the value of being in a particular state.
Advantage function: Indicates how much better taking a certain action is compared to others.

### Strengths
The paper introduces TTPI, an Approximate Dynamic Programming (ADP) algorithm designed for optimal control. The method leverages Tensor Train (TT) format to address challenges in hybrid system control in robotics.
Traditional control algorithms face problems with systems with non-smooth dynamics and discontinuous reward functions. Existing solutions also often assume differentiability in the system dynamics, which may not always hold.

The paper introduces TTPI, an Approximate Dynamic Programming (ADP) algorithm designed for optimal control. The method leverages the Tensor Train (TT) format to address challenges in hybrid system control in robotics. The experiments show TTPI outperforming other state-of-the-art algorithms in training speed and control performance. A real-world robotics experiment further demonstrates the effectiveness and robustness of this method.

### Weaknesses
As the authors themselves mentioned, hand-coding the dynamics in the experiments is very hard to do for complex environments.

TTPI approximates state-value and advantage functions over the entire state-action space, which can result in computational and storage challenges, especially if these functions are not low-rank in the TT representation. This is especially concerning for high-dimensional systems where the curse of dimensionality can make the TT representation itself computationally expensive, even if it is low-rank. The paper does not provide a clear analysis of the scaling of computational cost with increasing state and action space dimensionality, which is a critical consideration for practical applications.

### Questions
Tensor operations, especially in high-dimensional spaces, can sometimes introduce numerical instability. How does the TTPI algorithm ensure numerical stability, especially in long-horizon problems?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors use the Tensor Train (TT) model to approximate the state-value function $V$ and advantage function $A$ during policy iteration while solving optimal control problem. At each step of the policy iteration this functions is being rebuilt using well-known _TT-cross_ algorithm which adaptively queries a certain number of points to the black-box model function to be approximated. In addition, policy $\pi$ is built on these iterations using the known TTGO algorithm, which searches for the maximum of the TT-tensor based on sampling from it. The performance of the algorithm was tested on several model and real robot examples, showing its superiority on them. The distinctive feature of the algorithm is the use of hybrid actions.

### Strengths
- The paper is very well structured, the authors have described not only the method and practical application, but also the limitations.

- There is code, which allows for reproducible experimentation. In the supplementary materials there is a video with demonstrations of both synthetic experiments and real experiments with a mechanical arm.

- Numerical and in-situ experiments show the superiority of this method.


- Potentially, this approach is applicable to rather multi-dimensional problems (with large dimensionality of stats or actions) since the TT construction overcomes the curse of dimensionality, and the authors use TT-format compression for all possible functions.

- The approach presented in the paper allows for serious expansion in both quality and time. The authors have identified some of these potential opportunities in the paper.

### Weaknesses
I found no significant weaknesses in this article.
As a small remark, the use of a uniform grid in section 2.6 could be pointed out, while it might be more accurate to use, for example, a Chebyshev grid.
Also there are no theoretical estimates (ranks, for example) and no discussion when we expect small TT-ranks. I.e., can we say in advance, without iterating, that the method works. However, this is a general problem of methods using a low-parameter tensor representation.

The paper cited as arXiv (Sozykin et al., 2022) is now officially published: https://proceedings.neurips.cc/paper_files/paper/2022/hash/a730abbcd6cf4a371ca9545db5922442-Abstract-Conference.html

maybe typo: p4 "decomposition equation 5"

### Questions
- did you use ideas from _opitma_tt_ (paper Chertkov et al. (2022)) which utilize _top-k_ scheme and thus more accurate?
- what are the typical TT-ranks for double pendulum swing-up in the case of small $\Delta t$ when the model does work?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a method for solving optimal control problems (assuming a correct dynamics model is available) with mixed continuous and discrete state variables, using an efficient representation of the value function of the problem based on a set of low-dimensional tensors, in a tensor-train (TT) format. An empirical evaluation demonstrates the effectiveness of the proposed method on several control problems of moderate complexity.

### Strengths
One of the main strength of the paper lies in the efficient way of computing the optimal action from the tensor-based representation of the value function. It is based on an explicit representation of the advantage function, again in tensor-train format, and the use of the TT-Cross algorithm for an efficient TT approximation of the advantage function after it has been computed by means of a Bellman back-up.

Another strength of the paper is the rather impressive verification of the algorithm on control problem with six continuous state variables and a single discrete variable, on a real robot.

### Weaknesses
Although the example on the real robot is very impressive, the examples in simulation are less so. Four-dimensional state space is not that high, barely beyond what can be represented with a look-up table on modern computers. (10^8 cells will take around 400MB of FP numbers.) The authors clearly state that their algorithm is not meant to approximate value functions on very high-dimensional state spaces, such as images, but most robotics applications on 6 degree of freedom robots have 12-dimensional state space, so this is perhaps the dimensionality of highest interest. The paper would benefit from a more thorough analysis of the computational cost and scalability of the proposed method with respect to the dimensionality of the state and action spaces, going beyond the presented 4D examples. The current benchmarks do not fully demonstrate the advantages of the tensor-train representation over simpler methods for moderate state spaces.

Some claims are not entirely justified. For example, the authors say "OC is synonymous with ADP". There is some overlap, but the two fields are hardly the same. Many OC algorithms, including the celebrated LQR and LQG algorithms, are based on basic DP, nothing approximate about it. The statement oversimplifies the relationship between optimal control and approximate dynamic programming, and it should be revised to reflect the nuances of both fields. Furthermore, the authors say that MuJoCo is not parallelizable. I cannot agree with this, MuJoCo has always been easy to parallelize on multiple CPU cores, and the latest release of MuJoCo, 3.0.0, can run on GPUs and TPUs. True, it came out after ICLR papers were submitted, but please reconsider this claim. The claim about MuJoCo's parallelization capabilities is inaccurate and should be removed or updated to reflect the current state of the software.

The authors also mention "the need for differentiability of the system dynamics and reward function which is a common assumption in the existing ADP algorithms". This is probably not entirely correct, as many ADP algorithms simply sample the system dynamics. The statement about differentiability is misleading, as many ADP methods are model-free or rely on sampling, not requiring differentiability. Furthermore, the authors often use the phrase "policy retrieval", implying that somehow the policy has been lost. Suggest replacing with "policy computation" or "policy evaluation". The terminology "policy retrieval" is not standard and should be replaced with more appropriate terms. Some minor typos:
Appendix A.3: citation missing in the first sentence
Same place: "n=6 states" -> "n=6 state" (completely changes the meaning)
"HZ" -> "Hz"

### Questions
How well will the algorithm perform on a somewhat higher dimensional problem, for example a 6 or 12 dimensions?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

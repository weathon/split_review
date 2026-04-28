# Scaling Safe Learning-based Control to  Long-Horizon Temporal Tasks

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 5, 6, 3

## Abstract
This paper introduces a model-based approach for training parameterized policies for an autonomous agent operating in a highly nonlinear (albeit deterministic) environment. We desire the trained policy to ensure that the agent satisfies specific task objectives and safety constraints, both expressed in Signal Temporal Logic. We show that this learning problem reduces to the problem of training recurrent neural networks (RNNs), where the number of recurrent units is proportional to the temporal horizon of the agent's task objectives. This poses a challenge: RNNs are susceptible to vanishing and exploding gradients, and naive gradient descent-based strategies to solve long-horizon task objectives thus suffer from the same problems. To tackle this challenge, we introduce a novel gradient approximation algorithm based on the idea of gradient sampling, and a smooth computation graph that provides a neurosymblic encoding of STL formulas. We show that these two methods combined improve the quality of the stochastic gradient, enabling scalable backpropagation over long time horizon trajectories. We demonstrate the efficacy of our approach on various motion planning applications requiring complex spatio-temporal and sequential tasks ranging over thousands of time steps.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose an algorithm for optimizing neural network control policies to satisfy STL specifications on their behavior. They build on prior work in differentiating through a smoothed approximation of the STL robustness signal, adding two core contributions. First, they propose a smooth approximation scheme which guarantees a lower bound on the true robustness while avoiding numerical issues. Second they propose a gradient approximation scheme to manage issues with gradients exploding or vanishing over long temporal horizons, involving evaluating the gradient of the trajectory wrt to policy parameters only at certain timesteps.

### Strengths
- The paper tackles an important challenge of enabling STL-based training over long temporal horizons without running into the challenges such as vanishing gradients.
- The background on STL and STL robustness was thorough and helpful, though this may have come at the expense of having not enough room to clearly explain the core contributions of this work.
- The experimental results on show promising results in effectively satisfying STL formulae for reasonably high-dimensional systems over long temporal horizons.

### Weaknesses
 - The paper was difficult to follow. In particular, section 3.3 detailing the sampling based approximation of the gradient was quite hard to understand. A figure to help illustrate the trajectory subsampling approach would significantly improve the clarity of the paper.
- The impact of STL2LB as compared to other strategies to smooth STL formulae was not clearly demonstrated.
- The experimental comparisons were very limited: quantitative comparisons were only presented against ablations of the proposed approach, and not against many of the other cited works on training NN policies to satisfy STL objectives. In addition, there was no comparison against an approach which used the critical predicate-based time sampling, but without the waypoint functions. Thus it was not clear what improvement the critical predicate-based sampling strategy had over random time sampling.
- The paper would be strengthened with theoretical results detailing what factors impact the quality of the sampling-based gradient approximation.

### Questions
- Do you have empirical results investigating how well the sampling-based gradient strategy approximates the true gradient?
- The solution to the computational problems with the swish and softplus functions seems to break differentiability, especially in the case of the swish function. Would this lead to issues during optimization?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the problem of finding a controller satisfying a given Signal Temporal Logic (STL) specification in a given environment. The algorithm proceeds by sampling trajectories from a known environment given a parameterized policy after which a smoothened differentiable temporal logic structure is used to provide feedback. The policy is then updated using this feedback signal until a positive robustness score is reached indicating the specification is satisfied. The paper further introduces a technique to handle long horizon problems by approximating the gradient with fewer samples after identifying the critical predicate. Experimental results compare the effectiveness of these two methods over a range of task horizons and problems.

### Strengths
- Provides a lower bound to STL evaluation using differentiable computation graphs that fit well into neural network architectures.
- Addresses the vanishing gradient problem for long horizon tasks by means of sampling the gradients at given time steps.

### Weaknesses
 - Lack of comparisons made to the state-of-the-art methods [1,2,3] for control using STL. The presented algorithms are shown without reporting results on enough competing methods. This brings into question the relative benefits of the given approach. Specifically, the paper does not compare against methods that also learn control policies using smooth approximations of STL robustness, making it difficult to assess the novelty of the proposed approach. A more thorough evaluation would include comparisons to methods that utilize similar techniques for training controllers with STL specifications.
- The motivation for a smooth lower bound on the STL score is mentioned but not sufficiently justified (viz. empirically). It would be interesting to see how far the STL2NN method would work without the approximations provided by STL2LB in Algorithm 1. Another useful smoothing technique could be as introduced in [3]. The paper would benefit from an ablation study that isolates the impact of the proposed lower bound approximation on the overall performance, in comparison to using the raw STL robustness score or other smoothing techniques directly. This would clarify the specific contribution of the proposed approximation.
- Assumes differentiability of the simulator environment and knowledge of its transition functions to calculate the policy parameter gradients. This may be infeasible in many problems. The paper does not discuss the implications of this assumption, nor does it consider scenarios where the environment dynamics are unknown or non-differentiable. This limits the applicability of the proposed method to a subset of problems where the simulator is fully known and differentiable.

### Questions
1. In which steps in Algorithm 2 is the critical predicate $h^*$ and $k^*$ used? This is not entirely clear to me.
2. Is it possible to include comparisons to other algorithms in the same environment such as [1]? If not, why is that the case?
3. The introduction mentions  an RNN-based implementation, but this is not explained further in the text. Could there be a section in the appendix with more implementation details? Is there a clear benefit versus not using a fully connected network with the observation (and say the current time) as input being the policy?

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents an algorithm of synthesizing neural policies for signal temporal logic specifications. Since RNNs over long
time horizon has problems of exploding and vanishing gradients, two main claimed features are proposed: smooth operators for robustness representation and a sampling-based approach to approximate the gradient.

### Strengths
1. The related work is well-written and the authors are aware of many recent developments.
2. The paper is well-presented and easy to follow.
3. The proposed features and algorithm are effective.
4. The benchmarking environments are standard and convincing in the community.

### Weaknesses
My main concern lies in the experimental comparison. I think the authors are recommended to compare with some other baselines because readers are not sure how good are the learned policies on benchmarks. I would suggest to compare with the standard MPC approach using Mixed Integer Linear Program (MILP) [1] to see if the learned policies are close to the optimal policies returned by MILP or not.

MILP has high computational complexity but still can be practically well-solved using tools like Gurobi --- so the benefits and potential drawbacks of neural net based STL synthesis over MILP should be clarified and also compared in practice.

### Questions
I do not have question.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies control problems in which a neural network policy must satisfy a signal temporal logical formula on a long time horizon. The specific contributions are twofold: (1) a differentiable technique for evaluating the temporal logic formula, and (2) a lower-complexity approach to evaluating gradients which also reduces the chances of exploding gradient issues. Simulation experiments illustrate the relative impact of these two techniques.

### Strengths
- The problem of long-horizon planning is certainly challenging and important, and there is a gap in the literature here with regard to learning to satisfy temporal logic specifications.
- The proposed technique for smoothing the specification is intuitive and easy to follow. (The same cannot be said of the gradient approximation scheme.)
- The proposed approaches appear to handle the tested scenarios well, and tradeoffs are readily apparent and well explained.

### Weaknesses
 - nit: there are quite a few sporadic syntax and grammar issues, e.g. in the first paragraph there are two instances of improper spacing near punctuation marks. Similar issues around references: you may consider using the \citep{} option for parenthetical citations.
- In Section 3, the paper clearly states that a condition must be satisfied for all initial states, yet the training objective is an expectation measured at only a finite number of samples. The appendix contains an abrupt mention of this point which leads me to believe there is more going on here, but it is a fairly serious omission from the main text and is also not really clarified in the appendix.
- In “Challenge 1” and elsewhere, it is asserted that existing frameworks for stochastic optimization cannot handle non-smooth objectives. This is patently false: every ReLU network ever has been non-smooth, and yet SGD/Adam/… seem to do just fine. Obviously, there is also a rich theory in non-smooth optimization, sub-gradient methods, etc. My objection here is mainly that the paper just asserts that smoothness is critical without ever supporting that claim. Furthermore, the specific context of STL robustness introduces additional nuances that are not addressed.
- Where is the proof of Lemma 1? It seems important, but is nowhere to be found. Same for the equation at the bottom of page 4.
- The modified swish and soft plus functions below Ex. 1 appear to be non-smooth, and what smoothness there is derives only from numerical precision issues. This is less than satisfying. Surely if we are hitting numerical precision issues that points to something more subtle going on, right? For example, it is well-documented in the literature that unstable closed loop dynamics yield exploding gradients in these kinds of policy optimization problems. 
- What is the parameter \bar\rho in Alg. 1? (nit: note also that “Algo” is not a common abbreviation for Algorithm. I believe the IEEE standard, at at least, is “Alg.”)
- I do not follow the entire discussion of the gradient approximation scheme. Fig. 1 makes sense to me and I follow that part of the discussion, but my concern is that the sampling discussion following Definition 2 (and especially the part to the right of Alg. 2) is completely uninterpretable to me. A couple direct questions:
    - Is the matrix S actually being approximated at specific rows, or are entire rows being left out?
    - How is it more efficient to compute the gradient at a sampled point? Doesn’t this essentially require backpropagating through all time steps from the end of time to the beginning, regardless of whether or not you are going to then throw away some of the gradient information?
- Please help me to understand the last sentence before Section 4. Didn’t the guarantees come from simply evaluating the (potentially smoothed) STL formula from every initial condition—i.e., the optimization objective? Why does it matter if we change the algorithm used to approximate gradients?
- nit: "dubins" should be capitalized in the first paragraph of section 4. 
- The authors point to quite a lot of closely related work in this space: I feel that the experiments should benchmark the proposed approaches against one or two of these recent methods. The “comparison” paragraph on page 8 alludes to one such comparison, but it seems like a straw man because of the radical difference in performance. If this is not a straw man comparison, the paper should do a much clearer job of establishing why the baseline is a strong baseline. 
    - Relatedly, I would be interested to see how much of a difference the smoothed STL formula makes in learning (essentially an ablation of the first contribution of this paper).

### Questions
please see above

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

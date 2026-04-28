# Unveiling Options with Neural Network Decomposition

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
In reinforcement learning, agents often learn policies for specific tasks without the ability to generalize this knowledge to related tasks. This paper introduces an algorithm that attempts to address this limitation by decomposing neural networks encoding policies for Markov Decision Processes into reusable sub-policies, which are used to synthesize temporally extended actions, or options. We consider neural networks with piecewise linear activation functions, so that they can be mapped to an equivalent tree that is similar to oblique decision trees. Since each node in such a tree serves as a function of the input of the tree, each sub-tree is a sub-policy of the main policy. We turn each of these sub-policies into options by wrapping it with while-loops of varied number of iterations. Given the large number of options, we propose a selection mechanism based on minimizing the Levin loss for a uniform policy on these options. Empirical results in two grid-world domains where exploration can be difficult confirm that our method can identify useful options, thereby accelerating the learning process on similar but different tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes to decompose piece-wise linear neural networks into options. To do so the authors build on the idea of decomposing a neural network into a neural tree, a quantity closely related to oblique decision trees. As each node of the tree is a sub-policy, the authors propose to use a Levin loss to prune the important sub-policies from which options will be derived. The authors evaluate their approach on a series on grid worlds.

### Strengths
* The authors propose a novel way to learn options, directly from neural networks that are learning, or that have been retrained
* The overall presentation is rigorous as well as the empirical evaluation (10 seeds with 95% CI)
* The method seems to perform better compared to proposed baselines

One of the strong points of the method is the originality in the way the options are discovered. Although the empirical evaluation is limited, the method clearly has a lot of potential as stated by the authors, for example by learning options from "legacy agents". I think the community would do well in integrating such unusual ways of learning options/skills. Moreover, the empirical evaluation is rigorous and clearly shows statistical advantages.

### Weaknesses
 * The presentation is heavy and sometimes confusing. Efforts in addressing this are done but it is not close to being enough
* The HRL baseline of Option-Critic is outdated and does not reflect progress in the field
* The qualitative experiments are very limited

The whole of section 4.1 and 4.2 would require a deep rewriting. Many references to oblique trees are made, yet most of the readers will have no idea what that is. A better visualization than Figure 1 would be needed, and it should be on the same page as the description in 4.1.  I would suggest starting with a simple case of 2 actions and leave the generalizations too much later. The notation of Z is confusing, it adds many sub- and super-scripts that are not well presented. Are the Z functions really necessary to understand the method? The whole section of 4.2 suffers from similar problems. I would strongly suggest the authors to consider the point of view of someone who knows nothing about the specifics of their method and to write these sections from that point of view. It will be most helpful to the paper.

One of the HRL baseline is Option-Critic which is an outdated algorithm that has been beaten many times. [1] recently set strong performance across a wide range of environments. To adequately understand the merits of the method such a baseline should be included.

The qualitative experiments are very limited. Much more on this aspect is needed as interpretabiltiy is one of the hallmarks of HRL. I would suggest heatmaps that show option activation or trajectories that highlight when options are activated.

### Questions
What would be required to scale the method to larger neural networks?

Why investigate the ComboGrid environment? What is interesting about this task?

"we consider small neural networks with one hidden layer, so we can evaluate all sub-policies of a neural policy." This should be highlighted more.


======================================================================

[1] Deep Laplacian-based Options for Temporally-Extended Exploration. Klissarov and Machado. 2023

### Soundness
4 excellent

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the problem of extracting useful skills/options from existing neural network policies. The proposed method involves collecting a set of neural networks (that use piecewise linear activation functions) trained to perform a variety of tasks and then constructing tree structures (neural trees) representing the activation patterns of these networks. Every subtree of a neural tree can be interpreted as a separate policy giving rise to a collection of sub-policies which are used to construct options. Since this collection of options can be large and contain very specialized policies that may not be useful in general, the authors propose a greedy method for selecting a set of useful options. Experiments in grid world environments show that the extracted options are effective in learning to perform new unseen tasks.

### Strengths
- Inferring skills/options that can be used to perform new tasks is an important problem and the proposed approach provides an intuitive way of extracting options from pretrained neural network policies. This method leverages the compositional structure of neural networks to identify sub-policies that might be useful for performing new tasks. Based on my understanding, any such sub-policy matches the original policy on inputs triggering a specific set of activations in the network which represents a specific region of the state space where this option is used in the original policy. Therefore, this appears to be a principled way of extracting options from pretrained policies.
- The idea of directly extracting options from NN policies instead of constructing them during training appears to be novel and interesting. As far as I know, this is the first paper to propose this idea and this might lead to further research on such approaches.
- Experimental results look very promising with the proposed approach outperforming existing baselines for constructing options as well as transfer learning approaches.
- The paper is well-written and examples are provided to illustrate key concepts.

### Weaknesses
 - The main weakness appears to be scalability of the approach w.r.t. the size of the neural network. The total number of options considered is exponential in the size of the network, specifically in the number of piecewise linear units. This leads to a combinatorial explosion in the number of subtrees that need to be evaluated, making the method computationally expensive for larger networks. Furthermore, the option selection method involves enumerating all candidate options, which does not address the computational challenges associated with the exponential growth of the search space. This exhaustive search becomes a bottleneck as the network size increases, limiting the applicability of the approach to relatively small networks.
- Experiments are limited to grid world environments. While grid world environments provide a simplified setting for evaluating the proposed method, they do not fully capture the complexities of real-world tasks. The state and action spaces in grid worlds are discrete and low-dimensional, which may not accurately reflect the challenges associated with continuous or high-dimensional spaces. Experiments in more complex environments with continuous state and action spaces, such as those found in robotics or other control tasks, would significantly strengthen the paper by demonstrating the generalizability of the approach. The current experiments, while promising, do not provide sufficient evidence to confirm the applicability of the method in a wider range of scenarios.

### Questions
1. It appears that Levin loss corresponding to the uniform policy is equivalent to the minimum number of actions (or steps) required to explain a trajectory. Since the general Levin loss is described, are there other natural candidates (which would simply weight different actions/steps differently) besides the uniform policy to use for option selection?
1. Algorithm 1 uses $O(|\mathcal{T}|^2)$ space. It looks like the algorithm can be modified to use $O(|\mathcal{T}|)$ space (the loss after position j is independent of d). Is there a specific reason for using the version in the paper? 
1. It looks like Dec-Options-Whole is doing reasonably well in most cases. Could this suggest a heuristic to reduce the computational complexity by not considering all subtrees of the neural tree? From my understanding, Dec-Options-Whole is only considering a single subtree per tree which is the whole tree, so maybe there is a middle ground between the two extremes?

### Soundness
3 good

### Presentation
3 good

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
The paper proposes to distill policies from a learned neural network and use these as options. They provide an algorithm that translates the neural network into a tree, decomposes it into sub-policies and selects their subset. In experiments, they verify the usefulness of the approach in several variants of grid-based domains.

### Strengths
The paper is well-written and is original in the way the options are created -- i.e., extracting them from an already trained neural network. However, the suggested approach is limited only to simple NNs.

### Weaknesses
First substantial weakness is that the number of sub-policies raises exponentially with the size of the NN, limiting this approach to very small networks and thus the significance of the proposed algorithm. This exponential growth in the number of sub-policies with network size severely restricts the applicability of the method to only the smallest neural networks. For example, even a moderately sized network with a few layers and a reasonable number of nodes per layer would result in an unmanageably large set of sub-policies, making the subsequent selection process computationally infeasible. This limitation is not adequately addressed, and the experiments do not explore the scalability of the approach with larger networks.

Second, given the large number of the subpolicies, it is not clear whether the subset selection (step 3) is better than selecting from a set of random policies. That is, if steps (1) and (2) are ommited and step (3) would select from a random set. In the second example at the end of Experiments, the subpolicies consist of 4 actions, which can be easily randomly generated. This would drastically reduce the complexity of the algorithm, but still would be limited to simle domains. This ablation is crucially missing from the evaluation. The paper does not provide a clear justification for the necessity of the sub-policy extraction process, and it is not clear that the learned sub-policies offer any advantage over randomly generated policies. The evaluation should include a comparison with a baseline that uses randomly generated policies of similar length and number, to demonstrate the value of the proposed approach.

### Questions
Please, present a definite argument (e.g., an experiment or a disproval why I am wrong) that the steps (1) and (2) are needed and the set of extracted sub-policies is useful, compared to a set of random sub-policies. I may reconsider the rating based on the arguments presented.

I assume that in the beginning of the section 4.2, the authors meant `where a_t = argmax_a \pi(s_t , a)`, instead of `where a_t = argmax_a p(s_t , a)`. However, if that is true, why not to sample the actions as `a_t ~ \pi(s)`? If this is to make a unique sequence per each policy, clearly indicate it for the reader and add a reason.

---
Suggestions:
- The graph in Figure 1-right confused me for a while, as I was trying to read it from left-to-right, instead of top-to-down. Indicate this fact for the reader. Also, consider (I don't stress this point) showing the complete graph with the path highlighted.

Typos:
- p. 7: Since learning a policy [IN] the new set ...
- p. 7: baseline Dec-Options-Whole[.]

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

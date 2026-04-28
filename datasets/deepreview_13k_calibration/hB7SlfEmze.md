# PhyloGFN: Phylogenetic inference with generative flow networks

- Decision: Accept
- Avg Score: 6.75
- Scores: 5, 8, 8, 6

## Abstract
Phylogenetics is a branch of computational biology that studies the evolutionary relationships among biological entities. Its long history and numerous applications notwithstanding, inference of phylogenetic trees from sequence data remains challenging: the extremely large tree space poses a significant obstacle for the current combinatorial and probabilistic techniques. In this paper, we adopt the framework of generative flow networks (GFlowNets) to tackle two core problems in phylogenetics: parsimony-based and Bayesian phylogenetic inference. Because GFlowNets are well-suited for sampling complex combinatorial structures, they are a natural choice for exploring and sampling from the multimodal posterior distribution over tree topologies and evolutionary distances. We demonstrate that our amortized posterior sampler, PhyloGFN, produces diverse and high-quality evolutionary hypotheses on real benchmark datasets. PhyloGFN is competitive with prior works in marginal likelihood estimation and achieves a closer fit to the target distribution than state-of-the-art variational inference methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents an application of GFlowNets for phylogenetic inference. The approach encompasses both Bayesian posterior inference and parsimony-based inference (MLE with the assumption of site independence). To address the continuous nature of branch lengths, they are transformed into discrete bins, making the phylogenetic inference problem discrete. GFlowNets are parameterized by neural networks, teaching them a policy to generate phylogenetic trees by selecting and connecting pairs of subtrees. With its probabilistic policy, the system can produce a distribution of phylogenetic trees suitable for posterior inference. In the MLE scenario, the model employs a temperature parameter that, when annealed, ensures the GFlowNet samples align with the MLE samples. The training of GFlowNets utilizes standard trajectory balance. The results suggest that the approach matches the performance of variational inference-based methods for Bayesian posterior inference, and in the MLE case, it is comparable to traditional greedy heuristic-based search algorithms.

### Strengths
- *Innovative Application*: Utilizing GFlowNets for phylogenetic inference is a novel idea, showcasing the versatility of GFlowNets in unique problem settings.
- *Competitive Performance*: The approach not only matches up to VBPI-GNN-based methods in Bayesian posterior inference but offers capabilities beyond them, like generating from arbitrarily filled-in subtrees which preceding methods could not tackle.
- *Estimating probability of suboptimal structures*: The ability to outperform VBPI methods in estimating probabilities of suboptimal structures is a notable accomplishment.

### Weaknesses
 - *Performance vs. Efficiency*: While GFlowNets might perform comparably to PAUP* in the parsimony-based inference setting, the real differentiator would be computational efficiency on a new inference task. Unfortunately, no wall-clock time data is provided, making it challenging to discern any advantages of GFlowNets in this scenario. The lack of information regarding the number of tree evaluations during the search process further obscures any potential benefits in terms of search efficiency. It is unclear if the GFlowNet approach is more efficient in exploring the tree space or if it simply matches the performance of PAUP* by evaluating a similar number of trees, but with a higher computational overhead.
- *Methodological Novelty*: The paper does not seem to bring forth significant machine learning methodological advancements, with much of the methodology being straightforward applications without any notable novel ML innovations for the particular problem at hand. The biggest methodological contribution is the use of discretized bins for branch lengths, which is a compromised solution. The use of a transformer network and standard GFlowNet training is not novel in itself, and the paper does not demonstrate any new techniques in how these are applied to the problem of phylogenetic inference. The discretization of branch lengths, while necessary for the GFlowNet framework, introduces a potential loss of information and is not an ideal solution.
- *Utility of Results*: While the GFlowNets surpass VBPI methods in estimating probabilities for suboptimal structures, the practical significance of this in the context of phylogenetic applications remains unexplained. The experiments focus solely on the accuracy of probability estimates and fail to provide insights into their relevance for the broader application. It is not clear how these improved probability estimates translate to better biological insights or more accurate phylogenetic reconstructions in real-world scenarios. The paper lacks a clear demonstration of how the ability to model suboptimal trees provides a tangible advantage in downstream phylogenetic analysis.

### Questions
- *Time Efficiency*: Given the comparable performance of GFlowNets and PAUP*, can the authors provide information on the computational efficiency (wall-clock time) of GFlowNets to discern its advantages or disadvantages?
- *Utility of Suboptimal Structures*: Can the authors elucidate the practical implications of having estimates for suboptimal structures in the context of phylogenetics? Is there a tangible benefit in real-world applications?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper tackles the related problems of Bayesian phylogenetic inference and maximum parsimony phylogenetic inference.  These problems have recently seen a lot of development in the machine learning space with a flurry of variational approaches.  The novelty in this paper is framing the problem as a Markov Decision Problem, where one needs to sequentially build a tree from the bottom up by joining the roots of rooted trees (starting with each leaf being its own rooted tree with one node).  This paper tries to learn a good policy for the MDP (i.e., a generative model for building trees) using the recently developed GFlowNets.  The paper puts some effort into finding provably good features to use when learning the policy, and showing that the optimal policy would, in fact, result in a distribution over trees equivalent to the posterior.  The authors apply their approach to a number of standard benchmarking datasets and find reasonable performance, particularly for low probability tree topologies.

### Strengths
* The paper is clear and well-written.
* The approach is interesting, conceptually simple, and provides a nice, efficient way to generate distributions over trees that support all of tree space (as opposed to relying on a pre-defined subset of tree space like VBPI).
* The theoretical results and connections to Felsenstein's and Fitch's algorithms are really nice.
* The performance across the full space of trees is promising.

### Weaknesses
 * I know that it is common in the Bayesian Phylogenetics field, but I am uncomfortable with using the Marginal log-likelihood (MLL) as a measure of the accuracy of the posterior.  As the authors note, taking $K \to \infty$ in equation (5) or the log of (S1)results in the true MLL regardless of the distribution used.  For finite $K$, both the bias and variance of the estimated MLL will depend on the learned posterior and it is incredibly difficult for me to compare methods.  For example in Table 1, on DS7, GeoPhy is bolded for having the smallest mean MLL, but its standard error is huge, which suggests to me that by some measures it may not have learned a very good posterior.  Is there a different task that could get at the quality of the posterior in a more interpretable way?
* I also find it somewhat surprising how much VBPI-GNN outperforms PhyloGFN on the MLL estimation task. This is particularly concerning given that the stated goal of the paper is to accurately model the full posterior distribution, and MLL is a standard measure of posterior quality. The large gap in performance suggests that PhyloGFN may not be as effective at capturing the high-probability regions of the posterior as VBPI-GNN.
* Saying that VBPI-GNN is "severely" limited in its applicability to postulating alternative phylogenetic theories feels like far too strong of a statement, especially in light of Table 2 -- for trees with non-negligible posterior probability VBPI-GNN is quite accurate.  I agree that VBPI being unable to put mass on all of tree space is conceptually displeasing, but I don't think the presented evidence supports the claim that VBPI would result in any real-world failures of inference. The claim of severe limitation needs stronger empirical justification, perhaps by showing specific cases where VBPI fails dramatically in a way that PhyloGFN does not.
* Are the axes flipped on Figure 2? If I understand correctly the x-axis should be the unnormalized posterior under the long run of MrBayes, and the y-axis is the unnormalized posterior for either GFN or VBPI.  Why do the points fall on different x-axis ranges for the two columns but very similar y-axis ranges?  (Similarly for Figure S1) This discrepancy in the x-axis ranges raises concerns about the comparability of the results and the interpretation of the plots. It is essential to clarify the exact meaning of each axis and explain why the ranges differ between the two methods.
* It would be nice to include some information about runtime and to include some training curves.  Are these models difficult to train?  How sensitive is training to the choice of distribution over $\tau$?  Etc...

Typos:
* "Given a set of observed sequence" --> "Given a set of observed sequences"
* "Each action chooses a pair of trees and join them" --> "Each action chooses a pair of trees and joins them"
* Is it important or a typo in Proposition 1, Lemma 1, and Lemma 2 that only the branch lengths of the first tree are different?  I.e., it is $(z_1, b_1)$ and $(z_1', b_1')$ but then $(z_2, b_2)$ and $(z_2', b_2)$ and so on.  I don't see that used anywhere.
* In the statement of Lemma 1 I believe it should be $(b(e_{uv}), b(e_{uw}))$ not $(b(e_{uv}), (b(e_{uv}))$.
* This sentence needs substantial rewording: "Note that $R(x) \ne R(x') even $s_1$ and $s_2$ share the same Fitch feature because two trees can have different parsimony score when their root level Fitch feature equals."
* In the proof of proposition 2, I believe that one must multiply by $\frac{\exp \frac{\sum_i M(z_i)}{T}}{\exp \frac{\sum_i M(z_i)}{T}}$, not $\frac{\frac{\sum_i M(z_i)}{T}}{\frac{\sum_i M(z_i)}{T}}$.
* At the bottom of the first paragraph on p. 17 should it be $-\log P(\mathbf{Y} | z,b) P(b)$ not $-\log P(\mathbf{Y} | z,b) P(z)$ in order to match what is in the reward function?
* "ground-trueth" --> "ground-truth"

### Questions
* I am being a bit of a devil's advocate here, and it is a minor point, but, who cares about extremely unlikely trees?  Difference in log-likelihood on Figure 2 suggests that the trees with lowest posterior support are about $10^{-66}$ less likely than the trees with highest posterior support.  Does saying that those trees have zero probability really matter? Is there a real world use-case where knowing the posterior probability of those trees more accurately would be useful?
* Would it be possible to use the machinery presented in this paper just for topologies in the Bayesian setting by somehow marginalizing out branch lengths at each step?  This is obviously not necessary for the present manuscript, I am just curious.
* A preprint that was posted shortly after the ICLR deadline is highly relevant: https://arxiv.org/abs/2310.09553.  Since that was posted after the ICLR deadline, it did not influence my review of this paper.  The method in that preprint, ARTree, is based on reinforcement learning and also seeks to learn a posterior via framing a tree as the outcome of sequential tree building.  Yet, the training objectives and MDP formulation are substantially different, and so I do not see ARTree as reducing in any way the novelty of the present work.  I just bring this up in the hopes that it is interesting/helpful to the authors.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper develops a method for inferring phylogenetic trees, i.e. graphical representations of the evolutionary relationships of species, using Generative Flow Networks (GFlowNets). The GFlowNet treats the tree building processes as a reinforcement learning problem, where the action set corresponds to joining the roots of the subtrees existing in the pool. The paper uses a transformer architecture to encode the input states that correspond to a set of features extracted from subtree structures.

### Strengths
* Both the proposed model architecture and the use of GFlowNets for the chosen application are novel and interesting.

 * The paper conducts a large body of well-planned experiments, compares against a properly chosen set of baselines and reports results favorable to the proposed method. 

 * The fact that the comparison is not made against many alternative methods is understandable, as there probably are not many modern machine learning methods addressing the same problem.

* The design choices used in the model architecture are well justified, for instance the one given at the end of Page 6 for the transformer makes perfect sense.

### Weaknesses
 * The biggest weakness looks to me like the results in Table 1. The log-likelihood scores look very similar to each other. For instance -7108.95 for PhyloGFN and 7108.95 VBPI-GNN. Similar for other data sets. This raises concerns about whether the proposed method offers a significant improvement in terms of model fit, given that the reported values are practically identical. The lack of substantial difference in log-likelihood suggests that the GFlowNet approach might not be capturing significantly different aspects of the data compared to existing methods, at least as measured by this metric.

 * It is great that the paper makes lots of effort to ensure the reproducibility of the results. However, It looks to me like the main paper lacks some essential details about the experiments, making it a bit hard for the reader to evaluate the results. See my question below. For example, the precise details of the training procedure, such as the number of training epochs, learning rate schedules, and specific optimization algorithms used, are not clearly stated in the main text. This lack of information makes it difficult to assess the robustness and reliability of the reported results.

 * Likewise, the paper would be more readable by the machine learning community if the used tree-level features are explained. As far as I was able to detect, the main paper mentions only that they are Fitch and Felsenstein features, which may be obvious to an evolutionary biologist but they do not tell anything to me as a machine learning researcher. Now that this is not a biology journal but a machine learning research venue, an introduction to such basic concepts somewhere in the paper could be beneficial. The paper should provide a more detailed explanation of how these features are computed and what specific information they encode about the tree structure. This would help machine learning researchers better understand the input representation used by the model.

 * The paper reports log-likelihood results, which measures model fit. It measures parsimony, which appears to be about the computational aspect. The log densities reported in Figure 2 is an indicator of diversity. It may be better to have a more direct and interpretable score of the discovery performance, for instance prediction accuracy of evolution tree links or ancestral relationship detection between pairs of species in cases where there is agreement on the ground truth. The current result landscape looks a bit too exploratory. While the results make intuitive sense, they still leave many gray areas in their detailed interpretation. The paper should consider including metrics that directly assess the accuracy of the inferred evolutionary relationships, such as the Robinson-Foulds distance to a known ground truth tree when available, or the ability to predict ancestral states.

### Questions
Are the \pm values given in Table 1 standard deviation or standard error? What are these standard deviations/error over? Experiment repetitions? If standard deviation across repetitions, the results may be good enough. They may be alarming otherwise.

Overall this is an interesting piece of work with decent potential for impact. I also give sincere value to the effort the authors make to use advanced machine learning methods for such hard applications of natural sciences. However, the paper requires some work to improve, especially in terms of presentation and clarification before being ready for publication. The case looks to me like borderline at present but has potential to improve towards an accept after the rebuttal.

---

The rebuttal has addressed my concerns, so I raise my score to an accept.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This is a nice application of GFlowNets to the phylogeny problem in computational biology. There is a main issue that needs to be resolved, namely the performance. First the marginal likelihood comparison with other methods, are the PhyloGFN better in terms of lower bound and what is the running time required to get these results. Second, regarding the better estimates of posterior probabilities for low posterior  phylogenetic tree (which may be the main selling point for this paper), what is the gold standard and how does your running time compare with that of he gold standard and those of the other methods? Running time doesn't have to be measured as wall-clock or using a formal analysis, but could be based on the number of so-called Felsenstein peeling operations (or whatever that make it likely that this approach may with sufficient effort yield a efficient method in the future, if that isn't already the case). The proper resolution of these issues should make this become a good contribution.

### Strengths
The strength is really the novelty and that this method both obtains good performance and is not limited to a predefined set of trees.

### Weaknesses
This is a nice application of GFlowNets to the phylogeny problem in computational biology. There is a main issue that needs to be resolved, namely the performance. First the marginal likelihood comparison with other methods, are the PhyloGFN better in terms of lower bound and what is the running time required to get these results. Second, regarding the better estimates of posterior probabilities for low posterior  phylogenetic tree (which may be the main selling point for this paper), what is the gold standard and how does your running time compare with that of he gold standard and those of the other methods? Running time doesn't have to be measured as wall-clock or using a formal analysis, but could be based on the number of so-called Felsenstein peeling operations (or whatever that make it likely that this approach may with sufficient effort yield a efficient method in the future, if that isn't already the case). The proper resolution of these issues should make this become a good contribution.

It is not really trying to explain the GFN approach to the reader, but rather enumerating required items. The running time and performance in general require further explanation. The parsimony case is clearly less interesting and could partially be move to the appendix.

high complexity of tree space

■ Page 1
It is large! complex is less clear.  
 

PhyloGFN is competitive with prior works in marginal likelihood estimation and achieves a closer fit to the target distribution than state-of-the-art variational inference methods

■ Page 1

I don’t know, but the better fit for lower part of the posterior is worth mentioning. It may be key.


continuous vari- ables that capture the level of sequence divergence along each branch of the tree.

■ Page 1

Also the ml version has those.


Coming from the intersection of variational inference and reinforcement learning is

■ Page 1

Reformulate.


PhyloGFN leverages a novel tree representation inspired by Fitch and Felsenstein’s algorithms to represent rooted trees without introducing additional learnable parameters

■ Page 2

Make this clearer. In particular, in addition to what?


explores

■ Page 2

No it has capacity or potential to do this.


state-of-the-art MCMC

■ Page 2

The comparison must be made relative to resources since you use mcmc as gold standard


With their theoretical foundations laid out in Bengio et al. (2023);

■ Page 2

Is this the gfn sota? Then point out this fact.


The tree topology can be either a rooted binary tree or a bifurcating unrooted tree.

■ Page 2

This is a potential weakness. Can you restrict you method to binary trees? Does this mean that the posterior support of a subsplit consist of both binary and multifurcating trees? On an earlier reading i got the impression that you considered binary trees. Please clarify.


This equation can be used to recursively compute 𝑃(𝐿𝑖 𝑢|𝑎𝑖 𝑢) at all nodes of the tree and sites 𝑖. The algorithm performs a post-order traversal of the tree,

■ Page 3

This is called dynamic programming


recursively computed by (1)

■ Page 3

Again DP


The algorithm traverses the tree two times, first in post-order (bottom-up) to calculate the character set at each node, then in pre- order (top-down) to assign optimal sequences.

■ Page 4

Also this is DP


Generative flow networks (GFlowNets) are algorithms for learning generative models of complex distributions given by unnormalized density functions over structured spaces. Here, we give a con- cise summary of the the GFlowNet framework.

■ Page 4

This section could provide more insight


The direct optimization of 𝑃𝐹’s parameters 𝜃 is impossible since it involves an intractable sum over all complete trajectories.

■ Page 4

This argument is incorrect. With polynomial length trajectories, which you need, exponentially many trajectories implies exponentially many states. The ladder also yields your optimization infeasible, in worst case.


Each action chooses a pair of trees and join them at the root, thus creating a new tree

■ Page 5

This suggests binary trees. “At the root” is a poor formulation.


hus, a state 𝑠 consists of a set of rooted trees

■ Page 5

Disjoint rooted …


its two children

■ Page 5

This should close the case!


all of which can be reached by our sampler

■ Page 5

Are all probabilities always non zero ?


State representation To represent a rooted tree in a non-terminal state, we compute features for each site independently by taking advantage of the Felsenstein features (§3.1.1).

■ Page 5

Can you motivate this choice?


Although the proposed feature representation 𝜌 does not capture all the information of tree structure and leaf sequences, we show that 𝜌 indeed contains sufficient informa- tion to express the optimal policy

■ Page 6

What is the optimal policy? How do you show this?


Proposition 1. Let 𝑠1 = {(𝑧1, 𝑏1), (𝑧2, 𝑏2) . . . (𝑧𝑙, 𝑏𝑙)} and 𝑠2 = {(𝑧′ 1, 𝑏′ 1), (𝑧′ 2, 𝑏2) . . . (𝑧′ 𝑙, 𝑏𝑙)} be two non-terminal states such that 𝑠1 ≠ 𝑠2 but sharing the same features 𝜌𝑖 = 𝜌′ 𝑖. Let 𝒂 be any sequence of actions, which applied to 𝑠1 and 𝑠2, respectively, results in full weighted trees 𝑥 = (𝑧, 𝑏𝑧 ), 𝑥′ = (𝑧′, 𝑏′), with two partial trajectories 𝜏 = (𝑠1 → · · · → 𝑥), 𝜏′ = (𝑠2 → · · · → 𝑥′). If 𝑃𝐹 is the policy of an optimal GFlowNet with uniform 𝑃𝐵, then 𝑃𝐹 (𝜏) = 𝑃𝐹 (𝜏′

■ Page 6

Please explain the importance.


−7108.42 ±0.18 −7108.41 ±0.14 −7290.36 ±7.23 −7111.55 ±0.07 −7108.95 ±0.06

■ Page 7

At least the second method is a lower bound and it entire interval os above yours. Isn’t that better?


Pearson correlation of model sampling log-density and ground truth unnormalized posterior log-density for each dataset o

■ Page 8

How is the ground truth obtained?


589

■ Page 8


512

■ Page 8


0.624

■ Page 8

Fails miserably


BAYESIAN PHYLOGENETIC INFERENCE

■ Page 8

What is the computational resources required for these methods?


The base- lines we compare to are the MCMC-based MrBayes combined with the stepping-stone sampling tech- nique (Ronquist et al., 2012),

■ Page 8

How do you obtain that and are you sure of how it is computed?


To select pairs of trees to join, we evaluate tree-pair features for every pair of trees in the state and pass these tree-pair features as input to the tree MLP to generate probability logits for all pairs of trees. The tree-pair feature for a tree pair (𝑖, 𝑗) with representations 𝑒𝑖, 𝑠𝑗 is the concatenation of 𝑒𝑖 + 𝑒 𝑗 with the summary embedding of the state, i.e., the feature is [𝑒𝑠; 𝑒𝑖 + 𝑒 𝑗], where [·; ·] denotes vector direct sum (concatenation). For a state with 𝑙 trees, 𝑙 2 = 𝑙(𝑙−1) 2 such pairwise features are generated for all possible pairs

■ Page 16

### Questions
high complexity of tree space

■ Page 1
It is large! complex is less clear.  
 

 

PhyloGFN is competitive with prior works in marginal likelihood estimation and achieves a closer fit to the target distribution than state-of-the-art variational inference methods

■ Page 1

 

I don’t know, but the better fit for lower part of the posterior is worth mentioning. It may be key.

 

 

continuous vari- ables that capture the level of sequence divergence along each branch of the tree.

■ Page 1

 

Also the ml version has those.

 

 

Coming from the intersection of variational inference and reinforcement learning is

■ Page 1

 

Reformulate.

 

 

PhyloGFN leverages a novel tree representation inspired by Fitch and Felsenstein’s algorithms to represent rooted trees without introducing additional learnable parameters

■ Page 2

 

Make this clearer. In particular, in addition to what?

 

 

explores

■ Page 2

 

No it has capacity or potential to do this.

 

 

state-of-the-art MCMC

■ Page 2

 

The comparison must be made relative to resources since you use mcmc as gold standard

 

 

With their theoretical foundations laid out in Bengio et al. (2023);

■ Page 2

 

Is this the gfn sota? Then point out this fact.

 

 

The tree topology can be either a rooted binary tree or a bifurcating unrooted tree.

■ Page 2

 

This is a potential weakness. Can you restrict you method to binary trees? Does this mean that the posterior support of a subsplit consist of both binary and multifurcating trees? On an earlier reading i got the impression that you considered binary trees. Please clarify.

 

 

This equation can be used to recursively compute 𝑃(𝐿𝑖 𝑢|𝑎𝑖 𝑢) at all nodes of the tree and sites 𝑖. The algorithm performs a post-order traversal of the tree,

■ Page 3

 

This is called dynamic programming

 

 

recursively computed by (1)

■ Page 3

 

Again DP

 

 

The algorithm traverses the tree two times, first in post-order (bottom-up) to calculate the character set at each node, then in pre- order (top-down) to assign optimal sequences.

■ Page 4

 

Also this is DP

 

 

Generative flow networks (GFlowNets) are algorithms for learning generative models of complex distributions given by unnormalized density functions over structured spaces. Here, we give a con- cise summary of the the GFlowNet framework.

■ Page 4

 

This section could provide more insight

 

 

The direct optimization of 𝑃𝐹’s parameters 𝜃 is impossible since it involves an intractable sum over all complete trajectories.

■ Page 4

 

This argument is incorrect. With polynomial length trajectories, which you need, exponentially many trajectories implies exponentially many states. The ladder also yields your optimization infeasible, in worst case.

 

 

Each action chooses a pair of trees and join them at the root, thus creating a new tree

■ Page 5

 

This suggests binary trees. “At the root” is a poor formulation.

 

 

hus, a state 𝑠 consists of a set of rooted trees

■ Page 5

 

Disjoint rooted …

 

 

its two children

■ Page 5

 

This should close the case!

 

 

all of which can be reached by our sampler

■ Page 5

 

Are all probabilities always non zero ?

 

 

State representation To represent a rooted tree in a non-terminal state, we compute features for each site independently by taking advantage of the Felsenstein features (§3.1.1).

■ Page 5

 

Can you motivate this choice?

 

 

Although the proposed feature representation 𝜌 does not capture all the information of tree structure and leaf sequences, we show that 𝜌 indeed contains sufficient informa- tion to express the optimal policy

■ Page 6

 

What is the optimal policy? How do you show this?

 

 

Proposition 1. Let 𝑠1 = {(𝑧1, 𝑏1), (𝑧2, 𝑏2) . . . (𝑧𝑙, 𝑏𝑙)} and 𝑠2 = {(𝑧′ 1, 𝑏′ 1), (𝑧′ 2, 𝑏2) . . . (𝑧′ 𝑙, 𝑏𝑙)} be two non-terminal states such that 𝑠1 ≠ 𝑠2 but sharing the same features 𝜌𝑖 = 𝜌′ 𝑖. Let 𝒂 be any sequence of actions, which applied to 𝑠1 and 𝑠2, respectively, results in full weighted trees 𝑥 = (𝑧, 𝑏𝑧 ), 𝑥′ = (𝑧′, 𝑏′), with two partial trajectories 𝜏 = (𝑠1 → · · · → 𝑥), 𝜏′ = (𝑠2 → · · · → 𝑥′). If 𝑃𝐹 is the policy of an optimal GFlowNet with uniform 𝑃𝐵, then 𝑃𝐹 (𝜏) = 𝑃𝐹 (𝜏′

■ Page 6

 

Please explain the importance.

 

 

−7108.42 ±0.18 −7108.41 ±0.14 −7290.36 ±7.23 −7111.55 ±0.07 −7108.95 ±0.06

■ Page 7

 

At least the second method is a lower bound and it entire interval os above yours. Isn’t that better?

 

 

Pearson correlation of model sampling log-density and ground truth unnormalized posterior log-density for each dataset o

■ Page 8

 

How is the ground truth obtained?

 

 

589

■ Page 8

 

 

512

■ Page 8

 

 

0.624

■ Page 8

 

Fails miserably

 

 

BAYESIAN PHYLOGENETIC INFERENCE

■ Page 8

 

What is the computational resources required for these methods?

 

 

The base- lines we compare to are the MCMC-based MrBayes combined with the stepping-stone sampling tech- nique (Ronquist et al., 2012),

■ Page 8

 

How do you obtain that and are you sure of how it is computed?

 

 

To select pairs of trees to join, we evaluate tree-pair features for every pair of trees in the state and pass these tree-pair features as input to the tree MLP to generate probability logits for all pairs of trees. The tree-pair feature for a tree pair (𝑖, 𝑗) with representations 𝑒𝑖, 𝑠𝑗 is the concatenation of 𝑒𝑖 + 𝑒 𝑗 with the summary embedding of the state, i.e., the feature is [𝑒𝑠; 𝑒𝑖 + 𝑒 𝑗], where [·; ·] denotes vector direct sum (concatenation). For a state with 𝑙 trees, 𝑙 2 = 𝑙(𝑙−1) 2 such pairwise features are generated for all possible pairs

■ Page 16

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

# Offline RL with Smooth OOD Generalization in Convex Hull and its Neighborhood

- Decision: Accept
- Scores: 8, 5, 8, 6

## Abstract
Offline Reinforcement Learning (RL) struggles with distributional shifts, leading to the $Q$-value overestimation for out-of-distribution (OOD) actions. Existing methods address this issue by imposing constraints; however, they often become overly conservative when evaluating OOD regions, which constrains the $Q$-function generalization. This over-constraint issue results in poor $Q$-value estimation and hinders policy improvement. In this paper, we introduce a novel approach to achieve better $Q$-value estimation by enhancing $Q$-function generalization in OOD regions within Convex Hull and its Neighborhood (CHN). Under the safety generalization guarantees of the CHN, we propose the Smooth Bellman Operator (SBO), which updates OOD $Q$-values by smoothing them with neighboring in-sample $Q$-values. We theoretically show that SBO approximates true $Q$-values for both in-sample and OOD actions within the CHN. Our practical algorithm, Smooth Q-function OOD Generalization (SQOG), empirically alleviates the over-constraint issue, achieving near-accurate $Q$-value estimation. On the D4RL benchmarks, SQOG outperforms existing state-of-the-art methods in both performance and computational efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces the method of using the convex hull and a smooth Bellman operator to solve the challenge of over-conservative behaviors in offline reinforcement learning algorithms. 
Both theoretical analysis and empirical justifications of the proposed method are provided.
The results look promising on the reported tasks.

### Strengths
The paper is well written and the structure is clear. The idea is supported by both theoretical justification and relatively sufficient empirical study.


----

The authors made a great effort in the rebuttal process and addressed all my concerns.

### Weaknesses
Using convex hulls and nearest neighbors in reinforcement learning is not a new technique, yet the current paper does not discuss those methods. Giving credit to the existing work will not hurt the novelty of this paper but will help readers have a clearer understanding of the advancements in the field.

[1] Sun, Hao, et al. "Accountability in offline reinforcement learning: Explaining decisions with a corpus of examples." Advances in Neural Information Processing Systems 37 (2023).

[2] Lyu, Jiafei, et al. "SEABO: A Simple Search-Based Method for Offline Imitation Learning." arXiv preprint arXiv:2402.03807 (2024).


Figure 3 (the table) is not very clear. The authors may want to re-organize the information in a different format.

### Questions
Limitations and potential pitfalls of the proposed method are not discussed. Could the authors explain more about the potential challenges of the proposed method? e.g., how do the choices of distance metric affect the results? what would be the trade-off between generalization and conservative behaviors? Is there any task that would benefit more from a conservative estimation or more aggressive extrapolation? Having analyses of some case studies would greatly improve the clarity and impact of the paper.

How does the proposed method scale with different numbers of training samples (i.e., such that convex hulls differ)? Could the authors provide some analysis of the computational cost (time/memory usage), and compare different methods in those settings?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses the problem of generalization in offline RL. Most existing techniques tend to severely constrain the policy to produce actions that remain close to the data distribution, to avoid known nefarious effects of OOD generalization in unexplored parts of the state-action space. This paper suggests that these constraints can be alleviated. In particular, they identify a region close to the dataset (the CHN) where controlled estimation of the Q-values is possible, whereas this region is usually treated as completely OOD by existing techniques. After deriving a variant of the Bellman operator that leverages the existence of this region and showing some of its properties, the authors propose a concrete regularization term to add to the classic critic loss in offline RL. The authors first showcase the existence of the over-constraining problem on a classic offline RL algorithm, and that their method alleviates this issue. They then evaluate their method on the D4RL benchmark, showing improved performance compared to baselines while having a quick runtime.

### Strengths
- First, I find that the problem tackled is important and very well motivated. I found in particular that the introduction did a great job of exposing to the reader the problem of over-constraining the policy. The simple but logical explanation is rooted in the design of existing policies that completely avoid to generalize OOD. Having described the problem, the authors are then clear in their ambition: leveraging the part of the state space where neural networks actually are able to generalize to improve the approximation of Q, and possibly of the learned policy. I think this idea is very sensible, and sounds like a natural and promising follow-up to the existing literature following the introduction. I expect a work in this direction to be very interesting.
- The practical algorithm is simple to implement, as it is just adding a smoothing term to the loss. This is a strong point of the empirical part of the proposed approach, since practitioners can easily add this term to their training loss. This also makes the algorithm very quick to run, which is a great advantage compared to certain competitors (such as MCQ) that are much slower.
- I find the sanity check (in particular Fig 1.b) to be a very convincing illustration of the problem that motivated the paper. The authors show how a classic baseline, TD3+BC, tends to keep its high Q-value predictions close to the regions of high data density. I find this is a great illustration of the over-constraining problem. At the same time, this figure shows that SQOG does not suffer from the same limitations.
- The ablation study illustrated in Fig. 4 was a welcome addition that shows the sensitivity of the method to one of its main hyperparameters. 
- Finally, the algorithm seems to perform well according to the results in Table 1. In Fig. 1, the authors show that their method is indeed more robust to OOD and approximates well the true action values, while TD3+BC tends to keep its predictions well within the data distribution. This is consistent with the story of the paper.

### Weaknesses
Unfortunately, I found that the paper lacked clarity and mathematical rigor at several crucial moments, which severely hurt my understanding of the contribution.
- Most importantly, I believe there is a mistake with the definition of perhaps the most central object of the paper, CHN. As it is defined, by construction, $N(Conv(D)) \subset (S,A)_D \subset Conv(D)$, therefore $CHN(D) = Conv(D)$. It is not clear how to change the existing definition to get to the one that seems intended by the authors (on this note, a figure of $(S,A)_D$, $Conv(D)$, and $N(Conv(D)$) would have been enlightening, I encourage you to add one). The current definition implies that the neighborhood of the convex hull is contained within the convex hull itself, which is not geometrically plausible. This suggests a fundamental flaw in the definition that needs to be addressed for the rest of the paper to make sense.
- In Definition 1, the definition of $(S,A)_D$ is confusing: it is mentioned to be a space, using the space notation of the preliminaries, but it seems from the rest of the definition that it is the set of state-action tuples from D. Moreover, r is named as the neighborhood radius and seems like a free parameter to set, but is then defined in Proposition 1 as a function of D and its convex hull: what definition should we follow? The ambiguity in defining $(S,A)_D$ as both a space and a set of tuples creates confusion, and the dual definition of 'r' as a free parameter and a function of D introduces inconsistency.
- The definition of OOD was another major point of confusion to me. It is indicated that actions that are OOD are actions that are outside the support of the behavior policy $\mu$ (which is restated in Definition 2). But as far as I can tell there are no constraints on the behavior policy $\mu$ that generated the dataset. What if this policy put a non-zero probability on every action? This is far from an edge case, since a behavior policy parametrized as a Gaussian distribution would have support on the full action space. Then, what is the relationship with D? The text pushes me to think that what is OOD is what is far enough from D, but within the CHN (L153): then is OOD what is far from the empirical distribution derived from D? To illustrate the confusion, the authors write at L317 that the [-0.5, 0.5] region in Fig.1 is OOD, but the density is clearly non-zero for almost all of this range, contradicting how OOD was defined earlier. Overall, my impression is that two notions of OOD are colliding in this paper: the formal one from Definition 2 stating that every action outside of the support of $\mu$ is OOD, and the intuitive one from Figure 1 that regions of low-density are OOD. The lack of clarity in defining OOD undermines the theoretical framework and the interpretation of experimental results.
- The confusion inherited from the unclear definitions of the spaces of Sec 3.1 is transfered to Sec 3.2. For instance, in Definition 2, the authors refer to “neighborhood”. why not use a precise mathematical object that you defined earlier, likely in Definition 1? On that note, the neighborhood was defined w.r.t state-action tuples in Definition 1, but now refers to the action only, which does not help with the clarity of exposition. If that is normal, then I think it would be useful to comment on why the state space needs to be included in the CHN definition. As a consequence, neighbor/neighborhood is used several times (L170/175/214) but since it is not clear to me where the exact definition is, it is difficult to follow the text more than at an intuitive level.

_Other weaknesses_
- I find that a discussion of the link between the SBO and the proposed loss would have been helpful for the flow of the paper. As it stands, Section 3.2 introduces the SBO and some of its properties, while Sec 3.3 switches direction and proposes a regularization term, a bit out of the blue. I think a smoother transition between the two section, justifying the key elements to keep of the SBO, and how they motivated the new regularization term, would have helped the exposition. The lack of a clear connection between the theoretical SBO and the practical loss function makes it difficult to understand the motivation behind the proposed regularization term.
- One of the key aspects of the empirical loss is the noise added to the in sample action to possibly get an artificial OOD sample. The authors did an ablation on the type of noise, but I would have been curious to see a discussion on the scale of the noise instead, as this should control the amount of “OOD-ness” and might influence the performance of the algorithm. The absence of a discussion on the noise scale leaves a gap in understanding how this crucial hyperparameter influences the algorithm's behavior.
- In proposition 1, the authors refer to the NTK regime without explaining the acronym nor introducing the general framework. I think the framework should be at least introduced. The lack of context for the NTK regime makes it difficult to assess the validity and implications of Proposition 1.
- I am also unclear about the last sentence of the paragraph preceding proposition 2 (l. 138-139): how did you derive this statement? The derivation of this statement is not clear, which makes it difficult to verify the claim.
- The norm used in all mathematical statements besides Theorem 4 is unclear. The lack of clarity regarding the norm used in the mathematical statements introduces ambiguity and makes it difficult to follow the derivations.
- at L170, the authors write “the dataset action […]”: this assumes that this action exists and that it is unique, but it is not clear to me if this is true. The assumption of a unique dataset action within a neighborhood is not justified and requires further clarification.

_Minor weaknesses that did not affect the score but could be addressed anyway_
- A suggestion: Fig. 1 (1.b in particular) does a great job of illustrating the overconstraint issue of TD3+BC. It would be interesting to consider showing this figure earlier in the paper. I am OK with where the figure is right now and this did not impact my score, but I think this could convince the reader very early on that the problem you are tackling is real and substantial.
- In the experiments, I found confusion the exact definition of the true Q values (L314): are you using Monte Carlo estimation of a (s,a) pair, resetting the environment at this state? Similarly, what do you mean exactly by standardized and smoothed (L315)? The lack of detail in describing the true Q-value calculation and the standardization process makes it difficult to reproduce the results.
- Besides the comments above, I find that the mathematical notation was imprecise or inconsistent at a couple other spots. For instance, replacing “noise” in Eq. 14 by an actual variable; the action $a^{in}_{neighbor}$ is indicated sampled from a support (L170); the expectations are taken w.r.t $\pi$ (L.85) or $\pi(\cdot | s’)$. The inconsistent and imprecise mathematical notation makes it challenging to follow the derivations and understand the proposed method.
- “Longest diameter” -> you can drop the “longest”, diameter is already the supremum of the distances within the set.
- L135: “Due to the uniqueness of CHN”: this fact is never stated before, but since it is referred to like this, I would have expected to have a sentence stating that the CHN is unique (maybe at L115-116) with the other properties.
- In the appendix, you indicate in the proof “we can easily derive” (L744), but in a proof I would expect for this derivation to be there.
- The authors ran several algorithms on several algorithms, but unfortunately on a rather small number of seeds (4). A higher number of seeds could have gotten these confidence interval smaller and non intersecting.

### Questions
- Can you please precise the different definitions, most importantly of CHN? I believe there is a mistake in its current form. Please also confirm what $(S,A)_D$ is, as it is not properly defined (in mathematical terms).
- Could you please write a mathematical definition that confirms the notion of OOD that was chosen in this work? Is it the one of Definition 2?
- Could you comment on the link between the SBO and the OG loss of Eq.13? Are these two objectives equivalent? If not, what are the differences? What is captured by one but not the other?
- How did you decide on the scale (and the clip) of the noise distribution, indicated at p.19? Are they sensible hyperparameters for the performance of the algorithm?
- Regarding Eq. 14: for s’ that are at the “boundary” of D, and a’ potentially far from the dataset: the OOD backprop effect will not be countered by the new smoothing term, is that correct? 
- $a_{ood}$ seems to implicitly belong to CHN in Prop. 3. $a_{ood}$ was introduced in the main text of Sec 3.2, was it already part of CHN then or could it also be outside of CHN?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces the Smooth Bellman Operator (SBO), aimed at addressing the over-constraint issues prevalent in popular offline RL algorithms. Building on SBO, the authors propose SQOG, a practical algorithm that demonstrates superior performance over well-known baselines like CQL, IQL, and MCQ, on D4RL benchmark. The paper also includes ablation studies examining the impact of the hyperparameter \beta, which controls the out-of-distribution (OOD) generalization loss, and different types of noise. Additionally, the paper provides theoretical analysis that supports the efficacy of the SBO.

### Strengths
1. The paper is well-written and easy to follow.
2. SQOG achieves strong performance on the D4RL benchmark, remaining relatively simple, straightforward, and computationally efficient.
3. The sanity check on the Inverted Double Pendulum task empirically shows SBO’s effectiveness in alleviating the over-constraint issue, which is a valuable addition.

### Weaknesses
1. My key concern is the lack of discussion on the relationship between SBO and behavior cloning loss. While the paper claims that SBO alleviates the over-constraint issue in existing offline methods, it’s unclear to me that whether SBO’s effectiveness is limited to use with TD3+BC. Further discussion on this point would be beneficial.
2. The Inverted Double Pendulum task is relatively simple and differs from locomotion tasks, raising questions about whether SQOG can maintain accurate Q-value estimates in higher-dimensional environments. While visualizing Q-values in high-dimensional spaces may not be as straightforward as with the Inverted Double Pendulum, including experiments on a locomotion task to validate SQOG’s Q-estimation accuracy would strengthen this claim.
3. All experiments were conducted with only 4 seeds; additional seeds would improve result robustness.

### Questions
See above

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a novel offline RL algorithm, Smooth Q-function OOD Generalization (SQOG), aimed at improving Q-value estimation by enhancing the generalization of the Q-function within the Convex Hull and its Neighborhood (CHN). The authors provide theoretical guarantees, showing that the proposed algorithm approximates true Q-values for both in-sample and out-of-distribution (OOD) actions. On the D4RL benchmarks, SQOG demonstrates superior performance compared to state-of-the-art methods.

### Strengths
The paper is well-organized. The proposed algorithm SQOG significantly reduces computational costs compared to existing algorithms.

### Weaknesses
 - **Novelty:** The proposed SQOG method builds on the concepts of the Convex Hull and its Neighborhood (CHN) and the Smooth Bellman Operator (SBO). The use of CHN was first introduced in DOGE [1], and SBO for in-sample Q-value updates is a common practice in offline RL. These techniques are not new, which makes the contribution appear incremental. It would be better to clarify the difference or advantage of these techniques compared to existing methods.
- **Neighborhood**: While the introduction of the neighborhood is intended to alleviate the over-constraining issue of OOD actions, it is unclear how this concept is reflected in Theorem 1 and informs practical implementation. Additionally, although the authors theoretically demonstrate that SQOG can achieve good OOD evaluation, the underlying assumptions—such as the continuity of the Q-function—are idealistic. For example, in sparse reward environments like Montezuma's Revenge, where only a few actions yield rewards, the Q-function is likely to be discontinuous or stepwise. Furthermore, the continuity assumption, as presented, applies to the true Q-function ($Q^{\pi}$), not the parametric approximation, which is problematic as the true Q-function is often discontinuous in practice. This raises concerns about the validity of the theoretical analysis when the true Q-function is not smooth.
- **Connection between theory and practice:** There appears to be a disconnect between the theoretical and experimental sections. The theory suggests using CHN and SBO, but even without these components, a researcher familiar with offline RL could still design an algorithm based on principles like pessimism and in-sample updates. The writing should better emphasize the unique advantages of CHN to make its value more apparent. Specifically, the practical algorithm constructs OOD actions by adding noise to in-sample actions, but the theoretical justification for this approach and its connection to the CHN is not clearly established. The theoretical analysis does not explicitly address how the specific noise distribution and clipping range affect the safety guarantees or the quality of the learned OOD Q-values.
- **The quality of the dataset:** In my opinion, CHN essentially augments the data by adding state-action pairs near the original dataset, making the quality of the dataset crucial for performance. In high-dimensional state and action spaces, the main challenge is often limited sample size. It would help to discuss this issue further or use toy examples to illustrate the benefits of CHN.

### Questions
Q1: In Figure 1, I am curious about how to calculate the true Q values for action in the range $[0,1]$. Also, it would be more appropriate to refer to these as "ground truth" Q-values. Furthermore, the "true Q-values" are shown as a smooth line due to the use of neural network function approximation. However, as mentioned earlier, the true Q function (which is not precisely known in the MuJoCo environment) could be quite irregular or even stepwise.  This makes the toy example less convincing in demonstrating the accuracy of the approximation. 

Q2: In the conclusion, the authors state that solving the CHN and identifying all OOD regions within it is both impractical and unnecessary. While I partially agree, I also hold a different viewpoint. The authors mention that one advantage of CHN is its safety guarantees, as measured by the neighborhood radius. I noticed that in the code, the noise is clipped within the range [−0.5,0.5]. Have the authors experimented with tuning this parameter? If so, providing more experimental details would be beneficial, as the clipped range directly affects the neighborhood radius associated with the safety guarantees.

### Soundness
3

### Presentation
2

### Contribution
2

# Null Counterfactual Factor Interactions for Goal-Conditioned Reinforcement Learning

- Decision: Accept
- Avg Score: 6.75
- Scores: 6, 5, 8, 8

## Abstract
Hindsight relabeling is a powerful tool for overcoming sparsity in goal-conditioned reinforcement learning (GCRL). While effective in some domains like navigation and locomotion, hindsight relabeling can struggle in object-centric domains. For example, suppose that the goal space consists of a robotic arm pushing a particular target block to a goal location. In this case, hindsight relabeling will give high rewards to any trajectory that does not interact with the block. However, these behaviors are only useful when the object is already at the goal—an extremely rare case in practice. A dataset dominated by these kinds of trajectories will make learning more difficult. On the other hand, much of the meaningful behavior is filtered through interactions such as pushing the block with the gripper. To address this issue, we introduce Hindsight Relabeling using Interactions (HInt), which combines interactions with hindsight relabeling to improve the sample efficiency of downstream RL. However, interactions do not have a general consensus statistical definition, and especially one useful for downstream GCRL. Therefore, we propose a definition of interactions based on the concept of null counterfactual: a cause object is interacting with a target object if in a world where the cause object did not exist, the target object would have different transition dynamics. We leverage this definition to infer interactions in Null Counterfactual Interaction Inference (NCII), which uses a “nulling” operation with a learned model to simulate absences and infer interactions. We demonstrate that NCII is able to achieve significantly improved interaction inference accuracy on both simple linear dynamics domains and dynamic robotic domains in Robosuite, Robot Air Hockey, and Franka Kitchen. Furthermore, we demonstrate that HInt improves sample efficiency by up to 4× in these domains as goal-conditioned tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes to leverage the null assumption to filter out states without interaction between the agent and object, improving the sample efficiency of GCRL. The approach begins by using a learned dynamics model to identify null states—where the next state remains the same in the absence of a specific state. It then keeps those trajectories where the agent directly interacts with the object, training the agent with hindsight relabeling. This approach shows comparable or superior sample efficiency in both 2D dynamic and 3D manipulation environments.

### Strengths
- The introduction of the *Null counterfactual interaction assumption* could be a important contribution, improving sample efficiency across various domains, particularly in manipulation tasks where interaction is minimal.
- The method details engineering practices to make the approach both manageable and efficient.
  + This includes null state inference with a dynamics model and predicting null operation.
- The paper presents a rich set of environments, and design choices for these environments, etc.

### Weaknesses
 - **Scalability to high-dimensional state**
  + How is the state space defined across all environments? Assuming the entire environment has a low-dimensional state space, I’m curious how it computes the difference between states (Eq. 3) and infers the null state (Eq. 4) in a high-dimensional case (e.g., image).
  + From my understanding, inferring the null state should have a complexity of $O(n^2)$ based on state dimensionality, which may limit scalability in high-dimensional state spaces. However, L263 mentions a time complexity of $O(1)$. Could the authors clarify this?
  
- **Dependence on hyperparameters**
  + The method distinguishes null states based on prediction error (Eq. 3), but setting this hyperparameter could vary depending on environments and tasks.
  + Moreover, certain states, even within an environment or task, may have more complex dynamics than others. In such cases, how does the method define a single $\epsilon_{null}$?

### Questions
- While the authors use a learning-based dynamics model to infer the interaction, it can be clearly distinguished from existing work that utilizes other approaches. For example, [1] utilizes proprioceptive state changes to distinguish contact.
- The explanation of mixture distribution on L189 wasn't clear. How could it mix two distributions with a multiplication factor?
- The discussion on the limitation of this work can make readers better understand of the method. For example, authors can mention the domain where interaction is actually prohibitive (e.g., drone navigation)

#### Minor typo
- I believe L187 should be $d_{\pi}$

### References
[1] Manuelli and Tedrake, "Localizing external contact using proprioceptive sensors: The Contact Particle Filter"

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
3

### Summary
This paper considers a notion of null counterfactual: a cause object is interacting with a target object if in a world where the cause object did not exist, the target object would have different transition dynamics. Using this definition, the paper proposes ways to simulate virtual rollouts and perform data augmentation by leveraging null counterfactual. Hindsight Experience Replay is playing a key role in the algorithm, and the algorithm seems to inject some compositionality into hindsight replay. Toy tasks and robotic tasks are considered for evaluation.

### Strengths
- The notion of null counterfactual is interesting.
- The paper manages to devise a full-algorithm from this notion, and showed practical gain in object-centric robotic domains.
- Goal-conditioned RL is an important area of research, and using null counterfactual for data augmentation is a promising direction.

### Weaknesses
 - This method seems relatively limited to object-centric domains, where the dynamics between objects is relatively simple.
- Certain set-based architecture (such as PointNet and some version of GNN) might not work in general domains to model dynamics.
- The simulated nulling procedure and the filter criterion feel very heuristic and specific to the considered domains.

### Questions
See the weakness sections.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In the context of goal-conditioned RL, building on top of Hindsight Experience Replay, the paper proposes a filtering method that aims to improve the efficiency of learning. Under the proposed definition of interaction that is based on the change of the transition probabilities under null counterfactuals, a masked forward dynamic model is learned to identify interaction (NCII). Then the method filters the trajectory to be relabeled and only keeps those that the agent interacted with the target (NInt). The effectiveness of NCII and the improvements of NInt are verified by empirical analysis on simulated environments compared with established methods.

### Strengths
The problem setup is well motivated and the proposed algorithm extends , HER, an important technique in goal conditioned RL, to settings where it doesn’t work well and is effective. The presentation from the background of HER to the proposed method is smooth and well thought out, except a few minor places that can use some polish.

### Weaknesses
1. The null operation in Equation 3 depends on the threshold \( \epsilon_{\text{null}} \). This is an important part of the algorithm. Discussion on how to choose it and an ablation on the sensitivity of this threshold would make the analysis more comprehensive. More specifically we are interested in answering the following questions (actionable feedback below):
   - How sensitive is NCII to the choice of the threshold?
   - Does one threshold work across different environments in Table 1, or does each environment variant require a different threshold?
   
 Figures showing how the accuracy of HCII varies corresponding to a range of thresholds for environments, or one variant from each environment the authors already considered Table 1, would be compelling. Additionally, for a few selective environments that are sensitive to thresholds in the previous ablation, how does the episode reward change when HCII with different thresholds is used in HInt? This second ablation may not be necessary if HCII is shown to be robust across a range of thresholds in the previous one. The range of thresholds should be selected by the authors to show if there are values on the left or right tail where the algorithm starts to break down and success rates start to fall off. Success rate is the metric. 

2. Hindsight Experience Replay (HER) is an important baseline here. HER has several variants for how the goal is chosen, including “future,” “final,” and “episode.” It seems that, but it’s not clear, the HER implementation here refers to the default “final” variant. Expanding the baseline in Figure 4 to include other variants of HER, especially both the “final” and “future” variants, would make the comparison more comprehensive. This is particularly relevant as the performance difference between HInt and HER is small in a few environments in Figure 4, and a stronger variant of HER might change the gap here. This would entail running on the environments in Figure 4 and reporting on the already established metric, only this time under the alternative versions of HER goal selection strategies. 

3. In Equation 3, it appears that the logarithm is intended to apply to the entire subtraction; however, the syntax suggests otherwise.

4. There is a typo on line 268, page 5: “using using.”

### Questions
1. On page 5 around line 221, how exactly does the extra action column work with the core \( n \times n \) submatrix corresponding to the states? It appears that the interaction is defined around a pair of states. I also have the same confusion with Figure 2.

2. On page 5 around line 232, the mentioning of the vector \( \mathbf{V}^k \) would need more context. It seems to be a vector to zero out a column of the interaction matrix \( \mathbb{B} \), but it is not very clear. How is it related to, and what exactly is the property that not all tasks exhibit on line 233?

3. How should we deal with cases when there are very few trajectories satisfying the interaction criterion?

4. In Table 1, it is listed as accuracy, but it seems like lower values are better, which is a bit confusing.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes Hindsight relabeling using Interactions (HInt), a variant of Hindsight Experience Replay (HER) that leverages interactions to filter candidate trajectories for relabeling. Drawing inspiration from causality, an interaction is defined as an instance where removing (or nulling) an object would have an impact on the next state of another object (Null Counterfactual Interaction Inference or NCII). Given object-centric representations, the paper proposes to learn a masked dynamics model which can predict the next state of an object conditioned on what other objects are present. An influence of object A on object B is then detected by comparing the difference of the predictions for B with and without A against a threshold. During training, interaction detection is amortized in an interaction classifier. The main proposed criterion for using a trajectory for HER is the detection of a path in the unrolled graph corresponding to interactions, leading from an action to a target object (hence, an influence of the action on the target object). Experiments in two abstract and three robotics-inspired continuous control domains show increased sample efficiency when using HInt. An analysis suggests that HInt filters out trajectories in which the target object does not move (in the Spriteworld domain).

### Strengths
The argument for an interaction-based inductive bias in HER is well motivated. Moreover, the interpretation of a deviating transition probability under a null counterfactual as an interaction between objects is intuitive and concise. The existence of a path from an action to the target state as a filtering criterion for HER is well founded in causality and illustrated well by figure 2.

The domains considered for the experimental evaluation are relevant and sufficiently established. Table 1 indicates that NCII is more accurate in detecting interactions than the considered baselines. The RL performance is demonstrated to benefit significantly from using HInt.

The writing in the main text is clear and the presentation is well structured.

### Weaknesses
In my opinion, moving too much crucial algorithm components to the appendix is a main weakness of the paper. The main text conveys the impression that it presents the whole algorithm except for some unimportant implementation details, and that this algorithm achieves good performance in practice. However, the content of Appendix C and especially Appendix D seem to be quite important, and are probably crucial for obtaining the empirical results that were reported.

In particular the filtering criteria presented in Appendix D deviate from the intuitive path-from-action-to-target definition in the main text. Moreover, a somewhat simplified and engineered criterion is then used for the experiments. Yet, it is only referred to as one of several “alternatives” in the main text (line 318). In my opinion, it should be made more clear what form of the algorithm is actually used for the experiments and which components are crucial for obtaining good performance. An ablation study with different filtering criteria would be interesting, for example.

My understanding, based on the last paragraph of appendix D, is furthermore that for the experiments, only interactions between the controlled object and the target object were detected and used as a criterion. This is a much simpler algorithm than what is presented in the main text and effectively uses domain knowledge (as it happens to be sufficient to consider such interactions in the chosen domains). Moreover, another hyperparameter thresholding the interaction frequency in a trajectory is introduced. Combined, this makes me question the claim that NCII is really more general than using heuristics (line 87).
As the algorithm used in the experiments is considerably simplified, it seems like running CAI [1] as a baseline is required. CAI simply estimates the influence of actions on the target object. It would be interesting to see how much HInt can add in terms of sample efficiency to this approach.

The content of Appendix C reads like quite a few tricks were needed to get HInt to work well. In particular the reweighing based on the log probability of a transition seems important and should therefore be mentioned in the main text.

The writing in Appendix D is sometimes a bit dense and hard to understand, for example the enumeration point “1. Non-passive”. I think there is potential for illustrating these strategies better.

### Questions
* It would be interesting to see wall-clock time comparisons with the baselines as HInt adds quite a bit of complexity to them.

* I would have expected an expectation over the goal in the RL objective in like 181.

* The next paragraph (starting from line 183) is written like the goal space is equal to the state space. However, in the rest of the paper this is not the case.

* ‘min’ in equation (2) should be ‘max’.

* Why is no absolute value taken in equation (3) when thresholding the difference of log probabilities.

* In line 303, the filtering function is defined is defined as a decision to reject a trajectory while in appendix D it seems to be the decision to accept a trajectory.

* I think (left) and (right) are switched in the caption of Figure 1.

### Soundness
3

### Presentation
3

### Contribution
3

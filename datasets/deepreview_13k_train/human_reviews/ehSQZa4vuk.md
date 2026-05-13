# Bad Habits: Policy Confounding and Out-of-Trajectory Generalization in Reinforcement Learning

- Decision: Reject
- Scores: 6, 5, 5, 5

## Abstract
Reinforcement learning agents may sometimes develop habits that are effective only when specific policies are followed. After an initial exploration phase during which agents try out different actions in the environment, they eventually converge on a particular policy. At this point, the distribution over state-action trajectories becomes narrower, leading agents to repeatedly experience the same transitions. This repetitive exposure can give rise to spurious correlations. Agents may then pick up on these correlations and develop simple habits that only work well within the specific set of trajectories dictated by their policy. The issue here is that these habits can result in incorrect outcomes if agents are forced to deviate from their typical trajectories due to changes in the environment or in their policies. In this paper, we provide a mathematical characterization of this phenomenon, which we refer to as policy confounding, and show, through a series of examples, when and how it occurs in practice.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The phenomenon of "policy confounding" is identified, where an RL agent may learn to discard important information in the state due its policy focusing only on some small subset of states. Some theory is developed to understand conditions where the effect may arise and experiments in toy domains illustrate the identified phenomenon.

### Strengths
The phenomenon of "policy confounding" is intriguing and novel. The presentation of the paper is great, the text is easy to follow and the figures are clear. Explanations are given in sufficient detail. 
There are interesting connections made to a causality perspective and the theoretical framework used (considering a factored MDP) is well-chosen. The experiments clearly demonstrate the effect in a few illustrative environments.  

Overall, I find the main idea of paper to be very interesting and potentially relevant in many situations where RL agents are trained.

### Weaknesses
 The primary weakness is that the experiments focus on toy examples specifically designed to elicit the problem. It's not entirely clear if this problem is relevant in more realistic settings. Appendix C does contain examples of failures from previous works which may be related to policy confounding though.

A slight weakness is that no mechanisms outside of conventional strategies (e.g. experience replay) are proposed to address policy confounding.

### Questions
I'd be willing to increase my score based on the responses to the following questions. 

- T-Maze, sec2. It could be more clear to mention why the avg return is around 0.2. Is this around the level that is to be expected? Why is there a little bump around step 30k for the eval env? 

- As an alternate demonstration, instead of adding the ice to the environment, why not simply place the agent directly on the state above (or below) the original starting location and see how it fares on the train env? Then, it would clear to see that if the agent always follows the trajectory it expects instead of using the color signal. We wouldn't need to introduce this additional mechanism of the ice or modify the transition function.

- About the formal definition (def 9) of policy confounding:
	It would be helpful to understand this definition by explaining how it applies to the T-maze.
	Could you clarify the meaning of the do() operator here from a mathematical point of view? 
	Would it be the same as writing that the equality has to hold for all $s_t$ s.t. $\phi(s_t)$ rather than only the ones visited by $\pi$? 

- About "Narrow trajectory distributions". If the environment transitons leads to a diverse set of states, would we still observe policy confounding? What if the agent is incentivized to explore through exploration bonuses? Could this avoid the issue?

- The paper makes a link between policy confounding and causality (or lack of it). Are there any tools from causality that could be used to address the problem?

-  Is policy confounding inevitable to some extent? It seems to be a consequence of having policies focus on certain parts of the state space.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors discuss policy confounding, the phenomenon where RL agents rely on spurious correlations for their policies.  They define and study this problem from a theory standpoint, and empirically evaluate several proposed solutions.

### Strengths
This is an interesting, significant topic that is worthy of study, and I think that, issues below aside, authors have a solid approach to the problem.

### Weaknesses
See questions below for a couple of clarity weaknesses.

In Example 1 (Section 6), X_t and x_t seem to not be defined when they are first used.  Later, it is stated that X_0 is the signal received at t=0, but even then, it is not clear how X differs from G.  These should be better defined. Specifically, it's unclear if X_t is a random variable, a specific value, or a set. The relationship between X_t and the goal G at different time steps needs clarification. Is X_t a function of G, or are they independent? The description implies X_0 is related to G at the start location, but this relationship is not formally defined for subsequent time steps. The lack of a clear definition of the domain and range of X_t and its connection to G makes it difficult to understand the example.

The do operator is not well-defined.  Based on the informal description (just below Definition 9), I thought that it meant that there exists an s_t, such that we consider all possible values of Phi(s_t), and adversarially pick one to try to meet one of the conditions in Definition 9 if possible (even if this is the correct interpretation, it is not clear).  However, based on a few readings for Section 6.0, I suspect the correct interpretation is something different. The description of the do operator lacks the necessary precision for a formal definition. The idea of 'setting the variables' is vague; it's not clear how this setting is implemented or what it means for the state space. The connection between the do operator and the equivalence class {s_t}^Phi is also not clear. It seems like the do operator should manipulate the state representation, but the exact mechanism is missing.

It is not clear to me how exactly Example 1 corresponds to the ideas before and after it (perhaps this confusion would be resolved by resolving the confusions above).  The implication appears to be that the two different L_8 positions under the optimal policy (i.e., the green and purple positions in Figure 1) are equivalent under some Phi.  But, per Definition 3, this is not how state representations work: we can discard some subset of the state to get our state representation, but I do not see how the two different L_8 positions can have the same state representation per that definition.  So either I am misunderstanding the implication (possibly due to the clarity problems mentioned above), or else there might be a fundamental error in the example or the definitions. The example seems to suggest that different physical locations can have the same state representation, which contradicts the idea that state representations are derived from the underlying state. The example needs to clearly show how the state representation is constructed and how it leads to the observed policy confounding. The connection between the state representation and the observed behavior is not well-established.

Another possibility that may explain some of my confusion is that L_t and l_t do not encode the full position, but instead only the timestep or the “horizontal” position.  If this is the case, this confusion is caused by more imprecise/incomplete definitions. The paper does not explicitly state the dimensionality or the information encoded by L_t and l_t. If L_t only encodes the timestep or a partial position, this needs to be stated clearly. The lack of clarity on the encoding of L_t and l_t makes it difficult to understand the state space and the state representation.

Justifying/motivating the work: The examples given focus on the idea that we train on one MDP, and then evaluate on another.  This approach illustrates the issue well, but is too contrived to provide motivating examples that show why we should care about policy confounding in practice (and the experiments are all set up this way as well).  6.2 attempts to address this by discussing when we should worry in practice: function approximation and narrow trajectory distributions.  However, these two paragraphs are far too short and high-level to truly justify this work.  I believe that this is an interesting topic worthy of study, but I think this paper in its current form does a poor job of showing the reader that this is an interesting topic worthy of study.  Perhaps showing that policy confounding can be a problem in less contrived settings (for example, when the MDP or distribution of MDPs does not shift between training and evaluation) would help address this weakness.  Alternatively, another approach could be to focus a future version of the paper on a setting where the training and evaluation MDPs are inherently different, such as "sim-to-real" robotics.

The main theorem seems almost trivial, and the empirical work is based on extremely simple toy gridworlds.  So even aside from the issues above, the contribution may be a bit light.

### Questions
Starting at definition 2, the paper became difficult to follow.  Are \Theta^1, \Theta^2 random variables (RVs)?  For a while, I couldn’t figure out what they were (I was thinking that they were sets like \Theta, but that didn’t make complete sense, and then I was thinking that there must be typos in the definition, before I realized that they might be RVs).  If they are RVs, a statement that they are RVs, as opposed to \Theta, which is a set, would be helpful.

The \cross_i notation was extremely confusing (I almost gave up on trying to understand the paper over this).  The interpretation I settled on for \cross_i dom(\Theta^i) is dom(\Theta^1) \cross dom(\Theta^2) \cross …  Is this interpretation correct?  A definition would help clarify.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors investigate if RL agents develop myopic, suboptimal habits that rely on spuriously correlated inputs to make decisions. They formally define policy confounding by considering minimal representations of a policy's marginal state distribution, and then showing that these minimal representations do not generalize, like if the policy gets teleported to a state outside of it. They evaluate on toy gridworld settings where confounding happens, and show that some strategies that increase the diversity of data experienced by the agent (off-policy, exploration, etc.) reduces confounding.

### Strengths
The study of generalization for RL is quite important.
The study of the training dynamics of deep RL is also quite important. 
This paper addresses both such problems, since policy confounding can happen both during training and evaluation.

Overall, I appreciated the theoretical definition of policy confounding, and find the way the authors choose to define it by considering the representations induced by a policy to be intuitive. However, there are several writing issues (see below) that I fear will make this paper's message miss the mark.

The experiments the author chose, while toy, highlight the policy confounding problem well. The proposed improvements, while not novel, are simple and intuitive for tackling confounding.

### Weaknesses
## Presentation
Overall, the paper is very awkward for reading. The authors propose many definitions and setup notations in the early pages before finally arriving to the definition of policy confounding (Sec. 6). I would suggest for the authors to reformat the paper to first give a high level sketch or intuition of the definition, perhaps aided by a visual figure, and then explaining the numerous notations and definitions required for defining policy confounding.

In section 2, the authors provide a very lengthy (almost page long) textual description of policy confounding. This is very difficult to read, I would advise the authors to move explanations into visual aids, split up into paragraphs, highlight key steps, etc. The current presentation buries the key insights within a wall of text, making it difficult to grasp the core concepts quickly. The section introduces the T-Maze environment and the confounding problem simultaneously, which overloads the reader with too much information at once. The key environmental properties, such as the deterministic nature of training and the disjoint optimal paths, are not emphasized, and are lost in the detailed description. This makes it hard to understand why the agent's behavior is problematic.

Indeed, the authors have a tendency of writing long paragraphs and describing things step by step at a low level, rather than summarizing high level points, splitting points into multiple paragraphs, etc.  Section 6, Example 1 is almost impossible to read. I suspect most readers will not even bother reading this. The example is presented as a single, dense paragraph, making it hard to follow the logical flow and identify the key points. The low-level details obscure the high-level insights about how policy confounding manifests in this specific scenario.

## Experimentation
The authors can improve in two ways. First, they can connect their theory more to their toy experiments. For example, is it possible to come up with a toy environment where all possible representations can be enumerated and tracked? Then it could be interesting to see what kinds of representations RL algorithms learn, and if they indeed are minimal and do not generalize.

Next, it would be interesting to investigate confounding in existing deep RL tasks, especially in well-known benchmarks (Atari, DMC, etc.), and to see if some RL algorithms are better than others. For example, would MBRL algorithms fare better or worse than model-free RL algorithms?

### Questions
Can the authors improve the presentation? 

Can the authors think of experiments that analyze and connect to their theory more? 

Can the authors showcase policy confounding in non-toy tasks in deep RL (continuous states, actions, well-known benchmark, etc.)?

### Soundness
3 good

### Presentation
2 fair

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
The paper addresses the issue of spurious correlations in reinforcement learning (RL), introducing the concept of policy confounding to formalize and analyze this problem. The authors provide theoretical insights, examples, and experimental results to demonstrate the effect of policy confounding, comparing different solutions and highlighting its impact on state representations in RL. The work aims to shed light on how an agent's policy can induce spurious correlations, potentially leading to representations that do not generalize well outside the trajectory distribution induced by the agent's policy.

### Strengths
The paper introduces and formalizes the concept of policy confounding, shedding light on a previously underexplored aspect of spurious correlations in RL. The theoretical framework, complemented by some examples, enhances our understanding of how policy confounding impacts state representations in RL. The manuscript is well-structured, providing a logical flow of ideas, and the writing is clear, making complex concepts accessible.

### Weaknesses
The paper argues policy confounding poses a distinct challenge from general RL generalization, but does not extensively benchmark against recent generalization methods like invariant risk minimization, data augmentation, dynamics randomization, robust policy learning, and meta RL. These approaches could be highly relevant given the claims about out-of-trajectory generalization. While theory and simple experiments demonstrate policy confounding, how confident are you this poses a problem not already addressed by the latest techniques for improving generalization in RL? Comparisons to some of these state-of-the-art methods, particularly those focused on out-of-distribution robustness, are needed to better situate the claims within the broader context of research on robustness and generalization. The lack of empirical comparison makes it difficult to assess the practical significance of policy confounding relative to existing challenges.

You demonstrate policy confounding in simple domains. Do you have evidence this manifests in more complex, high-dimensional problems? Testing on complex benchmarks, such as those used in the Atari suite or MuJoCo environments, could better showcase the significance and practical relevance of the identified issue. The current experiments, while illustrative, do not demonstrate that policy confounding is a significant problem in more realistic scenarios. The absence of such evidence limits the impact of the paper.

The theoretical analysis introduces useful formalisms but is very dense. For readers less familiar with this notation, could you provide more intuitive explanations of key results like Proposition 1 and Theorem 1? The current presentation makes it challenging to grasp the core insights without significant effort. The lack of clear, intuitive explanations limits the accessibility of the theoretical contributions.

While you propose some basic mitigation strategies, the paper does not offer concrete solutions. What directions seem most promising for future work to address policy confounding? The current discussion of mitigation strategies is high-level and lacks specific, actionable recommendations. The paper would benefit from a more detailed exploration of potential solutions.

The distinction between out-of-trajectory and out-of-distribution generalization is somewhat unclear. Could you clarify this difference with explicit examples? The current explanation is not sufficiently clear, making it difficult to understand the precise scope of the policy confounding problem.

How does policy confounding relate to prior work on spurious correlations and generalization in RL? Are there clear differences in causes and solutions? The paper does not adequately discuss the relationship between policy confounding and existing work on spurious correlations, making it difficult to understand the novelty of the proposed concept. A more thorough comparison is needed to clarify the contribution.

You cite causal representation learning as a promising direction for future work, but do not provide specifics on how these techniques could be applied to address policy confounding. Could you expand on how invariant risk minimization or other causal inference tools could help mitigate the effects you demonstrate? Are there any concrete steps you propose for integrating causal representations into solving this problem? The current discussion of causal representation learning is vague and lacks concrete suggestions for how to apply these techniques to the problem of policy confounding.

### Questions
The paper argues policy confounding poses a distinct challenge from general RL generalization, but does not extensively benchmark against recent generalization methods like invariant risk minimization, data augmentation, dynamics randomization, robust policy learning, and meta RL. These approaches could be highly relevant given the claims about out-of-trajectory generalization. While theory and simple experiments demonstrate policy confounding, how confident are you this poses a problem not already addressed by the latest techniques for improving generalization in RL? Comparisons to some of these state-of-the-art methods could better situate your claims within the broader context of research on robustness and generalization.

You demonstrate policy confounding in simple domains. Do you have evidence this manifests in more complex, high-dimensional problems? Testing on complex benchmarks could better showcase significance.

The theoretical analysis introduces useful formalisms but is very dense. For readers less familiar with this notation, could you provide more intuitive explanations of key results like Proposition 1 and Theorem 1?

While you propose some basic mitigation strategies, the paper does not offer concrete solutions. What directions seem most promising for future work to address policy confounding?

The distinction between out-of-trajectory and out-of-distribution generalization is somewhat unclear. Could you clarify this difference with explicit examples?

How does policy confounding relate to prior work on spurious correlations and generalization in RL? Are there clear differences in causes and solutions?

You cite causal representation learning as a promising direction for future work, but do not provide specifics on how these techniques could be applied to address policy confounding. Could you expand on how invariant risk minimization or other causal inference tools could help mitigate the effects you demonstrate? Are there any concrete steps you propose for integrating causal representations into solving this problem?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

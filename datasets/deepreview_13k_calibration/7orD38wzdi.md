# Ego-centric Learning of Communicative World Models for  Autonomous Driving

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 6, 6, 3

## Abstract
We study multi-agent reinforcement learning (MARL) for tasks in complex high-dimensional environments, such as autonomous driving. 
MARL is known to suffer from the *partial observability* and *non-stationarity* issues. To tackle these challenges, information sharing is often employed, which however faces major hurdles in practice, including overwhelming communication overhead and scalability concerns. Based on the key observation that world model encodes high-dimensional inputs to low-dimensional latent representation with a  small memory footprint, we develop  *CALL*,  {C}ommunic{a}tive Wor{l}d Mode{l}, for ego-centric MARL, where  1) each agent 
first learns its world model that encodes its state and intention into low-dimensional latent representation which can be  shared with other agents of interest via lightweight communication; and 2) each agent carries out ego-centric learning while exploiting lightweight information sharing to enrich  her world model learning and improve prediction for better planning. We characterize the gain on the prediction accuracy from the information sharing and its impact on performance  gap. Extensive experiments are carried out on the challenging local trajectory planning tasks in the CARLA platform to demonstrate the performance gains of  using *CALL*.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes incorporating the world model into the multi-agent communication protocol to address the partial observability and non-stationarity issues in multi-agent reinforcement learning (MARL). In particular, this paper provides theoretical justification for how partial observability and non-stationarity can affect the world model performance. It derives the prediction-accuracy-driven information-sharing strategy for better communication. The paper shows the performance of its method in the autonomous driving setting.

### Strengths
- The paper is clear and well-written. It is very easy for me to follow.
- I like the theoretical analysis and how it can inform a better communication strategy.
- It provides the experimental results on how the method can help to solve the two issues in MARL.

### Weaknesses
 - This paper needs a comparison with other baselines (see Table 2) in your experiment result. Why is your proposed method superior to others? It is insufficient to show that you have specific components that others don't. The empirical results are essential to show that the method is effective.

- The experiment setting is limited. How would this method perform in other experiment settings besides CARLA?

### Questions
I suggest having a deeper analysis of your information-sharing mechanism in your experiment. I am curious: if your information-sharing mechanism is replaced by another mechanism, how would the performance change?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper tries to tackle the issues of partial observability and non-stationarity in multi-agent reinforcement learning (MARL) tasks in complex environments by developing a decentralized and adaptive communication pipeline. Verbatim from the paper, the authors presented an approach to answer: “How to synergize world model’s generalization capability with light-weight information sharing for enhancing ego-centric MARL in high-dimensional, non-stationary environments?”

The authors work on top of the Dreamer V3 architecture to learn a world model (WM) for compressing the sensor information and for learning the transition dynamics.
For light-weight communication, the authors propose to use the compressed latent representations to predict the next transitions and also to share the other agent’s latent state and latent intentions (waypoints).

They call this framework CALL (Communicative World Model), where every agent shares its latent state and intention (encoded using a learned WM) and tries to improve their WM by adaptive and effective sharing of information. This adaptive sharing of relevant latent information helps minimizing communication overhead and improves decision-making.
The authors presented some theorems and propositions to manifest how WM can improve the prediction performance and reduce sub-optimality gap.

### Strengths
- The paper tried to explain how prediction error can control the sub-optimality gap and present an upper bound on both these entities. 

- The paper did a good ablation study (both in terms of experiments and theoretically) to investigate the impact of insufficient information sharing, locally sufficient information sharing, latent information sharing and full observation sharing.

- The authors presented the numbers of how much the bandwidth can be improved using the latent representations for information sharing.

- The paper has experiments to show that WM generalization combined with information sharing is an effective	component to improve prediction in distributed RL in high-dimension environments.

### Weaknesses
 - The definitions, formulations, introduction of notations can be made a bit more coherent.

- Uncertainty related to information sharing was not discussed and taken care of in the paper and was mentioned as one of the problems in the introduction section as well. Specifically, the paper lacks a formal treatment of how uncertainty in the latent space affects the prediction and decision-making process. The method relies on a threshold for communication based on prediction error, but it does not address the inherent uncertainty in the predicted latent states and intentions themselves. This could lead to suboptimal communication strategies, where agents might share information that is not reliable or relevant due to high uncertainty in their own latent representations.

- The authors also mention privacy-preserving techniques can also be integrated during information sharing to prevent any sensitive information being leaked. However, the paper does not provide any concrete mechanisms or analysis of how such techniques could be implemented without compromising the performance of the proposed framework. The discussion on privacy is very high-level and lacks any technical depth.


### Questions
- Fig 1: Where is a_{1, t} and a_{2, t} coming from? I assume we can also have the notation for the policy from which these actions are getting sampled from.

- Fig1: Can we have the symbol for encoder be replaced by the conventional trapezoid? The current symbol gives an impression of a combined enc-dec model.

- Line 314: Can we please define PPAD?

- Line 318: Is that extra closing bracket here T_{i,t}) a typo?

- Line 377: ….3D environment…..: missing space after environment.

- Algorithm 1: Line 384: How is the communication range updated? Is there any update formula for that?

- Nit: Line 1322: “Large” could be made to “large”? 

- Can we call this similar/analogous to the unification of trajectory prediction and planning task where the next best action during planning is conditioned on the predicted trajectories of other agents; here, the latent intention (encoded waypoints) are provided as information that is used to predict the state dynamics?

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
3

### Summary
This paper presents CALL (Communicative World Model), a framework for addressing partial observability and non-stationarity challenges in multi-agent reinforcement learning (MARL) in high-dimensional environments. The key innovation lies in synergizing world models' generalization capabilities with lightweight information sharing. Each agent encodes its state and intentions into low-dimensional latent representations and selectively shares them with other agents based on prediction accuracy. The approach is theoretically analyzed and validated on the CARLA autonomous driving platform.

### Strengths
The paper makes several significant contributions to multi-agent reinforcement learning. The core innovation of synergizing world models with lightweight communication is both novel and practical, addressing two fundamental challenges in MARL: partial observability and non-stationarity. The technical approach is well-grounded in theory, with Theorem 1 providing a detailed analysis of prediction error structure and Proposition 1 establishing bounds on sub-optimality gaps. The implementation is particularly impressive, demonstrating substantial performance improvements in the CARLA autonomous driving platform - reducing communication bandwidth from 5MB to 0.11MB while increasing success rate from 52% to 87% (Table 5). The ablation studies thoroughly validate each component's contribution, and the method shows good generalization to unseen environments. The practical relevance of the work is clear, with the framework successfully handling realistic scenarios involving up to 250 vehicles while maintaining reasonable computational requirements.

### Weaknesses
1. The experimental validation is confined to autonomous driving scenarios, raising questions about generalizability
2. Lack of comparisons with state-of-the-art MARL methods is a significant omission. Specifically: No comparison with recent methods like QMIX, MADDPG, or other communication-based approaches; No evaluation on standard MARL benchmarks; Missing comparison with other world model-based methods
3. The ablation studies, while thorough for the proposed components, don't explore alternative design choices
4. The world model training process is not fully described in the main text: 1) Missing details about the training curriculum; 2) Unclear how the model handles different types of sensory inputs; 3) Limited discussion of failure cases and their analysis
5. The prediction-accuracy-driven communication mechanism needs more elaboration: 1) The threshold selection process is not well-explained; 2) The adaptation mechanism for the communication range isn't fully specified; 3) Missing analysis of communication overhead in different scenarios
6. The bounds in Theorem 1 might be loose, and there's no discussion of their tightness: 1) No lower bounds are provided for comparison; 2) The analysis assumes finite action spaces, limiting generality; 3) The impact of approximation errors isn't fully analyzed
7. Missing formal analysis of communication complexity: 1) No theoretical guarantees on the optimality of the information sharing strategy; 2) Limited analysis of the trade-off between communication cost and performance

### Questions
1. How is the prediction accuracy threshold c determined? Is it static or dynamically adjusted?
2. How does the system handle communication delays and packet losses in practice?
3. What's the maximum number of agents the communication protocol can efficiently handle?
4. Are the bounds in Theorem 1 tight? Can a lower bound be provided?
5. How does the finite action space assumption affect application to continuous action spaces?
6. Can the theoretical analysis be extended to handle heterogeneous agents?
7. Why weren't standard MARL benchmarks included in the evaluation?
8. Can performance comparisons with methods like MADDPG or QMIX be provided?
9. Is 250 vehicles the scalability limit? What's the performance in larger-scale scenarios?
10. What are the computational requirements for training the world model?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper developed CALL, Communicative World Model, for ego-centric MARL. The CALL allows agents to adaptively adjust their information sharing based on real-time evaluation of their prediction accuracy, and reduce unnecessary information transmission and improve system efficiency.

### Strengths
**Pros:**

1. Theoretical Support

The article provides theoretical analysis proving the impact of prediction errors on sub-optimality gaps and demonstrates the effectiveness of the CALL method through experiments.

2. Experimental Validation

Extensive experiments were conducted on the CARLA platform for trajectory planning tasks, showing that the use of CALL can significantly improve performance, particularly in lightweight communication scenarios.

### Weaknesses
 **Cons:**

1. Inaccurate Description of Literature

The article states: “Recent works on WM-based reinforcement learning still face significant limitations, and often rely on rigid, static information-sharing mechanisms, such as sharing information with all agents (Pretorius et al., 2020), using centralized frameworks (Krupnik et al., 2020; Pan et al., 2022; Liu et al., 2024).” In fact, Pan et al. (2022) and Liu et al. (2024), among others, learned and planned in the latent space. Therefore, lightweight information sharing is not unique to this paper, as most related works do this. The core issue is not whether latent representations are used, but rather the specific communication architecture. Many existing methods, despite using latent spaces, still employ centralized or static communication schemes, which this paper fails to adequately distinguish itself from.

2.  Questions about Scalability and Adaptability

The method described in the article establishes a world model for each agent. Since it sets the parameters and number of models beforehand, the method cannot adapt to changes in the number of agents during training or testing, especially during testing. Additionally, changes in the number of agents also change the observation dimensions for each agent, which the method cannot adapt to dynamically (dynamic changes in relevant information). When scaled up to large systems, the increase in the number of models and parameters with the number of agents leads to increased computational complexity and resource burden, thus limiting scalability. Although an experiment with 250 vehicles was conducted in Section E.3, there is no comparative analysis with the results from the experiment involving 150 vehicles, making it difficult to prove its good scalability. The core issue is that the method does not address the fundamental challenge of how to maintain performance when the number of agents, and thus the dimensionality of the observation space, changes dynamically. The method's reliance on a fixed number of models and parameters is a significant limitation.

3. Latent Intention

 There is no description of the definition and learning method of latent intention throughout the paper. Moreover, equations 11-13 also do not have terms related to informations T and latent intentions w.  Therefore, how to infer and learn these latent intentions? The paper lacks a clear explanation of how intentions are represented, learned, and integrated into the model's dynamics. The absence of explicit terms in the equations further obscures this process.

 4. Comparative Experiments

  There is a lack of comparative experiments with related methods, such as those by Pretorius et al. (2020), Krupnik et al. (2020), Pan et al. (2022), and Liu et al. (2024). The paper should include comparisons with other state-of-the-art methods, even if they are not directly in the autonomous driving domain, to demonstrate the method's relative performance. The absence of such comparisons makes it difficult to assess the true contribution of the proposed method.

5. Experimental Verification of Accumulative Error in Multi-step Prediction

 Although the method theoretically proves its effectiveness, there is a lack of direct experimental verification. Specifically, there are no curves showing the relationship between the number of prediction steps and cumulative error, comparison curves of cumulative error with other methods, or performance change curves at different prediction step numbers. The paper needs to provide empirical evidence of how prediction error accumulates over multiple steps and how this affects overall performance. This is crucial for validating the theoretical claims.

6.  Prediction Accuracy-Driven Information Sharing

The article claims that CALL allows agents to adaptively adjust their information sharing based on real-time evaluation of their prediction accuracy. However, the specific mechanism of how the method adjusts information sharing according to prediction accuracy has not been experimentally verified, i.e., there are no graphs showing the relationship between prediction accuracy and information sharing (T). The paper lacks empirical validation of the adaptive information sharing mechanism. It needs to demonstrate how prediction accuracy influences the amount of information shared and how this impacts overall performance.

### Questions
See the weakness  for Questions. 

**Suggestions for Improvement:**

1. Improve the accuracy of literature description  

2. Define intention clearly and explain learning mechanism
   
3. Add comparative experiments.

4. Supply experiments concerning accumulative errors in multi-step prediction and relationship between prediction accuracy and information (T)

### Soundness
2

### Presentation
3

### Contribution
2

# CLEAR: An Information-Theoretic  Framework for Distraction-Free Representation Learning in Visual Offline RL

- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 6, 5

## Abstract
Visual offline RL aims to learn an optimal policy for visual domains, solely from the pre-collected dataset comprised of actions taken on visual observations. Prior works on visual RL typically learn a dynamics model by extracting a latent state representation. However, the learned representation would contain factors irrelevant to control when there are distractions in the visual observations. These nuisance factors introduced by the distraction further exacerbates the difficulties of learning a good policy in the offline RL setting. In this work, we formalize the visual offline RL setting as a Partially Observable Markov Decision Process with exogenous variables (ExoPOMDP) and identify  these problems with previous approaches under an information-theoretic lens. To overcome these challenges, we propose CLEAR (**C**ontrollable **L**atent State **E**xtr**A**cto**R**) for visual offline RL, which learns the dynamics model of a succinct agent-centric state representation that is consistent with the underlying ExoPOMDP. We empirically demonstrate that CLEAR is able to outperform baselines on the DeepMind Control Suite with various types of distractions and perform consistently well across these distractions. We further provide qualitative analysis on the results showing that our approach successfully disentangles the distraction factors from the agent-centric state representation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper aims at disentangling distractions in the visual observations from agent-related information for visual offline RL tasks. To this end, the paper formalizes the visual offline RL setting as an ExoPOMDP and derive the corresponding objective with the tools of information theory. Specifically, the disentanglement is achieved by a VAE-like model, where the decoder network has a compositional architecture that blends the reconstructed foreground and background visual parts with masks.

### Strengths
- The idea is simple and effective.
- The experiments seem thorough on the DeepMind Control Suite.
- The paper is clearly written and well-organized.

### Weaknesses
 - I am admittedly not an expert of visual offline RL, and would like to hear my colleague reviewers' opinions on this.

### Questions
None

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper addresses the problem of visual offline reinforcement learning in settings with distractions in visual observations. The authors formalize this setting as an ExoPOMDP and propose CLEAR, a method that learns the dynamics model of a agent-centric state representation consistent with the ExoPOMDP framework. Specifically, they take an information-theoretic approach, introducing mutual information-based loss functions to disentangle distraction factors from the agent-centric representation. Their method is evaluated on three tasks in the DeepMind Control Suite with diverse types of distractions.

### Strengths
1/ The high-level motivation of the method and the information-theoretic foundation look solid. Specifically, the regularization term that encourages s_hat to encode an agent-centric state controllable by actions is particularly interesting, and its effectiveness is well supported by the experiments.

2/ They evaluate the methods on various types of distractions, with 2x2 grid distractions being especially notable. This setup serves as a great testbed for assessing whether a method can distinguish controllable parts from non-controllable ones. The experiments show that their method consistently outperforms other methods in this setting, indicating that the baselines lack the ability to discern controllability, while their method succeeds.

3/ Their experiments include a comprehensive set of prior work as baselines, covering not only offline RL but also model-based RL. This strengthens the paper by demonstrating that their method outperforms approaches across various frameworks.

### Weaknesses
1/ Three tasks from a single domain seem too few, particularly since some baselines are comparable to the proposed method in some tasks (e.g. InfoGating on Hopper Hop). Expanding the evaluation to include more tasks (e.g., 5-6 tasks) would significantly strengthen the paper. A larger set of tasks would provide a more robust assessment of the method's performance and demonstrate its versatility across different scenarios.

2/ Although a large set of prior works is presented as baselines, some important and closely related studies are missing. Notable examples include [1] and [2]. [1] also employs information theory to address controllability. A detailed comparison between [1] and CLEAR is necessary, both methodologically and experimentally. [2] leverages causality to learn disentangled representations across four different categories, focusing on controllability and reward relevance. The lack of a comparison with [2], especially given its publicly available code, is a significant oversight.


### Questions
1/ Which representation is used for offline RL (i.e., policy learning)? I assume s_hat is used and not e_hat, but I would like to clarify this.

2/ The method requires extensive hyperparameter search over the variance and balancing factors of the KL divergence for each task, domain, and distraction type (Table 9). It would be much more convenient to eliminate this necessity. Do you have any ideas on how to achieve this?

3/ Since the method aims to improve representation learning, it could potentially be applied within an MBRL framework. How do you think it would perform when integrated with an MBRL framework?

4/ How can this method handle other forms of nuisance information, such as color perturbations of task-relevant parts, where the assumption in L278 does not hold?

5/ Including more detailed descriptions of each column in the caption of Table 3 would make it much easier to interpret the results.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes CLEAR, an agent-centric state-representation method for vision-based offline reinforcement learning. The authors present an information theoretical approach to achieve this goal, disentangling exogenous variables while enforcing the Markovian properties. For computation, the author proposed a lower bound of compounded mutual information in Eq. (3) to  Eq. (4) and designed a corresponding encoder-decoder architecture that can be trained with image representation techniques. The authors demonstrated that learned state representations by the proposed CLEAR method show good performance when there is uncontrollable visual distraction in offline RL settings.

### Strengths
1. The paper is well-written. It was straightforward to understand the core idea; despite dealing with complex concepts. Figures and equations are appropriately placed. 
2. The proposed method is sound and properly designed to solve the offline RL problems. 
3. In the visual domain, circumstances that ExoPOMDP describes are very common. This work can directly contribute to solving RL in real-world problems. 
4. The authors have clearly put significant effort into reducing computation costs and simplifying architecture design. The work focus on enhancing efficiency and practicality of information theoretical approaches. I think most of the results could be implemented and reproduced even though source code is not provided.

### Weaknesses
1. Although the authors' claim primarily in the visual offline RL, the conducted experiments are strictly limited to MuJoCo variants. The authors are strongly encouraged to strengthen the experiment section by including (pure) vision-based RL problems with distractions. Specifically, while MuJoCo tasks with visual distractions are a good starting point, they do not fully represent the complexities of real-world vision-based RL. The visual distractions in MuJoCo are often synthetic and may not capture the nuances of real-world visual clutter, such as dynamic lighting changes, occlusions, and diverse object appearances. Therefore, experiments on more diverse and realistic visual datasets are necessary to validate the method's effectiveness in practical scenarios.
2. Extensibility. I think the adaptation ability of CLEAR representation for different visual distractions from the training environments is only partially validated by multiple videos. The authors are encouraged to analyze general extensibility of CLEAR in these aspects for real-world scenarios. The current evaluation primarily focuses on scenarios where the type of distraction is consistent across training and testing, with only the specific instance of the distraction varying. A more rigorous evaluation would involve testing the model's ability to generalize to entirely new types of visual distractions not seen during training. For example, if the model is trained with video distractions, it should be tested with distractions such as image overlays or dynamic lighting changes to assess its robustness.
3. It would be better if intuitive motivation or a toy experiment empirically verifies the ExoPOMDP setting. While the paper provides a high-level description of the ExoPOMDP setting, it lacks a concrete example or a toy experiment that demonstrates the practical implications of this setting. A simple experiment that isolates the effect of exogenous variables on the agent's state representation would be helpful in understanding the benefits of the proposed approach. This could involve a controlled environment where the agent interacts with a simple object while being subjected to different types of distractions, allowing for a clear visualization of how the CLEAR method disentangles the agent's state from the exogenous variables.

### Questions
1. In the graphical model in Fig 2, what happens when e_t is affected by s_{t-1}? Does this modification change Eqs. (2) and (3)?

### Soundness
3

### Presentation
3

### Contribution
3

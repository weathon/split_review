# World-Model based Hierarchical Planning with Semantic Communications for Autonomous Driving

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5

## Abstract
World-model (WM) is a highly promising approach for training AI agents. However, in complex learning systems such as autonomous driving, AI agents interact with others in a dynamic environment and face significant challenges such as partial observability and non-stationarity. Inspired by how humans naturally solve complex tasks hierarchically and how drivers share their intentions by using turn signals, we introduce HANSOME, a WM-based hierarchical planning with semantic communications framework. In HANSOME, semantic information, particularly text and compressed visual data, is generated and shared to improve two-level planning. HANSOME incorporates two important designs: 1) A hierarchical planning strategy, where the higher-level policy generates intentions with text semantics, and a semantic alignment technique ensures the lower-level policy determines specific controls to achieve these intentions. 2) A cross-modal encoder-decoder to fuse and utilize the shared semantic information to enhance planning through multi-modal understanding. A key advantage of HANSOME is that the generated intentions not only enhance the lower-level policy but also can be shared and understood by humans or other AVs to improve their planning. Furthermore, we devise AdaSMO, an entropy-controlled adaptive scalarization method, to tackle the multi-objective optimization problem in hierarchical policy learning. Extensive experiments show that HANSOME outperforms state-of-the-art WM-based methods in challenging driving tasks, enhancing overall traffic safety and efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
"World-Model Based Hierarchical Planning with Semantic Communications for Autonomous Driving" introduces HANSOME (Hierarchical Autonomous Navigation with Semantic Communication), a framework designed to improve autonomous driving using a world-model (WM) approach. HANSOME leverages hierarchical reinforcement learning (HRL) to manage complex, multi-agent driving scenarios by dividing decision-making into high-level intentions and low-level actions. This approach mirrors human driving strategies, where higher-level intentions like lane changes are communicated to other vehicles, while lower-level controls (e.g., acceleration) execute these decisions.

The contributions are summarized as follows:
1) HANSOME has a hierarchical planning strategy where the higher-level policy generates and shares semantic intentions in the form of text to guide the lower-level policy which in turn decides specific controls. 

2) hierarchical training as a multi-objective optimization problem and devise AdaSMO to dynamically balance learning of two-level policies

3) Exhasutive experimentation to show where current state-of-the-art WM-based RL methods may fail, and show AdaSMO’s effectiveness in training a good hierarchical planning strategy

### Strengths
1) The paper is well written and easy to follow, with appropriate diagrams to help readers understand the complex two level policy design
2) THe related work sections broadly offers a good overview of the world modeling literature
3) There is a lot of technical contribution in terms of both coming up with the two level policy approach to RL and as well design the adasMO objective to optimize the hierarchical policy planning.
4) Exhasutive experimentation and ablation allow the reader to understand the contibution of each of the proposed novelties.

### Weaknesses
1) I struggle to find what is the real world application of such a design where each agent needs to communicate policies with other agents to make progress? Are they limited to simulation or a pre training world modeling task to later be applied to a real world planner distribution where all agents are not controlled by a uniform policy? If the later, then the paper should include some analysis of such an adaptation otherwise it is unclear how effective the setup is for such a design. If the former, more exhasutive interactive agent analysis on other publically  available benchmarks must be provided to ascertain technical competitiveness of the proposed methodology.

2) the experimentation section is weak as it only compares to a corner of the planning research world, one one particular dataset. More exhasutive evaluation of ablation of the choices made would make it clear what are the true contributions of this work.

### Questions
1) I struggle to find what is the real world application of such a design where each agent needs to communicate policies with other agents to make progress? Are they limited to simulation or a pre training world modeling task to later be applied to a real world planner distribution where all agents are not controlled by a uniform policy? If the later, then the paper should include some analysis of such an adaptation otherwise it is unclear how effective the setup is for such a design. If the former, more exhasutive interactive agent analysis on other publically  available benchmarks must be provided to ascertain technical competitiveness of the proposed methodology.

### Soundness
3

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
4

### Summary
This paper proposes a world-model-based planner for autonomous driving, named HANSOME. HANSOME first predicts the high-level intention based on the hidden state and observation. Then it predicts both the low-level control signal and waypoints on BEV maps conditioned on the intention. The world model or latent encoding part takes BEV and intentions of other vehicles (waypoints under BEV) as input and reconstructs future trajectories of neighbors. HANSOME designs reward by combining intention generation and waypoint following in low-level policies. To learn the two levels of planning in HANSOME, the authors apply various stages of scalarization to control the entropy of high-level policy outputs and balance the ultimate optimization weight. HANSOME is tested on four scenarios on CARLA and outperforms Dreamer-based baselines. Ablations are also conducted to validate the effectiveness of the modules in HANSOME.

### Strengths
1. The paper is easy to follow and understand overall. Discussions on related works are relatively sufficient for understanding their differences. Even end-to-end driving and hierarchical planner in embodied AI are discussed in the appendix as well, which is very good and comprehensive.
1. The evaluation is adequate overall. Essential ablations have been conducted for different designs of HANSOME. I am glad to see the multi-agent learning experiments in the appendix, though the setting is relatively simple. As the paper highlights semantic information sharing, multi-agent or V2X settings should be validated to highlight its effectiveness.
1. The source code is provided and detailed parameters are listed in the appendix for reproduction.

### Weaknesses
- Multiple designs in HANSOME have been validated for their effectiveness, or widely adopted, in other areas. The semantic information sharing is widely used in V2X and multi-agent approaches, and the authors have cited some of these works. Hierarchical planning is also a common way in the industry, and a lot of language-related driving papers such as DriveVLM [1] and DriveVLM [2]. Predicting control signals and waypoints at the same time is used in previous works like TCP [3]. The world model predicts other vehicles future motion and does not feature very novel designs from my viewpoint.
- There seem a lot of heuristic settings or designs in HANSOME. Therefore, though HANSOME achieves much better performance compared to DreamerV2&V3, I am wondering if the effectiveness is carefully tuned and worrying about its broader impacts. For example, HANSOME uses a heuristic method to select agents for information exchange; the adaptive scalarization constant S is heuristically adjusted with various stages; the reward designs.
- Though the authors claim that HANSOME agents can generate intentions by themselves while other works like MILE, SEM2, and Think2Drive need pre-determined routes for guidance, I think this advantage is because current evaluations are solely conducted in a very small scenario, like LeftTurn and RightTurn. I also get why the authors mention the comparisons with route planning in Lines 89-97. However, in this work, HANSOME does not include route planning in its structure which limits its long-term planning ability.
- Based on the previous point, I believe the current benchmarks, four specifically collected scenarios, are relatively simple. Maybe it is a common way for world model-based methods, but standard evaluation setups like Town05Long or leaderboard v1&v2 should be much more convincing.
- The method is not strictly end-to-end planning as its inputs are BEV rendering images, not raw sensory inputs.
- Minors.
  - I do not see waypoints or destination directions of other vehicles in BEV in Fig. 3. 
  - Typos. Line 151, ``generated by the''

### Questions
- Could you provide the whole results under LeftTurn and RightTurn, including the results of other baselines? These results should show the effectiveness of hierachical planning and AdaSMO.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work introduces a method named HANSOME for autonomous driving that combines hierarchical planning with semantic communication in a Dreamer V3 framework. It adopts a hierarchical reinforcement learning structure where the higher-level policy sets semantic intentions, and the lower-level policy determines control actions based on these intentions. An adaptive scalarization method AdaSMO that dynamically balances multi-objective optimization between the hierarchical levels is also proposed.

### Strengths
- Easy to follow. Clear writing.
- The idea of incorporating language into the Dreamer V3 framework is straightforward and can lead to better performance.
- The illustration of intention and sharing across multiple agents are interesting.
- The AdaSMO method dynamically adjusts the focus between high-level and low-level objectives, allowing for more stable training and performance optimization across hierarchical levels.
- Better performance compared to baselines and very good visualizations provided.

### Weaknesses
 - The authors mainly use the toy testing scenario, only considering left turn, right turn, and merging. These simulated scenarios can be easily to be Could the author try complex scenarios or simulation environments?
- The model’s performance highly relied on the quality of semantic intentions, which may not always be accurate or available in real-world settings.
- The work is more like integrating language into the Dreamer framework,  lacking novelties.
- How does the model understand language or traffic rules? Did the author provide a text prompt of traffic rules or involve large language models?
- Could the framework handle unpredictable human driver behavior in mixed traffic environments?
- Could this framework framework be generalized to other complex, multi-agent environments beyond autonomous driving?
- The proposed AdaSMO looks like human-crafted parameter tuning, which is not considered adaptive.

### Questions
Please see the weaknesses part. Thanks.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes, HANSOME, a WM-based hierarchical planning model for AV under the V2V setting (the intention of other vehicles can be accessed by the ego vehicle). The proposed model uses the Dreamer backbone to train the high-level policy (intent conditioned trajectory prediction) and the low-level policy (waypoints following) through an entropy-controlled adaptive scalarization approach. The paper is well-written and easy to follow.

### Strengths
The paper is well-written and easy to follow. The proposed approach is validated through multiple experiment configurations to demonstrate its effectiveness compared to baselines.

### Weaknesses
1. The motivation of the low-level policy. Line276-279 indicate that the intention of the high-level policy is rendered as the waypoints on the bev, and the low-level policy just tries to track the waypoints. This means that the low-level policy is equivalent to a PID controller and is independent of tasks. So what is the motivation to include in the learning problem? To justify this, I encourage the authors to demonstrate that why directly calling a tuned PID waypoint tracking algorithm or an independently learned tracker is not good compared to jointly learn a tracker and motion planner. The current justification for end-to-end learning is not sufficient, as it does not explain why a standard, well-tuned PID controller or a separate learned tracker would be inadequate. Specifically, the paper needs to show that the joint training provides a benefit beyond what could be achieved by a modular approach, where a high-level planner feeds waypoints to a separate, well-performing tracker. The paper should provide evidence that the low-level policy learns to adapt to the high-level policy's capabilities in a way that a standard tracker could not, and that this adaptation leads to better overall performance.

2. The need of a simulator. The loss needs to compute the tracking error (eq 1). Does that mean you still need a simulator during policy rollout? This is a bit strange, because the motivation for learning a world model is to learn a realistic simulator. I think this work does three things: 1) an intent conditioned traj prediction (the encoder-decoder model) model; 2) a waypoints tracker model; 3) a loss that trains these models together. I feel that 1 is not new, and  3) is not necessary.

3. I encourage the authors to validate the proposed approach in Waymax in the future, which provides more traffic scenarios (> 100k) compared to just using 4 scenarios in the current version.

### Questions
Please see the comments in the Weaknesses section.

### Soundness
2

### Presentation
2

### Contribution
2

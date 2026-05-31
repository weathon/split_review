## Human Reviewer 1

### Summary
The paper proposes an algorithm for formation control of multiple UAVs tracking a wild fire using a federated learning approach to DDPG.
A _weighted_ federated learning approach is proposed whereby the parameters that are accumulated and merged into an averaged global policy are done so weighted by the performance of the individual agents.
Experiments are performed illustrating the advantages of this modified algorithm compared to DDPG in a simulated multi-UAV wild fire tracking simulation.

### Strengths
1. The paper proposes a novel weighted federated learning algorithm that could potentially be applied to many other RL settings beyond the application explored in this paper. As far as I am aware this weighted averaging of parameters in an FL algorithm is novel - although I am not very familiar with all the relevant literature - and given that the paper does not cite similar instances of this algorithm I am assuming that the authors consider it novel also.
2. The paper applies this novel algorithm to the important real world problem of wild fire tracking.
3. The results show _some_ evidence of improved performance compared to DDPG.

### Weaknesses
1. The paper is not written particularly clearly and fails to highlight the true novelty and purpose of the paper which is the _weighted_ FL algorithm. This is not mentioned in the abstract referring only to an FLDDPG approach, which has already been done before in Na et al. 2023. The abstract also highlights the reward difference between the two compared approaches; however, it is easy to construct a particular reward function such that a large reward difference doesn't necessarily reflect a large skill difference.
2. The proposed weighted FLDDPG is not compared to a non-weighted FLDDPG in the experiments, this would have been the most appropriate comparison to illustrate the advantages of the propose novelty. It is therefore unclear whether the proposed novelty of the paper is the reason for outperforming DDPG or just the fact that it integrates an FL aspect, which has already been explored in Na et al 2023.
3. The advantages of FLDDPG are not necessarily reflected in the results because both algorithms achieve the maximum reward of 1 during the simulation.
4. It is unclear to me whether training is occurring online during the simulated 20 seconds, or whether training occurred before this simulation and this simulation is a rollout of the optimised policies. If the former, then point 3. is even more pertinent because one would just select the final policy as that which achieved the maximum reward, which occurred for both algorithms.
5. As far as I can tell multiple experiments were not performed to highlight robustness.
6. There should be a single plot comparing both algorithms, rather than providing the results in two separate plots.
7. The images of the UAVs and the fire do not illustrate how to UAV swarm reacts to the fire evolving through time, which would have been informative.
8. It is unclear to me why bother reporting the results of a 3 UAV simulation _and_ a 5 UAV simulation when the latter illustrates the same advantages as well as demonstrating scalability. The 3 UAV experiments therefore seem redundant.
9. The mathematical notation is a little sloppy, in particular with relation to the t subscript in the equation in line 183 and the subscripts in equation 10. There are also multiple variables that are not adequately described making the maths a little hard to follow.
10. The images are pixelated and should instead be vector images.

### Questions
1. Is the learning performed during the simulated 20 seconds or is it performed prior to the simulation reported in the results section?
2. Why did you not compare to a non-weighted FLDDPG approach?
3. Did you perform multiple experiments or just the one per algorithm?
4. Do you forsee this weighted FLDDPG algorithm as a more general RL algorithm with applications beyond wild fire tracking?

### Soundness
2

### Presentation
2

### Contribution
3

### Rating
2

### Confidence
3

---

## Human Reviewer 2

### Summary
This paper addresses the challenge of formation control in multi-UAV systems for large-scale wildfire tracking using deep reinforcement learning. The authors propose FL-DDPG, a framework that combines Federated Learning (FL) with the Deep Deterministic Policy Gradient (DDPG) algorithm to enhance decentralized coordination among UAVs. Unlike standard DDPG, which struggles to scale across multiple agents and irregular wildfire dynamics, FL-DDPG enables collaborative policy updates without sharing raw data, using a distance- and performance-weighted averaging method. Simulation results demonstrate that FL-DDPG achieves far greater formation stability, reducing spacing variance from 14 m to 2.5 m.

### Strengths
- Strong and complete backgound ("Premininaries") section
- Great to see real-world fire data as part of the simulation

### Weaknesses
- Introduction could use additional references on MARL for Wildfires and communication / collaboration with human and machines: HIVEX: A High-Impact Environment Suite for Multi-Agent Research and LLM-Mediated Guidance of MARL Systems (Siedler et. al.)
- Section naming could be more conventional e.g. "Background" instead of "Preliminaries"
- Figure 1 could use more detailed but high level (non technical) description in the caption on how things work
- Figure 3: The differences between the two plots is barely noticeable, maybe would be good to zoom in and or highlight the differences explicitly in the caption.
- Experiment runs are statistically not satisfying. I would have expected 3-10 runs and resulting plots showing averages, and tables showing standard deviation etc.
- There could be more discussion on why FL-DDPG is better than DDPG
- Personally I believe it would be fruitful to also run UAV-count exepriments, how does the current solution scale from 3-9 UAVs? etc.

### Questions
- "The pair (Tx, Ty ) corresponds to a clockwise rotation; for consistency across the controller design,
we adopt the counterclockwise convention above throughout this work." - independent of counter or clockwise, there is a full update - the entire perimeter - for each step, correct?
- The description for the rewards given are not enough. This is what I understand: There is a reward for keeping safe distance to neighbours. What I don't understand is "UAV's heading with the direction of the spread" does that mean the UAV's must align with direction of fire-spread? Are we tracking "un-seen" fire front? How does this work?
- Generally we are looking at 2D coordinates for the UAV, however there is a mention that the "FARSITE model" includes terrain data, how does this relate?

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
6

### Confidence
4

---

## Human Reviewer 3

### Summary
The paper proposes a novel framework called FL-DDPG to coordinate a team of UAVs tasked with tracking the perimeter of a wildfire. The primary challenges with existing methods include - (1) Standard RL and DRDL methods are often very inefficient and do not scale well (2) Firefronts evolve continuously which make it hard for achieving formation control.

Federated Learning-based DDPG (FLDDPG) framework employs:- 
(a) A selective federation strategy where - each UAV transmits only the relevant subsets of its local model parameters—specifically those governing velocity and control gain
(b) A weighted aggregation of above said parameters - agents that maintain tighter adherence to the desired formation spacing exert greater influence on the global policy thereby biasing learning toward stability under asymmetric fire-front dynamics

The authors present simulation results, based on a FARSITE-calibrated environment, claiming that FL-DDPG significantly outperforms a "standard DDPG" baseline in both formation stability and average episode reward

### Strengths
1. Originality - A creative combination of Federated Learning and Deep Reinforcement Learning has been applied to a challenging domain which is definitely a great idea. Secondly, the federated aggregation is clever in the fact that it directly links the agent's influence on the global model to a key term from it's own rewards function (formation-spacing error). The selective federation strategy to share just the velocity and gain parameters is also an original win.
2. Quality - The quality of the paper lies majorly in its experimental setup where they have demonstrated results on a high fidelity simulation environment i.e the FARSITE simulator with calibration done on historical data. This points to a very non trivial problem being solved 
3. Clarity - For the most part, the clarity is great. The ideas are easy to follow and well articulated. The visual evidence also does provide a compelling story that FL-DDPG agents do maintain a coordinated formation compared to agents that use DDPG only.
4. Significance - The significance of the paper is high because the problem being solved is non trivial and is a great real world application with societal benefits.

### Weaknesses
1. Lack of ablation studies to prove "performance-weighted" aggregation  and the "selective federation" hypothesis actually work - because the paper includes no ablation studies, it's impossible to know if either of these novelties is actually necessary or beneficial.
2. The only baseline being compared against is standard DDPG. The lack of comparison to any credible MARL baselines like MADDPG or even MAPPO or VDN is a very critical flaw.
3. The reward function does not seem standardized - It is a complex, custom-engineered equation with multiple hand-tuned hyperparameters and no sensitivity analysis.
4. The reward plots are normalized which is poor practice. You are not able to figure out if the agents are actually solving the tasks or just converging to a less bad policy than the baseline

### Questions
1. Did the authors consider or experiment with more modern on-policy MARL algorithms (like MAPPO), which are often state-of-the-art for cooperative tasks?
2. Can the authors also provide an ablation study against MADDPG (an established MARL baseline) and/or VDN ? 
3. Can the authors provide ablation studies for proving the "performance-weighted" aggregation  and the "selective federation" hypothesis ? Like what would happen if a standard FedAvg algorithm is used ? 
4. What is the justification for the exact equal weighting of the fire-tracking penalty (value=20) and the formation-spacing penalty(value=20) ? Also can we get sensitivity analysis on both of these ? 
5. The paper claims that the main benefit of FL is reducing communication bandwidth. How is the O(N) state shared? Because Equation 7 is an O(N) state that probably requires O(N^2) communication cost and would it not negate scalability benefits ?

### Soundness
1

### Presentation
2

### Contribution
1

### Rating
0

### Confidence
4
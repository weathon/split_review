# Towards Greener and Sustainable Airside Operations: A Deep Reinforcement Learning Approach to Pushback Rate Control for Mixed-Mode Runways

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 5, 3, 3

## Abstract
Airside taxi delays have adverse consequences for airports and airlines globally, leading to airside congestion, increased Air Traffic Controller/Pilot workloads, missed passenger connections, and adverse environmental impact due to excessive fuel consumption. Effectively addressing taxi delays necessitates the synchronization of stochastic and uncertain airside operations, encompassing aircraft pushbacks, taxiway movements, and runway take-offs. With the implementation of mixed-mode runway operations (arrivals-departures on the same runway) to accommodate projected traffic growth, complexity of airside operations is expected to increase significantly. To manage airside congestion under increased traffic demand, development of efficient pushback control, also known as Departure Metering (DM), policies is a challenging problem. DM is an airside congestion management procedure that controls departure pushback timings, aiming to reduce taxi delays by transferring taxiway waiting times to gates. Under mixed-mode runway operations, however, DM must additionally maintain sufficient runway pressure---departure queues near runway for take-offs---to utilize available departure slots within incoming arrival aircraft steams. While a high pushback rate may result in extended departure queues, leading to increased taxi-out delays, a low pushback rate can result in empty slots between incoming arrival streams, leading to reduced runway throughput.
    
 This study introduces a Deep Reinforcement Learning (DRL) based DM approach for mixed-mode runway operations. We cast the DM problem in a markov decision process framework and use Singapore Changi Airport surface movement data to simulate airside operations and evaluate different DM policies. Predictive airside hotspots are identified using a spatial-temporal event graph, serving as the observation to the DRL agent. Our DRL based DM approach utilizes pushback rate as agent's action and reward shaping to dynamically regulate pushback rates for improved runway utilization and taxi delay management under uncertainties. Benchmarking the learnt DRL based DM policy against other baselines demonstrates the superior performance of our method, especially in high traffic density scenarios. Results, on a typical day of operations at Singapore Changi Airport, demonstrate that DRL based DM can reduce peak taxi times (1-3 minutes, on average); save approximately 27\% in fuel consumption and overall better manage the airside traffic.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a method based on Deep Reinforcement Learning (DRL) to address the airport takeoff control problem on mixed-mode runways. The core idea of the article includes formalizing the takeoff control problem as a Markov Decision Process (MDP), using a spatio-temporal event graph to characterize the traffic density in hotspots, and adopting a continuous deferral rate action space instead of the traditional binary open/close control method. In addition, the reward function aims to encourage high taxi speeds and runway utilization, and utilizes the Proximal Policy Optimization (PPO) algorithm to train agents. This method was evaluated on simulated traffic data from Singapore Changi Airport, and the results show that the DRL strategy reduces taxi delays, fuel consumption, and conflicts compared to baseline strategies. The article emphasizes the applicability and research characteristics of its application.

### Strengths
- Novel state representation using event graph captures airside congestion well

- Pushback rate action space is more practical than on/off metering

- Significant taxi delay and fuel burn reduction in experiments

- Outperforms other approaches like tabu search and baseline DRL

- Evaluated on realistic traffic scenarios from Singapore Airport

### Weaknesses
1) Unclear how method would transfer or scale to other airports  
2) This paper focus on the application and no new algorithms is provided. 
3）Lack of comparison of other optimization and planning algorithms.

### Questions
- How would the policy transfer to other airports with different layouts and traffic patterns?

- Could the event graph idea be used for other air traffic management tasks?

- What are other ways to set the hyperparameters instead of manual tuning?

- How would the policy perform with human controllers in the loop vs automation?

### Soundness
3 good

### Presentation
3 good

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
The authors propose a novel RL-based approach for Departure Metering (DM). This is achieved by introducing domain-specific state/action representations and together with a PPO-based RL agent for this task.

Empirically, the authors show that the proposed method outperforms other methods and ablations on a simulation based on Singapore Changi Airport surface movement data.

### Strengths
I am not an expert in the field of air traffic control, but the domain-inspired choices in the proposed MDP representation are well motivated. The authors encode specific domain knowledge to achieve good performance.

The paper is well written, although in some parts the narration feels a bit too slow (while in others the authors gloss over a few details).

### Weaknesses
In my opinion, the main weaknesses of this work lie in (i) the extreme specificity of the methodology, (ii) the lack of baselines and/or experiments to validate the proposed architectural innovations, and (iii) more generally, the relevance to the broader ICLR community.

(i) The extreme specificity of the methodology:
Air traffic control is a relevant problem. However, the proposed architecture seems to be extremely tailored for this one specific application. How generalizable are these methods beyond the this application? It'd be nice to see experiments on a more diverse set of problems.


(ii) The lack of baselines and/or experiments to validate the proposed innovations:
The set of baselines is extremely limited. The authors should provide additional RL-based approaches from literature or simply by implementing sensible alternative approaches to the problem.

Arguably, the major contribution of this work is the representations of MDP elements and the authors do a good job at motivating the reasoning behind their choices. It would be interesting to test how agnostic the proposed framework is to the choice of RL algorithm.

### Questions
(i) The extreme specificity of the methodology:
Air traffic control is a relevant problem. However, the proposed architecture seems to be extremely tailored for this one specific application. How generalizable are these methods beyond the this application? It'd be nice to see experiments on a more diverse set of problems.


(ii) The lack of baselines and/or experiments to validate the proposed innovations:
The set of baselines is extremely limited. The authors should provide additional RL-based approaches from literature or simply by implementing sensible alternative approaches to the problem.

Arguably, the major contribution of this work is the representations of MDP elements and the authors do a good job at motivating the reasoning behind their choices. It would be interesting to test how agnostic the proposed framework is to the choice of RL algorithm.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This research introduces a Deep Reinforcement Learning (DRL) strategy for Departure Metering (DM) during mixed-mode runway operations, focusing on optimizing pushback timings to alleviate airside congestion. By framing the DM challenge as a markov decision process and utilizing Singapore Changi Airport data, the study simulates airside activities to assess DM policies. The DRL agent uses spatial-temporal event graphs to detect airside hotspots and adjusts pushback rates dynamically. Compared to other methods, the DRL approach proves superior, especially under high traffic. Findings indicate notable reductions in taxi times and a 27% fuel savings at Singapore Changi Airport.

### Strengths
1. The author employs an "airside event graph", inspired by temporal constraint networks, to effectively represent the state of airside traffic. This novel representation captures spatial-temporal movements of aircraft, offering a sophisticated modeling approach.
2. It considers various types of conflicts (e.g., following, crossings, and head-on conflicts) that can occur during taxiing. This comprehensive approach ensures that the proposed solution addresses a wide range of operational challenges.
3. The paper doesn't just propose a solution, but also quantitatively evaluates its impact, as seen in the results section. This rigorous evaluation approach, including fuel consumption analysis, provides tangible evidence of the proposed method's efficacy.

### Weaknesses
1. The model primarily validates using the Singapore Changi Airport scenario, questioning its adaptability. The research falls short in demonstrating generalization across varied environments. Specifically, the paper lacks any analysis of how the model's performance would be affected by different airport layouts, traffic patterns, or operational procedures. This raises concerns about the robustness of the proposed approach in real-world scenarios that differ significantly from the specific case study.
2. The "hotspots" paradigm is ambiguously defined. Such lack of clarity in state representation can lead to convoluted state spaces and suboptimal policies in reinforcement learning. The paper does not specify the precise criteria used to define a hotspot, such as the density of aircraft, the duration of congestion, or the spatial extent of the affected area. This ambiguity makes it difficult to understand how the DRL agent identifies and responds to congestion effectively.
3. The reward structure is inadequately elaborated. Given its importance in shaping agent behavior in reinforcement learning, its cursory treatment raises concerns about potential biases and pitfalls. The paper does not clearly define the reward function, including the weights assigned to different components (e.g., taxi time reduction, fuel savings). The lack of transparency makes it hard to assess whether the reward function is properly aligned with the desired objectives and whether it might incentivize unintended behaviors.
4. The action space, narrowed to pushback rate control, oversimplifies the complexity of airside operations, missing out on capturing nuanced dynamics. The paper does not consider other potentially impactful actions that could be taken, such as adjusting taxi routes, prioritizing certain flights, or coordinating with other ground control systems. This limited action space restricts the agent's ability to respond effectively to complex situations.
5. The comparative evaluation against baselines lacks depth and rigor, failing to provide a comprehensive assessment against state-of-the-art methods. The paper does not provide sufficient details about the baseline methods used for comparison, such as their implementation details or parameter settings. This lack of transparency makes it difficult to determine whether the DRL approach truly outperforms existing state-of-the-art methods.

### Questions
1. How does your approach compare with existing MARL algorithms in terms of efficiency and efficacy? Are there benchmark comparisons against state-of-the-art multi-agent methods to validate the superiority of your approach?
2. How do agents in the model communicate during airside operations?
3. Reward shaping and credit assignment are critical in multi-agent settings. How do you ensure that individual agents receive appropriate credit for their actions to promote cooperative behavior? Are there specific reward shaping techniques employed to foster collaborative actions?
4. How does the method explore the joint action space and how scalable is it with increasing dimensions?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper considers using deep reinforcement learning to design pushback rate for mixed-mode runways. Based on the congestion information, a controller decides the pushback rate (from 0 to 4). The reward is a combination of how fast aircraft leave the gate and the time it spends waiting to take off.

### Strengths
+ Optimizing aircraft traffic within an airport is a complex and important problem. 
+ It's easy to understand what the paper is trying to do and the problem makes sense. 
+ Some numerical improvement are seen against an uncontrolled policy.

### Weaknesses
- It's not clear that deep reinforcement learning is the right tool to use here. Since the decision is centralized, and there are important safety constraints, a rolling horizon approach (e.g., a MPC) may do better. Specifically, the problem formulation lends itself to a more deterministic optimization approach, where the objective function can be explicitly defined based on the desired trade-off between gate departure and runway occupancy. The use of a black-box DRL approach makes it difficult to guarantee constraint satisfaction and interpret the learned policy. Furthermore, the state space is relatively low-dimensional, which may not be complex enough to justify the use of DRL.
- The learning problem setup is also fairly standard and it's hard to see innovations in that regard. As the authors point out, a rate would be more natural for the traffic controllers. Looking at how this can be directly learned rather than taking a discretization approach as currently done in the paper would be interesting. The discretization of the pushback rate into only 5 discrete levels (0-4) seems overly simplistic and may limit the potential performance gains. A continuous action space, or a more fine-grained discretization, could allow for more nuanced control of the pushback process.

### Questions
- In current practice, is the pushback process entirely unmetered? Or would an aircraft need the clearance from air traffic control to pushback? If the latter is true, the ATC would be implicitly doing some optimization right?
- Does the methods in the paper use the fact that a runway is mixed use? I'm not sure I see that in the algorithm. Also, for a large airport like Changi, are the runways mixed use?
- Sometimes a plane pushes back to free up a gate such that a landed aircraft can use it. So holding planes at gates is not exactly zero cost.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

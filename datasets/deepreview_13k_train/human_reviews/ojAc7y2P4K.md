# Dispatching Ambulances using Deep Reinforcement Learning

- Decision: Reject
- Scores: 5, 3, 8, 5

## Abstract
Emergency Medical Service (EMS) plays an essential role in today's society.  One EMS component is ambulance dispatch,  which impacts the ambulance's response time for a medical incident.  Fast response times are essential. The problem of ambulance dispatching differs from a typical Vehicle Routing Problem (VRP) since patients arrive stochastically, making the problem hard to solve. 
In addition to minimizing response time, EMS providers seek optimal resource utilization and good working conditions for EMS personnel while often experiencing an increase in demand. To meet these requirements, this work develops a Reinforcement learning (RL) method based on Proximal Policy Optimization (PPO) for the ambulance dispatching problem.  Varying incident priorities along with more flexible incident queue management are also integrated into our novel method.  Our PPO-based method and an EMS simulation model are implemented in Python and combined with Open Street Map (OSM) travel time estimation and simple synthetic incident data generation. Empirical results are presented using both synthetic and real incident data.  Results using real incident data from the Oslo University Hospital (OUH) in Norway suggest that our PPO model outperforms heuristic policies such as dispatching the closest ambulance by Haversine or Euclidean distance.  We hope that this work inspires future research on RL for ambulance dispatch and ultimately leads to improved decision-support tools for EMS in Norway and elsewhere.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposed to identify the optimal ambulance dispatching policy using deep reinforcement learning method, PPO. Given a set of ambulance base locations, allocation of ambulances to bases, patient demand distribution and travel time learnt from open street map, the authors designed an MDP formulation of the dispatching problem, where the goal is to map ambulances to patients while considering the severity of the issue so that overall response times are minimized. To learn the assignment policy, standard deep RL method PPO is used. Experiments are conducted with both real-world patient demand distribution and artificially learned demand distribution. The proposed Deep RL method outperforms existing heuristic based nearest ambulance assignment policies.

### Strengths
The paper solves a practically important and challenging problem of emergency response where even optimizing the response times by few seconds can save human life and has a great impact on society. I appreciate that the problem is formulated on real-world dataset and by considering practical constraints. The state and action definition are straightforward and practical. The reward function is designed intelligently that can cater to prioritizing high severity incidents. Experiments are conducted on real-world data from Oslo and by considering practical constraints such as the number of ambulances might change over time, or the reward might vary based upon the incident severity. Experimental results are also somewhat impressive as in both real and artificially learned demand data setting, the proposed method outperforms standard heuristics on real-world test dataset.

### Weaknesses
Although I appreciate the problem formulation, experimental settings and results on real-world data, I have several concerns about the technical and experimental novelties of the paper:
1. Identifying ambulance dispatch policy with deep RL is not a new problem, there are several prior works that try to solve the problem, some of them are even mentioned in references (e.g., Liu et al, 2020, or Hua et al, 2020).
2. In terms of technical contributions, while the MDP formulation is an important contribution (although not entirely new), the novelties seem very limited as it directly uses PPO to solve the problem. 
3. Emergency response systems typically follow hard constraints on response time (e.g., maximize number of patients served within D minutes). I failed to understand how the proposed reward function considers such threshold values. Even in experimental results, only mean response times are shown. Having percentage of requests from different severity levels served within threshold times would have been an ideal metric. 
4. Experimental setup and results are not up to the mark. Simple heuristics based on spatial distance are only considered as benchmarks, while avoiding state-of-the-art methods. A bare minimum requirement would be to consider different versions of deep RL methods to position why PPO is the best choice.
5.	There is a high chance that the simulator is biased towards historical demand distributions. As the spatio-temporal demand patterns typically change over time, some risk analysis is required on whether the assignment policy is overfitted. Moreover, it is not clear how the policy will adapt to dynamic nature of demand patterns.

### Questions
1. Why is the proposed method not compared with other deep RL based dispatching methods?
2. Have you done any analysis on what percentage of requests are served within threshold time for different priorities of incidents?
3. Can the simulator or learned policy be overfitted to historical demand? How to continuously adapt the policy to changes in demand patterns?
4. Usually, the action space in RL is fixed, but here the action space can change depending upon the number of available ambulances and patient requests. How are you dealing with this dynamic action space?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work  proposes a way to use RL, PPO to the ambulance dispatching problem as a potential decision-support tool for the Emergency Medical Services. The authors introduce two variants of this dispatching problem (with and without queuing) and provide sufficient motivation/justification for the relevance of the problem in real-world. They train a simulator to simulate the general EMS dispatch setup based on the incident and OSM datasets and use a PPO based RL policy to select the right ambulance given the state of the system. The key contributions are the adoption of PPO based agent in a dispatching problem along with consideration of queuing and introduction of a regularizer in form of synthetic incident generator.

### Strengths
Below are the strengths of the presented work -- 
1. The problem is well motivated in form of its application in a real-world setting. 
2. The authors do a good job at problem formulation in explaining how the dispatching problem can be formulated as a control problem, for e.g., clearly defining the state and action space, simulator, and the reward model. 
3. Paper is clear to understand and reasonably well written.

### Weaknesses
Below are the weaknesses of the presented work -- 
1. The experiment section is highly under-developed: The comparisons made to baselines are neither rigorous, not complete. I would've expected to see how the proposed PPO adoption in this particular setting compares to other RL-based baselines. Why was PPO the right choice? Specifically, the paper lacks a thorough ablation study. It is unclear how different components of the PPO algorithm, such as the clipping parameter, the value function loss coefficient, or the entropy regularization term, impact the final performance. The choice of hyperparameters seems arbitrary and lacks justification. Furthermore, the comparison to a simple heuristic baseline is insufficient to demonstrate the effectiveness of the proposed approach. A comparison to other state-of-the-art RL algorithms, such as DQN or SAC, is necessary to establish the superiority of PPO in this context. The evaluation metrics themselves could also be expanded upon to include more nuanced measures of dispatching performance, such as average response time per incident priority or resource utilization.
2. The work lacks novelty: To me the work appears to just be an implementation of PPO algorithm in a particular use-case (ambulance dispatching). I feel the work lacks novelty both in problem and solution. Even if the solution isn't novel, I'd like to understand what makes this problem technically hard and why PPO is the right choice as a solution. Hence, I don't find the paper to meet the bar.

### Questions
Questions are highlighted in the weaknesses section above.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper considers Emergency Medical Service (EMS) while focusing on the aspect of ambulance dispatch. Recognizing the necessity for the fast response times and the challenges posed by the stochastic nature of patient arrivals, the study introduces a novel method of addressing the ambulance dispatch problem. Rather than utilizing traditional approaches, the authors propose a Reinforcement Learning (RL) method based on Proximal Policy Optimization (PPO) to enhance the efficiency of ambulance dispatch.

### Strengths
The adaptation and application of PPO to the ambulance dispatch scenario, a method that has not been employed previously for this specific problem.
Unlike many prior studies, this paper places significant emphasis on incident priority, which plays a critical role in determining the order of ambulance dispatch.
In order to circumvent the risks associated with over-reliance on historical data, the authors have devised a synthetic incident generator. They have validated their model against both historical and this synthetic data, which is reflective of incidents reported to the Oslo University Hospital's EMCC.

### Weaknesses
The paper mentions the potential risk of a more complex RL model overfitting the training dataset. This raises concerns about the model's generalizability as well as robustness in different settings or scenarios beyond the ones tested. Specifically, the paper does not provide a detailed analysis of the PPO model's sensitivity to hyperparameter tuning, which is crucial for avoiding overfitting. The choice of network architecture, learning rate, and other parameters can significantly impact the model's performance and its ability to generalize to unseen data. Furthermore, the synthetic incident generator, while a good approach to circumvent reliance on historical data, may not fully capture the complexities and nuances of real-world incident patterns, potentially leading to a model that is optimized for a simplified environment. The validation against historical data is mentioned, but a more in-depth comparison of the model's performance on both synthetic and real datasets, including a discussion of any discrepancies, would be beneficial. The paper also lacks a detailed discussion on the computational cost associated with training the PPO model, which is an important consideration for practical deployment in real-time EMS operations.

### Questions
As related to the above weakness, given that the paper mentions results from the random agent being likely due to the small environment considered, how would the model perform in larger urban areas with more complex terrains and road networks?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this paper, the ambulance dispatching problem is studied using reinforcement learning. The ambulance scheduling problem is different from the typical vehicle routing problem in that patient arrivals are random and thus the problem is difficult to solve. This article uses a reinforcement learning approach to PPO, taking into account the different number of ambulances available during the day shift and night shift, and taking into account the priority of things. Finally, a synthetic event generator is used. Historical and synthetic data reflecting incidents reported to the EMCC of the OUH are used to test the model and to contrast some underlying ambulance dispatch methods.

### Strengths
1.	The application scenario of this paper is the ambulance dispatch task, which is a very important application domain. As we all know, the speed of ambulance arrival is very important, even 10 seconds early can make a difference. This research can make a real contribution to society.
2.	The dataset used in this article comes from the real world, and the analysis of the dataset is valuable.

### Weaknesses
1.	The authors highlight their contribution about the adaptation of Proximal Policy Optimization (PPO) to the ambulance dispatch tasking. But only applying an algorithm to one task seems to be a weak contribution. The paper does not sufficiently explore the nuances of adapting PPO to this specific problem, such as modifications to the reward function, state representation, or action space that are tailored to the ambulance dispatch context. The lack of ablation studies to justify the specific design choices further weakens this contribution.
2.	Figure 3 is very unclear. First of all, it's not a flowchart; it just shows the inputs and outputs; it doesn't make it clear how the data flows. Second, this is not like a diagram illustrating the proposed framework. Instead, it's more like an architectural diagram of a program, which is not informative enough to reflect the unique contributions of the authors. The diagram fails to illustrate the interaction between the PPO agent and the environment, and the specific steps involved in the reinforcement learning loop are not clearly defined.
3.	The content of the paper is not full, like a paper completed in a short period of time. The paper just expresses the various parts, and the logic is not complete. The number of experiments is not enough, and in the experimental results, only the results are listed, and no analysis and explanation are carried out. The experimental section lacks a thorough analysis of the results, such as statistical significance tests, sensitivity analysis to hyperparameters, and a discussion of the limitations of the proposed approach. The absence of these elements makes it difficult to assess the robustness and generalizability of the findings.

### Questions
1.	Since your metric is waiting time, why not compare it to an agent that sends the ambulance that takes the shortest time to get to the location? It is obvious that today's maps have a time of arrival (TOA) estimation function. The method of using the shortest distance compared in the paper is not persuasive enough, because the closest distance does not necessarily represent the fastest arrival speed. At the same time, the authors did not compare other reinforcement learning methods mentioned in background section and Table 1.
2.	How fast does the proposed method perform? Because dispatch of an ambulance is an urgent matter, it is also important to be able to make the decision in the shortest time.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

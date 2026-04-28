# Data Center Cooling System Optimization Using Offline Reinforcement Learning

- Decision: Accept
- Avg Score: 6.25
- Scores: 3, 8, 8, 6

## Abstract
The recent advances in information technology and artificial intelligence have fueled a rapid expansion of the data center (DC) industry worldwide, accompanied by an immense appetite for electricity to power the DCs. In a typical DC, around 30-40% of the energy is spent on the cooling system rather than on computer servers, posing a pressing need for developing new energy-saving optimization technologies for DC cooling systems. However, optimizing such real-world industrial systems faces numerous challenges, including but not limited to a lack of reliable simulation environments, limited historical data, and stringent safety and control robustness requirements. In this work, we present a novel physics-informed offline reinforcement learning (RL) framework for energy efficiency optimization of DC cooling systems. The proposed framework models the complex dynamical patterns and physical dependencies inside a server room using a purposely designed graph neural network architecture that is compliant with the fundamental time-reversal symmetry. Because of its well-behaved and generalizable state-action representations, the model enables sample-efficient and robust latent space offline policy learning using limited real-world operational data. Our framework has been successfully deployed and verified in a large-scale production DC for closed-loop control of its air-cooling units (ACUs). We conducted a total of 1900 hours of short and long-term experiments in the production DC environment. The results show that our method achieves 14-21% energy savings in the DC cooling system, without any violation of the safety or operational constraints. We have also conducted a comprehensive evaluation of our approach in a real-world DC testbed environment. Our results have demonstrated the significant potential of offline RL in solving a broad range of data-limited, safety-critical real-world industrial control problems.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors present a physics-informed offline reinforcement learning framework for optimizing energy efficiency in data center cooling systems, addressing critical challenges like limited data and safety constraints. Using a graph neural network model that respects time-reversal symmetry, the framework enables efficient and robust policy learning from real-world operational data. The authors claimed that this method was successfully deployed in a large-scale commercial data center and achieved 14-18% energy savings over 1300 hours without violating safety constraints. The work demonstrates the potential of offline RL for complex, data-limited industrial applications and calls for a shift from simulation-based benchmarks to real-world problems for more practical and impactful RL research.

### Strengths
1. The proposed solution integrates a physics-informed dynamics model to accurately capture the complex thermal behavior within the server room, paired with a graph neural network that embeds domain knowledge to reduce data requirements. 
2. The authors claim that this approach produces well-structured and generalizable latent representations, facilitating a sample-efficient offline RL algorithm that maximizes the value function in latent space with appropriate regularization.
3. The implementation includes a safety-aware reward function to ensure operational reliability.
4. The premise of this paper is that as offline RL enables efficient policy learning from pre-collected data, eliminating the risks and costs associated with continuous interaction in safety-critical or resource-constrained environments, it is more effective and practical than online RL.

### Weaknesses
1. Claimed but Not Established: The paper asserts strong out-of-distribution (OOD) generalization capabilities and effectiveness with limited real-world data, but these claims are insufficiently substantiated. The paper does not provide a rigorous analysis of the state-action space coverage of the training data, nor does it quantify the degree of OOD generalization required for successful deployment. The lack of such analysis makes it difficult to assess the true robustness of the proposed method.
2. Lack of Industry Baseline: The real-world validation experiments show 14-18% energy savings in DC cooling without safety violations, but the paper is unable to present any well-defined industry practice baseline with similar objectives for comparison under similar constraints. The comparison lacks fairness. Also, a thorough optimization metric for a data center operation should factor in elements other than safety violations. The paper should consider metrics such as the Power Usage Effectiveness (PUE) or the Data Center infrastructure Efficiency (DCIE) to provide a more comprehensive evaluation of the proposed method's impact.
3. Model Generalizability & Insufficient Benchmark Comparison: The method heavily relies on modeling, but the generalizability and robustness of the modeling technique remain unverified. The method's performance is not evaluated against established benchmarks, limiting the validation of its general effectiveness. The paper should include a comparison with standard system identification techniques or other physics-informed modeling approaches to demonstrate the superiority of the proposed method.
4. Data and Experiment Limitations: The method's performance evaluation is constrained by the definitions of the experimental setup and the data distributions used in this study, which is not standardized. The lack of standardized datasets or experimental protocols makes it difficult to reproduce the results and compare them with other methods. The paper should provide more details about the data collection process and the characteristics of the data distributions.
5. Minimal Algorithmic Novelty: The approach offers little innovation compared to existing methods, limiting its algorithmic contribution. The paper should clearly highlight the unique aspects of the proposed method and how it advances the state-of-the-art in offline reinforcement learning.
6. Comparison with other Physics-informed modeling: The paper does not convincingly demonstrate how the proposed approach is superior to well-established physics simulation models bootstrapped with collected data that use online RL to train. The claimed higher sample efficiency with the physics-informed model is not unique, as similar benefits are observed with both online and offline RL approaches. A more detailed comparison with these approaches is needed to justify the choice of offline RL.
7. Unclear Baseline Performance: There is an inadequate explanation for why aggressive baseline methods like CCA and CQL achieve lower energy consumption but fail to maintain critical thermal safety. The paper should provide a more detailed analysis of the failure modes of these baseline methods and how the proposed method avoids these issues.

### Questions
Please refer to the weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes physics informed offline RL framework to control datacenter cooling systems. The proposed framework constructs a dynamics model based on T-symmetry and Graph Neural Networks to embed domain knowledge, TD3-BC to perform the policy optimization.  The framework is deployed on a real system and the authors develop a test bed to compare with existing approaches.

### Strengths
1. The authors tackle a problem of significant relevance, and develop a framework that can be implemented in the real world.
2. The paper is generally well written, and the authors do a good job of testing the proposed framework under different conditions.

### Weaknesses
1. The algorithmic contribution is minimal. While effective, the proposed method is a combination of existing methods tailored to a specific use case.


### Questions
1. Apart from the reward function, what are the other measures taken to prevent safety violations? 
2. Have the authors tried Offline-Online methods? wherein the policy trained using offline RL deployed is constantly improved using new data obtained? 
3. It seems like CQL does perform better than the proposed method in Figure 6, but at the cost of safety. What was the reward function used for CQL?

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
5

### Summary
This paper presents a novel physics-informed offline reinforcement learning framework for optimizing energy efficiency in data center cooling systems. The core component is a T-symmetry enforced thermal dynamics model using graph neural networks to capture complex thermal patterns. This enables sample-efficient offline policy learning from limited historical data. The framework was successfully deployed in a large-scale commercial data center, controlling multiple air cooling units and achieving 14-18% energy savings without safety violations over 1300 hours of experiments. Comprehensive evaluations on a real-world testbed further demonstrated the method's effectiveness compared to baselines. The approach shows significant potential for solving data-limited, safety-critical industrial control problems beyond just data center cooling.

### Strengths
- The methods proposed have been deployed in a real-world data center. This is a big, big accomplishment 
- The proposed methods go beyond simply applying an existing algorithm. They have applied state-of-the-art offline RL methods to the data center cooling problem. The idea to use both a GNN and a physics informed loss function makes sense. 
- The T-symmetry is an interesting idea that has been adopted from another paper, and they show it works well in their setting. 
- They have performed controlled experiments in a large scale data center as well as a small one where they have more control over the settings. 
- Their evaluation includes comparison against the state-of-the-art as well as ablation of their algorithm

### Weaknesses
 - The key metric used in evaluation is ACLF -- Air-side cooling load factor. However, this metric is neither defined nor explained in detail. It appears to increase with server load based on the sentence -- "Due to the smaller scale of the testbed and significantly lower server
load as compared to the real-world DC, the calculated ACLF values are higher than those observed in the real DC experiments." The lack of a precise definition makes it difficult to assess the practical implications of the reported energy savings. It's unclear if this metric is normalized for server load, or if it's simply a raw energy consumption ratio, which would make comparisons across different server loads unreliable.
- The Air Cooling Units (ACU) are being optimized in isolation, and it is unclear what is the impact on the upstream cooling system demand. Specifically, it is clear that the algorithm reduces the CAT (cold aisle temperature?) and therefore increases the demand on the chiller and cooling towers. Is the algorithm simply increasing the energy demand in the upstream system while reducing it in the ACUs? This raises concerns about whether the reported energy savings are a net benefit or just a shift in energy consumption to other parts of the cooling infrastructure. A full system analysis is needed to validate the overall efficiency gains.
- There are many claims throughout the paper which are not substantiated. For example: it states: "building a high-fidelity simulator can be very costly and impractical." How expensive is it, and why is it impractical? What are the specific challenges in creating such a simulator for a data center environment? Another example: "the fan power consumption is proportional to the cube of the fan speed". Please cite the source of this information. Without these details, the claims lack credibility and make it difficult to assess the generalizability of the approach.
- There are two externalities to the system -- entering water temperature and server load. While server load has been accounted for in the experiments, it is unclear if entering water temperature is constant throughout the experiment. Fluctuations in the entering water temperature could significantly impact the performance of the ACUs and the overall energy efficiency of the system, making it a critical factor to consider.

### Questions
1. Why does the reward need to be positive? 
2. How did you tune the hyper-parameters?
3. T-symmetry is supposed to help with OOD generalization. Have you measured OOD in your dataset? 
4. The algorithm is based on TD3+BC. Why is TD3+BC not one of the baselines in your experiments? 
5. I'm surprised outside weather conditions is not considered in the modeling. Does the data center have perfect insulation? I would assume hotter conditions would lead to higher cooling demand. 
6. The ratio of ACU average electric power and average energy consumption seem to vary with each entry. Why would that be?

### Soundness
3

### Presentation
4

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
The paper introduces a physics-informed offline reinforcement learning framework for optimizing data center (DC) cooling systems, addressing their substantial energy demands. Utilizing a graph neural network (GNN) architecture with time-reversal symmetry (T-symmetry), the model effectively captures complex thermal dynamics and ensures robust policy learning from limited historical data. Deployed in a real-world DC, the framework demonstrated 14-18% energy savings over 1300 hours without safety violations. Validation in a testbed environment further confirmed its superior performance over conventional and baseline RL methods. This approach highlights offline RL's potential for data-limited, safety-critical industrial control applications beyond DCs.

### Strengths
- The paper integrates graph neural networks (GNNs) with time-reversal symmetry (T-symmetry) to enhance offline reinforcement learning (RL), showcasing an innovative approach to optimizing DC cooling systems.
- Comprehensive real-world validation includes 1300 hours of deployment in a production DC, proving the method’s effectiveness and robustness.
- The methodology is clearly detailed with supporting figures and tables, making the framework’s architecture and results easy to follow.
- Demonstrated 14-18% energy savings highlights significant practical impact, with potential for broader application to other data-limited, safety-critical industrial control scenarios.

### Weaknesses
 - The paper relies solely on simulation-based testing in the small-scale DC testbed environment, limiting the generalizability of the results to more diverse real-world DCs. While the full-scale production test demonstrates feasibility, more varied test environments could strengthen the claims.
- The deployment details and considerations for long-term adaptability, such as how frequently model retraining is needed or how it adapts to evolving DC conditions, are underexplored.
- The scalability of the approach for larger DCs or environments with higher variability is not deeply discussed. Addressing the implications for larger-scale or more complex DC configurations would improve the scope of the work.
- While T-symmetry and GNN integration are well-motivated, there is limited discussion on potential trade-offs, such as computational complexity or latency during model training and execution.
- The paper could benefit from including a comparison with relevant existing methods like CLUE[1], which demonstrated data-efficient HVAC control with only seven days of training data and reduced comfort violations. Such a comparison would provide valuable context regarding the data efficiency and performance trade-offs of the proposed framework, particularly under conditions of limited training data.


### Questions
- Could the authors elaborate on how their model adapts to changing DC conditions over time and how often retraining is needed to maintain optimal performance?
- What are the potential limitations or challenges when scaling the proposed approach to larger data centers or DCs with more complex cooling system architectures?
- Can the authors provide more details on the computational cost of deploying the GNN and T-symmetry framework, particularly in comparison to simpler baseline models like PID controllers?
- Was the impact of T-symmetry enforcement on training time and model convergence evaluated? It would be helpful to understand if this enhancement has significant trade-offs in terms of training efficiency.
- Given that CLUE [1] achieved effective HVAC control with only seven days of training data, have the authors considered comparing their method's data efficiency to similar approaches? How would their framework perform with similarly limited training data?
1. An, Zhiyu, Xianzhong Ding, Arya Rathee, and Wan Du. "Clue: Safe model-based rl hvac control using epistemic uncertainty estimation." In Proceedings of the 10th ACM International Conference on Systems for Energy-Efficient Buildings, Cities, and Transportation, pp. 149-158. 2023.

### Soundness
3

### Presentation
3

### Contribution
3

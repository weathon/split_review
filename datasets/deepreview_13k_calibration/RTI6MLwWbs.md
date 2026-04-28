# Physics-infused Intention Network for Crowd Simulation

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 3, 8

## Abstract
Crowd simulation has garnered significant attention in domains including traffic management, urban planning, and emergency management. Existing methods can be classified as either rule-based or learning-based approaches, with the former lacking authenticity and the latter lacking generalization. Recent research has attempted to combine these approaches and propose physics-infused methods to address the aforementioned limitations. However, they continue to adhere strictly to the framework of the physical model, neglecting to depict the attention mechanism as a critical component of behavior. This limitation results in deficiencies in both the fidelity and generalizability of the simulations. This paper introduces a novel framework called Physics-infused Intention NEtwork (PINE) for crowd simulation. Our model introduces a physical bias while endowing pedestrians with the ability to selectively enhance the fine-grained information most relevant to one’s current behavior. In addition, we design a variable-step rollout training approach with an optimized loss function to address cumulative errors in simulation. By conducting extensive experiments on four publicly available real-world datasets, we demonstrate that our PINE outperforms state-of-the-art simulation methods in accuracy, physical fidelity, and generalizability.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a crowd simulation model called Physics-infused Intention NEtwork (PINE) combining the merits of rule-based and learning-based methods to improve the authenticity and generalization performance of the simulation. The contributions of this research are as follows:
1) A proposal of PINE for crowd simulation
2) An introduction to the Variable-step Rollout Training algorithm
3) Conduction of extensive experiments

### Strengths
1. The authors evaluated their crowd simulation with multiple datasets to validate their model under various conditions.
2. they compared their framework with various models from different categories making their proposal reasonable.

### Weaknesses
1. More descriptions seem to be required for input data such as s_p and  s_e.
2. Variable-step Rollout Training Algorithm (VRTA) is one of the main proposals, but explanation is not sufficient to understand.

### Questions
1. What is the dimension of the s_p and  s_e considering the minimum dataset size?
2. Using VRTA, which mechanism is applied to incrementally increase the value of T for the purpose of saving computation?
3. For additional bias in VRTA, the latest value is multiplied by the biggest value by multiplying i to the subtraction term. What is the exact effect of multiplying i?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a physical infused intention method to conduct crowd simulation. In the proposed work, the authors strengthen the importance of combining both advantages of rule-based and learning-based. Specifically, in the PINE network, a force attention module is designed to optimize the original force weight calculated by the Social Force Model. And a sequential module with a MLP are used to produce residual actions. They also introduced a variable step training process and designed a novel loss to reduce the cumulative error.

### Strengths
1. The paper is another approach intended to provide a seamless fusion of physic model and learning model in a crowd simulation scenario. The problem it intends to solve is significant and interesting.
2. The purpose of an additional term in the variable step rollout algorithm is innovative, intended to consider the bias of predicted actions and true actions, reflecting the model’s learning status to better guide the training process.

### Weaknesses
1. The paper lacks explicit explanation on important components, like the design of sequential models, how the attention model is updated, which is critical for understanding the rationale of the proposed work. Specifically, the paper does not detail the architecture of the sequential model, such as whether it uses an LSTM, Transformer, or other sequence modeling techniques. Furthermore, the input to this model is unclear: does it use absolute positions, relative positions, or a combination? The lack of clarity makes it difficult to assess the model's ability to capture temporal dependencies in pedestrian movement. The description of the attention mechanism is also insufficient. It is unclear how the attention weights are computed and updated. The paper only mentions a sigmoid function, but it does not specify the inputs to this function or whether it is a standard attention mechanism. This lack of detail makes it hard to evaluate the effectiveness of the proposed approach.
2. The paper’s writing is a bit vague in claiming other work’s weaknesses or shortcomings, authors are suggested to make more detailed analysis when claiming a point. E.g.,  In Section 4.5, When discussing the limitations of existing work, It is not clear why "initiating iteration at a fixed length" is computationally expensive. The authors should elaborate on the specific computational bottlenecks associated with fixed-length rollouts. For instance, do they refer to the increased memory consumption due to storing long trajectories, or the computational cost of backpropagating through long sequences? Without these details, the claim lacks sufficient support.
3. The experiment baselines do not sufficiently include the important baseline methods, e.g., the Social-GAN[1], Social-LSTM[2], Social-STGCNN[3], etc. Furthermore, the paper does not analyze collision rates, which is a critical metric for evaluating crowd simulation methods. The reported performance of the PCS method also differs from the original paper, raising questions about the experimental setup and the validity of the comparison.

### Questions
1. Minor questions and suggestions: 
- In the caption of Figure 1, the timeline seems to be the horizontal axis and vertical axis is the various methods. 
- It is suggested to provide explicit descriptions, e.g., when authors describe the current exploration on a combination of rule based and learning based methods, author wrote:'They replace key components of the rule-based model with neural networks and train on real data.', where the ‘ key components' sound vague, what part is replaced? It is important to clarify when providing summary on existing methods.

2. In the paper, it is not clear on the implementation details of the sequential model, however, it is the crucial component to understand the rationality of later residual action generating. For example, In the equation (6), how does a simple MLP capture the intrinsic and stochastic factors in the behaviors? (i.e., whether the incorporated is the relative information, ect).

3. In Section 4.5, When discussing the limitation of existing work, It is not clear why "initiating iteration at a fixed length" is computationally expensive. It is suggested to provide profound analysis and discussion.
4. In equation (7), In the additional bias term, assume the i=100, the coefficient of the last item might be much greater than the actual gap between the actions, could the author explain more on the design here?
5. Based on the equation (5), How is the attention weight learned and updated? From what is written here, it seems to be a simple sigmoid function? Does the author imply any kind of standard attention machism? If not, the term is misleading.
6. In the experiment set ups, the baseline methods did not include some important methods like: Social-GAN, Social-LSTM, Social-STGCNN, etc. And the collision is not analyzed. Besides, one of the baseline methods: PCS does not seem to align with the original paper's performance on the same datasets GC and UCY. Could the author explain if is this caused by different settings or other factors?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper aims to improve crowd simulation methods, which are essential in various domains like traffic management, urban planning, and emergency management. Existing methods, rule-based and learning-based, have their limitations such as lack of authenticity and generalization, respectively. The authors introduce PINE, a framework that infuses physical biases and attention mechanisms into crowd simulation. PINE aims to enhance the authenticity and generalizability of crowd simulations by allowing pedestrians to adaptively adjust their behavior based on different influencing factors. PINE combines rule-based models with neural networks. It introduces modules like Feature Adaptive Extraction Module (FAEM) and Force Attention Module (FAM) to selectively extract and focus on relevant information and influences, improving the simulation's accuracy and physical consistency. A new Variable-step Rollout training algorithm is introduced to address cumulative errors during simulation, aiming to improve the model's performance further. Extensive experiments have been conducted, demonstrating that PINE outperforms state-of-the-art simulation methods in terms of accuracy, physical fidelity, and generalizability. Case studies are also visualized to help readers understand the advantages of this proposed method.

### Strengths
1. PINE introduces a novel framework that combines rule-based models with neural networks, infusing physical biases and attention mechanisms into crowd simulation. The way the physical model and the neural network are combined makes sense. The framework enhances the authenticity and generalizability of crowd simulations, allowing pedestrians to adaptively adjust their behavior based on different influencing factors. Feature Adaptive Extraction Module (FAEM) and Force Attention Module (FAM) have been introduced to selectively extract and focus on relevant information and influences to long trajectories. All the model design reflects the authors' original thinking and insights regarding the crowd simulation problem, which is a very important issue and approach. A new training algorithm is introduced to address cumulative errors during simulation, aiming to improve the model's performance further.

2. PINE has been extensively validated through experiments, demonstrating superior performance in terms of accuracy, physical fidelity, and generalizability compared to state-of-the-art simulation methods. I also enjoy the case study and visualization the authors give. The experiments are strong and promising. The generalization study and ablation study are comprehensive.

3. I can appreciate the way of incorporation of the physical model. To get the optimized force at the output end, the attention mechanism is used to obtain the coefficients for incorporating the forces to simulate the intent of the crowd. The residual action is then used as a “latent force” to help facilitate the limited capacity or missed information from the physical model. To me, it seems that the FAM part is quite interpretable. We will be able to understand each agent's action robustly. Moreover, I like that the problem is defined as a simulation, since the black-box model alone only tells us what to do. With simulation of pedestrians, for example, we can even cut out this particular part as a simulation environment (as long as it is stable and accurate) for the reinforcement learning of the vehicle agent to learn from.

### Weaknesses
1. While PINE aims to improve generalizability, it might still face challenges in adapting to various unforeseen scenarios or extreme conditions in real-world applications. These situations are really the main barriers and challenges in the field. It would be better to discuss more about such anomalies and whether the proposed model is robust enough. Specifically, the paper lacks a rigorous analysis of how the model would perform in situations with sudden changes in crowd density, unexpected obstacles, or unusual pedestrian behaviors that deviate significantly from the training data. The absence of specific experiments or discussion on these aspects makes it difficult to assess the true robustness and reliability of the proposed method in practical, unpredictable environments.

2. Given the complexity and the number of components involved in the PINE framework, it might require significant computational resources for training and simulation. It would be better to have more information regarding the time complexity and time cost compared to previous methods and SFM methods. The paper does not provide a detailed breakdown of the computational cost associated with each module (FAEM, FAM, and the variable-step rollout training). This lack of information makes it challenging to evaluate the practical feasibility of the method, especially when considering real-time simulation requirements or deployment on resource-constrained devices. A comparison of training time, inference time, and memory usage with existing methods would be beneficial.

### Questions
1. The paper mentions that uniform physical rules fail to effectively capture individual differences such as age, gender, and culture in pedestrian behavior. Since w/o residual action results in drastic performance degradation, relying too much on the physical model is indeed harmful. However, is residual action modeled by a single MLP enough? Do you need more advanced structure to help with that? Or, if MLP is way good enough, should we try a simpler RA model for better interpretability?

2. The so-called physical model of social force model is more like a self-defined “physical model” instead of the physical model for natural phenomenon such as the falling of apple or the precession of mercury. The authors are correct in a way that such a physical model has its limitations, so I agree that incorporating deep learning is necessary while the “physical model” provides stability and interpretability. I just wonder whether it would be better to have a more advanced “physical model” such as PDEs and symbolic regression to do the job, rather than the basic Newton's second law of motion (it might be too simple). There are some instances [1-4].

[1] Steven L Brunton, Joshua L Proctor, and J Nathan Kutz. 2016. Discovering governing equations from data by sparse identification of nonlinear dynamical systems. Proceedings of the national academy of sciences 113, 15 (2016), 3932–3937
[2] Udrescu, Silviu-Marian, and Max Tegmark. "AI Feynman: A physics-inspired method for symbolic regression." Science Advances 6.16 (2020): eaay2631.
[3] Michael Schmidt and Hod Lipson. 2009. Distilling free-form natural laws from experimental data. Science 324, 5923 (2009), 81–85
[4] Chen, Yuntian, et al. "Symbolic genetic algorithm for discovering open-form partial differential equations (SGA-PDE)." Physical Review Research 4.2 (2022): 023174.

I am not an expert in this specific area. My judgement is based on our understanding of similar tasks in Reinforcement Learning and Physics+AI.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

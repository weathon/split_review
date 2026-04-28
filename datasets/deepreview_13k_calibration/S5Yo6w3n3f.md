# ODE-based Smoothing Neural Network for Reinforcement Learning Tasks

- Decision: Accept
- Avg Score: 7.25
- Scores: 8, 8, 5, 8

## Abstract
The smoothness of control actions is a significant challenge faced by deep reinforcement learning (RL) techniques in solving optimal control problems. Existing RL-trained policies tend to produce non-smooth actions due to high-frequency input noise and unconstrained Lipschitz constants in neural networks. This article presents a Smooth ODE (SmODE) network capable of simultaneously addressing both causes of unsmooth control actions, thereby enhancing policy performance and robustness under noise condition. We first design a smooth ODE neuron with first-order low-pass filtering expression, which can dynamically filter out high frequency noises of hidden state by a learnable state-based system time constant. Additionally, we construct a state-based mapping function, $g$, and theoretically demonstrate its capacity to control the ODE neuron's Lipschitz constant. Then, based on the above neuronal structure design, we further advanced the SmODE network serving as RL policy approximators. This network is compatible with most existing RL algorithms, offering improved adaptability compared to prior approaches. Various experiments show that our SmODE network demonstrates superior anti-interference capabilities and smoother action outputs than the multi-layer perception and smooth network architectures like LipsNet.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
To adress the issue of smoothness in a policy in RL the authors propose an ODE-based approach to perform a low-pass filtering of the methods.

### Strengths
- The paper deals in an important area of research: finding stable control policies (where smoothness is one aspect) is a relevant area of research
- the derivations are sound and the concepts are explained in a clear way
- overall the paper is written quite well
- the authors perform experiments on different domains
- relevant work is mentioned as far as I can tell

### Weaknesses
 - One key problem is that the authors motivate their method e.g. by: " Filtering methods like Kalman and extended Kalman filtering Chen et al. (2023) effectively suppress noise and reduce output oscillation by estimating the current state from multi-step historical data. These methods work well with Gaussian noise but struggle with non-Gaussian noise." 

However, in the experiment the authors only test on settings with Gaussian noise:
  - MuJoco:  Table 2,3 and 4 specify a Gaussian noise level
  - vehicle trajectory tracking environment: it is unclear what the noise shape is here (perhaps its partial-observable and thus exhibits non-Gaussian noise). In that case the authors should perform an analysis of the shape of stochasticity in this benchmark. 

Either way: I would advise either testing again a Filtering method, such as an extended Kalman filter, re-designing the experiments under non-Gaussian settings and/or clearly present how the vehicle trajectory tracking is a RL problem with non-standard noise.

### Questions
.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a novel neural ODE-based architecture designed for reinforcement learning tasks, specifically addressing the problem of action fluctuation. The authors use ODEs as low-pass filters on network hidden states, with provided theoretical justifications. Their method controls the network's Lipschitz constant in a state-dependent manner, allowing for large actions when needed and smooth actions otherwise. The work demonstrates improved performance over state-of-the-art methods through comprehensive experimentation and ablation studies.

### Strengths
1. The novel approach of integrating smoothing into neural ODEs for resolving action fluctuation is an interesting idea.
2. Having state-dependence is shown to be important for performance, which is important knowledge for the community.
3. The comprehensive ablation studies show that the individual choices made are important for the performance of the method.
4. Testing with multiple noise levels on mujoco tasks is a good way of benchmarking such methods, and the results show clear improvements over existing techniques.
5. The authors provide proofs showing how their method can bound the Lipschitz constant.
6. The authors describe how their ODE integration is performed carefully making choices so that the method is not too expensive for practical use.

### Weaknesses
## Major issues

1. The discussion of limitations is relegated to the appendix, labeled as future work. This placement diminishes the importance of acknowledging the boundaries of the proposed method. A thorough discussion of limitations should be presented in the main body of the paper to provide a balanced view of the work.

3. The explanation of the Neural ODE section could be more pedagogical. Specifically, the transition from the theoretical concept to the practical implementation in the context of reinforcement learning is not clearly articulated. For instance, the discretization process and its implications on the stability and performance of the method are not adequately addressed.

4. The mathematical notation used throughout the paper is often confusing or only partially defined, leading to potential ambiguities.
    -   In Equation 12, the variable 'j' appears without proper quantification. It is likely that a summation over 'j' is missing, which is crucial for the equation's correctness.
    -   The term g(.)^max is used without a clear definition of what the maximum is taken over. Is it over the time domain, the state space, or the input space? This needs to be explicitly defined.
    -   In Equation 14, the function 'l' is defined to take one parameter, but then it appears to take two parameters within the equation. This discrepancy needs to be resolved, possibly by explicitly stating the dependency on two time points after discretization.

5. The use of "Bionic modeling" terminology is not well-established in the reinforcement learning literature and may cause confusion. The paper introduces concepts like membrane capacitance with arbitrary values (0.4-0.6) without providing a clear justification for these specific values. It is unclear whether the model aims for biological plausibility, which would require further justification and validation, or if it is a purely mathematical abstraction, in which case the biological terminology may be misleading.

6. The authors state that Kalman filters are limited by their assumption of Gaussian noise, yet their experimental evaluation only includes Gaussian noise. This does not fully test the robustness of their method under the broader range of conditions that they claim to address.

## Minor Issues

1. Line 096: "Multi-layer perception" should be corrected to "Multi-layer perceptron."

2. Line 332: "Regular" should be "Regularization."

4. Line 376: While DSAC is mentioned as a state-of-the-art method, it's worth noting that newer methods like TQC and CrossQ have shown superior performance in certain benchmarks. However, this does not significantly detract from the paper's contribution, as the focus is on the novel ODE-based approach.

3. Line 746: The phrase "According to Eq. equation 17" should be revised to "According to Eq. 17."

### Questions
How does this work relate to ODE-based Recurrent Model-free RL for POMDPs (https://arxiv.org/abs/2309.14078)?

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a Smooth Ordinary Differential Equation-based Neural Network (SmODE) architecture, designed to address the issue of unsmooth control actions in deep reinforcement learning (RL). The SmODE network mitigates high-frequency input noise and restricts the neural network’s inherent high Lipschitz constants by employing a dual mechanism that combines low-pass filtering with Lipschitz constant control. This approach enhances the smoothness and robustness of the policy.

### Strengths
1. **Innovative Approach**
    - **First Combination of Neural ODE to Address Dual Issues**:
        - This work is the first to attempt using Neural Ordinary Differential Equations (Neural ODE) to simultaneously address high-frequency input noise and action unsmoothness caused by the network’s Lipschitz constants. The SmODE network provides a comprehensive solution by integrating low-pass filtering with Lipschitz constant control, effectively improving policy smoothness and robustness rather than optimizing for a single issue alone. The design cleverly mimics the structure of a classical first-order low-pass filter but replaces the fixed time constant with a state-dependent learnable function. This not only retains the noise suppression capability of the low-pass filter but also enhances the model's adaptability and dynamic response through the learning mechanism. Additionally, it leverages the continuity properties of Neural ODEs.
    - **Dual Smoothing Mechanism**:
        - The SmODE network introduces learnable state-dependent time constants \(\tau(x)\) and state mapping functions \(g(x(t), I(t), t, \theta)\), controlling the rate of state change via the time constants and regulating the Lipschitz constants through the state mapping functions. This simultaneously suppresses high-frequency noise and controls the network’s sensitivity, achieving smooth and robust action outputs.
    - **Biologically-Inspired Neuron Design**:
        - SmODE neurons emulate the characteristics of biological neurons by combining synaptic weights (\(w_{ij}\)), membrane capacitance (\(C_{mi}\)), and resting potential (\(x_{leaki}\)). Through low-pass filtering, they enable adaptive adjustment of state boundaries. This design not only enhances the biological plausibility of the model but also improves its performance and stability in practical control tasks.
2. **Technical Depth**
    - **Theoretical Foundation**:
        - The paper provides formal theorems and proofs (Theorem 1 and Theorem 2), theoretically demonstrating the bounds on hidden states and the upper limits of derivatives, showcasing a deep understanding of Neural ODEs and control theory.
    - **Extensive Experimental Tasks**:
        - The authors conducted comprehensive experimental validations across various reinforcement learning tasks, including vehicle trajectory tracking, linear-quadratic regulation problems, and eight robot control tasks in Mujoco. The experimental results demonstrate that the SmODE network significantly outperforms traditional Multi-Layer Perceptrons (MLP) and methods like LipsNet in terms of action smoothness and noise robustness, showcasing superior control performance.
    - **Validation of Key Component Contributions**:
        - Ablation studies demonstrate the significant contributions of the time constant term and state boundary adjustment term in enhancing action smoothness. By individually removing these key components, the experimental results show a substantial degradation in the smoothness effect of SmODE, further validating the rationality and effectiveness of its design choices.

### Weaknesses
1. **Insufficient Description of the Core Neuron Model (Equation 12)**:
    - While similar works are referenced in the paper, the transition from the general smooth ODE neuron model (Equation 10) to the specific biological neuron model (Equation 12) deserves more detailed exposition, as it serves as the core design of the SmODE network. The roles, value ranges, and impacts on model performance of key parameters (\(w_{ij}\), \(C_{mi}\), \(\gamma_{ij}\), \(\mu_{ij}\)) are not thoroughly discussed. A more comprehensive explanation would enhance the paper's logical flow and motivation. Moreover, the introduction of multiple parameters in Equation 12 increases the model's complexity and raises concerns about the reliability of experimental results due to the extensive parameter tuning space. The introduction of multiple parameters in Equation 12 increases the model's complexity and the difficulty of parameter tuning. There is a lack of clear guidelines or empirical rules for selecting these parameters.
2. **Incomplete Theoretical Assumptions and Proofs**:
    - **Missing Boundedness Assumption for Function \( g(\cdot) \)**:
        - Theorem 1 asserts that the hidden state of the neuron is bounded by the maximum and minimum values of the function \( g(x(t), I(t), t, \theta) \), but it does not sufficiently explain or prove whether \( g(\cdot) \) itself is bounded. If \( g(\cdot) \) is unbounded, the validity of the theorem is questionable.
    - **Incompleteness and Rigorousness of Theorem Proofs**:
        - **Theorem 1**: The proof lacks a detailed discussion on the boundedness of \( g(\cdot) \) and does not adequately explain why \( \frac{dx_i}{dt} \leq 0 \) holds in all cases. The derivation steps for the lower bound \( \min(0, g(\cdot)_{\min_i}) \leq x_i(t) \) are not sufficiently clear.
        - **Theorem 2**: The derivation process lacks detailed explanations regarding the boundary control of \( f(x(t), I(t), t, \theta) \) and \( g(x(t), I(t), t, \theta) \). The origin of the constant \( C \) and its relationship with \( M(\cdot)_i \) are not clearly explained, resulting in the final inequality \( \left| \frac{dx_i(t)}{dt} \right| \leq M(\cdot)_i \cdot C \) lacking sufficient mathematical justification.
3. **Insufficient Discussion on Computational Efficiency**:
    - Although the paper mentions that the training time of SmODE increases due to the use of numerical ODE solvers, it lacks an in-depth discussion of this computational overhead and an analysis of its impact on scalability and real-time performance.
4. **Lack of Direct Comparisons with Some Related Works**:
Related research focuses on addressing action smoothness in reinforcement learning, with methodologies highly relevant to SmODE. Without comparing SmODE to these methods, readers would find it difficult to understand SmODE's specific advantages.
    - Related similar studies such as **"Smooth Filtering Neural Network for Reinforcement Learning"** are not included in the comparisons, potentially missing opportunities to demonstrate the relative advantages of SmODE against the latest methods.
    - Recent relevant methods like **Neural CDEs (2020)** and **Stable Neural Flows (2021)** are not compared experimentally. These methods are relevant to handling continuous-time sequences and controlling stability, aligning closely with the goals of SmODE.

### Questions
1. **Provide a Detailed Description of Equation 12**:
    - Offer a comprehensive explanation of each parameter in Equation 12 (\(w_{ij}\), \(C_{mi}\), \(\gamma_{ij}\), \(\mu_{ij}\)), including their the influences of value ranges, and specific roles in controlling action smoothness. Provide additional theoretical support or empirical results to demonstrate how the introduction of these parameters influences the model's performance.
2. **Discuss Computational Efficiency and Scalability**:
    - Provide a more detailed analysis of the computational overhead, the training time and inference speed of the SmODE network. Explore the influences of the ODE solving process or the number of iterations, to improve the model’s computational efficiency and real-time performance.
3. **Expand Experimental Comparisons and Discussions**:
    - [**Smooth Filtering Neural Network for Reinforcement Learning**](https://ieeexplore.ieee.org/abstract/document/10643291/): This work is highly relevant to the current paper and should be prominently compared to highlight the advantages and characteristics of the proposed method.

### Soundness
3

### Presentation
2

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
The authors propose an ODE that can serve as a neuron in a neural network. They then propose an actor-critic algorithm that incorporates the ODE neuron into the policy network, thereby allowing for smoother action outputs compared to existing methods. The authors present relevant theoretical results as well as extensive empirical validation that showcases the usefulness of their method.

### Strengths
This paper provides a theoretically-sound method for smoothing the action output, which, based on the empirical results, leads to better performance overall. The authors provide useful and sound theoretical results, as well as convincing empirical evidence that shows how their method generally outperforms existing methods. The paper is polished, and presented in an easy-to-read manner. Overall, this paper provides a solid contribution.

### Weaknesses
The authors heavily rely on the Action Fluctuation Ratio (AFR) as the key metric for their implementation and analysis. Given that the AFR was only proposed recently (in Song et al., 2023), the paper would benefit from a more thorough discussion on why this metric is an acceptable one to use. Specifically, the authors should provide a more rigorous justification for using AFR, including a comparison with alternative metrics for quantifying action smoothness. For instance, the authors could explore metrics related to the frequency domain representation of the action sequence, such as the mean weighted frequency. A comparative analysis using multiple metrics would strengthen the paper's argument and provide a more comprehensive evaluation of the proposed method's effectiveness in achieving smooth control.

Similarly, aside from MPC, the other baselines used in the experiments are not well-motivated in the text. In particular, it should be made clearer why the baselines used are the correct ones to use, and why they constitute a reasonably complete set of relevant baselines to consider. The authors should explicitly state why they chose to compare against MLP, LipsNet, and LTC, and justify why these baselines represent the current state-of-the-art or are the most appropriate for evaluating the proposed method. A more detailed discussion of the strengths and weaknesses of each baseline in the context of action smoothing would enhance the paper's experimental design.

Finally, in lines 231-232, “We also think that…” should be framed in a more scientific manner. Appendix C is not convincing either (while it shows an evidence). The statement regarding the adaptive Lipschitz constant constraint in the ablation study should be rephrased using more objective language. Instead of expressing a subjective opinion, the authors should focus on the empirical evidence and provide a quantitative analysis of the results. For example, they could discuss the specific impact of the adaptive constraint on the AFR and performance metrics across different tasks.

### Questions
1.	Theorem 2 is based on the specific setup in Eq (12) according to line 245 on p.5. But the proof does seem to rely on Eq (12). Can you discuss the generalizability of your main results. 
2.	How do the terms added to the loss in Equation 16 affect the performance? What are the guidelines on how to set the two weights (\lambda_1 and \lambda_2)?
3.	What is the computational burden due to the ODE solver?

### Soundness
3

### Presentation
3

### Contribution
3

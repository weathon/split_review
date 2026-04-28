# A deep inverse-mapping model for a flapping robotic wing

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 5, 8, 5

## Abstract
In systems control, the dynamics of a system are governed by modulating its inputs to achieve a desired outcome. For example, to control the thrust of a quad-copter propeller the controller modulates its rotation rate, relying on a straightforward mapping between the input rotation rate and the resulting thrust. This mapping can be inverted to determine the rotation rate needed to generate a desired thrust. However, in complex systems, such as flapping-wing robots where intricate fluid motions are involved, mapping inputs (wing kinematics) to outcomes (aerodynamic forces) is nontrivial and inverting this mapping for real-time control is computationally impractical. Here, we report a machine-learning solution for the inverse mapping of a flapping-wing system based on data from an experimental system we have developed. Our model learns the input wing motion required to generate a desired aerodynamic force outcome. We used a sequence-to-sequence model tailored for time-series data and augmented it with a novel adaptive-spectrum layer that implements representation learning in the frequency domain. To train our model, we developed a flapping wing system that simultaneously measures the wing's aerodynamic force and its 3D motion using high-speed cameras. We demonstrate the performance of our system on an additional open-source dataset of a flapping wing in a different flow regime. Results show superior performance compared with more complex state-of-the-art transformer-based models, with 11\% improvement on the test datasets median loss. Moreover, our model shows superior inference time, making it practical for onboard robotic control. Our open-source data and framework may improve modeling and real-time control of systems governed by complex dynamics, from biomimetic robots to biomedical devices.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper releases a deep learning architecture to model inverse dynamics of a flapping wing which addresses the challenge of controlling such complicated and intricate systems. They also developed an experimental setup to collect data on the wing motion using high speed cameras. Their model uses a sequence-to-sequence framework enhanced with a frequency domain layer for adaptive learning, outperformed baseline models on author collected test data.

### Strengths
1. Extensive hyperparameter search to get optimal results.
2. Data collection is commendable.
3. Valid ablation and limitation sections have been provided.

### Weaknesses
1. The results present in Table 2 does not present more significant information than what is present in figure 5. Instead the ablation results can be moved to the main manuscript from the supplementary material
2. The Seq-2-Seq ASL model does not outperform the transformer on the open source dataset. But does perform better on the authors dataset. An explanation for this would greatly help the contribution of this paper. 
3. The abstract should clarify that the 11% improvement is over the median since over mean the model performs worse than the baselines.

### Questions
1. Around 1000 experiments were performed for the hyperparameter search of the Seq-2-Seq ASL model. Was the same search conducted for other models in Table 2 ?
2. What is the effect of scaling this model on the MAE ? Considering the goal of this effort is to deploy on highly compute constrained platforms, it would be interesting to see if this model scales better than a transformer.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a machine learning approach to control flapping-wing robots by developing a model that determines how wings should move to achieve desired forces. The key innovation is combining a sequence-to-sequence neural network with a new Adaptive Spectrum Layer (ASL) that better handles periodic motions. Tested on experimental data, the approach shows 11% improvement over existing methods and provides practical real-time control capabilities.

### Strengths
**Originality:**
- Novel inverse mapping approach for flapping wing control
- Creative integration of frequency domain processing (ASL) with sequence learning
- New experimental setup combining force and motion measurements
- Innovative application of deep learning to fluid dynamics control

**Quality:**
- Rigorous experimental validation:
  * Two different datasets (air and viscous fluid)
  * Comprehensive ablation studies of ASL components
  * Clear performance metrics and comparisons
- Thorough implementation details:
  * Full hyperparameter specifications
  * Clear architectural choices
  * Reproducible results

**Clarity:**
- Well-structured presentation
- Clear problem formulation and motivation
- Detailed technical explanations with supporting figures
- Comprehensive supplementary materials
- Open-source data and framework

**Significance:**
- Practical impact:
  * Real-time capable control system
  * Improved performance (11% over state-of-art)
  * Direct application to existing robotic systems
- Broader implications:
  * Framework applicable to other complex dynamic systems
  * Potential applications in biomedical devices
  * Open datasets for future research
- Technical contributions:
  * New insights into frequency domain processing
  * Improved understanding of flapping wing dynamics
  * Efficient model architecture design

### Weaknesses
 - typo L418: (forces vs. force and torque) 
- paper mentions different measurement types between datasets without explaining impact on model or justification
- What is the sim2real gap for the real wing-driven robot? How to narrow the sim2real gap to make the research more useful.
- Can you scale to multiple degrees of freedom? how to evaluate the scaling?
- Can you scale to different geometry and material? How to evaluate?
- What are the flight conditions?
- Any analysis of frequency selection? Why 100Hz/210Hz?
- More implementation details could be provided: synchronization for different sensors, delay?
- How is the sensor data aligned between cameras (10,000 fps) and force sensors (5,000 samples/sec)?
- What's the real-time performance on actual hardware? Processing delays?
- Any stability analysis or guarantees for the control system?
- How does the system handle disturbances or noise?
- Is there any theoretical justification for the model architecture choices?
- How generalizable is this approach across different Reynolds numbers?
- How about the performance of some basic NN structures, like MLP/LSTM/RNN?

### Questions
One of the contribution is the whole pipeline to collect the data. As for the ASL structure, I am not sure the necessity of the complex network structure. One core aspect of the paper is modeling aerodynamics, and similar work exists in the UAV field, such as NeuralFly. Therefore, this core contribution or novelty needs to be better clarified by the authors.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a novel method for mapping the complex dynamics of a wing flapping to output thrust. The method employs a sequence to sequence model with a GRU encoder and decoder. The authors present a novel layer dubbed the Adaptive Sequence Layer (ASL) to attend to features across the frequency spectrum of the input sequence. The authors use two datasets: one is created by building a mechanical flapping wing and the second is an open source wing flapping dataset. The Seq2Seq+ASL method outperforms baseline methods such as Seq2Seq without ASL and a Transformer. The paper makes a clear and useful contribution to literature.

### Strengths
The paper has a number of strengths. The experimental setup is unique and interesting to the robotics community. The authors present a novel layer Adaptive Spectrum Layer (ASL), which in the experiments section is shown to improve the overall prediction performance. The choice of baselines are appropriate. The paper is well presented and clear to follow. The paper is significant.

### Weaknesses
Despite the strengths of the paper, there are a few weaknesses, but these should be easily addressed. Some of the key figures such as Fig. 1 and 2 are quite small. A recommendation would be to increase the size of these at the expense of some of the text of by resizing Fig. 5. For example, the abstract and introduction are a little on the verbose side. Nevertheless, these paragraphs are clear. 

There are many comparisons between different baseline methods, which is good. However, it would be beneficial to have a statistical test to show that the improvement in performance between Seq2Seq+ASL and the other baseline methods is statistically significant. In Figure 5, there is not that much difference between the Seq2Seq and Transformer models. A statistical test such as Mann Whitney U-test to compare the differences between the MAE losses. I leave the choice of statistical test to the authors discretion.

### Questions
There are a few questions I have for the authors and these are included below. 

Please would the authors perform the statistical test to compare the statistical differences between MAE of their method against the baselines. 

Since ASL is a novel contribution of the authors, I would emphasise this to a greater degree in the abstract and the introduction. Is there a reason for not doing this?

Please could you point me to where you state the size of the dataset and evaluation sets used to compare results against the baselines.

I have a further optional suggestion for authors. Can the authors comment on the frequency spectrum present in the data? 

This question is more one of curiosity, but may be of interest to other readers: I have a question about the RFFT and the IRFFT. How do you implement this in practice? I had assumed that most “fast” implementations are non-differentiable and I am curious which implementation you used.

### Soundness
4

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
3

### Summary
This paper presented an adaptive spectrum layer enhanced seq2sep deep learning framework to learn the inverse-mapping model of a flapping robotic wing. The employed adaptive spectrum layer is found to have the advantage of learning the periodic features in the frequency domain. Overall, the presentation is clear, and a real experimental test is conducted. However, some important improvements are further needed, mainly including the theoretical contributions and more practical tests.

### Strengths
1. Adaptive spectrum layer enhanced seq2sep learning framework.
2. Real experimental tests.
3. Clear presentation.

### Weaknesses
1. It seems the main contribution of this paper is the introduction of the adaptive spectrum layer in seq2sep prediction missions. Empirical effects are provided in the results (although the improvement provided in Table 2 seems not very promising). The innovation is relatively weak. The theoretical principle and intuitive explanation behind the learning architecture should be further abstracted and discussed. Specifically, the paper lacks a rigorous analysis of why the adaptive spectrum layer is beneficial for this specific inverse mapping problem. A more in-depth discussion of the spectral characteristics of the flapping wing dynamics and how the proposed layer exploits these characteristics is needed. The current explanation is too high-level and does not provide sufficient insight into the mechanism behind the observed performance gains, which appear marginal.

2. The implemented experiments are relatively simple. The real applied scenarios are usually more complicated, such as external disturbance, unknown dynamic model, and actuator uncertainty. The generalization problem of the developed learning architecture is not considered.  To improve contributions, it is highly recommended to further include the learned inverse model in the online control framework, not just offline demonstration on the dataset of a flapping wing. Moreover, a comparison with a traditional control method (e.g., MPC) is needed. The current experimental setup only demonstrates the feasibility of the approach in a controlled environment. The lack of robustness analysis and performance evaluation under more realistic conditions limits the practical impact of the work. The paper should address how the proposed method would perform with noisy sensor data, model uncertainties, and external disturbances.

3. Some presentation errors. Every abbreviation that appears first in an article should be given its full name, such as FFT. All symbols employed in Fig 3 should be illustrated.

### Questions
1. The equation (2) is called the one-step-ahead prediction model. Does \tau refer to the one-step size? However, \tau in equation (1) is defined as a period. It is confused.

2. Through the learned inverse model, the desired attitude can be obtained from the desired force. In real application, how to plan the desired force and how to implement the obtained attitude?  A special control framework can be provided to illustrate the implementation of the learned inverse model. It is wondered if the uncertainty that exists in the control loop would influence the learning performance.

### Soundness
2

### Presentation
3

### Contribution
2

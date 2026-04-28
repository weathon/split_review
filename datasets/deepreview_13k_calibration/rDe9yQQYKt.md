# TS-LIF: A Temporal Segment Spiking Neuron Network for Time Series Forecasting

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Spiking Neural Networks (SNNs) offer a promising, biologically inspired approach for processing spatiotemporal data, particularly for time series forecasting.
However, conventional neuron models like the Leaky Integrate-and-Fire (LIF) struggle to capture long-term dependencies and effectively process multi-scale temporal dynamics.
To overcome these limitations, we introduce the Temporal Segment Leaky Integrate-and-Fire (TS-LIF) model, featuring a novel dual-compartment architecture.
The dendritic and somatic compartments specialize in capturing distinct frequency components, providing functional heterogeneity that enhances the neuron's ability to process both low- and high-frequency information.
Furthermore, the newly introduced direct somatic current injection reduces information loss during intra-neuronal transmission, while dendritic spike generation improves multi-scale information extraction.
We provide a theoretical stability analysis of the TS-LIF model and explain how each compartment contributes to distinct frequency response characteristics.
Experimental results show that TS-LIF outperforms traditional SNNs in time series forecasting, demonstrating better accuracy and robustness, even with missing data.
TS-LIF advances the application of SNNs in time-series forecasting, providing a biologically inspired approach that captures complex temporal dynamics and offers potential for practical implementation in diverse forecasting scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces TS-LIF, a novel dual-compartment spiking neuron model for time series forecasting. The authors argue that traditional LIF models struggle to capture long-term dependencies and multi-scale temporal dynamics. Their proposed TS-LIF model incorporates dendritic and somatic compartments to process different frequency components, aiming to improve the accuracy and robustness of time series forecasting.

### Strengths
1. **Novelty**

The introduction of the TS-LIF model with its dual-compartment architecture (and signal decomposition), together its application to series forecasting is a novel contribution to the field of spiking neural networks .

2. **Placement**

The relationship of the work as respect to previous ones is well discussed.

3. **Performance Improvement**

The experimental results demonstrate clear improvements over traditional LIF-based SNNs and even some ANNs on standard benchmark datasets.

4. **Robustness**

The model shows good robustness in the face of missing data, which is a common challenge in real-world time series data.

### Weaknesses
1. **Limited Biological Plausibility? **

While the authors claim biological inspiration, the specific implementation of the dual-compartment model may not have direct biological correlates. 
E.g. I like the idea of decomposing of the input signal in different frequencies. (Maybe Hierarchical temporal memory could referenced here). Can the authors discuss more on the biological plausibility of this phenomenon?

2. ** Over-Reliance on Benchmark Comparisons** 

The paper heavily focuses on comparing TS-LIF with existing models on benchmark datasets. While this demonstrates performance improvements, it doesn't provide a deep understanding of the model's behavior. A more in-depth analysis of the model's inner workings, including how the dendritic and somatic compartments interact and contribute to the final prediction, would be beneficial.

It would be nice to some example of the network dynamics in response to data input, for different dataset, before and after training, while forecasting, populations analysis (such as the average power spectrum for different compartment over many realizations of the experiment).

### Questions
- Have you explored the computational efficiency of TS-LIF compared to traditional ANNs, particularly in terms of energy consumption?

- Are there specific types of time series data or forecasting tasks where TS-LIF might be particularly well-suited or, conversely, might struggle?
- How does the choice of the weighting parameter κ in the mixed spike output affect the model's performance? Is there an optimal way to determine this parameter?

- I suggest to include those references on spiking networks that are relevant for the topic. [1] is a biologically implementation of RFLO in spiking networks, [2] discuss learning temporal sequences leveraging multi-compartment neurons and local errors, [3] discuss learning in deep architectures thanks to multi-compartment neurons.

[1] Bellec, Guillaume, et al. "A solution to the learning dilemma for recurrent networks of spiking neurons." Nature communications 11.1 (2020): 3625.

[2] Capone, Cristiano, et al. "Beyond spiking networks: the computational advantages of dendritic amplification and input segregation." Proceedings of the National Academy of Sciences 120.49 (2023): e2220743120.

[3] Payeur, Alexandre, et al. "Burst-dependent synaptic plasticity can coordinate learning in hierarchical circuits." Nature neuroscience 24.7 (2021): 1010-1019.

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
4

### Summary
This article improves the dynamical characteristics of the LIF neuron and proposes a TS-LIF model for time series forecasting, incorporating interactions between dendrites and soma. The authors analyze the robustness and functionality of the improved dynamical system's different components and validate through experiments that TS-LIF outperforms the standard LIF on time series prediction benchmarks.

### Strengths
* The analysis of the improved model is quite thorough.  
* Experiments demonstrate that it outperforms previous SNN-based methods.  
* The writing is clear and easy to understand.

### Weaknesses
The main issue with this article is the somewhat unclear connection between the motivation and contributions. I believe the authors need to clarify their motivation for using a spiking model for time series tasks.

If the goal of using a spiking model is to achieve better performance, the following points should be addressed:

* If the spiking model is used to improve performance, it should be compared with the latest state-of-the-art methods, such as [1] and [2].
* In the introduction, it states, "In contrast, SNNs, with their event-driven and sparse computational architecture, can offer a more efficient solution, particularly for applications that involve sparse temporal events and demand low energy consumption." If the motivation for using a spiking model is to achieve low energy consumption, then additional experiments on hardware platforms should be provided to verify the model's energy efficiency, including specific tests on platforms like FPGA, GPU, and neuromorphic chips [3] to support this claim.
* The authors improved the model by introducing input stimuli into the soma, achieving a symmetric dynamical form. While this improvement indeed enhances performance, it also introduces additional computational overhead. I believe it would be beneficial to compare this model to others in terms of parameter count, training time, and FLOPs to illustrate the advantages of using a spiking model.

In the abstract, the authors mention that the spiking model is a biologically inspired neural network. If the purpose of this work is to validate the biological plausibility of this approach (or if the motivation is computational neuroscience rather than merely solving an engineering problem), then I believe the following points should be further addressed.

* In the proposed dynamic form where input stimuli are added to the soma rather than only to the dendrites, is there evidence that this mechanism is employed in the brain for similar time series forecasting processes?
* Can dynamics or data similar to TS-LIF be observed in the biological brain, thereby validating that TS-LIF indeed simulates brain mechanisms?
* It is suggested that the authors theoretically connect "shortcuts in soma" to analogous time series prediction processes in the brain, such as through predictive coding, active inference, etc. (This is optional, as it is challenging, but it would greatly enhance the contribution of the paper.)

### Questions
Please see weaknesses above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
To enhance the ability of SNNs to model long-term dependencies and process multi-scale temporal information, this paper proposes the Temporal Segment LIF (TS-LIF) model, which builds upon the existing Two-Compartment LIF (TC-LIF) model. The two compartments in TS-LIF are specifically designed to process low- and high-frequency signals, respectively. Theoretical analysis demonstrates the stability of the TS-LIF model, and experiments on time series forecasting tasks show that TS-LIF outperforms the standard LIF model.

### Strengths
- Effectively modeling long-range dependencies remains an important yet unresolved challenge in SNNs. 

- Using two compartments to separately capture low- and high-frequency information is novel.

### Weaknesses
 - The primary concern lies in the experimental design. This paper evaluates the TS-LIF model by integrating it with TCN, GRU, and Transformer architectures on time series forecasting tasks. However, it is questionable whether these setups and datasets effectively assess the ability of spiking neuron models to capture long-term dependencies. Given that GRU, TCN, and Transformers already have strong long-sequence modeling capabilities, the performance of SNNs may not be adequately represented.

- The paper lacks comparisons with existing spiking neuron models such as TC-LIF [1], LM-H [2], CLIF [3], and BHRF [4].

- It is biologically questionable whether the input current can be applied to both the dendrite and soma while producing weighted spikes.

### Questions
- How many time steps are used in TS-LIF on the time series forecasting tasks?

- What are the specific values of the hyperparameters used in TS-LIF on the time series experiments? Are there established principles for determining these hyperparameters, and what effects do they have on model performance?

- What is the value of the decay factor in the LIF baselines presented in Table 1? Have you examined the influence of the decay factor on performance in these time series tasks?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose an extension of the dual-compartment Leaky Integrate-and-Fire model with the aim of improving time-series forecasting, by capturing both low- and high-frequency input in their model. The authors validate the prediction accuracy of their model compared to other models on different datasets and demonstrate that their model performs slightly better.

### Strengths
The proposed model is interesting, and the paper is generally well-written. In addition, the authors include several lines of analysis and benchmark their model on four different timeseries datasets - the preliminaries section is also well written.

### Weaknesses
I have several concerns regarding the work.

1. **Questionable biological realism.** The proposed idea of modeling the voltage of the dendrites and soma separately is interesting (although not new [1]). However, adding the dendritic and somatic spike outputs using a weighted sum (Eq. 6) is biologically questionable, as the outputs of the units now become graded and are no longer spiking. How is this modeling step reconciled in biology?  If the model is intended to capture the biology, then I would expect to see more comparisons to actual electrophysiological recordings of neurons. The authors should clarify the biological plausibility of this weighted summation, as it deviates from the typical all-or-none nature of neuronal spiking, and provide justification for this modeling choice.

2. **Is the model more efficient than other neural networks?** You state that TCNs, Autofromers, and Transformers require more memory and computational resources (stated on line 49 and 145-148). Does your model overcome this issue? I would assume that your model would also incur significant resource demands during training. Furthermore, it is not clear how your model could be ported to a neuromorphic computer for inference, as the output is not strictly spiking. The authors need to provide a detailed analysis of the computational cost of their model, including memory usage and training time, and compare it to the resource requirements of the other models mentioned. The authors should also discuss the implications of the non-spiking output for neuromorphic hardware implementation.

3. **Missing controls.** The author's motivation for the work is that spiking neurons struggle to capture long-term dependencies in temporal input. However, they do not mention (or compare to) works using trainable membrane time constants [2] or trainable adaptive firing rates [3], which have been shown to significantly improve SNN performance on different time-series datasets. Simply making membrane time constant trainable can even make single-spike SNNs outperform standard multi-spike LIF-SNNs on complex temporal datasets [4]. I would suggest the authors compare their model to models in which the membrane time constant and adaptive firing rates are learned. The authors should include a comparison with these more advanced SNN models to demonstrate the unique advantages of their approach over existing methods for capturing long-term dependencies. A more comprehensive comparison is needed to justify the novelty of their approach.

4. **Confusion regarding the analysis.** In the stability analysis (Sec. 4.2) the authors use the equations of the dual comportment model (Eq. 4) rather than their model (Eq. 5). Why was this done? Furthermore, the analysis was only conducted on the homogenous part of the equations, please explain why this assumption can be made. I am also unsure why this analysis was done, as – unlike standard artificial neural networks – the output of spiking neurons is bounded, so why would we need to analyze these conditions? Lastly, where did you utilize this analysis in your work (e.g. for setting hyperparameters or initial weights)? The authors need to clarify why the stability analysis was performed on the homogeneous part of the equations and how this analysis is relevant to the performance of their model. The authors should also explain how the results of the stability analysis were used to guide the design and training of their model.

### Questions
### Questions:
- What is the reason for introducing equation 3 on page 4? This was not used anywhere else.
- I am not familiar with the frequency response analysis (Sec. 4.3). Perhaps you could provide more background on what this is measuring, why this was done, and where it is used. For example, how do we interpret the values of H_d(z) and H_s(d)? Shouldn’t the low frequencies and high-frequencies have units Hz (line 341-343)? Also, why is w=pi equal to high-frequency?
- What are the top row numbers in Table 1? Are these L? If not, what are they and what was L set to?
- Why does your model outperform the Transformer architecture (e.g. iTransformer)? SNNs do not usually outperform non-spiking neural networks. Please try to discuss this.
- Can you also discuss why your model might perform better on certain datasets? i.e. how certain frequency information is discarded by the other models.
- Did you use surrogate gradients for training? 
- In Figure 2, what do training timesteps refer to? Is this the number of training epochs or gradient updates?
- In the robustness evaluation you only use the Electricity dataset. However, this dataset seems to be “easily solved” using other models under different ratios of missing values, making it hard to infer if your model is better – perhaps you could run your analysis on a harder dataset (e.g. Metr-la)?
- What are the main limitations of your work – I would suggest adding a discussion to your paper.
- Is the code publicly available?
### Additional feedback to improve your paper:
- I would suggest moving the Temporal Analysis (Sec. 5.3.1) before the benchmarking section, as this allows the reader to get a better feel for the model early on.
- If possible, I would include multiple training runs with different random seeds and include some statistical analysis to better compare the results in Table 1, as many of the results are very similar, making it hard to know if this is due to weight initialization or not. Also, what are the shaded regions in Fig. 2 (eg. SD or SEM)?
- Typo in Fig. 2 plot 2 y-label.
- Missing reference for iTransformer (line 378).

### Soundness
2

### Presentation
3

### Contribution
2

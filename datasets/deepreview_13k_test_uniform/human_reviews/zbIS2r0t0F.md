# Allostatic Control of Persistent States in Spiking Neural Networks for Perception and Computation

- Decision: Reject
- Scores: 5, 3, 3, 3, 3

## Abstract
We introduce a novel model for updating perceptual beliefs about the environment
by extending the concept of Allostasis to the control of internal representations.
Allostasis is a fundamental regulatory mechanism observed in animal physiology
that orchestrates responses to maintain a dynamic equilibrium in bodily needs and
internal states. In this paper, we focus on an application in numerical cognition,
where a bump of activity in an attractor network is used as a spatial-numerical
representation. While existing neural networks can maintain persistent states, to
date, there is no unified framework for dynamically controlling spatial changes in
neuronal activity in response to enviromental changes. To address this, we couple
a well-known allostatic microcircuit, the Hammel model, with a ring attractor, re-
sulting in a Spiking Neural Network architecture that can modulate the location of
the bump as a function of some reference input. This localised activity in turn is
used as a perceptual belief in a simulated subitization task – a quick enumeration
process without counting. We provide a general procedure to fine-tune the model
and demonstrate the successful control of the bump location. We also study the
response time in the model with respect to changes in parameters and compare
it with biological data. Finally, we analyze the dynamics of the network to un-
derstand the selectivity and specificity of different neurons to different categories
present in the input. The results of this paper, particularly the mechanism for mov-
ing persistent states, are not limited to numerical cognition but can be applied to a
wide range of tasks involving similar representations.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces AlloNet, a spiking neural network architecture that incorporates an allostatic control mechanism for the regulation of persistent states. The authors use a ring attractor network coupled with a Hammel model to achieve dynamic control of spatial changes in neuronal activity. The model is applied to a numerical cognition task (subitization) to demonstrate its ability to modulate the location of a bump of activity as a function of a reference input. 

The main idea appears to be original and effective, however the relevance of the model, such as biological plausibility and comparison with other models could be better discussed.

### Strengths
1. Novelty of the Approach
Integrating an allostatic control mechanism into a spiking neural network architecture is a novel approach with potential implications for understanding self-regulation in neural systems.    

2. Dynamic Control of Persistent States
The model successfully demonstrates the dynamic control of persistent states in response to environmental changes, a crucial aspect of cognitive processing.    

3. Qualitative Reproduction of Behavioral Aspects
AlloNet qualitatively reproduces certain behavioral aspects of subitization, such as the relationship between reaction time and numerosity.

### Weaknesses
Limited Biological Plausibility: While the model draws inspiration from biological systems like the Hammel model for temperature regulation, the direct application of such a model to numerical cognition might oversimplify the underlying biological mechanisms.

Specificity of the Model: The paper focuses heavily on subitization as an application. It would be beneficial to explore additional cognitive tasks to demonstrate the generalizability of AlloNet.

### Questions
-I suggest to quickly introduce the Hammel model, for helping the reader.

-Could the authors elaborate on the biological plausibility of using the Hammel model, specifically in the context of numerical cognition? Are there any alternative biological mechanisms that might be more relevant?

-How does AlloNet compare to other models of numerical cognition in terms of performance and biological plausibility?

-What are the potential implications of this model for understanding cognitive deficits or disorders related to numerical processing?

Minor

-Caption of Fig5 should be more clear. E.g. what is panel B exactly, make clearer what colors refer to. (are bumps of different ring attractors?).

-References to figure 4 should be “Fig4” rather than just “4”.

-There is a missing dot at the end of the abstract, and at the end of figure 4 caption.

-fig1d is not readable

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents the AlloNet model, which applies allostatic control principles to spiking neural networks to maintain adaptable, persistent internal states. By extending the biological concept of allostasis, the authors enable a ring attractor network to dynamically align internal representations with external stimuli. The model is specifically applied to a subitization task, where it demonstrates the ability to align internal numerical representations with external stimuli through an attractor network’s localized bump of activity.

### Strengths
The authors provide a novel approach to applying allostatic principles to control internal representations within spiking neural networks. This approach may inspire further cross-disciplinary exploration of allostasis and neural network control. In particular, the use of allostasis as a tool of synchronizing the alignment between internal representations and external stimuli could make the model useful in applications requiring real-time adaptability, such as robotics or artificial agents interacting with unpredictable environments.

### Weaknesses
* The paper presents allostasis as a beneficial mechanism but does not sufficiently compare it to traditional homeostatic mechanisms or other neural adaptation frameworks. This limits understanding of when allostatic control is most useful or essential, making it difficult to gauge the model's full significance

* The experimental setup is limited to idealized, controlled tasks. Real-world applications, however, typically involve noisy, unpredictable inputs that can disrupt internal representations, which this model might struggle with. Current experiments do not address such robustness.

* The motivation for using a ring attractor with a "bump of activity" as the representation for the task of numerical cognition (e.g., subitizing) is not clear. What is the (systems) neuroscience evidence for this? 

* The authors note that error rates increase with numerosity and time, but more in-depth insights into the reasons for these errors, such as bump instability, could clarify model limitations

### Questions
* Is the bump instability, in Fig. 5, influenced primarily by synaptic time constants, or are other factors like network noise equally contributory?

* It would be interesting to see the AlloNet benchmarked against other attractor models that handle drift, like ring attractor networks with stabilizing feedback (e.g., [Accurate Path Integration in Continuous Attractor Network Models of Grid Cells
](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000291))

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a mechanism to control the activity of spiking neural networks through allostasis, in order to perform a subitising task. The proposed architecture uses the Hammel Model to regulate internal beliefs associated with the task in response to stimuli, and this is used to control bump activity on a ring attractor that encodes numerosity. The authors compare observed reaction times from their model to those of humans performing the same task, and are able to reproduce certain human behavioural responses with their model. They also assess the impact of the value of the neurons' time constant on task performance, and compare a single neurons' activity profile to known neural dynamics for subitising in humans.

### Strengths
* The proposed model is original to my knowledge, and is fairly simple to understand.
* The authors have compared observations from their models such as reaction times to those of humans performing the same task.
* A testable prediction, i.e., that small numerosities are encoded using a magnitude-based system (ring attractor in this case, which is central to the model), could potentially be validated using experiments with animals/humans.

### Weaknesses
* While the authors are able to recapitulate some observations in humans using their model, i.e., that reaction times increase with numerosity (for a specific value of the time constant), the actual reactions times from the model are far greater than human reaction times (almost 10000 ms vs less than 500 ms) ([Dehaene, 2011](https://psycnet.apa.org/record/2011-10610-000); [Kutter et al., 2023](https://www.nature.com/articles/s41562-023-01709-3)). Do the authors have an explanation for why this is the case, and could it be resolved with better choices for hyperparameters?
* I'm not entirely convinced with the authors' argument that they are able to properly reproduce reaction time patterns. The sharp jump in reaction time for a numerosity of 4 is only observed with a different, faster time constant value of 900ms, while the gradual increase in reaction times with numerosity is only observed with a slower time constant of 1000ms. Furthermore, in the 900ms case, the reaction times for lower numerosities do not match the human data at all, as the authors admit. Could the authors clarify this? I would expect the model to match human observations for a single value of the time constant in order to claim that it reproduces experimental results.
* The model is evaluated only on a single task, i.e., subitising. Especially given the use of a ring attractor and the authors' claims of the model's generalisability, it would be important to evaluate the model on other tasks involving numerosity estimation or tracking a magnitude, such as head direction integration ([Valerio & Taube, 2012](https://www.nature.com/articles/nn.3215)) or average estimation ([Lee & Ma, 2020](https://cognitivesciencesociety.org/cogsci20/papers/0304/0304.pdf)).
* The task is also limited in that it restricts numerosity from 1 to 4. To better compare the observations from the model to previous experiments ([Kutter et al., 2023](https://www.nature.com/articles/s41562-023-01709-3)), the authors should incorporate both small and large numbers (from 0 to 9, for example). If the authors want to align their work better with [Kutter et al. (2023)](https://www.nature.com/articles/s41562-023-01709-3), two different representations could be used for 0-4 vs 5-9 – and in this case it would be important to test whether discrete attractors (fixed points for each of 0-4) match the data better than when using a ring attractor.
* There are other issues with the results and their interpretation. For example, in Fig. 3B, it is not clear how much more variable the reaction times are for higher numerosities with longer time constants (as claimed on line 312). Furthermore, from Fig. 3D, it seems that the "quality score" is very low for numerosity 3 and longer time constants (while for shorter time constants, quality is 0 for numerosity 2 but quality is higher for 3), why is this the case, and is there any experimental evidence of this in animals/humans?
* The authors claim that the neural dynamics of their model are similar to those of several brain regions in human recordings, but this is not substantiated with a metric or even a plot showing qualitative similarity. Furthermore, some of the analysis of neuronal responses has only been done for a single, arbitrary neuron, but it would be important to look at population responses when making comparisons to human data.
* Another weakness is the specificity of these results to hyperparameter and architectural choices. The lack of learning also makes it harder to adapt this model to more complex tasks.
* Finally, the writing lacks clarity and contains grammatical, formatting and some typographical issues. Examples:

  * Line 50 ("can represent to track changes...", unclear what this means), Line 53 ("resemble to the" -> "resemble the"), Line 158-159 ("functions to take input for.."), Line 249 ("in an standard..."), Line 463-465 (sentences are vague, "we allowed to work on"), etc.
  * Several in-text citations are not properly enclosed within brackets.
  * "Excitatiory" -> "Excitatory" (Table 1), inconsistent use of "ise" vs "ize" (British vs American English), "... as a computation model ..." -> "computational", lack of proper spacing before and after parentheses, etc.

  I would encourage the authors to carefully revise the paper to improve its clarity and fix any other grammatical/typographical issues.

### Questions
See the Weaknesses section. I have some additional questions:
* I don't entirely understand the use of a ring attractor for this task. For a number line representation, wouldn't a bounded line attractor be a better idea, especially as it does not wrap around from the maximum to the minimum? Furthermore, the use of a continuous attractor makes the representation more akin to estimation rather than categorisation/subitising, and would align better with work such as [Piazza et al. (2002)](https://www.sciencedirect.com/science/article/abs/pii/S1053811901909802?via%3Dihub) claiming that counting and subitising use the same neural circuitry, as opposed to [Kutter et al. (2023)](https://www.nature.com/articles/s41562-023-01709-3). Could the authors clarify this and correct me if I have misunderstood something?
* How do the authors choose the various hyperparameters mentioned in Table 1? Have the authors tested the robustness of the results to changes in hyperparameters apart from the time constant?

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper investigates how structured networks, like ring attractors, control bump activity in response to external stimuli? The authors propose a network model combining a Hammel model and ring attractor network, with high/low gain modulation neurons driving the bump shift to align with an external stimulus. They argue that this model, due to its control over bump positioning, could model subitization (rapid counting) and compare it to biological data.

### Strengths
1. The authors propose a novel network model based on the ring attractor, enhanced with high/low gain modulation neurons to manage bump shifts, with the Hammel model controlling these shifts. This enables flexible positioning of the bump to match external signals.
2. Some aspects of the model’s performance on counting tasks align with human data, particularly when varying the synaptic time constant.

### Weaknesses
1. The counting task demonstration is very simple; the numerical information is directly encoded in the external signal’s firing rate.
2. Although certain model properties align with human data, they do so under varying synaptic time constants, which are not well explained. Additionally, the model’s reaction times are significantly slower than human responses, by about an order of magnitude.
3. The necessity of using a spiking neural network is not adequately justified.
4. The model’s structure, specifically the gain modulation neurons and the Hammel model component, lacks biological explanation.
5. The network dynamics and mechanisms are underexplained. For instance, in the connection weight formula $w_{ij}$, the term $d_{ij}$ is undefined, though it appears to represent the distance between neurons in the ring.


### Mino 
1. In Equation 1, $d_{ij}$ is undefined.
2. Figure 1, with its four subplots, could be clearer if organized differently.
3. In Figure 2, specify units for the x-axis (probably ms).
4. The synaptic decay constants \tau used are unusually long compared to standard neuron models. More explanation of these values and their role would improve readability.

### Questions
1. How did you decide on this setup, specifically the use of high/low gain modulation neurons to drive shifts and the Hammel model to control them? Is there biological evidence supporting these choices?
2. Could a similar task be achieved with a rate model? If so, how would its reaction time compare to that of the spiking model?
3. The alpha synapse decay constant for HGM and LGM is approximately 1000ms, which is unusually long for neurons. Could you provide more reasoning behind this choice?
4. The input setup is unclear. Do the four Poisson spike generators fire at the same rate? If not, how do they differ, and why is numerical information encoded in firing rates? Is there experimental evidence for this encoding, or could a different encoding method (like one-hot vectors or embeddings) be used?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work develops a framework that dynamically adjusts representation based on environmental inputs, drawing inspiration from the body’s temperature regulation system and incorporating the concept of allostasis. To encode stimuli, the model employs a ring attractor network, while an allostasis module called “Hammel model” serves to compare internal and external variables. This module then outputs gain control signals to drive the ring attractor’s response moving. The model was verified by a subitizing task.

### Strengths
1.	The introduction section provides a comprehensive overview of both numerosity and attractor networks.
2.	The integration of physiological concepts into neural circuit modeling is innovative and inspiring.

### Weaknesses
1.	Improper Citations:  For instance, in lines 173-174, citing Zhang, K. (1996) is essential for discussing the asymmetry in continuous attractor connections. Additionally, it appears that Fig. 1c is likely influenced by Fig. 1d in Wilson, R.I. (2023), but lacks appropriate citation.
2.	Lack of Clarity on Network Dynamics and Analysis: The model does not provide a clear definition of network dynamics or a detailed theoretical analysis of the results.
3.	Biologically Implausible Model Setup: The model’s structure and parameters are set in bio-unplausible ways. Specifically:
	- The synaptic time constants far exceed the plausible range, making the comparison across time constants in Figs. 4 and 5 less meaningful.
	- LGM and HGM neurons were designated as inhibitory. I agree that it is a feasible way to drive the ring attractor, but there has been both experimental and theoretical evidence showing that P-EN neurons in Drosophila brains fulfill this role as excitatory neurons (see Zhang, W., Wu, Y. N., & Wu, S., 2022; Mussells Pires, P., Zhang, L., Parache, V., Abbott, L. F., & Maimon, G., 2024).
4.	Failure to Model Human Behavior Accurately: Although section 3.1 attempts a loose comparison between the model and human behavior, the model does not successfully replicate human behavioral patterns.
5.	Unpolished text and figures: The text contains several typos, unified terminologies and missing punctuation.

### Questions
1.	There’s a saying suggesting that the number line is organized not linearly but log-linearly (Testolin, A., & McClelland, J. L., 2021). Could the present model still function effectively if the ring attractor network were replaced with a log-linear number line?
2.	Ideally, each point on the ring attractor should be neutrally stable, meaning the probability of bump initiation would be equal at any point on the ring. However, the initiation point significantly affects reaction time. How do you ensure the bump consistently initiates from the same point each time?
3.	In Eq. 4, should it be V_th-h so that the potential is below the threshold? Also, could you clarify lines 241-243 preceding Eq. 4? I ask because, in my understanding, the bump should remain stable as long as LGM and HGM neurons are firing equally but not necessarily silent.

### Soundness
2

### Presentation
2

### Contribution
2

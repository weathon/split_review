# Collective variables of neural networks: empirical time evolution and scaling laws

- Decision: Reject
- Avg Score: 6.00
- Scores: 3, 8, 5, 8

## Abstract
This work presents a novel means for understanding learning dynamics and scaling relations in neural networks.
We show that certain measures on the spectrum of the empirical neural tangent kernel, specifically entropy and trace, yield insight into the representations learned by a neural network and how these can be improved through architecture scaling.
These results are demonstrated first on test cases before being shown on more complex networks, including transformers, auto-encoders, graph neural networks, and reinforcement learning studies.
In testing on a wide range of architectures, we highlight the universal nature of training dynamics and further discuss how it can be used to understand the mechanisms behind learning in neural networks.
We identify two such dominant mechanisms present throughout machine learning training.
The first, information compression, is seen through a reduction in the entropy of the NTK spectrum during training, and occurs predominantly in small neural networks.
The second, coined structure formation, is seen through an increasing entropy and thus, the creation of structure in the neural network representations beyond the prior established by the network at initialization.
Due to the ubiquity of the latter in deep neural network architectures and its flexibility in the creation of feature-rich representations, we argue that this form of evolution of the network's entropy be considered the onset of a deep learning regime.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors use entropy and trace of the neural tangent kernel to understand the learning dynamics of neural network esp in regard to architecture scaling. They claim to see initial entropy decrease termed information compression and later entropy increase termed structure formation. They try to identify a deep learning regime. They also show how entropy and trace chance for various architecture-task combinations.

### Strengths
The idea of analysing the entropy and scale of the NTK during training seems novel.

The authors have done a fair number of experiments across relevant architecture-task combinations.

### Weaknesses
In section 3.1, drawing conclusions on scaling of entropy and trace of the NTK, just from architecture scans on MNIST seems quite premature. When even changing from ReLU to tanh changes results (line 353), it is unclear if results may change based on hyperparams requiring tuning for each architecture, i.e. each architecture needs its own learning rate, initialization, etc. Furthermore, quirks of MNIST might lead to some effects. These conclusions must hold across datasets and architectures to be justified -- the authors show this for dense and convolutional networks and MNIST and Fuel Efficiency tasks and say that results are qualitatively similar. The figures between MNIST and Fuel Efficiency dataset do not seem qualitatively similar to me. Main text says fuel efficiency dataset is Fig. 5 in Appendix, but in Fig 5, it says MPG regression dataset (which is not called this in the table either, but since it is the only task with regressions, this seems to be the Figure - please be consistent in nomenclature) In any case, this doesn't look qualitatively similar to the MNIST figures.

I'm not convinced that the trace gives any extra insight into why malicious data will affect the dataset more in the training. One could just as well use the argument used here in the usual weight update equation. If losses are low, and a new data point has a high loss in particular a high loss whose gradient with respect to current weights is high, then it'll have a large effect later in training. The authors claim that the trace isolates the gradient contribution of the network, but this is not clear. The trace of the NTK is a scalar quantity, and while it does scale the overall update, it doesn't provide insight into the direction of the update, which is what determines the effect of a malicious data point. The argument that a large trace will cause a significant update even with small losses is not sufficient to explain why malicious data is more impactful later in training, as the direction of the update is equally important.

The lack of a compression phase in models of section 4 is interesting, but is not studied, despite prominently mentioning this as information compression in the MNIST case. The authors just say this may be because of large batch /dataset size. This could have been easily studied by varying the batch size or restricting the dataset in some way. It's not clear why the authors did not explore this further, given that the compression phase is a key aspect of their analysis. The authors should have provided experimental evidence to support their claim about the effect of batch/dataset size on the presence of the compression phase.

The trace also varies very differently between different domains and no attempt is made to explain this except some conjectures on missing term in the energy equation. The authors should have provided a more detailed analysis of why the trace behaves differently across domains. The conjectures about the missing term in the energy equation are not sufficient without further experimental validation. A more in-depth investigation into the factors that influence the trace is needed.

Minor:
Line 185, use \cite instead of \citep to make authors of a work the subject of a sentence.

### Questions
I would like to see very similar behaviour of entropy and trace across a number of tasks to be convinced about this two stage phenomena.

And where it doesn't occur, I expect some effort in trying to figure out why but appropriately titrating aspects of the task / dataset / network between the showing up of two stages vs one stage and figuring out exactly why and when this occurs. Similarly, a better analysis of why the trace shows a dip versus not during learning.

Line 253-254: "increasing entropy indicates structure formation" -- this is counter to the usual physics entropy where entropy decrease with structure formation. I would call the second phase "structure separation" or "structure refinement".

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
2

### Summary
The authors explore neural network learning dynamics and scaling by using recently introduced entropy and trace measures on the empirical neural tangent kernel (NTK) spectrum. 
These metrics reveal insights into network representations and their evolution across diverse architectures and datasets, including a toy MNIST problem and more contemporary "novelty" architectures. 
Two main mechanisms are seen to emerge (1) information compression, characterized by entropy reduction and (2) structure formation, characterized by entropy increase especially in larger networks (noted by the authors to indicate a "deep learning regime"). While the novelty of the work is somewhat limited (because it's an empirical extension of work by Tovey et al (2023) who introduced the entropy and trace measures), I found the manuscript to be rigorous and very well written.

### Strengths
Strengths
* Useful contribution: the problem studied and the point of view presented is practically useful to a large segment of the ML community. The basic claims were well studied/supported, with only minor concerns. 
* Paper is clear and well written, and as such has high pedagogical value.

### Weaknesses
Weaknesses
* Limited novelty (as mentioned earlier), but by no means a deal breaker
* Some missing details (see below)

* The definition of "deep learning regime" is vague and lacks sufficient grounding in existing literature. The authors should provide a clear, testable definition, and discuss how it aligns or diverges from established concepts of depth in neural networks. The current description of structure formation as a hallmark of this regime is not sufficiently precise, and needs to be better connected to concrete, measurable properties of the network.
* The paper lacks crucial implementation details that are necessary for reproducibility. Specifically, the network architectures, including the number of layers, the size of each layer, the activation functions used, and the initialization schemes, are not consistently provided for each experiment. This makes it difficult to assess the generality of the findings. Furthermore, the specific data preprocessing steps, such as normalization or scaling, are not clearly described for each dataset, which is a critical omission.
* The choice of 200 samples of 20 data points for NTK approximation is not sufficiently justified. The authors should provide a more rigorous explanation of how this choice was made and why it is representative of the full dataset. It is unclear how this subsampling affects the accuracy of the NTK spectrum and the resulting entropy and trace measures. The term "non-ideal initialization" is also poorly defined and needs to be clarified. What specific properties of the initialization are considered non-ideal, and how do these properties affect the observed learning dynamics? The authors should also clarify the statement about the loss function in L418, explaining why the specific loss function is relevant to the discussion.

### Questions
Suggestions for improvement:
* Can the term "deep learning regime" be explicitly defined, and citations provided for wherever this definition matches or deviates from prior literature.
* Please explicitly provide information on network size/architecture/nonlinearities and initialization for every case considered. 
* For all tasks, how has the data been preprocessed/scaled/normalized? 
* L396: How was "200 samples of 20 data points" chosen? Justify this choice
* L406: Clarify "non-ideal initialization"; what would be ideal?
* L418: Unclear "loss, due to the specific one chosen…". What is being said here?
* L423: Missing details, what algorithm and hyperparameters were used for Deep RL?
* For the RL task, could some classic-control RL tasks be used instead of (or in addition to) a task like Atari CNN
* The idea of kinetic-energy introduced around L367 is quite interesting but seems underdeveloped. It should be left in, but more empirical details about this over training evolution could be provided. 
* The authors should consider connecting their findings to previous work on curriculum learning, specifically algorithms where loss on training examples are used for building automatic training schedules.

### Soundness
3

### Presentation
4

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
The authors introduce two quantities to describe the training of neural networks, based on the neural tangent kernel (NTK). These measures are the entropy of eigenvalues in the NTK, and its trace.

They then assert that entropy decreases and increases correspond to "information compression" and "structure formation", respectively. The trace measures aggregated learning rate multipliers over the separate modes of the NTK.

They train multiple neural networks of different types and observe the changes in loss as well as in both entropy and trace of the NTK, trying to identify patterns.

### Strengths
Understanding the dynamics of neural network training is an important problem.

The measures are reasonably well described.

The experiments appear thorough.

### Weaknesses
It is not quite clear what message we're supposed to get from this work. The authors introduce these measures, and propose some kind of intuitive description of what they measure, which is not necessarily wrong, but what exactly it means for training is not obvious. The connection between the proposed NTK-based metrics (entropy and trace) and concrete aspects of neural network training remains tenuous. While the authors suggest entropy decreases correspond to "information compression" and increases to "structure formation," these are high-level interpretations that lack precise, quantifiable links to the actual learning process. For instance, how does a specific change in entropy directly relate to the network's ability to generalize or memorize? The paper lacks a clear demonstration of how these metrics can be used to diagnose or improve training. 

The authors also try to discern patterns in the differences in the evolution of these measures with network architecture, but there doesn't seem to be anything consistent beyond "trace increases" and "entropy always increases at some point unless the model is very small". For example,  the authors suggest that smaller networks have only decreasing entropy due to inability to create structure, but then have to admit that this is only for depth, not for width (line 261-262). Even more puzzling are the very large changes caused by changing the activation function, which seem to be at least as large as those caused by architecture changes. The lack of consistent patterns across different architectures and activation functions undermines the generality and practical utility of the proposed metrics. The fact that activation function changes can have such a large effect, comparable to architectural changes, suggests that the metrics may be capturing something other than just the structural properties of the network. 

Basically there does not seem to be any clear message from the data. The parallel with kinetic energy at line 363 is unclear. The authors make one prediction, if a rather weak one: that introducing noisy data should produce more changes in the parameters at the end of training than at the start of training (line 376). This prediction doesn't seem to be tested.

### Questions
Figure 1 is very hard to grasp. Please use similar colors for a given value of the quantity of interest, and separate "test" from "train" with e.g. dotted vs solid, or anything else that would make it easier to separate the values.

Should there be a sum over k in the definition of big-theta_pi in line 133? Where does the k go?

l. 179 is hard to parse.

What are the dark splotches near the sides of the panels in Figure 2?

It's not clear how Eq. 11 was derived. The original equations relate f_dot(xp) to dloss / df, but Eq. 11 show dloss/dtheta_j instead?  What is the j variable here?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The authors present a study on collective variables of empirical Neural Tangent Kernels (NTK) of various scales, architectures, and tasks in order to describe the learning dynamics of these models. Two major results are described: 1) the evolutions of the entropy of the NTK spectrum during training can undergo two different modes, a decrease in entropy or increase. A decrease in entropy is described as an 'information compression' phase, where gradients from different inputs are aligning. This process seems to occur mostly for smaller networks in both width and depth and is often transitory. Conversely, an increase in entropy is described as ‘structure formation’, where different inputs result in more diverse gradient vectors, indicating more selective representations. An increase in the NTK spectrum’s entropy is almost always observed for large (or over-parametrized) networks and coincides with later stages of training when the models are converging to higher performance. The authors argue that the latter phase of increasing entropy can be argued as when a ‘deep learning’ phase is actually occurring. 2) The trace of the NTK increases as the loss decreases during training, where the trace can be interpreted as an ‘effective step size’ or learning rate. This increase in effective step size, even as the loss decreases, implies a heightened sensitivity of the model to loss, or, as an increase in confidence in the direction of the gradient vectors. The authors argue that this indicate that fictitious data has a stronger negative effect if shown at later stages of training compared to earlier, even if the loss value is the same. Finally, the authors show that these results share some universality across a variety of models and argue that this behaviour might indeed be descriptive of universality in learning dynamics and, in particular, deep learning.

### Strengths
Originality: The paper extends known methods, namely computing the trace and entropy of NTK spectra, to a broader scope than previous applications.

Quality: The paper is well motivated, and the background material is introduced with good detail with relevant literatures cited.

Clarity: It is also written clearly, in good scientific English and is relatively comfortable to follow. The key results of the paper are also introduced well and discussed in a way that was easy to appreciate why the authors argue their significance. The figures in the paper are also well formatted.

Significance: The interpretation of the results has the potential to condense the analysis of training dynamics into universal patterns of collective variables, an insight that could help diagnose and analyze a broad variety of models.

### Weaknesses
-	(Clarity) For the figures, the colour coding/line-styles aren’t well grouped to my eyes. It might benefit to have the smaller and larger models have similar shades and then have different line styles for train vs. Test. I found myself having to constantly check the legends for each panel which was a bit tedious to interpret each figure.
-	(Significance and Quality) The interpretation of the changes in the entropy of the NTK spectrum as “information compression” vs “structure formation” is, as it’s written, somewhat convincing, but I’m not actually sure if this interpretation is simply a good analogy or if that is what is exactly happening. Perhaps this criticism is due to my own ignorance on the topic, but I think making these statements more convincing would empower this paper quite a bit as these are the central results of the paper. I’m not entirely certain what would make this point more convincing unfortunately, but I wonder if there could be custom datasets that one knows a priori that the data points are somewhat redundant and that the entropy should only decrease versus datasets that require more sophisticated representations and so the entropy should increase, as an example. Doing so might also help relate these results to the results from Tovey et al. (2023) and would help elucidate the contribution. Furthermore, expanding on how these methods are explicitly different from the Tovey et al. (2023) would also clarify the significance and contributions of this paper.

### Questions
-	In all the examples shown, it seems the models studied are succeeding (at least somewhat) at solving their tasks. So, we see relatively universal trends, and this is, so far, a reasonable result. However, I wonder what does it look like if the models are too small, or badly initialized, or have the wrong architectures for their tasks? What would these curves look for regimes in which the training dynamics are failing to solve the task? 
   - Could you, for example, take some of the models used in figure 3 and handicap them in some way to force them to be bad? What would the curves look like then?
    - Furthermore, for the example shown in figure 3, all these models are large enough such that their entropy is always increasing, as argued by the authors should be the case for over-parametrized, deep models. Could you then make the same study for these models as done in Figure 2 by making them smaller or shallower and recreate the transient decreasing entropy phase? 
    - By doing such an analysis, can you relate your results to the cost/performance trade offs for models at different scales?

### Soundness
3

### Presentation
3

### Contribution
3

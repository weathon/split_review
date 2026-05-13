# Do Mice Grok? Glimpses of Hidden Progress in Sensory Cortex

- Decision: Accept
- Scores: 6, 5, 8, 5

## Abstract
Does learning of task-relevant representations stop when behavior stops changing? Motivated by recent work in machine learning and the intuitive observation that human experts continue to learn after mastery, we hypothesize that task-specific representation learning in cortex can continue, even when behavior saturates. In a novel reanalysis of recently published neural data, we find evidence for such learning in posterior piriform cortex of mice following continued training on a task, long after behavior saturates at near-ceiling performance ("overtraining"). We demonstrate that class representations in cortex continue to separate during overtraining, so that examples that were incorrectly classified at the beginning of overtraining can abruptly be correctly classified later on, despite no changes in behavior during that time. We hypothesize this hidden learning takes the form of approximate margin maximization; we validate this and other predictions in the neural data, as well as build and interpret a simple synthetic model that recapitulates these phenomena. We conclude by demonstrating how this model of late-time feature learning implies an explanation for the empirical puzzle of overtraining reversal in animal learning, where task-specific representations are more robust to particular task changes because the learned features can be reused.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors examine the phenomenon of overtraining in posterior piriform cortex of mice.  They show that class separation continues after performance saturates.  They further show that the margin of the maximum margin classifier increases in the overtraining period.  They construct a simple model, which is a one-hidden layer MLP, that shows this overtraining behavior.  They propose that this model provides an explanation for over-training reversal in animal learning.

### Strengths
The paper is very clear and well presented.  The basic result is simple and backed by both empirical data and a simple model.  Most of the figures are very clear and concise.  That the observation can be explained by so simple a model is nice.  The explanation of reversal training is nice.

### Weaknesses
I think there are a few improvements that could be made to the figures:

Figure 1 could use a quantitative indication of performance, so that it is clear when overtraining starts (as opposed to this being buried in the caption).  

Figure 2 is slightly confusing in terms of which column in each row represents what.  Do I understand correctly that the first column is the average and the others are the first and last 3 days, respectively?  If so, this could be labeled better.  If not, this could be labeled much better.  

In Figure 3, maybe add an indication of the cluster mean with a line separating the clusters to make the separation more clear?  It’s not bad now, but some of these are rather close.  

In Figure 5, panel labeled “Epoch 1000”, the target dot is obscured.

### Questions
This seems like it would be a very general phenomenon, in particular because natural gradient descent dynamics should keep lowering the loss, which by construction has to maximize some discriminant in the data being classified.  At the same time, the training samples are discrete so you are guaranteed to saturate the training error (i.e. you can’t get better than perfect on a finite set).  Your kernel argument at the end seems to back up this intuition.  What properties of networks would you envision would prevent this behavior?  Or what kinds of tasks?

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
This study examines grokking, an interesting phenomenon observed in both deep learning models and in animal learning. The authors re-examine a published dataset that tracks neural activity in the posterior piriform cortex (PPC) of mice trained to perform a multi-odor discrimination task. The authors found that the class margin measured in the neural activity space of PPC continued to increase after performance accuracy has reached a ceiling. In a simple MLP with one hidden layer trained to perform an in silico “odor” discrimination task, the authors found continued improvement in class margin measured in latent space, and “grokking” phenomenon in probe trial accuracy. Using this simple model, the authors also provide theoretical explanation and empirical demonstration of overtrained reversal, a phenomenon long reported in experimental psychology.

### Strengths
The study draws an interesting connection between the grokking phenomenon in deep learning and to the gradual evolution of neural representation in mice overtrained on classification tasks. By using a simple MLP model to demonstrate the link between increase in class margin and the emergence of “grokking”, the authors highlight a promising mechanism by which grokking may emerge in biological and artificial learning systems.

### Weaknesses
1)	The architecture of the MLP model is likely far removed from the actual structure and connectivity of the PPC, hence it appears more like a toy model to demonstrate the cooccurrence of margin maximization and grokking. The model lacks crucial biological constraints such as specific cell types, their connectivity patterns, and the influence of neuromodulators, all of which could significantly impact the observed dynamics. Whether similar phenomenon would emerge in more sophisticated models of olfactory cortex (or olfactory circuits in lower animals) that incorporate these biological details remains to be tested; the current model is insufficient to make strong claims about biological plausibility.
2)	While the emergence of grokking in the MLP model is interesting, the authors have yet to test whether the observed increase in class margin is causally related to grokking. The authors cite related theory, e.g. setting margin maximization as an optimization objective could drive the emergence of grokking. However, the study does not provide direct evidence that manipulating the margin directly affects the grokking phenomenon. Without such evidence, the link remains correlational rather than causal. It is unclear if margin maximization is a necessary or sufficient condition for grokking in this model.
3)	Without further analysis, it is unclear how the link between class margin maximization and grokking in more complex DL models, e.g. models trained to classify images. While the authors provide a theoretical basis for how overtrained reversal occurs, a theoretical advance on why grokking occurs remains lacking. The study does not address how the observed dynamics in the simple MLP would translate to more complex architectures and datasets, and whether the same mechanisms are at play. The theoretical explanation for overtrained reversal is not fully connected to the grokking phenomenon, leaving a gap in understanding the underlying principles.

### Questions
Could the authors comment specifically on:
1)	How results from the MLP model would generalize to more biologically constrained models of the PPC (or other olfactory processing circuits)?
2)	How results from MLP could generalize to more complex DL models for classification?
3)	Demonstrate a causal link between margin maximization and the emergence of grokking in the MLP model?

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
This paper examines an intriguing phenomenon where neural representations in mouse sensory cortex continue to evolve and improve even after behavioral performance has reached ceiling levels (Berners-Lee et al. 2022). The authors reanalyze neural recording data from mice learning an odor discrimination task and find evidence for "hidden progress" in how odor representations separate in piriform cortex during overtraining, similar to the "grokking" phenomenon observed in deep neural networks. They propose that this continued refinement of representations reflects implicit margin maximization and demonstrate this using a simplified neural network model. The paper makes novel connections between neuroscience and machine learning while offering new insights into both domains.

### Strengths
- Makes an important connection between seemingly disparate phenomena in biological and artificial neural networks (hidden representational changes during overtraining, grokking, reversal learning)
- Provides a compelling mathematical framework (margin maximization) that helps explain the neurobiological data
- Offers a novel explanation for the classic "overtraining reversal effect" from psychology in terms of rich feature learning
- Good empirical validation through neural data analysis and synthetic modeling
- Mostly clear writing and effective visualization

### Weaknesses
 - The characterization of their model as "biologically faithful" feels overstated, given the significant abstractions from real neural circuits. The model, while capturing some high-level principles, lacks the detailed dynamics and constraints of actual neural networks, such as specific neuron types, connectivity patterns, and temporal dynamics. For example, the model does not account for the diverse inhibitory interneuron populations or the complex synaptic plasticity mechanisms present in the piriform cortex. These simplifications limit the extent to which the model can be considered a direct representation of the biological system.
- The paper should cite relevant literature on deep learning approaches to perceptual learning, particularly work by Wenliang and Seitz (2019) that examines how perceptual learning can be explained as changing readouts from complex features. Specifically, the authors should discuss how their findings relate to the concept of representational drift and how the readout mechanisms from these evolving representations can be interpreted. The current lack of engagement with this literature leaves a gap in the discussion of how the observed phenomena fit within the broader context of machine learning and perceptual learning.
- The explanation of margin maximization was a bit inscrutable, particularly the part about distinguishing between different notions when a decoder is being retrained on evolving features. It could use a rewrite and tightening up, perhaps a subfigure. The explanation needs to clarify how the margin is calculated when the feature space is changing over time. It is unclear if the margin is being calculated with respect to the initial feature space or the current feature space, and how this distinction affects the interpretation of the results. Furthermore, the relationship between the margin and the specific loss function used in the model needs to be more clearly articulated.

### Questions
Suggestions for Improvement:
1. Tone down claims about biological fidelity and instead emphasize that the model captures key computational principles at an abstract level
2. Add discussion of connections to deep learning literature on perceptual learning, which provides complementary perspectives on how representations evolve during training
3. Clarify the precise definition of margin maximization being used, particularly in the context of evolving representations.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper demonstrates that animals can learn tasks and improve generalizability through over-training. The study begins by reproducing and reanalyzing experiments conducted on mice (Berners-Lee et al., 2023) and then proceeds to run toy experiments as proof-of-concept illustrations.

### Strengths
The paper addresses interesting topics at the intersection of foundation models and cognitive science, particularly within the realm of behavioral psychology.

### Weaknesses
 **1. Writing Quality:**

*   *Citation:* The poor writing significantly hinders the evaluation of this work. For instance, the authors misuse \citet and \citep throughout the paper. The frequency of these errors affects the paper’s professionalism; please revise these accordingly.

*   *Confusing Notation:*
Although Berners-Lee et al. (2023) represent each odor as a vector in their figures, the description "n-hot vector of $k$ possible odorants" may confuse readers. Given that ICLR’s primary audience is in machine learning, they may interpret this as a traditional vector representation, though in the authors' experiment it represents a combination of odorants rather than a vector. The lack of clarity regarding how these n-hot vectors are processed before being fed into the network is a significant issue.

*   *Undefined Notations:*
Several notations lack definitions (e.g., [N, T] in line 755) or exact values (e.g., $n$ in $n$-hot vector). It is unclear how the dimensions of these notations relate to the experimental setup.

**2. Validity of Experimental Setting:**

The results could be heavily dependent on the experimental setting. In the default setup, each odor is represented as a combination of odorants, defined by an $n$-hot vector, with limited overlap between odorants. Given the network’s simple architecture (a single fully connected layer), each odorant is almost linearly separable, meaning there is minimal interference among components. This could explain why the model resists overfitting and maintains increasing test accuracy even during overtraining. Conversely, as seen in Figure 6, when odor overlap is greater, neither the Fisher Linear Discriminant nor the test accuracy increases significantly beyond 100 epochs, at which point the model reaches perfect training accuracy. The use of n-hot vectors, where each odor is a sparse combination of odorants, raises concerns about the generalizability of the findings to more complex, realistic scenarios where odors might be represented by continuous, overlapping features. The authors should clarify how the random projection is implemented and whether it introduces non-linearities into the input space.

**3. Loss Interpretation:**

The authors claim in line 370 that after achieving perfect training accuracy, the loss "plateaus." However, it appears to continue decreasing (though this could be subjective). Additionally, perfect training accuracy does not imply the model has fully learned from the training data, especially since cross-entropy loss is used, and accuracy is based on the argmax classification. The authors should clarify what they mean by "training loss" in the context of the neural data reanalysis, as it is not immediately obvious how a loss function is calculated from neural recordings.

**4. Miscellaneous**

*   Lines 457–484: This section needs refinement. It is unclear how the original features differ from pre-trained features (L461–463), the relationship between $K$ and $K_0$ (L465), and the contrast between the original model’s readout and the randomly initialized network (L482).

*   Figure 1: The caption refers to (a) and (b), but these labels are absent in the figure.

*   Line 355: “are are” should be corrected to “are.”

### Questions
I am unclear about the contribution of the section "A mathematical model based on rich learning" on page 9. If the authors use a kernel method, isn’t the result somewhat trivial? Furthermore, the logical connection between the content of this section and the conclusion — “An animal overtrained on a task will have better task-model alignment and a richer feature set than an animal whose learning was stopped after behavioral plateau” — is unclear. Could the authors elaborate on this section?

### Soundness
3

### Presentation
2

### Contribution
2

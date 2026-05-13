# Shapeshifters: Auditory cortical neurons switch from polysemantic to monosemantic under anesthesia

- Decision: Reject
- Scores: 3, 6, 5

## Abstract
General anesthesia transitions the brain from a conscious to an unconscious state, but how does sensory processing differ between these conditions? To address this question, we trained neural network encoding models to predict the responses of auditory cortical neurons to natural sounds in both awake and anesthetized ferrets. Utilizing mechanistic interpretability methods, such as feature visualization, linearization and sparse autoencoders, we analyzed these networks tuning and connectivity to uncover key differences in sensory processing. We found that anesthesia decouples neural connectivity, shifting neurons from polysemantic (responding to multiple inputs) to monosemantic (responding to a single input), resulting in a lower-dimensional population code. These findings illuminate how anesthesia alters neural connectivity and encoding, offering new insights into the neural mechanisms underlying sensory processing.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work looks at auditory neurons collected during awake and anesthetized recordings to try and identify differences in the coding properties that differ during conscious and unconscious brain states. The authors use various forms of computational modeling and interpretability tools to investigate how the responses differ. The authors claim that neurons under anesthesia respond to single inputs (a lower dimensional code), while neurons in awake animals respond to multiple inputs (a higher dimensional code).

### Strengths
The paper presents a creative method of addressing the question of differences between awake and anesthetized neural responses. The goals of the paper are ambitious. The idea is to combine predictive modeling approaches and neural network interpretability tools with neural data to learn new things about the neural code. In doing so, the authors aim to unify conflicting claims about auditory processing.

### Weaknesses
The biggest weakness of the paper is the confounds between the awake and anesthetized datasets (this is noted by the authors in the discussion). The datasets are collected on different sound sets, with significantly more sounds in the awake recordings than in the anesthetized recordings. Even though the authors in one experiment show a control where they match the number of stimuli, there is not enough detail given on how these stimuli were chosen and the differences in sounds between the two datasets. Significantly more control analyses would need to be run to make sure that the differences observed are not simply due to differences between the datasets. Unfortunately, the best way to test this hypothesis would be for data to be collected in the same animal during awake and anesthetized recordings, which is far beyond the scope of an ICLR rebuttal period. 

Overall though, I found the paper to be using somewhat overly complicated methods to answer fairly standard questions, and description of the methods and results was not the easiest to follow (many critical details are missing, see some examples in the questions). I found myself wondering whether the methods used were actually necessary to ask the question of whether the responses under anesthesia become lower dimensional -- the PCA analysis by itself might be sufficient in a controlled neural dataset.

### Questions
1) Could the authors provide more detail about the two different sound datasets? How many repetitions were presented for each sound? What was the general composition of sound events of each dataset? 

2) Could the differences between results for the two datasets be explained by the recording locations of the neurons, or perhaps spike-sorting/preprocessing differences (and if not, what evidence is there that this isn’t the case)? The two datasets were collected by different labs and presumably very different recording setups.

3) Is the L2 regularization constraint for feature visualization (line 134) applied on the cochleagram? Why is this a reasonable constraint to use for the cochleagram (what is being “smoothed”?)   

4) On line 120 it is stated that a batch size of 64 sound clips is used for training, but one of the datasets only had 20 sound clips. Is there a different training dataset used in this section? 

5) I had some general questions about the PCA analysis. In figure 3 and the explanation of these results (lines 299-305) it would be helpful to remind readers what PCA is being performed on. As it currently reads, it seems like it is being done on something within UMAP (which would be a problem), but I believe it is on the raw DSTRF responses (the correct thing to do). Also, for this PCA in Figure 3 and also the PCA in Figure 4, is there any preprocessing done to the signal before PCA is performed? And what does each PCA analysis look like when using a matched number of stimuli and neurons (ie can the differences in this section be explained by the dataset differences?) 

6) For Figure 4d, it is noted that the number of neurons was subsampled so the number was matched between two datasets, but what if the number of neurons *and* the number of sounds is matched between the two datasets? 

7) It might be helpful to have a beginning of the discussion section that gives the overall summary of the results, and how all of the results fit together.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors seek to understand the response properties of a "conscious" neural network (e.g., a model that is trained to predict the firing rate of biological auditory cortex neurons during an "awake" state) and a "unconscious" neural network (e.g., a model that is trained to predict the firing rate of biological auditory cortex neurons during an "anesthetized" state). Interestingly, augmenting the encoding model with a "gating" mechanism improves the firing rate predictions.

### Strengths
The paper and results are very interesting, and has potential impact to both neuroscience and machine learning. In particular, the formal connection between the neural processing of auditory stimuli and the effect of anesthetics is inspiring. The paper is well-written and the formulation of the encoding model(s) and training setup is clear. 

The result on the transition from "polysemanticity" of the "awake" A1 neurons to "monosemanticity" of the "anesthetized" neurons is quite interesting.

### Weaknesses
 * There is no formal comparison of the "semanticity" of the biological A1 neurons and the artificial neurons in the (trained) encoder models (e.g., TC model). For example, are the "awake" TC neurons more polysemantic, while the  "anesthetized" TC neurons more monosemantic? It's crucial to quantify the degree of polysemy in both the biological and model neurons to validate the model's ability to capture this key aspect of neural processing. Without this direct comparison, the claim that the model reflects the biological transition in semantic processing remains unsubstantiated.

* The role of "gating" in these models, albeit briefly motivated, is quite sparse. For instance, how does the proposed "gating" compare to "dynamic thresholding," which aligns more closely with the observed properties of cortical sensory neurons. Dynamic thresholds allow neurons to activate only when inputs meet a certain criterion, essentially filtering out less relevant signals without directly scaling the output. The current gating mechanism appears to simply scale the output, which may not fully capture the dynamic filtering behavior observed in biological neurons. A more detailed exploration of how the gating mechanism interacts with the input signal and how it affects the neuron's selectivity would be beneficial.

### Questions
* In Figure 1, the authors bin the spike trains into $4$ ms intervals, leading to very high (possibly non-biological) firing rates ($150$-$250$ Hz). Do the A1 neurons in the Ferret actually display this range of firing rates?

* In sequence models(e.g., LSTM), the "gating" mechanism controls the routing of information to the next cell. In this work, what is the role of the gating mechanism in relation to anesthesia? In an anesthetized state, there is no conscious perception, so information of certain sounds doesn't reach higher-level brain regions, such as the hippocampus. In effect, there is more "gating" of information in an anesthetized state. However, in Figure 5, the results suggest the "awake" state displays more "gating" (e.g., more incoming connections to each output unit) than the "anesthetized" state, which displays less "gating." 

* Certain anesthetics are known to be amnesic (induce forgetting). In an LSTM, the "forget" gate removes irrelevant information. Does the "gating" in the anesthetized model learn to discard irrelevant information?

### Soundness
3

### Presentation
3

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
Authors analysed and modelled the responses of neurons from the primary auditory cortex (A1) in awake and anesthetised ferrets. They compared the performance of several recent decoding models and found the temporal convolutional model to be the best among tested alternatives. Further, authors showed a significant improvement in performance of encoding models by adding gating of the output. They found that neurons in awake animals are characterised by stronger, more dynamic and more complex tuning of single neurons compared to anesthetised animals. Also, they found that neural populations in awake animals have higher dimensionality compared to anesthetised animals. Finally, they find that in the awake animals, neurons receive more synaptic connections and are therefore more strongly coupled than in anesthetised animals.

### Strengths
The paper combines a number of known methods and techniques to brings new insights into the encoding differences between neural activity in the auditory cortex in the awake and anesthetised brain state. The paper addresses an interesting question. The writing is transparent about the methods and about the results.

### Weaknesses
1) While I appreciated the effort for transparency, the clarity of writing can be improved on several places. For example, the title and content of the section 3.2 could use clearer writing. The title of section 3.2 mentions that "anestetised neurons are more interpretable that awake neurons" . This is an awkward statement, because the level of interpretability always depends on what is being interpreted.  

2) Authors do not explain well what is the mechanism of gating and why it improves encoding. Some more methodological description of gating could be useful in Methods, and an intuitive description of what gating does would be a useful addition to Results. 

3) The description of different encoding models (LN, NRF, TC) can also be improved, as it remains unclear why would we expect these models to perform differently.

4) The discussion about depression in the last paragraph of the paper reads like a long shot and is tangential to the rest of the material presented in the paper. I suggest removing it and using the space to better describe the most important results.

### Questions
1) Even the best model systematically underestimates (undershoots) the firing rate during the sustained response in anesthetised animals. What might be the cause? 

2) The authors write that "the average number of active hidden units is a proxy of the dimensionality of the population code". This interpretation of the dimensionality of a population code is new to me, as the dimensionality is typically related to the number of independent variables encoded by a neural network. This is similar to the notion of dimensionality authors use when describing their Fig. 4b. Could authors comment on that?

### Soundness
2

### Presentation
3

### Contribution
2

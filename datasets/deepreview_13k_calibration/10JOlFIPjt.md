# In vivo cell-type and brain region classification via multimodal contrastive learning

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 8, 6

## Abstract
Current electrophysiological approaches can track the activity of many neurons, yet it is usually unknown which cell-types or brain areas are being recorded without further molecular or histological analysis. Developing accurate and scalable algorithms for identifying the cell-type and brain region of recorded neurons is thus crucial for improving our understanding of neural computation. In this work, we develop a multimodal contrastive learning approach for neural data that can be fine-tuned for different downstream tasks, including inference of cell-type and brain location. We utilize multimodal contrastive learning to jointly embed the activity autocorrelations and extracellular waveforms of individual neurons. We demonstrate that our embedding approach, Neuronal Embeddings via MultimOdal Contrastive Learning (NEMO), paired with supervised fine-tuning, achieves state-of-the-art cell-type classification for an opto-tagged visual cortex dataset and for brain region classification of the public International Brain Laboratory brain-wide map dataset. Our method represents a promising step towards accurate cell-type and brain region classification from electrophysiological recordings.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a novel application of contrastive learning to solve two important problems in systems neuroscience by incorporating just two electrophysiological recording modalities: spiking activity and extracellular action potentials (EAPs). The authors developed a new framework called Neuronal Embeddings via Multimodal Contrastive Learning (NEMO) by combining the well-established Contrastive Language-Image Pretraining (CLIP) framework with task-specific data augmentations and encoders. The authors demonstrate the multimodality as well as the power and utility of NEMO by evaluating its performance on two very different downstream tasks:

1.	cell-type classification among parvalbumin (PV), somatostatin (SST), and vasoactive intestinal peptide (VIP) inhibitory interneurons using opto-tagged Neuropixels Ultra (NP Ultra) recordings from the mouse visual cortex, and

2.	brain-region classification among 10 broad areas using the public International Brain Laboratory (IBL) brain-wide map data set.

This paper’s novelty mainly stems from the utilization of a paired data set that combines an autocorrelogram (ACG) image of every neuron’s spiking activity and a waveform template of the neurons’ EAPs, and from the application of two separate encoders for the aforementioned two modalities. In both cell-type and brain-region classification tasks, the authors show that NEMO outperforms the state-of-the-art multimodal cell-type embedding methods including PhysMAP and VAE-based methods as well as a fully supervised method in terms of balanced accuracies and macro-averaged F1 scores with minimal fine-tuning.

### Strengths
This is a very well-written paper with clear organization of the figures and sound presentation of the data sets used, methods applied, and results obtained. The authors apply a successful contrastive learning method to develop a new framework that outperforms comparable state-of-the-art methods in both the cell-type classification task and the less widely-explored brain-region classification task. The task relies on two electrophysiological recording modalities: spiking activity and EAPs, which are more accessible, and the decent classification performances come with minimal fine-tuning. NEMO is able to differentiate between VIP and SST cells, which is highly valued in systems neuroscience, and its ability to yield data embeddings that lead to separable classification regions is impressive. The method described in this paper will be particularly helpful and useful to systems neuroscientists interested in applying this technique with the goal of decoding the neural circuitry underlying multiple biological functions.

### Weaknesses
Detailed graphical representations of the architectures used in the authors’ method may help the readers understand the details of NEMO better. A more comprehensive description, such as including explanations of 10D and 500D in the VAE baseline versions’ latent spaces of the encoder architectures, would have further aided clarity to the method’s explanations.

The authors restrict the number of example neurons, whose recorded activities are inputted to the overall architecture, to five neurons without an explanation of why the input neuron number was kept low. Providing a rationale for limiting the number of input neurons to five as well as an explanation of how the results of the authors' method change with varying input neuron number would be greatly appreciated.

The authors state that they fixed the hyperparameters for all methods across the two data sets used in the experiments due to the limited number of labels for evaluation for the cell-type classification task. It is unclear whether this choice led to fair performance comparisons among the state-of-the-art methods. It would help to know that separate hyperparameter optimization among the different methods and data sets would not yield different results. Providing a brief analysis on the sensitivity of the results and the overall performance to variations in specific hyperparameters will notably strengthen the claims made in this paper.

Minor comments:

There seems to be a citation error or a missing preposition in Section 1 when the authors cite IBL et al.

Radford et al. 2021 to Radford et al., 2021 in Section 4

Table 6 is non-existent in Section 6.1. The authors may be referring to Table 1.

There seems to be a citation error or a missing preposition in Section 6.3 when the authors cite Chen et al. (2020).

Figure 5 (b) caption's word "then" should be changed to "than."

In Section 7, the phrase "should also be useful these down-stream tasks" should be changed to "should also be useful in these down-stream tasks."

### Questions
The waveform template is restricted to one channel with maximal amplitude and multi-channel template results are shown in Supplement E. What exactly is the definition of a channel in this context?

Why was additive Gaussian noise chosen as the sole data augmentation? Can a brief rationale for this specific choice be included in the paper? The authors demonstrate that adding two template augmentations: amplitude jitter and electrode dropout does not significantly improve the performance of the two downstream classification tasks. How do other data augmentation types impact the performance and results?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors proposed a multimodal contrastive learning approach for joint modeling of extracellular action potential data and spiking activity data. The proposed approach can be fine-tuned for different downstream tasks, including in vivo cell-type and brain region classification. More specifically, the author applied the classic contrastive learning framework established in CLIP on extracellular action potential data and spiking activity data. Although the theoretical innovation is relatively limited, the authors made the earliest efforts (as far as I know) to apply contrastive learning for joint modeling of extracellular action potential data and spiking activity data.

### Strengths
As mentioned above, this study is among the earliest efforts to apply contrastive learning for joint modeling of extracellular action potential data and spiking activity data. Most key components in the proposed analytical framework are fetched from previous work (e.g., CLIP contrastive learning and the ACG encoder), increasing the reproducibility of the study. In addition, the study was well presented and easy to follow.

### Weaknesses
As mentioned above, the theoretically contribution of the study is relatively limited. The readers may expect to see some components that are specifically designed with consideration for the unique characteristics of the data and the problem being  addressed.



### Questions
1.The authors emphasized “in vivo”, however, are there any results about the computational efficiency of the NEMO model that can support it? Does it support real-time processing?

2.I would expect a validation of the data augmentation strategy. It is understandable that the construction of ACG images is computationally expensive. But the authors are encouraged to validate the data augmentation strategy adopted in the study, augmentations directly for the ACG images, is reasonable by showing a couple examples.

3.The authors compared NEMO with the VAE-based method. However, in my opinion, it seems that a critical comparison is missing: the comparison between naive models, specifically, NEMO without fine-tuning and the VAE-based method without fine-tuning. This comparison would highlight the representational power of the two methods .

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
This paper introduces NEMO (Neuronal Embeddings via MultimOdal contrastive learning), a method for classifying neurons by their cell type and brain region location using electrophysiological data. NEMO uses CLIP-like contrastive learning to jointly analyze two types of neural data: the shape of neural electrical signals (waveforms) and patterns of neural activity over time (autocorrelograms). 

The authors evaluated NEMO on two datasets: an opto-tagged mouse visual cortex dataset for cell-type classification and the International Brain Laboratory dataset for brain region classification. In comparative experiments, NEMO achieved higher classification accuracy than existing methods including PhysMAP and VAE-based approaches. The authors also demonstrated that using multiple units improved performance, and that the method maintained effectiveness even with limited labeled training data. The paper includes ablation studies examining the importance of joint versus independent learning of the two data modalities.

### Strengths
- The paper is well written, the figures are well made, descriptions are generally clear.
- The paper contains extensive additional material for more details.
- The training and experimental setup seems to be carefully chosen and sound.
- Limitations are discussed at the end.

### Weaknesses
I only found minor weaknesses.

- Although, the authors did a great job providing necessary details, sometimes the training specifics for the control models and the clustering analyses were a bit too short in my opinion. It would be great if you could provide a bit more detail on this. For example, what specific architectures were used for the VAE encoders and decoders? What were the loss functions? What were the optimization parameters? Similarly, for the clustering analysis, what specific parameters were used for UMAP and the subsequent clustering algorithm? How was the number of clusters determined?
- It would be great to see an ablation for the data augmentation to see how important that is (see questions).

**Minor (do not expect you to respond to this)**

- Figure 3 typo in legend “Supervise” instead of “Supervised”
- Supplementary Figure 7 is blurred likely due to plotting settings
- As multi-unit has a particular meaning in neuronscience, I find the wording “multi-unit brain region classification”. I think you mean “multi-neuron” here. Unless I misunderstood and you are really using multi-unit activity, I would change the wording.

### Questions
- The VAE training is unclear to me. Do you jointly embed waveforms and autocorrelograms, or do you use two separate encoders/decoders with a shared latent space (which would require cross-decoding, i.e. encode waveform and decoder autocorrelogram)?
- How important are the data augmentations? Can you provide an ablation experiment for that?
- Waveforms and autocorrelograms are two reasonable choices for input modalities. However they are not the only conceivable choices. Have you thought/tried other choices or thought about learning an encoding of spiking activity directly?
- What are the results when you cluster on the latent embeddings directly instead of running UMAP first? How stable is the clustering? I.e. if you train two models of NEMO from different seeds and then cluster neurons, how consistently are two neurons assigned to the same cluster (as measured by adjusted rand index or similar)?
- Can you provide a definition for the modularity index?

### Soundness
4

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
The authors used multimodal (spike waveform + firing pattern) contrastive learning to classify three types of inhibitory neurons (PV/SST/VIP) and ten different brain regions. The proposed NEMO model is based on the widely used CLIP (Contrastive Language-Image Pre-Training) model. NEMO outperforms two previous multimodal models: PhysMAP and VAE.

### Strengths
1. The writing is clear, easy to understand, and follows a smooth logical flow, with almost no typos and well-presented figures.

2. The paper provides a thorough review of relevant literature in this field. I have closely followed the cell-type classification area, and all the papers I am aware of (and some I was not) have been accurately cited, except for one (see Weakness). Notably, the authors benchmarked two very recent models that are still in preprint format.

3. This is the second work to use contrastive learning for cell-type classification and the first to combine two modalities.

4. The multimodal approach outperforms single-modal models, which is consistent with previous studies.

### Weaknesses
1. In the best-case scenario (cell type classification, L344, Figure 2c), NEMO outperforms VAE by 11%. However, in brain region classification, the improvement is minimal. For example, in Figure 3e, comparing the deep orange (NEMO) to the deep blue (VAE) bars, the difference in balanced accuracy is less than 0.05. It is unclear if these differences are statistically significant, and the paper would benefit from a more rigorous statistical analysis to support the claims of improvement, especially given the small effect sizes in some comparisons. The lack of statistical testing makes it difficult to assess the practical significance of the reported gains.

2. Joint training shows little to no benefit over independent training. For example, in Figure 5b, comparing the deep orange (NEMO) to the deep violet (SimCLR) bars, the difference in balanced accuracy is around 0.01. Additionally, in Supplementary Table 9, independent NEMO performs either better (0.84 vs. 0.83) or similarly (0.83 vs. 0.84, 0.87 vs. 0.88) to joint NEMO. These small differences raise questions about the value of joint training, and without statistical tests, it is hard to determine if the differences are meaningful or simply due to random variation. The paper needs to justify the added complexity of joint training if it does not yield substantial performance gains.

3. To my knowledge, there is no strong neuroscience evidence suggesting a robust pairwise correlation between spike waveform and firing patterns. For example, layer 5 pyramidal neurons and cortical PV neurons both fire a large number of spikes (both spontaneously and evoked), but their spike waveforms are broad and narrow, respectively (Cortical connectivity and sensory coding, KD Harris, TD Mrsic-Flogel - Nature, 2013). Additionally, burst firing can be evoked in both excitatory (Chattering cells: superficial pyramidal neurons contributing to the generation of synchronous oscillations in the visual cortex. CM Gray, DA McCormick - Science, 1996) and SST neurons (Somatostatin-expressing neurons in cortical networks, Urban-Ciecko, AL Barth - Nature Reviews Neuroscience, 2016). This is fundamentally different from the relationship between an image and its description in CLIP. In other words, the word "puppy" and an image of a "puppy" represent the same concept, but a broad spike could be associated with either burst or dense firing, depending on whether the neuron is located in layer 2/3 or layer 5. The paper needs to address this potential limitation of the core assumption of the model.

4. This is the second paper to use contrastive learning for cell-type classification. The first is CEED (Vishnubhotla et al., 2023), which used an unsupervised model (SimCLR) to classify cell types and benchmarked against WaveMap (the single-modality version of PhysMAP). While the CEED work does not significantly compromise the novelty of this study, it should be more clearly acknowledged. The current citation, "Contrastive learning has been applied to raw electrophysiological recordings (Vishnubhotla et al., 2024)," is inappropriate. The paper should explicitly discuss the differences and similarities between NEMO and CEED, and clarify the specific contributions of NEMO beyond the existing literature.

### Questions
1. In Figure 1a, the text "Neuropixels 1.0" should be replaced with "Neuropixels Ultra" since your VIP/SST/PV data comes from NP Ultra, not NP 1.0, which is used in the IBL dataset for classifying brain regions. Also, please update the inset to show the schematic of NP Ultra instead of NP 1.0.

2. Figure 3b is not mentioned in the text. It could be referenced between L350 and L361.

3. Figure 3c is also not mentioned in the text. It might fit well between L362 and L366.

4. Consider changing the title of Figure 3b and 3c from "unit" to "neuron" to be consistent with the terminology used in the main text.

5. In the PhysMAP paper that you benchmarked, they applied three public datasets from S1, A1, and V1/Hippocampus. Have you tested these datasets? While I am not requesting additional experiments, if you have tested them, it would be helpful to include the results in the supplementary materials.

6. Please specify how you computed the two primary metrics: macro-averaged F1 score and balanced accuracy. Does the first metric equal the unweighted mean of all the per-cell-type F1 scores? Does the second metric equal the unweighted mean of sensitivity (True Positive) and specificity (True Negative)?

### Soundness
3

### Presentation
4

### Contribution
2

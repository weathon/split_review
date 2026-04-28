# Unsupervised Representation Learning of Brain Activity via Bridging Voxel Activity and Functional Connectivity

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 6

## Abstract
Effective brain representation learning is a key step toward revealing the understanding of cognitive processes and unlocking detecting and potential therapeutic interventions for neurological diseases/disorders. Existing studies have focused on either (1) voxel-level activity, where only a single beta weight for each voxel (i.e., aggregation of voxel activity over a time window) is considered, missing their temporal dynamics, or (2) functional connectivity of the brain in the level of region of interests, missing voxel-level activities. In this paper, we bridge this gap and design BrainMixer, an unsupervised learning framework that effectively utilizes both functional connectivity and associated time series of voxels to learn voxel-level representation in an unsupervised manner. BrainMixer employs two simple yet effective MLP-based encoders to simultaneously learn the dynamics of voxel-level signals and their functional correlations. To encode voxel activity, BrainMixer fuses information across both time and voxel dimensions via a dynamic self-attention mechanism. To learn the structure of the functional connectivity graph, BrainMixer presents a temporal graph patching and encodes each patch by combining its nodes' features via a new adaptive temporal pooling. Our experiments show that BrainMixer attains outstanding performance and outperforms 13 baselines in different downstream tasks and experimental setups.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This manuscript proposes a self-supervised framework, BrainMixer, that encodes time series and functional connectivity. For the time series, the authors adapted MLP-Mixer by introducing TimeMixer and VoxelMixer. For functional connectivity, the authors presented a Temporal Graph Mixer with a Temporal Pooling Mixer. For each encoder, they developed additional patching strategies. To train the multi-view model, the authors adapted an objective based on the maximization of mutual information (using InfoNCE estimator) between global embeddings of the time series and its functional connectivity and between local-global embeddings of the time series. The results show improvements in performance across multiple datasets, modalities, and baselines.

### Strengths
- The authors presented experiments with multiple datasets and modalities (fMRI, EEG, MEG) and compared the proposed model to various baselines.

### Weaknesses
 - Experiments:
  - The experimental design is poorly described. It is unclear whether the manuscript uses all available data during unsupervised/self-supervised pre-training or only the training set. Otherwise, when all the data is used, the self-supervised model may already remember the data, boosting the performance in downstream tasks on the test subset.
  - The cross-validation is unclear. Do you use training, validation, and hold-out sets? Validation sets must be used only to determine hyperparameters and checkpoints. The final performance must be reported on the hold-out test set.
  - Furthermore, did you ensure that splits do not contain the same subjects?
  - The comparison in Table 2 seems unfair when the setting is not described: the type of encoders and their capacity, the type of modalities used for downstream tasks, and whether pre-training is used. Baselines can use architectures with different capacities or might not utilize pre-training; hence, the performance might be worse due to capacity, use of concatenated embeddings from fMRI and FNC, or warm start.
- Rigor:
  - Table 1: There is no description of class distribution; hence, using Accuracy in Table 1 is unjustified, and you need to use additional metrics. It is important to show the confusion matrix to understand the performance of the model in each class.
  - Table 2: It is unclear whether the models give well-calibrated predictions because AUC's shortcoming is that it does not measure whether a prediction is calibrated. Hence, you might have better performance with worse calibration. Reporting Brier score or calibration curves would be beneficial.
  - Table 2: Anomaly detection asks for AUC PR because there are many "normal" cases and very few "anomalous" cases.
  - Statistical analysis for Table 2 and Table 3 has not been performed. Please compare statistically the performance of the models (best versus other) and then correct p-values for multiple comparisons. The normality assumption of the t-test must be checked, and if not met, a non-parametric test like Wilcoxon should be used.

- Clarity: 
  - The manuscript should clearly show that, specifically, joint pre-training of fMRI with Functional Connectivity is beneficial as the first contribution. The second contribution is the improvement of MLPMixer to fMRI and functional connectivity. The third contribution is 
functional patching. Currently, it is not clear whether the main performance comes from the proposed encoder architectures, functional patching, the unsupervised multimodal pre-training itself, or concatenated embeddings from fMRI and FNC. There are a lot of contributions that could be ablated and compared separately with other baselines.
  - The section "How Does Brain Detect GAN Generated Images?" has a very cramped discussion, and the experiment design is unclear. What was the performance of the GAN used in synthesized images? Also, the differences are shown only visually, and no numerical values are shown on how these distributions differ globally and locally (region-wise).
  - Figure 3 shows the distribution of detected abnormalities. How do you get the distribution? Where is the color bar? How do you test? Do you show the p-value, or do you show the effect size? Have you done FDR corrections based on p-values?

- Missing related work:
  - MLP mixer has been applied previously to fMRI data (Geenjaar et al., 2022). Additionally, in the same work, spectral clustering was used to develop a patching strategy for fMRI data. I have not found ablation for the patching approach in this work; it is unclear how the proposed patching is better.


### Questions
- The appendix is missing. The supplementary material is empty (https://anonymous.4open.science/r/br-CD4D/README.md).

### Soundness
2 fair

### Presentation
2 fair

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
The paper proposes to use the ideas from the MLPMixer paper for multi-view classification of functional neuroimaging data. One view is the spatial voxel information and the other is functional connectivity. For each of the views a different model is constructed and applied: for the voxel time series is a model very close to the MLPMixer, and for the functional connectivity an model that is less clear. The models are pre-trained via use of self-supervised contrastive pre-training. Evaluation is done in classification and anomaly detection settings, where the latter involves introducing a synthetic anomaly into functional neuroimaigng data. Classification performance is interestingly high.

### Strengths
1. The problem of spatiotemporal data analysis is important to the field of neuroscience and brain imaging.
2. The paper demonstrates an interesting application of contrastive pre-training of multi-view networks.

### Weaknesses
1.  The paper is unclear and difficult to follow.
    1.  "Dimension reduction" step of the voxel-Mixer should learn time-window specific spatial components in $W_{\mbox{segment}}^{(s)}$ since logically the voxels needs to be grouped into ROIs. However $\tilde{X}^{(t)}W^{(s)}_{\mbox{segment}}$ seems to be reducing time, not space. Notation is fairly mixed up making it difficult to follow what has been done exactly. The description of the voxel-mixer is confusing, particularly the role of the "segment" operation and how it relates to spatial information. It's unclear how the model aggregates information across voxels within a patch, and how this relates to the claimed goal of learning spatial components. The use of the term "dimension reduction" is misleading, as it appears the operation reduces the temporal dimension, not the spatial dimension as one might expect when dealing with voxel data.
    2.  "Functional connectivity encoder" starts with a connectivity graph $\cal{G}_{F}$ where does that graph come from? This section is also unclear - the source of patches and how they are mixed is very difficult to discern. The description of the functional connectivity encoder lacks crucial details. The origin of the connectivity graph is not clearly defined, and the process of creating patches from this graph is vague. It's unclear how the temporal random walks are implemented and how they contribute to the patch creation. The mixing of patches is also poorly explained, making it difficult to understand how information is aggregated across the connectivity graph.
    3.  Evaluation tasks cite evaluation in classifying ADHD and ASD but results are not reported in Table 1.
    4.  Experiments are not clearly explained. Specifically, how the test and train sets were split?
2.  The contribution to either the ML or Neuroimaging is unclear
    1.  For ML: it appears the paper is proposing to train a model on the functional connectivity graph and another model with a comparable number of parameters on time series. The number of parameters relative to the BNT used in the benchmark roughly doubles since the Temporal Graph Mixer in this paper is doing about what BNT is doing. This parameter doubling not surprisingly leads to improved performance. This is not explained. The paper does not adequately address the increase in model parameters compared to the baselines. The claim that the proposed model outperforms baselines due to its architecture, rather than the increased number of parameters, is not sufficiently supported. A more detailed analysis of the parameter count and its impact on performance is needed.
    2.  For ML: since clasification accuracy is of a major concern, why not compare to Logistic Regression on the FNC data as a much simpler model with much fewer parameters?
    3.  For Neuroimaging: The paper does not show what are the learned voxel groupings. Note, all voxel-level analysis papers with which the current submission contrast the work obtain biologically interpretable voxel maps. The current model supposedly should capture spatial maps like that since it is operating at the voxel level input from subjects. However, these maps are neither presented nor discussed. The lack of visualization of learned voxel groupings is a significant oversight. The paper contrasts itself with voxel-level analysis papers that provide biologically interpretable maps, yet fails to provide such visualizations. This omission makes it difficult to assess the model's ability to capture meaningful spatial patterns.
    4.  For Neuroimaging: What is the significance of Table 2? This problem is almost a toy problem on a synthetic task. This task is barely relevant to the neuroimaging field and the cited workshop is the only paper that uses this synthetic data generation approach for testing the method. The use of a synthetic anomaly detection task in Table 2 raises concerns about the relevance of the evaluation. The task appears to be a toy problem, and its significance to the neuroimaging field is questionable. The fact that the cited workshop is the only paper using this approach further undermines the validity of this evaluation.
    5.  For Neuroimaging: Why the ROIs in Figure 3 are so carefully delineated? The described methods would be unlikely to produce such precisely carved spatial maps. This result is unclear.
3.  Some relatively minor problems:
    1.  Abstract: "toward **revealing the understanding**" what do you exactly mean?
    2.  Abstract: "we bridge this gap", which gap? This is strangely phrased
    3.  The first paragraph of the introduction section is awkwardly written and can gain a lot from a rewrite.
    4.  Page 2: Limitations state that most studies focus on either voxel level or functional connectivity. However, to study functional connectivity researchers usually first extract intrinsic networks from the voxel level, by running ICA, RBM, NMF, Dictionary Learning or any other decomposition. The statement does not seem to hold.
    5.  Page 3 lats paragraph of section 2: MEG and EEG do not readily provide localization of the time-series to parts of the brain. The sensor space recordings need to be projected to the brain volume or surface by overcoming the difficulties of an ill-posed inverse problem.
    6.  Note, that a model that has the characteristics you describe for BrainMixer on page 3 is available:
        -   Mahmood U, Fu Z, Calhoun V, Plis S. [Glacier: Glass-Box Transformer for Interpretable Dynamic Neuroimaging](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10231935/). In ICASSP 2023-2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) 2023 Jun 4 (pp. 1-5). IEEE.
        -   and a paper from 2022 by the same author
    7.  On page 4 Notation: $\tilde{T}$ is not defined.
    8.  On page 4 Notation: is $K$ the same as $|\cal{V}|$? It would be simpler to follow the paper if the notation was consistent
    9.  Page 5: "even after 2 **minuetes**"
    10. Appendix is missing

### Questions
see weaknesses

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper discusses a neural network encoding methodology for learning representations of brain data described both in terms of voxel-activity and functional connectivity. Building on approaches from image or standard data representations the paper discusses the unique challenges of neuroimaging data and specific trainable processing to handle them. The paper presents results on a several data sets including the contribution of more comprehensive processing of a previously released dataset. Superiority of performance is seen across all datasets by a large margin.

### Strengths
The problem is well motivated. Numerous related works are discussed. The approach while taking inspiration from a number of works proposes tailored steps for brain data.  The significant improvements in performance are very encouraging.

### Weaknesses
Since the appendices are not attached to the initial submission and the paper's page limits mean many things are unclear.

Although Figure 1 organizes the many processes involved the level of detail is not sufficient to grasp how the dimensions or arrangement of data changes through the processing.  

Many terms are not precisely defined and the reader is left to guess the meaning (e.g. "temporal graph"). Some times jargon perhaps from other papers is not explained. "Functional patching" is not clear to me.  Another example,  "while in the brain the functionality of each token is important and a different set of
tokens should be mixed differently", I don't understand the word token in this context.  Are the segments akin to attention heads? Calling them segments has a connotation to time.  

**The clarity of the description of the methodology needs improvement:**

In Section 3.1's "voxel-mixer section" the subscript $i$ is not on the interpolated matrix, it appears only  on P and W_flat and isn't consistent. Is this a mistake or meaningful? The dimensions should be listed for these variables to help the reader (same for equation 1). It's not clear to me how softmax and flat operate together. 

$t_p$ appears twice and its not clear it has same meaning. Once is the length of the functional patch's time dimension in the "voxel-mixer section" and once it is the previous tilmestep in the "temporal patching" section. 

At the end of Section 3.2, dimensions are missing and subscripts "token" are not clear.  

The objective function has variables that are not clear (Z_V is not defined) and doesn't match the description which states that mutual information between functional connectivity and voxel activity is maximized. H_voxel and Z_V are both about the voxel activity. And $\psi$ and Z_F are about the functional connectivity. H_time which is a function of H_voxel is not used in the objective.  

In notation $\tilde{T}$ is not defined and probably should also be a function of $t$ if windows of a task are not same length. 

In the "functional patching" section, it is not clear if the patches are contiguous voxels or how are voxels in a function system arranged. It is not clear how linear interpretation would work in such a coordinate system unless this uses the 3D location of the voxels/channels. 

Some choices in the processing seem arbitrary and the paper doesn't motivate them all. It's not clear to me why the node uses a weighted average of timestamp encodings while the edge uses a single. 

A weakness is the lack of discussion of hyper-parameter selection for the method or baselines. At the end of the methodology data augmentation is discussed. This has a number of parameters itself, and itself can account for differences in performance if other methods are not trained on augmented data. The paper states "The effect of the walk length on performance peaks at a certain point, but the exact value varies with datasets", which means that a valid hyper-parameter selection algorithm (that does not have access to testing performance) is need. Without a valid hyper-parameter selection the impressive results are called into question. 

**Minor:**

In abstract "single beta weight" is jargon. Perhaps a "single weight relating the voxel activity to the task".  Also patching is not common in graph terminology, perhaps "local subgraphs". "Temporal graph" is also not clear from context or standard usage.

"jointly learn voxel activity and functional connectivity" -> "jointly learn representations of the voxel activity and functional connectivity"

"minuetes"

### Questions
How are the set of edges and functional systems obtained for the different modalities? 

How does the linear interpolation work (for both fMRI and EEG)? Are voxel/channel locations needed? 

In section 3.2 what is meant by a temporal graph?  Why is temporal graph used to describe connections between voxels across different time points?

In the temporal patching section, wouldn't it be better to call it a spatiotemporal random walk? 

Is the edge set $\mathcal{E}^{(t)}$ fixed and how is it defined or computed? 

The operation of softmax in (2) is not clear. Is it element wise to give as output a vector that lies in the probability simplex (argsoftmax) or does it literally return the softmax scalar, and if so which dimension does it operate along?
 

 How is hyper-parameter selection performed (including for augmentation)? 

Are other methods trained with defaults hyper-parameters or is a fair search done for them? Is the same data augmentation used for all methods?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

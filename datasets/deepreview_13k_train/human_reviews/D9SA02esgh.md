# MorphOcc: An Implicit Generative Model of Neuronal Morphologies

- Decision: Reject
- Scores: 3, 6, 3

## Abstract
Understanding the diversity and complexity of the morphology of different types
of neurons is important for understanding neural circuits. We need quantitative,
unbiased methods to capture the structural and morphological features of neurons.
With the advent of large-scale structural datasets, this analysis becomes feasible
using data-drive approaches. Existing generative models are limited to modeling
dendritic and axonal skeleton graphs, without considering the actual 3D shape. In
this work, we propose MORPHOCC, a model that represents the diversity of neu-
rons in mouse primary visual cortex (V1) in a single neural network by encoding
each neuron’s morphology into a low-dimensional embedding. From this embed-
ding the 3d shape can be reconstructed. We train our model on 797 dendritic
shapes of V1 neurons. The learned embedding captures morphological features
well and enables cell type classification into known cell types. Interpolating be-
tween samples in embedding space generates new instances of neurons without
supervision. MORPHOCC has the potential to improve our understanding of neu-
rons in the brain by facilitating large-scale analysis and providing a model for
representing neuronal morphologies.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors of the paper introduce MORPHOCC, a neural network model designed to capture and represent the diversity of neuron morphologies in the mouse primary visual cortex (V1). The model encodes the morphology of each neuron into a low-dimensional embedding from which the 3D shape can be reconstructed. Trained on 797 dendritic shapes of V1 neurons, the model's embedding effectively captures morphological features, aiding in cell type classification. The model also enables the generation of new neuron instances through interpolation in the embedding space.

### Strengths
- The approach addresses the essential need for quantitative, unbiased methods to capture and represent the structural and morphological features of neurons.
- MORPHOCC's ability to reconstruct 3D shapes from a low-dimensional embedding offers potential benefits for representing and analyzing neuronal morphologies.

### Weaknesses
 - The reliance on existing deep learning architectures like the PointNet encoder and SIREN decoder, without significant modifications or enhancements, raises concerns about technical novelty, especially considering the high standards expected for technical novelty in ICLR. The encoder and decoder are used in a standard way, without any novel architectural contributions or modifications to adapt them to the specific challenges of neuronal morphology. This lack of innovation in the core model architecture is a significant concern.
- The training dataset consists of only 797 neurons, raising concerns about the model's ability to generalize, especially when applied to classifying and generating new neurons outside this limited set. This is somewhat evident from the very high IoU scores and limited diversity of interpolated samples in Figure 5. The limited size of the dataset makes it difficult to assess the true generalization capabilities of the model, and the high IoU scores suggest that the model may be memorizing the training data rather than learning generalizable features of neuronal morphology. The lack of diversity in the interpolated samples further reinforces this concern.
- Using linear interpolation in the embedding space to generate new neuron instances may not produce neurons distinct from those seen during training. Essentially, this method interpolates between two known neurons, resulting in a neuron that isn't morphologically much different from the original ones. Linear interpolation in a high-dimensional latent space may not capture the complex non-linear variations in neuronal morphology. This approach may only generate variations within the convex hull of the training data, limiting the model's ability to generate truly novel and diverse neuronal structures.

### Questions
- When generating neurons via interpolation, how do structural details, like dendrite branching and length, evolve?
- What specific measures were taken to prevent overfitting, especially given that directly learning the embeddings led to overfitting?
- How might these findings be used in real-world applications, like neuroscience research or medical diagnostics?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a generative model of mouse V1 neuron shapes built with a PointNet encoder and an optional SIREN (MLP) decoder predicting a volumetric occupancy map. The encoder embeddings are shown to capture semantically meaningful features of the neurons useful for cell type, polarity and layer origin classification, while the generated meshes compare favorably with baseline methods. The embeddings are also shown to be useful for neuron retrieval and kNN cell type classification.

### Strengths
- Baseline methods for neural morphology generation only operate on skeletons, whereas MorphOcc uses a richer volumetric representation.
- The paper is overall well written and very easy to read.
- Sec. 2 provides an excellent overview of related work.
- A clean set of proofread dendrites is used for experiments, sourced from one of the largest public volume EM datasets.
- Local IoU metric is proposed to compensate for limitations of IoU when applied to volumetrically sparse objects like neurons.
- Results convincingly show that the embedding captures semantically meaningful features of neurons.
- The proposed model is evaluated against different baseline models of shape generation, and the paper reports results for different encoder architectures.

### Weaknesses
 - Only a single EM dataset is used in the paper. Have you considered other proofread volume EM datasets, particularly ones that are from different species, e.g. fruit fly?
- The interpolation results are not convincing in that the generated meshes seem to have disconnected components and thus not represent valid neurons.

### Questions
- How would the model scale for significantly larger neurons? Notably, axons can be much longer than dendrites, and fill space in an even sparser manner.
- Have you evaluated the impact of a larger latent dimension size?
- How were the ratios of points to sample from the different classes determined? (section 3.2)

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
- Morphocc is a generative model for soma + dendritic tree of cortical neurons. 
 - The input consists of 3d point clouds derived volumetric reconstructions of neurons imaged with electron-microscopy. 
 
 The model has two main components:
 1. A Pointnet learns a global representation vector per dendritic tree.
 2. An implicit decoder (SIREN) learns a function (conditioned on the global representation) that assigns whether a given position is on a given neuron or outside of it.

Authors use an EM microscopy dataset of ~800 neuron morphologies, and perform comparisons to justify architecture choice, share classification results to validate representations, and showcase reconstructions from latent traversals.

### Strengths
- S1. Manuscript is clearly written and easy to follow. 
 - S2. The authors come up with a scheme of training that provides reasonable reconstructions of training set soma + dendite shapes from point clouds, with a relatively small number of neurons
 - S3. Authors perform detailed comparisons with various encoder and decoder choices

### Weaknesses
 - W1. The method doesn't quite learn topology of neuronal dendrites. For example, in the latent traversals, the intermediate shapes are broken pieces and not valid dendritic trees (Fig 5). This is further exacerbated by post-processing.
> To enhance the quality of our reconstructed meshes used for visualization, we remove small components using a greedy algorithm that progressively adds com- ponents until at least 75% of the vertices are included.

 - W2. The volume bound has to be selected a-priori for the dataset. This approach seems to not be extensible for non-local morphologies (e.g. considering long range axons would require looking at the entire brain volume)

 - W3. It seems that the network has to be evaluated on points spread throughout the entire volume to create the iso-surface. This seems quite expensive to generate a single neuron's dendritic morphology.

 - W4. I think the following statement is a bit of an over-reach, since no tests are performed with out of distribution samples.
> Moreover, this process serves as a testament to the model’s generalization capabilities, as it effectively handles out-of-distribution samples.

 - W5. Overall, I think capturing connectivity (e.g. tree structure) should be a crucial ingredient in generative models for morphology. This is not captured in the current model. There isn't methodological novelty (Pointnets and SIREN are off-the-shelf components).

### Questions
- Q1. If one had 10x or even 100x as many morphologies, how would this method accommodate this? Is it mainly through increasing complexity of the decoder?

 - Q2. Could the authors elaborate on the no encoder experiment? Specifically, how is this aspect trained, and what embeddings is this referring to:
> Directly learning the embeddings (no encoder) produces the most accurate reconstructions, but the embedding space was not organized semantically at all

 - Q3. The soma position and coarse dendritic density are very suggestive of the cell types. In Fig 2, the representations seem organized by that. Is this a fair assessment? If so why is classification a good test of representations?

 - Q4. While not explicitly so, the volume is the same for the entire dataset, and the soma / origin of the dendrites contains layer information. Do the authors agree?
> Some of the layer 6 cells are more dispersed as they morphologically resemble inhibitory and more superficial cells, and the model is not provided with the laminar location.

 - Q5. A comparison of classification results with something simple e.g. density representation / PCA of the neuron point cloud (with similar bounding boxes and normalization as chosen for the model here) would help assess the improvements better.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

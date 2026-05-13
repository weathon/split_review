# Compositional Search of Stable Crystalline Structures in Multi-Component Alloys Using Generative Diffusion Models

- Decision: Reject
- Scores: 3, 3, 3

## Abstract
Exploring the vast composition space of multi-component alloys presents a challenging task for both \textit{ab initio} (first principles) and experimental methods due to the time-consuming procedures involved. This ultimately impedes the discovery of novel, stable materials that may display exceptional properties. Here, the Crystal Diffusion Variational Autoencoder (CDVAE) model is adapted to characterize the stable compositions of a well studied multi-component alloy, NiFeCr, with two distinct crystalline phases known to be stable across its compositional space. To this end, novel extensions to CDVAE were proposed, enhancing the model's ability to reconstruct configurations from their latent space within the test set by approximately 30\% . A fact that increases a model's probability of discovering new materials when dealing with various crystalline structures. Afterwards, the new model is applied for materials generation, demonstrating excellent agreement in identifying stable configurations within the ternary phase space when compared to first principles data. Finally, a computationally efficient framework for inverse design is proposed, employing Molecular Dynamics (MD) simulations of multi-component alloys with reliable interatomic potentials, enabling the optimization of materials property across the phase space.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a method and workflow for the generation of stable crystal structures, specifically targeting high entropy alloys.
The method is based on a cystal diffusion variational autoencoder (CDVAE) with an added classification model that predicts the crystal structure (FCC or BCC) based on the latent space representation.

### Strengths
From a modeling point of view, the biggest contribution of this work is the addition of a phase prediction network, that predicts whether the local structure around an atom is FCC or BCC. According to the authors' CP G-distance and qualitative visualisations this improves the structural integrity of the generated crystals structures.

### Weaknesses
Overall the paper is difficult to follow for machine learning specialists (main ICLR audience), because the main discussion points are with respect to the properties of the generated structures and less about the design choices regarding the model and the evaluation of the proposed improvement.
It is unclear whether the "local search for data augmentation" is used for expanding the training set or it is used to jump out of local minima during the langevin dynamics optimization of structures.
The authors introduce a local reconstruction score. It is not clear to me whether this metric is used as a replacement for the 
reconstruction error of the CDVAE during training or if it is only used as a final evaluation metric. And why is it important to only score the local structure. And if it is better than the usual reconstuction error of the VAE, why is it not used as the cost function for training? In 4.4 the authors write that the model is able to find bulk modulus that are similar to the values found during local search. How much faster is the search using the model vs the local search that doesn't use machine learning? Did the model use the local search data for training? If that is the case we don't really gain anything from using the model.

Overall the presented results might be good and sound, but the framing of the paper and each experiment is not clear enough
to make a judgement about the soundness of the results.

### Questions
Do you use different cell sizes (number of atoms) for training and testing? Does the model generalize to different number of atoms?
How big is the training set?
During training do you use the output of your crystal phase classifier as input to the decoder or do you feed the label directly into the decoder instead of predicting it?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper addresses the problem of discovering new, stable high-entropy alloys with generative machine learning. In particular, the paper proposes a modification of the Crystal Diffusion Variational Autoencoder (CDVAE) to be able to classify the phases of the ternary allow NiFeCr. Besides that, the paper contributes a data set for the aforementioned alloy and a method for augmenting the data set.

### Strengths
One of the positive aspects I see in this paper is that it tackles a problems that remains mostly unexplored in the machine learning for materials community, namely the discovery of high-entropy alloys with generative models. Another strength is the contribution of a data set for this problem, which the authors mention that would be made available upon acceptance (specifically, the data set creation workflow). The data set includes DFT and MD simulations.

### Weaknesses
 I have a few important concerns that I would like to discuss.

First of all, in my opinion the presentation and clarity of the manuscript could be largely improved. One challenge I faced throughout the paper is the difficulty to understand important details of the problem, methods and result. I believe that an important reason for this difficulty is the extensive used of materials or physics jargon. Even though I can safely say that my materials and physics background is stronger than the average machine learning researcher's, I had significant difficulty in following some sections. Therefore, I suspect that it would also be hard for most of the NeurIPS audience. To point at some examples, one is Section 3.4 Reconstruction Scores, which refers to multiple methods that will probably be unknown for the majority of the machine learning community, including many of those working in materials-related applications. Specifically, the paper mentions reconstruction scores based on metrics like the Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE) but does not clearly explain how these are computed in the context of the crystal structures or why these metrics are appropriate for this task. Section 3.1 was also particularly difficult to parse for me. The description of the Crystal Diffusion Variational Autoencoder (CDVAE) architecture and its adaptation for the high-entropy alloy problem lacks clarity, making it hard to understand the specific modifications and how they contribute to the classification of phases. More generally, I think that especially Section 3 could be further adapted to the NeurIPS audience. As another example transversal to the entire paper, I would note that the concept of "phase" plays a central role throughout the paper but it is nowhere defined. While the specific meaning in materials discovery or specifically in the domain of high-entropy alloys will obvious to the people in the field, this is a word with multiple meanings depending on the domain, even in different physics subdomains. I would recommend to explain as much as possible such concepts taking into account the target audience of the conference.

There are other aspects of the presentation that could be improved, in my humble opinion. For instance, the use of the figures could better support the text and ideally be self-explanatory. Figure 1 is not referred to in the text and the three-letter caption does not help a lot in its interpretation. Figure 2 also has a very short caption and I have not been able to make sufficient sense out of it, even after carefully reading the text. If I understand correctly, Algorithm 1 in page 5 refers to the property optimisation described in Section 3.3. However, the caption is merely a title and the algorithm contains a multitude of variables that are barely described in the text. For example, the algorithm uses variables like 'z', 'T', 'E', and 'x' without defining their physical meaning or how they relate to the alloy system. Incidentally, I would strongly recommend to use the LaTeX mathematical mode to write mathematical variables in the text (see, for instance, the second-to-last paragraph in Section 3.3).

Generally, one aspect of the presentation that could potentially be improved in multiple sections is that I found it difficult to understand what are the important pieces of information and what are less important details. I would recommend trying to devise a way to help the reader, of the machine learning community, understand the contributions of the paper, both with a clear structure and descriptions as well as with the help of diagrams. 

I found the discussion of the related work rather shallow. I think the paper effectively identifies relevant articles from the literature but falls short at putting them in context and explaining their relevance for the present manuscript.

Regarding the contributions, while I acknowledge that the domain is mostly unexplored, I would also note that the proposed method is a slight modification of the existing CDVAE and that the data set and experimental evaluation is limited to a specific alloy (NiFeCr). Therefore, it is uncertain whether the proposed framework will be applicable to other alloys and whether future research can easily build upon this work.

### Questions
My only question to the authors is whether they plan to make the data set available. The paper mentions that the "workflow" will be made available but it is unclear to me whether that will be sufficient for the community to follow up the work.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This submission seems to use a generative model to search for new HEA structures.

### Strengths
The problem seems to be new and significant.

### Weaknesses
The paper is too hard to follow. I'd like the make clear that I am trained in machine learning and have a weak background in chemistry. However, I have no problem reading the paper "Crystal Diffusion Variational Autoencoder for Periodic Material Generation".

In this paper, I understand the goal is to search for new HEA structures. But I don't understand how this is achieved by the work. I think the submission does not have a clear problem formuation, e.g. what is the structure of one training sample?

 Here is a list of detailed questions. 

1. In "Dataset creation with MD", what is one data point in the dataset? Is it a graph with node features? Could you give a clear definition of the sample space?

2. "Diffusion autoencoders are trained in a self-supervised manner, by removing the artificially induced noise of varying magnitudes from the data." What is the input to the model? How is the self-supervision task formed?

3. The training of "P-CDVAE": is the phase an observed variable so that you can trained the denoising model to predict the phase? 

4. "Local search for data augmentation": the data augmentation seems to be different from data augmentation in machine learning. Here the local search is used to optimize some property of structure, instead of increasing training data. 

5. "In order to cover the random ordering of the atoms in a specific point in the composition space," I don't see why node ordering should play a role here.

### Questions
Please check my questions above.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

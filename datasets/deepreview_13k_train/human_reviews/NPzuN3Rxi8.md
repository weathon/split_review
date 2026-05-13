# TAVRNN: Temporal Attention-enhanced Variational Graph RNN Captures Neuronal Dynamics and Behavior

- Decision: Reject
- Scores: 3, 3, 5, 1

## Abstract
We introduce Temporal Attention-enhanced Variational Graph Recurrent Neural Network (\TV{}),  a novel framework for analyzing the evolving dynamics of neuronal connectivity networks in response to external stimuli and behavioral feedback. \TV{} captures temporal changes in network structure by modeling sequential snapshots of neuronal activity, enabling the identification of key connectivity patterns. Leveraging temporal attention mechanisms and variational graph techniques, \TV{} uncovers how connectivity shifts align with behavior over time. We validate \TV{} on two datasets: \textit{in vivo} calcium imaging data from freely behaving rats and novel \iv electrophysiological data from the \DB system, where biological neurons control a simulated environment during the game of \textit{pong}. We show that \TV{} outperforms previous baseline models in classification, clustering tasks and computational efficiency while accurately linking connectivity changes to performance variations. Crucially, \TV{} reveals that high game performance in the \DB system correlates with the alignment of sensory and motor subregion channels, a relationship not evident in earlier models.
This framework represents the first application of dynamic graph representation of electrophysiological (neuronal) data from \DB system, providing insights into the reorganization of neuronal networks during learning. \TV{}’s ability to differentiate between neuronal states associated with successful and unsuccessful learning outcomes, offers significant implications for real-time monitoring and manipulation of biological neuronal systems.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces a new modeling approach called temporal attention-enhanced variational graph recurrent neural network (TAVRNN). The model is a graph RNN trained with a variational objective allowing the generation of latent spaces through time from a dynamically changing graph. The model adds an additional attentional mechanism that allows update of latent states based on all previous time steps. They train this model on two datasets: 1) a e-phys dataset from the hippocampus of a rat moving on a track and 2) a “DishBrain” dataset of neurons, cultured in a dish, playing a game of pong. The authors show that their model performs comparably to state of the art methods. Their approach improves the models ability to model changing topology of the underlying graph structure of the data in response to behavior modes. The authors show that clustering in the embedding space shows the model’s ability in learning the representation of sensorimotor neural activity.

### Strengths
The paper proposes a sophisticated modeling approach to tackle a big challenge in neuroscience. The application to the Brain in a dish seems promising. The application of GNNs to understand spatial patterns of neural activity seems like a promising approach.

### Weaknesses
 - The presentation was rather weak and calls into question the quality of the work. At various points, the authors switch back and forth about the type of data they are using. (Is it electrophysiological or calcium imaging data?).
- Figure 2 especially could use much more information (e.g. in the caption) to clearly describe the model. 
- Line 440-444, make a claim that has no figure / data to back up. 
- The innovation over previous models seems quite minimal. For the first example dataset, adding temporal attention, this work’s primary innovation, seems to only minimally improve performance over prior work. 
- The first dataset seems like an odd choice, given that quite simple methods, such as standard positional decoding, have long been shown to be effective. No comparison to much simpler standard methods was shown. I don’t believe this choice of data is a very good one to illustrate the potential of this method. 
- The significance of the TAVRNN method claimed in the abstract and introduction, doesn’t seem to match up with the performance and evaluation presented at the end of the paper. Would love to see a stronger connection between questions specific to the two datasets and the method proposed.
- In the abstract, TAVRNN is proposed to provide insight into the reorganization of neural networks during learning. It is unclear how accuracy of classification/clustering in place/sensorimotor encoding is related to adaptive learning. Could benefit from providing more evaluations on the single node connectivity dynamics learned by TAVRNN compared to GRNN. 
- Table 2: ablation study focused on temporal attention feature, which is the core contribution of the paper, only shows very marginal improvements compared to previous work VGRNN. Would love to see more justification on the necessity of adding attention to the application onto two datasets.

### Questions
N/A

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
This paper introduces a deep probabilistic latent dynamics model that uses graph RNNs and an attention mechanism to model the time evolution of pairwise correlations across a neural population in a lower dimensional embedding space. The approach is applied to a hippocampal rat data set, as well as a novel dataset involving in vitro brain culture trained by a closed-loop control MEA system to play a modified version of the pong video game. Ablation results are provided on variants of the model applied to the rat dataset. The paper shows insights into the brain culture population structure associated with varying performance in the game.

### Strengths
The paper combines a number of cutting-edge approaches (variational GRNNs, attention) and applies them to an exciting dataset involving in vitro closed-loop learning of a complex task, with potentially interesting insights.

### Weaknesses
The paper seems to be addressing an exciting application area with potential for very interesting insights into learning. However, given the serious limitations of this work I don’t recommend publishing this paper at ICLR in its present form. 

I found the premise compelling and spent a lot of time trying to understand the paper, but found the paper presentation sprawling and unfocused, with the conceptual goals and key mathematical setup quite hard to follow. The conceptual figure explaining the model is fairly confusing as well. Claims on the performance and potential impact of the model in the paper seem substantial, and it seems unclear that they are well justified by the evaluations presented here. 

If I followed correctly, it seems like a simple conceptual summary of the technical approach is: the authors want to model the time varying correlation structure of the network Xt at each timepoint, which seems like a good goal, by learning to reconstruct a thresholded adjacency matrix A. They would like to do this using a temporal latent variable model, ie by learning dynamics acting on a low dimensional latent space Z that summarizes this high dimensional structure. To facilitate this, they’ll also pass X, the unthresholded correlation matrices, to the latent dynamics function and inference network. An RNN will keep track of the history of the correlations going back beyond the previous timepoint. Confusingly, the Z dynamics function (transition network prior) operates on Ht or the summary of the past history provided by the inference RNN, so no explicit dynamics on Zt are learned (equation 8a). There is an attention mechanism applied to the history of H used to update Ht, further obfuscating the learned dynamics but potentially improving performance. This produces two latent state spaces of interest, one on Z and one on H, with line 295 referring to {Z,H} as the learned embedding spaces. It’s unclear how the two will be used for analysis: for example which of the two, or both, are used to visualize embeddings learned by the model. 

It would be helpful to write down the (generative) graphical model involved, ie Zt -> Xt -> At, as well as the time evolution of z. If i understand correctly, At should be conditionally independent of Z when considering X, since the adjacency matrix is a thresholded version of the correlation features?

The model presented is quite complex, so it is important to explain the goals of the model, to motivate why the complexity of the proposed model is necessary to achieve these goals, and why the benchmarks used to evaluate the model are both appropriate for these goals and for showcasing the particular capabilities of the model.

**Goals of the model:**

- It’s unclear why learning the adjacency structure, vs the full, thresholded correlation matrix X is a desirable goal for the model, since we can always apply thresholding afterwards. Is this easier than learning the full correlations X? Is there another reason for framing this as the objective?

- Is the learned time dynamics function also of interest, and if so how is it made accessible / interpretable and used for analysis? If not, what are the advantages of learning a temporal model, vs fitting a static latent variable model like a graph VAE to each timepoint / snapshot separately? Performance on the classification metric on the rat dataset for the model is better than for VGAE, but VGAE also outperforms some of the other temporal models, suggesting this benchmark may not be a good test of the advantages of a temporal model (more on this below). 

- It would be helpful to clarify what the desired capabilities of a learned embedding model are, and how these differ from the objective function used to train the network, as well as to motivate why it is advantagous not to include these downstream tasks in the objective in some way (eg generalization, emergent properties etc).

**Appropriate validation metrics:** 

- The model is trained to reconstruct the thresholded connectivity matrices At, but no metrics on the ability of the model to reconstruct these using the inference approach seem to be provided. Additionally, no test of the generative quality of the learned dynamics, when run in forward or generative mode, is shown. It would be important to show how the model compares on these with other complex models for which results are presented, as well as simple baselines, such as static models like VAE/GVAE variants, or even PCA. It is possible that Table S1 in the supplement, which does not have a legend explaining it or a reference in the text that I could find, includes something like this kind of result?

- 5.1 - if I understood correctly, this benchmark is a binary classification task that involves decoding whether the data comes from the start or end of the track the mouse is on. It’s not clear why this is a desirable target benchmark from the perspective of showing this complex model's capabilities, or whether it is challenging or easy. A relevant simple baseline benchmark may be decoding these labels from the recordings themselves, from the raw correlation matrices computed on the raw data (eg Xt), or even from a projection onto the first d PCs of the raw data, where d is equivalent to the dimensionality used by the model. If this classification is easy to do from the raw data, then this test seems like a sanity check that the latents are encoding structure in the data, rather than a particular advantage of the model. It is also worth noting that another model, GraphERT, performs better in this benchmark on accuracy and other metrics except recall, where it is very close. 

- 5.3 -  On this dataset as well it would be useful to show how the network performs on the task it was trained to do -- reconstructing the network adjacency matrices. 

**Impact**

Supp. Figure S4 seems to be the most interesting and impactful scientific result, indicating that the model’s learned representation can give insight into network structure underlying variable performance, but this is hidden in the supplement.

### Questions
- What is the dimensionality typically used for Z (or H? if that is the important embedding space) and how is it chosen?
- figure 5 -- how are labeled channels being embedded in the latent space presented here? Wouldn’t each point in the embedding space represent an embedding of a full network structure At?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work proposed a nonlinear and stochastic graph unsupervised representation learning to study neural activities data. This model integrates an attention-enhanced graph neural network to construct node representation from dynamical neuronal connectivity, temporal components are extracted using recurrent neural network and temporal attention mechanism to learn a time-dependent state matrix. It further incorporates variational inference frameworks with probabilistic node embedding to reflect uncertainty. The learned representation from this work is evaluated on two datasets including in-vivo calcium imaging from rate to decode position, and in-vitro ephys data from Dish Brain to study structure changes during adaptive learning.

### Strengths
1. This work focuses on a novel and important prospective to incorporate a dynamic view of neuron interaction to learn a temporal adapted graph embeddings with unsupervised learning, which allows study temporal structure changes during different behaviors. 
2. It introduces a novel dataset and benchmark from DishBrain to study how self-organization structure emerge during learning.
3. The work is compared against multiple extensive graph representation baselines, and outperforms others the clustering patterns in the DishBrain datasets, and demonstrate it is more scalable with advantages in time complexity.
4. Comprehensive ablation studies are performed.

### Weaknesses
1. TAVRNN's predictive performance is limited compared to GraphERT in classifying rat's position, as shown in Table 1.

2. The evaluation and benchmarking with other baselines are only based on graph representation approaches, which takes the functional connectivity with measured with zero-lag pearson correlation to start. However, the linearity assumed in this correlation metrics often ignore high-order statistics and nonlinear information in neural dynamics. Others dynamical modeling approaches such as LFADS or self-supervised contrastive learning approaches like CEBRA which directly take the time series as inputs and implemented in a more end-to-end fashion could also be potentially applied to the same tasks. The benefits of learning graph representation are not evaluated and remain unclear. Specifically, the use of Pearson correlation as the basis for graph construction is a significant limitation, as it only captures linear relationships and ignores potential non-linear dependencies and time-lagged effects that might be crucial in neural data. This choice may bias the results and limit the applicability of the model to more complex neural dynamics.

3. It is not clear in the section 5, how does the downstream task evaluations are performed, whether the downstream tasks only evaluate $Z_t$ or memory embedding $H_t$ as well? How are the train/val/test data split designed, whether cross-session, single- or multi-animal are evaluated, more implementation details should be included. The lack of clarity regarding the use of $Z_t$ vs. $H_t$ in downstream tasks makes it difficult to assess the true contribution of the temporal modeling component. Furthermore, the absence of details on data splitting (e.g., whether it is a single session or multiple sessions) makes it hard to evaluate the generalizability of the results.

4. Presentation and writing needs improvement.

### Questions
1. Add more clarification on what does $H_t$ represent? How it will be evaluated?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The authors present a graph RNN-based method for extracting insights from time-varying functional connectivity networks. They apply their approach to recordings of neural activity from two real-world datasets, and demonstrate good performance in classification and clustering tasks. Finally, they underscore the computational efficiency of their method.

### Strengths
The authors demonstrate that their proposed method performs comparably or better to other methods in classifying or clustering relevant behavioral states from observed recorded activity.

### Weaknesses
Much of the methods section appears to have been directly lifted from "A Deep Probabilistic Spatiotemporal Framework for Dynamic Graph Representation Learning with Application to Brain Disorder Identifcation", Yap et al., IJCAI 2024, with no reference to this work. 

Beyond that, the paper is poorly organized. The proposed method, as well as its evaluations, are described in an inscrutable manner. What exactly is being modeled? (Why are we extracting latent features from binarized functional connectivity matrices?) What exactly is used as node features? How are predictions (e.g. for classification or clustering) read out from the model?

I appreciate the clarification regarding how exactly features are readout for downstream tasks. Nonetheless, some things remain unclear. Are the features $Z_t$ used directly for performance quantification in clustering, or are those evaluations being computed on top of the further dimensionality-reduced t-SNE coordinates? Especially if it is the latter, why not simply evaluate classification performance of predicting the correct channel (Sens, R_{down}, etc.) from a linear readout of these features?

### Questions
See above.

### Soundness
1

### Presentation
1

### Contribution
1

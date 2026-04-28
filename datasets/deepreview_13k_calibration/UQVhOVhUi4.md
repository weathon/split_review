# Graph Generation with Destination-Predicting Diffusion Mixture

- Decision: Reject
- Avg Score: 6.25
- Scores: 8, 6, 5, 6

## Abstract
Generation of graphs is a major challenge for real-world tasks that require understanding the complex nature of their non-Euclidean structures. Although diffusion models have achieved notable success in graph generation recently, they are ill-suited for modeling the structural information of graphs since learning to denoise the noisy samples does not explicitly capture the graph topology. To tackle this limitation, we propose a novel generative framework that models the topology of graphs by predicting the destination of the diffusion process, which is the original graph that has the correct topology information, as a weighted mean of data. Specifically, we design the generative process as a mixture of diffusion processes conditioned on the endpoint in the data distribution, which drives the process toward the predicted destination, resulting in rapid convergence. We introduce new simulation-free training objectives for predicting the destination, and further discuss the advantages of our framework that can explicitly model the graph topology and exploit the inductive bias of the data. Through extensive experimental validation on general graph and 2D/3D molecule generation tasks, we show that our method outperforms previous generative models, generating graphs with correct topology with both continuous (e.g. 3D coordinates) and discrete (e.g. atom types) features.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work outlines the destination-predicting diffusion mixture, which is a novel framework using a mixture of learned OU bridge processes to generate graph data. The purpose of this method, as opposed to traditional diffusion approaches which invert a learned a mapping from noise to data, is to explicitly predict the (distribution of the) destination of a diffusion process sending noisy samples to a data distribution. The main claim is that this destination prediction facilitates more effective modeling of graph-structured data, as opposed to typical diffusion models like DDPM. This claim is substantiated by extensive experiments on diverse datasets of small to large graphs.

### Strengths
1. The explanation of the modeling approach is fairly clear, though some of the notation is a bit confusing. Regardless, the authors do well to explain how the mixture of bridge processes is constructed, finally leading to a straightforward objective in Eq (9).
2. The experiments are very thorough; the GEOM-DRUGS result is particularly demonstrative of the improved performance of the destination prediction of DruM. The chemical/physical metrics of Table 2 and Figure 3 do well to highlight that this method is well-suited to real-data scenarios.
3. The simulation-free training and rapid convergence to the destination distribution is a significant advantage when compared to expensive SDE simulation in typical diffusion.

### Weaknesses
1. The main weakness in the paper is the lack of clarity about the argument behind the central claim that destination prediction facilitates more effective modeling of graph topological data. While the experimental results clearly show that this is the case, I failed to understand why this would be the case as I read the paper. The methodology described in Section 3 is completely agnostic to the fact that we are considering graph data, and while I can understand why it might be in general advantageous to predict the destination of diffusion, I'm not sure why this is particularly the case for graphs. The authors claim that destination prediction explicitly learns graph structure, but it is not clear to me how this is the case. Specifically, the method appears to operate on the adjacency matrix as a generic matrix, without explicitly enforcing or leveraging any graph-specific properties during the destination prediction process. This makes it unclear how the method inherently captures graph topology better than a standard diffusion model that operates directly on the adjacency matrix. Maybe this can be explained more clearly early in the text, towards the beginning of section 3.
2. The sampling procedure does not seem to be explained in the main text. Figure 1 (b) demonstrates the diffusion process at sampling time, but since this is not explained in the text, it is a bit confusing to see how to connect the learned ${\bf s}_{\theta}$ to the sampling procedure. It would be better to include Algorithms 1 and 2 in the main body of the text, including a brief explanation of Algorithm 2. The text lacks a clear description of how the learned destination prediction model is used to generate new graph samples, making it difficult to understand the practical application of the proposed method.

### Questions
1. As above, how exactly does destination prediction relate to better graph generation? It is mentioned that it takes the graph topology into account more explicitly, but it is not clear to me how this is the case.
2. How does this approach compare to denoising-diffusion-type models in non-graph settings? While I understand this is not the focus of the paper, I think conducting a small experiment or at least commenting on this would make it clear why destination prediction is well-suited to graph data. As in the previous question, it is not clear to me why destination prediction is connected to the topology of the data.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes to use score function to predict the final graph. The resulting stochastic process is named "Destination-Predicting Diffusion Mixture (DruM).

### Strengths
1. The method is theoretically sound. The underlying stochastic process is well defined.
2. The motivation to forecast the final state at the early de-noising stage is interesting.

### Weaknesses
1. The idea of "prediction results in graphs with correct topology" is not very convincing. The paper does not provide a clear explanation of how predicting a destination mixture inherently leads to correct graph topology, especially given that the destination is a weighted mean of data. It's unclear why this approach would avoid generating graphs with incorrect or unrealistic connections. The connection between the prediction target and the resulting topological properties is not sufficiently justified.
2. Empirical results are limited to small graphs. While the paper mentions experiments on the Protein and GEOM-DRUGS datasets, the scale of these graphs is still relatively small compared to many real-world networks. The performance of the proposed method on much larger graphs, with thousands or millions of nodes, remains untested. This limits the practical applicability of the method.
3. The proposed method sacrifices novelty in generated graph. The method's focus on predicting a destination mixture, which is a weighted average of training data, raises concerns about its ability to generate truly novel graphs. The generated graphs may be too similar to the training data, lacking the diversity and creativity expected from a generative model. This could be a significant limitation in applications where novelty is a key requirement.

### Questions
1. Does Table 4 illustrate a tradeoff between novelty and other capabilities for DruM? If this outcome is a direct consequence of your objective in Eq. (65), would it be advisable to introduce a control mechanism in your algorithm to balance these capabilities?
2. Is it your view that DruM could be better suited for generating large graphs, prioritizing validity and other capabilities over novelty? Do you believe DruM has the potential to alleviate the scalability bottleneck for larger graphs?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes Destination-Predicting Diffusion Mixture:
 - While DDPMs derive the generative process by reversing the forward noising process, DruM constructs the generative process from the mixture of OU bridge processes, which does not rely on the time-reversal approach. The mixture process of DruM defines an exact transport from an arbitrary prior distribution to the data distribution by construction.

### Strengths
Being a graph diffusion paper, the paper makes a very large contribution to the general diffusion literature, as well as the growing literature on diffusion bridge process. The paper, if read with the appendix, is well written. The experiment compares the proposed method to the most comparable recent works and demonstrates great performance.

### Weaknesses
 - The paper mentions in numerous places that the proposed method captures the topology of the graph distribution because it predicts the destination of the diffusion process. I don't understand the arguments there, or if they are attempting to make one. x0-parameterization of DDPM (e.g. Vignac 2023) by definition predicts the destination. Does it capture topology? In fact, every generative model predicts destination in one way or another (VAE, GAN, and $\epsilon$-parameterized diffusion models are equivalent to x0-parameterization). Do they capture topology? "Loss-Guided Diffusion Models for Plug-and-Play Controllable Generation", for example, attempts to generate a destination "distribution" by doing MC on top of an x0-parameterization.
 - The paper assumes that the audience has prior knowledge on bridge processes. The only explanation offered is that they are "processes conditioned to an endpoint," which I find unhelpful. The writing can be improved in this regard.
 - The paper is without a discussion about the graph data structure in use; the omission is made explicit at the end of Sec 3. For this I find the writing difficult to follow at times. How does one take the weighted mean of discrete graphs and molecules? They are finally discussed in appendix B.3, but only in reference to other papers. 
 - The main paper can really use an \Algorithm block from appendix B.2 (although not sure what to remove), to help the readers follow the sampling procedure.

### Questions
- See Weaknesses
 - Why graphs? It appears that the methodology proposed isn't at all particular to discrete/combinatorial data structure.

### Soundness
3 good

### Presentation
2 fair

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes a novel diffusion-based graph generation framework. The framework leverages the process conditioning on the generation destination, which aims to more accurately capture the graph topology. The training objective in this framework can be approximately represented as to predict a weighted mixture/average of the data.  The empirical evaluation of 2D/3D graph generation shows the effectiveness of the proposed methods.

### Strengths
+ This work introduces a new diffusion-based graph generation framework where the generation procedure is conditioned on the destination graph. The framework at a high level combines the benefits of the previous discrete diffusion process for graphs (DiGress) that directly predict the destination, and the continuous diffusion process to handle the potential 3D continuous features that 3D graphs may have. 
 
+ The derivation seems reasonable at a high level. (I have not checked the proof). 

+ The empirical results show the effectiveness of the framework.

### Weaknesses
 - From the technical side, the framework seems to directly leverage the tool from [1][2]. So, the fundamental technique is not novel, though the application to graph generation may be novel. Moreover, the derivation seems to be nothing specified to graph topology but quite generic. So, it is not persuasive that the adopted framework may capture graph topology better than other frameworks. The benefits of practical performance seem to entirely inherit from the previously developed framework [1][2].
 
- Eq.9 seems to just estimate the exact endpoint $G_T$ instead of the destination mixture $D(G_t, t)$. However, Eq.8 is to estimate $D(G_t, t)$, isn't it? This seems a conflict with the statement just below Eq. 9.

### Questions
Please address the two weaknesses: 1) why is the framework related to graph topology? The framework seems to be a direct application of previous frameworks to graph generation; 2) why Eq.9 is to estimate a mixture of data points.

I may re-evaluate this work based on the authors' response.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

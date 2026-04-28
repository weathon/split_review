# Hierarchical Graph Latent Diffusion Model for Molecule Generation

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 8, 3, 5

## Abstract
Recently, generative models based on the diffusion process have emerged as a promising direction for automating the design of molecules. However, directly adding continuous Gaussian noise to discrete graphs leads to the problem of the final noisy data not conforming to the standard Gaussian distribution. Current graph diffusion models either corrupt discrete data through a transition matrix or relax the discrete data to continuous space for the diffusion process. These approaches not only require significant computation resources due to the inclusion of the bond type matrix but also cannot easily perform scalable conditional generation, such as adding cross-attention layers, due to the lack of embedding representations. In this paper, we first introduce the Graph Latent Diffusion Model (GLDM), a novel variant of latent diffusion models that overcomes the mismatch problem of continuous diffusion space and discrete data space. Meanwhile, the latent diffusion framework avoids the issues of computational resource consumption and lack of embeddings for conditional generation faced by current graph diffusion models. However, it only utilizes graph-level embeddings for molecule generation, losing node-level and structural information. Therefore, we further ex- tend the GLDM to the Hierarchical Graph Latent Diffusion Model (HGLDM). By including node embeddings and subgraph embeddings that contain structural in- formation, our model significantly reduces computation time compared to the cur- rent graph diffusion models. We evaluate our model on three benchmarks through unconditional generation and conditional generation tasks, which demonstrate its superior performance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The submission proposes a latent diffusion model for graph generation. The problem definition is very common and can be treated as a distribution-fitting problem. The framework utilizes PS-VAE as an encoding-decoding model. And apply a diffusion model over latent variables.

### Strengths
1. The presentation is good.
2. The structure design for the diffusion model is reasonable.

### Weaknesses
1. Equation (2) is not correct. The probability for each node is computed twice. I think the correct definition should be $\prod p(x_i) \prod \prod (e_{ij})$.

2. The submission claims that they first introduce the latent diffusion model into graph generation. This overclaims the contributions. [1] and many other previous works use latent diffusion models for graph generation tasks. I think the basic idea is the same: only diffuse node variables, and decode edge types from them. This is very common in the area.

3. It is not reasonable to design a hierarchical diffusion model. There is no need to sample three variables $z^x, z^M, z^G$ at the same time. As a hierarchical model, the decoding process of PS-VAE is $ G \sim q(G|z^M)q(z^M|z^G)$. That is, decoding a subgraph from a graph-level vector by a GRU, and then predicting the connection for the subgraphs. So actually, we only need to define a diffusion model over graph-level $z^G$. During the sampling process, we first sample $z^G$ from the diffusion model, and then use decoding of PS-VAE to get the graph. The current framework actually learns the decoding part twice, during the training of PS-VAE, the relationship between each level has been learned already. However, the diffusion model learns it one more time.

4. The results lack MMD metrics. I think it is very important to check the distribution of the graphs. The absence of MMD, especially metrics like the Maximum Mean Discrepancy with a suitable kernel such as the graph kernel, makes it difficult to assess the quality of the generated graph distribution compared to the training data. This is a crucial aspect for generative models, and its omission weakens the evaluation.

### Questions
1. "However, these approaches sacrifice the random exploration ability to ensure that the final noisy data conforms to the appropriate discrete category distribution. " Why do you make such claims? The definition for the distribution of the discrete variables is different. And people can also define a discrete diffusion process over them such as [1] and many other works. The performance is also very good and I think people should select models based on the specific problem. There is no any conclusion to support that continuous features is better than discrete process.

[1]https://arxiv.org/pdf/2209.14734.pdf

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a form of latent diffusion ala Rombach et al. for graphs, in particular, molecule generation. For this they combine a PS-VAE autoencoder with a DDIM style denoising diffusion model which leverages a hierarchy-aware GNN which uses a GAT style subgraph embedding update and PNA pooling for the graph embedding update at every layer.  The method is compared against it's constitutent components and two SotA Diffusion baselines (Digress/GDSS) as well as VAE and other methods on QM9,ZINC250K and Guacamol.

### Strengths
Overall a good "Nothing to complain about" paper.

Originality:

Latent diffusion for graphs was a thing waiting to be done, but it is still worth doing. The hierarchical block is a nice construction, as is the continuous-discrete combo.

Quality: The evaluation including Guacamol is good, the QM9 and ZINC250k benchmarks show impressive results.
clarity: The paper is very clearly presented and the appendix, while sparse, gives most of the information required for presenting things.
Significance: Getting hierarchical graph modeling like this going is likely to have a very high impapct, iff the method generalizes.

### Weaknesses
 - I'd like to see error bars indicating variance accross multiple seeds  if possible
- While QM9 and ZINC250k performance is imprressive, these graphs are kind of solved. What is the performance on MOSES or shapenet?
- There is no limitations section which is always sus, are there really *no* downsides and limitations worth discussing?

### Questions
1. To clarify, you are evaluating all datasets without hydrogens?
2. The PS-VAE is not permutation equivariant right (or does it canonicalize things)? Did you do any experiments with a purely equivariant backbone?
3. Purely because I found this [paper today](https://arxiv.org/abs/2210.02410) and found the idea exciting, if you manage to perform any diversity quantification using graph embedding similarity across the datasets, I'd be curious how the models differ. This is purely a nerd sharing a neat idea though, not a critique of the paper.
4.  There is no limitations section which is always sus, are there really *no* downsides and limitations worth discussing?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a latent diffusion model that aims to generate hierarchical levels of latent variables such as node-level, subgraph-level, and graph-level, simultaneously. To construct the latent space, the authors leverage the PS-VAE where the decoder converts the graph-level latent variables to the molecule by sequentially predicting the fragments and then predicting the links between fragments. To generate the latent variables of node-, subgraph-, and graph-level, the authors leverage the generative process of DDPM. The authors propose an architecture that models the dependency between node-, subgraph-, and graph-level embeddings alleviating the burden of considering the edge features. The proposed method is evaluated on the molecule generation tasks in the conditional and unconditional settings.

### Strengths
* The auxiliary generation of node and subgraph embeddings can enrich the forwarded information of the diffusion process. Specifically, even though PS-VAE requires only the graph embedding in the decoding stage, the authors propose to generate the node and subgraph embedding along with the graph embedding. Defining the correlated generative processes in this paper could convey more information to the model.

### Weaknesses
 * It is not clear why the authors select a way to generate graph embeddings and then decode them. Accessing the graph embedding could contain less information than accessing the subgraph- or node- and edge-level latent variables. The 
* The name of the proposed method is misleading. The goal of the proposed method is to generate the hierarchical latent variables. However, the name (Hierarchical Graph Latent Diffusion Model) can be misinterpreted as a sequence of the diffusion models to generate the latent variables.
* The authors report the validity, uniqueness, and novelty as the main results. However, these metrics seem to be restricted to only measure the sample diversity.
>- For the validity, it is unfair to compare with the denoising diffusion model such as GDSS and DiGress, as the decoding stage of the proposed method and PS-VAE intrinsically do the validity check while linking the fragments. Therefore, reporting and comparing the validity are not enough to demonstrate the effectiveness of the proposed method.
>- For the uniqueness and novelty, they demonstrate that the generative model can guarantee sample diversity. However, to demonstrate whether the generative model precisely learns the data distribution, reporting the uniqueness and the novelty is not enough. Please note that recent works [1,2] leverage FCD, Scaffold similarity, SNN and NSPDK to measure the difference of the generated distribution and the data distribution. Therefore, I believe that measuring the uniqueness and novelty is important, but to demonstrate the effectiveness, it would be better to measure the distributions of the generated molecules.
* The efficiency of the proposed methods seems to come from the light model architecture with smaller dimensions than the model architecture used in the DiGress.

### Questions
For clarification, I would appreciate if the authors provided an explanation of my questions.
1. In Section 4.1.1, to my understanding, the number of subgraph embeddings should not be the number of nodes. If so, how do you sample the number of subgraph embeddings at the beginning of the sampling stage?
2. How do you get the subgraph embeddings from the PS-VAE architecture?
3. In Table 3, how did you measure the mean absolute error (MAE) on the unconditional setting? Does it mean training on the selected 100 molecules without the conditions?
4. Why are some reported values different from the original papers? For example, the novelty and uniqueness of PS-VAE on the QM9 dataset and the validity of GDSS on the ZINC250k dataset.

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work presents a novel hierarchical latent diffusion model for molecular graph generation. To be specific, this work introduces GLDM, a latent diffusion model for graphs using graph-level embeddings, and proposes HGLDM, a latent diffusion model that further incorporates structural information, for which these approaches enable efficient training and sampling while outperforming previous graph diffusion models.

### Strengths
- The paper is well-written and easy to follow. 

- The motivation for using the latent approach, i.e., overcoming the mismatch between the continuous diffusion space and discrete data space and further reducing computational cost, is clear.

- Using hierarchical embeddings of graphs for graph latent diffusion is novel and shows improvements in conditional molecule generation tasks compared to the naive latent diffusion model (GLDM) as well as previous diffusion models.

### Weaknesses
 - Although this work states that the (hierarchical) latent approach for graph generation provides a scalable solution for molecule generation, the provided experiments are limited to datasets (e.g., GuacaMol) in which previous diffusion models (e.g., GDSS and DiGress) are applicable. In order to justify the scalability of the proposed method, it should be evaluated in a larger dataset.

- The experimental setting for evaluating the computational efficiency is not clear. Is the training and sampling time measured in the same condition, e.g., training conducted via DDP and using the same number of V100 GPUs? 

- Generation performance on unconditional molecule generation tasks should be evaluated with more descriptive metrics, for example, FCD, Scaffold similarity [1], and Fragment similarity [1]. Reported metrics, i.e., validity, uniqueness, and novelty fail to measure how similar (e.g., chemical aspects) are the generated molecules to the molecules from the test set. In particular, under the current setting, GDSS seems to be showing comparable results in large datasets (ZINC250K and GuacaMol) with significantly fewer parameters.

- The quantitative results of Tables 2 and 3 show that the performances of GLDM and HGLDM on unconditional generation tasks are almost the same, whereas there is a significant improvement using the hierarchical approach for conditional generation tasks. What is the reason for the hierarchical approach only effective in conditional tasks?

- As the continuous diffusion model (e.g., GDSS) outperforms the discrete diffusion model (e.g., DiGress) in Table 2, the continuous diffusion model should be compared as a baseline in Table 3 (i.e., conditional generation task). Although GDSS does not explicitly present a conditional framework, recent work [2] proposes a conditional molecule generation framework using classifier guidance based on GDSS, which could be used as a baseline.  

- The performance of GLDM (and HGLDM) comes from the effectiveness of using a latent representation of graphs compared to previous graph diffusion models, not from the diffusion processes. Thereby, analysis of the latent representation, e.g., interpolation in the latent space or clustering of the latent points with respect to certain conditions, would greatly strengthen this work.

- Missing references on related works:
  - Qiang et al., Coarse-to-Fine: a Hierarchical Diffusion Model for Molecule Generation in 3D, ICML 2023
  - Xu et al., Geometric Latent Diffusion Models for 3D Molecule Generation, ICML 2023

- I would like to raise my score if the above concerns are sufficiently addressed.

### Questions
- Please address the questions in the Weakness.

- Is the results of Table 2 from a single run or an average of multiple runs?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

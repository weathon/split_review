# Disentanglement Learning via Topology

- Decision: Reject
- Scores: 6, 5, 5, 5

## Abstract
We propose TopDis (Topological Disentanglement), a method for learning disentangled representations via adding a multi-scale topological loss term. Disentanglement is a crucial property of data representations substantial for the explainability and robustness of deep learning models and a step towards high-level cognition. The state-of-the-art methods are based on VAE and encourage the joint distribution of latent variables to be factorized. We take a different perspective on disentanglement by analyzing topological properties of data manifolds. In particular, we optimize the topological similarity for data manifolds traversals. To the best of our knowledge, our paper is the first one to propose a differentiable topological loss for disentanglement learning. Our experiments have shown that the proposed TopDis loss improves disentanglement scores such as MIG, FactorVAE score, SAP score, and DCI disentanglement score with respect to state-of-the-art results while preserving the reconstruction quality. Our method works in an unsupervised manner, permitting us to apply it to problems without labeled factors of variation. The TopDis loss works even when factors of variation are correlated. Additionally, we show how to use the proposed topological loss to find disentangled directions in a trained GAN.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors of this paper present TopDis, which is a regularizer based on Representation Topology Divergence (RTD). In this approach, the objective to be optimized is a combination of “classic” VAE loss and TopDis loss. Unlike the preceding approaches, topDis does not assume statistical independence between the factors of variations. Generally, introducing this loss term appears to further improve the current SOTA values for several disentanglement metrics (FactorVAE, MIG, SAP and DCI) across several different datasets (dSprites, 3D Shapes, 3D Faces, MPI 3D).

### Strengths
1. The paper is clearly written and easy to follow. In detail:

a. The authors explain the task of disentanglement rather clearly by providing a succinct overview of previous works.

b. The motivation and contribution of the paper are also clearly defined with an intuitive explanation of the designed methodology.

2. The authors provide a variety of experiments and ablations, helping to evaluate their proposed disentanglement regularization loss practically. In detail:

a. The experiments (Table 1) appear comprehensive (except for the vanilla VAE; we will explain in the weakness section our concerns).

b. The authors also provide enough qualitative examples, comparing models trained with TopDis regularizer and without.

c. The architecture is succinctly described in the Appendix

3. Computational complexity is also discussed in the Appendix, which is crucial for ML algorithms nowadays.

### Weaknesses
1. One of the contributions the authors mention is: “We improve the reconstruction quality by applying gradient orthogonalization;” - however, this contribution is only briefly mentioned in the conclusion and analyzed in the Appendix in greater detail. We suggest the authors to “move” the gradient orthogonalization part to the main paper.

2. As the authors explained, the RTD was defined in a previous work, but we believe it is important to be defined in the main paper.

3. In section 4.1, bullets (2-4). In (2), g\inG appears to be applied to both pixel and latent space. Later in (3,4), where decomposition G is defined, it seems that it can be applied only in the latent space. We believe the authors should re-write this part, clarifying how G can be applied in the pixel space or, if that is not the case remove from (2) the application of g in the pixel space.

4. In equation (4) regularization parameter /gamma is defined. Later in the appendix Q, \gamma_1, and \gamma_2 are used in the ablation table. Does this correspond, instead, to the loss: \gamma_1 L_{VAE-based} + \gamma_2 L_{TD}.

5. In page 5 footnote, the authors state that RPT can be computed in latent space instead of pixel space. Can the authors provide ablations in the appendix exploring this direction? Do the authors have insights into how this change can affect the final trained model?

6. Finally, our main concern is whether the proposed regularizer contributes to the learning of the disentangled representation or the used base models (i.e., \beta-VAE, Factor-VAE). Since, in the main paper, only the models with already disentanglement remedies are explored and not the vanilla VAE. More concerning in the ablation, VAE+TopDis is explored, but it seems that the training is not the same as the VAE reported in the main paper. Our guess is that the models in the ablation were trained for less number of iterations. We encourage the authors to include in the main paper VAE+TopDis trained under the same conditions (i.e. same number of iterations) as the reported VAE in Table 1. This will help readers understand to what extent the TopDis regularizer helps learn disentangled representations

### Questions
See above

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposed a disentanglement regularization term based on topology, to constrain the manifold relation between the latent points of original images and shifted images. The authors provided extensive experiments on VAE-based methods and showed the effectiveness of the proposed methods.

### Strengths
1.	It is important to explore the constrain in the manifold of latent space for disentanglement, due to the statistical arguments of Locatello et al. (2019). The paper explored a way from topology and proposed a regularization term, which can be easily optimized. 

2.	The paper provided a good formulation of the TopDis loss and how to optimize it in the VAE framework.

### Weaknesses
1.	The relation between the constrain on latent space and disentanglement is still unclear, the TopDis is based on VAE-framework, which is based on Probability, and the paper referred to the definition of disentanglement based Group. And the paper failed to connect the above two framework, and making the proposed TopDis only kind of an intuitive necessary condition, as shown in Figure 3. The paper does not adequately address how the topological constraint imposed by TopDis directly leads to disentanglement. The connection between preserving topological features and achieving disentangled representations is not rigorously established. While the intuition is that preserving topology ensures that shifts in latent space correspond to meaningful changes in the data manifold, this remains an assumption without clear theoretical backing. The use of a VAE framework, which relies on probabilistic modeling, further complicates the link to group-based definitions of disentanglement, which are inherently based on transformations and symmetries. The paper needs a more explicit formulation that bridges these two perspectives, moving beyond an intuitive argument.

2.	From Appendix L, the best performance hyperparameters are quite different across different methods and different datasets, is there any guidance or criterion to choose the hyper-parameter? The lack of a clear methodology for selecting the hyperparameter γ, which controls the weight of the TopDis loss, is a significant concern. The paper reports that optimal values for γ vary considerably across different datasets and methods. This implies that the method's performance is highly sensitive to this parameter, and the absence of a systematic approach to its selection limits the practical applicability of the proposed method. The current approach of using a greedy procedure is not sufficient, as it requires extensive experimentation for each new dataset or method. The paper needs to provide a more principled way for determining the optimal value of γ, which could be based on properties of the data or the latent space.

### Questions
1.	My main concern is the relation between the proposed TopDis and disentanglement, is there any theoretical guarantee or deduction?  
2.	The authors applied the proposed TopDis to infer disentangled directions in a pretrained style-GAN, is there some quantitative results? Then dose the method can be applied to other disentangled methods?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed a novel Topological Disentanglement loss (TopDis loss) that can be added to any VAE-type loss to improve the disentanglement by encouraging the preservation of topological similarity in the generated samples with shifted latent space. Experiments demonstrated the proposed TopDis loss increases the disentanglement performance of several SOTA methods for various disentanglement metrics and datasets.

### Strengths
(1) Inspired by [1], the proposed differentiable Representation Topology Divergence (RTD) as a loss for the VAE-framework looks promising to improve the disentanglement.

(2) Rich experiments are conducted to evaluate the performance of the proposed TopDis loss for various VAE-based methods.

[1] Barannikov, Serguei, et al. "Representation topology divergence: A method for comparing neural network representations." ICML 2022.

### Weaknesses
 (1) It is unclear how the hyper-parameters in Eqn (4) affect the performance. There are γ_1 and γ_2 in Table 9 (appendix N), but there is only one γ in Eqn (4). 

(2) In Table 1, it seems that some advanced disentanglement methods performed significantly worse than the vanilla VAE (e.g. FactorVAE on 3dshapes, and β-TCVAE on MPI3D, etc), making it a little suspicious for the experimental results and/or the model selections of baselines. Besides, two important evaluations of VAE+TopDis and β-TCVAE+TopDis are missing. 

(3) The evaluation of how the proposed methods handle the tradeoff between disentanglement and reconstruction is limited. Besides Table 4 and Table 8, the authors are encouraged to report the reconstruction errors of the proposed method with and without "gradient orthogonalization" for a complete comparison with the baselines. Did the "gradient orthogonalization" apply to the baselines as well?

### Questions
(1) The authors are encouraged to respond to the concerns above.

(2) How the γ should be selected for different VAE-based methods? Does TopDis improve disentanglement when β is already very large? How does the TopDis loss affect the optimization of the original disentanglement loss in those baselines (like the total correction in TC-VAE and FactorVAE)?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors propose a method, named TopDis (Topological Disentanglement), for learning disentangled representations via adding a multi-scale topological loss term. The experiments results show that the proposed TopDis loss improves disentanglement scores such as MIG, FactorVAE score, SAP score and DCI disentanglement score with respect to state-of-the-art results while preserving the reconstruction quality.

### Strengths
- This paper is the first to introduce the use of a topological regularization term in the field of disentangled representation learning.
- The topological regularization term is shown to be effective across multiple VAE models and metrics.
- The regularization term proposed in this paper is also demonstrated to be effective for discovering pre-trained StyleGAN models.

### Weaknesses
 - The paper lacks a clear reasonable explanation as to why topological constraints are meaningful/effective for disentanglement representation learning.
- The new loss function was already proposed in a 2022 ICML paper [a]. The main contribution of this work is applying it to disentanglement, making the explanation of the above issue crucial for this paper.
- The experiments focus on models with some disentanglement capabilities, but the effectiveness of this regularization term on vanilla VAEs has not been studied.
- The performance of vanilla VAEs presented in this paper show high DCI performance, but other papers [b] report poor performance instead. A reasonable explanation is needed, and it would be helpful to include evaluation code in the supplementary materials.

### Questions
See weakness

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

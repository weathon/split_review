# Zebra: In-Context and Generative Pretraining for Solving Parametric PDEs

- Decision: Reject
- Scores: 8, 6, 3, 6, 5

## Abstract
Solving time-dependent parametric partial differential equations (PDEs) is challenging, as models must adapt to variations in parameters such as coefficients, forcing terms, and boundary conditions. Data-driven neural solvers either train on data sampled from the PDE parameters distribution in the hope that the model generalizes to new instances or rely on gradient-based adaptation and meta-learning to implicitly encode the dynamics from observations. This often comes with increased inference complexity. Inspired by the in-context learning capabilities of large language models (LLMs), we introduce \texttt{Zebra}, a novel generative auto-regressive transformer designed to solve parametric PDEs without requiring gradient adaptation at inference. By leveraging in-context information during both pre-training and inference, \texttt{Zebra} dynamically adapts to new tasks by conditioning on input sequences that incorporate context trajectories or preceding states. This approach enables \texttt{Zebra} to flexibly handle arbitrarily sized context inputs and supports uncertainty quantification through the sampling of multiple solution trajectories. We evaluate \texttt{Zebra} across a variety of challenging PDE scenarios, demonstrating its adaptability, robustness, and superior performance compared to existing approaches.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a foundation model to solve time-dependent parametric PDEs. Their architecture consists of a learned CNN encoder-decoder which makes the PDE trajectories into a latent sequence space, and an autoregressive transformer which learns the solution operator on the latent space. The transformer is trained using the cross-entropy loss on the latent space. The model is trained on several classes of parametric PDEs, such as heat, advection, and burgers equations, whose parameters are varied during training. The trained model is then able to perform inference for new equations without any parameter updates. They compare their results with baselines, considering one-shot adaptation, in-context learning, and temporal conditioning. They also explore the ability of the generative model to perform uncertainty quantification on various statistics of the PDE trajectories.

### Strengths
1. The authors take on an important challenge in scientific machine learning, developing reliable foundation models for PDEs. Their method has the additional advantage of not requiring any parameter updates at inference time. Their architecture appears novel and their results are competitive with the compared baselines.

2. Experiments are conducted on a fairly diverse class of PDEs exhibiting different physical phenomena and their results are achieved using a relatively small amount of training data compared to other scientific foundation models.

3. The paper is well-written and easy to follow considering its technical nature.

### Weaknesses
1.The main limitation I find in the paper is that they do not provide any experiments demonstrating the out-of-distribution generalizability of their ICL solver. While the authors vary the PDE parameters between training and inference, it seems that the distribution of the parameters remains the same. For example, for the heat equation, the coefficients of the forcing terms are generated from uniform distributions in a fixed range. It would be interesting to shift the distribution of these coefficients at test time and compare the performance of the pre-trained model. For a more extreme shift, one could use the pre-trained model to generate solutions corresponding to new PDEs that were not seen during pre-training using few-shot conditioning. This is crucial for assessing the true robustness of the model and its applicability to real-world scenarios where parameter distributions may vary significantly.

2. The decoder does not seem to reconstruct the trajectories very well. However, the authors address this in the main text and I see this as only a minor weakness. Specifically, the reported reconstruction errors, while acknowledged, raise concerns about the fidelity of the latent space representation. If the decoder struggles to accurately reconstruct the input trajectories, it suggests that the latent space might not fully capture the essential information, potentially limiting the model's overall performance and interpretability.

### Questions
1. Have you compared your generative solver with the In-Context Operator Network (ICON) architecture introduced in [1,2]? It seems they are not directly comparable because with ICON, the goal is to generate the PDE solution given an initial condition, whereas your model also generates the initial condition. However, I think it is worth discussing the key technical differences between your model and ICON, and, if possible, outline how a direct experimental comparison might be set up. In addition, Table 1 seems to suggest that Zebra is the first model which attempts to solve PDEs in-context. Could you clarify if this claim of novelty is specifically about the combination of in-context learning and generative modeling in PDEs?

2. Could you explain your rationale for using the L^2 norm as an evaluation metric for the generated solutions? I would imagine, since you are predicting a PDE solution, that it might be natural to use the H^1 norm as a metric, or other metrics which are tailored to PDE data.

3. Do you have a sense of how your solution error depends on the parameters of your VQVAE, e.g., the number of codes or the number of parameters of the CNN encoder? You mention that in its current construction, the decoder is limited in its ability to accurately reconstruct the trajectories. I am curious because in [3], the authors identify that the test error follows a U-curve with respect to the spatial discretization size for in-context learning elliptic equations. While the setting of [3] is more mathematically idealized than yours, I wonder if your architecture might exhibit a similar phenomenon.

References:

[1] Yang, Liu, et al. "In-context operator learning with data prompts for differential equation problems." Proceedings of the National Academy of Sciences 120.39 (2023): e2310142120.

[2] Yang, Liu, and Stanley J. Osher. "Pde generalization of in-context operator networks: A study on 1d scalar nonlinear conservation laws." arXiv preprint arXiv:2401.07364 (2024)

[3] Cole, Frank, et al. "Provable In-Context Learning of Linear Systems and Linear Elliptic PDEs with Transformers." arXiv preprint arXiv:2409.12293 (2024).

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The manuscript proposes a data-driven method for solving systems of PDEs given an initial condition and/or trajectories of previous states as context, leveraging in-context learning. The proposed generative model is capable of zero-shot and one-shot learning, generalizing across different parameterizations of a given system of PDEs. To achieve this, the approach combines a VQ-VAE to represent physical states (given by images, i.e., regular meshes) and a transformer architecture trained for next-state prediction.

### Strengths
The paper is well written and quite accessible. To the best of my knowledge, the approach is novel, albeit being just a combination of a VQ-VAE and a transformer model. The quality of the research seems to be on a high level, as the approach appears valid and the experiments appear well designed and executed. In the experiments, the proposed approach performs excellently in terms of the relative L2 error (but some experimental details are not clear).

### Weaknesses
I have a few concerns that prevent me from assigning a higher score, and I would appreciate hearing the authors' thoughts on them:
- I am missing some references from the literature that may be relevant in this context. For example, how does Zebra compare to DeepONets (which are mesh free) and to MeshGraphNets [1] (which can use irregular meshes)? I assume that DeepONets and MeshGraphNets can be used to solve similar problems, even if the underlying approach is different. I would thus appreciate a numerical comparison, or at least a paragraph why such a comparison is not reasonable. This is important to put Zebra in context with the existing literature.
- In Section 3.3, it is mentioned that the transformer has a causal structure. This is not clear a priori, as the attention mechanism can in general be acausal (if I understood correctly). I would appreciate a few clarifying statements here. How was this causal structure enforced?
- In the experiments, some aspects are not fully clear. 
  - For example, in Sec. 4.2, does "the same underlying dynamics as the target" refer to the same parameter set $\mu$, or to something different? In the same section, does "Predictions are generated using a single sample" refer to the fact that, the future trajectory that has to be predicted has length 1? Or does it mean something else (and how would then multiple samples be used in the generative model)? In the same section, the results from Fig. 2 are not very strong as they do not exhibit a clear trend, suggesting that these figures can be moved to the appendix.
  - In Section 4.3, Fig. 3 could benefit from including the same analysis using CAPE and CODA, thus enabling a more fair comparison between these methods.
  - In both Sections 4.2 and 4.3, it may be a good idea to display ground truth trajectories together with predictions from all approaches. I briefly saw that the predictions of Zebra are included in the appendix, but I think one or two exemplary results (with those from the competing approaches) could be moved to the main text.
  - Section 4.4 is not entirely clear. On the one hand, it is not clear whether the quantified uncertainty is epistemic (resulting from too little training data) or aleatoric (influenced by inherent noise). The fact that it relies on $\tau$ suggests at least an aleatoric component. From that perspective, the usefulness of this is not clear. It is little surprising that for a large temperature $\tau$ the output is more random, hence there is a larger probability that the true trajectory is drawn by chance. Given that $\sigma_*$ can be made arbitrarily large via $\tau$, it is not clear to me if a high confidence level can be a meaningful objective. I suggest to clarify this, or to remove this section entirely.


### Minor:
- Line 068: "can can"
- Line 217: There is a double $\times$ in the exponent.
- What is the meaning of $sg[Z_q^t]$ in line 221? The function $sg$ was never introduced.
- Line 495: "traedoff"
- Figure 5: The axis labels and plot titles are not clear. What is the "rollout loss"?

### Questions
- How does the proposed approach compare to DeepONets (which are mesh free) and to MeshGraphNets [1] (which can use irregular meshes)?
- How was the causal structure enforced for the transformer mentioned in Sec. 3.3?
- In Sec. 4.2, does "the same underlying dynamics as the target" refer to the same parameter set $\mu$?
- Does "Predictions are generated using a single sample" refer to the fact that, the future trajectory that has to be predicted has length 1?
- Is the uncertainty quantified in Sec. 4.4 epistemic, aleatoric, or both?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper employs in-context learning to address a wide range of PDEs with varying equation parameters. The proposed method demonstrates competitive performance compared to baselines on the evaluated synthetic datasets.

### Strengths
1. This paper targets a important problem: generalization within a wide scope of PDEs.
2. This paper is clearly written and esay to understand.

### Weaknesses
1. **In-Context Learning:** The novelty of employing in-context learning appears limited. It seems that in-context learning is conceptually similar to “leveraging historical data to condition the neural network.” Tokenizing each frame individually could also enable handling arbitrary-sized context token inputs.
2. **Performance Concerns:** The performance results are not particularly compelling, and the dataset used appears relatively simple. Could you conduct additional experiments on some real-world datasets?
3. **Irregular data:** The paper focuses exclusively on grid-based data, which can be easily tokenized using VQ-VAE, as is common in latent diffusion models (LDM). What distinctions do you perceive between grid-based PDE data and images? Moreover, how would you extend your method to accommodate irregular data?
4. **Out-of-distribution testing:** The test environments are all within the distribution of the training environments, which is uncommon in real-world applications. Could you consider incorporating out-of-distribution test settings, particularly for extrapolation tasks? Since the test cases fall outside the training distribution, the zero-shot inference performance is suboptimal. How would you adapt the trained model to address these cases? Perhaps fine-tuning the VQ-VAE would be required initially, which may complicate adaptation compared to baseline models.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the problem of generalization of purely data-driven neural solvers to new PDE parameter values, without the need for gradient descent at adaptation time. Building on its successes in the language and vision communities, it proposed to use in-context pretraining (ICP) with a generative autoregressive transformer model to quickly adapt to new situations based on flexible contexts that can either be extra trajectories or historical states from the same underlying dynamics.

### Strengths
1) One of this paper's strongest point is its creative combinations of existing ideas. It successfully learns dynamics in latent space and illustrates a transversal application of vision and language techniques to physical systems. 
2) Although the related work section lacks in certain areas, the paper is overall well-presented, with extensive experimentation across a wide range of PDEs.
3) For Markovian systems such as the ones considered, zero-shot learning with temporal conditioning is just a special case of few-shots learning. This works picks up on that and suitably adapts CoDA [4] for zero shot learning. This is a great contribution, just as the adaption of the CLS vision transformers for parametric PDEs is.
4) The work has remarkable analysis of the uncertainty quantification capabilities built-in the Zebra framework. Specifically, the consideration of 3 different metrics helps understand how one can adjust the temperature $\tau$ to best suit our needs.

[4] Generalizing to New Physical Systems via Context-Informed Dynamics Model, ICML 2022

### Weaknesses
The paper has clear strenghts in its novel appreach, but lacts in other areas like related work and analysis. The main weaknesses I find are:
1) I fail to see how the third bullet point counts as a contribution (cf. line 90). Evaluation of one's proposed framework, however extensive, is to be expected.  
2) Although it is addressed elsewhere in the paper, Table 1 needs proper referencing of the methods Zebra is compared to. Also, it should be made clear that the method mentioned is the vanilla CoDA since you've shown it can easily be adapted for temporal conditionining.  
3) By "temporal" conditioning, it is clear that you mean that you are providing a history of previous states to the model. But you need better clarification of what "adaptive" conditioning means:
	- Wouldn't fine-tuning a subset of parameters count as adaptive conditioning ? These two appear to be contrasted in the section 2.2.
	- In appendix A.1, adaptive conditioning seems to be equated to meta-learning and multi-environment learning. The later two are quite different scenarios [3].
4) I remark limited analysis of the results in sections 4.2 and 4.3. Notably, in line 402, the authors hypothesize that leveraging more than a single sample per trajectory would ensure a more robust estimation. What would these samples be, if not the trajectories that are already provided ?
5) The main text and appendix literature on parametric PDE learning is very limited, especially concerning adaptive conditioning and uncertainty quantification. In recent years, several work have attempted to bring UQ into this field, e.g. CoNDP [1], NCF [2], etc.

[1] Stochastic Neural Simulator for Generalizing Dynamical Systems across Environments, IJCAI 2024. 

[2] Neural Context Flows for Meta-Learning of Dynamical Systems, ICLR 2024 Workshop on AI4Differential Equations In Science. 

[3] Bridging Multi-Task Learning and Meta-Learning: Towards Efficient Training and Effective Adaptation, ICML 2021. 


### Other minor issues
- Throughout the paper and especially in section 3.1, the authors mention the "need to convert physical observations into discrete representations". They also point out that their model is trained on numerical simulation data, which is already a form of discretization. This causes confusion and needs better clarity.
- At line 217, and extra "$\times$" is present.
- The stopgradient operator "sg" would benefit from some explanation in the main text.

### Questions
1) Concerning the experimentation, why do you find it necessary to "drastically increase the different number of environments compared to previous studies", e.g. by roughly 2 orders of magnitude more than in CoDA ? Also, given that so few environments are used for testing (120 or 12) compared to training, it is not surprising that all methods would perform well in-distribution. It is crucial, however, to know how well Zebra and the baselines perform when the testing environments are taken out-of-distribution (whenever possible based on the varying parameter).  

2) Related to Q1, given the need for a high-number of environments, on the Wave-b problem with varying boundary conditions, why weren't *periodic* boundary conditions considered to boost this environment count ? (This is all the more perplexing since the Wave-b dataset seems to be where the model struggles most - cf. Figure 3). 

3) How quick is Zebra given that it tokenizes and de-tokenizes states during autoregressive inference (cf. Figure 6) ? I don't believe this walltime metric should be ignored, especially if it led to slower adaptation than say CoDA's 250 gradient steps followed by fast numerical integration.  

4) From Table 4, why is Zebra so performant on **2D** zero-shot prediction tasks, and less so on 1D ? Is this somehow related to the structure of the codebook terms leaned in the VQ-VAE, where according to the equation in line 220, each spatial code corresponds to an entry, i.e. the codebook (and by proxy the model parameter count) grows exponentially with the dimensionality of the problem ? 
5) Why does the CAPE baseline diverge so often during evaluations ? Is there something that can be done to avoid that ?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses a critical challenge in solving parametric PDEs, where no prior knowledge of the underlying equations—such as PDE coefficients, boundary conditions, or forcing terms—can be utilized. To tackle this, the work makes two key contributions: 1) an auto-regressive framework based on VQ-VAE, and 2) an in-context learning paradigm designed to encode the implicit information of the underlying PDEs. The proposed methods are evaluated in two distinct settings: 1) zero-shot evaluation with temporal conditioning, where only the first few frames of data are used for inference, and 2) one-shot evaluation with context, where a new initial condition and a trajectory from the same environment are provided to guide inference.

### Strengths
* The paper tackles an interesting and important problem.

* This paper provides a well-organized presentation that lays out the shortcomings of existing approaches while clearly articulating the rationale behind the use of in-context learning. The figures effectively illustrate the framework of the method, enhancing clarity and aiding comprehension.

* Through extensive validation across a wide spectrum of PDEs, the method demonstrates remarkable generalization performance.

### Weaknesses
While the paper addresses an interesting problem, there are two primary concerns: 1) the proposed method lacks novelty compared to MPP [McCabe et al., 2023], which employs an autoregressive Transformer-based model and tackles a similar environment-unaware scenario with zero-shot evaluation via temporal conditioning, and 2) the empirical evaluation appears limited.

1. The main distinction between the proposed method and MPP lies in the use of the VQ-VAE framework and in-context learning. However, the rationale behind employing VQ-VAE is not clearly articulated. Since MPP’s architecture can also be trained in an autoregressive manner, what is the unique advantage of your proposed architecture for this task?

2. Although MPP focuses on zero-shot evaluation with temporal conditioning, extending it to the in-context learning setting is straightforward—by incorporating context examples into the input sequence. This reduces the novelty of your proposed approach. I suggest a direct comparison between Zebra and an MPP model trained with in-context learning, evaluating both context adaptation and zero-shot settings to highlight any distinct advantages.

3. While the in-context learning paradigm offers a method for addressing environment-unaware parametric PDEs, its effectiveness in encoding the underlying PDE information appears limited. The proposed Zebra shows only marginal improvement with additional context examples. For instance, Zebra’s performance in Vorticity 2D with a single context example (0.119) is worse than in the zero-shot scenario (0.0874). Moreover, as depicted in Figure 2, increasing the number of context examples does not consistently yield better results, with only modest gains observed (e.g., 1.14e-1 vs. 1.02e-1 in the Burger’s equation). Based on these findings, the introduction of in-context learning seems less impactful for solving parametric PDEs than it is for tasks in large language models (LLMs), offering no significant new insights for this problem domain. Could you elaborate on the possible reasons for the limited effectiveness of in-context learning in this domain, and do you have any suggestions for enhancing its impact?

4. For context adaptation settings, it would be beneficial to experiment with a larger number of context examples for both Zebra and the baselines.

5. In the zero-shot setting, consider using more frames during inference for both Zebra and the baselines.

6. Lastly, I recommend testing on more complex datasets, such as the one used in MPP, which involves a collection of four 2D PDEs (including incompressible and compressible Navier-Stokes equations, the shallow-water equation, and 2D diffusion-reaction equations) for pretraining.

7. The concept of in-context learning has been previously explored in the context of solving PDEs. Could you provide a specific comparison between Zebra and the approach in [Yang et al., 2023], highlighting key differences in methodology and applicability to different types of PDEs?

### Questions
See weaknesses

### Soundness
2

### Presentation
3

### Contribution
2

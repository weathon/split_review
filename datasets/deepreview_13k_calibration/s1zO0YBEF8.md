# Dynamics of Concept Learning and Compositional Generalization

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6

## Abstract
Prior work has shown that text-conditioned diffusion models can learn to identify and manipulate primitive concepts underlying a compositional data-generating process, enabling generalization to entirely novel, out-of-distribution compositions. 
Beyond performance evaluations, these studies develop a rich empirical phenomenology of learning dynamics, showing that models generalize sequentially, respecting the compositional hierarchy of the data-generating process. 
Moreover, concept-centric structures within the data significantly influence a model's speed of learning the ability to manipulate a concept.
In this paper, we aim to better characterize these empirical results from a theoretical standpoint.
Specifically, we propose an abstraction of prior work's compositional generalization problem by introducing a structured identity mapping (SIM) task, where a model is trained to learn the identity mapping on a Gaussian mixture with structurally organized centroids. 
We mathematically analyze the learning dynamics of neural networks trained on this SIM task and show that, despite its simplicity, SIM's learning dynamics capture and help explain key empirical observations on compositional generalization with diffusion models identified in prior work.
Our theory also offers several new insights---e.g., we find a novel mechanism for non-monotonic learning dynamics of test loss in early phases of training.
We validate our new predictions by training a text-conditioned diffusion model, bridging our simplified framework and complex generative models.
Overall, this work establishes the SIM task as a meaningful theoretical abstraction of concept learning dynamics in modern generative models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper sets out to explain previously reported characteristics of the learning dynamics of text-conditioned diffusion models with respect to  their ability to compose concepts to generalize to unseen combinations. Specifically, the paper aims to study why models learn concepts in a specific order and how the structure of the data influence a model's learning speed. To this end, the authors propose a simple reconstruction task (which they term structured identity mapping, SIM) in which an MLP should reconstruct its inputs drawn from a mixture of Gausssians. The authors argue that this task allows them to study and explain the key empirical observations on compositionally generalizing diffusion models and lead to the novel characterization of a non-monotonic learning dynamic.

### Strengths
This work studies a relevant problem: The learning dynamics of compositional generalization in diffusion models are important to understand how models can learn in a sample-efficient manner, how generalization can be achieved, or how training data should be curated, to name a few ways insights could be impactful.

The paper is easy to follow for the most parts and builds on a prior line of work in this area.

The non-monotonic training dynamics of a symmetric two-layer linear model are well explained by the theory and offer a novel (as far as I can tell) characterization of the training behavior of basic models. The theoretical training dynamics outlined in §4 and especially §4.2 and Fig. 5 model the empirical observations from §3 and Fig. 2 well.

### Weaknesses
In summary, I find the paper misses the mark, as the SIM task is, as far as I understand, a poor setting to study compositional generalization, and the insights on this simple task translate poorly to the training of a diffusion model, even for the simple toy setting that is used (which itself is approximating the compositional generalization of text-conditioned diffusion models that this paper aims to study). I will elucidate the issues I see with the setting and results below.

As it stands, I cannot recommend acceptance of this work; however, I could see how the results on the learning dynamics of symmetric linear models from §4 might be interesting in their own right, without considering any (as I understand, faulty) connection to compositional generalization. Maybe a reconsideration of the scope of the paper and a reframing of the results without overclaiming meaningful insights regarding the training dynamics of text-conditioned diffusion models could be an interseting contribution on its own.

# The SIM Setting
As far as I understand, previous works took the "concept space" as an abstracted view of the training and test data in order to study training trajectories of diffusion models. In the SIM task, this concept space is instead interpreted directly as the input and output space of a model. While I can see that this choice is motivated by the intuition in LL89, "a good generator essentially performs as an identity mapping in the concept space", this simplification of the setting is not explicitly mentioned, e.g., in the introduction, and the limitations this simplification imposes on the applicability and transferability of the results are not discussed.

Further, the training distribution in the SIM task is a mixture of Gaussians. In general, I find that this setup is not explained very clearly, see minor issues below. The central issue I see is that this setup entirely misses the point of (compositional) generalization. First, by introducing the training clusters as Gaussians, any point in $\mathbb R^d$ has probability $> 0$. So it is simply not true that any "[test] point is outside of the training distribution—not just the training data, necessitating out-of-distribution generalization." (LL173). Second, since test loss is only tracked on an individual point, not a test distribution, the experiments cannot even consider distribution shifts. Overall, describing this setting as requiring "generalization" to an "OOD test point" is misleading. The use of Gaussians, even with small variance, ensures that the test point, while potentially low in density, is still within the support of the training distribution, fundamentally undermining the claim of out-of-distribution generalization. The experiments do not explore the behavior of the model when the test point is truly outside the support of the training data, which is a critical aspect of compositional generalization.

If we understand that in this setting, any test point has non-zero probablity in the training set, the conclusions from §3 are mostly unsurprising. Consider the probability density of a given point in the grids in Fig. 2 belonging to the training set (in fact, I encourage the authors to include this information in the figure). I expect that for Fig. 2a, we will see that the trajectories are skewed towards higher-density regions, which roughly speaking can be interpreted as the model reducing the risk of a certain output. Similarly, we can understand the takeaway from Fig. 2b, the "terminal slow down" differing for different values of $\boldsymbol \sigma$ as an effect of the probability density. For $\boldsymbol \sigma = (2, 0.05)$, the overall density at point $(1, 2)$ is much higher than for $\boldsymbol \sigma = (0.05, 0.05)$, making it much less likely that this point (or points close to it) are sampled, so that the model takes much longer to learn it. The observed learning dynamics are therefore likely a consequence of the varying probability densities of the Gaussian mixture components, rather than a genuine reflection of compositional generalization.

While the "transient memorization" is an intersting behavior of even simple models, and the author's explanation of this phenomenon seems interesting, I find it hard to justify translating any insights from this setting to a compositional generalization regime.

# Transferring Results to Diffusion Models
§5 is very bare-bones, to the point that it is unclear how well the observations from the SIM setting actually translate here. E.g., there doesn't seem to be as much of a "terminal slow down" in Fig. 6 as was shown in Fig. 2a/b. The "transient memorization" also seems much less pronounced. The connection between the SIM task and the diffusion model experiments is weak, and the paper does not provide sufficient evidence to support the claim that the observed phenomena in the SIM setting are relevant to the training dynamics of diffusion models. The lack of a clear explanation of how the SIM task captures the complexities of diffusion model training further weakens the paper's claims.

Additionally, it is unclear _why_ results form the SIM setting should translate here, as in this case the test point is truly out of distribution, and, if I understand the training setting correctly, the trianing set only contains discrete values for each factor.

### Questions
# Questions
- LL86: "The model output is then passed through a classifier which produces a vector indicating how accurately the corresponding concepts are generated (e.g. a generated image of big blue triangle might be classified as (0.8, 0.1, 0.9)). In this way, the process of generation becomes a vector mapping, and a good generator essentially performs as an identity mapping in the concept space." In this setup, the vector mapping is $c \circ g$, comprising the generator $g$ _and_ classifier $c$. While it is clear that a good generator should be the identity, the role of the classifier also has to be analyzed. Can we be sure a priori, that $c$ is an identity mapping?
- How is training done? Is a fixed number of points sampled in the beginning to be used as a training set, or are points instead drawn for each batch?
- LL193: Why is $\mu_k$ equated with signal strength? Intuitively, instead of the absolute value of $\mu_k$, the distance between clusters should be more meaningful, which might be high for an individual cluster even if $\mu_k$ is low.
    - it is also not clear why this should matter to the model. The model could simply normalize each input dimension such that inputs are always balanced, e.g., in the task of Fig. 2b
- App. B: This observation mainly seems to imply that test loss _increases with the distance from the training set_, which, again does not say anything about OOD generalization or compositional generalization, and instead is a clear effect of the increasing probability density of the training set.
    - Also, why is the loss truncated instead of normalized?

# Minor Suggestions
- Fig. 1 and LL73 show that the data is clustered around nodes of the hypercube, yet LL150 and LL160 explain that each cluster has a different $\mu_p$ (distance from the origin). How do these statements fit together?
- L163 “There is also optionally a cluster centered at 0.” Is this in addition to the $s$ clusters, or is this just specifying that $\mu_p$ might be 0?
- LL170: "We evaluate the model at a Gaussian cluster centered at the point that combines the cluster means of all training clusters." What does this mean? Say the test cluster is $\boldsymbol x_k^\text{test} \sim \mathcal N(\boldsymbol \mu_\text{test}, \boldsymbol \sigma_\text{test}^2)$, does this just mean that $\boldsymbol \mu_\text{test}$ is the mean of all $\mu_p \boldsymbol 1_p$? 
- §3.1 and Fig. 2: What are the markers at each optimization timepoint? The model output for the given input $\boldsymbol x = \boldsymbol \mu$?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates the dynamics of neural networks in achieving compositional generalization. The authors propose a Structured Identity Mapping (SIM) task, where models are trained on a Gaussian mixture dataset organized around concept-centric clusters. They find that concept strength and diversity strongly influence the speed of convergence and the ability to generalize to compositional out-of-distribution (OOD) test points. They also observe a phenomenon called "transient memorization," where models initially memorize the training distribution but eventually reorient towards OOD generalization with extended training. Theoretical analyses on simple linear models substantiate these findings, highlighting the role of signal strength and diversity in learning order and the occurrence of non-monotonic loss behavior. Finally, the authors validate these findings by training diffusion models, observing similar patterns in generalization dynamics.

### Strengths
1. The paper is clearly written, with a logical flow that makes each insight and conclusion easy to follow.
2. The simplicity of the problem setup enhances the clarity and robustness of both the empirical observations and the theoretical contributions.
3. The diffusion model results are compelling, mirroring the behavior observed in simpler settings and offering explanations for phenomena noted in prior work.

### Weaknesses
The paper effectively accomplishes its aims, though a few points could be noted for improvement:
1. **Limited Theoretical Scope**: While the theoretical framework successfully supports the empirical observations in more complex models, it is based on simple linear models.  I acknowledge the difficulty in analyzing more complex neural networks theoretically. Nonetheless, for future work, extending the analysis to objects like kernel methods, particularly the Neural Tangent Kernel (NTK) [1], could provide a deeper understanding as NTK has been shown to capture certain behaviors of neural networks during training [2]. The current analysis, while insightful for linear models, does not fully address the non-linear dynamics inherent in neural networks, particularly regarding the feature learning process and the evolution of the loss landscape. The theoretical analysis also does not account for the effects of different activation functions, which can significantly impact the learning dynamics and generalization capabilities of neural networks.
2. **Contextualization of Findings**: Some insights, such as the speed and order of generalization, have been observed in different forms in previous OOD works [3, 4, 5]. Further contextualizing the findings within these works could enhance the paper’s relevance and depth. Specifically, the paper could benefit from a more detailed comparison of its findings with the specific mechanisms proposed in these prior works. For example, the paper could discuss how its concept strength and diversity relate to the notion of 'spurious correlations' or 'invariant features' discussed in these works. A more thorough comparison would help to position the current work within the existing literature and highlight its unique contributions.

### Questions
The paper effectively accomplishes its aims, though a few points could be noted for improvement:
1. **Limited Theoretical Scope**: While the theoretical framework successfully supports the empirical observations in more complex models, it is based on simple linear models.  I acknowledge the difficulty in analyzing more complex neural networks theoretically. Nonetheless, for future work, extending the analysis to objects like kernel methods, particularly the Neural Tangent Kernel (NTK) [1], could provide a deeper understanding as NTK has been shown to capture certain behaviors of neural networks during training [2]. 
2. **Contextualization of Findings**: Some insights, such as the speed and order of generalization, have been observed in different forms in previous OOD works [3, 4, 5]. Further contextualizing the findings within these works could enhance the paper’s relevance and depth.

[1] [Jacot 2018] https://arxiv.org/abs/1806.07572

[2] [Lee 2020] https://arxiv.org/abs/2007.15801

[3] [Nagarajan 2020] https://arxiv.org/abs/2010.15775v3

[4] [Arjovsky 2019] https://arxiv.org/abs/1907.02893

[5] [Rosenfeld 2020] https://arxiv.org/abs/2010.05761

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces the structured identity mapping (SIM) task, where a network is trained to learn the identity mapping from inputs which are sampled from largely disjoint Gaussian distributions, and evaluated on a test point defined as the average of their means. By analyzing learning dynamics of one-layer and symmetric two-layer linear networks on this task, the paper shows that several existing empirical observations can be modeled - higher SNR features are learnt earlier and faster, an epoch-wise double-descent phenomenon (termed Transient Memorization) occurs on the test point, and that learning slows down exponentially with time.

### Strengths
- Paper formalizes a proxy task (SIM) to model the learning dynamics of compositional generalization, and shows that real-world text-conditioned diffusion models exhibit similar behavior on a specific task. 
- Theoretical setup is clearly explained and theoretical conclusions are also well-elaborated. Limitations of theoretical results on the one-layer and symmetric two-layer linear models are also clearly discussed.

### Weaknesses
 - It is not at all apparent that $\hat{x}$ is "outside of the training distribution", since $p(x_k^{(p)} = \hat{x}) > 0$ for training data $x_k^{(p)}$, despite what is claimed on L174. Why not choose sigma such that $\sigma_p \geq 0$ while keeping $\sigma_{q \neq p} = 0$? Furthermore components of $\sigma$ seems to be as large as $2$ in Fig 1., with $\mu$ ranging from $0 - 2$. In such cases, the converse seems to hold -- that $x_k^{(p)}$ is very much in-distribution of the training data.
- As a result, the introduced terminology "Transient Memorization" does not seem to be different from epoch-wise double descent. The paper stresses that the main difference is OOD vs in-distribution test loss (L263-265), but (a) as mentioned above the test sample considered are in fact in-distribution, and (b) even for double descent, it is actually essential for testing samples to differ significantly from the training ones as pointed out by [1].
-  The proposed SIM task is claimed to be a "further abstraction of the 'concept space' previously explored" (L531), however it appears instead to be an (over)-simplification of previous investigations. The motivation of the SIM model and how it relates with more general real-world settings are also unclear (for instance, why the proposed auto-encoding loss?). The choice of using an auto-encoding loss, rather than a direct regression to the identity, is not well-motivated and seems to complicate the analysis without clear benefits. This raises questions about the relevance of the SIM task to real-world scenarios.
- The paper's main empirical results section (Page 10) appear very underdeveloped and all important experiment details are left to the Appendix. Figure 6 is also not clearly explained, and different plots are distinguished based on "difference of class mean pixel values". Without reading App G, it is almost impossible to interpret what these results and experiments are doing. $\Delta$ Color is not defined in App G either. The lack of clarity in the main text regarding experimental setup and results makes it difficult to assess the validity and significance of the findings. The description of Figure 6 is particularly vague, hindering the reader's ability to understand the experimental design and interpret the results.
- Paper concludes from Fig. 2 that "deceleration is not determined by ... the loss value ... but more depends on the data and training time" (L215). This is not self-evident, since (1) the training loss is not even plotted in Fig 2, and (2) regions with denser arrows are clearly also regions of lower test loss. The conclusion drawn from Figure 2 is not adequately supported by the presented data. The absence of training loss plots makes it difficult to assess the relationship between training loss and the observed deceleration. Furthermore, the visual correlation between arrow density and test loss suggests a potential link that contradicts the paper's claim.
- The paper also claims that "there is a timescale determined by the training data such that if the model does not achieve OOD generalization within that period, significantly more computation will be required for the model to achieve it." (L238-240), which purportedly can be observed in Fig 2(b). However, the figure simply shows that configurations with lower $\sigma$ values take longer to correctly predict the test point. This conclusion seems self-fulfilling, since when $\sigma$ is larger, the density of training samples around $\hat{x}$ will be much higher. The interpretation of Figure 2(b) seems to be an overreach. The observation that lower sigma values require longer training times is not surprising, given that a smaller sigma implies a sparser sampling around the test point. The claim about a specific timescale for OOD generalization appears to be a misinterpretation of the observed behavior.
- Minor: L534-L535 incomplete sentence - "We make a comprehensive."
- The work's primary area is stated as interpretability / explainability in AI, but the contributions to these areas are unclear. The bulk of the theoretical contributions seem to be instead exploring learning dynamics for one-layer/deep-linear models, which I have insufficient experience to evaluate with regards to recent literature.

### Questions
See weaknesses

### Soundness
3

### Presentation
3

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
This paper presents a theoretical framework for understanding the dynamics of compositional generalization in neural networks. Building on prior work that examines how models generalize by manipulating underlying primitive concepts, the authors introduce a Structured Identity Mapping (SIM) task, where a model learns the identity mapping on a Gaussian mixture with structured centroids. Through analysis of this SIM task, the paper reveals mechanisms behind non-monotonic learning dynamics, which is validated through experiments on text-conditioned diffusion models.

### Strengths
1. The paper’s explanation of learning dynamics, including the multi-stage Jacobian evolution and its impact on concept learning order and speed, sheds light on underlying model behaviors. I think the interesting point is the high similarity between the diffusion experiment and the theoretical model behavior, even though the correlation between the two is not clearly demonstrated.

2. Experiments on SIM and diffusion models are well-designed, with relevant results that support the theoretical predictions, enhancing the practical relevance of the results.

### Weaknesses
1. The theoretical model studied in this paper differs significantly from practical diffusion models. Although the authors attempt to demonstrate a relationship between the theoretical analysis and practical model behavior through empirical results, this connection remains unclear, making it challenging to confirm whether the behavior observed in diffusion models is directly related to the theoretical insights presented. While I acknowledge the value of the analysis for single-layer and two-layer linear networks, it would be beneficial if the authors conducted further analysis on simplified diffusion settings to bridge the gap between theory and practice more effectively.

2. In reference [1], the authors also discuss learning primitives in compositional tasks. Additional discussion on this work could be beneficial. Based on this, I have the following question: In [1], small initialization is an important factor for the model to learn primitives. In this paper’s theoretical part, small initialization is also assumed, but in practical diffusion models, is small initialization a crucial factor for learning primitives, or is it merely a theoretical necessity?

3. Could Figure 5 display the training data’s trajectory evolution? I am curious whether there is a similarity between the training and test trajectories in the early stages of training.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

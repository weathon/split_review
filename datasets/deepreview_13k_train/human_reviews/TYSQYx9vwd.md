# Uncertainty Modeling in Graph Neural Networks via Stochastic Differential Equations

- Decision: Accept
- Scores: 10, 6, 6

## Abstract
We address the problem of learning uncertainty-aware representations for graph-structured data. While Graph Neural Ordinary Differential Equations (GNODE) are effective in learning node representations, they fail to quantify uncertainty. To address this, we introduce Latent Graph Neural Stochastic Differential Equations (LGNSDE), which enhance GNODE by embedding randomness through Brownian motion to quantify uncertainty. We provide theoretical guarantees for LGNSDE and empirically show better performance in uncertainty quantification.

## Human Reviews

## Human Reviewer 1

### Rating
10

### Rating Number
10

### Confidence
3

### Summary
This paper generalizes GNODE to its stochastic counterpart, using SDEs to derive uncertainty-aware representations for graph-structured data. Theoretical and experimental characterization of the framework, named LGNSDE, showed its robustness and uncertainty quantification capability.

### Strengths
- The idea is sound and innovative.
- The mathematical framework is simply elegant.
- The robustness of this model is clearly demonstrated by theoretical and experimental results.
- This framework can be of high utility to the community.

### Weaknesses
 - I would imagine the result is heavily dependent upon the integration methods. See the extensive study conducted in GRAND: Graph Neural Diffusion, Chamberlain et al. 2021.
- The accuracy of this model is not as performant as many cheaper variants.
- I would love to see its speed and memory benchmark, as I imagine it to be quite expensive.

### Questions
- Have you tried varying the backbones of the GNN and is there any performance change? I think rewiring the graph structure might have a huge impact.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a new GNN architecture version based on stochastic differential equations to improve uncertainty estimation.

### Strengths
1. The paper demonstrates good empirical performance.
2. The authors evaluate uncertainty estimation through OOD detection, noise perturbation, and active learning.

### Weaknesses
1. The paper lacks comparisons with SOTA works. Some strong methods, such as GPN (Stadler et al., 2021) and GNSD (Lin et al., 2024), are mentioned but not evaluated, despite their better empirical performance compared to the baselines used. Additionally, other high-performing methods that utilize energy variants are not tested.
2. The method shows significant similarities to Lin et al. (2024), who also propose an SDE-based GNN. While the authors acknowledge the difference with one sentence in the related work section, I believe the similarities and differences should be further discussed in detail, such as by comparing the frameworks mathematically and conducting a specific study (even on a synthetic dataset) to highlight the unique merits of their approach. But the method is not compared against at all.
3. Can you elaborate on how the 'framework effectively quantifies uncertainty' based on Proposition 1? It is not immediately clear to me how this bounded output variance translates to effectively quantified uncertainty.

### Questions
1. Can you elaborate on how the 'framework effectively quantifies uncertainty' based on Proposition 1? It is not immediately clear to me how this bounded output variance translates to effectively quantified uncertainty.


While the topic and approach are interesting and the method appears potentially promising, I have concerns about the evaluation and the presentation, particularly the lack of differentiation from existing methods. If additional data and clarifications are provided, I would be willing to reconsider my rating.


--- 
Post rebuttal: experimental evaluation seems good now.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a new model (LGNSDE) for learning on graphs with uncertainty quantification. It leverages an Ornstein-Uhlenbeck prior and a posterior with drift parameterized by a GCN model that is trained through variational inference. This SDE approach is latent as it operates on node feature embeddings. Two novel theoretical results are shown, providing a bound on model output variance and a bound on solutions under node feature perturbations. Six graph models are then compared in various experiments on five standard graph datasets, including studies of OOD detection, test noise, and active learning. The proposed model performs favorably across these experiments.

### Strengths
- The LGNSDE model description is clear, concise, and intuitive.
- The two theoretical results are important and original, providing a good deal of strength to the proposed methodology.
- The experiments clearly show this model has significant potential in delivering upon the promise of uncertainty quantification for graph-structured learning problems.

### Weaknesses
 - Some of the cited works (particularly Calvo-Ordoñez et al., 2024, and Xu et al., 2022) leverage SDEs in a very similar way, but do not consider the problem of learning on graphs. While the application to graphs is creative, the model definition is somewhat limited in novelty.
- The choice of a constant drift and diffusion function in the OU prior is not sufficiently explored. It would be great if there was mention of why this is a reasonable restriction if this is indeed the case. Specifically, the implications of this choice on the expressiveness of the prior and its impact on the posterior distribution are not discussed. The lack of exploration into alternative, potentially more flexible, drift and diffusion functions is a notable gap.
- The experimental section would benefit from increased clarity and specificity, especially in regard to the structure and setup of experiments. Choices such as number of epochs and early stopping criteria, if any, are not explicitly stated. Furthermore, the specific data splits used for training, validation, and testing in each experiment are not clearly defined, making it difficult to assess the robustness of the results.
- It is stated in Section 5 that hyperparameters that achieved the highest validation accuracy were chosen. It is unclear to me which validation accuracy is used here, and knowing the exact grid search setup would be ideal for improved reproducibility. The lack of detail regarding the hyperparameter search space and the specific metric used for validation makes it difficult to understand the model selection process.
- Table 7 shows that uniform hyperparameters were chosen across all models; if the hyperparameter choice was performed via search for each model independently, the comparison results might be more fair. The potential for suboptimal performance due to uniform hyperparameter selection across different models is a significant concern.
- The most impactful perceived weakness of this paper was the lack of experimental comparison with the models referenced as related works, particularly those referenced in Section 6. The other methods used in comparison do not follow a stochastic approach, limiting the ability for a fair comparison. I would be extremely interested to see a comparative study against the referenced GNSD (Lin et al., 2024) method, for example. The absence of comparisons with relevant stochastic methods hinders the assessment of the proposed model's advantages.
- For OOD detection, comparison against methods built specifically for this task on graphs, like GNNSafe (Wu et al., 2023) would be enlightening. The lack of comparison with specialized OOD detection methods limits the evaluation of the proposed model's performance in this specific task.
- One of the theoretical claims was a resistance to small perturbations in graph structure. This might lead to a compelling experiment, but this claim is not tested. The absence of experimental validation for the theoretical claim regarding robustness to graph structure perturbations is a significant omission.

There are two small writing nitpicks:
- In the first line of the introduction, "Before the widespread of neural networks" is missing a word. Perhaps use "widespread success" or similar?
- In Section 6, "Hence, constructing a different method." does not read as a complete sentence, and should probably be folded into the line before it.

### Questions
- Is it possible to allow a non-constant drift function in the prior OU process? Would a similar method or extension allow this?
- What is the effect upon training and convergence for different choices of hyperparameters, and in particular, for different choices of constant drift and diffusion functions? Has an ablation study been performed for this proposed model?
- How does the walltime of learning with an LGNSDE compare to walltime for the other tested methods?
- Are there any interesting limitations on the practicality of this method, and in your experience, what can allow for learning the best results?

### Soundness
2

### Presentation
3

### Contribution
2

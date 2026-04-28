# Graph Neural Networks for Interferometer Simulations

- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 6, 3, 3

## Abstract
In recent years, graph neural networks (GNNs) have shown tremendous promise in solving  problems in high energy physics, materials science, and fluid dynamics. In this work, we introduce a new application for GNNs in the physical sciences: instrumentation design. As a case study, we apply GNNs to simulate models of the Laser Interferometer Gravitational-wave Observatory (LIGO), and show that they are capable of accurately capturing the complex optical physics at play, while achieving runtimes 815 times faster than state of the art simulation packages. We discuss the unique challenges this problem provides for machine learning models. In addition, we provide a dataset of high-fidelity optical physics simulations for three interferometer topologies, which can be used as a benchmarking suite for future work in this direction.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors present a graph neural network purpose-constructed for interferometer simulations, which combines a graph attention network with the recently introduced Kolmogorov-Arnold networks. Deriving networking constraints from the physical symmetries belying the simulation approach to interferometer simulations, the two are combined to abide by the physical symmetries of the problem. The proposed model is evaluated on 4 successively more difficult interferometer topologies, and evaluated for its predictive capability as well as computational efficiency.

### Strengths
The paper is very well-written, and all network design decisions are motivated out of the demands by the physical problem which are introduced in the requisite detailed manner. Especially the description of the physical problem is very well-written and enables an easy understanding of the imposed demands.

### Weaknesses
The weaknesses of the paper can on a high level be summarized with lack of depth of the evaluation, a lack of embedding into the wider literature, and imprecision in a number of key claims.

**Lack of depth of Evaluation**
- Specifically table 1 seems to only capture a limited window of the design space. The evaluated models, as well as the dataset evaluations could be improved considerably with a limited amount of effort, such as on the architectural side evaluate "GAT + KAN", "GAT only", "KAN only", and "MLP". Each of these 4 would then be evaluated with the 3 dataset specifications "FP Only", "Mixed Dataset", and "Half ALIGO Only". In addition the current caption is imprecise in its description of what is happening in the present table.
- Equivariant layers for GNNs being readily available, it is unclear to the reviewer while the GAT + KAN hybrid is not contrasted to a pure GNN with Equivariant layers motivated out of the physical symmetries of the interferometry problem as a point of comparison, and a further point of comparison for the computational efficiency of the introduced architecture. The lack of comparison to equivariant GNNs is a significant oversight, as these architectures are explicitly designed to respect the symmetries inherent in physical systems, and would serve as a strong baseline for comparison. The authors should clarify why this approach was not considered, and provide a comparison to at least one such model.
- The exact details of the GNN architecture are not further specified before the results section, while it is specified that it used 15 GAT layers + deep KAN, but for the full reproducibility of the results it would be beneficial to provide a succinct table containing the details of the overall architecture plus the design specification of other models used in the evaluation. This should include the number of attention heads per GAT layer, the dimensionality of the hidden layers, the activation functions used, and the specific architecture of the KAN, including the number of layers, nodes per layer, and activation functions. Without these details, the results are difficult to reproduce and the evaluation is less rigorous.
- With regards to the evaluation of the computation efficiency, please see the imprecision in key claims below.

**Lack of Embedding into wider Literature**
- While the work on GNNs for fluid simulations is mentioned throughout the paper, the paper yet contradicts literature in claiming for these GNNs to not be applicable to the interferometry problem. Shock simulations, which exhibit the sharp jumps characteristic to interferometry are an integral part of fluid simulations, and works such as Poseidon, as well as the widely used PDE-Bench contain shock simulations, and are hence able to represent those sharp jumps. Setting the presented work in relation with GNNs for shock simulations, and potentially even testing one of the fluids-trained models on interferometry such as Poseidon by fine-tuning it on the introduced dataset would benefit the paper greatly. The authors should specifically address why models trained on shock simulations are not applicable, given the similarities in the sharp discontinuities present in both domains. A more thorough discussion of the limitations of existing fluid simulation models when applied to interferometry is needed.
- The training across multiple interferometer configurations bears close resemblance to the Multiple Physics Pretraining introduced in _Multiple Physics Pretraining for Physical Surrogate Models_ by McCabe et al., I would urge the authors to relate their work to the MPT approach, and if applicable in the author's eyes consider other recent Transformer or GNN architectures for PDEs trained across multiple problem settings such as the models trained on PDE-Arena, or PDE-Bench, as well as large models like the Universal Physical Transformer of Alkin et al., and the Poseidon model series by Herde et al. The latter is furthermore trained on shocks, and as such should be able to be fine-tuned for the interferometer simulation as it is natively trained to be able to handle the sharp jumps of interferometry (line 431). The authors should explicitly discuss the differences between their approach and the MPT approach, and justify why they did not explore pre-training on a larger dataset of interferometer configurations, or fine-tuning models pre-trained on related physical simulation tasks.

**Imprecision in key claims:**
- The authors claim an 815x speedup, while at the same time emphasizing the benefits of outputs with a lower fidelity. At the same time, the abstract leaves the impression that this speedup is realized at the same simulation fidelity. It is furthermore unclear to the reviewer if those fidelities are actually the same. Going from the results table, this does not seem to be the case. In addition the reviewer asks for further clarification if both are performed on the same platform. The GNN network does seem to be running on a GPU, but it remains unclear if the FINESSE model is also running on a GPU. The authors need to clarify the exact conditions under which the speedup is measured, including the hardware used for both the GNN and the baseline simulations. Furthermore, they should provide a more precise definition of what they mean by “fidelity” in this context, and how it relates to the accuracy of the simulation results.

### Questions
Line 258-260: Ablations of model design decisions, why don't the authors consider using their spare space to extend the paper with an in-depth ablation study? Going from the mentioned paragraph, you have done these ablations, and mention them, but have not synthesized the ablations into a dedicated ablation section, which could improve the paper.

What is the GNN 815x faster than, and how does the fidelity compare? A way to seek to quantify this relation would either be a discrete fidelity on the x-axis, with the y-axis representing the speedup, or the fidelity could also be a continuous axis, where one would use the Pearson correlation [1] between the full fidelity result of the FINESSE simulation, and the output of the GNN. Further depth could be added to this plot by performing the same calculations for a GAT-only architecture, a KAN-only architecture, and the MLP used in the main results section.

[1] https://mathworld.wolfram.com/StatisticalCorrelation.html

### Soundness
4

### Presentation
4

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
This paper applies GNN and KAN to simulate LIGO instrumentation models and shows that it can accurately capture the optical physics at play while achieving 815x faster than SOTA EM numerical simulation packages. It also provides a high-fidelity dataset of optical physics simulation for three interferometer topologies for benchmarking.

### Strengths
+ Shows the necessity of using GNN rather than MLP for feature extraction and generalization, as well as the benefit of KAN, as compared to MLP in more actually addressing spatial features such as the prediction of varying spatial intensity distribution. 
+ Results show significant speedups than numerical simulation

### Weaknesses
Authors should provide more details & clearer explanation about their datasets and the mapping from optics of EM field to a graph. I would highly recommend showing a figure to illustrate an example, including the node features and edge features.

About the dataset, can you provide more characteristics? e.g., how many data points, how many nodes, etc. in a table. Also, why the full ALIGO is not covered in the dataset, which seems to be the practical establishment for LIGO.

I would expect more concrete discussion on the advantages of using KAN than MLP for such a type of physics-information models. It's not clear if the MLP's poor performance is due to inherent limitations or simply suboptimal training. The 6-layer MLP may be under-parameterized compared to the 20-layer GAT, making a direct comparison difficult. The paper should also explore whether a deeper MLP could achieve comparable results to the GAT+KAN model, or at least provide a more thorough ablation study on MLP depth.

### Questions
What are the practical benefits of using this AI model in addition to reducing optical simulation time and what are their implications? Have you observed that the AI model can provide better manufacturing design parameters that are more robust?

Can you provide more insights on the rationale of designing such a 20-layer GAT + 6 layer MLP or 1 layer KAN kind of model? It seems to me the lack of ability to generalize for MLP is due to overfitting by using the 6-layer MLP.

### Soundness
3

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
3

### Summary
This paper applies graph neural networks (GNNs) to interferometer simulations, specifically modeling LIGO’s optical physics. The authors show that GNNs simulate electromagnetic field propagation accurately while running 815 times faster than traditional methods, which is supposed to enable efficient optimization of interferometer design. They also release a dataset of high-fidelity simulations for benchmarking future models in this domain.

### Strengths
* The paper introduces a new dataset that can be used to predict interferometer simulations. 
* A GNN model that includes a KAN layer is introduced for the new data.
* The model is empirically evaluated and shows some promising initial results.

### Weaknesses
 * Incomplete results: I would expect that the authors compare the results of both the GNN and MLP trained and tested on all possible combinations of datasets. However, Table 1 only contains a subset of these results. In particular, results for the MLP are only provided when trained on the mixed dataset. This makes it impossible to deduce a fair comparison from these results. Also, these partial numbers are only provided for power prediction, for intensity prediction only two numbers are mentioned in the text. Suggestion: Provide a full table showing results for both GNN and MLP models trained and tested on each individual dataset (Fabry-Perot, Half ALIGO, Coupled Cavity) as well as the mixed dataset. Additionally, quantitative results for the intensity prediction task can also be included in the table.
* The GNN is only compared to an MLP, which makes the analysis quite limited. Other methods should be tested, for example a KAN without the GNN. This would highlight the contribution that the GNN makes. As is, it is impossible to say whether the KAN alone might be the main contributor to better performance or not. Further, the GNN should also be tested with an MLP as a drop in replacement for the KAN to verify that it works better (as was partially done in the intensity prediction, but just for one setting). Suggestion: Include an ablation study that compares:
    * The full GNN+KAN model
    * A KAN-only model without the GNN component
    * A GNN with an MLP replacing the KAN 

This would help isolate the contributions of each component. Ideally, these comparisons would be done across all datasets and tasks (power and intensity prediction) for consistency.

* Essential information on the setup and parameter ranges that were used to generate the ground truth data are missing in the paper (for example the parameter ranges that were used and how these were sampled). Specifically, the base interferometer designs and the exact parameters that are varied during the random walk need to be clearly defined. This includes the distances between optical elements, their radii of curvature, and reflection coefficients. The sampling method (e.g., uniform, Gaussian) for these parameters should also be specified to ensure reproducibility.
* The GNN architecture and constructed graphs are very simple and no advanced methods were tested. More recent GNN variants like GraphTransformers or exploring edge feature incorporation methods would strengthen the paper in that regard. It is unclear how the graph transformer was implemented, specifically whether positional encodings were used. It also seems that only a single, potentially excessive, number of transformer layers (20) was tested.

### Questions
* This is a suggestion: Add an ablation study for the KAN and different GNN layers (not just GAT).
* Figure 3 is never referenced in the text 
* I’m not an expert in interferometer spectography, so I cannot quite judge the impact of this work. Is this something that could be deployed as is or are the datasets too simplistic? Could you maybe provide a more detailed discussion on the practical applicability of your current model and dataset? What are the limitations of the current approach and what additional steps would be needed to make the model deployable in real-world interferometer design scenarios?
* It is unclear for me whether the direct comparison of a GNN with Finesse in terms of runtimes is really adequate. Is Finesse also just computing the same values that the GNN is computing here?

Overall, the experimental evaluation, which is a crucial part of this paper, is too limited and needs to be reworked before this paper should be accepted. I’m happy to reconsider my rating once the full results are provided.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors present a GNNs based approach for accelerating simulations of optical interferometers. They demonstrate that their model can achieve significant speedups over traditional simulation methods while maintaining reasonable accuracy. However, the paper has several notable limitations.

### Strengths
1. The paper proposes a GNNs based method that can simulate electromagnetic (EM) field propagation in optical cavities at a fraction of the computational cost of traditional methods.
2. The authors provide a dataset on three interferometer topologies, which may offer potential future use in benchmarking for similar studies.

### Weaknesses
1. Insufficient Novelty in Model Design. The model primarily relies on standard GAT layers and KANs without substantial adjustments specific to interferometer physics. The use of Graph Attention Networks (GATs) and Kolmogorov-Arnold Networks (KANs) in this context, while not inherently flawed, lacks a clear justification beyond their general applicability. The paper does not explore how these architectures are specifically tailored to capture the underlying physics of electromagnetic wave propagation within interferometers. For instance, the GAT layers do not seem to incorporate any inductive biases related to the known symmetries or conservation laws governing EM fields. Similarly, the application of KANs, while a relatively recent approach, is not presented with a clear rationale for why they are superior to other function approximators in this particular domain, beyond a general claim of better performance.

2. Incomplete Comparisons with Existing Methods. The results reported are insufficient for an in-depth assessment. Without comparisons with other methods, the use of GNNs feels unjustified, and the work seems as an attempt to apply GNNs to a novel domain without fully validating its effectiveness. The paper lacks a rigorous comparison against established numerical methods for simulating optical interferometers, such as Finite Difference Time Domain (FDTD) or Finite Element Method (FEM). The absence of such comparisons makes it difficult to assess the true computational advantage of the proposed GNN approach. Furthermore, the paper does not include comparisons with simpler machine learning models, such as standard Multi-Layer Perceptrons (MLPs) or other regression techniques, to demonstrate the necessity of using a graph-based approach.

3. Poor clarity and presentation. The content and figures do not meet high standards and lack clarity. For instance, while the authors emphasize the importance of instrumentation design in the abstract and introduction, the paper has minimal discussion on actual instrumentation design. The paper's figures are often difficult to interpret, lacking clear labels, scales, and explanations of the data presented. The connection between the proposed GNN model and the actual physical parameters of the interferometer is not clearly established, making it hard to understand how the model's predictions relate to real-world instrument design. The lack of clear descriptions of the specific interferometer configurations used in the experiments further hinders the reproducibility and understanding of the results.

### Questions
Please see Weaknesses.

### Soundness
2

### Presentation
1

### Contribution
1

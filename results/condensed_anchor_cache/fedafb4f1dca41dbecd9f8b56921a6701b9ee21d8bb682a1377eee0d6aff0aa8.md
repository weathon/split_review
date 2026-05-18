- Decision: Accept
- Scores: 6, 8, 8

## Merged Review

### Summary
This paper proposes a graph-based framework for processing the parameters of neural networks by converting any architecture into a compact “neural graph” (related to the computation graph) and applying GNNs or graph transformers. The approach handles different nonlinearities, residual connections, and network sizes, and does not require bespoke equivariant layers for each architecture. Extensive experiments on classifying implicit neural representations (INRs), predicting CNN generalization, and learning to optimize show significant improvements over prior methods (Navon et al., 2023; Zhou et al., 2023a). Ablations of probe features are included in the supplementary material.

### Strengths
1. **Novelty and flexibility** – The method handles heterogeneous architectures (different nonlinearities, residual connections, widths, depths) with a single model, avoiding the need for architecture-specific equivariant designs. It also supports different base models (GNN and Transformer).
2. **Clear presentation** – The paper is well written and easy to follow, with adequate detail and full source code provided.
3. **Thorough empirical evaluation** – Strong, consistent improvements over baselines across three diverse tasks: INR classification (2D images) and style editing, CNN performance prediction, and learned optimization. Error bars are included for all experiments.
4. **Interesting learned optimization experiments** – Reviewer 1 specifically highlights these as particularly compelling.

### Weaknesses
1. **Confounding role of probe features** (Reviewer 1, more critical) – Probes are derived from the input data itself (e.g., giving representations from different layers). With enough probes, the model effectively sees the original input, making it unclear how much of the performance gain comes from the graph-based method versus the privileged information. This complicates direct comparison with methods that operate solely on network parameters. Reviewer 2 and 3 also note the need for detailed ablation of probes (see point 4).  
   - *Requested analysis*: Impact of the number and nature of probe features on overall performance; report how many probes are used in each experiment.
2. **Missing theoretical justification** (Reviewers 1 and 2) – Claims of invariance/equivariance to permutation symmetries are stated without proofs. Prior work provides formal expressivity and group-equivariance results, but this work does not.  
   - *Questions that double as criticisms*: How can the statement that “neural graphs ensure invariance to neuron symmetries” be proved? Can the claimed one-to-one correspondence between natural symmetries in neural graphs and neuron permutation symmetries be formalized (Sec 2.1)?
3. **Limited coverage of layer types and lack of systematic recipe** (Reviewers 2 and 3) – The CNN graph construction requires specifying a maximum kernel size, and it is unclear how to extend the approach to other parameter-sharing layers (e.g., attention layers whose sequence length varies widely) or to normalization layers. Only MLP and convolutional layers were tested experimentally, even though the framework proposes handling residual connections and normalizations. A clear, general recipe for diverse layer types is missing.  
4. **Missing ablation of design components** (Reviewer 2, echoed by Reviewer 1’s probe concern) – No ablation disentangling the contributions of probe features, nonlinearity identification, positional encoding, and other design choices. Without this, it is difficult to judge the necessity of each component.  
5. **Unexplained discrepancy in MNIST dilation results** (Reviewer 1) – The reported MNIST dilation error (~0.02) differs substantially from Zhou et al. (~0.07). The reason for this gap is not addressed.  
6. **No discussion of scalability or expressive power relative to baselines** (Reviewer 3) – For a fixed architectural budget, can the proposed method handle neural networks of the same size as baselines (Navon et al., Zhou et al.) for a given memory limit, or can it scale to larger networks? Is the expressive power comparable?  
7. **Baseline generalization gap** (Reviewer 2) – Baselines achieve equal training loss but fail to generalize as well (Sec 4.1). The authors did not explore regularization or other modifications for baselines; it is unclear whether the probe features or other modifications provide the generalization benefit.  
8. **Minor presentation issues** (Reviewer 2) – The claim of “outperforming state-of-the-art approaches by a large margin” should be quantified. In Sec 2.3, clarify whether nonlinearities are added via concatenation and what happens when no activation is present.
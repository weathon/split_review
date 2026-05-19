- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 8, 5, 5
Now I will produce the final consolidated review.

## Summary

This paper introduces hypergraph dynamic systems (HDS), bridging hypergraph representation learning with continuous ODE dynamics. The authors propose HDS<sup>ode</sup>, a neural implementation that separates the ODE into alternating control steps (learnable MLP per vertex/hyperedge) and diffusion steps (parameter-free propagation via a specially designed diffusion matrix). The method is evaluated on 9 hypergraph benchmarks across transductive and production settings, achieving state-of-the-art results and demonstrating steady performance when scaled to 16+ layers — directly addressing the oversmoothing problem that limits existing HGNNs to 2 layers.

## Strengths

1. **Empirical superiority across all transductive benchmarks**: Table 1 shows HDS<sup>ode</sup> achieves the best test accuracy on all 7 datasets (average rank 1.0), outperforming 8 baselines including hypergraph-specific methods HGNN and HGNN<sup>+</sup>. The gap is consistent across datasets with varying sizes and structures.

2. **Stable performance with increased depth**: Figure 1 demonstrates that HDS<sup>ode</sup> maintains stable accuracy as layers increase from 2 to 16+, whereas HGNN and HGNN<sup>+</sup> peak at 2 layers and sharply decline. This directly supports the paper's central claim of solving poor controllability in existing HGNNs and is the single most compelling piece of evidence.

3. **Clean theoretical grounding via ODE discretization**: Using Lie-Trotter splitting (Equation 5), the paper formally separates the continuous dynamics into control and diffusion steps, enabling a straightforward multi-layer neural implementation. The diffusion matrix A is designed with provable eigenvalue properties (Propositions 5.1 and 5.2) guaranteeing stability of the diffusion process.

4. **Formal connection to existing HGNNs**: Section 5.2 shows that when the control term is masked and teleport probabilities are 1, HDS<sup>ode</sup> reduces to a linear HGNN<sup>+</sup> layer, establishing theoretical continuity with prior work and explaining how the additional control and diffusion parameters improve representations.

## Weaknesses

### Fatal
None.

### Major

1. **Number of layers / termination time T for Tables 1 and 2 not stated**. The paper's headline results — the accuracy figures that demonstrate "beat all compared methods" — do not specify how many layers (equivalently, termination time T) were used. Section 6.2 states that HDS<sup>ode</sup> "produces reliable results" beyond 16 layers, and Figure 1 shows it underperforms HGNN<sup>+</sup> at shallow depths (e.g., 2 layers) before improving. Without knowing the layer count used to produce Tables 1 and 2, the reader cannot interpret the results, reproduce them, or assess whether the comparison is fair. A reader might reasonably wonder: were the reported numbers obtained at 2 layers (where Figure 1 shows HDS<sup>ode</sup> is worse than HGNN<sup>+</sup>) or at 16+ layers (where it excels)? This must be disclosed per dataset.

2. **Graph-based baseline adaptation to hypergraphs not described**. The paper compares against GCN, GraphSAGE, GDE, and GraphCON — methods designed for graphs, not hypergraphs. How these were adapted to hypergraph data (e.g., clique expansion, star expansion) is never specified. While the comparison against hypergraph-native methods (HGNN, HGNN<sup>+</sup>, UniGCN, UniSAGE) is the fairer one, the graph-based baselines, particularly the graph ODE methods (GDE, GraphCON), are central to the paper's discussion of "ODE-based methods show a clear advantage." If these were improperly adapted, that specific claim is on less solid ground.

### Minor

3. **Control step masking frequency unspecified**. The paper states "we mask the control function in most time iterations... (i.e., a control step is conducted every certain number of layers)" but never says what that number is. Since the control step introduces all learnable parameters, this decision directly determines model capacity, parameter count, and runtime. It is essential for reproducibility and for interpreting the complexity analysis.

4. **Stability analysis covers only the diffusion component, not the full ODE**. Propositions 5.1 and 5.2 and the analysis in Equation 8 address the diffusion matrix A in isolation. The full ODE (Equation 3) includes the nonlinear control term g, whose interaction with the diffusion dynamics is not analyzed. The paper acknowledges this ("Control terms are required to stabilize distinct categories...") but the claim that the analysis "indicates that HDS<sup>ode</sup> can capture long-range relations" is only partially supported — stability of the diffusion step is necessary but not sufficient to guarantee that representations preserve class separability after many steps.

5. **Teleport probabilities α_v and α_e not reported**. These hyperparameters (Equation 7) control how much information flows between vertices and hyperedges per diffusion step and directly affect the dynamics. Their values, tuning procedure, and sensitivity are not disclosed. This is relevant because Section 5.2 treats the case α_v=α_e=1 as the connection point to HGNN<sup>+</sup>, but the actual values used in experiments are unknown.

6. **Training/validation split description is ambiguous**. The paper states the combined training+validation set contains "a total of 1,500 vertices including 10 vertices per class for training." The intended meaning (training set = 10 per class, validation = remainder of 1,500) can be inferred, but the wording is unclear. Since datasets have different numbers of classes (7–20), this affects the training/validation ratio across datasets and should be stated unambiguously.

### Trivial

7. **"Production setting" terminology is non-standard**. The paper uses "production setting" to describe a setting where some vertices are held out during training (inductive). Standard terminology in the field calls this an inductive setting; "production" is not a recognized term and may confuse readers. The caption of Table 2 mixes "prod.", "ind.", and "trans." in ways that are not immediately clear.

## Nice-to-Haves

- Reporting average pairwise cosine similarity of vertex representations within vs. across classes as a function of depth (a standard oversmoothing metric) would strengthen the claim that HDS<sup>ode</sup> avoids representation collapse.
- Statistical significance tests (e.g., paired t-test over the 5 random splits) between HDS<sup>ode</sup> and the best competitor per dataset would add confidence, as the improvements are sometimes modest (1–2%).
- A dataset statistics table showing |V|, |E|, feature dimension, number of classes, and average hyperedge size would be a helpful reference.

## Removed Points

These points from the inputs are flagged for removal — treat them with caution:

- **Harsh Critic's claim that the split description is "incoherent" and that "10 per class" doesn't sum to 1,500**: The critic misread the sentence. The paper says the *combined* training+validation set totals 1,500 vertices, with 10 per class allocated for training specifically. The sentence is awkwardly phrased but not incoherent; the meaning is recoverable. Removed as an overstatement; preserved as Minor weakness 6 above with softened language.
- **Harsh Critic's suggestion that the comparison is "potentially misleading" because graph baselines are at a "systematic disadvantage" on hypergraph data**: Comparing graph methods on hypergraph data is valid and standard — it establishes a lower bound and shows that hypergraph structure matters. The asymmetry favors the baselines (the paper's method is hypergraph-native), which is permissible per the rules. Removed as an unfair-comparison concern that favors the baseline; the core observation (adaptation not specified) is kept as Major weakness 2.
- **Strength Finder's claim about Proposition 5.2 being "the same property as the graph Laplacian" as a weakness**: This appears only as an observation in the harsh critic's comment, not as a raised weakness per se. The critic notes this is a standard result, which is accurate, but the paper does not claim novelty for this proposition — it uses it to characterize the diffusion matrix. Removed as a non-weakness (no claim violation).
- **Harsh Critic's request for "learning rate, optimizer, weight decay, epochs, early stopping"**: These are standard implementation details that many papers defer to supplementary material (which is stripped in this PDF extraction). Removed per the rule against nitpicking trivial reproducibility details.
- **Harsh Critic's request for "broader comparisons" to hypergraph versions of GREAD/CGNN**: This is a nice-to-have suggestion, not a weakness. The paper already compares against the most relevant baselines (HGNN, HGNN<sup>+</sup>, UniGCN, UniSAGE, GDE, GraphCON). Removed as scope creep.
- **Strength: "Explicit time complexity analysis"** — kept as valid; "Clean ODE discretization via Lie-Trotter splitting" — kept as valid; "Formal connection to hypergraph neural networks" — kept as valid. None of these conflict with verified weaknesses.

## Novel Insights

The harsh critic correctly identifies that the paper's stability analysis addresses only the diffusion component and not the full control-diffusion dynamics, which is a genuine limitation that the paper acknowledges but does not resolve. Beyond this, the reviews do not produce a genuinely novel observation that the paper itself does not surface. The paper's own framing — that separating discrete message-passing into continuous control and diffusion steps via ODE discretization enables deeper, more stable hypergraph networks — is the central insight.

## Suggestions

1. **Disclose the number of layers / termination time T used for every result in Tables 1 and 2**, either per dataset or with a clear justification for the chosen value. Optionally include accuracy as a function of layers for all datasets (not just Cora-CA) in an appendix.
2. **Specify how graph-based baselines were adapted to hypergraph data** (clique expansion, star expansion, or other). If standard adaptation was used, state it and cite the reference.
3. **Report the control step masking schedule** (e.g., one control step every K=4 diffusion steps) and the values of teleport probabilities α_v, α_e used per dataset (or state that they were fixed across all datasets).
4. **Clarify the training/validation/test split**: explicitly state the number of training vertices per class, the total labeled set size, and whether these numbers are consistent across all datasets.
5. **Replace "production setting" with "inductive setting"** to align with standard terminology.
6. **Acknowledge the scope of the stability analysis** more precisely — state that it covers the diffusion component alone and that the interaction with the control term is left for future work.

### Summary

This paper proposes to apply sparse autoencoders to the attention output, i.e., the value vector after attention aggregation and before the feed-forward layer, to extract features and interpret the attention heads. The authors evaluate the sparsity and fidelity of the extracted features and, based on case studies, conclude that the features are generally interpretable. The authors further leverage the proposed features to investigate polysemanticity of attention heads and to study the so-called "induction heads". Finally, they apply the proposed features to study the indirect object identification (IOI) circuit and claim to deepen the understanding of the circuit.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper studies the attention output, a relatively underexplored area in mechanistic interpretability, whereas previous work mostly focused on the attention pattern or the feed-forward layer.

2. The authors provide a thorough evaluation of the extracted features based on the established criteria in the literature (e.g., sparsity and fidelity).

3. The authors leverage the proposed features to investigate interesting questions, such as the IOI circuit and the induction heads.

### Weaknesses

#### Some Related Works

[1] Monosemanticity and the geometry of features in transformers.
[2] The transformer family: Variations on a theme.
[3] Attention head analysis: A case study on vanilla transformers.
[4] The culture of attention: Discovery and characterization of emergent attention heads in GPT-2.
[5] Interpreting Attention Layer Outputs with Sparse Autoencoders.

#### comment

1. The paper does not offer novel insights into the attention mechanism that have not been previously discussed in the literature. Many findings, such as the various types of attention heads (e.g., induction heads, previous token heads, successor heads, and duplicate token heads), were already identified in [1, 2, 3, 4] through alternative methods. While the authors attempt to provide a more detailed analysis of induction heads in Section 4.2, the results are not convincing. The synthetic datasets used to distinguish between long-prefix and short-prefix induction heads are not adequately described, making it difficult to assess the validity of the results. Furthermore, the claim that long-prefix induction heads are more sensitive to longer prefixes is not strongly supported by the evidence presented. The differences in attention scores between long-prefix and short-prefix induction heads in Figure 5 are subtle, particularly for heads 5.1 and 5.5, and lack error bars, making it hard to determine if the observed differences are statistically significant. The intervention analysis in Figure 6 also suffers from similar issues, with small differences in attention scores and a weak correlation between the intervention effect and prefix length. The attempt to link these findings to performance changes would further weaken the argument.

2. The paper's main contribution, the application of sparse autoencoders to attention outputs, has already been explored in [5]. Although the authors claim that their main contribution lies in the analysis of the extracted features, the lack of novel insights undermines this claim. The paper would benefit from a more thorough investigation that leads to new, previously unreported findings about the attention mechanism.

3. The writing is not clear and is often confusing. The paper would benefit from a thorough revision to improve clarity and readability.

### Suggestions

The paper would significantly benefit from a more rigorous analysis of the synthetic datasets used to differentiate between long-prefix and short-prefix induction heads. Currently, the description of these datasets is insufficient, making it difficult to evaluate the validity of the experimental setup. The authors should provide detailed information on how these datasets were generated, including the specific parameters used and the criteria for distinguishing between long and short prefixes. Furthermore, it would be beneficial to include a more diverse set of synthetic examples to ensure the robustness of the analysis. For instance, the authors could vary the length of the prefixes and the types of tokens used to induce patterns. This would allow for a more comprehensive understanding of the behavior of induction heads under different conditions. The analysis should also include error bars in Figure 5 to allow for a more accurate assessment of the statistical significance of the observed differences. Without error bars, it is impossible to determine if the differences are meaningful or simply due to random fluctuations. The authors should also consider using a larger sample size to increase the statistical power of their analysis.

The intervention analysis in Figure 6 also needs further refinement. The current analysis relies on a small set of examples, which makes it difficult to draw strong conclusions about the relationship between intervention effect and prefix length. The authors should expand the set of examples to include a wider range of prefix lengths and token types. This would allow for a more robust analysis of the intervention effect and its correlation with prefix length. Additionally, the authors should provide a more detailed explanation of how the intervention is performed and how the attention scores are measured. The current description is too brief and lacks the necessary details to allow for a thorough evaluation of the methodology. It would also be beneficial to include a control group in the intervention analysis to ensure that the observed effects are indeed due to the intervention and not to other confounding factors. The authors should also consider using a more sophisticated statistical analysis to determine the significance of the observed effects.

Finally, the paper should focus on generating novel insights about the attention mechanism that have not been previously reported in the literature. While the application of sparse autoencoders to attention outputs is a valuable contribution, the analysis of the extracted features should lead to new and unexpected findings. The authors should explore different types of attention mechanisms and model architectures to see if the proposed approach can reveal new patterns and behaviors. For example, they could investigate the attention mechanisms in larger models or in models trained on different datasets. This would allow for a more comprehensive understanding of the attention mechanism and its role in language models. The paper should also provide a more detailed comparison of the proposed approach with existing methods for analyzing attention mechanisms. This would help to highlight the advantages and limitations of the proposed approach and to position it within the broader context of mechanistic interpretability research.

### Questions

1. In Section 4.2, the authors claim that they "confirm this hypothesis with independent lines of evidence that don't require SAEs." However, the evidence presented is limited to the analysis of synthetic datasets and the intervention on real examples of long-prefix induction. I am curious about what other lines of evidence could further strengthen the claim.

2. In Section 4.3, the authors state that "Attention Output SAEs immediately reveal the positional signal by decomposing these activations into interpretable features." However, it is unclear how the proposed features are used to identify the positional signal. In the subsequent paragraph, the authors mention that they "localized and interpreted causally relevant SAE features from the outputs of the attention layers that contain induction heads (Layers 5 and 6) with zero ablations." It is unclear how the causally relevant features are localized. Is the process similar to the one described in Section 4.2, involving intervention on real examples? Additionally, why are the ablations performed at the feature level rather than at the head level?

3. In the introduction, the authors state that "Sparse Autoencoders (SAEs) are a popular method for decomposing the internal activations of trained transformers into sparse, interpretable features." However, it is not clear why the features extracted by SAEs should be inherently interpretable. The interpretability of these features depends on various factors, such as the quality of the SAEs, the criteria used for interpretation, and the specific examples analyzed. A more accurate statement would be that SAEs are a popular method for decomposing internal activations into sparse features, and that these features can potentially be interpretable under certain conditions.

4. In the introduction, the authors state that "We introduce Recursive Direct Feature Attribution (RDFA)." However, the RDFA algorithm is not fully described in the paper. It would be helpful to provide a more detailed description of the algorithm in the main text.

### Rating

3

### Confidence

4

**********

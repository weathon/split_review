# Scaling Sparse Feature Circuits For Studying In-Context Learning

- Decision: Reject
- Scores: 3, 6, 5, 6

## Abstract
Sparse autoencoders (SAEs) are a popular tool for interpreting large language
model activations, but their utility in addressing open questions in interpretability
remains unclear. In this work, we demonstrate their effectiveness by using SAEs
to deepen our understanding of the mechanism behind in-context learning (ICL).
We identify abstract SAE features that encode the model’s knowledge of which
task to execute and whose latent vectors causally induce the task zero-shot. This
aligns with prior work showing that ICL is mediated by task vectors. We further
demonstrate that these task vectors are well approximated by a sparse sum of SAE
latents, including these task-execution features. To explore the ICL mechanism,
we adapt the sparse feature circuits methodology of Marks et al. (2024) to work for
the much larger Gemma-1 2B model, with 30 times as many parameters, and to
the more complex task of ICL. Through circuit finding, we discover task-detecting
features with corresponding SAE latents that activate earlier in the prompt, that
detect when tasks have been performed. They are causally linked with task-
executing features through attention layer and MLP.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This work uses sparse autoencoders (SAEs) to study in-context learning (ICL). In particular, The author uses SARs to identify task-execution features with task vector cleaning algorithm and uses sparse feature circuits to find task-detection features to better understand mechanisms of ICL.

### Strengths
1. The author make use of sparse autoencoders (SAEs) to decompose task-vectors, which is an interesting approach to analyze task vectors.

### Weaknesses
1. The writing of the paper can be improved. In many places (e.g., background in Section 2.2 and 2.3, Section 3 and 4), the author uses plain text to describe the method. It would be better to include clear definitions, illustrations or formulations. The current writing is confusing.
2. Line 175 to 183 should be embedded in a Figure.
3. It seems like algorithm task vector cleaning is the main algorithm (and one of the claimed contributions) of this paper. It is better to have that in the main part of the paper rather than in the Appendix. Furthermore, Appendix C only shows an overview Figure and an example without clear definition / formulation. Since this is the main proposed method, it is better to have an algorithm description with clear step-by-step formulation (or in pseudocode). Current form is confusing.
4. Observations from line 243 to 249 lack supporting evidence (it would be better to have some visualization or quantitative metric).
5. It seems hard for me to find the main contribution of this paper. While the author lists three contributions in the introduction, the first one might not be significant enough and the last two ones are vague (what are some specific observations?)

Minor issues:
1. Full stop symbol missing at some places (e.g., line 215, 287, 356 and all equations).

### Questions
1. In line 153, what is "do" in "do$(a=a')$"?
2. What is the "layers of interest" in line 197?

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper focuses on enhancing the interpretability of large language models (LLMs) through Sparse Autoencoders (SAEs), particularly in understanding the mechanism behind in-context learning (ICL). The authors propose a novel approach that uses SAEs to decompose complex ICL processes into task-specific features, which are responsible for detecting and executing tasks within the model. They identify two key types of features: task-detection features, which recognize tasks early in the prompt, and task-execution features, which are activated to complete the task. By adapting the Sparse Feature Circuits (SFC) methodology to a larger model (Gemma-1 2B), the authors provide a more detailed view of how ICL tasks are processed and executed by language models.

The paper introduces a task vector cleaning (TVC) algorithm that effectively decomposes task vectors into interpretable components using SAEs, leading to improved precision in ICL analysis. By analyzing these sparse task vectors, the authors uncover the causal connections between task-detection and task-execution features, which are mediated through attention layers and multilayer perceptrons (MLPs). This work not only advances the understanding of ICL but also showcases the potential of SAEs as powerful tools for interpretability research in LLMs, paving the way for future studies to refine and control model behavior.

### Strengths
One of the strengths of this paper is the successful implementation of a relatively complex combination of methods. From my perspective, the paper effectively combines pretrained SAEs, Inference-Time Optimization (ITO), and end-to-end loss into a cohesive approach. The fact that the authors managed to integrate these techniques and make them work together is a significant contribution, showcasing the potential of this hybrid methodology in enhancing model interpretability.

Another key advantage is that this approach eliminates the need to retrain an SAE. Given that training SAEs is a resource-intensive and time-consuming task, avoiding this step greatly reduces the computational burden. This not only makes the proposed method more practical for widespread use, but also encourages further research and experimentation within the community by lowering the entry barrier for other researchers.

### Weaknesses
One of the key weaknesses of this paper is the limited selection of models for experimentation. Currently, several models, including the Gemma-2 series (2B and 9B) and some from Qwen, have released portions of their SAE weights. I believe the authors should explore their method’s performance across a broader range of model architectures and parameter scales. Given the complexity of the proposed approach, there is some doubt as to whether the model would maintain the same level of effectiveness on more intricate SAE architectures. Testing the method on different models would help clarify its robustness and generalizability.

Additionally, the paper does not present a comparative analysis of the proposed method under varying SAE widths. For example, there is no exploration of how the method’s performance, in comparison to SAE reconstruction, shifts with different SAE widths. I believe the authors should provide multiple charts that, similar to Figure 2, compare their method’s stability across different SAE widths. There is a possibility that when the SAE width changes, the advantages of this method might diminish, particularly if the gap in sparsity between the SAE and the proposed method narrows.

Another potential weakness is the lack of detailed case studies. The paper would benefit from more specific examples that demonstrate how intervening on particular features affects task vectors in ICL. For instance, showing how intervention on specific task features leads to changes in ICL outcomes, or how the model loses its ICL capability, would significantly strengthen the paper’s claims and provide deeper insights into the causal mechanisms behind the proposed approach.

### Questions
- How well your cleaning method works in different model architecture e.g. Qwen 0.5B?
- How about different SAE widths? i.e. will a wider SAE further benefit your method or in contrast, hurt the performance?
- Is there any explanation to feature 1878 in Figure 3 that has effect to both it_en and algo_second, also feature 11173 ?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies task features for in-context learning (ICL). By applying SAEs, the authors identify sparse features within the task vector that represent task-specific knowledge and can activate tasks in a zero-shot manner, consistent with prior work on task vectors. To further explore this, the study extends the sparse feature circuits methodology to the larger Gemma-1 2B model for ICL tasks. The results reveal task-detecting features that activate early in prompts, signaling task performance and interacting causally with task-execution features through attention and MLP layers, providing new insights into ICL mechanisms in large models.

### Strengths
1. understanding how ICL works is an important problem
2. the paper is structured in a good way
3. the presentation using heatmap is intuitive and shows the effectiveness and exclusiveness of these task features

### Weaknesses
1. as the author has mentioned in the limitation section, this study only involves Gemma2-2b model. However, to ensure that the method is general, more model should be considered, especially since Gemma Scope also provides trained SAEs for Gemma2-9B models.
2. Fine-tune cost should be included in the paper to show whether the training requires a lot of resource.
3. Ablation study on L1 regularization during fine-tuning should be included to show what is the optimal L1 value for obtaining meaningful sparse features.

### Questions
1. the separation of task detection and task execution features is not clear to me. My understanding is that they are just features in earlier and later layers that both represents the task. Is there any more specific characteristics that defines these two kinds of features?
2. the author mentions that ablating a few hundred nodes can cause significant performance drop. Is this number small? What if only the task detection features are ablated? Removing these nodes will shut down the activation of task execution features?
3. since there are a few activated sparse features for the task vector, what is the functionality of other sparse features that are not task features? If all of them can boost the task, then the contribution of this work will be limited.

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
This paper presents novel techniques for analyzing in-context learning (ICL) mechanisms in large language models using sparse autoencoders. The authors develop a task vector cleaning algorithm and modify sparse feature circuits methodology to work with the Gemma-1 2B model. Their key findings include identifying and validating two critical components of ICL circuits: task-detection and task-execution features. The work demonstrates how these components causally interact to enable ICL capabilities, providing new insights into how language models perform this important function.

### Strengths
1. The paper makes significant technical contributions by developing novel methods (task vector cleaning algorithm and modifications to SFC) that enable analyzing in-context learning mechanisms in larger language models like Gemma-1 2B, which is substantially larger than models typically studied at this depth.

2. The work provides meaningful insights into how ICL works by identifying and validating two key circuit components (task-detection and task-execution features) and demonstrating their causal relationships, advancing our understanding of the mechanisms behind this important capability.

3. The methodology is rigorous, with extensive ablation studies, careful experimental design, and thorough validation of findings through steering experiments and causal analysis.

### Weaknesses
1. The paper's scope is limited to simple task vector settings and may not capture the full complexity of ICL as used in practice with longer sequences and more open-ended tasks.

2. While the authors acknowledge approximation errors in their interpretations (particularly regarding the role of attention heads vs MLPs), more discussion of the potential implications of these approximations on their conclusions would strengthen the paper.

3. The reproduction of results may be challenging since some key implementation details and hyperparameters are not fully specified, particularly regarding the task vector cleaning algorithm.

4. The paper would benefit from more direct comparisons to existing methods for analyzing ICL mechanisms to better contextualize the advantages of their approach.

### Questions
1. How might your findings generalize to more complex ICL scenarios involving longer sequences or open-ended tasks? Have you done any preliminary investigations in this direction?

2. Could you provide more details about the hyperparameter selection process for the task vector cleaning algorithm and its sensitivity to different parameter choices?

3. How do the approximation errors in interpreting the roles of attention heads versus MLPs affect the reliability of your conclusions about the causal relationships between task-detection and task-execution features?

4. Could you elaborate on how your approach compares to other methods for analyzing ICL mechanisms in terms of scalability, interpretability, and accuracy?

### Soundness
3

### Presentation
2

### Contribution
3

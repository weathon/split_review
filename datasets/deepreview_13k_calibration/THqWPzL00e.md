# TopoNets: High performing vision and language models with brain-like topography

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 6, 8, 8

## Abstract
Neurons in the brain are organized such that nearby cells tend to share similar functions. AI models lack this organization, and past efforts to introduce topography have often led to trade-offs between topography and task performance. In this work, we present *TopoLoss*, a new loss function that promotes spatially organized topographic representations in AI models without significantly sacrificing task performance. TopoLoss is highly adaptable and can be seamlessly integrated into the training of leading model architectures. We validate our method on both vision (ResNet-18, ResNet-50, ViT) and language models (GPT-Neo-125M, NanoGPT), collectively *TopoNets*. TopoNets are the highest performing supervised topographic models to date, exhibiting brain-like properties such as localized feature processing, lower dimensionality, and increased efficiency. TopoNets also predict responses in the brain and replicate the key topographic signatures observed in the brain’s visual and language cortices, further bridging the gap between biological and artificial systems. This work establishes a robust and generalizable framework for integrating topography into AI, advancing the development of high performing models that more closely emulate the computational strategies of the human brain.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a novel topoloss aimed at aligning AI models with the structure of brain neurons to create brain-like topography within these models. The topoloss defines a cortical sheet within AI models by reshaping the weight matrix and maximizes the cosine similarity between this cortical sheet and its blurred version, simulating synaptic pruning in the brain. The authors apply the topoloss to both CNN for vision and transformer for language models. Evaluation results indicate that the resulting toponets achieve a balance between maintaining topographical structure and overall model performance.

### Strengths
The idea of mapping model weights to a topographical cortical sheet is interesting, with a simple and elegant approach. The reshaping technique appears versatile and could potentially be applied to the weights of various models. The discussion on topographic signatures within toponets highlights promising avenues for brain-inspired AI research.

The paper is well-written, and the idea is easy to follow. The authors have provided sufficient detail and references to support reproducibility.

### Weaknesses
The selected backbone is somewhat outdated and lacks current relevance, reducing the overall significance of the work. For vision and language models, more meaningful choices would include ViT and LLMs like Llama.

No performance improvement compared to the original no-topo model, nor is there any discussion on time and data efficiency or interpretability. This makes the topography alignment appear theoretical, aligning with brain structures only on a formulaic level without contributing to human-level intelligence.

Furthermore, the application of the topological loss on the `mlp.c_fc` module of the transformer, while theoretically grounded, may not be practically aligned with how large-scale transformer models are typically fine-tuned. These models often rely on LoRA fine-tuning, which primarily targets the attention matrix, potentially limiting the practical applicability of the proposed approach in state-of-the-art large language models.

### Questions
Consider incorporating ViT and LLaMA as backbones for the framework to enhance relevance and performance. 

Compare the application of topological loss on the transformer's attention matrix instead of the fc matrix.

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
4

### Summary
The paper introduces a novel loss function called TopoLoss, which promotes spatially organized topographic representations in AI models without compromising task performance. The authors present TopoNets, a suite of models that incorporate this loss function into existing architectures, such as ResNet-18, ResNet-50 for vision tasks, and GPT-Neo-125M for language tasks. The key contributions include demonstrating that TopoNets outperform previous topographic models while maintaining high performance and replicating the topographic signatures observed in the human brain's visual and language cortices, thus bridging biological and artificial systems.

### Strengths
The strengths of the paper lie in its innovative approach to integrating topographic organization into AI models through the introduction of TopoLoss. This loss function effectively promotes spatially organized representations, which are crucial for achieving localized feature processing and lower dimensionality, like biological neural networks. The experimental validation across diverse architectures, including ResNet-18, ResNet-50, and GPT-Neo-125M, showcases the adaptability of TopoLoss and its ability to enhance model performance without sacrificing accuracy.

### Weaknesses
The weaknesses include a lack of extensive benchmarking against state-of-the-art models beyond those already tested, which may limit the generalizability of the findings. While TopoLoss is shown to improve performance, the paper does not sufficiently address how it scales with larger models or more complex tasks, raising questions about its applicability in high-dimensional settings. Additionally, the discussion surrounding the choice of scaling factor τ could be more detailed, particularly regarding its impact on various architectures and datasets. In addition, the inspiration from the brain's vision and language processing is superficial. The authors could strengthen their claims by providing additional insights into potential trade-offs between topographic organization and task-specific performance metrics!

### Questions
How does the choice of scaling factor τ affect performance across varied datasets beyond ImageNet?

Can you elaborate on the potential limitations of TopoLoss when applied to larger or more complex architectures?

What specific challenges do you encounter while integrating TopoLoss into existing architectures, particularly transformers?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper addresses the development of a novel loss function designed to create layer-wise 2D topographical organization in NLP and vision models, demonstrating improvements in performance over previous topographic models while maintaining spatial smoothness. This advancement has potential applications in achieving more biologically plausible neural networks with enhanced weight sparsity.

### Strengths
The proposed model improves both performance and topographic organization compared to previous models.

The core claim is well-supported, particularly in vision models, with evidence showing better performance and smoothness.

This approach opens up avenues for more biologically grounded AI models and potential advancements in weight sparsity.

### Weaknesses
The motivation for choosing a 2D topographic map as the structure is somewhat unclear. Other possible topographical structures might need consideration, such as hierarchical or radial organizations, which could potentially align better with certain neural architectures or functional requirements. The current justification lacks a strong theoretical basis for why a 2D sheet is the most appropriate representation for all types of data.

Comparisons lack consistency across architectures, raising questions about fairness (e.g., LLCNN-G has a different architecture). This makes it difficult to isolate the effect of the proposed loss function from the influence of architectural differences. It's not clear if the performance gains are solely due to the topographic loss or if they are confounded by the specific architecture of LLCNN-G.

Claims are primarily substantiated in vision models without equivalent evidence in NLP or other areas. The paper does not adequately address the challenges of applying topographic organization to sequential data or high-dimensional embeddings common in NLP. The lack of comparable models in NLP makes it hard to assess the generalizability of the proposed approach. In figure 5, the differences in performance between parameter-efficient TopoNets and baseline models only become significant when there are substantial drops in performance. This raises concerns about the practical utility of the method in scenarios where performance is critical.

### Questions
1.	Are there alternative topographical structures to 2D maps that could be more theoretically justified, and could the cortical sheet be better motivated?
2.	Is there a specific rationale behind comparing this model against LLCNN-G, given the architectural differences?
3.	Why is perplexity lower for tau = 5.0 compared to tau = 1.0, as shown in Figure 4B (Left)? Could adding a margin of error clarify this?
4.	Beyond effective dimensionality and smoothness, what additional metrics could quantify topography?
5.	Would adding a Brain Score comparison with TDANN provide valuable insight into brain-like topographic signatures?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work explores cortical topography from a representational standpoint, aiming to integrate such in both vision and language model classes to observe a higher performance than previous models that have attempted to do so, while reproducing certain aspects of topographic signatures within the learned feature representations and model parameters. Specifically, TopoNets show category-selectivity for faces, scenes, and bodies. Representations match neural responses in higher visual cortex under one-to-one mapping. Language TopoNets contained clusters of units with distinct temporal integration windows.

### Strengths
Modeling cortical topography is an important line of research for both neuroscience and AI, and I appreciate the authors’ work on the matter.
- The authors synthesize the application of a single loss term—namely, TopoLoss—to both residual vision networks and GPT. The motivation behind the loss seems well founded.
- Models trained using TopoLoss incur minimal drop in task performance, which is an important result, since previous models have struggled with this.
- The emergence of specific topographic signatures in sparse networks is again an important finding, given that the brain is optimized to work in an energy-efficient way.

### Weaknesses
 - Comparisons have been made in the manuscript (such as in result 3.1) where TopoNets are compared to the TDANN. TDANN was trained in a self-supervised way (precisely, using SimCLR), but I did not find (and I apologize if I may have missed it) any mention of the training/finetuning objective (categorization versus self-supervision) that the authors used. If TopoNets were trained through self-supervision, what objective was used? If supervised, is it justified to compare TopoNets with the TDANN? What contribution, if any, do the authors speculate the choice of the training objective plays alongside TopoLoss?
- Figure 6 - I appreciate the analysis around topographic signatures. However, I would prefer seeing the same plots replicated for the baseline vision and language models—(a) without being trained jointly on TopoLoss, (b) unoptimized (control) on both the task and topographic losses. This would really emphasize that what is being shown is not artifactual and attributable to the use of TopoLoss.

**Things (manuscript writing) that can be improved but did not impact my score**:
- In-text citations that are parenthetical and not narrative should be enclosed in parentheses. For example, lines 30-31 should be written as (Barlow, 1986; Rakic, 1988, …). Use the \citep{} LaTeX feature to do so.
- Line 182 - there should be at least a single sentence explanation of what FFCV is.
- “Resnet" -> “ResNet"
- Lines 213+ - the authors explain "L1 unstructured pruning” and “downsampling” as policies but not how they are being used as metrics. This should be made clear at this point in the manuscript.
- The first paragraph of Result 3.1 talks extensively about "model performance” without being explicit about what the task is (I am presuming object categorization) and what dataset it is being evaluated on (i.e., ImageNet). It is only in the figure on the next page that this is made apparent. I would encourage the authors to be more direct in their writing.
- Double quotes, such as on line 398, should be implemented using the ``...’’ LaTeX feature to show both opening and closing quotes.
- There should be a paragraph in the introduction talking about what topographic signatures look like for both vision and language—such as the emergence of pinwheel-like smooth orientation preference maps in V1 (Blasdel and Salama, 1986; Nauhaus et al., 2012), category selective maps in IT/VTC (Desimone et al., 1984), etc. This has been done later in the manuscript, but needs to be brought up earlier.
- Line 450 - "B. opographic" (typo)
- Line 483 - the authors claim that they have created “a broad suite of topographic AI models”. The use of the term “broad suite” is, in my opinion, an overstatement, given that the only model classes that were evaluated were residual networks and GPT. I would rephrase this claim.

### Questions
- Line 85: “… show diminished capacity to predict brain data.” (a) "brain data" is a highly vague term - are you implying neural predictivity (and if so, V1? VTC?), image-by-image human behavior prediction, or something else? (b) Margalit et al. (2024) show that TDANNs have a higher NSD voxel correlation to the VTC than purely categorization-driven models under one-to-one matching. Can the authors please clarify?
- Line 161 - “We trained 8 distinct ResNet-18 models …”. The authors mention that one is the baseline, and 6 others are TopoNets. What is the 8th model?

### Soundness
3

### Presentation
1

### Contribution
3

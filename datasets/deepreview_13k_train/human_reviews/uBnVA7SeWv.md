# XoRA: Expander adapted LoRA finetuning

- Decision: Reject
- Scores: 6, 3, 6, 5, 3

## Abstract
Parameter-efficient fine-tuning aims to reduce the computational cost of adapting foundational models to downstream tasks. Low-rank matrix based adaptation (LoRA) techniques are popular for this purpose. We propose XoRA, an efficient fine-tuning scheme, which sparsifies the low-rank matrices even further using expander masks. The mask is generated using extremal expander graphs (Ramanujan graphs) to maintain high edge connectivity even at a very high sparsity. Experimental results demonstrate that this method has comparable performance with the LoRA fine-tuning method while retaining much fewer number of parameters.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper presents a novel parameter-efficient fine-tuning method, XoRA, which leverages Ramanujan expander graphs to sparsify the low-rank matrices used in LoRA (Low-Rank Adaptation). This interdisciplinary approach integrates graph theory with machine learning to reduce the number of trainable parameters while preserving performance, showing potential for applications where computational resources are limited. The paper’s strengths lie in its innovative methodology and solid theoretical grounding. However, further clarity on computational complexity, practical scalability, and detailed explanations of technical terms would make the work more accessible and impactful. These minor revisions would strengthen the paper’s presentation and broaden its applicability.

### Strengths
1. Originality: XoRA brings novelty in sparsity for fine-tuning by proposing the use of Ramanujan expander graphs-a very unique conjunction between graph theory and machine learning.
2. Quality: The theoretical grounding is solid; the empirical results support the proposed approach. Employing expander graphs is an option that adds robustness and connectivity, which are well-justified in the paper.
3. Clarity: Generally, the methodology is well-structured with a clearly described experimental setup. Subsequent sections develop well from the preceding ones, and thus it is not too hard to follow.
4. Impact: XoRA resolves one of the basic issues in parameter-efficient fine-tuning and extends the usability of LLMs in resource-constrained settings. Insights drawn through XoRA will be useful in developing efficient model adaptation in different applications.

### Weaknesses
1. Complexity of Graph Generation: This paper is expected to further discuss computational complexity with regard to generating an expander graph, especially in relation to large and realistic applications. This would help the audience make a judgment based on how practically feasible XoRA would be. Specifically, the paper should analyze the time and space complexity of generating Ramanujan expander graphs for various sizes of the low-rank matrices used in LoRA. It should also discuss the impact of the bi-regularity parameter on the computational cost and the trade-offs involved in choosing different values for this parameter.
2. Limited Benchmark Diversity: Experimental results have been presented for only one GLUE benchmark with RoBERTa as the model backbone. In this aspect, increasing the diversity of benchmarks or model types will strengthen such results more reliably for other fine-tuning scenarios. The paper should include experiments on a wider range of tasks, such as those from the SuperGLUE benchmark, and also explore the performance of XoRA with different model architectures, such as those based on transformers or convolutional neural networks.
3. Technical Clarity: Several technical explanations, in particular about the Cheeger constant and the Ramanujan graph construction, assume some prior background in graph theory. Adding intuitive explanations for these terms could improve accessibility for a wider readership. For example, the paper should provide a more detailed explanation of how the Cheeger constant relates to the connectivity properties of the graph and how these properties are beneficial for the proposed method. The construction of Ramanujan graphs should also be explained in a more accessible manner, without assuming deep knowledge of algebraic graph theory.
4. Visual Comparisons: The paper would largely benefit from more schematics, diagrams, or tables comparing performances and/or the efficiency of parameters of XoRA against the other methods of fine-tuning. That way, it would be easier for the readers to perceive the advantage of the method at once. The paper should include a table that directly compares the number of trainable parameters, the computational cost, and the performance of XoRA with other parameter-efficient fine-tuning methods, such as LoRA, Adapter, and BitFit. This would help readers quickly grasp the advantages of the proposed approach.

### Questions
1. Computational Feasibility: Would the authors elaborate on the computational cost of the generation and use of large-scale Ramanujan expander graphs? Is there any trade-off in using sparse operators for a gain in efficiency versus the computational expense in generating the expander masks?
2. Has the XoRA approach been theoretically evaluated or verified for architectures that extend beyond RoBERTa? The paper's impact would be significantly increased by an understanding of its adaptability across various model structures.
3. Limitations of expander graph-based sparsity: What type of models or under what conditions does this method fail to work? Knowing the limitation, if any, would give a balanced view of the scope of the method.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes using expanders for employing sparsity on LoRA parameters.

The proposed method, XoRA, was examined on GLUE benchmarks with Roberta models.

### Strengths
Expanders have been used in deep learning for employing sparsity constraints on network architectures.

Their application for LoRA is interesting and the initial results are promising.

### Weaknesses
Although the initial results are promising, the experimental analyses are limited. Therefore, the contribution of the work is not clear.

More precisely, the proposed XoRA should be compared with the state-of-the-art sparse LoRA methods in different tasks using various models to show its merit and superiority.

### Questions
- There are some problems with the notation. For instance, the gradient update was defined by both AxB and BA. If BA is matrix multiplication of A and B, then, what does x denote?

- What does $h_V(\Gamma)$ denote?

- How does the XoRA perform with different LLMs and VLMs on additional tasks such as text and image generation?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the authors propose a novel LoRA-based optimization framework centered around Expander Graphs, specifically Ramanujan graphs. Ramanujan graphs possess remarkable properties that maintain high edge connectivity even at significant sparsity levels. This characteristic provides an opportunity to further sparsify the original LoRA while preserving comparable performance. Experiments conducted on the GLUE benchmark using the RoBERTa model demonstrate that, at approximately 50% sparsity in comparison to LoRA, the proposed method exhibits similar performance with LoRA.

### Strengths
1. The theory of Ramanujan graphs offers a formal mathematical framework for analyzing the sparsity of LoRA. This could represent a novel perspective for future LoRA optimization and, furthermore, opens avenues for mathematical analysis applicable to general pruning algorithms.
2. The presentation is commendable overall; the writing is clear and cohesive, making it easy to comprehend.

### Weaknesses
1. The novelty of this paper appears to be somewhat ambiguous. While the theory of Ramanujan graphs is well-established, the paper allocates considerable space to introducing the background. It remains unclear what new contributions this paper presents, as well as the distinction between existing knowledge and the authors' original work. I believe that merely applying an established technique to a new problem does not sufficiently meet the standards for publication at ICLR.
2. The experimental results do not sufficiently demonstrate the superiority of the proposed method in several respects:
2.1. The numerical results are not particularly striking. With 50% sparsity, XoRA is comparable to the original LoRA, while further increases in sparsity lead to diminished results. It is unclear how to effectively balance sparsity and performance.
2.2 The experiments are somewhat limited. I would recommend expanding the evaluation beyond the RoBERTa model to include BERT, GPT, and LLaMA. These well-known language models, along with multimodal models, could provide a more comprehensive perspective for assessing XoRA. In addition to the GLUE benchmark, I suggest incorporating the WikiText and PTB datasets for language model evaluation and MMLU for multimodal model assessment.
2.3. Furthermore, I propose including comparisons with methods such as LoRAPrune and LLM-pruner, as both approaches address the problem from a sparsity perspective.
2.4 Regarding practical applications, sparsity metrics may not be reliable indicators. It would be beneficial to see actual runtime improvements achieved with XoRA, such as inference latency and training costs. These critical aspects are currently omitted from the paper.

### Questions
In light of the identified weaknesses, I have the following inquiries:

1. What is the main contribution of this paper?
2. Could you provide additional insights into XoRA? Specifically, what type of sparsity pattern does the method have, and how might this impact runtime performance, including inference latency and training costs?
3. How can one effectively balance sparsity and performance with XoRA?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This authors propose XLoRA which is a PEFT technique that apply sparsity to LoRA low-rank matrices through expander graph-based masking, specifically leveraging Ramanujan graphs for sparsity while maintaining connectivity. The method aims to further reduce parameter count of LoRA fine-tuning.

### Strengths
1. Introducing expander graph-based masking for structural sparsity in fine-tuning models is innovative.
2. The paper clearly motivates the need for reducing parameters in LoRA and the potential benefits of sparsity.

### Weaknesses
1. Insufficient introduction of other advanced PEFT methods. The authors mainly focus on the introduction of LoRA-related PEFT methods. While other PEFT methods, such as IA3, OFT/BOFT and prompt-based methods are not discussed.
2. Insufficient comparison with advanced PEFT methods mentioned in weakness 1.
3. The manuscript highlights the benefits of using expander graphs, but it does not discuss any potential downsides. For example, generating Ramanujan graphs can be computationally intensive, especially for very high degrees. A discussion on computational overhead and any trade-offs in performance versus simplicity of other masking techniques would be beneficial.
4. Although parameter efficiency is demonstrated, it’s not clear how XoRA impacts memory usage and computational cost during.

### Questions
The paper shows that XoRA can perform well even at 75% sparsity. However, is there a threshold where the sparsity level starts to significantly degrade performance? What is the relationship between that sparsity level and the rank of LoRA adapters?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes an approach to sparsify LoRA's low-rank matrices to reduce redundancy. They induce sparsity using extremal expander graphs (Ramanujan graphs) to generate a mask which can be applied on the low-rank A,B matrices.

### Strengths
Using Ramanujan graphs for LoRA is interesting and empirical results show that comparable performance can be achieved with a small amount of trainable parameters.

### Weaknesses
- There is no comparison with other LoRA variants. In particular, approaches which enforce sparsity such as VeRA [1], RoSA [2], SoRA [3], AdaLoRA [4]
- Only RoBERTa base (125M) and RoBERTa large (355M) are evaluated. These models are small in size and there is no practical need to reduce their number of parameters when training. Experiments at a larger scale e.g., Llama 7B should be carried out.

### Questions
- How does the method differ from other sparsity-inducing LoRA methods in terms of performance and complexity?
- What is the time complexity to generate the expander masks in section 4.1? 
- How are the masks updated during training? Will the updates result in masks that do not satisfy the Ramanujan criteria?

### Soundness
2

### Presentation
2

### Contribution
2

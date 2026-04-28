# Compositional Video Generation as Flow Equalization

- Decision: Reject
- Avg Score: 6.75
- Scores: 8, 8, 6, 5

## Abstract
Large-scale Text-to-Video (T2V) diffusion models 
    have recently demonstrated unprecedented
    capability to transform natural language descriptions into stunning and photorealistic videos. 
    Despite the promising results, a significant challenge remains: 
    these models struggle to fully grasp complex compositional 
    interactions between multiple concepts and actions. {This issue arises when some words dominantly influence the final video, overshadowing other concepts.}
    To tackle this problem,     
    we introduce \textbf{Vico}, a generic framework for compositional video generation 
    that explicitly ensures all concepts are represented properly.
At its core, Vico analyzes how input tokens influence the generated video, 
and adjusts the model to prevent any single concept from dominating. 
Specifically, Vico extracts attention weights from all layers to build a spatial-temporal attention graph, and then estimates the influence
as the \emph{max-flow} from the source text token to the video target token.
Although the direct computation of attention flow in diffusion models is typically infeasible,
we devise an efficient approximation based on
subgraph flows and employ 
a fast and vectorized implementation,
which in turn makes the flow computation
manageable and differentiable.
By updating the noisy latent to balance these flows, Vico captures complex interactions and consequently produces videos that closely adhere to textual descriptions. We apply our method to multiple diffusion-based video models for compositional T2V and video editing. Empirical results demonstrate that our framework significantly enhances the compositional richness and accuracy of the generated videos. Visit our website at~\href{https://adamdad.io/vico/}{\url{https://adamdad.io/vico/}}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a novel approach for compositional video generation. The proposed method begins by analyzing the impact of input tokens on the video output, ensuring that no single concept predominates the generated content. The core concept involves computing each text token's contribution to the video generation process through maximum flow. The paper introduces an efficient computational technique by approximating the subgraph flow with a vectorized implementation.Finally, the method has been tested across various diffusion-based video models, and the experimental results confirm its effectiveness in enhancing both visual fidelity and semantic accuracy.

### Strengths
1. The proposed method is innovative and can be integrated with existing video generation techniques. The experiments demonstrate the effectiveness of applying the "Vico" method on current models such as AnimaDiff, ZeroScore V2, and VideoCrafter V2, showing notable improvements in results.

2. The paper is well-articulated, featuring thorough theoretical analysis and proof.

### Weaknesses
1. The user study (Table 2) is limited to only ten video clips, which is insufficient to conclusively prove the effectiveness of the method.

### Questions
n/a

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This manuscript tackles the problem of video generation, focusing on improving the compositional and complex interactions in the final output. The proposed approach utilizes a flow equalization formulation to ensure that different tokens of input get a fair amount of attention throughout the self-attention layers.

### Strengths
Capturing compositional relationships in the final generated output is a very important problem and, to the best of my knowledge, is one of the biggest issues with current SOA in GenAI.
This paper correctly identifies one of the main issues throughout the attention mechanism and tries to improve the contribution of different tokens in attention layers as a test-time optimization. The authors model the information flow of the generative model as a graph, which is a smart and (semi-)novel strategy (for the videos) in my opinion.

### Weaknesses
The biggest weakness of the solution is the readability of this paper. It was very hard for me to read through the text and jump from text to mathematical notations and back. I will ask for a few clarifications in the questions block.

In line 247, the capacity matrix W, what are each row and column? Why does the first row have the `t` index while other rows don't?
Lines 241, and 243. What is the difference between e_(i,j), i=j and e_(i,i) difference?
Section 3.1: At first glance, it is not clear what is x_t (definition) and how A_i is extracted out of it.
What is token-reweight in Table 1?
There are some valid categories of issues in Video Generation shown in Figure 1. My question is if the lack of fair attribution and attention is the only problem that causes these issues. If not, what are the other factors?

### Questions
1-  In line 247, the capacity matrix W, what are each row and column? Why does the first row have the `t` index while other rows don't?
2- Lines 241, and 243. What is the difference between e_(i,j), i=j and e_(i,i) difference?
3- Section 3.1: At first glance, it is not clear what is x_t (definition) and how A_i is extracted out of it. 
4- What is token-reweight in Table 1? 
5- There are some valid categories of issues in Video Generation shown in Figure 1. My question is if the lack of fair attribution and attention is the only problem that causes these issues. If not, what are the other factors?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces Vico, a novel framework specifically designed for compositional video generation. Vico employs a maximum flow approach to ensure fair contributions from each input token, integrating sub-graphs, a soft flow strategy, and vectorized path flow computation for efficient inference. Extensive experiments demonstrate that Vico significantly surpasses existing baselines in compositional generation tasks.

### Strengths
1. This paper presents a highly innovative solution to the problem, utilizing traditional max flow to address token-level response balancing, thereby achieving effective compositional generation.
2. I appreciate that extensive effort has been put into designing feasible experiments. The authors introduce practical techniques such as subgraph, soft min, and vectorized flow strategies, which significantly enhance inference speed.
3. The experiments are thorough and well-executed, including comprehensive comparative studies and a detailed user study, which provides strong validation for the proposed approach.
4. The visual quality of the generated videos is satisfying, despite the limited number of examples presented.

### Weaknesses
1. The primary concern is the lack of comparisons or discussions involving recent text-to-video (T2V) methods. The baseline model, VideoCrafter2, was released over a year ago. To convincingly demonstrate the relevance of the compositional generation problem, the paper should ideally compare against more advanced, recent baselines like OpenSora,  CogVideoX, or more. The absence of these comparisons makes it difficult to assess the true advancement offered by Vico in the current landscape of T2V generation.
2. Additionally, the paper lacks comparisons to existing compositional video generation models. For instance, methods like LVD, which uses LLMs for prompt decomposition with gradient-based layout optimization during inference, VideoTetris, which employs spatiotemporal diffusion for multi-object generation, and VideoDirectorGPT, which combines an LLM director with spatial convolutions for layout learning, are not discussed. Including comparative studies with these related works would strengthen the evaluation and clarify the advantages of the proposed approach. The lack of these comparisons makes it hard to determine if Vico offers a novel approach or if it is simply a re-implementation of existing techniques.
3. The paper lacks a theoretical justification for the assumption that each token should have an equal impact on the generated result. In typical prompts, not all tokens necessarily require equal influence; for instance, non-descriptive tokens or function words might logically play a reduced role in the attention process. Given the strength of this assumption, a more rigorous rationale or proof would help validate its applicability. The paper should provide a more detailed analysis of why equal token influence is a reasonable or necessary constraint for compositional video generation.
4. Another strong assumption is made regarding cross-attention in T2V models. The paper’s approach relies on cross-attention being embedded uniformly across all layers and frames, yet many contemporary T2V models, such as CogVideoX, Mochi-1, and commercial models like Kling, utilize 3D attention mechanisms similar to MMDiT. This raises concerns about the applicability of the paper’s assumptions to modern architectures, which may limit its generalizability. The paper needs to address how its method can be adapted to these more complex attention mechanisms.
5. The paper contains a few typographical errors that affect readability. For example, in the introduction, the prompt "a bird looks like a cat" is used as an example, but the actual effect of this prompt is not demonstrated. This lack of clarity detracts from the overall presentation and makes it harder to follow the paper's arguments.

### Questions
1. My primary question is,  do the paper's assumptions hold true for modern 3D attention models, such as the open-source CogVideoX. Can the proposed method balance token contributions effectively when applied to an attention graph in such models?
2. In the case of 3D attention, how much additional computational overhead does the proposed approach introduce? Cross-attention calculations are relatively lightweight, but if full attention is employed, as in MMDiT, would the method’s computations lead to significant cost increases?
3. The paper mainly showcases relatively short prompts. I would like to ask if the proposed method can handle modern, highly descriptive prompts that may reach up to 100 words. Would the method remain feasible for inference, and what would be the associated computational cost in such cases?
4. As a fair comparison, could the paper utilize T2V CompBench[1], a benchmark specifically designed to evaluate compositional video generation, to better assess and compare the performance of the proposed model against other existing models? I wonder how well this method performs under a more comprehensive benchmark.

[1] Sun, Kaiyue, et al. "T2V-CompBench: A Comprehensive Benchmark for Compositional Text-to-video Generation." arXiv preprint arXiv:2407.14505 (2024).

### Soundness
3

### Presentation
2

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
This paper presented a new method named Vico, a framework designed for compositional video generation. Different from existing methods that may not reflect the intended composition of elements, the proposed Vico tries to adjust the model to ensure that no single concept dominates. Specifically, Vico calculate the contribution of each text token using max-flow and leverage a sub-graph flow to propagate information. The proposed method can be implemented by inserting into diffusion-based methods. Extensive experimental results verify the effectiveness of the proposed method.

### Strengths
1.	A new method named Vico for compositional video generation is proposed.
2.	The proposed Vico leverage max-flow to ensure that no single concept dominates.
3.	Extensive results verify the effectiveness of the proposed method in generation high-quality videos.

### Weaknesses
1.	This paper argues that the proposed method explicitly constrains the contribution of each token to be the equal, but in fact there are some words with no contribution or words with outstanding contribution in a sentence, that is, the importance of each word should be different. For example, "On a certain day, a boy is running", where "On a certain day" is not informative, only the following "the boy is running" is informative. The authors should discuss the problem.
2.	The proposed method needs to be optimized at test time, and the resource consumption of optimization such as time and computational overhead should be discussed. The paper lacks a detailed analysis of the inference time overhead introduced by the optimization process, which is crucial for practical applications. The computational cost, especially in terms of GPU memory usage, should also be quantified and compared with baseline methods.
3.	This paper said “While the compositional text-to-image sythesis Liu et al. (2022); Chefer et al. (2023); Kumari et al. (2023); Feng et al. (2023); Huang et al. (2023) has been more studied, the challenge of compositional video generation has received less attention.” My question is that whether these image methods can be extended to compositional video generation task? If not, the authors should give a explanation. If yes,  please give a comparison with them.
4.	Can Vico be used in compositional motion scenarios? Such as "In a room, a cat is running from left to right, a dog is running from right to left", this complex movement scene is very interesting.

### Questions
Please refer to Weaknesses for more details.

### Soundness
3

### Presentation
2

### Contribution
2

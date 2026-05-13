# Uncovering the Spectrum of Graph Generative Models: From One-Shot to Sequential

- Decision: Reject
- Scores: 5, 3, 6, 5, 5

## Abstract
In the field of deep graph generative models, two families coexist: one-shot models, which fill the graph content in one go given a number of nodes, and sequential models, where new nodes and edges are inserted sequentially and autoregressively. Recently, one-shot models are seeing great popularity due to their rising sample quality and lower sampling time compared to the more costly autoregressive models. With this paper we unify the two worlds in a single framework, unlocking the whole spectrum of options where one-shot and sequential models are but the two extremes. We use the denoising diffusion models' theory to develop a node removal process, which destroys a given graph through many steps. An insertion model reverses this process by predicting how many nodes have been removed from the intermediate subgraphs. Then, generation happens by iteratively adding new blocks of nodes, with size sampled from the insertion model, and content generated using any one-shot model. By adjusting the knob on node removal, the framework allows for any degree of sequentiality, from one-shot to fully sequential, and any node ordering, e.g., random and BFS. Based on this, we conduct the first analysis of the sample quality-time trade-off across a range of molecular and generic graphs datasets. As a case study, we adapt DiGress, a diffusion-based one-shot model, to the whole spectrum of sequentiality, reaching new state of the art results, and motivating a renewed interest in developing autoregressive graph generative models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new Insert-Fill-Halt (IFH) framework for graph generation, which tries to bridge two types of existing approaches, i.e., one-shot generation and sequential generation. Specifically, at each step, the Insertion Model chooses how many new nodes to generate, the Filler Model fills the new nodes’ labels, features, and connections, and the Halt Model chooses if the generation needs to terminate. The training of the IFH framework uses the denoising diffusion model to develop a reversed node removal process, which destroys a given graph through many steps. Experimental results demonstrate the sample quality-time trade-off across a range of molecular and generic graphs datasets.

### Strengths
1. It is interesting to bridge one-shot and sequential graph generation methods with a unified framework.

2. Authors provide the analysis of the sample quality-time trade-off across many real-world datasets.

3. The paper is well-written and easy to understand.

### Weaknesses
1. The proposed framework does not provide insightful knowledge regarding choosing one-shot or sequential generation methods. 

2. Only one base model is tested in the proposed IFH framework.

3. Experiments are not sufficient. Ablation studies are missing. The comparisons of time/memory cost with baselines are missing.

### Questions
Please see my listed weakness above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper explores combining autoregressive method with one-shot diffusion model. Diffusion model builds the forward process with adding noise gradually and the backward process with removing noise step-by-step. Similarly but not the same, the paper models the forward process as removing block of nodes and edges gradually towards an empty graph, and in backward process it reverts this process with adding nodes and edges back. This view combines autoregressive method and one-shot method together, via changing the granularity of node/edge removing. The author also discussed many different choice of node/edge removing random process. The experimental results show certain improvement on molecular datasets.

### Strengths
1. Exploring the direction of combining autoregressive method and one-shot diffusion model is meaningful, as they have different strength. The proposed method successfully combined them together, and the proposed process of block removing is interesting. 
2. The author shows that the complexity of sequential model is lower than one-shot generation, and discussed its strength in section 4.3. This is interesting, and engineering wise one can use sparse storage for already generated components to save runtime and memory. 
3. One key component of this proposed process is the block removing process, and the author discussed many choice with ablation studies.

### Weaknesses
1. The proposed method shares certain similarity with GRAN, while being novel for adapting diffusion process inside.
2. The goal of combining autoregressive method and one-shot generation is to combine their strength together while eliminate their shortcomings. However I think the proposed method is not ideal for this goal. For example, one-shot diffusion is a permutation equivariant generation model that is invariant to node permutation, here the designed model becomes ordering sensitive, which needs a careful ablation over node removing process. And autoregressive method has the problem of being hard to parallel during training, hence the designed model will be even slower in training comparing with one-shot generation. Last, the reported experimental result doesn't show a significant benefit of adapting sequential generation to one-shot diffusion.
3. The experimental result is kind of weak at current stage. First, for both QM9 and ZINC, the result doesn't beat the baseline like CDGS in many perspective. Second, for generic graph generation in Appendix, the designed method is significantly worse than the baseline. This questions whether the designed method, while being combination of autoregressive and one-shot, may suffers from the shortcoming of both sides instead of combining their strengths. Also, the designed method may suffer from the randomness of block removing process.
4. I suggest the author also discuss the training cost instead of just the test runtime and memory cost.

### Questions
1. For Table 2, there is no result for the baseline DiGress, is that equivalent to one-shot? 
2. It seems that you have many different models trained: halting model, node size prediction model, and one denoising model. Can you talk about how do you do model selection for them? 
3. You mentioned that you can use sparse format for already generated part, are you using this format during training?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper unifies the one-shot and autoregressive graph generation methods into a diffusion framework and proves that these two methods are two extremes of the unified model. Specifically, in the forward phase, blocks, i.e., a set of nodes, are gradually removed as the noise increases. In the backward phase, blocks are gradually added as the denoising process proceeds. When the block size is set to 1, the diffusion model degenerates to an autoregressive approach. When the block size is equal to the graph size, the diffusion model becomes a one-shot method. Experiments on both molecular and generic graphs witness a trade-off between the quality and time of sampling.

### Strengths
1. This paper unifies the autoregressive and one-shot graph generation methods into a unified diffusion model, where the removal of nodes is used as the forward process and the generation of nodes is the denoising process. The idea is sound and interesting.

2. The proposed method trade-offs the quality and time of sampling. The proposed method outperforms state-of-the-art autoregressive methods when degenerating to 1-node sequential.

### Weaknesses
1. This paper combines the ideas of autoregressive graph diffusion [1] and block generation [2]. Although the combination is natural, I am not clear on the main difference between the proposed method and GRAN. It seems that the unity of autoregression and one-shot is due to the design of block generation, rather than the diffusion of node removal. Specifically, the paper does not clearly articulate how the proposed diffusion process over blocks differs fundamentally from the block-based generation in GRAN, beyond a high-level claim of unifying different generation paradigms. The core mechanism of adding or removing blocks seems conceptually similar, and the novelty of the diffusion aspect in this context needs further clarification. The paper should provide a more detailed comparison of the algorithmic differences, especially in how the block selection and generation are handled during the forward and reverse processes, to justify the claim of a novel diffusion approach.

2. It's not clear to me what advantages 1-node IFH has over autoregressive methods. Does the benefit come from the prediction of the number of nodes? The paper states that 1-node IFH is an autoregressive model, but it does not explain why this specific instantiation of the framework provides any advantage over existing autoregressive methods. It is unclear if the performance gain comes from a better node-by-node generation process, or if it is simply a result of the unified framework. The paper needs to elaborate on the specific mechanisms within the 1-node IFH that lead to improved performance compared to other autoregressive baselines, beyond just stating that it is a special case of the proposed framework. A detailed analysis of the differences in the node generation process is needed.

3. The time and memory costs of baselines are not reported in Tables 2 and 3. It is therefore impossible to see the trade-off between sampling quality and time. Without the computational costs of the baselines, it's difficult to assess the practical advantages of the proposed method. The paper should include the time and memory costs for all baselines in the same tables as the quality metrics, to allow for a direct comparison of the trade-offs. This is crucial for evaluating the practical utility of the proposed framework, especially when the goal is to offer a trade-off between quality and sampling time.

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a generalization of deep graph generative models that results in a spectrum between one-shot models and sequential models. They take inspiration from diffusion model theory to train a model on the corruption of graphs (removal of blocks of the node) to learn how to insert multiple nodes and fill in edges. They adapt a diffusion-based one-shot model DiGress to their approach (1-node sequential) and show that it outperforms state-of-the-art on some datasets.

### Strengths
- The method unifies one-shot and sequential generation methods and opens up new opportunities for searching for new graph generation methods.
- Evaluation covers several datasets and metrics.

### Weaknesses
1.  **Performance on other datasets** - The paper presents the evaluations on two datasets in the main content and three datasets in the appendix. While the proposed approach outperforms the state-of-the-art in the former two, multiple one-shot methods outperform the proposed approach. This undermines the impact of the new approach. Also, it is not clear why only the two datasets with good performance were shown in the main paper. How about other datasets that have been used in prior work, such as Grid, Protein, and 3D point-cloud?

2. While the method unlocks a spectrum between one-shot and sequential models, it does not present a way to choose one from the spectrum. How many nodes should be added per step? Is this a hyperparameter? The presented experiments show that seq is better. Does "seq" refer to 1 node per step? There are seq-small and seq-big in the Appendix, but none of the variations outperform CDGS except for one metric on one dataset. 

3.  **Presentation Issues** - While the writing is understandable, there are several presentation issues. For example:
    - Definition 6: "*An* halting process ... ." Also, I don't think the first sentence completely defines the halting process; the second sentence does. So, this should be rewritten.
    - Page 6: "On the other hand, ...  such as VAE, Normalizing Flow, Diffusion" is missing an *and*.

### Questions
Addressing the following would significantly improve my score
1. Among the five datasets presented, the proposed approach does not outperform other methods in majority of the metrics. Can the authors  justify the utility of their approach given these results?

1. How to select $r_s$ and what are the differences between seq, seq-small, and seq-big?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a diffusion-based graph generative model that unifies both one-shot and autoregressive generative models. The node removal process is conducted with a denoising diffusion model and the insertion reverses the process by predicting the number of nodes that have been removed. Setting the number of nodes from 1 to n enables the unification of one-shot and autoregressive generation.

### Strengths
1. This paper proposes the novel unification between one-shot and autoregressive graph generative models using diffusion models.
2. The introduction of flexible-sized block-wise generation for graph generation stands out as a noteworthy contribution.

### Weaknesses
1. Can the unification of one-shot and autoregressive graph generative models be a strong contribution? For instance, GRAN (Liao et al., 2019) can also be the unification between one-shot and autoregressive graph generative model by setting the block size as the number of nodes. What is the key difference of the work from GRAN except for the usage of diffusion models? The flexibility argument is not fully convincing. While the proposed method allows for varying block sizes, it's not clear if this flexibility translates to a significant practical advantage over methods like GRAN, which, although using a fixed block size, can still generate graphs of varying sizes by controlling the number of blocks. The core innovation seems to be in the application of diffusion models, but the unification aspect needs more justification beyond simply allowing different block sizes.
2. I wonder if it is proper to say the performance as the new state-of-the-art results as mentioned in the abstract. The FCD for QM9 and NSPDK for ZINC do not seem to be state-of-the-art results. Also, as the authors adapted DiGress, the performance comparison with DiGress can be meaningful. The claim of state-of-the-art performance is misleading, as the results are not consistently superior across all metrics and datasets. Specifically, the FCD score on QM9 and NSPDK on ZINC are not state-of-the-art, and the comparison against DiGress, the model this work is based on, is essential to properly contextualize the contribution. The lack of a direct comparison makes it difficult to assess the true advancement of this model.
3. Lack of detailed analysis on the sample quality-time trade-off. A more detailed analysis of the correlation between the sample quality and time (or memory consumption) is needed by comparing the one-shot and autoregressive versions of the IFH model. The analysis should also include how the different block sizes affect the trade-off. The current analysis is insufficient, as it does not provide a clear picture of how the different levels of sequentiality impact the sample quality, computational time, and memory consumption. A more detailed analysis is required to understand the practical implications of choosing different block sizes and sequentiality levels.

### Questions
1. Which level of sequentiality did the authors use (I cannot find details in appx D.)? Does the degree of sequentiality imply the block size (or the number of steps)?
2. The generic graph generation results in appx B do not look good enough. Is there any particular reason that the model works okay for molecular graphs but not for non-attributed generic graphs?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

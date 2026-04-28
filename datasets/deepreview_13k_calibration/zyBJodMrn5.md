# On the generalization capacity of neural networks during generic multimodal reasoning

- Decision: Accept
- Avg Score: 5.67
- Scores: 8, 3, 6

## Abstract
The advent of the Transformer has led to the development of large language models (LLM), which appear to demonstrate human-like capabilities.
To assess the generality of this class of models and a variety of other base neural network architectures to multimodal domains, we evaluated and compared their capacity for multimodal generalization.
We introduce a multimodal question-answer benchmark to evaluate three specific types of out-of-distribution (OOD) generalization performance: distractor generalization (generalization in the presence of distractors), systematic compositional generalization (generalization to new task permutations), and productive compositional generalization (generalization to more complex tasks structures). 
We found that across model architectures (e.g., RNNs, Transformers, Perceivers, etc.), models with multiple attention layers, or models that leveraged cross-attention mechanisms between input domains, fared better.
Our positive results demonstrate that for multimodal distractor and systematic generalization, either cross-modal attention or models with deeper attention layers are key architectural features required to integrate multimodal inputs.
On the other hand, neither of these architectural features led to productive generalization, suggesting fundamental limitations of existing architectures for specific types of multimodal generalization.
These results demonstrate the strengths and limitations of specific architectural components underlying modern neural models for multimodal reasoning. 
Finally, we provide \textit{Generic COG} (\texttt{gCOG}), a configurable benchmark with several multimodal generalization splits, for future studies to explore.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a new multimodal question answering benchmark for out-of-distribution generalization, specifically covering task compositionality, robustness to distractors and combinatorial generalization. It uses this benchmark to evaluate various models and analyze their performance.

### Strengths
- **Topic**: The paper studies an important topic which in my opinion is underexplored in current deep learning research. Especially given the tendency these days to scale training up to vast amounts of data, I believe it is particularly important to design carefully controlled benchmarks that can: evaluate the model’s performance from a critical and cautious standpoint, point to their fundamental limitations (e.g. systematic generalization), and support further research about ways to overcome these.  
- **Evaluation**: The paper offers both extensive extrinsic evaluation, with performance comparison of various models on the different generalization skills, as well as intrinsic analysis of their internal representations’ degree of alignment to the stimuli.
- **Clarity**: The writing quality is good and the paper is clear and easy to follow. The paper is well-organized, claims and findings are clearly stated, and useful figures and diagrams are provided.
- **Related Works**: It does a good job in providing the relevant context, motivation and related works. 
- **Contribution**: The empirical findings of the paper on the benefits and limitations of different inductive biases such as recurrent and attention-based are important and may be of broad interest to the community.

### Weaknesses
 - **Pre-trained models** The paper focuses on models trained from scratch rather than pre-trained. This could be a strength and a weakness. On the one hand, it allows for isolating the contribution of the architectural choices from other factors of optimization, and training data. On the other hand, it has been observed that by training models at large enough scales enables the emergence of generalization capabilities, which we don’t see in smaller scales. I think it will be critical to also analyze the performance of pretrained models on the benchmark, in order to strengthen the paper.
- **Visual Simplicity**: The visual side of the benchmark is quite rudimentary, featuring colorful letters. Extending it to a larger range of visual tokens/objects, that could have more than one property (color), and a broader set of elements and variations (than 26 letters), could be a straightforward extension that could help make it a bit more challenging visually.

### Questions
- **COG task**: It will be useful to discuss the COG task (rather than just mentioning it) before describing the new gCOG one, so that it will be clearer to the reader what are new contributions of the new benchmark compared to COG and the degree of their importance. In the overview diagram I would also recommend showing a sample also from COG to make the differences clearer. 
- **Grid size / generalization**: It could be interesting to vary the size of the grid in training/evaluation and study its impact on model’s performance. 
- **Terminology**: I recommend changing the phrase “Distractor generalization” to one that better conveys it’s about changing the answer distribution. Maybe e.g. answer distribution shift. I also recommend changing the name “Systematic compositional generalization” to “combinatorial generalization”, to emphasize that the main point is the generalization to permutation, and also to better contrast it with the following “Productive generalization” (which could also be systematic).
- **Figures**: Would be good to increase the size of the plots in Figure 3b. It will also be good the increase the distance and visual separation between the sub-figures in each figure throughout the paper. 
- In the introduction: “multimodal question-answer” -> “answering”.
- “This design allowed us” -> “This design allow us”.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new benchmark for assessing various forms of generalization in a multimodal setting named gCOG. The dataset includes several different splits intended to measure different aspects of generalization. The paper also compares several different model architectures on the dataset.

### Strengths
* The paper introduces a new dataset, gCOG. While the dataset is conceptually similar to those from prior work, such as gSCAN, it supports different types of contexts and instruction types, including more compositional instructions. I'm aware of some prior work (e.g. [1], [2]) that studied compositional generalization in natural language tasks and found that gains on one synthetic task did not always transfer to other tasks, so increasing the diversity of such benchmarks for assessing compositional generalization and related challenges in the multimodal setting could be a potentially valuable contribution.

[1] https://arxiv.org/abs/2007.08970
[2] https://aclanthology.org/2021.acl-long.75/

### Weaknesses
 * I'm concerned about the strength of the baselines used in the paper (see my related questions below). While the primary contribution of the paper is the dataset, it is also important to establish strong baselines for this new dataset and to ensure that the conclusions from the empirical results are valid. The appendix states that only a *single Transformer layer* with a *single attention head* was used. This is almost certainly not an optimal depth and number of attention heads. Relatedly, it looks like some models are potentially underfit, according to the figures. With >5M training examples and a relatively simple input space, I would have expected a reasonably sized Transformer model to achieve low training loss and reasonable IID generalization. If these models could have been applied to similar tasks such as gSCAN (even using symbolic tokens to represent the scene context), where they could be compared with comparable baselines from prior work, this would have helped establish that these are indeed reasonably strong baselines that have been well tuned.
* The qualitative difference between gCOG and datasets from prior work such as gSCAN was not very clearly described. For example, one of the key claims seemed to be gCOG "employs generic feature sets that are not tied to any specific modality". However, it seems like it is a useful property for a multimodal dataset to have a clear relation to real-world multimodal tasks. Indeed, the authors provide interpretations of their tasks in the form of natural language instructions and visual scenes (e.g. in Figure 1), and these are very useful for understanding the task. Representing this dataset using familiar modalities (e.g. vision, natural language) could enable future work to study different research questions, e.g. the impact of pre-training. The ability to alternatively represent the task input as a sequence of tokens is also reasonable for studying certain research questions, but this also seems possible for datasets from prior work. For example, I understand that gSCAN includes both symbolic descriptions as well as visual renderings. Anyways, I think clarifying the motivation for this dataset (e.g. increasing diversity of available benchmarks, focusing on different generalization challenges, etc.) separately from how inputs are represented for the experiments in this paper (e.g. token sequence vs. images and natural language) would be useful.
* Some of the main empirical conclusions (e.g. that generalization to greater "depth" is challenging for models such as Transformers) are generally known from prior work.

nits:
* Introduction paragraph 1 - "on a carefully controlled generic multimodal reasoning tasks" -> "on carefully..." or "...task"
* Appendix A.2.1 - Maybe reference Tables 8 and 9 where you discuss different positional embeddings.
* Consider discussing [3] in related work. [3] demonstrated the importance of cross-modal attention for gSCAN, and similarly studied the relative difficulty of various aspects of generalization, including distractors.

### Questions
* Why not try more layers and attention heads, e.g. following a standard hyperparameter setting for model size such as those of BERT-Base? Or even BERT-Small?
* In Figure 2 (F) why does the single-stream Transformer have almost double the parameters of the double stream Transformer? For the other Transformers, do the encoder blocks used for the task vector and stimulus vector share parameters? 
* What optimizer and hyperparameters (e.g. learning rate) were used for training? How were these chosen? I didn't see these details in Appendix A.2. 
* Position embeddings - Since you are representing 10x10 grids as 1D sequences, 1D relative positions may not capture this structure well. On the other hand, absolute position embeddings seem potentially problematic in the case of the SSTrfmr model, since they will not be consistently assigned to the same grid position if the text sequence is first and has varying length. Mitigating this may be important to provide for a fairer comparison with the SSTrfmr model.
* To what do you attribute the periodic loss spikes during training that are shown in Figure 4 (E)?
* I found the usage of "cross-attention" a bit confusing. For example, the single stream Transformer features cross-modal attention as an implicit consequence of self-attention over the concatenated sequence. I thought this would commonly be referred to as an instance of "cross-attention" between modalities. 
* Does the dataset also contain visual renderings and natural language instructions to enable future work to study these tasks using familiar modalities?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies multi-modal generalization in neural networks such as transformer-based models and recurrent networks. To do so, the authors propose Genertic COG, a modular benchmark with multi-modal splits to test for 3 types of generalization: 1) distractor (generalization to different noise distribution), 2) systemic compositional (generalization to new permutation of task structures) and 3) productive compositional (generalization to tasks of greater complexity) generalization. Experiments conducted by the authors showed that while cross-attention based transformers (e.g. CrossAttn and Perceiver) outperform other models and perform well on distractor and systemic compositional generalization, they fail at productive generalization when the depth of the task tree goes to out-of-distribution (>3). Representational analysis is done to show that cross-attention based transformers (e.g. CrossAttn and Perceiver) superior performance on distractor generalization might be due to their ability to better retain task-relevant (e.g. stimulus and response) information at the penultimate layer.

### Strengths
+The paper studies a timely and critical question about the generalization capability of multimodal transformer-based models

+The proposed benchmark dataset uncovers a limitation of current multimodal transformer-based models: productive generalization which can facilitate the development of more generalizable transformers/LLMs. 

+The paper is generally well-written and easy to follow

### Weaknesses
-While the paper’s studies show that certain designs (e.g. cross-attention) seem to confer multi-modal generalization, there are still some key questions that can be more thoroughly studied to uncover the reasons why this is the case.

-Similarly, important discussions such as why the (cross-attention) transformers might fail at productive generalization is lacking.

### Questions
What is the key architectural difference between dual stream transformer and transformers with cross attn that can explain their generalization performance? Is it only the lack of a cross attention between the different modalities?

Possible typo:
“Finally, we included a Perceiver-like model (Jaegle et al., 2021), an architecture designed to generically process multimodal inputs (Fig. 2f).”:  (Fig. 2f) > (Fig. 2e).


==Post-Rebuttal==
I appreciate the authors' response and decided to keep my score.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

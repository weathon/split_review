# Two Heads Are Better Than One: Exploiting Both Sequence and Graph Models in AMR-To-Text Generation

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 6, 5

## Abstract
Abstract meaning representation (AMR) is a special semantic representation language, which can capture the core meaning of a sentence with a syntax-irrelevant graph.
AMR-to-text generation, which aims to generate a sentence according to a given AMR graph, is a well-studied task and has shown its helpfulness in various other NLP tasks.
Existing AMR-to-text generation methods can be roughly divided into two categories, while either has its own advantages and disadvantages.
The first one adopts a sequence-to-sequence model, especially a pretrained language model (PLM). 
It has good text generation ability but cannot cope with the structural information of AMR graphs well.
The second category of method is based on graph neural networks (GNNs), whose advantages and disadvantages are exactly the opposite. 
To combine the strengths of the two kinds of models, in this paper, we propose a dual encoder-decoder model named \modelName, which integrates a specially designed GNN into a pre-trained sequence-to-sequence model.
We conduct extensive experiments as well as human evaluation and a case study,  finding that it achieves the desired effect and yields state-of-the-art performance in the AMR-to-text generation task. 
We also demonstrate that it outperforms the most powerful general-purpose PLM GPT-4.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this paper, the authors focus on the AMR-to-text generation task.  To leverage the advantages of PLMs and GNNs, the paper proposes a dual encoder-decoder model called DualGen, which integrates a specially designed GNN into a pre-trained sequence-to-sequence model. The paper presents extensive experiments, human evaluations, and a case study, showing that DualGen achieves state-of-the-art performance in AMR-to-text generation tasks and outperforms the GPT-4.

### Strengths
1. The motivation for this paper is intuitive and the description of the proposed methodology is clear and comprehensible.

2. The proposed method exhibits compatible with any encoder-decoder architecture pre-train models. 

3. The authors conduct an exhaustive comparsion, and the experimental results show the proposed method outperforms all previous work.

### Weaknesses
1. Actually, the multi-source structure (multiple encoders - one decoder) is a common approach in many NLP tasks. Even this paper does present some enhancements for the AMR-to-text generation task, the novelty of the proposed method appears to be somewhat constrained. The specific enhancements, such as the GNN architecture and its integration, lack a detailed justification regarding why this particular configuration is superior to other existing multi-encoder approaches. Without a more rigorous ablation study or theoretical analysis, it's difficult to ascertain the true contribution beyond a straightforward combination of existing techniques.

2. A commendable aspect of this paper is the authors' comparison of performance with GPT-4. However, considering that GPT-4 is a general model, the comparison may not be entirely equitable. It would be more appropriate to utilize an open-source large language model (e.g., Llama) for the experiment. This is crucial to verify the effectiveness of the proposed method in the context of Large Language Models. Furthermore, the comparison lacks a controlled setting, such as fine-tuning both the proposed model and the chosen LLM on the same AMR-to-text dataset. Without this, it's unclear if the performance differences stem from the model architecture or simply from the training data and pre-training objectives.

### Questions
N/A

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a new framework, DualGen, for AMR-to-text generation. The paper builds a new dual encoder-decoder model based on BART. Specifically, apart from the original BART sequence encoder, the paper introduces a new transformer-based graph encoder that takes in both node and edge embeddings as input. The graph attention mechanism incorporates edge embeddings into node representations. The paper then conducts experiments on both AMR 2.0 and AMR 3.0 datasets by comparing the proposed method with multiple state-of-the-art baselines. Following previous papers, the paper evaluates the results with BLEU, METEOR, and CHRF++. The paper also performs human evaluations. Additionally, the paper compared the proposed model with GOT-3.5 and GPT-4.

### Strengths
1. The paper proposes a new dual-encoder architecture, combining graph representation and linearized input. The paper also proposes a new graph attention mechanism incorporating edge embeddings into the node representations.  
2. The paper did comprehensive experiments with automatic and human evaluations on two datasets. The proposed methods surpass other state-of-the-art models in both automatic and human evaluations. In addition, the paper analyzes the relationship between graph complexity and model performance. It shows that the proposed method can capture the complexities of the graphs more effectively. The proposed method outperforms GPT4. The paper includes a case study with detailed output for readers to compare. 
3. The paper provides code, GPT4 results, silver data, etc.

### Weaknesses
1. The idea is a little bit incremental. The graph encoder is built upon Song et al., 2020. The idea of the dual encoder is also not new. For example, OntG-Bart (Sotudeh & Goharian, 2023) also uses a GNN and BART encoder-decoder framework to generate summarization. The dual encoder has also been applied to the multimodal domain (Li et al., 2021).
2. It would be better for authors to include an additional ablation study for the proposed method instead of only showing the final model. In this way, readers can have a better understanding of the contribution of each component. The analysis in section 4.5 is superficial and needs additional in-depth analysis. The authors can include additional quantitative analysis by analyzing the types of failures for each model.  
3. Some parts of the paper are not clear. The paper fails to report the inter-annotator agreement for the human evaluations. The paper also includes typos. Typo in "Metor"-> METEOR

### Questions
Could the authors elaborate on how each encoder contributes to the overall performance of the model? Would the authors consider conducting an ablation study? Specifically, it would be insightful to demonstrate that the pretrained encoder effectively handles Out-Of-Domain (OOD) test cases, while the graph encoder adeptly captures structural information.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The main contribution of the paper is to show that an ensemble of two established methods, sequence-to-sequence (s2s) and graph-to-sequence (g2s), performs better than either method by itself on two standard abstract meaning representation (AMR) benchmarks: AMR 2.0 and AMR 3.0.  The proposed ensemble method is called DualGen.

The paper shows results for a number of baselines including GPT-4.  It is interesting that the proposed method is considerably better than that on these benchmarks.

### Strengths
This paper is basically an incremental improvement over prior work (s2s and g2s).  It isn't surprising to see ensembles do well, but it is nice to see that that is the case. 

The paper shows results for a number of baselines including GPT-4.  It is interesting that the proposed method is considerably better than that on these benchmarks.

### Weaknesses
This paper is basically an incremental improvement over prior work (s2s and g2s).  It isn't surprising to see ensembles do well, but it is nice to see that that is the case.

The paper shows results for a number of baselines including GPT-4.  It is interesting that the proposed method is considerably better than that on these benchmarks.

This paper is written for an audience that is already familiar with the literature on AMR.  One would hope that the result (two heads are better than one) might generalize beyond this specific case, but there is little evidence or discussion of that.

I found the paper unnecessarily hard to read.  The lead sentence of the abstract doesn't make it clear that AMR is well-established in the literature, and many of the cited papers have hundreds/thousands of citations.

It may be useful to compare the description of the problem and the task in https://aclanthology.org/P18-1150.pdf (one of the key cited papers) with the description in this submission.  This submission does not make it as clear that AMR is an established concept in the literature.  Nor is it as clear what the task is.  The cited paper follows the standard formula where there is a section labeled "Experiments" with a subsection on materials (5.1 data).   The submission has a short section (4.1 Datasets) with references to LDC.  This made it clear that this is a standard problem in the literature. But by the time I get to the discussion of the dataset, it should be clear what the task is, and how much work there is on this task.

One would hope that the incremental improvement would be at least as good as the prior art in describing the problem and motivating it, but I found it easier to do that by reading the references than by reading this submission.

### Questions
Can you make this paper more accessible to an audience that is not already familiar with AMR?

The first part of the title (two heads are better than one) suggests that this result might generalize beyond this specific case (ensembling of s2s and g2s on two AMR benchmarks).  Is this paper limited to this specific case, or should it be of interest to a broader audience that may not be familiar with AMR?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

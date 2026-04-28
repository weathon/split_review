# Transformers meet Neural Algorithmic Reasoners

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 6, 3, 6

## Abstract
Transformers have revolutionized machine learning with their simple yet effective architecture. Pre-training Transformers on massive text datasets from the Internet has led to unmatched generalization for natural language understanding (NLU) tasks. However, such language models remain fragile when tasked with algorithmic forms of reasoning, where computations must be precise and robust. To address this limitation, we propose a novel approach that combines the Transformer's language understanding with the robustness of graph neural network (GNN)-based neural algorithmic reasoners (NARs). Such NARs proved effective as generic solvers for algorithmic tasks, when specified in graph form. To make their embeddings accessible to a Transformer, we propose a hybrid architecture with a two-phase training procedure, allowing the tokens in the language model to cross-attend to the node embeddings from the NAR. We evaluate our resulting TransNAR model on CLRS-Text, the text-based version of the CLRS-30 benchmark, and demonstrate significant gains over Transformer-only models for algorithmic reasoning, both in and out of distribution.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes combining transformers with graph neural networks (GNNs) to build enhanced neural algorithmic reasoners. The core approach involves a cross-attention module, enabling language transformers to leverage information from a pretrained GNN. Experiments on the CLRS-Text benchmark indicate that the proposed method improves both in- and out-of-distribution performance.

### Strengths
1. The TransNAR approach is well-motivated, and the core concept is clearly articulated.  

2. The method achieves competitive performance compared to a vanilla Transformer.  

3. The study explores a distilled version of the TransNAR transformer, demonstrating improved out-of-distribution robustness over a transformer trained from scratch without GNN support.

### Weaknesses
1. The novelty is somewhat limited, as combining text-based transformers with GNNs via cross-attention is well-explored in previous works, such as [1] and [2].  
[1] https://aclanthology.org/Q19-1002.pdf. Semantic Neural Machine Translation Using AMR.   
 [2] https://aclanthology.org/2020.tacl-1.2.pdf. AMR-To-Text Generation with Graph Transformer.   

2.Both Figures 4, 5 and 6 are not clear enough. I cannot clearly read them in a print version. Please consider to use at least a table to show the results. 

3. Only the Chinchilla base transformer is used in experiments. Testing with open-source pretrained LLMs like LLaMa and Mixtral could provide broader insights. 

4. Experiments are limited to a single dataset with pre-constructed input graphs, leaving questions about generalizability. Testing on automatically constructed graph datasets, which may be less accurate but useful, could strengthen the study’s applicability.

### Questions
Please refer to Point 3 and Point 4 in the weaknesses section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a transNAR architecture by having both texts and graphs as input and using cross-attention to combine the strengths of both. Systematic results on CLRS-text demonstrate significant improvements in a number of problems, even though no improvements are achieved in some of them.

### Strengths
The paper uses graphs and texts so that the new system can use the natural language inputs as well. The combination leads to significant performance improvements over the baseline systems. While the integration uses cross attention very similar to those in multimodal models, the benefits seem significant.

### Weaknesses
The paper is sketchy in covering important technical details. For example, the abstract states a two-phase training procedure is used; yet the main paper does not mention the two-phase training procedure even once. Related to this, the paper describes the system wide issues only from lines 213 to line 223 without mentioning some known issues. For example, the particular implementation of the transNAR uses 6 layers and it is well known beyond two to three layers oversmoothing becomes an issue in graph neural networks. The paper freezes the weights for graph embeddings, but multimodal models rely on a shared embedding space; the differences between the two embedding spaces should be a factor, yet there is no mention about that.

A major strength of the paper is the improvements as highlighted in Figure 1. However, the baselines do not reflect the actual state of the art. One naive way to combine NAR and transformers for CLRS-text is to use start of the art transformers to convert the problems into the graphic form required by NAR and then apply NAR. Also the transformer model used in the paper is far from the state of the art; as a baseline, the authors should use the performance of a fine-tuned state-of-the art transformer model on the CLRS-text dataset. In addition, it seems the input to the transformer model is only the text but the transNAR has dual inputs; the impact of the dual inputs should be factored in when stating the improvements.

### Questions
- Is every iteration the same as illustrated in Figure 3? It seems it is not as the final output is only from the last layer; for other layers, the outputs from both modules feed to the next layer as inputs. Could you revise Figure 3 to show the entire process accurately?

- Given that the proposed transNAR fails to improve on some of the problems, could you please comment on the limits of the NAR approach? While it can generalize over a larger range of lengths, NAR and transNAR would still lack the generalization and robustness of correct algorithms.

- Reasoning is inherently sequantial but it seems the graphs are not. Could you comment on how the graphs emulate the sequential nature of reasoning steps?

- One of the known issues with graphs is the oversmoothing issue. Could you comment how that affects the NAR and transNAR?

- While the improvements over the baseline seem impressive, could ypu give the specific contributions beyond combining NAR and transformers? It seems to me a fair comparison is to use a straightforward combination as the baseline rather than the transformers alone, whose limitations are known in this area.

- Could you provide references for transformers' natural langaue UNDERSTANDING properties? The paper mentioned that transformers have unrivaled such properties (Section 1)  and at the same time they are limited in generalization due to their autoregressive, causally-masked objective (Section 2). These two do not seem to go together well.

- Would you opens-source the code code for your transNAR and baseline models? As many of the papers are from one group due to the unfair advantages created, it is not acceptable to the research community.

- More generally, would you be committed to the principle that scientific research should be for the common good and accessible to all?

- Could you comment why you chose to call Q as Key and K as Query in equations (1) and (3)?

- How would you pronounce NAR? Please make sure it is consistent in the paper (for example in line 065 as "a NAR-" and as "an NAR" in many other places).

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a TransNAR neural architecture that is a hybrid of Transformer and Neural Algorithmic Reasoner (NAR) architectures. The Transformer part of the model is allowed to cross-attend to NAR states. The model requires a hybrid input: the Transformer part expects text and the NAR part consumes a graph. The paper tests the proposed architecture on CLRS-Text, which is a text version of an algorithmic benchmark called CLRS-30. The model is trained on both textual inputs and the corresponding graph. The paper’s main claims are that (1) TransNAR performs better than Transformer. (2) that TransNAR teacher can produce extra training data for the Transformer student, and that this data increases the generalization of the latter.

### Strengths
The paper was clear enough for me to understand the main idea. I appreciate that the paper contained a “Limitations” section.

### Weaknesses
The paper proposes a very straight-forward idea and presents unsurprising results. Of course a hybrid of a general-purpose model (transformer) and a task-specific model (NAR) will perform better on the specific task. Especially when the model requires special graph-structured data, which is the case for TransNAR. 

The distillation results were hard for me to process and verify. The error bars (constructed on just 3 samples!) are very large. An obvious baseline is missing: distilling a NAR model to Transformer.

On the writing side, the paper could benefit from the following improvements: 
- Give more context to the reader:
   - better explain CLRS-30 benchmarks
   - better explain NAR architecture
- Include a rigorous textual analysis of performance numbers (e.g." in 3 cases out of 7 our model is significantly better than the baseline (p-value = 0.01)"), in addition to presenting all numbers on all tasks in large overwhelming figures
- Include a tabular version of the results

### Questions
Did you look into how the distillation data that TransNAR produces is different from the groundtruth?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a new model architecture, TransNAR, that combines a Transformer model with a Neural Algorithmic Reasoner via a cross-attention mechanism. The motivation is to leverage the reasoning and generalization ability in NAR representation to improve the performance of the transformer model. The experiment shows promising results in the out-of-distribution regime and over 20% absolute improvement in several classes.

### Strengths
The method is straightforward and well-motivated. Experiment results also show that it performs well on the targeted tasks compared to standard transformer architecture.

### Weaknesses
The proposed method is domain-specific. It's hard to imagine how this method would benefit broader domains, as the NAR requires a specific type of input. Combining this method with existing large language models would also require further experiments. Figure 5 and 6 are hard to read.

### Questions
1. How can we combine this method with a pretrained language model? So that we can leverage the math reasoning ability in state-of-the-art language models.
2. Have you compared with using GNN-based NAR alone?
3. How does a pretrained language model perform on these tasks?

### Soundness
3

### Presentation
3

### Contribution
3

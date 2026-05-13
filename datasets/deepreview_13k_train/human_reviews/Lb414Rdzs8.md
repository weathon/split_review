# NODE-SAT: Temporal Graph Learning with Neural ODE-Guided Self-Attention

- Decision: Reject
- Scores: 3, 8, 5

## Abstract
We propose NODE-SAT, a novel temporal graph learning model that integrates Neural Ordinary Differential Equations (NODEs) with self-attention mechanisms. NODE-SAT's design requires only historical 1-hop neighbors as input and comprises three key components: a temporal link processing module utilizing NODE-guided self-attention layers to capture temporal link information, a node representation module summarizing neighbor information, and a prediction layer. Extensive experiments across thirteen temporal link prediction datasets demonstrate that NODE-SAT achieves state-of-the-art performance on most datasets with significantly faster convergence. The model demonstrates high accuracy, rapid convergence, robustness across varying dataset complexities, and strong generalization capabilities in both transductive and inductive settings in temporal link prediction. These findings highlight NODE-SAT's effectiveness in capturing node correlations and temporal link dynamics.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a temporal graph leanring algorithm that combine ODE with self attention mechanism.

### Strengths
1.  The paper is well written and easy to follow.

2. The results are pretty good.

### Weaknesses
1. The novelty of this work is not high, a mixture of self attention with neural ODE. It mainly uses some engineer effrot in my mind.

2. The results sounds too good to be true, In table 1, I saw many of the datasets can achieve 100% accuracy. Does mean that this paper almost close this area?

3. How is the complexity of this work.

### Questions
1. The novelty of this work is not high, a mixture of self attention with neural ODE. It mainly uses some engineer effrot in my mind.

2. The results sounds too good to be true, In table 1, I saw many of the datasets can achieve 100% accuracy. Does mean that this paper almost close this area?

3. How is the complexity of this work.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The NODE-SAT model introduces a novel approach to temporal graph learning by combining Neural Ordinary Differential Equations  with self-attention mechanisms. Designed for temporal link prediction, NODE-SAT captures evolving temporal relationships between nodes by modeling continuous-time dynamics. NODE-SAT achieves strong performance across multiple benchmarks.

### Strengths
**Good contribution and engineering** : The use of NODEs for modeling the continuous evolution of node representations is, to the best of my knowledge, a novel approach **in the field of temporal graph learning**. 

**Rigorous Experimental Results**: The experimental results are robust, and the authors follow a well-documented experimental pipeline that thoroughly assesses the performance improvements of NODE-SAT.

**Open-Source Code:** The release of the code is an excellent contribution, allowing for replication and further exploration of the experimental results. This transparency greatly enhances confidence in the impressive performance claims made by the authors.

### Weaknesses
 **Some choice of presentation** , the big table is difficult to read i'll suggest to put hist and ind negative sampling in supplementary. Same remark for the graphics. 

**Novelty** The core components introduced in NODE-SAT, particularly the use of Neural Ordinary Differential Equations (NODEs) for continuous-time modeling, rely on well-established methods in machine learning. While the combination of NODEs with self-attention is creative and effective for temporal graph learning, these elements themselves are not novel. Neural ODEs have been widely used for modeling continuous dynamics in various applications, and self-attention is a standard technique for capturing complex relationships in structured data. As such, the innovation here is more about the application of these established techniques rather than the introduction of fundamentally new methods. The paper would benefit from a more detailed discussion of how the specific combination of NODE and self-attention addresses the unique challenges of temporal graph learning, beyond simply stating that it is a synergistic application. For example, what specific limitations of existing temporal graph models are overcome by this particular combination, and how does the continuous-time modeling of NODE interact with the attention mechanism to capture temporal dependencies more effectively than alternatives?

### Questions
1. Impact of Multi-Hop Neighbors: What would be the effect on performance if the model used multi-hop neighbors instead of only 1-hop neighbors? Would incorporating multi-hop information further improve the model's ability to capture long-range temporal dependencies, or would it increase complexity without significant performance gains?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper is about temporal graph learning, which is an interesting topic. The authors propose a novel temporal graph learning model that integrates Neural Ordinary Differential Equations (NODEs) with self-attention mechanisms. The paper is well written and well organized. However, there are several concerns in the current version of the paper that addressing them will increase the quality of this paper

### Strengths
1 Cutting-edge research directions.

2 Leading experimental results.

### Weaknesses
1 Authors should provide more research background in the abstract and introduction to help non-field readers better understand the paper.

2 The modules used by the authors in the model design seem to have been proposed by previous methods, but they are simply combined. Are there any new concepts or technologies proposed by the authors? At present, it is impossible to understand the challenges that the paper attempts to solve and the core contributions.

3 The authors should provide a more complete introduction to the dataset used, such as its size.

4 Through experiments, we can find that the method proposed in the paper has obvious improvements on some data sets. Perhaps the author has indeed done a commendable job, but the narrative is not good enough to capture the highlights.

5 The layout and structure of the entire paper could use considerable improvement, making it seem like a work in progress rather than a finished work.

### Questions
In the method section, did the author omit the introduction of the loss function?

### Soundness
2

### Presentation
1

### Contribution
2

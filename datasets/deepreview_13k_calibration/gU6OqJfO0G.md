# ON LEARNABILITY AND EXPERIENCE REPLAY METHODS FOR GRAPH INCREMENTAL LEARNING ON EVOLVING GRAPHS

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 3, 6, 5

## Abstract
Recent research has witnessed a surge in the exploration of Node-wise Graph Incremental Learning (NGIL) due to its substantial practical relevance. A central challenge in NGIL stems from the structural shifts induced by the inherent interdependence among vertices within graph data, adding complexity to the task of maintaining consistent model performance over time. Although several efforts have been made to devise incremental learning methods for NGIL, they have overlooked a fundamental question concerning the learnability of NGIL—whether there always exists a learning algorithm capable of consistently producing a model with a small error from the hypothesis.  In this paper, we present the first theoretical study on the learnability of the NGIL problem with the statistical learning framework. Our analysis uncovers a critical insight: NGIL is not always learnable when structural shifts are uncontrolled. Additionally, in order to control structural shift, we leverage the idea of experience reply which selects a small set of representative data to replay with the new tasks, and propose a novel experience replay method, Structure-Evolution-Aware Experience Replay (SEA-ER). SEA-ER comprises a novel experience sample selection strategy founded on the topological awareness of GNNs and a novel replay objective utilizing importance re-weighting, which can effectively counteract catastrophic forgetting and mitigate the effect of structural shifts in NGIL. Comprehensive experiments validate our theoretical results and showcase the effectiveness of our newly proposed experience replay approach.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper is about incremental learning of graphs where increment happens in terms of nodes. They propose a plan to solve catastrophic forgetting in incremental learning. The idea is to subsample from historic evidence and reuse them as replay. The paper also provides theoretical analysis of the method.

### Strengths
1. Learning from graph in incremental setup is an important problem. 
2. The idea of reusing older samples as revision seems ok.
3. The authors have provided some theoretical analysis too.

### Weaknesses
1. The paper is written with unnecessary formalism in some cases which makes it harder to read. 
2. The main idea and the rational could have been presented in a more straightforward manner.

3. However the main concern is using some samples again and again. Although it may appear to be replay or revision but it has to be critically analysed how revisiting some samples is justified. 
4. It is not clear if there is some unlearning and relearning effect is there or not. 
5. It is also not clear how such replays deviate the overall learning objective. 
6. How does the objective or the learning path change with respect to the order of increments of the graphs ? 
7. How does the final solution change if all increments are available at the same time ?

### Questions
Please refer to the weakness part.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper focuses on the challenges posed by Graph Incremental Learning (GIL), particularly within the context of Node-wise Graph Incremental Learning (NGIL). Traditional Graph Neural Networks (GNNs) are typically modeled for static graphs. However, many real-life networks, such as citation and financial networks, are dynamic, evolving over time. This dynamic nature results in challenges like catastrophic forgetting, where newly acquired knowledge supersedes prior learning. The paper delves deeply into the learnability of NGIL, where tasks are sequential, and the graph structure changes with each new task, giving rise to what is termed a "structural shift." Experimental results from various datasets showcase the efficacy of the proposed method.

### Strengths
S1. The study is well-motivated, with a comprehensive review of related work.
S2. The paper's content is easy to understand and follow.
S3. Experiments conducted on real-world datasets demonstrate the effectiveness of the methods proposed.

### Weaknesses
W1. The problem setting is not novel. My first concern is the novelty of the problem setting. Node-wise Graph Incremental Learning has been extensively studied by previous works

W2. The technical contributions, while sound, seem limited. The method presented integrates an experience buffer and importance re-weighting to tackle challenges such as catastrophic forgetting and structural shifts. However, using an experience buffer for stream data isn't a new concept, and many works have already explored it. The reviewer finds the technical contributions of this section somewhat limited.

W3. The theoretical innovation appears to be minimal. Once the input graph is broken down into a series of ego-graphs, the definitions, formulations, and theoretical underpinnings seem like straightforward adaptations from their IID data counterparts.

W4. The writing requires refinement:
The use of "bf" before "Node-wise Graph Incremental Learning" appears to be a formatting mistake.
The definition of distortion, as presented in Definition ??, is incomplete or missing.

W5. Lack of   time complexity analysis. it would be beneficial to compare the overall time complexity of the entire framework to that of the baselines and to provide insights into the runtime of the proposed method.

### Questions
See the above

### Soundness
2 fair

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents a theoretical examination of the learnability of Node-wise Graph Incremental Learning (NGIL) in dynamical settings. Specifically, the paper presents that NGIL is not always learnable under uncontrolled structural changes. 
Based on this analysis, the paper presents a technique, the Structure-Evolution-Aware Experience Replay (SEA-ER) 
to control structural shifts with a sample selection that uses topological information of the GNN with importance re-weighting. 
In the experiments, three real-world datasets and synthetic data are used to evaluate the proposed method (SEA-ER) and compare it to existing experience replay NGIL frameworks. It evaluates the impact of structural shift (dynamics of graph structure) and that the distortion rate is small for the datasets. Finally, the paper also presents a meta-analysis of the model with the corresponding ablation study on the size of the experience replay buffer.

### Strengths
This paper has several strong points. The NGIL learnability problem presents an interesting re-interpretation of the effect of cyclic probabilistic dependencies of nodes and node attributes in an evolving graph. Creating a formulation that is relatively agnostic to the mechanics of how those probabilities were produced is interesting. Theorem 2.3 is the main theoretical contribution of the paper and has some intuitive components to it, particularly concerning the fact that the impossibility of learning unconstrained dynamics.  However, this is in itself a subtle line, since the probabilistic causes for this are not fully described in the paper. Other strengths of the paper include its organization (although the clarity could be improved) and the meta-analysis.

### Weaknesses
The main weakness of this paper is that central to the argument is the content of Theorem 2.3. I have my reservations about this result not because it may not be true (I think is true) but because this result could be traced back to the cyclic dependencies of the node probabilities that are ultimately the contributors to the structural shift. However, this is not indicated in the paper. The paper also has several imprecisions in the descriptions for example, the metric $r_{i,j}$ is only briefly indicated to be accuracy in the "Evaluation Metric" subsection between parentheses with a "e.g." before stating it. Thus, it reads like an example and not a definitive fact. However, this is not fully confirmed later in the paper. The choice of accuracy as a metric, itself could be considered a little problematic for the problem at hand. A graph is a sparse topological mathematical entity and accuracy alone may not be the most appropriate for the task. Finally, since Theorem 2.3 is the core of the contribution the proof cannot be relegated to the appendix.

Minor comment. The caption for the Figure in page 8 is missing.

### Questions
I would appreciate if you could clarify the points I raised in the weakness section above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors study the problem of graph incremental learning, where (a batch of) nodes arrive at each time step. We hope to update our model efficiently in this setting as in the standard incremental or online learning setting. The authors claim that this problem is not ``learnable`` when the structural shift is not controlled. They propose a replay-based method to mitigate the effect of structural shift.

### Strengths
-	The studied problem is important.
-	The extensive experiments show that the proposed method outperforms prior works.

### Weaknesses
 - The clarity, especially for the theoretical results, can be improved.
- The Theorem 2.3 seems problematic. See the counter-example below.
- It is not clear why the proposed method can mitigate the issue of ``structural shift``.

I really like to convey ideas and it is great to see the authors attempt to provide some analysis to understand the problem of Node-wise Graph Incremental Learning (NGIL). However, I find it hard to understand the impossibility result of NGIL and why the proposed method can solve the issue. For instance, what do the authors mean by a **good** classifier $f$ in Theorem 2.3? What is exactly the setting of available training data information we can use at each time step considered in Theorem 2.3? Clearly, it has to rule out the case of retraining from scratch (denoted as Joint Training by the authors) otherwise Theorem 2.3 makes no sense. Unfortunately, I cannot see where and how Theorem 2.3 rules out this method. Also, the authors assume that we can sample the $k$-hop ego-subgraph for all nodes in $\mathcal{V}_i$ at each time step $i$. Notably, the statement of Theorem 2.3 is independent of the choice of $k$. As a result, if we set $k$ sufficiently large, then getting $g_v$ is equivalent to getting the entire graph. Thus, retraining from scratch is included in this scenario. I feel there must be some other assumption in order to make Theorem 2.3 reasonable, and I hope the authors can state them clearly. 

On the other hand, even if the conclusion of Theorem 2.3 is correct the main issue is the structural shift being uncontrolled. The authors claim that their method can mitigate this issue, which sounds weird to me. Note that the structural shift is defined by how a new node (or batch of nodes) is added to the current graph, which changes the graph topology. This is definitely not controllable in practice, as this process depends on the nature of the data but not the algorithm design. I am confused as to why the authors can claim that their method mitigates this issue.

Finally, I wonder how the problem of NGIL is related to graph unlearning [1,2]. If we do not care about the privacy issue in the graph unlearning, essentially NGIL is the reverse direction of graph unlearning. Then for a simple problem and model, the technique in [1,2] seem also provably applicable. I wonder if Theorem 2.3 contradicts the finding of the machine unlearning literature.

### Questions
Please check my comments in the weaknesses section. In summary, my questions are:

1.	What does ``good $f$`` mean in Theorem 2.3?

2.	Why Theorem 2.3 is correct? Isn’t retraining from scratch a counter-example?

3.	Since Theorem 2.3 does not depend on the number of hop $k$. If we choose $k$ sufficiently large (i.e., larger than the diameter of the graph), then essentially getting $g_v$ means we get the entire graph, and thus retraining from scratch must be included. Do the authors miss some assumptions for Theorem 2.3 to hold?

4.	Why the proposed method can mitigate the structural shift? Isn’t this dependent on the data nature that we have no way to control?

5. Does Theorem 2.3 contradict with graph unlearning literature [1,2]?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

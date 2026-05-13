# Graph Neural Network Is A Mean Field Game

- Decision: Reject
- Scores: 5, 5, 6

## Abstract
In current graph neural networks (GNNs), it is a common practice to apply a pre-defined message passing heuristics to all graph data, even though the stereotypical relational inductive bias (e.g., graph heat diffusion) might not fit the unseen graph topology. Such gross simplification might be responsible for the lack of an in-depth understanding of graph learning principles, which challenges us to push the boundary from crafting application-specific GNNs to embracing a "meta-learning" paradigm. In this work, we ratchet the gear of GNN another notch forward by formulating GNN as a *mean field game*, that is, the best learning outcome occurs at the *Nash*-equilibrium when the learned graph inference rationale allows each graph node to find what is the best feature representations for not only the individual node but also the entire graph. Following this spirit, we formulate the search for novel GNN mechanism into a variational framework of *mean-field control* (MFC) problem, where the optimal relational inductive bias is essentially the critical point of mean-field information dynamics. Specifically, we seek for the best characteristic MFC functions of transportation mobility (controlling information exchange throughout the graph) and reaction mobility (controlling feature representation learning on each node), on the fly, that uncover the most suitable learning mechanism for a GNN instance by solving an MFC variational problem through the lens of *Hamiltonian flows* (formed in partial differential equations). In this context, our variational framework brings together existing GNN models into various mean-field games with distinct equilibrium states, each characterized by a unique MFC functional. Furthermore, we present an agnostic end-to-end deep model, coined *Nash-GNN* (in honor of Nobel laureate Dr. John Nash), to jointly carve the nature of the inductive bias and fine-tune the GNN hyper-parameters on top of the elucidated learning mechanism. *Nash-GNN* has achieved SOTA performance on diverse graph data including popular benchmark datasets and human connectomes. More importantly, the mathematical insight of mean-field games provides a new window to understand the foundational principles of graph learning as an interactive dynamical system, which allows us to reshape the idea of designing next-generation GNN models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a variational framework for abstract learning in Graph Neural Networks (GNNs) from a mean-field control perspective. The authors demonstrate that several existing GNN architectures can be viewed as specific instances within this framework, differing in their choice of diffusion and reaction functions. Building upon this framework, they design an end-to-end deep learning architecture that characterizes information propagation in GNNs. Experimental results on benchmark graph datasets show that the proposed framework significantly outperforms GNN baselines in both node and graph classification tasks.

### Strengths
1. The paper is clear and easy to follow.

2. The proposed framework is interesting, and several existing graph neural diffusion architectures fit into this framework, even though viewing GNNs as dynamic systems has been studied in the literature (e.g., [1]).

3. The experimental results on OGBN and TUDatasets demonstrate that the proposed model significantly outperforms several GNN baselines.

### Weaknesses
1. While the proposed framework is intriguing, it does not address several important challenges such as over-smoothing, over-squashing, and the ability to capture long-range dependencies in graphs. Specifically, the framework lacks explicit mechanisms to control the depth of information propagation, which is crucial for mitigating over-smoothing. The reliance on a mean-field approximation might also limit its ability to capture long-range dependencies effectively, as it primarily focuses on local interactions. As a result, it is unclear whether the framework can mitigate these problems.

2. Some of the datasets used in the experiments are either relatively small (e.g., Texas, Wisconsin, and Cornell, which have only several hundred nodes) or problematic. For instance, as highlighted in Section 3.1 of [2], the Chameleon and Squirrel datasets reportedly contain repeated nodes, casting doubt on their reliability for fair and robust model testing. This raises concerns about the generalizability of the results to larger and more complex graphs.

3. It would be good to clarify the conditions required for the optimization problem in Eq. (6) to be well-posed, i.e., to have a unique solution. Moreover, when Eq. (6) is non-convex, how does converging to a local minimum influence the model's predictive performance? The paper should discuss the implications of using non-convex optimization and how it might affect the stability and reliability of the learned parameters.

### Questions
1. Under what scenarios would non-linear diffusion and reaction functions be superior to linear functions, and vice versa? Could you provide some insights on this?

2. Could you conduct evaluations on the filtered versions of the Chameleon and Squirrel datasets, as well as on new heterophilic datasets provided by Platonov et al. [2]?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The work formulates GNNs as a mean field game. My understanding is that the goal is to find a good trade off between information exchange (what the authors call transportation mobility) across the graph and possibly the sharpness of the features (what the authors call reaction mobility). The authors propose Nash-GNN to achieve this.

### Strengths
The authors present an interesting perspective on learning on graphs. I believe that there seem to be some fundamentally novel and interesting ideas within the work.

I liked Table 1 that acts as a unification between different existing variations types of methods that exist in the GNN literature. Overall I think that sections 2.1, 2.2, and 2.3 have a lot of potential, but they need to be better presented.

### Weaknesses
I found the paper to be very hard to understand, even though I’m familiar with many of the related works. I think the language in many cases is quite confusing and overall the paper lacks clarity.  

As an example in the abstract the authors write “to jointly carve the nature of the inductive bias and fine-tune the GNN hyper-parameters on top of the elucidated learning mechanisms”. Phrases like this seem scattered throughout the work, which in my opinion are very hard to understand and make the paper challenging to read. There seems to be an overall distinct lack of clarity in the work. 

Figure 1 is quite non-standard presenting a rather imprecise analogy. 

Figure 2 is quite confusing and dense, it might be worth swapping Figure 2 with algorithm 1 in the appendix as that to me is much more clear.

Figure 3 is quite confusing, the caption needs more information. 

I found Table 5 to be misleading as Nash-GNN has results in bold for 100% for the TaoWu, PPMI, and Neurocon datasets when many techniques seem to achieve 100% (so at the very least they should be coloured in bold as well). 

Many terms are poorly defined such as “transportation mobility” and “reaction mobility”, It would be quite important in my opinion to change these terms to make them more digestible for someone working in the field of GNNs.

### Questions
Please see weaknesses. 

Overall, I believe that the ideas contained in the paper are interesting and worthy of a paper, but the presentation unfortunately detracts significantly from the readability of the work. My recommendation is that the authors take time to re-write the paper in order to make the main message much more clear. I am however keen to read the opinions of the other reviewers to see if I have missed something.

To me it was also unclear exactly how Nash-GNN differs from for example GRAND. It would be useful to compare the models more concretely, I.e. I think that Nash-GNN should appear in Table 1 to make it more clear what the difference is.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The authors propose a new framework, that investigates GNNs from the perspective of mean field theory. Within this framework, they propose a new model architecture called NashGNN, which is reported to achieve better than state of the art performance on node and graph classification on  several benchmark datasets.

### Strengths
1) The proposed algorithm surpasses the state of the art. 

2) The framework is novel.

3) The authors made extensive experiments.

### Weaknesses
1) The paper appears not to be written for the ML/GNN community.

a) The introduction is rather long and covers GNN downsides, that are not mentioned in the rest of the paper.

b) I believe the motivation is that the proposed framework can offer a solution for all learning tasks an data sets, but this motivation (or any other) is not given precisely enough in the introduction.

c) The concept of mean field theory and why it can be used for GNNs is not well explained for reader with ML background.

d) Some important information can only be found in the appendix or footnotes: the pseudo code is in the appendix, the eq that tells me how the graph topology is used in the model is in footnote 2, the explanation for Def 1 is in the appendix, model limitations are briefly mentioned in the appendix

2) The authors claim in the intro, that state of the art performance is not well suited for the underlying graph problem (p2., line 89-97) but evaluate their algorithm comparing it to state of the art.

3) The authors claim to be the first to propose a graph meta-learning method (p. 7, line 330), but I found several other papers, for example: https://dl.acm.org/doi/abs/10.1145/3357384.3358106  and https://ieeexplore.ieee.org/abstract/document/9772740

4) The GIN model is missing in the benchmark algorithms.

5) The read thread can be improved.

6) There is no comprehensive state of the art section.

7) Figure 1 does not really help in understanding the method and figure 3 is confusing.

### Questions
a) Can you please explain, where exactly the graph structure is used in the model, is it only as specified in footnote 2?

b) I would suggest shortening the intro and making it more concise.  Specifically, you can shorten the part on GNN downsides but make the motivation more clear. Why do you regard the node feature vectors as potential energy?

c) I believe an introductory paragraph on mean field theory as well as, short explanatory sentences instead of remarks would improve the red thread.

d) Can you please clarify or elaborate on what you meant with the sentence I mentioned under weakness 2?

e) Can you please elaborate on your claim I mentioned in weakness 3? I believe for meta learning you should have experiments, where you actually learned on one task and can still predict in another.

f) Can you please compare your model also to the GIN model, since it is maximally expressive.

g) The discussion on page 10 seams to draw very strong conclusions regarding neuro-degenerative diseases. Please either provide more supporting investigations or formulate less strongly.

### Soundness
3

### Presentation
2

### Contribution
4

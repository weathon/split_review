# Graph Neural Networks Gone Hogwild

- Decision: Reject
- Scores: 6, 5, 3, 3

## Abstract
Message passing graph neural networks (GNNs) would appear to be powerful tools to learn distributed algorithms via gradient descent, but generate catastrophically incorrect predictions when nodes update asynchronously during inference.
  This failure under asynchrony effectively excludes these architectures from many potential applications, such as learning local communication policies between resource-constrained agents in, e.g., robotic swarms or sensor networks.
  In this work we explore why this failure occurs in common GNN architectures, and identify ``implicitly-defined'' GNNs as a class of architectures which is provably robust to partially asynchronous ``hogwild'' inference, adapting convergence guarantees from work in asynchronous and distributed optimization, e.g., \citet{bertsekas1982distributed, hogwild}. 
  We then propose a novel implicitly-defined GNN architecture, which we call an \emph{energy GNN}. We show that this architecture outperforms other GNNs from this class on a variety of synthetic tasks inspired by multi-agent systems, and achieves competitive performance on real-world datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper develops energy GNN, a novel architecture for distributed GNN inference with asynchronous communication which can be applied to robotics, remote sensing, and other domains. Most existing GNN architecture cannot handle this problem. Energy GNN leverages input-convex GNN to ensure convergence.

### Strengths
- This paper explains the related works and background in details, and the proposed method is well-motivated.
- The research problem studied in this has some practical applications but was seldom studied before.
- The proposed algorithm is interesting and intriguing.
- Experimental evaluation shows that Energy GNN works well on the synthetic datasets.

### Weaknesses
 - The experiments are not sufficient.

  - The convergence curves of Energy GNN are not reported.

  - The efficiency and time complexity of Energy GNN are not reported.

- The accuracy performance is relatively worse than GCN on real-world datasets (e.g., PPI and MUTAG).

### Questions
- What's the performance of GCN (async) on real-world datasets?

- Is $\tau_i^j(t)$ in Equation 8 a staleness bound? If yes, how to set this term in your evaluation? What's the effect of changing this term?

- It would be great if the authors can provide a similar histogram in Figure 1(d) for Energy GNN.

- Some reference links in the supplementary material are broken.

- The citation format is not consistent. Some first names are abbreviated (e.g., A Bojanczyk) but some are not.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
One major issue in running graph neural networks (GNN), at inference time, in a distributed fashion is that GNNs require synchronous communication between layers of the graph, but distributed execution is asynchronous which means communications between nodes in a GNN are done at different times or can have stale communications. This can lead to the GNN inference failing. However, some types of GNNs can handle asynchronous execution which are termed “Hogwild” GNNs. This paper introduces a ‘hogwild’ GNN architecture termed “energy GNN” which views message passing (communication) between nodes as a convex optimization problem during training and, as a result, can run asynchronously during inference, in addition to having good performance compared to modern GNN architectures.

### Strengths
•	Good introduction that clearly explains the problem and good grammar throughout the paper.
•	Comprehensive experimental evaluation done on multiple datasets.

### Weaknesses
•	Some GNN related terminology is difficult to follow, due to not having explicit definitions. For example, Finite depth GNN, contractive (in context of GNNs), and energy function have no explicit definition. Implicit GNN and fixed point GNN seem to be used interchangeably. IGNN is first used in the evaluation section without being defined, (is it referring to Implicit GNNs?).
•	Section 4 last paragraph difficult to understand.
•	Paper is math-heavy in several sections. 
•	Many references to appendix, which is not visible.

•	In Section 4, the last paragraph which explains the advantages of a fixed-point GNN over finite depth GNNs, it is unclear what the benefit is, due to insufficient explanation. For example, what do “change its output in response to changes in the inputs” and “coordinating another forward pass of the network” mean, and why is it important for GNNs?

•	The experiments section is easy to follow, since each experiment and its results are explained clearly. In addition, several different datasets used for experiments, which makes the benefits of the proposed architecture stand out. However, only a total of 3 GNN architectures are tested. Having more architectures or explaining why the chosen architectures are sufficient would be good to include. Furthermore, in all experiments we see the proposed energy GNN performs best, but is this always the case and could there be cases where energy GNN fails to perform well?

•	Lastly, the paper is also math-heavy in several sections, which makes it difficult to follow for readers unfamiliar with GNNs. Perhaps some figures could be used to supplement the math sections.

### Questions
One issue in this paper is that it uses terminology which is not explicitly defined (if such terminology is commonly known in the target audience, this may not be big issue). For example, Finite depth GNN, contractive (in context of GNNs), and energy function have no explicit definition. Implicit GNN and fixed point GNN seem to be used interchangeably. IGNN is first used in the evaluation section without being defined, (is it referring to Implicit GNNs?).

In Section 4, the last paragraph which explains the advantages of a fixed-point GNN over finite depth GNNs, it is unclear what the benefit is, due to insufficient explanation. For example, what do “change its output in response to changes in the inputs” and “coordinating another forward pass of the network” mean, and why is it important for GNNs?

The experiments section is easy to follow, since each experiment and its results are explained clearly. In addition, several different datasets used for experiments, which makes the benefits of the proposed architecture stand out. However, only a total of 3 GNN architectures are tested. Having more architectures or explaining why the chosen architectures are sufficient would be good to include. Furthermore, in all experiments we see the proposed energy GNN performs best, but is this always the case and could there be cases where energy GNN fails to perform well?

Lastly, the paper is also math-heavy in several sections, which makes it difficult to follow for readers unfamiliar with GNNs. Perhaps some figures could be used to supplement the math sections.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper considers the problem of distributed inference of GNNs. The authors focus on partial asynchronism, which bounds the time between updates across each node and the the amount of data that can be outdated at each node. They then present how GNN inference is performed under the partial asynchronism. Finally they propose an architecture, called Energy GNN in which node embeddings are computed by minimizing an energy function which is amenable to partially asynchronous inference.

### Strengths
The problem of distributed executions in the context of GNNs is interesting.

### Weaknesses
I think the paper only considers distributed inference, but does not deal with distributed training. I am not sure I understand why one would want only the inference to be distributed if the training is not. More precisely, if the graphs are so large that inference needs to be distributed, how was the model even trained?

The paper is hard to follow and tends to lack clarity. The appendix is confusing and it contains broken pointers (see the number of "??") thus I did not find it useful in understanding the paper better. Also what is the meaning of the "*" in the tables?

The experimental section is limited and tends to be not very clear. I think it should explore much larger graphs having millions of nodes, and certainly not those having 100 nodes that can be easily ran by standard non-distributed GNNs. For example, what about the ogb MAG240M dataset?


### Questions
1. Please evaluate on large scale datasets, e.g., MAG240M, where distributed executions are needed.
2. Why some entries of the tables have the std while some others have not?

### Soundness
1 poor

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors study the execution of graph neural network under asynchrony. This is claimed to be advantageous for executing GNNs on very large graphs or efficiently simulating a group of agents with limited communication. Specifically, the partial asynchronism model of execution is used, where the the authors propose a new architecture: Energy GNN. EGNN is an Implicit GNN with appropriate input-convex networks, for which the author can guarantee convergence of the EGNN under partial asynchronism (with appropriate step size). Moreover, the proposed method is empirically tested on a variety of synthetic and real world tasks.

### Strengths
The main idea of studying GNNs under a different perspective than the common synchronous message passing, in this case, the partial asynchrous execution model is both novel and interesting.  

The theoretical analysis and the needed mathematical tools to properly connect the existing insights to graph neural networks are non-trivial and interesting contributions.

### Weaknesses
I do not see sufficient evidence to support the main claim of the paper for the mentioned use cases of more efficient execution on larger graphs. In its current form, there are no runtime measures, nor any comparisons where asynchronous EGNN is better (i.e. number of executed steps). 

The experimental section should be improved. The choice of baselines against which EGNN is compared to can be improved. Furthermore, it is not exactly clear to me why it is these synthetic tasks the authors focus on - they are mainly long range communication tasks, which I find interesting, but are not in the spirit or in alignment with the main claims of the paper. Moreover, if the focus is more on the long range communication ability, I believe there should be other baselines (from the MPNNs) other than a 2 layer GCN.

Presentation of the paper could be improved. This not as big of a concern as the two points mentioned above and I believe to be (easily) fixable as they are not conceptual issues.

Regarding the performance of synchronous GNNs which are executed asynchronously: I can see that the error can become arbitrarily large (as the synchronous assumption is violated). Are there other methods which could make them more robust? Could you already train them using the outlined schedule in Appendix A.5 (or dropout?) or use something similar to the original Scarselli work to encourage a contraction operation that converges? Especially a baseline similar to the Scarselli work I believe to be very important for your comparisons - this would support the claim that these models are too simple. 

What about other MPNN baselines beyond the 2 layer GCN (which of course can learn to solve the tasks)? Do regular MPNNs which could learn the task correctly (and do so) also have the same performance drop?

If long range communication should be more of a main feature of the presented architecture I would recommend comparison against other baselines which also focus on this, i.e. by building deeper GNNs (or even graph transformers)

How long do the implicit GNNs and the EGNN run in practice? How deep are the “infinite depth” gnns in practice?

I was not quite able to follow the task setup for 6.3. I think a precise formulation of the problem using mathematical notation would help to clarify the task and training objective (can also be included in the Appendix).

If the main claim of the work is regarding improved performance on larger graphs when execution can be asynchronous I would expect at least some real world measurements or an otherwise adequate comparison (maybe number of node activations, or rounds per node) to further support the statement.

Related to the previous point, in Figure 2 of the Appendix: (i) what exactly is the dataset loss? And I interpret the plot that you need 2k updates per node in a graph of size 10 to reach convergence during inference? Do I understand this correctly and if this is the case, how is this more efficient than a 10 layer synchronous GNN?

In the real world dataset experiments EGNN performs worse than IGNN. Especially for PPI, EGNN only reaches performance similar to a 2 layer GCN, whereas EGNN is almost perfect. A performance loss, which comes at the benefit of execution speed would be ok or in some cases even desired. I would appreciate at least a comment or hypothesis on why the performance does not translate. Also I would suggest keeping the notation consistent and report the number of layers for all models in the tables.

The insight that EGNN still converges (with the right step size) seems like the main contribution of your work and I would suggest highlighting this more (in the main part).

The required step size is in O(1/nb) (which seems quite small). Could you provide an intuition on why this has to be dependent on n, to me this is not obvious (I would have thought maybe a graph parameter such as the node degree might be necessary?)

The results provided in the main part of the paper are only on individual modes and not reported as the mean over multiple runs if I understand correctly? I see that it might not be straightforward, as you also need to avg. over the used schedule - but I would appreciate it if the results would be averaged over multiple learned models.

What is the limiting factor of scaling to larger graphs? Could you go beyond the size of 100 nodes used in the paper, what are the tradeoffs?

Are the models trained on the same graph sizes that they are run on during inference? Or do you only train on one and then generalize across sizes for the synthetic tasks? 

Additional Feedback:
I know that some of these comments are just personal preference, feel free to dismiss the comments that concern presentation style if you disagree.
In the related work section, I would encourage to include the work on asynchronous GNNs (rather than the focus on distr. training which is not that close to the presented ideas). This includes the work of Faber et al. and Dudzik et al 
I would suggest to move the first two paragraphs before 3.1 and the GCN formulation in your notation to the Appendix. Instead, I would try to include A1, which actually outlines the specific assumptions of partial asynchronism. 
The update of (9) should consider multisets instead of just regular sets right?
It is a bit weird to have all the def. on node levels but then (6) on graph level
Section title 4 is a bit long, also title A4 is almost a paragraph in itself.
I have trouble understanding the definition of $\tau^i_j$, shouldn’t it be the last updated timestep rather than the amount by which the embedding is outdated (this in my understanding is the quantity $s_{ij}$)
In Section 4 adaptivity to dynamic inputs is mentioned (as a feature of the framework) but no further evidence is provided. I rewrite to make it more clear that this could be an application but should be further investigated as future work (as is done in the conclusion).
A5 Appendix; nodes never deviate by more than one, i.e. which means regular updates. Is this correct? In my understanding this ensures that the total work of all nodes is similar B=20 ensures (somewhat) regular updates
The sampling notation in A5 is a bit weird - but this might be due to my confusion about the role of $tau^i_j$ which makes it hard for me to verify the correctness of the shown procedure.
In the Appendix layer sizes are noted as 4,4,1 - this seems quite small, is there a particular reason for this limitation?
In the Appendix multiple references are broken, where a ? shows instead.
In Section 5 you mention that prior work unifies the objective oriented view. But then you continue with saying that there is no reason to restrict - so what is a unifying or restricting view? I believe this to be mostly a formulation issue.
How would you like to capitalise during the paper, in the main text energy GNN is used but then in the Appendix it is Energy GNN. I would recommend keeping it consistent throughout. 
In Section 5, how does the energy function enable robustness? Isn’t this a property of the implicit GNNs and not limited to EGNN?
I did not follow the statement “not necessarily convex with respect to the features”, but the node embeddings, but usually the initial node embeddings are the features? I also think it would be good to make explicit where the convexity is required (in the final convergence proof I assume, following the original proof).
In A.2 there is an additional + on the third line of the proof
The proof of the main insight could be improved for presentation: restating the original theorem, showing the individual assumptions (the second condition where the Ks are set is not immediately obvious), is this why e_i is defined this specific way?
Do you have any intuition on why IGNN is first stable, but then diverges for larger graphs?

### Questions
Regarding the performance of synchronous GNNs which are executed asynchronously: I can see that the error can become arbitrarily large (as the synchronous assumption is violated). Are there other methods which could make them more robust? Could you already train them using the outlined schedule in Appendix A.5 (or dropout?) or use something similar to the original Scarselli work to encourage a contraction operation that converges? Especially a baseline similar to the Scarselli work I believe to be very important for your comparisons - this would support the claim that these models are too simple. 

What about other MPNN baselines beyond the 2 layer GCN (which of course can learn to solve the tasks)? Do regular MPNNs which could learn the task correctly (and do so) also have the same performance drop?

If long range communication should be more of a main feature of the presented architecture I would recommend comparison against other baselines which also focus on this, i.e. by building deeper GNNs (or even graph transformers)

How long do the implicit GNNs and the EGNN run in practice? How deep are the “infinite depth” gnns in practice?

I was not quite able to follow the task setup for 6.3. I think a precise formulation of the problem using mathematical notation would help to clarify the task and training objective (can also be included in the Appendix).

If the main claim of the work is regarding improved performance on larger graphs when execution can be asynchronous I would expect at least some real world measurements or an otherwise adequate comparison (maybe number of node activations, or rounds per node) to further support the statement.

Related to the previous point, in Figure 2 of the Appendix: (i) what exactly is the dataset loss? And I interpret the plot that you need 2k updates per node in a graph of size 10 to reach convergence during inference? Do I understand this correctly and if this is the case, how is this more efficient than a 10 layer synchronous GNN?

In the real world dataset experiments EGNN performs worse than IGNN. Especially for PPI, EGNN only reaches performance similar to a 2 layer GCN, whereas EGNN is almost perfect. A performance loss, which comes at the benefit of execution speed would be ok or in some cases even desired. I would appreciate at least a comment or hypothesis on why the performance does not translate. Also I would suggest keeping the notation consistent and report the number of layers for all models in the tables.

The insight that EGNN still converges (with the right step size) seems like the main contribution of your work and I would suggest highlighting this more (in the main part).

The required step size is in O(1/nb) (which seems quite small). Could you provide an intuition on why this has to be dependent on n, to me this is not obvious (I would have thought maybe a graph parameter such as the node degree might be necessary?)

The results provided in the main part of the paper are only on individual modes and not reported as the mean over multiple runs if I understand correctly? I see that it might not be straightforward, as you also need to avg. over the used schedule - but I would appreciate it if the results would be averaged over multiple learned models.

What is the limiting factor of scaling to larger graphs? Could you go beyond the size of 100 nodes used in the paper, what are the tradeoffs?

Are the models trained on the same graph sizes that they are run on during inference? Or do you only train on one and then generalize across sizes for the synthetic tasks? 

Additional Feedback:
I know that some of these comments are just personal preference, feel free to dismiss the comments that concern presentation style if you disagree.
In the related work section, I would encourage to include the work on asynchronous GNNs (rather than the focus on distr. training which is not that close to the presented ideas). This includes the work of Faber et al. (https://arxiv.org/abs/2205.12245) and Dudzik et al (https://arxiv.org/abs/2306.15632)
I would suggest to move the first two paragraphs before 3.1 and the GCN formulation in your notation to the Appendix. Instead, I would try to include A1, which actually outlines the specific assumptions of partial asynchronism. 
The update of (9) should consider multisets instead of just regular sets right?
It is a bit weird to have all the def. on node levels but then (6) on graph level
Section title 4 is a bit long, also title A4 is almost a paragraph in itself.
I have trouble understanding the definition of $\tau^i_j$, shouldn’t it be the last updated timestep rather than the amount by which the embedding is outdated (this in my understanding is the quantity $s_ij$
In Section 4 adaptivity to dynamic inputs is mentioned (as a feature of the framework) but no further evidence is provided. I rewrite to make it more clear that this could be an application but should be further investigated as future work (as is done in the conclusion).
A5 Appendix; nodes never deviate by more than one, i.e. which means regular updates. Is this correct? In my understanding this ensures that the total work of all nodes is similar B=20 ensures (somewhat) regular updates
The sampling notation in A5 is a bit weird - but this might be due to my confusion about the role of $tau^i_j$ which makes it hard for me to verify the correctness of the shown procedure.
In the Appendix layer sizes are noted as 4,4,1 - this seems quite small, is there a particular reason for this limitation?
In the Appendix multiple references are broken, where a ? shows instead.
In Section 5 you mention that prior work unifies the objective oriented view. But then you continue with saying that there is no reason to restrict - so what is a unifying or restricting view? I believe this to be mostly a formulation issue.
How would you like to capitalise during the paper, in the main text energy GNN is used but then in the Appendix it is Energy GNN. I would recommend keeping it consistent throughout. 
In Section 5, how does the energy function enable robustness? Isn’t this a property of the implicit GNNs and not limited to EGNN?
I did not follow the statement “not necessarily convex with respect to the features”, but the node embeddings, but usually the initial node embeddings are the features? I also think it would be good to make explicit where the convexity is required (in the final convergence proof I assume, following the original proof).
In A.2 there is an additional + on the third line of the proof
The proof of the main insight could be improved for presentation: restating the original theorem, showing the individual assumptions (the second condition where the Ks are set is not immediately obvious), is this why e_i is defined this specific way?
Do you have any intuition on why IGNN is first stable, but then diverges for larger graphs?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

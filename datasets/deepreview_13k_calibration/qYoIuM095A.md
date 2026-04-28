# GNN-based Probabilistic Supply and Inventory Predictions in Supply Chain Networks

- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 5, 3, 3

## Abstract
Successful supply chain optimization must mitigate imbalances between supply and demand over time. 
While accurate demand prediction is essential for supply planning, it alone does not suffice. 
The key to successful supply planning for optimal and viable execution lies in maximizing predictability for both demand and supply throughout an execution horizon.
Therefore, enhancing the accuracy of supply predictions is imperative to create an attainable supply plan that matches demand without overstocking or understocking.  
However, in complex supply chain networks with numerous nodes and edges, accurate supply predictions are challenging due to dynamic node interactions, 
cascading supply delays, resource availability, production and logistic capabilities.  
Consequently, supply executions often deviate from their initial plans.
To address this, we present the Graph-based Supply Prediction (GSP) probabilistic model.  
Our attention-based graph neural network (GNN) model predicts supplies, inventory, and imbalances using graph-structured historical data, demand forecasting, and original supply plan inputs.  
The experiments, conducted using historical data from a global consumer goods company’s large-scale supply chain, 
demonstrate that GSP significantly improves supply and inventory prediction accuracy, potentially offering supply plan corrections to optimize executions.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This article presents the highly researched problem i.e. supply and demand imbalances over time using Graph-based supply prediction probabilistic model that predicts supplies, inventory, and imbalances using graph-structured historical data, demand forecasting, and original supply plan puts.

### Strengths
Good detailing of the problem statement and to point literature review to distinguish the contribution from the traditional prediction scenarios.

### Weaknesses
One of the key problems in supply chain networks is lead time predictions and probably a potential extension the authors can think about extending it. 

GATs apply stacked layers in which nodes consists feature of neighboring nodes, applying these attention makes the whole network with different weights to the different nodes present in the neighbors which was leveraged to predict supply & that's interesting. The authors need to explore a bit more in detail in section 3.1 for better readability. 

Is there any stabilization process carried out in output layer such as multi-head attention?  
any sort of transformation or concatenation is done on the output features?

Typo error could have been avoided in Page 4 -foot note no. 3 - dailiy basis needs attention.

### Questions
GATs apply stacked layers in which nodes consists feature of neighboring nodes, applying these attention makes the whole network with different weights to the different nodes present in the neighbors which was leveraged to predict supply & that's interesting. The authors need to explore a bit more in detail in section 3.1 for better readability.

Is there any stabilization process carried out in output layer such as multi-head attention?  
any sort of transformation or concatenation is done on the output features?


Typo error could have been avoided in Page 4 -foot note no. 3 - dailiy basis needs attention.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors propose a novel GNN-based architecture to predict supplies, inventory, and imbalances for supply chain optimization. This is achieved by introducing (i) a probabilistic model that operates on carefully designed representations (e.g., discretized timing-deltas for an event or multipliers for event quantities), and (ii) an iterative inference approach to ensure supply capacity constraints.

Empirically, the authors show that the proposed method outperforms domain-specific algorithms (i.e., Croston’s method) and planned shipments from the dataset using historical data from a global consumer goods company.

### Strengths
I am not an expert in the field of supply chain forecasting, but I enjoyed the thought process behind the development of the architecture. The authors encode specific domain knowledge to achieve good performance and reliability (e.g., constraint satisfaction).

Despite the readability of Section 3 could be improved, the narration is fairly clear and complete. Figures are also generally informative and overall the paper is well written.

### Weaknesses
In my opinion, the main weaknesses of this work lie in (i) the extreme specificity of the methodology, (ii) the lack of baselines and/or experiments to validate the proposed architectural innovations, and (iii) more generally, the relevance to the broader ICLR community.

(i) The extreme specificity of the methodology:
Supply chain is an extremely relevant problem. However, the proposed architecture seems to be extremely tailored for this one specific application. How generalizable are these methods beyond the supply chain application? It'd be nice to see experiments on a more diverse set of problems.


(ii) The lack of baselines and/or experiments to validate the proposed architectural innovations:
Arguably, the major contribution of this work is the neural network architecture and input/output representations. The authors do a good job at motivating (in text) the reasoning behind their choices, however, there is little to no evidence to support the specific choices. Can the authors provide ablations in support of the individual choices in the architecture? For example: 
- Discrete time-deltas vs continuous representation
- Delta vs Non-delta
- Quantity multiplier vs absolute number
- etc.

Moreover, in the same direction, the set of baselines is extremely limited. The authors should provide additional learning-based prediction models from literature or simply by implementing sensible alternative approaches to the problem

### Questions
(i) The extreme specificity of the methodology:
Supply chain is an extremely relevant problem. However, the proposed architecture seems to be extremely tailored for this one specific application. How generalizable are these methods beyond the supply chain application? It'd be nice to see experiments on a more diverse set of problems.


(ii) The lack of baselines and/or experiments to validate the proposed architectural innovations:
Arguably, the major contribution of this work is the neural network architecture and input/output representations. The authors do a good job at motivating (in text) the reasoning behind their choices, however, there is little to no evidence to support the specific choices. Can the authors provide ablations in support of the individual choices in the architecture? For example: 
- Discrete time-deltas vs continuous representation
- Delta vs Non-delta
- Quantity multiplier vs absolute number
- etc.

Moreover, in the same direction, the set of baselines is extremely limited. The authors should provide additional learning-based prediction models from literature or simply by implementing sensible alternative approaches to the problem

### Soundness
3 good

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
The paper proposes to address the problem of predicting supply and inventory in supply chain networks using a GNN-based method.

### Strengths
*Originality*
The work demonstrates the capability of AI adoption in a relatively uncommon domain. The author designed new lost function and iterative procedure for ensuring feasibility.

*Quality and Clarity*
The author introduces clearly the motivation of the research. The authors made successful use of figures and tables that helped understanding the background and methodology.

*Significance*
The authors are able to demonstrate the efficacy of their method in predicting supply for a historical data.

### Weaknesses
### weaknesses:
 My major concerns are with the presentation and clarity. It is almost impossible to follow the details and check the correctness of the methods introduced. The authors directly dive into the methodology without clearly stating the problem. For example, the paper lacks a clear definition of what constitutes a "planned shipment" and how it differs from actualized shipments. Furthermore, it combines the modeling with discussions of GAT, making it difficult to understand the core contributions. It is rarely possible to immediately distinguish which parameters are known a priori, and which are decision variables that the model aims to determine. What are inputs of your prediction? What is the definition of planned shipments? Do you know a plan of future supply before making prediction? The paper needs to explicitly define the inputs to the prediction model. Are these historical data, planned schedules, or a combination of both? Without this clarity, it's impossible to assess the feasibility and practicality of the proposed method. Not mentioning that the overwhelming number of parameters and notations used without sufficient explanations make it even tougher. It is a must to explicitly setup the problem and introduce all assumptions and formulation details of your supply chain model, especially when it seems that your formulation and model of the supply chain is different from traditional literature.

Other minor presentation problems include:
- It is uncommon in the network literature using the term "lane"; commonly used are edges or arcs. The author used "edges" when describing the graph but used "lane" elsewhere. It is misleading.
- Overuse of footnotes is annoying. If the texts are important, bring them to the main text; if not, delete it or put in the supplementals.
- The notations are bad and unreadable. For example, 7 super/sub-scripts for a single variable
$$\hat{q}^{day, t, Iter=n}_{u, v, est at w, recv}$$

*Contributions*

I may misunderstand some parts (for reasons stated above) but I personally don't think this paper makes sufficient realistic contribution to the real supply chain planning problems. From a macroscopic view, the prediction problem makes plausible sense and the ability to predict the incoming of supply is good. In reality, the supply chains are rather decentralized and divided without a centralized decision maker that overlook everything and make the planning. The paper does not address how data would be collected and aggregated across such decentralized systems. Local decision makers meet much smaller-scale problems and have more well-controlled supplier relationships that leads to accuracte local prediction of incoming supply. Collecting data and make centralized prediction can be infeasible and unnecessary.

The authors claim contributions on the design of loss function, which is bi-objective controlled by a weight hyperparameter. In optimization society, it is usually wise to avoid such formulation because it is hard to interpret and justify the results, especially when your two objectives are in different scale (one daily error, and the other weekly cumulated errors). The paper needs to provide a more rigorous justification for the chosen loss function. How can you quantify the impacts of the two objectives to the followup planning? Which error will result in higher operational costs? Specifically, how was the weight hyperparameter chosen, and what is its impact on the trade-off between daily and weekly prediction accuracy? A sensitivity analysis of this parameter would be beneficial.



### Questions
- The baseline methods are obviously not good enough and compare your method with them does not stand you out. Are they the only options people can use to predict the ongoing supply?

- Is the method introduced robust to disruptions? It is one of the most important questions to think about when claiming the usefulness. If there is SKU shutting down or suddenly high labor shortage (as in the pandemic), I doubt if the method can quickly capture the dynamics and still have good performance.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a predictor for the lane-level cumulative outgoing supply along with the node-level inventory levels. The solution is based on a Graph attention mechanism. The authors show that their predictor performs well on a real dataset.

### Strengths
The method seems to solve the problem for the industry sponsor of the project.

### Weaknesses
### weaknesses:
 1. The authors do not state the contribution of the paper. I am having a hard time judging the significance of the problem and the results. Specifically, it is unclear what aspects of the proposed method are novel compared to existing graph attention network (GAT) approaches. The paper would benefit from explicitly stating the theoretical and practical contributions in the context of supply chain management and graph learning.
2. Numerical experiments lack competing baselines. The numbers in Table 1 and 2 thus do not carry a lot of meanings. The rationale behind incorporating demand prediction inputs in the inventory prediction is not clearly stated. The numerical results only compare the performance when the hyperparameter is chosen from {0,0.5,1}. A more comprehensive evaluation should include comparisons with other relevant methods, such as traditional time-series forecasting models or other graph neural network architectures. Additionally, a more thorough hyperparameter search is necessary to ensure the reported results are representative of the method's best performance.
3. What is a lane? Is it an edge on the graph? This notion is quite untraditional both in the supply chain literature and the graph learning literature. The paper needs to clearly define the terminology used, especially when it deviates from established conventions. Providing a clear definition of "lane" and its relationship to edges and nodes in the graph would improve the clarity and understanding of the proposed method.
4. There are no innovations in terms of neural network architectures. The paper appears to apply a standard graph attention mechanism without significant modifications. The authors should elaborate on any specific adaptations or modifications made to the GAT architecture for this particular application, or justify why a standard implementation is sufficient.
5. The design of the solution seems ad-hoc. It is unclear how the solution package proposed in this paper can be generalized to solve other practical problems. The paper also lacks some theoretical contributions to justify the soundness of the approach. The authors should discuss the generalizability of the method beyond the specific problem addressed in the paper. Providing theoretical insights into why the proposed approach is effective would strengthen the paper's contributions.


As I am also a researcher working on the intersection of machine learning and supply chain management, I do not see that this paper fits with the audience of this conference. Simply using a GAN to solve a specific dataset does not excite the audience of this community.

### Questions
1. I find the discussion in Section 3.2 intimidating with an overload of indices. To my understanding, the difficulty of this paper only lies in the construction of the target variables (partly due to the dynamism of the system). Section 3.2 and 3.3 are simply preparing these target values, so I think the authors should make this information simpler. So far, Section 3.2 and 3.3 look more like a "project report" to the industry partner. For the audience of this conference, why should we care about these calculations leading to equation (12) and (18)? In the end, neural networks are just functional approximations: we match input with output. Thus, even though the output can be difficult to compute, preparing the target variables is just data-processing. Unfortunately, it may not be exciting for the audience of the ICLR conference to learn about how the authors process the data.


// Post-rebuttal: I thank the authors for their replies. I slightly increase my score.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

# A Theory of Initialisation's Impact on Specialisation

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Prior work has demonstrated a consistent tendency in neural networks engaged in continual learning tasks, wherein intermediate task similarity results in the highest levels of catastrophic interference. This phenomenon is attributed to the network's tendency to reuse learned features across tasks. However, this explanation heavily relies on the premise that neuron specialisation occurs, i.e. the emergence of localised representations. Our investigation challenges the validity of this assumption.
Using theoretical frameworks for the analysis of neural networks, we show a strong dependence of specialisation on the initial condition.
More precisely, we show that weight imbalance and high weight entropy can favour specialised solutions.
We then apply these insights in the context of continual learning, first showing the emergence of a monotonic relation between task-similarity and forgetting in non-specialised networks, and, finally, assessing the implications on the commonly employed elastic weight consolidation regularisation technique.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
- The authors introduce a theoretical framework that demonstrates how initialization controls whether networks develop specialized or shared representations
- This work contains a rigorous mathematical analysis demonstrating that weight imbalance between layers drives specialization
- This paper presents a novel analysis of how initialization affects continual learning methods, particularly demonstrating the dependency of EWC on specialization

### Strengths
- This work takes a new perspective on the class catastrophic forgetting problem and provides theoretical justification for why initialization is important
- I believe continual learning researchers will be interested in this approach and in building on this work

### Weaknesses
 - The primary weakness is the lack of empirical experiments. I would like to see different initialization methods compared on several simple continual learning or class incremental learning benchmarks. Overall, I think this work still has value as a theory paper.


### Questions
How would your initialization schemes scale to modern architectures with skip connections?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper studies how the initialization of a network can affect its ability to “specialize” where representations are localized and disentangled. The paper discusses a simple student-teacher framework with extensions to disentangled attribute learning and continual learning. I think the paper looks solid but it is highly likely that I didn’t understand the paper.

### Strengths
- The paper is informative on the theoretical setup and its implication in empirical experiments such as disentangled learning and continual learning.
- The conclusion about network initialization is insightful.
- The figures in the paper are nicely organized.

### Weaknesses
 - Clarity: I found the paper not very clear. First it builds off from some prior knowledge on “specialization” and its definition of specialization is “one pathway finish learning (reach it’s hitting time t ∗) before the other begins learning (reaches it’s escaping time tˆ)”. However, “hitting” and “escaping” are two new concepts without definition. And why does the leading time matter for specialization? Can’t a MoE like architecture also specialize? In other words, the two neurons could simultaneously specialize into two different aspects of the input data, where the lead time of one neuron does not matter. Perhaps this is because I am very new to the literature, but without properly understanding the concept of specialization, I cannot have a confident judgment on the paper.
- Although the paper is theoretical, the main paper does not have any formal theorem/claim to explain the relation between initialization and specialization.
- The paper lacks a core claim. The first part attributed specialization to the “imbalance” in initialization (I also didn’t understand why h-ww^T is imbalance). The second part focuses on how “gain” of initialization affects disentanglement. And lastly, in continual learning, initialization was mentioned but unclear which part of initialization can cause the failure of continual learning. Basically, it seems that the whole paper is talking about initialization but the actual mechanism is quite different in each part and lacks a unifying explanation.

### Questions
See weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper investigates how weight initialization, specifically imbalance, affect the arising of specialization in the network representation and the subsequent consequences on forgetting wrt. task similarity.

### Strengths
Originality: Although specialization and continual learning have been widely studied in the context of modularity, this paper attempts to take a more thorough investigation from the perspective of weight imbalance at initialization which is interesting and an important direction. 

Quality: Figure 3&4 provide good insights on how imbalance leads to specialization/disentanglement both theoretically and experimentally. 

Clarity: Notations are clear and maths are largely clear (except Eq. 9). 

Significance: I think weight imbalance is an interesting and important angle for continual learning thus the paper has great potential.

### Weaknesses
Quality: 1) As mentioned by the authors, simplified setting is a limitation of the paper: all theoretical results are on single-hidden layer networks (linear for learning dynamic, nonlinear for student-teacher); All experiments including the ones on continual learning are on toy examples except Figure 4. 2) I find the overall main message unclear - is specialization good or bad for continual learning?  (see question)
		
Clarity:  The current flow of the paper can be problematic, it required significant back-and-forth for me to understand the messages (example see questions).  The manuscript seems incomplete, for example the caption for Figure 4.  
		
Significance: Apart from the other mentioned comments, one key aspect the paper could gain on its significance is to make more clear conclusions (see questions).

### questions:
a. Conflicting results? - Figure 6 orange is no specialization and with lowest forgetting (good?) but Figure 7 trying to say no specialization is not good? Is specialization good or bad for continual learning? 

b. Can the authors give any explicit conclusion on weight imbalance and their impact on continual learning, apart from initialization has an effect? This seems to be the most important message of the paper but I can't find any statement in the text. Eq 9 gives the generalization error but was not explained.  

c. Fig 6 is very confusing. Two factors: layer-wise imbalance (r) vs. pathway imbalance (theta). But they are both changing across scenarios; without controls, I don't see how conclusions can be drawn. 

d. Figure 6 blue - why is it 'specialization after the first task' since theta=pi/4 and according to Figure 5 that's yellow = no specialization? 

e. Unclear conclusion: For example, Sec 4.3 on continual learning, its conclusion only mentions the concerned factors without making clear their consequences on CL so standing more like an introduction than a conclusion "In a broader context, a rich diversity of behaviours can emerge, driven by factors such as the initialisation schemes, the scale of weights in the first layer, and the readout heads for both tasks."

f. Could the authors somehow materialize the concept of 'specialization' in Figure 2? I could vaguely see how two pathways of different lambda could lead to specialization as one simply wins the race but it was after much back-and-forth comprehension.  

g. Figure 1b main message = activation function is subsidiary to weight imbalance? If so, it seems to be disconnected from the rest of the paper and seems like better belonging to the appendix than as a killer figure. 

h. Flow problem: Q and R in Figure 1 are not really introduced until in Sec 4.1 but even then they are only defined without explained (l352).

### Questions
a. Conflicting results? - Figure 6 orange is no specialization and with lowest forgetting (good?) but Figure 7 trying to say no specialization is not good? Is specialization good or bad for continual learning? 

b. Can the authors give any explicit conclusion on weight imbalance and their impact on continual learning, apart from initialization has an effect? This seems to be the most important message of the paper but I can't find any statement in the text. Eq 9 gives the generalization error but was not explained.  

c. Fig 6 is very confusing. Two factors: layer-wise imbalance (r) vs. pathway imbalance (theta). But they are both changing across scenarios; without controls, I don't see how conclusions can be drawn. 

d. Figure 6 blue - why is it 'specialization after the first task' since theta=pi/4 and according to Figure 5 that's yellow = no specialization? 

e. Unclear conclusion: For example, Sec 4.3 on continual learning, its conclusion only mentions the concerned factors without making clear their consequences on CL so standing more like an introduction than a conclusion "In a broader context, a rich diversity of behaviours can emerge, driven by factors such as the initialisation schemes, the scale of weights in the first layer, and the readout heads for both tasks."

f. Could the authors somehow materialize the concept of 'specialization' in Figure 2? I could vaguely see how two pathways of different lambda could lead to specialization as one simply wins the race but it was after much back-and-forth comprehension.  

g. Figure 1b main message = activation function is subsidiary to weight imbalance? If so, it seems to be disconnected from the rest of the paper and seems like better belonging to the appendix than as a killer figure. 

h. Flow problem: Q and R in Figure 1 are not really introduced until in Sec 4.1 but even then they are only defined without explained (l352).

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
1

### Summary
The paper presents an analysis of specialization in neural networks without nonlinearities, with focus on the determinants of specialization and its influence on forgetting.

The analytical methods of the paper fall outside my expertise hence I cannot give a meaningful evaluation of the paper as a whole as they make up the majority of the argument. The below ratings and comments are limited to a superficial evaluation of the main points and should not be regarded as reliable.

### Strengths
The analysis and discussion about the relevance of specialziation to forgetting, as well as the determinants of specialization, is an interesting area on inquiry.
The analysis is provided with a rigorous mathematical framework.

### Weaknesses
The analysis is performed on linear networks, while nonlinearity is the defining feature of NNs. Authors are clear about that and apparently it is not an unprecedented way to conduct a similar analysis, but this would render the conclusions of the analysis questionable nonetheless. I would suggest the authors to include a more detailed discussion regarding what sort of guarantees can be given when transferring conclusions obtained from linear networks to conventional, nonlinear ones.

### Questions
Please see weaknesses point above.

### Soundness
3

### Presentation
3

### Contribution
2

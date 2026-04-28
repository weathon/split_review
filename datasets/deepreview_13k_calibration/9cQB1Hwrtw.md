# Transformers Struggle to Learn to Search Without In-context Exploration

- Decision: Accept
- Avg Score: 6.75
- Scores: 5, 6, 8, 8

## Abstract
Search is an ability fundamental in many important tasks, and recent studies have shown that large language models (LLMs) struggle to perform search robustly. It is unknown whether this inability is due to a lack of data, insufficient model parameters, or fundamental limitations of the transformer architecture. In this work, we use the fundamental graph connectivity problem as a testbed to generate effectively limitless high-coverage data to train small transformers and test whether they can learn to perform search. We find that, when given the right training distribution, the transformer is able to learn to search.

We analyze the algorithm that the transformer has learned through a novel mechanistic interpretability technique that enables us to extract the computation graph from the trained model. We find that for each vertex in the input graph, transformers compute the set of vertices reachable from that vertex. Each layer then progressively expands these sets, allowing the model to search over a number of vertices exponential in the number of layers.

However, we find that as the input graph size increases, the transformer has greater difficulty in learning the task. This difficulty is not resolved even as the number of parameters is increased, suggesting that increasing model scale will not lead to robust search abilities. We also find that performing search in-context (i.e., chain-of-thought) does not resolve this inability to learn to search on larger graphs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This study investigates whether transformers can learn to perform search by training small models on graph connectivity data. Results show that transformers can learn to search under certain conditions, but struggle with larger graphs, indicating that simply scaling LLMs may not enable robust search. The study introduces a new interpretability method to analyze the model's learned algorithm.

### Strengths
- The study tackles an intriguing and practical research question: understanding the mechanisms behind search capabilities in LLMs. This is not only scientifically interesting but also has meaningful implications for real-world applications.
- Training a small GPT model on synthetic graph data is a reasonable and well-justified approach to investigate this research question.

### Weaknesses
The logical flow of the paper is weak in several areas. The authors should clarify the connection between their empirical results and the statements made, as well as provide more intuition behind their hypotheses. 
For example, in line 51, the authors state, "We demonstrate experimentally that transformers can indeed be taught to search, but only under fairly restrictive conditions on the training distribution." However, Figure 3 does not fully support this claim. While it may indicate that the model does not generalize well to a larger number of lookaheads than seen in the training data, it does not substantiate any firm conclusions about the training distribution itself. The claim lacks a clear definition of what constitutes a 'restrictive' training distribution and how this restriction is specifically manifested in the data. The experiments should include a more controlled variation of the training distribution to isolate the impact of specific distribution properties on the model's ability to learn search.
In line 359, the authors mention, "We noticed a pattern and formed a hypothesis about the algorithm the model has acquired to solve the search problem." However, the pattern observed and its connection to the proposed hypothesis remain unclear and should be elaborated upon. The description lacks specific details about the nature of the observed pattern and how it translates into a concrete hypothesis about the model's internal algorithm. The authors should provide a more detailed explanation of the pattern, including the specific features or behaviors that were observed, and how these observations led to the proposed hypothesis. 

Additionally, the proposed method and analysis require clarification. For instance, in line 337, the phrase "path of explainable attention operations" is used—was this path inspected manually? And in line 358, the authors mention "a number of input examples" without specifying the exact number. Providing this detail would help improve the robustness of their claim.

### Questions
- Interpretation of Figure 3: The paper claims that transformers can search under restrictive training distributions, but Figure 3 only seems to show limited generalization to larger lookaheads. Can the authors explain how this supports claims about the training distribution?
- Pattern and Hypothesis Formation (Line 359): What specific pattern did the authors observe, and how did it lead to the hypothesis about the algorithm the model uses? Could they provide a clear link between the observed pattern and their hypothesis?
- Explainable Attention Path (Line 337): What exactly is meant by a "path of explainable attention operations"? Was this path derived through manual inspection, or was there a specific method used?
- Quantifying Examples (Line 358): The authors mention using "a number of input examples" but do not specify the exact number. Could they provide this detail to strengthen the robustness of their conclusions?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper aims to explore LLMs' internal mechanisms for graph connectivity problems tasks: given a graph (nodes and connections between nodes), a starting vertex, and a goal vertex, the LLM outputs the next vertex from the starting vertex.
Specifically, the paper constructs a training set to train a small decoder-only transformer. It improves the Mechanistic Interpretation visualization method to explore which tokens influence the LLM's output. Based on experimental results, the authors conclude that LLMs must be trained with in-context samples to fully understand the graph search problem.

### Strengths
The topic is interesting and may have influence in the community.

### Weaknesses
1. There are potential data leakage issues in the training and testing datasets constructed by the authors:
The authors use a generation method to generate training data online and save the first few generated results as test data. While the authors claim they will remove overlapping samples between training and test data, they don't explain how they compare whether two graphs are identical. If only using string matching, it cannot determine whether two graphs are completely equal. For example, these two graphs: node 1 -> node 2 and node 3 -> node 4 are completely equivalent but cannot be detected through string matching. Therefore, the test set is likely included in the training set. Additionally, given the number of vertices and max number of in-out edges, DAG generation is finite. Thus, the authors' claim about infinite graph generation may be incorrect.
The authors trained a simplified model that doesn't correspond to currently widely-used LLMs:
First, since the authors used full attention rather than causal attention, they actually trained an encoder-only model rather than a decoder-only model.

2. Second, the authors only used one-hot embedding for each token and position embedding when training this encoder-only model.
Finally, for the graph connectivity problem, the authors' trained model only outputs one token, while current LLMs typically have reasoning steps.

3. The authors' improved Mechanistic Interpretation has the following issues:
The proposed method requires performing perturbation and forward pass once for each element in every attention map of the LLM, and then forward pass to see the effects on the output logits, which is time consuming.
In Line 318, determining the influence of modified tokens on attention through frozen previous layers is not reasonable, as modified tokens also influence previous attention calculation and thus influence the activation for each layer.

### Questions
Please refer to the weaknesses part.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper explores the behavior of transformers models when trained on search questions on directed acyclic graphs (DAGs). The authors show the importance of training data distribution for better generalization. Then, they conduct mechanistic understanding of the trained models to discover a progressive message passing algorithm utilized by the model to explore search paths. However, the models struggle to learn from larger graphs. Finally, the authors propose proxy in-context examples that help the model for robust exploration of the graph before solving the search problem. Overall, the paper represents a significant step towards our understanding of the inner mechanisms of transformer models.

### Strengths
The major strength of the paper lies in its motivation to understand transformer mechanisms in search based tasks. The authors take carefully designed experimental exploration to train transformers on directed acyclic graphs, with careful design discussion on data distribution, and propose a new mechanistic approach to analyze the learned algorithm. The authors discover a message passing algorithm, where the neighborhood information are shared progressively among the vertices, which leads to an exponential path-merging algorithm. 

The authors also touch upon the difficulty of training transformer models on larger graph structures, and propose in-context tasks to help the model explore the graph better. Overall, the paper conducts an in-depth analysis of transformer model training on search problems and will be an important contribution to the academic community.

### Weaknesses
As such, the paper doesn't have many weaknesses. I have a couple of questions regarding the experimental setup.

a) **Sequence length in In-context exploration:** As the experiments require training on higher sequence length, how are the samples in training data distribution decided? How many steps in DFS traces are necessary for the model to learn? If the authors had provided same 'K' padding tokens to the experiments in the experiments in section 4, would the models generalize better?

b) **Distribution of path-merge operations:** Are there patterns in the distribution of path-merge operations and copy operations across the layers in the trained model? Specifically, is there a trend in the number of path-merge operations per layer, and how does this relate to the depth of the graph being explored?

c) **Evaluation with density of graphs?:** Do the trained models generalize to extremely sparse graphs? 
- Furthermore, on cases where the graph contains $2$ disconnected components, what will the model output be for start and goal vertices not in the same component? This is a critical edge case that could reveal limitations in the model's understanding of graph connectivity.

d) **Values of $\alpha$, $\kappa_1$ and $\kappa_2$ in section 4**: How are these values decided in experiments? What is the sensitivity of the results to these hyperparameter choices? A more detailed discussion of the selection process and the impact of these parameters on the mechanistic analysis would be beneficial.

e) **Clarification questions:**

- "the log attention weight of each important operation in the last layer." (line 303) - 
What does log attention weight mean? How do you define important operation?
- "it requires many forward passes (linear in the number of attention operations and in the number of input examples)." (line 354) -  Can the authors give details on the number of passes necessary? Furthermore, do the number of necessary passes depend (logarithmically) on the length of the search process for a given input example?

### Questions
Please check my questions in the above section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper explores the ingredients that constitute the search ability in pre-trained language models. The authors introduce a synthetic setting--searching over DAGs represented in the natural language space--and pre-train autoregressive transformers of varying scale. The finding is mixed: transformers can implement search under restrictive data distribution, but face significant challenges with scaled problem sizes.  The authors have explored training strategies that encourage the transformer to generalize better.

### Strengths
- Combining mechanistic interpretability with the search problem is, to my knowledge, novel, as most prior works have focused on "classification"-style tasks that feature a very restricted output space in terms of vocabulary and length. The problem is more challenging in term of complexity, and would presumably require chain-of-thought capabilities to solve effectively. This new setting also prompts the author to introduce a new algorithm for mechanistic analysis, which may be of interest to the interpretability community.
- I enjoyed the exposition style presentation of the paper, with each section introducing problem setting of growing complexity, as well as experimental findings that sufficiently supports these findings.
- The authors study nuanced challenges for transformers to generalize on algorithmic tasks in the presence of distribution shift.

### Weaknesses
 - My primary concern of this paper stems from the broader implication of the authors findings. Several prior works have found that large-language models can implement certain graph algorithms [1][2], including graph connectivity, and that this type of algorithmic reasoning can be improved with appropriate adaptations of chain-of-thought [3]. It is unclear whether the authors findings contradict, confirm, or offer more nuanced insights to prior works. Specifically, the paper does not clearly delineate how its findings on the limitations of transformers in search tasks relate to the demonstrated capabilities of LLMs in graph-related tasks. The paper should clarify whether the observed limitations stem from the specific synthetic task design, the scale of the graphs used, or inherent limitations in the transformer architecture itself when applied to search problems. 
- While the paper does a fine job surveying relevant works in mechanistic interpretability, it is somewhat lacking when situating itself in the LLM planning/search and theoretical expressivity literature. Aside from the aforementioned works, several works have directly studied whether LLM can internalize search (in the form of MCTS) [4] and explore in-context [5]. The lack of a theoretical analysis, or a proper discussion of them make understanding the authors' contribution challenging. For example, the paper could benefit from a discussion on the theoretical underpinnings of why transformers might struggle with search tasks, such as the limitations of their attention mechanisms in capturing long-range dependencies or the challenges in learning recursive algorithms. The paper should also discuss the implications of its findings on the broader understanding of the capabilities and limitations of transformers in complex reasoning tasks.
- While the strategy that strengthens the LLM's search ability in the means of data augmentation is nice, it may not directly translate to practical guidance due to the synthetic nature of the task setup. The augmentation strategy, while effective in the synthetic setting, lacks a clear connection to real-world search problems. The paper should discuss how the proposed data augmentation techniques could be adapted to more realistic scenarios, such as planning in robotics or natural language understanding tasks that require search over a large space of possibilities. The lack of generalizability of the augmentation strategy limits the practical impact of the findings.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
3

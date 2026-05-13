# Is uniform expressivity too restrictive? Towards efficient expressivity of GNNs

- Decision: Accept
- Scores: 6, 8, 6, 8

## Abstract
Uniform expressivity  guarantees that a Graph Neural Network (GNN) can express a query without the parameters depending on the size of the input graphs. This property is desirable in applications in order to  have number of trainable parameters  that is independent of the size of the input graphs. Uniform expressivity of the two variable guarded fragment (GC2) of first order logic is a well-celebrated result for Rectified Linear Unit (ReLU) GNNs [Barcelo &. Al, 2020]. In this article, we prove that uniform expressivity of GC2 queries is not possible for GNNs with a wide class of Pfaffian activation functions (including the sigmoid and $\tanh$), answering a question formulated by [Grohe, 2021]. We also show that despite these limitations, many of those GNNs can still efficiently express GC2 queries in a way that the number of parameters remains logarithmic on the maximal degree of the input graphs. Furthermore, we demonstrate that a log-log dependency on the degree is achievable for a certain choice of activation function. This shows that uniform expressivity can be successfully relaxed by covering large graphs appearing in practical applications. Our experiments illustrates that our theoretical estimates hold in practice.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This is a theoretical work about the connection between GC2 and GNNs with various activation functions. Its first contribution is to prove that uniform expressivity is not possible for GNNs with bounded Pfaffian activations. The second contribution is to build non-uniform expressivity for GNNs with Pfaffian activations via a constructive approach. Some synthetic experiments are provided to verify the theoretical arguments.

### Strengths
1. The motivation is good: rigorously understanding the expressive power of GNNs is a significant direction, especially it requires carefully quantify expressive capacities with sizes and depths. This work follows this motivation.
2. A rich family of activation functions is considered (such as arctan, tanh, sigmoid), as an extension of previous works about positive and negative results with simpler activation functions. And the general definition of Pfaffian functions makes it possible to generalize to other activations in the future.
3. The presented theory in the main text looks good.

Note that I didn't check all the proof in the appendix.

### Weaknesses
1. The presentation seems incomplete in some places, so thorough proofread and revision are necessary. For example:
    * in theorem 3.1, the last sentence is confusing in grammar. It is unclear what the precise implication of the theorem is due to the awkward phrasing.
    * in line 197, ''two blue neighbors'' should be ''red''. This is a minor but important error for understanding the construction.
    * in line 195, 199, 202, please check whether the parentheses are complete or not. There appear to be some missing or mismatched parentheses which makes the expressions difficult to parse.
    * in line 279, the last sentence is not complete. This makes it difficult to understand the conclusion of the argument.
    * in Figure 2, $l_i$'s are missing. I suppose they are the leaf nodes. This should be explicitly stated in the figure caption or the text.
    * around line 318, notations are not consistent, where line 685 uses $\nu_{t,m}(k)$ instead of $\nu_{t}(k,m)$. This inconsistency in notation makes it difficult to follow the arguments.
    * in line 363, what is the meaning of $\sigma^N(R\setminus (\epsilon, 1-\epsilon))$? The notation is not standard and requires further explanation. It is unclear how this set is being used in the proof.
    * in Corollary 5.5, tanh -> arctan. This is a minor but important error.
    * in Figure 3, please use different linestyles for easiness of reading, instead of only using different colors. Using only color makes the figure difficult to interpret for those with color vision deficiencies.
    * in line 495, a ''second'' shall be removed. This is a minor grammatical error.
2. around 335, the mentioned $T[0,k,m]$ and $T[1,k,m]$ seem to assume the tree in Figure 2 is rooted tree from $s$ without backtracking, which means $s$ is not in the leaf nodes. If so, please clarify this when defining the tree. The definition of the tree structure needs to be more precise, including whether it is a rooted tree and the role of the starting node $s$.
3. in line 495, please clarify how this layer argument is connected with theoretical results. Does it mean the different layers for activation functions in Prop 5.2-5.4? The connection between the experimental setup and the theoretical results is not clear. It is unclear how the number of layers in the experiment relates to the theoretical analysis of activation functions.
4. in line 500, the conjecture about SGD is too sudden without evidence. The claim about the difficulty of training with step-like activation functions needs more justification and evidence. It is not clear why the authors suspect this is the case.

### Questions
Please see the above concerns.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper aims to more closely characterize the uniform approximation capabilities of graph neural networks as a function of the activation functions applied to each aggregation of messages. There are primary theoretical contributions:
1. While previous results suggest that bounded-size guarded model logic (GC2) queries can be expressed by fixed-size GNNs with CReLU activations, Section 3.1 proves that certain GC2 circuits cannot be expressed by GNNs with sigmoid and tanh activations (or more generally, for superpolynomial Pfaffian activations). This limits the universality properties of GNNs. The proof involves constructing pairs of tree graphs whose outputs will be identical as a result of their activations.
2. However, Section 3.2 shows that all bounded-size GC2 queries can be expressed by a GNN whose size grows slowly as a function of the graph degree for sigmoid and tanh activations (and more generally, for "step-like activations").

They validate their theoretical results by training GNNs to learn two synthetic GC2 queries on different graph sizes. These experiments reveal sharp thresholds between the abilities of different activations to distinguish between similar graph instances.

### Strengths
The results of the paper are well-motivated theoretically---it is interesting to understand the trade-offs of different activations and the limitations of universal approximation. In particular, such fine-grained separations between constant-size and near-constant-size architectures are interesting, seeing as most graphs are small enough for the $\log\log\Delta$ scaling to be surmountable. 

As far as I can tell, the mathematical results are correct. The proof ideas of distinguishing similar tree graphs and constructing separations with step-wise activations are intuitive.

### Weaknesses
In general, the presentation of the results would be improved by more context for Pfaffian and step-like activations. A more close linkage between tanh and sigmoid and the parameters of Pfaffian chain of order would appreciated, along with more examples of step-like activations and an intuitive discussion of their parameters. While the authors mention that tanh can be expressed as a Pfaffian chain, the specific parameters and structure of this chain, and how they relate to the properties of tanh, are not made explicit. Furthermore, the discussion of step-like activations lacks concrete examples, making it difficult to understand how these functions are parameterized and how their parameters affect the behavior of the GNN. 

While individually unimportant, there are several areas with ambiguous notation or minor mistakes that I would appreciate the authors clarifying:
* Definition 2.3 and Example 2.1 have some inconsistent notation, e.g. $E$ and $Edge$ are used interchangeably, and $\exists^{\geq p}$ is not defined (although it is fairly intuitive). The formula in Example 2.1 appears to indicate that at least one neighbor has at least two neighbors that are _red_, not blue. The meaning of $E(x,y)$ is not explicitly defined in the context of the graph, which could lead to confusion about whether it represents an edge or some other relationship between vertices $x$ and $y$.
* Definition 2.4 introduces a Pfaffian chain of order, but not Pfaffian functions. The relationship between the two should be made explicit. It is unclear if a Pfaffian function is simply the final function in the chain, or if there are other constraints. 
* In Theorem 3.1, "Conversely, any (aggregation-combine) GNN expresses with activation function CReLU expressed a
GC2 query" does not parse. The sentence structure is unclear and the intended meaning is difficult to extract.
* Grammar nit on line 250: "superpolynomial if it non constant".
* On line 291, what is the $y$ limit over? $y$ appears to be vector-valued. It's not clear whether the limit is taken element-wise or in some other sense.
* If Definition 5.1, does the $\sigma^N$ notation reference exponentiation or composition? The notation is ambiguous and could refer to either repeated application of the function or raising it to a power.

### Questions
In general, (approximate) linear threshold activations are not practical in neural networks because of lack of bounded derivatives. Are the authors concerned about the learnability of their constructions in Section 5 that simulate threshold activations?

What is the significance of the parameters $H$ and $\epsilon$ on the construction in Theorem 5.1? The other parameters seem to have influence on size complexity, but not those.

Likewise, do know whether the network weights for Theorem 5.1 can be bounded?

### Soundness
4

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
In the study of GNN expressivity, it is crucial for practical usage to take the number of parameters needed into consideration. To this end, uniform expressivity has been proposed to test whether GNNs can express a query with the number of parameters independent on the size of the input graphs. However, in this paper the authors found that uniform expressivity tends to be too restricted for a wide class of GNN models. This paper then relaxes the concept of uniform expressivity into almost-uniform expressivity and further show that most GNNs can be still quite expressive when restricting the number of parameters to be logarithmic on the maximal degree, satisfying most practical needs. The results in this paper are justified by both theoretical analysis and numerical experiments.

### Strengths
- Compared with general expressivity measurement of GNNs, uniform expressivity sometimes tends to be too strict, thus provides negative results for GNNs: as shown in this paper, MPNNs with sigmoid activations cannot uniform express GC2 queries. To this end, it is nice to find a balance between general expressivity (which does not consider the number of parameters) and uniform expressivity (where the number of parameters is independ w.r.t. input graphs) for practical needs. The log complexity of parameters described in this paper is realizable for most practical situations.
- This paper considers a wide class of activations, defined as step-like activation functions. The authors show that their results are applicable for many practical activation functions including sigmoid and tanh.

### Weaknesses
 - The study in this paper relies on the definition of step-like activation functions. The properties of step-like activation function still requires more discussion. Specially, I have some concerns regarding the definition of step-like activation functions:
  - The Relu function ReLU(x)=max{0,x} clearly is not a step-like activation function since it disobeys (a): $\sigma(1)=1$. A question naturally arises: is the set of all possible step-like activation functions large enough to cover up most situations (or further, is it possible to find the maximal set of activation functions that satisfies Theorem 3.4)? The paper should provide more justification for why this specific class of activation functions is relevant and what are the implications of not including other common activations like ReLU.
  - In Definition 5.1, I assume in (b), $\sigma'$ is the derivative of $\sigma$. What does $\sigma^N$ in (c) mean? I searched over the paper but couldn't find an explanation. This lack of clarity hinders the understanding of the theoretical results.
  - To derive Corollary 3.5 from Theorem 3.4 it is necessary to show that sigmoid and tanh are special cases of step-like activation functions with $\eta=0$. However, Proposition 5.3 and Proposition 5.4 states that only a 3-layer NN with tanh and a 5-layer NN with sigmoid can be step-like activations. If this is the case, it largely restricts the structure of GNNs: the results in this paper are only applicable to MPNNs whose activations are again multi-layer NNs. This setting should be mentioned in the former parts of the paper when defining GNNs. The implications of this restriction on the practical applicability of the results should be discussed more thoroughly.
  - Continuing from the above concern. In Proposition 5.3 (and similarly in Proposition 5.4), a 3-layer NN is needed to express step-like activation function. Note that an activation function is a **point-wise** function that applies independently to each element of the input vector. How does the 3-layer NN behave like a poin-wise function to the input vectors in the whole GNN computation procedure? For example, let $X=[x]$ be the input and $W=[w_1,w_2]^T$ be the parameter at first layer. The output is $[w_1 x,w_2 x]^T$. If the dimension input is changed to be $X=[x_1,x_2]$, how does this reflect to $W$? To me this can be done by setting $W=[[w_1,w_2,0,0]^T,[0,0,w_1,w_2]^T]$ but this makes the number of parameters in each layer linerly grows w.r.t. the input dimension ( and thus makes the total number of parameters $O(d^2)$). Please correct me if I am wrong.

### Questions
Please refer to Weakness. There are some concerns that limit the impacts of the theory in this paper. I am willing to change the score if the concerns / problems are properly discussed / solved.

### Soundness
2

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
This papers studies the following fundamental question. Any node binary classification task can be defined as a logic formula. The paper tries to understand whether common GNN architectures can learn a given logic formulas **uniformly** (over all graphs with unbounded size). This is in stark contrast with prior research, which typically allows the model size to grow with input graph size. The authors gave both negative and positive results, showing that GNNs with sigmoid/tanh activations cannot uniformly approximate GC2 logic formulas, but they can almost-uniformly approximate them. The authors gave both counterexamples and constructions in their proof. Finally, they conduct experiments to verify their results.

### Strengths
I would like to say this is a quite interesting paper and I like it a lot. First, this paper studies GNN expressivity from a novel perspective. Unlike prior work which largely focuses on graph isomorphism (which is mainly TCS/graph theory perspectives), this paper is clearly more relevant to real neural network architectures instead of abstract color refinement algorithms, making it especially relevant to the community. On the other hand, this paper differs from traditional function approximate theory, as these theories often let the model size to grow in order to approximate better with a larger input domain. Instead, this paper gives both positive and negative results on whether a *fixed* model can deal with graph learning tasks for all inputs. This ability is unique for graph learning tasks.

Secondly, the paper provides a rigorous theoretical foundation. All definitions and statements are well-defined and accessible, which enhances clarity. I find the results nontrivial and impactful, and it enhances our understanding in the community.

### Weaknesses
One potential weakness of these results is that almost-uniform expressivity is perhaps already sufficient. Therefore, the limitations of sigmoid/tanh networks is not that severe in practice. So this paper may have a limited impact in guiding practical design of GNNs.

Update: I should acknowledge that I am not very familiar with first-order logics beyond the paper of Barcelo (2020). I am not sure if similar ideas have been raised in prior work (possibly under a different community).

### Questions
I am curious about the insights behind the theoretical results. I suspect this may be due to the sigmoid/tanh function is bounded, so it can not  express a quantity that grows with input size. On the other hand, ReLU/CReLU is not bounded. I wonder whether any unbounded non-linear activation is sufficient for uniform expressivity?


Miscellaneous：
1. Definition 2.4: U should be $U$.
2. Page 7, line 350: the word "the" is redundant.
3. What is the difference between Corollaries 5.6 and 5.7? I suspect there is a typo here.

### Soundness
4

### Presentation
3

### Contribution
3

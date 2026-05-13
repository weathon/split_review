# Differentiable Reasoning about Knowledge Graphs with Reshuffled Embeddings

- Decision: Reject
- Scores: 3, 6, 5, 3, 6

## Abstract
Knowledge graph (KG) embedding methods learn geometric representations of entities and relations to predict plausible missing knowledge. These representations are typically assumed to capture rule-like inference patterns. However, our theoretical understanding of the kinds of inference patterns that can be captured in this way remains limited. Ideally, KG embedding methods should be expressive enough such that for any set of rules, there exists an embedding that exactly captures these rules. This principle has been studied within the framework of region-based embeddings, but existing models are severely limited in the kinds of rule bases that can be captured. We argue that this stems from the use of representations that correspond to the Cartesian product of two-dimensional regions.
As an alternative, we propose RESHUFFLE, a simple model based on ordering constraints that can faithfully capture a much larger class of rule bases than existing approaches. Moreover, the embeddings in our framework can be learned by a Graph Neural Network (GNN), which effectively acts as a differentiable rule base. This has some practical advantages, e.g. ensuring that embeddings can be easily updated as new knowledge is added to the KG. At the same time, since the resulting representations can be used similarly to standard KG embeddings, our approach is significantly more efficient than existing approaches to differentiable reasoning. The GNN-based formulation also allows us to study how bounded inference can be captured. We show in particular that bounded reasoning with arbitrary sets of closed path rules can be captured in this way.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
In this work the authors propose a region-based knowledge graph embedding method which they term ReshufflE. In their method, each entity $e \in \mathcal E$ is represented by a vector $\eta(e) \in \mathbb R^d$, and each relation $r \in \mathcal R$ is represented by a region in $\eta(n) \subseteq \mathbb R^{2d}$. The regions are an intersection of half-spaces, and the score function for a triple $(e, r, f)$ is the $\ell^2$ distance of the concatenated vector $e \oplus f \in \mathbb R^{2d}$ from the region $\eta(r)$.

The authors provide extensive theoretical analysis of the representational capacity of their model, including propositions which claim that the model is capable of representing certain cyclic rules, and moreover capable of embedding any triples which require a bounded number of rule applications from the original graph. Finally, the authors present empirical results on a transductive knowledge graph completion task, where their model does not achieve state-of-the-art results but does seem to deliver "best in class" results considering the more efficient inference of embedding-based models.

### Strengths
Both the proposed model and the methods of analyzing the representational capacity are novel. I am not familiar with other approaches which are amenable to the extent of theoretical guarantees regarding the representational capacity as presented in this paper.

The clarity is high. The authors do an excellent job motivating their design decisions and presenting the rather technical arguments which draw on a wide range of foundational concepts. I was able to follow their arguments clearly.

### Weaknesses
Significance is moderate. As the authors acknowledge, this model does not obtain SOTA results, and therefore would be unlikely to be leveraged in practice. That said, the authors' techniques and analysis suggest that the model is sufficiently expressive to capture rule bases in practical settings, and so the reason for the difference in performance may be (as they stated) that the evaluation sets are not necessarily rich enough to benefit from these rules alone, and would require a "fallback model".

The overall quality of the work is also moderate. I was very pleased with the principled theoretical analysis the authors presented, however I believe there is an error with the definition of a rule graph which makes some of the propositions incorrect. I believe this may be a small fix, however.


Overall, I very much like this work, and I believe the authors will be able to address the questions I have listed below or correct me if I am mistaken in my understanding.

### Questions
**Rule Graph Definition:** First, a minor point is that the rule graph $\mathcal H$ is defined not only with respect to a rule-base $\mathcal P$ but also with respect to the original set of relations $\mathcal R$. (Given a rule-base $\mathcal P$ without a set of relations $\mathcal R$ we can't create a rule graph, since, in particular, it needs one edge for each relation.)

The main question I have is related to the definition of the rule graph, specifically (R4). My interpretation of this rule is the following:

First, for a given multi-graph $\mathcal H$, let $S_{(n_1, n_2)}$ be the set of edge paths from $n_1$ to $n_2$.
Now, given $r\in \mathcal R$, let $T_r =\cup_{(n_1, r, n_2) \in \mathcal H} S_{(n_1, n_2)}$.
Then my interpretation of (R4) is that: for each $r \in \mathcal R$, we have some path $(r_1; \ldots; r_q) \in T_r$ such that $P\models r_1(X_1, X_2) \wedge \cdots \wedge r_q(X_q, X_{q+1}) \rightarrow r(X_1, X_{q+1})$.

Note that the premise of (R4) (as written in the paper) is trivially satisfied because for every two nodes connected by an $r$-edge there is a path connecting these nodes in $T_r$ - in particular, $r$ itself, which is why it wasn't stated in my interpretation above. This could become slightly more interesting if we remove $r$ from $T_r$, in which case we would only apply this condition to situations where $r$ is such that every pair of nodes connected by an $r$-edge have a non-trivial path connecting them, but this is not my main concern.

The main issue I have is that I do not see how this condition ensures that "only the rules in $\mathcal P$ are captured". For example, what prohibits a graph with edges $\\{(n_1, r_i, n_1)\\}_{r \in \mathcal R}$ from being a rule graph for any rule base $\mathcal P$?

I think perhaps what was intended was that $T_r = \cap_{(n_1, r, n_2) \in \mathcal H} S_{(n_1, n_2)} \setminus \\{r\\}$.

Without clarification on this point many of the proofs cannot be verified.

**Example 4:** There is a minor error here in that I think it must be intended that $\mathcal P$ is exactly equal to the set

$$\\{r_1(X, Y) \wedge r_2(Y,Z) \wedge r_1(Z,U) \rightarrow r_2(X, U)\\},$$

because if it merely contains such a rule then it may also contain some other rules which makes it no longer impossible to create a rule graph (eg. $$r_1(X,Y) \rightarrow r_2(X,U)$$). Apart from this, unless the definition for the rule graph is clarified I don't see what would prohibit the graph $\mathcal H$ with edges $\{(n_1, r_1, n_1), (n_1, r_2, n_1)\}$ from satisfying the definition as a rule graph for $\mathcal P$.

**eq edges:** The authors introduce the eq edges, presumably for good reason, but they seem to add complexity and I am not sure what purpose they serve. For example:
1. Line 255: An eq-reduced type of a path is mentioned, but surely any "eq-reduced type"is also, itself, a path in the graph, since eq simply returns to itself. Maybe this was meant to handle the fact that the GNN will have a fixed number of layers, and therefore we need to consider paths of a fixed length always, but it is not clear to me.
2. Figure 1: The rule graphs depicted do not even allow for paths with eq in arbitrary positions, actually to my understanding (perhaps I am wrong?) the depicted rule graphs would not allow for any path which includes "eq" more than once, and then only at the last position.

**Some claims are too strong:**
1. In the abstract, the authors argue that the lack of representational capacity for other models "stems from the use of representations that correspond to the Cartesian produce of two-dimensional regions", however the author's proposed model also uses regions which are cartesian products of 2-dimensional regions.
2. On line 153 the authors claim that BoxE is not capable of capturing closed path rules, but this doesn't seem to be true - simply represent $r$ by any box which contains the intersection of the boxes for $r_1, \ldots, r_p$.

### Soundness
3

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
Reasoning over Knowledge Graphs is an area of machine learning that is primarily concerned with completing knowledge by predicting missing information (relations between entities). This work explores our theoretical understanding of KG embedding approaches that are region-based and studies one aspect of how well these learned embeddings capture rule-like inference patterns. In particular, the authors focus on faithfully capturing closed path reasoning rules and describe a GNN formulation that can provably capture bounded reasoning of such rules. Their proposed Reshuffle model is also efficient, works in the inductive KG completion setting, and performs well empirically on standard KG completion datasets. The authors also show that when a rule exists, there is a formulation of Reshuffle model can faithfully capture these rules.

### Strengths
The strength of the work lies in its systematic and formal treatment of question of expressivity of a certain class of KG completion methods. While studying the ability of such models to capture logical rules is not new, the specific type of closed path rules with cyclic dependencies that the authors consider is. 

The authors have generally done a good job providing formal proofs for most of their propositions. The paper is well written, with examples that help the reader clarify the definitions and concepts. The definitions are clearly explained (even as notation needs work, see details below) and the work well motivated. In particular, the discussion about negative results in Section 6 is appreciated.

Being able to prove that a model is expressive and has the capacity to capture certain sets of rules is important aspect of research. This work brings us a step closer to understanding and characterizing rule capturing abilities of region-based KG completion models and their limitations.

### Weaknesses
There are two main observations I would like to make about this work.

1) Notation: Anyone interested in doing a thorough technical reading of the work will have a hard time keeping track of the notation, which is defined across three sections (3 to 6) as the discussion of ideas moves forward. Given the large span of the use of this notation, it would be better to have a notation section defining most of the key notation so that the reader knows what section to refer to as they read.  
In addition, make sure every notation is defined properly (for example, what is an r-edge exactly? I could not find a definition) and avoid overloading notation (for example, on line 370  x^{(l)} means “l repetition of x”, while on the previous page it refers to the message passing layers representations). 


2) Cartesian product is mentioned in the abstract as being a limiting factor for many models to capture rules. This mention made me expect more discussion about this later in the paper but there was none. It would be good to expand on how exactly cartesian product ties into this and why is it a limiting factor. There is a relevant paper entitled “Knowledge Hypergraph Embedding Meets Relational Algebra” about capturing of rules (in this case, relational algebra operations) with embedding methods that is missing  from the related work section; this work also highlights the difficulty of capturing cartesian product. 



Other remarks and suggestions: 
-	The first paragraph of Section 6 mentions that Propositions 1 and 2 imply that Reshuffle can capture rules entailed by P. This is a key result of the paper and needs to be stated formally as a Lemma that follows from these propositions.

-	On line 399, should the (4) be (R4)? 

-	Equality on Line 352: (x_{l-1}, r_1, r_l) should be (x_{l-1}, r_1, x_l)

-	The discussion of the results at the end of Section 7 mentions the efficiency of the Reshuffle model compared to NBFNet and GraIL. This efficiency is an important property of this work and should be given a more proper treatment. A quick glance at Table 2 suggests that Reshuffle does not outperform NBFNet in raw performance metrics, highlighting its efficiency benefits would provide valuable context to interpret these.

### Questions
Can you give some more insight as to how cartesian product ties into the ability of these models to capture inference patterns?

Did you perform any experiments in a controlled setting, using a synthetic knowledge graph generated based on the closed path rules that this work is trying to capture?  This may allow to better understand in what cases the self-loop relation matters.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes ReshufflE, a knowledge graph embedding model based on GNNs which aims to better capture closed path rules. To this end, ReshufflE proposes an order-based relation scoring function, in which a triple $(e, r, f)$ holds when $r$, which defines a mapping between head entity ($e$) and tail entity ($f$) dimension indices, is true for all mapped dimensions. As orderings are non-differentiable, the paper proposes a soft approximation to produce the ReshufflE model. The paper additionally proposes dimensionality reduction based on Kronecker product to reduce parametrization, and subsequently overfitting. The paper provides an extensive theoretical analysis of the rules that ReshufflE can capture, and in doing so defines the notion of a *rule graph*, showing that any set of rules representable by a rule graph can be captured by the ReshufflE GNN. The paper also provides negative results when rule graphs cannot be built, further reporting sets of rule grammars that correspond to the aforementioned rule graphs and subsequently can be captured. As a final theoretical contribution, the paper weakens the general reasoning requirement and looks into bounded reasoning paths, showing that an $m-$layer ReshufflE GNN can capture arbitrary sets of $m-$bounded rules.

On the empirical front, the paper runs experiments on standard inductive link prediction benchmarks, showing competitive performance with rule-based systems (with the exception of WN18RR), and reporting an ablation study on Reshuffle to validate the model's design choices.

### Strengths
- The theoretical arguments appear sound, and the problem being addressed is well-motivated: Representing closed path rules is an important question in knowledge graph embeddings, and this paper proposes an improvement over the state of the art. 
- The discussion of the results is very objective, and limitations are acknowledged upfront. On the theoretical front, the set of closed path rules that can and cannot be captured is explored very thoroughly. Empirically, less flattering results are highlighted and discussed. 
- The writing of this paper is easy to follow. I especially appreciate the examples and figures in the theoretical discussions, which really help clarify the contributions of this work.

### Weaknesses
- Unfortunately, the paper appears to be highly specialized to representing closed path rules, so much so that it sacrifices useful inductive biases that are often standard in other, more basic models. For example, ComplEx clearly fails to represent hierarchies in the general sense, but can learn that a relation $r$ is symmetric, i.e., $r(x, y) \implies $r(y, x). By contrast, reshuffle seems to specialize exclusively in closed path rules, at the expense of, e.g., symmetry. Concretely, if $r$ is a symmetric relation, then, in ReshufflE, $e_{\sigma_r} (i) \leq f$ and $f_{\sigma_r} (i) \leq e$ must hold simultaneously for all $i$ in $I_r$. However, this implies that symmetry cannot be enforced at the relation level, as the aforementioned inequalities are entity-dependent, preventing the model from capturing this pattern (this could be a reason for the underperformance on WN18RR, in my opinion, but I leave this as a comment for the authors to consider). Therefore, it would be very useful for the authors to discuss which of the basic inference patterns (symmetry, reflexiveness, hierarchy, etc.) can be captured by ReshufflE and how, in order to better place the strengths of ReshufflE more generally. 

- The empirical performance of ReshufflE is not convincing, and seems to corroborate my above concern about over-specialization. To address this, I suggest that the authors try to report settings where ReshufflE can achieve SOTA results, to at least establish a set of rules of thumb where this model can be considered a strong SOTA candidate. Moreover, I recommend that the authors include more benchmarks, including potentially transductive benchmarks, to provide a more holistic picture of the strengths and weaknesses of this model. 

Overall, I find that Reshuffle provides a meaningful and useful theoretical contribution that has a place in the knowledge graph embeddings literature. However, I have serious concerns about the over-specialization of this model, and how this seems to negatively affect representing common patterns such as symmetry, hierarchies, both separately and jointly with the aforementioned closed path rules. Note that over-specialization is not a problem in itself, as specialized models can be advantageous in the right settings: The problem here is that this hasn't been clearly demonstrated neither in a theoretical nor an empirical setting. Hence,  given my current concerns with the paper, I lean towards rejection. Nonetheless, I am happy to revise my rating should the authors address my concerns. In particular, my main recommendations to the authors to 1) better elaborate the strengths and weaknesses of the model with regards to other rules, and 2) to provide concrete empirical settings (including potential synthetic data, but ideally real-world data) in which Reshuffle has a compelling competitive advantage, to illustrate scenarios where the model can more reasonably be applied.

### Questions
Please see "Weaknesses" section above.

### Soundness
4

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes RESHUFFLE, a novel model for differentiable reasoning over knowledge graphs that utilizes ordering constraints for improved embedding efficiency and expressiveness. RESHUFFLE can capture a broader class of rules than prior models and is especially effective for inductive KG completion using graph neural networks.

### Strengths
1. Proposes a unique, scalable model based on ordering constraints, extending the scope of rule capture beyond previous region-based approaches.
2. Employs a GNN framework to achieve efficient, update-friendly KG embeddings, advantageous for inductive tasks.
3. Demonstrates strong performance on benchmark datasets, outperforming some of existing reasoning models in some datasets.
4. Includes a rigorous theoretical and empirical analysis that supports the model's efficiency and robustness.

### Weaknesses
1. **Inability to Handle Noisy Data**: The RESHUFFLE model struggles significantly with noisy datasets like WN18RR, a major weakness for real-world applications where knowledge graphs often contain errors or incomplete data. The lack of adaptability to noisy or uncertain data undermines the model’s generalizability and limits its utility across varied datasets.

2. **Expressivity Limitations with Cyclic Dependencies**: Despite proposing a novel approach, RESHUFFLE cannot represent certain cyclic dependencies in rule bases, which restricts its applicability to only a subset of knowledge graphs. This limitation contradicts the paper's goal of providing a broadly applicable, flexible model for knowledge graph completion.

3. **Insufficient Support for Probabilistic Reasoning**: The model’s deterministic approach to embedding rules falls short in settings requiring probabilistic or non-monotonic reasoning, which are increasingly important in real-world KGs. This oversight limits the paper's contribution, as modern KGs benefit from methods that accommodate uncertain or evolving data.

4. **Over-Reliance on Ordering Constraints**: The novel use of ordering constraints, while interesting, imposes rigid structural assumptions that may lead to overfitting and limit the model’s expressivity. The reliance on strict ordering could restrict its effectiveness in scenarios requiring nuanced or flexible rule handling, making it less adaptable to complex inference tasks.

5. **Presentation and Organization Issues**. The paper's presentation and organization need improvement. The storyline, particularly in the introduction, lacks clarity and focus. Clearer structuring and a refined presentation of the motivation, methodology, and contributions would help readers follow the key points more easily.

6. **Performance Trade-offs with State-of-the-Art**: ESHUFFLE underperforms compared to NBFNet on multiple benchmarks where high accuracy is essential. Although RESHUFFLE offers efficiency advantages, its relatively lower accuracy raises concerns about its competitiveness. Additionally, A* Net [1], an incremental model of NBFNet, demonstrates efficiency and scalability; thus, the current experimental comparison with baselines appears insufficient.

7. **Limited and Incomplete Baselines**: The baselines included in this paper focus only on three categories—GNN-based, classical rule-based, and differentiable rule-based methods—overlooking several prominent classes, including translational KG embedding (e.g., RotatE[2], TransE[3], TransH[4]), probabilistic reasoning (e.g., Markov Logic Network[5], Probabilistic Soft Logic[6]), neuro-symbolic approaches (e.g., pLogicNet[7], RNNLogic[8], RLogic[9], DiffLogic[10]), and region-based models. Additionally, several recent state-of-the-art methods (e.g., A* Net[1], DiffLogic[10]) are missing, while RESHUFFLE still underperforms against NBFNet, a baseline from 2021. A more comprehensive and up-to-date set of baselines would strengthen the empirical claims.

8. **Insufficient experiments**. The experimental setup includes only a baseline study and an ablation study, which is insufficient to fully support the claims made in the paper regarding RESHUFFLE’s generalization ability and rule-capturing capabilities. Moreover, the evaluation is limited to Hit@10, whereas additional metrics like Mean Reciprocal Rank (MRR) and Hit@1, which offer more insight into ranking quality, are missing.


- [1] Zhu, Zhaocheng, et al. "A* net: A scalable path-based reasoning approach for knowledge graphs." Advances in Neural Information Processing Systems 36 (2024).
- [2] Sun, Zhiqing, et al. "Rotate: Knowledge graph embedding by relational rotation in complex space." arXiv preprint arXiv:1902.10197 (2019).
- [3] Bordes, Antoine, et al. "Translating embeddings for modeling multi-relational data." Advances in neural information processing systems 26 (2013).
- [4] Wang, Zhen, et al. "Knowledge graph embedding by translating on hyperplanes." Proceedings of the AAAI conference on artificial intelligence. Vol. 28. No. 1. 2014.
- [5] Richardson, Matthew, and Pedro Domingos. "Markov logic networks." Machine learning 62 (2006): 107-136.
- [6] Bach, Stephen H., et al. "Hinge-loss markov random fields and probabilistic soft logic." Journal of Machine Learning Research 18.109 (2017): 1-67.
- [7] Qu, Meng, and Jian Tang. "Probabilistic logic neural networks for reasoning." Advances in neural information processing systems 32 (2019).
- [8] Qu, Meng, et al. "Rnnlogic: Learning logic rules for reasoning on knowledge graphs." arXiv preprint arXiv:2010.04029 (2020).
- [9] Cheng, Kewei, et al. "Rlogic: Recursive logical rule learning from knowledge graphs." Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining. 2022.
- [10] Shengyuan, Chen, et al. "Differentiable neuro-symbolic reasoning on large-scale knowledge graphs." Advances in Neural Information Processing Systems 36 (2024).

### Questions
Please see above weaknesses for my concerns.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper is motivated by the shortcomings of region-based KG embedding methods, it is proposed to take advantage of the ordering constraints of the reshuffled entity embeddings. In practice, an implementation using GNNs is proposed to enable the ability to perform inductive KGC.

### Strengths
1. The structure of the paper is well organized, i.e., the scope of the problem is precisely stated, the motivation and related work are comprehensively discussed.
2. The formal presentation of the problem (e.g., examples), the theoretical investigation, and the proposal are satisfactory and very helpful for understanding the idea of the paper.
3. Experimental results on inductive KGC and ablation studies are promising.

### Weaknesses
1. $\mathcal{P}\cup \mathcal{G} \models (e,r,f)$ is unclear to me, i.e. the first paragraph on page 4. Could you please provide a concrete example illustrating how $it is applied? Also, please clarify whether the first 'and' in line 163 should be 'or' instead? 
2. The order of entities is not formally defined before Equ. (3). It's better to be illustrated in section 3.
3. The computational cost of constructing rule graphs should be studied and compared with other rule-based KG embedding methods. For instance, the complexity of constructing the rule graph w.r.t. the number of entities or the time cost proportional to the training time. And the training time cost comparisons to RuleN, AnyBURL, Neural-LP, DRUM, including the possible rule construction procedure.
4. The experimental results of applying possible sparsity constraints should be interesting to add, as claimed in line 238, even if some technical obstacles hinder the applausability of the idea. And the ability to capture cyclic rules should be investigated in experiments, for example, some simulation experiments should be helpful, which is not shown in the existing real data concentrated evaluations.

### Questions
1. Regarding the definition of closed path rules, given a graph $Z'\rightarrow Y'\rightarrow X \rightarrow Y \rightarrow Z$, and $X \rightarrow Z$, is the closed path rule embodied? Since it is captured by the induced subgraph of $\{X,Y,Z\}$, but not by $\{X, Y', Z'\}$. Or the rules are fully represented at the instance level, i.e. the symbols used to denote a rule all correspond to entities and relations in the graph, instead of just being placeholders.
2. In Eq. (3), is the period in the conditional really a comma?
3. What are the justifications for the conditions when initiating the embeddings to learn from lines 209 to 212?

### Soundness
3

### Presentation
4

### Contribution
3

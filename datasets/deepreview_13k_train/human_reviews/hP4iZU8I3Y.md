# Understanding Inter-Session Intentions via Complex Logical Reasoning

- Decision: Reject
- Scores: 6, 5, 6

## Abstract
Understanding user intentions is essential for improving product recommendations, navigation suggestions, and query reformulations. However, user intentions can be intricate, involving multiple sessions and attribute requirements connected by logical operators such as And, Or, and Not. For instance, a user may search for Nike or Adidas running shoes across various sessions, with a preference for purple. In another example, a user may have purchased a mattress in a previous session and is now looking for a matching bed frame without intending to buy another mattress. Existing research on session understanding has not adequately addressed making product or attribute recommendations for such complex intentions.
In this paper, we present the task of logical session complex query answering (LS-CQA), where sessions are treated as hyperedges of items, and we frame the problem of complex intention understanding as an LS-CQA task on an aggregated hypergraph of sessions, items, and attributes. This is a unique complex query answering task with sessions as ordered hyperedges. We also introduce a new model, the Logical Session Graph Transformer (LSGT), which captures interactions among items across different sessions and their logical connections using a transformer structure.
We analyze the expressiveness of LSGT and prove the permutation invariance of the inputs for the logical operators. By evaluating LSGT on three datasets, we demonstrate that it achieves state-of-the-art results.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this work, the authors focus on product and attribute recommendation by modeling complex user intention. They employ the logical session query answering (LSQA) to formulate the task. The proposed logical session graph transformer (LSGT) model runs on a hyper session graph, which uses a standard transformer structure to encode different entities. Experiments on three real-world datasets demonstrate the effectiveness of LSGT for complex session query answering.

### Strengths
1. The motivation that incorporates logical session query answering into product recommendation to model user intent is novel.
2. The experimental results demonstrate the effectiveness of the proposed LSGT.
3. The authors theoretically justify the expressiveness and operator-wise permutation invariance of LSGT.

### Weaknesses
1. There are some obvious typos. Authors should scrutinize the writing of the paper.
(1) In the 5th line of section 4.3, the formula after “The edge feature is denoted as” lacks a proper superscript.
(2) In Table 5, the first word “Predicti” in explanation of query type 2p should be “Predict”.
(3) In Table 5, the word “prodict” in explanation of query type ip should be “product”.
(4) In the 2nd line below Figure 5, the word “descibed” should be “described”.
2. In Figure 5, the query structure of ip is the same as up and the query structure of 2iS is the same as 2uS. It would be better to distinguish them like [1].
3. The paper lacks detailed description for figures especially Figure 3, which is hard to understand for readers.
4. It would be better to evaluate the model’s generalization ability of unseen query structures like [1,2,3].

### Questions
1. Why do authors not evaluate the model’s generalization ability of unseen query structures like existing works?
2. Is there an explanation for the author's choice of 14 query structures? Can some other query structures like 2i, and pni be incorporated?
3. Is it possible to make an ablation study for hypergraph and logical reasoning?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper formulates an item recommendation task based on the previous session history as a complex logical graph query (named as Logical Session Query Answering). In such a query, items and attributes are nodes, several items can be connected in sessions (hyperedges denoting the order of obtaining the items), relations form projection operators in a query, and other logical operators (intersection, union, negation) combine nodes and projections into a single complex query. Instead of operating on the complete hypergraph of items, sessions, and attributes, the authors decide to operate on the single query level and predict answer entities directly after linearizing the query via the Logical Session Graph Transformer (essentially, a TokenGT from [1]). The authors prove that their transformer is permutation invariant (with respect to intersection and union operators), and run experiments on 3 datasets showing marginal improvements over the baselines.

### Strengths
**S1.** The item recommendation task is framed as a complex logical query. While the task per se is not new (LogiRec [2] originally introduced it with projection and intersection operators), this paper extends it to unions and negations and to hypergraphs.

**S2.** Evaluation includes several baselines (that show, on the other hand, that the proposed approach only marginally outperforms existing models, but more on that in W2)

### Weaknesses
Starting from the claimed contributions:

**W1. Task.** The formulated task of Logical Session Query Answering is essentially query answering over hypergraphs. Sessions are n-ary edges, and other relations form 2-ary edges, so the hypergraph has edges of different arity. The temporal aspect of items in session hyperedges (that items follow each other in one session) seems to be of little use as the best-performing models are not using this information anyway. I would recommend the authors to focus the contribution on extending complex query answering to hypergraphs as there is not that much work in that subfield (StarQE is for hyper-relational graphs, and NQE supports both hyper-relational and hypergraphs). The claim of bridging CQA with session-based recommendations is not strongly supported, as the temporal ordering within sessions, a key aspect of session-based recommendations, is not effectively utilized by the models, which treat sessions as unordered sets of items when learning the representation of the session hyperedges. The task could be reframed as a hypergraph query answering problem with a specific focus on handling hyperedges of varying arity, which would be a more accurate representation of the problem.

**W2. Encoder + Experimental results.** The proposed logical session graph transformer (LSGT) is just one of the many query linearization strategies, eg, BiQE [3], kgTransformer [4], or SQE [5] that convert the query graph into a sequence with some positional information to be sent jointly into a Transformer. Architecture-wise, LSGT is TokenGT [1] but with a slightly different input format that sends tokens of logical operators. Experimentally, LSGT is very close to SQE [5] (the gap is often <1 MRR point) so it is hard to claim any novelty or effectiveness in this linearization strategy or in a slightly different transformer encoder. The experimental results do not convincingly demonstrate the superiority of LSGT over other linearization strategies, particularly when considering the marginal improvements observed. The lack of a thorough ablation study on the impact of the specific input format of LSGT further weakens the claim of novelty. The performance differences are too small to justify the claim of a significant advancement in query linearization.

**W3. Theory.** The theoretical study in Section 4.5 is derived from TokenGT and seems to be hardly applicable to the case of logical query answering. TokenGT’s theory of WL expressiveness assumes the graphs are non-relational whereas all logical query graphs studied in this work are relational, i.e., they have labeled edge types. There is a different line of work studying expressiveness of GNNs over relational graphs [6,7] and I would recommend starting from them in order to derive any expressiveness claims. Permutation invariance proofs are rather trivial because the Transformer architecture itself is permutation equivariant. The theoretical analysis does not adequately address the relational nature of the query graphs, making the expressiveness claims questionable. The permutation invariance proof is not a significant contribution, as it is a known property of the Transformer architecture. The theoretical analysis needs to be significantly strengthened by considering relational graph theory.

Overall, I think the paper has more potential if:
* The authors frame the task as the hypergraph query answering with the full support of first-order logical operators (intersection, union, negation) and demonstrate that several existing Transformer-based models show similar results on 3 benchmarks despite different linearization strategies; 
* Tone down the claims on the _logical session_ QA (it’s a hypergraph), new graph transformer and its expressiveness (TokenGT is not new, theory for non-relational graphs does not apply to relational ones), and state-of-the-art (all Transformer-based models show a very similar performance).

I understand that it would require substantial re-writing of several sections, so I am willing to increase the score if the authors decide to do it during the discussion period.

Minor comments:
* Too many sentences (especially in Section 3) start with noisy and artificial “however” and “meanwhile”. You don’t have to contrast every sentence to each other every time.
* $p$ and $q$ denote different things in 4.2 (item and session) and 4.3 (just two nodes) and it is confusing.   
* 4.4 Learning LSGT -> Training LSGT

### Questions
N/A

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces the task of Logical Session Query Answering (LSQA) and presents a solution called the Logical Session Graph Transformer (LSGT) model. The objective of LSQA is to learn logical queries for observed user interaction sessions. This task could help understand the logical intention of user interactions. The LSGT model achieves this by uniformly representing sessions, items, relations, and logical operators as tokens and leveraging a transformer-based sequential model for encoding.

The paper provides a theoretical analysis that primarily focuses on demonstrating the expressiveness of the proposed LSGT model. Additionally, comprehensive experiments are conducted to validate the superiority of the proposed model compared to existing baselines.

### Strengths
- This paper proposes the task of Logical Session Query Answering (LSQA), providing an novel paradigm for enhancing applications like session-based recommendation and query recommendation by understanding the logical structures of users' latent intents.
- The paper provides a theoretical analysis on the expressiveness of the proposed Logical Session Graph Transformer (LSGT) model.
- The paper innovatively build a unified representation model for items, sessions and logical operators using hypergraphs and sequential models.

### Weaknesses
 - Though the proposed task is novel, the proposed technical solution LSGT relies on existing hypergraph structures and transformer architeactures. Such designs have limited differences compared to existing sequential models and graph models. This lower the technical contribution of this paper.
- The evaluation part could be enhanced with more diverse experiments to conduct a more comprehensive empirical study, such as ablation study, hyperparameter study, case study on the generated queries, and an investigations on the benefits of LSGT brought to downstream tasks like session-based recommendation.

Minor mistake: In the summary for contributions: "We propose to propose ..."

### Questions
My concerns would be alleviated if the authors could provide further clarification on the technical novelty aspect and the comprehensiveness of the experiments. Please refer to the weaknesses part for details.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

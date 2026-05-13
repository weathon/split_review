# AutoRegressive Knowledge Base Completion

- Decision: Reject
- Scores: 3, 3, 3, 3

## Abstract
Despite their large sizes, many Knowledge Graphs (KGs) remain highly incomplete. This problem has motivated numerous approaches to $\textit{complete}$ the KGs by embedding them in a latent space to find the missing links. Although these methods show promising performance, a general limitation is that the scores given to possible links are uncalibrated and cannot be interpreted across different queries. Hence, we say they are $\textit{local}$ as they relate to a specific context. This limitation makes it non-trivial to deduce the truth value of the links and to answer complex queries. Another limitation is that their learning depends on negative sampling, which is challenging due to the Open World Assumption (OWA). 

To solve this problem, we propose a novel auto-regressive generative model that learns a joint distribution of the entities and relations of the KG without resorting to negative sampling. This distribution can be used to infer the probability that a link is sampled from the KG, which allows us to return a $\textit{global}$ score that is interpretable in different contexts. Moreover, our method has the additional advantage that it offers probabilistic semantics for complex reasoning and knowledge base completion, achieving state-of-the-art performance on link prediction with consistent scores across the entire KG.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces an autoregressive model for knowledge graph (KG) completion that avoids negative sampling. Traditional knowledge graph embedding (KGE) models rely on negative sampling, which can be problematic under the Open World Assumption (OWA), as distinguishing true facts from false negatives can lead to inconsistent scoring. The proposed approach aims to avoid this by factorizing the joint distribution $p(S, R, D)$  into $p(S) p(R \mid S) p(D \mid S, R)$  and modeling each factor as a categorical distribution.

While the problem addressed is significant and the approach of using an autoregressive model to learn effectively under the OWA without relying on negative sampling is novel and interesting, there are concerns regarding the proposed solution's modeling choices, the experiment setting, the fairness and soundness of the evaluation strategy, and the lack of convincing empirical results.

### Strengths
1. **Addressing the Open World Assumption**: The paper addresses an important gap in existing KGE methods: the Open World Assumption (OWA). This challenge is particularly relevant for KGs, as real-world KGs are highly incomplete, and it cannot be assumed that unseen facts are false. Therefore, an ideal training methodology should respect the OWA, unlike common negative sampling methods, which incorrectly treat unseen facts as negatives.

2. **Maintaining Probabilistic Interpretation during Training**: The proposed probabilistic factorization modeling and autoregressive approach is notable for maintaining a global probabilistic score throughout training—something not guaranteed by most existing methods. Typically, existing approaches either maintain a local probabilistic score per query or use a global energy-based score that requires time-consuming post-hoc normalization.

### Weaknesses
 **W1. Unclear Presentation of Existing Literature Gap**: The paper could benefit from a clearer presentation of the gaps in existing literature, an explanation of why addressing these gaps is important, and a more intuitive explanation of how the proposed method addresses these challenges. To my understanding, there are two main gaps in existing KGE methods that this paper attempts to address: (1) the Open World Assumption (OWA) challenge and the use of negative sampling, which conflicts with the OWA, and (2) the lack of a global probabilistic score consistent throughout training. The second gap can be further divided into two cases: (2.a) some query-based methods (e.g., NBFNet) can maintain a probabilistic score, but these scores are conditioned on the query and not global, and (2.b) other global KGE methods are mostly energy-based, requiring post-hoc global normalization, which can be time-consuming. Addressing the first gap is crucial, but the paper does not clearly articulate why solving the second gap is important. The introduction could be improved with a deeper explanation of why addressing these two gaps matters, perhaps by including a figure for illustration or providing a concrete example to support the argument.

**W2. Missing Discussion of Related Work and Calibration Techniques**: One of the key promises of the proposed method is its ability to maintain a consistent global probabilistic score that is informative for downstream decision-making by accurately reflecting the likelihood of an unknown fact being true. This is a well-studied concept in the literature known as calibration. Calibration is crucial because it enables determining an optimal threshold for making predictions. Without proper calibration, the probabilistic scores learned by a neural network may not align with real-world probabilities, as the scores are optimized solely to satisfy the training objective. This could lead to arbitrarily high scores for positive training examples and arbitrarily low scores for negative examples, compromising reliability.

Although the paper cites Zhu et al. (2023) (on Line 62), it lacks a broader discussion on calibration techniques and their relevance to the proposed approach (e.g., [1] for KGE and [2] for general classifiers). More significantly, the proposed methodology does not implement any common calibration techniques, which undermines the claim that the learned global probabilistic score is consistent and useful for downstream decision-making. Including a discussion of calibration techniques and incorporating such methods into the proposed approach would strengthen the validity of this claim.

**W3. Problematic Modeling Choice**: The proposed method circumvents negative sampling by decomposing the joint distribution $p(S, R, D)$ into $p(S) p(R \mid s) p(D \mid S, R)$ and assumes $p(R \mid s)$ and $p(D \mid S, R)$ are categorical distribution by applying Softmax activations. However, this modeling assumption is problematic because it suffers from poor expressivity. There is a reason why most existing KGE choose to model each individual edge as a Bernoulli random variable, rather than modeling $p(D \mid S, R)$ as a categorical distribution. Specifically, a categorical $p(D \mid S, R)$ assumes that given a particular $S=s$ and $R=r$, there is one and only one target entity $D=d$. This is generally not true in real-world KGs. For instance, in a KG about company structure, a single source entity may link to multiple target entities with the same relation, as seen in triples like (Google, employee, Jeff Dean), (Google, employee, Salar Kamangar), (Google, employee, Craig Silverstein). Even if the KG is carefully constructed to avoid such one-to-many mappings, the proposed method introduces inverse triples (LIne 251), converting any many-to-one mapping to one-to-many in the inverse, which violates the categorical assumption. The only scenario where the proposed method does not suffer from poor expressivity is when all relations are unique one-to-one mappings—an unrealistic scenario for most real-world KGs.

Another problematic assumption mentioned in the paper is that the dataset is sampled i.i.d. (Line 134). This assumption does not hold for KGs because entities are shared among different facts. For example, if (Google, employee, Jeff Dean) is observed in the dataset, then it is far more likely that (Google, owned by, Alphabet Inc.) will also be observed, then in a dataset where (Google, employee, Jeff Dean) is not observed, because perhaps the previous case is a KG about company structure, whereas the latter is a KG that has nothing to do about Google. The paper could greatly benefit from either improving the methodology to circumvent these assumptions or, at the very least, including a discussion on why these assumptions can be made and why their violation might not significantly affect practical outcomes.

**W4. Strange Experiment Desing and Unfair Evaluation Against Baseline Methods**: The experiment task was "global link prediction" (Line 281). However, this task is not designed in such a way that could showcase the potential benefit of the proposed method. As the proposed method is supposed to fix the gap of OWA challenge in existing KGE methods and thus could produce a "consistent global probabilistic score", a better experiment setting could be to first define a measure of what it means for a model's score to be "consistent" for the given task at hand, and then evaluating and showcasing that the proposed autoregressive model indeed outputs scores that are more "consistent" than the baseline methods, while achieve on-par performance to the baseline on the link prediction task. In contrast to simply attempting to beat SOTA methods on link prediction performance, such experiment can truly highlight the competitive edge of the proposed method. Regarding how to define such a "consistency" measure, a suggestion is to take inspirations from the calibration literature ([1][2]) and use their experiment methodology to show how the calibrated score is more informative to downstream users.

On the other hand, the link prediction performed "globally" is a task whose evaluation is unfair to query-based methods such as NBFNet, because they are designed solely for query-based prediction. If one is only interested in asking whether an unknown triple $(s, r, d)$ is true, then one should apply the query-based method as they were designed, which is to look at the score of all potential $d$'s by giving a specific $s$ and $r$. By "executing all queries from the test set and merging the obtained scores together" (Line 313), one greatly diminishes the expressivity of NBFNet, which was exactly one of the original challenges that NBFNet set out to address.

The authors argue that the "global link prediction" task is valid because one prefers global scores to local scores, because local scores hinder one's ability to "support more effectively complex and inter-contextual query answer and to perform KB completion across the entire scope of the KB" (Line 282 -284). This is not true, as many work has studied using query-based method like NBFNet to perform complex query answering on KGs. For instance, Zhu et al. [3] first proposed a method named GNN-QE, which is essentially applying fuzzy logic operators onto NBFNet to effectively and efficiently perform complex logical query answering (CLQA) on KGs. A follow-up work [4] then showed that GNN-QE can perform CLQA while generalizing to new KGs with unseen entities. Finally, a most recent work from Galking et al. [5] proposed the method ULTRA-Query that is able to generalize to KGs to different domains with completely unseen entities and relations types. Hence, these literature has solved the challenge of using query-based KGE models for effective and inter-contextual query answering task.

### Questions
Q1. **Alternative modeling choice**: Would it be possible to consider other probabilistic models instead of categorical distributiosn on $p(R \mid S)$ and $p(D \mid S, R)$? Say, for example, a mixture of distributions where it is allowed to have at most $K$ modes (e.g. peaks in the p.d.f. curve) for some predefined hyperparameter $K$? This way, we might be able to model multiple ground-truth $D$’s given specific $S$ and $R$ and (to some extent) cope with the one-to-many relational mappings in real-world KGs. Another way to think about this potential improvements is to draw analogy to multi-head attentions. If we interpret the Softmax logits as attention scores over the vocabulary of entities, then having multi-headed attention is essentially implementing a mixture of categorical distributions. Would it be possible to improve the proposed methods with multi-headed “attentions”?

Q2. **Conflicting Experiment Results**: In Section 5.3 and Figure 2, it is explained that “we see in Figure 2(c) that although the scores for the negative edges still receive a low probability, they are not excessively concentrated around zero …” However, looking at Figure 2(c), it seems that the negative edge score (orange curve) is indeed excessively centered around 0. Could you explain this discrepancy between the Figure and the text?

**References**

[1] Tabacof, Pedro, and Luca Costabello. "Probability calibration for knowledge graph embedding models." (2019).

[2] Silva Filho, Telmo, et al. "Classifier calibration: a survey on how to assess and improve predicted class probabilities." (2023).

[3] Zhu, Zhaocheng, et al. "Neural-symbolic models for logical queries on knowledge graphs." (2022).

[4] Galkin, Michael, et al. "Inductive logical query answering in knowledge graphs." (2022).

[5] Galkin, Michael, et al. "Zero-shot Logical Query Reasoning on any Knowledge Graph." (2024).

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes ART and ARC, two auto-regressive generative models that learn a joint distribution of the entities and relations of the KG without resorting to negative sampling.

### Strengths
1, The proposed method does not need negative sampling in the training.

2, The proposed method give consistent global scores instead of local scores.

### Weaknesses
1, The novelty is not clear in this paper. The proposed autoregressive model is a simple use of the conditional probability formula $p(s,r,d)=p(s)*p(r|s)*p(d|r,s)$ which lacks novelty. The paper does not adequately address how this formulation differs from existing autoregressive models for knowledge graph completion, particularly those that also decompose the joint probability of triples. The claim that this is the only method modeling the joint distribution exactly needs more rigorous justification, especially given the prevalence of probabilistic models in this domain. The authors should clarify the specific architectural innovations that enable their model to learn this joint distribution more effectively than existing methods.

2, The empirical performance of the proposed method is not strong. In Table 2, compared with NBFNet, ART only shows slightly better performance on FB15k-237 dataset while being outperformed by a large margin on OGBLBBioKG dataset and WN18-RR. In Table 3, ART did not show convincing advantages neither. The emprical results are not enough to show the superiority of the proposed method. The paper needs to demonstrate a clear advantage over existing methods across a wider range of datasets and evaluation metrics. The current results do not provide sufficient evidence that the proposed method is a significant advancement in the field. The authors should consider including more challenging datasets or tasks to better showcase the strengths of their approach.

3, This paper needs to discuss more on the difference of 'local' and 'global' scores. Learning 'global' scores is the contribution claimed in the paper. However, the concepts of 'local' and 'global' are not clearly defined. What's the necessity of computing global scores in the knowledge base completion tasks and downstream tasks? What advantages do global scores have over local scores especially give that the empirical results of global score methods are even worse than existing local score methods? The paper should provide a formal definition of 'local' and 'global' scores within the context of knowledge graph completion. It should also explain why global consistency is a desirable property and how it translates to improved performance in downstream tasks. The current discussion lacks the necessary rigor to support the claim that global scores are a significant contribution.

4, The presentation of the paper is not good. (1) Figure 1 shows the architecture of ARC instead of ART. However, ARC is not even in Table 2 or Table 3. (2) Best numbers in Table 2 and Table 3 are not highlighted. (3) The legends of Figure 2 are too small and can not be seen clearly. (4) Figure 4 does not have a name for X-axis.

### Questions
Please refer to the questions mentioned in the Weaknesses part.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Paper Summary:
The paper proposes a novel autoregressive approach for Knowledge Graph (KG) completion, aiming to address limitations in traditional Knowledge Graph Embedding (KGE) methods, which often rely on local scoring and negative sampling. Instead, the authors introduce an autoregressive generative model, which learns a global, joint distribution across entities and relations in the KG without requiring negative sampling. By using neural networks to model conditional probabilities, this approach produces interpretable global scores for query answering. 

Conclusion:
The paper proposes a novel autoregressive approach for Knowledge Graph (KG) completion, which learns a global, joint distribution across entities and relations in the KG without requiring negative sampling. Although the proposed approach is novel and interesting, its performance is less convincing due to lack of state-of-the-art results, lack of baseline models and lack of benchmark datasets. So in general, this is not an acceptable paper to ICLR.

### Strengths
Strength:
1. The method proposed by the authors are relatively novel. The introduction of an autoregressive generative model to address these issues by learning a joint distribution across entities and relations without negative sampling is compelling. This approach yields global, interpretable scores, which appears to enhance the method's adaptability to large KGs.
2. The method and deep network structure is described with details in this paper. Conditional probability reasoning is described with detailed mathematical formats. The paper is well-organized as well.

### Weaknesses
Weakness:
1. The performance of the model is not convincing. 
(i): The F1 scores for the proposed model is not comparable to NBF on the WN18-RR dataset. Also, the performance of the model on the OGBLBioKG is several percentages behind the NBF model. So in general, the proposed ART model only out-performs the baselines on the FB15K-237 dataset, which is not convincing. The fact that the model only shows superior performance on one of the three datasets, and that dataset being FB15K-237, which is known to have issues, raises concerns about the generalizability of the approach. The performance gap on WN18-RR and OGBLBioKG is significant enough to question the practical applicability of the proposed model in diverse KG scenarios.

(ii): Other than NBF and Complex, there are so many other baseline models published in the recent years: RotatE, GPFL, ConvE, DisMult, SACN, DRUM, Neural-LP, CoMPILE, etc. In order to make the paper more convincing, the authors should definitely include more baseline models when evaluating the performance of the proposed model. The current comparison set is insufficient to establish the model's position relative to the broader landscape of KG completion techniques. The lack of comparison with models like RotatE, which is known for its strong performance, makes it difficult to assess the true merit of the proposed approach.

(iii): I am not familiar with the OGBLBioKG dataset, which I assume is a biomedical knowledge graph dataset. But now that working with bio KG, why not use Bio2RDF and DRKG, which are more popular benchmark datasets? Also, I think most link prediction researchers will use WN18-RR, FB15K-237, Nell-995, YAGO3-10, DBpedia (50K & 500K). Why not include Nell-995, YAGO3-10, DBpedia? I am wondering why the authors only select specific KG reasoning datasets to evaluate their model. This issue makes the paper less convincing. The selection of datasets seems arbitrary and does not align with the common benchmarks used in the field, making it difficult to compare the results with other published work. The absence of results on standard datasets like Nell-995 and YAGO3-10 further limits the scope of the evaluation.

2. Some minor defects: 
While the paper mentions applications in complex query answering and knowledge base completion, specific examples of query types and scenarios could illustrate how the proposed model would outperform traditional KGEs. A few comparative examples could significantly enhance the paper's practical utility. Figure 1 is too small, could you please enlarge the font size?

### Questions
1. Why not include more baseline models? 
2. Now that working with bio KG, why not use Bio2RDF and DRKG, which are more popular benchmark datasets?
2. Now that working with WN18-RR and FB15K-237, why not include Nell-995, YAGO3-10, DBpedia?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
1. This paper presents a generative model for knowledge base completion that learns the distribution of triples $p(S, P, O)$ through an autoregressive approach, where $p(S, P, O) = p(S) p(P|S) p(O|S, P)$, optimized via maximum likelihood estimation (MLE).

2. Experimental results show that the model achieves competitive performance across three knowledge graphs (WN18RR, FB15k-237, and OGBLBioKG), demonstrating its effectiveness for tasks requiring consistent truth values, such as complex query answering.

### Strengths
1. This work offers two notable advancements over traditional KGE methods: a) it eliminates the need for negative sampling, which improves training efficiency; and b) it provides a probability score for each query, allowing for comparisons between distinct queries.

2. Empirical results regarding negative sampling reveal insightful perspectives, showing that this approach can introduce a potentially undesirable bias in training.

### Weaknesses
1. Presentation Issues

    1.1. Inappropriate language usage: Frequent grammatical and spelling errors detract from readability.

    1.2. Insufficient figure and table descriptions: Missing descriptions make it unclear what each component represents.

    1.3. Inadequate method explanation: The ART model lacks a diagram, and the structural and mathematical details of both the ARC and ART models are insufficient. Specifically, the paper does not detail the exact architecture of the 1D convolutional layers in ARC or the transformer layers in ART, making it difficult to understand the model's inductive biases. Furthermore, the paper does not specify the activation functions used, the number of filters, the kernel sizes, or the dimensionality of the embeddings, which are crucial for understanding the model's capacity and behavior.

2. Experimental Concerns

    2.1. Reproducibility issues: Due to incomplete model descriptions, achieving reproducibility is challenging. The lack of detail regarding the model architecture and training procedure makes it difficult for others to replicate the results. For example, the paper does not specify the optimizer used, the learning rate schedule, or the batch size, which are all important factors in achieving good performance.
    
    2.2. Missing ARC results in Table 2: Including ARC results alongside other methods would allow for a more comprehensive comparison. The absence of ARC results in the main table makes it difficult to assess the relative performance of the two proposed models and to understand the impact of using a transformer architecture versus a convolutional architecture.

    2.3. Weakly supported conclusions: The claim on Page 8, Line 395, that “our model is more open to the possibility that some of the unknown triples are true,” is not backed by experimental evidence. How does this openness benefit the model? The paper does not provide any quantitative analysis or ablation studies to support this claim, and it is unclear how this supposed openness translates into improved performance on downstream tasks. The analysis of the optimistic scenario is not sufficiently justified and lacks a clear connection to the model's architecture or training procedure.

### Questions
Setting aside the weaknesses mentioned, my primary concern lies with the overall contribution of this work. The primary objective of KGE methods is to complete missing triples in KGs. Models like $\text{Complex}^2$ proposed by [1] aim to adapt existing KGE methods into generative models, enabling applications in maximum likelihood estimation (MLE) and sampling. However, the authors emphasize that generating new triples—a core capability of generative models—is not necessary for this work. Additionally, the knowledge graph completion performance of this model, as shown in Table 6, is relatively underwhelming. In summary, the model seems unable to learn a robust distribution over triples or achieve strong knowledge graph completion. So, what is the intended purpose of this model?

[1] Loconte, L.; Di Mauro, N.; Peharz, R.; Vergari, A. How to Turn Your Knowledge Graph Embeddings into Generative Models. Advances in Neural Information Processing Systems 2023, 36, 77713–77744.

### Soundness
2

### Presentation
2

### Contribution
2

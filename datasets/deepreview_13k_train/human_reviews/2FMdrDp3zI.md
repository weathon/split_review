# Is Complex Query Answering Really Complex?

- Decision: Reject
- Scores: 3, 5, 5, 5

## Abstract
Complex query answering (CQA) on knowledge graphs (KGs) is gaining momentum as a challenging reasoning task.
In this paper, we show that the current benchmarks for CQA are not really \textit{complex}, and the way they are built distorts our perception of progress in this field.
For example, we find that in these benchmarks most queries (up to 98\% for some query types) can be reduced to simpler problems, \eg link prediction, where only one link needs to be predicted.
The performance 
of state-of-the-art CQA models drops significantly when such models are evaluated on queries that cannot be reduced to easier types.
Thus, we propose a set of more challenging benchmarks, composed of queries that \textit{require} models to reason over multiple hops and better reflect the construction of real-world KGs.
In a systematic empirical investigation, the new benchmarks show that current methods leave much to be desired from current CQA methods.
\blfootnote{\includegraphics[width=.025\textwidth]{./figures/pretzel} = shared supervision.}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This manuscript presents a data-level study of knowledge graph complex query answering. The main argument is that the query-target pairs in existing datasets (q, t) can be somehow reduced to the easier ones (sub(q), t) if the required triple can be found in training KG. Therefore, the paper proposes to focus on the irreducible query answer pairs and empirically examine that the performance of all existing methods will drop significantly. The facts revealed above motivate a search approach highlighted by letting the edges in the train graph be memorized. The performance of the approach is compared against previous works on old and new benchmarks.

---

## Retrospective summary after the rebuttal period.

This author-reviewer discussion thread goes on for too long during the rebuttal period, and particularly, the later part of the debate becomes intense. I think it is necessary to provide such a summary to digest my concerns and how they are not fully addressed for future readers of this page. Finally, I respond to the authors' accusation of a goalpost shift. 

### My concerns and why they are or are not addressed.

My initial concerns are, as stated in the weakness in the very first review:
1. the missing but essential baseline QTO/FIT.
2. the missing discussion in similar datasets, such as the BetaE dataset, FIT dataset, and EFO_k dataset.
3. distribution of the new benchmark.

The situation of those concerns are
1. Addressed.
2. Addressed partially. The BetaE dataset was considered empirically, which satisfies my minimum standard. However, no discussion about how their methodology of benchmark construction applies to query types in FIT and EFO_k datasets can be found.
3. It is still under debate, and let me expand on it as follows.

My concerns about the distribution of the proposed benchmark are decomposed into several fine-grained issues during the rebuttal period.

Distribution issues:
1. I proposed a new set of terminology that clearly describes two parts of samples $S_{X, II}$ and $S_{X, III}$ based on the split of training and testing edges. The old benchmark, although sampled in a synthetic data distribution (no matter how weird it is), still covers both sets. The new benchmark only focuses on the $S_{X, III}$. My view is that the ignorance of $S_{X, II}$ is worrisome because such ignorance failed to reflect CQA's performances on link prediction, logical connectives, and variables on $S_{X, II}$.
2. Besides, the new benchmark, even used jointly with the old ones, actually stresses the importance of $S_{X, III}$, which is picked by enforcing the missing links. By emphasizing such a subset of data, the author tries to encourage a better link prediction because the simplest way of eliminating the gap between the new benchmark and the old one is just to make a better link prediction.

Both two issues are not fully addressed.

1. The authors acknowledge the new benchmark's ignorance. However, they tried to alleviate the negative impact in two ways. The first way is the joint usage or the stratified analysis, which leads to my second issue. The second way is to state that $S_{X, II}$ is way less important than $S_{X, III}$, which leads to our disagreement in non-factual belief. My belief is the missing link (which needs to be filled to satisfy practical application) is relatively small and will be smaller due to the advancement of knowledge graph construction and knowledge harvesting. The authors believe that the missing links in a KG are significantly large proportion. Their belief is claimed to be supported by valid math derivation, which I don't think their math can support their belief.
2. For the second issue, I think the performance gap between old and new benchmarks is caused by only picking the missing links, and it can be narrowed by proposing better link predictors that have better link prediction performances on the missing links in existing KG datasets. There are some neverending debates about whether the gap can be fully closed or if it really reflects the measurement of CQA. It does not change my view that, as a benchmark that encourages researchers to get higher and higher scores, it is very important that a benchmark does not have a clear shortcut deviating from the original goal of the task (logical connectives and variables besides link prediction). Clearly, If one method can achieve better link prediction performance on test data, it can first predict all missing links and just run symbolic algorithms. The limit of this solution is exactly one begins with a link predictor that overfits the test set, which is how the authors create benchmark data. I don't think this is a valid outlook for constructing a new benchmark to facilitate the study. Ironically, optimizing on the old benchmark, criticized by the authors that are mostly measuring link prediction (suppose the authors are correct here), will finally close the gap between new and old benchmarks, making the new benchmark less and less useful.

### Some accusations from the authors.

The authors accused of continuous goalpost shifting. However, my concerns are centered on the data distribution of the new benchmark and how it will impact the study. 

I decomposed and expanded my claims to respond to the authors' words, such as "we don't see any problems here.". I believe that the active authors deserve to know why I am against them. The authors, although very eloquent, repeatedly misunderstood my terms and words. Such as narrowing down my mentions of link predictors to neural link predictors (or knowledge graph embeddings) and refusing to accept my thoughts by just stating that neural models can never achieve perfect performance. However, no matter whether the neural models are perfect or not, the emphasis of new benchmarks on link prediction still remains unchanged.

I understand that people sometimes get emotional during the debate, and the emotional words from both the authors and me are already documented in the following threads. Please also let me express my apology if any of my words ever hurt anyone.

### Strengths
- This paper conducts an in-depth study of existing benchmarks and reveals biases regarding tree-shaped queries and union operators in several datasets.

### Weaknesses
I have two concerns about the content discussed and the angle studied in this paper.

Firstly, the content seems to be very old. I am not sure whether this paper has been recycled on a sufficiently long time, so the author is not aware of the recent progress in this field. 
1. The dataset discussed only covers the query types in [1], which is outdated today. In 2024, several datasets covering far more complex queries are also proposed, including [2] for queries with logical negation, [3] for cyclic queries, and [4] for multi-answer variables. For the ``fair'' split of triples, the answer is also unaware of existing studies on temporal CQA [5].
2. The baselines discussed are also no later than the year 2023. ULTRAQ is almost the same as the GNN-QE.
3. Given the above ignorance, the proposed CQD-hybrid method is fundamentally identical to the QTO [6] proposed in ICML'23. Those two methods are all search-based approaches that involve memorizing the train edges, which is proposed in this paper and also reflected in Equation 4 in [6], noticing that normalizing link predictor scores into [0,0.9] will not change the order of solutions. 

I prefer to recognize methodological identicality as unawareness rather than plagiarism. Therefore I didn't raise an ethical review flag.


Secondly, saying that "the existing benchmark is problematic" is questionable and somehow self-contradictory with this paper's philosophy of choosing outdated simple queries. 
- On the one hand, scores on the previous benchmarks [1-5] are far from saturated because the average score is still less than 50 out of 100. Optimizing empirical models on previous benchmarks will also benefit the performance of the proposed "hard" benchmark. Meanwhile, recognizing the importance of training edges, although motivating the CQD-hybrid in this paper, is not new to the community because it is practiced in QTO [6] and later followed by FIT [3]. It hardly says why these findings are essential.
- On the other hand, the paper only focuses on the simpler query forms proposed in [1]. One might argue that such simple query forms cover a sufficiently large portion of real-world user cases, so the choice of such forms is reasonable. The same practical point of view can also apply to the easy-hard contrast produced by whether the reasoning triples of a query are observed or not. Although the previous benchmark consists of too many observed triples, as shown in this paper, it can also be reasonable by arguing that the train graph consists of a sufficiently large portion of knowledge that users are interested in.

### Questions
Please respond to my two concerns in the weakness part.

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper studies the complex query answering task on knowledge graph and questions whether the data in existing dataset is unqualified. To be specific, the author proposes to term those pairs of complex query & answers which the corresponding reasoning process can leverage some parts of the knowledge in the training graph as partial inference pair and thus evaluate existing CQA models on full-inference pairs. This paper conducts extensive experiments to showcase this observation and analysis on some certain query types like 2u.

### Strengths
1. The key observation of this paper is interesting. The partial-inference pair is prevailing in existing datasets and the paper shows that full-inference pair is empirically much harder than partial-inference pair and thus the reasoning ability of SOTA CQA models may be less powerful than our imagination.

2. This paper's case study and deep analysis are praiseworthy. For example, the paper studies the query type with union and additionally finds that if we filter out such pairs that can be accessed by just one link, the performance of 2u will increase significantly, similar to that of the 1p query type.

### Weaknesses
1. Firstly, the discussion of the query type is constrained in this paper. Most dominantly, almost all researches conducted on complex query answering in recent years included negative queries yet this paper avoids that completely. Perhaps it's a drawback of their model design originating from the initial CQD paper, or perhaps the reasoning process defined in this paper fails in a negative query. Either way, it's problematic as the scope of the query type it investigated is strictly contained. The paper's analysis and conclusions are therefore limited to a subset of complex queries, failing to address the broader challenges in complex query answering.

2. The claim of SOTA CQA models fail significantly on so-called full-inference pair is questionable, as it doesn't include recent models that are built by symbolic search algorithms, like QTO[1] and FIT[2], which use neural link predictors combined with searching algorithms and seems to bypass the challenges proposed by full-inference pair.  As the paper itself proposes a symbolic search method, the missing baselines in other symbolic search methods is questionable. This omission undermines the paper's central claim by not comparing against relevant state-of-the-art approaches.

3. The comparison of 2u-filter is dubious. As the definition of union query just requires one link to hold in the graph, I do not see the necessity to do such filtering as Figure A.1 as it more resembles 2i query type after filtering. The filtering process seems to alter the fundamental nature of the union query, making the comparison less meaningful. By requiring both links to be missing, the filtered 2u query effectively becomes a different type of query, and the reported performance gains may not reflect the true capabilities of models on standard union queries.

### Questions
The comparison of 2u-filter is dubious. As the definition of union query just requires one link to hold in the graph, I do not see the necessity to do such filtering as Figure A.1 as it more resembles 2i query type after filtering.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The hard answers studied in complex logical queries are those that cannot be retrieved due to gaps in the knowledge graph (KG). This paper reclassifies these hard answers into two categories: full-inference and partial-inference The authors argue that partial inference can be reduced into simpler query types and partial inference occupies the majority of  existing datasets, BetaE. They discover that current models perform poorly on full inference tasks and propose a new benchmark to highlight this issue. Additionally, they introduce a new model specifically designed to tackle partial inference answers by explicitly retrieving existing links from the training knowledge graph.

### Strengths
1. This paper find a interesting weakness of existing CQA dataset and propose a useful method and benchmark.
2. This paper is well written and easy to follow.

### Weaknesses
1. The baselines lack of the symbolic methods like QTO and FIT, which are the mainstream of CQA methods. The used CQD is a old symbolic method.
2. BetaE have three KGs but only two KGs are presented in the paper.
3.  The argument of 'reduced to easier types' is weird because query types with less constraint will be easy to solved than original query types, for example the performance of 3i is good than 2i. I suggest the authors use a preciser expression.
4. I disagree your arguments that your proposed CQD-hybrid is the first an hybrid solver. QTO and FIT use the information from observed KG and trained link predictor to construct the matrix and can use the hybrid information of train edges and pre-training embeddings.
5. Because of Weak 4, I am curious that the performance of symbolic method QTO and FIT as they already have the hybrid information.

### Questions
1. Do you vary your argument in train queries? I am wondering  the phenomenon that existed CQA models fails is caused by the train datasets have too many partial inference answers. Thus I am curious about the performance of symbolic search methods where these methods don not use queries to train.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, authors re-examine the existing problems of knowledge graph complex reasoning datasets. The authors propose that the current dataset cannot effectively measure the generalization ability of the reasoning model, that is, the complex queries in the dataset can be solved by the triples leaked in the training graph, and verifies their conjecture through extensive and sufficient experiments. Further, the authors propose a new set of benchmarks to more effectively measure the performance of complex reasoning models.

### Strengths
* Motivation of the paper is novel, and the re-examination of existing benchmarks is valuable.
* Experiments in this paper can support the conclusion well.
* Writing of the paper is good, the structure is clear, the layout is good, and it is easy to follow.

### Weaknesses
 * Lack of discussion of related work, if the space is limited, this part can be placed in the appendix.
* In Section 5.1, the author proposes a CQD-Hybrid solver. Actually, the practice described in the paper is very similar to the QTO [1] and I think the difference should be cited and discussed.
* As an effort to propose new benchmarks, the experiments for the new benchmark are a little less. More baselines, some case analysis, etc., should be added.
* Some typos, such as line.468: 50.000
* The problem of information leakage in training graphs can be solved well by the inductive setting in naive knowledge graph reasoning (one-hop reasoning) task. Actually, there have been some attempts to establish inductive settings in CQA[1][2], where there will be no information leakage because the training and test graphs are different. How do you think this paper differs from these works?
* In my opinion, link leaks in the training graph only affect the GNN based and neural link predictor based methods, while the embedding-based methods do not take advantage of the information in the training graph (except for 1p queries). Why does this type of approach also degrade on the new benchmark?

### Questions
* The problem of information leakage in training graphs can be solved well by the inductive setting in naive knowledge graph reasoning (one-hop reasoning) task. Actually, there have been some attempts to establish inductive settings in CQA[1][2], where there will be no information leakage because the training and test graphs are different. How do you think this paper differs from these works?
* In my opinion, link leaks in the training graph only affect the GNN based and neural link predictor based methods, while the embedding-based methods do not take advantage of the information in the training graph (except for 1p queries). Why does this type of approach also degrade on the new benchmark?
* As mentioned in weakness, what's the difference between CQD-Hybrid and QTO?


[1] Inductive Logical Query Answering in Knowledge Graphs. In NeruIPS 2022.

[2] Type-aware Embeddings for Multi-Hop Reasoning over Knowledge Graphs. In IJCAI 2022.

### Soundness
3

### Presentation
3

### Contribution
2

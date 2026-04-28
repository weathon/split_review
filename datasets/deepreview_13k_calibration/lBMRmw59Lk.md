# Rethinking Graph Neural Networks From A Geometric Perspective Of Node Features

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 6, 8

## Abstract
Many works on graph neural networks (GNNs) focus on graph topologies and analyze graph-related operations to enhance performance on tasks such as node classification. In this paper, we propose to understand GNNs based on a feature-centric approach. Our main idea is to treat the features of nodes from each label class as a whole, from which we can identify the centroid. The convex hull of these centroids forms a simplex called the feature centroid simplex, where a simplex is a high-dimensional generalization of a triangle. We borrow ideas from coarse geometry to analyze the geometric properties of the feature centroid simplex by comparing them with basic geometric models, such as regular simplexes and degenerate simplexes. Such a simplex provides a simple platform to understand graph-based feature aggregation, including phenomena such as heterophily, oversmoothing, and feature re-shuffling. Based on the theory, we also identify simple and useful tricks for the node classification task.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a novel perspective for studying datasets used in node classification, which focuses not on the graph structure but on the "behavior" of node features, in particular their centroids.
The authors leverage geometric concepts to enhance class representation and model interpretability. Each class is represented through probabilistic centroids and geometric centroids organized within simplexes in lower-dimensional spaces. This approach offers new insights into why it is challenging to achieve significant results on certain datasets, identifying simple strategies that can improve node classification performance in GNN models, such as in the case of degenerate simplex and the feature re-shuffling phenomenon.

### Strengths
The first strength is that the paper introduces a new approach to studying datasets, which in turn allows for the analysis of GNN performance based on input datasets. I also find it particularly interesting that the method is entirely based on node features, making the study simple and fast.

I also believe that other strengths include the solid theoretical support provided by the authors and, above all, the practical aspect of the study, which proposes simple and effective strategies capable of improving GNN performance as well as model interpretability.

### Weaknesses
The paper is well-written and rich in content; however, it is somewhat difficult to follow due to the abundance of theoretical contributions and the numerous references to the appendix. I understand, however, that with the page limit, it is challenging to organize all the material effectively.

It should also be noted that some assumptions are rather optimistic: for instance, even in the simple Lemma 1, I would expect some overlapping in reality. Nonetheless, I understand that this is intended as a starting point.

Another shortcoming is that the studies conducted so far have limited applicability, as the approach mainly focuses on node features and datasets used for node classification.  I was wondering if it might be possible to gain some insight in the case of graph classification as well.

It also seems that a thorough discussion on scalability is lacking (or maybe I missed it): what happens, for instance, when the graphs are not very large or when the features are low-dimensional? 
I did not notice a section dedicated to the actual limitations of the method.

### Questions
In Figure 5, I would add class centroid as well.
I would also use in fig. 1 Squirrel.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper "Rethinking Graph Neural Networks from a Geometric Perspective of Node Features" proposes a new framework for understanding Graph Neural Networks (GNNs) by focusing on node features rather than solely on graph topology. The authors introduce the "feature centroid simplex," a geometric structure representing the distribution of node features across classes, as a tool to explore phenomena like heterophily (when nodes connect across classes), oversmoothing, and feature reshuffling in GNNs. This feature-centric perspective addresses limitations of traditional topology-based approaches, especially for datasets where graph structure alone does not fully capture data complexity. The concept of the "feature centroid simplex," a high-dimensional simplex formed by the centroids of node features within each class introduced by the authors, is presented as a geometric model that enables a deeper understanding of key GNN phenomena, such as heterophily, oversmoothing, and feature aggregation. By studying the convex shapes of these simplexes and their proximities, the paper explains the behavior of GNNs across different graph structures, especially on challenging tasks like node classification. It also suggests simple, graph-independent tricks to improve GNN performance, such as early stopping and feature normalization, particularly on heterophilic datasets where standard GNNs often struggle. The paper works to provide a unified geometric framework to enhance theoretical understanding and practical efficacy in GNN applications​

### Strengths
The paper’s novelty lies in its shift from topology-based to feature-centric analysis in understanding GNNs, introducing the concept of a "feature centroid simplex" formed by class-based feature centroids, which allows GNN behavior to be studied within feature spaces rather than solely relying on graph structure. By applying coarse geometry to examine simplex shapes, the paper offers new insights into common GNN challenges, including heterophily, oversmoothing, and feature variance. This graph-agnostic, feature-driven approach provides a unique way to assess dataset-specific difficulties, such as classification "hardness," focusing on intrinsic feature properties rather than external graph characteristics. The primary contributions of the paper include developing a theoretical framework based on the feature centroid simplex, which offers new perspectives on GNN phenomena. It also provides practical, graph-independent tricks like early stopping and adding edges between nodes of the same class to improve GNN performance in difficult settings. These insights are supported by empirical validation on heterophilic datasets such as Actor, Chameleon, and Squirrel, where the feature-centric approach and proposed techniques demonstrate substantial improvements over traditional GNN models.

The paper provides a clear, succinct abstract that outlines its goal to rethink Graph Neural Networks (GNNs) from a feature-centric, geometric perspective. The structure flows logically from a foundational background to theoretical concepts like the feature centroid simplex and quasiisometry, and then to practical applications for GNN improvement. Each section builds upon the previous, and a notation table in the appendix enhances clarity. 

The paper demonstrates theoretical rigor with a strong foundation in geometric and probabilistic models, supported by detailed proofs in the appendices

Visuals, including feature centroid simplexes, effectively clarify complex ideas, and experiments are presented with comprehensive tables and discussions on framework effectiveness across datasets. 

Appendices are well-used to include supplementary proofs, notation, and experiments, keeping the main content focused while providing technical depth for interested readers.  Overall, the structure, visual aids, and appendices provide a strong foundation for understanding the paper’s contributions.

The provided illustration were found to be well done and very informative.

### Weaknesses
The level of novelty and degree of contributions in the work presented were not fully convincing and could perhaps be made clearer by making explicitly the degree to which the proposed work contributes as well as a more explicit discussion on where the proposed work has limitations. For example, the feature-centric approach, while novel, may have limited applicability in cases where feature information alone is insufficient, or where the graph structure itself is crucial, such as in social networks or molecular graphs where node connections are integral to understanding relationships. The framework and tricks presented are mainly beneficial for heterophilic datasets; however, for homophilic graphs, where existing GNN models already perform well, the proposed tricks may not offer significant improvements. Additionally, the tricks suggested, such as early stopping and feature normalization, are simple yet not inherently innovative, as these techniques are standard practices in machine learning for managing overfitting and feature scaling; the novelty lies more in their application to GNNs than in the techniques themselves.

Another limitation is the paper’s reliance on certain assumptions about feature distribution and convexity, which may not hold across all types of graph data, potentially limiting the framework’s generalizability, especially when features are not easily separable or node classes lack well-defined centroids.

In terms of novel contributions, the paper's innovation is somewhat limited. Although the feature-centric perspective provides a new approach, it builds on well-known GNN challenges such as oversmoothing and heterophily without fundamentally altering GNN structures or proposing new architectures. Thus, the framework offers insights rather than resolutions to these issues. Furthermore, the recommended tricks, while practical, are widely used machine learning techniques, and applying them to GNNs does not significantly advance the field. The empirical comparisons primarily focus on baseline models and lack a thorough analysis of how more advanced GNNs, with adaptive architectures or attention mechanisms, might perform with these tricks, which constrains the paper’s insights into how its geometric perspective could be leveraged in state-of-the-art models.

The paper would benefit from an experimental evaluation with datasets with low label informativeness to assess the quality of their feature centric approach such as those offered by recent works such as “A critical look at the evaluation of GNNs under heterophily: Are we really making progress?” by Platonov et. al. A more in depth comparative analysis to other similar methods which perform topological or geometric analysis of the feature space to implore learning model performance such as persistence landscapes or persistence images by Adams et. al.and other methods such as those discussed in Architectures of Topological Deep Learning: A Survey of Message-Passing Topological Neural Networks by Papillon et. al. should be experimentally compared to and definitely discussed in the background and related works section. The authors should also consider comparing to other geometry based approaches as presented in “Feature Expansion for Graph Neural Networks” by Sun et. al. or “A Survey of Geometric Graph Neural Networks: Data Structures, Models and Applications” by  Han, Cen, and Wu et. al. however I have not extensively read these last two works.

On reading the paper, I was not convinced of the validity and generalized applicability of the approach due to the assumptions that were required in order to provide proof of necessary lemmas and theorems as presented and needed to support the paper's claims. A more detailed analysis of the bounds in the number of sample points is needed in order for the probabilistic claims to be met such as convex positioning or the number of samples needed to justifiably use the geometric centroid of a class.

The related works discussed in the introduction and background should be expanded as well as more explicit discussion of the proposed paper in the context of contemporary literature. An more explicit discussion with the novelty of the current work could be made more persuasive. A more explicit limitations section and discussion would also be appreciated.

Definitions of concepts used and background information is at times distributed throughout the paper rather than presented at first in background and related work. Background and foundational concepts should be presented earlier and consolidated.

### Questions
Can the assumptions made to provide proofs to lemmas and theorems be listed and justified as reasonable?

Can the limitations caused by the assumptions made be discussed? 

Can the limitations of the approach be made more explicit, and despite those limitations, the novely and contributions of the proposed approach be justified?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces a *feature-centric approach* to analyzing GNNs by examining the node embeddings for each class in feature space  rather than graph topology. The authors define a *feature centroid simplex* and leverage coarse geometry to explore GNN behaviors like heterophily and oversmoothing, offering new insights and simple techniques for improving node classification performance. They make extensive experiments to validate their analysis

### Strengths
1. The paper introduces an innovative approach to studying GNNs by focusing on the clustering behavior of node embeddings for each class in feature space.
2. By defining a *feature centroid simplex* as a (K-1)-simplex using the centers of these clusters, where K is the number of classes, the authors provide a geometric representation in $\mathbb{R}^m$ that effectively captures class relationships.
3. They use this geometric perspective to explain key GNN challenges, such as homophily/heterophily and oversmoothing, in terms of the feature centroid simplex.
4. The mapping of the probability simplex to the *feature centroid simplex* is particularly insightful, as it reveals additional learning opportunities within the feature space.

### Weaknesses
1. **Presentation Quality**: The paper’s main weakness lies in the presentation, which does not effectively communicate its promising ideas. Although grounding concepts in mathematical rigor is essential, the technicalities in this paper obscure the overall clarity and may hinder comprehension.

2. **Mathematical Statements**: The mathematical claims in Sections 2 and 3 lack interpretability. The space of graphs with feature vectors is vast and diverse, requiring more restrictive assumptions or narrowing to particular subclasses for these statements to hold meaning. For instance, Lemma 1, which relates the feature centroid simplex to the probability simplex, is difficult to justify without more explicit assumptions on the feature space and the node embeddings. Specifically, it's unclear how the feature dimension m being large enough guarantees the stated relationship, and a more detailed explanation of the underlying assumptions is needed. Similarly, Lemma 2 could benefit from a focus on the geometric simplex rather than the ambiguous term $e_c$, which complicates the exposition. The use of probabilistic centroids, while mathematically convenient, makes it harder to connect the theoretical results to practical observations. Such imprecise statements make the argument obscure and challenging to follow.

3. **Distinction of Homophily and Heterophily**: The idea to distinguish homophily and heterophily through feature centroid differences or clustering behaviors of node neighborhoods is promising. However, adding a geometric quantification—such as using the diameter, the volume of the simplex, or embedding of node neighborhoods with normalization—would strengthen the approach and add greater empirical rigor. For example, a measure of the dispersion of node embeddings within each class could provide a more concrete way to quantify homophily and heterophily, rather than relying on qualitative observations of centroid differences.

4. **Oversmoothing Analysis**: Analyzing changes in the feature centroid simplex under oversmoothing is an excellent idea, with the potential to develop a metric for measuring oversmoothing. To achieve this, the paper would benefit from more precise definitions of the geometric quantities involved, along with a demonstration of changes in these quantities across epochs. For example, seeing the changes in the volume of feature centroid simplex under each epoch for oversmoothing would be very interesting. Specifically, the paper should define how the volume is computed in the high-dimensional feature space, and provide empirical evidence that this volume decreases with increasing GNN layers.

5. **Incremental Improvements**: Although the simple tricks suggested are useful, they offer only incremental improvements. A more substantial contribution, such as a more comprehensive approach that integrates the meaningful information (e.g., some geometric quantities) obtained from feature centroid simplex approach to ML pipelines, would significantly strengthen the impact of this work. For instance, the paper could explore how the geometric properties of the feature centroid simplex can be used to design new GNN architectures or training strategies, rather than just applying simple normalization tricks.

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes to look at the node features from a simplex perspective. The main observations are a new view on oversmoothing and homo/heterophily. Further, some tricks (feature normalization and feature shuffling) are proposed to improve empirical results.

### Strengths
Node features and their proper handling has proven effective for a number of graph-learning tasks, so focusing on those instead of taking features as a second-class citizen after structure makes sense.
The main contribution of the paper is a theoretical model which allows to analyze GNNs wrt overfitting and homo/heterophily.
Experiments show that the presented tricks can indeed improve empirical performance.

### Weaknesses
The paper is unnecessarily hard to read. There is a lot of notation and the definitions and usage are sometimes far away (including non-standard notation). For instance, the initial formal definitions in section 2.1 introduce $m$ as the feature dimension, but then also use $m_1$ and $m_2$ as seemingly unrelated constants, creating confusion. The text refers to the appendix for dataset examples, when simply naming two datasets would improve clarity. The distinction between individual feature components in [0,1] and feature vectors $x^i \in [0,1]^m$ is not immediately clear, leading to difficulty in understanding the notation for features $x^1,\dots,x^n$. The use of "for each index $i$" instead of "For each node $v_i$ with $i = 1,\dots n$" further complicates the initial reading. The variable $\gamma$ is introduced without clear definition, and the phrase "over C" is missing, making it difficult to follow the logic. The probabilistic node feature model is not motivated. Since all results are based on this model, it would be good to at least argue in how far the assumptions are ``natural''. E.g. what does it mean for features to be convex? And does that appear in practice? (again, only a reference to the appendix...) None of the theorems as an extensive description of what it means or why it is important. Usually its just the theorem and nothing else. E.g. 314 mentions an example that is no longer part of the main text. The proposed feature normalization is as informal as it can get (which is surprising, given the formality in the rest of the paper). So its unclear whether each feature (across nodes) or each node's feature vector is normalized. The former is a standard trick and not new at all, so I guess its the latter. The feature-shuffling trick is also not well-explained (but well-motivated). How would that be applied in a real-world dataset where e.g. 5-10% of the nodes are labeled? 

Further small points:
- 226: G is undefined. (or rather, the quantifier is unclear)
- 220: please make clear that the model in the paper is not quite the original GCN but rather the version without sqrt(d). I believe that moving the formal definition of GCN in front of 224 would significantly improve readability.
- 406: how does this now differ from the spectral result? (looks pretty much like the same result)
- 472: the list of tricks that is applied did not make it into the main paper. I guess that should be changed.
- 527: please repeat what $\ell_v$ is about, this is not standard and most of all not just some standard accuracy.
- 537: "many" could be made specific.

### Questions
Overall, I believe that a long version of the paper (e.g. one for arxiv), with all examples, filler texts and some proofs re-inserted is a much better version of the paper. Currently, the setup is not well-motivated and the paper not self-contained. It also felt overly formal over large parts of the text.

I would thus like to encourage to work on the presentation.

### Soundness
3

### Presentation
3

### Contribution
3

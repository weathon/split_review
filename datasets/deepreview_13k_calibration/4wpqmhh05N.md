# The Mutual Information Matrix in Hyperbolic Embedding and a Generalization Error Bound

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 5, 3

## Abstract
Representation learning is a crucial task of deep learning, which aims to project texts and other symbolic inputs into mathematical embedding. Traditional representation learning encodes symbolic data into an Euclidean space. However, the high dimensionality of the Euclidean space used for embedding words presents considerable computational and storage challenges. Hyperbolic space has emerged as a promising alternative for word embedding, which demonstrates strong representation and generalization capacities, particularly for latent hierarchies of language data. In this paper, we analyze the Skip-Gram Negative-sampling representation learning method in hyperbolic spaces, and explore the potential relationship between the mutual information and hyperbolic embedding. Furthermore, we establish generalization error bounds for hyperbolic embedding. These bounds demonstrate the dimensional parsimony of hyperbolic space and its relationship between the generalization error and the sample size. Finally, we conduct two experiments on the Wordnet dataset and the THUNews dataset, whose results further validate our theoretical properties.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper provides both theoretical and empirical analysis of Skip-Gram Negative-Sampling (SGNS) embeddings in hyperbolic space. While SGNS traditionally embeds words and contexts in Euclidean space (Word2Vec), the authors extend this approach to hyperbolic space using  Poincaré embeddings. Two types of errors are used to evaluate the embeddings: spatial error, which is influenced by the dimensions and structure of hyperbolic space, and generalization error, which measures the relationship between embedding error and sample size across different spaces. An empirical study of hyperbolic embeddings is conducted on WordNet and THUNews.

The authors investigate how hyperbolic distance relates to mutual information, deriving bounds on both spatial and generalization errors. Furthermore, they demonstrate that the distance, d(w,c), between w and c corresponds to the mutual information between w and c in a hyperbolic space. This finding helps to motivate the use of Poincaré embeddings.

### Strengths
The paper provides novel insights by studying the mutual information matrix in Skip-Gram Negative-sampling (SGNS) embeddings in hyperbolic space. In particular, demonstrating that distance in hyperbolic embeddings obtained by using SGNS equates to mutual information is an interesting finding that can motivate the use and further study of Poincaré embeddings in NLP. Additionally, the empirical result that hyperbolic embeddings are more unstable during training than their Euclidean counterpart and that more samples are needed to reduce training error can help guide further works in training hyperbolic embeddings.

### Weaknesses
Overall, the paper is extremely dense and difficult to follow because it provides little motivation or intuition for mathematical notation.

I understand that one of the paper's main contributions is to provide a detailed mathematical analysis of the mutual information matrix in hyperbolic embeddings. Still, some detail is unnecessary in the main body of the paper and hinders the reader's ability to read the paper. For example, results such as those in section 3.1 that use straightforward algebraic computations to show that distance approximates mutual information should be moved to the appendix. 

While the paper provides some nice theoretical insights, the methods used for the evaluation of hyperbolic embeddings with Skip-Gram Negative-Sampling are not robust.  Using the rank of the restored point-wise mutual information matrix as the sole metric to compare Euclidean hyperbolic embeddings is not particularly interesting. Investigating the performance of hyperbolic embeddings on word similarity tasks, e.g., WordSim-353 or SimLex999, would provide a meaningful quantitative comparison of using embeddings based in different spaces and help motivate the study of static, hyperbolic word embeddings. Further, comparing the performance of classification models that use standard Word2Vec embeddings and hyperbolic Skip-Gram Negative sampling embeddings would provide a much stronger motivation for the paper.

### Questions
1. 263-264: I don’t understand the reasons for setting $V_{w} = V_{c} = V$. Can you elaborate more on why this setting is used? If it is common practice, there should be some citations. 

2. It would be helpful to provide a clear definition of parsimony in Section 3.2

### Soundness
2

### Presentation
2

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
the paper proposed to replace the Euclidean embeddings learned in word2vec with Hyberpoblic embeddings specifically with Poincare geometry. The method is straightforward - rather than using dot-product, a Euclidean-space similarity measure, the submission measures the distance between two word vectors on a Poincare disk. However, the evaluation approach puzzles me.

### Strengths
1. It directly replaces the distance/similarity measure in learning word2vec, which makes the approach easy to conceptualize.
2. Under mild assumptions, the submission provides interesting generalization bounds.

### Weaknesses
It puzzles me that there are many simple 'real-world'-ish datasets for evaluating learned word embedding, but somehow, the submission doesn't provide any of them. IMO, the submission conducts the study as if the problem is orthogonal to NLP.

1. Having an understanding of the sample complexity and how the error bound of the estimation depends on the sample complexity is generally informative, however, in recent years, we have found ourselves in a wacky situation that, for a model to generalize, the training loss just needs to be small, but it doesn't need to be very small, because many plateaus in the loss landscape provide models with good generalization, thus, having a theoretical understanding of the loss function or the error bound becomes somehow outdated.

2. A crucial aspect or consideration of learning on massive corpora is the complexity of the algorithm itself, which the submission doesn't mention.

3. The submission didn't use common datasets for learning word embeddings, nor does it provide any evaluation on common benchmarks, e.g. SimEval or SentEval.

### Questions
n/a

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
3

### Summary
Hyperbolic embeddings were introduced in the literature as an alternative to the embeddings in Euclidean space. This paper provides an analysis of the skip-gram embedding model in hyperbolic space. The authors offer their take on many dimensions of the hyperbolic embeddings, including their connection to the mutual information matrix, generalization capabilities (with theoretical proof), and required sample size/training stability. Theoretical results are further supported by empirical results on two datasets: Wordnet and THUNews.

### Strengths
- I strongly believe exploring the embedding spaces beyond Euclidean space is crucial for the field
- Theoretical and empirical results are provided
- Reflection on the advantages (low-dimensionality) and disadvantages (training instability, large sample size etc.)

### Weaknesses
 -  Although it's crucial and interesting to explore various properties of hyperbolic embeddings, they do not exist in a vacuum, so it would be useful to see the performance of the embeddings on downstream tasks
- Provided experimental setup and results are hard to follow (see questions)

- Why choose 400 Euclidean dimensionality and 2 for Poincare?
- Table 1,2,3: I don't really understand the reported numbers (what is the distance function exactly in Table 1? What is the distance in Table 2?). I suggest you give an explicit interpretation of those numbers to make it clear to the reader
- There is a conclusion that training with hyperbolic embeddings takes more time and iterations. However, it's unclear from your experiments if Poincare space embeddings can achieve the same loss as Euclidean ones with a higher number of samples (or iterations) (Table 6 and Table 7) or it is still behind the Euclidean embeddings
- Lime 418: `Moreover, hyperbolic space requires more than 70,000 samples to achieve adequate training`: what is _adequate_? How do you define it?

- Table 7 has the incorrect title. It's 400-dimensional Euclidean space, not Poincare space

### Questions
__Questions__:
- Why choose 400 Euclidean dimensionality and 2 for Poincare?
- Table 1,2,3: I don't really understand the reported numbers (what is the distance function exactly in Table 1? What is the distance in Table 2?). I suggest you give an explicit interpretation of those numbers to make it clear to the reader
- There is a conclusion that training with hyperbolic embeddings takes more time and iterations. However, it's unclear from your experiments if Poincare space embeddings can achieve the same loss as Euclidean ones with a higher number of samples (or iterations) (Table 6 and Table 7) or it is still behind the Euclidean embeddings
- Lime 418: `Moreover, hyperbolic space requires more than 70,000 samples to achieve adequate training`: what is _adequate_? How do you define it? 

__Writing__:
- Table 7 has the incorrect title. It's 400-dimensional Euclidean space, not Poincare space

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper discusses the relationship between the point-wise mutual information matrix and the hyperbolic distance. Furthermore, the authors establish generalization error bounds for hyperbolic embedding. These bounds demonstrate the dimensional parsimony of hyperbolic space and its relationship between the generalization error and the sample size. Experiments on the Wordnet dataset and the THUNews dataset validate the theoretical properties.

### Strengths
1) Connecting hyperbolic embedding with mutual information is interesting.

### Weaknesses
1) The motivation of connecting hyperbolic embeddings and PMI is unclear. Both are distance measure, hyperbolic distance captures similarity of hierachies, while PMI quantifies the discrepancy between the probability. What do you mean by the “equivalence between the Gramian matrix in hyperbolic embedding and the dimension of the space”? 
2) What is the research questions that you want to answer in the Experiment section? The authors said that the theoretical findings are evaluated by conducted the experiments. However, it is unclear how the experimental results related to the theoretical findings. Which theorems (theorem 1 or 2? ) you want to answer? It would be much clear if the authors list the research questions. What do you really want to evaluete and compare. 
3) I could not understand what do the tables in the experiment section want to tell us? perhaps the authors want to show some correlation between dimension and mutual information matrix? then it is better to plot it with some line plots.

### Questions
See my questions in Weaknesses.

### Soundness
2

### Presentation
1

### Contribution
2

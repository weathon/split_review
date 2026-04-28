# Zero-Shot Learning of Causal Models

- Decision: Reject
- Avg Score: 6.25
- Scores: 8, 6, 5, 6

## Abstract
With the increasing acquisition of datasets over time, we now have access to precise and varied descriptions of the world, capturing all sorts of phenomena.
These datasets can be seen as empirical observations of unknown causal generative processes,  which can commonly be described by Structural Causal Models (SCMs).
Recovering these causal generative processes from observations poses formidable challenges, and often require to learn a specific generative model for each dataset.
In this work, we propose to learn a \emph{single} model capable of inferring in a zero-shot manner the causal generative processes of datasets. 
Rather than learning a specific SCM for each dataset, we enable the Fixed-Point Approach (FiP) proposed in~\cite{scetbon2024fip}, to infer the generative SCMs conditionally on their empirical representations.
More specifically, we propose to amortize the learning of a conditional version of FiP to infer generative SCMs from observations and causal structures on synthetically generated datasets.
We show that our model is capable of predicting in zero-shot the true generative SCMs, and as a by-product, of (i) generating new dataset samples, and (ii) inferring intervened ones.
Our experiments demonstrate that our amortized procedure achieves performances on par with SoTA methods trained specifically for each dataset on both in and out-of-distribution problems. 
To the best of our knowledge, this is the first time that SCMs are inferred in a zero-shot manner from observations, paving the way for a paradigmatic shift towards the assimilation of causal knowledge across datasets.
\nnfootnote{
$^*$Equal Contribution. Correspondence to: \texttt{t-mscetbon@microsoft.com}.}
\nnfootnote{
This work was done when Divyat
Mahajan was an intern at Microsoft Research. Cheng Zhang worked on this project when she was affiliated with Microsoft Research and she is currently with Meta.
}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Learning the causal generative process from observational data is a challenging problem bottlenecked by the necessity of learning a separate causal model for each dataset. This paper studies a unifying framework to enable zero-shot inference of causal generative processes of arbitrary datasets by training a single model. The authors adapt a recent advancement in causal generative modeling (FiP) to infer generative SCMs conditional on empirical dataset representations in a supervised setup, where the SCM is reformulated as a fixed-point problem. They propose an amortized procedure that takes in a dataset and its causal graph and learns a dataset representation. Then, the authors train a model conditioned on dataset embeddings to learn the functional mechanisms of the generative SCM. This framework enables both observational and interventional sample generation in a zero-shot manner. Empirical results show that the method performs competitively with baseline models for in-distribution and out-of-distribution settings.

### Strengths
- This paper is one of the first to consider generalizing the learning of functional mechanisms of structural causal models from arbitrary datasets and causal graphs and is a significant step toward building causally-aware foundation models.
- The paper is written well with clear intuitions and explanations as to how it relates to similar work (e.g., FiP).
- Although the assumptions are a bit strong (additive noise model, causal graphs known, noise variables known), the general idea of using an amortized procedure to approximate SCM distributions in a zero-shot manner is quite interesting.
- The empirical results are convincing and show interesting observations, especially the performance of sample generation under distribution shifts and as the causal graphs scale up. It is certainly impressive that Cond-FiP can approximate the SCM distribution of 50 and 100 graph nodes quite well given that it was trained on only datasets with 20-node graph size.

### Weaknesses
 - In a synthetic data scenario, assuming access to the noise samples is a feasible assumption, but for real-world datasets, this will not typically hold. Using the noise samples as the supervision for the dataset embedding model may easily become unrealistic. The authors have an evaluation on a real-world benchmark (Sachs) in the appendix where they fit a Gaussian model. However, interventional sample results are not provided. The reliance on noise samples for training the dataset embedding model is a significant limitation, as obtaining these samples is not feasible in most real-world scenarios. This limits the practical applicability of the proposed method, despite its theoretical appeal.
- I believe the idea to directly infer the SCM distribution under the additive noise model assumption is interesting. However, again, the feasibility of this assumption may not always hold. It is true that we often parameterize causal models as linear/nonlinear additive noise models, but this can be violated in practice. It seems that this approach would only hold under the strict assumption of additive noise models. The method's reliance on the additive noise model (ANM) is a strong constraint. While ANMs are commonly used, they do not capture the full complexity of real-world causal relationships, where non-additive noise or more complex functional dependencies may exist. This limits the generalizability of the approach to scenarios where the ANM assumption is violated.
- Knowledge of the causal graph for several datasets can potentially be a strong assumption. In real-world datasets, the causal graph may be unknown and must be discovered. However, for the sake of this work, the synthetic scenarios are good for proof of concept. The assumption that the causal graph is known for all datasets is a significant limitation. In many real-world scenarios, the causal structure is unknown and must be inferred from data, which introduces additional challenges and uncertainties. The method's performance in such settings is not explored, limiting its practical applicability.

### Questions
- Could the authors explain why Cond-FiP performs similar to some baselines in noise prediction and sample generation, especially when the node scale is the same or smaller than used in training? How is the FiP model implemented? In the original paper, it seems that the task is the recovery of the topological ordering. Is the FiP baseline here aware of the causal structure of datasets?
- How does the alternating application of transformer blocks E work? Is this just an alternating optimization method where you optimize for samples when nodes are fixed and optimize for nodes when samples are fixed?
- For zero-shot inference of the SCM distribution, what is the level of distribution shift that a new dataset can have for this method to be able to extrapolate well?
- The main capabilities of the proposed framework are noise prediction and observational/interventional sample generation. However, individual counterfactual sample generation is also important in many applications. Can this framework enable counterfactual inference?
- In the Adaptive Transformer Block, which iteratively updates the noise conditioned on the dataset embedding $z_{emb}$, can we interpret this as sort of a noise abduction typically performed in counterfactual inference?
- How exactly does one perform interventions in the Cond-FiP? It would be beneficial if the authors elaborate on this mechanism in the paper. From my understanding, we just feed in an intervened SCM causal graph with the mutilations and use the corresponding dataset embedding for conditional generation. However, this is not made very clear in the paper.

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
3

### Summary
The authors propose a novel method and task of inferring functional relationships of SCMs from observations and their associated causal structures in a zero-shot manner. The problem is well motivated by the literature. The main technical contributions of the work are the definition of Cond-FIP (modification to the FIP architecture), and the construction of the dataset embeddings (used to condition FIP). The latter is done by training the transformer-based encoder to predict the evaluations of the functional relationships over the distribution of SCMs. The former is done using the FIP architecture that takes as input sample embeddings conditioned on the SCM and is trained with the MSE objective on samples from multiple SCMs.

The method is evaluated in the synthetic setup on varying graph structures, functional relationships, and noises. It performs comparably to the selected set of baselines on noise prediction, sample generation, and interventional sample generation tasks.

### Strengths
1. The problem is well motivated by recent advances in the area, novel, and of interest to the community.
2. The method’s description is detailed and well-structured.

### Weaknesses
1. Experimental evaluation seems limited. The authors claim that their approach matches the performance of SoTA, but they only compare against a small set of methods. It seems natural that authors would compare against cited work (Javaloy et al., 2023; Khemakhem et al., 2021) and architectures used in causal discovery literature [1, 2], specifically methods that also perform functional causal mechanism inference, such as those based on normalizing flows or other deep generative models. The current comparison to DoWhy and DECI is insufficient to demonstrate state-of-the-art performance in the specific task of zero-shot SCM inference.
2. In various fragments of the text the authors claim that “this is the first time that SCMs are inferred in a zero-shot manner from observations“. While it is clear to me that this work combined with previous literature technically allows SCM inference (graph and functional relationships), this ability is not demonstrated nor evaluated in this work. The paper focuses on predicting samples and noise, but not on explicitly inferring the SCM, which is a crucial distinction. The claim of zero-shot SCM inference is therefore misleading without direct evaluation of the inferred SCM.
3. The method does not generalize well to larger datasets (as stated in Appendix C). This is an important limitation and should be stated explicitly in the main text. The lack of scalability to larger datasets significantly restricts the applicability of the proposed method in real-world scenarios, where datasets are often large and complex. The paper should provide a more thorough discussion of the factors limiting scalability and potential avenues for improvement.
4. The evaluation would be hard to reproduce as the details of train and test dataset generation are not provided. Specifically, the distribution of graph structures, the parameterization of functional relationships, and the noise models used in training and evaluation are not clearly specified. This lack of detail makes it difficult to verify the experimental results and to compare the method with other approaches.
5. Some parts of the method’s explanation are unclear to me. (see Questions)

### Questions
1. I have a hard time understanding the Generation with Cond-FiP paragraph. The \mathcal{T} symbol seems to have a different meaning in the Projection paragraph than in the Generation with Cond-FiP. Is it a notational error? Please clarify.  Also, what is the relation between eq. 5 and the equation in the Adaptive Transformer Block paragraph? They seem oddly similar yet, if I understand correctly, the \mathcal{T} denotes the whole generation process described in the Adaptive Transformer Block paragraph.
2. The Interventional Predictions explanation is unclear to me. Could you elaborate more on how you “modify in place the SCM obtained by Cond-FiP”?
3. Could you provide more details on the generation of the datasets? What is the density of the graphs used in training and evaluation? What are the differences in the parametrization of functional relationships between P_in and P_out?
4. What kind of regressor was used as a causal mechanism in DoWhy? What architecture was used in DECI?
5. What is the role of DAG attention in dataset embedding? Can you elaborate on what would happen if you were to use standard dot product attention in the dataset encoding phase?
6. It seems that the performance of baselines on RFF OUT dataset degrades significantly compared to RFF IN. Could you explain why?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes to amortize the learning of a conditional version of FiP to infer directly the generative SCMs from observations and causal structures in a zero-shot manner.

### Strengths
1.The idea of zero-shot learning with conditional FiP is interesting. 

2.The problem studied is important in the sense that zero-shot learners are commonly needed to finish the tasks.

### Weaknesses
1.The theoretical  justifications need to be improved.
2. Some experiments are missing.

### Questions
1.The theoretical foundation of "ZERO-SHOT LEARNING OF CAUSAL MODELS" indeed needs to be improved, given its complexity and the challenges it presents in the field of machine learning. Because the cross domain SCM difference seems to be significant. I still feel puzzled why zero shot learning theoretically works. Is there problems such as incapability of the observation-based learning with conditional FiP?

2.In the experimental section, I think more comparisons are needed. For example in DoWHY dataset, you may vary the node number and more generative mechanisms. Also, some ablations study of the important modules of FiP (e.g., encoder) should be presented since this seems to be an important factor for the final results.

3.I still feel that the interventional and sample generation can be more comprehensive. Is there any demo example to show that how your method differs from others? I guess that which node you manipulate still has a huge impact on the result. Am I right or not?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a method to learn a single model capable of inferring the causal generative processes of datasets in a zero-shot manner, rather than learning a specific model for each dataset. The general idea is to amortize the learning of a conditional version of the FiP architecture, which can infer the generative SCMs directly from observations and causal structures on synthetically generated datasets.

### Strengths
Zero-shot learning of a causal model is an important task, potentially due to the limitation of the training dataset when training the model. So I believe the task proposed by the paper is highly motivated. Additionally, the paper is written in a structured way.

### Weaknesses
1. I would suggest author to either use a figure or introduce a bit more background of the idea of amortized causal learning in related works.

2. In background on causal learning, I still don't know how to compute H. and what $Jac_x$ is. Also, $d_n$ and M are not defined.

3. In training setting, I don't understand how to use noise samples. In equation (1), they seem to be residual terms but in Section 3.1, they are said to play the rule of the target variable.

4. Do we need specific requirements on training data? Are they supposed to cover as many as domains?

5. Why modeling noise will help zero-shot ability of SCM? I wish the paper gives more explicit explanations.

6. In Table 2 and Table 3, it seems that sometimes Cond-FiP has the worse performance than FiP. This needs to be explained.

### Questions
Please see weakness above.

### Soundness
3

### Presentation
3

### Contribution
3

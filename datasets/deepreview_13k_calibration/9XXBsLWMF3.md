# PRUC & Play: Probabilistic Residual User Clustering for Recommender Systems

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 3, 5, 5

## Abstract
Modern recommender systems are typically based on deep learning (DL) models, where a dense encoder learns representations of users and items. As a result, these systems often suffer from the black-box nature and computational complexity of the underlying models, making it difficult to systematically interpret their outputs and enhance their recommendation capabilities. To address this problem, we propose *Probabilistic Residual User Clustering (PRUC)*, a causal Bayesian recommendation model based on user clustering. Specifically, we address this problem by (1) dividing users into clusters in an unsupervised manner and identifying causal confounders that influence latent variables, (2) developing sub-models for each confounder given the observable variables, and (3) generating recommendations by aggregating the rating residuals under each confounder using do-calculus. 
Experiments demonstrate that our *plug-and-play* PRUC is compatible with various base DL recommender systems, significantly improving their performance while automatically discovering meaningful user clusters.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper proposes Probabilistic Residual User Clustering (PRUC) for interpretability and computational complexity.\
PRUC is a causal Bayesian model that clusters users and identifies influential causal factors.\
PRUC enhances recommendations by modeling these clusters, applying confounder-specific sub-models and do-calculus.

### Strengths
1. The paper includes solid mathematical equations and derivations, which lend rigor to the proposed approach and offer a detailed understanding of the methodology.
2. Extensive experiments provide robust validation of the model's effectiveness, demonstrating its impact across various evaluation metrics and base recommender systems.

### Weaknesses
1. The presentation could benefit from refinement for clarity and conciseness.
For instance, Equation 11 seems self-evident and might not require such an extensive derivation, as it could detract from the focus on more critical aspects.
2. The motivation for employing confounders or clustering to enhance interpretability lacks clarity.
A more robust explanation of why these techniques specifically contribute to interpretability and how they address issues in recommendation systems would strengthen the paper.
3. The complexity and scalability of the approach are not thoroughly addressed.
Providing insights into the computational demands of the clustering process and the scalability of the model when applied to large datasets would enhance its practical relevance.
4. The paper would benefit from a more detailed evaluation of the quality of clustering and the confounder identification process.
Additional metrics or analyses could validate the interpretability and meaningfulness of the clusters and confounders.

### Questions
Please refer to weaknesses.

### Soundness
2

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
3

### Summary
The paper presents Probabilistic Residual User Clustering (PRUC) as a solution for challenges in modern recommender systems relying on deep learning models. These systems are often complex and lack transparency, making it difficult to understand and improve recommendations. PRUC automatically categorizes users into clusters, identifies causal influences on hidden variables, and constructs specialized models for each cluster based on causal reasoning. By combining rating residuals based on causal factors using do-calculus, PRUC enhances recommendation quality. Experimental results indicate that PRUC can seamlessly enhance various deep learning recommender systems, leading to performance improvements and the discovery of meaningful user groupings in an automated fashion.

### Strengths
1. The authors designed a plug-and-play PRUC to enhance the performance of existing DL-based recommenders, capable of discovering meaningful user clusters and improving the interpretability of recommendation results.

2. The authors simulated cold-start scenarios to test the PRUC method, validating its corresponding performance.

### Weaknesses
1. The experimental description in the paper is unclear. Why did the authors choose to conduct tests in cold-start scenarios rather than performance tests in full-shot scenarios? What are the specific meanings of source domain and target domain in the experimental section? Will the base models be pre-trained on the source domain?

2. The lack of a more direct case study to demonstrate the role of user clustering makes it difficult to understand the motivation behind the paper.

3. The selection of base models is limited, lacking some common collaborative filtering (CF) and GNN-based recommendation system methods, such as NCF [1] and LightGCN [2].

### Questions
Please refer to the issues mentioned in the Weaknesses section.

### Soundness
3

### Presentation
2

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
This paper presents Probabilistic Residual User Clustering (PRUC), a novel causal Bayesian model for recommendation systems that enhances interpretability and mitigates biases in deep learning-based recommenders. PRUC adopts a plug-and-play approach, making it compatible with various existing DL recommendation models. The experimental results demonstrate that PRUC consistently enhances the performance of multiple base DL recommender systems by addressing biases and uncovering latent user groupings.

### Strengths
1.	This paper introduces an innovative recommendation approach that uniquely applies causal inference to deep learning recommenders, addressing interpretability and bias correction.

2.	This paper addresses critical limitations in existing DL-based recommenders, particularly around transparency, interpretability, and domain shift adaptability, marking a significant advancement for recommender systems research.

### Weaknesses
1.	The introduction is too brief, especially in describing the proposed method. Expanding this section would clarify the paper’s contributions and provide a more comprehensive overview of the approach.

2.	The "Problem Setting and Notations" subsection is disorganized and unclear, making it challenging for readers unfamiliar with this work to understand.

3.	Experimental setup details are critical to the paper, yet they are insufficiently described, and additional information could not be found in the appendix.

4.	The paper lacks an in-depth analysis of the experimental results. Although many results are presented, the analysis remains overly simplistic, with no detailed examination in the appendix either.

### Questions
1.	Could you expand the introduction to provide a clearer and more comprehensive overview of PRUC? More details on how the proposed method addresses interpretability and bias correction would help readers understand its unique contributions early on.

2.	Could you revise Problem Setting and Notations subsection for better organization and clarity? A clear and well-structured presentation of the notations and problem setup would help readers understand your approach more effectively. 

3.	The paper lacks sufficient detail on the experimental setup, which is critical for evaluating the model's effectiveness.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a Bayesian recommendation model to enhance cross-domain recommendations through a plug-and-play approach called Probabilistic Residual User Clustering (PRUC). PRUC creates user clusters based on latent confounders, increasing the model's interpretability.

### Strengths
1. Strong theoretical foundation
2. Addresses a problem with extensive real-world, especially industrial, applications

### Weaknesses
W1. Lacks comparison with previous state-of-the-art approaches.

W2. Experiments are limited in scope, focusing only on user and item settings. For instance, while conducted on a reliable dataset, they do not extend to more complex datasets encompassing diverse domains (e.g., age, demographics) beyond geographical location.

### Questions
Q1. How does PRUC adapt to an online training setting where item popularity constantly changes?

Q2. Are there any ablation studies examining the effect of the number of domains (M) on PRUC's performance? How does this hyperparameter impact the degree of model quality improvement PRUC provides?

Q3. What are the system overheads of deploying PRUC compared to previous state-of-the-art methods? For example, can the authors provide an analysis of PRUC's impact on metrics such as Area Under Curve (AUC) to illustrate any potential system overheads from adopting this approach?

Q4. Many modern recommendation systems treat recommendation as a binary classification problem (e.g., whether to recommend an item to a user). Could the authors explain how PRUC could enhance model quality if the recommendation task is framed in this binary classification context?

Q5. In Table 3, where CKL is used as the base model, PRUC does not appear to improve overall model quality across different domains. Could the authors provide further explanation on this outcome?

### Soundness
3

### Presentation
3

### Contribution
3

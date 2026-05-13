# Constraining embedding learning with Self-Matrix Factorization

- Decision: Reject
- Scores: 5, 3, 5

## Abstract
We focus on the problem of learning object representations from solely association data, that is observed associations between objects of two different types, e.g. movies rated by users. We aim to obtain embeddings encoding object attributes that were not part of the learning process, e.g. movie genres. It has been shown that meaningful representations can be obtained by constraining the learning with manually curated object similarities. We propose Self-Matrix Factorization (SMF), a method that learns object representations and object similarities from observed associations, with the latter constraining the learned representations. In our extensive evaluation across three real-world datasets, we compared SMF with SLIM, HCCF and NMF obtaining better performance at predicting missing associations as measured by RMSE and precision at top-K. We also show that SMF outperforms the competitors at encoding object attributes as measured by the embedding distances between objects divided into attribute-driven groups.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a method, Self-Matrix Factorization (SMF), for learning object representations from association data without prior knowledge of object attributes. The paper claims that SMF outperforms other methods like SLIM, HCCF, and NMF in predicting missing associations and encoding object attributes.

### Strengths
- Performance Evaluation: The paper uses a variety of metrics (RMSE, precision at top-K, AUROC, AUPRC) across different datasets to evaluate the model's performance, which provides an assessment of its capabilities.
- Comparison with State-of-the-Art: SMF is compared against several established methods, which strengthens the paper's claims about the superiority of the proposed method.

### Weaknesses
 - Lack of Theoretical Foundation: The paper could benefit from a deeper theoretical analysis of why SMF works better than existing methods. The underlying assumptions and mathematical properties of SMF need more exploration, specifically regarding the convergence properties of the proposed optimization algorithm and the conditions under which the learned similarities accurately reflect the underlying data structure.
- Complexity and Scalability: The paper does not discuss the computational complexity of SMF or how it scales with larger datasets, which is crucial for practical applications. A detailed analysis of the time and space complexity, along with empirical evaluations on larger datasets, is needed to understand the practical limitations of the method. The analysis should also consider the impact of the embedding dimension on computational cost.
- Limited Discussion on Hyperparameter Sensitivity: While the paper mentions hyperparameter tuning, there is limited discussion on how sensitive the model's performance is to these hyperparameters, which is important for reproducibility and practical use. A more thorough analysis of the impact of each hyperparameter, including the regularization weights and the embedding dimension, on the model's performance is needed, along with guidelines for selecting appropriate values.
- Overfitting Concerns: The paper does not address potential overfitting issues, especially given the use of regularization terms in the loss function. It is important to analyze how the regularization parameters affect the generalization performance and to provide empirical evidence that the model is not overfitting the training data.
- Generalization to Other Domains: The paper primarily focuses on association data between two types of objects. It is unclear how well SMF generalizes to other types of data or more complex relationships. The paper should discuss the limitations of the method and explore potential adaptations for other data types, such as multi-relational data or data with more complex structures.

### Questions
- How does SMF handle sparse data matrices, and what is its performance compared to other methods in such scenarios?
- Can the authors elaborate on any potential biases that might be introduced by the learned object similarities in SMF?
- What are the computational requirements for training SMF, and how does it compare to other methods in terms of training time and resource usage?
- How does SMF perform in dynamic environments where the association data changes over time, and is there any strategy to update the embeddings efficiently?
- Could the authors provide more insights into the choice of hyperparameters and their impact on the model's performance?

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
2

### Summary
This paper introduces Self-Matrix Factorization (SMF), a matrix decomposition method that constrains the nonnegative matrix factorization optimization, among other with a "Self-Expressivity" term that aims to preserve the linear manifold information implicit in the original association matrix. 

Tested on datasets like MovieLens and Drug-SE, SMF outperformed traditional methods in predicting associations and clustering objects based on latent features (e.g., genres or categories). This method shows promise for recommendation systems and unsupervised learning tasks where labeled data is limited.

### Strengths
- The paper explores an interesting topic, ie to generate embeddings that capture implicit object attributes by leveraging similarities inferred from associations 

- The addition of the term that exploits the fact that objects (amy) lie on multiple linear manifolds, is interesting and seems to provide some gains over NMF.

### Weaknesses
W1) There is no related works section, and the contribution and relationships to the closest matrix factorization methods is unclear. Although a popular topic, there is only a handful of matrix factorization works cited. What are the closest matrix factorization works and how does Eq 2 compares? The second term in Eq. 2 allows each row to be reconstructed from others. Is this the first use of this "self-expressive" constraint in MF and representation learning, or have similar constraints been applied in other methods?
I think that authors should consider adding a dedicated related work section comparing SMF to other recent matrix factorization methods, particularly those using similar self-expressive constraints.

W2) The update rule in Eqs 3-4 are derived from Lee & Seung, 2000 and applied to Eq 2. Unclear if there is any substancial contribution there. Same as the addition of factor alpha that is borrowed from related work.

W3) Figure 1 seems way too generic and fails to adequately illustrate the novel aspects of SMF. Figure 1(a) depicts a generic matrix factorization, which does not highlight SMF’s unique contributions. Figure 1(b) shows linear subspaces, but it lacks clarity on how the method effectively utilizes only points within the same subspace to reconstruct an object. 
The authors should consider adding a visual representation of how SMF utilizes points within the same subspace for reconstruction, or including a side-by-side comparison with traditional matrix factorization to highlight SMF's unique approach.

W4) The datasets used for evaluating SMF are relatively small, which limits the generalizability of the results, and the comparative analysis is not extensive. The main competitor in Table 2 is NMF, with modest improvements in RMSE observed for SMF. Additionally, SLIM performs significantly worse than NMF, so it may be more insightful to reorder the rows in Table 2 to better highlight SMF's performance against the second-best model.

### Questions
Please see weaknesses above. My main questions are with respect to the differences of this approach to other MF works. Section 4 kind of wraps this up but doesnt discuss relations and what this method offers.

Q1) What would you say are the contributions of this method compared to the closest ones?
Q2) could  you clarify what specific innovations, if any, have been made in deriving these update rules in Eq3-4 compared to previous work? Could you discuss how the incorporation of the alpha factor contributes to the overall novelty of their approach?
Q3) could you include more state-of-the-art matrix factorization methods in the comparative analysis? This would help provide a more comprehensive evaluation of SMF's performance.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper focuses on the problem of learning object representations from solely association data, and proposes a Self-Matrix Factorization (SMF) method. The innovation of this paper is relatively weak, and the core contributions have not been clearly elaborated.

There are several concerns that need to be addressed. 

Firstly, the paper relies on the assumption that objects reside on multiple linear low-dimensional manifolds embedded within a high-dimensional space. However, this assumption appears to have already been utilized by numerous prior matrix factorization works, rendering it relatively uninnovative. 

Secondly, the paper asserts that object similarities can be derived directly from the data matrix, yet it fails to elucidate the method of learning or the criteria for determining these similarities.

Thirdly, the paper compares its proposed SMF to other methods such as SLIM, HCCF, and NMF, but it does not provide a comprehensive analysis of the strengths and weaknesses of each method. 

Forthly, the experiments conducted in this paper are relatively simplistic, both in terms of the datasets and tasks employed, and the comparative methods utilized are outdated.

### Strengths
1. This paper focuses on the problem of learning object representations from solely association data, and proposes a Self-Matrix Factorization (SMF) method. 
2. The authors performed experiments at recovering missing values on the different association matrices and show that SMF obtains comparable or better predictions than its competitors.

### Weaknesses
1. The paper relies on the assumption that objects reside on multiple linear low-dimensional manifolds embedded within a high-dimensional space. However, this assumption appears to have already been utilized by numerous prior matrix factorization works, rendering it relatively uninnovative. The authors do not adequately address how their method distinguishes itself from existing techniques that leverage similar manifold assumptions. Specifically, the paper lacks a detailed explanation of how the proposed Self-Matrix Factorization (SMF) method incorporates this assumption in a novel way compared to other matrix factorization approaches that also operate under the same premise. The use of this assumption, without a clear demonstration of unique application, significantly diminishes the contribution of the work.

2. The paper asserts that object similarities can be derived directly from the data matrix, yet it fails to elucidate the method of learning or the criteria for determining these similarities. The paper does not provide a clear mathematical formulation or algorithmic description of how these similarities are extracted from the data matrix. It is unclear how the method determines which objects are similar and what specific properties of the data matrix are used to establish these relationships. Without a concrete explanation of the similarity learning process, the claim that similarities are derived directly from the data matrix remains unsubstantiated and difficult to evaluate.

3. The paper compares its proposed SMF to other methods such as SLIM, HCCF, and NMF, but it does not provide a comprehensive analysis of the strengths and weaknesses of each method. The comparison lacks a detailed discussion of the specific advantages and disadvantages of each method in the context of the problem being addressed. The paper does not explain why these specific methods were chosen as baselines or how they relate to the proposed SMF method. A more thorough analysis should include a discussion of the computational complexity, scalability, and sensitivity to hyperparameters for each method, as well as a justification for their selection as appropriate comparators.

4. The experiments conducted in this paper are relatively simplistic, both in terms of the datasets and tasks employed, and the comparative methods utilized are outdated. The datasets used in the experiments are not sufficiently complex or diverse to demonstrate the robustness and generalizability of the proposed method. The tasks performed, such as missing value recovery, are not challenging enough to fully evaluate the capabilities of the SMF method. Furthermore, the comparative methods, such as SLIM, HCCF, and NMF, are not representative of the current state-of-the-art in representation learning and matrix factorization, which limits the significance of the experimental results.

### Questions
1. The paper relies on the assumption that objects reside on multiple linear low-dimensional manifolds embedded within a high-dimensional space. However, this assumption appears to have already been utilized by numerous prior matrix factorization works, rendering it relatively uninnovative. 

2. The paper asserts that object similarities can be derived directly from the data matrix, yet it fails to elucidate the method of learning or the criteria for determining these similarities.

3. The paper compares its proposed SMF to other methods such as SLIM, HCCF, and NMF, but it does not provide a comprehensive analysis of the strengths and weaknesses of each method. 

4. The experiments conducted in this paper are relatively simplistic, both in terms of the datasets and tasks employed, and the comparative methods utilized are outdated.

### Soundness
2

### Presentation
3

### Contribution
1

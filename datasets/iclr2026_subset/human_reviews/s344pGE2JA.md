## Human Reviewer 1

### Summary
This paper aims to improve and evaluate the performance of learning models by adjusting the training data. By analyzing the boundaries of influence functions for each category, the method samples data that make the learning process difficult, thereby enhancing the overall learning performance.

### Strengths
By analyzing the influence functions, the method identifies and extracts data that negatively affect the learning process, thereby improving the model. The approach is also evaluated on real-world datasets.

### Weaknesses
The primary concern with this paper lies in whether its novelty and performance evaluation are sufficient. More specifically:

- The proposed approach and the problem it aims to solve appear to correspond to what is generally known as hard negative mining. A large body of prior work already exists in this area — for instance, see [1], among many others. Even if the proposed method is indeed novel and achieves superior performance, it must be properly situated within this existing literature, with relevant prior studies surveyed and direct comparisons presented.
    
- The paper currently provides an explanation of the proposed method and reports improvements in model performance. However, the evaluation is entirely self-contained, presenting only the authors’ own claims without comparisons to other methods. This lack of objective, external evaluation significantly limits the strength of the paper’s contribution.

[1] H. Meghwani et al., Hard Negative Mining for Domain-Specific Retrieval in Enterprise Systems, ACL 2025

### Questions
- First, please clarify the relationship between the proposed method and hard negative mining.
    
- If the proposed method falls within the framework of hard negative mining, please explain why comparisons with existing methods are not provided. While adding such comparisons would be one option, note that doing so may require more than a minor revision — at present, it does not seem feasible to address this point with only small changes.
    
- If the proposed method does not fall within the scope of hard negative mining, please clearly state the reasons for this.
    
- Furthermore, if the proposed method is indeed outside that framework, is the problem it aims to solve itself novel? If so, a self-contained evaluation could be acceptable in principle, but in that case, please provide a clear justification for the absence of comparisons with other approaches.

### Soundness
2

### Presentation
1

### Contribution
2

### Rating
2

### Confidence
3

---

## Human Reviewer 2

### Summary
This paper focuses on diagnosing and improving the performance of multiclass classifiers by analyzing the impact of individual training samples at the category level. The authors introduce a vectorized influence function that quantifies each sample’s effect across all classes, enabling a precise assessment of Pareto-optimality in model performance. Building on this, they propose a linear programming-based sample reweighting method (PARETO-LP-GA) to achieve targeted improvements in specific classes with minimal compromise to others. Experimental results on synthetic and real-world datasets validate the method’s effectiveness in identifying performance bottlenecks and enhancing class-wise accuracy.

### Strengths
1. The contribution of this paper is simple and clear.

2. The paper introduces an innovative approach by decomposing the influence function over the entire validation set into class-specific influence functions. This allows for precise identification of how individual training samples affect model performance on specific classes.

3. Building upon the vectorized influence function, the authors design a fine-grained sample reweighting algorithm, which enables targeted adjustment of training sample weights to optimize performance.

### Weaknesses
Although the paper introduces the concept of class-wise influence functions, the originality of this idea is somewhat limited; the main contribution lies more in the development of a sample reweighting algorithm based on these class-wise influence functions.

The experimental section lacks comparative analysis with other relevant methods. While most existing influence function-based approaches focus on overall accuracy as the primary metric, the paper claims that its method can push classifier performance towards its upper bound. Therefore, it would be more convincing if the authors compared their approach with state-of-the-art methods such as Chhabra et al. (2024) [1] using overall accuracy or other relevant metrics to demonstrate its superiority.

[1] Chhabra, Anshuman, et al. "" What Data Benefits My Classifier?" Enhancing Model Performance and Interpretability through Influence-Based Data Selection." The Twelfth International Conference on Learning Representations. 2024.

### Questions
1. Could you provide a more detailed explanation of the formula used to compute "fitness $F(\alpha^g)$" in Algorithm 1? I found its specific meaning somewhat unclear.

2. As I am not very familiar with Pareto frontier-related concepts, could you elaborate on the practical implications if a model reaches the Pareto frontier, or as you mentioned, if all samples are close to the line $y=−x$? Specifically, what advantages does this provide for practitioners? Does it guarantee that the accuracy for all classes is maximized? How does this relate to, or differ from, the conventional goal of optimizing overall accuracy? This question is also related to the concerns I raised under the weaknesses section.

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
3

---

## Human Reviewer 3

### Summary
This paper applies influence functions on the category level to assess and enhance a classifier's Pareto performance from a data-centric perspective. Specifically, the authors propose a category-wise influence vector to quantify how each training sample affects multiple classes, and a PARETO-LP-GA (Linear Programming + Genetic Algorithm) method to reweight samples for Pareto-optimal improvement. Experiments on synthetic and benchmark datasets show that the method can identify performance ceilings and achieve targeted, balanced improvements.

### Strengths
1. Clear presentation and good illustration.
2. Demonstrates practical utility for model improvement and interpretability in multi-class tasks.
3. Sound theoretical grounding combined with a clear optimization formulation (LP + GA).

### Weaknesses
1. The first main weakness is the proposed method's novelty and theoretical validity. Applying the influence function to each category has already been explored (see 2.), and the proposed method does not seem to have a deeper insight; rather, it simply takes the "influence vectors" and operates as they fully indicate how the model will change, while neglecting the fact that it is only a first-order approximation.
2. The second main weakness lies in its limited comparison with the existing literature. For instance, FairIF [1] and D3M [2] are all related works but not discussed.

[1]: Wang, Haonan, Ziwei Wu, and Jingrui He. Fairif: Boosting fairness in deep learning via influence functions with validation set sensitive attributes.
[2]: Jain, Saachi, Kimia Hamidieh, Kristian Georgiev, Andrew Ilyas, Marzyeh Ghassemi, and Aleksander Madry. Data debiasing with datamodels (d3m): Improving subgroup robustness via data selection.

### Questions
1. (Weakness 1+2) How does the proposed method compare to other related works in terms of theoretical guarantees, scalability, etc.? A careful discussion will be necessary in order to position the paper in the literature.
2. Can you elaborate more on the proposed algorithm and discuss/justify the design choices?

### Soundness
3

### Presentation
3

### Contribution
1

### Rating
2

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper proposes to estimate the influence function at a per class level, instead of the overall influence function on loss in prior literature. The aim is to learn classifier well to reach the pareto fronties. The authors propose an LP based formulation to estimate influence and use it to improve the accuracy in the training. Experiments on CIFAR-10 and Synthetic data are shown for verifying the claims.

### Strengths
1.	The paper is clearly written and is intuitively understandable.

2.	With the disclaimer of my limited knowledge in Influence Functions, I find the work to be novel.

### Weaknesses
1.	Missing Optimality Guarantees: Although the method is intuitive, it's hard to believe that the proposed algorithm would reach the Pareto frontier without the convergence guarantees for the algorithm.

2.	Missing experiments on Larger Class Datasets: The datasets that are used in the paper are either synthetic or small-scale, like CIFAR-10. It's unclear whether the method can scale to datasets like ImageNet and what its runtime complexity would be.


3.	Hard to parse Fig. 3 and Fig. 4 without detailed captions explaining the results in the figure, as it has a lot of details. Could you please explain how the Spearman correlation is plotted? Is it for validation accuracy?

4.	There are other ways of cost-sensitive learning that could be used to balance the performance of the method across classes.

### Questions
1.	In Table 1, the correlation is established for the particular epoch. However the performance at the end of training is more pratical. Could the authors explain how the Influence function improves the final performance?

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
3
# Algebraic SPD and Correlation Geometry: A Gyro Approach

- Decision: Reject
- Avg Score: 4.20
- Scores: 5, 3, 5, 5, 3

## Abstract
The generalization of Deep Neural Networks (DNNs) to Riemannian manifolds has garnered significant attention across various scientific fields. Recent studies have demonstrated that several manifolds, including hyperbolic, spherical, Symmetric Positive Definite (SPD), and Grassmann manifolds, admit gyro-structures—powerful algebraic structures that enable the principled extension of DNNs to manifolds. Inspired by these advancements, we introduce a novel gyro-structure for SPD manifolds, leveraging the flexible and powerful Power-Euclidean (PE) geometry. Moreover, full-rank correlation matrices, which are scale-invariant, serve as compact representations of SPD manifolds. Consequently, we propose two novel gyro-structures for correlation matrix manifolds, based on two theoretically and empirically convenient metrics: Euclidean-Cholesky (EC) and log-Euclidean-Cholesky (LEC) geometries. Extensive experiments on knowledge graph completion tasks validate the effectiveness of our proposed gyro-structures.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents novel algebraic structures (gyro-structures) for Symmetric Positive Definite (SPD) manifolds and full-rank correlation matrices, inspired by the extension of Deep Neural Networks (DNNs) to non-Euclidean geometries. Leveraging Power-Euclidean (PE) geometry, the authors introduce gyro-structures for SPD manifolds, alongside Euclidean-Cholesky (EC) and log-Euclidean-Cholesky (LEC) metrics for correlation matrices. Empirical validation is conducted on knowledge graph completion tasks, showing improvements in computational efficiency and model accuracy.

### Strengths
**Novelty:** Introduces new gyro-structures tailored for SPD manifolds using PE geometry, which recovers existing LE spaces and provides flexibility.

**Theoretical Rigor:** Detailed theoretical results, including binary operations and scalar multiplication, rigorously define the gyro-structures.

**Empirical Validation:** Experiments on knowledge graph tasks demonstrate that the proposed gyro-structures can outperform existing models in some metrics.

### Weaknesses
The most critical weakness is the lack of clear explanation of how the theoretical concepts are actually implemented in the experimental algorithms:
- Missing details on algorithm implementation: The experimental section typically needs to elaborate on the details of the algorithm's implementation, including framework overview, pseudo-code, parameter selection, and specific implementation techniques. Without these details, the practical applicability of the theoretical results may be questioned. For instance, the paper introduces gyro-structures based on the Power-Euclidean (PE) metric, but it is unclear how this metric is specifically used within the optimization process. Are standard gradient-based methods directly applicable, or are specialized optimization techniques required? The paper should clarify how the gyro-operations (binary operations and scalar multiplication) are integrated into the learning process, especially within the context of backpropagation.
- Insufficient correspondence between experimental validation and theoretical support: Theoretical research should directly support the design and analysis of experiments, but the connection between the experiments presented and the preceding theoretical derivations is loose in this paper. It would be better to add an explanation of how theory inspires the design of algorithm. For example, while the paper proposes novel gyro-structures for SPD manifolds and full-rank correlation matrices, the experimental section does not provide a clear rationale for why the chosen knowledge graph completion task is particularly suitable for validating these structures. A more detailed explanation of how the properties of these gyro-structures align with the requirements of the KGC task would strengthen the paper.

### Questions
How do the gyro-structures affect performance in other DNN applications, such as image or text classification?

### Soundness
3

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
3

### Summary
Gyrovector spaces extends transformations to hyperbolic geometry (originally), it captures operations analogous to addition and multiplication in Euclidean geometry. This paper studies gyrovector spaces for Symmetric Positive Definite (SPD) manifolds associated with Power-Euclidean metrics. Next, the paper looks into full-rank correlation matrices, as an example of SPD manifold, with two concrete Riemannian metrics: Euclidean-Cholesky and log-Euclidean-Cholesky metrics. The major contribution falls into proposing these metrics that can be applied to correlation matrices. The empirical study is implemented with the knowledge graph completion tasks, evaluating the proposed metrics on two datasets. The performance is marginally improved over previous work.

### Strengths
In general, the paper is well-organized. It is still notation-heavy due to the group operations etc. but I see the authors put efforts in making things clear. 

To the best of my knowledge the paper is mathematically solid. I only had time to check the proof in section 3. I am happy to check more details if anything comes up, but at this moment I believe the later proofs follow quite similarly from the definitions.

It is illuminating to discuss the geometry of correlation matrices separately from the general SPD matrices, with a good motivation presented in section 4.

### Weaknesses
The presentation can still be improved.
- PE geometry has been emphasized quite a lot but not really explained what it is (for general audience). The only relevant description I could find locates in line 169, which is not a clear definition.
- I would say the related literature has been covered quite well in the introduction section. Maybe, it would be better to mention more motivation, technique used and other discussions in the intro, and have a related work section. It could be helpful to discuss various Riemannian geometries and how (and if) gyrovector spaces are different on each.
- I like section 4. It might be regarded as discruptive, because we are in the middle of technical sections but suddenly something more like prelimianry appears. I am personally fine with what it is, it should be also fine to cut it shorter, and merge with section 5
- Maybe this is the most concerned comment. The method for KGC task is compressed a bit too much. I understand it is not very complicated and extends from prior work. But for readers, the KGC is a new mateiral and it is better to introduce your method with more intuitions before having heavy notations.

My major concern is two-fold: the technical novelty is limited and the experiment results are not convincing enough.

The mathematical elements, though non-trivial, heavily inherit from the gyro group definitions. The gyro structure has been stuided for other Riemannian metrics, at this point, I do not see what is the techincal barrier to extend these definitions to another metric.

The empirical study has three issues, with importance in order: (1) The improvement is very small, especially, there is not a significant gap from the previous Gyro-LE metric. (2) The baselines are not inclusive -- only a similar prior work and rather trivial SPD transformations. (3) Two datasets are not enough.

### Questions
Just to make sure I did not miss it: what is the new technical challenge to extend the gyro structure to PE (and two others for correlation matrices) geometry? Especially, comparing to the prior work.

The EC and LEC metrics are tailored to benefit correlation matrices better, but this is not corroborated by table 2 and 3. Results by PE seems to be better mostly. Do we have any understanding on this?

Are there other tasks to be considered fit to evaluate the proposed metrics? Deep learning can in fact add more randomness into evaluation, is it possible to evaluate on tasks that are more dependent on "distance between matrices" itself? I am thinking of clustering and some time series analysis tasks such as anomaly detection or change point detection, only for reference.

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
2

### Summary
The paper titled "Algebraic SPD and Correlation Geometry: A Gyro Approach" introduces a novel approach to leveraging gyro-structures on SPD manifolds, focusing on Power-Euclidean (PE) geometry and extending this to full-rank correlation matrix manifolds with Euclidean-Cholesky (EC) and Log-Euclidean-Cholesky (LEC) metrics. The main text is dense with theoretical formulations which are presented with rigorous mathematical proofs. Further, several experiments are conducted to validate the effectiveness of proposed methods on knowledge graph completion tasks.

### Strengths
1.The inclusion of detailed proofs and lemma/theorem statements provides a strong mathematical foundation and supports the credibility of the approach.

2.Using SPD and correlation matrix manifolds for knowledge graph completion is well-motivated and relevant, especially as these tasks require handling non-Euclidean data structures.

### Weaknesses
1.The application of gyro-structures on SPD manifolds and correlation matrices is indeed novel, but the paper does not clearly articulate the theoretical significance or unique advantages of using Power-Euclidean (PE) geometry over existing approaches like Affine-Invariant (AI) or Log-Euclidean (LE) methods. The work seems incremental without providing substantial theoretical or empirical evidence that PE geometry offers practical improvements beyond computational convenience. Especially, while gyro-structures are presented as an extension to non-Euclidean spaces, the paper does not establish a strong need or motivation for this approach within the broader context of machine learning or geometry-based learning. It lacks a thorough discussion on why gyro-structures would fundamentally enhance SPD or correlation matrix-based learning in a way that current methods do not. The claim that PE geometry converges to LE as the power approaches zero is not sufficient justification; a deeper exploration of the specific benefits of PE in the context of SPD and correlation matrices is needed, especially considering that LE already provides a well-established framework. The paper needs to demonstrate scenarios where PE geometry provides a clear advantage in terms of learning performance or geometric properties over LE or AI, rather than just being a computationally convenient alternative.

2.Some key theoretical concepts and mathematical operations, such as those in gyrovector space theory and correlation matrix manifold construction, are highly technical and lack intuitive explanations. Additional clarification or simplified summaries would improve accessibility for readers unfamiliar with advanced Riemannian geometry. For instance, the paper introduces gyro-addition and gyro-scalar multiplication without clearly explaining how these operations relate to the underlying geometry of the manifolds. A more detailed explanation of how these operations preserve the manifold structure and why they are appropriate for the given task is needed. Furthermore, the construction of the correlation matrix manifold and the choice of metrics (EC and LEC) should be motivated with more intuitive explanations, linking them to the specific properties of correlation matrices and their role in knowledge graph completion.

3.On the experiments part, the related discussion lacks interpretive insights that would elucidate why the proposed gyro-structures outperform existing methods. In addition, while the paper compares its methods against SPD-based models and a few gyro-structure-based approaches, it lacks comparison with other state-of-the-art methods that might not rely on gyro-structures. This omission makes it unclear whether the proposed approach actually outperforms simpler or more commonly used techniques in manifold-based learning. The experimental section should include a more comprehensive comparison with a wider range of baselines, including non-gyro-structure methods, to provide a more robust evaluation of the proposed approach. Furthermore, the discussion of the results should go beyond simply reporting numerical improvements and should provide insights into why the proposed methods perform better in certain scenarios, relating the performance gains to the specific properties of the gyro-structures and the chosen metrics.

### Questions
Please refer to the weaknesses.

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
2

### Summary
This paper considers endowing the set of correlation matrices with a gyro (weak group) structure, which has the potentially of subsequently allowing deep learning over the set of correlation matrices. As highlighted by the authors, recent work over the past few years has suggested the potential gains from working in non-Euclidean geometry in certain tasks. Work has already been done on endowing the set of SPD matrices with a gryo structure.
More specifically:
- the authors propose a new gyro structure on the set of SPD matrices
- the authors propose two gyro structures for full-rank correlation matrices
- the performance of the DNN that they allow is evaluated on two datasets.

### Strengths
The paper is reasonably well written and seems to

### Weaknesses
-**Style:**
   -  The exposition might be improved by being a bit more specific. I understand the authors might want to provide just a brief overview of the literature, but some of the paragraphs become a bit vacuous (too many uses of the word "others", and extremely unspecific): "The space of SPD matrices forms a manifold, known as the SPD manifold which has been successfully applied in various fields. To respect the non-Euclidean geometry, several Riemannian structures on the SPD manifold were proposed .Due to the fast computation speed and theoretical convenience of the Power-Euclidean (PE) metric, and when the power tends to 0, this metric approaches the Log-Euclidean (LE) metric, building a bridge between Euclidean and LE metrics. Based on the above advantages, the PE metric has already seen successful applications in other fields."
  - I think the justification for this paper comes it much too late. The first few pages read more like an intellectual exercise, rather than something that could be useful. I am still a bit confused as to (a) why we need another gyrostructure on SPD matrices, and 2 new on correlation matrices: what is wrong with existing methods? Maybe, to make the exposition clearer, the authors could start with a use case example.

**Content:**
- Overall, my main comment is that the paper reads too much like a list (e.g. "here's 2 geometry and three metrics to consider). It does not provide insights as to (a) the current issues with the method (brief mention of the computational complexity only), or (b) try to make the reader understand why and when certain manifold and grystructure types are useful.
- in the experiments, it is unclear why the correlation matrix makes sense.

### Questions
See above

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces a gyrovector space structure on symmetric positive definite (SPD) matrix manifolds based on the Power-Euclidean (PE) geometry and proposes two new gyro structures for full-rank correlation matrices using the Euclidean-Cholesky and Log-Euclidean-Cholesky metrics. These structures extend the applicability of deep neural networks in non-Euclidean geometry, with demonstrated effectiveness in knowledge graph completion tasks.

### Strengths
1. The paper introduces new gyrovector space structures for SPD and full-rank correlation matrix manifolds based on PE, EC, and LEC metrics, providing rigorous theoretical derivations that establish their mathematical validity and potential contribution to geometric deep learning.

2. The experiments validate the effectiveness of the proposed structures in knowledge graph completion tasks, demonstrating their applicability in handling non-Euclidean data.

### Weaknesses
1. From the perspective of theoretical construction, the paper **lacks significant theoretical innovation**, as the theoretical derivations are relatively simple and straightforward. The proofs in the appendix largely focus on verifying basic gyrovector space axioms, relying on direct calculations rather than innovative techniques. The approach primarily involves straightforward matrix operations, such as verifying identities and inverses through simple substitutions. The proofs for different metrics (PE, EC, LEC) follow nearly identical steps, showing limited structural novelty and repetitive methods across manifold types. Overall, the derivations lack deeper geometric insights or complex algebraic manipulation, limiting theoretical innovation.


2. The paper’s writing employs complex manifold language and notation, which may be inaccessible to machine learning researchers without a geometry background. Many concepts and derivations lack clear contextual explanations, making the content dense and challenging to follow. Additionally, the paper includes numerous technical details but does not provide sufficient simplifications or examples, making it hard for readers to grasp the main points quickly, potentially impacting readability and appeal.

3. While the experiments validate the proposed structures on knowledge graph completion, they are limited in scope and do not demonstrate performance on other practical tasks or non-Euclidean datasets. Moreover, the lack of publicly available code and the complex implementation details may hinder reproducibility. The experimental results focus on specific tasks and do not comprehensively showcase the method's potential advantages and limitations.

### Questions
1. The derivations mainly verify basic gyrovector space axioms through straightforward matrix operations, lacking complex geometric insights or novel algebraic techniques. So, what are the  theoretical innovations?

2. The complex manifold language and notation may be hard to follow for those without a geometry background. Is it possible to add simplified explanations, examples, or background to improve accessibility for a broader audience?

3. The experiments are limited to knowledge graph tasks, and the lack of public code and detailed implementation may hinder reproducibility. It is possible to expand the scope of applications and release the code for reproducibility?

### Soundness
2

### Presentation
2

### Contribution
2

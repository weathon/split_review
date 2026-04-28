# A Meta-Learning Approach to Bayesian Causal Discovery

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Discovering a unique causal structure is difficult due to both inherent identifiability issues, and the consequences of finite data.
As such, uncertainty over causal structures, such as those obtained from a Bayesian posterior, are often necessary for downstream tasks.
Finding an accurate approximation to this posterior is challenging, due to the large number of possible causal graphs, as well as the difficulty in the subproblem of finding posteriors over the functional relationships of the causal edges.
Recent works have used Bayesian meta learning to view the problem of posterior estimation as a supervised learning task.
Yet, these methods are limited as they cannot reliably sample from the posterior over causal structures and fail to encode key properties of the posterior, such as correlation between edges and permutation equivariance with respect to nodes.
To address these limitations, we propose a Bayesian meta learning model that allows for sampling causal structures from the posterior and encodes these key properties.
We compare our meta-Bayesian causal discovery against existing Bayesian causal discovery methods, demonstrating the advantages of directly learning a posterior over causal structure.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes the Bayesian Causal Neural Process (BCNP), a Neural Process-based framework for learning a posterior distribution over causal graphs given a dataset $P(G \mid X)$ . The proposed method is scalable and captures distinctions between graphs within the same Markov equivalence class. Since BCNP learns causal structures across multiple (synthetic) datasets, it is considered a meta-learning approach.

### Strengths
1. This paper provides a well-structured and self-contained summary of prior works in Bayesian causal discovery, allowing readers to clearly follow the evolution of Bayesian approaches for learning causal graphs. As a reviewer, this summary enables me to track the advancements in the field and understand the recent progress in addressing challenges like scalability and uncertainty in causal inference.

2. The paper clearly outlines its unique contributions in Table 1, highlighting significant advancements over existing methods. The proposed model addresses critical aspects such as acyclicity, permutation invariance, and edge dependencies—all of which are critical for accurate causal graph learning. These improvements over prior approaches directly enhance the reliability and precision of inferred causal structures, making the contributions both clear and impactful.

3. The proposed BCNP is particularly attractive due to its innovative use of Neural Processes to directly sample the posterior distribution $ P(G | X) $. This approach enables BCNP to achieve scalability and uncertainty-aware inference by learning across tasks (= datasets), allowing the model to efficiently adapt to new datasets while maintaining a robust representation of causal uncertainty. This combination of scalability, direct posterior sampling, and adaptability positions BCNP as a strong advancement over existing Bayesian causal discovery methods.

### Weaknesses
1. One of the main limitations of this paper is the assumption that there are no latent confounders between variables. This assumption severely restricts the applicability of the method to real-world datasets, where unobserved confounders are not just common but often the norm. The absence of a mechanism to account for these confounders means that the causal inferences drawn by BCNP could be spurious or misleading in many practical scenarios, limiting the scope of the method.

2. I think this method is heavily relying on the assumptions on the choice of modeling class of functions F, the types of graphs, and the noise model. Unlike fully nonparametric approaches like the PC algorithm, which make minimal assumptions about the underlying functional relationships, BCNP's effectiveness is contingent on these choices being well-suited to the data. For example, if the true data generating process involves highly non-linear relationships or heteroscedastic noise, the performance of BCNP could degrade significantly if the chosen function class or noise model does not adequately capture these complexities. This reliance on specific modeling choices introduces a potential vulnerability to model misspecification.

3. The proposed framework may be sensitive to hyperparameter settings and architecture choices, such as the hyperparameters for the encoder-decoder network, or the types of prior distributions. The performance of the BCNP could be highly dependent on the specific configuration of these parameters. The process of fine-tuning these parameters is often data-dependent, which could reduce the model's robustness and generalization capability. Without a systematic approach to hyperparameter selection, the practical utility of the method could be limited, as optimal performance may require extensive experimentation and careful tuning for each new dataset.

### Questions
1. Is it nontrivial to consider the setting where latent confounders between variables exist? 

2. Is the proposed method computationally efficient when a function class is chosen as neural networks? 

3. How sensitive the proposed framework is regarding to the sparcity of the graph? 

4. Are there any interesting example where the Bayesian approach beats the Markov-equivalence-based method?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a Bayesian meta-learning model for causal discovery, named the Bayesian Causal Neural Process. This "meta-learning" algorithm learns a model from pairs of datasets and their associated causal graphs. Specifically, the model incorporates a neural process to address model uncertainty and employs an encoder-decoder architecture carefully designed to achieve desirable properties for causal discovery in a meta-learning context. These properties include permutation invariance to sample order, permutation equivariance to nodes, and acyclicity, achieved by decomposing the adjacency matrix into a lower triangular matrix and a permutation matrix—some of which build on existing approaches. The authors demonstrate the empirical superiority of this model over other explicit Bayesian and Bayesian meta-learning models

### Strengths
- As summarized in Table 1, this approach implements several key desiderata for a Bayesian meta-learning model more effectively than existing alternatives.
- The paper is well-written, allowing readers to easily follow the motivation and desiderata of Bayesian meta-learning models.

### Weaknesses
 - While I appreciate the overall architecture of the model, it is challenging to identify which components provide truly novel technical contributions. For instance, the results on pages 4 and 5 appear to largely rely on existing findings, and, if I'm not mistaken, page 6 includes results from Annadani et al. (2024). The contributions of this paper are not clearly or explicitly articulated. Specifically, the use of a permutation lower triangular matrix decomposition for enforcing acyclicity, while effective, is not a novel contribution in itself, as this has been explored in other works. The paper needs to more clearly delineate the novel aspects of their approach, beyond combining existing techniques.
- The Bayesian prior is learned through pairs of datasets and directed acyclic graphs (DAGs). From my perspective, learning P(X,G) is likely very challenging. Indeed, Appendix B.1 notes that, for a case involving two variables, the model was trained on 200,000 datasets. I understand that Section 4.1 is intended to evaluate the posterior, but in Appendix B.2, 500,000 datasets are used for training. This information would be better suited for the main text, and details on computational resources should be transparently reported there as well (they are not provided even in the appendix). The sheer scale of data required raises concerns about the practical applicability of this approach, especially given that real-world datasets with known ground-truth DAGs are scarce. The computational cost of training such a model also needs to be more transparently discussed.
- I find it difficult to be fully convinced by the meta-learning approach to causal discovery. While I understand the importance of establishing a strong Bayesian prior, can we realistically expect access to hundreds of thousands of dataset-graph pairs? The reliance on synthetic data for training, while understandable, raises questions about the generalizability of the learned prior to real-world scenarios where the underlying data distributions and causal structures might be significantly different from the synthetic training data.

### Questions
- For DiBS and BayesDAG, the authors mention that they “keep all other hyperparameters to their preset values.” What if these hyperparameters were tuned? Would the results differ significantly? For instance, DiBS and BayesDAG perform well on the Syntren dataset for certain metrics, so tuning may further widen this performance gap.
- In the caption, it says, “Each dataset contains D nodes and N samples.” Does this imply that all datasets must be of the same size? What if the sample sizes vary, such as 100, 200, or 500? Should N be set to 100, or can larger datasets (e.g., 200 and 500 samples) be split into multiple parts (e.g., 2 or 5 parts) to train the model? In that case, should there be weighting adjustments (1/2, 1/5), also training perhaps only for data-related parameters and not for those related to the graph prior?
- If there is no training involved, does your model function like a standard Bayesian causal discovery method with a uniform prior?
- Each variable might have distinct functional priors, such as some being linear, others non-linear, discrete, or having different means. Does the encoder “implicitly” reorder these variables (perhaps using attention mechanisms) to align them by their functional type? I’m trying to conceptually grasp how the encoder handles such diverse functional characteristics under the hood.
- What if permutation equivariance among nodes was not enforced? Would this potentially improve performance, especially if nodes are ordered consistently between training and test data?
- In Line 382, could you clarify what is meant by “correlations between edges” when dealing with just two variables, X and Y, with at most a single edge?

Minor comments
- It would be better to have some annotations in Figure 2 (given that the figure takes lots of space)
- Not quite sure whether it is sufficient to say the dependence in permutation and lower triangular binary matrices is modeled because they share the same representation R0.
- 047, 137 citep for Wenzel et al. 
- 115 citing PC, GES might be good (given you have some space for 119)
- 141 Bayesian metal → meta
- 305 Is the grammar correct? (The matrix … and thus … )
- 340 space before Mena
- 389 In section section 4.2
- 389 its 
- 414 space after comma
- 480 enable
- 485 period
- BayesDAG is not highlighted in Table 4 for Linear data/SHD
- Figure 2 shouldn’t o be the input to Theta? or onto the edge between R^L1 to Theta?
- Sorry for suggesting my preference here but can we align Theta and Phi (parameters, vertically) and align Qs and As with the same horizontal line as Theta and Phi, respectively, and put Gs at far right.

(I can change to weak accept (or accept) depending on the response and others' reviews.)

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
In Bayesian causal discovery, the goal is to approximate the posterior over graphs. Since computing the posterior over graphs requires computing posterior over functional parameters, previous approaches have tried to approximate the posterior over function parameters.  This paper uses neural processes to approximate the posterior over graphs directly by learning a map from the dataset to the set of distributions. The neural process is an encoder-decoder network that claims to sample, permutation-invariant, acyclic graphs that capture edge dependencies.

### Strengths
The paper proposes a technique that can directly sample from the posterior over graphs. The main contribution of the paper is in the architecture of the encoder-decoder network that captures necessary properties like the permutation invariance by cross-attention, and ayclic DAGs and edge dependencies by sampling the decomposition of a DAG into permutation and lower-triangular matrices. The comparison of the proposed model is done with existing meta-learning approaches and Bayesian approaches using multiple metrics. The proposed model is shown to be competitive on synthetic and simulated datasets. The paper is written clearly and flows well.

### Weaknesses
My main concern is that of this being an incremental contribution. The framework is not new and the only contributions I see are a change in how permutation invariance and acyclicity is incorporated. Please let me know if I am missing something else. I have a detailed list of questions below whose answers might help strengthen the paper.

My concern about the incremental nature of the contribution remains. While the specific method of incorporating permutation invariance and acyclicity using cross-attention and a decomposition into permutation and lower-triangular matrices is novel, the overall approach of using a neural process to map datasets to graph distributions is not fundamentally new. The core novelty seems limited to architectural choices within the neural process, rather than a conceptual breakthrough in Bayesian causal discovery. The paper needs to more clearly articulate the significance of these architectural choices beyond simply achieving permutation invariance and acyclicity, and how they lead to a better approximation of the posterior over graphs compared to existing methods.

The experimental validation for the case when the true posterior is known, is done only for the two-variable case. This limited scope raises concerns about the generalizability of the findings. It is unclear how well the proposed method would perform in higher-dimensional settings where the posterior landscape is more complex. The lack of experiments with more variables makes it difficult to assess the practical utility of the method. The paper should include experiments with more variables or provide a strong justification for why the two-variable case is sufficient to demonstrate the method's effectiveness.

The paper states that the metrics average over the posterior. While this is a common practice, it is important to acknowledge that averaging over the posterior can mask important details about the posterior distribution itself. For example, if the posterior is multi-modal, averaging can lead to misleading results. The paper should discuss the limitations of averaging over the posterior and explore alternative metrics that can capture the full complexity of the posterior distribution, such as metrics that evaluate the quality of the samples from the posterior rather than just the average.

### Questions
1) The ideas that the paper uses to impose acyclicity and permutation invariance seem applicable in general. Can existing meta-learning approaches be modified to get the same? While this is not the focus of the paper. It would make it stronger to highlight it if that's the case.

2) The experimental validation for the case when the true posterior is known, is done only for the two-variable case. Is it possible to scale this up? 

3) How can the posterior over the graphs be used for inference on that of the functional parameters? 

4) How is the performance on Gene Regulatory Network simulated data like SERGIO? I believe it would be useful to add that in given its importance. 

5) The paper says that the metrics average over the posterior. I believe this is a problem with any metric. Are there alternatives that the authors propose?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces the Bayesian Causal Neural Process (BCNP), a novel approach for Bayesian causal discovery that leverages meta-learning to address challenges in traditional methods. BCNP learns a mapping from datasets to posterior distributions over causal graphs, thereby bypassing the need to explicitly infer the posterior over causal mechanisms and allowing for efficient sampling from high-dimensional spaces. By encoding key properties like permutation equivariance and edge dependencies, BCNP accurately approximates the true posterior and generates acyclic graph samples. The paper demonstrates BCNP's effectiveness through experiments on synthetic and semi-synthetic datasets, showcasing its superior performance compared to existing Bayesian and meta-learning models for causal discovery.

### Strengths
* The paper is well-written and clear and includes a range of well-designed experiments.

### Weaknesses
For me, there are two major concerns regarding the novelty and contributions of the proposed method to the community:

1.  The paper presents the direct mapping from data to a posterior over graphs ($P(G|D)$) as a main advantage, bypassing the need to model causal mechanisms. However, learning a distribution over causal mechanisms is crucial for many applications, such as causal inference and treatment effect estimation [1, 2]. Could the authors elaborate on potential applications of the proposed approach beyond the discovery of the causal graph? Specifically, the method's inability to directly provide a distribution over causal mechanisms limits its applicability in scenarios requiring counterfactual reasoning or intervention analysis, which are often the end goals of causal discovery.
2.  The proposed method builds on several modules from existing work. For instance, the representation of the posterior distribution as permutation and upper triangular matrices is also similar to [3]. Although the method outperforms baselines in graph-based metrics in causal discovery, the specific novelty remains unclear, particularly given the first concern. The use of permutation and upper triangular matrices, while ensuring acyclicity, is not a novel contribution in itself, and the paper needs to better articulate how the meta-learning approach significantly advances the field beyond these existing structural constraints.

### Questions
1. As my main concerns, I would appreciate the authors to elaborate on the abovementioned weaknesses.
2. Given that the proposed method does not utilize interventional data, using CPDAG E-SHD (as used in previous papers such as in BayesDAG) might be more reflective of the performance of the models compared with E-SHD.
3. Have the authors tried any experiments on low data regime where the number of samples is close to the number of nodes? This is particularly important since Bayesian Causal Discovery is most desirable in low data regime where $n \approx d$. Do you have an intuition about how the proposed model performs in these particular settings?
4. In several experiments, other baselines such as BayesDAG and DiBS achieve a better E-SHD compared to the proposed method. Could you elaborate on why this happens?

### Soundness
3

### Presentation
3

### Contribution
2

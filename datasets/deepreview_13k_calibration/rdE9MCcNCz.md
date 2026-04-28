# A Revisit of Total Correlation in Disentangled Variational Auto-Encoder with Partial Disentanglement

- Decision: Reject
- Avg Score: 4.50
- Scores: 6, 5, 1, 6

## Abstract
A fully disentangled variational auto-encoder (VAE) aims to identify disentangled latent components from observations. However, enforcing full independence between all latent components may be too strict for certain datasets. In some cases, multiple factors may be entangled together in a non-separable manner, or a single independent semantic meaning could be represented by multiple latent components within a higher-dimensional manifold. To address such scenarios with greater flexibility, we propose the Partially Disentangled VAE (PDisVAE), which generalizes the total correlation (TC) term in fully disentangled VAEs to a partial correlation (PC) term. This framework can handle group-wise independence and can naturally reduce to either the standard VAE or the fully disentangled VAE. Validation through three synthetic experiments demonstrates the correctness and practicality of PDisVAE. When applied to real-world datasets, PDisVAE discovers valuable information that is difficult to find using fully disentangled VAEs, implying its versatility and effectiveness.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper describes a modification of the loss function of a variational autoencoder which results in a group-wise independent latent distribution. Similar to the existing TC-beta-VAE (Chen et al 2018), where the evidence lower bound is modified to contain a total correlation term that results in independence of the latent components, in this work the total correlation is computed group-wise, resulting in latent representations in which several groups of latent components become independent.

### Strengths
The paper is well written and with compelling experiments that demonstrate the effectiveness of the proposed modification of the loss function for training a VAE with group-wise independent latent distribution. An importance sampling method for estimating the group-wise posterior lower variance than the one in Chen et al 2018 is proposed.

Especially the three cases, non-separable dependent, rank-deficient, and independent presented in section 3.3 are tested with a dedicated experiment on synthetic data that demonstrate the effectiveness of the proposed method.

### Weaknesses
Novelty seems to be limited because the idea of group-wise independence is not novel. A prior that results in a group-wise independent latent distribution was already proposed in [1]. In contrast that method does not need to compute a group-wise posterior which simplifies the overall training process and removes the necessity of importance sampling.

Technical remarks:
The Pdf-file takes very long to render in Adobe - perhaps this can be solved by sparsifying the scatter plots.

### Questions
Please discuss the work [1] in section 2.2 as additional VAE with a non-gaussian prior and its relation to ICA, and additionally compare to [1] as related baseline with group-wise independent latent prior in your experiments.

So far only dsprites, celebA and a dataset from neuroscience seem to have been used for evaluation. Another good test case would be to integrate the proposed method into disentanglement lib [2] which would enable the direct comparison to the baselines and datasets evaluated in [3], e.g. shapes3d and cars3d.

[2] https://github.com/google-research/disentanglement_lib
[3] Locatello, F., Bauer, S., Lucic, M., Raetsch, G., Gelly, S., Schölkopf, B. and Bachem, O., 2019, May. Challenging common assumptions in the unsupervised learning of disentangled representations. In international conference on machine learning (pp. 4114-4124). PMLR.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a new type of VAE (Partially Disentangled VAE), which adapts the traditional total correlation (TC) term used in fully disentangled VAEs to a new partial correlation (PC) term. This modification allows the model to capture group-wise independence, offering more flexibility when full independence among latent components is impractical. The authors validate PDisVAE through experiments on synthetic and real-world datasets, demonstrating its effectiveness in achieving interpretable and flexible disentangled representations compared to fully disentangled VAEs. The paper highlights the practical advantages of partial disentanglement, presenting PDisVAE as a robust alternative in complex applications.

### Strengths
- 1) The introduction of the partial correlation (PC) term in VAEs is an innovative approach that extends the traditional total correlation (TC), enabling group-wise independence and addressing limitations in full disentanglement.

- 2) The paper is backed by rigorous theoretical derivations and thorough empirical validation on both synthetic and real-world datasets, proving the effectiveness and flexibility of the proposed PDisVAE model.

- 3) By allowing partial disentanglement, PDisVAE broadens the applicability of VAEs in practical scenarios, making it a meaningful advancement for generative modeling and representation learning.

### Weaknesses
-1) The paper does not include a dedicated Related Works section, which would help contextualize its contributions and distinguish it from existing literature on disentangled representation learning. This can greatly improve the presentation as well as make it easier to understand the work in the context of the works before it. Moreover, the citations are very old and the recent works have not been cited appropriately.

-2) The paper does not provide a numerical comparison table for evaluating the performance of PDisVAE against other models on synthetic as well as real world datasets, limiting the clarity and impact of its empirical results. Could the authors provide a table with quantitative comparisons on different datasets to reinforce the empirical validation of PDisVAE? Reporting MIG-SUP scores would also be a plus. Note: The reviewer is willing to improve the scores if the work can be substatiated with quantitative results.

### Questions
See Weaknesses

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper introduces the Partially Disentangled VAE (PDisVAE) as a flexible extension to fully disentangled VAEs, addressing the issue of over-restrictive full independence assumptions in latent representations. By introducing partial correlation (PC) instead of total correlation (TC), the model can achieve group-wise disentanglement, which can be more suitable for complex data.  The paper provides a generalized formulation of partial correlation for group-wise independence and proposes an optimal importance sampling (IS) batch approximation to reduce the high variance issue seen in traditional TC computation methods

### Strengths
- The authors introduce the Partially Disentangled VAE (PDisVAE), which effectively addresses the limitations of fully disentangled VAEs by permitting group-wise disentanglement. This focus aligns well with current literature trends in the field of disentangled VAEs.

- The paper highlights the high variance issues present in existing batch approximation methods for total correlation (TC) and proposes an optimal importance sampling (IS) batch approximation for partial correlation (PC) as a solution to this challenge.

- Experiments conducted on synthetic datasets demonstrate the model's capability to effectively manage group-wise independence.

### Weaknesses
 **Structure of the Paper**

- The current structure could be refined for clarity. The introduction, in particular, could be reworked to clearly convey why disentanglement is needed and how incorporating total correlation (TC) or partial disentanglement can address specific limitations. This would help readers follow the paper’s motivation more naturally.
- Additionally, the use of `$ \vspace $` throughout the document, for example in lines 24–26, 197–200, and 370–371, does not align with ICLR formatting guidelines. Frequent use of `$ \vspace $` reduces readability, creating dense blocks of text. To improve flow, consider adjusting content and shortening details in the experimental section where information is clear from figures.

**Notation and Clarity Issues**

- There are a few instances where the notation could be made clearer. For example, `$ p(z|n_{*}) $` is introduced without a clear distinction from `$ p(z|n) $`, and `$ N $` in the summation notation is somewhat ambiguous. If `$ n_{*} $` refers to a specific data point, this should be clarified. Additionally, in line 206, batch notation could be simplified for readability by avoiding complex subscripts or just referring to "batch" directly.

**Context of Literature and Definition of Disentanglement**

- The paper introduces claims related to disentanglement but does not define the concept in enough detail. It would strengthen the paper to clarify at the beginning why disentanglement is challenging to achieve directly with VAEs.
- The authors might reference prior results indicating these challenges (which is not the case in the current version), such as those found in [Locatello et al., 2019] and [Ahuja et al., 2022]

**Clarification on Importance Sampling (IS) Approach**

- The authors state that their importance sampling (IS) approach in Table 1 improves prior methods, yet the differences and underlying assumptions remain unclear. It would be helpful to explicitly describe how this IS approach differs from previous work and to specify any variance assumptions. This would help readers better understand the novelty and practical impact of the method.

**Metrics for Assessing Disentanglement**

- The metrics selected, particularly $ R^2 $, assess identifiability but may not fully capture disentanglement. Complementing $ R^2 $ with additional metrics like DCI or RMIG (see [Eastwood et al., 2022] and [Carbonneau et al., 2022]) would provide a more comprehensive view of group-wise disentanglement. This addition would enhance the evaluation and provide stronger evidence of the model’s effectiveness.

**Concerns with Theorem 1 and Its Proof**

- In Theorem 1, the statement that $ (x_1, \ldots, x_I) \perp (y_1, \ldots, y_J) \iff f(x_1, \ldots, x_I) \perp g(y_1, \ldots, y_J) \ \forall $ functions $ f $ and $ g $ is not fully substantiated. While the forward implication $ \Rightarrow $ holds, the backward implication $ \Leftarrow $ requires additional assumptions.
- The authors attempt to establish the $ \Leftarrow $ direction by setting $ f $ and $ g $ as identity functions. However, this choice does not sufficiently demonstrate general independence of $ (x_1, \ldots, x_I) $ and $ (y_1, \ldots, y_J) $, as the independence of all functions of $ x $ and $ y $ does not imply the independence of $ x $ and $ y $ themselves. A counterexample, such as when $ x $ and $ y $ are jointly normal with non-zero correlation, illustrates this point.
- This portion would benefit from either additional assumptions to support the implication or a reformulation of the theorem to avoid overstating the result.

### Questions
1. **Use of $R^2$ for Assessing Disentanglement**: The paper utilizes $R^2$ as a metric to evaluate disentanglement. What justification do the authors provide for this choice, and how is $R^2$ theoretically connected to the concept of disentanglement? There appears to be ambiguity regarding how $R^2$ specifically relates to the disentanglement characteristics of the groups. For more information on alternative metrics, please refer to the weaknesses section.

2. **Comparison with Other Models**: How does the partial correlation term in PDisVAE theoretically improve the learning of latent representations when compared to existing methods like [5], including recent works that utilize Hausdorff distances to achieve independence of support instead of strict independence [6]? Are there particular theoretical guarantees or properties that PDisVAE upholds?

3. **Impact of Group Size**: In your experiments, varying group ranks may present challenges. From a theoretical perspective, how does the size of the groups influence PDisVAE’s ability to recover meaningful latent structures? Are there specific thresholds or bounds that could affect its performance?

4. **Variance in Estimates**: The authors highlight the high variance present in batch approximations for total correlation (TC). What theoretical considerations contributed to the creation of the optimal importance sampling method, and in what ways does it address these variance-related issues?

**References:**

[5] Yao, Dingling, et al. "Multi-view causal representation learning with partial observability." arXiv preprint arXiv:2311.04056 (2023).

[6] Roth, Karsten, et al. "Disentanglement of correlated factors via hausdorff factorized support." arXiv preprint arXiv:2210.07347 (2022).

### Soundness
2

### Presentation
1

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
The partially disentangled VAE is proposed to enforce groups of latent dimensions independent of each other. Within the group, the latent variables are correlated. The method outperforms baselines ($\beta$-VAE and $\beta$-TCVAE) in synthetic datasets, providing interpretable features for real datasets.

### Strengths
The paper's topic is relevant, and the idea behind the method is valuable.

### Weaknesses
While I appreciate the interest behind the partial correlation term in (5), I am not convinced about the paper in many aspects.

1) First of all, the writing style is sometimes vague and there and imprecise:

- "The core idea inspired by ICA is that non-Gaussian is independent", This statement seems oversimplified.

- " if the true number of disentangled latent components is two but we instruct the logcosh-priored VAE to find three, it will yield three components with poor disentanglement instead of finding two disentangled components and one non-informative component" Is there empirical evidence or theoretical justification for this claim about logcosh-priored VAE behavior? If so, could you provide it?

2) Important recent literature is overlooked. After a quick search I found:

- $\alpha$TC-VAE: On the relationship between Disentanglement and Diversity (ICLR 2024)
- Why do Variational Autoencoders Really Promote Disentanglement? (ICML 2024)
- Disentanglement via Latent Quantization (NeurIPS 2023)

    How do the methods in these papers compare to the proposed method in terms of handling group-wise independence?
    Are there specific metrics or experimental setups from these papers that would be particularly informative to include in the comparison?
    Do any of these papers address partial disentanglement, and if so, how does their approach differ from the one proposed here?

3) I cannot assess how conclusive the experimental results are over real data sets. 

-  Provide CelebA results for $\beta$-TCVAE and FactorVAE, or explain why these were not included.
- Describe their hyperparameter tuning process for all methods, including baselines. What range of values were explored for each hyperparameter?
- Report the best hyperparameter configurations found for each method, along with the performance achieved.
- If possible, include a sensitivity analysis showing how performance varies with key hyperparameters for each method.

4) Scalability and sensitivity. It would be important to analyze at least the following points:;

- Testing the method with increasing latent dimensions (e.g., 32, 64, 128) and reporting performance trends.
- Analyzing the impact of different grouping strategies on performance for a fixed latent dimension. For example, comparing random groupings vs. learned groupings. 
- Evaluating the method's performance with increasingly complex decoder architectures, and reporting how this affects both disentanglement and reconstruction quality.
- Discussing potential strategies for determining optimal groupings in high-dimensional spaces, or acknowledging this as a limitation if no clear solution exists.


Minor typo: q(z), the aggregated posterior, is not defined in (1)

### Questions
See above

### Soundness
2

### Presentation
3

### Contribution
3

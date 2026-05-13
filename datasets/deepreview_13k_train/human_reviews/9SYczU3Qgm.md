# Meta Flow Matching: Integrating Vector Fields on the Wasserstein Manifold

- Decision: Accept
- Scores: 8, 5, 6, 6

## Abstract
Numerous biological and physical processes can be modeled as systems of interacting entities evolving continuously over time, e.g.\ the dynamics of communicating cells or physical particles.
Learning the dynamics of such systems is essential for predicting the temporal evolution of populations across novel samples and unseen environments.
Flow-based models allow for learning these dynamics at the population level --- they model the evolution of the entire distribution of samples.
However, current flow-based models are limited to a single initial population and a set of predefined conditions which describe different dynamics.
We argue that multiple processes in natural sciences have to be represented as vector fields on the Wasserstein manifold of probability densities.
That is, the change of the population at any moment in time depends on the population itself due to the interactions between samples.
In particular, this is crucial for personalized medicine where the development of diseases and their respective treatment response depends on the microenvironment of cells specific to each patient.
We propose \textit{Meta Flow Matching} (MFM), a practical approach to integrating along these vector fields on the Wasserstein manifold by amortizing the flow model over the initial populations.
Namely, we embed the population of samples using a Graph Neural Network (GNN) and use these embeddings to train a Flow Matching model.
This gives MFM the ability to generalize over the initial distributions unlike previously proposed methods.
We demonstrate the ability of MFM to improve prediction of individual treatment responses on a large scale multi-patient single-cell drug screen dataset.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces Meta Flow Matching (MFM), a novel approach for modeling the evolution of systems consisting of interacting samples/populations. Unlike previous flow-based models, MFM can generalize to unseen initial populations by using a Graph Neural Network to embed the population and amortizing the flow matching model over these embeddings  The authors demonstrate MFM's effectiveness on an interesting synthetic letter denoising task and a large-scale single-cell organoid screening dataset, showing its ability to predict patient-specific responses to treatments.

### Strengths
- Novel approach: The paper proposes a new method for integrating vector fields using the full of probability densities - allowing the modeling of the evolution of entire distributions of samples (which is important for many biological and physical processes). I also believe this amortization effect is especially helpful in small-sample regimes.
- Theoretical foundation: The paper provides a solid theoretical basis for the proposed method, including the connections to existing approaches like conditional generative flow matching.
- Readability: The paper is *very* well written and easy to read and understand (although it's covering a complex topic)

### Weaknesses
 - Honestly, no weaknesses come to my eye. I've been working on Flows for a quite some time now, and have to say this is a good and well-executed idea.
-  Figure 1 (c) is not that helpful in my opinion.

Typos:
- "a a standard" (l420)
- "of of model" (l464)

### Questions
- In Eq.17, shouldn't the condition `c` be part of `\phi` or `v_t` as well?
- I am wondering in what cases I should *not* use MFM to model the change of a distribution using a flow? I can see that in Exp. 5.1 and 5.2, the samples have strong dependencies (e.g., to create the silhouettes), but in case there are no dependencies, would MFM also model this well?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This article deals with the problem of learning many-body dynamics via flow matching. The main objective is to model the interaction between components (e.g. particles) rather than modeling the entities separately. The resulting methodology allows to correctly model the evolution of distributions from the time evolution of observations of sample populations.

### Strengths
-- The problem is known to have plagued science for a long time. Therefore, new approaches and solutions are important contributions.
-- The idea of modeling the fields in the Wasserstein setting is intriguing, and intuitively meaningful.  
-- The authors relate their approach with mean-field limits and diffusion processes. This is certainly something of interest.

### Weaknesses
 -- First and foremost, the article is written in a very confusing way. It seems that the narrative is scattered, and this really makes it difficult to follow.
-- The problem seems to boil down to embedding populations using graph neural networks and then flow matching in Wasserstein manifolds.
-- It is unclear what a Wasserstein manifold is to start with. It clearly should not be a finite dimensional manifold, as depicted in their Figure 2. This is an infinite dimensional manifold, but the atlases are not clearly specified. For instance, a Banach manifold is a well understood object. In this case, the authors do not bother to introduce what they are talking about. P_2(X) is not generally even a Banach manifold. My understanding is that P_2(X) has a geometric structure only in some relatively special cases (Otto calculus), and usually people talk about metric over P_2(X), and the notion of curvature in Wasserstein spaces is often not the curvature of a manifold in the traditional sense of differential geometry. How is the tangent space defined in this context? In section 2.3 it seems that the author suggest that using the Wasserstein setup is rather important. As a consequence, I think it should not be left to the interpretation of the reader, but it should be clearly explained (at least defined).
-- In general, there is a terrible lack of definitions. Even the theorem, which should be a formalization of the work, is unclear because the definitions are either absent, or scattered throughout the article. At least an appendix with all definitions should be added.
-- The results do not seem overall particularly good. The table included in the text seems to show good results, but those in the appendix seem to show that the model is not particularly outperforming. One might not care much about this if the paper were a very well written piece of theoretical work, but as explained above it does not seem to be that case either.
-- Once the tangent space becomes an L2 space, some problems might arise. For instance, the matching now is a sort of average. Errors might be small "on average", but might blow up in certain regions that have not been explored. This is not considered in the article. Is there a reason to assume that it does not give rise to issues?
-- I have now noticed that some of the errors were train errors, as pointed out. I am unsure why these are included, since it is not usually a metric of particular interest, but this clarifies my previous comment. Is there a reason why OT does not seem to help the other models? Is there a theoretical reason, or just lack of hyperparameter fine-tuning?

### Questions
All weaknesses as stated above are my main questions.

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces an extension to Flow Matching (FM) called Meta Flow Matching (MFM) that efficiently accommodates generalizing to varying base distributions by featurizing the base distribution with a nearest-neighbor graph neural network (GNN).

More specifically, FM is a recent popular framework for generative modeling that works by first matching up a target distribution with a base distribution (e.g., a standard normal distribution, coupled to the target distribution via an independent coupling) and then training a vector field to match the resulting particle vector fields via minimizing the Mean Squared Error (MSE). A natural extension of this is Conditional Flow Matching (CFM) where the vector fields can be conditioned on some covariate, such as a generative prompt for image generation. The authors argue that there are compelling reasons to extend the problem setup to include varying base distributions. First, naturally occurring dynamics such as interacting particles or diffusion equations have dynamics that are explicitly distribution dependent and thus their particle versions cannot be modeled by vector fields that only depend on the particle location alone. Second, problems in molecular biology naturally lend themselves to considering different base distributions, such as predicting the drug response for different baseline cell distributions per patient.

Therefore, the authors suggest expanding the FM formulation with a distributional embedding that captures the base distribution and that is used as input to the vector field neural network. To obtain the embedding, they first calculate a k-nearest-neighbor graph on the base distribution and then embed it with a GNN, leading to the proposed MFM formulation. They show that MFM can be trained in the same manner as FM and show that it outperforms baseline architectures in experimental results on synthetic data (denoising rotated letter profiles) and on real data (mass-cytometry cell profiles on patient-derived cultures under drug treatments).

### Strengths
* The manuscript is overall well-written and organized.
* Flow matching is a popular generative modeling framework and is of significant interest to the ML community. I like the authors' motivation of the distribution dependence through the continuity equation and interacting particle systems. Their idea to solve this problem is simple and elegant and deserves exploration.

### Weaknesses
 * **Empirical results are not fully convincing and need strengthening:** The presentation of the empirical results leave me slightly puzzled, as explained in the following.
    * First of all, the authors consider [ICNN/CellOT](https://www.nature.com/articles/s41592-023-01969-x) as a baseline that can accommodate varying baseline distributions and conditioning. I think the introduction to ICNN presented in in Section 4 is slightly misleading: in lines 348-350, it is sometimes not clear what "the method" refers to. ICNN *can* generalize to new distributions, but the novelty in MFM is to take additional interactions into account. It is unclear if the authors are referring to the ICNN architecture itself or the CellOT method which uses this architecture. The distinction is important as the ICNN architecture alone does not address the distributional shift problem, while CellOT does attempt to address this, albeit in a different manner than MFM.
    * Since ICNN is conceptually the closest competitor to MFM, why did the authors not benchmark their method on the [dataset consider in that manuscript](https://onlinelibrary.wiley.com/doi/epdf/10.1111/exd.12683)? The chosen dataset in Section 5.2 seems well suited for the task, but it leaves me wondering why they swapped out datasets. Did their method not give them the desired results on previously considered datasets? The lack of direct comparison on the same dataset makes it difficult to assess the true improvement of MFM over CellOT.
    * The authors often claim that one method, in particular FM, "fails to fit the train data" (e.g., lines 472-473). This is a strong statement given that FM often surprisingly scores second-best out of the baseline methods. This makes me wonder about the underlying dataset and the employed metrics. At a minimum, I suggest reporting $\mathcal{W}_1$, $\mathcal{W}_2$ and MMD for the following very simple uninformed baselines to account for trivial underlying biological phenomena:
        * The base distribution itself, i.e., distance of the unperturbed patient cells to the perturbed cells without applying any model.
        * The base distribution shifted by a constant vector that is the mean over all perturbed cells (e.g., those in the train dataset)
    * Further, are there ways to better understand the overall quality of the predictions? Are there downstream conclusions of the dataset paper that can or cannot be reproduced by the various predictive algorithms? Can the authors plot some of the predicted distributions just as they did in Figure 3? It is not clear if the models are capturing meaningful biological signals or simply overfitting to the training data. Visualizing the predicted distributions and relating them to known biological effects would strengthen the results.
    * The generalizability of the results might be compromised by the authors' picking specific patients for the patient holdout setup (see Section C.2). Can the experiment be performed over several splits? The current evaluation setup might not be robust enough to demonstrate the generalization capabilities of MFM. Evaluating on multiple patient splits would provide a more reliable assessment.
    * In the same vein, I do not understand how the authors arrive at the error estimates for their experimental results if only one split is considered. I am afraid these estimates could be vastly underestimating the actual uncertainty. This is important since MFM sometimes only shows a small edge compared to FM. The lack of proper uncertainty quantification makes it difficult to assess the statistical significance of the results.
* **Independent matching may be supoptimal for all considered methods:** [Tong et al (2023)](https://arxiv.org/abs/2302.00482) propose to train flow matching by coupling base and target distribution via Optimal Transport instead of an independent coupling. This is a simple tweak that could be applied to all considered FM methods, i.e., FM, CFM, and MFM. I am curious if this would improve results across the board or specifically help FM and CFM because those methods currently have no way of accounting for different source distributions. Potentially, this could be a much simpler fix than MFM.
* **(minor)** The text contains quite a few typos. I suggest the authors do another round of proof-reading for the final version.

### Questions
I am recapitulating some of the problems outlined in "Weaknesses" above as questions to the authors here, as well as some other things that were not clear to me:

* How are uncertainties on your results calculated? If they are not derived from independent splits/seeds, I would suggest you do that.
* Why did you not benchmark MFM on the [dataset consider in the CellOT manuscript](https://onlinelibrary.wiley.com/doi/epdf/10.1111/exd.12683)?
* How is CFM set up on the patient data set? I assume you condition on the drug, while ignoring the base distribution/patient identity. Is this correct, or are you also feeding the patient identity as condition? If the latter, I would recommend the former.
* Can you add the following uninformed baselines to the experiments in Sections 5.1 and 5.2?
    * The base distribution itself, i.e., distance of the unperturbed patient cells to the perturbed cells without applying any model.
    * The base distribution shifted by a constant vector that is the mean over all perturbed cells (e.g., those in the train dataset)
* Are there ways to better understand the overall quality of the predictions? Are there downstream conclusions of the paper that introduced that can or cannot be reproduced by the various predictive algorithms? Could you plot some of the predicted distributions just as they did in Figure 3?
* I am surprised by the dynamic range of the Wasserstein distances vs MMD. For example, in Table 2, ICNN on the patient holdout achieves MMD of 74.00 and $\mathcal{W}_2$ of 4.681 vs MFM (k=100) with 8.96 and 4.269, respectively. Is there any intuition about this discrepancy in dynamic range?
* How is the $r^2$ calculated here? The model does not actually predict an output for a single target cell, but a distribution instead, so I am confused as to how this is done.
* Would you consider running experiments with Optimal Transport matching instead of independent coupling as considered in [Tong et al (2023)](https://arxiv.org/abs/2302.00482)?

### Soundness
2

### Presentation
3

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
- The paper proposes a new diagram of conditional flow matching models named meta flow matching.
- The high-level understanding is: meta flow matching represents the conditional input in a new way -- by embedding the information of the whole population (or saying distributions).
- In math, this can be formulated as constructing the vector field in the Wasserstein manifold.
- The authors then provide the technical construction of the model, including objective functions and parametrization.
- Numerical experiments are conducted on synthetic and organoid drug-screen datasets.
- I am happy to see this conceptual novelty in the approach.
- I didn't thoroughly check the technical part in the paper while I didn't see anything odd.
- I am a little concerned on certain claims and the effectiveness of the method, both conceptually and numerically.

### Strengths
I am listing both strengths (+), weakness (-) and questions (?) in the following to make the review more logistic.

- (+) The meta flow matching diagram is clearly novel. The specific new part is the population/distribution embedding that the model can distinguish and evolve differently in different population, for the same particle.
- (?) Question on ODE: Then what is the particle-level ODE corresponding to the PDE (12)? Is it similar to FP-equation that dx/dt = vt(x, pt)? Can the author prove it or give the detailed reference?
- (?) Can you method be extent to SDE case?
- (?) Analysis of population embeddings: To learn the population embeddings, I believe you should have enough example of populations otherwise the generalization is less promised. I would like to see a detailed analysis of population embeddings for a sanity check in both experiments.
- (-) Reduced number of data points: Following the last point, for the organoid drug-screen experiment where only contains 10 patients, does it mean there are only 10 populations (data point for patient population embeddings)? It is out of expectation that model can capture the right population embeddings from 10 data points.
- (?) Why replicate-split in the organoid drug-screen experiment is meaningful? In my understanding the conclusion drawn from different replicates usually would be consistent (that they has similar patterns).
- (?) I also do not quite understand why other baselines under-perform in the replicate-split since if I understand correctly, generalization would not be a big challenge here.
- (?) Can you provide a random baseline for your experiments? Random guess baseline and random initialized model baseline.
- (-) An extremely important reference of "Deep Generalized Schrödinger Bridge" is missed here. Conceptually this paper should be sth ahead of yours and need to be discussed in details. Population embedding is also adopted in the paper in a simpler way.
- (?) To further illustrate the effectviese, I think comparison with the numbers and experiments in "Deep Generalized Schrödinger Bridge" is necessary.
- (?) Comparison with the number and experiment in "Learning single-cell perturbation responses using neural optimal transport" is also necessary in my eye. This is a classical paper and one of your competitor method.
- (?) Complexity: Can you provide a complexity analysis here? Your method need additional embedding of the whole population and I think the scalability performance needed to be shown somehow (w.r.t. the size of population) which is very useful to the community for method selection.
- (?) How do you construct the graph in the organoid drug-screen experiment? How different graph construction impact your model results?

### Weaknesses
See Strengths.

- (+) The meta flow matching diagram is clearly novel. The specific new part is the population/distribution embedding that the model can distinguish and evolve differently in different population, for the same particle.
- (?) Question on ODE: Then what is the particle-level ODE corresponding to the PDE (12)? Is it similar to FP-equation that dx/dt = vt(x, pt)? Can the author prove it or give the detailed reference?
- (?) Can you method be extent to SDE case?
- (?) Analysis of population embeddings: To learn the population embeddings, I believe you should have enough example of populations otherwise the generalization is less promised. I would like to see a detailed analysis of population embeddings for a sanity check in both experiments.
- (-) Reduced number of data points: Following the last point, for the organoid drug-screen experiment where only contains 10 patients, does it mean there are only 10 populations (data point for patient population embeddings)? It is out of expectation that model can capture the right population embeddings from 10 data points.
- (?) Why replicate-split in the organoid drug-screen experiment is meaningful? In my understanding the conclusion drawn from different replicates usually would be consistent (that they has similar patterns).
- (?) I also do not quite understand why other baselines under-perform in the replicate-split since if I understand correctly, generalization would not be a big challenge here.
- (?) Can you provide a random baseline for your experiments? Random guess baseline and random initialized model baseline.
- (-) An extremely important reference of "Deep Generalized Schrödinger Bridge" is missed here. Conceptually this paper should be sth ahead of yours and need to be discussed in details. Population embedding is also adopted in the paper in a simpler way.
- (?) To further illustrate the effectviese, I think comparison with the numbers and experiments in "Deep Generalized Schrödinger Bridge" is necessary.
- (?) Comparison with the number and experiment in "Learning single-cell perturbation responses using neural optimal transport" is also necessary in my eye. This is a classical paper and one of your competitor method.
- (?) Complexity: Can you provide a complexity analysis here? Your method need additional embedding of the whole population and I think the scalability performance needed to be shown somehow (w.r.t. the size of population) which is very useful to the community for method selection.
- (?) How do you construct the graph in the organoid drug-screen experiment? How different graph construction impact your model results?

### Questions
See Strengths.

### Soundness
3

### Presentation
2

### Contribution
3

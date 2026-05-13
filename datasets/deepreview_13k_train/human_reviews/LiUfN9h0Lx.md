# Efficient and Accurate Explanation Estimation with Distribution Compression

- Decision: Accept
- Scores: 6, 8, 8

## Abstract
Exact computation of various machine learning explanations requires numerous model evaluations and in extreme cases becomes impractical. The computational cost of approximation increases with an ever-increasing size of data and model parameters. Many heuristics have been proposed to approximate post-hoc explanations efficiently. This paper shows that the standard \iid sampling used in a broad spectrum of algorithms for explanation estimation leads to an approximation error worthy of improvement. To this end, we introduce \emph{compress then explain}~(\cte), a new paradigm for more efficient and accurate explanation estimation. \cte uses distribution compression through kernel thinning to obtain a data sample that best approximates the marginal distribution. We show that \cte improves the estimation of removal-based local and global explanations with negligible computational overhead. It often achieves an on-par explanation approximation error using 2--3$\times$ less samples, i.e. requiring 2--3$\times$ less model evaluations. \cte is a simple, yet powerful, plug-in for any explanation method that now relies on \iid sampling.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
the paper introduces CTE uses distribution compression through kernel thinning to obtain a data sample to better and more efficiently approximate the marginal distribution. This method is recommend to significantly reduce the computational complexity of attribution-based methods such as SHAP and SAGE.

### Strengths
This approach significantly reduces the computational complexity of SHAP and SAGE.

### Weaknesses
line 53 - "We introduce a new paradigm for estimating post-hoc explanations based on a marginal distribution" ---> The main contribution of paper is not clearly described. From the introduction, reader might get the idea that you are proposing a new explanation method that employs KT, but as we go further into the paper, the tone of authors changes and they focus on the effectiveness their approach for Kernel SHAP and SAGE.

the idea of this paper needs to be more clearly stated. From my understanding the paper attempts to improve the computation time of SHAP and SAGE using Kernel thinning. The Kernel Thinning is proposed to better select the samples for the feature attribution explanation. The idea seems interesting and this can help with the Shapely and Sage method, but this approach is only specific to these explanation method that are based on the selection of subsets of data. 

The experimental evaluation is heavily focused on MAE with  the explanation as "...". I wonder if this approach is the main criteria that paper investigated, what is the main baseline that they compare with to obtain the explanation error. If the explanation error is calculated with the SHAP with the iid sampling, so what does Table 1 mean. because in this table the paper explains that from the iid sampling the MAE of explain improved to something that is achieved with CTE.

Also the paper only explored the Gaussian Kernel. Why that choice? why not exploring other kernels? What is the theoretical aspect of Gaussian that advantages your approach?

also, I wanted to see some examples of how the trained explainer using your method performs for image and examples of IMDB dataset. The paper heavily focuses on the MAE without providing any example to show the qualitative comparison of generated explanation

The main purpose of KT, is reducing the computational complexity and the quality of generated explanation, but since this method is focused on the data attribution concept, I was expecting see a comparison between the KT and Influence Function in extracted explanations.

### Questions
line 184 - definition 4 - it is not clear what is the output f this function and how do you compare it with for calculation of MAE. how the explanation error is defined and how it is calculated? as far as I understand the mean absolute error is measured based on the difference between the assigned values to  features of explanation from the SHAP  with iid and CTE. but to it is not clear that without iid how do you calculate the feature values. if SHAP + i.i.d sampling is not the baseline, the please clearly explain how you calculated the baseline feature values? what is the baseline for that you compared the iid and cte sampling? (Table 1)

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper proposes distribution compression as an alternative to iid sampling for explanation estimation. The proposed approach is supported by theoretical guarantees. It also improves computation cost while still achieving errors comparable with iid sample empirically.

### Strengths
- The proposed method is solid and supported by theoretical bounds on the error.

- This topic is outside my expertise but I was able to follow the paper. So I think the authors did a good job summarizing the related work and providing relevant background information.

### Weaknesses
 - I overall enjoyed reading this paper. 

- I am not an expert on this area. But it looks like going from iid sampling (the paper's main comparison point) to this more complicated CTE framework (based on kernel thinning) is a big step. I am wondering if there are any other baselines in between these two extremes. For instance, a sampling strategy but not exactly uniform? If there are such baselines, I think it would be good to see a comparison against them too to understand the tradeoff between how complicated the compression scheme is vs how much we can reduce the data size vs the error.

### Questions
-

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper tackles the problem of efficiently approximating the marginal distribution that is often used in post hoc explanation methods. The authors propose using kernel thinning to obtain a compressed sample of the "background" samples that are used to empirically estimate the marginalization. The proposed compress then explain method is then empirically demonstrated to require orders of mangitude fewer samples to achieve on-par explanation approximation error compared to i.i.d sampling which is generally utilized.

### Strengths
The paper is well written. The biggest strength of the paper is the thoroughness of the experiments. For a paper that is largely an empirical demonstration it is great to see the rigour that clearly went in to the experiment section. The proposal is a neat application of an existing technique in a new domain.

### Weaknesses
While the experiment section is rigorously presented, there's room for improvement in presentation - specifically the figures and figure captions. Most of the figures have multiple plots and a single caption. It'd be better to label the sub-plots in each figure as a, b, c,... and then use the caption to describe each figure succinctly. This allows the reader to look at the figures and understand them, rather than having to jump back and forth between the main text and figures.

The other weakness is the fact that this is largely an application of an existing method for efficient sampling. It *is* still a useful contribution to apply this method to explanations, this could be an even better publication if the sampling method was also improved specifically for post explanation methods.

### Questions
I'd be interested in hearing the authors' thoughts on the second "weakness" above.

### Soundness
3

### Presentation
3

### Contribution
3

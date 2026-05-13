# Multi-Marginal Stochastic Flow Matching for Alignment of High-Dimensional Snapshot Data at Irregular Time Points

- Decision: Reject
- Scores: 6, 5, 5, 3

## Abstract
Modeling the evolution of high-dimensional systems from limited snapshot observations at irregular time points poses a significant challenge in quantitative biology and related fields. Traditional approaches often rely on dimensionality reduction techniques, which can oversimplify the dynamics and fail to capture critical transient behaviors in non-equilibrium systems. We present Multi-Marginal Stochastic Flow Matching (MMSFM), a novel extension of simulation-free score and flow matching methods to the multi-marginal setting, enabling the alignment of high-dimensional data measured at non-equidistant time points without reducing dimensionality. The use of measure-valued splines enhances robustness to irregular snapshot timing, and score matching prevents overfitting in high-dimensional spaces. We validate our framework on several synthetic and benchmark datasets and apply it to single-cell perturbation data from melanoma cell lines and gene expression data collected at uneven time points.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper presents a novel flow matching method. This method can be applied to high dimensional data measured at non-equidistant time points without reducing dimensionality, so that the dynamics of the data are not oversimplified. The method is validated on several datasets and showed the improvement compared to existing methods.

### Strengths
I think the paper is in good quality. Other than the concerns about the window size k, the paper is clearly written.

### Weaknesses
My impression is that this paper is somewhat an extention of Tong et al. (2023b). Although, my research is not in stochastic flow matching, so I cannot correctly evaluate originality or significance.

As far as I understand, the window size k is a hyperparameter that critically affects the performance. Though it is not clear how to choose k. On page 5, it seems like k=2 is a natural choice, but without any reasoning or discussion. I think a discussion of the tuning of k would be helpful to readers, for e.g., it should be just trying several different values of k and choose the best one, or k=2 is the natural choice for some reason.

On Table 1, triplet(k=2) seems to dominate pairwise(k=1) for many cases, which makes readers to wonder if k=3 can be even better. This is due to that "k is balancing bias and variance" in line 215, since then bias-variance tradeoff is likely to appear, i.e., as k increases, the cost would decrease and increase. If there is a reason to use k=1 or 2, a reasoning should be helpful, and if there is no specific reason to stick to k=1 or 2, then more experiments with increasing the values of k and observing the bias-variance tradeoff trend would be very helpful to readers.

Algorithm 1 is written for general values of k, but in line 216-276 the k is fixed as 2 in the explanation. My impression is that explaining with k=2 doesn't really simplify the explanation by much, but making extra confusions: I wondered if the explanation would be the same for general k or some extra changes are needed. I think it's better to write the explanation in line 216-276 with general k.

### Questions
As far as I understand, in line 9 and 10 of Algorithm, X_i should be X_{t_i}, based on the explanations on Section 2 3.1.. Are these typo, or is my understanding wrong?

### Soundness
4

### Presentation
2

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
The paper tackles the problem of modeling time evolution in high-dimensional systems, from limited snapshots at irregular time-points. In contrast to traditional dimensionality reduction approaches (which can oversimplify dynamics), this paper extends the recently proposed flow matching method to the multi-marginal setting. By learning flows over rolling windows of aligned subsets of snapshots, they focus on modeling local dynamics with additional improvements to incorporate stochasticity and reduce overfitting. 

The method is validated on three synthetic datasets, constructed with specific characteristics, and a real world dataset of cancer cell lines from uneven timepoints.

### Strengths
**Significance**
The problem being studied is highly significant, given its utility in understanding biological processes, and designing effective interventions

**Originality**

Since the paper focuses on extending flow matching to the multi-marginal setting, my comments are restricted to this. Currently, flow matching methods focus on learning vector fields that transport a distribution $q_0$ towards a distribution $q_1$, without explicit modeling of $q_t$. Extending flow matching to multi-marginal settings can be accomplished by either using trajectory information (if available), or performing flow matching over restricted subsets of snapshots. This paper adopts the latter route. 

The paper locally aligns snapshots, and uses this alignment to compute the conditioning vector fields for flow matching. The proposed solution is simple and elegant in that regard, and easy to implement computationally. 

**Clarity**
The paper in itself is well-written and clear, and the motivation, objectives and method were easy to follow. Some of the presentation can be enhanced (see Weaknesses and Questions), especially in experiments.

**Quality**
The quality of the submission is moderate. The proposed idea is simple and well-executed, the text is well-written, but presentation can be improved in the experiments and prior work needs to be properly contextualized.

### Weaknesses
The main weaknesses of the papers are in the presentation concerning the experimental section, and improper contextualization of prior work. 

**Prior Work**

OT-based methods for understanding cellular modelling of trajectories are largely missing. Example such works included below:
1. Optimal-transport analysis of single-cell gene expression identifies developmental trajectories in reprogramming. Schiebinger et al 2019.
2. Proximal Optimal Transport Modeling of Population Dynamics. Bunne et al 2022.
3. Trajectorynet: A dynamic optimal transport network for modeling cellular dynamics. Tong et al. 2020

Multi-marginal generative modeling has also been studied by a few works in recent times:
1. Deep multi-marginal momentum schrödinger bridge. Chen et al 2023
2. Multimarginal generative modeling with stochastic interpolants. Albergo et al. 2023

I can see the methodological differences between existing work and the current one, but without proper experimental comparison, it makes it unclear why and where the proposed method improves / fails compared to the previous ones.

**Experiments**

The experiments of synthetic data would benefit from improved presentation. My takeaway is that the authors validation attempts to recover bifurcation points in the trajectories, based on other local snapshots but this is very hard to see in the figures. 

1. It would be nice to add a colored window / vertical line to differentiate between training and validation snapshots, and improve the font corresponding to time. 
2. The authors should also add the ground truth trajectories wherever possible, or make the ground truth snapshots more visible.

### Questions
**Experiments**
1. On the DynGen simulated trajectories, MIOFlow seems to do a much better job at capturing the evolution compared to the proposed method. Do the authors have any insight on whether this happens because of a specific training-validation split or an inherent difference between the two methods?

2. The experimental validation can further be improved by considering multiple snapshots to predict instead of just a single one. For example, in the $\alpha$-gaussians, it would be interesting to see if the model can recover the bifurcations given just the snapshots in the initial and latter timepoints. 

3. Is local modeling of dynamics always the best option? I agree there must be a tradeoff between local vs global dynamics modeling, but my intuition is that encouraging the model to learn global patterns (by doing flow matching on initial and terminal distributions), while having rolling windows locally would help the model learn both local and global patterns. I would be interested in hearing any comments the authors have in this regard, and if they have some experimental validation for this.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a multi-marginal stochastic flow matching framework to align high-dimensional snapshot data observed at irregular time points. By extending simulation-free conditional flow matching methods, incorporating overlapping subsets, and using measure-valued splines, the authors aim to improve robustness and stability. The method is applied to synthetic datasets and single-cell biological data, showing potential for high-dimensional data alignment.

### Strengths
Strengths:
- **Originality**: This paper proposes a new method to improve multi-marginal stochastic distribution matching in a rolling window fashion. 
- **Clarity**: This paper is well-written and easy to follow. 
- **Significance**: The problem investigated in this paper is important in single-cell computational biology.

### Weaknesses
Despite the strengths discussed above, there still exists some concerns:

- **Methodological novelty** :  While this paper proposes a multi-marginal stochastic distribution matching framework by leveraging overlapping subsets and score matching, many of the novelty claimed in the paper are inherent over existing methods (e.g., SF2M [1], CFM [2, 3]). For example, coupling the distribution without reducing dimensionality (already be presented in both CFM and SF2M), score matching (already be presented in SF2M), and measure-valued spline used in the computation of multi-marginal optimal transport. And handling the multi-marginal distribution matching can also be done by CFM and SF2M. The key novelty here, to my knowledge, is insert multi-marginal OT in SF2M framework with a rolling windows fashion, which may lack significant technical or methodological improvements. Specifically, the use of measure-valued splines, while mathematically sound, doesn't inherently guarantee a superior solution to the underlying optimal transport problem compared to existing methods, especially when considering the computational overhead. The core idea of using overlapping windows, while intuitive, lacks a strong theoretical justification for why it would lead to more accurate or robust results compared to direct pairwise transport, especially given that the underlying transport problem is still solved locally within each window.

- **Experimental design**:  There is a lack of direct comparisons with highly closely related methods like SF2M or CFM where this framework builds upon them, which undermines the credibility of the benchmarking.  Furthermore,  in SF2M it can handle thousands of gene dimensions, but this paper only tested 15 gene dimensions in the scRNA-seq data. It also raises the question of why the authors chose to compare their method with MIOFlow, which may rely on a low-dimensional manifold and seemed not be a fair enough comparison. The choice of MIOFlow as the primary baseline is questionable, as it does not directly address the same problem of multi-marginal stochastic flow matching in high dimensions. A more appropriate comparison would involve methods that explicitly handle time-series data with similar characteristics, such as those based on Schrödinger bridges or other forms of optimal transport.

- **Weaknesses in explaining why the framework is better**: For example, the explanations of the claimed robustness and stability in multi-marginal settings and handling irregular time points are descriptive rather than supported by theoretical rigor. The paper claims to handle irregular time points effectively, but the main challenge in such scenarios is the information loss over longer intervals, which may not be easily mitigated by the algorithm alone. The paper does not demonstrate a concrete advantage in this regard. The manuscript does not provide a clear explanation of how the proposed method addresses the challenges posed by irregular time points, such as varying intervals between observations. It is unclear how the method adapts to these irregularities, and there is a lack of empirical evidence demonstrating its superiority in such scenarios compared to methods that assume uniform time intervals.

- **Computational complexity and scalability**： When taking the multi-marginal OT in a rolling windows fashion rather than direct two point OT, there is a lack of discussions of the increased computational complexity and the balance between computational cost and accuracy. I think it may be taken into account to ensure a fair comparison. The paper does not include a detailed analysis of the computational complexity of the proposed method, particularly in relation to the window size and the number of time points. This is crucial for understanding the scalability of the method to larger datasets and more complex scenarios. The lack of discussion on the trade-offs between computational cost and accuracy makes it difficult to assess the practical applicability of the proposed approach.

- **Hyperparameter selection**: The hyperparameter $k$ seems an important factor in the framework. However, how to choose $k$ was not discussed in this paper, e.g., to balance accuracy and computational cost. It seems also need further investigations. The selection of the window size $k$ is a critical aspect of the proposed method, yet the paper lacks a clear strategy or guidelines for choosing an appropriate value. The impact of $k$ on the accuracy and computational cost of the method is not thoroughly investigated, and there is no discussion of how to balance these factors when selecting $k$.

- **Code and data availability**: The code and data is not available.

### Questions
see my questions asked in weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a method for computing the evolution of high-dimensional snapshot data taken at irregular time points using multi-marginal stochastic flow matching. Aimed at single-cell perturbation studies, it addresses the limitations of traditional approaches that often rely on dimensionality reduction. Instead, this model operates in a high-dimensional space where it interpolates smooth transitions between non-equidistant time points using optimal transport plans. Experimentally, the paper demonstrates the method on a limited set of synthetic and a single real-world single-cell datasets.

### Strengths
- **Introduction and Motivation**: The paper is well-motivated and effectively introduces the research problem. Both the abstract and Section 1 are clearly written.
- **Problem Statement**: The problem is clearly stated and directly addresses an existing challenge in practice, particularly within life sciences. It is well-grounded in biological applications and provides relevant context.
- **Approach**: The approach seems to be solid. It directly models flows in high-dimensional space, aims to introduce a certain robustness, and uses overlapping triplets in time-series alignment captures local dynamics at non-equidistant intervals.

### Weaknesses
 - **Problem Formulation and Methodology**: The explanation in Section 2 could benefit from additional intuitive descriptions, particularly clarifying relationships between indices $i$, $t_1$, and $t_i$. The transition from Section 2.0 to 2.1 lacks motivation, and it is not immediately clear why the authors chose to consider Optimal Transport (OT) in their methodology. The rationale behind some methodological decisions---such as the use of dynamic formulation for Wasserstein distance---needs significant expansion. Defining $u_t(x)$ earlier in the text would also improve clarity.
- **Hermitian Cubic Splines**: The introduction of Hermitian cubic splines seems superfluous for the remainder of the paper, adding complexity without relevancy. Additionally, it is unclear why the transition from basic transport splines to complex OT plan compositions (l. 157) is necessary or beneficial, as it lacks arguments. This part needs a better contextualized to clarify why compositions of OT plans are advantageous.
- **Drift Networks and Score Networks**: In Section 2.3, the introduction of "drift networks" and "single score networks" lacks clear motivation and context. It is unclear why these are required, how they work, and what role they play in the overall approach. More motivation and context are necessary.
- **Choice of Hyperparameters**: The choice of $k=2$ (l. 216) as a window size lacks sufficient explanation. Similarly, the roles of bias and variance (l. 215) are not adequately explained. The connection between the window size $k$ and the computational cost is also not discussed.
- **Computational Cost**: The computational complexity of multi-marginal OT and spline calculations may limit the scalability of this approach for large datasets, which could be problematic for real-world applications---a more comprehensive discussion is required. The paper does not provide an analysis of how the computational cost scales with the number of time points, the dimensionality of the data, or the window size $k$.
- **Competitors**: The paper considers a limited set of benchmark algorithms in its comparisons. Expanding the selection of competing methods would provide a clearer context for assessing the practical performance of MM-SF2M. The choice of baselines is not well-justified, and it is unclear why specific methods were selected while others were omitted.
- **Experimental Setup**: The experimental setup lacks clarity, detailed motivation, and clear reasonings. It is unclear why specific datasets were chosen, what the intended outcomes of these experiments are, or how they systematically test the capabilities or limitations. The paper does not provide a clear explanation of how the experimental parameters were chosen or how they might affect the results.
- **Datasets**: As experiments are limited to three synthetic datasets and only one real-world dataset, it is uncertain whether MM-SF2M can be broadly applied across diverse problem domains. The paper does not address the limitations of the datasets used and how they might affect the generalizability of the results.
- **Pairwise vs. Triplet Model**: Figures 1–3 suggest that the pairwise model is quantitatively sufficient, which the authors also acknowledge. This behavior is quite unexpected, and additional investigations and clarifications are needed. The paper does not provide a clear explanation of why the triplet model does not offer a significant improvement over the pairwise model, which contradicts the motivation for using multi-marginal OT.
- **Mini-Batch Sampling**: While the authors mention inconsistency through mini-batch sampling, it has never been motivated why we would use mini-batch sampling in in the first place. A discussion is quite important, especially if they suspect a problem with this choice. The paper does not discuss the potential impact of mini-batch size on the stability and convergence of the method.
- **Experimental Conclusions**: Some experimental claims are unclear, for example the claim that the "GAE provides a consistent and invertible representation, allowing new data to be embedded in the same coordinate system **without distortion**." Given that distortion-free low-dimensional embeddings are highly challenging and quite unlikely, this point requires further proof, more substantiation, and considerable clarification. The paper does not provide a rigorous justification for this claim, and it is unclear what specific properties of the GAE enable this.
- **Claims Not Validated**: The paper claims that the method enhances robustness and stability in multi-marginal settings "even when handling arbitrary timepoints", but lacks sufficient theoretical or experimental evidence to support this claim. The paper does not provide a theoretical analysis of the robustness and stability of the method, and the experimental results do not sufficiently validate this claim.

#### Minor Comments  
- To enhance the appeal to a wider audience, the authors could consider broader terminology, such as using "relevant information" instead of "biological information."
- **Figures**: While pretty, Figures 1–3 are not particularly informative and could be compactified to make room for an extension to Section 2.
- l. 142: "challenging in high dimensions [CITATION NEEDED]": A reference here would support this claim, which, while likely true, would benefit from citation for readers interested in further exploration.

### Questions
-/-

### Soundness
3

### Presentation
2

### Contribution
2

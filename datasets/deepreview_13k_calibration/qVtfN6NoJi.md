# Layer-Varying Deep Reservoir Computing Architecture

- Decision: Reject
- Avg Score: 4.60
- Scores: 5, 3, 5, 5, 5

## Abstract
Data loss and corruption are common incidents that often lead to catastrophic consequences in both theoretical and experimental facets of data analytics. The aspiration to minimize the impacts of such consequences drives the demand for the development of effective data analytic tools and imputation methods to replace missing, corrupted, or artifacted data. 
The focus of this paper is on multivariate time series imputation, for which we develop a dynamical systems-theoretic deep learning approach. The central idea is to view a multivariate time series as a trajectory of a dynamical system. Then, we construct a deep reservoir computing architecture to model the temporal evolution of the system by using existing data in the time series. In particular, this architecture is composed of a cascade of echo state network (ESN) layers with diminishing reservoir sizes. We then propose a layer-by-layer training scheme, which gives rise to a deep learning-based time series imputation algorithm. We further provide a rigorous convergence analysis of this algorithm by exploiting the echo state property of ESN, and demonstrate the imputation performance as well as the efficiency of the training process by utilizing both synthetic and real-world datasets arising from diverse applications.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work describes a new deep reservoir computing architecture (RCN) composed of multiple echo state network (ESN) layers, focused on the task of multivariate time series imputation. The authors then state the echo state property (ESP) for this new network and prove a sufficient condition for the RCN to satisfy ESP. They also study the convergence of RCN, proving an upper limit for the convergence rate. The method is then tested on both synthetic and real-world data.

### Strengths
*Originality*

To the best of my knowledge, the architecture introduced in this work (RCN) is original.

*Quality*

The authors perform all the analyses that I would expect from a paper that proposes a new reservoir computing architecture. In particular, they don't just test their method experimentally, they also provide theoretical grounds, rooted in dynamical systems theory, to show that RCN does satisfy ESP and a study of the complexity and efficiency of their method. The experiments are rigorous, with a large selection of baselines to show the network's performance, but also to explore the role of some hyperparameters.

*Clarity*

The claims and the arguments to sustain each of them are logically and consequentially laid out. The structure of the paper follows what one would logically expect.

*Significance*

The topic of how to deal with corrupted data is very relevant. The application of reservoir computing to imputation tasks is relevant, given the efficiency of RC.

### Weaknesses
 *Quality*

1. In line 161, you state that a monotonically decreasing nonnegative sequence necessarily converges to 0. Maybe you are missing some other assumptions?

2. In line 269, you define the reservoir space as the vector space spanned by the rows of $\boldsymbol R^{(k)}$, so I understand that it's a $(T-\omega)$-dimensional space. I think that this name is a bit misleading since it's usually used to refer to the space of the reservoir states, so the columns of $\boldsymbol R^{(k)}$. Later, in line 279, you mention increasing the number of neurons (i.e. $N$), and you call that the "dimension of the reservoir space". Unless I'm missing something, there is a bit of confusion in terms. But I do find the underlying argument sound.

3. While reading your work, the mind goes quite naturally to the deep ESN architecture described by Gallicchio et al., which you mention in the related works section. There you state that your method is "fundamentally different" form the deep ESN. I do agree that it is different since you have an output layer sandwiched between ESN layers, but I think that more details are required to understand why that structural change is "fundamental". Is it better in terms of performance and efficiency? 

4. When proving that RCN has ESP, you never mention (unless I missed it) the standard hypotheses on the compactness of the reservoir and input states. It stands out because the ESP can't be linked only to the dynamics of the reservoir state, it must depend also on the input.

5. In line 431, you state that the MSE results "are lower than 50% of those resulting from other methods", which doesn't seem a fair description of the table for all baselines, in my opinion.

6. One of the claims of the paper is that your method is more efficient, I presume in terms of computational resources. I don't see this claim supported by experiments, could you maybe quantify it?

*Clarity*

There are several mistakes and typos that, to different degrees, affect the readability of the paper. I list here a few:
- At about line 134, the superscripts of the definition of the function $f$ are wrong. Similarly, on line 165, it should be $\boldsymbol{Ar}+\boldsymbol{Bu}\in\mathbb{R}^N$.
- At line 158, it seems to me that the contraction is on the first component of the reservoir state, not the second.
- In line 163, you call "activity function" instead of "activation function". Line 215, "wight" instead of "weight".
- Lines 221-231: 
  - The matrix $\boldsymbol C$ I think it should have a superscript $(k)$
  - The definition of $\boldsymbol R^{(k)}$ is a bit confusing since all its components have the same subscript $t$, while it should change from $\omega$ to $T$
  - Sometimes the $\omega$ becomes a $w$. They are very similar, but if you notice the difference it can be confusing.
  - Is the dagger symbol the More-Penrose pseudoinverse?
- The total number of layers is sometimes referred to as $\mathcal K$, sometimes as $K$.
- Line 349, the symbol $p$ was already used to describe to dimension of the input $\boldsymbol u_t$
- Line 373, the reservoir size is referred to as $N_x$, it was just $N$ before
- Line 394, "the algorithm converges in no more than iterations", it's missing something

Apart from typos and other easily fixable mistakes, I report here what are in my opinion some more serious problems:
- The clarity is affected negatively by the use of a quite heavy notation, with a lot of superscripts and subscripts. To mitigate this, maybe something that could help is to remove all the $1:\omega$ subscripts: in my opinion, they are not necessary, especially because they are almost always the same. Would it be possible to just assume $\omega=0$ everywhere and forget about it during the theoretical discussions?
- The parameters $\omega$ (line 221) and reservoir node degree $d$ (line 374) should be defined somewhere first. I presume $\omega$ is the relaxation time, and maybe $d$ is the connectivity (?).

### Questions
1. In their work on Deep ESN, Gallicchio et al. argued that a deep structure provides a "multiple time-scales representation" of the input. Is there a similar argument that justifies your modification?

2. Proposition 3.1 provides a sufficient condition for the RCN to have ESP. How does it relate to other criteria developed in the literature? Is it equivalent to the "diagonal Schur stable" condition given by Yildiz et al. in *Re-visiting the echo state property*? It would be nice to expand the relationship between the two, at least to clarify if your proof is also new or if it's standard

3. In "Limitations and future works", you say that ESP is problematic when there is missing data at the beginning of the time series. I don't fully understand the link between ESP and having missing data, could you maybe clarify this?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The work discusses an application of deep echo state networks (ESN( to timeseries imputation. Missing measurements are incrementally imputed in the multivariate timeseries through predictions generated by the readouts attached to the different layers of the ESNs. Experiments are provided to validate the efficacy of the methodology against related timeseries imputation methodologies and 4 datasets.

### Strengths
* Imputation in multivariate timeseries, especially when considering missing whole blocks of observations, is an interesting topic for the community working on spatio-temporal data and may achieve good impact.

 * The proposed approach is well rooted into the literature of efficient timeseries processing via reservoir computing methods: design choices are solid in this sense.

### Weaknesses
 * Originality of the approach is minor. The proposed methodology is essentially using a standard deepRC/deepESN architecture with read-outs for each layer (an architectural pattern already explored by Gallicchio et al, 2017 and Gallicchio et al, 2018, among the others). The key catch of the approach is that a read out at layer k is trained to predict masked/missing dimensions of the multi-variate timeseries using observable dimensions and a self-generated target from the previous layer. Section 2 (last line) contains a claim of novelty against previous deepRC approaches (being "fundamentally different") but no discussion is provided to substantiate what is such substantial difference. Architecturally the approach seems very much the same of earlier works, with the addition of a self-supervised incremental training and the application to timeseries imputation.

 * Clarity and quality of the presentation are also limited. The manuscript is particularly unclear about the separation between literature results and own novel contributions. An example has been given in the comment above. Another example is the attribution of results on reservoir contractivity and the dynamical systems interpretation of timeseries and reservoirs. These are widely known results from literature which are not appropriatly acknowledged, e.g. by providing bibliographic references in Section 3. Also, the paper mixes reservoir computing with echo state networks without making explicit the difference between the two (in fact ESNs are used without being introduced and a sort of synonimity between RC and ESN is hinted at in the paper, which is wrong): this is confusing for a novice of the RC field. Low presentation quality is also evident from wording errors which could easily spotted with any syntax checking tool (not even grammar checkers): e.g. "wigth matrix" in page 4, "groudtruth" in page 6, etc.

 * The soundness of the theoretical results is not entirely convincing. The error bounds in page 6 (Theorems and corollary) seem to be demonstrated for the $Y_w:T$ part of the timeseries, which is convincing as this is the target of the readout training on those portions of the timeseries which have no missing values (at least this is what stated in page 5). Now, what it is unclear to me is how this result can be generalized for portions of the timeseries outside these $w:T$ intervals (which are those where the observations are actually missing). I am not doubting how these can be inferred using the trained read-outs. It is not clear to me how the error bounds apply to those missing portions of the timeseries.

 * The empirical analysis is limited in scope and depth of the discussion. Scope of the comparison should be enlarged to include those works approaching time-series imputation from a spatio-temporal perspective (e.g. https://www.ijcai.org/proceedings/2024/0445.pdf). The results provided are not analyzed in depth: for instance in Table 2 top, the confidence intervals seem to be very much overlapped with those of GRU-D and no discussion on the significance of these results is provided. 

 * The work does not make any attempt at using the insight provided by earlier works on deep reservoirs (i.e. Gallicchio et al, 2017) to explain the effect of multiple reservoirs on the timeseries. E.g. it is know from earlier literature that layers in a deep reservoir architecture tend to produce an incremental filtering effect in which each layer focuses on filtering out selective frequencies out of the input timeseries. The impact of such a process on the imputation application should be analysed more in depth.

### Questions
1) Can you please elaborate on the statistical significance of the performance differences in Table 2?

2) Given the strong inductive bias of reservoir computing methods (due to the restrictions imposed by the randomization of weights), it is largely surprising that the hyperparameters do not vary across datasets (aside from reservoir size, which seems to be the only one in model selection). Can the authors elaborate more on this? For instance, the leaky parameter can be expected to be different between datasets as its choice typically depend on the different “speed” of the signals involved. Similarly for the spectral radius and, to a minor extent, to the effect of sparsity.

3) Can you please clarify how the theoretical results generalize to parts of the sequences that need imputation and where this can be tracked in the demonstrations provided in the appendices?

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
4

### Summary
The authors study data-imputation problem in multivariate time series, and consider random- and block-missing structures. To approach this problem, the authors propose a ESN-based approach which refines the imputations at each iteration by projecting the representations of the observed covariates onto the imputed sequence for each layer. The representations at each layer are computed using a reservoir with decreasing number of neurons at each layer.
The authors display this approach's benefits on a synthetic dynamical system dataset, and 3 real-world datasets.

### Strengths
1. The paper is well writen and easy to follow.
2. The method appears appears to be well-motivated, the burdens of the iterative process devised by the authors are offset by the lightweight computational costs of ESNs. Overall, the method appears elegant.
3. Results are positive and underscore the benefits of the proposed architecture.

### Weaknesses
1. Comparison against vanilla ESN baselines is lacking:
   - ESNs are known to perform well on chaotic time series. Comparisons should include a vanilla ESN with basic imputation methods.
   - Additionally, it would be informative to show qualitative results for a vanilla ESN, similar to Fig. 2.
2. Insufficient comparison with related methods on more realistic datasets:
   -  Comparisong in Table 3: only cases with 10% missing values are shown; the original paper also includes 50% and 90% missingness.
3. The claim on convergence of the algorithm appears to be misleading.
   - I believe this to be a typo. For instance, you claim "The sequence of imputed time series resulting from this algorithm is guaranteed to converge to the ground truth time series...". I believe the authors mean to claim the method converges to the ground truth known target values $Y_{\omega:T}$, not $Y_{1:T}$. Claiming that the imputations can recover the unknown ground truth sequence would be puzzling.

### Questions
1. Why did you use ESNs specifically for this application over other recurrent NNs, e.g. GRUs? Was efficiency the main factor here?
2. In the "Dynamical systems-theoretic approach to time series analytics" section, why is $u_t$ defined as $u_t \in \mathbb{R}^{q \times p}$? Isn’t $u_t$ $p$-dimensional?
   - Additionally, $y_t$ is assumed to depend only on $y_{t-1}$ and $u_t$, but not $u_{t-1}$. Are there no carry-over effects? While $y_{t-1}$ indirectly depends on $u_{t-1}$, is this sufficient?
3. The method’s efficacy is challenging to understand intuitively. How does independent hidden state generation $r_t^k$ at each layer improve predictions, given it doesn’t rely on prior target predictions? It’s also puzzling that a 1-layer DL-DRCN (up to additional hyperparameters equivalent to a vanilla ESN on known target states) underperforms.

Small details:
1. The authors write: "The main complexity of our algorithm comes from the matrix inverse operation, yielding an $O(KN^2T)$ complexity with $N$ as the number of neurons in the first ESN layer and $K$ as the total number of ESN layers," but matrix inversion typically requires $O(N^3)$ operations. This is expressed correctly in Table 4 of the Appendix.
2. The distinction between $Y_{1:T}$ and $Y_{\omega:T}$ in Fig. 1 is confusing, as the caption refers to the latter while the figure uses the former notation. Could this notation be unified for clarity in the figure?


Overall I'd be open to increase my score by at least 1 point if the weaknesses and the questions are addressed.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors model a multivariate time series as a trajectory within a dynamical system and develop a deep reservoir computing architecture composed of multiple echo state network (ESN) layers with progressively smaller reservoir sizes. They introduce a layer-by-layer training method that leverages the echo state property of ESNs, which aids both in convergence and efficiency. Through experiments with synthetic and real-world datasets, they demonstrate the effectiveness of this model in accurately imputing missing or corrupted data.

### Strengths
This article is clearly presented, with adequate theoretical and experimental support, effectively demonstrating the proposed DL-DRCN method. This work plays an important role in the task of interpolation in multivariate time series.

### Weaknesses
This work primarily conducts research based on the reservoir computing, however, the introduction section lacks discussions on the latest research concerning the reservoir computing method, such as references [1] and [2].

Furthermore, the author lacks significant ablation experiments. specifically, the practical difference between traditional reservoir computing and multi-layer reservoir computing.  I even think that merely utilizing a reservoir computing, repeatedly employing Equation 3 for interpolation, could also achieve relatively good results.

### Questions
1. Section 3.1's first paragraph has some unclear statements regarding $X, Y, U, M$.

2. Proposition 3.1 does not seem to be a new theoretical result proposed by the author. If not, it needs to be cited, and including it in the main text is inappropriate.

3. Section 4.2, the first line contains a typographical error.

4. What concerns me is, what are the advantages of the multi-layer reservoir computing approach proposed by the author compared to the single-layer one? To my knowledge, the single-layer reservoir computing method can also perform well in the task of reconstructing the Rossler system, and according to Takens' Embedding Theorem, partial observations can still learn the dynamics of the system.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a framework to perform imputation of multivariate time series with Reservoir computing. In particular a stack of Reservoirs is used to learn increasingly more complex (and arguably expressive) representations of the underlying dynamical systems observed through the time series. Those representations are used to impute the missing values.

### Strengths
- The approach is rather straightforward and easy to implement.
- The authors provide a theoretical analysis of the structure of the Reservoir model necessary to achieve a desired imputation error.

### Weaknesses
1. Contribution. The idea of using Reservoir computing to perform imputation of missing data is not novel. See for example my comment about the missing references. The main contribution seems to be the theoretical derivations, but I have some issues with those (see next point).

2. To my understanding, the theoretical results rely on the assumption that the Reservoir, if sufficiently large, contains the ground truth $\bar{Y}$, i.e., the complete time series with also the true values that are missing. If that is the case, such information can be easily retrieved by a linear readout. Such a ground truth should emerge from the Reservoir dynamics, which is driven by the input U. However, I am skeptical that this would happen in practice. What, for example, if U is just a constant input? How the Reservoir dynamics could contain any possible time series $\bar{Y}$, e.g., a time series representing a non-stationary process, such as the stock prices of a given company, the number of sales of a given product, the number of cars going through a cross-road, and so on? The paper makes no assumptions about relationships between U and Y, making it difficult for me to believe that *any* U could produce *any* desired $\bar{Y}$. In addition, due to the ESP property, the Reservoir cannot learn a whole set of time series, e.g., those that are not stationary, that are very chaotic, and so on.

3. There are some strong assumptions (see more in the questions).

4. There are some imprecisions. For example, the ESP depends also on the leakage $\alpha$.

5. Some minor issues with the notation. For example, the \bar is used both in line 216 and to express the ground truth. Also, in 229 and 231 "w" is used instead of omega. In 307 should be $\mathcal{K}$ rather than $k$?

6. Some missing references. About the claim in lines 100-101, some recent papers such as [1] should be referenced and contextualized with the current paper. About time series imputation with Reservoir computing some relevant literature should be cited and compared with the current paper, see e.g., [2, 3]. Literature about the ESP in deep Reservoir computing should be cited, see e.g., [4].

### Questions
- Can you handle the univariate time series case, i.e., when there is no $\mathbf{U}$?
- There are some strong assumptions, such as not all values can be missing from every covariate of the time series at once. I believe this is somewhat a limitation because in real-world scenarios that is something that actually happens. Imagine if the variables of the time series are different measurements collected from the same sensor that goes offline and stops recording all of them. In addition, there is an assumption that missing values are not allowed at the beginning of the time series, i.e., when the Reservoir is still going through a transient phase. What can be done if that happens?

### Soundness
2

### Presentation
3

### Contribution
2

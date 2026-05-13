# Non-Exchangeable Conformal Risk Control

- Decision: Accept
- Scores: 8, 5, 5, 6

## Abstract
Split conformal prediction has recently sparked great interest due to its ability to provide formally guaranteed uncertainty sets or intervals for predictions made by black-box neural models, ensuring a predefined probability of containing the actual ground truth.
While the original formulation assumes data exchangeability, some extensions handle non-exchangeable data, which is often the case in many real-world scenarios.
In parallel, some progress has been made in conformal methods that provide statistical guarantees for a broader range of objectives, such as bounding the best $F_1$-score or minimizing the false negative rate in expectation.
In this paper, we leverage and extend these two lines of work by proposing \emph{non-exchangeable conformal risk control}, which allows controlling the expected value of any monotone loss function when the data is not exchangeable. 
Our framework is flexible, makes very few assumptions, and allows weighting the data based on its
\rebuttal{relevance for a given test example;}
a careful choice of weights may result on tighter bounds, making our framework useful in the presence of change points, time series, or other forms of distribution drift. 
Experiments with both synthetic and real world data show the usefulness of our method.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper describes how to perform conformal risk control for non-exchangeable data in the split conformal setting. It is shown that the proposed method has adaptive coverage guarantees, and performs well on a mixture of real-world and synthetic settings.

### Strengths
The paper connects two modern techniques in conformal prediction, and is thus very relevant for the community. It is well-written and easy to follow as an expert. The writing is simple, and I expect the paper will also be easy-to-follow for readers unfamiliar with conformal prediction.

### Weaknesses
The method combines previous work in a relatively straightforward way. The proof of Theorem 1 does not introduce new techniques. The experiments follow settings proposed in previous works. The paper is solving a completely new problem, and naturally, there are no baselines for it.

Thus, while the proposed method is novel and useful, the paper would be strengthened with a more in-depth theoretical/experimental study. Some suggestions are,
- Writing down full-conformal and cross-conformal versions of the proposed method
- Considering new experimental settings, such as established ML distribution shift datasets
- Discussion on how one can set the weights in practice
- An interpretation of Theorem 1 for a non-expert in conformal
- A discussion around the implication of Theorem 1 for specific types of distribution shift

For instance, for the synthetic experiment in Sec 4.1, some questions that can be considered are,
- What is the exact coverage guarantee of Theorem 1? Could you put it on the plot and compare it to the obtained coverage?
- Are there some "optimal" weights that give close-to optimal coverage?
Similar questions can be considered for the other experiments, although the true TV is not known, so the authors would have to think of other ways of analyzing the experiment.

## Small errors/questions:
- Just below eq. (5), C_\lambda' should be C_{\lambda'}
- Sec 2.3: "loss is nonincreasing": nonincreasing in which parameter and in what sense?

### Questions
Please look at questions in the "Weaknesses" section.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper expands on the non-exchangeable setting for conformal risk control by Angelopoulos et. al. (2023). Conformal risk control is a generalization of conformal prediction that expands control of coverage losses to control of any monotonic, upper-bounded, exchangeable function $L \colon \Lambda \rightarrow [0, B]$, where $\Lambda$ is the space of single-dimensional inputs to ${L}$. Most often ${L}$ is some deterministic function $\mathcal{L}$ of a parametrized, conformal set $\mathcal{C}(X; \lambda)$ and the label $Y$ that obeys $\lambda_1 \leq \lambda_2 \implies \mathcal{C}(X; \lambda_1) \subseteq \mathcal{C}(X; \lambda_2) \implies \mathcal{L}(\mathcal{C}(X; \lambda_1), Y) \geq \mathcal{L}(\mathcal{C}(X; \lambda_2), Y) $.

As the paper by Angelopoulos et. al. (2023) showed, conformal risk control is considerably more flexible than standard conformal prediction, while still retaining nearly identical guarantees. The work by Angelopoulos et. al. (2023) briefly touched on straightforward extensions to conformal risk control, including proving a bound on the degradation in guaranteed risk as a function of $\sum TV(Z_i, Z_{n+1})$, where $Z_i = (X_i, Y_i)$, similar to the work of Barber et. al. (2022). This paper further includes the use of data _weight_ functions (as in Barber et. al. (2022)), and shows that this can have good empirical impact on several experimental domains.

[1] Conformal Risk Control. Anastasios N. Angelopoulos, Stephen Bates, Adam Fisch, Lihua Lei, Tal Schuster. 2023.

[2] Conformal prediction beyond exchangeability. Rina Foygel Barber, Emmanuel J. Candes, Aaditya Ramdas, Ryan J. Tibshirani. 2022.

### Strengths
This paper is clear, and does a good job at deriving bounds for how weighted conformal risk control performs under non-exchangeability. Non-exchangeability will happen often in practice, so it is impactful to explore more robust weighting schemes and their implications. The empirical results are encouraging. It's a bit unclear as to how _useful_ the guarantees are, in the sense that they can be too loose if $\sum w_i TV(Z, Z^i)$ is very large, or more likely yet, simply unknown. When some practical knowledge about the domain is available, however, designing an appropriate weighting scheme can be effective (which is demonstrated for some of the experiments here).

### Weaknesses
While, again, the paper is nicely written, it is a somewhat incremental step from previous work in Barber et. al. and Angelopoulos et. al. It's also a bit of an over-claim to say that risk is _controlled_ in a non-exchangeable setting, rather what the paper does is develop a conservative upper bound for the risk under non-exchangeability that depends on quantiles that we cannot realistically know, i.e., $TV(Z_i, Z_{n+1})$.

I'm unclear if Theorem 1 holds for data-dependent weights? A similar requirement of independence is in Barber's results, and it would seem that it should be required here too. Particularly in the iterated expectation step here, I think this assumes $K \perp Z$. This is a major claim in the paper (e.g., "[...] allows weighting the data based on its statistical similarity with the test examples" in the abstract), and in the QA experiment, the weights are a function of the data points, $w_i = \textrm{sim}(X_i, X_{n+1})$.
- Otherwise, it's also unclear what the best strategy should be for selecting weighting functions (this seems rather adhoc in the experiments).
- Note that we can get the same bound in Lemma 1 directly from the analysis of Angelopoulos et. al. by defining $\tilde{g}(Z) = g(Z) - A$, which then has range $[0, B - A]$ for $g(Z) \in [A, B]$, and then it follows that
$| \mathbb{E}[g(Z)] - \mathbb{E}[g(Z')] | =  | \mathbb{E}[g(Z) - A] - \mathbb{E}[g(Z') - A] | = | \mathbb{E}[\tilde{g}(Z)] - \mathbb{E}[\tilde{g}(Z') ] |$,
and then we proceed directly with the proof in Angelopoulos et. al. to get
 $| \mathbb{E}[\tilde{g}(Z)] - \mathbb{E}[\tilde{g}(Z') ] | \leq (B-A) TV(Z, Z').$

### Questions
- I'm unclear if Theorem 1 holds for data-dependent weights? A similar requirement of independence is in Barber's results, and it would seem that it should be required here too. Particularly in the iterated expectation step here, I think this assumes $K \perp Z$. This is a major claim in the paper (e.g., "[...] allows weighting the data based on its statistical similarity with the test examples" in the abstract), and in the QA experiment, the weights are a function of the data points, $w_i = \textrm{sim}(X_i, X_{n+1})$. 
- Otherwise, it's also unclear what the best strategy should be for selecting weighting functions (this seems rather adhoc in the experiments).
- Note that we can get the same bound in Lemma 1 directly from the analysis of Angelopoulos et. al. by defining $\tilde{g}(Z) = g(Z) - A$, which then has range $[0, B - A]$ for $g(Z) \in [A, B]$, and then it follows that
$| \mathbb{E}[g(Z)] - \mathbb{E}[g(Z')] | =  | \mathbb{E}[g(Z) - A] - \mathbb{E}[g(Z') - A] | = | \mathbb{E}[\tilde{g}(Z)] - \mathbb{E}[\tilde{g}(Z') ] |$,
and then we proceed directly with the proof in Angelopoulos et. al. to get
 $| \mathbb{E}[\tilde{g}(Z)] - \mathbb{E}[\tilde{g}(Z') ] | \leq (B-A) TV(Z, Z').$

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper extends conformal risk control (CRC) under the exchangeable setup to the non-exchangeable setup, i.e., converting “Angelopoulos et al. (2023a)” to the “Barber et al. (2023)”-style. In particular, the coverage guarantee under non-exchangeability is stated and proven in Theorem 1 and the proof follows techniques by Barber et al. (2023) and Angelopoulos et al. (2023a). The efficacy of the proposed algorithm is empirically demonstrated by using synthetic and real data with multiple shifts.

### Strengths
Originality: This paper combines the results by Barber et al. (2023) and Angelopoulos et al. (2023a), leading to a new result. 

Quality: the claim is well-justified via Theorem 1 and its proof. 

Clairity: the paper is mostly well-written. 

Significance: considering that the conformal prediction can be extended to the non-exchangeable setup by Barber et al. (2023), so it is not surprising that conformal risk control can be extended in a similar way. But, it is still a new result.

### Weaknesses
The following includes my concerns. 

1. Under the non-exchangeable setup, the CRC should be broken, and this is why we need non-exchangeable extension of CRC. But, I cannot see the trend in Setting 3 in Figure 1 and Figure 3, which is unsatisfactory. In particular, I’m not convinced why open-domain QA experiments (related to Figure 3) fit the non-exchangeable setup – the concrete scenario on why we need to consider the non-exchangeable setup here is required. Moreover, the way to generate w_i is not correct – by Barber et al. (2023), w_is prespecified but not data-dependent (see Section 4.5. by Barber et al. (2023) for a careful discussion on the data-dependent weights). This may demonstrate that open-domain QA is not a proper target of this method. 

2. It would be more readable if the controlled loss is summarized in scalar statistics. For example, in Setting 3 in Figure 1, I cannot see why the proposed approach is good.

### Questions
1. Can you draw plots such that CRC is clearly broken under the non-exchangeable setup?
2. Can you provide the concrete scenario on why we need to consider the non-exchangeable setup in open-domain QA experiments? You also can replace the experiments. 
3. Can you justify why weights are generated in a data-dependent way in open-domain QA experiments?
4. Can you summarize / provide scalar statistics on the controlled loss such that we can see whether the proposed approach controls the risk but the baseline fails to control it?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper shows how to perform conformal risk in a non-exchangeable setting --- i.e. for any given loss l, providing a threshold such that the true loss is less than some pre-specified alpha. Unlike the typical conformal prediction setting that assumes that data satisfies the exchangeable assumption (i. e. any permutation of the data is equally likely), it tries to relax such assumption. Also, unlike the typical conformal prediction that provides a prediction set that's supposed to contain the true label, it studies a more general form usually referred to as conformal risk control.

The paper achieves the above goal by combining Barber et al. (Conformal Prediction Beyond Exchangeability) and Angelpoulos et al. (Conformal Risk Control). 

Finally, the paper tests the idea on three datasets.

### Strengths
-The idea proposed here seems to actually work in practice as shown by their experiments.

### Weaknesses
-The main contribution of the paper seems to be just a combination of two techniques, conformal prediction beyond exchangeability and conformal risk control. Once one understand the idea behind conformal prediction (i.e. finding an (1-alpha) quantile of the conformal score in the calibration data set), the idea of conformal risk control follows pretty naturally (finding some alpha-cut off for some monotonic loss in the calibration data set). And hence, techniques known for conformal prediction can be easily translated to conformal risk control — i.e. handling distribution shift. In this specific case, the paper is leveraging the technique of conformal prediction beyond exchangeability. Also, there isn’t inherent difficulty in applying the beyond the exchangeability idea to this conformal risk control setting to my knowledge. If there is additional difficulty in applying the beyond the exchangeability idea to the conformal risk control setting compared to applying the idea to the typical conformal prediction setting, it would be great if the authors can emphasize that and how this difficulty was overcome.  
-There’s no clear guideline as to how to go about setting these weights and one has to resort to heuristics. But I think this point is not necessarily specific to the approach in this paper but with the original conformal prediction beyond exchangeability of Barber et al.


### Questions
-In Equation (3) where Z_i is defined, shouldn’t Z_i be what you get by swapping the test point (X_{n+1}, y_{n+1}) with (X_i, y_i) as opposed to the nth calibration data point (X_n, y_n)? This is how things are defined in Barber et al. as well.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

# Efficient Fairness-Performance Pareto Front Computation

- Decision: Reject
- Scores: 6, 6, 8, 5, 5

## Abstract
There is a well known intrinsic trade-off between the fairness of a representation and the performance of classifiers derived from the representation. 
Due to the complexity of optimisation algorithms in most modern representation learning approaches, for a given method it may be non-trivial to decide whether the obtained fairness-performance curve of the  method is optimal, i.e., whether it is close to the true Pareto front for these quantities for the underlying data distribution. 

In this paper we propose a new method to compute the optimal Pareto front, 
which does not require the training of complex representation models. We show that optimal fair representations possess several useful structural properties, and that these properties enable a reduction of the computation of the Pareto Front to a compact discrete problem. We then also show that these compact approximating problems can be efficiently solved via off-the shelf concave-convex programming methods. 

Since our approach is independent of the specific model of representations, it may be used as the  benchmark to which representation learning algorithms may be compared. We experimentally evaluate the approach on a number of real world benchmark datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper has two main technical contributions: The first is to deeply analyze structural properties of optimal fair representations, and the other contribution is develop a method to compute the Pareto front for data distributions with any dimension. A particular advantage of this new method is its model independence: By using well-established optimization techniques, the computation of such Pareto front does not require an extensive of training of representation models; instead, much simpler data operations shall be sufficient.

### Strengths
1.This paper studies an interesting and important problem, as realizing the Pareto front is indeed important for any practical problems.

2. This paper is theoretically rigorous. The main techniques to achieve the goal, such as reduction to focus on invertible representations and solve the optimization problem (17) with restrictions listed below, are sound with formal justifications. Consequently, the method is theoretically credible.

### Weaknesses
The sensitive attributes here are assumed to be binary, but recently there have been some results for more general cases (multi-class, multi-group), and computing Pareto front for those cases are certainly more desirable, yet the setting in this paper is limited.

### Questions
I do not have any significant questions.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors work with approximately fair representation learning, where the goal is to learn a fair representation random variable Z in $R^{d’}$. They define a $\gamma$-Fair representation as one which has a small L1 distance between the random variable Z conditioned on either a = 1 or a = 0 (where a is the sensitive attribute realization). Perfectly fair ($\gamma=0$) representation implies demographic parity / equalized odds w.r.t. attribute A for any classifier built on top of Z. The goal is to find a representation Z which minimizes total error (any concave function $h$) of the label random variable $Y$ conditioned on the representation $Z$. That is, we want to be able to reconstruct the ground truth conditional label distribution $Y$ with only the ability to modify the representation $Z$, subject to the constraint that $Z$ is $\gamma$-fair.

The main issue tackled by the paper is the fact that it can be difficult to work in the representation space $R^{d’}$ if the representations are allowed to be arbitrarily complex. Therefore, the authors focus on _invertible_ representations (line 240), which are those with a small basis in the original feature space (X,A). In theorem 4.1, the authors demonstrate that at least w.r.t. the fairness constraint, it suffices to search only in the space of invertible representations, whose total error is guaranteed to be “good enough”. 

Next, in section 5, the authors show how to use the invertibility theorem 4.1 in order to efficiently optimize over the representation space. Finally, in Section 6, the authors experiment with the proposed method, MIFPO, and compare against an existing fair representation learning algorithm FNF. They demonstrate that by estimating the base conditional probabilities with calibrated classifiers, MIFPO allows for construction of fair classifiers which tradeoff fairness and accuracy to a specified degree better than prior methods.

### Strengths
I really enjoyed the fact that we can restrict to looking at a small, finite number of “parents” of points in the representation space, and this totally describes the set of pareto efficient transformations (I have a soft spot for such factorizations). The experiments also seem reasonable, and tie in with the theory directly. The fact that the proposed method MIFPO utilizes existing solvers is also a strength, given the power of these existing solvers in practice. Overall, the paper seems to propose a clear improvement over the compared method from previous work (FNF).

### Weaknesses
I have not worked in and am not familiar with the area of fair representation learning, and did not check any proofs of the paper. I think a major weakness of the paper --- as someone in algorithmic fairness with some background in theory --- is that it can be difficult to read. In particular, the main body is quite notation heavy, especially as you push into section 5. For example, some of the triple indexing in equation (17) seems a bit unnecessary, given that only two orders ever appear — $r_{u,v,j}$ or $r_{v, u, j}$ — and these two are very difficult to tell apart. Perhaps having a notation guide somewhere (maybe in the appendix) can be useful, since I found myself going back and forth needing to look up the definition of each variable.

I also think that there is some room for improvement in terms of detailing what the sources of randomness are (e.g. via the parameterization $\theta$), or better describing some of the notation (see minor comments for detailed examples). This could be a consequence of my background and being unfamiliar with working with labels and representations as random variables directly.

I am open to raising my score if the readability can be improved for the general theory / fairness audience. Perhaps this will require making parts of the discussion in the main body less formal in order to better give some intuition. It may also require having more statements / sections which describe the contributions and importance of different theorems and parts at a high level (especially for Section 5.2). This can be difficult, given that you would of course like to formally spell out the concave program that you are solving in the main body. I am open to suggestions on how the readability of 5.2 can be improved.

As far as I can tell, all non-pareto efficiency in the experiments come from the following factors: 1) Not enough samples 2) suboptimality of the DCCP solvers 3) Not enough expressibility of the chosen (proxy) representation space via choice of $k$ value. I believe that these should be discussed in a self-contained section within the experiments section. In addition, could there be more sources of errors which combine to make the curves not only have “pareto optimal” points in Figure 3?

Other minor comments:

1. Some inconsistent usage of \citet vs. \citep (for example in the first paragraph of the paper). Please see the reference: https://towson.libguides.com/mlastyle/in-text
2. Figure 1 seems to be slightly vertically squashed, which makes it a bit harder to read the equations. I would also recommend using a vector graphic (pdf) figure instead of a png / jpg, as the latter does not allow for highlighting / reduces accessibility. A pdf may also scale up / down better in terms of figure quality.
3. What is figure 1 depicting? Can you provide an explanation in the caption?
4. What is the randomness over in $P(Z|X = x, A=a)$ in line 78? Is there assumed to be an underlying distribution $D$ on $X \times Y$? Note: I believe the randomness is over theta, the parameters of the representation, but it may be helpful clarify this earlier if using the notation $P(Z|X = x, A=a)$ in the introduction.
5. Is $P(Y|X=x)$ the ground truth conditional label distribution (line 174)? If so, is $P(Y|Z=z)$ the same ground truth conditional label distribution in the representation space Z? I guess I am just a bit confused. I thought we defined Y as a random variable of X,A, how can we condition Y on a representation z?
6. To make sure I understand footnote 1, if we consider $\beta_a(s)$ in line 228, this should formally be written as $P(X=s|A=a) = P(X = (x, a) | A = a)$, where in the latter, the two realizations of $a$ are identical?
7. Invertible representation seems to be a key concept, maybe it should be a formal definition in line 240?
8. The choice of $k$ seems quite important for MIFPO. Do you have any ablations of the method performance across $k$ size? I’m assuming the computational complexity scales in $k$?
9. How does the work relate to Impossibility results for fair representations (Tosca Lechner, Shai Ben-David, Sushant Agarwal, Nivasini Anathakrishnan)? Is it that they require perfect statistical parity (i.e., TV distance 0)?
10. Missing citations for “Health”, “Crime”, and “Law” datasets. What are these datasets?
11. Missing citations for Adult, LSAC, and COMPAS datasets.
12. More generally, more details are needed for the experiments, how many train points for the calibrated classifiers? Do you hold out some fixed percent for post-processing?
13. “Pareto front is flat for Law dataset” (468-473), but the MIFPO curve doesn’t seem very flat in Figure 3a? In fact, the vertical variability looks similar to the health dataset.
14. Non-monotonicity of pareto curve in Figure 3a: is this only due to sample size issues?
15. Figure 4: inconsistent legends between plots. Could probably remove the legends from COMPAS and ADULT plots, or ensure that all legends are identical. Pareto Front should also maybe be labeled as “Pareto Front as Found by MIFPO (Ours)”, or something similar for clarity.
16. As a reader, I gained very little (if anything) from Figure 1 and 2. Ideally, they should be self-contained, or at least have an explanation somewhere in the text. Neither figure is explained in the main text or the caption.
17. In the appendix align environments, consider using \nonumber in order to hide the equation numbers of unreferenced lines. For example, equation 118 is — to my knowledge — not referenced anywhere.
18. The full concave program should be stated somewhere, instead of for example in Def. 5.1 saying that we minimize equation (17) subject to constraints (15-16) and (20-22) which are spread throughout the paper.

### Questions
As far as I can tell, all non-pareto efficiency in the experiments come from the following factors: 1) Not enough samples 2) suboptimality of the DCCP solvers 3) Not enough expressibility of the chosen (proxy) representation space via choice of $k$ value. I believe that these should be discussed in a self-contained section within the experiments section. In addition, could there be more sources of errors which combine to make the curves not only have “pareto optimal” points in Figure 3?

Other minor comments:

1. Some inconsistent usage of \citet vs. \citep (for example in the first paragraph of the paper). Please see the reference: https://towson.libguides.com/mlastyle/in-text
2. Figure 1 seems to be slightly vertically squashed, which makes it a bit harder to read the equations. I would also recommend using a vector graphic (pdf) figure instead of a png / jpg, as the latter does not allow for highlighting / reduces accessibility. A pdf may also scale up / down better in terms of figure quality.
3. What is figure 1 depicting? Can you provide an explanation in the caption?
4. What is the randomness over in $P(Z|X = x, A=a)$ in line 78? Is there assumed to be an underlying distribution $D$ on $X \times Y$? Note: I believe the randomness is over theta, the parameters of the representation, but it may be helpful clarify this earlier if using the notation $P(Z|X = x, A=a)$ in the introduction.
5. Is $P(Y|X=x)$ the ground truth conditional label distribution (line 174)? If so, is $P(Y|Z=z)$ the same ground truth conditional label distribution in the representation space Z? I guess I am just a bit confused. I thought we defined Y as a random variable of X,A, how can we condition Y on a representation z?
6. To make sure I understand footnote 1, if we consider $\beta_a(s)$ in line 228, this should formally be written as $P(X=s|A=a) = P(X = (x, a) | A = a)$, where in the latter, the two realizations of $a$ are identical?
7. Invertible representation seems to be a key concept, maybe it should be a formal definition in line 240?
8. The choice of $k$ seems quite important for MIFPO. Do you have any ablations of the method performance across $k$ size? I’m assuming the computational complexity scales in $k$?
9. How does the work relate to Impossibility results for fair representations (Tosca Lechner, Shai Ben-David, Sushant Agarwal, Nivasini Anathakrishnan)? Is it that they require perfect statistical parity (i.e., TV distance 0)?
10. Missing citations for “Health”, “Crime”, and “Law” datasets. What are these datasets?
11. Missing citations for Adult, LSAC, and COMPAS datasets.
12. More generally, more details are needed for the experiments, how many train points for the calibrated classifiers? Do you hold out some fixed percent for post-processing? 
13. “Pareto front is flat for Law dataset” (468-473), but the MIFPO curve doesn’t seem very flat in Figure 3a? In fact, the vertical variability looks similar to the health dataset. 
14. Non-monotonicity of pareto curve in Figure 3a: is this only due to sample size issues?
15. Figure 4: inconsistent legends between plots. Could probably remove the legends from COMPAS and ADULT plots, or ensure that all legends are identical. Pareto Front should also maybe be labeled as “Pareto Front as Found by MIFPO (Ours)”, or something similar for clarity.
16. As a reader, I gained very little (if anything) from Figure 1 and 2. Ideally, they should be self-contained, or at least have an explanation somewhere in the text. Neither figure is explained in the main text or the caption.
17. In the appendix align environments, consider using \nonumber in order to hide the equation numbers of unreferenced lines. For example, equation 118 is — to my knowledge — not referenced anywhere.
18. The full concave program should be stated somewhere, instead of for example in Def. 5.1 saying that we minimize equation (17) subject to constraints (15-16) and (20-22) which are spread throughout the paper.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a method for calculating the Fairness-Accuracy Pareto front for all fair representations for a particular fairness-constrained learning task without needing to explicitly train representation models. As such, this front describes a space of possible trade-offs for fair representations in terms of their fairness vs. accuracy, which might have downstream applications in benchmarking particular trained fair representations and check if their performance still has room for improvement. The authors accomplish this through transforming the fair representation learning problem to a much lower-dimensional problem through observing a mapping from the input space to the simplex of the output space, $\Delta_{\mathcal{Y}}$. In binary classification, this is particularly appealing because $\Delta_{\mathcal{Y}} = [0, 1]$, which is nicely discretizable and much "more compact" than the arbitrary space of inputs. This results in a concave *minimization* program that, although unsolvable through nice black-box methods for convex optimization (it is concave *minimization* not *maximization*), still has easily estimable quantities from data and is experimentally feasible through certain DCCP frameworks. The authors show this in their suite of experiments over various standard fairness datasets.

### Strengths
Overall, I found the main idea of this paper and the technical contribution very nice, and the authors mostly present their results in a well-organized way. I am not an expert in the fair representations literature, so I am not sure how these methods are positioned with respect to other fairness-ensuring methods (i.e. inprocessing methods, postprocessing methods), so I am unclear whether the paper as a whole is well-motivated (it very well may be, I could just be ignorant of how widely adopted fair representation learning is). But, if we take it as given that it is desirable to construct new ways to benchmark fair representations without needing to train them explicitly with complicated nonconvex NNs and such, then this paper presents a worthwhile and interesting contribution.

**Originality.** As far as my knowledge goes, this paper is an original contribution to the fair representation learning literature. It is particularly novel because it presents a way to compute a Pareto frontier for fairness-accuracy tradeoffs without explicitly training a representation itself. The authors come to this computation through analyzing the theoretical properties of a fair representation by first positing an intuitive optimization problem and then breaking down its constituent parts into quantities that are easily estimable from the data. The key step in doing so is interesting and, in my opinion, novel --- the authors reduce the search space of the problem from the input space (which can be any arbitrary subset of $\mathbb{R}^d$) to $\Delta_{\mathcal{Y}}$ through basic properties of representations.

**Quality.** The result itself is interesting and significant, and I particularly believe that the general technique of reducing the search space to $\Delta_{\mathcal{Y}}$ to make the computation feasible is interesting. The experiments seem to be comprehensive, and Algorithm 1, the implementation to solve MIFPO, relies on simple primitives that are easily estimable from the dataset. The derivation in Sections 3, 4, and 5 are sound as far as my reading of the results go, though I did not carefully step through the proofs of the main theorems and lemmas.

**Clarity.** The writing itself is mostly clear, although there are some notation changes I would suggest to make the exposition clearer (see "Weaknesses"). The main suggestion would be to stick with probability notation (e.g. $\mathrm{Pr}(Z = z \mid A = a)$, etc.) throughout the paper or to stick with the defined notation (with $\alpha, \beta, \rho, \mu$, etc.) throughout the paper. Switching between the two obscures some of the results and made reading the results slightly more difficult. Besides that, the paper itself is well-structured and, overall, gives a clear exposition of the main technique. Besides these notational difficulties, I had little trouble following along.

**Significance.** Because I am not an expert or well-versed in the specific fair representation subfield of the fairness literature, I cannot speak to the motivation of this particular method and whether it is a big gap in the literature. However, if it *is* desirable to have methods for computing such Pareto frontiers without explicit training of representations in order to benchmark fair representations well, I believe this is a significant contribution.

### Weaknesses
There are a a couple of weaknesses I found in the paper, but none are significant enough to warrant rejecting the paper, in my view. Most of the weaknesses relate to the clarity of the paper, but the main technical weakness, in my eyes, is that the resulting optimization problem, though simpler, still relies on nonprovable guarantees --- it is a concave minimization problem, so we have no guarantees of global optima.

- **Concave minimization.** The authors themselves acknowledge in the conclusion that this is a weakness of their work, but it would be nice to see some more exposition justifying that computing this optimization problem, though it does not provably converge to global optima, is still a good thing to do in the context of constructing this Pareto front (more in "Questions"). The fact that the optimization is concave minimization, not maximization, is a significant concern because it means that standard convex optimization techniques cannot be applied to guarantee convergence to a global optimum. While DCCP may find a local optimum, there's no guarantee that this local optimum is close to the global optimum, and the quality of the resulting Pareto front is therefore questionable. The authors should provide a more thorough justification for using DCCP in this context, given the lack of convergence guarantees.
- **Figures are slightly confusing.** I found the figures to be slightly confusing, as the notation in the figures doesn't quite match up with the notation in the paper, and the figures themselves are blurry and don't quite give a clear picture to what's going on, in my opinion. I would suggest going a bit lighter on the notation in the figures to make them a bit more comprehensible; for example, I don't think that Figure 2(b) needs the $\overline{T}$ full definition in it, and I don't think that Figure 2(a) needs a presentation of the probability distribution on $v, u, u'$ in the form of the squiggly red line and the accompanying $\beta$ labels. Cleaning up the figures to be more presentable would help in the clarity of presentation. Specifically, the use of both mathematical notation and graphical representations in the same figure makes it difficult to parse the information. The figures should be simplified to focus on the key concepts and avoid unnecessary clutter.
- **Notational issues.** My main issue with the clarity of the paper is that there is much switching back and forth between established notation and introducing of new notation. I think the paper would be clearer if the authors either stuck to just using the probability notation through, so it is clear what probabilities factorize into what (i.e. sticking to just presenting $T_a(z, s)$ instead as just $P(Z = z \mid X = s, A = a)$), or at least introducing notation that is a bit more evocative of what each quantity is. I would suggest perhaps using notation that invokes the relationship between $A, Z, X,$ and $Y$ in the symbols themselves. I found that Sections 4 and 5 were a bit heavy on introducing new notation and then not using it everywhere, such as in the definition of the $r$ variable in Section 5.2. I was still able to track the main arguments, but I believe that clarifying the notation a bit would assist in the overall clarity. The inconsistent use of notation, especially the switching between probability notation and the introduced symbols, makes it difficult to follow the mathematical arguments. A more consistent and intuitive notation throughout the paper would greatly improve its readability.
- **A couple of typographical issues/nitpicks.** These don't have an impact on my overall impression of the paper, but I just wanted to point out some small nitpicks I noticed to assist the authors in revising:
- "MIFPO" is never defined as an acronym. I assume that the acronym should stand for "Model Independent Pareto Front Optimization," but I guess it would be MIPFO then?
- In Equation 5, as a minor clarity fix, I would treat make the dependence of $Z$ on $\theta$ explicit and then just mention that, for the rest of the paper, we can assume that it is implicit in the distribution governing $Z$. 
- In Section 5.2, in the first paragraph, I would suggest writing the Lemma D.1 more formally in the main body, or, at least, explaining the $k$ point approximation a bit more. I found it a bit confusing until I checked the Appendix section.

### Questions
My main questions concern how the authors view the nonconvexity of the entire optimization problem as a major or minor issue. They point out in the Conclusion section that their optimization problem, as it is concave *minimization*, does not provably converge to global optima, but I wasn't sure after reading the paper why solving the MIFPO program with DCCP is satisfactory. We see that the fairness-performance curve in Section 6 leaves some points that FNF doesn't quite reach, but is there anything we can formally say about how close to true optimal this fairness-performance curve is? I think that would rely on formal guarantees for DCCP, but I am unfamiliar with such guarantees.

Related to this question: how do we evaluate how good this "local" optimal Pareto frontier is? And what modifications to the MIFPO program seem promising to make it provably convex? My intuition suggests that the problem lies in the choice of $h$, but, in that case, it seems there's not much one can do.

### Soundness
3

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
3

### Summary
This paper addresses the problem of understanding the critical tradeoff between fairness and accuracy. They propose strategies to obtain the Pareto frontier without performing any additional model training but instead by formulating an optimization problem. 
They consider the TV as their measure of fairness, and then go on to show how for every representation, one can find an invertible representation of the same data that satisfies at least as good a fairness constraint, and has at least as good performance as the original (shown in Theorem 4.1). Next, using this result they construct a model independent optimization problem -- that they call MIFPO -- which can approximate the Pareto Front of arbitrary high dimensional data distributions, but is much simpler to solve than direct representation learning for such distribution. They specifically use off-the-shelf concave-convex programming methods to obtain the Pareto frontier. Experiments have been performed on a few benchmark datasets such as LSAC, COMPAS, and ADULT.

### Strengths
-- Interesting optimization-based strategy to obtain Pareto frontiers of the fairness-performance tradeoff 
-- Bypasses expensive model training
-- Strength lies in being able to restrict the problem space to invertible transformations, and then use off-the-shelf concave-convex optimization strategies

### Weaknesses
 --The presentation of the paper can be significantly improved. It is difficult to understand or properly check everything. For every subsection, it would be good to start with the main theorem/lemma/assertion being made in that subsection, then provide its significance towards arriving at your main result, and then provide the proof sketch/intuition behind it. 
Specific Example: The Invertibility Theorem, The Factorisation, The MIFPO  -- all these sections start with "This section provides ...." which is sometimes already understood from the title but what is important is to mention what role this particular aspect plays in the final optimization before getting into the details.  

-- In the introduction, it would be nice to summarize the main contributions as a list.
Specific Example: It would be great to have a flow-chart summarizing what are the various Theorems/Assertions made and specifically what role they play/why they are needed for the final optimization.

-- There are related works in accuracy-fairness literature which have proposed model-agnostic optimization formulations to characterize the trade-off. These two prior works share close similarities with the formulation in this paper and should be discussed.
Briefly explaining the key similarities and differences: Interestingly, while these prior works finally arrived at a convex optimization problem, but this paper arrives at a concave minimization problem with convex constraints which presents an intriguing nuance.
[1] Kim, Joon Sik, Jiahao Chen, and Ameet Talwalkar. "FACT: A diagnostic for group fairness trade-offs." International Conference on Machine Learning (ICML) 2020.
[2] Hamman, Faisal, and Sanghamitra Dutta. "Demystifying Local & Global Fairness Trade-offs in Federated Learning Using Partial Information Decomposition." International Conference on Learning Representations (ICLR) 2024.

-- There are several other related works on accuracy-fairness tradeoffs which have been missed. See the references and follow-up works from these two papers above to find more references.

### Questions
-- Could you discuss the implications of using different accuracy measures on your optimization formulation? Entropy accuracy seems to be challenging and also more involved than regular accuracy of prediction=true label.
-- Would the Pareto frontier optimization problem be simpler if other accuracy measures were used?
-- Could you simplify the flow chart of the mathematical arguments leading onto your main optimization (which btw has not been written together  with all the constraints)? For instance, what role does the factorisation, invertibility, etc. individually play to simplify and get to your final version?
-- What is the role of post-processing strategies?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a model-independent method called MIFPO for computing the Pareto front of performance versus fairness in machine learning classification models. MIFPO achieves this by discretizing the space of possible distributions of the target variable and formulating a concave minimization problem with linear constraints. This problem can be efficiently solved using off-the-shelf solvers, such as the disciplined convex-concave programming (DCCP) framework. Experimental evaluations demonstrate MIFPO’s advantages over existing methods in both fair representation learning and fair classification.

### Strengths
1. **Use of Structural Properties**: The approach leverages the structural properties of optimal fair representations to efficiently approximate the Pareto front. By exploring previously underutilized properties, the authors have created a way to directly compute the fairness-performance front without a specific model structure.

2. **Model-Independent**: MIFPO’s model-agnostic nature allows it to serve as a comparative benchmark against complex fair representation models and classifiers, contributing to broader applications in fair ML model assessment.

### Weaknesses
1. **Generalizability Issue:** The MIFPO method relies on discretizing the target space, which limits its application to finite or low-dimensional scenarios. This assumption restricts the method's generalizability to cases where target variables are continuous or involve multi-dimensional labels. A preliminary exploration of alternative methods that could apply to these contexts, or potential theoretical adjustments, would strengthen the paper and broaden its impact.

2. **Insufficient Coverage and Comparison with Related Works:** A major concern is the limited discussion of related works, which affects the paper’s positioning and diminishes the impact of MIFPO’s contributions in the context of established fairness-performance trade-offs. This trade-off problem is well-explored in fairness in machine learning, with numerous studies proposing methods to balance these objectives. However, these methods are not cited or analyzed here. Beyond just discussion, comparing MIFPO’s empirical results against these established approaches is essential to validate its contribution, demonstrating where MIFPO achieves improvements or differs significantly in performance. While the following papers represent a sample, many other relevant studies would also merit discussion and empirical comparison:

- [1] Wang, Hao, et al. "Aleatoric and epistemic discrimination: Fundamental limits of fairness interventions." Advances in Neural Information Processing Systems 36, 2023.

- [2] Dehdashtian, Sepehr, et al. "Utility-Fairness Trade-Offs and How to Find Them." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2024.

- [3] Sadeghi, Bashir, et al. "On characterizing the trade-off in invariant representation learning." Transactions on Machine Learning Research, 2022.

- [4] Menon, Aditya Krishna, and Robert C. Williamson. "The cost of fairness in binary classification." Conference on Fairness, Accountability and Transparency, PMLR, 2018.

- [5] Zhao, Han, et al. "Inherent tradeoffs in learning fair representations." Journal of Machine Learning Research, 2022.

3. **Computational Complexity and Practicality:** The MIFPO implementation relies on DCCP which can be computationally intensive, especially for large datasets. The lack of guarantees for global minima in DCCP further raises questions about MIFPO’s ability to reliably converge to optimal solutions on larger, more complex datasets. Addressing scalability concerns would improve MIFPO's applicability to real-world scenarios. Exploring alternative solvers or optimization frameworks with scalability features, or clarifying computational requirements and limitations for different dataset sizes, would make the method more accessible to practitioners.

4. **Consideration of Alternative Fairness Definitions:** The paper exclusively uses statistical parity as the fairness metric; however, multiple definitions of group fairness exist, and studies [2, 6] have shown that statistical parity may not be ideal in practice since it does not consider target attributes. Alternative metrics such as Equality of Odds and Equal Opportunity are often more practical and widely used. The paper would be significantly strengthened if the authors discussed how MIFPO could be adapted to incorporate these alternative fairness definitions, as doing so could broaden its applicability and relevance in real-world settings.

- [6] Hardt, Moritz, et al. "Equality of opportunity in supervised learning." Advances in neural information processing systems 29, 2016.

### Questions
All the questions and suggestions are mentioned in the Weaknesses section.

### Soundness
3

### Presentation
2

### Contribution
2

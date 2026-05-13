# Adaptive backtracking for fast optimization

- Decision: Accept
- Scores: 5, 6, 8, 6

## Abstract
Backtracking line search is foundational in numerical optimization. 
The basic idea is to adjust the step size of an algorithm by a {\em constant} factor until some chosen criterion (e.g. Armijo, Goldstein, Descent Lemma) is satisfied. 
We propose a new way for adjusting step sizes, replacing the constant factor used in regular backtracking with one that takes into account the degree to which the chosen criterion is violated, without additional computational burden. 
We perform a variety of experiments on over fifteen real world datasets, which confirm that adaptive backtracking often leads to significantly faster optimization.
For convex problems, we prove adaptive backtracking requires fewer adjustments to produce a feasible step size than regular backtracking does for two popular line search criteria: the Armijo condition and the descent lemma.
For nonconvex smooth problems, we prove adaptive backtracking enjoys the same guarantees of regular backtracking.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies the backtracking line search commonly used for step size selection in optimization algorithms. The main focus is to propose an adaptive approach for setting the decay parameter when searching for the step size. The authors consider several examples (e.g., Armijo, descent lemma) to illustrate the concept, which is straightforward and presented in Algorithm 2. They also conduct extensive numerical simulations to demonstrate the effectiveness of the adaptive approach.

### Strengths
Backtracking line search is a fundamental task in general optimization algorithms. The numerical simulations show promising potential for the adaptive method.

### Weaknesses
As my work primarily focuses on the theoretical aspects of optimization, my comments and concerns mainly relate to the theoretical analysis of the proposed adaptive approach. Broadly speaking, the theorems presented in Section 4 provide limited insight into the advantages of the new approach compared to the conventional backtracking line search in Algorithm 1. I will elaborate on this and discuss other concerns below.

* My main technical concern is with the lower bound of the adaptive factor, which will affect the overall complexity of the algorithm, not just the number of function evaluations in a single iteration step. As mentioned by the authors in Line 395, the search procedure should ensure a sufficiently large step size to achieve fast convergence. Following this, the authors argue that their construction guarantees that the adaptive factor is bounded away from zero. However, this is not sufficient to ensure convergence of the (outer-loop) algorithm iteration sequence, as the step size can be arbitrarily small compared to the step size selected by "regular" line search (for example, in the descent lemma setting, the regular search will produce a step size lower bounded multiplicatively by the factor $\rho$). Indeed, using some standard theorems for smooth optimization, the adaptive factor appears in the final complexity guarantee and may not be easily controlled. Therefore, an important task here is to investigate the overall evaluation complexity when the proposed adaptive line search is used. Specifically, the analysis should consider how the adaptive factor impacts the convergence rate, not just the per-iteration cost. The concern is that while the adaptive factor might reduce function evaluations per step, it could also lead to smaller step sizes that require more iterations to converge, potentially negating any benefits.

* As for the theorems presented in Section 4, specifically Propositions 1, 2, and the two informal theorems, it seems that these results do not demonstrate the advantage of using an adaptive approach compared to the regular search method. These results essentially state that, under certain assumptions, the adaptive approach is not worse than the regular method in terms of the number of function evaluations in a single step. Also, as mentioned above, it is unclear how this affects the total number of iterations in the outer loop. The analysis focuses solely on the number of function evaluations within a single line search iteration, without addressing the global convergence properties of the optimization algorithm that uses this adaptive line search. The theorems should ideally demonstrate a clear advantage in terms of overall convergence rate or iteration complexity, not just a per-step function evaluation count.

* The first question that likely arises after seeing Algorithm 2 is how to design the adaptive factor $\hat{\rho}$. The authors demonstrate some possible constructions in Section 2, but these are mostly reformulations of known methods. Thus, is there a principled way to construct this adaptive factor, even for specific settings? The paper lacks a clear methodology for selecting or tuning the adaptive factor. While examples are provided, there isn't a systematic approach or theoretical guidance on how to choose the best adaptive factor for a given problem or class of problems. This makes it difficult to apply the method in practice without extensive trial and error.

### Questions
See above.

### Soundness
2

### Presentation
2

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
This paper proposes an "adaptive" version of backtracking line search (BLS) for descent steps in optimization. Namely, while in classical BLS the candidate step-size shrinks by a fixed factor of $\rho$, this paper proposes an adaptive choice of $\rho$ at each iteration which depends on how much the line-search condition is violated. The paper demonstrates in a series of experiments that this adaptive version of BLS seems to be more robust to starting point and usually leads to significant savings in compute-time if compared to classical BLS with a fixed rate. Moreover, they show theoretical results demonstrating that, in convex and/or Lipschitz smooth problems, Adaptive BLS is *effectively* no worse than BLS and the worst-case step-size guarantee are similar.

### Strengths
- Usually papers on backtracking line-search tend to focus on effects of non-monotonic searches or on changing the condition of the line-search. This paper proposes a seemingly simple modification to the choice of the backtracking factor that preserves most of the theoretical guarantees. This seems like one of those simple observations that is of interest to the optimization community in general. In fact, I think the contribution is good exactly because of the simplicity: there seems to be a easy modification to BLS that most likely improves it;
- The presentation is relatively clear and easy to understand;
- The variety of experiments gives confidence about the empirical performance of the method if compared to BLS with a fixed parameter;

### Weaknesses
I believe the main area of improvement of this paper is its discussion previous work, which is even more important in a paper about such a classical topic.  I will detail two aspects of the paper that I believe could be improved.

- **Discussion of related research work**: Backtracking line-search is a classical topic with a vast amount of work on it (even if most of it is not necessarily on the backtracking factor). Yet, besides references to classical books and the original works on BLS, there is almost no discussion of previous work. Although I am not familiar with the most recent work on line-search, while reviewing this paper I found at least two papers [1,2] that should at least have been cited, and probably this line of research discussed in more depth. 

- **Lack of comparison with line-search variants**: The paper focuses on backtracking line-search with a fixed backtracking parameter $\rho$ as the main method they are comparing against. However, there are classical variants of this idea that are more often used in practice, and the main one that comes to mind is polynomial interpolation, and there are likely other heuristics the authors could have at least discussed.  Moreover, a quote from the classical textbook [3, Sec. 3.1] mentions that BLS with a varying backtracking parameter is more often used in practice:

> In practice, the contraction factor $\rho$ is often allowed to vary at each iteration of the line search. For example, it can be chosen by safeguarded interpolation, as we describe later. We need ensure only that at each iteration we have $\rho\in [\rho_{\mathrm{lo}},\rho_{\mathrm{hi}}]$, for some fixed constants $0 < \rho_{\mathrm{lo}} < \rho_{\mathrm{hi}} < 1$.

---

### Questions
- Do you think it would be interesting to compare adaptive BLS with LS with polynomial interpolation (mainly quadratic or cubic)? It seems to me it would be a more interesting comparison than simply comparing with fixed-parameter BLS, but the authors could disagree with me. Also, I believe there is likely other methods or heuristics used in the literature that should be at least acknowledge an briefly discussed in the paper;

- Are there other relevant research work on BLS that the authors are aware? The two papers I referenced I found on a brief web search, thus I only found somewhat recent work that hasn't been necessarily published yet (although one of them appeared in 2019 as a workshop paper), and I am quite certain that the authors are more better acquainted with the literature in the area than myself;

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
5

### Summary
This paper describes a backtracking strategy suitable to both convex/non-convex and smooth/non-smooth optimisation which relies on the definition of a violation factor adjusting the decrease of the step-size along the iteration. Such factor quantifies the amount at which standard backtracking conditions (e.g., Armijo) are *not* satisfied and is thus cleverly used to choose an optimal decreasing factor. In comparison to, e.g., standard Armijo condition, this avoids unnecessary overdecrease of the step (in case of small factors) and high computational costs (in case of big ones, which makes the decrease slower).
The paper is a pleasure to read: the motivation is clearly given, some examples are used to motivate the strategy used and, before providing the main theoretical results, some triggering empirical evidence is provided. The main sets of experiments reported in the body of the paper are convincing and show improvements with standard backtracking line search w.r.t. to a suitable gain measure related mostly to computational evaluation. Experiments are performed in both convex and non-convex settings as well as in a convex non-smooth scenario where comparisons with FISTA are made.
The presentation of the theoretical results is complete and the appendices are very well written and substantiated. 
I congratulate with the authors for such a nice piece of work which, in my opinion, opens the path to many questions and future research directions additionally to the ones highlighted in the final section of this work.

### Strengths
The paper is very nicely written, the intuitition behind the proposed adaptive strategy is well described and the numerical tests are convincing. I liked the choice of the authors of presenting first the numerical results raather than the theoretical ones, since the reader is really triggered to keep reading and understanding more. The exhaustive list of experiments reported in the appendix is very convincing and shows that the proposed strategy performs indeed very well, as supported by the thoeretical results which I have checked and, up to some minor typos, appear correct to me.

### Weaknesses
The only "weaknesses" I could highlight relate to some (minor) lack of referencing to existing work and/or to some refinement that could be made to guarantee that the proposed strategy maintains (as it seems) the convergence speed of stnadard algorithm also in more 'regular' scenario (e.g., strong convexity). Some minor imprecisions can be easily fixed as I will suggest below. 
Specifically, the discussion on the potential for local step-size increase could be expanded. While the monotone nature of the backtracking strategy is acknowledged, it's worth exploring whether allowing for a temporary increase in step-size could further enhance efficiency, particularly when the initial estimation of \alpha_0 is significantly underestimated. Additionally, the theoretical results focus on quantifying backtracking iterations, but a more in-depth analysis of how the proposed method guarantees usual convergence rates when employed as an 'inner loop' would strengthen the paper. The consideration of strongly convex optimization schemes also warrants further clarification. The rationale behind choosing specific schemes (e.g., Algorithm 4) and the potential adaptation of the proposed method to scenarios where the strong convexity parameter is unknown could be elaborated upon. Finally, the observation regarding the convergence curves in Figure 1 and t2 with different \beta values warrants further investigation. A comparison of the step-size evolution along iterations would provide valuable insights into the behavior of the proposed method compared to standard BLS.

### Questions
- I think that some further referencing should be added. In these works (DOI1: 10.1137/17M1149390, DOI2: 10.1137/21M1391699) adaptive backtracking strategies that could be generally employed for smooth/non-smooth and convex/strongly-convex optimisation schemes are considered. The main idea there is the possibility of the step-size to increase locally as long as the desired backtrcking conditions (there defined in terms of a Bregman distance of the smooth component) are used. Despite the adaptivity of the approach you propose, your backtracking strategy is still monotone (at least in the, indeed, monotone case). Is this really needed? Couldn't you allow also the local increase of the step-size, check if the condition is violated and, if not, allow it and, if yes, perform your strategy with suitable adjustments? I think that a comparison with these approaches should be added and such extension possibly considered.
The use of non-monotone approaches as the one mentioned above is interesting, for instance, where you have, for some reason, a very bad estimation of \alpha_0  (e.g., very small) which as far as I undertsand, not even with your approach you would be able to inrease along iterations.
- Another approach that is worth mentioning is the one studied here (Malitsky, Mishchenko Adaptive Gradient Descent without Descent
 PMLR 119:6702-6712, 2020) which is computationally very effective and relies on different backtracking rules adaptive to local geometry.
- Your theoretical results aim at quantifying, essentially, the amount of backtracking iterations in comparison with the standard approaches, but can you indeed guarantee that usual convergence rates are obtained whenever the strategy is employed as an 'inner loop' of any underlying algorithm?
- In some sections I found a bit of overlooking on the regularity properties of the problems considered and/or of the schemes employed. This in particular when you considered strongly convex optimistation schemes. In the non-smooth examples you considered AGD schemes adapted to strong convexity (e.g., relying on the knowledge/estimation of strong-convexity parameters) as in the case of Algorithm 4 (where I whink that m is indeed the strong convexity parameter although never mentioned) or not (FISTA). For strongly convex algorithms linear convergence is normally achieved, contrarily to convex ones where only O(1/k^2) speed is obtained. Some more precision on the reasons why you consider one or the other and on how potentially your idea adapts to situations where the strongly convex parameter is unknown (and estimated via restarting strategies, see, e.g., DOI3: 10.1137/23M158961X) should be added. This is interesting, for instance, when one wants to control oscillations due to inertia in accelerated schemes. Interestingly, you don't seem to have that many oscillations. Do you have any guess on why this happens? It is surely related to the adaptation to the local geometry of the function.
- It's a bit surprising that for standard BLS, in the results in Figure 1 and t2, with the same \rho, the convergence curve obtained with a higher value of \beta (higher initial step-size), pink curves, lies *above* and not below the one with smaller step size. Is this due to the 'bad' adjustment of the step-size in the standard backtracking inner routine?
I think it would be very interesting comparing the evolution of the step-size estimation along the iterations, in comparison with the (over)estimation of 2/L (convex) or 1/L (non-convex) used as a fixed reference.




Minor points:
- I would change notation in (5) on page 3, lines 151 and subsequent since, as you said, (5) has to hold for F (capital) while it looks it has to hold only for the smooth part. 
- Page 4, line (191) is somehow bizarre (the regularisation parameter can be anyhing), is there any reason why you relate this to \bar{L}?
- What is the stopping criterion for achieveing "designated precision" used in the experiments in section 3?
- What is the interest of using accelerated schemes in the non-convex objective example? It's not clear that they improve at all the speed of convergence right?
- In Figure 3 and the corresponding table you use the value of the non-convex loss functions as a measure of how good one approach is w.r.t. others. This may suggest that convergence to different local minimisers is achieved, althoutgh from the examples it seems that the trajectory is pointing towards the same local minimiser. So why is the loss smaller? Did you stop iterations after a max number of iterations and notice that in one case you got a lower value (closer to the one of the minimiser you are converging to)?
- The two 1d illustrations in Figure 4 are enlightening but not clear at all without looking at the appendix. I would provide some more details in the main body of the paper
- In the Informal Theorem on page 9 (line 477) what is the function "g"?
- I would be careful with the use of the word "restarting" as in the standard optimisation community this is a strategy more concerned with the estimation  of the strongly convex parameter (see for instance DOI4: 10.1007/s10208-013-9150-3) than the step-size. Also, the use of the restarting strategy you propose sounds unnecessarily expensive. Why keep starting with the initial step-size especially when this is too big when one can use the last estimated one? You say that they seem to work much better but I imagine they require more inner checks?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes an enhancement to backtracking line search by introducing an adaptive adjustment to step size rather than the traditional multiplicative retraction. The basic idea is to not just backtrack when the acceptance criterion is not met but rather to use the violation information to adjust the backtracking factor. The empirical results demonstrate significant improvements in several cases and the authors also provide some theoretical justification for the performance.

### Strengths
The empirical results are strong which in my books is also the main merit of the paper. The theory while nice/ok is not particularly spectacular or unexpected but does provide a nice complement to the observed performance in practice. 

Still I like the paper quite a bit and set my initial score to accept based on the computational benefits of the proposed approach.

(while not strictly required to be read the appendix provides some additional computational results which are nice)

### Weaknesses
The paper feels a little thin on the contribution mostly consisting of strong empirical results. the underlying idea of a dynamic adjustment is nice but not particularly surprising. I personally very much like the paper, however I could understand if other reviewers find its theoretical contributions too little.

While the empirical results are indeed compelling, the core algorithmic contribution, while practically useful, lacks a certain depth. The adaptive adjustment mechanism, while intuitive, doesn't introduce a fundamentally new concept in line search methodologies. It primarily refines an existing backtracking approach, rather than presenting a novel theoretical framework or a significantly different perspective on step size selection. The theoretical results, while providing some justification, don't offer substantial new insights into the convergence properties or the behavior of the algorithm under various conditions. The analysis seems to follow standard techniques for line search methods, and does not delve into more nuanced aspects of the proposed adaptive backtracking.

### Questions
no questions - see above

### Soundness
4

### Presentation
4

### Contribution
3

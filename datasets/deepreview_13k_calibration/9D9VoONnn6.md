# Provable Data-driven Hyperparameter Tuning for Deep Neural Networks

- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 8, 3

## Abstract
Modern machine learning algorithms, especially deep learning-based techniques, typically involve careful
hyperparameter tuning to achieve the best performance. Despite the surge of intense interest in practical
techniques like Bayesian optimization and random search-based approaches to automating this laborious and
compute-intensive task, the fundamental learning-theoretic complexity of tuning hyperparameters for deep
neural networks is poorly understood. Inspired by this glaring gap, we initiate the formal study of hyperparameter tuning complexity in deep learning through a recently introduced lens of data-driven algorithm design. We assume that we have a series of deep learning tasks, and we have to tune hyperparameters to do well on average over the distribution of
tasks. A major difficulty is that the loss as a function of the hyperparameter is very volatile and furthermore,
it is given implicitly by an optimization problem over the model parameters. This is unlike previous work
in data-driven design, where one can typically explicitly model the algorithmic behavior as a function of
the hyperparameters. To tackle this we introduce a new technique to characterize the discontinuities and 
oscillations of the loss function on any fixed problem instance as we vary the hyperparameter; our analysis 
relies on subtle concepts including tools from differential geometry and constrained optimization. This can be 
used to show that the intrinsic complexity of the corresponding family of loss functions is bounded. We instantiate 
our results and provide the first precise sample complexity bounds for concrete applications—tuning a hyperparameter that interpolates neural activation functions and setting the kernel 
parameter in graph neural networks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposes a learning theoretic approaches to hyperparameter optimization. They show that using results from learning theory, it is possible to estimate the error of hyperparameter optimization in the case where the function $f(x, \alpha, \omega)$, representing the neural network, is piecewise constant or piecewise polynomial. The authors prove that this assumption is true for two instances of hyperparameter optimization for deep neural networks, providing corresponding learning guarantees.

### Strengths
- Applying a learning theoretic approach to hyperparameter optimization is original, challenging and novel.
- Hyperparameter optimization is a very heuristic research domain and it is refreshing to see some efforts towards more principled understanding and characterisation of the problem.
- The paper presents an impressive piece of theoretical work.
- The paper is well structured

### Weaknesses
 - Applying a learning theoretic approach to hyperparameter optimization is original, challenging and novel.
- Hyperparameter optimization is a very heuristic research domain and it is refreshing to see some efforts towards more principled understanding and characterisation of the problem.
- The paper presents an impressive piece of theoretical work.
- The paper is well structured

### weaknesses:
 I would like to state that I was not able to check the proofs completely since I am not an expert in learning theory. I think that this paper would at least require an examination of these proofs by an expert in the field before acceptance.

### Major

- My main problem is about the positioning of the paper. The paper claims to provide guarantees for hyperparameter optimization for deep neural networks, but in reality, it provides guarantees:
	- In a setting that is unusual for hyperparameter optimization, i.e. the setting where $\alpha_{ERM}$ is obtained after a sampling  of several whole datasets from $\mathcal{D}$ (see l.163), whereas usually hyperparameter optimization is performed for one single dataset. So, this setting does not correspond to reality, diminishing the impact of the work. In addition, the paper focuses on the optimization of one single hyperparameter, which misses the stakes and challenges of hyperparameter optimization that are more about the large number of hyperparameters and their interactions.
	- It is not applicable to "hyperparameter optimization of deep neural nets" but rather to (i) the interpolation parameter of activation function in a (debatable, see questions) application of one hyperparameter opt algorithm called DARTS (2) kernel parameter of graph neural nets. They are two very specific and not-so-common instances of hyperparameter optimization, and each of them required significant theoretical work to prove that they match the piecewise constant / polynomial assumptions.
*  l.177 $u_{\alpha}$ is computed by solving an optimization problem. This problem is stochastic by nature, whereas $u_{\alpha}$ is presented as a function (see questions)
- Some problems in the proofs:
	- **(potentially serious)** I did not find any proof of Lemma 3.3 in the Appendix, whereas it seems central, and the authors clearly state that Lemma 3.1 is not applicable in the case of Lemma 3.3 (so it would need a proof even more).
	- **(presentation)** Warren's theorem used in the proof of Th. 6.1 but no references, we don't know what it is. It is not a standard Theorem.
	- **(presentation)** l.926, 1424, 1476 "standard learning theory results gives us..." which standard learning theory result ??
### Minor

- The presentation could be improved:
	- l.56: random search methods [...] only work for a discrete and finite grid" this is not true.
	- l.93-95 sentence not correct
	- l.249 state that the results holds thanks to Th. 2.1
	- l. 258 piece function not defined, $c_i$ is introduced and no no longer used (why not defining as in 5?)
	- l.282 Theorem 4.1 you meant Lemma 4.1 right ?
	- l. 308 Notation $R_{x,t}$ different as before
	- l.309 "behaves regularly" not defined
	- l. 310 preimage introduced but not defined (defined below but you should define it prior to using it)
	- Assumption 1 is really difficult to grasp. The authors say that it is "relatively mild" but it is not at all conveyed by the presentation.

### Questions
- What is the link between assumtion 1 and deep neural networks?
- Can you calrify the link with DARTS? To my understanding, what they do is not what is stated in the paper. They use weights to encode the probability of using $o_1$ and $o_2$, to make the NAS differentiable. It is not an interpolation.
- l.177 $u_{\alpha}$ is computed by solving an optimization problem. This problem is stochastic by nature, whereas $u_{\alpha}$ is presented as a function. How do you cope with this stochasticity in your analysis ?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proves statistical learning generalization bounds for the task of optimizing architectural hyperparameters (ie those static during training) when allowed multiple problem instances. In particular, using machinery derived from piecewise decompositions of the associated utility function, the authors are able to (under some assumptions on geometric regularity of the decomposition) derive PAC-style sample complexity results for two architectural optimization applications of interest: (1) learning an optimal interpolation between piecewise-polynomial activations and (2) optimizing a certain parameterized polynomial adjacency kernel in graph convolutional networks. The proofs rely on recent statistical learning results for problems with piecewise-structured utilities, and adapt/apply these techniques to more specific and involved settings.

### Strengths
I think the overall approach to getting generalization bounds for this type of architecture search (which is fairly understudied) is solid. Finding piecewise/local structure (w.r.t. $\alpha$) in the costs of optimized networks, deriving learning complexity results for these piecewise structures, and bootstrapping up to a generalization bound for the overall problem feels like a very natural high-level process. Since the main statistical learning theory workhorse (the [Balcan '21] paper) expresses complexity in terms of oscillation, the authors proceed to use certain problem structures (in particular, piecewise constant, piecewise poly) to control these oscillations in a reasonable way -- the latter setting requires some clever geometric reasoning to pull off. To me, the main strength of this paper is the overall perspective taken on architecture search and the method of translating geometric structure of the meta-loss landscape to learning complexity results. Furthermore, the approximation method to relax Assumption 2 to Assumption 1 is very smooth.

### Weaknesses
I will list several considerations that are mainly in terms of presentation/contextualization of the results. I am sorry in advance for how long this section is, but I wanted to be helpful and thorough :)

1. This paper sets out to prove generalization bounds for the empirical risk minimizer $\hat{\alpha}$, and it does so. This is a worthwhile theoretical goal on its own (and I really like how you did it!), but I think you should be careful to separate this goal from the results that would be applicable and impactful directly to practitioners. For one, (as is often the case in statistical learning), the analysis is not structured to yield an efficient, implementable algorithm for your hyperparameter tuning nor any clues for how to design one (i.e. unless we can figure out how to find the piecewise structure dynamically and make use of it, one is still stuck doing grid search, hypergradient descent, or bandit methods). In fact, I would argue that the way you've set up your analysis is counterproductive in terms of designing such an algorithm (again, I recognize that algorithm design is not the goal of your paper, but I think the presentation would benefit from being more clear about this). For one concrete example of this point, note that your initial definition of the utility function $u_\alpha$ on p. 3 implicitly assumes finding a *global optimizer* of the loss w.r.t. the network weights, which will be wildly non convex and NP-hard for DL applications. Because of this, it cannot be claimed that $u_{\alpha_1} > u_{\alpha_2}$ implies $\alpha_1$ is a better architectural choice than $\alpha_2$ since there is no telling that an efficient optimization method (like GD) will find local minima that prefer $\alpha_1$ to $\alpha_2$. In a sense, this subtlety is the whole point of papers like [Li '21 (Geometry-Aware...)] -- a useful architecture optimization algorithm needs to improve the architecture **in a way that GD can find**. To reiterate, I understand that your paper does not set out to design such an algorithm, but I think to call the architecture optimization problem "learnable" at all requires some sort of recognition of this subtlety in a way that is clear to the reader. My philosophy is that the theoretical setting should capture the interesting phenomena you wish to explain and ignore those you don't: if you want to work in a setting that is farther from practical considerations, you should make that clear and perhaps reconsider the phrase "for deep neural networks" in the title?

2. I think this paper would benefit from being more careful about presentation. To start, the phrase "hyperparameter tuning" is often (and perhaps more ubiquitously) used to refer to tuning hyperparameters of an optimization algorithm (such as learning rate), whereas your setting is focused on a static choice of $\alpha$ during the NN training and the applications are therefore architectural. This is a bit of my own bias as an optimization theorist, but I think that provable hyperparameter tuning in this dynamic sense is quite different (and, perhaps wrongly, more studied, see "meta-optimization", "learning to learn", and many adaptive LR papers) than provable NAS, but the abstract and much of your exposition is written in a way that is vague about this difference -- it confused me in the beginning and might confuse others similarly. Perhaps more importantly, I think the claim that you provide the "first precise sample complexity bounds for applications" and "first analysis for the learnability of parameterized algorithms involving both parameters and hyperparameters" should be treated with more care. For one example, I would call Prop 4 of https://jmlr.org/papers/volume18/16-558/16-558.pdf a quantitative sample complexity bound and a (constructive) analysis of learnability -- it's not clear at first glance if your and their results are comparable or one stronger than the other, but at the very least this problem has been looked at before. I am fairly sure that you are the first to present a sample complexity bound for your two applications (and this is nontrivial through your analysis, since it requires unveiling particular piecewise structure of the applications), but I see no reason why one couldn't get some result in these applications as a corollary of Theorem 1 of the Hyperband paper. Again, we would have to see if your geometric analysis gives any advantage over such a bound -- I am not saying that your bound is worse or equivalent, I am saying that it's a slightly cavalier thing to say that your bound is the "first" in such a setting where prior results seem directly applicable. 

3. In terms of the proof methodology, I would like to know more about how to control the # of piecewise components in the piecewise decompositions you use. Your Lemma D.1/E.8 are in a sense the exponential worst-case bounds, but perhaps there is more advantage to be had from a closer look into when the number of pieces is smaller? As an example, here is a cool result https://arxiv.org/pdf/1901.09021 showing that, for piecewise-linear activation functions, while the worst-case number of linear regions is exponential in the # of neurons, the average case is actually linear (proven on initialization, experimentally verified during training). Such investigations shed significant light on the relationship between complexity and expressivity as measured by # of pieces, and would really help contextualize the strength/pessimism of your bounds (and may even directly strengthen them in certain settings!). I am not sure if there are more useful results in the literature, but I think it's worth revisiting.

### Questions
To recap the suggestions that I kind of roped into the "Weaknesses" section, I would advise that you:
1. be more specific about the differences between your theoretical setup and the practical setting (i.e. local optima w.r.t. NN weights instead of global) and maybe highlight which parts of your analysis help toward designing practical hyperparameter-tuning algorithms
2. be more thorough and precise about the particular type of hyperparameter-tuning you study (i.e. exemplify differences with the dynamic perspective on hyperparameter-tuning) and the relationships with prior results (such as Hyperband paper and others you cite)
3. look a bit deeper into how '# of pieces' has been studied by the deep learning theorists as a measure of complexity in order to gain insight, contextualize your results better, or perhaps even strengthen them

To finish, I want to ask a question that was lingering in my head while thinking about your paper. I feel that the [Balcan '21] paper is the main statistical learning workhorse of these results, and it all boils down to the use of 'oscillation of the utility function' as the measure of learning complexity. My geometric intuition tells me that the suitable condition is specified in terms of curvature of the meta-loss landscape, perhaps through smoothness assumptions such as Lipschitz gradients (ie bounded Hessians) -- at a high level, bounded second derivatives implies reduced oscillation. One could appeal to something like the differential part of Danskin's theorem (which is similar to your Lemma E.2) to convert smoothness of the loss to smoothness of the utility and proceed that way... do you think that a plan of attack along these lines could be more direct and result in proofs that are sharper, more transparent, or more general? I feel that the polynomial formulation may be an indirect way of doing a morally similar thing -- while the polynomial structure allows you to use Bezout and co., perhaps it puts too much emphasis on things like degree and zero sets and obscures the more fundamental object of oscillation. Do you think there are sufficient analytic/geometric tools to carry out such an approach? And do you think there is something particularly special about the (piecewise-)polynomial structure w.r.t. generalization bounds, or do you view it more as a mechanical tool that we know how to prove things about?

Thank you for reading this review! Have a lovely day.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The first formal study of hyperparameter tuning with discontinuous and oscillating optimization landscape considered, introducing a new technique utilizing techniques from differential geometry and constrained optimization.

### Strengths
Solid paper.

The subject studied is an important one. We have seen major empirical breakthroughs in empirical worlds, including training, hyper paramter tuning, fine-tuning, etc. Theories have been hard to follow up with these progresses. Work like the paper should definitely be encouraged.

The authors apply many advanced mathematics for the topic. Writing on the theory side is clear and pretty. The authors go very deep into analyze the circumstances described by their theoretical assumptions.

### Weaknesses
The settings are not well-explained. "We assume that we have a series of deep learning tasks, and we have to tune hyperparameters to do well on average over the distribution of tasks." Why not fine tuning for each different task? Why is it necessary to introduce the difficulty of task distribution for the problem of hyper parameter tuning? These questions naturally arise and there's a lack of explanation.

Some sentences are hard to parse. "A major difficulty is that the loss as a function of the hyperparameter is very volatile and furthermore, it is given implicitly by an optimization problem over the model parameters. This is unlike previous work in data-driven design, where one can typically
explicitly model the algorithmic behavior as a function of the hyperparameters." I'm confused by two sentences. A volatile function is still a function of the hyperparameters. It's likely the meaning is not well conveyed.

Maths are not necessarily relevant to the topic. The introduced techniques from differential geometry, algebraic geometry are not necessarily relevant to the real difficulties of the hyper parameter tuning problems, but might just be useful because the assumptions are taken in their favor. This leads to the question, how relevant are the assumptions to the reality? The authors argue that the landscape of hyper parameter tuning is very volatile, which gives me the impression that algebraic geometry and differential geometry are too smooth to be applicable. The authors could have presented a visualization of neural network hyperparameter landscape that confirms their assumptions. This could make the whole paper much more convincing if the actual landscape is shown to obviously satisfy the assumptions in the paper. For example, this blog https://sohl-dickstein.github.io/2024/02/12/fractal.html gives a very good presentation of beautiful fractals made by neural network training. Sometimes, blogs are much better at faithfully presenting information and more polished than papers. It feels like the papers' assumptions on discontinuities are much less discontinuous than reality.

There's a lack of discussion of implications that could be useful for the empirical community. I couldn't find relevant empirical experiments done in this paper. As the nature of the subject is quite empirical, it's essential to have empirical support and evidence of significance for improving existing results.

### Questions
Included in weaknesses already.

Why the abstract doesn't say "we use both algebraic and differential geometry"?

### Soundness
3

### Presentation
2

### Contribution
2

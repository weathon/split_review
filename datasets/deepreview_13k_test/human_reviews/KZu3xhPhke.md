# Cauchy-Schwarz Regularizers

- Decision: Accept
- Scores: 5, 6, 8, 8

## Abstract
We introduce a novel class of regularization functions, called Cauchy–Schwarz~(CS) regularizers, which can be designed to induce a wide range of properties in solution vectors of optimization problems. To demonstrate the versatility of CS regularizers, we derive concrete regularization functions that promote discrete-valued vectors, eigenvectors of a given matrix, and orthogonal matrices. The resulting CS regularizers are simple, differentiable, and can be free of spurious critical points, making them suitable for gradient-based solvers and large-scale optimization problems. In addition, CS regularizers automatically adapt to the appropriate scale, which is, for example, beneficial when discretizing weights of neural networks. To demonstrate the efficacy of CS regularizers, we provide results for solving underdetermined systems of linear equations and weight quantization in neural networks. Furthermore, we discuss specializations, variations, and generalizations, which lead to an even broader class of new and possibly more powerful regularizers.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces Cauchy–Schwarz (CS) regularizers. These regularizers can be designed to impose various structural properties in the solution vectors of optimization problems, such as promoting discrete-valued vectors, eigenvectors of a given matrix, or orthogonal matrices. The CS regularizers are differentiable, adapt automatically to appropriate scales, and avoid spurious critical points, making them suitable for gradient-based solvers and large-scale optimization tasks. The authors validate the proposed CS regularizers through applications in under-determined linear systems and neural network weight quantization.

### Strengths
The introduction of CS regularizers is the contribution of this paper. The versatility is demonstrated effectively through several concrete examples, including weight quantization and underdetermined linear systems.

Specific CS regularizer examples for various optimization problems are given to make reader easier to follow and use.

### Weaknesses
While the applications demonstrated are valuable, they are limited to weight quantization and linear systems. It would have been beneficial to explore other potential applications of CS regularizers in broader machine learning problems. 

The paper mentions the nonconvex nature of the proposed regularizers and briefly discusses the presence of spurious critical points for some variants. However, the convergence properties of the optimization algorithm in the presence of these regularizers are not analyzed. More rigorous theoretical or empirical analysis regarding convergence would strengthen the argument for their practical viability.

### Questions
I suggest adding experiments to evaluate the performance of CS regularizers in other machine learning contexts beyond neural network quantization,. This could further illustrate the broader applicability of the proposed framework.

It would be helpful to either provide convergence guarantees for specific cases of CS regularizers or at least include empirical evidence demonstrating reliable convergence across multiple trials.

The regularization can be non-convex, e.g., Symmetric Binary case in Sec. 3.1. Using multiple starting points will increase the computational cost and this may be a bottleneck for some large-scale problems.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a novel class of regularization functions, called Cauchy–Schwarz (CS) regularizers, which can be designed to induce a wide range of properties in solution vectors of optimization problems. The resulting regularizers are (i) simple, (ii) automatically determine the appropriate scale, (iii) free of any spurious critical points, and (iv) differentiable, which enables the use of (stochastic) gradient-based numerical solvers that make them suitable to be used in large-scale optimization problems. Furthermore, the authors also discuss specializations, variations, and generalizations, which lead to an even broader class of new and possibly more powerful regularizers.

### Strengths
1. The tool used in this paper is the CS inequality from (Steele, 2004)

2. The authors introduces a novel class of regularization functions, called Cauchy–Schwarz (CS) regularizers.

### Weaknesses
1.There are too many refereces in lines 80-84. If you don't compare and explain them one by one, the literature is superfluous.

2.The tool in this paper is the CS inequality from (Steele, 2004). Is there any other advance tools that can be used to desigh such regularization? The authors should compare these methods to show the superiority of CS inequality.

3.The propositon 1 is a known conclusion. A literature is necessary here.

### Questions
See weaknesses.

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
4

### Summary
The paper introduces a class of regularizers which they coin Cauchy-Schwarz regularizers. This class is fairly general and special cases can be used for promoting binary vectors or eigenvectors. They prove a few properties of these regularizers, e.g. some have no spurious critical points. Numerical experiments then showcase the potential of these regularizers for various applications.

### Strengths
The paper is original in its idea and clear its description. It builds upon a broad basis of related research but has its own clear novelty. Both the theoretical and numerical contributions are interesting. Modelling a-priori knowledge into regularizers is not a very timely topic but in my view still important as it gives users more freedom what can easily be incorporated e.g. into training ML models. The discussion is well-written and comprehensive.

### Weaknesses
- It is not clear how much impact the proposed work will have. In my view this is a bit niche. This is because, 1) the applications are likely fairly limited and 2) the field has largely moved on from explicit regularizers. That being said, I don't mind that.

- CS regularizers are very related to a branch in imaging inverse problems where structural similar images are encouraged, see e.g. https://royalsocietypublishing.org/doi/full/10.1098/rsta.2020.0205 for an overview. 

Key papers in this context are:

Gallardo LA, Meju MA. 2003 Characterization of heterogeneous near-surface materials by joint 2D inversion of DC resistivity and seismic data. Geophys. Res. Lett. 30, 1658. (doi:10.1029/2003GL017370)

Haber E, Holtzman Gazit M. 2013 Model fusion and joint inversion. Surv. Geophys. 34, 675–695. (doi:10.1007/s10712-013-9232-4) 

Ehrhardt MJ, Thielemans K, Pizarro L, Atkinson D, Ourselin S, Hutton BF, Arridge SR. 2015 Joint reconstruction of PET-MRI by exploiting structural similarity. Inverse Prob. 31, 015001. (doi:10.1088/0266-5611/31/1/015001)

That being said, both approaches are absolutely complementary, so this does not reduce any novelty but could be mentioned for completeness.

- The first paper gives a fairly slow and repetitive start, e.g. abstract and contributions read very similar and are just a paragraph apart.

### Questions
- The property of no spurious critical points is also called invexity. What can be said about minimization of invex functions over convex domains? My guess would be that this is still invex, so the property could be preserved by the constrained formulation. In contrast, if we add a convex data fidelity term, I am certain that this will not lead to an invex problem, hence the usual nonconvex issues arise (as also discussed in the paper)

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The author(s) study a class of regularization functions that aims to discretize vectors, but also in other cases to find solutions to constrained problems. The derivation is flexible and returns differentiable regularizers (apart from some motivated examples in the appendix). From the idea, some theoretical and practical examples are discussed. This is done especially for cases in which finding discretized versions of solution vectors is of interest, e.g. Neural Network quantization.

### Strengths
The paper is well written. Derivation of the regularizers is from first principles. The discussion brought forward after presenting the method has the right balance between practical examples and theoretical examples. It is a nice conference paper idea and looks like there is room for theoretical extensions. Experiments and plots are well exposed. Also, the limitations discussion is very honest.

### Weaknesses
- the computational cost might be very high; 
- from the paper, one big question/weakness I have (but I will place it here), is: what is the class of constraints that this method can give? This is not discussed in the text, as only explicit examples are shown. We can see it discretizes vectors, we can see it finds solutions to Procrustres-type problems, and we can see it finds eigenvalues. What else?

### Questions
- line 097-098: Why would an alternative solution to the orthogonal Procrustres problem be needed? I do not understand the justification. 
- figure 4: why is $\ell_{\infty}$ beating some methods? 
- why do we observe the "non-convexity of regularizers"-problem only in the bad performance of $\ell_{ter}$ in figure 5? I mean, why not everywhere else? I understand that the ternary regularization is more unstable, but are there other evident reasons?

### Soundness
3

### Presentation
3

### Contribution
3

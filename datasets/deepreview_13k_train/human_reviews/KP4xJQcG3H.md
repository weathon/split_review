# Lagrangian Proximal Gradient Descent for Learning Convex Optimization Models

- Decision: Reject
- Scores: 3, 5, 8, 6

## Abstract
We propose Lagrangian Proximal Gradient Descent (LPGD), a flexible framework for learning convex optimization models. 
    Similar to traditional proximal gradient methods, LPGD can be interpreted as optimizing a smoothed envelope of the possibly non-differentiable loss. The smoothening allows training models that do not provide informative gradients, such as discrete optimization models. 
    We show that the LPGD update can be efficiently computed by rerunning the forward solver on a perturbed input, capturing various previously proposed methods as special cases. 
    Moreover, we prove that the LPGD update converges to the true gradient as the smoothening parameter approaches zero. 
    Finally, we experimentally investigate the benefits of applying LPGD even in a fully differentiable setting.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on a learning model with parameter $\theta$ that produces another set of parameters $w$ that defines a primal-dual optimization problem with solution $z^* = (x^*, y^*)$. The goal is to optimize the whole pipeline with respect to the problem defining parameters $w$ that can be then connected to model parameter $\theta$. Since with respect to $w$, this is a non-smooth problem, the authors design a framework inspired by classical proximal gradient method (PGM). The new framework is named Lagrangian PGM since a "divergence" based on difference of Lagrangians is used to define the gradient-descent type update. The authors show an asymptotic result that as the coefficient in front of the Lagrangian "divergence" term approaches to 0, the true gradient is achieved.

### Strengths
The problem considered in the paper and the motivation are interesting (albeit difficult to understand in the current presentation). The authors are making connections with classical approaches in nonsmooth optimization such as Lagrangian, Moreau envelopes, mirror descent and Bregman divergences to get inspiration to tackle the specific nonsmooth optimization problem at hand. The subtle and important aspects such as assuming the existence of unique solutions are pointed out and some effort has been made to partially address these shortcomings. It is also good to see the authors discussing the limitations in Appendix A with preliminary ideas on how one might go around improving on them.

### Weaknesses
Unfortunately, the paper is not written in a precise way for problem statements, results, tools etc. In many places it is not clear what the goal is and hence the contribution of the paper is quite unclear both in terms of mathematics and also practical aspects (not clear how to solve subproblems etc.). The assumptions and discussions about them are unclear. Even though many technical concepts are introduced, not much is proven with them and much of the claims in the paper are not proven (a list is below). The problem definition, goal etc are not clearly written and it requires the reader to read multiple times to even understand this. Unfortunately, the presentation needs to be vastly improved for this paper to be suitable for readers to understand and gain from.

- Proper references are not given in many places. For example, last paragraph in page 1 cites for "traditional proximal optimization" the papers by Moreau, 1962 (an excellent reference) and Parikh&Boyd, 2014, Boyd&Vandenberghe, 2004 which are okay (even though it is not clear where in Boyd&Vandenberghe's book proximal methods are discussed) however many of the most important references are not there. For example, no mention of Rockafellar who is the founding father of the field along with Moreau, his book Convex Analysis (at the least) should be cited here with many of his other founding papers. One of the most impactful proximal gradient based algorithms is FISTA by Beck and Teboulle which is also not cited. Nesterov's or Tseng's accelerated proximal methods are not cited. Another important reference is by Figueiredo, Nowak, Wright, 2007 which is again, not cited. It is also not hard to find these references, they are all included in Parikh & Boyd's text. 

- Sect 3.1, problem setup is not written well. One can write this in a much clearer fashion. Especially for optimization audiences, it is much better to write a well-defined problem, rather than the arrows and unclear notation in the start of Sect 3.1. For example, one should define precisely the "model" $W_\theta$. What kind of a function is it? What assumptions are needed on it? One then needs to write the optimization problem in terms of the main variable ($w$ or $\theta$) and then clearly describe the assumptions on each function appearing in the problem.

- Problem (1) is well-defined but it depends on $w$ hence it does not really describe the whole problem. It should be written in a precise problem formulation by taking into account the relations with arrows given at the start of the section.

- For problem (1) the authors assume that unique solution exists, which is, of course a very strong assumption. The authors say they address this point in App F, which in my reading goes to a tangent about "graphical derivatives" rather than showing us how to get around this assumption. In particular, how to generalize the results in the paper without assuming unique solution? A precise statement is needed rather than an extended discussion which is both difficult to follow and also difficult to follow to other parts of the paper. What would be good is to point out how the particular statements in the paper will change when one considers non-unique solutions etc. Right now, this is not very understandable unfortunately.

- Sect 4.2 requires eq. (14, 15) are uniquely attained, why would this be true? App F or G does not really show this (or even if it does, it is very unclear). Please provide precise statements and then proofs in App F and G. Right now it is unclear what the authors are trying to show.

- It is not clear how one actually implements the algorithms described in the paper. In fact, the algorithms are not even written down, only gradients are derived for example in eq. (28, 29).  I understand the algorithm is just gradient descent but the gradients depend on many other things such as $z^*$ and $\tilde z^\tau$ that the reader needs to track down in the quite heavy text. They need to be presented in a compact fashion to be able to see what the algorithm is. Next, lookng at eq. (28, 29), how does one solve for $z^*$ and $\tilde z^\tau$? The authors mention here "same efficient optimization algorithm used to solve (1)": what is this algorithm? What kind of an algortihm are we lookng for? What is its cost? Clearly, one cannot solve the problem to exact solution, how does one tolerate inexactness?

- Example 2 again refers to Appendix F for an "in-depth" discussion whereas the discussion in Appendix F is quite hard to connect to things in the main text. As I asked above, App F and G should be more precise with statements and proofs and connections to the main text.

- Where in App G the proof for Theorem 4.1 with non-unique solutions given?


+++ post-rebuttal

I already explained the reasons for keeping my score unchanged in my follow-up message. Here are some more remarks for the authors so they can hopefully improve their manuscript in the future. --  the main result as stated by the authors is essentially stating that asymptotically they can approximate the gradient. This result is not a satisfactory convergence result in my reading. It is unclear to me how the authors would extract meaningful results from here. I do not believe that results in this form where the implications or meaning are not clearly explained help the community, but I think such practice cause only confusion. Please give an effort to explain your results to show what they can and **more importantly** what they cannot do. -- I am not against the improvement of the paper during review stage and totally acknowledge this is one of the most important aspects of the review process. However, when the arguments of the paper needs to be significantly modified as is the case here and these modifications are not clear to the reviewers (not clear to me in this case), I do not think that we can do a healthy evaluation in such a short time frame. There is a limit to the amount of changes that can be made to a paper after which the paper needs a new conference review cycle. I am not sure that it is fair to the reviewers that the authors submit a version of their manuscript with incorrect or imprecise claims (as pointed out in my review and accepted by the authors) and then expect the reviewers to do another review to the paper with major modifications in a short discussion period (until Dec 5th). In summary, I am not claiming the analysis is not correct (the next review cycle should help clarify this), but I am saying that even if it is correct, the results do not seems satisfactory to me and the paper, in my view, is not written in an accessible fashion. Please refer to my review for examples.

### Questions
More questions also appear in "Weaknesses" section of my review.

- Last paragraph of page 1 states that the paper can solve problems with non-linear objectives or learnable constraints. First, it is not clear what "learnable constraints" mean. Second, the paper itself says in Sec 4.3 that eq. (16) and (17) might "diverge" and hence they focus on linear loss in Sec 4.5. How does the paper handles non-linear loss functions? Also, what does it mean for (16) a value of an optimization problem and (17) the optimizer of the problem to "diverge"? Do the authors mean that a solution might not exist? Or do the authors mean that an algorithm might diverge for solving the problem? It is quite unclear.
 
- What is the purpose of introducing $D_2$ in eq. (5)? clearly it is just the Euclidean squared norm. I can see that the authors generalize later to a "divergence" in Sect 4.1 but $D_2$ notation is not really necessary here given that the paper has so many other notations making it difficult to follow for a reader.

- With Moreau smoothing, we have an extended theory on the smoothing affect, but the authors just replace the squared norm with the "Lagrangian divergence" and state that now we have a smoothed objective. This needs to be proven. Why is this envelope smooth? With which Lipschitz constant? What does one need to assume about the Lagrangian to be able to argue smoothness of the envelope? For sure justification is needed since as the authors also cite in App C, Bauschke et al., 2018 did a systematic study with Bregman Moreau envelopes. Such a precise statement justifying "smoothness" is missing.

- eq. (12): bad notation, x on the left and right hand sides are not the same.

- eq. (13): either needs to be proven or given a reference.

- Where are the proofs of Prop 4.2 and 4.3?

- Sect. 4.4: why are the assumptions of Danskin's theorem satisfied in this case, can the authors please clarify?

- Sect. 4.5: what does it mean to "expose the linear parameters of the Lagrangian" right before eeq. (25)? Where is $\Omega$ defined?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The main contribution of this paper is the unification of several prior methods into a comprehensive framework termed Lagrangian Proximal Gradient Descent (LPGD). This approach is rooted in traditional proximal optimization techniques. The study further delves into the application of LPGD in different scenarios, emphasizing its potential improvements over gradient descent in certain settings namely, those where the gradient is uninformative (e.g. discrete optimization).

### Strengths
Overall, the paper is well-written and easy to follow. The contribution is of interest for the community.

### Weaknesses
There are two main weaknesses:

1) The experiment section is rather small compared to the rest of the presentation. A lot of mathematical details could be eluded or referred to by a citation to a previous work (e.g. derivation of Moreau envelope, proximal operators, etc..). A quick (and rigorous) definition is more than enough, see below for a few remarks. The current experimental setup lacks depth and real-world relevance. The toy experiment, while illustrative, does not sufficiently demonstrate the practical advantages of the proposed LPGD framework. It is crucial to evaluate the method on more complex and realistic datasets to validate its effectiveness and potential for real-world applications. The absence of comparisons with state-of-the-art methods in relevant domains further limits the impact of the experimental results.

2) There is too much context at the beginning of the presentation. No need to mention a vector $\mu$ that is not used in the demonstration. I would first consider a convex optimization problem, and introduce the Lagrangian and the primal/dual variables. Explain that $f$ can be composite and have a non-smooth component, and explain Moreau and its connection with the proximal operators with 2 definitions. Finally, you can start your demonstration. Some space would be saved by shortening in "Background and Notations" section can be used to do one more experiment (see above).

=========

A few remarks:
- Missing hypotheses in the Moreau envelope definition: $f$ must be proper and lower semi-continuous. 
- Instead of establishing a connection between the Moreau envelope and the proximal operator, refer the reader to a chapter in a well-known textbook that already explains in great detail the connection (e.g. Bauschke and Combettes).

=========

Overall, I believe this work deserves to be published in a venue like ICLR. However, in its current form, the manuscript is not ready for publication. The authors need to put more effort into establishing a more concise background and more rigor in the definitions of the notions used. Furthermore, the experiments section should be enriched with real-world data.

### Questions
1) In your experiments figure (figure 2), how do you explain that the $LPGD$ (avg) yields a significantly lower loss compared to the $LPGD$ (lower) and $LPGD$ (upper) schemes? Could you provide an intuition?

2) Could you elaborate on the convergence rate of LPGD? Is is the same as vanilla gradient descent with the additional cost of evaluating the upper and lower proximal maps?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a class of Lagrange Proximal Gradient Descent method. As the authors claimed, the main contribution of this work is that It generalizes many existing methods. The technical part of this paper is solid, and the paper is well-written and easy to follow.

### Strengths
I read over the paper. The technical part of this paper is solid and the ideas are promising. Similar to the idea of Mirror descent, they consider a specific distance function (Eq (11)). This idea is not surprising to me, but the authors then construct lower and upper Lagrange-Moreau envelop, and average them to improve the accuracy of the gradient with respect to the parameter w. This idea is similar to the idea of the central difference method which usually has higher precision than the forward and the backward difference method. They also demonstrated this by numerical experiments.

### Weaknesses
1. The literature survey in this paper is not good enough. They surveyed many papers in Section 2, but the details of the most relevant papers are not provided either in the main text or in the Appendix. I'm particularly interested in existing papers that can also compute the (approximate) gradient of the function $\ell(x^\star(w))$. Moreover, the authors claim that the proposed method generalizes many existing methods and discuss this in Example 1,2,3. For more general problems rather than these examples, whether the proposed method generalize existing methods?

2. From the experiment (Figure 2), even in terms of Epochs, LPGD-medium $\tau$ is faster than GD. This is not straightforward to me. If I understand correctly, all the simulated methods in the experiments are based on GD, while the gradient is computed based on different approaches. Therefore, I wonder whether the poor performance of GD comes from the low accuracy of gradient information computed by the method in Argarwal 19b?

### Questions
1. What is the state-of-the-art method for solving the considered problem? Stochastic gradient-based or? Can this work be extended to that setting? I will suggest the authors to discuss this in Conclusion.

2. Should the sentence "Note that for a general loss, the optimization (16) and (17) may diverge" below Eq (17) be revised as "Note that for a general loss, update using (17) may diverge". This sentence is unclear and less accurate because first, (16) is only an approximate loss and it's incorrect to say it may diverge.

### Soundness
3 good

### Presentation
3 good

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
The paper proposes Lagrangian Proximal Gradient Descent (LPGD), an optimization framework for learning convex optimization models. It is effective for problems with non-differentiable loss functions and can handle models where gradients are not readily available. LPGD smooths the loss function, making optimization feasible in such scenarios. It efficiently computes updates by rerunning the forward solver and converges to the true gradient as the smoothing parameter approaches zero. LPGD can also offer benefits in fully different settings, making it a versatile tool for various optimization tasks. The method is interesting with promising performance.

### Strengths
The authors provide a new method, which considers a model with an embedded constrained convex optimization. They also provide a new update, the Lagrangian divergence proximal operator, which generalizes the classical Bregman divergences. Compared to classical proximal gradient descent methods, the update is new.

### Weaknesses
1. The proposed method does not come with the convergence rate analysis.

2. Could the authors provide examples of neural network-type constrained minimization problems? The neural network can be chosen as a simple one. This is to demonstrate the difference and the connection between current methods and the classical ones.

### Questions
One expects to see the method working on a neural network-type constrained optimization problem.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

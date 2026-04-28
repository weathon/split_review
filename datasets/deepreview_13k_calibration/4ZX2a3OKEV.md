# Solving hidden monotone variational inequalities with surrogate losses

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 8, 6, 6

## Abstract
Deep learning has proven to be effective in a wide variety of loss minimization problems.
However, many applications of interest, like minimizing projected Bellman error and min-max optimization, cannot be modelled as minimizing a scalar loss function but instead correspond to solving a variational inequality (VI) problem.
This difference in setting has caused many practical challenges as naive gradient-based approaches from supervised learning tend to diverge and cycle in the VI case.
In this work, we propose a principled surrogate-based approach compatible with deep learning to solve VIs.
We show that our surrogate-based approach has three main benefits: (1) under assumptions that are realistic in practice (when hidden monotone structure is present, interpolation, and sufficient optimization of the surrogates), it guarantees convergence, (2) it provides a unifying perspective of existing methods, and (3) is amenable to existing deep learning optimizers like ADAM.
Experimentally, we demonstrate our surrogate-based approach is effective in min-max optimization and minimizing projected Bellman error. Furthermore, in the deep reinforcement learning case, we propose a novel variant of TD(0) which is more compute and sample efficient.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a new method for optimizing variational inequalities with hidden structure by optimizing a series of surrogate losses, thereby extending previous methods for optimizing scalar loss functions. The authors provide a new $\alpha$-descent condition on the sequence of inner surrogate optimization problems which is used to derive linear convergence rates for the outer optimziation in the deterministic and unconstrained stochastic setting. Specific choices of optimizer for the inner surrogate loss are shown to generalize previous works. Additionally, the authors provide conditions under which linear convergence is achieved.

Experimentally, the method is tested on optimizing min-max games and projected Bellman error. In the min-max setting different variants of the method are compared, showing that the choice of the inner optimizer matters by improving on the special cases treated in previous work. In the RL setting, the surrogate loss perspective is connected to computationally expensive preconditioning methods which is shown to be approximated in the linear case via the presented iterative scheme. In the non-linear case the policy evaluation problem is tackled for two mujoco environments, where different versions of the method are shown to improve over the special case of TD(0) in terms of wall-clock time and sample efficiency.

### Strengths
- The extension of iterative surrogate optimization from the scalar to the variational inequality case is a significant contribution.
- Paper offers a rigorous theoretical analysis.
- Strong performance of the method compared to the TD0 baseline.
- Well-written and relatively easy to follow.

### Weaknesses
 - The empirical finding of better optimization of the inner problem not leading to better optimization of the outer loop is very interesting but unfortunately not examined in more detail. Both a more in-depth experimental investigation and a theoretical justification for this effect could strongly improve the paper, see also the questions below.

 - The authors write: "In general $\ell_t^*$ may not be zero and so this condition cannot be verified directly, however, this condition can often be met via first-order methods for a fixed number of steps or can be approximated with $\ell_t^*=0$." (line 171) I am wondering how practical $\alpha$-descent condition is, is it possible to verify this condition in the presented experiments in section 5?

Style:
- Fig 1: It is hard to tell the methods apart, maybe use different line styles.

### Questions
- It is very interesting that better convergence of the inner loop does not necessarily translate to better convergence of the outer loop, i.e. more iterations are not necessarily useful (e.g. LM, Sur-GD, GN, Gig 1 & 2). Is there a theoretical justification? How does that tie in with the $\alpha$-descent rule? If not a low loss value, what makes a "good" solution to the inner problem that improves convergence of the outer loop? Has this effect also been observed in the scalar minimization case? If yes, how does it compare?
- The authors write: "In general $\ell_t^*$ may not be zero and so this condition cannot be verified directly, however, this condition can often be met via first-order methods for a fixed number of steps or can be approximated with $\ell_t^*=0$." (line 171) I am wondering how practical $\alpha$-descent condition is, is it possible to verify this condition in the presented experiments in section 5?

Style:
- Fig 1: It is hard to tell the methods apart, maybe use different line styles.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this paper, the authors introduce a surrogate-loss-based framework for optimization of variational inequality (VI) systems, such as min-max. 

This paper is the first to extend the surrogate methodology to (strongly-monotone) VIs, where the inner loop calls a scalar optimization routine black-box. Importantly, they demonstrate with an elementary adversarial example that surrogate methods in these VIs are qualitatively more complex than surrogate methods in traditional scalar optimization (the inner loop progress needs to be strong enough to counteract the effects of $F$ to ensure outer convergence, as opposed to just $<1$ in scalar case). They show that (under sufficient inner loop optimization assumptions, quantified in the form of the $\alpha$-descent condition) the overall VI optimization succeeds in deterministic and stochastic regimes, with rates matching what is to be expected of strongly-convex optimization (ie geometric convergence). Lastly, they observe that an existing VI optimization method (PHGD) can be seen as a particular choice of inner loop optimization routine, and they investigate the benefits and consequences of alternative choices of inner loop algorithm and number of steps. 

Experimentally, the authors test the surrogate method for VI optimization in previously-investigated small-scale games, as well as on value prediction in fairly substantial RL settings. They observe interesting consequences of certain choices of inner loop algorithm and number of steps, and they demonstrate the value of the surrogate framework. In the RL experiments they see a significant improvement in environment sample complexity due to multiple inner loop iterations -- this matches some related work, but importantly does not require complex learned surrogate reward signals!

To summarize, the paper introduces the surrogate framework (outer loop over outputs and inner loop over model parameters) to a class of VI problems, demonstrates the nontrivial result that scalar optimization can (under some assumptions) be used black-box as a subroutine, and empirically investigate the associated phenomena on tasks of increasing complexity. Very cool!

### Strengths
This paper has a strong originality in that it appears to be the first to extend this type of surrogate losses to VIs, and it does so in a way that provably takes advantage of hidden monotonicity/convexity structure. Importantly, this extension is nontrivial -- there is a simple and solid adversarial example the authors provide (Prop. 3.3) that shows a difficulty gap in comparison with surrogate losses in the scalar optimization case. I think there is the extra strength (though perhaps it isn't highlighted enough, see my "Weaknesses" section) that it appears the framework, broad proof techniques, and main takeaways seem rather robust to choice of inner optimization routine (i.e. robust to assumptions, rates of convergence, etc.). In my eyes, the authors have constructed a fairly general methodology to reduce VIs with hidden structure to scalar optimization in a way that directly leverages that hidden structure -- this is very cool, and in general such reduction results tend to be quite powerful (such as online-to-batch reduction, nonconvex-to-convex reduction such as Algorithm 3 in https://arxiv.org/pdf/1806.02958, etc). 

The analysis is also quite clear, proceeding along similar lines to many optimization papers and doing a fantastic job of contextualizing results, definitions, and assumptions in prior works. In particular, Section 4 (before subsection 4.1) skillfully highlights the flexibility of choices of inner loop optimizers in an organized way, noting equivalence to prior methods (such as PHGD) where applicable. This is a good transition to the experiments, which compare different setups of the inner loop routine in various minimax and RL value-prediction environments. Overall, I think this presentation is clear, the assumptions are obvious, and the experimental apparatus seems right for the general framework (though it would have been cool to see a slightly larger-scale experiment, and I think GAN training is the perfect low-hanging fruit if the authors have the resources!). Lovely stuff :)

### Weaknesses
I think the main (and only, to be honest) weakness of this paper is a weakness of presentation -- in particular, I feel that (as outlined in the "Strengths" section of my review above), the main contribution of this paper is that it clarifies and formalizes a framework where black-box scalar non convex optimization guarantees can be bootstrapped up to hidden-structure VI guarantees. However, at many points I felt that the presentation did not highlight this strongly enough, and instead chose to focus on particular rates/modes of convergence and substantiating particular assumptions. 

To be specific, I would argue that the $\alpha$-descent condition for inner loop progress is a bit of a red herring. As you mention, such convergence can only be shown in specific situations under the usual non convex optimization assumptions (PL condition, for example), which can often be difficult to justify. However, I feel that it's even unnecessary for you to justify it! It seems to me that, for example, Lemma A.2 and Prop A.3 would go through (perhaps with significantly more work) for weaker/more exotic types of inner loop guarantee -- the vibe of the proofs is moreso that (strongly-monotone) VIs allow you to push through the classic optimization proofs (the [Sakos '24] paper offers a similar takeaway in terms of bootstrapping convex VI guarantees up to hidden-convex VI guarantees, see their statements on p. 11). I bet there is a way to turn this into a strength of your paper: maybe something more like "we prove things under the $\alpha$-descent condition for clarity, but our meta-point is a more general reduction from VI optimization to scalar optimization via surrogate losses". I am not recommending you to do the analysis under all kinds of crazy inner loop guarantees, but instead to reweight the presentation a bit to highlight the robustness to inner loop method.

I will say that the $\alpha$-descent setting is a fantastic choice of inner loop guarantee to demonstrate the difficulty gap between scalar vs VI surrogate methods; it makes the presentation of the adversarial example very clear. However, I would have liked to see it used more as a presentation tool/particular instantiation of a more general phenomenon, whereas it often felt like you were keeping it around as a core part of your results. If the impact of this condition was qualitatively different in the VI setting than in scalar surrogate optimization then that would be one thing, but I am unsure of this (note: I am not too familiar with this style of surrogate losses via hidden convexity/monotonicity -- if I am wrong about this perhaps a toy example exemplifying the difference would be cool!). 

To really hammer this point home (sorry, but I don't really see any other weaknesses to write about), I feel like over-indexing on this particular criterion forces you to get stuck in the muck of justifying assumptions such as spectrally bounding input-output Jacobians of neural networks -- to some this may be a losing battle (models on complex, high-dim data will be likely to disregard features dynamically and hopefully learn lower-rank representations), but one I don't think you need to be fighting! Certain hypothesis classes/optimizers/datasets/etc will have different choices of inner loop routine that make sense, and the beauty of what you've shown here is that surrogate methods in VIs appear flexible to these choices. The language of reductions feels much more natural for such a result: I give you a VI problem with hidden monotone structure, you reduce it to a sequence of scalar non convex problems, and the practitioner/domain expert figures out the right inner loop soup (choosing between first-order or second-order methods, bias-variance tradeoffs, etc) to make it work. 

To sum up, it is my opinion that if you are going to use non convex optimization as a black-box for the inner loop, treat it like a black-box (not just in terms of whether to use ADAM as the optimizer, but even in a broader sense). Aside from this (and some questions that I put in the "Questions" section), I have nothing else to say but awesome paper!

### Questions
1. I think it's very interesting that sometimes more inner loop iterations damage the performance as a whole! (I once did some empirics for boosting weak learners in RL, where I saw a similar thing that I attributed to overfitting...). Do you have any explanations/intuitions for why this could happen (ie is it a general phenomenon in surrogate learning, or an artifact of these small-scale game experiments)?

2. The results on improved sample complexity in the RL value prediction tasks are very compelling in my opinion! I think it fits neatly into an overarching philosophy that blind RL is wasteful (in terms of samples/environment interactions), and that some form of guidance really helps. There are whole fields (search goal-conditioned RL, contrastive RL, etc) that attempt to figure out how to learn the right flavor of guidance, and it seems to me that your form of (not-learned!) surrogate losses can be seen as a particularly simple form of this. From your work and the related literature (which you know 1000x better than I), do you suspect that there can be any theoretical insight/proofs on synthetic settings for how surrogate losses get a provable advantage in terms of number of diverse samples? Certainly one can make claims about decreasing the # of outer loop iterations, but I would be very interested if the extra regularity of your simple surrogate loss trajectory (ie the GD trajectory on $z_t$) can manifest as more efficient exploration?

3. Probably not a valuable question, but I have to ask: would it be possible for you to do GAN training? It would be convincing to deep learning practitioners and theorists alike!

3. This is more a question of personal interest regarding this style of surrogate losses (i.e. ones where you take a step in output space, use inner loop to make the model catch up, repeat) and perhaps not specific to VIs, but here goes: *is there any understanding of how this framework assists/counteracts the implicit biases of either (1) optimization methods in the inner loop or (2) architectural choices in the model $g$?* I ask because, particularly in deep learning theory, there is often the vibe that the natural dynamics induced by such design parameters actually can help (see this paper https://arxiv.org/pdf/1802.06509 for a cool result on GD acceleration caused by model depth, for example). I could imagine some settings where the rigidity of the outer loop dynamics on $z_t$ prevent these complicated phenomena (for example, in the linked paper I suspect surrogate losses could prevent the acceleration for adversarial choices of $F$). Conversely, I can certainly imagine settings where the structure of the outer loop drives the optimization more usefully, in a similar fashion to how surrogate rewards in RL help orient an agent in a sparse-reward environment (see Question 2). Is there any understanding of this tradeoff, and perhaps more importantly do you imagine any differences to this tradeoff in the VI setting?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes an algorithm using some type of surrogate approximation to solve variational inequality (VI) problems. Those problems can be seen as finding first-order stationary points of a constrained optimization problem, but probably the setting in this paper is more general than that since the vector-valued function F is not necessarily a gradient (e.g. max-min game). The main idea is that "composite" (between the model and the loss) optimization problems in machine learning normally exhibit some structure, e.g., the loss w.r.t. to the model's output is convex (but the whole optimization function is not convex w.r.t. the model's parameters), one can push the "difficulty part" relating to model into the constraint to make the objective function convex. The authors then design a sequence of surrogate functions to minimize this reformulation problem and show convergence under a condition called "alpha-descent". To minimize the surrogate functions, they employ classical methods like Gaussian-Newton or Levenbergh-Marquardt. Numerical experiments are performed for some toy min-max games and in the reinforcement learning context.

### Strengths
The considered problem is important in the classical optimization context (i.e., constrained optimization, complementarity) and mordern ML where the loss is structured. The problem is also more general than minimizing a scalar loss usually showing up in supervised learning. The experiments show that the proposed method work fine in practice.

### Weaknesses
The paper is challenging to follow, particularly in its transition from problem (1) to the construction of the surrogate model, where additional discussion would be beneficial. The assumptions also seem overly restrictive. For instance, while assuming convexity of the loss with respect to the model's output is reasonable for most loss functions, the assumption that the constrained domain is convex feels unnecessarily limiting, even though the authors provide a few narrow examples. Furthermore, the alpha-descent condition (5) requires closer examination, as it appears to be a stringent requirement. Specifically, it requires a single constant alpha that holds uniformly across all t. This condition is particularly concerning because it implies a uniform rate of convergence across all iterations, which may not be realistic in practice, especially when the surrogate model's accuracy varies significantly over the course of optimization. The lack of discussion regarding the sensitivity of the algorithm to the choice of alpha is also a significant weakness.

### Questions
(1) In the basic case of supervised learning with a scalar loss, can we expect the proposed method perform better than off-the-shelf optimizers that work directly in the parameter space, i.e., Adam?

(2) The condition in the while loop of Algorithm 1 can not be verified. How could we let alpha be the user-defined parameter?

### Soundness
2

### Presentation
2

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
This paper studies the problem of solving variational inequalities with deep learning methods with a hidden monotone structure. The authors present an iterative optimization algorithm with two nested loops, where In the outer loop, a surrogate square loss is constructed and partially minimized in the inner loop (until a sufficient decrease condition called $\alpha$-descent is satisfied) using an optimiser such as a quasi-newton method or ADAM. When $\alpha$ is sufficiently smaller than $1$, The authors prove linear (in the outer iterations) convergence guarantees in deterministic and stochastic settings, where in latter, the algorithm converges to a neighbourhood of the solution. They also prove that, when considering general variational inequalities, $\alpha < 1$ is not sufficient to guarantee convergence. Further, they show how several methods can be seen as special cases of their algorithm. They also present experimental results on min-max optimization and reinforcement learning.

### Strengths
1. The theoretical analysis is quite thorough, considering  deterministic and stochastic cases and also addressing an issue with a previous analysis. The authors also explain how previous methods fit in their framework and discuss assumptions and potential limitations.
2. Promising experiments showing that the method can achieve faster convergence with more than one inner step iteration also in practical settings such as reinforcement learning with MLP value functions.

### Weaknesses
1. Certain parts lack clarity. Condition 2 in Theorem 3.2 seems unnecessary and needs refinement. The condition as stated, that there exist $C, p > 0$ such that for all $\eta > 0$, $\alpha < C\eta^p$, is problematic. This condition is never satisfied, as for any given $\alpha, C, p > 0$, one can always find an $\eta$ small enough such that $C\eta^p < \alpha$. This suggests a misunderstanding of the relationship between $\alpha$ and $\eta$ in the theorem's context. The proof hints at a dependency between these parameters, which is not made explicit in the theorem statement. Specifically, the condition appears to be a sufficient condition for a contraction, but this is not clearly articulated. (See question and comments).
2. The paper lacks larger scale experiments. For example Deep RL experiments (with bigger underlying neural networks) could be included to demonstrate the claimed scalability of the method. The provided 16-layer experiment in the appendix does not adequately address this concern, as the performance is similar to the 2-layer network, suggesting that the task itself does not require such a large network, and therefore does not demonstrate the scalability of the method in a meaningful way.

### Questions
Questions:
1. You claim that Sakos et al. (2024) assumes $\mathcal{Z}$ bounded implicitly in their main lemma. Can you clarify which lemma, where it is assumed and which results are affected? I could not easily find it and I think this is an important point since it uncovers a fallacy in a previous analysis.

Comments:
- The second condition on $\alpha$ in theorem 3.2 seems to be always satisfied by setting $p=1$ and $C‎ = \alpha/\eta$. From the proof it appears that there is an hidden dependency between $\eta$, $C$, $p$, and $\alpha$. The statement should either include such dependency or at least clarify this aspect.
- The use of the term “gradient step” contrasts with the Variational inequality formulation where in general $F$ is not a gradient. A possible alternative could be "proximal step".
- The related work paragraph in the introduction should probably be a subsection or its name should be removed or changed.
- The PL condition is not properly defined in the main text. It could be defined close to Line 345 or at least in the appendix.

References:

Sakos, Iosif, et al. "Exploiting hidden structures in non-convex games for convergence to Nash equilibrium." Advances in Neural Information Processing Systems 36 (2024).

### Soundness
3

### Presentation
2

### Contribution
3

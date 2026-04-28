# Simulation-Free Differential Dynamics through Neural Conservation Laws

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 5, 6, 6

## Abstract
We present a novel simulation-free framework for training continuous-time diffusion processes over very general objective functions. 
Existing methods typically involve either prescribing the optimal diffusion process---which only works for heavily restricted problem formulations---or require expensive simulation to numerically obtain the time-dependent densities and sample from the diffusion process.
In contrast, we propose a coupled parameterization which jointly models a time-dependent density function, or probability path, and the dynamics of a diffusion process that generates this probability path.
To accomplish this, our approach directly bakes in the Fokker-Planck equation and density function requirements as hard constraints, by extending and greatly simplifying the construction of Neural Conservation Laws.
This enables simulation-free training for a large variety of problem formulations, from data-driven objectives as in generative modeling and dynamical optimal transport, to optimality-based objectives as in stochastic optimal control, with straightforward extensions to mean-field objectives due to the ease of accessing exact density functions. We validate our method in a diverse range of application domains from modeling spatio-temporal events, to learning optimal dynamics from population data.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a new simulation-free method for training (stochastic) dynamics which is driven by a continuity equation (i.e., follows stochastic sde) and satisfies some objectives. 
In particular, the authors propose specific parameterization of the class of continuity equations and then optimize the given objectives in this class.

### Strengths
Personally, I like the text. It is more-or-less clearly written, understandable (but somewhere in pages 5-6 some inconsistencies appear with indices ($i \leftrightarrow D$) - I reflected them in my questions / comments); logic is clear. So, I thank the authors (but some of the “raw” moments need tweaking).

Also, It was a pleasant nostalgia for me, when reading about all of these autoregressive models and mixtures of logistics.

### Weaknesses
1. The main question for the method (and it is partially reflected in the appendix) is that the approach is not dimension-scalable. Also, the proposed parameterization with autoregressive models and mixture of logistics does not seem to be very expressive.
2. No source code for the submission.
3. While text is clearly written, some "raw" moments and misprints to be fixed (se below).

Also, please see my questions and comments below

1. Lines 037 - 038. “[...]but these methods all require simulating from the learned diffusion process to some varying degrees [Peyre&Cuturi]” - what do you mean by citing this work here?
2. A general question, eq. 12. The choice for $a_t^{\theta}$ looks a bit strange - it is kind of “not symmetric”, not “invariant” under the coordinates of the vector - because it “respects” only the last coordinate. Why do you consider exactly this “not-symmetric” parameterization? (I understand that formally this is correct)
3. I do not completely understand the second row of Figure 1. As I understand, black arrows on the canvases denote fluxes $j_t$. But following the definition of $a_t^{\theta}$, eq. 12 all these arrows should be directed along one axis (i.e., they should be parallel to unit vector $(0, \dots, 0, 1)$). But it seems that the actual arrows in Figure 1 may be directed along *two* axis.
4. Lines 297-298. Something strange, may be an inaccurate denotations' intersection: you add a quantity with $\Pi_{i = 1}^{D - 1}$ to the $i$-th coordinate. The same index $i$. Given my comment 2, may be $i$ should be equal to $D$? The same problem seems to affect eqs. 21, 22, 23 (it seems that somewhere $x_i$ should be substituted with $x_D$).
5. Lines 299  - 300. Do not understand the comment that $\sigma$ could be substituted with “function/NN whose first derivative has compact support. I think - for such an NN  there should be a condition, that at $x_D \rightarrow \infty$ this NN should approach $1$.
6. Results in Table 1. For CNF, you grab the results only for “time-varying CNF”. The other variants of CNF, e.g., jump CNF and attentive CNF are excluded from the comparison (and, by the way, achieve better NLL). Why?
7. Lines 468 - 475. I do not understand, how you achieve kinetic optimality (for AR model). Ok, you have an additional term introduced in Section 3.7 - but it is just improves expressivity and does not lead to kinetic optimality out of the box (as I understand)
8. Results in Figure 2. What is the reason of the “explosion” of particles at the final time points in the first column of the Figure?

**Misprints**

1. Eqs. 14, 15: For cdf $F_t^{\theta}$ and pdf $f_t^{\theta}$ - missed conditioning $\vert x_{1:i-1}$. So does for eqs. (19) and (20), (21), (22), (23), (25).
2. Eq. (22) - $\frac{\partial}{d \partial}$.

**Comments**

1. You state that your work stems from the ideas of NCL in [Richter-Powell]. However, in the manuscript, there are no comparison between the constructions proposed in your work and in [Richter-Powell]. It would be great to have such a comparison, especially how do all these diff forms in [Richter-Powell] relate to your much simpler construction.
2. I think, lemma 2 holds only for $x_i = x_D$ ($i = D$), and other coordinates of $x$ being within support of $\rho_t$ (otherwise, right-hand side of eq. (20) would be zero).
3. Lemma 3, while explained intuitively, should have rigorous proof (e.g., in appendix)
4. Section 3.7. It is bad to call your newly introduced learned divergence-free vector field to be $f_t^{\theta}$. Because $f_t^{\theta}$ is already reserved for density in the previous text.

### Questions
1. Lines 037 - 038. “[...]but these methods all require simulating from the learned diffusion process to some varying degrees [Peyre&Cuturi]” - what do you mean by citing this work here?
2. A general question, eq. 12. The choice for $a_t^{\theta}$ looks a bit strange - it is kind of “not symmetric”, not “invariant” under the coordinates of the vector - because it “respects” only the last coordinate. Why do you consider exactly this “not-symmetric” parameterization? (I understand that formally this is correct)
3. I do not completely understand the second row of Figure 1. As I understand, black arrows on the canvases denote fluxes $j_t$. But following the definition of $a_t^{\theta}$, eq. 12 all these arrows should be directed along one axis (i.e., they should be parallel to unit vector $(0, \dots, 0, 1)$). But it seems that the actual arrows in Figure 1 may be directed along *two* axis.
4. Lines 297-298. Something strange, may be an inaccurate denotations' intersection: you add a quantity with $\Pi_{i = 1}^{D - 1}$ to the $i$-th coordinate. The same index $i$. Given my comment 2, may be $i$ should be equal to $D$? The same problem seems to affect eqs. 21, 22, 23 (it seems that somewhere $x_i$ should be substituted with $x_D$).
5. Lines 299  - 300. Do not understand the comment that $\sigma$ could be substituted with “function/NN whose first derivative has compact support. I think - for such an NN  there should be a condition, that at $x_D \rightarrow \infty$ this NN should approach $1$.
6. Results in Table 1. For CNF, you grab the results only for “time-varying CNF”. The other variants of CNF, e.g., jump CNF and attentive CNF are excluded from the comparison (and, by the way, achieve better NLL). Why?
7. Lines 468 - 475. I do not understand, how you achieve kinetic optimality (for AR model). Ok, you have an additional term introduced in Section 3.7 - but it is just improves expressivity and does not lead to kinetic optimality out of the box (as I understand)
8. Results in Figure 2. What is the reason of the “explosion” of particles at the final time points in the first column of the Figure?

**Misprints**

1. Eqs. 14, 15: For cdf $F_t^{\theta}$ and pdf $f_t^{\theta}$ - missed conditioning $\vert x_{1:i-1}$. So does for eqs. (19) and (20), (21), (22), (23), (25).
2. Eq. (22) - $\frac{\partial}{d \partial}$.

**Comments**

1. You state that your work stems from the ideas of NCL in [Richter-Powell]. However, in the manuscript, there are no comparison between the constructions proposed in your work and in [Richter-Powell]. It would be great to have such a comparison, especially how do all these diff forms in [Richter-Powell] relate to your much simpler construction.
2. I think, lemma 2 holds only for $x_i = x_D$ ($i = D$), and other coordinates of $x$ being within support of $\rho_t$ (otherwise, right-hand side of eq. (20) would be zero).
3. Lemma 3, while explained intuitively, should have rigorous proof (e.g., in appendix)
4. Section 3.7. It is bad to call your newly introduced learned divergence-free vector field to be $f_t^{\theta}$. Because $f_t^{\theta}$ is already reserved for density in the previous text.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper introduces a method to train a diffusion process that satisfies the Fokker-Planck equation along with a "sum-to-1" density constraint, transforming this constrained optimization problem into an unconstrained one through reparameterization. This approach can cause the spurious flux phenomenon, which can be mitigated by a careful choice of parameters in the reparameterized process.

### Strengths
* The idea of converting the constrained problem into an unconstrained one is nice.
* The method is also theoretically justified, although I have not fully checked the math.
* The proposed approach is "simulation-free", which I think should translate to better cost-accuracy tradeoff.

### Weaknesses
### Major
* The method claims scalability (i.e. better cost-accuracy trade-off) as a primary benefit, yet there is no such comparison (experimental or otherwise). A comparison of the wall-clock time or FLOPS will be good. Furthermore, a detailed breakdown of the computational cost, including forward and backward passes, would be beneficial to understand the method's efficiency.
* While this is the first simulation-free approach to address Section 4.3, is there a non-simulation-free baseline to check the quality of the solution? It's crucial to understand how the proposed method compares to alternative approaches, even if they are not directly simulation-free, to assess its performance.
* Justifications for Lemma 3 and Theorem 1 are missing. Remarks on Proposition 1 would be helpful, although this might be trivial for experts in this area. The lack of detailed proofs or at least a sketch of the proof makes it difficult to assess the validity of the theoretical claims. Specifically, the assumptions and conditions under which these results hold need to be clearly stated.
### Minor
* Missing standard errors for baselines in Tables 1 & 2. The absence of standard errors makes it difficult to assess the statistical significance of the results and compare the performance of different methods.
* Detailed hyperparameters would support reproducibility. The lack of specific hyperparameter values used in the experiments makes it hard to reproduce the results and evaluate the method's sensitivity to these parameters.
* Minor typos and grammar errors (e.g., line 228 "functions dependent on $t$").

### Questions
* How is "negative log-likelihood" defined in Table 1? Is it (33)?
* Are there any recent baselines for the setup in Section 4.1?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The manuscript introduces a simulation free approach for the training of diffusion processes. This is achieved by an ansatz the exactly satisfies the Fokker-Planck equation -- which circumvents costly simulation for its solution. The approach is motivated by Neural Conservation Laws. The authors then numerically demonstrate their method.

Disclaimer: The paper is somewhat outside of my comfort zone, so my judgment is to be taken with a grain of salt.

### Strengths
- Hard-coding PDEs or PDE terms often outperforms soft penalties (as would be prevalent in physics-informed neural networks). Constructing an ansatz that does this for a Fokker-Planck equation is thus quite interesting.

- The paper is well-written and more or less understandable, even for me as a reader outside of the field.

### Weaknesses
 - I am unfortunately not very familiar with the challenges or difficulties of the field, so I will pose questions rather than pointing out weaknesses.

 - Universality of the ansatz: In equations (1)-(3) the authors are interested in finding the optimal $u$ and $\rho$ subject to the Fokker-Planck equation. To avoid the solution of the Fokker-Planck equation, both $u$ and $\rho$ are parametrized in terms of a vector field $a_\theta$ (and also $b_\theta$). Can the authors comment on the universality of that construction? Will every pair $(u, \rho)$ be asymptotically realizable? If no, which pairs can be reached and which cannot? This can be a potential problem for the proposed method if the minimizers of problem (1)-(3) are not well representable.  The parameterization of both $u$ and $\rho$ through $a_\theta$ and $b_\theta$ might impose a restrictive structure on the solution space. Specifically, while the authors aim to satisfy the Fokker-Planck equation exactly through their ansatz, the chosen parameterization might limit the achievable solutions to a subset of all possible solutions. It is not clear if this subset is sufficiently rich to capture the desired dynamics for all practical cases. For example, if the true underlying dynamics require a velocity field with specific complex spatial dependencies not easily captured by the chosen parameterization, the method might struggle to converge to an accurate solution. A more detailed analysis of the limitations of the ansatz is needed. 

Minor Questions/Typos:

- Line 131 The flux $j_t$ should be time dependent, hence map $\mathbb R^{1+D} \to \mathbb R^D$, correct?

### Questions
- Universality of the ansatz: In equations (1)-(3) the authors are interested in finding the optimal $u$ and $\rho$ subject to the Fokker-Planck equation. To avoid the solution of the Fokker-Planck equation, both $u$ and $\rho$ are parametrized in terms of a vector field $a_\theta$ (and also $b_\theta$). Can the authors comment on the universality of that construction? Will every pair $(u, \rho)$ be asymptotically realizable? If no, which pairs can be reached and which cannot? This can be a potential problem for the proposed method if the minimizers of problem (1)-(3) are not well representable.  

Minor Questions/Typos:

- Line 131 The flux $j_t$ should be time dependent, hence map $\mathbb R^{1+D} \to \mathbb R^D$, correct?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a novel framework for the simulation-free training continuous-time diffusion processes in a general setting. This is achieved by a coupled parameterization that jointly models the *density* path $\rho_t$  and associated *dynamics* $u_t$ (vector field). The authors achieve this by enforcing the Fokker-Plank (FP) equation as a hard constraint for a very general objective function.  The  FP equation ensures that $dX_t =u_t(x_t)dt + g_tdW_t$ has marginally density $X_t\sim p_t$. Enforcing these constraints hardly allows the application standard unconstrained optimization. The authors test the proposed method on a set of tasks, including: density estimation, optimal transport, and mean-field optimal control.

### Strengths
1. **Novelty**: The paper presents an interesting method that, to my knowledge, is novel. 
2. **Clarity**: The paper is generally well-organized, with a logical progression from theoretical developments to practical implementation. It elaborates on design choices made by the authors, its implications and how to adress potential problems (i.e., spurious flux).
3. **Generality**: The paper demonstrates that the method can be applied to various problem settings. The authors show that the method can achieve state-of-the-art results on some (lower-dimensional!) spatio-temporal generative modeling data sets and on learning transport maps in cellular dynamics.

### Weaknesses
1. **Scalability**: While promising in low-dimensional settings, the authors acknowledge limitations in scaling this methodology to higher dimensions "due to its reliance on likelihood-based models" and leave it to future work. Yet many other likelihood-based generative models (discrete normalizing flows, autoregressive models (transformer, RNN), etc.) are scalable to (moderately) high dimensions. The core issue is that the proposed method relies on an autoregressive model to parameterize the density, which is known to suffer from slow sampling and high computational costs as dimensionality increases. This is not just a matter of engineering effort, but a fundamental limitation of the approach. The paper would significantly benefit from a more thorough investigation into the scalability bottlenecks, and at least a demonstration that the proposed method can scale to standard generative modeling tasks such as MNIST or CIFAR, even if the results are not state-of-the-art. The current experiments do not provide sufficient evidence that the method can be practically applied to real-world high-dimensional problems.

### Questions
Can the authors provide a demonstration of scalability (see Weakness)?

### Soundness
3

### Presentation
3

### Contribution
3

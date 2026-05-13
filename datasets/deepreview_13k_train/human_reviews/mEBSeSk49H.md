# On the Convergence of Adam under Non-uniform Smoothness: Separability from SGDM and Beyond

- Decision: Reject
- Scores: 5, 8, 3, 1

## Abstract
This paper aims to clearly distinguish between Stochastic Gradient Descent with Momentum (SGDM) and Adam in terms of their convergence rates. We demonstrate that Adam achieves a faster convergence compared to SGDM under the condition of non-uniformly bounded smoothness. Our findings reveal that: (1) in deterministic environments, Adam can attain the known lower bound for the convergence rate of deterministic first-order optimizers, whereas the convergence rate of Gradient Descent with Momentum (GDM) has higher order dependence on the initial function value; (2) in stochastic setting, Adam's convergence rate upper bound matches the lower bounds of stochastic first-order optimizers, considering both the initial function value and the final error, whereas there are instances where SGDM fails to converge with any learning rate. These insights distinctly differentiate Adam and SGDM regarding their convergence rates. Additionally, by introducing a novel stopping-time based technique, we further prove that if we consider the minimum gradient norm during iterations, the corresponding convergence rate can match the lower bounds across all problem hyperparameters. The technique  can also help proving that Adam with a specific hyperparameter scheduler is parameter-agnostic, which hence can be of independent interest.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper provides a comparative analysis of Stochastic Gradient Descent with Momentum (SGDM) and simplified Adam (considering the same step-size for each coordinate and ignoring the corrective terms), focusing on their convergence rates under varying conditions. The authors argue that the variant of Adam converges faster than SGDM when dealing with non-uniformly bounded smoothness. 

In the deterministic environments, the authors claim that simplified Adam can reach the optimal convergence rate for deterministic first-order methods, while SGDM shows a higher dependence on the initial function value, suggesting a slower convergence rate.

In the stochastic setting: the authors claim that simplified Adam's convergence rate upper bound is shown to align with the theoretical lower bounds for stochastic first-order methods, considering both the initial function value and final error. The authors highlight that SGDM can sometimes fail to converge, regardless of the learning rate, under certain conditions.

The paper use a stopping-time-based technique, enabling analysis of the minimum gradient norm over iterations. This method demonstrates that simplified Adam’s convergence rate can match lower bounds.

### Strengths
The article establishes convergence theory for Stochastic Gradient Descent with Momentum (SGDM) and simplified Adam. 
The comparsion of the convergence theory between SGDM with simplified Adam could be interesting from some certain points of view.

### Weaknesses
1. The proof of Theorem 3 in Appendix C.1 appears to be **NOT complete**. Specifically, in deriving an upper bound for Adam in terms of the average gradient norm, the first-order term $\mathbb{E}^{\vert \mathcal{F}_t}[\langle\nabla f(w_t),u_{t+1}-u_t\rangle]$ is decomposed into three components as shown in equation (7). However, referring to equation (8), the combination of inequalities (11) and (12) provides an upper bound only for the second term on the RHS of equation (7). Then, the RHS of inequality (13) provides an upper bound only for the sum of the first two terms, neglecting the third term on the RHS of equation (7). Thus, the proof lacks justification for establishing an upper bound on the third term. 

2.  Some statements in the paper are not consistent. The consistency of the statements is critical for a theoretical paper. For example, the proof of Theorem 3 provided in Appendix C.1 relies on assumptions that $\beta_1 \leq \beta_2$ (line 1390 in page 26), $0\leq \beta_1^2 < \beta_2 < 1$ (requirement of Lemma 1), $\beta_2 \geq \frac{1}{2}$ and $1-\beta_2\leq \frac{1-\beta_1}{1024\sigma_1^2}$ (line 1416 in page 27), which are not captured in the corresponding formal statement. Similarly, the formal statement of Theorem 5 omits assumptions that $\beta_1 \leq \beta_2$ and $0\leq \beta_1^2 < \beta_2 < 1$ (see Theorem 11 in Appendix D.1). 

3. The convergence results for Adam presented in Theorem 3 and Theorem 5 stipulate "a proper choice of learning rate $\eta$ and momentum hyperparameter $\beta_2$". However, as shown in the corresponding formal statements in Appendix C.1 (Theorem 9) and Appendix D.1 (Theorem 11), deriving these results necessitates tuning $\eta$ and $\beta_2$ with prior knowledge of the non-uniformly bounded smoothness parameters $(L_0,L_1)$ and affine noise variance parameters $(\sigma_0,\sigma_1)$. Since these parameters may be unknown or difficult to estimate in realistic situations, the practical utility of the derived results is questionable as their conditions on hyperparameters would be challenging to satisfy. 

4. There is a lack of clarity around the focused version of Adam. Two different versions are assumed in this paper: the coordinate-wise version and the norm version. While Algorithm 1 introduced in the main text is the coordinate-wise Adam, it is not until Appendix B that the authors first state that all the subsequent theorems apply to the norm version of Adam. Although a footnote in the appendix mentions that an extension to the coordinate-wise version from the norm version is not difficult, more detailed discussions are necessary and helpful. 

5. There are some typos in this paper. Also, the citation format should be carefully checked.

### Questions
see weaknesses

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
2

### Summary
The paper presents a convergence analysis of Adam and SGD with Momentum (SGDM) under the non-uniform (L_0, L_1)-smoothness assumption (where the gradient smoothness depends on the gradient norm itself) and an affine noise assumption on the gradient in the stochastic setting. The authors show that under these assumptions Adam has an upper bound that is better than the lower bound of (S)GDM in both the deterministic and stochastic settings.

In the deterministic setting the authors provide a tighter upper bound for Adam than two cited previous papers and for GDM they re-iterate on a prior known lower bound in more realistic setting (with choosing learning rate after the objective function is known). Based on these two bounds the authors are then able to separate the convergence rates of Adam and GDM showing that Adam is superior in the deterministic setting.

The authors then move on to extend their analysis to the stochastic setting where they claim that their new Adam upper bound extends prior convergence results of Adam and clipped SGDM with their new Adam bound giving the best upper bound achieved under the assumptions made in the paper so far. For the lower bound of SGDM the authors provide a bound that is tighter than the prior results from the literature to be able to separate the Adam and SGDM bounds.

In the final sections the authors discuss what happens when the “regularizing” constant lambda is used and introduce a stopping-time analysis under which they discuss how Adam can actually achieve the optimal lower bound rate.

### Strengths
* Paper is clearly structured, moving from motivations to assumptions, to the simpler determinstic setting to the more complex stochastic section.
* Paper provides clear exposition and arguments for the practical relevance of the non-uniform smoothness assumptions they use.
* Paper provides the intuition behind the different convergence behaviors e.g. explaining the behavior of the adaptive conditioner used in AdaGrad or GDM’s inability to manage varying degrees of sharpness in the loss function.
* Authors explain the limitations of a previous derivation of the lower bound of determinstic GD in the literature and use this to motivate their lower bound formulation that allows adjusted hyperparams (learning rate) after the objective function has been selected but arrives at the same bound and is taking into account momentum.
* For their Adam upper bound in the stochastic case they provide a high level summary of the additional challenges addressed compare to an analysis of Adam under L-smooth condition from the literature.

### Weaknesses
Overall, the paper brings no substantial contribution compared to the literature.


- The convergence rates use classical and elementary tools (smoothness inequalities, stopping time in the stochastic setting) that already exist in the literature. For instance, similar convergence rates were established in Li et al., 2023a. The authors highlight some differences (section 4.1) with the related works but the arguments seem wrong or irrelevant.

- Some mathematical parts are wrong. For instance, the authors consider the regularization parameter $\lambda$ to be zero but this leads to divisions by zero in the proofs (see for instance line 857) with no further assumption.

- The lower bounds are based on trivial and degenerate situations, especially in the stochastic setting. The lower bound function (Theorem 10 in Appendix) is based on a gradient noise which image by the gradient is not integrable, thus leading to a vacuous bound (all expectations become infinite). For instance, it does not depend on the smoothness parameters, which was the motivation stated in the introduction. Exhibiting the lower bounding function in the main text would make the presentation more honest and transparent. Lower bounds found in the literature are based on constructions that are much more sophisticated because they exhibit more restrictive properties (stability, gradient boundedness, etc.); see, for instance, Carmon et al., Arjevani et al.

### Questions
How does this paper relate to the following prior work which also analyzes Adam and SGD(M) under non-uniform smoothness:
```@inproceedings{wang2024provable,
  title={Provable adaptivity of adam under non-uniform smoothness},
  author={Wang, Bohan and Zhang, Yushun and Zhang, Huishuai and Meng, Qi and Sun, Ruoyu and Ma, Zhi-Ming and Liu, Tie-Yan and Luo, Zhi-Quan and Chen, Wei},
  booktitle={Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining},
  pages={2960--2969},
  year={2024}
}
```

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper aims to theoretically compare the convergence rates of Adam and Stochastic Gradient Descent with Momentum (SGDM) to explore the superior empirical performance of Adam over SGDM. Specifically, it separates Adam and SGDM regarding the convergence rate under $(L_0,L_1)$-smooth condition in both deterministic and stochastic settings. One interesting point in this paper is that the authors used a novel stopping time technique to show Adam's convergence rate in terms of the minimum gradient norm matching the lower bound for first-order stochastic optimizers, considering all problem hyperparameters. With the aid of this technique, the authors show that Adam with a specific parameter scheduler is parameter-agnostic.

### Strengths
1. This work analyzes Adam's convergence rate under mild assumptions. Specifically, the convergence results are established under the $(L_0,L_1)$-smooth condition and affine noise variance assumption, relaxing the commonly used $L$-smooth condition and bounded variance assumption in prior studies. 
   
2. The obtained upper bound on the convergence rate of Adam is tighter than those given in prior studies and matches the lower bound of first-order optimizers in both deterministic and stocahstic settings. 

3. A novel stopping time technique is developed. Based on this technique, it is demonstrated in Theorem 12 that Adam with some **specific parameter scheduler** is parameter-agnostic.

### Weaknesses
1. The proof of Theorem 3 in Appendix C.1 appears to be **NOT complete**. Specifically, in deriving an upper bound for Adam in terms of the average gradient norm, the first-order term $\mathbb{E}^{\vert \mathcal{F}_t}[\langle\nabla f(w_t),u_{t+1}-u_t\rangle]$ is decomposed into three components as shown in equation (7). However, referring to equation (8), the combination of inequalities (11) and (12) provides an upper bound only for the second term on the RHS of equation (7). Then, the RHS of inequality (13) provides an upper bound only for the sum of the first two terms, neglecting the third term on the RHS of equation (7). Thus, the proof lacks justification for establishing an upper bound on the third term. 

2.  Some statements in the paper are not consistent. The consistency of the statements is critical for a theoretical paper. For example, the proof of Theorem 3 provided in Appendix C.1 relies on assumptions that $\beta_1 \leq \beta_2$ (line 1390 in page 26), $0\leq \beta_1^2 < \beta_2 < 1$ (requirement of Lemma 1), $\beta_2 \geq \frac{1}{2}$ and $1-\beta_2\leq \frac{1-\beta_1}{1024\sigma_1^2}$ (line 1416 in page 27), which are not captured in the corresponding formal statement. Similarly, the formal statement of Theorem 5 omits assumptions that $\beta_1 \leq \beta_2$ and $0\leq \beta_1^2 < \beta_2 < 1$ (see Theorem 11 in Appendix D.1). 

3. The convergence results for Adam presented in Theorem 3 and Theorem 5 stipulate "a proper choice of learning rate $\eta$ and momentum hyperparameter $\beta_2$". However, as shown in the corresponding formal statements in Appendix C.1 (Theorem 9) and Appendix D.1 (Theorem 11), deriving these results necessitates tuning $\eta$ and $\beta_2$ with prior knowledge of the non-uniformly bounded smoothness parameters $(L_0,L_1)$ and affine noise variance parameters $(\sigma_0,\sigma_1)$. Since these parameters may be unknown or difficult to estimate in realistic situations, the practical utility of the derived results is questionable as their conditions on hyperparameters would be challenging to satisfy. 

4. There is a lack of clarity around the focused version of Adam. Two different versions are assumed in this paper: the coordinate-wise version and the norm version. While Algorithm 1 introduced in the main text is the coordinate-wise Adam, it is not until Appendix B that the authors first state that all the subsequent theorems apply to the norm version of Adam. Although a footnote in the appendix mentions that an extension to the coordinate-wise version from the norm version is not difficult, more detailed discussions are necessary and helpful. 

5. There are some typos in this paper. Also, the citation format should be carefully checked.

Overall, I found this paper made some interesting theoretical comparisons between Adam and SGDM. But the rigorous proofs and statements are the key to a theoretical paper. **My current rating of this paper is under the assumption that the first point above can be fully addressed**.

### Questions
The main concerns from my perspective for this paper have been listed in the **Weakness** part. Below are some more related questions that need to be addressed:

1. How to ensure that the choice of $\beta_2$ provided in Theorem 9 satisfies all the assumptions ($\beta_1 \leq \beta_2$, $0\leq \beta_1^2 < \beta_2 < 1$, $\beta_2 \geq \frac{1}{2}$ and $1-\beta_2\leq \frac{1-\beta_1}{1024\sigma_1^2}$) required in the derivation of this result? 

2.  How to ensure that the choice of $\beta_2$ provided in Theorem 11 satisfies all the assumptions ($\beta_1 \leq \beta_2$ and $0\leq \beta_1^2 < \beta_2 < 1$) required in the derivation of this result? If such a choice of $\beta_2$ exists, can we guarantee that inequality $\frac{\eta}{\sqrt{1-\beta_2}}\leq \frac{1-\beta_1}{128L_1\sigma_1}$ given on page 39 hold true? 

3. Could you please give more details on the choice of $\beta_2$ and the derivation of the inequality $\Vert w_{t+1} - w_t\Vert \leq \frac{1}{\sqrt[4]{t}}$ in the case where $t\geq \left(\frac{128\sigma_1 L_1}{1-\beta_1}\right)^4$?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
ADAM and momentum based stochastic gradient algorithms are popular optimization methods used in deep learning. Classical analyses of such methods rely on a globally Lipschitz gradient assumption (L-smoothness). Yet   this condition is not satisfied in practical situations. This paper studies stochastic gradient method with momentum and ADAM algorithm under "$L_0, L_1$ smoothness", where compared L-smoothness, the Lipschitz constant of the gradient depends on the gradient norm (hence allowing for non Lipschitz gradients). This follows many works dealing with relaxed smoothness conditions.

The authors provide convergence rates in (expected) best iterate, or averaged gradient norms. They also provide lower bounds by exhibiting one dimensional functions attaining the guarantees.

### Strengths
L0,L1 smoothness assumptions are interesting to consider as they better coincide with deep learning situations.

### Weaknesses
Overall, the paper brings no substantial contribution compared to the literature.


- The convergence rates use classical and elementary tools (smoothness inequalities, stopping time in the stochastic setting) that already exist in the literature. For instance, similar convergence rates were established in Li et al., 2023a. The authors highlight some differences (section 4.1) with the related works but the arguments seem wrong or irrelevant.

- Some mathematical parts are wrong. For instance, the authors consider the regularization parameter $\lambda$ to be zero but this leads to divisions by zero in the proofs (see for instance line 857) with no further assumption.

- The lower bounds are based on trivial and degenerate situations, especially in the stochastic setting. The lower bound function (Theorem 10 in Appendix) is based on a gradient noise which image by the gradient is not integrable, thus leading to a vacuous bound (all expectations become infinite). For instance, it does not depend on the smoothness parameters, which was the motivation stated in the introduction. Exhibiting the lower bounding function in the main text would make the presentation more honest and transparent. Lower bounds found in the literature are based on constructions that are much more sophisticated because they exhibit more restrictive properties (stability, gradient boundedness, etc.); see, for instance, Carmon et al., Arjevani et al.

### Questions
- Remove the blue color in theorems.
- Define the sequence $\( w_t \)$ in Theorems 3, 4, 5. Also, add a proper name for each theorem to understand which algorithm each result deals with.
- The appendix needs a thorough re-reading; for instance, look at line 2015: "Also, as  $\tau$  is a bounding stopping theorem, by optional stopping time, we obtain ..."
- Writing literature reviews in the appendix in the middle of the proof makes the reading inefficient.
- Line 465: the quantifier $\forall$ looks weird this way. I suggest writing "for all."
- Throughout the paper, rewrite the left quotation mark in the correct direction.
- Avoid cumbersome expressions such as "to the best of our knowledge," "for the first time" (used many times on page 7).

### Soundness
2

### Presentation
1

### Contribution
1

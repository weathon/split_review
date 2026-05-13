# RESuM: A Rare Event Surrogate Model for  Physics Detector Design

- Decision: Accept
- Avg Score: 7.40
- Scores: 8, 10, 8, 5, 6

## Abstract
The experimental discovery of neutrinoless double-beta decay (NLDBD) would answer one of the most important questions in physics: Why is there more matter than antimatter in our universe? To maximize the chances of detection, NLDBD experiments must optimize their detector designs to minimize the probability of background events contaminating the detector. Given that this probability is inherently low, design optimization either requires extremely costly simulations to generate sufficient background counts or contending with significant variance. In this work, we formalize this dilemma as a Rare Event Design (RED) problem: identifying optimal design parameters when the design metric to be minimized is inherently small. We then designed the Rare Event Surrogate Model (RESuM) for physics detector design optimization under RED conditions. RESuM uses a pretrained Conditional Neural Process (CNP) model to incorporate additional prior knowledges into a Multi-Fidelity Gaussian Process model. We applied RESuM to optimize neutron moderator designs for the LEGEND NLDBD experiment, identifying an optimal design that reduces neutron background by ($66.5\pm3.5$)\% while using only 3.3\% of the computational resources compared to traditional methods. Given the prevalence of RED problems in other fields of physical sciences, the RESuM algorithm has broad potential for simulation-intensive applications.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents a surrogate model for rare events in physics.  The model is a hybrid model combining a conditional neural process (CNP) model and a multi-fidelity Gaussian process (MFGP).  The CNP is pre-trained on both low-fidelity (LF) and high-fidelity (HF) simulation data.  Subsequently the CNP model is used to calculate additional design data (averaged CNP scores for LF and HF data).  The MFGP model is initially trained using HF, HF CNP and LF CNP data, and further tuned using Bayesian Optimization (BO) equipped with the integrated variance reduction acquisition function to minimize the total variance of the model.

### Strengths
The RESuM model is well-motivated and the application in physics is quite interesting.  While I am not a statistician nor familiar with the CNP model, I am very familiar with GP models and BO design, and can see no obvious mistakes in the paper.  Moreover the results are thorough and I can see a clear application for this model outside of that considered here.

### Weaknesses
It appears that the real goal of this paper is to optimise particle detector design.  As such, it strikes me that the surrogate model need only be accurate in those regions of design space that are "good" - ie minimise background noise.  However the RESuM model is designed to model the entire design space, including "bad" designs (eg it may request HF simulations for regions whose prior confidence bounds are such that we know whp will not be appropriate in practice).

As such perhaps a more efficient approach would be to replace the integrated variance reduction acquisition function used in the BO portion of the design with a more goal-oriented acquisition function like expected improvement (EI) or GP-UCB, which would naturally focus computational effort on optimizing the detector design (ie the real underlying goal) rather than modeling all possible detectors (essentially the first step in the current design procedure).

(Note I intend this more as a point for discussion rather than a major criticism - the current approach is valid, but perhaps the strong focus on modeling is obscuring the real goal).

### Questions
In addition to the above:

- I am a little unclear regarding the role of CNP here.  Is it primarily a means to include the LF simulations in the overall model in a way that takes advantage of the physical insight in the combined LF/HF data?
- in the active learning / Bayesian optimization phase you only run HF simulations.  Have you considered using multi-fidelity BO [1,2] to take advantage of the cheaper LF simulations as well?
- As a minor note, on line 53 you say that N is $\mathcal{O} (10^4)$.  Do you mean $N$ is of order $10^4$?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
10

### Rating Number
10

### Confidence
5

### Summary
The article presents a study on the optimal design of a neutrinoless double-beta decay detector, a Rare Event Design. The authors introduce a surrogate model, RESuM, to solve this optimization problem and gain computational cost. This algorithm is based on Conditional Neural Process, incorporating prior information. The authors applied their work to the LEGEND experiment, a physics detector for neutrinoless double-beta decay.

The Rare event Design problem is mainly well stated and very clear.  The Large and Small N scenarios provide a very good understanding of the problem.

Bayesian prior knowledge with Conditional Neural Process (CNP) is clear in the text. CNP is explained in Appendix 11. The details shows the CNP is rich : by the use of surrogate modelling it generates data as fast simulator. It is more efficient for exploration of parameter space, uncertainty quantification and model validation.

The simulations, results and validation of RESuM are well explained.

RESuM reduces LEGEND neutron background by (66.5 \pm 3.5)% using only 3.3% of the computational power of traditional methods. This is a very good achievement.

All in all, this is a very good paper.

### Strengths
The study is well conducted, very clear and concise, very interesting. The stated results are also very impressive and I hope this will lead to a larger breakthrough regarding neutrinoless double-beta decay community. The code is well presented and commented.

The work can be applied to Astronomy or Material Science. There are many other application possibilities in physics.

The work is motivated by the experimental discovery of neutrinoless double-beta decay (NLDBD), leading to answering the question ‘Why is there more matter than antimatter in our universe?’. Which makes a link with one of the opening questions of Javier Duarte talks at ICML24 ‘What is our universe made of?'. Thus, this work is very relevant for the community, and source of enthusiasm since the potential discovery of NLDBD would  lead to a Nobel-Prize-level breakthrough in physics.

### Weaknesses
The authors indicates in the limitations and applications part that due to limitation of ressources available they computed only 100 High Fidelity simulation, maybe the publication of the article will help to convince to gain more ressources.

The authors also add that the active learning functions used un RESuM are simplistic, they will consider more sophisticated one in future work.

Minor comments that do not impact the score :

They are many inconsistencies in the notations, here are what I noted while reading, some might be redundant

Line 95, independent of the other events

Line 97, \mathbf{Phi} is not defined. Is it for conciseness?

Line 97,  dollar i dollar-th

Line 133, dollar { y \in  blablabla } dollar should make it appear on the same line

Line 153-154, Why highlight +1 and +0? Should be in dollar 1 dollar, same for dollar 0 dollar

Line 186, \mathbf{\phi}

Line 187, the same

Line 188,  \mathbf for theta

Line 172, The use of the nuisance parameters is unclear to me. The vertical bar followed by X_ki, phi_ki, theta_k means conditionally, if possible this should be improved.

Line 183, Figure 1 title is ‘Overview of the RESuM framework’ which is not the case of Figure 3. I assume the authors mean Figure 1 then.

In Figure 1, if the MFGP combines prediction from LF and HF simulations, why are the arrows pointing at them and not starting from them?

In the section 3, the vector of design parameters is \mathbf{\theta} thus it should be the same in all the study.

In the introduction, line 49, 51, 52. According to section 4 it should be in \mathbf?

In the section 3,

Line 92-93, is it in \mathbf?

Line 96, in \mathbf

Line 108-109, the same

Line 113-114, the same for \theta and \phi

Line 120,  the same for \theta, N should be in  dollar N dollar

Line 124-125, the same for \theta

Line 126, the same for \theta twice in the eq

Line 126-127, \infty should be used and same for \theta

In the section 4,

Line 140, mathbf for \theta

Line 151, the same for \theta_k the k-th simulation trial

Line 152, the same for \theta_k and \phi_ki

Line 153, it should be  dollar N dollar,  dollar y dollar also

Line 160-161, \mathbf for \theta_k and \phi_ki

Line 187-188, \mathbf for \phi and \theta

Line 204, the same for \theta

Line 209, the same for \theta_k and \phi_ki

Line 212-213, the same for \theta and \phi_ki

In the section 5,

Line 261-263, the parameters of design should be the same as in the figure 2 (\varphi in particular). Figure 2 represents explicitly 4 parameters, n is missing

Line 265, \mathbf for the design parameters and the corresponding space

Line 289-290, \mathbf for \phi

Line 298, the same for \phi

Line 360, I suggest ‘plotted against the five parameters in Fig3.’ Since you only present five.

Line 370-371, the same for \theta

Line 395-400, parameters should be consistent with line 261-263

Line 404-405, parameters should be consistent with line 261-263

Line 409, also

Figure 4 and Table 1, should be consistent with line 261-263

Line 441-446, the same for \theta and the corresponding space

In section 6,

Line 491 and 492, the same for \theta and \phi

In section 2,

Line 93-93, I would have introduced the stochastic process X_1, …, X_N and specify after that

Line 213, \mathbf for theta and phi

Line 222, ^{HF} is necessary for y_CNP

Line 224, ^{LF} is necessary for y_CNP

In the supplementary materials

Line 738, \mathcal{L}_k appears two times

A.9 must be improved:

Are \theta and \theta’ vectors as in the manuscript?

What kind of matrix is K? What are K_LL, K_\delta?

Could you give a reference or improve the theory, please?

A.10 \Theta must be in bold

Is \theta a scalar or a vector?

Could you give a ref or a proof for the approximation of I(\theta) for GP model? It seems simple, but I would like to be convinced this is right.

### Questions
Line 53, this is interesting, where does this order of magnitude 'N needs to be extremely large (O(10^4))'come from? Could you give a quick explanation or a reference, please?

In part 5.0.2. why are relationship dependencies clear for R and N and not for the thickness and the angle? What does this implies on the model's interpretation or performance?

Line 171, the nuisance parameters are introduced quickly. Can you provide a brief explanation and give a reference, please?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper addresses a key question in physics: the matter-antimatter asymmetry in the universe, focusing on neutrinoless double-beta decay (NLDBD). The authors tackle the challenge of optimizing detector designs to minimize background event contamination, framing it as a Rare Event Design (RED) problem.
They introduce the Rare Event Surrogate Model (RESuM), which combines a pre-trained Conditional Neural Process with a Multi-Fidelity Gaussian Process to optimize detector designs. Applied to neutron moderator designs for the LEGEND NLDBD experiment, RESuM achieves a 66.5±3.5% reduction in neutron background while using only 3.3% of the computational resources of traditional methods. This innovative approach has broad implications for similar challenges in physical sciences.

### Strengths
The authors did a great job narrating each step of the procedure and model description. However, since I am not in the field, I got a little lost in the setup of the Experiment section, which involves applications. The results are convincing, though.

### Weaknesses
- It would be better if the authors provided more detailed explanations in the Experiment section.
- Several mathematical symbols are not in math mode.

### Questions
Are there no other works attempting to solve the same problem that we can use to benchmark your work against?

### Soundness
3

### Presentation
2

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
This work presents a generative approach for optimizing physics detector design in rare event scenarios by leveraging a Conditional Neural Process (CNP). By incorporating techniques like simple co-kriging, data augmentation, and multi-fidelity modeling, the authors demonstrate that their surrogate model effectively addresses the computational demands of rare event detection while maintaining the accuracy.

### Strengths
The authors provide a solid background introduction to the NLDBD problem and offer clear, detailed explanations of the technical methods used in this work, including co-kriging and Conditional Neural Processes (CNP), in the appendix.

### Weaknesses
Some of the critical weaknesses:

- While the authors provide a solid introduction to NLDBD and its motivation, the paper lacks a literature review on rare event simulation/modeling. Rare event simulation is a well-established field in engineering, including techniques such as the first/second-order reliability methods (FORM/SORM) [1, 2, 3], polynomial-based surrogate modeling [4, 5], adaptive and sequential importance sampling [6, 7], and ensemble Kalman filters [8]. These approaches have also been extended to multi-fidelity settings, as seen in [9, 10, 11]. Although it’s not necessary to cite all related works, the authors should clarify why they focus on deep generative modeling, highlighting its advantages over traditional models. Specifically, the paper should address how the proposed method compares to established techniques in terms of computational efficiency, accuracy, and applicability to the specific challenges of rare event simulation, such as the need for efficient exploration of the design space and accurate estimation of small probabilities. The current lack of discussion makes it difficult to assess the novelty and practical value of the proposed approach.

- The computational results of the proposed method appear to lack a baseline, making it challenging to assess performance without a fair comparison. The absence of a baseline, such as a standard Monte Carlo simulation or a method from the rare event simulation literature, makes it impossible to determine whether the proposed method offers any improvement in terms of accuracy or computational cost. The authors should include a comparison with at least one established method to demonstrate the effectiveness of their approach.

- Some notations are not statistically rigorous. Specific comments on notations are provided in the questions section. Also, the variables $\phi$ and $\theta$ are inconsistently bolded, which can cause confusion. For instance, the use of $t(\theta_k, \phi_{ki})$ and $X_{ki}$ without clear distinction is problematic. The authors should clarify the relationship between these notations and ensure that all variables are defined consistently throughout the paper. Furthermore, the inconsistent bolding of $\phi$ and $\theta$ introduces ambiguity and should be standardized to maintain clarity and rigor.

### Questions
- This works uses CNP as the major tool for rare event modeling. Is it model originally proposed by the authors? If not, please provide the corresponding citations. Also, please give the motivation here. Why CNP is more advantageous than VAE/GAN in this setting? 

- In line 51, the authors said "If $m_1/N_1 < m_2/N_2$, it suggests that the design $\theta_1$ is better than $\theta_2$." This statement holds only if $N_1, N_2$ are sufficiently large, right? Otherwise, since it is in a rare event scenario, a bad $\theta$ may also lead to zero values when $N$ is not large enough. 

- It looks like $X_{ki}$ is equivalent with $t(\theta_k, \phi_{ki})$, why use two separate notations? Please correct me if I am wrong.

- Formula (4): I don't understand what does Bernoulli($p=t(\theta_k, \phi_{ki})$) mean here. Do you mean Bernoulli($p=\bar{t}(\theta_k)$)? Also, the letter $p$ has been used as density function. 

- The variable $\beta$ is applied in different versions without clear definitions. In line 160, the authors introduce $\beta_{ki}$, while $\beta$ appears in formula (5) without clearly showing its dependency. My guess is that $\beta_{ki} = \beta(\theta_k,\phi_{ki})=\beta\vert\theta_k, \phi_{ki}=\beta$. Please clarify. 

- Line 182, typo: "RESuM as shown in Figure 3." Here it is supposed to be Figure 1.

- Line 230: you don't need to give the fourmulation of the acquisition function, since $\boldsymbol{x}$ is not introduced here.

- Line 299 and line 308: The density $g(\phi)$ for LF and HF models are different, right? If so, please use different notations for them.

- Line 517-520: "Based on the statistical formulation and ... for accelerating simulations. " I don't see the comparison between the proposed method with VAE/GANs, could you please clarify how you draw this conclusion?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper introduces RESuM (Rare Event Surrogate Model), designed to optimize physics detector design, specifically for reducing background events in neutrinoless double-beta decay (NLDBD) detection. The authors frame the challenge as a Rare Event Design (RED) problem, where background events are so rare that traditional simulation methods become computationally prohibitive. RESuM employs a multi-fidelity approach, using a Conditional Neural Process (CNP) model to learn from limited data and a Gaussian Process (GP) model to efficiently explore the design space. The authors apply RESuM to the LEGEND experiment’s neutron moderator design and achieve an  efficient performance.

### Strengths
1. The model targets a critical challenge in physic.
2. The integration of CNP and MFGP is a novel approach for handling rare event problems.
3. The framework’s formulation makes it generalizable to other simulation-heavy domains.

### Weaknesses
I do not find major concerns.
Minor issues:
1. The success of RESuM’s multi-fidelity modeling approach relies on access to both high-fidelity and low-fidelity simulation data. In situations where these data sources are unavailable or highly dissimilar, would the model's effectiveness be reduced?
2. It seems to me that the RESuM does not embed physics constraints or validation check to the model, thus it might be possible that RESuM would suggest some invalid designs. In practice, do we need to first define the valid range of parameters for RESuM? And thus for different application contexts, we need to modify the model accordingly?
3. Section 5 uses subsubsections without subsections.
4. Can RESuM scale to applications with larger or more complex detector designs? How to estimate the relationship between the dimension of design space and model performance? Also, can RESuM incorporate expert knowledge on the design space to make it more efficient?

### Questions
See Weaknesses for questions.

### Soundness
3

### Presentation
3

### Contribution
3

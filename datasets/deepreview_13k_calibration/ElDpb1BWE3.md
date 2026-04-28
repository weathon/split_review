# Compositional Generative Multiphysics and Multi-component Simulation

- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 5, 5, 8, 5, 5

## Abstract
Multiphysics simulation, which models the interactions between multiple physical \revisionp{processes}, and multi-component simulation of complex structures are critical in fields like nuclear and aerospace engineering. Previous studies often rely on numerical solvers or machine learning-based surrogate models to solve or accelerate these simulations. However, multiphysics simulations typically require integrating multiple specialized solvers—each responsible for evolving a specific physical \revisionp{process}—into a coupled program, which introduces significant development challenges.  Furthermore, no universal algorithm exists for multi-component simulations, which adds to the complexity.
Here we propose compositional \underline{Multi}physics and \underline{Multi}-component \underline{Sim}ulation with \underline{Diff}usion models (\model) to overcome these challenges. During diffusion-based training, \model learns energy functions modeling the conditional probability of one physical \revisionp{process}/component conditioned on other \revisionp{processes}/components. In inference, \model generates coupled multiphysics solutions and multi-component structures by sampling from the joint probability distribution, achieved by composing the learned energy functions in a structured way.
We test our method in three tasks. In the reaction-diffusion and nuclear thermal coupling problems, \model successfully predicts the coupling solution using decoupled data, while the surrogate model fails in the more complex second problem. For the thermal and mechanical analysis of the prismatic fuel element, \model trained for single component prediction accurately predicts a larger structure with 64 components, reducing the relative error by 40.3\% compared to the surrogate model.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a data-driven approach for multiphysics and multi-component simulations using compositional generative diffusion models. The proposed method tackles the complexities of coupled simulations by learning energy functions that model conditional probabilities between physical fields and components. The proposed method is validated on 3 tasks, including reaction-diffusion, nuclear thermal coupling, and thermal-mechanical simulations of prismatic fuel elements. The results show improved accuracy and reduced error over traditional surrogate models.

### Strengths
1. The use of compositional generative models for multiphysics and multi-component simulations is a fresh approach in this field, addressing the challenges of coupling multiple physical domains.
2. This paper demonstrates the capability of MultiSimDiff to predict coupled interactions from models trained on decoupled data, simplifying data requirements and model development.

### Weaknesses
1. Only accuracy is compared in the examples. Efficiency comparison is also important. Specifically, a fair comparison with standard numerical methods (such as FEM or FVM) is important.
2. The iterative nature of the diffusion process in MultiSimDiff can be computationally intensive, particularly for multiphysics simulations due to the high complexity. 
3. Since the model is trained on decoupled data, the approach's success may depend on the quality of this initial data. The paper could benefit from further discussion on the robustness of MultiSimDiff when the decoupled data does not closely resemble the coupled dynamics.

### Questions
1. There is only one example for demonstrating training one small structure simulation data and predicting larger structures. Graph Neural Network also has similar abilities. How's the performance comparison?
2. How does MultiSimDiff handle cases where the decoupled training data does not closely match the dynamics of coupled data? Would the model performance degrade significantly?
3. Could you clarify if there are specific scenarios where traditional numerical solvers might still outperform MultiSimDiff in terms of accuracy or computational cost?

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
3

### Summary
The paper proposes a diffusion-based model for simulating multiphysics, multi-component systems. The model learns the conditional distributions of each field/component given the others. During inference, the model iteratively denoises each field/component in a manner similar to diffusion models. The model is applied on reaction-diffusion, nuclear thermal and prismatic fuel element datasets.

### Strengths
The paper is well-written and clear, presenting a novel combination of ideas by proposing to use diffusion models for simulating multiphysics, multi-component systems.

### Weaknesses
 - the main claim of the papers (2) and (3) are questionable. See the below two points
- claim (2): There are several datasets in the literature that can be described as simulations of multiphysics, multi-component, such as PDEBench [Takamoto et al., 2022]. The authors should better precise why the new datasets they propose is a contribution to the literature. Specifically, the distinction between coupled PDEs and multiphysics simulations needs clarification. While the reader might infer the distinction, it should be explicitly stated to better motivate the choice of baselines. The authors should also clarify what constitutes a 'component' in the context of multi-component simulations. The current definition of 'a repeatable basic unit that makes up a complete structure' is insufficient, as it does not specify the nature of these units or their interactions.
- claim (3): More importantly, based on the results, it is difficult to determine whether the proposed method is advantageous for other multiphysics, multi-component systems, given the fact that it may not be competitive in terms of computational cost (see below question)

Minor remarks. 
- l102. "a process we have mathematically proven", I don't think a "process" qualifies as being able to be "mathematically proven". You should precise what is "mathematically proven"
- l107. "This reverse diffusion process is also mathematically validated", same remark
- l137. "there do not exist utilized machine learning methods for multi-component simulation". I don't really understand the novelty since, technically, UNets [Ronneberger et al. 2015], FNO [Li et al. 2022], Transformer [Mccabe et al. 2023], diffusion [Kohl et al. 2024] models are already used on multi-component simulations.
- l251. Paragraph 3.2 is confusing. In particular, there can be confusion between "multiple fields", "multiphysics" and "multi-components". After having read the paper carefully, it seems to me that the main difference between "multiphysics" and "multi-components" is in the way they are treated computationally. The multiple components being treated as interchangeable, in the sense that the same model is used for the conditioning of one on the others, while multiple "physics" do not assume such interchangeability. 
- l253. The paper would benefit greatly by providing at this stage a clear examples of what a "component" is.

### Questions
- You mention several times that the model "learns the energy", as well as the conditional energies, but do you actually learn the energy function E? Or, do you learn the gradient of the energy function (that is the scores, and conditional scores), thanks to the denoiser?
- As your mention, your method seems computationally intensive compared to a FNO for example, not just because of the denoising steps but also because of the loop over the physical fields. Do you have a rough estimation of how it compares in terms of execution time and in terms of FLOPs? 
- In algorithms 1 and 2, could you clarify what the "outer inputs" are in comparison to the "physical fields"?

### Soundness
2

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The author proposed compositional Multiphysics and Multi-component Simulation with Diffusion models (MultiSimDiff) to overcome the diffculty of solving complex systems

### Strengths
The paper is good with the originality and create a novel approach on multiphysics simulation

### Weaknesses
The algorithm lacks clarity, and the model structure is not sufficiently detailed.

The iterative nature of MultiSimDiff, especially in multiphysics simulations, requires multiple diffusion steps for each field, which may lead to slow inference times. This constraint limits its practicality for scenarios requiring rapid predictions. While the authors recognize this issue and propose exploring faster sampling methods in future work, an initial investigation into such techniques within this paper could enhance its contribution.

### Questions
1. For algorithm 1, it is identical to the alogrithm 2 in the DDPM paper [1]. And also the way identify $z_i$ is confusion when apply the third for loop.
2. How time in involved in the alogrithm as you are doing time dependent system




[1] Jonathan Ho, Ajay Jain, and Pieter Abbeel. Denoising diffusion probabilistic models. In
H. Larochelle, M. Ranzato, R. Hadsell, M.F. Balcan, and H. Lin (eds.), Advances in Neural Information Processing Systems, volume 33, pp. 6840–6851. Curran Associates, Inc.,
2020. URL https://proceedings.neurips.cc/paper_files/paper/2020/
file/4c5bcfec8584af0d967f1ab10179ca4b-Paper.pdf.

### Soundness
3

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
4

### Summary
Article summary: This article is about the application of diffusion model in engineering model (mainly thermal and material science). Because engineering problems often involve multiple physical processes (that is, multiple complex processes are involved when modeling), this article establishes a multi-process model to deal with different physical problems. (Mostly reflected in reaction diffusion and nuclear thermal coupling problems)

### Strengths
Advantages:

1. The starting point of this article is very novel, hoping to use limited data to deal with more physical problems at the same time. Especially a mechanical structure and thermal problem, and the performance is very good from the results of the article. (Especially page 18)

2. The adaptability of the ML model to the actual parameters of the engineering problem makes me feel that the design of the entire model is justified, and the motivation is clear and credible. (That is, the content in the appendix, Tables 10-13)

3. Strict model comparison, such as using consistent hyperparameters and settings, and having different parameter designs in different engineering problems (such as porous/multi-part materials).

4. The superiority of the model, from the perspective of energy (density probability form), some of the results obtained are indeed very good

### Weaknesses
Disadvantages:

1. In the comparative experiment, is the surrogate model too simple? Or can you compare your model with a more complex model? Or explain the current popularity of the surrogate model.

2. I would like to know whether the model you designed has other innovations in structure and implementation compared with the diffusion model, in addition to the differences in parameter settings and application issues. I feel that the model is not deep enough, judging from the algorithms shown in the first six pages. (I will consider this again)

3. I also found that your experiments often combine your model with other NNs (FNO, etc.). Why don't you use your model to implement it independently? Because I am worried that NNs such as FNO will additionally correct the errors of your model (if they occur).

### Questions
There are some unnecessary blank lines in the article that can be corrected. I will be happy to improve my score in subsequent discussions.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents MultiSimDiff, a novel generative approach for Multiphysics and multi-component simulations, using diffusion models to overcome the limitations of surrogate models. MultiSimDiff framework can be seamlessly integrated with existing backbone architectures, modeling the conditional probability of each physical field or component within a system. By training on decoupled data, it can generate joint solutions through reverse diffusion. This method demonstrates high accuracy, including reaction-diffusion, nuclear thermal coupling and prismatic fuel elements.

### Strengths
- The application of novel machine learning techniques, (the use of diffusion models in scientific domains is relatively new), particularly for multiphysics and multi-component simulations. 
- Trained on small, decoupled datasets, this method can provide solutions for extended, unseen data composed of smaller components, showing great potential for applications across various scientific and engineering fields. 
- The benchmarks are somewhat new and practical, beyond traditional toy PDE benchmarks.

### Weaknesses
 - The multi-level “for loops” can cause a significant computational bottleneck, limiting the practical applicability of the method. While the author briefly acknowledged this limitation, they did not provide any metrics on the method’s computational efficiency, particularly in comparison to surrogates, which are a key consideration for physical simulations and their surrogates. The lack of concrete performance metrics, such as wall-clock time or FLOPs, makes it difficult to assess the practical viability of the approach, especially when compared to established surrogate modeling techniques. The authors should provide a detailed breakdown of the computational cost associated with each loop and the overall method, including the time required for training and inference.
- Although the authors noted the application of various compositional generative models in scientific domains in their related works, no compositional baselines were compared in the experiments. This omission makes it difficult to ascertain the true novelty and effectiveness of the proposed method compared to existing compositional approaches. A comparison with relevant compositional baselines would provide a clearer understanding of the advantages and disadvantages of the proposed method.
- In some experiments, the combination of “surrogate+x” outperformed the proposed methods. This raises concerns about the robustness and generalizability of the proposed method. The authors should clarify the conditions under which the proposed method outperforms or underperforms existing surrogate models, and provide a more thorough analysis of the factors that contribute to these differences in performance.
- Although interesting, it remains unclear how models trained on small structures can effectively extrapolate to larger structures. For instance, a model trained on a single pendulum cannot easily predict the behavior of a double pendulum, as the interactions within coupled systems add complexity beyond a simple combination. Could you clarify the difference between this scenario and the benchmarks used in paper, or at least explain if this method can be applied to this scenario?

### Questions
See above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses an important problem in the area of computational physics: namely, the composition (coupling) of multi-physics and multi-component simulations. The authors present a 'Bayesian approach' to model composition, with Eq 6 being the 'foundation' of their proposed method.  

The reviewer agrees with the importance of the problem and with the general (proposed) approach.  The reviewer, however, does not find the literature review to be sufficiently broad as the proposed method (as given) has been proposed in the computational mechanics literature they use as motivation.

### Strengths
The main strength of this paper is the use of a Bayesian approach to allow simulation scientists to 'decouple' their solvers by characterizing them in a probabilistic way.

### Weaknesses
The major weakness of the paper is that it is not clear that the method is novel.  For those who are embedded in the work of D.A. Knoll and D.E. Keyes (paper referenced by the authors -- good paper), George El Haber, Jonathan Viquerat, Aurelien Larcher, David Ryckelynck, Jose Alves, Aakash Patil, and Elie Hachem (JCP paper referenced), etc.,  --- these people (e.g., David Keyes) would probably start a history lesson with pointing out the seminar paper of Kennedy and O'Hagan (Bayesian calibration of computer models, Jan 2002) as the starting point of an entire class of methods on using the Bayesian approach for coupling, uncertainty estimation, etc.  With the Kennedy and O'Hagan paper as a starting point, you get things like:

https://amses-journal.springeropen.com/articles/10.1186/s40323-022-00237-5
(and lots of Wolfgang Wall's work)

http://mcubed.mit.edu/files/public/RT3/2016__Allaire__Quantifying_Model_Discrepancy_in_coupled_multi-physics_systems.pdf

https://www.sciencedirect.com/science/article/pii/S0021999119304206

and then particular people like Karen Willcox (UT-Austin), Youssef Marzouk (MIT), etc. and their use of Bayesian methods for "all kinds of things."   

Given that there is a rich history of these methods within the journals referenced by the authors and given that it is difficult to evaluate the novelty of the statements against this 20 year history, the reviewer (at this time) cannot recommend the paper for acceptance.

### Questions
What is the novelty of the method in comparison to the papers mentioned above and more broadly the papers/journals in which these papers reside?  The papers mentioned below are not necessarily the seminal papers, but what one gets by googling with keywords associated with the topic and the journals mentioned by the authors.

Specifically, in terms of addressing the weaknesses:

+ How does the author's compositional diffusion model approach compare to the Bayesian calibration methods of Kennedy & O'Hagan and subsequent work that builds on this (of which the reviewer has given some, but which is a vast area)?

+ Whether and how the author's method of learning conditional energy functions and composing them differs from existing Bayesian coupling approaches?  The Bayesian approach as presented seems consistent with what a practitioner might do for uncertainty quantification, but does not replace the weak and strong coupling methods mentioned in the early part of the paper (which is interested in specific instances, not probabilistic statements).

The author is asking If the focus on using decoupled training data to predict coupled solutions, and small structure data to predict large structures, represents a novel contribution.

### Soundness
3

### Presentation
3

### Contribution
1

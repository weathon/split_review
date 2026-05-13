# Unisolver: PDE-Conditional Transformers Are Universal PDE Solvers

- Decision: Reject
- Scores: 3, 8, 3, 8

## Abstract
Deep models have recently emerged as a promising tool to solve partial differential equations (PDEs), known as neural PDE solvers. While neural solvers trained from either simulation data or physics-informed loss can solve PDEs reasonably well, they are mainly restricted to a few instances of PDEs, e.g. a certain equation with a limited set of coefficients. This limits the generalization of neural solvers to diverse PDEs, impeding them from being practical surrogate models for numerical solvers. In this paper, we present the Universal PDE Solver ({Unisolver}) capable of solving a wide scope of PDEs by training a novel Transformer model on diverse data and conditioned on diverse PDEs. Instead of purely scaling up data and parameters, Unisolver stems from the theoretical analysis of the PDE-solving process. Our key finding is that a PDE solution is fundamentally under the control of a series of PDE components, e.g.~equation symbols, coefficients, and boundary conditions. Inspired by the mathematical structure of PDEs, we define a complete set of PDE components and flexibly embed them as domain-wise (e.g.~equation symbols) and point-wise (e.g.~boundaries) conditions for Transformer PDE solvers. Integrating physical insights with recent Transformer advances, Unisolver achieves consistent state-of-the-art results on three challenging large-scale benchmarks, showing impressive performance gains and favorable PDE generalizability.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
In this paper they add symbolic representation of the PDE operator to an LLM based PDE solver.  For the one dimensional wave equation, they add Prompt: "u_{tt} - aˆ2 u_{xx} = f(x,t)"".  More PDE prompts are included in Table 12 of the Appendix. The model is trained "for solving multitudinous PDEs universally."   The architecture is based on Theorem 1, which shows that the PDE solution depends on the PDE equation, the input data, the forces, and the boundary data.   The method is compared to several baselines. However,  since the baselines do not include the language model prompt for the PDE they augment these baselines "by providing sufficient physics information to ensure a fair comparison, either by concatenating the inputs with varied PDE components, providing prompting trajectories (ICON) or applying physics-informed loss (PINO)."

### Strengths
The strength of the paper is the implementation of an LLM based PDE solvers, which includes prompt describing the PDE equation, e.g. Prompt: "u_{tt} - aˆ2 u_{xx} = f(x,t)"".
They introduce HeterNS, an extension of the widely used 2D NS dataset (Li et al., 2021a), to assess how models handle diverse PDE components, particularly viscosity coefficients and force terms.
They also perform experiments on 1d time dependent PDEs, and 2d mixed PDEs.  They claims results which mostly beat the performance of their model, compared to the modified baselines.

### Weaknesses
PDE solvers are a machine learning approach to a problem where, if the inputs are properly specified, and the PDEs is well-posed, there is no need for machine learning: standard scientific computing results give very precise and well-understood solvers. So machine learning approached need to be properly motivated, and the problem needs to be carefully defined.

In this paper, the problem is not clearly defined.  I understood that an LLM method was used, along with a text prompt including the equation for the PDE.  But it was not clear exactly what the PDE was trained on, in for example, Table 2.  The training times are extremely long, compared to standard methods.   Also the modification to the baselines is not clearly described.  Inputs, outputs, and data need to be specified.   
There are not standard datasets with standard performance measures: these are new datasets defined by the authors, and performance measures and baselines defined by the authors.  So the meaning and importance of the numbers in the table is really not clear.
To repeat: it's not clear to me what the models were trained on exactly, and it's not clear how the errors were measured, or what the meaning of the experiments are.  See questions below.

Even when the problem is underspecified, or the PDE is not well posed, there are a number of approaches which seek to find solutions.  For example, there is a notion of weak solutions to PDEs which lack classical solutions. https://en.wikipedia.org/wiki/Weak_solution There is the notion of inverse problems, for learning operators from data. https://en.wikipedia.org/wiki/Inverse_problem . There is also the notion of homogenization, which deals with small scales in the data. https://en.wikipedia.org/wiki/Asymptotic_homogenization .  

This paper critiques existing methods as not taking full advantage of of the data, but this is a misrepresentation of the learning problem for previous methods, which are expressly designed to solve the PDE without knowing the form of the equation.     

Contribution: "Motivated by the mathematical structure of PDEs, we define the concept of complete PDE components, classify them into domain-wise and point-wise categories, and derive a decoupled conditioning mechanism for introducing physics information into PDE solving."  
- This is a concept completely original to the paper, which ignores exiting expertise on PDE operators, and is not clearly explained.  It's also not clear how it corresponds to what they do in the paper. 

Theorem 1: This is not a theorem. It is a restatement of an undergraduate textbook example of the solution of the analytical solutions to the one dimensional wave equation.  But it is not clear how this solution formula relates to a universal solution method for PDEs.  The solution expressed in the theorem is particular to the equation, and there do not exist similar explicit solutions for most PDEs.  For example, the heat equation solution depends in a very different way on the initial data: in a special case, it is simply convolution with a Gaussian.  The analogy no longer holds. 

"In this paper, we will elaborate on how Unisolver finely and completely embeds all considered PDE components (Table 1) into deep PDE conditions based on our insights from the mathematical analysis."
- all the equation prompts had constant coefficients.  How would you prompt a two dimensional equation, with variable coefficients?
- How do you distinguish between the exact  PDE and incomplete knowledge of the PDE?

"Unisolver stems from the theoretical analysis of the PDE-solving process."
- How so? There is no universal PDE solver, since PDEs do not universally have solutions.  
- Some PDE operators are well-posed, which means there existing unique solutions which are stable under certain types of perturbations of the data..  Others are not:  For example the wave equation with have multiple solutions if the initial data is mis-specified.  Some PDEs develop finite time singularites.  
- How is the question of PDE ill posed / well posed addressed by this paper?

Paragraph 2: "previous neural solvers can be broadly categorized into two paradigms:  physics-informed neural networks (PINNs) (Raissi et al., 2019) and neural operators"
- This is an imprecise characterization.  There are multiple formulations of PDEs problems: these include: (i) learning a solution operator, based on a dataset of solutions on grids, and (ii) learning a single PDEs solution, based on incomplete data, as well as knowledge of the PDEs, as well as (iii) learning the PDE operator from sample(s) of (possibly incomplete data.

### Questions
"We compare Unisolver with six advanced baselines on the HeterNS to demonstrate its generalizability under varied PDE components: the well-established FNO (2021a), PINO (2021b) and ViT (2020) and current state-of-the-art methods Factformer (2023b), ICON (2023) and MPP (2023). We augment these baselines by providing sufficient physics information to ensure a fair comparison, either by concatenating the inputs with varied PDE components, providing prompting trajectories (ICON) or applying physics-informed loss (PINO). Furthermore, we compare Unisolver with two generalizable solvers—PDEformer (2024) and DPOT (2024) on zero-shot generalization performance in a head-to-head manner. We refrain from including additional baselines on these two benchmarks due to the substantial computational cost of using million-scale samples."
- what exactly is the training data, expressed in terms of the solutions to which PDEs?  Was it all the PDE solutions, were the text prompts included with the data?  What is the test data?  An initial condition? Along with the text of the PDE?
- Please describe what were the inputs to the training dataset, what were the inputs to the model (besides the latex text prompt for the PDE) and he models trained on a dataset of PDEs for each of the three main cases?  
- what were the millions-scale samples?  

This paper critiques existing methods as not taking full advantage of of the data, but this is a misrepresentation of the learning problem for previous methods, which are expressly designed to solve the PDE without knowing the form of the equation.    On the other hand, if the LLM is given the form of the PDE (as a text prompt), what is stopping it from simply using an existing scientific computing method solver to solve the PDE precisely?  Or is this meant to be the point of the method?  The lack of problem definition makes it hard to asses the contribution.

Contribution 1: Unisolver achieves consistent state-of-the-art performances across three large-scale benchmarks with impressive relative gains and presents favorable generalizability and scalability. 
- what is meant by "favorable generalizability"?

"Our key finding is that a PDE solution is fundamentally under the control of a series of PDE components, e.g. equation symbols, coefficients, and boundary conditions."
- this key finding is not correct, and ignores many years of expertise in PDEs.  Please clarify and explain more precisely how this motivated your architecture.

"Thus, due to the omission of PDE information, current neural operators are mainly trained and tested on a limited set of PDEs."
  - This is imprecise, and misleading.  It suggests that the omission of the PDE operator is a flaw in current neural operator methods.  But that is not the case: these methods are designed to learn the PDE solution operator from data.  If we included knowledge of the PDE equation, we could simply avoid machine learning and solve the PDE using traditional scientific computing methods. 
- Please explain how this method compares with and related to traditional scientific computing solvers.  Was the method trained on code for these solvers?

"We augment these baselines by providing sufficient physics information to ensure a fair comparison, either by concatenating the inputs with varied PDE components, providing prompting trajectories (ICON) or applying physics-informed loss (PINO)."
- how is this done?  These are no longer baselines, but new methods.

"Concretely, Unisolver proposes a complete set of PDE components and embeds these components into domain-wise and point-wise deep conditions separately for deep conditions. "
- This is not clear: what are "point-wise deep conditions "

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a new foundation model for solving PDEs. The core contribution is a systematic way to include all possible PDE information in the model.  The PDE information is divided into point-wise and domain-wise information, such as the PDE parameters. Most notably, the authors propose to include the mathematical equation of the PDE into the model by using an LLM encoding. The model is evaluated on three large-scale benchmarks and is shown to surpass the considered baselines.

### Strengths
1. Good experimental design, including challenging tasks and an appropriate choice of baselines. The authors provided an evaluation of the standard deviation in the appendix as well.  
2. Stronger performance than comparable foundation model architectures. 
3. Simple but powerful architectural design considering all aspects encountered while solving PDEs.
4. The paper is clearly written and easy to follow.

### Weaknesses
1. The components defining the behavior of a PDE are already known and not a "key finding," as stated in the abstract. 
2. Limited methodological novelty (but a good combination of existing components).
3. No evaluation of inference times and memory consumption compared to the baselines; only the training time and parameter count are provided. 
4. The claim that the LLM uses its mathematical knowledge obtained from pretraining on language data is not well supported. The ablation shows that the performance drops when not using the LLM by comparing it to a random vector encoding, but it is not shown that this is due to prior mathematical knowledge of the LLM. Another explanation for the good results of using the LLM encodings could be that they are simply a good representation of the number of symbols in the equation or that they make it easy for the model to differentiate between the considered PDEs.

### Questions
1. Regarding the LLM ablations:
    1. Please clarify how you performed the random vector encoding. Does random vector encoding mean that all the different equation combinations get their own fixed random vector? Or is the model fed with a new, different random vector for every input? 
    2. Wouldn't a one-hot encoding of which PDE version is currently used be a better baseline?
    3. Another possible experiment could be to train the model with “wrong” mathematical encodings. For example, map “u_{xx}” to “b_{vvv}” or a “+” to “-”  (with fixed maps and keeping the number of elements in the equation identical). This would keep the string encoding close, but if the LLM really used mathematical understanding, this should lead to a worse performance.
2. In line 1347, you introduce a binary mask to notice the model which component is active. Shouldn’t the LLM encoding of the equation handle this?
3. How costly is using an LLM to encode the equation?
4. Is the model trained with one-step predictions or autoregressive rollouts?
5. How are the inputs aggregated in the “deep condition consolidation”?
6. Please clarify in the paper on all figures that the numbers refer to the relative L2 (missing in Fig. 8, Fig 6a, Tab7.), especially since you switch between relative L2 and relative L2 x 10^-2.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes the Universal PDE Solver (Unisolver) which is capable of solving a wide scope of PDEs by training a novel Transformer model on diverse data and conditioned on diverse PDEs. Unisolver defines a complete set of PDE components and flexibly embeds them as domain-wise (e.g. equation symbols) and point-wise (e.g. boundaries) conditions for Transformer PDE solvers. Unisolver has achieved consistent state-of-the-art results on three challenging large-scale benchmarks.

### Strengths
1. A novel and decoupled conditioning mechanism for introducing physics information into PDE solving.
2. Extensive experiments on three challenging large-scale benchmarks and state-of-the-art performance. 
3. Easy to follow.
4. Substantial implementation details are included.

### Weaknesses
1. In the proof of Theorem 1 in Appendix D, the proof from line 942 to 971 and the first term in line 992 are just the d'Alembert solution of wave equations, which is well-known in PDE theory and physics and appeared in standard textbooks. In line 937, equation (9) should be  equation (6). It is suggested to remove these proofs and cite a textbook. Further, I think it is unneccessary to use Theorem 1 to introduce the concepts of domain-wise and point-wise PDE components, since these concepts are clear and easy to understand by themselves and the paragraph following Theorem 1 did not point out explicitly why coefficient a works domain-wisely and external force f point-wisely using the solution expression in equation (2), and some PDE components in table 1, such as equation symbols, did not appear explicitly in equation (2). 
2. Using complete PDE information will certainly help the solution prediction. Regarding the motivation of the proposed method, please explain why you choose to predict solutions in a data-driven manner instead of using numerical solutions and PINNs, which both can take full advantage of complete PDE components. Especially, please disucss the pros and cons of Unisolver vs PINNs in terms of accuracy and computational efficiency. 
3. Traditional operator learning method such as FNO train neural networks to generalize across different configuratons (such as viscosity coefficients and force terms) of the same type of PDE. Unisolver used large dataset to train a PDE-conditional Transformer model and expect it to generalize across diverse PDEs. Did different types of PDEs help each other during prediction? If possible, please give an ablation study to show the transfer learning capability of Unisolver among different types of PDEs, and justify the integration of a wide range of PDEs instead of treating them independently. The Burges and Convection equations, used in table 5 to show zero-shot generalization capability, are only special cases of the equations in line 1044 used for training. You could, for example, train Unisolver on Navier-Stocks equation and test it on the diffusion-reaction equation, or train and test Navier-Stocks equation on different domain geometry, to demonstrate the transfer learning capability of Unisolver among different types of PDEs.
4. Please explain why Unisolver works much better than PINO in table 3 in terms of relative error. In principle, by incorporating physics-informed loss, PINO is able to obtain accurate solutions.  Can we improve the accuracy of PINO if we weight the physics-informed loss more heavily?
5. Please give the computational cost to generate the datasets, including hardware used and simulation time, especially for HeterNS.

### Questions
Why use the LLM embedding of PDE symbol instead of Latex code? It is better to give an intuive example to show the addtional useful information provided by LLM beyond equation symbols.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a surrogate neural PDE solver model, called Unisolver, that adapts a transformer model with a novel conditioning mechanism for better generalization. Based on the analysis of a PDE-solving process, this work identifies complete PDE components, categorizes them into two groups (i.e., domain-wise and point-wise conditions), and proposes a decoupled conditioning.

### Strengths
This work promotes the research direction for developing a generalizable surrogate neural PDE solver. The proposed conditioning method is novel and clearly described with reasonable motivation and thorough analysis through experiments.

The experiments present a meaningful improvement of the proposed model in various examples, particularly highlighting the improved capacity for zero-shot generalization.

The ablation study validates the importance of the proposed ideas.

### Weaknesses
One of the essential requirements for having a reliable neural PDE solver is the capacity for accurate solutions for a long temporal evolution. The current experiments seemed to fix the temporal evolution up to 20 steps (shown in Fig. 17). (The accompanied videos show only 10 steps.) Experiments and analysis for long trajectory prediction will be invaluable. It is unclear if the model can maintain accuracy over extended simulations, which is crucial for practical applications. The limited temporal scope of the experiments raises concerns about the model's stability and error accumulation over longer time scales. Additionally, the lack of explicit analysis of error propagation with respect to time is a significant gap.

Additionally, reproducibility will be improved if the codes are released. The proposed model relies on existing designs such as transformer, ViT, and DiT. This should not be a critical weakness of the work, though. Rather, It will be particularly useful to have actual codes because of the combinatory design of the proposed model. The specific implementation details of the conditioning mechanism and how the transformer architecture is adapted for PDE solving are not fully transparent without the code. This makes it difficult to verify the claims and replicate the results.

### Questions
What will happen if the LLM model (i.e., conditioning equation symbols) is omitted in a single PDE dataset? I guess it may not affect the performance because such a dataset does not need to be conditioned on this component. For example, will this be true for the HeterNS example, which I guess that it embeds the same condition on equation symbols?

It looks like a good idea to embed the equation symbols using LLM; on the other hand, I am wondering if a simple manual encoding (e.g., representing each PDE term as a one-hot vector and composing them to represent a full PDE equation) could be enough for a similar performance. This question also relates to the "Random vector" ablation study in Table 7. How did the random vectors get assigned for each PDE?

### Soundness
4

### Presentation
4

### Contribution
3

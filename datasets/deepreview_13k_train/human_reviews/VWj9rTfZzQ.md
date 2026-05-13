# MEENT: DIFFERENTIABLE ELECTROMAGNETIC SIMULATOR FOR MACHINE LEARNING

- Decision: Reject
- Scores: 5, 6, 5, 3

## Abstract
Electromagnetic (EM) simulation plays a crucial role in analyzing and designing devices with sub-wavelength scale structures such as solar cells, semiconductor devices, image sensors, future displays and integrated photonic devices. 
Specifically, optics problems such as estimating semiconductor device structures and designing nanophotonic devices provide intriguing research topics with far-reaching real world impact. 
Traditional algorithms for such tasks require iteratively refining parameters through simulations, which often yield sub-optimal results due to the high computational cost of both the algorithms and EM simulations. 
Machine learning (ML) emerged as a promising candidate to mitigate these challenges, and optics research community has increasingly adopted ML algorithms to obtain results surpassing classical methods across various tasks.
To foster a synergistic collaboration between the optics and ML communities, it is essential to have an EM simulation software that is user-friendly for both research communities.
To this end, we present \texttt{meent}, an EM simulation software that employs rigorous coupled-wave analysis (RCWA). Developed in Python and equipped with automatic differentiation (AD) capabilities, \texttt{meent} serves as a versatile platform for integrating ML into optics research and vice versa.
To demonstrate its utility as a research platform, we present three applications of \texttt{meent}: 1) generating a dataset for training neural operator, 2) serving as an environment for the reinforcement learning of nanophotonic device optimization, and 3) providing a solution for inverse problems with gradient-based optimizers.
These applications highlight \texttt{meent}'s potential to advance both EM simulation and ML methodologies.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
- This work emphasizes the significance of electromagnetic simulation in the analysis and design of photonic structures. 
- The integration of machine learning into electromagnetic simulation has emerged as a promising solution, with the optics research community increasingly leveraging machine learning algorithms.
- The paper introduces meent, a user-friendly electromagnetic simulation software developed in Python that utilizes rigorous coupled-wave analysis and automatic differentiation.
- It includes three key applications of meent.

### Strengths
- It is generally well-written.
- It introduces machine learning researcher-friendly electromagnetic simulation software.
- It provides several interesting applications of meent.

### Weaknesses
 - I don't know what the technical novelty of this work is.

### Questions
- What is the technical novelty of this work?
- This work might be not fit to ICLR, because it proposes a simulation tool.  I would like to discuss this issue with the authors, reviewers, and area chairs.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This work presents meent, a framework that aims to integrate EM simulators into the ML pipelines. In particular, meent contains a differentiable, Python-native EM simulator. The authors demonstrate the value of meent through three concrete applications: (1) generating datasets to train the neural operators; (2) enabling RL-based design of nanophotonic device; (3) constructing solutions for  inverse-problems

### Strengths
- Combining ML with EM simulator is an important problem. 
- The paper is organized really well and well-written. Starting with the technical details of meent, the authors also present concrete applications. This helps significantly in illustrating the value of meent. 
- The contribution of the proposed framework has been clearly discussed and the comparison with existing packages is comprehensive.

### Weaknesses
 - Missing related work: *Benchmarking Data-driven Surrogate Simulators for Artificial Electromagnetic Materials.* Thirty-fifth Conference on Neural Information Processing Systems Datasets and Benchmarks Track (Round 2) 
- I think it would be helpful to present a set of experiments comparing the efficiency of meent. In particular, how fast does meent generate EM simulation comparing to existing Cpp-based methods? 
- In other words, does the whole ML+EM pipeline take longer time by incorporating differentiable EM simulation? If the extra time is considerable, then the benefits of meent should be evaluated more carefully. 
- Since meent has some simulation error as discussed in Section 3, what is the performance degrade comparing to ML + classical EM simulators (e.g., Reticolo)? I think **it is helpful conduct the same set of experiments with ML+ Reticolo** and compare the resultant performance with the ones under meent.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
A differentiable electromagnetic simulation framework (called "meent"), which is able to operate on a continuous space. Moreover, authors have presented six different applications for how to use "meent" as a tool to generate data for ML as well as a solver for inverse problems.

### Strengths
- Clear presentation
- Comprehensive set of applications, including investigating machine learning (ML) algorithms in optics problems, and on development of nanophotonic devices.

### Weaknesses
I have a concern about the contribution of this paper. While having access to a user-friendly and differentiable software for Physics applications (e.g., EM simulator) is important and definitely helps research communities to accelerate their ideas, I am not completely convinced that this conference is a right place and fit for this paper. The main contribution of this paper is to introduce a python-based software, making the use of other developed tools easier for solving Physics applications. There are certainly other great venues where readers can take advantage of reading this paper and might be more fit to the audience.

### Questions
Could you either provide a comparison of your method to MaxwellNet (Lim & Psaltis, 2022)  for electric field prediction, or explain why MaxwellNet was not included as a baseline?"

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces Meent, a software designed for electromagnetic field simulation using RCWA, and highlights potential applications in machine learning (ML) through Meent. The paper is clear and easy to follow. See below for detailed comments.

### Strengths
The paper is easy to follow.

### Weaknesses
A key contribution of this work is the development of Meent. However, it is important to note that Meent is purely software based on numerical algorithms, and its development does not involve any ML techniques. The only connection to ML is the authors' use of Meent as a simulation backbone for dataset generation or device optimization.

This raises a significant concern: **there is no substantial contribution to the field of ML in this work**. If I may respectfully provide some examples that would align with ICLR's focus on ML, especially in the context of ML for photonics or AI for science: (1) The authors could propose a new neural operator (or architecture) that outperforms existing approaches such as FNO in predicting electromagnetic fields, such as [1,2]. (2) The paper could introduce a novel reinforcement learning algorithm that demonstrates better performance than current RL methods or use RL addressing a problem no one has done before, such as AlphaFold, AlphaGo. (3) The authors could apply ML techniques to design a more compact photonic device with much better performance that no one can. 

Unluckily, this work doesn't fall into any of the categories above. While I recognize the potential value of this work, the primary contribution is not centered on ML. Therefore, I must recommend rejection for ICLR and suggest the authors consider alternative venues that might be more suitable, such as IEEE JLT, APL Photonics, Optica, Optica Express, Nature Photonics, or Nanophotonics.

### Questions
See 'Weakness' section.

### Soundness
2

### Presentation
3

### Contribution
1

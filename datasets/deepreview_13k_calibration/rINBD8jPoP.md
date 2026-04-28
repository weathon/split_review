# Curriculum reinforcement learning for quantum architecture search under hardware errors

- Decision: Accept
- Avg Score: 5.60
- Scores: 6, 6, 6, 5, 5

## Abstract
The key challenge in the noisy intermediate-scale quantum era is finding useful circuits compatible with current device limitations.
Variational quantum algorithms (VQAs) offer a potential solution by fixing the circuit architecture and optimizing individual gate parameters in an external loop. 
However, parameter optimization can become intractable, and the overall performance of the algorithm depends heavily on the initially chosen circuit architecture. 
Several quantum architecture search (QAS) algorithms have been developed to design useful circuit architectures automatically.
In the case of parameter optimization alone, noise effects have been observed to dramatically influence the performance of the optimizer and final outcomes, which is a key line of study. 
However, the effects of noise on the architecture search, which could be just as critical, are poorly understood.  
This work addresses this gap by introducing a curriculum-based reinforcement learning QAS (CRLQAS) algorithm designed to tackle challenges in realistic VQA deployment. 
The algorithm incorporates (i) a 3D architecture encoding and restrictions on environment dynamics to explore the search space of possible circuits efficiently, (ii) an episode halting scheme to steer the agent to find shorter circuits, and (iii) a novel variant of simultaneous perturbation stochastic approximation as an optimizer for faster convergence. 
To facilitate studies, we developed an optimized simulator for our algorithm, significantly improving computational efficiency in simulating noisy quantum circuits by employing the Pauli-transfer matrix formalism in the Pauli-Liouville basis. 
Numerical experiments focusing on quantum chemistry tasks demonstrate that CRLQAS outperforms existing QAS algorithms across several metrics in both noiseless and noisy environments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Variational quantum algorithms (VQAs) stand for a promising candidate of practical quantum algorithms in the NISQ era. Nevertheless, the performance of VQA is significantly influenced by the choice of ansatz and noise effects. 

In this paper, the authors adopt curriculum reinforcement learning for quantum architecture search (QAS), aiming to select ansatz with good performance under hardware errors. Specifically, they devise a CRLQAS algorithm with tensor-based 3-D encoding of quantum circuits, a random halting scheme to reduce the circuit length, and an variant of Adam-SPSA for better convergence. In addition, this work accecelerate simulation of noisy quantum circuits by employing pauli transfer matrix formalism. 

Numerical experiments on quantum chemistry tasks demonstrate the performance of the proposed method under noiseless and noisy circumstances.

### Strengths
- Originality: As far as I know, this is the first work to consider noise models from real quantum machines in RL-based QAS. Previous work focus on noiseless scenarios or only touch on simple noisy configurations. The setting of this work is closer to real applications in NISQ era, hence making it an advance over the previous state-of-the-art.
- Quality: The paper proposes several techniques which are effective and easy to realize. The tensor-based binary encoding is straightforward but efficient and compact. Pruning of illegal actions successfully narrow the search space. Random Halting is introduced to reduce the training episodes, which is a major drawback of previous work. The offline computation with Pauli-transfer matrices and JAX achieves considerable acceleration for noise simulation.
- Clarity: The main ideas and techniques in the paper are mostly clear, but many issues remain (see Weaknesses & Questions). 
- Significance: This paper seeks to tackle an important problem by considering noise of current devices in QAS for VQA, which is well-motivated. Literature discussing the negative impacts of noise on VQA has been thoroughly cited. The numerical demonstration of achieving chemical accuracy and outperforming previous methods is impressive.

### Weaknesses
 - The writing is poor, full of mistakes in grammar and notation. For example, the first sentence in the second paragraph of Section 3.6 is incomplete. There are erroneous notations such as  $T_{s}^{e}$ v.s $T_{s^{e}}$ in Section 3.3, wrong format of citation like (Wang et al., 2021) in introduction, inconsistent proper nouns such as "ansatz" v.s. "ans{"a}tze", and numerous syntax errors. These issues impair the quality of the paper. 
- Originality: This paper extends the ideas from previous work (Ostaszewski et al., 2021). Some techniques such as feedback driven curriculum learning and Adam-SPSA seem to be the direct adaptation of existing methods.
- Although several techniques are proposed, the paper may lack insights into which component principally improves the results, especially under noisy circumstances. It is unclear to me which technique is specialized for facilitating noise adaptations, rather than general improvement over existing methods. For instance, the tensor-based encoding, while compact, may not inherently contribute to noise resilience. Similarly, random halting could simply reduce training time without specifically addressing noise.
- Related to the previous question, in the noisy simulation section, the paper conducts no comparison with other RL-based QAS methods. Therefore it is unclear what is the improvement of this algorithm over previous methods in noisy environments. Moreover, for molecules such as LiH-4, the experiments only consider shot and 1-qubit depolarizing noise, which is far from real noise models. This undermines the persuasiveness of this work. The use of only single qubit depolarizing noise, while computationally convenient, does not capture the more complex correlated noise present in real quantum devices, such as crosstalk or coherent errors. This makes it difficult to assess the practical utility of the proposed method.
- Important related work not discussed. Despite little consideration of noise in previous reinforcement learning methods for QAS, there have been many attempts in the traditional architecture field. The paper may need more comparison with other QAS algorithms under hardware erors, especially those targeting noise-aware search, for example Wang et al. QuantumNAS 2022.

### Questions
- Please proofread the manuscript and correct the numerous mistakes in grammar and notation. Also there is a repetition in the reference section, where "Abhinav Kandala, Antonio Mezzacapo, Kristan Temme, Maika Takita, Markus Brink, Jerry M Chow, and Jay M Gambetta. Hardware-efficient variational quantum eigensolver for small molecules and quantum magnets. nature, 549(7671):242–246, 2017" is listed twice.
- Some descriptions are unclear to me. In Section 3.3, what does "$n_s$ is the number of successes" mean? Details in Section 3.4 could also be better stated. Moreover, from a reader's point of view, the organization of Section 3 is scattered and lacks emphasis on major contributions. 
- Does the model need retraining for different noise models to deliver competitive results? I am curious about the efficiency for adaptation to new noise models. Also I believe experiments on real quantum machines comparing the proposed method with other algorithms would make the work more solid.
- Although the authors claim to tackle the general employment of VQAs, numerical experiments on applications are actually limited to VQE for quantum chemistry tasks. The authors should avoid overstatement, or apply the method to general VQA settings and tasks.
- There is almost no discussion of limitations. What is the weakness of this method and what are the potential future directions?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper tackles the challenge of identifying optimal quantum circuits within the constraints of noisy intermediate-scale quantum (NISQ) devices. It introduces a novel curriculum-based reinforcement learning algorithm for quantum architecture search (CRLQAS), which innovatively employs a 3-D architecture encoding, an episode halting mechanism, and an enhanced simultaneous perturbation stochastic approximation optimizer for more efficient exploration and convergence. By incorporating Pauli transfer matrix formalism to improve simulation times, the proposed CRLQAS demonstrates superior performance in automating the design of quantum circuit architectures, outstripping existing methods in both noiseless and noisy conditions, specifically for quantum chemistry applications.

### Strengths
The paper excels in its strategic approach to quantum computing in the NISQ era by giving paramount importance to the role of quantum noise and its effect on circuit architecture. It introduces a pioneering curriculum-based reinforcement learning (RL) algorithm, CRLQAS, which specifically addresses the challenges posed by noise in quantum systems. The use of the Pauli transfer matrix formalism in this algorithm marks a substantial improvement in the simulation of noisy quantum circuits, significantly reducing computational time and increasing simulation fidelity. 

In addition to the quantum-specific advancements, the paper contributes to the field of RL by implementing a 3-D architecture encoding and an episode halting mechanism within its curriculum-based framework, enhancing the RL agent's ability to discover shorter and more hardware-efficient circuit architectures rapidly. The introduction of a novel optimization technique further refines the learning process, facilitating faster convergence and potentially leading to more robust quantum computing solutions. These combined strengths showcase the paper's dual focus on developing an efficient simulation that carefully accounts for quantum noise and on refining RL techniques to ensure that the architecture search yields practical, hardware-efficient designs.

### Weaknesses
One area for improvement in the paper is the absence of the promised source code, which limits the ability of others to replicate and build upon the work. It is essential for the authors to provide the source code to enhance the transparency and applicability of their research. Therefore, it is recommended that the authors include a link to the open-sourced code or an appendix containing the code in any subsequent revision of the paper. This addition would be a valuable resource for the community and would greatly facilitate further research and validation of the proposed methods.

The paper could be enhanced by broadening the scope of its comparative analysis with existing methodologies. While the current work focuses on a specific approach to quantum circuit optimization, there are alternative methods worth considering, such as those based on SMT (Satisfiability Modulo Theories) solvers. For instance, the technique presented by B. Tan and J. Cong in "Optimal layout synthesis for quantum computing," (ICCAD, 2020) could serve as a valuable benchmark. It would be beneficial for the authors to include a comparison with these kinds of potentially optimal circuit compilers to contextualize the effectiveness of their proposed method when applied to analogous problems.

Furthermore, the terminology used in the paper, specifically the term "architecture," may lead to ambiguity within the broader scientific community. In the realm of computer architecture, "architecture" typically refers to the low-level hardware design, as discussed in sources like the one available on IEEE Xplore. Since this work is centered around the optimization of parameterized quantum circuits, and not the hardware itself, clarity could be improved by selecting a term that more accurately describes the subject of optimization. A term like "circuit design" or "circuit configuration" may better capture the essence of the research without the potential for misinterpretation.

### Questions
1. Can the authors provide the source code that was mentioned as a part of the paper's contributions to facilitate replication and further research by peers?

2. Would it be possible to expand the comparative analysis section of the paper to include methodologies based on SMT solvers, such as the approach detailed by B. Tan and J. Cong in ICCAD 2020, to provide a broader context and demonstrate the relative effectiveness of the proposed algorithm?

3. Considering the potential for confusion within the interdisciplinary community, could the authors consider using a more precise term than "architecture" to describe the optimization of parameterized quantum circuits, thereby avoiding conflation with low-level hardware design?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a new combined RL algorithm tailored for the domain of quantum architecture search (QAS). AN empirical study shows benefits over state-of-the-art approaches in this very early field of research.

### Strengths
The paper does a reasonable job introducing the issue of quantum architecture search and, from the presented difficulties of the domain, manages to derive its adaptations to standard RL employed to tackle this domain. The adaptations presented are sound and straight-forward. The results give a nice guideline for future research in that direction.

### Weaknesses
As with most approaches in the field of quantum computing, the evaluation is rather weak does not allow to draw too strong a conclusion (which, luckily, the authors did not draw). The presentation of the sequence of experiments is rather convoluted (and not helped by putting the plots very late in the document). More clear-cut scenario descriptions would be helpful.

The discussion lacks an explanation how adaptations which were largely motivated by the accommodation of noise models then manage to outperform the state-of-the-art in the noiseless case.

Also, I would have liked a singled-out study on the impact of the "illegal actions" adaptations. It appears that it might do a lot of the heavy lifting, which would then change the overall story of the paper.

Many discussions are left to the Appendix and several forward-references point to it. The structure should be improved here to make a clearer distinction between important and less important points.

The writing still has several problems including:
- p1, second paragraph, last sentence: no verb
- p2, fig1, caption: "(i)" without "(ii)"
- p3: "Methods like this" should read "Methods like these"
- p4, eq2: parameters/variables are not sufficiently explained in the text, at least not in a concise manner
- p4, last paragraph before 3.1, first sentence: It is unclear how the "environment" is deterministic/stochastic. Refer to transition function, reward function etc.
- p5, section3.3, throughout: Typo "T_{s^e}" instead of "T _s^e"?
- p4, section3.4: do not put comma after "where"
- p6, section3.6: Use "it is", not "it's"
- p6, section3.6: "the Appendix" randomly appears in a sentence

### Questions
see above...

What is the distinct impact of the "illegal actions" adaptation?

Why is the result even better upon "closer inspection"? (p7, very bottom)

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In the era of noisy intermediate-scale quantum computing, selecting effective circuits in line with current device constraints is pivotal. This study accelerates quantum circuit simulations using the Pauli transfer matrix method and introduces a novel Curriculum-based Reinforcement Learning Quantum Architecture Search (CRLQAS) approach for optimal circuit structure determination.

### Strengths
1. A detailed analysis of the error rate.
2. Using the Pauli transfer matrix method to accelerate simulation and consider the noise in the training process.

### Weaknesses
1. The paper does not specify the function used to fit the spin orbital of the molecule. If the 'sto-3g' function is used, the claim of achieving chemical accuracy might be an overstatement. While it's not impossible, further clarification is necessary.

2. I'm concerned about the computational cost and efficiency of the reinforcement learning approach, especially when adding the noise injection method. Even with GPU acceleration, reinforcement learning is inherently expensive. Given that the noise model is derived from "current" calibration data and the gate-level noise model is only an approximation, there are concerns about its accuracy. For instance, although noise might seem stable over a short time frame, over a more extended period (e.g., a week), one can observe significant shifts. If the framework has a high computational cost, it may yield unreliable results if the calibration data changes rapidly during training.

3. Some parts of the paper could be clearer. For example, Table 4 should specify which molecule task is being discussed. There are several sections in the paper with similar clarity issues, making it harder to understand.

4. I observed that only one quantum architecture search work is considered in the comparative experiments. There are many other relevant works in the quantum architecture search for VQE, such as:

[1] Wang, Hanrui, et al. "Quantumnas: Noise-adaptive search for robust quantum circuits." 2022 IEEE International Symposium on High-Performance Computer Architecture (HPCA). IEEE, 2022.

[2] Rattew, Arthur G., et al. "A domain-agnostic, noise-resistant, hardware-efficient evolutionary variational quantum eigensolver." arXiv preprint arXiv:1910.09694 (2019).

[3] Liu, Xiaoyuan, et al. "Layer VQE: A variational approach for combinatorial optimization on noisy quantum computers." IEEE Transactions on Quantum Engineering 3 (2022): 1-20.

[4] Cheng, Jinglei, et al. "TopGen: Topology-Aware Bottom-Up Generator for Variational Quantum Circuits." arXiv preprint arXiv:2210.08190 (2022).

While there is a brief comparison with previous reinforcement learning-based architecture search papers, the fact that they don't consider noise models means it's expected for your approach to perform better. However, the increased computational cost is also a concern.

5.There's a notable absence of results on real quantum hardware. Testing only on a noisy simulator might not be entirely convincing, especially when using reinforcement learning, which is assumed to achieve the upper bound of performance. Given that you utilize a noise model from the current noisy environment and consider only one seed, real hardware testing is crucial.

### Questions
1. What is the function you used to fit the spin orbital of the molecule?

2. What is the computational cost for your framework? Say, based on the GPU acceleration, on what specific classical hardware, how long does it take? Please specify in detail.

3. Have you tried to implement your final result on real hardware? - I believe it should be easy for you since you already get your optimal arch and parameters from noisy simulation. You can just run this circuit on real quantum hardware and obtain the result.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a novel quantum architecture search (QAS) algorithm based on curriculum reinforcement learning (CRL) for designing parameterized quantum circuits (PQCs) under realistic noisy environments. The main contributions include a tensor-based binary encoding scheme, a mechanism of illegal actions to prune the search space and avoid redundant gates, and a random halting technique to encourage the agent to find shorter circuits. Additionally, it presents a variant of simultaneous perturbation stochastic approximation (SPSA) algorithm with adaptive momentum and variable sample budget for faster and robust optimization, and a fast GPU simulation framework using Pauli transfer matrix formalism to fuse gates with their noise models. The effectiveness of CRLQAS is demonstrated on quantum chemistry tasks of finding the ground state energy of various molecules, such as H2, LiH, and H2O, in both noiseless and noisy settings.

### Strengths
- Novel QAS algorithm: The paper proposes a curriculum-based reinforcement learning QAS (CRLQAS) algorithm that can automatically construct parametrized quantum circuits for variational quantum algorithms in realistic noisy environments. The algorithm introduces several novel features, such as tensor-based binary circuit encoding, illegal actions, random halting, feedback-driven curriculum learning, and Adam-SPSA optimizer.
- Experiments on real quantum devices: The paper demonstrates the efficiency and robustness of CRLQAS under different noise models inspired by real IBM quantum devices, and provides comprehensive descriptions of the experimental setup and the source code for reproducibility.

### Weaknesses
1. (Major) The absence of the comparison of some key methods in terms of theory and experiments. This paper emphasizes the design for quantum hardware errors, but there is no mention or comparison of some methods of QNAS that are also designed for noise, such as QuantumNAS (a noise-adaptive quantum circuit search) [1]. In addition, as far as I know, QCAS (Du et al., 2022) is tested on depolarizing errors, and QuantumDARTS (Wu et al., 2023) is evaluated readout errors. However, these methods under noise are not compared in the experiments.


2. (Minor) The representations of some tables are not clear enough. For example, if the best result is bolded, then ‘7.21*10^-8’ and ‘2.9*10^-4’ should be bolded in Table 1. In Table 4, CRLQAS (RH) has two rows of results but they're not marked what do they mean.

### Questions
1. As mentioned in the Intro, current NISQ devices are characterized by limited qubit connectivity and susceptibility to noise, but how does the proposed approach deal with qubit connectivity?
2. The proposed method is based on reinforcement learning, but only one related method is mentioned in this paper, and there are several QNSA works based on reinforcement learning that are not mentioned, such as [2,3,4]. Furthermore, compared with these methods, what is the innovation of CRLQAS, and whether it can reflect the advantage of the experiment? 

[2] Kuo, E. J., Fang, Y. L. L., & Chen, S. Y. C. Quantum architecture search via deep reinforcement learning. arXiv preprint arXiv:2104.07715, 2021.

[3] Chen, S. Y. C. (2023, August). Quantum Reinforcement Learning for Quantum Architecture Search. In Proceedings of the International Workshop on Quantum Classical Cooperative (pp. 17-20), 2023.

[4] Sun, Y., Ma, Y., & Tresp, V. Differentiable quantum architecture search for quantum reinforcement learning. arXiv preprint arXiv:2309.10392, 2023.

3. In Table 4, why is CRLQAS(wo-RH) better than CRLQAS? What is the meaning of random halting (RH)? 

4. What are the advantages and disadvantages of the proposed method and the Predictor-based QAS methods [5,6]?

[5] Zhimin He, Xuefen Zhang, Chuangtao Chen, Zhiming Huang, Yan Zhou, and Haozhen Situ. A gnn-based predictor for quantum architecture search. Quantum Information Processing, 22(2): 128, 2023b.

[6] Shi-Xin Zhang, Chang-Yu Hsieh, Shengyu Zhang, and Hong Yao. Neural predictor based quantum architecture search. Machine Learning: Science and Technology, 2(4):045027, 2021

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

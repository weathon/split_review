# Harnessing the Power of Neural Operators with Automatically Encoded Conservation Laws

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 6, 3, 6, 5

## Abstract
Neural operators (NOs) have emerged as effective tools for modeling complex physical systems in scientific machine learning. In NOs, a central characteristic is to learn the governing physical laws directly from data. In contrast to other machine learning applications, partial knowledge is often known a priori about the physical system at hand whereby quantities such as mass, energy and momentum are exactly conserved. Currently, NOs have to learn these conservation laws from data and can only approximately satisfy them due to finite training data and random noise. In this work, we introduce conservation law-encoded neural operators (clawNOs), a suite of NOs that endow inference with automatic satisfaction of such conservation laws. ClawNOs are built with a divergence-free prediction of the solution field, with which the continuity equation is automatically guaranteed. As a consequence, clawNOs are compliant with the most fundamental and ubiquitous conservation laws essential for correct physical consistency. As demonstrations, we consider a wide variety of scientific applications ranging from constitutive modeling of material deformation, incompressible fluid dynamics, to atmospheric simulation. ClawNOs significantly outperform the state-of-the-art NOs in learning efficacy, especially in small-data regimes.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a way to automatically guarantee the divergence-free of the NO outputs. This is done by introducing additional layers (the skew-symmetric matrix  and numerical differentiation layer) after the regular NO layers to form. The divergence-free architecture can be applied to different kinds of NO architectures.
The proposed method is evaluated on several examples (elasticity, shallow water equations and incompressible Navier-Stokes equations.) and compared with several existing methods (INO, GNO, FNO, G-FNO, U-Net). From the results, the method performs better compared with others, especially on small training dataset.

### Strengths
- Enforcing the conservation law can be a very useful way to improve the performance of neural operators, and the paper proposes a novel way to construct a network architecture to enforce a divergence-free output of NOs.
(I am not an expert in this area and I am assuming the paper’s method is the first one to enforcing the divergence-free form using the skew-symmetric matrix and numerical differentiation layers, based on their discussion of related work.)

### Weaknesses
 - The examples provided in the paper are relatively simple. There are not enough evaluation on real 3D models.  It would be good to see how the method performs on more complex cases, for example, 3D NS equations.
- The paper doesn’t explain the setup of experiments well. For example, different test cases use different Ts, number of samples and other settings. Why different settings were chosen for each test case?

### Questions
- As the paper proposes an architecture to enforce the divergence-free NO output, it would be good to have some analysis of the output divergence of the proposed method compared to other methods, and whether the improvement of the output divergence corresponds to the improvement of the accuracy of the proposed method.
- It would be good if the paper could provide more details in the training experiments. For example, how many training iterations it takes for the proposed methods and other methods. How much time it takes for each iteration in training and inference.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper targets a hot topic, where a group of deep learning that encodes inductive bias to recover physical governing functions. Specifically, the conservation law is integrated into neural networks for physical consistency. Different from existing work, this work builds the conservation law into the networks and considers a divergence-free aspect.

### Strengths
Considering physics-based learning is a hot topic with plenty of work, the paper provides a detailed review and a smooth transition from existing work to the proposed work.

The built-in conservation law is novel, enabling a hard constraint in data-driven function discovery.

### Weaknesses
Except for the neural operators adopted as baselines, there are other deep learning methods using physics-based inductive biases, such as energy conservation in Hamiltonian/Lagrangian neural networks and their variations. In methodology, it’s unclear what is the distinction of the proposed method. In experiments, there is no comparison with these methods to show the strengths.

It remains unclear how the proposed method's constraint on divergence-free fields compares to other approaches that enforce similar constraints. Specifically, the method's performance relative to techniques that directly parameterize divergence-free fields, rather than enforcing it through a loss function, needs further clarification. The current presentation lacks a detailed explanation of the advantages and disadvantages of each approach, making it difficult to assess the novelty and effectiveness of the proposed method.

### Questions
Are the proposed methods free of any prior knowledge of the targeted physical functions? Could the author(s) explain why, compared to previous designs?

The conservation law encoded by this work seems generalizable for different conservative quantities in various physical systems. Is it true?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces conservation law-encoded neural operators (clawNOs) that allows satisfaction of conservation laws by providing a divergent free prediction. The proposed method can be integrated with any neural operator architecture to enforce the conservation law on model prediction. To evaluate the performance of clawNO models different PDE-based problems were considered and the model accuracy was compared with a few baseline models such as vanila FNO, GFNO. The numerical experiments demonstrated that the clawNOs can outperform the baseline methods specially when there is limited number of training sample data is available.

### Strengths
- The idea of baking conservation law into NO model architecture is a valuable effort towards more reliable ML models that respect physics-based constraints such as conservation laws.
- the variety of scientific problems considered for the evaluation of the proposed method is nice. Also providing the effect of different size of training data was insightful and nice.

### Weaknesses
The following are the main reasons that I do not recommend the publication of this paper:
- The presentation of paper could have been much better. For some parts such as last two paragraphs of section 3.1 and section 3.2 sound very unclear to me. Additionally, the description of different experiments and the result discussions could have been better. for example: were all tests out of domain evaluation or in-domain evaluation? for the cases where FNO outperformed GFNO, authors could easily provide numerical investigation instead of describing the reason as their "guess" (I refer to last paragraph of section 4.1)
- Another observation is that there are missing related papers which aimed to address the same topic (enforcing conservation laws), which could potentially raise questions about the comprehensiveness of this work, the literature review, and the originality of the idea. For example, one closely relates work is:
Neural Conservation Laws: A Divergence-Free Perspective (https://arxiv.org/abs/2210.01741)
Since the idea of this paper is pretty much similar to this past work, authors should have at least acknowledged that the idea of thsi paper is related. It would be more appropriate to have discussions about the similarities and the parts the methods departs, and why not using this work as one of the baselines? There are of course additional works that could have been at least covered in literature review, such as: learning physical models that can respect conservation laws (https://arxiv.org/abs/2302.11002) which proposes a projection method to enforce integral form of conservation, learning differential solvers for systems with hard constraints (https://arxiv.org/pdf/2207.08675.pdf), and definitely more!
- I wish authors also had provided information (preferably numerical experiments) to discuss the computational complexity of their method. As far as I found, they just mentioned in one sentence that their method has comparable network size and computational cost. A good quality works requires to explore different aspects and report them properly.

### Questions
- Is this method applicable for other NO models such as Koopman neural operators (KNO), which has been gaining attention for learning long term dynamics?
- Does enforcing the divergence-free into model architecture bring any challenges for model training? could it cause numerical stability? could you comment on this?
- I know that the commonly used NO architecture is FNO, even for non-periodic boundary conditions. But how about using other basis functions which are shown to be more appropriate choices for other boundary constraints in conventional spectral methods, such as Chebychev for Dirichlet? It would be nice to address this as a possibility, and potential challenges which made authors not try that?
-  As mentioned in weakness section, could you comment on the computational complexity and potential challenges you had in your experiments? 
- (very minor comment) For Section 4.1, keep in mind that vorticity is a vector variable, just as velocity field, and for the 2D problem considered it only has the component normal to page.
- I did not clearly understand how training data and evaluation data are related? in other words, did authors conduct out of domain evaluation (which is more challenging task even for NO models), or it was in-domain evaluation. Could you clarify your train-test split and provide some details on the evaluation procedure?
- It is great that authors ran replicates of the same problem (with different seed of course) and reported mean and standard deviation. But how did they decide that 3 replicates could be enough? Did you try more replicates for at least one problem to see how the deviation change?
- In last paragraph of section 4.1, for GFNO lower performance you brought a "possible" reason that: This is possibly due to the expressivity degradation in GFNO outweighing the equivariant advantage, as the latent width of GFNO is reduced from 20 to 11 in order to maintain a similar total number of parameters to FNO for fair comparison.
Did you try the larger latent width to confirm that? It would be nice that you provide numerical reasoning.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This manuscript proposes a method of incorporating conservation laws into neural operators (clawNOs) that perform physical modeling. Using the proposed method, high accuracy can be achieved, especially for small sample sizes. The proposed method is demonstrated by applying it to material deformation, fluid dynamics, and atmospheric simulations.

### Strengths
This manuscript proposes a novel method of incorporating physical conservation laws into the Neural Operator architecture, enabling physical modeling with small data sizes. It also validates the proposed method on a wide range of physics system and demonstrates that it outperforms existing state-of-the-art Neural Operators. As such, I believe that the proposed method is generally useful in physical modeling.

### Weaknesses
Lack of comparison with existing methods other than neural operators. There is no examination of the scalability of the method in high dimensional systems. It is unclear how the computational cost changes as the conservation laws and system dimensionality increase in complexity.

### Questions
It would be good to compare the method with existing methods other than neural operators.
It would be good to add an examination of the scalability of the methods in high dimensional systems.
It would be good to present how the computational cost changes as the conservation laws and the dimensionality of the system become more complex.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents the clawNOs to automatically encode the conservation law to neural operators. Instead of directly learning final solution, clawNOs propose to learn a substitute skew-symmetric matrix-valued function, whose differentiation naturally holds the divergence-free property. Technologically, a special differentiation layer is proposed for implementation. clawNOs surpass FNO and geo-FNO in three benchmarks and performs well in small-data regimes.

### Strengths
-	The proposed method performs well in three typical benchmarks.

-	Encoding the conservation law can boost the model performance in small-data regimes.

### Weaknesses
1. About the novelty.

The analysis in Section 3.1 is similar to this following paper. But they didn't cite this paper in this section, making it is hard to judge their contribution.

Neural Conservation Laws: A Divergence-Free Perspective, NeurIPS 2022.

2. About the efficiency.

Since clawNOs introduce an additional differentiation layer, the comparisons w.r.t. FNO and GFNO in running time, GPU memory, model parameter are expected.

3. More baselines.

Actually, FNO and GFNO are both simple baselines. Recently, there are many advanced neural operators, such as LSM [1], U-NO [2]. It is hard to judge the model performance unless they compare with the above mentioned baselines.

[1] Solving High-Dimensional PDEs with Latent Spectral Models, ICML 2023

[2] U-NO: U-shaped Neural Operators, TMLR 2023

4. More analysis about the divergence-free property of outputs.

I can understand that if the model does learn an optimal differentiation layer, the output results will strictly satisfy the divergence-free property. But the authors adopt an approximation design. How well will the differentiation layer perform? A metric for the output divergence-free property is expected. Does clawNOs really perform better than FNO or GFNO in learning divergence-free results? Experiments are required.

5. More showcase comparisons.
The authors only provide the showcases for their own model in the supplementary materials. More showcase comparisons are expected to intuitively demonstrate the advantages of clawNOs.

6. About the long-term prediction.
Since the authors claim the long-term performance as an important advancement of clawNOs, they should plot the time-stamp-wise error curves in comparison with other baselines. Concretely, how does the prediction error change along the temporal dimension?

7. The authors claim that “ClawNOs significantly outperform the state-of-the-art NOs in both accuracy and generalizability” in the abstract. What does the “generalizability” mean here?

8. I am also confused about the physical understanding of clawNOs. Are there any physical meanings to the skew-symmetric matrix-valued function $\mu$? Or this is just a mathematical trick. I think this question is important, since it determines whether clawNOs hold potential physical limitations or not.

### Questions
Since they do not properly cite the previous work, it is hard to judge their contribution. Besides, the experiments and clarifications about their design are insufficient. All the details are included in the weaknesses section.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

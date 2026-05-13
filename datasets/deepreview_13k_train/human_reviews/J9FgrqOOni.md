# Discretization-invariance? On the Discretization Mismatch Errors in Neural Operators

- Decision: Accept
- Scores: 5, 8, 8, 5

## Abstract
In recent years, neural operators have emerged as a prominent approach for learning mappings between function spaces, such as the solution operators of parametric PDEs. A notable example is the Fourier Neural Operator (FNO), which models the integral kernel as a convolution operator and uses the Convolution Theorem to learn the kernel directly in the frequency domain. The parameters are decoupled from the resolution of the data, allowing the FNO to take inputs of different resolutions.
However, training at a lower resolution and inferring at a finer resolution does not guarantee consistent performance, nor can fine details, present only in fine-scale data, be learned solely from coarse data. In this work, we address this misconception by defining and examining the discretization mismatch error: the discrepancy between the outputs of the neural operator when using different discretizations of the input data. We demonstrate that neural operators may suffer from discretization mismatch errors that hinder their effectiveness when inferred on data with resolutions different from that of the training data or when trained on data with varying resolutions. As neural operators underpin many critical cross-resolution scientific tasks, such as climate modeling and fluid dynamics, understanding discretization mismatch errors is essential. Based on our findings, we propose a Cross-Resolution Operator-learning Pipeline that is free of aliasing and discretization mismatch errors, enabling efficient cross-resolution, multi-spatial-scale learning, resulting in superior performance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper examines "discretization mismatch errors" in neural operators, like the Fourier Neural Operator (FNO), which learn mappings between different types of data. The authors find that training these models at low resolutions and applying them at high resolutions can lead to performance issues. They propose a new Cross-Resolution Operator-learning Pipeline to avoid these errors, improving accuracy in tasks requiring precise predictions across multiple resolutions, such as climate modeling and fluid dynamics.

### Strengths
1. The phenomenon of "discretization mismatch errors" is a significant issue in operator learning. This paper proposes the CROP framework to address (reduce) this error.

2. The numerical examples in this paper show that CROP achieves improved performance over classic neural operator architectures, with the Fourier Neural Operator (FNO) used as an example.

### Weaknesses
1. Compared to approaches like "physics-informed constraints" and "continuous-discrete equivalence (CDE)," the CROP framework takes a more practice-oriented perspective. That is, the CROP framework is not inherently discretization-invariant. Specifically, it can only operate on fixed scales chosen *a priori*. This raises a question: how can the CROP framework be adapted to handle infinitely fine resolutions? Is there a formulation of CROP that accommodates an infinite range of scales?

2. The theoretical treatment of "discretization mismatch errors," particularly the results in Proposition 4.4, warrants closer examination:
   1. The authors only provide an upper bound for the error $E_{MN}$. Mathematically, this does not necessarily imply that the "discretization mismatch errors" will vary in line with the trends of the upper bound.
   2. Given the upper bounds in Lemma B.2, how should we interpret the conclusion that "discretization mismatch errors" increase as $M$ grows? Interestingly, it appears that the upper bound does not depend on $M$.
   3. The derivation of Lemma B.2 is relatively straightforward, especially for the terms $\omega^L$ and $\prod_{\ell=1}^L C_\ell$, making the conclusion that "discretization mismatch errors" may increase with $L$ and $\omega$ unsurprising. This could likely be generalized to other neural operator models as well.

3. The numerical results in Table 2 could be expanded. Specifically, it would be beneficial to include results from training resolutions of $127 \times 128$ or even $256 \times 256$. Many recent studies on neural operators (such as papers from ICLR 2024) include similar numerical tests, but their results appear more favorable than those shown in Table 2 of this manuscript.

4. I have concerns about the numerical tests in Table 4, as the operators used in the Darcy and Poisson problems are both linear, while the neural operators being tested (FNO, CNO, U-Net, ResNet, DeepONet) are nonlinear. Moreover, the results for the Poisson problem in Table 7 do not demonstrate a significant advantage of CROP over the standard FNO.

### Questions
Please refer to the questions in the weaknesses section.

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
4

### Summary
This paper first pointed out a common misconception that FNO does not depend on the resolution of input. The authors proved that resolution DOES affect FNO and defined a metric, discretization mismatch error (DME), to quantify the effect of resolution changing. Then they proposed a solution to mitigate the issue that ensures FNO's high performance across different resolutions.

The author provided estimation of DME by mathematical analysis. 
Lemma B.1. provides the estimation of difference between input functions of FNO layers at different resolution $N$ and $M$, which is bounded by $o(\frac{1}{N^{s-1}})$ assuming $N<M$ and $s\geq2$. Lemma B.2. extended the analysis of Lemma B.1. to neural operators with lifting and projection layers.

They proposed a solution, cross-resolution operating learning pipeline (CROP), which relies on 1x1 convolution as lifting and projection layers.
Then the authors conducted experiments to show two superior aspects of CROP: cross-resolution tasks and learning capability.

### Strengths
**Originality** Though the development of neural operators has been accelerating recently, some fundamental concepts need clarification. I really appreciate the contribution of this paper that addresses the particular misconception of cross-resolution ability of FNO and puts neural operators on solid ground. The solution proposed here is based on band-limited function spaces and implemented as 1x1 convolution.

**Quality** The mathematical analysis is solid and experiment is persuasive. 

**Clarity** I find the paper clear to read and carefully composed.

**Significance** is relatively high. Cross-resolution application is a favorable feature of neural operators like FNO. The price to pay for such feature should be reminded for researchers in this field.

### Weaknesses
Since your work is to some degree a direct challenge to part of the arguments in [1], can you provide some insights to their evidence of "discretization invariance" that contradicts your findings? Namely, in Section 7 of [1], several experiments support the argument "the error of FNO is independent of resolution or any specific discretization", see Fig. 8 and Table 2&3. How would you explain such results?

Specifically, the experiments in [1] demonstrate that when training and testing are performed at the same resolution, the FNO exhibits consistent performance across various resolutions. This seems to contradict the claim that FNO's performance is significantly affected by changes in resolution. The paper should address this discrepancy more directly by explaining why the observed 'discretization invariance' in [1] does not extend to cross-resolution scenarios. A more detailed discussion of the specific experimental setups in [1] and how they differ from the cross-resolution tasks considered in this paper would be beneficial. Furthermore, it would be helpful to clarify whether the 'discretization invariance' discussed in [1] is a property of the specific datasets or tasks used, or if it is a more general characteristic of FNOs under certain conditions. This clarification is crucial for understanding the scope and limitations of the proposed CROP method.

### Questions
N.A.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper addresses the challenge of discretization mismatch errors (DMEs) in neural operators, particularly FNOs. The authors identify that while FNOs are theoretically designed to be discretization-invariant, they still exhibit performance inconsistencies across different resolutions due to DMEs. I like that they also provide a thorough mathematical analysis of how these errors accumulate through the layers of the neural network. To address this issue, they propose a novel Cross-Resolution Operator-learning Pipeline (CROP). CROP introduces lifting and projection layers that map input and output functions to and from a band-limited function space, allowing the use of fixed discretization's in the latent space. This approach effectively minimizes DMEs and enables consistent performance across different resolutions. The authors demonstrate CROP's effectiveness through extensive experiments on various partial differential equations, including the Navier-Stokes equation at high Reynolds numbers. Results show that CROP not only achieves robust cross-resolution performance but also outperforms baseline models in learning complex dynamics. Overall, this paper contributes significantly to the field of neural operators by addressing a critical limitation and proposing a solution that maintains the advantages of FNOs while overcoming their resolution-dependent weaknesses. As a person who works primarily on Neural Operators, I figured someday someone would finally do this work: ) and talk about it. I do have certain questions and concerns but overall, i really enjoyed the presentation of this paper.

### Strengths
1. Analysis: The paper  identifies and provides a rigorous theoretical analysis of discretization mismatch errors (DMEs) in neural operators, particularly FNOs, addressing a critical gap in the field. The results do make sense to me as it makes sense that although FNO does have the discretization invariance property, just training on low res - isnt guaranteed enough to get the high level features in high -res images.
2. Unique solution: The proposed CROP method effectively mitigates DMEs through a clever use of lifting and projection layers, allowing for consistent cross-resolution performance and flexibility in choosing intermediate neural operators. 
3. Strong empirical validation: Extensive experiments across multiple PDEs, including challenging cases like high Reynolds number Navier-Stokes equations, demonstrate CROP's superior performance compared to state-of-the-art baselines.
4. Clear exposition and reproducibility: I like the fact that the paper is well-structured, clearly written, and provides detailed information on experimental setups, enhancing understanding and reproducibility of the results as well as they don't just bash FNO's, they actually justify their reasons well.

### Weaknesses
Some weaknesses
1. Variance in some results: Some empirical results, particularly in Figure 3b, show high variance. Maybe some explanation of the high variance?
2. There's minimal discussion on how sensitive CROP is to hyperparameter choices, which is important for understanding its robustness and ease of application to new PDE problems
3. Long-term stability in time-dependent problems: For time-dependent PDEs like Navier-Stokes, there's limited discussion on the long-term stability of CROP predictions over extended time horizons.
4. Limited exploration of high-frequency information: While CROP addresses the issue of DMEs, the paper doesn't deeply explore how effectively it captures high-frequency information, especially in comparison to methods specifically designed for super-resolution tasks.
5. It would be also great to have pseudocode or the full architecture.

### Questions
I have several questions so please bare with me:
1  - So, is CROP still a universal approximation for operators? It seems like its not but I may be mistaken.
2 - I do understand the concept of band limiting and then learning a NO in the intermediate representation, but to be more fair in comparison to FNO for high Reynolds tasks, you should use higher number of modes to capture those details or use something like an Incremental Fourier Neural Operator [1]. It would be great to do some ablation studies on that if you have the time. 
3 - How sensitive is CROP's performance to the choice of band-limit in the lifting and projection layers? Is there a systematic way to determine optimal band-limits for different types of problems?
4 - How does the computational complexity of CROP compare to standard FNO, especially for very high-resolution inputs?
5 - How does the choice of intermediate neural operator in CROP affect its performance and computational efficiency? Are there certain types of problems where specific architectures are preferable?
6 - Also I do get you have additional experiments on deeper FNO's but it would be great to actually also use skip connections or other techniques to actually train them well. They do suffer from convergence issues.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper emphasizes that the colloquial definition of discretization invariance does not align with the formal definition. They also demonstrate both formally and empirically that popular operator learning architectures (such as FNO) do not have constant performance across resolutions for many problems. The authors propose the CROP method to address these issues with bandlimited lifting and projection operators (as well as some pointwise operators to capture high frequency details), and they show improved performance compared to popular neural operator architectures.

### Strengths
The paper is well-written, especially for those who may not be experts in neural operator theory. I appreciate the formal definition of discretization invariance from Kovachki et al., 2021 and the discussion of the differences between this definition and the colloquial definition. The experimental results are also quite compelling and suggest that the proposed CROP method vastly outperforms other methods.

### Weaknesses
Although the paper has some strengths, there are still some areas of improvement. My first concern is with the novelty of the insights about discretization invariance. Previous works have included similar discussions, such as [1] (See Figure 1 and Section 2), which uses the term “discretization convergence” to refer to the formal definition by Kovachki et al., 2021. Prior works have also demonstrated empirically that FNO performs well in zero-shot super-resolution tasks on smooth problems. Given these results, it seems to me that the primary contribution of this work is some theoretical analysis of the discretization mismatch error (the Lemmas in the appendix) and the CROP method.

In regards to the proposed CROP method, it is unclear to me whether high frequencies are adequately being captured by the proposed pointwise neural network in the projection layer. For some problems, looking at the L2 error may not be sufficient to ensure that high frequencies are captured. As such, I would recommend the authors include additional evaluation metrics, such as plotting the spectrum of each and seeing how CROP vs. FNO perform on the higher frequencies (for reference, see Figure 1 in [1]).

I also have some concerns about the statement of Proposition 4.4. I understand that it is meant to be written informally for a broad audience. However, I believe some aspects of it are potentially misleading: for instance, it is not necessarily always true that the discretization mismatch error must increase with the higher resolution, right? If the operator learns a constant function, for instance, then this would not strictly increase.

**References:**
1. “Neural operators for accelerating scientific simulations and design” (2024).

**Minor notes and typos:**
1. The authors write that “The FNO architecture is not limited to rectangular domains, periodic functions, or uniform grids.” I think this might be a bit misleading, since typical instantiations of FNO are limited by these constraints: the FFT can only be applied on uniform grids, without Fourier continuation, the output of the FNO is periodic, etc. It would be ideal if the authors can add some context to this claim.
2. Typo in line 234 “aN FNO.”
3. I see that the appendix contains proofs of rigorous statements. I would clearly denote that Proposition 4.4 is informal.

### Questions
1. In the introduction, the authors claim that “It is widely believed that training an FNO on one resolution allows inference on another without degrading its performance, since FNO operates and parameterizes the kernel on the Fourier space.” Do you have references for this claim?
2. What is L in the equation in Definition 4.1?
3. In Proposition 4.4, it is stated that the discretization mismatch error increases with M, but M does not seem to appear in Lemma B.2. I may be missing something, but how does Proposition 4.4 follow from Lemma B.2?
4. How much were the hyperparameters tuned for the baselines, particularly in the Navier-Stokes setting?
5. What architectures were tested for the intermediate neural operator in CROP?

### Soundness
3

### Presentation
3

### Contribution
2

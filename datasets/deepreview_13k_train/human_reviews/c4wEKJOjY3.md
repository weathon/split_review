# Out-of-distribution Generalization for Total Variation based Invariant Risk Minimization

- Decision: Accept
- Scores: 6, 5, 6, 3

## Abstract
Invariant risk minimization is an important general machine learning framework that has recently been interpreted as a total variation model (IRM-TV). However, how to improve out-of-distribution (OOD) generalization in the IRM-TV setting remains unsolved. In this paper, we extend IRM-TV to a Lagrangian multiplier model, named OOD-TV-IRM. We find that the autonomous TV penalty hyperparameter is exactly the Lagrangian multiplier. Thus OOD-TV-IRM is essentially a primal-dual optimization model, where the primal optimization reduces the entire invariant risk and the dual optimization strengthens the TV penalty. The objective is to reach a semi-Nash-equilibrium where the balance between the training loss and OOD generalization is kept. We also develop a convergent primal-dual solving algorithm that facilitates an adversarial learning scheme. Experimental results show that OOD-TV-IRM outperforms IRM-TV in most situations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes to learn the penalty term $\lambda$ in IRM-TV using a neural network to improve the OOD generalization performance of IRM-TV. As $\lambda$ is associated with the feature extractor $\Phi$, which also requires learning, $\lambda$ and $\Phi$ are learned alternatively via minimax adversarial learning. Experiments on a simulated dataset and real-world datasets show that learning $\lambda$ can improve IRM-TV's performance when distribution shifts.

### Strengths
1. Developing methods to learn $\lambda$ is important to improve IRM, which is a commonly used algorithm in OOD generalization. 
2. The proposed minimax adversarial learning is novel and looks like a promising method to learn $\lambda$ well. 
2. The writing is clear to follow.

### Weaknesses
My concern mainly falls in the experimental results:
1. The experiment seems only to be performed once as no standard deviation of the performance is reported. 
2. Adversarial learning could be hard to converge. Analysis like Figure 1 on real-world datasets could be given to facilitate the understanding of how capable OOD-TV is when facing larger $\Phi$ and more complex datasets.

Another major concern (maybe the biggest) I would agree with the reviewer Hkpi  is that the math in the paper is really hard to follow: (On the other hand, it is evident that the value of a work shall not be judged based on the citations only, there are many first works ignored by the community because of lack of PR resources especially in the field of AI).

1.1 Take the definition for the total variation for example, In Eq (5), where is $s$ in the formula to be integrated? The conclusion that "this formulation shows the TV integrates allover all the contours of the function, reinforcing its capability in capturing piecewise-constant features" is a bit confusing here. It is suggested to add figures in the appendix to illustrate it.

1.2 In Eq (8), the usage of the symbol "<-" creates some burdens for people to quickly understand it. This symbol has many meanings. It could be approximating as time step proceeds or giving values to. People maybe able to read it by reading more texts in the main paragraph. But it indeed creates much unnecessary burdens which may not be hard to be fixed.

1.3 The same applies to line 162. Maybe using the term "measure" is more rigorous, but it does not help the readers to quickly get what the method is doing, and how it is different from previous methods used.

1.4 In Line 234, the paper tries to explain why the method works from the perspective of game theory, which is more concrete than the abstract and introduction parts. The authors can consider majorly revised the paper to improve the readability.

1.5 There are many examples like this.

However, the above issue may not deny the technical contributions of this paper. This paper is suggested to make improvements in writing for clarity.

### Questions
1. Is there any repetition of experiments presented in section 4.2 to 4.4?
2. How do $g(\Psi, \Phi)$, $h(\Psi, \Phi, \rho)$, $||\Phi^{(k+1)}-\Phi^{(k)}||_2$ and $||\Psi^{(k+1)}-\Psi^{(k)}||_2$ change in real-world datasets as training goes by? Are $g(\Psi, \Phi)$ and $h(\Psi, \Phi, \rho)$ able to converge and how long does it take to converge?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
Previously proposed Invariant Risk Minimization aims to extract invariant features across different environments to improve the generalization and robustness of the model.  A recent work reveals that the mathematical essence of IRM is a total variation (TV) model. TV measures the locally varying nature of a function, which is widely applied to different areas of mathematics and engineering, such as signal processing and image restoration. In this paper, the authors proposed to generalized versions of IRM with the TV framework and demonstrates the improvements of IRM.

### Strengths
The generalized framework of IRM provides a novel perspective for IRM and provide new possibilities for improvements.

### Weaknesses
There are several weakness for this paper.

1.The performance improvements are quite marginal. As shown in Table 3, the TV framework IRM can only outperform baselines by a slight margin. Besides, as shown in Figure 1, the curves are quite close with each other. It is suggested to add experiments to demonstrate what the previous IRM cannot do while the novel proposed IRM is good at.

2.It is not clear why this framework demonstrates improvements. As min-max optimizes on the worst-case scenarios, is it possible this could bring potential overfitting issue. Additionally, there are already lots of paper incorporating min-max optimization procedure into IRM. By googling, it can be found that these following papers all use minimax methods and invariant learning:
[1]Heterogeneous risk minimization
[2]Invariant risk minimization games

3.No comprehensive experiments on OOD generalization are conducted. This paper only evaluate on the spurious correlation dominated datasets. It can also evaluate the methods on diversity shift dominated datasets with widely-used OOD generalization evaluation benchmark, such as ood-bench. It is known that the IRM cannot deal very well on diversity shift dominated datasets. This can potentially strengthen this paper to point  out clearly the advantage of the proposed method.

### Questions
See weakness.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies invariant risk minimization by introducing an additional penalty named TV penalty. The proposed TV penalty aims to quantify the global variation of a function and further enhance the performance of IRM. To realize such a penalty, the authors propose to leverage additional learnable parameters and train them in an adversarial manner. As a result, the learning performance and be further improved thanks to the variance penalty and enforces learning of invariant features. Through extensive quantitative results, the effectiveness of the proposed OOD-TV-IRM is carefully justified.

### Strengths
- By incorporating an additional penalty with learnable parameters, the proposed methodology is novel and interesting. The introduction of TV penalty is also novel in the field of invariant learning.
- The proposed method is theoretically justified, which ensure the training stability when adversarial process is incorporated.
- The writing is clear and sound, it is not hard to understand this paper.
- Experimental results shows satisfactory improvement compared to baseline methods.

### Weaknesses
 - Motivation needs to be further justified. It is interesting to introduce such a novel penalty to invariant learning. However, it is unclear that why such a penalty is beneficial compared to other techniques, such as ZIN. If such a penalty applies stronger regularization to extract invariant features compared to other methods, the intuitive reason should be further explained. Specifically, the paper lacks a clear explanation of how the Total Variation (TV) penalty encourages the learning of invariant features, and why this approach is superior to existing methods that also aim to minimize spurious correlations. The connection between the global variation quantified by the TV penalty and the desired invariance is not sufficiently established.
- Introducing additional parameters just for a penalty is not computationally friendly. If the application is for large-scale machine learning problems, such a method would be unfavorable. Moreover, it requires extra effort on deciding the hypothesis class of the parameters. The paper does not provide a detailed analysis of the computational overhead introduced by these additional parameters, nor does it discuss the sensitivity of the method to the choice of the hypothesis class for these parameters. This raises concerns about the practical applicability of the method, especially in resource-constrained settings or when dealing with high-dimensional data.
- Limited number of baseline methods. There are only a few baselines are chosen for comparison. It would be better if more recent and state-of-the-art invariant learning methods are considered. The experimental evaluation would benefit from a more comprehensive comparison against a wider range of state-of-the-art invariant learning methods. The current selection of baselines does not fully demonstrate the competitive advantage of the proposed method, especially in comparison to methods that have shown strong performance in recent literature.
- Computational efficiency of the proposed method is not discussed. The paper lacks a thorough discussion of the computational complexity and runtime performance of the proposed method. This is a crucial aspect for assessing the practical feasibility of the method, especially when considering its application to large-scale datasets. A detailed analysis of the time and space complexity, as well as empirical runtime comparisons, would be necessary.
- Missing some related references:  
Huang et al., Harnessing Out-Of-Distribution Examples via Augmenting Content and Style, in ICLR 2023.  
Yang et al., Invariant learning via probability of sufficient and necessary causes, in NeurIPS 2023.    
Xin et al., On the connection between invariant learning and adversarial training for out-of-distribution generalization, in AAAI 2023.

### Questions
Please see the weaknesses part.

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
3

### Summary
This manuscript is motivated by the practical challenge of Out-of-Distribution (OOD) generalization within the context of the IRM-TV framework. Specifically, prior work on IRM-TV aimed to interpret Invariant Risk Minimization (IRM) through the lens of total variation models. Despite its theoretical contributions, the previous research did not offer any concrete algorithms or practical solutions to tackle the OOD generalization problem (according to the authors' assertion)—an area where IRM is often regarded as a classic approach.

In response to this gap, the current study introduces OOD-TV-IRM, an innovative methodology that builds upon the insights drawn from IRM-TV. The authors highlight a critical observation: that the penalty parameter, which plays a vital role in regularization, should be tailored to vary across different extractors. This consideration is particularly important for effectively addressing the nuances associated with OOD tasks.

To implement this idea, the manuscript employs a neural network to dynamically fit the penalty parameter, thereby ensuring adaptability in response to the model's requirements during training. The proposed model engages in an adversarial training process, balancing empirical risk with the total variation penalty. This strategic approach not only enhances the model's robustness but also facilitates its generalization capabilities.

To validate the effectiveness of their proposed method, the authors conducted experiments using several toy datasets. These datasets serve as controlled environments that allow for a clear examination of the model's performance and its ability to generalize to unseen distributions. The results presented in the manuscript demonstrate the potential efficacy of OOD-TV-IRM in navigating the complexities of OOD scenarios, thus contributing valuable insights to the field.

### Strengths
1. The manuscript is commendably well written, providing a clear and logical progression of ideas. The motivation behind this study is articulated effectively, emphasizing the goal of addressing the shortcomings present in prior research. This clarity helps to engage the reader right from the beginning, setting the stage for a meaningful exploration of the topic at hand. Additionally, I would like to highlight Section 2, which is particularly well-executed. This section offers valuable insights and serves as an excellent guide for understanding the core concepts of the Invariant Risk Minimization through Total Variation (IRM-TV) framework. The organization and clarity in this section significantly enhance the reader's ability to grasp the foundational ideas that underpin the subsequent analysis.

2. The theoretical analysis presented in this manuscript is notably comprehensive and rigorous. The authors begin with a clear definition of Invariant Risk Minimization (IRM) and Total Variation (TV), systematically leading to the derivation of the IRM-TV formulation. This step-by-step approach allows readers to follow the logical flow of the authors' reasoning easily. Furthermore, the manuscript provides compelling evidence to address the limitations of IRM-TV in effectively managing OOD generalization tasks. By articulating these limitations clearly, the authors lay a solid foundation for the necessity of their proposed method. Subsequently, the manuscript delves into a detailed explanation of the proposed approach, presenting it in a theoretical context. This thorough exploration not only clarifies the mechanics of the new method but also reinforces its relevance in tackling the identified shortcomings of previous works.

### Weaknesses
1. The significance of this work seems to be limited.
2. The contributions of this work are not enough.
3. The necessary summary on the theoretical analysis is missing.
4. The experimental results are not enough.

Concretely,
1. The overall significance of this work to the broader research community appears insufficient. While the manuscript aims to implement an insight from the IRM-TV framework, it does not convincingly demonstrate the explicit advantages of applying this framework specifically to OOD generalization tasks. Assuming that IRM-TV is a significant advancement—although it is yet to gain citations despite being accepted to ICML-24—the manuscript fails to articulate why its implementation in OOD generalization is strategically important. Clarity on this point would greatly enhance the work's relevance to the community.

2. When evaluating the contributions of this manuscript, it seems that they are primarily derived from insights proposed in IRM-TV, along with the design of an adversarial training paradigm. While the thorough theoretical analysis is commendable, it does not present novel findings that advance the field. The approach of using a neural network to fit hyperparameters is a well-established concept, seen in various contexts such as Neural Architecture Search. Without distinctive contributions that push the boundaries of current knowledge, the manuscript struggles to establish a strong impact.

3. The manuscript presents an extensive theoretical analysis, but it suffers from a lack of necessary summarization. The inclusion of many intermediate derivative processes in the main text can overwhelm readers and challenge their ability to follow the core arguments. While the authors do provide remarks at the end of Section 3.2, there is no clear conclusion to encapsulate the preceding derivations effectively. A concise summary that highlights the key findings would greatly enhance the readability and coherence of the theoretical analysis.

4. The experimental results presented in the manuscript are insufficient to draw robust conclusions. This inadequacy arises from two dimensions: the choice of datasets and the range of methods for comparison. The authors primarily use simulated toy data, CelebA, and Landcover for evaluation, yet they neglect to include mainstream datasets commonly used in the OOD community, such as NICO and Colored MNIST. Given that IRM is known to perform well in scenarios involving correlation shifts, it is imperative to include datasets that exemplify these characteristics—for instance, NICO and Colored MNIST should be at least considered. Furthermore, expanding the range of compared methods would enhance the significance of the experimental findings. Including additional baseline approaches would provide a more comprehensive understanding of the proposed method’s performance relative to existing techniques.

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
2

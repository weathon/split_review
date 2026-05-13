# MAP: Multi-Human-Value Alignment Palette

- Decision: Accept
- Scores: 8, 8, 8

## Abstract
Ensuring that generative AI systems align with human values is essential but challenging, especially when considering multiple human values and their potential trade-offs. Since human values can be personalized and dynamically change over time, the desirable levels of value alignment vary across different ethnic groups, industry sectors, and user cohorts. Within existing frameworks, it is hard to define human values and align AI systems accordingly across different directions simultaneously, such as harmlessness, helpfulness, and positiveness. To address this, we develop a novel, first-principle approach called Multi-Human-Value Alignment Palette (MAP), which navigates the alignment across multiple human values in a structured and reliable way. MAP formulates the alignment problem as an optimization task with user-defined constraints, which define human value targets. It can be efficiently solved via a primal-dual approach, which determines whether a user-defined alignment target is achievable and how to achieve it. We conduct a detailed theoretical analysis of MAP by quantifying the trade-offs between values, the sensitivity to constraints, the fundamental connection between multi-value alignment and sequential alignment, and proving that linear weighted rewards are sufficient for multi-value alignment. Extensive experiments demonstrate MAP's ability to align multiple values in a principled manner while delivering strong empirical performance across various tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work studies the problem of aligning multiple human values in generative AI systems. The key challenge is the potential conflicts between human values, which require the model to adapt in varying directions. To address this, the authors propose to first define each value principle as a constraint in model optimization process. They demonstrate, through a primal-dual approach, that this constrained optimization problem is equivalent to optimizing a linear combination of multiple values. Their analysis shows the proposed method could reach the Pareto Frontier. The optimization problem is solved via gradient ascent approach. An extensive evaluation on two datasets with multiple value dimensions show that the proposed method could adjust the model to reflect diverse human preferences.

### Strengths
The proposed constrained formulation to address multiple value alignment problem introduces a novel perspective, and their primal-dual analysis shows an interesting mapping between such formulation and a linear weighted combination formulation. Both theoretical analysis and experiment evaluations are comprehensive, showing the generality and applicability of the proposed approach in realistic cases. Overall, this paper is of high quality with clear presentation.

### Weaknesses
One minor issue is about the interpretability of the approach. Despite some discussions on interpretations of $\lambda$ and value palette c, their practical implications and selection criteria are unclear. Specifically, the paper lacks a clear methodology for setting the value palette c, especially when dealing with classifier-based rewards. For instance, if the goal is to make the model align with value A more often, the paper does not specify how to translate this into a concrete numerical value for the constraint. The paper mentions using quantiles, but it is unclear how these quantiles should be chosen to achieve a desired level of alignment. Furthermore, the paper does not discuss the potential impact of the choice of quantiles on the final performance of the model. Another limitation is the reliance on a numerical representation for each human value, either obtained from pre-trained models or from human evaluations. However, such dependency is a constraint shared by many existing work, and falls beyond the scope of this work.

### Questions
1. Regarding Remark 2, could the authors clarify how to select the value palette c? For a classifier-based approach, how to set the log probability, if the objective is to make the model align with value A 20% more often than before tunning?
2. Following Question 1, if there are 3 values {A, B, C}, how to set the constraint c, if  the goal is to achieve an order A>B>C? where the model should prioritize value A alignment, follow B if A is satisfied, and align with C is both A and B are respected? 
3. In the simulation experiments, since the rewards for values come from pre-trained classifiers in the form of log probabilities, would an additional step for bounding or normalization be necessary?
4. In section 3.3, $\lambda$ is sampled randomly instead of c, despite $\lambda$ being uniquely dependent on c. Could the authors clarify the reasoning behind this choice?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces MAP, a novel approach for aligning generative AI systems with multiple human values, addressing the complexity of value trade-offs through an optimization framework with user-defined constraints. It provides a theoretical analysis of value trade-offs, sensitivity to constraints, and establishes the sufficiency of linear weighted rewards for multi-value alignment, supported by extensive empirical studies demonstrating MAP's effectiveness across various tasks. The paper contributes to the field by offering a structured method for value alignment that holds potential for positively impacting complex decision-making domains, with future work suggested to extend MAP's application to empirical risk calculations using mixed data sources.


However, to further strengthen the paper, the authors could provide more insights into practical challenges such as scalability, robustness to reward model uncertainties, and handling of non-linear value interactions. Additionally, a deeper exploration of ethical considerations and user guidance for feasible value palette specification would enhance the impact and applicability of the approach in real-world settings.

### Strengths
s1 
The paper introduces a novel and principled formulation of the multi-human-value alignment problem. By introducing user-defined value palettes and framing alignment as a constrained optimization task, they provide a flexible and interpretable method for aligning AI models with complex human value systems. Meanwhile, the problem setup, i.e. a “Pallette”, also allows a user-friendly framework for future adaptation in real case alignment applications. 

s2
The paper makes rigorous theoretical analysis of the problem and corresponding solutions,  including proofs of key properties such as the equivalence of realizable value levels between MAP and traditional RLHF methods. It demonstrates that linear combinations of individual reward functions are sufficient to capture the entire Pareto frontier in the value space(like shown in Theorem 3), which is a significant insight for multi-value alignment. 

s3 
The introduction of primal-dual method as a solution is both natural and practical.  The algorithm includes feasibility checks for user-specified value palettes and provides guidance on adjusting infeasible palettes, making it applicable in real-world scenarios where computational resources and feasibility constraints are critical.

### Weaknesses
w1
While the paper discusses the efficiency of the primal-dual approach, it does not thoroughly address how the computational complexity scales with larger models (e.g., models with hundreds of billions of parameters) or with an increasing number of value dimensions. Practical implementations on very large-scale models may face computational challenges.

Generally the primal-dual method requires the computation of gradients with respect to the dual variables (λ), which involves expectations over the model's outputs. When dealing with large models or a large number of human values (i.e., higher-dimensional λ), the computational burden increases. Specifically, the need to compute gradients with respect to λ, which are expectations over model outputs, can become prohibitively expensive as the dimensionality of λ increases. This is because each gradient computation requires sampling from the model, and the number of samples needed for a reliable estimate grows with the number of values. Therefore it will be helpful if the paper introduces more experimental study with larger models and settings with more values and discusses the performance of the methods when it scales.

w2
The primal-dual method relies on accurate reward functions (r_i) to guide the optimization. If these reward functions are noisy, biased, or mis-specified, the dual variables λ may be estimated incorrectly. This can lead to suboptimal or unintended alignments. The paper should explore the sensitivity of the method to such inaccuracies. For example, if the reward model for a specific value is consistently over- or under-estimated, how does this affect the final alignment? Also, computationlly, the primal-dual solution settings may have certain infeasible inputs(like stated in section 2.3 as well), this might further limit the application of complicated value alignment cases.

w3
This is related to w2. Generally, the concavity of the dual function is crucial for guaranteeing convergence to a global maximum using gradient ascent. However, in practice, especially when dealing with large scale foundation models, which may present non-convex loss landscapes, the assumptions may not hold strictly. The paper assumes that the dual function is concave, but it does not discuss the potential impact of non-convexities in the underlying model's loss landscape on the convergence of the primal-dual method. Also as described in equations(7) and equations(8), the expectations are approximated with finite samples, which may introduce not only errors but also non-convexities. And this may lead to unconvergence of the primal-dual method. It will be helpful if the paper could also provide discussion and empirical studies over these concerns. Also, though might be very hard, it will be great if the paper could provide a theoretical discussion concerning the convergence of the primal-dual solution in the paper’s setting, or empirically show if off-the-shelf models generates convergence problem(like saddle points) and how to deal with them.

### Questions
As most technical concerns are addressed in strong points and weak points, here are some questions and further comments:
* How does MAP perform when reward models are uncertain or biased? Are there mechanisms within MAP to mitigate negative effects from mis-specified rewards or to assess the robustness of the alignment?
* Like stated in section 2.3, "MAP either prompts the user to adjust the value palette or automatically modifies 𝑐 c to ensure feasibility.”, is there any quantitative/qualitative guidance for users to adjust their value to enhance usability? If yes, what are the technical framework?
* To deal with the computational overhead and scalability problem, is it feasible to further adapt the primal-dual method with a more stochastic manner or make it a bi-level optimization primal-dual setup?

### Soundness
3

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
4

### Summary
This paper introduces MAP, a novel approach for aligning AI with multiple human values. MAP formulates alignment as a primal-dual optimization problem with user-defined constraints, allowing precise adjustment of alignment levels based on specific user-defined values. The authors provide a robust theoretical analysis, including quantification of solution representation, sensitivity to variations in the value palette, and the feasible operational range. Extensive experiments demonstrate MAP’s effectiveness in aligning multiple values across models like OPT-1.3B and Llama2-7B-chat.

### Strengths
1. The theoretical foundation of MAP is robust.
2. The paper includes comprehensive experimental validation, comparing MAP with baseline methods and demonstrating its capacity to achieve desirable alignment results.
3. The paper is well-organized, with a clear presentation of the main ideas, making it easy to follow.

### Weaknesses
My primary concerns relate to practical implementation issues.
1. When the value palette is infeasible, the automatic adjustment process gradually reduces the target values toward the model's original performance. However, it's not clear how often infeasible palettes occur in practice and how much adjustment is typically needed. Additionally, the adjustment process requires extra calculations and iterations, which could become computationally intensive, particularly in high-dimensional, multi-value alignment scenarios. The authors should provide empirical results on these aspects and analyze and report on the computational complexity of the adjustment process for different numbers of values being aligned. 
2. The decoding option is time-consuming, although it appears to offer better performance. Could you provide runtime comparisons between the decoding and finetuning options for different model sizes and numbers of values being aligned, along with corresponding performance metrics?

### Questions
In the decoding option, could different sample sizes $m$ affect final performance? Increasing sample size could improve performance but would also increase computational cost, suggesting a potential tradeoff. Could the authors elaborate on this?

### Soundness
3

### Presentation
4

### Contribution
3

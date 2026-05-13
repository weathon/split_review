# GeoLoRA: Geometric integration for parameter efficient fine-tuning

- Decision: Accept
- Scores: 6, 8, 6, 5

## Abstract
Low-Rank Adaptation (LoRA) has become a widely used method for parameter-efficient fine-tuning of large-scale, pre-trained neural networks. However, LoRA and its extensions face several challenges, including the need for rank adaptivity, robustness, and computational efficiency during the fine-tuning process. We introduce \ALGNAME{}, a novel approach that addresses these limitations by leveraging dynamical low-rank approximation theory. \ALGNAME{} requires only a single backpropagation pass over the small-rank adapters, significantly reducing computational cost as compared to similar dynamical low-rank training methods and making it faster than popular baselines such as AdaLoRA. This allows \ALGNAME{} to efficiently adapt the allocated parameter budget across the model, achieving smaller low-rank adapters compared to heuristic methods like AdaLoRA and LoRA, while maintaining critical convergence, descent, and error-bound theoretical guarantees. The resulting method is not only more efficient but also more robust to varying hyperparameter settings. We demonstrate the effectiveness of \ALGNAME{} on several state-of-the-art benchmarks, showing that it outperforms existing methods in both accuracy and computational efficiency.
\footnotetext[1]{{
This manuscript has been authored by UT-Battelle, LLC under Contract No. DE-AC05-00OR22725 with the U.S. Department of Energy. The United States Government retains and the publisher, by accepting the article for publication, acknowledges that the United States Government retains a non-exclusive, paid-up, irrevocable, world-wide license to publish or reproduce the published form of this manuscript, or allow others to do so, for United States Government purposes. The Department of Energy will provide public access to these results of federally sponsored research in accordance with the DOE Public Access Plan(\url{http://energy.gov/downloads/doe-public-access-plan}).}
\renewcommand{\thefootnote}{\arabic{footnote}}}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper come up with a more efficient and robust variant of low-rank adaptation, GeoLoRA. The intuition is straightforward — existing implementation of low-rank adaptation using gradient descent, which update U, S, V together and the update of S cause the algorithm slow to converge.  

This method proposed GeoLoRA, which integrates rank adaptivity, low-rank optimality, and memory and computational efficiency. This method controls the update of S, supported by theoretical convergence guarantee and error analysis, and various experiment results.

### Strengths
- [Major] Easy to follow, well-written
- [Major] The intuition is straightforward, and the method is simple yet effective
- [Major] The proposed method is supported by many evidence, including theoretical convergence guarantee and error analysis, and various experiment results.
- [Major] The experiments are diverse, including both language tasks and vision tasks.

### Weaknesses
 - [Major] While the figure between L222 and L232 exhibit great performance of GeoLoRA, the improvement caused by GeoLoRA seems to be marginal, especially in Table 2.
- [Major] Some experiment settings are not well-justified. For instance, in Table 2, the authors report the experiment results of GeoLoRA individually, while for others, it seems not. It looks like an unfair comparison, and the reason why GeoLoRA are reported individually should be justified. For Table 3, the results of LoRA are missing; for Table 4, the results of AdaLoRA are missing. More discussion are needed to justify the experiment results.
- [Medium] More baselines are needed, since there exists many LoRA variants.

### Questions
See the weakness section.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The popular finetuning method LoRA is learned as an optimization problem with some variant of gradient descent. However, these may not arrive at the optimal low-rank solution. This issue has been looked into before, but that solution provides a stiff gradient flow. This work first reparameterizes the gradient flow to be non-stiff. Further, GeoLoRA allows for the rank of the LoRA adapters to vary, eliminating the need to specify that hyperparameter. This parameterization only requires a single backward pass rather than multiple which are needed by other methods. Based on a clear theoretical backing, theoretical results follow, with loss descent being guaranteed.

### Strengths
- This work provides a novel way of solving the stiffness/convergence issues in existing LoRA solvers, finding the LoRA factors at around the same rate as full fine-tuning. 
- GeoLoRA, while being more efficient than standard LoRA training, also includes adaptive rank finding, which is the most common alternative AdaLoRA has been shown to do but at a significantly greater cost than GeoLoRA. Finding LoRA-like fine-tuning factors can be done without specifying the rank a prior at nearly the same if not fewer training iterations.
- Experiments showing GeoLoRA converging to around the same number of trainable parameters, with both starting with lesser and greater parameters, depict how this method does work towards decreasing rank if the extra dimensions are unneeded.
- Timing experiments showing a direct efficiency improvement over AdaLoRA in Table 2 strongly defend that this method is an improvement over its alternatives.

### Weaknesses
 - For clarity, the motivation (Section 3) is currently a little lengthy. When reading, there was some expectation that one of these major derivations was part of the GeoLoRA algorithm, and it only became clear that the algorithm's description happened a few pages later. Including either a more complete description of Section 3 at its beginning, another subsection title, or moving some of Section 3 to the appendix/another section would help with readability.


### Questions
- Determining if the rank should be changed is dependent on calculating orthonormalizations of n-by-2r0-sized matrices and SVDs of r-by-r matrices. With r significantly less than n, is it possible to use approximate methods such as power iteration to accelerate GeoLoRA further?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes a new parameter efficient fine-tuning (PEFT) technique based on low-rank adaption with adaptive rank allocation. Existing PEFT methods with adaptive rank allocation either lack optimality guarantees or require multiple backward passes per step---the proposed method, GeoLoRA, only requires a single gradient tape per step and comes with optimality guarantees. GeoLoRA does this by using the low-rank geometry of the adapters and work on matrix differential equations. Empirically, GeoLoRA is more efficient than existing adaptive PEFT techniques and yields higher performance on a variety of benchmarks.

### Strengths
- The paper is well-written and the technique is overall well-motivated. 
- The theoretical support for the proposed method is solid -- the majority of the theoretical results are built on the single-layer case, but Proposition 1 extends this to the general multilayer case. If I understand this result correctly, this implies that GeoLoRA can obtain the optimal rank configuration for arbitrary architectures -- this seems like a particularly strong result to me. 
- GeoLoRA appears to robustly outperform or match existing PEFT methods, and it also seems faster in terms of wall-clock time compared to existing adaptive PEFT techniques. 
- GeoLoRA is robust to changes in the hyperparameters, which is already a substantial improvement over existing techniques.

### Weaknesses
 - This paper could benefit from more discussion of the details of existing methods, and why the best adaptive methods require multiple gradient tapes and what types of guarantees they have. This information is currently summarized in a table. 
- In Table 2, it appears that the same rank allocation configuration is used for every dataset, for each of the baselines, whereas the parameter count of the proposed method varies for different datasets. Can the authors comment on this? 
- In Section 4.1, the authors claim that GeoLoRA can be used for low-rank pre-training, but unless I've missed something, the authors do not present any empirical validation of this claim.

### Questions
I am confused about the results in Table 2. Why do adaptive methods like AdaLoRA only have one parameter count for all datasets? Is this the budget, or is the same configuration used for all datasets?

### Soundness
4

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
2

### Summary
This paper proposes a new LoRA variant, GeoLoRA, which can adaptively allocate rank budget and reduce the computational overhead. They analyze the limitation of low-rank optimization  and imporve LoRA according to the Riemannian gradient flow analysis. They also provide theoretical results about convergence and error bounds. The experiments show that GeoLoRA can improve accuracy and training speed compared to AdaLoRA.

### Strengths
1. The analysis of Section 3 clearly point out the limitation of current low-rank optimization, i.e., the optimality condition for low-rank optimization is that the projection of the gradient to 0. Further analysis shows that parallel optimization may not be able to achieve such optimality condition, indicating the urgency of more advanced methods.
2. The paper describes their methodology very clearly. The readers can easily understand how GeoLoRA is implemented.

### Weaknesses
1. GeoLoRA needs to be validated on larger datasets and models, such as MetaMathQA task and  LLAMA. The authors claim GeoLoRA can converge to an optimal low-rank solution, so they should evaluate GeoLoRA under the settings where LoRA's performance is worse than full finetuning to validate their claim. 
2. The improvements seems to be minor, in some subsets of GLUE, GeoLoRA performs even worse than vanilla LoRA. Moreover, the authors should include more baseline methods (DoRA, LoRA+, PiSSA) in their experiments to show the necessity of adaptive rank allocation (TABLE 2,3,4). 
3. The paper lacks an intuitive explanation of their method. Although there are some formal connections between  Section 3 and Section 4, it's not clear to me why the authors design GeoLoRA. Thus, the theoretical contribution of GeoLoRA is not clear. 

### Questions
1. How to choose a proper $\tau$ and initial rank for GeoLoRA? In Table 7, it seems that you chose different $\tau$ and initial rank for different dataset. Does this suggest that GeoLoRA is sensitive to hyperparameters on visual experiments?
2. The authors provide a toy example to show the  behaviours of different low-rank adaptation strategies. How does they behave in more practical settings? (for example, the settings of Table 2)

### Soundness
2

### Presentation
3

### Contribution
2

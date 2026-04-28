# Stochastic Adaptive Sequential  Black-box Optimization for  Diffusion Targeted Generation

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 6, 5

## Abstract
Diffusion models have demonstrated great potential in generating high-quality content for images, natural language, protein domains, etc. However, how to perform user-preferred targeted generation via diffusion models with only black-box target scores of users remains challenging.   To address this issue, we first formulate the fine-tuning of the targeted reserve-time stochastic differential equation (SDE) associated with a pre-trained diffusion model as a sequential black-box optimization problem. 
Furthermore, we propose a novel covariance-adaptive sequential optimization algorithm to optimize cumulative black-box scores under unknown transition dynamics.   Theoretically, we prove a $O(\frac{d^2}{\sqrt{T}})$ convergence rate for cumulative convex functions without smooth and strongly convex assumptions.  
Empirically,  experiments on both numerical test problems and target-guided 3D-molecule generation tasks show the superior performance of our method in achieving better target scores.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This is the second paper on diffusion for black-box optimization. The previous work, DDOM, trains a conditional diffusion model using a reweighted objective function, and samples conditioning on the maximum y in the dataset and use classifier-free guidance.

The paper proposes to optimize an approximation by first order Taylor expansion and derives a closed-form update formula for the mean and variance of the score, computed by MC sampling. The convergence rate is proven

### Strengths
This paper offers an a method alternative to DDOM for diffusion-based black-box optimization. The method is well motivated and the performance is promising.

### Weaknesses
 - What do you mean by a "full matrix update" and an "adaptive update"? When making claims such as "algorithm is the first full matrix adaptive black-box optimization with x convergence rate," it is important to explain the qualifiers and the relevant literature. Specifically, it's unclear what is meant by 'full matrix' in the context of covariance matrix updates. Does this imply that the method is not making any simplifying assumptions about the structure of the covariance matrix, such as diagonal or low-rank approximations? Furthermore, the term 'adaptive' needs more clarification. Does it refer to adapting the learning rate, the update rule, or some other aspect of the optimization process? It's also crucial to explicitly define what 'x convergence rate' refers to, including the specific metric being used to measure convergence, and how it compares to other methods in the field. Without these details, the claim of being the 'first' is difficult to assess.
 - Can the proposed method be adapted to the tasks studied in DDOM and if so, how do they compare? It would be beneficial to see a direct comparison of the proposed method with DDOM on the same tasks to understand the relative strengths and weaknesses of each approach. This would help to contextualize the contribution of the proposed method and identify scenarios where it might be more suitable than existing alternatives.
 - Page 4 Talor -> Taylor
 - Page 8 larger the score -> higher

### Questions
See weakness

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents method to fine-tune the inference phase of a pre-trained diffusion model as a sequential black-box optimization problem in order to maximize some pre-defined score function. The paper proves a $O(d^2/\sqrt{T})$ convergence rate for cumulative convex functions. Empirically, the proposed method is evaluated on a text-to-image generation tasks and yields higher target scores compared to other approaches.

### Strengths
The biggest strength of the paper lies in its technical novelty and motivation to solve the targeted generation problems with diffusion models using an adaptive sequential scheme. By utilizing the sequential generation structure of diffusion models, the proposed model can "fine-tune" the inference hype-rparameters at each generation step, targeted to some black-bock function by only leveraging the function calls. 

In addition, the proposed approach is proven to achieve some convergence rate for convex functions without smooth or strongly convex assumptions (though I haven't checked the proof and the correctness of the claim).

### Weaknesses
 - The major weakness lies in the clarify of writing, which made it challenging for me to understand the exact mechanism of the method, and to check the claim on the convergence rate. In particular, (1) the indexing of $k$ and $t$ are confusing, and (2) which of the algorithm 1 qnd 2 is the practical algorithm? How are they different? 


- The empirical evaluation is limited and unconvincing. E.g. In Figure 2, the extended dataset (last row) seems to have higher CLIP score, but lower visual quality. (1) While the author briefly touched upon this point and leaves it to future work, this behavior definitely limit the practical use of the proposed method. And I think it is a concern that needs to be well addressed within the scope of this work in order for it to be well-received in the community. (2) Furthermore, , I have reservations regarding whether the proposed method has effectively demonstrated superior practical utility, given that visually the samples from competing methods also align with the generation goal and can have better visual quality despite a lower target score. 

Please see my detailed comments expanding the above two points in the below question section.

### Questions
1. Page 2, section 2.2 third line: "a relax the problem" -> "a relaxation of the problem"

2. Page 2, last paragraph, "Evolution Strategies (ES)", the acronym has been defined and used before.

3. Equation 4: describe the indexing of $t$ and $t+1$.

4. How is the proposed method different from DDOM? 

5.  Section 3 Notation and symbols: a lot of them are introduced without providing the context. For example, in "denote $\bar \mu_k$ and $\bar \Sigma_k$ as the ... for Gaussian distribution", what "Gaussian distribution" is this referring to? And in the following sentence "Denote $\bar \theta_k$ ... as the parameter for optimization", what "optimization"? And "at $t^th$ iteration in optimization", what do you mean by iteration? Is the iteration in optimization the same thing as the generation step in regular diffusion model sampling?

6. Section 3: define $d$ (the dimension of data?)

7. Section 3: what value does $k$ take in (e.g. from 1 to some $K$ , where $K$ is the total of sampling steps)? What does $k$ and $t$ mean practically in $\bar \theta_k^t$? Is one of them the generation step index, and the other the dimension index?

8. Eq 5: from my impression of equation 5, $k$ should index the time step in diffusion sampling. However, here $k$ starts from $0$ which corresponds to random noise, and ends at $K$ which corresponds to the final data sample. But equation (1) (and equation (3)) uses $t$ to denote step and suggests a "reverse-time" manner, which seems not consistent. 

9. When first introduced the black-box target score function $F(\cdot)$ (in the line above equation (6)), describe its argument, as in is it defined for $x_t$ at all steps or just the final one?

10. Page 3 last sentence, should choosing $\{\theta_{k-1}, \theta_{k-1}, \cdots, \theta_1\}$ proceed in a reverse order?

11. Equation 9, I wonder if it is correct to factorize the distribution w.r.t. $\bar \epsilon_k$ across $k$? If I understand it correctly, $\bar \epsilon_{k+1}$ contains $\bar \epsilon_k$ as a sub-component. 

12. How is Algorithm 1 and 2 different from each other?

13. It seems like Algorithm 2 is the one used in practice (e.g. see the summarizing part in Section 1). Then why is it proposed in the Convergence Analysis section instead of the Method section?

14. Algorithm 1: $K$ should be an input argument. It is better to replace $\hat \mu_\phi (x_k, k)$ with $\hat \mu_\phi$ unless the arguments are defined. In the last two lines of the algorithm, what is $t+1$? 

15. Page 7 Section 5.1, what does the subscript $m$ in $f(x) = \sum_{m=1}^d ... x-m2^2$ mean? Is it suppose to index the dimension of $x$? It seems to encode a different meaning of subscript $k$ used before. 

16. In both experiments, how do you choose the total number of steps, and how do you choose the fine-tune steps to present, e.g. tabel 1 (steps =1596, 2646). Are they chosen randomly?

17. Does Figure 2 shows independent draws?

18. While the proposed method (last two panels of Figure2) can achieve a higher target score value, it is not clear that the visual quality is outperforming others, especially we see a deterioration in the last row. I would suggest addressing this concern, also provide other metrics to summarize the performance. 

18.2 Furthermore, considering that the target score is determined by the CLIP score, which measures the proximity to the prompt "a close-up of a man with long hair," it appears that all the samples presented in Figure 2 reasonably align with the objective of achieving this generation goal. In this context, I have reservations regarding whether the proposed method has effectively demonstrated superior practical utility, particularly considering the lower visual quality of the generated content.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed a novel algorithm (stochastic adaptive black box sequential optimization) to generate user targeted samples.   The authors provided a theoretical analysis on the convergence rate as well as other properties.  Empirically, the experiment results on CelebA-HD datasets showed a clear improvement on generating more targeted images.  However, this comes at a cost of perception quality.

### Strengths
The paper has a solid theoretical ground, and proposed a novel approach.  The authors are able to validate the theory by their empirical results.

### Weaknesses
1.  The organisation and writing of the paper need to be improved.  The notations and equations need to be better defined.  For example, the authors should define all terms appeared in equation 1, 2, and 3, such as g(t) and \alpha_t and so on.  The writing made it very difficult for readers to follow the proposed method.  

2.  The loss of perception quality of the targeted generation is a hurdle for this approach to have any practical use.  It'd be better if the authors explored this trade-off a bit further.

### Questions
What do you think has caused the loss of perception quality in the targeted generation? You mentioned the solution could be adding a quality measurement (I'm guessing something like LPIPS)  into the black-box function.  Do you have any insight in what will happen? Would it help the perception quality while keeping the target score high? Or would it be a tradeoff?

### Soundness
3 good

### Presentation
1 poor

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper discusses a significant challenge in performing user-preferred targeted generation via diffusion models with only black-box target scores of users. They address this challenge by formulating the fine-tuning of the inference phase of a pre-trained diffusion model
as a sequential black-box optimization problem. In practice, they propose a stochastic adaptive sequential optimization algorithm to optimize cumulative black-box scores under unknown transition dynamics. Theoretical and empirical evidence are provided to support the method.

### Strengths
* The formulation regarding the fine-tuning of the inference of diffusion models as a black-box sequential optimization problem is sound and novel, which may inspire subsequent works in this area.
* The paper includes an extensive theoretical analysis to validate the convergence of the proposed method and its superior ability to manage non-smooth problems.

### Weaknesses
 * The methodology, as currently presented, might be heavy and unfriendly to the general audience. The authors should aim to articulate their primary contributions and the uniqueness of their proposed methodology more clearly, focusing on how it addresses the identified challenges.
* The empirical results section could be enhanced.
     * The rationale for using text-guided generation as a demonstration of the proposed method is not entirely clear. The authors should elaborate on why they believe this setting poses a challenging black-box optimization score. Does this scorer belong to those touch non-smooth cases? 
    * The quality of generated images is damaged. As evidenced in Figure 2, the generated images of baseline methods are more natural and clear than those of the proposed method. Is there any solution to resolve this problem? 
    * The single-domain experiment on text-guided generation does not sufficiently prove the effectiveness of the method proposed. The authors should consider introducing more diverse black-box scorers to exhibit the method's versatility. For example, DDOM conducted experiments across multiple domains; perhaps a similar approach could be beneficial here.



### Questions
* It is recommended that the authors revise the methodology section to accentuate the main technical challenge they've addressed and the motivation behind their method.
* The derivation process in Equation (10) and how this objective aligns with Equation (8) is not clear. Can the authors provide further clarification on this?
* Certain notations, such as $\alpha$ and $s$ in Section 2.1, lack explanation and should be clarified for reader comprehension.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

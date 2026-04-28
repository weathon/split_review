# Differentiable Causal Discovery for Latent Hierarchical Causal Models

- Decision: Accept
- Avg Score: 6.75
- Scores: 6, 8, 5, 8

## Abstract
Discovering causal structures with latent variables from observational data is a fundamental challenge in causal discovery. Existing methods often rely on constraint-based, iterative discrete searches, limiting their scalability to large numbers of variables. Moreover, these methods frequently assume linearity or invertibility, restricting their applicability to real-world scenarios. We present new theoretical results on the identifiability of nonlinear latent hierarchical causal models, relaxing previous assumptions in literature about the deterministic nature of latent variables and exogenous noise. Building on these insights, we develop a novel differentiable causal discovery algorithm that efficiently estimates the structure of such models. To the best of our knowledge, this is the first work to propose a differentiable causal discovery method for nonlinear latent hierarchical models. Our approach outperforms existing methods in both accuracy and scalability. We demonstrate its practical utility by learning interpretable hierarchical latent structures from high-dimensional image data and demonstrate its effectiveness on downstream tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The main theoretical contribution of the paper is showing identifiability of nonlinear latent hierarchical causal models. Building on this theory, the authors propose a practical differentiable latent causal discovery approach. Experiments are performed on synthetic data as well as the coloured MNIST dataset to demonstrate efficacy of the approach.

### Strengths
1. The paper is, to the best of my knowledge, the first to provide identifiability results for nonlinear latent hierarchical causal models. The proof technique seems correct to me, though I did not check it thoroughly (for example, the appendix).

2. Estimating equation 9 using Donsker-Varadhan representation is novel.

### Weaknesses
1. **Experimental limitations**:

    a. **Synthetic experiments**: Instead of experimenting on just 4 structures given in figure 3, I would encourage authors to randomly generate DAGs and run experiments on these structures. For the synthetic experiments, the analysis would be stronger if the authors also try nonlinear activations for eq 1, instead of piecewise linear activation such as LeakyRELU. Specifically, the use of only LeakyRELU limits the generalizability of the findings, and exploring other common nonlinearities like tanh or sigmoid would provide a more comprehensive evaluation of the method's performance under different functional relationships.

   b. **Real experiments**: The baselines for the experiments on CMNIST are VAE and $\beta$-VAE -- both of which do not learn a structure over latent variables -- when  better baselines exist [1-3]. The choice of baselines is not adequate to demonstrate the advantage of the proposed method. Specifically, methods that explicitly learn a latent causal structure, such as those based on structural equation models or graphical models, should be included for a more rigorous comparison. Applications to real world data is also limited, and even in the colored MNIST setting, only 2 digits seem to be used. The limited scope of the real-world experiments raises concerns about the practical applicability of the method to more complex datasets.

2. **Missing/weak motivation**: It is also unclear why such models are useful in the real world: motivation for why one needs such models would make the paper more strong. In the introduction, causal discovery is motivated but the there is no true causal structure for the CMNIST data. Given this, what is the purpose for obtaining a hierarchical structure as in Fig 2b? For what tasks, is such a hierarchical representation useful? The absence of a clear task or application for the learned hierarchical structure makes it difficult to assess the practical significance of the proposed method. Without a concrete use case, the value of learning such a structure remains questionable.

3. L447 - 453 mentions interventions but key details are missing regarding interventional data generation (single node or multi node interventions, soft vs hard intervention, and intervention values). The lack of specific details regarding the intervention setup makes it difficult to reproduce the experiments and evaluate the method's performance under different intervention scenarios. The type of intervention (e.g., single vs. multi-node, soft vs. hard) and the intervention values can significantly impact the results, and these details should be clearly specified.

4. **Related work**: The task of causal discovery over latent variable hierarchical models is closely related to causal representation learning but this has not been discussed and  works in the space have not been cited [1, 2]. The omission of relevant work in causal representation learning weakens the paper's positioning within the existing literature. The authors should discuss how their work relates to and differs from existing approaches in this area, highlighting the novel contributions of their method.

### Questions
1. What is the implication of condition 3? 

2. There is a typo in equation 8, the number of small norms and large norms do not match.
 
3. From eq 6, we see that $|| M_{i, :} \odot \pi (1 - M_{j, :})||_1 \geq 2$. 

However in the subject to constraint in eq 8, $||M_{i,:}||_1$ times the above entity is enforced to be $\geq 2$. This is a bit unclear -- can the authors clarify?

4. Caption for figure 2c is unclear.

PS: Score has been increased post rebuttal.

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
3

### Summary
This paper shows that are particular class of causal graphs with  hierarchical latent variables are identifiable by leveraging properties of the Jacobian of the conditional exception function between subsets of observed variables. They then present an efficient algorithm for inferring the hierarchical graph. They present strong empirical results on both synthetic & image based problems.

### Strengths
- I thought this was interesting, original work. The class of graphs that they study is obviously limited but seems practical & the rank condition is intuitive.
- The paper is very well written - both the theory and methods section do a good job of explaining the intuition for why the method works
- The empirical results are strong on the datasets that they tested.

### Weaknesses
 * The coloured MNIST results appear very strong (though this is not my area), but not contextualized in the domain generalization literature. I would have at least expected you to report the published numbers from recent work from that setting. Autoencoders & Beta-VAE is not the right baselines?
* I would have liked a more detailed discussion of the learned MNIST graph. I am not sure what to make of figure 4 or table 3 in the appendix? Do those latents make sense? Is there a natural hierarchical structure that we would expect?

### Questions
See weakness above.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Differentiable causal discovery has been a key focus of the causality community in the past years. Despite the advance of representation learning and deep learning, differentiable hierarchical causal discovery with latent variables has been a challenging subfield with at least empirical limited results and limited impact despite the need and call for these methods from practical applications. 

The paper proposes a new method and investigates some of the conditions for identifiability. 

While the paper has some very interesting and promising components, I overall can not recommend it for acceptance in its current form.

### Strengths
I really like that the evaluation is not just done with respect to a causal metric but wrt to "a regression classifier trained on the learned representation". If the causality field would move towards the standard evaluation practices of deep learning progress would be faster and this paper is one of the few which actually does perform this evaluation! 
However, when reading the paper in more detail e.g. Table 1 is then again evaluated wrt to discovery metrics only table 2 is evaluated with a learned classifier and arguably table 2 provides only a very limited setting and very limited evaluation. Especially given that these are deep learning approaches, the performance should not even reported in a table but as plots where the x-axis is training time and the y-axis performance. This would account for complexity and cost of training and really allow for a fair comparison of the approaches. 

While it is argued that causal representations lead to better generalizations and transfers this is so far actually not shown in the literature. DomainBed and or [1] clearly state the need for better evaluation and clearer demonstrations of the benefits beyond deriving identifiability results. I am thus really encouraging the authors to significantly extend the ablations and plot train vs performance curves and the performance of the classifier at different stages of training in a larger scale setting and across significantly more datasets. 

[1] Saengkyongam, Sorawit, et al. "Identifying representations for intervention extrapolation." arXiv preprint arXiv:2310.04295 (2023).

### Weaknesses
The key claimed advantage for better identifiability results comes from the fact that instead it is assumed that "not yet account for structures where measured variables have children".

There is some exchangeability of these assumptions and in that sense I agree that the current assumption is a more practical one but it is not a novel one or a clear contribution until a clear relation between the assumptions is shown. Specifically, the paper does not clearly articulate how this assumption differs from existing approaches that also allow for latent variables, and what specific limitations those assumptions have that this paper overcomes. The paper needs to clarify the exact conditions under which the proposed approach provides a novel contribution to identifiability, and why this particular assumption is more practical than existing ones.

The evaluation is really lacking wrt to datasets and shown clear benefits across different settings. As mentioned I think the authors already take a very valuable step for the community by not only evaluating wrt to discovery metrics (see strengths) but adopting the established evaluation frameworks in deep learning of training a classifier on top of a learned representation. However that evaluation is unfortunately severely limited. The evaluation in Table 2 is performed on a very limited setting, and it does not provide sufficient evidence that the learned representations are truly beneficial for downstream tasks. The paper should include a more comprehensive evaluation with a wider range of datasets and tasks, and it should also provide a more detailed analysis of the performance of the classifier at different stages of training.

### Questions
It seems that the baselines are chosen from one lab only i.e. Xie et al, Kong et al and Huang et al which are used to sell the method are all from one lab. 

Given the number of baselines available for the task that seems a bit strange. Can you please clarify?

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
4

### Summary
This paper introduces a novel differentiable causal discovery method for latent hierarchical causal models (LHCMs) and derives identifiability conditions of LHCMs in non-linear cases with relaxed assumptions (i.e., no requirement of invertible functions). In the experimental evaluation, the authors show promising results outperforming existing methods on synthetic and image data.

### Strengths
- paper is written clearly while keeping a formal discussion of assumptions and theorems
- the authors derive and prove their identifiability conditions. The proofs look correct after careful checking.
- a novel differentiable DAG learner for LHCMs is introduced, allowing differentiable structure learners to be applied in latent variable settings
- the experimental section introduces an interesting experiment on image data that demonstrates that the proposed algorithm can be seamlessly integrated into the autoencoder framework, thus allowing learning of LHCMs on complex and unstructured data such as images

### Weaknesses
 **Section 2**
- the authors discuss "differentiable causal discovery" in the related work. However, most (if not all) works referenced here do not perform causal discovery. This has been shown by several works, e.g., [1], [2]. Specifically, many methods optimize for a score that does not necessarily correspond to causal relationships, and thus cannot be considered causal discovery methods.

**Section 4**
While the theorems and proofs in Sec. 4 are correct, it is unclear to me whether the identifiable model still allows for a causal interpretation if variable permutations are allowed (Theorem 3). It would be good to clarify which permutations are allowed and why the permutations do not change the causal structure (and thus $d$-separation statements). To illustrate what I mean, consider a LHCM (where observed $X$ are dropped for the sake of simplicity) $Z_2 \leftarrow Z_1 \rightarrow Z_3$. If (any) permutation is allowed, Theorem 3 would also allow for $Z_1 \leftarrow Z_3 \rightarrow Z_2$. However, this model entails different $d$-separation statements and thus has different causal semantics. Hence the causal model would not be identifiable. The authors should clarify how the identifiability result aligns with a causal interpretation of the learned graph, given the permutation invariance.

**Section 5**
It is unclear to me how the acyclicity and overall model structure from Condition (1) (ii) is ensured/reflected in the objective (if at all reflected) (Eq. 10). Based on this, it is not easy to see why the proposed method is not just a structure learner, but a causal discovery method. Could the authors please provide more details on how this is achieved? Specifically, how does the optimization procedure prevent the model from converging to a solution that violates the acyclicity constraint, and how does the objective function explicitly encourage the discovery of causal relationships rather than just any structural pattern?

**Section 6**
- Tab. 1: Why do the baselines perform so badly? Is there any specific explanation for that? It would be helpful to understand the limitations of the baseline methods in the context of the specific data and model assumptions used in this work.
- Synthetic experiment: How were the ground truth structures chosen? By hand or randomly? If by hand, could the authors explain why and why these? The choice of ground truth structures can significantly impact the evaluation of the proposed method, and it is important to understand the rationale behind these choices.
- image experiments: There is the work on causalVAEs [3], why did you not choose this as a baseline? Since it is more related to the overall problem setup of this work than standard VAEs, this baseline would make much sense. The lack of comparison with a relevant method makes it difficult to assess the true contribution of the proposed method.

### Questions
see weaknesses

# Additonal Notes
Note that I decided on a score of 6 as there is no option 7. If the authors address the points in the weaknesses section accordingly, I'm inclined to raise my score.

### Soundness
3

### Presentation
3

### Contribution
3

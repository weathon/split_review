# Balanced Neural ODEs: nonlinear model order reduction and Koopman operator approximations

- Decision: Accept
- Scores: 8, 6, 6, 5

## Abstract
Variational Autoencoders (VAEs) are a powerful framework for learning compact latent representations, while Neural ODEs excel in learning transient system dynamics.
This work combines the strengths of both to create fast surrogate models with adjustable complexity. 
By leveraging the VAE’s dimensionality reduction using a non-hierarchical prior, our method adaptively assigns stochastic noise, naturally complementing known NeuralODE training enhancements and enabling probabilistic time series modeling.
We show that standard Latent ODEs struggle with dimensionality reduction in systems with time-varying inputs. 
Our approach mitigates this by continuously propagating variational parameters through time, establishing fixed information channels in latent space. 
This results in a flexible and robust method that can learn different system complexities, e.g. deep neural networks or linear matrices. 
Hereby, it enables efficient approximation of the Koopman operator without the need for predefining its dimensionality.
We demonstrate the effectiveness of this method on academic test cases and apply it to a real-world example of a thermal power plant.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
A method for model order reduction using $\beta$-VAEs and state space NeuralODEs called **balanced neural ODE** is described and tested on a few examples. The hyperparameter $\beta$ controls the number of active latent space dimensions, i.e. the reduced dimension of balanced neural ODE. Two main methods of evolution are proposed for the latent VAE parameters: constant-variance and dynamic-variance. Koopman operator approximation is shown to be a special case of balanced neural ODE.

### Strengths
1. Method is fully described, intuitive to understand, many derivations are fully given
2. Balanced neural ODE outperforms latent neural ODE and is able to learn latent dynamics.
2. Numerical experiments demonstrate the breadth/diversity of application of the method.

### Weaknesses
1. Method combines two existing approaches (however, the combination is novel)
2. Presentation feels brisk at times (might be alleviated with an extra page)
3. The model involves many components with architecture choices, and there is not enough ablation on

### Questions
1. Are there other related works that combine model order reduction and latent space evolution, other than latent ODE?
2. How does the balanced neuralODE compare to Dynamic Mode Decomposition method (for linear operator learning)?

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a novel method, called B-NODE, for time-series modeling of dynamical systems (e.g. power plants). B-NODE is claimed to be fast (in terms of runtime) and accurate (in terms of reconstruction error on the original data). The main idea behind B-NODE is a combination of $\beta$-VAE (for dimensionality reduction) with a Neural ODE (for dynamical systems' modeling). 

The faster runtime of B-NODE results from dimensionality reduction via the VAE. Previous approaches (like standard latent ODEs) fail to provide such dimensionality reduction. B-NODE also claims to offer the user with a knob to balance the trade-off between dimensionality reduction and reconstruction accuracy.

As for the paper structure, section 3 describes the methodology. Sections 4 and 5 demonstrate the advantages of B-NODE on certain synthetic and real-world tasks.

### Strengths
- The paper shows promising results with using B-NODE on certain tasks.
- The paper provides certain handy illustrations and detailed figures explaining their approach.

### Weaknesses
**Technical Weaknesses**:
1. *Limited evaluation.* Since this is a paper that proposes a novel method to solve a problem, the authors should aim to provide a comprehensive suite of experiments showing the advantages of the proposed methodology over existing baselines. The only real-world use case is presented in Section 4.2, which is just one single task. In Figure 5 (in the same section), B-NODE is compared against only one baseline, which is NODE. As a reference, two closely related papers in this field are [1] and [2]. Both provide much more detailed evaluation (Table 3 in [1] and Tables 2,3 in [2]).

**Presentation Weaknesses**: 

1. *Unclear on the main advantage of B-NODE.* Is your main contribution speed of the proposed methodology, or accuracy, or both? It would be good to explicitly state it. The paper abstract mentions the word "fast", but the only runtime comparison I could find was Figure 6(b), which is only discussed briefly in the text in lines 388-392. In contrast, Figures 4,5,7,8 all seem to focus on accuracy via the RMSE.

2. *Vague exposition.* Below I list certain examples where the exposition is vague.

Example 1: The "B" in B-NODE stands for "Balanced", but what exactly is the knob that lets one choose the balance of the trade-off between reconstruction accuracy and latent dimension size?

Example 2: In lines 150-155, how is the $D_{KL}$ measured per channel? The overall $D_{KL}[q(z|x^\mathcal{D})||p(z)]$ is well-defined, but to measure for certain channel $i$, do you measure $D_{KL}[q(z_i|x^\mathcal{D})||p(z_i)]$? Are the marginals on a "channel" $i$ well-defined? It would have been nice to see this in proper notation. 

Example 3: It is unclear what the following statement means: "The VAEs sampling-based robustness complements stability enhancements for Neural ODEs". This statement is mentioned twice, in line 180 (Methodology section) and line 476 (Conclusion section).

Example 4: Line 280 says "state $x_i^z$ is inactive", but no notion of active/inactive-ness is defined? Likely by inactive, the authors mean that the $D_{KL}$ of the $i^{th}$ channel is below the threshold, but this is sloppy exposition.

Example 5: Line 60 (and a few other places) mention that B-NODE *requires* a non-hierarchical prior, but the paper does not explain why this is the case.

Overall, I found the paper difficult to understand. Sentences that follow one another do not necessarily build the same idea in a linear/sequential fashion. This makes it hard to extract what the authors are trying to convey.


```
[1] Naiman, I., Erichson, N. B., Ren, P., Mahoney, M. W., & Azencot, O. (2023). Generative modeling of regular and irregular time series data via koopman VAEs. arXiv preprint arXiv:2310.02619.
[2] Wi, H., Shin, Y., & Park, N. (2024, March). Continuous-time Autoencoders for Regular and Irregular Time Series Imputation. In Proceedings of the 17th ACM International Conference on Web Search and Data Mining (pp. 826-835).
```

### Questions
**Technical questions**:
1. How exactly does B-NODE "balance" between dimensionality reduction and reconstruction accuracy? Is it simply just varying the $\beta$ in $\beta$-VAE? If yes, it would be nice to explicitly mention this. 
2. In equation 4, why is it $q(u_{0:T}^z|u_{0:T})$ instead of $q(u_{0:T}^z|u_{0:T}, p^z, p)$? Since the latter is what one would get from the definition of $x^\mathcal{D}$ and $z$ in line 188. Is it because the external input $u$ is independent of the time-invariant parameters $p$? Is this a standard assumption?

**Suggestions for presentation**:
1. In the first paragraph explaining motivation, it would be nice to present more examples so that the reader can conceptualize the problem. Currently, only the words "yearly energy system simulations" are mentioned as examples.
2. In Figure 4(a), the reader needs to zoom in a lot to read the values of $\beta$ around the markers on the plot. Please make the plots easier to read.

### Soundness
3

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
3

### Summary
This work presents a novel approach combining Variational Autoencoders (VAEs) and Neural ODEs to address model order reduction (MOR) for dynamic systems. The proposed model, named Balanced Neural ODE (B-NODE), utilizes VAEs for latent dimensionality reduction and Neural ODEs for capturing transient dynamics, resulting in a compact, efficient surrogate model that can dynamically adapt to the complexity of input data.

### Strengths
The paper effectively combines Variational Autoencoders (VAEs) and Neural ODEs, leveraging their complementary strengths for dimensionality reduction and transient dynamics modeling. This approach could significantly impact surrogate modeling in dynamic systems.

### Weaknesses
Although the paper acknowledges areas for future work, a more detailed discussion on scenarios where B-NODE might underperform would be helpful. Specifically, it would be beneficial to outline any cases where the model might struggle with particular types of inputs or dynamic systems.

### Questions
- Please provide more comprehansive understanding of β-value?  A discussion of the theoretical implications of different β values
- It seems that β-value is small does it mean that information bottleneck become negligible?
- if you set β=0 what will happen? please discuss the theoretical implications of setting β=0

If the authors can clarify my concern, I could change my opinion.

### Soundness
3

### Presentation
2

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
This paper proposes a novel method called Balanced Neural ODE (B-NODE), which combines Variational Autoencoders (VAEs) with Neural ODEs to reduce the complexity of dynamical systems while maintaining accuracy. This approach extends Latent ODEs to handle time-varying inputs by continuously propagating latent variables. It also aims to approximate Koopman operators by leveraging the weight factor of KL divergence during VAE training. The proposed method is evaluated on both academic and real-world scenarios.

### Strengths
- The problem addressed is both interesting and crucial for applying Neural ODEs to dynamical systems with time-varying inputs. The combination of VAE and Neural ODEs to achieve dimensionality reduction alongside dynamic modeling provides an approach for managing complex systems. 

- The inclusion of real-world test cases adds practical value to the study and demonstrates its potential applicability.

### Weaknesses
## Presentation 
- The layout of this paper is somewhat disorganized, which makes it very hard to follow. The presentation is unclear without a main thread, with complex concepts that are not explained adequately and unnecessary.
- The concepts and some formulations appear to be justified solely by the authors themselves, lacking sufficient external validation or references to prior work (see points in Questions).
- Please ensure there is proper spacing between different paragraphs and sections. 

## Experiments 
- There are no baseline comparisons with Koopman-based models, Neural ODEs, or VAE-based forecasting approaches (which are highly relevant to this work), which limits the ability to assess how much improvement the proposed model actually provides.

## Minor issues 
some examples:
- Lines 100 the integral should be $\int_{t_0}^{t}f_{\phi NODE}(\mathbf{x}(\tau))d\tau$
- Line 225, is -> are
- Line 312, Observed -> observe 

I'd encourage authors redo proofreading.

### Questions
- In line 159, the statement "Combining VAEs with State Space Models leverages VAEs' ability to generalize through an information bottleneck with a numerically pre-determined latent space that promotes data locality and latent orthogonality" is unclear. Specifically, what is meant by "data locality" and "latent orthogonality"? Could the authors provide further explanation, relevant citations, or supportive numerical results to clarify these concepts?

- Could author further explain how they arrive equation (4ba)? You assume that the $x_0^z$ only related to initial state $x_0$?

-  Lines 297-299: Could the authors further justify why they do not need to pre-determine the dimensionality of the latent space? The weighting factor might contribute to sparsity in certain contexts, but it is unclear how it directly adapts the dimensionality. Additional explanation on this point would be helpful.

### Soundness
3

### Presentation
2

### Contribution
2

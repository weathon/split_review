# A Probabilistic Approach to Optimizing Hardware Control Parameters in System Property Estimation using Gumbel-Softmax

- Decision: Reject
- Scores: 3, 3, 3, 3, 3

## Abstract
Optimizing control parameters is crucial to estimate reliable tissue characteristics in quantitative MRI. Basically, multiple hardware parameters are simultaneously controlled to generate a signal from MRI system. Repetitive acquisitions with different control parameter combinations create distinct signal modulations and then tissue characteristics are deduced from prior knowledge of physics-based relationship among modulated signals, control parameters, and tissue characteristics. The choice of control parameters, which determines the attribute of signal modulation, directly impacts the inverse problem in tissue characteristic estimation. Thus, the multidimensional control parameter optimization remains an open research topic in MRI field for accurate analysis of tissue characteristics. Typically, optimal parameters are determined by iteratively updating sets of control parameters to maximize the estimation accuracy of the tissue characteristics. However, the conventional optimization process is restricted to explore only the vicinity of control parameters at the current iteration. Therefore, it could highly depend on initialization and current parameters, which might lead to inefficient search especially when noise is present in the system. In this work, to mitigate this limitation, we propose a novel Gumbel-Softmax-based optimization scheme that enables a probabilistic search across an expanding set of all candidates for each control parameter using categorical reparameterization. As a case study, the proposed method is employed to find optimal control parameters for quantitative MRI. We demonstrate that our Gumbel-Softmax-based optimization simultaneously explores the entire range of control parameters from early iterations and outperforms the conventional optimization approach on accuracy of MR tissue characteristic estimation and repeatability of optimization, especially under noisy environments.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This study aims to improve the accuracy of self-supervised estimation of system properties (sp) by estimating better the control parameters (cp) of hardware.
Proposed method is based on quantized representation of cp, and Gumbel-Softmax operation (Jang et al., 2017).
Authors claim that the proposed method enables a probabilistic search across an expanding set of all candidates for each control parameter, and it works better under noisy environments.

### Strengths
S1: The idea of quantizing cp may be interesting and promising for better search across an expanding set of all candidates.

S2: The paper is easy to read.

### Weaknesses
W1: I'm curious to see if there are similar ideas of quantization (for better search across an expanding set of all candidates) in other, more general research areas. Namely, I cannot judge the degree of novelty of quantization from the description of the paper alone.

W2: Regarding the Gumbel-Softmax operation, the proposed method is a direct application of (Jang et al., 2017).
I think that a methodological novelty is not big.

*W3: I consider that the setting studied in this paper (sp is known, cp is unknown, and signal data is not available) does not simulate realistic situations.

W4: Explanation of the proposed method is not clear.

*W5: I cannot understand where the merits of the proposed method come from only with presented experimental results.
Also, experimental settings are not clearly explained or may not be appropriate.

W6: Minor optional points:

It may be confusing (abuse mathematically) that $^{−1}$ in $PM^{−1}(S(sp,cp))$ is only for sp.

$f$ is a deep neural network -> $f_\theta$ is a deep neural network

$cp_{soft}$ in (11) -> $cp_{soft,l}$

`||` in (6) is strange -> use `\|` in Latex for $\|\cdot\|_2^2$

(7) and (8) require $|_{(\theta,cp)= (\theta_i,cp_i)}$ for partial derivatives.

I cannot understand ``One million sets of system properties, accounting for possible scenarios, were utilized for optimization. For test dataset, ten thousand sets of system properties with ten times finer step size was used.'' in Sec. 2.2.

equation 16 -> use `\eqref{}`

ADAM -> Adam (the latter is conventional)

normalized mean absolute error (nRMSE) -> normalized rooted mean squared error or nMAE

### Questions
*Q~ is critical.

Q1 (for W1):
It is my understanding that this paper claims that the proposed method's ability to successfully estimate cp has led to improved accuracy in estimating system properties.
If "the proposed method is useful for better search across an expanding set of all candidates" is true, wouldn't it be effective in a simpler regression setting?
Namely, I'm curious if there are similar discussions in a simpler regression setting?
Have authors researched that?
If such research exists, it could be used to make this paper more persuasive.
Also, is there a reason why quantization is effective in the setting of this paper specifically, and not in a regression setting?

Q2 (for W2):
Is W2 correct?

*Q3 (for W3):
Is W3 correct?
I consider this weakness to be the most serious.

*Q4 (for W3 and W5):
For example, when S=sp+cp, update (say, perturbation) of cp will just degrade self-supervised estimation accuracy of sp;
It will be better to keep cp fixed.
I think that the quantization of cp makes this situation more likely to occur.
Is there any point in estimating cp in the first place?

Q5 (for W4):
I cannot understand the necessity of Gumbel-Softmax operation around equations (10) and (11) only from this paper.
Is there any reason why we can't just use $\\pi_i$ in equation (9) for $cp_{soft,i}$ in (11)?
Is (10) efficient than "Sample $u\\sim Uniform(0,1)$, and let $y=\\min\\{l\\in\\{1,\\ldots,k\\}:\\sum_{i=1}^l\\pi_i>u\\}$"?
Or, is the temperature parameter $\\tau$ that is increasing in step $t$ important?

*Q6 (for W4):
In the proposed method, a quantized representation of the cp is used for learning, but it seems that a representative value of $cp$ is required to calculate $S(sp,cp)$.
The paper does not describe how to define that representative value.

Q7 (for W4):
Authors write "Categorical reparameterization of hardware control parameter is particularly beneficial for noisy real-world environments which may cause noise for stochastic gradient (Gitman et al. (2019)):"
Is this a claim of (Gitman et al. (2019)) or an authors' claim?
If this is an authors' claim, this writing is confusing, and I feel that an authors' paper does not properly provide a rational for this claim:
I cannot understand "The second term of the rightmost side of equation 16 would sum up to zero if $N\\times M$ is high enough due to the randomness of the interference matrix."

*Q8 (for W5):
In numerical experiments, I cannot understand which of the following was effective in causing the proposed method to outperform a conventional method: update of cp, quantization of cp, or Gumbel-Softmax operation.
Please conduct an ablation study: for example, compare the no-update method (fix cp at some values; see Q4), the conventional method (without quantization of cp), another method (with quantization of cp and without Gumbel-Softmax operation; see Q5), the proposed method (with quantization of cp and Gumbel-Softmax operation).

Q9 (for W5):
Is the computational efficiency of the proposed method comparable to other methods?
If the computational efficiency of the proposed method is poor, we can simply use another efficient method with a larger acquisition number $N$.

*Q10 (for W5):
I think the learning rate is quite important in this experimental comparison.
Did you try several different settings of the learning rate?
Did $(10^{-4},10^{-4})$ for the conventional method and $(10^{-4},10^{-2})$ for the proposed method yield the best result?
I am concerned about a situation where the iteration gets trapped in poor local minima since $(10^{-4},10^{-4})$ for the conventional method is too small.

Q11 (for W5):
I don't understand the significance of multiplying the sigmoid activation function in the final hidden layer.
If the scale issue is important, I think it would be better to standardize system properties themselves.

Q12 (for W5):
Why is the criterion (6) adopted for learning different from the criterion for evaluation (normalized mean absolute error or nRMSE in Table 1)?
If we want to improve the average normalized mean absolute error (or nRMSE), then our training criteria would be better to correspond to that.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The manuscript discusses a methodology to optimally adjust the control parameters of a physical system specified by set of equations and  a set of system parameters. The idea is to simultaneously train a neural network system parameter estimator and optimize the control parameters of the system such that the estimated system parameters are as accurate as possible. Rather than maintaining a single estimated value per control parameter, the manuscript proposes to use a categorical distribution over a discretized range of the parameters.

A set of experiments are conducted on a system with 4 control parameters and 4 system parameters simulating magnetization based on modified Bloch equations.

### Strengths
* System inversion and parameter estimation is a relevant field of research.

### Weaknesses
 * The experimental validation is not convincing. The authors use a single baseline "conventional optimization approach" to study their method. The simulated system is very basic.
* Some parts of the text could be improved: e.g. 1. Intro l. 40 "parameters is to find an", l. 42 "signal from physical system", l. 47 "Thus physics model enables". 2.1 Physics Model l.159 "the noise could be originated from"
* It is not simple to reproduce the experimental findings given the information provided in the manuscript.
* The manuscript needs to better connect to the big literature of system identification and parameter estimation.

### Questions
* Why do you have "hardware control parameters" in the title rather than "control parameters" given that in the experimental Section, in Equation (1) and Figure 1 you are studying a physics model without any hardware footprint? It took me a while to understand that the entire methodology is virtual, hence this might be misleading for other readers in particular since the term MRI features in the abstract.
* Do you agree that the paper doe no set any "optimal hardware control parameters for MRI system" as claimed in the Introduction and the phrase should be removed?
* Could you please move the relevant aspects of your spin system from the Appendix to the main text (Experiments) to facilitate reading?
* Do you intend to provide code for the methodology and the experiments?
* Is there an explanation why the training loss for the "conventional" method is smaller given that the Gumbel-parametrized model has less options due to the discretization of the parameter space?
* In a practical setting, how do you differentiate between system parameters and control parameters?
* Can you explain, why you cited [Black 1986] and [Blanter et al. 2000] in Section 2.1?
* Can you make your noise model more explicit by integrating it more prominently in Eq. (1)? In practice, it is impossible to observe a clean signal.
* Can you please explain the additive noise component in the control parameters, in particular in the Experiments section?
* How would you select a good discretization scheme in practice both in terms of lower/upper bound and step size?
* Is there a sweet spot the number of discrete steps? Possibly, very coarse discretizations allow little flexibility while overly fine discretizations might be hard to estimate.
* Can you characterize the systems where your idea is applicable and beneficial?
* What about strongly (anti)correlated sets of parameters? What about parameters with little influence on the system behavior?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper proposes an optimization method for control parameter search in physics-based models. The method relies on the categorical reparametrization of the control parameters through Gumbel-Softmax, simultaneously enabling non-deterministic search across the control parameter space, and  improving the robustness of gradient descent under the presence of noise.
The method is evaluated on a two-pool proton exchange model using an MLP, evaluated under varying noise levels and dataset sizes. Compared to a "conventional" approach (that does not rely on the Gumbel-Softmax reparametrization), the proposed method demonstrates better robustness to noise and improved accuracy,

### Strengths
This paper presents a concise method for parameter search in noisy environments, demonstrating its potential on a complex physical system simulator. The simplicity of the proposed approach contributes to its robustness, making it promising for applications that demand accurate parameter estimation under noise and under a large search space.

Notably, the method simultaneously optimizes the parameters of a neural network, which estimates system properties, alongside the control parameters defining the physical system. This integrated approach appears well-suited to the challenges in the targeted application domain, addressing both noise and the inherent difficulty of optimizing control parameters in complex systems.

### Weaknesses
 - The paper lacks clear contextualization relative to prior work, omitting key references to research on soft labels and reparameterization in search problems—well-studied subjects in ML and optimization. 
- Validation is limited to a single physics-based model, narrowing its scope, with unclear implications for generalization to related systems. The exclusive use of simulated data in experiments further restricts claims of noise robustness. 
- Additionally, the method is only compared to an undefined "conventional" approach, with no comparisons to other ML-based methods in the literature, making its contribution to the field unclear.

### Questions
- Can you clarify what are the characteristics of the  "conventional" method used as a baseline?
- Could you clarify how does this method extend to other use cases (physics-based models and beyond)?
- What do you see as the main contribution of the paper? Is it the overall optimization methodology or its applicability to the considered application?

### Soundness
2

### Presentation
1

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
In this work, the authors propose to optimize the hardware control parameters with deep learning approach. Generally saying, this is an interesting application of AI4Physics by fitting the physical procedure with neural network.

### Strengths
1. The topic is interesting. 

2. The writing is easy to follow.

### Weaknesses
1. While the framework is quite general, the experiments are not sufficient. Is there any dataset from industry or from the simulation of more integrated system?  

2. What does it mean for the differences shown in Figure 3? How to evaluate the practical differences caused by such fitness difference?

3. The description of the physical procedure could be shorten as well as the definition of non-specific formula like 9-11. The authors should focus on how and why the NN improves the overall estimation. 

4. As there are many other approaches and models in fitting parameters like evolutionary algorithm and other data fitting approaches. If this problem is a worthy one, there should be existing results to allow for the comparison.

### Questions
Please check the weakness.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper applies the Gumbel-softmax reparameterization trick to optimize the hardware control parameters. It takes the MRI system as an example, demonstrating that the proposed method can achieve lower estimation errors than the conventional approach.

### Strengths
This paper is well-structured and considers a realistic problem. The application of the Gumbel-softmax reparameterization trick sounds correct in the context.

### Weaknesses
 - The novelty of this paper is limited, as the Gumbel-Softmax trick has been implemented to address the categorical distribution problem in many fields over the past few years. Besides merely applying the trick to another concrete problem, additional improvements and contributions are expected.
- In the evaluation, comparing with only one other method is not comprehensive. More SOTA methods of optimizing the control parameters should be mentioned in the introduction and compared with the proposed one. 
- The notations in the equations are inappropriate, such as in (4), (5), etc. Using letters (such as Greek letters) instead of abbreviations would be more suitable.
- Some training details are ignored such as the initialization of the unnormalized log-probabilities (logits), and whether the Gumbel noise was added once or at each iteration.

### Questions
- Is the temperature annealing necessary? And why is the starting temperature set to be $1$ but not greater than $1$?
- Figure 3 shows the training loss decreasing from $4\times 10^{-7}$ to around $1\times 10^{-7}$, why is the reduction so minimal? The errors summarized in Table 1 approximate $10$, why are these values so greater than the losses?
- Figure 4 shows the selected parameters at the end are all at both extremes, why were none of the parameters in the middle selected? Are the results totally different from those from the conventional method? After training, did the other logits $z$ become zeros or negative values?

### Soundness
2

### Presentation
2

### Contribution
2

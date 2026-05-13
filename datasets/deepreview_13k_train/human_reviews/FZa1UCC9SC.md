# Exact risk curves of signSGD in High-Dimensions: quantifying preconditioning and noise-compression effects

- Decision: Reject
- Scores: 6, 3, 6

## Abstract
In recent years, SignSGD has garnered interest as both a practical optimizer as well as a simple model to understand adaptive optimizers like Adam. Though there is a general consensus that SignSGD acts to precondition optimization and reshapes noise,  quantitatively understanding these effects in theoretically solvable settings remains difficult. We present an analysis of SignSGD in a high dimensional limit, and derive a limiting SDE and ODE to describe the risk. Using this framework we quantify four effects of SignSGD: effective learning rate, noise compression, diagonal preconditioning, and gradient noise reshaping. Our analysis is consistent with experimental observations but moves beyond that by quantifying the dependence of these effects on the data and noise distributions. We conclude with a conjecture on how these results might be extended to Adam.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies SignSGD to have better qualitative understanding of this algorithm, especially in the high-dimensional limit. The authors derive SDE and ODE for the limiting equation as continuous approximation of SignSGD. Using this framework they quantify four effects of SignSGD: effective learning rate, noise compression, diagonal preconditioning, and gradient noise reshaping. They finally conjectured how this might be extended to ADAM.

### Strengths
(1) The presentation is very clear;

(2) The results present a good quantitative understanding of SignSGD;

(3) A comparison with vanilla SGD is provided;

### Weaknesses
Overall, the paper looks good.

Using continuous approximation may explain features of SignSGD but only at the qualitative level. At the quantitative level, long-time behavior of SignSGD and its continuous approximation may be very different. Can the authors explain more about this situation? This may include:

(1) Discuss any theoretical or empirical evidence the authors have for how well the continuous approximation matches discrete SignSGD over long time horizons.

(2) Clarify if there are specific regimes or conditions where the authors expect the approximation to break down for long-time behavior.

(3) Consider adding a discussion of the limitations of the continuous approximation approach, particularly for long-time dynamics, to their paper.

### Questions
Using continuous approximation may explain features of SignSGD but only at the qualitative level. At the quantitative level, long-time behavior of SignSGD and its continuous approximation may be very different. Can the authors explain more about this situation? This may include:

(1) Discuss any theoretical or empirical evidence the authors have for how well the continuous approximation matches discrete SignSGD over long time horizons.

(2) Clarify if there are specific regimes or conditions where the authors expect the approximation to break down for long-time behavior.

(3) Consider adding a discussion of the limitations of the continuous approximation approach, particularly for long-time dynamics, to their paper.

A suggested reference paper: Kushner, H. J. (1982). A cautionary note on the use of singular perturbation methods for “small
noise” models. Stochastics: An International Journal of Probability and Stochastic Processes, 6(2):117–120.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The objective of this paper is to study SignSGD under the lens of SDEs in high dimensions. They try to use this continuous-time model to unveil some aspects of the dynamics of SignSGD such as i) Its effective learning rate; ii) Noise compression; iii) Preconditioning iv) Gradient noise reshaping. They provide some limited experimental evidence supporting their claims and close by highlighting that they expect these findings to be extended to Adam as well.

### Strengths
- **Originality:** The authors attempt to contribute by deriving an SDE for SignSGD in a simple high-dimensional setup, which appears to be a new direction in modeling this optimizer.

- **Quality:** The derivation of an ODE that models the risk function for linear regression based on this SDE provides an interesting theoretical perspective which is also partially corroborated empirically.

- **Significance:** The use of this model to predict the asymptotic expected risk level under Gaussian label noise offers some potential insights into SignSGD’s behavior in specific scenarios, though its practical relevance remains limited to the assumptions made.

- **Clarity:** The paper presents the theoretical results in a generally understandable manner.

### Weaknesses
 **Weak Points**

Since there is no dedicated space to provide one, I will write my "Overall Comment" here. I relegate a "Detailed Feedback" to the Questions, where I corroborate more on the points below.

**Overall Comment:** The paper addresses interesting questions and demonstrates potential through its mathematically sound approach. To enhance the quality and impact of the manuscript, I recommend focusing on several key areas for improvement, which are detailed below. Given the current status of the paper, I recommend **rejection**: Addressing these points could significantly strengthen the work which certainly deserves it.

1. **Inclusion of Related Works:** To strengthen the manuscript, it would be beneficial to discuss existing literature on continuous-time modeling of optimizers, particularly the Weak-Approximation (WA) Framework introduced by Li et al. (2019). Including this framework and comparing it with your approach could provide valuable context and demonstrate how your work contributes to the field. Additionally, since the SDE of Adam has been derived by Malladi et al. (2022), and given that SignSGD is a special case of Adam, incorporating a comparison with these results would enhance the depth of the analysis. Including relevant references when stating key facts will also improve the manuscript's credibility (See below for details).

2. **Assumption Justification and Validation:** Clarifying and justifying the assumptions upon which your analysis is based would strengthen the paper. Providing theoretical or experimental validation for these assumptions will help readers understand their appropriateness and relevance. It would also be valuable to explain any advantages your setup may have over the Weak-Approximation framework. For instance, elaborating on the necessity of the high-dimensional setup in your SDE derivations, especially when such a requirement is not present in weak approximations, could clarify the benefits of your approach.

3. **Addressing Conceptual Missteps:** It's important to ensure that the continuous-time models derived in your work faithfully represent the behavior of the optimizers they are intended to model. While your paper provides guarantees for the risk (as per Theorem 1), extending these guarantees to other critical aspects—such as the gradient norm and the norm of the iterates (as defined in Definition 2 of Li et al.)—would strengthen the validity of your models. **Currently, insights are derived primarily about the SDEs rather than the optimizers themselves but are framed as insights on the optimizers.** To effectively carry these insights over to the optimizers, it would be beneficial to provide guarantees that the SDEs closely track the behavior of their respective optimizers or to include experimental verifications demonstrating this correspondence.

4. **Inclusion of Experimental Validation:** Incorporating experimental validation of your results and insights would greatly enhance the manuscript. Validating the theoretical findings empirically will demonstrate the practical applicability of your SDE models and confirm that they are informative. For instance, if you derive a bound on the risk using an SDE, empirically verifying this bound for the respective optimizer would provide strong support for your theoretical claims.

5. **Improving Structure and Clarity:** Enhancing the organization and clarity of the manuscript would significantly improve its readability and impact. Formalizing key results as Lemmas, Propositions, or Theorems, rather than discussing them in free text, would make the arguments more rigorous and easier to follow. Clearly defining all symbols and terms, such as "Vanilla ODE," will help avoid confusion. Additionally, ensuring that figures are accessible to all readers, including those who are colorblind, by choosing appropriate color schemes and providing clear labels, will enhance the overall quality of the presentation.

I have provided detailed feedback on these points in the **Questions** section below, where I elaborate further on how the manuscript can be improved.

**References:**

- Li et al. (2019) *"Stochastic Modified Equations and Dynamics of Stochastic Gradient Algorithms I: Mathematical Foundations"*.
- Malladi et al. (2022) *"On the SDEs and Scaling Rules for Adaptive Gradient Algorithms"*.

### Questions
**Detailed Feedback:**

In the following, I provide detailed feedback. These points are generally marked in the same order as they appear in the paper and are not arranged by relevance.

1. **Literature Review:** It would be beneficial to include a review of the literature surrounding continuous-time models for optimizers. In particular, discussing weak approximations (Li et al. 2019) could enhance the context of your work, as they have been successful in deriving SDEs and ensuring their accuracy. Additionally, since not all readers may be familiar with SDEs and the concept of continuous-time models, providing visual aids—such as plotting a trajectory of the optimizer alongside that of the SDE—could make these ideas more accessible.

2. **Discussion of Limitations:** Including a section dedicated to the limitations of your approach would be appreciated. A subsection comparing your method with existing literature could provide readers with a clearer understanding of the advantages and potential drawbacks of your work.

3. **High-Dimensional Setting Clarification:** It would be helpful to clarify why your derivations require the high-dimensional setting, especially since the Weak Approximation framework does not have this requirement and has been effectively used to derive SDEs for various methods like SGD (Li et al.), Adam and RMSprop (Malladi et al.), and SAM (Compagnoni et al.). Explaining could enhance readers' understanding of your approach.

4. **Focus on Linear Regression Model:** It might be beneficial to explain why your analysis focuses on the linear regression model, particularly when the Weak Approximation framework allows for SDE derivations with relatively general loss functions. Highlighting any specific advantages your setting offers would strengthen your argument.

5. **Relation to Existing SDEs:** Considering that the SDE of Adam/RMSprop has been derived by Malladi et al. (2022), and since SignSGD is a special case of these algorithms, it would be helpful if you could explain how their SDE relates to yours. Demonstrating this connection could enhance the comprehensiveness of your work.

6. **Definition Clarity:** Regarding **Definition 1**, it appears that the risk definitions do not depend on the labels. It might improve clarity to list Assumption 1 first and then define the risks, enhancing the logical flow of your presentation.

7. **Assumption 1 Concerns:** In deep learning, we often encounter overparameterized regimes where there are more parameters than data points, leading to potentially infinite solutions for the regression task. This could make the SDE ill-posed because you define it in terms of a specific $\theta_*$, but the dynamics might converge to a different solution. This could result in the risk in the denominator approaching zero while the numerator does not. Therefore, it seems that the SDE may have **non-Lipschitz coefficients, which could hinder the existence and uniqueness of the solution**: Could you comment on this aspect?

8. **Conceptual Mistake (Line 86):** In **Line 86**, the statement that "an important characterizing feature of SignSGD is its effect on the covariance matrix K" seems conceptually wrong. The matrix K is fixed and exists independently; it is not influenced by the choice of optimizer. Perhaps it would be more accurate to say that K influences SignSGD.

9. **Universality Reference (Line 96):** In **Line 96**, you mention *universality* as if it's a commonly known concept. Providing a reference for this phenomenon and considering whether this is the best place to introduce it in your manuscript would be helpful.

10. **Assumption 3 Organization and Discussion:** Regarding **Assumption 3**, presenting assumptions on the matrices immediately after their definitions, rather than after Assumption 3, could avoid confusion. Additionally:

    - **i)** You mention that the upper bound is standard; including a reference would be helpful. Regarding the lower bound, does it hold in practice? High-dimensional data often have a lot of structure, and their generating covariance might be degenerate.
    - **ii)** There is no discussion of the second assumption; adding this would enhance understanding.
    - **iii)** The discussion around the third assumption is somewhat informal. Clarifying what you mean by "typical" and providing references or experimental validation would strengthen this section, as real-world covariance matrices are not random and possess rich structures.

11. **Assumption 4 Clarification:** Concerning **Assumption 4**, this assumption appears cumbersome, especially since the Weak Approximation setting does not require such special rescaling. Does this imply that SignSGD needs to be run with a learning rate that scales with $1/d$? Clarifying this point would be beneficial.

12. **(Assumption 5):** Regarding **Assumption 5**, Equation (4) guarantees an upper bound on the resolvent. However, in Equation (6), you divide by it. How do you ensure that you are not dividing by zero?

13. **Conceptual Misunderstanding (Line 149):** In **Line 149**, there may be a conceptual misunderstanding. Compression does not change the landscape; the landscape exists independently, and the optimizer moves through it without altering it. Are you suggesting that there is some implicit regularization of the landscape (Li. et al. & Compagnoni et al.)?

14. **Naming Convention (Line 153 and Definition 2):** In **Line 153 and Definition 2**, you refer to the method as "Homogenized." It might be clearer to call it what it is: the SDE of SignSGD. Additionally, as mentioned earlier, the SDE appears to be ill-defined in overparameterized settings.

15. **Recovery of ODE from SDE (Definition 2):** Regarding **Definition 2**, explaining how we can recover the ODE of SignGD when there is no noise would be helpful. If this is not possible, it raises questions about the explanatory power of the method. Experimenting with your provided Python code did not clarify this for me. Additionally, relating and comparing this SDE with that of Adam in Malladi et al. (2022), if possible, would enhance the comprehensiveness of your analysis. If not possible, providing an explanation would be helpful.

16. **Figure 1 Clarity:** Concerning **Figure 1**, it's crucial for figures to be clearly readable and well-described. The labels in the legend are unclear; terms like "Vanilla ODE" are not defined in the text, and I had to refer to your code to understand them. Similarly for "ODE." Additionally, the color scheme is not color-blind-friendly. I recommend using different markers for the lines and avoiding overlapping colors, as it was challenging to distinguish them. Regarding the caption:

    - **i)** Are you representing the dynamics of Sign(H)SGD, or is it the dynamics of the risk under the dynamics of Sign(H)SGD?
    - **ii)** When you mention the "usefulness of the ODE," do you mean its faithfulness or accuracy in describing the optimizer's behavior?
    - **iii)** The phrase "and the significant estimation of key quantities" is unclear. Could you clarify what you mean?

17. **Extended Plotting (Figure 1):** While the initial part of the dynamics is well captured in **Figure 1**, the central purpose of SDEs is to model the stochastic nature of the optimizer, which is often most evident near convergence. Could you extend the plots to include more epochs (e.g., 100 or 1000) to illustrate this aspect?

18. **Terminology Clarification (Remark 1):** In **Remark 1**, it might be confusing to refer to this as interpolation. You can have label noise and still achieve interpolation; indeed, it's possible to fit random inputs x to random outputs y. Clarifying your terminology here would be helpful.

19. **Theorem 1 Commentary:** **Theorem 1** is a key result and could benefit from further commentary:

    - **i)** Do you have any insights into how strong the exponential explosion is?
    - **ii)** What role do the moments play in this statement?
    - **iii)** It might be clearer to denote the two constants currently marked with $C$ using different letters to avoid confusion.
    - **iv)** It seems that under your framework, you're only able to derive the curves for the loss, whereas the Weak Approximation method provides guarantees for each sufficiently regular test function (Def. 2 of Li et al.). This might limit your framework. Is it possible to generalize your result to other functions, such as the norm of the gradient or the norm of the iterates? Would each quantity require a separate theorem, or is there a way to cover a class of interesting test functions under a broader theorem, similar to the WA setup?

20. **Formalizing ODE Results:** It might enhance your manuscript to formalize the ODE for the Risk as a Proposition or Theorem, rather than just describing it in the text. Additionally, providing a similar result for SGD would allow for a better comparison between the methods.

21. **Equation Clarification (Eq 10):** Regarding Equation (10), is this a definition or an equality?

22. **Theorem 2 Statement Clarity:** **Theorem 2** is another key result, and similar observations as those for Theorem 1 apply here. Also, $R_t$ is given by Equation (10), but its dynamics are described by Equations (11.a) and (11.b). It might be helpful to rephrase the statement to make this clearer.

23. **SDE Derivation for SGD (Eq 13):** Regarding Equation (13), the SDE of SGD does not seem to be derived in the paper, and I couldn't locate it in the given reference. Could you provide more details on this? Additionally, the SDE of SGD has been extensively studied and derived without requiring high-dimensional settings (see Li et al.). Why is the high-dimensional setting needed here? How can we see that in a noiseless setup, this SDE becomes the ODE of Gradient Descent?

24. **Scheduler Boundedness (Eq 14):** Concerning Equation (14), is this scheduler actually bounded? As you approach a stationary point, it seems to diverge. Additionally, this scheduler resembles the normalization used to define Normalized SGD. Could you elaborate on this point?

25. **Highlighting SignSGD's Advantage (Lines 276-277):** In Lines 276-277, you mention that SignSGD is favored when the noise has unbounded variance. This point hasn't been mentioned earlier. It might be helpful to highlight this earlier in the manuscript, provide a reference, or offer an argument or example to support this claim.

26. "Training with signSGD": To my understanding, you are not training anything here. It seems like you are comparing the dynamics of the SDE models for SGD and signSGD: It is important to remember that you are not comparing the behavior of the real optimizers but that of their SDE models. To confirm your insights from the models, you need to run experiments on the real optimizers.

27. **Definition of Variables (Eq 15.b):** In Equation (15.b), the variable $\psi$ is not defined at this point. It might be clearer to include a remark or lemma where you define all the variables used in the equation before proceeding with the analysis.

28. **Preservation of Optimizer Properties (Line 315):** In Line 315, if I understand correctly, you suggest that SignSGD does not converge properly when the risk is small, and to address this, you propose multiplying the increments of SignSGD by the square root of the risk. However, this could negate the optimizer's resistance to noises with unbounded variance. Could you explain why you would want to remove such a significant advantage of the optimizer?

29. **Relevance of Comment (Lines 316-318):** Lines 316-318 contain a comment that seems somewhat disconnected from the surrounding discussion and lacks sufficient motivation. You might consider elaborating further to clarify its relevance or consider removing it.

30. **Empirical Validation (Theorem 3):** **Theorem 3** presents an interesting result, and I strongly encourage you to provide empirical validation for this limit. Including a corresponding result for SGD would greatly enhance the ability to compare the methods. Additionally, is it possible to extend this result to scenarios with unbounded variance?

31. **Section 4.2 Clarification:** Section 4.2 may need further clarification. If the noise variance approaches infinity, wouldn't the risk also tend to infinity? In that case, $\psi$ might not actually diverge to infinity. Modeling unbounded variance is highly relevant because it's precisely the situation where SignSGD would be most beneficial. Addressing this point could strengthen your analysis.

32. **Framing and Definitions (Lines 370-377):** In Lines 370-377:

    - **i)** It might be beneficial to formalize this discussion as a Proposition. Additionally, kurtosis is not defined for all degrees of freedom of the Student's t-distribution, and it quickly becomes unbounded in cases of interest like unbounded variance. Could you clarify why you use this term in such contexts?
    - **ii)** Is Equation (19) straightforward? Is it possible for the risk to be nearly zero while the noise has an increasingly large (possibly unbounded) variance?

33. **Collecting Equations into Results:** It might strengthen the flow of the paper if you combined Equations (19), (20), and (21) into a clearly stated result, and present the equivalent findings for SGD for comparison. Including experimental validation would further support your theoretical claims.

34. **Scheduling SignSGD Concerns:** Regarding **Scheduling SignSGD**, this appears to be a puzzling point. In Equation (24), you suggest using a scheduler that increases or decreases with the risk. This could effectively undo the normalization that contributes to SignSGD's effectiveness: For instance, if the noise variance is unbounded, this scheduler could diverge, which may not be desirable. It might be counterproductive to undo the adaptive gradient rescaling. Could you provide further insight into this?

35. **Relation to Existing SDEs (Line 432):** In Line 432, it seems that this analysis could be performed by considering the SDE of Adam as derived in Malladi et al. Could you elaborate on this point? In your appendix, I noticed only an informal SDE for the iterates of Adam, but not the differential equations for $m_t$ and $v_t$.

36. **Merging Results (Theorem 4):** Regarding **Theorem 4**, is it possible to merge this result with Theorem 3, or am I misunderstanding something? Including experimental validation and comparisons with SGD would be valuable additions to your manuscript.

37. **Elaboration Needed (Line 465):** In Line 465, you mention "when the covariance—the Hessian of the risk." Could you elaborate on this point? Providing a reference or a brief explanation would help clarify this statement.

38. **Practical Implications (Section 4.3):** A general comment on Section 4.3: In practical terms, could you provide guidance on when it is better to use one method over the other? This would help readers understand the practical implications of your findings.

39. **Quantitative Characterization (Section 4.4):** In Section 4.4, the discussion is mostly qualitative and intuitive. It would be helpful to include a quantitative characterization of the differences in noise structure to provide a clearer understanding of your analysis.

---

**Minor Points:**

1. **Rewriting for Clarity (Lines 87-93):** It might improve the readability to rephrase this section into a cohesive paragraph rather than a list of facts and observations. Regarding Equation (4), elaborating further and possibly providing a brief proof for the derivation of $K_\sigma$ would enhance the clarity.

2. **Lines 94 to 96:** Please rephrase and make correct use of words and commas. Suggestion: "Although our theory is framed in the setting of Gaussian data, as we will see, the results are still a good description for real-world, a priori non-Gaussian settings."

3. **Punctuation (Line 248):** Please add a comma before the word "respectively".

4. **Consistent Notation:** It would be helpful to maintain consistent notation throughout the manuscript. For example, choose either $P_t$ or $P(t)$ for processes and use it consistently.

5. **Formal Language (Line 267):** The phrase "apples-to-apples" is informal. Consider using more formal language appropriate for a scientific paper.

6. **Terminology Correction (Figure 3):** The correct term is "Student's t," not "Student-t." Please make this correction.

---

**Appendix:**

While I won't go into detailed comments about the appendix, I noticed that it's quite technical and could benefit from better organization. Presenting technical lemmas upfront and breaking down major results into smaller components could streamline the proofs. Several missing preliminaries and notation definitions affect readability. Here are some examples that came to mind:

1. **Equation Justification (Line 738):** It would be preferable to first prove, in a technical lemma, what is necessary to justify Equation (44) before using it. Since you seem to drop this term and mention that you will justify it later, it's important to handle such a key step carefully to ensure clarity and rigor.

2. **Assumption Clarity (Line 739):** It appears that you're working under the assumption of bounded risk, which may not be realistic in practical scenarios. **This is a significant assumption that should be explicitly stated in the main paper.**

3. **Accessibility of Concepts:** Concepts like nets, stopped processes, and martingales may not be familiar to all readers. Including a section that compiles all the notation, technical lemmas, and theoretical preliminaries would help make the appendix more accessible and provide a more self-contained experience for readers. I attempted to follow the proofs **but found it challenging to verify all the steps in a reasonable amount of time.**

4. **Lemma Placement (Line 836):** **Lemma 8** is referred to here but is stated much later in the appendix. Reorganizing the content so that lemmas are introduced before they are used would improve the flow and readability.

5. **Undefined Notation (Line 915):** The notation $\mathcal{E}_j^i$ is used but not defined at this point. Defining all notation when first introduced would help prevent confusion.

6. **Conceptual Clarification (Line 1007):** There seems to be a conceptual misunderstanding here. It is the dynamics of the SDE that converge to those of the optimizer, not the other way around.

7. **Variable Definition (Line 1025):** The notation $\sigma_{k+1}$ is used but not defined. Providing a definition would improve clarity.

8. **Term Introduction (Line 1049):** The term "HSGD" is mentioned, but it hasn't been introduced earlier in the paper.

9. **Notation Clarification (Line 1630):** The notation $v_i$ is used without prior definition.

Compagnoni et al. "An SDE for Modeling SAM: Theory and Insights".

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The authors motivated by the signed gradient interpretation of the stochastic gradient algorithm, develop and apply an SDE/ODE framework to analyze the dynamics of the stochastic gradient algorithm using signed gradients. With this framework they study quantities like the effective learning rate of the algorithm, preconditioning and gradient noise. In addition, they draw up a conjecture to explain Adaptive moment estimation using their framework.

### Strengths
I think the biggest strength of the paper is its clarity of presentation.

### Weaknesses
The weakness of the paper lies in the technical side, most especially relatively recent work that attempt to connect diagonal preconditioning and sign gradients to Adam.

1. For the generic reader, the authors fail to explicitly define what SDE and ODE mean.

2. In line 458, the authors can better reframe the content of the line to be more technically sound.  
The use of the phrase: "... optimal deterministic convex opt algorithm such as Heavy ball momentum and conjugate gradient..." is not accurate with respect to stochastic gradient algorithms. The wording passes the two algorithms as two different algorithms, whereas, you have the same stochastic gradient algorithm, only with a different learning rate setting and a lowpass filter (momentum parameter) setting.
A better phrase could be: "... the stochastic gradient algorithm with smooth gradients (momentum) and optimal convex optimization settings such as Polyak's Heavy Ball and the Conjugate Gradient ...".
Note that the stochastic gradient algorithm itself does not care whether we use a minibatch gradient or not.

3. The extra conjecture adds nothing essentially to the paper. 
Adam is simply a learning rate setting for the stochastic gradient algorithm. It is when you decompose the learning rate that you get a normalized gradient in expectation. It is the normalized gradient that has a connection with the sign function. 
Again, these things are not new. A careful study of classic literature, especially Tsypkin's classic 1971 work on Adaptation and learning in automatic systems will make this much clearer.
Also, diagonal preconditioning is only true, if the hessian of the objective function is diagonal. In the case of the learning rate called Adam, we are only implementing it by dividing the gradient with its estimated variance (or moment), which gives a normalized gradient in expectation. 
The diagonal preconditioning is also in expectation because, in a sense, the eigenvalues of the hessian can be interpretated as variances of the gradient.

### Questions
None.

### Soundness
3

### Presentation
3

### Contribution
2

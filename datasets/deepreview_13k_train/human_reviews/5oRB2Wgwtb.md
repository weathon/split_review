# Online Bandit Nonlinear Control with Dynamic Batch Length and Adaptive Learning Rate

- Decision: Reject
- Scores: 5, 6, 6, 6

## Abstract
This paper is concerned with the online bandit nonlinear control, which aims to learn the best stabilizing controller from a pool of stabilizing and destabilizing controllers of unknown types for a given nonlinear dynamical system. We develop an algorithm, named \textbf{D}ynamic \textbf{B}atch length and \textbf{A}daptive learning \textbf{R}ate (DBAR), and study its stability and regret. Unlike the existing Exp3 algorithm requiring an exponentially stabilizing controller, DBAR only needs a significantly weaker notion of controller stability, in which case substantial time may be required to certify the system stability. Dynamic batch length in DBAR effectively addresses this issue and enables the system to attain asymptotic stability, where the algorithm behaves as if there were no destabilizing controllers. Moreover, adaptive learning rate in DBAR only uses the state norm information to achieve a tight regret bound even when none of the stabilizing controllers in the pool are exponentially stabilizing.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper addresses the online bandit nonlinear control problem, where the objective is to learn an optimal controller for a nonlinear dynamical system amid unknown stabilizing and destabilizing controllers. The authors introduce the DBAR (Dynamic Batch length and Adaptive learning Rate) algorithm, which adapts batch length and learning rate to improve control stability and minimize regret without requiring exponentially stabilizing controllers. Unlike existing approaches that need stronger stability assumptions, DBAR works with a weaker, asymptotic stability notion. This flexibility allows DBAR to achieve stability and a regret bound even when the pool of stabilizing controllers is limited or includes only asymptotically stabilizing ones.

Theoretical contributions include proving asymptotic and finite-gain stability of DBAR and bounding its regret. The authors also compare DBAR's performance with existing algorithms, illustrating through simulations that DBAR provides improved stability and reduced regret in both linear and nonlinear systems under adversarial disturbances.

### Strengths
Originality: 
    The paper introduces a new algorithm, DBAR, combining a dynamic batch length and an adaptive learning rate, which expands on existing Exp3 approaches for bandit learning. This design theoretically broadens the applicability of online control by relaxing the requirement for exponentially stabilizing controllers, a novel aspect in nonlinear control with adversarial disturbances.

Quality: 
    The paper presents a well-structured algorithm and offers some theoretical analysis, including stability and regret bounds, which demonstrate rigor in method development. The authors provide proofs for their main results and discuss conditions under which stability is achieved, showcasing technical precision.

Clarity: 
    The problem setup, assumptions, and main results are generally clear, with key terms defined (e.g., asymptotic stability and finite-gain stability) and a well-organized structure. The authors also make efforts to contextualize the algorithm in comparison to prior work, which aids readability for readers with a background in online control or bandit learning.

### Weaknesses
Originality:
    While DBAR's approach to adapting the learning rate and batch size is new, the actual contribution may be seen as incremental. The improvements over existing algorithms are mainly in modifying specific assumptions rather than introducing a breakthrough method, and it is unclear if these modifications substantively advance the field. The core idea of adapting batch size and learning rate based on system state is not entirely novel, and the specific adaptation rules, while technically sound, do not represent a significant departure from existing techniques in online learning. The paper does not adequately demonstrate that the relaxed stability assumptions lead to a practical advantage in real-world scenarios, where the distinction between asymptotic and exponential stability may not be as critical.

Quality:
    The theoretical guarantees, though valuable, rest on assumptions that may be difficult to satisfy in real-world applications, such as requiring knowledge of an ISS controller in advance. This assumption, while common in control theory, limits the practical applicability of the algorithm. Furthermore, empirical validation is limited to relatively simple experiments, which may not fully demonstrate the algorithm’s effectiveness or scalability in more complex settings. The experiments do not adequately explore the sensitivity of the algorithm to the choice of parameters, such as the initial batch size and the rate of increase of the batch length. The lack of a thorough parameter study limits the practical guidance that can be derived from the paper.

Significance:
    The practical impact of DBAR appears limited, as the algorithm’s assumptions—particularly on controller stability—may not align well with typical scenarios in nonlinear control. The significance for broader ML audiences is thus moderate, as DBAR seems primarily useful in niche settings where exact stability knowledge is available. The paper does not clearly articulate the specific scenarios where DBAR would be more advantageous than existing methods, and the potential benefits in real-world control applications are not well-established. The lack of a clear use case limits the overall impact of the work.

Significance:
    The paper's experimental evaluation does not robustly validate the theoretical claims, as it relies on lower-dimensional systems that may not capture the challenges posed by high-dimensional, complex environments. This limits the confidence in DBAR's utility beyond the examples shown, reducing its impact. The experiments do not include a comparison with state-of-the-art methods in online nonlinear control, making it difficult to assess the relative performance of DBAR. The lack of a comprehensive benchmark limits the ability to generalize the findings.

### Questions
1. How does the dynamically increasing batch length affect the algorithm's computational cost, particularly in real-time applications? It would be helpful to discuss any trade-offs between stability assurance and computational efficiency.

2. The current experimental setup involves relatively simple, low-dimensional systems. Can the authors provide results on more challenging benchmarks to better demonstrate DBAR’s performance and stability claims?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies the problem of online bandit non-linear control where both transition dynamics and cost functions are non-linear and adversarial, and we only receive bandit feedback on either of them. Removing the assumption on exponentially stabilizing controllers, this paper ensured $\tilde{\mathcal O}(T^{2/3})$ regret with the help of only asymptotically stabilizing controllers.

Technically, this paper uses geometricly increasing batch lengthes to remove the requirement of exponentially stabilizing controllers, and further make the $\mathcal O(T^{1/3} e^{\lvert \mathcal U\rvert})$ dependency to $\mathcal O(T^{-1/3} e^{\lvert \mathcal U\rvert})$ via an adaptive learning rate tuning scheme.

### Strengths
1. The removal of exponentially stabilizing policies looks pretty good.
2. The resulting regret is satisfactory.
3. The algorithms are stated and motivated clearly.
4. Results are supplemented with numerical evaluations.

### Weaknesses
From the main text, it looks like the two main techniques, geometrically-increasing batch lengthes and geometrically-decaying learning rates, are the main technical contributions of this paper. But these two techniques seems both extensively studied in other online learning problems. So --
1. How are they different from those used in other online learning problems? Say, do you specifically adapt them to this control theory problem?
2. Do they bring special difficulties under this specific setup of nonlinear control? Say, do they break some previous analysis ideas in online nonlinear control?
3. Why previous works didn't use them?

[EDIT. After rebuttal, it turns out that batch lengths and learning rates are both not simply geometric, but follow some more meticulous designs.]

Minor:

1. To create a reference inside parentheses, please try using the command `\citep{}` instead of manually typing `(\citet{})`.
2. Section 2 is notation heavy. I suggest the authors to add subsections / paragraphs to group the definitions.
3. The results part (especially Section 4.2) contains a huge amount of formal statements with almost no informal descriptions of them; it is definitely not enjoyable to read. I suggest the authors to replace them with informal versions (and also add a paragraph of intuitive description before/after each of them) and defer the formal ones into the appendix.

### Questions
See Weaknesses.

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
In this paper, the authors study the online bandit nonlinear control, which aims to learn the best stabilizing controller from a pool of stabilizing and destabilizing controllers of unknown types for a given nonlinear dynamical system. They develop an algorithm, named Dynamic Batch length and Adaptive learning Rate (DBAR), and study its stability and regret. DBAR achieves better regret bounds than Exp3 under even weaker assumptions.

### Strengths
1. The problem of online bandit nonlinear control is well-motivated.

2. This paper weakens the assumptions in previous works and derive a stronger regret bound. The proof looks correct.

3. There are simulations to support the theoretical findings.

### Weaknesses
Main concerns:

1. It seems to me that the results heavily depend on the assumption that $H(t)$ has finite limitation (Thm 4.2) or $H(t)\leq O(\log t)$ (Thm 4.6), this assumption does not seem to be very mild ($H(t)$ has finite limitation is far from the conclusion in Lem 4.3). What will the result be like without such assumptions? Or is there any further justifications of such assumption? Specifically, the assumption that $H(t)$ is bounded seems particularly strong, as Lemma 4.3 only provides a bound on the *growth* of $H(t)$, not its absolute value. It's unclear how a bound on the growth rate translates to a finite limit, and this leap requires more justification. The practical implications of this assumption also need to be discussed, as it restricts the class of systems to which the results apply.

2. In the experiments, the claim 'While the simulations are on low-dimensional systems for illustration purposes, similar observations can be made for high-dimensional systems.' is made. Is this a conjecture, or is there any experimental evidence for this? It seems not hard to do experiments with higher dimensionality. The lack of concrete high-dimensional experiments significantly weakens the empirical support for the algorithm's scalability. The claim should be backed by at least some experimental evidence, even if it's a simplified high-dimensional scenario.

Some questions and suggestions for writing:

1. The notation $|\mathcal{U}|$ first appears in the table, while it is not defined until Def 2.6.

2. The previous papers depend on 'exponential stability'. What is its definition and how is it stronger compared to 'asymptotic stability'? It would be beneficial to explicitly define exponential stability and contrast it with asymptotic stability, highlighting the stronger convergence guarantees it provides. This would clarify the contribution of the paper in relaxing this assumption.

3. I did not quite understand the motivation of Lemma 4.3. This is too weak to support the assumption $\lim_{t\rightarrow\infty}H(t)<\infty$. The connection between Lemma 4.3 and the assumption on $H(t)$ needs to be clarified. Lemma 4.3 seems to establish a bound on the growth of $H(t)$, but the assumption requires a finite limit, which is a much stronger condition. The paper should explain how the lemma leads to the assumption, or if they are independent, clarify the role of the lemma.

4. Listing the steps to solve for $z,\nu$ in Theorem 4.6 could help justify the results. Providing a more explicit description of how $z$ and $\nu$ are chosen would make the results more transparent and easier to reproduce. The current description is somewhat vague, and a more detailed explanation of the selection process would be beneficial.

### Questions
Please refer to the weakness part.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the problem of online bandit nonlinear control, proposing a new algorithm called Dynamic Batch length and Adaptive learning Rate (DBAR). The algorithm in this paper is designed to handle a nonlinear dynamical system with a mix of stabilizing and destabilizing controllers, offering stability guarantees and regret bounds.

### Strengths
1. The paper provides rigorous theoretical analysis, including stability proofs and regret bounds, which demonstrate the effectiveness of the DBAR algorithm under weaker assumptions. The comparison with existing methods is clear and it strengthens the contribution. 
2. The introduction of the DBAR algorithm relaxes the requirement for exponentially stabilizing controllers, allowing a broader range of controllers to stabilize the system. It also achieves better result for known and unknown $\mathcal{U}$.

### Weaknesses
1. While the theoretical analysis is thorough, the experiments are somewhat limited. The paper focuses on low-dimensional systems (a 2D linear system and a simple nonlinear system), and it would be beneficial to demonstrate the algorithm's performance in more complex, high-dimensional scenarios to validate the practical applicability of DBAR. Specifically, the current experiments do not adequately explore the scalability of the proposed algorithm with respect to the state space dimension, which is a crucial factor in real-world control problems. The lack of experiments on systems with more degrees of freedom makes it difficult to assess the algorithm's performance in more realistic settings.
2. The writing of this paper is not very clear, especially in Section 2 and Section 3. I suggest using more references, formulas, and illustrations to explain the rationale behind the assumptions and the intuition behind the algorithm design, rather than relying solely on extensive text descriptions. The current presentation makes it difficult to understand the motivation behind the specific choices made in the algorithm design, and the lack of visual aids hinders the comprehension of the core concepts. The assumptions, particularly those related to stability, need more detailed explanations and connections to existing literature.

### Questions
1. Could you include more experimental results on complex systems?
2. Could you explain the necessity of Assumption 2.5? You may refer to previous literature to support your explanation.
3. Could you clarify the proof ideas and intuition behind Theorems 4.5 and 4.6? The current explanation is quite brief, and it's difficult to grasp the core proof strategy as well as how the earlier algorithm design relates to this proof. I suggest expanding this section and moving some of the lemma proofs, such as Lemma 4.7, to the appendix.

### Soundness
3

### Presentation
2

### Contribution
2

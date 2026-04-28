# LayoutRL: A Reinforcement Learning-Based Approach to Keyboard Layout Optimization

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3

## Abstract
Keyboards are a key interface between humans and computers, with character arrangements offering numerous layout possibilities. Many existing designs follow standardized ergonomic principles and explore Pareto-optimality in multi-objective functions using metaheuristics or deep learning. In this work, we propose a reinforcement learning-based approach to designing optimized keyboard layouts that integrate both technical and ergonomic considerations. Our results demonstrate that reinforcement learning optimization can produce layouts more efficiently than conventional designs, such as the "QWERTY" keyboard. Specifically, our approach achieves approximately an 12.4\% improvement in ergonomic parameters over traditional keyboards, underscoring the potential for a more data-driven, systematic approach to keyboard layout optimization.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work proposed a RL base method to find the best keyboard layout specifically designed for English. The proposed framework aims to optimize the ergonomic parameters/variables, and the authors have shown that the layout identified by their RL algorithm achieves significant improvement over traditional keyboard layout.

### Strengths
1. RL algorithm for finding the optimal keyboard layout is a new angle to approach the problem.

2. In the fields of Human Computer Interaction, the paper holds great potential where a lower cost layout will not only improve user experience, but also improve productivity. From that perspective, the high level direction/scope of finding a more optimized/improved keyboard layout holds significant importance. However, I have questions about the significance of this particular work in the absence of rigorous validation or user study.

3. The reduction in cost of the layout detected by the RL algorithm is statistically significant compared to the cost of traditional layout, which proves that the RL framework is generally capable to identifying the best layout from a massive corpus, hence eliminating human effort to manually think of and design a better layout.

### Weaknesses
1. While I am excited about the high level direction (optimizing the keyboard layout with ergonomics and productivity considerations), the paper does not explain the implications and significance of the results. For example, how much performance and productivity does the new layout provides (e.g., speed of typing) for actual human participants? If a participant is already trained with a QWERTY layout, how much performance benefit can we expect to see? How long does it take for a person to get used to the new layout (assuming that the person is already trained with QWERTY)? What are the longer term kinematics benefits? In order to actually evaluate success of the project, one needs to be able to answer/discuss some of these points. Otherwise, it's very difficult to understand the significance of the work. 

2.  Why the RL approach is better than a standard optimization based approach? For example, why not genetic search with the same set of constraints? The paper does not provide detailed comparison with the proposed approach (that convert the optimization problem to a sequential decision making RL problem) to a large body of standard optimization based approaches?

3. The performance in the table isn’t highlighted, for which is hard for readers to realize the significant improvement at the 1st time. Although the cost of layout identified by RL is not the best, a gradient table cell color identifying 1st, 2nd, and 3rd best performance will improve the table presentation. 

4. The quality of figures and tables can be improved. Some of the text on the figures can not be easily read.

### Questions
how much performance and productivity does the new layout provides (e.g., speed of typing) for actual human participants? If a participant is already trained with a QWERTY layout, how much performance benefit can we expect to see? How long does it take for a person to get used to the new layout (assuming that the person is already trained with QWERTY)? What are the longer term kinematics benefits? Why the RL approach is better than a standard optimization based approach? For example, why not genetic search with the same set of constraints?

### Soundness
2

### Presentation
1

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
This paper presents a RL-based method to optimize keyboard layouts. Using a handcrafted reward function based on ergonomic principles and by training on large text corpuses, the proposed method is able to generate keyboard layouts with improvements to commonly used layouts (such as "QWERTY" keyboards).

### Strengths
There are a few strengths of this paper:

- Presents a reward function that takes into account important ergonomic principles and transforms them into actionable objective functions
- Generated Reasonable Optimized Keyboard Layout that follows traditional keyboard structure but with lower cost on large text corpuses
- Provided guidelines for restrictions on Keyboard Layout optimization problems that can be useful for further optimization

### Weaknesses
There are a number of significant weaknesses to this paper:

- **Unclear why RL-based approach is the best solution to this problem, or why this problem warrants an RL-based approach**: For a keyboard layout optimization problem with the author(s)' proposed formulation, the order of actions should not matter (given the return is evaluated at the end of the episode). It is thus unclear why a full policy should be learned to adapt to all state/action pairs, and why other optimization methods (such as simulated annealing) are insufficient for such a problem [1]. At the very least, the author(s) could include an ablation with these optimization methods that do not consider states. The problem, as formulated, appears to be a combinatorial optimization problem where the goal is to find the optimal permutation of characters on a keyboard given a fixed cost function. The use of RL, which is designed for sequential decision-making problems, seems like an overkill for this task. The authors should provide a strong justification for using RL over simpler optimization techniques, such as genetic algorithms or direct search methods, which are more commonly used for problems with a fixed objective function.

- **Lack of use of recent innovation in RL**: Recent advancements in reinforcement learning have introduced more efficient learning algorithms (e.g., PPO), and it is unclear if the paper has cited or used them. Furthermore, the paper does not specify the RL algorithm used, making it difficult to assess the method's efficiency and convergence properties. The lack of detail on the specific RL algorithm used and the absence of any comparison with more advanced RL techniques is a significant weakness.

- **Missing Important Technical Details**: Some important technical details on the methods are missing from the paper. For instance, while the author(s) have presented elements of ergonomic rules that contribute to the 'objective function', it is unclear how exactly the final return function was formulated. Moreover, there are no details about the text corpus used to train the model, and I'd be curious to see whether the optimized keyboard layout can generalize to other text corpus in a different domain (e.g., trained on general domain corpus, evaluated on medical corpus). The paper lacks crucial details about the reward function, specifically how the individual ergonomic costs are combined and weighted. The absence of information about the training corpus, such as its size, source, and preprocessing steps, makes it hard to reproduce the results and assess the generalizability of the optimized layouts.

### Questions
Directly corresponding to the weaknesses above:

- Can the author(s) clarify the rationale of using RL for the problem? 
- Can the author(s) provide ablations against other optimization-based approaches? 
- Did the author(s) use more advanced, recently introduced RL learning algorithms?
- Can the author(s) provide a formula for the final return function used?
- Can the author(s) provide details on the training text corpus?
- Was the evaluation done on a held-out text corpus? If not, would it be possible to provide experiment results on a held-out text corpus, preferrable in a slightly different domain than the training text corpus?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces LayoutRL, a reinforcement learning-based method for generating keyboard layouts that are optimized with regard to six ergonomic criteria taken from previous work. The authors motivate this by claiming that previous work has so far not evaluated ergonomic criteria sufficiently. In their results, they show that their method can design a keyboard layout that has a lower cost of corpus completion compared to some classical keyboard layouts and that scores better on the ergonomic criteria. In their comparison, they also compare against the optimized ant-keyboard and while their results show that their best layout scores worst on these metrics the authors reason that this is because they have restricted themselves to a QWERTY-like keyboard layout.

### Strengths
The method the authors introduce is novel in that no previous work has used reinforcement learning to optimize keyboard layouts. Optimizing keyboard layouts has the potential to improve human-computer interaction as it could improve the speed of typing, reduce the number of errors and improve the ergonomic features of a keyboard. In the past keyboards that improve upon QWERTY in this regard (i.e. most notably DVORAK) have seen some level of adoption. Their results show that their method can design keyboard layouts that show some improvement over some of the more classical layouts.

### Weaknesses
I have several concerns that must be addressed before this paper can be accepted:

- Limited novelty: Their novelty mostly stems from using an already known objective function [7] and optimizing it with a simple RL-based method. There is no distinct method contribution that would strongly suggest to include this submission in ICLR (that has a strong focus on algorithmic/method contributions).

- The writing should be improved (see the end) to make the paper easier to follow.

- The explanation of the method is not clear and should be rewritten or improved. Specifically: 
  - Section 2 L106: What does it mean for an “alphabet” to be “mapped to each key”? Should that read as letters being assigned to keys?
  - Section 2.2.: It is unclear to me how these design choices were made. Previous work [2] used a dissimilarity metric to measure the distance of designed layouts from QWERTY instead of relying on hand-crafted design choices. More clearly stating why these design choices were made and how they compare to previous work would help to improve this section.
  - Section 2.2 L209: The authors mention the state space here which has not been explained or introduced yet. 
  - Section 2.3: This section I find to be most confusing. The authors should provide an example to improve the section and reference Algorithm 1 earlier to guide the reader through their method.
  - Section 2.3: The authors should state the dimensions of the state/action value matrix. This would possibly help with some of the confusion. I assume it is of size 95 x 96?
  - Section 2.3: Why is the state transition probability non-deterministic? If the agent assigns a letter to a key it always results in the letter being assigned to this key, correct? This makes the state transitions deterministic.
  - Section 2.3.: Figure 2 shows B34 being mapped to G. What is B34 in this context? From Figure 1 it seems that it is not a coordinate in the keyboard layout. 
  - Section 2.3.: Figure 2 (esp. the font size) needs to be larger. The text next to the matrix on the top left for instance is not readable at all on paper.
  - Section 2.4: The authors state that they run random episodes to randomize the state-action matrix for effective convergence but to me it reads more like an off-policy optimisation step depending on the inner workings of the adjust_corresponding_values function.
  - Section 2.4: In general the section could be improved by explaining why this algorithm was picked over more classical approaches. The authors could for instance explain why they picked this approach over a more simple epsilon-greedy learning approach for training their policy.

- Few comparisons: The authors should compare their best layout to other layouts in the literature, possibly the ones from [1,2,3,6]. While it seems to beat classical layouts - which were not optimized by any algorithm - their results indicate that other optimisation techniques might work better. I would personally also at the very least consider BZQ [6], GA-optimized keyboard [2], Carpalx Sim. Ann. (see [2]) and Dvorak. More would be better though.

- Evaluation of the designed layouts can be improved. First, previous work [7] has used a global score (a linear combination of the scores mentioned in the paper) that makes it easier to compare layouts by a single number. Second, other previous work [4] has calculated the Carpalx effort value [5] to compare keyboards. I suggest the authors include these values or other ways of quantifying their designed keyboard.

- Poor discussion and comparison to other techniques that optimize keyboards: The introduction motivates the paper by claiming that (in contrast to previous work) ergonomic criteria are not always modeled or validated and that keyboard optimisation methods should incorporate them. This seems to be correct but authors could have evaluated other optimized keyboard layouts later to show that there indeed is a gap in the literature. For instance by showing that while related work manages to produce optimized keyboard layouts that they score badly on their ergonomic criteria. This would provide a stronger motivation for both their method and the paper. Such a result could then also be reused in the introduction.

- Poor results: From Table 2 in the paper it seems that the final keyboard designed by LayoutRL is only the best in 1 out of 6 metrics. The ant-keyboard overall seems to be a better keyboard. This makes it unclear why LayoutRL should be used when ACO is available. The authors say that their keyboard is more similar to QWERTY and thus should be preferred but do not validate this claim with experiments. A user study might help to show that their keyboard is preferred by users over other optimised keyboards. In general though [2] has also accounted for similarity to QWERTY and the resulting keyboards thus need to be compared in such a study.

- In Table 2 it is unclear what MLRL is and where it comes from. It certainly is not mentioned in Table 1 and I cannot find another mention in the text. Also, why is it bold?

Other weaknesses:
- I found several spelling and grammar issues. For example L25 (The sentence start is missing), L226, L307 etc. This makes the paper hard to follow in places.
- I believe that throughout the work authors are misusing the word alphabet.

### Questions
The motivation for using RL for optimizing keyboard layouts is not quite clear to me. Can the author elaborate on the motivation?

Will the authors provide code and trained model files to aid reproducibility?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper formulates keyboard layout optimization as an RL problem, using heuristic objectives derived from prior work and several evaluation criteria and comparing with black box optimization-based baselines (e.g. Ant Colony optimization) along with standard layouts like QWERTY and Colemak.

### Strengths
I think formulating the problem this way requires some creativity (e.g. in the design of the state and action spaces), which I acknowledge and appreciate. I also acknowledge that the method appears to work reasonably well, as seen in the evaluation, and has been compared with a reasonable range of baselines. More broadly, I think the application of RL to problems in design and ergonomics is a very promising area and should be explored more, since RL has the potential to better capture behavioral factors of those who ergonomic systems are designed for.

### Weaknesses
My biggest concern with this paper is that the motivation for formulating keyboard layout optimization as an RL problem lacks sufficient motivation. Though I acknowledge RL is a powerful framework, keyboard layout optimization can be much more easily approached through other well-established methods such as those reviewed in this work (e.g. various black-box optimization algorithms).

The paper should clearly establish why RL provides unique advantages over traditional approaches for this particular problem. E.g. this could be justified if one or more of the following conditions were claimed and convincingly demonstrated:
- The goal is to learn user-adaptive strategies for keyboard layout design, where a generalizable policy could automatically customize layouts based on individual typing patterns, language preferences, usage contexts, etc.
- The policy can dynamically modify keyboard layouts over time in response to changes in user behavior or proficiency, shifts in their language usage patterns, different typing contexts (e.g., coding vs. stories), device form factors, etc. It would need to be established that there is a need for this, and users are capable of rapidly learning these layouts.
- The learned policy could transfer insights across languages and scripts, various input modalities (e.g. physical keyboards, touch screens, gesture input like swiping), new character sets or symbols, etc.

Without establishing these (or similar compelling motivations), RL seems to be a more complex solution to a problem that might be better served by simpler, more interpretable approaches.

In addition to this, I find it challenging to interpret the results. For example, the argument made (following from Table 1) is that LayoutRL gets the best results when considering keyboards that use the traditional layout structure. How can this be quantified, in terms of adherence to traditional layouts and the potential impact on downstream users? Without this, it’s difficult to understand what trade-offs are made when using Ant-keyboard, given its better overall results.

Another question is how difficult it would be to retrofit Ant-keyboard to adhere to the traditional layout structure, and what impact this would have on the evaluation. The search/optimization framework still seems like a more natural choice for this task, so it’s conceivable that if this could be done with a minor modification without substantially weakening the results, that might be preferable. A priori, it is not clear to me why the mixture of alphabet and non-alphabet keys compromises usability, or has other issues that arise from it. Additionally, plenty of optimization algorithms could likely admit such a straightforward constraint.

Finally, the adaptation from optimization to RL seems fairly direct: the objective terms described in 2.1 all come from Eggers et al. 2003, and the applicability of these various terms, etc. to RL contexts isn’t considered. As such, the knowledge contribution is limited; it would be interesting to know which of these are useful to an RL based approach, etc.

Minor notes and typos:
- Line 019: “an 12.4%” -> “a 12.4%”
- Line 025: “keyboard” -> “The keyboard”?
- Line 083: “combinational” -> “combinatorial”?
- The figure and table captions are too brief and uninformative. E.g. Figure 3 caption should clearly state what the two sides are, and provide a brief takeaway. Similarly, Table 2 caption should discuss the significance of the * notation used.

### Questions
What are the specific benefits obtained by modeling this problem using RL, over and above optimization based solutions? E.g. what scenarios does this solution apply in that optimization would not?

What are the (ideally, quantified or quantifiable) negative effects of non-adherence to the traditional layout structure’s separation of alphabet and non-alphabet keys?

How difficult would it be to modify Ant-keyboard or a similar approach to introduce the traditional layout constraint?

### Soundness
2

### Presentation
2

### Contribution
2

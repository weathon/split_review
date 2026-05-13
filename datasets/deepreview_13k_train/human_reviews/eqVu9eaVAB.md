# What Matters in Hierarchical Search for Combinatorial Reasoning Problems?

- Decision: Reject
- Scores: 5, 6, 5, 6

## Abstract
Efficiently tackling combinatorial reasoning problems, particularly the notorious NP-hard tasks, remains a significant challenge for AI research. Recent efforts have sought to enhance planning by incorporating hierarchical high-level search strategies, known as subgoal methods. While promising, their performance against traditional low-level planners is inconsistent, raising questions about their application contexts. In this study, we conduct an in-depth exploration of subgoal-planning methods for combinatorial reasoning. We identify the attributes pivotal for leveraging the advantages of high-level search: \emph{hard-to-learn value functions, complex action spaces, presence of dead ends in the environment, or using data collected from diverse experts}. We propose a consistent evaluation methodology to achieve meaningful comparisons between methods and reevaluate the \mbox{state-of-the-art} algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper reports on an empirical evaluation of two types of algorithms for solving combinatorial search problems: “standard” graph search algorithms and “hierarchical search” algorithm. Worth noting that, unlike the classical literature on combinatorial search, here the main setup is that the algorithm does not have a given domain-specific heuristic. Instead the algorithm is  given a dataset of solutions to problems in the same domain, and can learn from this dataset how to solve other problems in the same domain. The “standard” graph search algorithms considered in this work learn a heuristic function (referred to as a value function here) and the “hierarchical search” algorithms considered in this work also learn a method to generate subgoals in this domain and performs a higher-level planning in the space of subgoals. 
The results show that hierarchical search methods are often much better. The purpose of this work is to dig deeper and analyze why and when they are better. This is done by adding noise to the heuristic, considering test problems significantly different from those used for training, domains with dead-ends, and analyzing domains with particularly many actions. The results, very concisely show that hierarchical search is better in general, and in particular when the heuristic is weak, the training is very different from the test, and when there are many dead-ends or many actions.

### Strengths
1.	The problem is interesting, the evaluation is extensive. 
2.	The conclusions drawn from the evaluation are useful for future research and implementer. 
3.	Some interesting insights into the nature of combinatorial search problems.

### Weaknesses
The paper is far from being self-contained. This can be viewed by the large number of appendices. To me, this work is more fitting for a journal than a conference paper. A major example for this is Theorem 1, which one cannot fully understand without reading the appendices. 
In addition, the scope is maybe not a perfect fit for a top conference, as they mainly studied the existing algorithms and the conclusions are not ground breaking.

### Questions
1.	Is my depiction above of the setup – no domain-specific heuristic, but yes data, is correct?
2.	Are the methods for detecting subgoals domain independent, i.e., only based on the given dataset, or do they also include domain-specific hard coded procedures. 
3.	In Section 3, the use of “planning” in the third bullet is not clear to me (and I’ve experience in planning). 
4.	Where you use the term value function, I think you mean state value heuristic? My guess is that if any, the term reward would be more accurate e(as per reward shaping)

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper examines the efficacy of hierarchical search methods in combinatorial reasoning problems compared to low-level search methods. It identifies specific conditions where hierarchical search excels due to the handling value function approximations and complex action spaces. The paper proposes standardized evaluation guidelines for search methods and reassesses state-of-the-art algorithms. The research highlights how hierarchical search methods can mitigate the challenges of large action spaces and variable training data.

### Strengths
1. The paper offers a novel analysis of hierarchical versus low-level search methods in NP-hard problem domains, a less frequented area of research with significant implications for AI optimization tasks (Section 1). 
2. The paper's structure is logical and well-articulated. It presents complex methodologies and findings in a manner that is accessible to readers with a background in AI and machine learning. The diagrams and tables effectively illustrate key points and comparisons. 
3. Robust empirical analysis supports the claims, with extensive testing across various scenarios to demonstrate the superior performance of hierarchical methods under specific conditions. 
4. The findings contribute valuable insights into applying hierarchical search methods, particularly their resilience to value function noise and their efficiency in environments with complex action spaces, which are critical for advancing AI capabilities in real-world applications.

### Weaknesses
1. The study’s focus on specific NP-hard problems may limit the generalizability of the findings. Additional studies could help determine if the advantages of hierarchical methods hold across a broader range of combinatorial problems (General Discussion).
2. The performance advantages of hierarchical methods heavily depend on the diversity and quality of training data. The paper could delve deeper into the effects of lower-quality or less diverse data sets (Section 5.1).
3. While the paper addresses the effectiveness of hierarchical search methods, it underplays their computational complexity and resource demands, which could be a significant drawback in practical applications (Section 4).
4. The robustness of hierarchical methods to training data variability could lead to overfitting if not adequately managed. The paper could discuss strategies to mitigate this risk (Section 5.2).
5. A missing comparison with other foundation models in combinatorial problems, such as DeepCubeA, which are trained in an unsupervised setting.

### Questions
1. How adaptable are hierarchical search methods to other complex domains outside the specific NP-hard problems tested, such as real-time decision-making environments? 
2. How do computational constraints affect the performance of hierarchical search methods compared to low-level search methods in real-world applications? 
3. What improvements do the authors foresee or recommend for hierarchical search methods to handle larger datasets or more variable environments effectively? 
4. Could the authors elaborate on the standardized evaluation guidelines proposed? How do these guidelines compare to existing benchmarks in AI research?

### Soundness
4

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper answers two primary questions: 1. Will hierarchical search outperform classical search under the same heuristic function and other settings? 2. In what situations do hierarchical search methods significantly outperform classical search? The authors conduct experiments to compare the performance of hierarchical search with classical search, finding that hierarchical search performs better in instances with complex action spaces and less guided heuristic functions. Additionally, data with high diversity also favors hierarchical search.

I am uncertain whether the authors have addressed all possible influencing factors to arrive to the final conclusion. Since hierarchical search relies on a subgoal generator, which functions as another form of heuristic, this additional generator could significantly influence the improved performance of hierarchical search compared to classical search, especially in tests involving noisy value functions. This reliance on a subgoal generator may also be a critical factor that warrants further investigation.

And the motivation behind this paper is also unclear. After answering these two questions, what potential impact could this research have on future algorithm design or other related fields?

### Strengths
Strengths:

- The paper includes numerous experiments examining various factors that could impact the performance of algorithms.

### Weaknesses
Weaknesses:

- The motivation for the study is unclear.

- The presence of a subgoal generator could heavily influence the analysis of the experiments. Specifically, the paper does not sufficiently explore the potential impact of the subgoal generator's quality on the overall performance of hierarchical search. Since the subgoal generator is essentially another form of heuristic, its influence on the results needs to be rigorously examined. The experiments should include ablations that vary the quality of the subgoals, such as by introducing noise or limiting the search space of the subgoal generator, to understand its impact on the final results.



### Questions
Other Comments:

- Line 52: "low-level" likely refers to hierarchical algorithms.

- Line 59: The phrase "hard-to-learn value functions" requires clarification.

- Line 83: There is a reference error.

- Line 175: The description “Planner that determines the order in which subgoals are generated” seems to refer to the "Subgoal generator."

- Figure 7: Since both AdaSubS and kSubS rely on value functions, why do they not experience a significant drop in performance with high noise levels? For instance, kSubS in Sokoban (2 to 100 noise) shows better results.
  
- Figure 7: What is the value scale (minimum and maximum) for the value function, given that A* and BestFS tolerate a 0.5 error in the Rubik’s Cube test?

- Figures: Some figures should be adjusted to enhance readability by increasing font sizes and displaying full labels, such as “Step” and “Subgoal” in Figures 8 and 9.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper reviews hierarchical approaches to reasoning tasks, in particular comparing hierarchical search to low-level search. 

While the paper has no serious flaws, I am not entirely sure what to make of it. The insights the paper provides may be useful, but I am somewhat worried if they are contrived or overstated. In general, I think many would agree subgoal methods are worth pursuing, so arguing for this alone may not be entirely useful. At the same time, there are theoretical reasons why subgoal methods are imperfect, namely the upwards refinability property, e.g. that an optimal solution can be expressed in terms of abstractions. In general, subgoal methods may not be as flexible as a method which can use low-level actions (for an arbitrary problem at least), and to retain completeness a system needs to be able to use both abstract and primitive actions. Accordingly, I am somewhat skeptical of the takeaways, which seem to be based on limited empirical evaluation compared to what they claim. Regardless, I think the breakdown of benefits into the four separate takeaways is useful and overall think the paper is headed in the right direction.

### Strengths
The paper summarizes hierarchical reasoning methods and performs experiments to show their desirable properties. 

The insights regarding robustness to noisy value functions are quite useful and seem to be well supported by the experiments.

Similarly, the breakdown of claims regarding complex action spaces, ergodicity, and data diversity is useful, but I am less certain about the validity of these claims, given that there are theoretical reasons why they may not be true.

### Weaknesses
I believe the related work section could be better organized, it didn't seem to flow with the rest of the paper so maybe it could be at the very end instead? e.g. Section 1 seems to better flow into Section 3. 

I think the paper could better distinguish between planning and learning -- many of the problems discussed are amenable to classical algorithms, so where does learning come in best and why?

I think the paper would benefit from more theory -- while subgoal methods may have benefits in the experiments performed, their theoretical properties are not entirely discussed. In particular, issues such as the upwards refinability property make me skeptical of the second takeaway (line 417). In other sections, I think the paper would benefit from contrasting theory and experiment. 

In general, the writing was somewhat difficult to follow and clarity could be improved.

### Questions
I don't have any specific questions about the paper -- but there are likely parts of it I did not fully understand.

### Soundness
3

### Presentation
2

### Contribution
2

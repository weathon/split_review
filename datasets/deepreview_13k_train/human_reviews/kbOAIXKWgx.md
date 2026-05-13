# Re-evaluating Open-ended Evaluation of Large Language Models

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
Evaluation has traditionally focused on ranking candidates for a specific skill. Modern generalist models, such as Large Language Models (LLMs), decidedly outpace this paradigm. Open-ended evaluation systems, where candidate models are compared on user-submitted prompts, have emerged as a popular solution. Despite their many advantages, we show that the current Elo-based rating systems can be susceptible to and even reinforce biases in data, intentional or accidental, due to their sensitivity to redundancies. To address this issue, we propose evaluation as a 3-player game, and introduce novel game-theoretic solution concepts to ensure robustness to redundancy. We show that our method leads to intuitive ratings and provide insights into the competitive landscape of LLM development.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a methodology for rating-based evaluation of Large Language Models (LLMs). The motivation arises from the shortcomings of the current Elo rating system, which may suffer from redundant or invariant prompts, leading to biased or less robust evaluation results. The proposed solution extends the evaluation method from a common 2-player game scenario to a 3-player game, incorporating a measure of separability based on game outcome distributions to favor prompts that better differentiate between models. The quality of the proposed method is assessed using Shannon entropy over model or prompt strategies, and the strategy derivation is based on Coarse Correlated Equilibrium (CCE), which is more accessible compared to the commonly used Nash Equilibrium (NE). Experimental results show that the proposed evaluation method effectively resists the impact of redundant prompts while maintaining similar performance in standard scenarios.

### Strengths
* The study of LLM evaluation addresses a promising and urgent need. The proposed method appears to be a reasonable approach for focusing on separability among LLMs, especially for those fine-tuned from the same foundational model.
* Including the condition of prompts in the rating evaluation is a straightforward approach, and I believe this direction will soon gain more popularity.
* The overall narrative is promising, supported by sufficient experiments that demonstrate the robustness of the evaluation method against redundancy.
* Although I did not go into the details in the appendix to verify all theoretical aspects, my rough review suggests that they are likely correct.

### Weaknesses
 * The main idea is based on the fact that the importance of prompts in average cases may not be balanced; however, the proposed solution may lead to exploitation by niche prompts if LLMs share similar general abilities and some major prompts are marked as redundant. This approach lacks a mechanism to verify prompt redundancy. For a more formal evaluation, it would be better to provide some information on redundancy rather than directly applying the inferred results.
* I found the use case of the proposed method highly related to game balance analysis. It would be beneficial to discuss the strengths and weaknesses of Elo ratings in greater detail, such as their scalar strength representation, which is better than vanilla win values but cannot handle scenarios like Rock-Paper-Scissors. The discussion mainly focused on Elo’s inability to handle redundancy, but it inherently has some resistance to redundancy, at least compared to vanilla win values.
* I have concerns about the focus on the utility of separability. Is high separability always beneficial for evaluation? In my understanding, it can sometimes lead to biased positioning, and it requires more careful assessment rather than direct application.

### Questions
* How can we identify redundant prompts or models? Would it be necessary to include human verification of redundancy?

* Scalar rating evaluations still suffer from intransitivity issues, as seen in Rock-Paper-Scissors scenarios. Does LLM evaluation face this problem? If so, does your method have the ability to handle it?

* I found some recent game balance research related to this problem. Is LLM evaluation similar to game balance analysis? For example:
    * Bilevel Entropy-based Mechanism Design for Balancing Meta in Video Games. Adaptive Agents and Multi-Agent Systems (AAMAS), 2023.
        * Discusses game design aimed at maximizing strategy entropy to achieve balance.
    * Identifying and Clustering Counter Relationships of Team Compositions in PvP Games for Efficient Balance Analysis. Transactions on Machine Learning Research (TMLR), 2024.
        * Discusses redundant settings and the problem of using strategy entropy, proposing conditional analysis with evaluation ratings.

* What are the trade-offs of the proposed evaluation method? It is clearly stated that it can alleviate redundancy, but what are the potential drawbacks? Are there risks in excluding some common evaluation prompts, even if they seem redundant? It would be valuable to know if the proposed method has any specific limitations when applied, especially in cases where common prompts might still hold evaluative value despite redundancy concerns.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This work studies an equilibrium rating framework that can scale to real-world LLM evaluation and move beyond traditional Elo ratings. The authors start by displaying that Elo ratings are sensitive to redundancy. Then, the authors introduce their specific method, describing the proposed rating method in terms of gamification. The authors then provide several results, finding that the proposed equilibrium ranking framework is fairly consistent with Elo rankings and that the proposed system is invariant to redundancy.

### Strengths
Strengths:
+ This paper has an abundance of citations and explains how the proposed work relates to those prior well. 
+ There are several interesting, important results. Figure 2, specifically, provides a very clear indication of the utility of the proposed equilibrium ranking approach.

### Weaknesses
Weaknesses
- I found the paper a bit difficult to read. As the paper is a bit outside my exact expertise, this difficulty may be attributed to that. However, if other reviewers also found difficulty in understanding the exact details in the methodology section, I would recommend expanding this section with additional intuitive explanations and also expanding some of the descriptions in the appendix.
- Figure captions could be improved by concluding with important takeaways.

### Questions
Please address the weaknesses noted above.

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
4

### Summary
This paper explores a new approach to evaluating LLMs in open systems to address the bias introduced by Elo, proposing an evaluation framework based on game theory that views the evaluation process as a three-player game involving the " promptplayer," "king player," and "rebelplayer." By introducing novel solutions applicable to both general and game settings, the proposed method is more robust in handling data redundancy and excels in balancing model skills. Experimental results demonstrate the effectiveness of this approach.

### Strengths
This paper is good. Firstly, from a technical perspective, it introduces a 3-player game model based on game theory, providing equilibrium solutions applicable to N-player games. This is highly innovative in my opinion. Moreover, the paper conducts an analysis based on this paradigm, utilizing Affinity Entropy to meet assumptions and thereby addressing the limitations of traditional Elo evaluation methods in handling redundant data and biases. 

Secondly, there is a very close integration between the main text and the experimental section of the paper. The theoretical design of the game theory model and its experimental validation complement each other, showcasing the effectiveness of the method on real-world datasets. The authors demonstrate the advantages of the Affinity Entropy method through theoretical analysis, which is further supported by experimental data, ensuring a coherent and consistent research logic.

Lastly, in terms of experimental design, the authors conducted thorough validation on real open LLM evaluation datasets, demonstrating the robustness and wide applicability of the method. The introduction of various comparison methods and key evaluation metrics adds to the robustness of the study.

### Weaknesses
There are a few points that confuse me:
1. In the background section, the introduction to NE and CCE seems somewhat limited, although this is a focal point of the paper. Insufficient explanation might lead to misunderstandings upon re-reading. LLE, a refinement of Nash Equilibrium, is also an important concept, yet it is only mentioned in section 3.2, causing some logical confusion. The paper would benefit from a more thorough discussion of these concepts early on, including their limitations and relationships, to provide a solid foundation for the proposed method.
2. In the paper, what specific meaning does "p" represent in the context of Affinity Entropy? Is it reasonable to directly set p=1 in Theorem 1? The subsequent appearance of p in D_{pq} further adds to the confusion. The paper needs to clarify the role of 'p' as a hyperparameter, explaining its impact on the entropy calculation and the rationale behind setting it to 1 in the theorem, as well as its use in D_{pq}. A more detailed explanation of the parameter's influence on the results is needed.
3. Could it be beneficial to consider including more benchmark comparison methods, such as other evaluation systems based on game theory or related equilibrium solutions, to clearly demonstrate the relative performance of this method across different evaluation frameworks? The current comparison to Elo is useful, but the paper could benefit from a more comprehensive comparison to other game-theoretic approaches to highlight the specific advantages of the proposed method.

### Questions
In Weaknesses

### Soundness
3

### Presentation
2

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
The current evaluation focuses on assessing a specific ability, but the emergence of technologies like LLMs has made the evaluation of open-ended tasks more important. Existing methods use Elo ratings for evaluation, but this approach's sensitivity to redundancy may lead to biased assessments. The authors propose a game theory-based evaluation method to address this issue. Experimental results indicate that this method can effectively identify prompts that can be distinctly differentiated and is less sensitive to redundancy compared to Elo-based methods.

### Strengths
The motivation of this paper is relatively meaningful, and studying the impact of evaluation on the development of LLMs is indeed an important issue, especially for open-ended evaluation.

Using game theoretical methods to assess the open-ended response capabilities of LLMs seems to be a relatively novel approach.

### Weaknesses
The article severely lacks background information, leaving readers quite confused about its position in the current research landscape. The Background section is too general; at least, it should introduce what 'king-of-the-hill' used in the actual modeling of this paper is. The Related Works section also fails to fulfill its intended purpose and function in the whole paper. I believe there are far more rating methods than those mentioned (such as [1][2] mentioned later). The differences between the method in this paper and other rating methods, other Elo-based methods, and other game-theoretic methods are not explained in detail. Moreover, the contribution of this paper is unclear. What specific shortcomings of the Elo-based method does it aim to address? Is it the robustness and sensitivity to redundancy mentioned in the abstract, or the poor skill assessment mentioned in section 1.1? Given the unclear statements in this paper, it is difficult for me to evaluate its contribution. If there are any misunderstandings on my part, I welcome further discussion at a later stage.

The paper emphasizes that this method can be applied to fully open skill assessments, but I believe its openness and generality come from the scoring model based on LLM (such as the gemini-1.5-pro mentioned in the paper). This is not a satisfactory solution, and what are the essential advantages of this over traditional LLM-eval-based methods (such as AlpacaEval [1][2])?

Figure 3 is confusing and lacks explanations for the connections. Figure 5 is even more perplexing, as it is unclear what the purpose of displaying these color blocks is and what it is trying to convey.

The experimental section lacks a comparative baseline. How much advantage does this evaluation method have over existing methods (such as various Elo-based methods and previous game-theoretic methods mentioned in the related works section)? Additionally, the dataset used in the experiments of this paper consists of only 500 questions, which is not a sufficiently convincing amount of data.

### Questions
Around line 60, why is this setting a necessity? I understand that using game-theoretic methods might have certain advantages, but why must this paper choose this type of method?

This paper uses gemini-1.5-pro as the judger. What considerations went into this choice? Why not use other more powerful models?

The text repeatedly mentions skill, skill entropy. What exactly is the definition of skill in this paper? Is it capability? If so, why can't we use targeted evaluations, or LLM-eval (in fact, I think this paper is also a type of LLM-eval method), and must instead use Elo-based methods?

For other questions see the **Weaknesses** section.

### Soundness
3

### Presentation
2

### Contribution
3

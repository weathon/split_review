# Advantages, Risks and Insights from Comparing In-Context Learning Models with Typical Meta-Learners

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 8, 3

## Abstract
We investigate in-context learning (ICL) models from the perspective of learning to learn. 
Unlike existing studies that focus on identifying the specific learning algorithms that ICL models learn, we compare ICL models with typical meta-learners to understand their superior performance. 
We theoretically prove the expressiveness of ICL models as learning algorithms and examine their learnability and generalizability across extensive settings. Our findings demonstrate that ICL with transformers can effectively learn data-dependent optimal learning algorithms within an inclusive space that encompasses gradient-based, metric-based, and amortization-based meta-learners. 
However, we identify generalizability as a critical issue, as the learned algorithms may implicitly fit the training distribution rather than embodying explicit learning processes. Based on this understanding, we propose transferring deep learning techniques, widely studied in supervised learning, to meta-learning to address these common challenges. As examples, we implement meta-level meta-learning for domain adaptability with limited data and meta-level curriculum learning for accelerated convergence during pre-training, demonstrating their empirical effectiveness.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper begins by framing the rise of large language models (LLMs) and their use of in-context learning (ICL) to perform diverse tasks without fine-tuning. This sets up ICL as a unique form of "learning to learn," contrasting with traditional meta-learning models. A theoretical foundation is provided, showing that ICL, particularly with transformers, can express and replicate the behaviors of all main meta-learning approaches (gradient-based, metric-based, and amortization-based). The paper tests ICL’s ability to learn optimal algorithms in three task types, showing that it can indeed achieve data-dependent optimal performance on simple, homogeneous tasks. However, when tasked with mixed types, ICL models exhibit implicit (distribution-sensitive) learning rather than general, explicit algorithm selection. This distinction introduces the core limitation: limited generalizability. To address generalizability and efficiency issues, the authors suggest transferring established deep-learning techniques into the meta-learning realm. They propose meta-level meta-learning for domain adaptability (training ICL models to quickly adapt to new domains with limited data) and meta-level curriculum learning to accelerate pre-training.

### Strengths
- The paper provides a theoretical foundation for understanding ICL models as learning algorithms, proving their expressiveness and comparing them to traditional meta-learning algorithms.
- By comparing ICL with various meta-learning techniques, it offers insights into how and why ICL might outperform traditional meta-learning methods due to its flexibility in the hypothesis space.
- The paper highlights the critical issue of generalizability in ICL models and offers potential solutions to improve it.

### Weaknesses
 - The extensive theoretical background may limit accessibility for practitioners interested in practical applications, as certain concepts (e.g., implicit vs. explicit optimality) are dense and could benefit from simpler, more intuitive explanations.
- The proposed solutions, meta-level meta learning and meta-level curriculum learning, are promising but lack empirical evaluation on complex, real-world tasks where curriculum ordering could be less clear-cut. Researchers are suing ICL since it can save us from training tons of parameters, although propose method can improve ICL’s performance on specific domain with very limited data for adaptation and transferring deep-learning techniques to the meta-level is a good point, the proposed method lack its practicability.
- There is a vague treatment of data dependency in "optimal" algorithms. The paper mentions data-dependent optimality without fully clarifying how this dependency impacts performance across tasks. The authors do not delve into specific criteria or metrics for measuring optimality across distributions, making it challenging to objectively evaluate their claims.

### Questions
- How would you define or quantify the "optimality" of the ICL model’s learning algorithm in real-world settings with diverse and complex task distributions?
- ICL demonstrates limited generalizability on tasks from seen types, and is sensitive to the data distribution, why this behavior (distribution-sensitiev) is called as "implicit"? How the term "implicit" is defined in this paper?
- Does ICL prioritize simpler or more complex tasks, and what strategies might be implemented to balance performance across tasks of differing complexity levels? Given the challenges of defining a task "difficulty" hierarchy in real-world scenarios, how would you propose constructing an effective curriculum for complex, real-world datasets?
- Does increasing the size or diversity of the training dataset systematically improve generalization across unseen distributions?

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
4

### Summary
This paper investigates ICL model from a learning-to-learn perspective, examining its expressiveness, learnability and generalizability as a meta-learner. It theoretically demonstrates that ICL, when integrated with a transformer, is expressive to perform various existing categories of meta-learning algorithms. The paper also reveals that while the ICL model can learn data-dependent optimal algorithms, but it is not "algorithm selection". Finally, it proposes training ICL models using a task-level meta-learning framework and with curriculum.

### Strengths
1. The exploration of the ICL model from a learning-to-learn perspective is thorough and yields significant insights, particularly in enhancing our understanding of ICL's role in large transformers. Notably, the clarification that "ICL is not algorithm selection" challenges previous interpretations and adds depth to the academic discussion on this topic. 
2. The clarity and logical flow in Sections 3 and 4 are particularly commendable, making complex findings accessible and substantiating the solidity of the research.

### Weaknesses
1. The introduction section could be improved for better accessibility. Key concepts such as "expressiveness," "learnability," and "generalizability" should be clearly defined early. For instance, integrating these definitions in the introduction section would enhance comprehension and engagement from the outset. Additionally, Figure 1 needs a clearer explanation to effectively convey its intended message. 
2. Another concern is the validation of the proposed methods, which currently relies solely on simplistic synthetic data. This limitation raises questions about the practical applicability of the methods in real-world scenarios.

### Questions
Could the authors elaborate on whether the proposed methods can be adapted for use with real-world datasets? If so, what modifications or considerations would be necessary to accommodate the complexities of real-world data?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Summary:
This paper studies in-context learning (ICL) models from the perspective of meta-learning with solid theoretical analysis and experiments. 

Contributions:
1.It theoretically proved that the hypothesis space of ICL encompass the hypothesis spaces of typical meta-learners.
2. it experimentally verified that ICL with transformer learns the optimal algorithms by designing different types of meta-learning tasks, and several other aspects.
3.It proposed new techniques including meta-level meta-learning and meta-level curriculum learning to improve ICL’s performance and convergence, respectively.

### Strengths
1.The paper is well-motivated, well-written and easy to follow.
2.The topic discussed in this paper is interesting and worth studying.
3.The proposed assumptions are proved and confirmed with solid theoretical analysis and experiments.
4.The contribution of this paper is solid, please refer to the summary of contributions.

### Weaknesses
1.The paper only focuses on ICL with transformer, ICL with other deep architectures are also worth exploring 
2.Typo: line 482 tunie

### Questions
1.Please elaborate why M^2-ICL without adaptation sometimes works worse than ICL
2.For meta-level curriculum learning, how would you define the complexity of other tasks, such as classification tasks? Could you add some more experiments with regard to few-shot classification tasks?
3.For task generation, what is the definition of p_f, and how to obtain p_f for different tasks?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates the meta-learning capabilities of in-context learners (ICLs) by comparing them to state-of-the-art meta-learning algorithms. The authors demonstrate how ICL can learn optimal algorithms in various scenarios and propose a strategy to enhance generalization by incorporating techniques from supervised learning. They also explore the impact of applying curriculum learning during the training phase.

### Strengths
*  The observation that different meta-learning methods generalize best on their respective task sets is interesting. The paper shows that ICL, when trained on a mixture of task sets, can outperform individual meta-learners.
* The study of generalization across tasks is valuable for understanding the capabilities of ICL in various domains.

### Weaknesses
 *  The paper is poorly written, with numerous typos and a lack of clarity, making it difficult to follow. A complete revision is necessary.
*  The related work section needs significant improvement. Rather than simply listing various meta-learning studies, it should focus on situating this work within the broader literature, especially by incorporating more relevant references on in-context learning and model generalization.
*  Several key references are missing in the text, including citations for MatchNet, ProtoNet and CNP in line 244.
*  There are incorrect assumptions present throughout the paper. For example, lines 82–85 incorrectly claim that transformers are inherently permutation-invariant, and line 453 mistakenly implies that all in-context learners are pre-trained, whereas studies such as [1] and [2] demonstrate otherwise.
* The main text and the appendix feel disconnected, almost as if they belong to separate studies. Mathematical proofs, even if valuable, bring a little contribution if left in the appendix.
*  The experimental design is weak, and there is no reference to standard literature or pipelines for task creation. The authors should either adopt state-of-the-art experimental methodologies or provide a strong justification for deviating from established practices.
*  More details about the task generation process  should be included in the main text, not only in the appendix section. This would give readers a better understanding of the experimental setup and strengthen the paper’s presentation.
*  The results presented in Figure 7, which show that adapting a model to a different distribution leads to higher squared error, seem trivial. Furthermore, the meta-meta-learner does not outperform in a meaningful way, so the contribution of this section is unclear.
*  The experiments with curriculum learning are insufficient to demonstrate its effectiveness in improving in-context learning. A more robust and comprehensive evaluation is needed to validate these claims.
*  What is the meaning of Figure 1? What guarantees the orthogonality among the three methods?
*  In the first part of the paper, the authors claim that ICL can act as different types of meta-learners (gradient/metric/amortization-based) and learn the "optimal" algorithm. However, the notion of "optimal" is vague and needs to be better defined within the context of the study.

### Questions
See Weaknesses part.

### Soundness
1

### Presentation
1

### Contribution
1

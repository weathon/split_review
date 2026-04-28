# O-Edit: Orthogonal Subspace Editing for Language Model Sequential Editing

- Decision: Reject
- Avg Score: 5.67
- Scores: 5, 6, 6

## Abstract
Large language models (LLMs) acquire knowledge during pre-training, but over time, this knowledge may become incorrect or outdated, necessitating updates after training. Knowledge editing techniques address this issue without the need for costly re-training. However, most existing methods are designed for single edits, and as the number of edits increases, they often cause a decline in the model's overall performance, posing significant challenges for sequential editing. To overcome this, we propose Orthogonal Subspace Editing, O-Edit. This algorithm orthogonalizes the direction of each knowledge update, minimizing interference between successive updates and reducing the impact of new updates on unrelated knowledge. Our approach does not require replaying previously edited data and processes each edit knowledge on time. It can perform thousands of edits on mainstream LLMs, achieving an average performance improvement that is 4.2 times better than existing methods while effectively preserving the model's performance on downstream tasks, all with minimal additional parameter overhead.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces O-Edit and O-Edit+, two methods for sequential knowledge editing in large language models (LLMs) that address the challenge of catastrophic forgetting during multiple edits. The key idea lies in performing edits in orthogonal subspaces, ensuring that new knowledge updates minimally interfere with both previously edited knowledge and the model's implicit knowledge. The methods work by projecting update directions into orthogonal subspaces and using post-processing techniques to maintain complete orthogonality between different knowledge updates. Through extensive experiments on Mistral-7B and Llama3-8B models using the COUNTERFACT and ZsRE datasets, the authors demonstrate that their approaches significantly outperform existing methods like ROME and MEMIT, especially when handling large numbers of sequential edits (up to 1,500). The methods also better preserve model performance on downstream tasks while requiring minimal additional parameters. The paper provides theoretical and experimental evidence showing that strong orthogonality between update matrices is crucial for successful sequential editing, offering a promising direction for future research in this area.

### Strengths
1. The results look excellent compared to previous approaches.
2. The paper is well-written and easy to follow.
3. The analysis is comprehensive, which helps to understand the key insights of the proposed method.

### Weaknesses
1. The method is only evaluated on two datasets. It would be interesting to see results on more scenarios where knowledge editing is important.
2. Although the idea of orthogonal subspace editing looks interesting, I am wondering is it possible to ensure the orthogonality of the direction of each knowledge update when the editing number scales to the millions level? In updating a pre-training LLM, I think it is meaningful to investigate knowledge editing where the training corpus is so large that the number of edits is hard to count.



### Questions
Have you explored the influences of context lengths on knowledge editing?

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
4

### Summary
The author finds that the update weights of existing knowledge editing methods are within low-rank subspaces. Based on this, the author proposed two knowledge editing methods (O-Edit & O-Edit+) based on orthogonal subspaces to handle sequence editing. O-Edit and O-Edit+ both aim to ensure that the current updates aligns vertically with the previous updates and the original knowledge. O-Edit introduces new loss function to ensure orthogonality, while O-Edit+ directly guarantees orthogonality between different knowledge. The author demonstrates through experiments that ensuring the orthogonality of knowledge helps improve the performance of existing methods in sequence editing.

### Strengths
* Logical consistency: based on the assumption that knowledge from orthogonal domains has minimal mutual influence, the author has proposed two methods, O-Edit and O-Edit+, respectively. Furthermore, O-Edit+ ensures a stronger orthogonality between different knowledge. Experimental results also demonstrate that O-Edit+ exhibits superior performance.
* Innovative: the use of orthogonal subspaces to enhance sequence editing is not only novel but also intuitive.
* The ablation study demonstrates that the method proposed in the paper indeed brings performance improvement.

### Weaknesses
 **Main Weaknesses**

The effectiveness of O-Edit and O-Edit+ in sequence editing needs further validation.

* *W1*: In Line 51, the author says "there is still no effective solution to these problems". However, some progress [1, 2] has been made in sequence editing. I suggest the author compares these methods to demonstrate the effectiveness of O-Edit and O-Edit+ in sequence editing. Specifically, a comparison against methods that utilize external memory or knowledge bases for sequential editing is needed to understand the trade-offs between direct weight modification and memory-based approaches.
* *W2*: I suggest the author to increase the number of sequence edits T, in order to explore the limits of O-Edit and O-Edit+. GRACE [1] can make the number of editing to 3,000. The current experiments do not sufficiently demonstrate the scalability of the proposed methods, especially when compared to memory-based methods that can handle a large number of edits. A more thorough investigation into the performance of O-Edit and O-Edit+ with a significantly higher number of edits is needed to make a compelling case for their effectiveness in long sequence editing scenarios.

**Minor Weaknesses**
* *W3*: Previous work [3] has found that increase in the norm of edited parameters leads to a decrease in model performance and edit failures. Therefore, I suggest conducting additional experiments to demonstrate that O-Edit and O-Edit+ can suppress the increase in the weight norm. It is crucial to show that the proposed methods can effectively control the norm of the updated parameters to avoid performance degradation and edit failures, especially in long editing sequences.

**Missing References**
* A Survey on Knowledge Editing of Neural Networks. (2023)
* Editing Large Language Models: Problems, Methods, and Opportunities. (2023)

### Questions
**Main Questions**
* *Q1*: There is a research [1] indicating that existing editing methods are not suitable for multi-hop editing. This could be due to conflicts between new and old knowledge. So, I have the following question: can O-Edit and O-Edit+ in this article be applied to multi-hop editing tasks with orthogonal subspace?
* *Q2*: I want to delve deeper into the issue of forgetting previous edited knowledge in O-Edit and O-Edit+. I hope the author studies the issue of forgetting previous edited knowledge when editing up to 1500 pieces of knowledge.

**Minor Questions**
* *Q3*: Do O-Edit and O-Edit+ incur additional time costs?


$Ref$:

[1]  Mquake: Assessing knowledge editing in language models via multi-hop questions. (2023)

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a novel approach to continuous editing by orthogonalizing the direction of each knowledge update, thereby minimizing interference between successive updates and reducing the impact of new updates on unrelated knowledge. This results in performance improvements while effectively maintaining the model’s performance on downstream tasks.

### Strengths
- This paper proposed an innovative knowledge editing approach to address the challenge of continuous editing.
- Continuous editing of the model is achieved without introducing additional parameters.
- The theoretical derivations are detailed and convincing.

### Weaknesses
 - The primary experiment was conducted using only CounterFact dataset, without performing tests on a broader set of datasets.
- There is no further elaboration on the time and computational costs associated with O-Edit.
- It would be beneficial to analyze and compare the advantages of O-Edit over other knowledge editing methods such as WiSE and GRACE.
- I noticed that generalization is reduced at T=200. I think this is due to your constraints leading to insufficient thoroughness in editing, which increases generation and decreases localization.
- The theoretical validity of the CGS needs further exploration, such as investigating the relationship between CGS and the offset of the model's hidden state.

### Questions
- I found that as the number of edits increases, the loc metric significantly decreases. Is this because the 7B model has a smaller dimensionality? Could you investigate the relationship between O-Edit's loc and the number of edits with different model sizes?
- Additionally, what are your thoughts on the fact that different vectors are almost orthogonal at higher dimensions? Does this mean that the effect is not significant in larger models?
- For methods like ROME and MEMIT that modify model parameters, they usually have better portability. Could you explore how the portability of your method changes after multiple edits?

In summary, this paper presents a significant advancement in sequential knowledge editing by proposing an orthogonal subspace approach. However, expanding the evaluation to more datasets, detailing computational costs, and exploring broader theoretical insights would enhance the paper’s depth and practical relevance. Additionally, addressing the questions raised could provide valuable insights for future work. Overall, this is a promising direction, deserving further investigation.

### Soundness
2

### Presentation
2

### Contribution
3

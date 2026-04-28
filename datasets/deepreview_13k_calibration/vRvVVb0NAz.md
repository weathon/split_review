# When is Task Vector Provably Effective for Model Editing? A Generalization Analysis of Nonlinear Transformers

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 6, 8, 8

## Abstract
weighted sum of task vectors, each of which is the weight update from the pre-trained model to fine-tuned models for certain tasks. This approach recently gained attention as a computationally efficient inference method for model editing, e.g., multi-task learning, forgetting, and out-of-domain generalization capabilities. However, the theoretical understanding of why task vectors can execute various conceptual operations remains limited, due to the highly non-convexity of training Transformer-based models. To the best of our knowledge, this paper provides the first theoretical characterization of the generalization guarantees of task vector methods on nonlinear Transformers. We consider a conceptual learning setting, where each task is a binary classification problem based on a discriminative pattern. We theoretically prove the effectiveness of task addition in simultaneously learning a set of irrelevant or aligned tasks, as well as the success of task negation in unlearning one task from irrelevant or contradictory tasks. Moreover, we prove the proper selection of linear coefficients for task arithmetic to achieve guaranteed generalization to out-of-domain tasks. All of our theoretical results hold for both dense-weight parameters and their low-rank approximations. Although established in a conceptual setting, our theoretical findings were validated on a practical machine unlearning task using the large language model Phi-1.5 (1.3B).

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper explores the theoretical aspects of task vector arithmetic as a model editing technique for multi-task learning, unlearning, and out-of-domain generalization. The authors provide a theoretical analysis to justify why and when task vector methods are effective in nonlinear Transformer models, especially for binary classification tasks. They prove that task addition facilitates multi-task learning for aligned or irrelevant tasks, while task negation can effectively unlearn contradictory or irrelevant tasks. Additionally, they offer generalization guarantees for out-of-domain tasks and theoretical justification for task vector approximations. These findings are empirically validated through various experiments.

### Strengths
- The paper is very well-written and easy to follow.
- It provides a guideline for when and why task arithmetic works in multi-task learning, machine unlearning, and generalization to new tasks.
- The discussion of low-rank approximations and magnitude-based pruning of task vectors supports the use of efficient approximation techniques in task arithmetic fine-tuning.
- This is the first known theoretical generalization analysis of task vector arithmetic in nonlinear Transformer-based models, filling a notable gap in the literature.
- The theoretical claims are validated through empirical experiments on the Phi-1.5 language model and Colored-MNIST image classification, adding practical credibility to the proposed framework.

### Weaknesses
 - The theoretical analysis relies on a single-head, one-layer Transformer model, which may limit the applicability of the results to more complex multi-layer Transformer architectures.
- While the empirical validation includes a large language model and a basic image classification task, the study could benefit from a broader set of tasks, including more complex or structured tasks beyond binary classification.
- Although the theoretical framework outlines conditions for selecting arithmetic coefficients, more practical guidelines or analyses for tuning these coefficients in real-world applications would be beneficial.

typos:
- line 288, "fine-turning" -> "fine-tuning"
- line 388, "are are" -> "are"

### Questions
I don't have questions.

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
3

### Summary
This work focuses on the task vector in the context of task arithmetic, demonstrating its role in learning and unlearning tasks through experiments. It’s an interesting topic that needs more exploration. The authors find that task correlation affects the performance of the task vector and conduct theoretical justification on the low-rank approximation of the task vector and it's ability to adapt to out-of-domain tasks.

### Strengths
* Very comprehensive mathematical analysis and theoretical proofs
* Discussion on the task vector is extensive.

### Weaknesses
 * There are some issues with the paper's writing (Formula 4 and Definition 2 in the Section 3.2 is confusing).
* In the language generation task, only a model with 1.5B parameters is used, and the experimental results are not fully meet expectations (also a noticeable performance loss in so-called irrelevant task).

* Line 236-238, the conventional attention expression is $softmax(W_QXX^TW_K^T)W_VX$, why is it written as $W_VXsoftmax(X^TW_K^TW_QX)$ in Formula 4?
* Line 236-238, what is the meaning of $X^n$?
* Line 242, Why is $x_i$ used here, while $X$ is used in Formula 4?
* Line 261, Since $\mu_T$ and $v_j$ are orthogonal, what is the meaning of  tokens corresponding to $\mu_T$?
* How to quantify the relevance of different language generation tasks？Are semantically similar and task-related equivalent?

### Questions
* Line 236-238, the conventional attention expression is $softmax(W_QXX^TW_K^T)W_VX$, why is it written as $W_VXsoftmax(X^TW_K^TW_QX)$ in Formula 4?
* Line 236-238, what is the meaning of $X^n$?
* Line 242, Why is $x_i$ used here, while $X$ is used in Formula 4?
* Line 261, Since $\mu_T$ and $v_j$ are orthogonal, what is the meaning of  tokens corresponding to $\mu_T$?
* How to quantify the relevance of different language generation tasks？Are semantically similar and task-related equivalent?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper provides a theoretical analysis of the effectiveness of task vector methods for model editing in transformers. The authors investigate the conditions under which task addition (for multi-task learning) and task negation (for unlearning) are effective, proving that task correlation plays a crucial role. They also establish conditions for successful out-of-domain generalization using task vectors. Experiments with both synthetic and real-world data validate the key concepts of the proposed theory.

### Strengths
- This paper is the first to theoretically examine the generalization of task vectors, filling a significant gap in current research.
- Writing is well-written and easy to follow.
- The theoretical contributions are well-supported by experiments, effectively bridging theory and empirical validation.
- The theoretical insights align well with intuitive expectations regarding the effects of task vectors across aligned, irrelevant, and contradictory tasks.

### Weaknesses
 - Although insightful, the data model may be overly simplistic for capturing the complexities of real-world data. For example, even for simple yes/no questions, a negation word in a sentence may flip the relevance of certain words in the sentence, which cannot be captured by the proposed data model. I wonder if some theoretical aspects can be generalized independently of this data model.
- The analysis is restricted to a one-layer transformer with limited nonlinearity, despite claims in the title and introduction regarding the challenges of analyzing nonlinearity in task vectors.

### Questions
I found this paper highly engaging and believe it would attract even greater interest with an exploration of the theory across a broader set of tasks, particularly generative tasks. For example, could the proposed theoretical framework be extended to multiclass classification as an initial step? A discussion on how these insights might be applied to a wider range of tasks would substantially enhance the paper's appeal. I would be willing to increase my score if the authors could provide even preliminary ideas on these extensions.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper produces the first theoretical result on the ability of task vectors to generalize to new tasks and ability to unlearn a task. The study is conducted under the lens of "aligned" vs "irrelevant" vs "contradictory" tasks. The authors studies the necessary fine-tuning hyperparameters and the task vector coefficients ($alpha$) that enable generalization and unlearning.

Additionally, the authors also verify the theory result with experiments on toy CMNIST dataset and on next token prediction task.

### Strengths
- Very exciting theoretical result that includes very practical aspects (e.g., hyperparameters of the fine-tuning, how to set alpha for each task vectors, etc)
- Novel characterization of generalization conditions on 1 layer transformer, building up on previous work that uses NTK assumptions
- Practical scenarios in terms of the relation between tasks (aligned vs irrelevant vs contradictory)
- Nicely written and relatively accessible to non-theory people. I particularly like the remark after each theorem that explains what the theory is and what does it imply
- Nice setup on CMNIST that reflects the aligned vs. irrelevant vs. contradictory condition, followed by a nice non-toy experiment.

### Weaknesses
N/A -- good paper overall :)

### Questions
Definition 2 -- what is the dimension of $mu_{\tau}$? is it the same as $v$?

### Soundness
4

### Presentation
4

### Contribution
4

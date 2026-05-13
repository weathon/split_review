# Combining Induction and Transduction for Abstract Reasoning

- Decision: Accept
- Scores: 8, 3, 6, 8

## Abstract
When learning an input-output mapping from very few examples, is it better to first infer a latent function that explains the examples, or is it better to directly predict new test outputs, e.g. using a neural network?
We study this question on ARC by training neural models for \emph{induction} (inferring latent functions) and \emph{transduction} (directly predicting the test output for a given test input).
We train 
on synthetically generated variations of Python programs that solve ARC training tasks.
We find inductive and transductive models solve different kinds of test problems, despite having the same training problems and sharing the same neural architecture:
Inductive program synthesis excels at precise computations, and at composing multiple concepts, while transduction succeeds on fuzzier perceptual concepts.
Ensembling them approaches human-level performance on ARC.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper studies the differences between inductive approaches and transductive approaches on ARC tasks.  They generate a synthetic dataset of ARC problems for training.  They demonstrate that induction and transduction solve different problems, and that neither is obviously superior to the other, and rather ensembling both approaches leads to the best performance.  They achieve impressive performance (40%) using LLama 3.1.

### Strengths
* The study of the different types of problems that induction and transduction solve is of great conceptual interest
* The synthetic dataset and it's generation pipeline has value that can be of independent interest
* They achieve compelling performance (40%) with LLama 3.1, matching or beating stronger models GPT-4o, Claude 3.5
* The illustrations are informative

### Weaknesses
 * A more principled understanding of the difference between induction and transduction, or a categorization of the problems they can solve  seems to be missing.  Adding some minimal insight into this could enhance the papers impact.

 * In the authors definition of induction, the distribution over the hypothesis $f$ depends on $x_{test}$, i.e. $f \sim i_{\theta}(x_{train}, y_{train}, x_{test})$.  In pure induction you would believe that the hypothesis only depends on the train set, i.e. $f \sim i_{\theta}(x_{train}, y_{train})$, and only at test time $x_{test}$ is used.  The authors definition seems to blur the line between induction and transduction, as their definition of induction forms the hypothesis based on the train examples and the test example, which clasically would be considered transduction, see e.g. the definition of Vapnik [1].

* How are the grids that are inputs to the ARC problem encoded.  It would be helpful to explicitly reference how in Python code the visual examples are represented, as in my understanding LLama 3.1 is a pure text model (not a multimodal model)

### Questions
* In the authors definition of induction, the distribution over the hypothesis $f$ depends on $x_{test}$, i.e. $f \sim i_{\theta}(x_{train}, y_{train}, x_{test})$.  In pure induction you would believe that the hypothesis only depends on the train set, i.e. $f \sim i_{\theta}(x_{train}, y_{train})$, and only at test time $x_{test}$ is used.  The authors definition seems to blur the line between induction and transduction, as their definition of induction forms the hypothesis based on the train examples and the test example, which clasically would be considered transduction, see e.g. the definition of Vapnik [1].

* How are the grids that are inputs to the ARC problem encoded.  It would be helpful to explicitly reference how in Python code the visual examples are represented, as in my understanding LLama 3.1 is a pure text model (not a multimodal model)

[1] Alex Gammerman, Volodya Vovk, and Vladimir Vapnik. Learning by transduction. preprint arXiv:1301.7375, 2013.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This work validated the Transduction and Induction methods on ARC tasks and found them to be suitable for different tasks. By combining these two, a methodology is proposed to gain performance improvement in ARC.

### Strengths
1. The authors have developed a diverse set of experiments around transduction and induction with respect to the ARC task.  
2. The authors improve the performance on ARC tasks with an ensemble that includes both transduction and induction.

### Weaknesses
1. The overall presentation could be improved. The presentation about the main contributions is confusing. The paper's title combines induction and transduction, but the abstract claims that inductive models and transductive models perform differently. The abstract does not summarize how the authors combine induction and transduction, nor does it provide a specific statement on the differences. 
2. The paper does not provide a theoretical analysis, and the experimental validation is somewhat narrow. Specifically, the authors only conducted verification on the ARC benchmark. Although the authors argue that ARC includes different types of tasks, they are all tasks in a grid-world environment, rather than real-world tasks. This casts doubt on the reliability of the proposed conclusions in the real world. 
3. A more specific discussion is needed for the conclusions obtained from the authors' experimental analyses. it's reasonable that induction and transduction methods are applicable to different problems. But what exactly are the types? Figure 6 provides some examples of ARC problems, which are insufficient to give the reader valid conclusions. What we are more interested in knowing is whether there are some guidelines for determining what tasks are more suitable for induction and what tasks are more suitable for transduction.  
4. The author's statement of combining induction and transduction in the title is not sufficiently elaborated in the manuscript. In Section 5, the author simply states that an ensemble method is proposed, but exactly how the two are combined is important to the current title and should be elaborated. 

Overall, I think this work is more of a technical report around the ARC challenge and doesn't bring significant insights to the community.

### Questions
1. Are there guidelines for determining what tasks are appropriate for induction and what tasks are appropriate for transduction? 
2. How is the ensemble method proposed in Section 5 designed?

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
4

### Summary
The paper expands ARC dataset with LLM generated synthetic data, and investigate induction and transduction approaches on this dataset.

### Strengths
1. The paper contributes a expanded ARC dataset generated by LLM combined with manual efforts. This is valuable to the community.
2. The paper performs a thorough evaluation of induction-based and transduction-based approach.
3. The paper is written clearly and easy to follow.

### Weaknesses
1. As we know LLM often hallucinates. How do the authors quality check the generated dataset?
2. While the authors concluded that induction and transduction approaches are complementary, I hoped to see more in-depth analysis of why induction works better for some while transduction works better for the others.
3. While the authors also discussed the limitation that such method is only tested on ARC, I still think this is a weakness. I wonder the conclusion would be different for some other real-world datasets.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents an interesting approach to combining induction and transduction for solving reasoning tasks. Induction methods predict functions that explain the training data and use them to forecast test inputs, while transduction methods directly predict test outputs based on the training and test inputs. The paper proposes a way to effectively integrate both approaches by utilizing LLMs to generate synthetic datasets, which are then used to train neural networks for induction and transduction, respectively. Experiments conducted on the ARC benchmark demonstrate that induction and transduction complement each other effectively.

### Strengths
Combining induction and transduction to tackle challenging reasoning tasks such as ARC appears to be a novel approach. The successful use of LLMs to generate additional examples for training the proposed model is a noteworthy demonstration. While the idea may seem straightforward, its simplicity allows for broad applicability to other tasks.

The paper is well-written and easy to follow. The technical sections are clearly explained with well-defined formulas, ensuring high-quality presentation throughout.

The discovery that induction and transduction are complementary is particularly intriguing and is likely to spur further research in the field of abstract reasoning.

### Weaknesses
My primary concern is that the intuition behind the proposed ensemble method isn't clearly articulated. It's not immediately evident why the approach outlined in Equations (3)-(5) is expected to be effective. When ensemble, the method starts with induction and then applies transduction if the induction doesn't find a solution—does this suggest that induction takes precedence? For example, does the method presume that any problem should be addressed with induction whenever possible? Offering more insight into the reasoning behind these choices would be beneficial. Please refer to the first question in the subsequent section as well.

While the finding regarding the complementary is interesting, it is not well-investigated why this is happening:
> line 244; most problems solved by induction are not solved by transduction, and vice versa

It would be interesting to explore why this separation occurs. What distinguishes problems suited for induction from those better addressed by transduction? Any insights into these questions would be valuable.

Minors:

As the authors noted in the limitations section, the method has only been demonstrated using the ARC benchmark. Evaluating it against other benchmarks would enhance the robustness of the paper. This raises several questions, such as whether the complementary nature of induction and transduction will apply to other reasoning benchmarks. However, I'd agree with the authors that the ARC is an unsolved, challenging task, and the experiments reasonably underpin the paper's claim.

### Questions
Regarding the ensemble approach:
> line135-136: Transduction and induction can be ensembled by predicting according to induction whenever at least one of the B functions fits ..., and otherwise using transduction ...

Instead of switching sequentially between these two approaches, would it be possible to develop a learning method to blend induction and transduction? A meta-function could predict whether induction or transduction should be applied based on the input. This resulting function may provide insights into what differentiates induction-friendly tasks from transduction-friendly ones.

Please refer to the weakness section for other questions.

### Soundness
3

### Presentation
3

### Contribution
3

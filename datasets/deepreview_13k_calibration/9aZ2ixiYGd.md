# Vision and Language Synergy for Rehearsal Free Continual Learning

- Decision: Accept
- Avg Score: 5.00
- Scores: 8, 6, 3, 3

## Abstract
The prompt-based approach has demonstrated its success for continual learning problems. However, it still suffers from catastrophic forgetting due to inter-task vector similarity and unfitted new components of previously learned tasks. On the other hand, the language-guided approach falls short of its full potential due to minimum utilized knowledge and participation in the prompt tuning process. To correct this problem, we propose a novel prompt-based structure and algorithm that incorporate 4 key concepts (1) language as input for prompt generation (2) task-wise generators (3) limiting matching descriptors search space via soft task-id prediction (4) generated prompt as auxiliary data. Our experimental analysis shows the superiority of our method to existing SOTAs in CIFAR100, ImageNet-R, and CUB datasets with significant margins i.e. up to 30$\%$ final average accuracy, 24$\%$ cumulative average accuracy, 8$\%$ final forgetting measure, and 7$\%$ cumulative forgetting measure. Our historical analysis confirms our method successfully maintains the stability-plasticity trade-off in every task. Our robustness analysis shows the proposed method consistently achieves high performances in various prompt lengths, layer depths, and number of generators per task compared to the SOTAs. We provide a comprehensive theoretical analysis, and complete numerical results in appendix sections. The source code of our method is available in \url{https://anonymous.4open.science/r/xt124j05} for further study and reproducibility.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a new method for prompt based continual learning. Unlike previous methods that focus on task-specific prompts or growing prompt components, this work generates prompts using language descriptions of top-k similar classes from all the previously trained tasks to an input image. The generated prompts are plugged in to the Key and Value pairs of the backbone model for the given input image. In addition, the combined encoded language descriptions of the top-k similar classes are appended to the input image embeddings. Result on CIFAR100, ImageNet-R and CUB datasets with pretrained ViT-B/16 backbone shows significant improvements across accuracy and forgetting metrics over previous works. Extensive ablation study on different components provides better insights on the proposed approach.

### Strengths
•	Introduction is clear in terms of discussing drawbacks of prior works and motivating the proposed approach. Contributions are listed clearly.

•	I appreciate Section 3 and Figure 1 as it gives provides brief recap of the previous SOTA methods and laid some foundation for discussing the proposed method.

•	Leveraging language descriptions and using all language descriptors to find top-k similar classes to generate the prompts is novel in the context of continual learning.

•	The strategy to incorporate inter-class loss helps the method to achieve better results.

•	Comparisons are made against various previous works and significant improvements are shown with their proposed method.

•	Appreciate the detailed ablation study to understand benefits of different components.

### Weaknesses
I don’t find any major weakness but have set of questions (see below) to improve the understanding. However, I find that learning with auxiliary data and inter-task loss are critical components of the method (as shown in ablation study), which are not sufficiently emphasized in the contributions.

1. Between L155-160, under the context of previous task-specific approaches, it is mentioned that two different tasks could produce similar key vectors. It would make a stronger point to justify this statement with some empirical analysis.

2. What is the value of k for top-k descriptors and how many Generators are chosen for each task? Can we chose a single generator for each task? How {E_i}^t of size |C^t|gets chosen for k set of generators?

3. From the Figure 2 or its caption, it is not clear what is the component that is compared against input x to get the cosine similarity. The sentence “search space for top-k” in the figure gives some hint, but the arrows for entire blue block rising the confusion. Please clarify it in the figure or caption.

4. Why it is interesting to solve equation 3, if the task is to search for E_i in all tasks [1, 2, ….t]? Similarly, why consider K^t and why not just use {L_i}^t ?

5. Under the ablation study, what does absence of generator mean? How do you get prompts in this approach without generator?

6. Is the MLP head (classifier) also trained for each task? How can it produce list of softmax values of all classes for equation 7?

7. Please explain why inter-task loss help improve FAA and CAA? What does it tell us about the learned parameters?

8. Has the importance of inter-task loss already explored in previous continual learning papers?

### Questions
1. Between L155-160, under the context of previous task-specific approaches, it is mentioned that two different tasks could produce similar key vectors. It would make a stronger point to justify this statement with some empirical analysis.

2. What is the value of k for top-k descriptors and how many Generators are chosen for each task? Can we chose a single generator for each task? How {E_i}^t of size |C^t|gets chosen for k set of generators?

3. From the Figure 2 or its caption, it is not clear what is the component that is compared against input x to get the cosine similarity. The sentence “search space for top-k” in the figure gives some hint, but the arrows for entire blue block rising the confusion. Please clarify it in the figure or caption.

4. Why it is interesting to solve equation 3, if the task is to search for E_i in all tasks [1, 2, ….t]? Similarly, why consider K^t and why not just use {L_i}^t ?

5. Under the ablation study, what does absence of generator mean? How do you get prompts in this approach without generator?

6. Is the MLP head (classifier) also trained for each task? How can it produce list of softmax values of all classes for equation 7?

7. Please explain why inter-task loss help improve FAA and CAA? What does it tell us about the learned parameters?

8. Has the importance of inter-task loss already explored in previous continual learning papers? 

Minor suggestions:

a. In Figure 1, reposition the labels “fixed”, “trainable”, and “generated” since these labels affect entire Figure, not just the green block.

b. In section 3.b, I suggest to use emphasized text style for “pool-based approach”, “task-specific prompt approach”, and “growing component approach”.

c. In Line 242, correct the typo “tem” -> “them”

d. Line 267 mentions t_hat, but eq. 3 uses notation as t, but not t_hat.

------------------------------------------------------------------------
Final review: I thank authors for their responses. I find that paper proposes a novel method to leverage language descriptors within the context of continual learning. Authors have conducted thorough experimental evaluation and demonstrated notable improvements across multiple datasets. I read the fellow reviewers concerns and I find that authors have sufficiently addressed the major concerns and revised their manuscript accordingly. In particular, regarding the utilization of GPT, authors have justified that their method does not necessarily rely on compute heavy GPTs or LLMs, and can also work without GPT-generated descriptors. Overall, I believe that this paper would be interesting to the research community and suggest towards acceptance.

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
This paper proposes a novel method LEAPGen (Language as Prompt Generator) for continual learning that leverages language knowledge for prompt generation.
LEAPGen uses language descriptors for each class as input for prompt generation, rather than shared embeddings. For each task, LEAPGen employs a fixed number of generator networks, a learnable task-level key, and learnable class-level parameters associated with the descriptor embeddings. To generate a prompt, it first predicts the task ID using a soft prediction mechanism, then selects top-k matching descriptor embeddings based on cosine similarity to the input. Experimental results on datasets like CIFAR100, ImageNet-R, and CUB demonstrate that LEAPGen significantly outperforms existing state-of-the-art methods in terms of accuracy and forgetting measure, addressing key limitations of previous prompt-based continual learning approaches.

### Strengths
- LEAPGen uses language descriptors as input for prompt generation, leveraging richer semantic information compared to previous methods.

- As a prompt-based method, it doesn't require storing and replaying old data.

- By using fixed language descriptors as input, LEAPGen potentially reduces catastrophic forgetting compared to methods that continuously update shared embeddings.

- Experimental results show significant improvements over state-of-the-art methods.

### Weaknesses
 - The paper does not explicitly specify some key details about the pre-trained models used. Which Sentence Transformer does the paper employ? Whether this is a pre-trained language model and if any fine-tuning of these models occurs during the continual learning process.

- The paper does not provide a clear comparison of the increase in parameters due to the addition of generators for new tasks. Based on the paper, the generator is not a lightweight module. As the proposed method requires adding new generators for some new tasks, even if not all tasks, this could lead to a significant growth in the number of parameters as the number of tasks increases. And also an unfair comparison with related works.

### Questions
see above

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a novel approach to address the catastrophic forgetting in continual learning through a prompt-based structure. This method incorporates language inputs for prompt generation and utilizes task-wise generators and soft task-ID prediction. The authors highlight the advantages over existing methods across various datasets, showcasing substantial improvements accuracy while minimizing forgetting metrics.

### Strengths
- The authors systematically review the limitations of existing prompt-based methods, and Figure 1 commendably illustrates the comparison of these methods.

- The proposed method demonstrates performance that far exceeds current methods, which is pleasantly surprising.

- The paper introduces the novel and meaningful use of large language models to generate more refined descriptions.

### Weaknesses
 - The writing of this paper needs significant improvement. Additionally, the structure is overly compact, affecting readability. For instance, the theorem presented in the paper has weak relevance to the proposed method, and I believe it is unnecessary. I suggest moving it to the supplementary materials. Given the complexity and sophistication of the method, I encourage the authors to provide an overview initially.

- The provided ablation study is not sufficiently convincing. I recommend that the authors validate the effectiveness of the proposed modules step-by-step starting from a standard baseline.

- The inclusion of the ChatGPT model raises the question of how to ensure the fairness of experimental comparisons under such settings, and to what extent the performance gains are due to more accurate descriptions.

- Considering the authors (are about to) open-source their code, I suggest making the descriptions obtained via ChatGPT publicly available for deeper analysis. I believe this will enhance the impact of the paper.

### Questions
Please see the comments of weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces a new prompt-based approach for continual learning that take advantage of language guidance. It uses task-wise generators, soft task ID prediction, and generated prompts as auxiliary data. The method outperforms state-of-the-art models on CIFAR100, ImageNetR, and CUB datasets with significant improvements in accuracy and forgetting measures.

### Strengths
1. The paper provides a detailed explanation of current prompt-based continual learning methods and analyzes the weakness associated with these methods, effectively leading to the introduction of the authors' proposed method.
2. The paper presents a novel language-guided continual learning method and thoroughly demonstrates its effectiveness through extensive experiments.

### Weaknesses
1. The comparison mentioned in lines 183-184 between "the photo of car" and "the photo of cat," stating they have 15/16 similarity but 1/16 dissimilarity, is confusing. The authors compared the similarity between these two prompts on a **letter-by-letter** basis and concluded that they are similar. However, the similarity between two prompts should not be evaluated in such a manner. After being processed by the tokenizer, the embeddings of the two prompts are not similar, as their meanings differ significantly.
2. The proposed method relies on using ChatGPT to generate descriptive terms for each class and requires an additional Sentence Transformer to obtain embeddings. The introduction of these extra resources creates an unfair comparison with other methods and limits the practical applicability of the approach in real-world scenarios.
3. Although the proposed method achieves state-of-the-art performance on multiple datasets, the improvement is minor on some, such as the comparison with HiDe-Prompt on the CUB200 dataset. This is particularly relevant given the substantial additional resources, like ChatGPT, required by the method, which other approaches do not utilize. Moreover, this suggests that the performance gains on fine-grained datasets may not be significant, as the generated descriptive terms for each class are quite similar.
4. The authors have used excessive line spacing adjustments, which negatively impact the visual presentation of the paper, such as in lines 437-438 and 446-447. They should revise the layout of the entire paper to provide a better reading experience for the reader.

### Questions
Please the weakness.

### Soundness
3

### Presentation
3

### Contribution
2

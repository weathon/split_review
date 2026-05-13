# Iterative Vectors: Boost In-Context Learning within Activations

- Decision: Reject
- Scores: 6, 5, 6, 5, 8

## Abstract
In-context learning (ICL) has emerged as a standard paradigm for utilizing language models. Although ICL is convenient due to the absence of backpropagation, selecting and processing appropriate demonstration examples can be difficult and time-consuming, particularly when the number of examples is large. We propose to explore the potential of activation space through Iterative Vectors (IVs), a technique designed to enhance in-context performance and necessitating only forward inference passes. IVs are employed by first extracting and iteratively steering activations within a language model, then applying them during inference with minimal computational and memory overhead. We evaluate IVs across numerous tasks using four popular models and observe significant improvements. Our findings suggest that activation steering can serve as a promising direction for in-context learning, thereby opening new avenues for future research.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes an interesting idea for improving the efficiency of in-context learning (ICL). Building on former observations like Function and Task Vectors, this work invented an iterative procedure that mirrors gradient-based training. The authors compare this method with the two predecessors and standard ICL on multiple models and datasets, showing accuracy improvement. They also study the effect of the number of shots and extraction episodes on this method.

### Strengths
* This paper has performed experiments in a principled way, using multiple datasets and base models, and conducted hyperparameter searches for the proposed method and previous method alike.

* This paper is well-written. The motivation and most of the details of the method are well explained.

### Weaknesses
 * I'm unsure how to interpret some experiment results; more details in the questions.

* The functionality of this method (IV) overlaps with PEFT, but it lacks comparison with any of the PEFT methods. Both IV and PEFT take a small number of training examples, spend some amount of upfront computation (training in the case of PEFT, iterative extraction in the case of IV), produce a small number of additional states (parameters in the case of PEFT, V vectors in the case of IV), and use these states to specify a model more effective on a downstream task. PEFT has already been well adopted and understood. So, if we are to prove this new approach is worth exploring, we need to show that it has unique advantages or better outcomes. (e.g., measuring or analyzing the memory requirement could be helpful.)


### Questions
* When we extract the vector iteratively, are the examples encountered in the new iteration the same as the first iteration or resampled every time?

* The FT paper also performed experiments on agnews and sst5, with GPT 1.3B and GPT2.7B, which should be weaker than the models in this paper. But they had sst5 = 39.5, agnews = 65.3 for GPT1.3B, and sst5 = 39.1, agnews = 65.7 for GPT2.7B, significantly higher than the numbers in Table 1. I would guess there are some differences in your experiment setting. I wonder if you could test your method with their setting and report the numbers.

* If we want to test the inference time reduction, why do we need to introduce a brand new dataset? I would guess it will be more informative to use established datasets.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces Iterative Vectors (IVs), a method designed to enhance in-context learning (ICL) within large language models (LLMs) by leveraging activation steering in the activation space rather than in the discrete prompt space. The authors propose extracting activation vectors from the difference in model activations for queries with and without prior context examples, and iteratively reapplying these vectors during inference to improve ICL performance. This approach is evaluated on multiple models and diverse classification tasks, demonstrating performance gains over traditional ICL and other activation vector methods.

### Strengths
1. The concept behind IVs is simple and straightforward, and the approach of leveraging activation vectors in the model’s activation space intuitively makes sense.

### Weaknesses
1. The paper suffers from poor clarity in both writing and figures. For instance, the contributions listed in the Introduction are not clearly differentiated, making it difficult to identify the unique impact of the proposed approach. Additionally, Figure 1 is difficult to interpret and does not clearly explain the IV process. Both the writing and presentation need substantial refinement for the paper to be clear and accessible.
2. The approach is evaluated exclusively on classification tasks, which restricts its generalizability. No experiments are conducted for tasks involving multi-token responses or other types of reasoning, limiting the broader applicability of the findings. The lack of exploration into tasks beyond classification raises concerns about whether the observed performance gains are specific to this task type or if they can be generalized to more complex scenarios.
3. The theoretical section does not provide sufficient insight into why IVs improve ICL performance. Although the paper claims that meta-gradients from in-context examples may not fully capture the task, it lacks an explanation of how IVs solve this limitation. The paper does not delve into the specific mechanisms by which iterative vector application addresses the shortcomings of standard ICL, leaving the reader with an incomplete understanding of the underlying principles.
4. More thorough justification and explanation would be necessary for the approach to be convincing. The paper needs to provide a more rigorous analysis of the method's behavior and its relationship to existing techniques. Without this, the claims of improved performance are not fully substantiated.

### Questions
1. Could the authors add a written-out algorithm to clarify the procedure for extracting and applying IVs? This would improve reproducibility and understanding of the method.
2. In the theory section, what specific mechanisms in IVs address the purported limitations of ICL in the discrete prompt space? A more detailed explanation here would add to the paper’s depth.
3. Given the observed performance drops with a low number of extraction episodes, are there any strategies the authors could suggest to improve stability in such contexts?
4. The paper notes that extraction and inference strength values play a critical role in performance. Could the authors explain the role of each hyperparameter in a clearer manner? Detailed guidance on tuning these values would improve the usability of the proposed method.

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
The authors introduce iterative vectors (IV), a method designed to enhance the in-context learning (ICL) performance of language models during inference. Their main comparison is with the standard ICL approach, where $k$ examples are included in the prompt, leading to increased performance and computation costs as $k$ increases. In contrast, IV captures the meta-gradients made by in-context examples in a condensed format, which can be applied during inference. The computational cost of these updates is incurred mostly during the creation of IV and is amortized over multiple inference rounds. The authors conduct several experiments to showcase the advantages of using IV in various ICL tasks.

### Strengths
1. The framing of iterative vectors as a way to capture the meta-gradients that occur during ICL is well-done and well-motivated (Section 3.1).
2. This paper addresses an important problem: efficiently boosting LM performance without relying on longer prompts.

### Weaknesses
1. Presentation: Section 3.3 is difficult to follow. In particular, lines 298-317 are meant to describe how the iterative component of IV works, but I could not understand it even after multiple readings. As currently written, this section heavily relies on formulas to communicate how IV works. There is nothing necessarily wrong with including the formulas, but the surrounding text lacks clarity. Consider adding a new figure, pseudocode, or examples. The description of the iterative update lacks a clear explanation of how the gradients are accumulated and applied across iterations. It's unclear how the model's internal state is modified by the iterative process, and how this differs from a standard gradient update. The text does not adequately explain how the iterative process converges or what criteria are used to determine the number of iterations.
2. Missing experiment: Line 36 states, “This finding is also corroborated by our experiments, wherein adding more in-context examples does not always result in improvements. Instead, it introduces uncertainty, which compromises LMs’ reliability and usability. I could be mistaken, but do not see any experiments that support this claim. While the authors allude to this phenomenon, they do not provide a clear demonstration of how increasing the number of in-context examples leads to a decrease in performance in any of the datasets used in the paper. The claim is not supported by the experiments presented.
3. Missing zero-shot experiments: Given the framing in Section 3.1, it seems natural to include zero-shot experiments. I recommend that the authors either include them or provide an explanation in the paper justifying why these experiments were left out. The authors allude to a reason in line 482, but I did not find it compelling. The motivation for iterative vectors is framed around capturing meta-gradients from in-context examples, which should also be applicable to zero-shot settings. The absence of zero-shot experiments raises questions about the generality of the proposed method.

### Questions
1. Please clarify how the iterative component of IV works.
2. Which experiment supports the claim in line 36?
3. Where is C in formula 17 defined?
4. Please clarify why only the one-shot setting was considered for Table 1. I do not follow the reasoning in lines 350-351.
5. How are iterative vectors different from task and function vectors? A short section comparing their differences will help me better understand the the technical novelty of iterative vectors.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces Iterative Vectors (IVs) for enhancing in-context learning (ICL) by exploring the potential of activation space without the need of backpropagating and with minimal computation overhead.

IVs are generated by extracting the difference of attention activations from queries with and without preceding examples during the inference process, with the goal of capturing the insights the model learns from the input examples. These IVs are then iteratively reintroduced into the model, facilitating the formation of more stable and effective vectors while continuously incorporating information from subsequent examples.

The authors evaluate IVs across three models and different classification tasks, reporting improvements over previous  vector-based ICL methods Function Vectors and Task Vectors. They also demonstrate how IVs reduce inference time and scale with the number of demonstrations and extraction episodes. An ablation study is provided to examine the impact of hyperparameters on ICL stability and performance.

### Strengths
This work has several notable strengths regarding its topic and results:
- S1 -  The paper addresses an interesting topic of in-context learning (ICL), where authors are specifically focusing on task vectors that enable fast and robust ICL performance. The method Iterative Vectors (IV) contributes to the ongoing research in this direction by further supporting the use of task vectors instead of standard ICL.
- S2 - The authors demonstrate that their method, Iterative Vectors (IV), achieves strong performance over 3 different models and 13 tasks, outperforming previous vector-related approaches without requiring additional memory or backpropagation.

### Weaknesses
 The paper has several areas that could benefit from improvement in terms of clarity, novelty, evaluation, and formatting:
- **W1** - The introduction lacks a complete motivation for the use of task vectors, making it challenging to understand their necessity in in-context learning. 
The writing appears unpolished and the paper should be improved structural-wise. For example, Section 3 discusses the theory of transformers as meta-optimizers, but its connection to the main contributions and approach of IVs is unclear. I would suggest either integrating this better with more related works on this topic, or focusing more directly on the proposed method. 
Next, the paper lacks clarity in some parts. For example, the method description could be clearer, especially regarding the hyperparameters, which are mentioned, but not explained properly. Figure 2 also seems to be redundant. 
Moreover, there are formatting issues, such as excessive empty space around Figure 3 and within the related work section.  Reformatting the text and refining the introduction would improve the overall presentation and clarity.
- **W2** - The related work section misses important studies on in-context learning, including research on demonstration sensitivity, brittleness, and pretraining dynamics [1, 2, 3] - areas relevant to task vectors. Additionally, it does not reference recent work on task vectors in visual models [4], multi-modal models [5], and VQA [6]. Including these would provide a more comprehensive overview of the field and the paper would be more complete.
- **W3** - Figure 3 is difficult to interpret due to small font sizes and a lot of details and information. I suggest the authors simplify this figure or move it to the appendix while summarizing key findings in the main text to enhance comprehension and clarity.
- **W4** - The proposed method appears to be an extension of existing task-vector based approaches, with slight modifications such as aggregation and different prompt designs applied to new tasks. Further, the method relies on several hyperparameters that require tuning, which might not be practical in few-shot in-context learning situations where minimal parameter adjustment is preferred. Have the authors conducted some additional analysis of the feature space or the underlying mechanisms that could strengthen the paper’s contributions? 
- **W5** - The experiments are limited to classification tasks and do not extend to more complex tasks that reflect real-world scenarios or involve multi-modal models. Moreover, the paper does not include evaluations on newer large language models like Llama 3. Have the authors tested different model sizes? If so, how much does the performance differ in such scenarios? 
- **W6** - The finding that performance improves with more iterations and demonstrations is somewhat expected in small-data scenarios and few-shot learning. Prior research on multi-modal [5] and visual task vectors [4] has reported similar results. Have the authors conducted more analysis in this direction that can bring new insights for this direction? 

### Questions
While the paper introduces an interesting approach with Iterative Vectors (IVs) that shows performance improvements over existing methods for vector-based in-context learning methods, there are several areas that require improvement. Strengthening the motivation, refining the method description, expanding the related work to include recent studies, and providing more comprehensive evaluations on a variety of tasks and models would significantly improve the paper. With these revisions, the work could become a strong contribution to the community. 

My further questions to the authors are:
- Could you evaluate your method on more challenging tasks that are closer to real-world applications to demonstrate its broader applicability?
- Could you evaluate your method on multi-modal models?
- How does your method perform on newer language models, and is there a significant difference in performance between smaller and larger models?
- Have you analyzed what more iterations and demonstration do to the feature space of the task vectors? 
- Have you observed compositionality with Iterative Task Vectors?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper discusses the use of Iterative Vectors (IVs) to enhance In-Context Learning (ICL) in language models. IVs are shown to improve performance in various tasks, particularly in few-shot learning scenarios. The paper compares IVs with other vector methods (TV, FV) and demonstrates its effectiveness in reducing inference time and scaling with the number of demonstration shots. The results suggest that IVs offer advantages in improving model performance and can potentially be applied to more advanced applications.

### Strengths
The paper shows rigorous process of the research methodology, experimental design, and result analysis. The study rigorously evaluates IVs across multiple models and diverse tasks, providing a comprehensive assessment of their performance.

The clarity of the paper is evident in the detailed explanation of IV generation, their iterative reintroduction into the model, and their impact on ICL performance. The use of clear and concise language, along with illustrative examples, enhances the readability and understanding of the paper. Additionally, the comparison with other methods and the discussion of practical applicability contribute to the overall clarity of the research.

By demonstrating the effectiveness of IVs in improving ICL performance, the paper addresses a critical aspect of language models related to few-shot learning and adaptation to real-world datasets. The practical implications of IVs in enhancing model performance, reducing inference time, and scaling with the number of demonstration shots underscore their significance in real-world applications.

### Weaknesses
Clarity could be improved in certain figures and tables.

Table 1: Include brief reminders of the terms FV and TV directly within the table, as they are first defined in Section 2.1, which is distant from their use here. Providing concise definitions and a comparison with IV will improve comprehension.

Figure 3: To improve readability, round the score to one decimal place, which should make the figure appear less dense and easier for readers to interpret at a glance.

Table 4: Converting the results to a plot could visually emphasize the effectiveness of IVs in extracting and utilizing a greater number of examples. This format may better showcase the comparative strengths of IVs.

To make the experiment more comprehensive, consider expanding the experiment in Inference Time Experiment to evaluate FV and TV on the emoji dataset. Assessing their respective performance and inference times would offer a clearer picture of each method's efficiency in various contexts.

### Questions
Could you provide further details on the emoji dataset? Additional examples and explanations might help clarify its structure and significance.

The paper primarily evaluates models with relatively small parameters (6B, 7B, and 13B). Would extending experiments to include larger models, such as 70B, offer additional insights or strengthen the findings?

### Soundness
4

### Presentation
3

### Contribution
4

# A Closer Look at Machine Unlearning for Large Language Models

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Large language models (LLMs) may memorize sensitive or copyrighted content, raising privacy and legal concerns. Due to the high cost of retraining from scratch, researchers attempt to employ machine unlearning to remove specific content from LLMs while preserving the overall performance. In this paper, we discuss several issues in machine unlearning for LLMs and provide our insights on possible approaches. To address the issue of inadequate evaluation of model outputs after unlearning, we introduce three additional metrics to evaluate token diversity, sentence semantics, and factual correctness. We then categorize unlearning methods into untargeted and targeted, and discuss their issues respectively. Specifically, the behavior that untargeted unlearning attempts to approximate is unpredictable and may involve hallucinations, and existing regularization is insufficient for targeted unlearning. To alleviate these issues, we propose using the objective of maximizing entropy (ME) for untargeted unlearning and incorporate answer preservation (AP) loss as regularization for targeted unlearning. Experimental results across three scenarios, i.e., fictitious unlearning, continual unlearning, and real-world unlearning, demonstrate the effectiveness of our approaches.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the machine unlearning problem in LLMs. It critiques the inadequate evaluation of model outputs in current benchmarks and introduces three additional metrics: token diversity, sentence semantics, and factual correctness. The paper then categorizes existing unlearning methods into untargeted and targeted approaches, proposing new objectives for each that outperform existing methods on the proposed new metrics. Experimental results across various unlearning scenarios demonstrate the effectiveness of the proposed methods.

### Strengths
The paper identifies limitations in current evaluation methods for machine unlearning in LLMs and introduces three new metrics (token diversity, sentence semantics, and factual correctness), providing a more comprehensive evaluation framework. These metrics may improve the reliability of evaluations, addressing a gap in the field. The paper then proposes new unlearning objectives—entropy maximization for untargeted unlearning and answer preservation loss for targeted unlearning—that consistently outperform existing unlearning objectives across different unlearning scenarios.

### Weaknesses
My main concern lies in the newly introduced evaluation metrics. While I agree that current metrics, such as ROUGE and probability, are insufficient, the new metrics proposed in this paper don’t seem good either. Based on the descriptions provided, it appears the authors aim to assess output quality across these aspects:
1. Validity/Fluency (via token diversity): evaluates whether the response is readable by humans (not necessary for the forget set in untargeted unlearning).
2. Correctness (via cosine similarity): assesses whether the new answer aligns with the original.
3. Hallucinations (via entailment score): checks if the new answer introduces any additional, potentially hallucinated information.

My questions on the metrics are as follows:

1. The paper doesn’t present a thorough discussion of the limitations of current metrics. While the authors provide case studies, a more comprehensive analysis is needed to clarify why these new metrics are essential.
2. It’s unclear if existing metrics sufficiently address these aspects. For instance, I am particularly concerned about the token diversity metric, which aims to measure fluency—already somewhat captured by the probability metric. Additionally, in the appendix, there appears to be a strong correlation between the evaluation results of these two.
3. I don't think cosine similarity is a good measure. For factual knowledge, accuracy is more binary—either the information is correct or it isn’t—making similarity scores potentially meaningless. I would recommend considering knowledge extraction-based metrics, which are widely used for hallucination detection and might provide a more direct measure for this aspect.

Typos:
line 457: unleanred -> unlearned

### Questions
See weaknesses.

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
The paper evaluates existing machine unlearning (MUL) methods. It classifies methods into targeted and untargeted methods and examines the existing evaluation metrics for MUL. To overcome of limitations of existing metrics, authors propose three new metrics: Token Entropy, Cosine Similarity, and Entailment Score. Finally, to overcome limitations of existing MUL methods, authors propose entropy based method for untargeted unlearning and regularization based method for targeted unlearning. Authors perform extensive experimentation on variety of synthetic and real-world datasets.

### Strengths
1. The paper performs good analysis of existing unlearning methods and evaluation metrics and proposes solutions for overcoming the existing methods.
2. The paper performs extensive experimentation on a variety of datasets including synthetic and real world datasets.

### Weaknesses
Some other metrics have also been proposed for MUL , e.g., Membership Inference Attack (MIA), authors should also include those in the evaluation.

Not necessarily a weakness but there are many typos in the paper that authors should fix, e.g., line 280 (practical -> practice), line 284 (minimizing -> minimize)

### Questions
In line 39, authors say "fine-tuning the target LLM on a specified set, known as forget set..." but shouldn't the fine-tuning be done on "retain set" since forget set is what the model wants to forget?

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
3

### Summary
This paper addresses the limitations of current machine unlearning methods, initially proposing three new evaluation metrics—token diversity, sentence semantics, and factual correctness—to better assess model outputs. Token diversity penalizes repetition in the model’s output, sentence semantics penalizes the addition of unnecessary information during testing on the retain set due to unlearning, and factual correctness measures the semantic relationship with the ground truth using textual entailment, aiming for high scores on the retain set and low scores on the forget set. The paper further proposes a new machine unlearning approach. For untargeted unlearning, the maximum entropy loss aligns the unlearned model’s behavior with that of a randomly initialized model. For targeted unlearning, the Answer Preservation loss is introduced to reduce the probability of generating rejection templates on the retain set while maintaining the probability of original answers.

### Strengths
1. The structure of the paper is well-organized, explanations are clear, making it very readable overall.
2. Evaluation is conducted on three different scenarios (fictitious unlearning, continual unlearning, and real-world unlearning), with significant performance improvements of the proposed method observed in all tasks. The improvements in real-world scenarios especially indicate its usefulness.
3. The paper discusses the motivation for the proposed method in detail (Sections 3.1 and 4.1), which strengthens the persuasiveness of the proposed approach.
4. The proposed methods (the maximum entropy loss and the answer preservation loss) are both simple and easy to implement yet proven effective in many scenarios.

### Weaknesses
1. The proposed methods (3.2 and 4.1) are not consistent to each other. While Section 3.2 describes an untargeted unlearning approach, it seems fundamentally similar to a targeted unlearning problem using a random word sequence as a ground-truth response in $\mathcal{D}_\mathrm{IDK}$. If so, it should inherit the same issues discussed in Section 4.1, but this is not discussed.
2. Although new evaluation metrics are introduced, the results are not analyzed deeply with these new metrics. Instead, overall metrics such as Model Utility and Forget Efficacy are primarily used. More discussions on the strengths and weaknesses of the existing and proposed methods using the proposed three individual metrics could add value to the paper.
3. Typos
    - Line 280: “In practical” => “In practice”
    - Line 284: “we minimizing” => “we minimize”

### Questions
1. Line 163: “We calculate all metrics except TE on the forget set, as TE does not involve any ground truths.” Could you elaborate on why TE should be removed?
2. Regarding Weakness 1, is it possible to combine the methods in Section 3.2 and Section 4.2?
3. Regarding Weakness 2, would such analysis and discussion be a reasonable addition to this paper?

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
The paper focuses on LLM unlearning, which aims to remove specific content—especially sensitive or copyrighted information—without necessitating complete retraining. The authors propose three additional metrics to improve the evaluation of unlearning performance: token diversity, sentence semantics, and factual correctness. They categorize unlearning methods into untargeted and targeted approaches, analyzing their limitations. For untargeted unlearning, they introduce a method based on maximizing entropy to avoid hallucinations, while for targeted unlearning, they propose an answer preservation (AP) loss to prevent excessive ignorance. Experimental evaluations demonstrate the effectiveness of these methods across different unlearning scenarios, including fictitious, continual, and real-world contexts.

### Strengths
The paper provides some new insights about LLM unlearning. The contributions include defining new evaluation metrics and proposing novel methods for both untargeted and targeted unlearning approaches. 
The authors also provide some insightful analysis about the limitation of the existing regularization methods.

### Weaknesses
In Section 2, the authors propose several new evaluation metrics and use aggregated metrics combining both the old and new metrics for most experiments in the evaluation section. While the proposed methods show advantageous performance with these aggregated metrics, it remains unclear how they perform under the existing metrics alone. Even if the authors view the existing metrics as insufficient, the new methods should still demonstrate comparable or advantageous performance when evaluated solely with them. Therefore, I believe additional experimental results and clarification are needed.

### Questions
Please check my question in the weakness part.

### Soundness
3

### Presentation
2

### Contribution
2

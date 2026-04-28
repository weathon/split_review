# CAD-Editor: Text-based CAD Editing through Adapting Large Language Models with Synthetic Data

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 5, 6

## Abstract
Computer Aided Design (CAD) is indispensable across various industries. 
\emph{Text-based CAD editing}, which automatically modifies CAD models following textual instructions, is important yet not extensively studied. 
Existing work explores design variation generation, which randomly alters specific parts of a CAD model, offering no control over the final appearance.
This work introduces \emph{CAD-Editor} for text-based editing.
We leverage Large Language Models (LLMs) as the backbone to take the concatenation of textual instruction and original CAD sequence as input and predict the edited CAD sequence, where the sequence representation of a CAD model is designed for easier processing by LLMs.
Moreover, we propose fine-tuning LLMs by using a synthetic dataset followed by a selective dataset.
The synthetic data is produced by leveraging powerful existing models, including design variation generation models for producing paired CAD models and multi-modal models for capturing textual differences between these pairs.
The selective data is created by choosing top examples from outputs of the initially fine-tuned LLMs based on human feedback or metrics.
In this way, a large-scale synthetic dataset offers basic capability while a selective dataset that is less noisy and better aligned with human intentions boosts performance further.
Extensive experiments demonstrate the advantage of CAD-Editor both quantitatively and qualitatively.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces CAD-Editor, a novel approach for text-based CAD editing that leverages LLMs to interpret and apply textual instructions to CAD models. CAD-Editor is designed as a sequence-to-sequence generation model, enabling users to edit CAD models via natural language inputs. The paper outlines a method involving two phases of fine-tuning on synthetic and selective datasets to optimize performance. Experimental results demonstrate CAD-Editor’s improvements in accuracy, alignment with textual instructions, and CAD model validity over other models, including SkexGen and Hnc-CAD. This work also establishes a benchmark for text-based CAD editing.

### Strengths
- The paper is well-written and it's easy to follow. 
- As the authors have also mentioned, CAD generation and editing has gotten relatively little research attention although they play a huge role in different industries.

### Weaknesses
 - I believe this paper is a better fit for a computer vision conference for being more of an applied paper investigating CAD editing. 
- I think the authors should provide a couple of examples of D-CLIP scores and their corresponding text/image pairs to show the effectiveness of their proposed metric.



### Questions
- In line 69, what do the authors mean by "without control over the final appearance"? Aren't they text to CAD models? 
- In line 259, how do you automatically exclude instructions with more than three edits? 
- Have you tried fine-tuning any of the baseline text-to-cad models instead of LLama3-8b-instruct?

### Soundness
2

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
4

### Summary
The paper introduces CAD-Editor, a text-driven CAD editing method based on large language models (LLMs). To generate high-quality training data, the article adopts a two-stage training strategy. The first stage generates a large-scale synthetic dataset, and the second stage constructs a selective dataset. Experimental results show that CAD-Editor outperforms other methods on multiple evaluation metrics, including GPT-4o.

### Strengths
- Innovatively transforms CAD editing tasks into sequence-to-sequence problems, leveraging large language models (LLMs) to achieve text-driven CAD model editing.
- Adopts a multi-stage training strategy, significantly improving model performance by combining synthetic datasets and selective datasets.

### Weaknesses
 - I am deeply concerned about the generalization ability of CAD-Editor. On one hand, the choice of the base dataset is crucial for the model's generalization ability, and CAD-Editor is only optimized on the DeepCAD dataset. On the other hand, the generation of the synthetic dataset relies on existing CAD generation models (such as SkexGen and Hnc-CAD), both of which are also trained on DeepCAD. Therefore, the performance of CAD-Editor on the DeepCAD benchmark raises suspicions of overfitting. That is, if the fine-tuning dataset mainly contains CAD models from a specific industry (such as the automotive industry), the trained model may not handle CAD models from other industries (such as aerospace or construction) well.
- The reliance on GPT-4o. The proposed method requires multiple prompts to GPT-4o to obtain generated data. The article does not discuss the token cost of GPT-4o and potential performance bottlenecks. Furthermore, the quality of the generated training data is highly dependent on the ability of GPT-4o to accurately capture the nuances of CAD operations and transformations, which could introduce biases or inaccuracies into the training process if not carefully validated.

### Questions
- The article mainly focuses on models with 8B parameters, and based on the qualitative analysis results provided, there is still a significant gap between the current model's effectiveness and being able to provide productivity. I am curious whether CAD-Editor can be more effective when scaled to larger models or more diverse datasets.
- How does CAD-Editor perform when dealing with vague or ambiguous text instructions? Does the model have the ability to identify and correct erroneous editing instructions?

### Soundness
3

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
3

### Summary
The paper proposes a CAD editing dataset. The CAD models are collected and fed into design variation generation models to create design variations. A large language model (LLM) is used to generate multi-level captions, which are then compressed into sentences with a maximum of 10 words. To enhance model performance, the paper suggests filtering some synthetic data using D-CLIP or human evaluation. The model is fine-tuned on LLAMA 3 and achieves the best performance compared to other methods.

### Strengths
The paper proposes an interesting dataset focused on instruction-based CAD editing, a task that holds significant value for industrial applications.

The paper is well-written and easy to follow.

It introduces an innovative model-based data selection method that enhances the quality of the dataset.

### Weaknesses
I am curious about the D-CLIP evaluation. It is unclear whether the adapted D-CLIP model was pretrained on any specific datasets. Was it fine-tuned on the proposed dataset? If not, is there a potential domain gap between the proposed dataset and the datasets used to train D-CLIP? This domain gap could potentially influence the effectiveness of the data selection process. Specifically, if the proposed dataset is also used to train D-CLIP, how can we ensure that D-CLIP is good enough to evaluate the CAD data? There is a concern about the risk of overfitting. If D-CLIP and the LLM model share the same training set, D-CLIP may learn dataset-specific characteristics too finely. This could result in evaluation outcomes that do not generalize well to other data, potentially compromising the reliability and objectivity of the results and also influence the data selection process.

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
3

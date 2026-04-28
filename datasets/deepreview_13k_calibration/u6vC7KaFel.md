# Instant Transformer Adaption via HyperLoRA

- Decision: Reject
- Avg Score: 4.75
- Scores: 6, 5, 5, 3

## Abstract
While Foundation Models provide a general tool for rapid content creation, they regularly require task-specific adaptation. Traditionally, this exercise involves careful curation of datasets and repeated fine-tuning of the underlying model. Fine-tuning techniques enable practitioners to adapt foundation models for many new applications but require expensive and lengthy training while being notably sensitive to hyper-parameter choices. To overcome these limitations, we introduce HyperLoRA, a model capable of adapting Large Language Models on the fly---solely based on a natural language description of the target task.  HyperLoRA is a hypernetwork trained to construct LoRAs in a single inexpensive forward pass. After training HyperLoRA on a suite of 9 pre-trained LoRA adapters (GSM8K, Arc, etc.), we show that the ad-hoc reconstructed LoRA instances match the performance of task-specific adapters across the corresponding test sets.
Furthermore, HyperLoRA can compress hundreds of LoRA instances and zero-shot generalize to entirely unseen tasks. This approach provides a significant step towards democratizing the specialization of foundation models and enables language-based adaptation with minimal compute requirements. Our code and pre-trained checkpoints will be available through https://github.com/AnonymousAuthor/hyperlora and https://huggingface.co/ upon publication.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
## Overview
The paper introduces HyperLoRA, which is a method involving training LLMs to adapt to new domains and tasks on-the-fly, without having to do expensive training at test-time. This is achieved through the use of a hypernetwork of LoRA adapters. During test-time, the natural language instruction is encoded and a LoRA adapter is zero-shot generated after a single forward pass.

The main hypothesis is that different LoRA adapters share similar underlying mechanisms and hence can be optimized simultaneously.

## Method + Experiments
- Three different variants (small, medium, large) with various output heads and learnable embeddings
- Can be trained either using LoRA reconstruction (shown to be poor at generalization) or through SFT
- 500 tasks. 11 held out for evaluation.
- Evaluate on 10 widely used tasks like ARC, HellaSwag, GSM8k, etc.
- Outperforms LoRA routing baseline

### Strengths
**1. Flexibility and efficiency with minimal overhead** -- The main strength of the method is that it allows for good generalization to new tasks without adding much extra in terms of training. It is also very flexible because it can adapt to unseen prompts during test time. This can help make LLMs a lot more accessible and easier to interact with.

**2. Strong results with a relatively simple method** -- The method generalizes well, even to zero-shot settings as seen in Table 2. Meanwhile, in Table 1, we see that In most cases, the model performs almost as well as, if not better, than the task-specific LoRA fine-tuning.

**3. Thorough ablations and analysis** -- The whole section 5 (ablations) and section 6 (analysis) go pretty in-depth into the models and what makes them work. For instance, the paper explores varying task embedding models, task descriptions, etc.  

**4. Clean presentation** -- The paper uses color and space very effectively, which makes reading quite pleasant.

### Weaknesses
 **1. Possible scaling concerns** -- I find it a bit concerning that adding more training tasks doesn't improve the performance (Table 3). Usually for most algorithms, adding more data would result in a better model. Otherwise, the concern is that the performance of the method will be capped at a certain level and it will be hard to increase further. Also, in the paper, the model was evaluated on 11 different tasks (which are somewhat close to each other). I am wondering how the model would scale to even more tasks beyond the basic ones.

**2. Comparison with full fine-tuning** -- The study is limited to the LoRA setting, which has been shown to perform worse than full fine-tuning, and this method likely wouldn't generalize to full fine-tuning settings. Similar to the above point, this makes me slightly concerned that the method might have its performance capped at a certain level.

### Questions
- The paper claims to introduce HyperLoRA but one of the papers cited in the paper (Xiao et al https://aclanthology.org/2023.emnlp-main.487.pdf) also calls their method HyperLoRA? Not sure how to reconcile this naming overlap.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes HyperLoRA, which is a method to generate a new low-rank adaptor(LoRA) based on the natural language task description without training an adaptor. Through experiments, the paper shows HyperLoRA successfully generate an adaptor for new task by achieving comparable or even higher performance than trained adaptor.

### Strengths
- Generating a new adaptor without tuning one can be utilized widely as it can minimize expensive tuning step.
- It is impressive that generating parameters itself rather than text or other data can show promising results

### Weaknesses
 - The presentation of the paper lacks intuitiveness.
    - There are many typos and grammatical errors.
    - The figures are not clear.
        - For example, figure 1. left does not denote what the each arrow represents, and the figure looks like the HyperLoRA is optimizing both reconstruction loss and SFT loss at the same time, but it seems like the HyperLoRA optimize either one of the losses according to the paper
        - Also I was not able to find a part that shows the number of tasks in figure 3
    - Preliminary explanations for the many parts are not enough
        - For example, it does not explain what the prediction offset is.

### Questions
- What is the prediction offset?
- Is it possible to optimize both reconstruction loss and SFT loss at the same time?
- Does HyperLoRA work better than given task description as a prompt?

### Soundness
2

### Presentation
1

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
The paper focuses on the problem of reusing knowledge from pretrained parameter-efficient adapters to new tasks without target task specific fine-tuning.

In particular, the authors propose to leverage the hypernetwork as a means to generate such LoRA adapters by using two kinds of training signals, task-specific training loss and task-dependent LoRA weight reconstruction loss.
Specifically, the hypernetwork generates three variants of LoRA matrices by using information of the target task (one-hot or natural language embeddings) and target module to be adapted (depth and FFN vs MHA). Compared with the backbone LM, the hypernetwork is parameter-efficient too.

The authors then apply the proposed method on top of a pretrained language model (Mistral-7B-instruct) with several representative English natural language understanding tasks.
Compared with LoRA baselines and recent work on combining LoRA weights for unseen tasks, the proposed method HyperLoRA shows promising improvements.

### Strengths
The paper studies a practically interesting problem, i.e., adapting LLMs on the fly based on the natural language descriptions. 

The proposed HyperLora architectures are well designed.

Experiments show positive results of the proposed approach.

### Weaknesses
The experiments only use one base model (i.e., Mistral-7B-Instruct). It is unclear whether the approach can generalize to other model families (e.g., Llama, Phi) and other model sizes. It would be also interesting to see if the HyperLora can benefit from learning to generate LoRA adapters for different model families.

It would be useful to add few-shot and many-shot in-context-learning results as baselines as well. And also compare the cost between such in-context-learning and the proposed HyperLoRA.

The need of using a multi-task LoRA as a prediction offset to boost the performance is a little undesired, as it requires extra cost for training a multi-task LoRA in the first place.

Minor:
Line 225: it would be useful to describe the prediction offset clearly in the main body of the paper, or at least refer to the Eq 6 & 7 in the appendix.

### Questions
1) How stable is training process of the proposed method? e.g., different AB configs, different batch sizes are required for different configs. 

2) Is there any benefits of combining the SFT loss and the reconstruction loss? 

3) What is included in the task descripton? Just the high-level task description? What about adding a few examples of the tasks?

### Soundness
3

### Presentation
3

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
This work proposes using hypernetworks to generate LoRA weights for unseen tasks based on natural language instructions. It does so by embedding the instructions using an existing embedding model (or activations from an LLM) and generates the LoRA weights using a newly trained neural network. The authors show that this approach to generate LoRA weights can extend to tasks not seen in the training set.

### Strengths
- The authors provide clear evaluation of their proposed method.
- The authors conduct informative analysis on different configurations for training the hypernetwork, showing the impact of varying the number of tasks and embedding method.

### Weaknesses
 - The authors omit key prior work [e.g. 1,2,3] in their related work. For instance, [1] similarly uses SNI and trains a hypernetwork to generate LoRAs, with both few-shot as well as instruction-only configurations. [3] Likewise also uses both SNI (formerly NIv2) and an instruction-only setting.
- Correspondingly, the authors largely fail to compare their currently method to existing hypernetwork methods (both the ones omitted above, as well as the ones they cite in their work). The primary other method they compare to is Arrow Routing, which seems largely unrelated to the setting besides the connection of (directly rather than indirectly) relying on a set of pretrained LoRAs.
- The results are directionally good but many of the evaluated tasks already look saturated. There are also some oddities such as LoRA on PiQA underperforming the base model, which seems to suggest an inadequate configuration for their baseline.
- Parts of the writing are unclear, e.g. the distinction between the "Task Description Embeddings" setting and the unseen task descriptions used for "Zero-Shot LoRA Generation". (My understanding is that all task descriptions on evaluated tasks should be unseen?) There is also reference to both Train and Eval descriptions referenced in Table 5, which makes it further unclear what tasks/descriptions are actually unseen during training.
- There is some unconvincing post-hoc justification for empirical results. For instance "This result is in line with the general knowledge that certain inductive biases improve models' robustness and generalization" is used to explain why the middle M configuration outperform S and L reads to me like trying to force a scientific interpretation to an unexplained (which is okay) quirk in empirical result.

### Questions
- See above: what is the distinction between seen and unseen task descriptions?
- How are the one-hot embeddings generated?

### Soundness
3

### Presentation
2

### Contribution
2

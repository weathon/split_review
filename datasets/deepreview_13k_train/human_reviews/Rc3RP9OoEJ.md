# In-context Prompt Learning for Test-time Vision Recognition with Frozen Vision-Language Model

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
Current pre-trained vision-language models, such as CLIP, have demonstrated remarkable zero-shot generalization capabilities across various downstream tasks. However, their performance significantly degrades when test inputs exhibit different distributions. In this paper, we explore the concept of test-time prompt tuning (TTPT), which facilitates the adaptation of the CLIP model to novel downstream tasks through a one-step unsupervised optimization that involves only test samples. Inspired by in-context learning in natural language processing (NLP), we propose \textbf{In}-\textbf{C}ontext \textbf{P}rompt \textbf{L}earning (InCPL) for test-time visual recognition tasks, 
which empowers a pre-trained vision-language model with labeled examples as context information on downstream task. Specifically, InCPL associates a new test sample with very few labeled examples (sometimes just one) as context information, enabling reliable label estimation for the test sample and facilitating model adaptation. To achieve this, InCPL employs an efficient language-to-vision translator to explore the textual prior information for visual prompt learning.
Further, we introduce a context-aware unsupervised loss to optimize visual prompts tailored to test samples. Finally, we design a cyclic learning strategy for visual 
and textual prompts to ensure mutual synergy across different modalities. This enables a pre-trained, frozen CLIP model to adapt to any task using its learned adaptive prompt. Our method demonstrates superior performance and achieves state-of-the-art results across various downstream datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a method called "visual In-Context Prompt learning (InCP)" to enhance the CLIP model's performance in various downstream tasks. InCP enables a pre-trained vision-language model to adapt to new tasks by leveraging in-context examples without changing its core parameters. The key contributions of the paper include the introduction of InCP as an effective method for incorporating in-context information, exploration of language descriptions for visual prompt initialization, and achieving state-of-the-art results across diverse downstream datasets.

### Strengths
+ The paper presents a new method by combining natural language processing and computer vision insights.
+ The paper maintains high quality through a well-structured methodology and rigorous experiments, ensuring robustness and reliability in its findings.
+ The paper is exceptionally clear, providing a strong background and conveying complex concepts effectively, making it accessible to a wide audience.

### Weaknesses
 - Efficiency is a crucial factor in test-time adaptation, given the significance of swiftly adapting to new environments. It is imperative that the paper includes explicit reporting and a comparative analysis of inference time metrics for InCP, especially when compared to existing methods like TPT.
- This paper requires clarification regarding InCP's performance on the SUN397 dataset (utilized in TPT) in Table 1 and the ImageNet dataset (also used in TPT) in Table 2. Providing a comprehensive comparison of InCP's performance on these specific datasets will significantly enhance the paper's clarity and the reader's understanding.
- The performance improvement in Table 2 appears to be marginal. Further explanation or additional results may be needed to demonstrate the significance of the improvement.

### Questions
Please refer to the weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes a prompt learning method for vision-language models. It proposed to optimize both textual and visual prompts jointly (via cyclic learning) using an unsupervised objective on the test sample along with a supervised objective on some few-shot (in-context) examples. Experiment results show that it performs better than existing single-modality prompt learning methods.

### Strengths
1. The proposed prompt learning method connects textual and visual prompts, which sounds well-motivated. Experiment results also support the idea.
2. The ablation studies are well-designed and comprehensive.

### Weaknesses
1. The method and experiment sections need more elaboration. Currently, there are many unclear points about the method itself and experiment set up. The implementation detail in Appendix A.1.2 doesn’t cover all the details. (See my questions below.)
2. I don’t think it is appropriate to call the proposed method an “in-context learning” method. In-context learning in both the language and vision literature does not involve optimizing any parameters including exterior ones like prompts. I think the method proposed in this work is more like few-shot learning, which updates parameters on some example images and then uses the updated parameters to run inference on the test sample.
3. It needs to provide more details about how Token Net is trained. If it is randomly initialized and only optimized for one step at test time, I don’t think it can “translate” text tokens into visual prompts that the vision encoder comprehends. 
4. If I understand correctly, the InCP in Section 4.1 is learned using in-context examples from the target dataset. However, CoOp and CoCoOp are learned on the ImageNet dataset. A fair comparison would be to report CoOp/CoCoOp’s results using the same few-shot examples as InCP.

### Questions
1. In Figure 4, it seems like both $P_v$ and $P_t$ and the token net are trainable. But the learning objective in Eq (2) only involves $P_v$?
2. Section 3.4 can be more elaborated. Currently, it’s not very clear. For example, it seems like cyclic prompt learning involves multi-step optimization, while in the paragraph above section 3.4, it says the method is a single-step optimization. 
3. During testing, when a new test sample comes in, do you reset $P_v$, $P_t$, and TokenNet back to its initial state? Or are the parameter updates accumulated?
4. Is the Token net separately trained before test-time adaptation or randomly initialized? How are $P_v$ and $P_t$ initialized?
5. How many tokens do you use for $P_v$ and $P_t$? How big is the TokenNet?
6. How many in-context examples do you use?
7. I don’t find the “generic-language prompt” baseline in Table 6.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper focused on the task of test-time prompt learning for vision-language models like CLIP, and proposed a visual in-context learning method to conduct one-time prompt tuning using both labeled samples as context and unlabeled test sample in a semi-supervised learning manner. The method updates both visual prompt and language prompt. Experiments are conducted on fine-grained classification datasets and distribution shift setting.

---

After rebuttal: My concerns on the comparison with few-shot learning and the information leakage of in-context samples remain. The authors confirmed that the in-context samples are guaranteed not to share the same label as the test sample, and the model can benefit from avoiding predicting the categories of in-context samples. In other words, the in-context samples help to filter out wrong answers and improve the performance, which is unfair for evaluation.

### Strengths
+ The task of test-time prompt tuning is relatively new and worth investigating. The idea of in-context prompt learning for vision-language models is novel to me.

+ The proposed method achieved consistent improvement on fine-grained classification datasets, and competitive performance on distribution shifting datasets.

### Weaknesses
 - (Major concern) This work proposed a in-context prompt learning method that used labeled samples as context during test stage. However, different from traditional in-context learning that used additional samples as a part of prompts and did not tune any parameters, these method used additional samples to tune the network rather than serve as part of prompt, which is like traditional semi-supervised learning pipeline but with fewer data and training loops. I am wondering whether the terminology of "in-context prompt learning" is proper. More evidence or reference on the terminology definition is expected during discussion.

- (Major concern) Random sampling may cause the information leakage of test set. Sec. 3.1 and Appendix A.2 indicate that the labeled data are randomly sampled for different test samples, which means that the model may see a wide range of test samples during evaluation, although they are not simultaneously seen. Compared to few-shot tuning setting, only a fixed set of labeled data is accessed. As shown in Appendix A.2, a fixed set of labeled data underperforms random sampling. I am wondering whether the performance gain is due to the information leakage caused by random sampling. A strict implementation would be using sampling from the same subset of labeled data for rather than the whole test set.

- The figures are confusing and not well designed. First, in Figure 2, it is not clear what does token space mean. The number of input tokens are 4 and the number of output tokens are 2. Does it mean the number of input tokens equals to the number of words in the prompt, and the token net aims to compress the tokens? Second, in Figure 3, the module and tokens are denoted in many colors, but it is hard to understand what each color indicates, and what is the difference between different tokens in (c) and (d). Third, in Figure, the dimension of $P_t$ (i.e., 3) does not equal to the number of prefix tokens (i.e., 4). Is it in intention? Figure 1(c) is also confusing to me to understand what happened during the cyclic learning stage.

- Difference between this method and fully test-time adaptation. According to Table 1, the main difference is that this method used additional labeled data for tuning the prompts. If so, the novelty is just additional annotations in a semi-supervised manner, which is limited.

- The ablation studies in Tables 4 and 6 are not comprehensive, which are only on three datasets compared to the main results on Table 2. Why only these three datasets are selection? How are they representative?

### Questions
Please see Weaknesses for detailed comments.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper adapts visual prompt tuning to TTA of vision-language models. They use a token net and more examples to increase the generalization of vision-language models on domain-specific tasks.

### Strengths
The introduction of visual prompt tuning is interesting.

### Weaknesses
The pros and cons of the proposed method are not discussed thoroughly.

The dataset-specific context selection process will largely limit the application of the proposed methods. The creation of the context put a strong prior on the method.

### Questions
- 1. Why use the term "in-context"? What is the "context" for an incoming test sample? What is the relationship between the context samples and the test sample?

- 2. The goal of TTA is to address the domain shift on the fly. The introduction of the context samples makes the model task-specific. For each dataset in Table 2 and Table 3, do we need to construct a dataset-specific context?
    - 2.1 If the answer is YES, I think this is not a TTA method. It is a domain/dataset-specific 1-shot or few-shot approach.
    - 2.2 If the answer is NO, the method is like [TPT with CoOp weights]. It is a one-shot training + test time visual prompt tuning. However, TPT+CoOp has much better performance.
    - 2.3 The authors should further clarify how the context samples are selected. In Table 4, we can see the context samples are vital in the proposed method.

- 3. Please also provide the inference time of the proposed method to evaluate the efficiency.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

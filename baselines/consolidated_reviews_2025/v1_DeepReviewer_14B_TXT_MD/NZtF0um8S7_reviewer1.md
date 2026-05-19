### Summary

The work explores the in-context learning ability of encoder-decoder models. The authors claim that they are the first to study in-context learning in encoder-decoder models across a wide range of tasks. Prior work mainly explored in-context learning in decoder-only models. The authors propose objective-aligned prompting and fusion-based approaches to enhance in-context learning in encoder-decoder models. They show that these approaches help seq2seq models outperform much larger decoder-only models.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The paper explores an important area that is not widely studied.
- The findings in this paper can guide future work on encoder-decoder models.

### Weaknesses

#### Some Related Works


#### comment

 - The main weakness of this paper is the lack of details about the experimental setup. I will list a few missing details below:

  - The authors do not explain how they select the 5 (or more) examples for each task. The few-shot examples are crucial for in-context learning, and the selection process can significantly impact the results. The paper should specify whether the examples are randomly selected, chosen based on some similarity metric to the test case, or selected through some other method. Without this information, it is difficult to assess the validity and reproducibility of the experiments.

  - The authors do not explain how they get the model outputs for the encoder-decoder models (how to decode and when to stop decoding). Do they use greedy decoding? Do they use a maximum sequence length? Do they use a minimum sequence length? Do they use BERT-like decoding? The decoding strategy is a critical aspect of sequence-to-sequence models, and the lack of details makes it hard to understand the experimental results. The paper should specify the decoding algorithm, the criteria for stopping the decoding process, and any hyper-parameters used during decoding. The absence of these details makes it difficult to reproduce the results and compare them with other methods.

  - The authors do not explain how they compute the model outputs for the encoder-decoder models into predictions for the NLU tasks (e.g., the authors mention that they select the option with the lowest cross-entropy loss among all the available multiple-choice options, but how do they get cross-entropy losses for the options? Do they compute cross-entropy loss for each option together with the input question and the target answer? Do they compute cross-entropy loss for each option together with the input question only?). A similar comment applies to the generation tasks (how do they compute ROUGE scores? Do they use model outputs directly? Do they apply some processing steps?). The paper needs to provide a clear explanation of how the model outputs are transformed into final predictions for both NLU and generation tasks. For NLU tasks, it is essential to clarify how the cross-entropy loss is calculated for each option and how the final prediction is made. For generation tasks, the paper should specify how the model outputs are processed (e.g., tokenization, detokenization) before computing ROUGE scores.

- The paper lacks some important baselines. The authors should include the following baselines in Table 2:

  - The performance of the models with zero-shot prompts (e.g., for SuperGLUE: <task specifics> Question: <question> Answer: <options> <target answer>).
  - The performance of the models in a few-shot setting where the few-shot examples are presented on the decoder side (e.g., for SuperGLUE: <5 few-shot examples> <task specifics> Question: <question> Answer: <options> <target answer>).

- The authors make a bold claim in the abstract that their approach outperforms a decoder-only model that is 6 times larger. However, the results in Table 2 show that T5-11B performs better than OPT-66B for 3 tasks (WiC, CB, and StoryCloze). This discrepancy needs to be addressed. The claim in the abstract is misleading, and the paper should provide a more nuanced discussion of the results, highlighting the specific tasks where the proposed approach excels and where it does not.

### Suggestions

The paper would benefit significantly from a more detailed explanation of the experimental setup. Specifically, the authors should clarify the process of selecting few-shot examples. Are the examples randomly selected, or is there a specific strategy involved? If there is a strategy, how is it implemented, and what is the rationale behind it? For instance, are the examples chosen based on their similarity to the test case, or are they selected randomly from the training set? Providing these details is crucial for ensuring the reproducibility of the experiments and for understanding the impact of the few-shot examples on the model's performance. Furthermore, the authors should specify whether the same set of examples is used for each run or if they are randomly sampled for each run. If the examples are randomly sampled, the authors should report the variance in performance across different samples of examples. This level of detail is essential for a rigorous evaluation of the proposed methods.

In addition to the few-shot example selection, the paper needs to provide a comprehensive description of the decoding process. What decoding algorithm is used (e.g., greedy decoding, beam search)? What are the hyper-parameters used for decoding (e.g., beam size, maximum sequence length)? How is the decoding process stopped (e.g., end-of-sequence token)? These details are critical for understanding how the model generates its outputs and for reproducing the results. For the NLU tasks, the paper should explain how the model outputs are transformed into predictions. How are the cross-entropy losses computed for each option? Is the input to the model the question, the options, and the target answer, or just the question and the options? Is the target answer used during inference? For the generation tasks, the paper should specify how the ROUGE scores are computed. Are the model outputs used directly, or are there any preprocessing steps involved (e.g., tokenization, detokenization)? Providing these details will enhance the clarity and reproducibility of the paper.

Finally, the paper should include the suggested baselines in Table 2. The zero-shot performance of the models provides a crucial reference point for evaluating the effectiveness of the proposed methods. Including the zero-shot performance will allow readers to assess the absolute improvement achieved by the few-shot prompting strategies. Additionally, the paper should include the performance of the models when the few-shot examples are presented on the decoder side. This baseline will help to understand the impact of presenting the examples on the encoder side versus the decoder side. The paper should also address the discrepancy between the claim in the abstract and the results in Table 2. The abstract claims that the proposed approach outperforms a decoder-only model that is 6 times larger, but the results show that T5-11B performs better than OPT-66B on some tasks. The paper should provide a more nuanced discussion of the results, highlighting the specific tasks where the proposed approach excels and where it does not. This will provide a more accurate and balanced view of the contributions of the paper.

### Questions

Please see the weaknesses section above.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

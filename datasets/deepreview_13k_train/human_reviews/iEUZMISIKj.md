# SwitchLoRA: Switched Low-Rank Adaptation Can Learn Full-Rank Information

- Decision: Reject
- Scores: 5, 5, 6, 3

## Abstract
In the training of large language models, parameter-efficient techniques such as LoRA optimize memory usage and reduce communication overhead during the fine-tuning phase. However, applying such techniques directly during the pre-training phase results in poor performance, primarily because the premature implementation of low-rank training significantly reduces model accuracy.
  Existing methods like ReLoRA and GaLore have attempted to address this challenge by updating the low-rank subspace. However, they still fall short of achieving the accuracy of full-rank training because they must limit the update frequency to maintain optimizer state consistency, hindering their ability to closely approximate full-rank training behavior.
In this paper, we introduce SwitchLoRA, a parameter-efficient training technique that frequently and smoothly replaces the trainable parameters of LoRA adapters with alternative parameters. SwitchLoRA updates the low-rank subspace incrementally, targeting only a few dimensions at a time to minimize the impact on optimizer states. This allows a higher update frequency, thereby enhancing accuracy by enabling the updated parameters to more closely mimic full-rank behavior during the pre-training phase.
  Our results demonstrate that SwitchLoRA actually surpasses full-rank training, reducing perplexity from 15.23 to 15.01 on the LLaMA 1.3B model while reducing communication overhead by 54\% on the LLaMA 1.3B model.
  Furthermore, after full fine-tuning the SwitchLoRA pre-trained model and the full-rank pre-trained model on the GLUE benchmark, the SwitchLoRA pre-trained model showed an average accuracy gain of about 1\% over the full-rank pre-trained model. This demonstrates enhanced generalization and reasoning capabilities of SwitchLoRA.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
- the authors proposed a method that leverages frequent parameter updates in LoRA (Low-Rank Adaptation) matrices during pre-training. 
- LoRA techniques in related works shown in the paper optimize memory and communication overhead during fine-tuning but underperform during pre-training due to low-rank constraints. 
- Existing methods (ReLoRA and GaLore) address this by periodically resetting low-rank subspaces, but their large intervals result in accuracy loss according to the perspectives of the authors. 
- In constrast, the method in this paper (SwitchLoRA) allows smooth, frequent parameter updates by switching LoRA vectors without significantly impacting the model’s optimizer states. 
- Key features of the idea:
  - SwitchLoRA frequently replaces portions of column and row vectors in LoRA matrices with pre-defined candidate vectors, allowing it to approximate full-rank training behavior more closely.
  - For each matrix in the LoRA adapter, a set of candidate vectors is maintained. The system can switch vectors dynamically, keeping model output consistent and effectively increasing the adaptability of low-rank spaces.
  - The frequency of switching is controlled by an exponential decay function, allowing the model to dynamically adjust update rates.
  - To manage the switch in parameters while maintaining optimization stability, SwitchLoRA resets certain optimizer states, allowing the model to stabilize quickly.
  - SwitchLoRA employs a specific initialization scheme for candidate vectors, enhancing stability and effectiveness during training.

### Strengths
- In empirical tests, SwitchLoRA demonstrates performance improvements, achieving lower perplexity than full-rank training, especially on the LLaMA 1.3B model.
- Despite frequent updates, SwitchLoRA keeps computational and memory overhead low by using pre-trained candidate vectors.
- When fine-tuned on GLUE tasks, SwitchLoRA shows a slight improvement in accuracy over full-rank models, indicating enhanced generalization.

### Weaknesses
 - Dynamic parameter adjustment impedes scalability for very large models or environments with limited resources due to additional overhead and computational costs of scaling factors.
- Broader applicability is limited since the paper primarily evaluates SwitchLoRA within language tasks, leaving its performance and adaptability in other domains.
- SwitchLoRA assumes that task-appropriate configurations can be achieved simply by adjusting scaling factors on existing model parameters. While effective within the tested scenarios, this approach may not generalize across models with different architectures or to tasks where such adjustments cannot capture necessary model changes.
- The SwitchLoRA paper provides limited comparison to other parameter-efficient fine-tuning techniques, such as adaptive pruning or selective parameter updates.
- lines 470-472: there are missing numbers at "[insert performance difference]".
- line 193-198: The authors implemented an exponential decay function for switching frequency during training, defined as frequency = Ce^(-θ * step), with coefficients determined empirically.
  - This reliance on empirical tuning limits the method’s generalizability across various models and datasets, as optimal values may vary depending on specific training scenarios.
  - The approach assumes a progressive decrease in each layer’s internal rank during training, yet this behavior may not be consistent across all models or tasks.
  - Although the exponential decay function is inspired by observed trends, the paper does not provide a theoretical framework to justify this specific form of decay.
  - A comparative analysis is lacking in the current approach to support the superiority of this decay function.
  - The predetermined exponential decay schedule does not account for the dynamic nature of training, potentially reducing its effectiveness in varied scenarios.

Furthermore, the authors provided some critics on previous works but the reviewer has a different perspective. the switchLoRA brings about specific scenarios without generalization. while, based on previous works, the reviewer can argue the following process to enhance:
  - The low-rank adaptation matrices are initialized by performing SVD on the pretrained weights. This method selects only the top singular vectors, retaining task-relevant information while significantly reducing the number of trainable parameters.
  - The low-rank matrices derived from the pretrained weights are kept frozen during training. Only a small, trainable matrix, positioned between these frozen matrices, is updated in fine-tuning. This approach reduces computational and memory overhead, as adaptation occurs through a single small matrix rather than full-rank updates.
  - In contrast to methods where parameter count scales with model dimensions, this approach keeps a constant trainable parameter count by using the small matrix with fixed dimensions. This design is highly efficient for large-scale models, where maintaining a low parameter count and memory efficiency is essential.

### Questions
- lines 470-472: there are missing numbers at "[insert performance difference]". 
- line 193-198: The authors implemented an exponential decay function for switching frequency during training, defined as frequency = Ce^(-θ * step), with coefficients determined empirically.
  - This reliance on empirical tuning limits the method’s generalizability across various models and datasets, as optimal values may vary depending on specific training scenarios.
  - The approach assumes a progressive decrease in each layer’s internal rank during training, yet this behavior may not be consistent across all models or tasks.
  - Although the exponential decay function is inspired by observed trends, the paper does not provide a theoretical framework to justify this specific form of decay.
  - A comparative analysis is lacking in the current approach to support the superiority of this decay function.
  - The predetermined exponential decay schedule does not account for the dynamic nature of training, potentially reducing its effectiveness in varied scenarios.

Furthermore, the authors provided some critics on previous works but the reviewer has a different perspective. the switchLoRA brings about specific scenarios without generalization. while, based on previous works, the reviewer can argue the following process to enhance:
  - The low-rank adaptation matrices are initialized by performing SVD on the pretrained weights. This method selects only the top singular vectors, retaining task-relevant information while significantly reducing the number of trainable parameters.
  - The low-rank matrices derived from the pretrained weights are kept frozen during training. Only a small, trainable matrix, positioned between these frozen matrices, is updated in fine-tuning. This approach reduces computational and memory overhead, as adaptation occurs through a single small matrix rather than full-rank updates.
  - In contrast to methods where parameter count scales with model dimensions, this approach keeps a constant trainable parameter count by using the small matrix with fixed dimensions. This design is highly efficient for large-scale models, where maintaining a low parameter count and memory efficiency is essential.

### Soundness
3

### Presentation
2

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
SwitchLoRA addresses limitations in low-rank adaptation methods like ReLoRA and GaLore, which restrict update frequency to maintain optimizer state consistency, thus limiting their approximation of full-rank training. SwitchLoRA frequently and smoothly alternates LoRA adapter parameters, updating only a few dimensions at a time to reduce the impact on optimizer states. This approach allows for higher update frequency, achieving accuracy improvements by closely approximating full-rank behavior. The authors validate SwitchLoRA on various LLaMA model sizes, comparing against full-rank training, ReLoRA, and GaLore. They further perform full fine-tuning of the pre-trained model on GLUE to the model’s validate reasoning abilities.

### Strengths
- The overall switching methodology - selecting candidate vectors to reset the optimizer states - is novel and enables the use of high switching frequencies. 
- The evaluations and experiments against LoRA and full-rank training are extensive and clearly show the benefits of using SwitchLoRA against them.
- The proposed method maintains performance against full-rank training while reducing the number of trainable parameters to 50-60% to full-rank training, with minimal communication overhead.

### Weaknesses
 - The paper posits that high intervals between reset/update steps are necessary in ReLoRA and GaLore to maintain optimizer state consistency and approximate full-rank training. However, SwitchLoRA employs a default highest switching frequency of 40, which decays exponentially. GaLore suggests this frequency is near-optimal without causing issues. The paper's core motivation hinges on GaLore's supposed inability to handle high switching frequencies, yet these frequencies are not tested in the paper, creating a contradiction. Experiments demonstrating SwitchLoRA's performance at these high frequencies are needed to validate the stated motivation.

- The source of the claimed improvements remains unclear. While the authors attribute them to resetting optimizer states and temporarily freezing parameters, there is a lack of concrete evidence. The improvements could stem from (1) the exponential decay switching rule or (2) the use of a random subspace instead of SVD-based updates. If either of these is the primary driver, it would significantly diminish the novelty of the work. Rigorous experiments are required to isolate the true cause of the performance gains and confirm the paper's claims.

- Table 5 presents a discrepancy in perplexity values compared to those reported in the GaLore paper. Specifically, the first two columns, presumably using a rank of 256, show values of 19.58 and 25.93 in this paper, whereas GaLore reports 18.95 and 25.36 for these configurations, despite claims of identical settings. This inconsistency raises concerns about the accuracy of the results and, if the original GaLore values are correct, suggests that GaLore might outperform SwitchLoRA in these cases. The lack of clarity regarding the configurations linked to each value further complicates the interpretation of this table.

### Questions
- The main claim of the paper must be backed with experiments, as noted in the Weaknesses section.
- The authors don’t compare validation loss curves with GaLore, which, along with point 2 in Weaknesses, casts doubt on their claims of outperforming GaLore. Including these validation loss curves would better substantiate their claims.
- Can the optimizer states be updated layer-wise, instead of updating the entire model? This could lead to further memory saving.
- The authors can include Tables/Figures comparing the memory usage of SwitchLora compared to other methods,

Minor
- Table 5 needs clarity. Are the metrics in the first two columns for a rank of 256? The configurations linked to each value are unclear and difficult to follow.

### Soundness
2

### Presentation
2

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
The paper explores the use of LoRA adapters during pre-training. The authors detail a new technique that is able to often replace vectors of the trainable parameters of LoRA adapters during training. This smooth and frequent adjustment of the trainable parameters provides a better approximation to full-rank training. Comparisons are made to full-rank training, ReLoRA and GaLore. 

When an existing vector in the LoRA adapter is replaced, W is adjusted by adding the difference between the old and new LoRA components. Vectors are chosen from a predefined set of options. 

The switching frequency using this technique is must higher than for the other approaches compared. A high-frequency of switching is employed early in training and this is reduced over time (exponentially decreasing in frequency).

### Strengths
The technique appears to offer significant gains over previous approaches. It achieves similar levels of accuracy to full-rank training with only 50-60% of the trainable parameters. The idea seems to intutively make sense.

### Weaknesses
It is currently a little unclear to me if the approach would scale or not to larger models. Could you detail the memory and compute implications of training larger models in more detail please. Can you extropolate from your current experiments to give us more confidence of the scalability of the approach?

### Questions
Qu 1: Did you experiment with different frequencies of resetting in ReLoRA? (and for GaLore?)

Qu 2: Do you, or can you, provide a direct comparison of training times between the different approaches?

Qu 3: Could you say more about how the approach would scale in terms of memory/compute requirements for much larger models?

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
This paper proposes SwitchLoRA, a parameter-efficient training method that periodically switches the vectors in low-rank terms with a set of vectors of trainable parameters. SwitchLoRA aims to achieve full fine-tuning model performance with much less memory footprint.

### Strengths
This work identifies the limited restarting frequency in ReLoRA, and proposes SwitchLoRA to address this problem by replacing the LoRA adapters frequently in the form of vectors of trainable parameters.

### Weaknesses
- This submission is wordy and incomplete. Here are some examples:
    - In line 472, there are two placeholders for experiment results, "`[insert performance difference]`". Please fill in all placeholders.
    - The oversimple flowchart in Fig. 5 does not add information beyond the Section 5 of future work. 
    - Inconsistent spelling like "pre-train" vs "pretrain". Please ensure consistency in terminology and spelling.
- Problematic experiment design.  
    - Section 4.2, in line 342, it is unclear to me how to use LoRA and SwitchLoRA to pretrain a language model from scratch. What is the value of the frozen weights, i.e., $W$ in Fig. 1(b)? Please consider providing a clear explanation of how LoRA and SwitchLoRA are initialized and used for pretraining from scratch. Specifically, if $W$ is randomly initialized and only the adapters are trained, are these random weights just noise? Why not initialize $W$ with zeros?
   - Section 4.4 fine-tunes the resultant checkpoint from Section 4.2 for each baseline and SwitchLoRA, which means the baselines and SwitchLoRA have different start points when the fine-tuning starts. In other words, this is not a controlled experiment. 
- Questionable results. 
    - The standard deviation annoted in Tab 6 and 7 are questionable. For GLUE, such large std values like $23.13\pm 15$ and $72.70\pm 4$ in Tab 6 and $47.43\pm 3$ in Tab 7 cannot be seen in other works. Please verify the correctness of these values and explain any potential sources of such high variability. This raises concerns about the stability of the method and/or the implementation, and/or the experiment setup being very sensitive to the choice of random seed.
- Insufficient experiments
    - In line 465, Table 6 presents the fine-tuning experiments on half of the subsets of the GLUE benchmark without MNLI, QNLI, QQP, and STSB. In most literature they are included. Please consider expanding the GLUE benchmark experiments to include the missing subsets. The current GLUE results are also very poor compared to prior work. For example, the fine-tuned results on the 350M model in Table 6 are much lower than BERT-large results from 2018, despite having a similar number of parameters. This raises questions about the effectiveness of the pretraining and fine-tuning process.
    - Lack of large models. This work claims that SwitchLoRA improves the training efficiency of LLMs, but only small models (up to 1.3B) are included. Conduct experiments on larger models (e.g., models with tens of billions of parameters) to better support the claims about improving LLM training efficiency. The evaluation part is insufficient to show its efficacy.

### Questions
Please refer to the Weakness.

### Soundness
1

### Presentation
2

### Contribution
1

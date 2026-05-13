# READ: Recurrent Adaptation of Large Transformers

- Decision: Reject
- Scores: 5, 5, 5

## Abstract
In the realm of Natural Language Processing (NLP), large-scale transformers have established themselves as pivotal, achieving unparalleled results across numerous tasks. The conventional approach involves pre-training these models on extensive web-scale data, followed by fine-tuning them for specific downstream tasks. However, the burgeoning size of these models, which has surged almost two orders of magnitude faster than GPU memory since 2018, has rendered their fine-tuning financially and computationally exorbitant, limiting this capability to a select few well-funded institutions. Parameter-efficient transfer learning (PETL) has emerged as a potential solution, aiming to efficiently adapt pre-trained model parameters to target tasks using smaller, task-specific models. Nonetheless, existing PETL methods either introduce additional inference latency or marginally reduce memory requirements during training, thus not fully addressing the primary motivation behind PETL. This paper introduces REcurrent ADaption (READ), a novel, lightweight, and memory-efficient fine-tuning method that incorporates a small RNN network alongside the backbone model. READ not only achieves comparable model quality to traditional fine-tuning, saving over 84\% in energy consumption, but also demonstrates scalability and independence from the backbone model size. Through extensive experiments on various NLP benchmarks, including the GLUE benchmark, READ showcases robust performance and high efficiency, reducing model training memory consumption by 56\% and GPU energy usage by 84\% relative to full-tuning, without significantly impacting inference latency and memory. We provide a theoretically justified, scalable solution for fine-tuning large transformers.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a efficient adaptation method, recurrent adaption (READ), for Transformers.  The idea is to use recurrent neural networks plus the so-called Joiner networks to learn the correction for the output of the original transformer backbone during fine-tuning.  The experiments verify the effectiveness of the proposed approach.

### Strengths
- According to the experimental result presented in this paper, the saving in memory consumption and energy usage are decent.

- The idea of learning _corrections_ for the output of the original Transformer is well-motivated and looks interesting to me. That being said, given my limited familiarity with existing methods in this domain, I'm unable to ascertain the novelty of this idea.

- The authors are upfront about the limitation of the current paper in Sec. 6.

### Weaknesses
 - I find the notion of recurrence in this paper somewhat tricky. Typically,  Recurrent neural networks process the input sequentially by taking one token as the input at a time and updating the hidden state. However, in this paper, recurrence does not occur in the sequence level. Instead, it occurs at the model layer level, which seems non-standard for me. The authors should clarify the specific mechanism of information flow between layers in their recurrent adaptation module. It is unclear how the hidden state is initialized at each layer and how the information is propagated across the layers. This non-standard use of recurrence needs to be justified with clear explanations and potentially comparisons with other methods that use layer-wise processing.

- The scope of the method and experiment seems narrow. It only considers the encoder-decoder Transformers on a single natural language understanding benchmark. The paper would be significantly strengthened by including experiments on more diverse Transformer architectures, such as decoder-only models, and a wider range of tasks, including other NLP tasks (e.g., text generation, summarization) or even tasks from other domains like computer vision. This limited scope makes it difficult to assess the general applicability of the proposed method.

- Training time is not reported in this experiment. It is essential to include training time for a comprehensive comparison among different methods. The efficiency of the proposed method should be evaluated not only in terms of memory and energy consumption but also in terms of training time. Without this information, it is difficult to fully assess the practical advantages of the proposed approach.

- Currently the presentation of the paper is flawed. There are many formatting issues which impedes readability.
  - In the abstract on OpenReview, Latex commands (`\textbf`) are not deleted. $\%$ is missing in the discussion of the reduction in memory consumption and GPU energy usage.
  - The format of citation is bad in this paper. The authors should have used `\citet` and `\citep` appropriately.
  - In the abstract, the first letter of "Transformer" is capitalized but in the main body of the paper it's not. The authors should make this consistent and I recommend to always capitalize the first letter of "Transformer".
  - Missing references. "Appendix ?" and "Table ?" in Sec. 4.
  - Bad notation. Eq. (4) uses $\bar U$ to denote a cumulative sum. This can be misleading because people are more likely to interpret $\bar U$ as an average.

- Minor comments.
  - Abstract. "empirical evaluation of the GLUE benchmark" $\to$ "empirical evaluation on the GLUE benchmark".
  - Page 4. "the following equation systems gives" $\to$ "the following equation system gives"
  - Page 4. "." is missing in the last sentence of the last paragraph.

### Questions
Please refer to the **Weaknesses** part.

One more clarification question:
- What does "normalized" mean in the caption of Fig. 1 mean? What are the original results and how are they normalized?

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents READ (Recurrent Adaption), a light weight and memory-efficient finetuning method by inserting a small RNN network to bypass the back propagation to the large backbone network. Results show that READ can achieve great reduction in both memory and energy consumption.

### Strengths
(1) Clear description of the proposed method in Section 2.

(2) Good evaluation of the proposed method on T5 model and GLUE benchmark.

### Weaknesses
 (1) The main result described in abstract/introduction (memory consumption reduced by 56%, and gpu energy reduced by 84%) are compared with full-tuning, not the SOTA memory/energy-efficient finetuning methods. At least we need another data point: a direct comparison to the current best SOTA. From the figure 2, I believe that the comparison with SOTA will lead to much smaller reduction percentages. Specifically, the comparison should include methods like LoRA and Adapter, as these are common baselines for parameter-efficient fine-tuning.

(2) A drawback in figure 2 is that it’s hard to justify the advantage of the proposed READ method by just a single data point. Ideally, it’d be helpful to have multiple data points for READ, under different energy/memory consumptions, in order to build a “Pareto curve”. In this way, it’d be much easier to tell whether READ advances the whole Pareto frontier. The current single point comparison makes it difficult to assess the trade-offs and the overall efficiency of the method across different resource constraints. A Pareto curve would clearly show if READ is superior across various operating points.

(3) In Table 1, it is unfair to only try the proposed method on the larger T5-large. You need to also try other methods + larger T5 in order to prove your points. The comparison should include other parameter-efficient methods on the same T5-large model to demonstrate the relative advantage of READ. Without this, it's hard to tell if the performance gain is due to READ or simply the model size. It would also be beneficial to test READ on smaller T5 models to understand its scalability.

(4) As the authors also mentioned in limitation section, it’d be great to add evaluation on GPT-style models and corresponding downstream tasks. This is crucial to demonstrate the generalizability of the method beyond encoder-decoder architectures. The current evaluation is limited to T5 and GLUE, which may not fully capture the potential of the method.

(5) To me, the overall proposed idea make sense but not very exciting. It seems more like an incremental work compared to existing methods (the RNN being the only main novelty). The core idea of using a small RNN for adaptation, while sensible, doesn't seem to introduce a significant paradigm shift in parameter-efficient fine-tuning.

### Questions
See the concerns I listed in weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors proposed REcurrent ADaption (READ), a lightweight and memory-efficient fine-tuning method for pre-trained foundation models. READ inserts a small RNN network alongside the frozen backbone model, which is trained for downstream tasks. READ can achieve comparable or better accuracy compared to existing parameter-efficient fine-tuning methods on the GLUE benchmark, using less training memory and energy consumption.

### Strengths
1. Firstly, the paper is generally well-written and easy to follow.
2. There is no need for an extra step pre-training the side network due to the compact design, making the transfer learning pipeline simple. 
3. The proposed method achieves a better accuracy-energy trade-off compared to existing methods on GLUE.

### Weaknesses
1. The writing quality should be improved. For example, Appendix?? and Table ??  in Sec 4. 
2. The experiments are quite restricted, only using T5 on GLUE benchmarks. It would be better to evaluate more model architectures like GPT-style (if LLaMA is too expensive for the hardware setup, maybe evaluate smaller ones like GPT-2) and more tasks. 
3. The latency evaluation in Figure 6 is confusing: why are BitFit and LoRA slower compared to vanilla fine-tuning? Both methods do not introduce extra parameters into the base model (LoRA weights can be fused). It is not reasonable that READ is faster than BitFit/LoRA. 
4. What is the non-recurrency setting in Table 2? Why are there more training parameters?
5. The power statistics from NVIDIA's smi are highly unstable. Have you found the calculation to be stable based on a minute-level sampling?
6. One good thing about transformers is the better training parallelism compared to RNN models. Does the design prevent parallel training due to the recursive nature? (I think it can still be parallelized if using the vanilla RNN)

### Questions
Please see the questions in the weakness sections. I will wait for the authors' feedback for the final ratings.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

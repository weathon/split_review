# Lightweight Neural App Control

- Decision: Accept
- Avg Score: 7.50
- Scores: 6, 8, 8, 8

## Abstract
This paper introduces a novel mobile phone control architecture, termed ``app agents", for efficient interactions and controls across various Android apps. 
The proposed Lightweight Multi-modal App Control (\textbf{LiMAC}) takes as input a textual goal and a sequence of past mobile observations, such as screenshots and corresponding UI trees, to generate precise actions. To address the computational constraints inherent to smartphones, within LiMAC, we introduce a small Action Transformer (\textbf{AcT}) integrated with a fine-tuned vision-language model (VLM) for real-time decision-making and task execution.  We evaluate LiMAC on two open-source mobile control datasets, demonstrating the superior performance of our small-form-factor approach against fine-tuned versions of open-source VLMs, such as Florence2 and Qwen2-VL. It also significantly outperforms prompt engineering baselines utilising closed-source foundation models like GPT-4o. More specifically, LiMAC increases the overall action accuracy by up to 19\% compared to fine-tuned VLMs, and up to 42\% compared to prompt-engineering baselines.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces Lightweight Multi-modal App Control (LiMAC), a framework designed for efficient mobile app control by combining a small Action Transformer (AcT) and a fine-tuned vision-language model (VLM). LiMAC processes user goals and smartphone states, making real-time decisions through AcT for action types like clicking or scrolling. For complex tasks requiring text input, it leverages the VLM to generate appropriate content. Evaluation of LiMAC on AndroidControl and Android-in-the-Wild datasets, LiMAC shows superior accuracy and speed over traditional VLMs and foundation models like GPT-4o, achieving up to 42% higher action accuracy and reducing task completion time by 30-fold. This approach emphasizes efficient model use on resource-limited devices, while future improvements may incorporate reinforcement learning for enhanced performance.

### Strengths
- LiMAC combines a small Action Transformer (AcT) with a fine-tuned vision-language model (VLM). This hybrid approach is tailored to the computational constraints of mobile devices, achieving efficient and accurate control without relying on large, resource-intensive models. The AcT independently handles common actions, while the VLM is selectively employed for complex natural language tasks, optimizing both resource usage and response time.
- LiMAC’s modular structure supports the integration of different models for specialized tasks, such as using AcT for action type prediction and click targeting, while optionally substituting modules for specific needs (e.g., Qwen2-VL for text generation tasks). This flexibility enables developers to adapt LiMAC easily for varied app control tasks, optimizing specific components without overhauling the entire architecture​.
- The AcT component employs a contrastive objective to identify UI elements for click actions, using cosine similarity and a learnable temperature parameter. This approach is advantageous in handling class imbalance and dynamically varying UI elements across episodes. The use of contrastive learning allows AcT to focus on directional alignment in the embedding space, facilitating precise UI element targeting even in dense or complex layouts

### Weaknesses
 -  Although the paper evaluates LiMAC on two datasets, both datasets are relatively specific to Android applications, potentially limiting the generalizability of results to other operating systems (e.g., iOS) or app control tasks with distinct interface designs. This is a significant concern as the UI paradigms and interaction models can vary substantially across platforms, and the current evaluation does not sufficiently demonstrate the robustness of LiMAC to such variations.
- The paper does not provide an extensive scalability analysis of LiMAC’s architecture as task complexity or the number of available UI elements increases, which may impact its robustness in more complex or densely populated app environments. Specifically, the paper lacks an analysis of how the performance of the Action Transformer (AcT) degrades as the number of UI elements increases, particularly in terms of computational cost and prediction accuracy. This is crucial for understanding the practical limitations of the approach in real-world applications.
- LiMAC operates within a fixed action space, which could restrict its adaptability to applications requiring more dynamic or unconventional actions not included in its current design. This limitation is particularly relevant when considering the wide range of interactive elements and gestures that modern mobile applications employ, potentially hindering its flexibility in expanding to novel app interaction scenarios.
- The evaluation is conducted on simulated datasets without testing LiMAC’s performance on actual mobile devices. This limits understanding of its practical usability, particularly concerning latency, responsiveness, and potential challenges from hardware constraints and real-world conditions. The absence of real-world testing makes it difficult to assess the true feasibility of deploying LiMAC on resource-constrained mobile devices.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces LiMAC (Lightweight Multi-modal App Control), a new architecture designed for mobile app control that combines a lightweight transformer, AcT, with a fine-tuned vision-language model (VLM). The standout feature here is the gated architecture, which smartly assigns tasks: AcT handles basic interactions like clicks and scrolls, while the VLM is called upon only for text-based actions that require deeper language comprehension. The approach yields substantial improvements in both inference speed and accuracy on two mobile action datasets.

### Strengths
1. **Novel design.** The authors designed a lightweight module to predict the type of actions to be taken, and execute simple actions with this light-weight module directly. Leaving the VLM to solve complex tasks that involve text generation. This leads to both performance speed-up and better accuracy.

2. **Thorough evaluations.** I like how the authors compared using AcT/VLM for different tasks, clearly demonstrating the performance gain by adopting the current design, which makes sense to me.

3. **Good writing.** The paper is easy to follow.

### Weaknesses
1. **Limited Dataset and Tasks.** The authors used two datasets of relatively small size, this paper could benefit from larger-scale experiments and maybe real-world user studies. The datasets used, while open-source, may not fully capture the diversity and complexity of real-world mobile applications. This limitation makes it difficult to assess the model's generalization capabilities, particularly in scenarios with more intricate UI designs or less common interaction patterns. The lack of diverse data may also lead to overfitting on the specific characteristics of the used datasets, thus limiting the model's applicability in broader contexts.

2. Due to the limited data size, the proposed model may have additional difficulties in solving difficult tasks (which is where the mobile AI is needed to most, from my opinion). More studies/analysis on failure mode could make this paper better. It would be beneficial to see a detailed breakdown of the types of errors the model makes. For instance, does it struggle more with certain types of UI elements (e.g., complex menus, custom widgets) or with tasks that require a longer sequence of actions? Understanding these failure modes would provide valuable insights into the model's limitations and areas for improvement.

### Questions
See my suggestions in the weakness section, here are some of my questions:

1. How does the model handle dynamic UI elements or applications with frequently changing interfaces? Do you need to retrain a model for each software update?

2. What is the impact of the VLM size on the overall performance? Could one larger VLM learn to solve all the tasks?

3. How does the system handle errors or recovery from incorrect actions? Or safegaurding it from performing unwanted actions (for example send out user's passwords to someone else).

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents a new framework, called LiMAC, for lightweight and efficient Android navigation. Combining text and image embeddings, an action transformer predicts which of ten actions needs to be taken, and, depending on this output, a fine-tuned VLM may be queried to help with more complex tasks, such as text input. A major advantage of this setup is its significantly reduced inference time requirements compared to models such as SeeAct, while attaining higher overall performance on the Android-in-the-Wild and AndroidControl datasets. The authors apply ablation studies to demonstrate the usefulness of CLIP fine-tuning and the image embeddings, as well as the robustness of their setup to the absence of UI tree descriptions. In all, LiMAC is just a 520M-parameter addition, allowing it to run efficiently directly on Android devices.

### Strengths
The paper is incredibly clear and well-written. I am not an expert on Android or UI agents, but it was obvious what the contribution was, and why it was important. The small number of parameters in LiMAC make it clear how this advances the ability of users to run advanced Android control models directly on devices. The way the information is encoded is also very thoroughly described. It is somewhat difficult for me to evaluate novelty, but, assuming the related works section does not have any glaring omissions, is a novel approach to solving this problem. The figures are very clear and well-made, and efficiently convey the achitectural design to the reader. Finally, the ablation experiments are well-run, and justify the use of the multiple submodules, as well as demonstrating robustness to a lack of a UI hierarchy description, implying that this method may be applicable out-of-the-box to completely novel Android environments.

### Weaknesses
I am not an expert in this area, so it is difficult for me to point out major weaknesses—the paper clearly states a contribution, and is very self-contained. However, there are several minor things that were unclear to me, where the paper might benefit from more detail:

1. The paper mentions that positional encodings are used to represent the nesting of UI elements. How is this done, exactly? It's unclear how the positional encodings are combined with the visual information of the UI elements, and whether the positional encodings are absolute or relative to other elements. Furthermore, it is not clear how the positional encodings are generated for elements at different depths of the UI hierarchy.
2. It would be good to know what the "ten distinct action types" are—it seems like the same few examples are given at several points in the paper, and only a few are focused on. Are the rest omitted because they're not very interesting and "just work", or are very similar to each other, or something else? A more detailed explanation of the full action space would be useful, including the frequency of each action in the datasets used, and the specific challenges associated with each action type.
3. In Table 1, is Florence2 fine-tuned or the base model? (I know that in LiMAC with Florence2, Florence2 would be fine-tuned, but it's not fully clear whether this is the case for Florence2 alone). The paper should explicitly state whether the Florence2 baseline is fine-tuned or used as a zero-shot model. If fine-tuned, it would be good to know the fine-tuning procedure and hyperparameters used.
4. How, exactly, is "end-to-end accuracy" calculated? Why would predicting "wait"s rather than "input-text"s increase overall accuracy? I understand that you try to explain this on lines 369–403, but a clear definition of the accuracy calculation would make this paragraph make more sense. It would be helpful to have a formal definition of the accuracy metric, including how the action type prediction and action parameter prediction are combined, and how the "wait" action is handled differently from other actions in the accuracy calculation.

Minor issues:
- On line 118, "that treat" should probably be "that they treat"
- On line 142, it's a bit weird that the full architecture link links back to the current section

### Questions
Please see the weaknesses section, parts 1–4.

5. You mention that LiMAC "address[es] the computational constraints inherent to smartphone". Have you tried running it on a smartphone? If so, how well did it go?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work introduces LiMAC, which is an architecture for training smaller neural networks that could fit on-device for UI control. LiMAC processes UI elements as embeddings, uses a contrasting learning approach for click actions, a gated architecture for selectively invoking a fine-tuning VLM to generate text content, and it shows ablations of the architecture.

The work evaluates several different variances of LiMAC and compares them to multiple baselines, including those using large, proprietary models. In addition to comparing accuracy, they also compare inference time, which is important for on-device applications.

### Strengths
The work tackles an under-explored problem of considering compute/inference costs for UI control agents. To get practical agents, the community needs this type of work.
The performance of the LiMAC agent is strong compared to the baselines in the paper. They apply InfoNCE loss in an interesting way for screen understanding and automation. The work includes a large number of baselines, which is appreciated. The authors take off-the-shelve VLMs and fine-tune them for device control, as part of the baselines and main results. And the work include ablation analyses of their results.
The authors explain their methodology well and do rigorous evaluation.

### Weaknesses
The results are not that much better compared to the baseline of fine-tuning an off-the-shelf model, particularly for Florence2 as shown in Table 1 (70.8 vs 72.2 for AitW and 57 vs. 63.1 for AndCnrl). It's also hard to tease out if the improved performance is from architectural breakthroughs or rather just from adding more parameters by incorporating the LiMAC network. Specifically, while the authors claim computational efficiency, the memory footprint of the approach is not clear, as the larger VLM needs to be loaded and ready to go at all times. This could negate the benefits of a smaller model from a practical on-device perspective.

On a related note, the claims of the superiority of the proposed architecture would be strengthened with online evaluation by using model-based evaluation on AitW as in DigiRL: https://arxiv.org/abs/2406.11896 or using an online benchmark (e.g., AndroidWorld https://arxiv.org/abs/2405.14573).

The architecture of LiMAC is not particularly novel. While the contrastive loss is interesting, the other parts such as representing UIs using embeddings of UI elements is not novel (past examples: Mapping Natural Language Instructions to Mobile UI Action Sequences: https://arxiv.org/pdf/2307.10088, Android in the Wild: A Large-Scale Dataset for
Android Device Control https://arxiv.org/pdf/2307.10088). While the gated architecture with the VLM is a sensible engineering decision, it is not novel from a research perspective.

### Questions
Please see weaknesses.

## Comments
(You do not need to respond to these; they are intended to be helpful)

In future work, you can…
* Do actual on-device implementation. I suspect it may be non-trivial
* You could report mobile-specific performance metrics (battery impact, memory usage, etc.)
* Analyze real-world latency measurements on real phone, which would be compelling

### Soundness
3

### Presentation
3

### Contribution
3

# HeadMap: Locating and Enhancing Knowledge Circuits in LLMs

- Decision: Accept
- Scores: 5, 5, 5, 6

## Abstract
Large language models (LLMs), through pretraining on extensive corpora, encompass rich semantic knowledge and exhibit the potential for efficient adaptation to diverse downstream tasks. However, the intrinsic mechanisms underlying LLMs remain unexplored, limiting the efficacy of applying these models to downstream tasks. In this paper, we explore the intrinsic mechanisms of LLMs from the perspective of knowledge circuits. Specifically, considering layer dependencies, we propose a layer-conditioned locating algorithm to identify a series of attention heads, which is a knowledge circuit of some tasks. Experiments demonstrate that simply masking a small portion of attention heads in the knowledge circuit can significantly reduce the model's ability to make correct predictions. This suggests that the knowledge flow within the knowledge circuit plays a critical role when the model makes a correct prediction. Inspired by this observation, we propose a novel parameter-efficient fine-tuning method called HeadMap, which maps the activations of these critical heads in the located knowledge circuit to the residual stream by two linear layers, thus enhancing knowledge flow from the knowledge circuit in the residual stream. Extensive experiments conducted on diverse datasets demonstrate the efficiency and efficacy of the proposed method.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper represents another method of task-specific training and is one of the parameter-efficient fine-tuning approaches, referred to as HeadMap. The authors discovered that for certain tasks, specific attention heads are particularly influential; masking these heads significantly decreases performance. They propose a layer-conditioned locating algorithm to identify knowledge circuits in LLMs that greatly impact predictive accuracy. Based on this, they suggest training focused on these knowledge circuits, where only a small number of parameters are updated. The results are complementary to those of LoRA, and together they yield improved outcomes.

### Strengths
It complements LoRA-type fine-tuning with utilizing significantly fewer parameters. When combined, they enhance accuracy for specific tasks and could be a valuable method for various applications.

### Weaknesses
Compared to LoRA, this approach is more challenging to utilize in practice.

### Questions
Is the code available? How can we verify the results?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper attempts to explore the intrinsic mechanism of LLMs with the concept of knowledge circuits. Specifically, the termed knowledge circuits refer to the attention heads that are more important to specific tasks in all attention heads across all transformer layers. To locate the knowledge circuits, the paper explores direct strategy, simple greedy strategy and layer-conditioned strategy. The underlying assumption is that if the attention head is important, masking this attention head would cause significant increase of the task loss. After locating knowledge circuits, the paper fine-tunes the attention heads therein with LoRA-like Map modules. Experimental results evaluate the effectiveness of this design.

### Strengths
1. Knowledge circuit is an interesting concept that can help understand the mechanism of LLM performance on specific tasks.
2. The paper proposes three strategies to locate the knowledge circuits, and two strategies to fine-tune the model with knowledge circuits, which can be inspirable for future works on knowledge circuits.
3. Experimental results demonstrate the effectiveness of the proposed model.

### Weaknesses
1. The use of locating knowledge circuits is somewhat straightforward, and the concept of knowledge circuit was proposed be existing studies [1]. Actually, the reference [1] is missing in this paper, and it requires to make discussion with [1].
2. The proposed method may have less efficiency and less generality. The knowledge circuit has to be located specifically for specific tasks, and then be adopted to enhance the model on the target task. The method requires to detect the 64 samples with lowest losses, and then conduct layer-conditioned locating by masking each attention head in each layer one-by-one. This procedure would have high time-consume. Besides, the knowledge circuit may hardly be transferred on different tasks. This would cause the limitation of the proposed method in application. The generality is also concerned whether the method can be used for different tasks.
3. The selected samples with lowest losses may also be dubious. The 64 samples with lowest losses may be the 64 most easy samples for each task. Therefore, the located knowledge circuit may not be optimal.
4. The performance improvements are somewhat marginal. This also affects the contribution of the proposed method.

[1] Knowledge Circuits in Pretrained Transformers. NeurIPS 24.

### Questions
1. In Figure 1 (a) and (b), it has different value ranges of attention visualization between the results on SIQA and HellaSwag. What may be the reason of that? Why there is only a light point in Figure 1(d) on Layer-0 and Head-25?
2. What are the impacts of other attention heads beside the knowledge circuits? Can these attention heads be ablated to further enhance the accuracy and efficiency?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a novel method called HeadMap, aimed at identifying and enhancing knowledge circuits within large language models (LLMs). The authors propose a layer-conditioned locating algorithm that identifies critical attention heads layer by layer, which are essential for making accurate predictions on specific tasks. Through extensive experiments on various commonsense reasoning datasets, the authors demonstrate the effectiveness of the HeadMap method in improving model performance while maintaining parameter efficiency. Additionally, the paper explores the overlap of knowledge circuits across different datasets, revealing the varying knowledge requirements for different tasks.

### Strengths
1.	The proposed layer-conditioned locating algorithm and the HeadMap method provide a fresh perspective on understanding and optimizing LLMs, particularly in identifying and leveraging critical attention heads, showcasing innovation.
2.	HeadMap outperforms random selection and simple greedy methods, and the HeadMap method achieves comparable performance to baseline models while using fewer parameters

### Weaknesses
1.	While the paper shows that masking certain attention heads affects performance, it does not provide in-depth mechanistic insights into why these specific heads are critical.
2.	The layer-conditioned locating algorithm may introduce bias in selecting attention heads based on the specific datasets used. If the algorithm is overly tuned to the characteristics of these datasets, it may not generalize well to other tasks or datasets
3.	The experiments primarily focus on commonsense reasoning tasks. How does it perform in tasks like generative tasks, domain-specific applications?
4.	Lack of Ablation Studies on Redundant Heads

### Questions
Refer to Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper ‌explores‌ the intrinsic mechanisms underlying the attention heads of LLMs, and ‌proposes‌ an algorithm to detect the important heads that ‌play‌ a critical role in LLMs. Based on these observations, the authors further ‌propose‌ a new PEFT method that only fine-tunes these important heads, and ‌verify‌ its effectiveness via extensive experiments.

### Strengths
The overall writing is good. This paper is easy to follow.

The analysis about the  attention heads is comprehensive and reasonable.

The experimental results demonstrate the state-of-the-art performance, and the ablation study empirically proves the effectiveness of the proposed method.

### Weaknesses
The concept of the knowledge circuit is interesting, but the algorithm to find such a circuit is overly greedy. From my perspective, the selected heads are only layer-wise optimal. It seems this problem can be ‌solved‌ by dynamic programming to find a more optimal result, and ‌wouldn't‌ cost much. And then, the knowledge circuit can become a real "circuit".

The improvement of adopting HeadMap is not significant in Table 1, ‌especially‌ when using Llama3-8B as the LLM.

### Questions
Please see the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

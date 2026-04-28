# E5-V: Universal Embeddings with Multimodal Large Language Models

- Decision: Reject
- Avg Score: 6.25
- Scores: 8, 6, 6, 5

## Abstract
Multimodal large language models (MLLMs) have shown promising advancements in general visual and language understanding. However, the representation of multimodal information using MLLMs remains largely unexplored. In this work, we introduce a new framework, E5-V, designed to adapt MLLMs for achieving universal multimodal embeddings.
Our findings highlight the significant potential of MLLMs in representing multimodal inputs compared to previous approaches. By leveraging MLLMs with prompts, E5-V effectively bridges the modality gap between different types of inputs, demonstrating strong performance in multimodal embeddings even without fine-tuning.
We propose a single modality training approach for E5-V, where the model is trained exclusively on text pairs. This method demonstrates significant improvements over traditional multimodal training on image-text pairs, while reducing training costs by approximately 95\%. Additionally, this approach eliminates the need for costly multimodal training data collection.
Extensive experiments across four types of tasks demonstrate the effectiveness of E5-V. As a universal multimodal model, E5-V not only achieves but often surpasses state-of-the-art performance in each task, despite being trained on a single modality.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces E5-V, a prompt-based representation designed to achieve universal multimodal embeddings based on Multimodal Large Language Models (MLLMs). E5-V applies a cost-effective single-modality training approach using text-only data, and achieves better multimodal embeddings than image-text pairs across four tasks.

### Strengths
1. A new multimodal representation framework leveraging the multimodal understanding capability of MLLMs, with a clear motivation and a simple yet effective method.
2. Strong performance on text-image retrieval and composed image retrieval tasks with text-only training data, eliminating the need for costly multimodal training data and computing.

### Weaknesses
There are no major weaknesses. Just some minor weaknesses and a few questions in need of clarification.
Minor weaknesses:
1. The authors provide a visualization to illustrate the "modality gap". It would be better to provide a quantitative metric ( such as
https: //openreview. net/pdf? id=S7Evzt9uit3 ) to evaluate the gap between image embeddings and text embeddings from MLLMs w/o prompt-based representation.
2. Could you clarify whether the visualization of Figure 3(b) is before or after single modality training? Could you provide a visualization comparison of before and after single modality training?
3. One-word embedding might be not enough. I am wondering whether expanding the length of output words will lead to performance gains. For example, What if in Figure 2, there are multiple objects in the image and the instruction is to modify one object of them, will E5-V get it right?

### Questions
1. It is intriguing to see adding one modality could improve the performance of multiple modalities. I am wondering about the scalability of this method. What will happen if there is more text data included in fine-tuning? (Furthermore, will adding multimodal pairs further improve the performance?)
2. Some claims need supporting citations. For example, line 42-43, "adapting CLIP to universal multimodal embeddings will have shortcomings such as poor language understanding, limited real-world knowledge, .."
3. Regarding the robustness of this method, Would the difference in prompt during inference give substantial performance variations?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a method of training a multimodal model that can output multimodal representations. In contrast to conventional multimodal models such as CLIP, which consists of separate encoders for different modalities, the proposed E5-V is based on a single pretrained MLLM (multimodal large language model) such as LLaVA-Next. E5-V is trained on only text data (natural language inference dataset) and requires a lower computational cost than the previous models by leveraging the knowledge of the MLLM. The authors conducted experiments on text-image retrieval, composed image retrieval, image-image retrieval, and sentence embedding tasks. The experiments demonstrated that the proposed training method works well.

### Strengths
1. The paper is well written. I could understand their motivation, the proposed method, and the experimental results.
2. The proposed method is simple but effective. If we have a good pretrained MLLM, we can easily fine-tune it for multimodal representations. This method can be applied to other combinations of two or more modalities as well.
3. A trained embedding space is free from the modality gap issue, one of the important issues of contrastive learning-based multimodal models.
4. The authors conducted several experiments to show the proposed training method works well.

### Weaknesses
I acknowledge that the proposed training method is efficient if we have a good enough pretrained MLLM and that a trained embedding space is free from the modality gap. These properties are excellent. However, I doubt if the comparative experiments are fair in terms of model size. The model size of E5-V (LLaVA-Next-8B) is 8B, which is larger than CLIP, BLIP, and even EVA-CLIP used for comparison. As shown in the [EVA-CLIP paper](https://arxiv.org/abs/2303.15389), the model size affects its performance. If possible, a smaller size of E5-V should be evaluated/compared as well. I know that LLMs show emergent abilities and smaller models might have no/weak capabilities of encoding images/text very well. Even if so, showing comparisons will be informative to readers.

### Questions
- I would appreciate the authors' response about my comment in "Weaknesses".
- I recommend placing some samples of query and retrieved image pairs from the composed image retrieval and image-image retrieval tasks in the main body and/or Appendix. Such visualization will provide readers with a clear vision of the differences between the conventional and proposed models.

### Soundness
2

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
E5-V is a framework that adapts multimodal large language models (MLLMs) for universal multimodal embeddings. By training solely on text pairs, E5-V reduces training costs by 95% and demonstrates high effectiveness across tasks, bridging modality gaps efficiently.

### Strengths
Using MLLM so that E5-V could deal with interleaved input and using small batch size.

Only trained on text-only data leads to better performance compared to the model trained on multimodal data.

Use “summary XXX in on word” to bridge the modality gap between text and vision effectively

### Weaknesses
The "summary XXX in one word" prompt enables the model to handle simple image or text inputs. If the input complexity increases, a word cannot illustrate the input text /image well.

For new multi-model task, the new prompt needs to be designed to ensure effective performance.

### Questions
Since there is no training for modality encoder and projector, how can the modality encoder and projector generalize to the model in the 
inference time?

E5-V is trained on text-only data, yet it shows minimal improvement in text-only tasks (e.g., sentence embeddings: 86.00 vs. previous SOTA 85.70). However, it achieves significant gains in image-related tasks, such as image retrieval. Why does this difference in improvement occur?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper focuses on obtaining representations of texts and images
from multimodal LLMs (MLLMs).  Authors approach this goal by proposing
E5-V, which leverages prompts like "summarize above image in one word"
along with an image
to input to the MLLMs to close the modality gap.  E5-V is a Llava-based
MLLM finetuned on text-only data (NLI) to extract multimodal
representations. It also supports for embedding interleaving text and
image sequences, which potentially supports for new applications.

Authors show that E5-V outperforms CLIP-based methods in text-to-image
retrieval benchmarks. Usage of E5-V on composed image retrieval and
image-to-image retrieval is also presented.

### Strengths
- E5-V is simple, intuitive, and can be potentially adopted in various applications.
 
- Training E5-V seems lightweight -- it just requires training on text-only data.
  
- E5-V highlights the potential of extracting representations from LLM-based models. Expanding the scope of the current research and
  real-world applications where CLIP-like models are still extensively used.

- Representing modality-interleaved sequences is beneficial and can unlock many new applications.

### Weaknesses
 - Compared with CLIP-like models, inference with LLM-based E5-V seems
  still heavy (e.g., 8B of E5-V vs 5B of EVA-CLIP).

- More in-depth analyses are desirable/needed to show the inner
  workings of E5-V, e.g., how did it close the modality gap, by just
  using a prompt? Also, some qualitative examples are necessary. E.g.,
  is E5-V better at encoding higher-level semantic information than
  some low-level features like textures?

- Image-to-text retrieval performance (Tab1) on standard benchmarks
  Flickr30K and COCO are not good and consistently worse than
  baselines. This is counter-intuitive, given that E5-V was finetuned
  on the  NLI datasets, which is text data.

So overall I feel the paper is a bit pre-mature, and more rounds would
be beneficial.

### Questions
In Tab1, why E5-V achieved worse text-retrieval results, consistently,
than EVA-02-CLIP-5B? E5-V was finetuned on NLI datasets, which are
supposed to improve its ability of embedding texts. But this seems not
the case. What are the hypotheses of this observation?

### Soundness
3

### Presentation
2

### Contribution
3

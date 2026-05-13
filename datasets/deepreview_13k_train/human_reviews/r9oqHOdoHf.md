# TULIP: Token-length Upgraded CLIP

- Decision: Accept
- Scores: 6, 6, 8

## Abstract
We address the challenge of representing long captions in vision-language models, such as CLIP. By design these models are limited by fixed, absolute positional encodings, restricting inputs to a maximum of 77 tokens and hindering performance on tasks requiring longer descriptions. 
Although recent work has attempted to overcome this limit, their proposed approaches struggle to model token relationships over longer distances and simply extend to a fixed new token length. Instead, we propose a generalizable method, named TULIP, able to upgrade the token length to any length for CLIP-like models. We do so by improving the architecture with relative position encodings, followed by a training procedure that (i) distills the original CLIP text encoder into an encoder with relative position encodings and (ii) enhances the model for aligning longer captions with images. By effectively encoding captions longer than the default 77 tokens, our model outperforms baselines on cross-modal tasks such as retrieval and text-to-image generation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper addresses the challenge of integrating positional information effectively in contrastive vision-language models, particularly when dealing with long captions. Traditional models like CLIP are limited by short context windows, which restricts their ability to process detailed and dense textual descriptions. The authors propose an approach that combines Rotary Position Embedding (RoPE) and Contextual Position Encodings (CoPE) to better handle long captions without the need for training from scratch. This method aims to enhance the model's ability to comprehend pairwise token relationships and capture fine-grained relative positions in longer, more complex captions. The paper builds upon existing work such as Long-CLIP and proposes a refined technique to address the limitations of absolute positional encodings through interpolation.

### Strengths
1. Although the techniques themselves (RoPE and CoPE) are not novel, the paper demonstrates creativity in combining these methods to tackle the limitations of existing models like CLIP. This approach leverages the strengths of both RoPE and CoPE to address the shortcomings of absolute positional encodings, thereby providing a more dynamic and effective way to capture positional relationships in long sequences.

2. The paper is well-written and clearly presented. The authors effectively communicate their ideas and methodologies, making it accessible to readers with a background in machine learning and natural language processing. The use of figures, tables, and examples to illustrate key points is helpful in conveying the technical details of the proposed approach.

### Weaknesses
1. The proposed method appears to be an incremental improvement based on existing models like Long-CLIP. The combination of RoPE and CoPE, while potentially effective, does not introduce fundamentally new concepts. Both RoPE and CoPE are not novel and have been introduced in prior works. The primary contribution seems to be the application of these methods to the specific task of processing long captions, which may not be sufficient to claim significant novelty.

2. The paper does not adequately compare its proposed method with other approaches that handle long text descriptions, such as those based on the encoder of T5 model. T5-based models are known for their capability to process long texts effectively. The authors need to clearly articulate the advantages of their approach over T5-based methods and provide empirical evidence to support these claims. Without this comparison, it is challenging to assess the relative effectiveness of the proposed method.

3. The paper lacks a deep theoretical analysis of why the combination of RoPE and CoPE is expected to perform better for long captions. A more detailed theoretical justification or analysis could strengthen the paper by providing a solid foundation for the proposed method's expected performance improvements.

### Questions
None

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The TULIP model enhances CLIP's capability to process long captions by replacing fixed positional embeddings with relative positional encodings, extending the model's inherent context window beyond the 77 token limit. This approach is shown to improve performance on cross modal retrieval and text to image generation tasks. The TULIP training method is 2 stage - relative position distillation from the original CLIP model and finetuning to handle longer captions. Benchmark tests demonstrate TULIP's superior performance in long-caption scenarios. The paper also introduces a new evaluation benchmark, Long-DCI, to better assess long-caption retrieval tasks.

### Strengths
- Significant improvements across cross-modal retrieval and text-to-image generation
- The introduction of a benchmark for long captions is a step towards better evaluation of other research works in this domain
- The innovative approach with relative captioning and distillation has shown improved performance
- The paper writing is easy to follow

### Weaknesses
 - Switching from absolute to relative positional encodings does improve flexibility with token length but can also introduce challenges in retaining fine-grained positional relationships in shorter contexts
- No specific details about the human annotators
- Needed a more qualitative comparison of how the new approach led to better performance in shorter context
- While CLIP possesses excellent zero-shot capabilities, it suffers from certain limitations in perceptual understanding. A discussion on TULIPs limitations in perceptual understanding would boost the presentation of the proposed approach

### Questions
1) How does the new model affect the compositionality of text inputs as dicussed here? https://aclanthology.org/2023.emnlp-main.301.pdf
2) What do you attribute the improved performance in a shorter context to? In Table 2, TULIP performs a lot better than CLIP.
3) Why are the values in Table 4 lower than those in Tables 1 or 3? If I missed something, can you clarify the caption to avoid confusion?

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
The authors propose TULIP, a method that allows for extending the capabilities of CLIP beyond the 77 token limit that is often used when training such models. The authors demonstrate that their method improves performance of CLIP trained models, on both traditional image-text retrieval tasks, as well as long-context tasks (one of which is proposed by the authors themselves).

### Strengths
- The paper examines the quality of CLIP models in the setting of long text descriptions of images. This setting is of interest to the community - as the context of models grows, the ability to retain information from the entire caption decreases as well, and trying to remedy this is an interesting problem.

- The paper is also clear and easy to understand. I did not have any issues understanding the method presented, or any other part of the paper.

- I also believe that the inclusion of the Long-DCI evaluation dataset is an important contribution to the community. Having benchmark specifically for images with long context captions is extremely important in the advancement of this field.

### Weaknesses
 - While the method itself appears useful, I am slightly worried about its novelty. At the end of the day, the model still requires training with longer contexts, so it is not immediately clear to me how different the method is from prior work. I believe that elaborating a bit more on which part of the method proposed by the authors provides the most benefit over prior work such as Long-CLIP would alleviate this concern.

- The paper has an important limitation, in that the setting considered is only CLIP-style models, and not autoregressively trained ones. The latters tend to have much larger context length than the ones considered in this paper. While I understand that direct comparison between the two may not be possible/ideal, having the method being applied to this category of models would greatly strengthen the paper.

- I would also be grateful if the authors could perform evaluation on a task based on the DOCCI dataset [A], which has the same stated goal as the proposed Long-DCI one.

- The experimental evaluation on image generation in Section 4.2 is qualitative rather than quantitative. I believe that the authors could greatly strengthen the conclusions of the paper by evaluating the generated images in a more principled manner (for example, by performing a human preference study on the generated images).

### Questions
I would be grateful if, in addition to the points I raised above, the authors could elaborate on the amount of data with long context is needed to train the student model with TULIP, in order for it to perform well on long contexts.

### Soundness
3

### Presentation
3

### Contribution
2

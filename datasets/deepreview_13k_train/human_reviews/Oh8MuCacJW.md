# Towards Unified Human Motion-Language Understanding via Sparse Interpretable Characterization

- Decision: Accept
- Scores: 8, 6, 6, 8

## Abstract
Recently, the comprehensive understanding of human motion has been a prominent area of research due to its critical importance in many fields. However, existing methods often prioritize specific downstream tasks and roughly align text and motion features within a CLIP-like framework. This results in a lack of rich semantic information which restricts a more profound comprehension of human motions, ultimately leading to unsatisfactory performance.
Therefore, we propose a novel motion-language representation paradigm to enhance the interpretability of motion representations by constructing a universal motion-language space, where both motion and text features are concretely lexicalized, ensuring that each element of features carries specific semantic meaning.
Specifically, we introduce a multi-phase strategy mainly comprising Lexical Bottlenecked Masked Language Modeling to enhance the language model's focus on high-entropy words crucial for motion semantics, Contrastive Masked Motion Modeling to strengthen motion feature extraction by capturing spatiotemporal dynamics directly from skeletal motion, Lexical Bottlenecked Masked Motion Modeling to enable the motion model to capture the underlying semantic features of motion for improved cross-modal understanding, and Lexical Contrastive Motion-Language Pretraining to align motion and text lexicon representations, thereby ensuring enhanced cross-modal coherence.
Comprehensive analyses and extensive experiments across multiple public datasets demonstrate that our model achieves state-of-the-art performance across various tasks and scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The main idea of the paper is to address the limitations of existing methods in comprehending human motion by proposing a new motion-language representation paradigm. It introduces a novel method aimed at enhancing the interpretability of motion representations, where a universal motion-language space is proposed to lexicalize and align both motion and text features. In practice,  a multi-phase training strategy, which includes various modeling schemes, is proposed to optimize the motion-language space. Through comprehensive analysis and extensive experiments across multiple public datasets, the proposed model demonstrates state-of-the-art performance in various tasks and scenarios.

### Strengths
1. The proposed representation uses a unified motion-language space, effectively capturing and aligning complex motion and textual information. It allows for an efficient and semantically rich reconstruction of human motions, as demonstrated through experimental results.
 
2. The model design ensures that both motion and text features are concretely lexicalized, providing a clear and interpretable mapping between the elements of the features and their specific semantic meanings

3. A unified multi-phase training strategy is proposed to optimize the motion-language space.

4. The paper is well-written and presents its main ideas, making it accessible to readers and facilitating a deep understanding of the proposed methodology and its applications to motion understanding.

### Weaknesses
 1. Some ablation studies about the motivation behind the proposed lexical representation are still required. The authors emphasize that some existing language representations are not effective in aligning semantic keywords essential for human comprehension. Is this related to the representation ability of the text encoder? If a more powerful text encoder, such as T5-XXL, were used, would the design of a lexical representation still be necessary? Verifying that even a strong text encoder struggles to align with certain motions would be crucial for validating the motivation behind the proposed scheme.
 
2. Some implementation details are still required. For example, it is better to provide more detailed descriptions of how the Lexical Disentanglement Head transforms dense motion and text embeddings into sparse lexical representations, rather than just citing a reference. This additional information would help in better understanding and replicating the proposed method.

3. Although the authors have already validated the effectiveness of the proposed representation learning method on retrieval and captioning tasks, I still think it is essential to design experiments to verify its performance on text2motion generation tasks. As the input of text2motion, language can be more flexible and imaginative. If the motion generation can produce reasonable motions from flexible and creative language descriptions, such as "wave the hands and jump in an S-shaped path," it would provide stronger evidence for the effectiveness of the lexical vocabulary space.

### Questions
1. From the motion captioning results presented in Appendix A.0.4, the generated captions appear to be nearly identical to the GT, raising concerns about potential overfitting. It would be beneficial if the authors could test more zero-shot examples to further validate the model's generalization capabilities. For instance, taking a sample from a different dataset, such as Motion-X[a], and evaluating the model's performance could provide additional insights into its robustness and versatility.

2. In line 81, the connotation of this LexMLM appears to be incorrectly stated and is inconsistent with the content in the abstract.

[a] Motion-X: A Large-scale 3D Expressive Whole-body Human Motion Dataset

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces the lexical representation paradigm to the motion and language domain, where both the motion and language are mapped into a shared vocabulary space to enhance the interpretability of motion representations. A novel multi-phase pre-training framework is proposed to learned aligned, semantically correct sparse lexicon representation for both language and motion modalities. Comprehensive experiments show that the model achieves state-of-the-art performance across various tasks and scenarios.

### Strengths
1. Introducing the lexical representation paradigm to the text-motion domain is novel;
2. Experimental results show remarkable improvements over baseline methods;
3. The paper is well written and easy to follow.

### Weaknesses
1. The lexical representation of motion and text is trained on small datasets, such as HumanML3D and KIT-ML. Are these datasets enough to learn good lexical representations? Generalization experiments are desired to show the robustness and effectiveness of the learned representation.
2. Interpretability of motion representation: From the visualization results in Figure 5, it seems that there exist some meaningless words in the word cloud visualization result. Does that mean that the representation is not compact or noisy?
3. In Figure 2, the caption of the four modules is out of order.

### Questions
Please refer to the weaknesses for my main concerns.

### Soundness
3

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
4

### Summary
This paper proposed a new method to better align text and motion via lexical representation contrastive learning. To address the problem of semantic deficiency, rough alignment between dense text and motion, etc., the authors proposed several new methods, i.e., LexMLM, CMMM, LexMMM, and LexCMLP to build a new pipeline. On several tasks and benchmarks, the proposed method performed well and verified the effectiveness of the proposed alignment algorithm.

### Strengths
+ The motivation of this paper is sound and non-trivial, the alignment of motion and text is vital for better joint representation learning of human motion and language.

+ The adopted methods make sense and show decent performance on widely used benchmarks and tasks.

+ Fig 5 shows well visualization.

### Weaknesses
 - Need more discussions to better clarify the method, e.g., does the proposed alignment paradigm generate uneven semantic density within the joint feature space? What is the relation of different terms? How to understand the overlap between words and synonyms (verbs)?

- Some presentation details:

-- Fig 1: please add the variables of features in the alignment part.

-- What is the detailed implementation of the visualization of lexical representation?

-- Fig 2: hard to follow, please add more main text-figure corresponses, to help the readers to understand the detailed methodology.

- Fig 3: fonts are too small.

- Fig 6: hard to distinguish the sequential motions, there is too much overlap. Please use more frames or a larger interval.

- Fig 7: fonts are too small.

- Fig 8: please add more captions to clarify the comparison and details, e.g., what do the red fonts mean?

### Questions
Some typos:

- L148: pre-trained language models**space**(PLMs) 

- L192: f a language model head**space**(LM-Head)

### Soundness
3

### Presentation
2

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
This paper presents a novel human motion-language pre-training framework that leverages lexical representation to enhance the interpretability of motion representations. The authors propose a multi-phase training strategy, including Lexical Bottlenecked Masked Language Modeling (LexMLM), Contrastive Masked Motion Modeling (CMMM), Lexical Bottlenecked Masked Motion Modeling (LexMMM), and Lexical Contrastive Motion-Language Pretraining (LexCMLP). The framework aims to align motion and text within a shared lexical vocabulary space, thereby improving the understanding of human motion. The authors demonstrate the effectiveness of their model through comprehensive experiments on multiple public datasets, showing state-of-the-art performance across various tasks and scenarios.

### Strengths
1. The paper is well-organized and easy to follow.
2. The paper introduces a pioneering approach to human motion-language understanding by creating a unified motion-language space that enhances interpretability through lexical representation. The proposed framework align both motion and text within a shared lexical vocabulary space, which can be trained by a multi-phase training strategy.
3. The authors have conducted extensive experiments and provided thorough analyses. The model achieves state-of-the-art results across multiple benchmarks, indicating the effectiveness of the proposed approach.
4. The proposed method enjoys better interpretability compared to existing method, which is further validated by the provided qualitative results.

### Weaknesses
1. Complexity of the Model: The multi-phase training strategy, while effective, may be overly complex and could potentially hinder reproducibility for researchers with limited resources. The authors could provide more details on the computational consumption for training the model compared to existing works. Specifically, the paper lacks a detailed breakdown of the computational resources required for each phase of the training process, such as GPU memory usage, training time per epoch, and the number of parameters for each sub-network. This information is crucial for other researchers to assess the feasibility of replicating the results.
2. One of the primary applications for motion-language pretraining is the text-to-motion generation task. What are the prospects of applying the proposed lexical-based method to this task?

### Questions
None

### Soundness
3

### Presentation
3

### Contribution
3

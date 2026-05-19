### Summary

This paper proposes OmniSep, a framework for omni-modal sound separation that can isolate clean soundtracks based on queries from various modalities, including text, images, and audio. The key contributions include the Query-Mixup strategy for optimizing multiple modalities, the introduction of negative queries for sound manipulation, and the Query-Aug method for open-vocabulary sound separation. The model achieves state-of-the-art performance across different sound separation tasks on multiple datasets.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. OmniSep is a unified framework that can handle sound separation tasks with queries from different modalities, including text, images, and audio. This is a significant advancement over previous methods that were limited to single-modal queries.
2. The introduction of negative queries allows for the retention or removal of specific sounds, enhancing the flexibility and control of the sound separation process.
3. The Query-Aug method enables open-vocabulary sound separation, allowing the model to handle unrestricted natural language queries. This is a crucial step towards making sound separation models more practical and versatile.

### Weaknesses

#### Some Related Works


#### comment

1. The paper mentions that the model is trained on the VGGSOUND and MUSIC datasets, which may not fully represent all real-world audio events. This could limit the model's ability to generalize to unseen sounds or scenarios. Specifically, the datasets may lack the diversity of acoustic environments, sound sources, and recording conditions found in real-world settings, potentially leading to performance degradation when the model encounters novel audio inputs. The limited representation of certain sound categories, such as environmental sounds or speech in noisy environments, could further impact the model's robustness.
2. The reliance on ImageBind as the Query-Net means that the performance of OmniSep is inherently tied to the capabilities of ImageBind. Any limitations or biases in ImageBind could propagate to OmniSep. For example, if ImageBind struggles with certain types of images or text descriptions, the corresponding sound separation performance might be negatively affected. Furthermore, the fixed nature of the pre-trained ImageBind model prevents the model from adapting to the specific nuances of the sound separation task, potentially limiting its overall performance.
3. The Query-Aug method relies on retrieving similar in-domain class queries, which might not always be effective for truly out-of-domain or novel queries. The effectiveness of this approach depends on the quality and coverage of the query set. If the query set does not adequately represent the diversity of possible sound descriptions, the model's ability to generalize to unseen queries will be limited. Additionally, the similarity metric used for retrieval might not capture all relevant semantic relationships between queries, leading to suboptimal query augmentation.

### Suggestions

To address the limitations in dataset diversity, future work should explore incorporating more varied and realistic audio data into the training process. This could involve curating datasets that include a wider range of acoustic environments, sound sources, and recording conditions. Specifically, the inclusion of datasets with environmental sounds, speech in noisy environments, and music from diverse genres would be beneficial. Furthermore, data augmentation techniques could be employed to artificially increase the diversity of the training data, such as by adding noise, reverberation, or pitch shifts to the existing audio samples. This would help the model become more robust to variations in the input data and improve its generalization capabilities. Additionally, exploring unsupervised or self-supervised learning techniques could allow the model to learn from unlabeled data, further enhancing its ability to handle real-world audio scenarios.

To mitigate the reliance on ImageBind, future research should investigate alternative query networks that are specifically designed for sound separation tasks. This could involve training a query network from scratch using a large dataset of audio queries and their corresponding sound separations. Alternatively, a lightweight adaptation of ImageBind could be explored, where the pre-trained weights are fine-tuned on the sound separation task. This would allow the model to leverage the general knowledge captured by ImageBind while also adapting to the specific requirements of the task. Furthermore, exploring different architectures for the query network, such as transformers or graph neural networks, could lead to improved performance and flexibility. The choice of query network should be guided by the specific requirements of the sound separation task and the characteristics of the input queries.

To improve the effectiveness of the Query-Aug method, future work should focus on developing more robust and comprehensive query sets. This could involve incorporating a wider range of text descriptions, including both common and rare sound categories, as well as more abstract and nuanced descriptions. Additionally, exploring different similarity metrics for query retrieval could lead to more accurate and relevant query augmentation. For example, using a metric that captures semantic similarity rather than just lexical similarity could improve the model's ability to generalize to unseen queries. Furthermore, the Query-Aug method could be extended to incorporate other modalities, such as images or audio, to provide a more comprehensive representation of the query. This would allow the model to leverage the strengths of different modalities and improve its ability to handle complex and diverse queries.

### Questions

1. How does the model perform on sound separation tasks involving sounds or scenarios not well-represented in the VGGSOUND and MUSIC datasets? Are there any specific limitations observed in such cases?
2. What are the potential challenges and solutions for scaling up the training data for OmniSep? How can the model be made more generalizable to a wider range of real-world audio events?
3. How does the performance of OmniSep compare to other state-of-the-art sound separation models on a broader range of datasets and tasks? Are there any specific areas where OmniSep excels or falls short?

### Rating

6

### Confidence

3

**********

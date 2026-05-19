### Summary

This paper proposed a sound separation model that can take queries from various modalities, including text, image, and audio. The authors also introduce additional techniques, such as negative queries and query-augment, to further improve the performance and flexibility of the model. The experiments on MUSIC and VGGSOUND datasets demonstrate the effectiveness of the proposed method in text-, image-, and audio-queried sound separation tasks.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The idea of handling multiple query modalities in sound separation is interesting and promising. 
2. The techniques of negative queries and query-augment are simple and effective.

### Weaknesses

#### Some Related Works


#### comment

1. The technique contributions of this paper are limited. The model is based on ImageBind, and the main contribution is the query-mixup technique, which is a simple linear combination of different modal queries. The query-augment is just a similarity search within the existing query set.
2. The model is trained on VGGSOUND and MUSIC datasets, but they only cover a small fraction of real-world sounds. How to scale this model to handle more general sound separation tasks remains a challenge.
3. The evaluation is not comprehensive. The paper only reports SDR metrics, but it is unclear how the separation quality is in terms of perceptual quality. The SDR metric can sometimes be misleading, as it might prioritize the removal of interference over the preservation of the target sound, leading to a high SDR but poor perceptual quality. The paper lacks a more detailed analysis of the separation performance, such as examining the model's ability to separate overlapping sounds or handle complex acoustic environments.

### Suggestions

The paper's core contribution, the query-mixup technique, while simple, could benefit from a more thorough investigation into its limitations and potential failure modes. For example, it would be valuable to explore how the linear combination of query features affects the model's ability to handle complex queries or those with conflicting information. The authors should also consider exploring more sophisticated methods for combining multi-modal queries, such as attention mechanisms or learned fusion techniques, which might offer better performance and flexibility. Furthermore, the negative query approach, while effective, could be enhanced by incorporating more nuanced negative examples, such as sounds that are semantically similar but acoustically distinct from the interference, rather than just random sounds from the dataset. This could lead to a more robust and selective sound separation model.

To address the limitations in the evaluation, the authors should include a more comprehensive set of metrics that capture both the objective and perceptual quality of the separated sounds. In addition to SDR, metrics such as perceptual evaluation of speech quality (PESQ) or short-time objective intelligibility (STOI) could provide a more complete picture of the model's performance. Furthermore, the authors should conduct a more detailed analysis of the model's behavior under different conditions, such as varying levels of interference, different types of sounds, and complex acoustic environments. This could involve visualizing the attention maps of the model or analyzing the spectrograms of the separated sounds to understand how the model is making its decisions. The inclusion of qualitative examples, such as audio samples, would also be beneficial for assessing the perceptual quality of the separation results.

Finally, the paper should address the scalability of the model to more general sound separation tasks. The current reliance on the VGGSOUND and MUSIC datasets limits the model's applicability to real-world scenarios. The authors should explore methods for incorporating more diverse and uncurated data into the training process, such as using weakly labeled data or unsupervised learning techniques. Furthermore, the authors should investigate the model's ability to generalize to unseen sound categories or acoustic environments. This could involve evaluating the model on a more diverse set of datasets or conducting experiments in real-world settings. The authors should also discuss the computational cost of training and deploying the model, as well as potential strategies for reducing the cost and improving the efficiency.

### Questions

1. How does the proposed method perform on the real-world sound separation task? For example, how does it separate the speech of a specific person out from a noisy environment?
2. How does the model handle the queries from different modalities but with conflicting information?
3. What are the potential benefits and challenges of scaling up the training data for this model?

### Rating

5

### Confidence

3

**********

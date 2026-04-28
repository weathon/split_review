# Dynamic Adapter Merging for Continual Video Question-Answering Learning

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 6, 5

## Abstract
We present a parameter-efficient method for continual video question-answering (VidQA) learning. Our method, named DAM, uses $\textbf{D}$ynamic $\textbf{A}$dapter $\textbf{M}$erging to address the issues of (i) catastrophic forgetting, (ii) the costly retraining of large VidQA models on continually shifting distribution of training data, and (iii) handling inputs from an unknown domain during test-time inference. Given a set of different VidQA datasets, we sequentially train domain-specific adapters for each VidQA dataset while freezing the parameters of a large pretrained video-language backbone. During inference, given a video-question sample from an unknown domain, our method first uses a non-parametric video-language router function to compute a probability for each domain-specific adapter, reflecting how relevant that adapter is to the current video-question input instance. Afterward, to exploit beneficial cross-domain cues and reduce the impact of potentially incorrect router predictions, we dynamically merge the parameters of several highest-scoring adapters for the final VidQA prediction. Despite the simplicity of our approach, we demonstrate that it works well on continually streaming VidQA datasets across $6$ different domains. In particular, our model outperforms prior prompt-based continual learning approaches by 9.1% while exhibiting 1.9% less forgetting. The code and pretrained models will be publicly released.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes the Dynamic Adapter Merging (DAM) for video question-answering under Domain-Incremental Learning scenario, which is a rehearsal-free approach. DAM leverages the fusion of parameters from multiple adapters to mitigate the interference of erroneous predictions, thereby enhancing the performance of the model.

### Strengths
The paper is well organized and the proposed method is verified through many experimental results.
The DAM is straightforward and easy to follow.

### Weaknesses
The paper provides a detailed elaboration to the framework of the model. However, the authors do not explicitly mention the loss function used during the training of adapters.

The contributions of the paper may be insufficient.  Although the Introduction section mentions four contributions, these contributions revolve primarily around one aspect, i.e. related to combining domain-specific adapter learning and model merging techniques.

The proposed method may lack innovation as the idea of model merging techniques in deep/machine learning is frequently used. The non-parametric router function is simply based on cosine similarity with no improvements. However, the application of such a concept to Continual Learning does introduce somewhat novelty.

### Questions
Can such ideas bring about desired performance improvements when extended to class-incremental learning and task-incremental learning scenarios? Can the author incorporate some results to demonstrate the generalizability of the idea in the context of continual learning?

How were the experimental results in the article obtained? Were multiple runs conducted to obtain an average, or was only a single experiment performed? I would like to know the stability of the proposed method.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The article presents to address continual video question-answering (VidQA) learning with a simple framework, named DAM. Through sequentially training domain-specific adapters and leveraging a video-language router to merge the adapters for inference, DAM outperforms prior methods by 9.1% while forgetting less by 1.9%.

### Strengths
1) The paper assumes that this is the first attempt to address the issue of continual learning in VideoQA.
2) Comprehensive Ablation Studies: The article includes sufficient and in-depth set of ablation experiments, which provide a thorough understanding of the method's performance and help identify critical components.
3) Clear Method Framework: The method's framework is straightforward and well-explained, making it accessible to readers and researchers in the field.

### Weaknesses
1) Limited Dataset Diversity: The article's experimental use of six datasets with relatively small differences between them, especially MSVD and MSR-VTT, raises concerns about the method's domain adaptation and continual learning capabilities. The use of internet-sourced videos in the datasets does not fully explore the potential challenges posed by more diverse datasets, such as those collected in virtual environments (e.g., Env-QA[1]), traffic scenarios (e.g., TrafficQA[2]), or indoor human activities (e.g., AGQA[3]). What’s more, the out-of-date issue proposed in Figure 1 hasn’t been evaluated, also.
2) While the article demonstrates the effectiveness of the adapter and router, their simple design might not generalize well to more challenging datasets. The reviewer has doubts about their applicability in more complex scenarios.
3) The article does not provide a fair comparison with backbone models under few-shot learning setting. A direct comparison between in-context learning using FrozenBiLM and the proposed approach could offer a more comprehensive evaluation.
4) The article does not provide sufficient evidence of severe catastrophic forgetting in current large models.

### Questions
1) The article does not provide sufficient evidence of severe catastrophic forgetting in current large models.
2) It is worth discussing whether there are unique challenges related to continual learning in the domain of VideoQA.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies VideoQA in a domain continual-learning setting. The task encourages VQA models that can quickly adapt to new domains/datasets while simultaneously prevent catastrophic forgetting on learned domains. To achieve the goal, the paper proposes the dynamic adapter merging (DAM) method. Given a random instance, DAM dynamically (learning-free) merges a series of domain-specific parameter adapters for answer prediction, where the adapters are continually learned across datasets of different domains. The authors conduct extensive experiments on 6 VideoQA datasets and additionally 4 ImageQA datasets to show the effectiveness of the proposed method.

### Strengths
1.	The paper conducts the first study on domain-incremental learning in VideoQA. It also presents a nice solution to benchmark the task.
2.	The DAM method is simple, easy to understand and shows strong results as well. Also, the experiments and analyses are in-depth.
3.	The paper is well-presented and easy to read.

### Weaknesses
1.	The definition of domain regarding VideoQA is not clear. The authors simply treat different datasets as different domains. This is certainly problematic and prevents detailed model analysis. For example, regarding the question type, all datasets define similar questions except for LSMDC with fill-in-blank setting.  Regarding the video type, there are instructional videos (iVQA), social videos (MSVD, MSRVTT, TGIF), movie videos (LSMDC) and activity videos. Regarding video length, all videos are short (3~15s) except for ActivityNet(3 mins). It would be better to experiment with more clarified domains instead of datasets.

2.	While the ‘dynamic merging’ design mitigates the problem of catastrophic forgetting and improves the overall performance as well, it necessitates all the learned adapters for inference. This resembles more on model ensemble versus continual learning a ‘single’ model. It is necessary to show the size of the adapters and analyze the efficiency.

3.	The authors obtain the upper-bound results by individually finetuning on target datasets. My concern is that this ‘upper-bound’ may not be the actual upper-bound for incremental-learning because of data augmentation. Moreover, the gap between DAM' results and this upper-bound results is too small to show that there is need for future efforts as a novel task setting. The authors need to find a more convincing upper-bound or just mention the current one as a reference.

4.	According to the task setting, providing more analyses /comparisons on an OOD setting (aside from Fig.3(b)) would make the experiments more sound.

### Questions
Minor:
1. Why is the performance on ActivityNet not as good as on other datasets? 

2. In Sec. 3.2, what specific model does ‘f’ refer to? 

3. Analyses of table 5, 6 should be moved from the appendix to the main text.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a dynamic adapter merging framework for domain-incremental VideoQA learning. The framework is capable of obtaining multiple domain-specific adapters and dynamically integrating different domain information through model merging techniques. Experiments results on multiple public datasets verify the effectiveness of the proposed method.

### Strengths
1.	The logic of the paper is reasonable.
2.	The experiments are relatively adequate.

### Weaknesses
The technical details of this paper are not described clearly enough, my concerns are as follows:
1.	Why do you set up N adapters for each domain instead of one?
2.	Why do you choose to insert domain-specific adapters after the self-attention and feed-forward layers, respectively? What are the considerations?
3.	What exactly is meant by the pre-trained model f in Eqn. (1)?
4.	What does the symbol k in the baselines section on page 6 refer to? I cannot find a definition in the previous text.
5.	What is the exact structure of the adapter?

### Questions
See above.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

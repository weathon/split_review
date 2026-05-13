# High-quality and controllable time series generation with diffusion in transformers

- Decision: Reject
- Scores: 6, 6, 3, 3, 3

## Abstract
Current research on time series generation frequently depends on oversimplified data and lenient evaluation methods, making it challenging to apply these models effectively in real-world scenarios. Diffusion in Transformers (DiT) has demonstrated that the traditional inductive biases in neural networks are unnecessary. This paper shows that the advantages of DiT can be extended to time series generation.  We add the attention mask and dilated causal convolution to introduce the temporal characteristic. Additionally, we introduce a novel smooth guidance policy for style control during generation, leveraging a property of the diffusion process. Furthermore, our proposed model can generate longer sequences with training in short sequences. Experimental results reveal that our variant of DiT achieves state-of-the-art performance across various data types.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents TimeDiT (Diffusion in Transformers for time series), a model designed to generate high-quality and controllable time series data by employing a Transformer-based diffusion approach. To improve on the limitations of conventional time series generation methods, the authors incorporate dilated causal convolutions and a guidance policy for style control, enhancing the Transformer’s temporal representation and understanding.

The model demonstrates scalability through its ability to generate longer sequences from relatively limited training data. Experimental results indicate that TimeDiT achieves state-of-the-art performance on several benchmarks, surpassing traditional GAN- and VAE-based models in terms of temporal fidelity and diversity in generated sequences.

- Personally, I find the application of diffusion within a Transformer framework intriguing, especially for time series data, where both structure and variability are critical. However, further discussion on the computational trade-offs involved in this model would strengthen the paper and offer valuable insights for researchers considering similar architectures in their work. It is between weak reject and weak accept to me.

### Strengths
- Enhances the model's ability to capture temporal dependencies without traditional position encoding.

- Enables smooth and flexible generation of diverse styles within time series data.

- Allows generation of sequences significantly longer than the training set, a vital feature for many real-world applications.

### Weaknesses
1. The model requires high computational resources and long training durations to converge, with the paper noting that over 100K steps are necessary for effective training. This contrasts with GAN or VAE models that converge faster, raising potential accessibility issues for those without extensive computational infrastructure. Furthermore, the paper does not provide a detailed analysis of the computational complexity of the proposed architecture, making it difficult to assess its scalability beyond the reported experiments. A breakdown of the FLOPs and memory requirements for different sequence lengths and model sizes would be beneficial.

2. The authors adopt classifier-based metrics for evaluation, but these are highly contingent on classifier accuracy. The classifier imperfections could impact fidelity and diversity assessments, potentially misleading users in applications where these evaluations are critical. Specifically, the paper does not explore the sensitivity of the FID scores to variations in classifier performance, such as using classifiers trained on different datasets or with varying architectures. This lack of robustness analysis raises concerns about the reliability of the reported results.

3. The authors note a lack of unified time series datasets, which hinders consistent comparisons. Without a standardized benchmark, it becomes challenging to generalize the model’s performance to broader datasets or applications outside the selected ones. The absence of a rigorous comparison against established time series generation benchmarks makes it difficult to position the proposed model within the broader landscape of time series research. This limits the ability to assess the true contribution of the method.

4. While the model performs well on cleaner time series, it has a tendency to amplify noise in high-density datasets. This noise issue is not fully addressed by the dilated convolution approach, and it raises questions about the model's performance on heavily fluctuating real-world data. There are also some theoretical works [e.g., A] on the population density estimation and error bounds, the author(s) may consider to add it for future discussion. The paper lacks a detailed analysis of the noise characteristics in the generated time series and how they compare to the noise profiles in the training data. A spectral analysis of the noise components would be useful to understand the limitations of the model.

5. Diffusion models are known for long sampling times, and TimeDiT is no exception. While the model provides high-quality outputs, the extended sampling time could be a bottleneck in time-sensitive applications where fast data generation is needed. The paper does not provide a detailed comparison of the sampling times with other generative models, such as GANs or autoregressive models, which makes it difficult to assess the practical implications of this limitation.

### Questions
1. Given the classifier dependency, how can the metrics be adapted to reduce classifier bias, especially for more diverse or noisy time series data?

2. The model’s optimal performance is achieved under specific hyperparameters. Could the authors clarify the robustness of TimeDiT to changes in parameters such as learning rate, layer depth, and batch size, and suggest guidelines for optimal parameter tuning?

3. Many real-world applications involve non-stationary data, such as traffic patterns and stock prices. Has TimeDiT been tested on non-stationary data, and if not, what adaptations might be needed?

4. Given the autoregressive advantage of Transformers in other domains, can the authors compare TimeDiT’s long-sequence generation capacity to that of an autoregressive Transformer-based method?

5. The model has been evaluated on driving, stock, weather, and solar data. Could the authors discuss TimeDiT’s transferability to unrelated domains like medical or social time series data?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper presents TimeDiT, a model that leverages Diffusion Transformers (DiT) for generating high-quality, controllable time series data. By incorporating dilated causal convolution and an innovative smooth guidance policy, the model extends DiT to handle complex time series. Experimental results indicate that TimeDiT achieves state-of-the-art performance across several metrics and is able to generate longer sequences from short training sequences. Key contributions include a novel diffusion-based time series generation framework, a method for fusing features during diffusion, and the application of classifier-based metrics to evaluate model quality and diversity.

### Strengths
The model addresses an important gap in time series generation by **adapting diffusion models**, which have primarily been used in image generation, to handle temporal data. The incorporation of temporal characteristics through dilated causal convolution is innovative, making TimeDiT a pioneering approach in this space.

The **experimental** design is rigorous, comparing TimeDiT against several benchmarks on multiple datasets with varied characteristics. The use of classifier-based metrics enhances the evaluation's robustness, and the inclusion of both univariate and multivariate tasks demonstrates the model’s adaptability.

The paper is generally clear and well-structured, with **detailed explanations** of the model design and experimental procedures. 
The model’s ability to generate longer sequences and control the output’s features makes it significant for applications in fields that rely on time series data. Additionally, TimeDiT's scaling properties and ability to capture diverse temporal patterns position it as a meaningful contribution to the field.

### Weaknesses
The model’s performance with low-dimensional datasets is promising, but **high-dimensional time series** data may pose additional challenges, especially in cases where dependencies across dimensions are intricate. There is limited discussion on how TimeDiT would perform in such complex multivariate contexts. Specifically, the paper lacks a thorough analysis of how the dilated causal convolutions handle inter-dimensional dependencies, and whether the model can effectively capture complex relationships between different time series within a high-dimensional dataset. For instance, in scenarios with numerous correlated time series, the model's ability to distinguish and generate these dependencies accurately is not well-explored. 

A notable limitation is the high computational cost of TimeDiT due to the diffusion process and the need for long training times to achieve high-quality outputs. The paper does not examine the scalability of the method with **larger datasets**. This includes a lack of analysis on how the training time scales with increasing dataset size and dimensionality, and whether the model's performance degrades with larger datasets. The paper also does not provide any information on the memory requirements of the model, which is crucial for practical applications with large datasets. 

Although the authors present results on generating longer sequences, the paper lacks detailed experiments and evaluations on **training with the same longer sequences**. This gap makes it difficult to assess the model's accuracy on longer time series. Furthermore, the lack of a direct **comparison with state-of-the-art methods** trained using longer time series makes the model's performance in this regard unclear. The paper does not explore how the model's performance changes when trained on longer sequences, and whether the model is able to capture long-range dependencies effectively. The absence of a comparison with other models trained on similar long sequences makes it difficult to benchmark the model's performance in this specific scenario.

### Questions
Please refer to Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work proposes TimeDiT, a diffusion transformer model that models temporal sequences. It is equipped with causal attention mask, dilated causal convolution and could generate a sequence longer than the training sequence in inference. It is also demonstrated that it's possible to exchange the condition during the backward process of the diffusion. The main evaluation is based on several metrics(IS,FID, etc.) on multiple datasets(solar, stock, weather, VED, Argoverse2). The proposed TimeDiT performs the best in the main evaluation. There are also other extended experiments demonstrating long sequence generation, smooth controllability and the ablation of several design choices in network architecture.

### Strengths
This work adapts DiT to model several temporal sequences, proposed several techniques(the use of zero-initialized AdaLN, smooth prior, causal dilated convolution) to improve the prediction/generation quality and described some issues observed when applying DiT to these datasets. Specifically, replacing time positional embedding with dilated convolution could be helpful in some applications.

### Weaknesses
Unfortunately, many detail of on the implementation and experiment is missing in the main text, and not even included in appendices. Also, besides the main evaluation(Table 1), the rest of experiments cannot justify what they aimed to claim, some of them have no numerical results at all. Also, the cause of "noise" without using dilated convolution in DiT is not well investigated. Although removing positional embedding and replace it with dilated convolution improved the evaluation metrics, it is not known if such treatment is generalizable.

- Soft prior: There's no theoretical or sufficient heuristic evidence to say that the unwanted noise is caused by masked attention. In Figure 2(a), the observation is merely an example. It cannot really verify whether "noise" and "number of peaks" will be increased in general due to the temporal masking on attention. Although soft prior can mitigate this phenomenon, it could create another side effect that's not easily observable. For example. if there's no external label to indicate the time, the model will not be able to reflect the long-term temporal distribution change, for example, the trend of global warming (although it can be resolved by using "year" as a condition in generation).

 - It's already reported in DDPM's paper that predicting noise leads to better quality than predicting x_0. However, to argue that predicting variance is useful, it needs theoretical/heuristic results.

- Adding dilated causal convolution can encourage the model to attend more on modulated past information. However, this is also achievable by standard attention with more layers. Is there any ablation to show this is more efficient than adding extra attention layers, MLPs, or other methods?

- The experiment on long sequence generation is not convincing. First, a length of 1200 is not really long considering much longer sequences has been tackled in LMs, images and sounds. Second, there's no result showing that the long sequence generated by the model is reflecting the long-term trend in the original data.

- The design of the classifier used for IS/FID evaluation is not explained at all. Although in Appendix there is an experiment showing that a similar trend on relative quality can be observed when using 5 classifiers, most of important details are missing. For example, the NN architecture of these classifiers, how the classification tasks are designed, and how are they trained, etc. Above all, testing with only 2-5 classifier is not convincing, what if all of them missed some important property of the data?

- The experiment on feature-fused generation (replacing condition in the middle of backward diffusion) does not have numerical result. How does it justifies the usefulness of condition fuse? In appendix C2, the description regarding Fig 12-13 is also not convincing. Few selected examples without quantitive analysis cannot justify the whether the "controllable guidance" is working or not.

- What's the significance of combining several arbitrary datasets for multi-variate generation, if they do not have dependency with each other?

- Diffwave is a work in 2020, it's hard to say it is "most advanced". Furthermore, there are several models[1,2] developed for Argoverse dataset, it would be good to compare with these models using the same evaluation protocol.
[1] B. Varadarajan, A. Hefny, A. Srivastava, K. S. Refaat, N. Nayakanti, A. Cornman, K. Chen, B. Douillard, C. P. Lam, D. Anguelov, et al., “Multipath++: Efficient information fusion and trajectory aggregation for behavior prediction,” in 2022 International Conference on Robotics and Automation (ICRA).   IEEE, 2022, pp. 7814–7821.
[2] Y. Liu, J. Zhang, L. Fang, Q. Jiang, and B. Zhou, “Multimodal motion prediction with stacked transformers,” in Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2021, pp. 7577–7586.

- Some of the metrics are not well explained. For example, in Table 2 and 6, it seems recall and precision are evaluated based on some events defined for each datasets, but they're not explained clearly. This is the same for "discriminative score" and "predictive score" in Table 1.

- In Fig 7-11, TimeDiT's generated distribution under t-SNE and PCA projection is sometimes more distinct than DiffTS and TimeGAN. This contradicts to the results shown in the main text (Table 1).

- In Appendix C4, Fig 15-18, capable of generating 1D curves that looks similar to human does not mean the model can really model the data correctly based on events and conditions. Again, numerical result is needed.

Minor errors and concerns:
- Did not explicitly define what is "DiffTS". Although it can be inferred that it's "Diffusion-ts" mentioned in related works, still this impacts the readability.
- Missing dash, "-", in dataset URL, it should be "https://www.bgc-jena.mpg.de/wetter/weather_data.html". Also, datasets should be referenced in the main text.
- Appendix A referred in main text is actually Appendix B.
- L714: Missing right ")".

### Questions
- Following the concern on soft prior, it would be good to have previous works or experiments to justify that positional encoding is the cause of the noise. It can be argued that for some data, its context can be entirely dependent on the past context, and therefore using absolute positional encoding is not reasonable. Just to mention, there's another work that can replace absolute time positional encoding but also support long sequence generation at inference time, for example, the rotary position embedding[1], which has shown its effectiveness in other tasks.  
[1] RoFormer: Enhanced Transformer with Rotary Position Embedding, Jianlin Su, Yu Lu, Shengfeng Pan, Ahmed Murtadha, Bo Wen, Yunfeng Liu, https://arxiv.org/abs/2104.09864 

Some other questions:
- L66: what does the "scaling properties" mean here? Although later in Figure 4 it is said that TimeDiT's "scaling properties" is the reason why it outperform DiffTS in the later stage of training, but I wonder what is the actual definition of this?

- The explanation of "point-wise layer" is unclear. It is reasonable that it must be something independent of sequence length, but isn't that any convolutional layer with proper padding could also fit the purpose?

- Although dilated convolution layer allows parallelization by the factor of dilation size, but unless the attention is also masked in a dilated manner, the parallelized evaluation will not have the same result to the sequential evaluation. How this is tackled in this work?

- In L341, since the classification task used for IS score in this work is not disclosed, how could a reader know such score difference is due to the loss of a class? Can you explain us how the IS classifier is designed?

- L347: Why smoother is always better? I believe it is data dependent. For example, speech data is non-smooth in this sense. 

- L370: Where I can find the condition generation setup? How could we know if the result is good or bad if no other subjects in comparison?

- L474: Here it claims the proposed model outperforms the baseline, but there's no baseline for comparison in Table 5? In other modalities such as audio or music generation, generating much longer sample at inference time while maintaining a reasonable segment-wise FID is not a problem. Also, how does the model used in FID evaluation is designed?? usually the model has a fixed context length, how do you configure this for fair evaluation on longer outputs?

- L493: For fair comparison, does the 1D CNN has the some context length as DCC?

- L693 What's the term "dimension" mean here ?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper adapts the DiT model to the time series domain with diluted casual convolutions. Furthermore, it promotes a new technique to smoothly control signal conditioning for time series generation. The paper offers a task of class conditioning and presents the method's capability in this task while also showing results on other unconditional generation tasks, including long-time series generation.

### Strengths
- The integration of causal dilated convolutions into the DiT for time series analysis is compelling, and the smooth guiding technique has demonstrated its effectiveness.  
- I believe the author’s proposed task of class conditional generation is significant, and the ability to generate longer sequences is an important characteristic of any model and an interesting task.  
- The model's efficiency compared to other diffusion models has been empirically validated.

### Weaknesses
 - **Unconditional Generation Benchmark**  
  - The benchmark lacks state-of-the-art methods like [1], which demonstrate significantly better results than those presented, leaving the claim of being state-of-the-art unsubstantiated. Specifically, the absence of comparison with models using Koopman operator theory, which have shown superior performance in capturing complex temporal dependencies, is a significant oversight. The benchmark also lacks datasets comparison such as MuJoCo and Energy (can be seen in Diffusion-TS benchmark), which are standard datasets in time series generation and would provide a more comprehensive evaluation.

- **Class Conditional Generation Benchmark**  
  - The evaluation protocol is not clearly defined in the main text nor the appendix. It's unclear how the class conditional generation is evaluated beyond basic metrics, such as accuracy and recall, which might not fully capture the quality of the generated time series. There is no baseline method provided, making it impossible to assess the relative performance of the proposed method. It appears that the task has reached a saturation point, with nearly perfect scores, suggesting that either the task is too simple or the evaluation metrics are not sensitive enough to distinguish between different methods.

- The multivariate task lacks clarity, and there is a notable absence of state-of-the-art comparison models [1]. The specific architecture and training procedure for multivariate time series generation are not detailed enough, making it difficult to reproduce or understand the results. The lack of comparison with established methods for multivariate time series generation, which often employ techniques like attention mechanisms or graph neural networks, further weakens the evaluation. 
- While the generation of longer sequences is a fascinating challenge, there are no baseline methods provided, though I believe a straightforward extension of current methods is feasible, and it is currently only evaluated on a single dataset. The absence of comparisons with methods that explicitly address long-range dependencies in time series, such as those based on recurrent neural networks or transformers, makes it hard to assess the true contribution of the proposed method in this area.

### Questions
- Could the author clarify what y and y' represent in the smooth control? It is unclear how they differ in the context of conditional classes. An example would be helpful.  
- To enhance the related work section quality and keep it up to date, I recommend incorporating references to cutting-edge papers [2, 3, 4]. I emphasize that it’s not necessary to compare or include these in the benchmarks of this paper (experiments).  

[1] Generative Modeling of Regular and Irregular Time Series Data via Koopman VAEs.

[2] Utilizing Image Transforms and Diffusion Models for Generative Modeling of Short and Long Time Series.

[3] SDformer: Similarity-driven Discrete Transformer For Time Series Generation.

[4] IDE: Frequency-Inflated Conditional Diffusion Model for Extreme-Aware Time Series Generation.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a diffusion in transformer for time series generation, called timeDiT. There are a couple of architectural improvements such as dilated causal convolution to model the time-series data better. The smooth control sampling is introduced in order to fuse different categories in the diffusion steps. The experimental results are provided to show the effectiveness of the proposed approach in time-series generation tasks.

### Strengths
This paper incorporates the state-of-the-art techniques and methods proven by other domains such as image generation. Some sensible modifications are applied to make the system perform well for time-series data. A variety of time-series data is used in the experiments.

### Weaknesses
This paper should be rejected since 1) it is difficult to understand in the experiments 2) there are large gaps between the experimental results and statements derived from the results. The main arguments are listed in Questions below.

1.  4.2 Unconditional generation: It is not clear how the proposed system is configured. Does “unconditional” mean that the samples are generated with y=y’=null?
2.  4.2 Conditional generation: Similar to the above question, how the system is set up for conditional generation? What is the y and y’, and what value is tau for these experiments?
3.  Table2: What are reasons to use Precision/Recall instead of Discriminative/Predictive Scores shown in Table1? How the classifier is trained, binary or multi-class detection, what data is used to train the classifier models?
5.  Table2: It is not straightforward to compare Table1 and Table2. FID is the common metric for both tables, but other metrics are different. Even for FID, there is degradation on some dataset (e.g. Stock: 9.06 -> 9.43, Weather: 6.09 -> 7.37), how should this be interpreted?
6.  4.2 Correlation constraints on multivariate sequences: Like earlier questions, it is not clear how the system is configured (y, y’, tau, etc.) for the multivariate task.
7.  Table 4: What do FID_a and FID_b represent?
8.  4.3 Longer sequence generation: It is claimed that “extended sequences have slight distortions in small segments but outperform the baseline”. It is not agreeable that the FID drop from 3.44 (T=120) to 37.18 (1200) is considered as “slight distortion”. In addition, the baseline result cannot be found to compare.

Things to improve the paper that did not impact the score:
1.  Point-wise layer: If the layer is something new, the explanation should be made. Otherwise, some reference should be added.
2.  Figure 2(b): What is x-axis and the size of circle? What are single and mixed pattern? Some descriptions are helpful.

### Questions
1.	4.2 Unconditional generation: It is not clear how the proposed system is configured. Does “unconditional” mean that the samples are generated with y=y’=null?
2.	4.2 Conditional generation: Similar to the above question, how the system is set up for conditional generation? What is the y and y’, and what value is tau for these experiments?
3.	Table2: What are reasons to use Precision/Recall instead of Discriminative/Predictive Scores shown in Table1? How the classifier is trained, binary or multi-class detection, what data is used to train the classifier models?
5.	Table2: It is not straightforward to compare Table1 and Table2. FID is the common metric for both tables, but other metrics are different. Even for FID, there is degradation on some dataset (e.g. Stock: 9.06 -> 9.43, Weather: 6.09 -> 7.37), how should this be interpreted?
6.	4.2 Correlation constraints on multivariate sequences: Like earlier questions, it is not clear how the system is configured (y, y’, tau, etc.) for the multivariate task.
7.	Table 4: What do FID_a and FID_b represent?
8.	4.3 Longer sequence generation: It is claimed that “extended sequences have slight distortions in small segments but outperform the baseline”. It is not agreeable that the FID drop from 3.44 (T=120) to 37.18 (1200) is considered as “slight distortion”. In addition, the baseline result cannot be found to compare.

Things to improve the paper that did not impact the score:
1.	Point-wise layer: If the layer is something new, the explanation should be made. Otherwise, some reference should be added.
2.	Figure 2(b): What is x-axis and the size of circle? What are single and mixed pattern? Some descriptions are helpful.

### Soundness
2

### Presentation
3

### Contribution
2

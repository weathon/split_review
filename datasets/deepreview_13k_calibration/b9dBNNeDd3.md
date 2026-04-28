# Customize Your Visual Autoregressive Recipe with Set Autoregressive Modeling

- Decision: Reject
- Avg Score: 4.60
- Scores: 5, 5, 5, 5, 3

## Abstract
We introduce a new paradigm for AutoRegressive (AR) image generation, termed \emph{Set AutoRegressive Modeling} (SAR). SAR generalizes the conventional AR to the next-set setting, \textit{i.e.}, splitting the sequence into arbitrary sets containing multiple tokens, rather than outputting each token in a fixed raster order. To accommodate SAR, we develop a straightforward architecture termed \emph{Fully Masked Transformer}. We reveal that existing AR variants correspond to specific design choices of sequence order and output intervals within the SAR framework, with AR and Masked AR (MAR) as two extreme instances. Notably, SAR facilitates a seamless transition from AR to MAR, where intermediate states allow for training a causal model that benefits from both advantages of AR and MAR, such as few-step inference, KV cache acceleration and image editing. On the ImageNet benchmark, we carefully explore the properties of SAR by analyzing the impact of sequence order and output intervals on performance, as well as the generalization ability regarding inference order and steps. We further validate the potential of SAR by training a $900$M text-to-image model capable of synthesizing photo-realistic images with any resolution. We hope our work may inspire more exploration and application of AR-based modeling across diverse modalities.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work investigate image generation with discrete tokens. It proposes Set AutoRegressive Modeling (SAR), which can generate image tokens in arbitrary order and intervals. The authors also develop a variant of encoder-decoder Transformer named FMT to enable KV cache. Experiments on ImageNet show competitive performance and the model also shows capability in text2image generation.

### Strengths
1. The paper investigates an interesting problem to make autoregressive image generation model more efficient. 
2. The work includes standard benchmarks like ImageNet 256 and achieves competitive performance.

### Weaknesses
1. Though the work is motivated by a more flexible framework for image generation, the best performing setting is still using raster order as standard autoregressive model (table 5). This raises questions about the practical advantages of the proposed approach, as the core benefit of arbitrary order generation seems not fully realized in the best-case scenario. The experiments should better highlight the specific scenarios where the proposed method outperforms standard raster-scan approaches, rather than simply showing that it can match their performance.
2. It misses some comparison to baseline models to help understand the benefit of the proposed method. Specifically, the paper lacks a direct comparison of the proposed SAR method with Masked Autoregressive models (MAR) under the same fixed generation order. This comparison is crucial to isolate the benefits of the proposed token generation approach from the effects of different generation orders. Without this, it is difficult to determine if the performance gains are due to the specific token generation method or simply the choice of a particular generation order. Furthermore, the paper should include comparisons with other autoregressive models, not just in terms of final performance but also in terms of computational cost and inference speed.

### Questions
1. How much training/inference speed gain does KV cache give? Some benchmark with AR/MAR models would be helpful to understand the benefits of the model. 
2. What does SAR-TS mean? I may miss something, but I'm confused about how this transition state variant is built. 
3. To better show the benefit of the proposed method, it would be valuable to compare SAR with MAR with the same fixed order both on FID and inference speed. 
4. The model shows nice visualization on text2image generation. Are there any metrics to evaluate the performance over different inference settings like CLIP score?

### Soundness
4

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a Set AutoReggressive Modeling (SAR) as a new paradigm for AutoRegressive image generation. By definition, SAR is a much more flexible way compared with AR which generate tokens in a fixed raster order, and covers several variants including Masked AR, as well as VAR. To support the use of SAR, the paper introduces a new variants of the original Transformer architecture, named as fully masked Transformer. Experiments on ImageNet and text-to-image generation has shown that SAR outperforms previous benchmarks including LlamaGen, MaskGiT under comparable settings, which proves the effectiveness of proposed method.

### Strengths
- The exploration of set AR could be helpful for future works that uses AR models for image/video generation.

- The paper provides a good way to transform traditional Transformers architecture into fully masked transformer.

- This paper conducts quite a lot experiments and ablations that tests different variants of the model (which I appreciate).

### Weaknesses
 - The idea of using cosine schedule to determine the number of tokens seems not novel [1, 2]

- Although the paper includes many different ablations and variants of SAR design, most of them are probably not very necessary. For example, the ablation of sequence order settings shows raster is the best (Fig. 5), and training/inference with different order settings shows aligned training/inference works the best (Table 5). Both of these experiments are quite intuitive (without any surprise). Furthermore, the paper does not provide sufficient analysis on why raster order performs the best, which limits the insights that can be gained from this work.

Writing typos: 
- line 231-232: Eq. equation 2/3

### Questions
NA

### Soundness
3

### Presentation
2

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
This paper introduces Set AutoRegressive Modeling (SAR), a new paradigm for autoregressive image generation that generalizes conventional autoregressive (AR) models by allowing the sequence to be split into arbitrary sets containing multiple tokens, rather than outputting each token in a fixed order. The authors propose a Fully Masked Transformer (FMT) architecture to implement SAR. The paper shows that existing AR variants (like AR and Masked AR) are special cases within the SAR framework, and SAR enables smooth transitions between them.

### Strengths
1. Authors present a unified framework that generalizes existing AR approaches.

2. Good T2I result demonstrates real-world applicability through text-to-image generation.

### Weaknesses
1. The performance of SAR-TS is suboptimal compared to pure AR or MAR approaches.

2. The authors claim that  Fully Masked Transformer is the first work supporting KV cache for AR image generation. llamagen already has support this feature as llamagen is a causal transformer.

### Questions
The paper's presentation is mainly based on the discrete tokenizer. Does it support the continuous tokenizer AR method, like MAR. Could the authors detail the (SAR,K=1) results below mask AR in Table 4.

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
This paper proposes SAR as a unified framework of AR and MAR. The key components of SAR include the number of sets, the number of tokens per set and the sequence order. To enable flexible design for these components, this work further propose FMT, an encoder-decoder transformer that utilizes an encoder to output the embedding of prefix tokens and generate new tokens via decoder, guided by the positional embeddings. Experimental results are provided to compare SAR with existing methods and show how each component influence the performance of SAR.

### Strengths
1. SAR incorporate several important design choice in AR models, including the number of sets, the number of tokens per set and the sequence order. Additionally, SAR employs Fully Masked Transformer to address the challenges of using arbitrary choices.
2. The paper includes a substantial amount of experimental results:
    - SAR achieves better performance than LlamaGen and reproduces comparable performance with MAR by using appropriate design choices.
    - Extensive ablation studies illustrate the impact of each design choice on the performance-step trade-off.
    - Experiments on text-to-image generation are also conducted.

### Weaknesses
1. Further clarification is needed regarding the fundamental differences between SAR and existing methods. While SAR is presented as a flexible framework, its key components exhibit similarities to those of existing methods.
    - For the number of sets and set length: Fig.2 shows that SAR represents a smooth transition from AR to MAR, as it enables different numbers of sets and set lengths. However, as stated in the paper and based on my understanding, MAR [1,2] also supports different set lengths during inference to achieve a trade-off between steps and performance. The extreme case for MAR mentioned in the paper (i.e., K=1) occurs only during training. Moreover, VAR [3] also uses the set-prediction approach and generates tokens in a causal manner. Therefore, whether viewd from the perspective of extending the inference of MAR to training and using causal architecture, or from the perspective of extending VAR accommodate different numbers of sets and varying set lengths, the modifications in this paper seem to be straightforward. The authors need to clarify the essential differences between the "continuous new state that SAR offers between AR and MAR" and the aforementioned methods. Is the difference only lies in the introduction of a new architecture FMT?
    - For the sequence order: The most general form of sequence order, random order, has already been used by previous MAR works [2]. This paper seems to simply adopt this method.

2. Regarding experimental results:
    - My main concern is that the performance improvement of SAR shown in Tab.4 is relatively limited.
        - For SAR-TS: Currently, the performance of SAR-TS does not significantly exceed other methods. The reported FID of 11.33 is only marginally better than the 11.46 achieved by MaskGIT, and it is unclear if this difference is statistically significant given the variance in generative models. Furthermore, the practical advantage of SAR-TS is not clearly demonstrated, as the authors do not show a clear use case where this marginal improvement translates to a tangible benefit.
        - For Masked-AR: The comparison between FMT and Masked AR is incomplete, as no baseline methods use a comparable parameter size to FMT-L or FMT-B. From the results presented, the improvements brought by SAR are also limited (e.g., a 0.05 lower FID than MaskGIT while having 50% more model parameters). Additionally, strong baselines like MAR-L and MAR-B from [2] are not not included. The lack of comparison with these strong baselines makes it difficult to assess the true contribution of FMT.
        - For VAR: There is also no valid comparison with VAR. It is unclear how SAR compares to VAR in terms of both performance and computational efficiency, especially given that both methods use a set-prediction approach.
        - For LlamaGen: While FMT performs better than the LlamaGen baseline, I would like to confirm what modifications are made by SAR compared to the LlamaGen baseline aside from the new architecture. It seems the token number per set is 1, and Tab.5 shows that raster order performs the best, both of which are settings used by LlamaGen. The authors need to clarify if the improvement is solely due to the new architecture or if other factors are involved.
    - Additionally, there is a certain dependency between various choices in training and inference, making it difficult to train a model that supports different steps and orders in inference while achieving optimal results. For example, from Tab.5, the negative impact of order mismatch appears significant; From Fig.8 and related discussions in the paper, the mismatch in steps can lead to undesirable results. Therefore, the flexibility of SAR seems somewhat limited. The practical value of SAR is further diminished by the observed sensitivity to training and inference configurations, which makes it difficult to leverage the claimed flexibility.

    Given these concerns, although SAR is a new framework offering various options, the results do not show superiority over existing methods, nor is it fully flexible. The pratical advantages of SAR needs to be further clarfied.

3. Some statements need further clarification:
    - Since random-2-random appears to be a general form of training, which supports predicting an arbitrary number of tokens based on an arbitrary number of tokens, the "mismatch" between MAR's training and inference in Tab.1 needs more explanation. The authors should provide a more detailed explanation of the specific differences in masking strategies and loss calculation between training and inference in MAR, as this is not clear from the current description.
    - The definitions of $m_e$, $m_{ds}$, and $m_{dc}$ in the Alg.1 and Alg.2 seem to be missing (please correct me if I missed something, thank you).
    - In line 426, why does it state that only 64-sets can work for a few steps? From Fig.8, it seems that 4-sets perform best at 4-steps sampling?
    - As discuss, MAR is a special case of SAR with "random-2-random". However, the authors indicate the K of MAR as 1 in Tab.6 and Fig.2.
    - In the middle sub-figure of Fig.9, are the training steps and sampling aligned? Additionally, do "causal calculation" and "full calculation" refer to causal and full attention masks, respectively?

### Questions
1. Why not use a decoder-only architecture? At each step, the tokens sampled in the previous step and the positional embeddings of the next set of tokens are fed into the transformer as input, with other generated tokens as the prefix. Tihs apporach would also allow the use of KV cache to store the information of all previously generated tokens.
2. If the training and sampling steps are aligned for the middle sub-figure of Fig.9, it indicates that 2-step sampling achieves a FID of around 30, which is too good to be believed for me. Could the authors provide some code for verification?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces a new image generation method called SAR, which extends the traditional autoregressive model to a "next-set" framework. SAR enables flexible sequence ordering and output intervals, thus encompassing both the autoregressive and masked autoregressive models as specific cases. Additionally, the authors propose the Fully Masked Transformer architecture for SAR. Quantitative and qualitative results are presented on class conditional and text-to-image generation.

### Strengths
1. SAR is a flexible formulation and unifies the existing autoregressive and masked autoregressive models. A unified formulation is interesting.
2. The authors present an effective, new Fully Masked Transformer architecture for SAR.
3. The authors systematically studied the impact of factors such as sequence order and output interval on generation quality. I believe these experimental results provide valuable insights for advancing the field.

### Weaknesses
1. The authors claim that SAR unifies autoregressive and masked autoregressive models; however, SAR's FID lags significantly behind masked autoregressive models. The presented FID scores for SAR are notably inferior, suggesting that while the formulation may be unified, the practical performance, particularly in terms of image quality, is not competitive with established masked autoregressive approaches. This discrepancy raises concerns about the practical utility of the proposed unification, as it does not translate to improved or even comparable generation quality.
2. The authors note that SAR can utilize KV-cache acceleration, whereas masked autoregressive models cannot, and they claim this as an advantage of SAR. However, they do not provide any speed comparisons between SAR and masked autoregressive models. Instead, they only compare generation speed with LlamaGen, which is insufficient. Moreover, it raises questions as to why SAR’s FID is worse than LlamaGen’s in Figure 7, despite both models having a similar number of parameters. The lack of direct speed comparisons with masked autoregressive models makes it difficult to assess the true benefit of KV-cache acceleration in the context of the proposed method. Additionally, the performance discrepancy with LlamaGen, despite similar parameter counts, suggests potential inefficiencies in the SAR architecture or training process.
3. The Text-to-Image generation experiment lacks proper evaluation. The evaluation relies solely on FID, which is known to have limitations in capturing the nuances of text-to-image alignment and overall generation quality. The absence of more comprehensive metrics makes it difficult to assess the true performance of the proposed method in the text-to-image setting.

### Questions
1. What does $N$ represent in Line 330 and Line 334? It seems that $N$ refers to the number of tokens in an image based on the notations in Figure 2 (a1), but the authors use $n$ to denote the number of tokens in an image in Equation (1).

2. In Line 342, the authors state that 'random-2-random' indicates the MAR setting. However, as shown in Figure 2 (d1), $K=1$ for MAR. I'm a bit confused; could you please provide further clarification?

3. What do $m_e$, $m_{ds}$ and $m_{dc}$ mean in Algorithm 1 and Algorithm 2?

4. When training with a fixed number $K$, how does SAR inference when the sampling steps differ from $K$?

5. I am concerned about the scaling properties of the encoder-decoder network structure. I recommend that the authors explore the scaling behavior of SAR or even scaling laws in their future work.

### Soundness
3

### Presentation
2

### Contribution
3

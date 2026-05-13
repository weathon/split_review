# Generalized Video Moment Retrieval

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
In this paper, we introduce the Generalized Video Moment Retrieval (GVMR) framework, which extends traditional Video Moment Retrieval (VMR) to handle a wider range of query types. Unlike conventional VMR systems, which are often limited to simple, single-target queries, GVMR accommodates both non-target and multi-target queries. To support this expanded task, we present the NExT-VMR dataset, derived from the YFCC100M collection, featuring diverse query scenarios to enable more robust model evaluation.
Additionally, we propose BCANet, a transformer-based model incorporating the novel Boundary-aware Cross Attention (BCA) module. The BCA module enhances boundary detection and uses cross-attention to achieve a comprehensive understanding of video content in relation to queries. BCANet accurately predicts temporal video segments based on natural language descriptions, outperforming traditional models in both accuracy and adaptability. Our results demonstrate the potential of the GVMR framework, the NExT-VMR dataset, and BCANet to advance VMR systems, setting a new standard for future multimedia information retrieval research.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper first introduce a novel GVMR framework that significantly expands the scope of traditional VMR, catering to a wider range of query types and enhancing the model’s practical nutility and  present a meticulously curated dataset. To deal with GVMR, they propose the BCANet model. Totally speaking, the contributions about extend task and new dataset is valuable.

### Strengths
1. This paper introduces a extend task about TVG which covers more situations about video localiztion.
2. They build a new dataset for their introduced dataset which helps the deeper researches in future.
3. They propose a model based on LLM generate queries in fine-grain semantic, to benefit the video content understanding to the next stage

### Weaknesses
1. The boundary awareness is a common question in this field and many works like[1] focus on this problem. The author didn't analyse the differences between them to show their novelty.


### Questions
1. The model relies on the LLaVa to generate scene captions to divide the backgrounds and foregrounds. Will it brings noisy due to the diversity of generated samples?
2. Did you compare your model with the finetuinng model based on multimodal LLM ?
3. With using the LLM to generate captions , what about the time cost and memory usage?
4. Will the dataset be open source? If so ,it will be an important contribution.

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
5

### Summary
This paper introduces the Generalized Video Moment Retrieval (GVMR) framework, which extends traditional Video Moment Retrieval (VMR) to handle a wider range of query types. To support this expanded task, it presents the NExT-VMR dataset, derived from the YFCC100M collection, featuring diverse query scenarios to enable more robust model evaluation. Additionally, a novel transformer-based model named BCANet is proposed and achieves outperforms when compared with traditional VMR approaches.

### Strengths
1. A novel GVMR framework is first introduced that significantly expands the scope of traditional VMR, catering to a wider range of query types and enhancing the model's practical utility.

2. A meticulously curated dataset, NExT-VMR, is presented. The dataset is specifically designed for GVMR task, which includes a variety of query types and scenarios, thereby enabling more robust and versatile model training and evaluation.

### Weaknesses
1. As mentioned in the paper, "GVMR aspires to deliver a robust and flexible solution for video moment retrieval, significantly enhancing the model's interpretative prowess, precision, and retrieval efficiency." Would the enhancement of the model on interpretative prowess, precision, and retrieval efficiency be proved and presented in experiments?

2. More statistics of the proposed dataset are needed to be listed in Table 1, such as the entire/average lengths of videos and queries and the number of one-to-multi and no-target samples in the dataset.

3. Is it possible to demonstrate the evaluation of this method on traditional VMR datasets (e.g., Charades, ActivityNet, and TACoS) for one-to-one (different from the mentioned one-to-multi or no-target) VMR tasks? 

4. The BCANet pipeline presented in Figure 1 is confusing and difficult to interpret. The respective variable symbols should be labeled in Figure 1. Moreover, the processes for the BCL and QCA modules, along with query-text cross-attention, are also not clearly depicted in the figure. Moreover, what's the meaning of the "region" and "region features" in this paper? Dose the "region" mean a video clip?

5. The BCANet proposed in this paper does not seem to include specific designs for handling one-to-multi cases. Compared to traditional VMR methods, what advantages does BCANet offer in dealing with such data?

6. Since the retrieval speed is also an important metric in VMR, for example, [a] analyze the speed of various VMR approaches. I recommend the authors conducting speed analysis in this paper. In addition, is GVMR slower than traditional VMR?
[a] Fast video moment retrieval, ICCV 2021.

### Questions
Please refer to the weakness part.

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
5

### Summary
This paper introduces the Generalized Video Moment Retrieval framework, which expands traditional VMR to handle complex, non-target, and multi-target queries. To support this, the authors present the NExT-VMR dataset and BCANet, a transformer-based model with a Boundary-aware Cross Attention module that improves boundary detection and query understanding. 
The results show that GVMR, NExT-VMR, and BCANet significantly enhance VMR performance, setting a new benchmark for future research in multimedia information retrieval.

### Strengths
The problem the authors solve is interesting.

This paper provides a good moment retrieval dataset.

The paper is clearly written and the method can be understood.

### Weaknesses
- The NExT-VMR dataset is not large enough to be used for large-scale training. In addition, why not divide the test set on NExT-VMR for experiments?

- Figure 3 is confusing. There are many colored blocks around the Query-Text Cross Attention module. I don't understand what it wants to express? Lack of technical details.

### Questions
- Can't the previous model achieve multi-target query well after training on the standard dataset? Lack of relevant experiments to prove the author's motivation.

- Can the model in this paper use a single query to query multiple related clips in the video? This is a more worthy of attention.

- YFCC100M is an excellent large-scale video dataset, but why did the author only select 9957 videos from YFCC100M? How was it selected?
- Will the author open source the dataset and code?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces the Generalized Video Moment Retrieval (GVMR) framework, which expands traditional Video Moment Retrieval (VMR) to accommodate both non-target and multi-target queries, moving beyond the usual single-target focus. To support this, the authors present the NExT-VMR dataset, derived from the YFCC100M collection, featuring diverse query scenarios for robust model evaluation. They also propose BCANet, a transformer-based model that incorporates the Boundary-aware Cross Attention (BCA) module to enhance boundary detection and improve understanding of video content in relation to queries. Experiments demonstrate the potential of the NExT-VMR dataset and BCANet to advance VMR capabilities.

### Strengths
- This paper introduces a new task called Generalized Video Moment Retrieval (GVMR), which is designed to adeptly handle the complexities of various query types, extending the traditional Video Moment Retrieval (VMR) paradigm to include both multiple-target and no-target queries.
- This paper presents a specialized dataset, NExT-VMR, which is meticulously constructed and analyzed from the YFCC100M dataset. Tailored specifically for GVMR, this dataset features a diverse range of query types, including one-to-multiple and no-target queries.
- This paper introduces a model called BCANet, aimed at improving performance on the challenging task of GVMR, where the model must accurately predict a variable number of temporal timestamps based on natural language descriptions.

### Weaknesses
 - Why does the paper utilize the YFCC100M dataset as the primary data source instead of existing VMR datasets such as TACoS, Charades-STA, MAD, or ActivityNet-Captions?
- From the statistics in Table 1, it can be seen that the average number of segments corresponding to a query is less than 2, which contradicts the paper's motivation for creating multiple-target queries. Additionally, the proportion of non-target queries is very low. Based on the dataset statistics, it is unclear where the challenges of this new dataset compared to existing ones lie. The low average number of segments per query, especially when considering the stated goal of addressing multi-target scenarios, suggests that the dataset might not be as representative of complex multi-target retrieval as claimed. Furthermore, the scarcity of non-target queries raises concerns about the dataset's ability to effectively evaluate models on their capacity to distinguish between relevant and irrelevant video segments.
- From Table 2, it can be seen that BCANet shows a significant advantage only in the single-moment retrieval task, while its performance in multi-target and non-target scenarios is not as pronounced. This raises questions about the overall effectiveness of the method. The limited performance gains in multi-target and non-target scenarios, despite the introduction of the Boundary-aware Cross Attention (BCA) module, suggests that the model's architecture might not be fully optimized for the complexities of these tasks. The fact that the model excels primarily in single-moment retrieval indicates a potential weakness in its ability to handle the more nuanced aspects of generalized video moment retrieval.

### Questions
- BCANet is a supervised learning framework. How does it address the issue of inconsistent target quantities for each query in a batch during the training process? Additionally, if a query corresponds to three moments, are all three segments' timestamp information used in the loss function calculation?
- For queries labeled as non-target, what information do they provide during training?
- Why does the paper utilize the YFCC100M dataset as the primary data source instead of existing VMR datasets such as TACoS, Charades-STA, MAD, or ActivityNet-Captions?
- From the statistics in Table 1, it can be seen that the average number of segments corresponding to a query is less than 2, which contradicts the paper's motivation for creating multiple-target queries. Additionally, the proportion of non-target queries is very low. Based on the dataset statistics, it is unclear where the challenges of this new dataset compared to existing ones lie.
- From Table 2, it can be seen that BCANet shows a significant advantage only in the single-moment retrieval task, while its performance in multi-target and non-target scenarios is not as pronounced. This raises questions about the overall effectiveness of the method.

### Soundness
3

### Presentation
3

### Contribution
3

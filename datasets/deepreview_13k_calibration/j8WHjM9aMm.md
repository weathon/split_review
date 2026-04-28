# Diffusion-based Neural Network Weights Generation

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 5, 6, 5, 8

## Abstract


## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Authors propose a diffusion-based approach to generate parameters of neural networks for transfer learning conditioned on the target dataset. Prior work often relies on the diversity of pretrained models or datasets used to train these parameter prediction models but it limits their ability to generalize to new datasets. Encoding both model parameters and architecture jointly enhances the generality of the parameter prediction approach to unseen tasks. Several experiments are performed to test the efficacy of the approach for domains such as vision and large language models, demonstrating that it outperforms several meta-learning and parameter prediction approaches.

### Strengths
- The proposed approach is conceptually simpler to train and test than previous meta-learning approaches which often involve solving a bi-level optimization problem.
- The dataset conditioning in the approach increases the generality of the approach to new unseen datasets.
- Extensive sets of experiments are presented for different settings such as few-shot learning, zero-shot learning, model retrieval, classifier head adaption, LoRA weight generation, and adapting LLM weights for specific tasks.

### Weaknesses
 - Although the authors argue that previous approaches rely on diversity of training architectures and dataset for generalization, the proposed approach also has limitations along the same axis: it may only generalize to new datasets which are in-distribution for the dataset encoder otherwise the dataset encodings can be noisy. For instance, if the dataset encoder is only trained on imagenet-like natural images, it may not generalize to unseen dataset distributions like medical images. Table 17 seems to suggest the same since accuracies for unseen datasets are poorer in absolute numbers, so it’s unclear if dataset encoding is really needed otherwise one could simply train a parameter prediction model on combined datasets which could generalize to new ones.
- Missing baselines/ablations: Building on above, there are no ablations or baselines testing how effective are each component in the proposed approach: dataset encoding, layer-vectorization, spectrum ranking. It’s unclear how much importance all these components play in the final performance of the proposed approach. Moreover, some crucial baselines are missing -- for instance, training a simple param prediction diffusion model (e.g. Peebles et al. (2022)) without dataset encoding vs training it with dataset encoding to see how much generalization performance is improved with dataset encoding (which is one of the main contributions of this work).
- It seems that image dataset encoding uses the dataset samples (images) with a set transformer model whereas the language dataset encoding is done by simply picking LLM embeddings of the task description which seems weaker. If it’s not, is it possible to also encode image datasets in the same task-description-based way using LLM or VLM?
- For LLM param generation, authors use spectrum technique from prior work in order to deal with a large number of parameters in LLMs but it’s unclear how effective it is. It may be a good idea to use this technique on small-to-medium scale models where encoding all parameters is feasible to gauge the loss of performance and potential scope for improvement in this stage.
- It seems that authors train separate D2NWG models for param prediction in each setting. Is it possible to train a single param prediction model? Are there any technical hurdles in the approach which could prevent doing this (assuming access to large-scale compute and data)?

### Questions
See weakness section for my concerns and questions.


Writing suggestions:
- What do the task descriptions look like for NLP tasks which are used for encoding them? Adding pointers in section 3.3 (line 234-237) will be helpful for readers.
- Section 3.3 is a bit confusing to read due to paragraph titles. It looks like authors use 4 types of encoding in their work corresponding to 4 paragraphs but it’s actually just 2 (image and language dataset encoding). The middle two paragraphs (set-based dataset encoding and contrastive dataset encoding) are essentially describing image dataset encoding in detail. It may be a good idea to re-organize this section to be clearer.

Nit:
- Double dot at the end of line 116.
- Line 1147: “ios” -> “is”
- Line 184: “Parametrs” -> “Parameters”
- Line 1323: “metho” -> “method”
- Line 512: “robustnets” -> “robustness”
- Line 1331: remove “par”

### Soundness
2

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
This paper proposes a diffusion-based neural network weight generation technique named D2NWG, which directly learns the weight distributions of models pre-trained on various datasets. Specifically, the authors have developed a complete framework for latent diffusion models to learn from pairs of weights and datasets. The paper evaluates D2NWG across various tasks, both for direct generation and additional fine-tuning, outperforming state-of-the-art meta-learning methods and pre-trained models. The results demonstrate a capability for scalable transfer learning.

### Strengths
1. The paper investigates an interesting problem, the methodology is promising, and the paper is well-written and easy to read.
2. The experimental results are very solid, covering diverse tasks across a variety of datasets. These results outperform state-of-the-art meta-learning methods and pre-trained models.

### Weaknesses
1. Although the idea is interesting and the methodology looks promising, my main concern is about the practical significance of the proposed method, considering that training an effective diffusion model requires substantial computational resources. I will expand on this concern below:
2. Tables 1 and 2 show that D2NWG outperforms several baselines. Notably, D2NWG is tagged with 'CH', indicating that it only modifies the last classifier layer, similar to linear probing. This suggests that it may still be challenging for D2NWG to generate complete parameters with robust performance.
3. The concept of 'Zero-shot adaptation' does not seem applicable as the weights generated by D2NWG are conditioned on the target dataset (possibly the test set). This could be considered a form of 'test data leaking', which limits the practical utility of D2NWG.
4. Section 4.2 discusses the need for further fine-tuning of the generated models, suggesting that D2NWG's role is similar to that of pre-trained models. However, there is no evidence to suggest that training a usable D2NWG model is more cost-effective than using pre-trained models.
5. The generalization capability remains the most challenging issue for D2NWG. Although the authors attempt to demonstrate its adequacy across a range of datasets, there is no evidence that a well-trained D2NWG can handle diverse tasks and different model architectures simultaneously. Currently, D2NWG seems like a suboptimal alternative to a well-developed optimizer. Additionally, the supporting components such as the autoencoder and the dataset encoder, which are trained separately, also suffer from generalization issues.

### Questions
Please refer to the weakness for my questions. If it is solved, I am willing to raise my score.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a method called D2NWG, a diffusion-based neural network weight generation technique that enhances transfer learning by generating task-specific neural network weights based on target datasets. Unlike traditional transfer learning approaches that require fine-tuning or access to large collections of pretrained models, D2NWG uses a latent diffusion process to model and sample weight distributions, allowing efficient generation of adaptable weights for both seen and unseen tasks. This approach is scalable to large architectures, including large language models, and shows improved performance across various domains, outperforming existing meta-learning and pretrained models. The technique has been tested extensively, demonstrating superior adaptability and convergence speed, making it a promising tool for scalable transfer learning and model customization across diverse tasks.

### Strengths
1. The authors considered a wide range of evaluation settings (zero/few-shot learning, model retrieval, fine-tuning, domain transfer, conditioned weight generation, etc.) and provided comprehensive experiments.
2. The authors considered multiple ways to vectorized the model weights and encode the datasets.

### Weaknesses
1. **High Workload and Tuning Challenges Due to Additional VAE Training**: The additional VAE for parameter encoding introduces significant computational workload and requires hyperparameter tuning, making it less scalable and potentially costly. What steps could be taken to simplify this process, and are there alternative methods for parameter encoding that maintain performance but reduce overhead? The computational cost of training the VAE, especially for large models, is a major concern. Furthermore, the hyperparameter tuning required for the VAE adds another layer of complexity and computational overhead, making the method less practical for researchers with limited resources. The paper does not explore alternative encoding methods that could potentially reduce this overhead while maintaining the performance of the diffusion model. For example, a simpler dimensionality reduction technique or a more efficient autoencoder architecture could be explored.

2. **Ambiguity in Dataset Encoding Choices in Section 3.3**: The paper mentions several methods for encoding datasets, but it’s unclear how to choose the best encoding approach for a new dataset. Could the authors clarify the conditions under which each encoding method would be preferable, and provide a decision-making framework or guidelines to help practitioners adapt this approach to their datasets? The paper lacks a clear decision-making framework for selecting the appropriate dataset encoding method. For instance, it is unclear whether the choice of encoding should depend on the dataset size, modality, or complexity. Without such guidance, practitioners might struggle to effectively apply this method to new datasets. The paper should provide specific guidelines on when to use each encoding method and what are the expected trade-offs.

3. **Minor Typos and Formatting Issues**: There are minor typos and formatting inconsistencies in the paper that could be addressed to improve clarity and professionalism. For example, a colon is missing on line 177, and "while" on line 184 should begin with a capital "W." A thorough proofreading could enhance readability and reduce the risk of misinterpretation due to formatting errors.

### Questions
1. **Quantifying and Mitigating Bias in Public Checkpoint Weight Distributions**: The paper leverages publicly available pretrained models for weight distribution modeling, but it doesn’t address how potential biases in these weights—arising from the original datasets or training methods—might affect the generated weights. How can biases be quantified in these weight distributions, and what mechanisms could be implemented to ensure the generated weights are robust to such biases? Addressing this might require specific adjustments to the diffusion model or additional constraints on the weight distributions.

2. **Criteria for Selecting Additional Datasets for Training Target Architectures**: The method involves further training on a curated selection of datasets to improve model adaptability. However, there is little guidance on how to select these datasets to optimize the target architecture effectively. What are the criteria or metrics that could guide dataset selection to ensure it sufficiently represents the intended tasks and enhances generalization without introducing redundancies or biases?

3. **Evaluating the Impact of Generating All Parameters Versus Only the Classification Head**: In Table 1, the results compare the performance of models with generated classification heads to baseline models. However, it would be informative to understand the effect of generating all parameters instead of just the classification head. Would this provide additional performance gains, or might it introduce complications in terms of stability or adaptability to new tasks?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes to generate parameters using the latent diffusion model, which is a very new direction. Compared to traditional meta-learning, the authors want to show that D2NWG can generate parameters for both seen and unseen dataset, be applied to either classification task or NLP task, and achieve better accuracy with faster convergence. The most important contribution comes from the dataset encoding and use it as the condition when generating parameters.

### Strengths
- This paper is interesting in terms of the overall topic - generating the model parameters using the latent diffusion model. To my knowledge, there are only two other papers [1,2] in this direction and they have not been published yet. 
- The idea is easy to understand.

[1] Wang K, Xu Z, Zhou Y, et al. Neural network diffusion. arXiv 2024.    
[2] Jin X, Wang K, Tang D, et al. Conditional lora parameter generation. arXiv 2024

### Weaknesses
 - The presentation is poor, especially the experimental parts. It's like people writing each subsection separately and putting them together directly without good organization. 
- There are gaps between the claimed contribution and the real work they did. 

Please refer to the questions part. Thanks.

- Introduction:
    - You mentioned recent methods in latent diffusion-based weight generation in line 47 and said their limitations are limited to small models and a subset of parameters. However, in this paper, you try to generate parameters for classification heads (in Sect. 4.1) and LoRA (in Sect. 4.4). It seems that you are just generating a small number of parameters. So is this paper different from existing methods under this context? You also mentioned "generating weights for architectures with over 200 million parameters" in the fourth contribution, but I cannot find the supporting experiments for that.
    - You also mentioned some meta-learning few-shot methods in line 51 and said their generated parameters still need fine-tuning. Does this paper overcome the requirement of fine-tuning? I asked this question because in Table 2 of Sect. 4.1.2, the accuracy of D2NWG on those simple classification tasks are still not satisfying, which indicates the requirement of further fine-tuning. For example, for CIFAR-10 and Aircraft, I'm sure that after a few epochs of fine-tuning, the accuracy will reach above 90%. Then the current accuracy of D2NWG is not acceptable.
    - In Figure 1, in the sampling stage, the unseen architecture is also used as the condition to generate parameters. However, there is no explanation about unseen architecture in the main paper. I do see the results in the Appendix, but the unseen architecture is not really used as the condition. The method actually generates parameters for the seen architecture and then wraps it for the unseen architecture with some "careful concatenation" as mentioned in line 1171. So what is the "careful concatenation" here? I believe this part should be put in the main paper to fit Figure 1.

- Approach:
    - Typo in line 171: "The extraction process follows one one the main preprocessing methods:"
    - When will the model-wise vectorization be used and when will the layer-wise one be used?
    - Can you give an intuitive explanation about set-based dataset encoding in line 208, like encoding images from each class separately, then convert to the dataset encoding? It is currently hard to understand $x_p^{y_i}$.
    - In dataset-conditioned training, why the weights latent is used as the condition as well? It's like in the text-to-image diffusion model, the model will be conditioned on the text only, and the image is the distribution to learn. Why it is used as a condition as well? If it is conditioned on the weight, how can you do the inference without weight latent?
    - In Sect. 3.5, you mentioned "ranks LLM layers based on their importance", however, the experiments in Sect. 4.4 is about LoRA. If you choose to claim that in the main paper, you should put relevant experiments in the main paper.

- Experiments:
    - In Table 1, can you explain what is 5-way 1-shot a little bit?
    - In Table 2, for D2NWG_CLIP, I believe it is using CLIP. Then how about the two rows of D2NWG? What does it use?
    - In Sect. 4.1.1, you mentioned "evaluate the performance on 600 subsets from the UNSEEN test split". What do you mean by "unseen" here? It's like in general model training, we have train set and test set, and we test the trained model on the test set. Now you have multiple trained models, and you use that to train the diffusion model to generate weights, which is expected to work on the test set just like what we did in the normal training. Why it can be called "unseen" task?
    - In line 348, you mentioned "potentially eliminating or significantly speeding up the fine-tuning process". As I mentioned in the last point, it's normal to NOT fine-tune if it is a SEEN task/dataset. While for real unseen tasks as you did in Sect. 4.3, the generated parameters do need fine-tuning.
    - Starting from Sect 4.1.3, the experiments become hard to follow since you change the settings in each section frequently. It's better to organize your experiments better. For example, for the experiments in Sect. 4.2, we can still use the dataset in Table 2. Otherwise, it's hard to understand (1) What are the train and test datasets? Are the test ones seen or unseen? How do you define unseen? (2) How do you train the diffusion model? What models' parameters do you use to train the diffusion model? 
    - In Figure 2, why dessert food is so good from the beginning? Do you have any clue? Whether because the class/dataset is put in the trainset occasionally?
    - Sect. 4.4. is still seen task case right?

### Questions
I will list my questions according to the order appearing in the paper. You may want to combine some of them when rebuttal if necessary.
- Introduction:
    - You mentioned recent methods in latent diffusion-based weight generation in line 47 and said their limitations are limited to small models and a subset of parameters. However, in this paper, you try to generate parameters for classification heads (in Sect. 4.1) and LoRA (in Sect. 4.4). It seems that you are just generating a small number of parameters. So is this paper different from existing methods under this context? You also mentioned "generating weights for architectures with over 200 million parameters" in the fourth contribution, but I cannot find the supporting experiments for that.
    - You also mentioned some meta-learning few-shot methods in line 51 and said their generated parameters still need fine-tuning. Does this paper overcome the requirement of fine-tuning? I asked this question because in Table 2 of Sect. 4.1.2, the accuracy of D2NWG on those simple classification tasks are still not satisfying, which indicates the requirement of further fine-tuning. For example, for CIFAR-10 and Aircraft, I'm sure that after a few epochs of fine-tuning, the accuracy will reach above 90%. Then the current accuracy of D2NWG is not acceptable.
    - In Figure 1, in the sampling stage, the unseen architecture is also used as the condition to generate parameters. However, there is no explanation about unseen architecture in the main paper. I do see the results in the Appendix, but the unseen architecture is not really used as the condition. The method actually generates parameters for the seen architecture and then wraps it for the unseen architecture with some "careful concatenation" as mentioned in line 1171. So what is the "careful concatenation" here? I believe this part should be put in the main paper to fit Figure 1.

- Approach:
    - Typo in line 171: "The extraction process follows one one the main preprocessing methods:"
    - When will the model-wise vectorization be used and when will the layer-wise one be used?
    - Can you give an intuitive explanation about set-based dataset encoding in line 208, like encoding images from each class separately, then convert to the dataset encoding? It is currently hard to understand $x_p^{y_i}$.
    - In dataset-conditioned training, why the weights latent is used as the condition as well? It's like in the text-to-image diffusion model, the model will be conditioned on the text only, and the image is the distribution to learn. Why it is used as a condition as well? If it is conditioned on the weight, how can you do the inference without weight latent?
    - In Sect. 3.5, you mentioned "ranks LLM layers based on their importance", however, the experiments in Sect. 4.4 is about LoRA. If you choose to claim that in the main paper, you should put relevant experiments in the main paper.

- Experiments:
    - In Table 1, can you explain what is 5-way 1-shot a little bit?
    - In Table 2, for D2NWG_CLIP, I believe it is using CLIP. Then how about the two rows of D2NWG? What does it use?
    - In Sect. 4.1.1, you mentioned "evaluate the performance on 600 subsets from the UNSEEN test split". What do you mean by "unseen" here? It's like in general model training, we have train set and test set, and we test the trained model on the test set. Now you have multiple trained models, and you use that to train the diffusion model to generate weights, which is expected to work on the test set just like what we did in the normal training. Why it can be called "unseen" task?
    - In line 348, you mentioned "potentially eliminating or significantly speeding up the fine-tuning process". As I mentioned in the last point, it's normal to NOT fine-tune if it is a SEEN task/dataset. While for real unseen tasks as you did in Sect. 4.3, the generated parameters do need fine-tuning.
    - Starting from Sect 4.1.3, the experiments become hard to follow since you change the settings in each section frequently. It's better to organize your experiments better. For example, for the experiments in Sect. 4.2, we can still use the dataset in Table 2. Otherwise, it's hard to understand (1) What are the train and test datasets? Are the test ones seen or unseen? How do you define unseen? (2) How do you train the diffusion model? What models' parameters do you use to train the diffusion model? 
    - In Figure 2, why dessert food is so good from the beginning? Do you have any clue? Whether because the class/dataset is put in the trainset occasionally?
    - Sect. 4.4. is still seen task case right?

- Suggestion:
    - So generally you'd better make it clear about what you want to claim. For example, you may want to say, for the seen task, the generated parameters can be used directly with high accuracy. For the unseen task, the generated parameters may need fine-tune but with better final accuracy and faster convergence. 
    - Then for each claim, you will have an experiment section to support. Each section may include both results for CNN classification and NLP task.
    - The settings should be uniform throughout the paper. If some experiments do need different setting, give reason.

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces D2NWG, a diffusion-based method for generating neural network weights conditioned on target datasets. The key idea is to learn the distribution of pretrained model weights across different datasets and use latent diffusion to generate new weights that are optimized for specific tasks. The method can generate both classifier heads and full model weights, and scales to large architectures including LLMs. Extensive experiments demonstrate strong performance on few-shot learning, zero-shot transfer, and model retrieval tasks.

### Strengths
- Paper introduces a novel approach by combining latent diffusion models with neural network weight generation
  
- The authors conduct thorough experiments across various tasks, providing strong empirical evidence of the method’s effectiveness.
  
- The method exhibits robust performance both within the distribution of training datasets and on unseen datasets

### Weaknesses
1. **Limited Theoretical Analysis:**
   
   While the paper presents strong empirical results, it lacks a comprehensive theoretical framework that explains why diffusion-based weight generation effectively enhances transfer learning and generalization. The current analysis does not adequately address the curse of dimensionality inherent in high-dimensional parameter spaces. Specifically, it is unclear how the method ensures a tight approximation of target weights across millions of parameters without requiring an impractically large latent space. The theoretical claims about the existence of a latent vector $z_i$ for every specialized model $F_i$ with parameters $w_i$ such that $||H(z_i) - w_i|| \leq \epsilon$ need more rigorous justification, particularly considering the non-convex nature of neural network loss landscapes and the potential for the diffusion process to get stuck in local minima.

2. **Computational Costs:**
   
   The D2NWG method necessitates maintaining extensive collections of pretrained weights across a multitude of datasets. This requirement can lead to significant storage and computational overhead, potentially surpassing the costs associated with traditional pre-training approaches. Additionally, details on the training time and resource consumption compared to existing methods are limited. The paper does not provide a clear breakdown of the computational costs associated with each stage of the method, including the training of the VAE, the diffusion model, and the weight generation process. This makes it difficult to assess the practical scalability of the approach, especially when considering the memory requirements for storing the pretrained weights and the computational demands of the diffusion process.

3. **Reliance on Dataset-Specific Encoding:**
   
   The effectiveness of D2NWG heavily depends on the dataset encoding mechanisms, such as the Set Transformer and CLIP-based encoders. This reliance may limit the method's adaptability to datasets with unique characteristics or those that significantly differ from the training datasets. The paper does not explore the sensitivity of the method to the choice of encoders or provide a systematic analysis of how different encoding strategies affect the quality of the generated weights. Furthermore, the method's ability to generalize to datasets with significantly different modalities or structures is not thoroughly investigated.

### Questions
**[Q1]:** Could the authors provide a detailed analysis of the computational resources required to maintain and utilize the extensive collections of pretrained weights in D2NWG? Specifically, how does the storage and processing overhead of D2NWG compare to traditional pretraining and fine-tuning methods, particularly when scaling to very large models such as LLMs?

**[Q2]:** In terms of generalization, how does D2NWG ensure that the generated weights do not overfit to specific characteristics of the training datasets? Are there mechanisms in place to promote diversity and prevent homogenization of the generated weights?

### Soundness
3

### Presentation
4

### Contribution
2

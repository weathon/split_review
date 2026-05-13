# LLM-Codebook for Extreme Compression of Large Language Models

- Decision: Reject
- Scores: 5, 5, 3, 6

## Abstract
Large Language Models (LLMs) have exhibited outstanding performance in both understanding and generating language. However, their remarkable abilities often correlate with large model sizes, leading to challenges during deployment, inference, and training phases. While weight quantization and pruning are prevalent strategies, they tend to lose crucial information under extreme compression.
In this paper, we propose LLM-Codebook for extreme compression of large language models (LLM-Codebook), which maps expansive LLMs (in GB) to compact codebooks (in KB). The foundation of LLM-Codebook is our novel Hessian-aware K-means algorithm, which clusters weights into codebooks based on Hessian information, preserving parameters that have significant impacts on predictions. Simultaneously, the tuning technique, LoRA is adopted to update layers that have not been compressed, aiming to recover performance using only a limited corpus. LLM-Codebook effectively preserves the generation and multi-task solving abilities of LLMs, surpassing advanced methods such as GPTQ, QLoRA, LLM-Pruner, and SparseGPT. We validate our approach by extremely compressing LLaMA-7B and Vicuna-7B to a memory requirement of 2GB (a 6x compression factor) while retaining 99% of the baseline performance. Furthermore, our approach maintains reasonable accuracy even under extreme compression ratio, achieving 90% of the original performance (36% better than GPTQ) when the model size is compressed to one-eighth.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a codebook-based compression method for LLM. The compression technique indeed has a higher potential to achieve higher accuracy than the naive uniform quantization. However, the idea is not new and has been widely used in model compression before the era of LLM. Besides, the LoRA introduced to recover the accuracy is also not new. Therefore, the novelty of this paper is limited.

### Strengths
- The paper is well-written and clear
- The improvement compared with the naive quantization method is solid.

### Weaknesses
1. This work is essentially an application of production quantization on LLMs. Although the final performance surpasses the baselines, the method itself does not present much novelty. The idea of Hessian-aware k-means has also been utilized in previous works [1][2]
2. From the perspective of LLM compression ratio, this work does not compare with the state-of-the-art quantization works [2][3][4]
3. The current evaluation is focused solely on the 7b model. Could the author also provide evaluations on larger models, such as Llama-13b?

### Questions
Please refer to the part of weakness.

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces LLM-codebook for extreme compression of LLMs, which clusters LLM weights into codebooks (in KB) with three stages: (i) the salience stage derives the salience of the random layer's weight through the hessian matrix; (ii) the cluster stage employs the hessian-aware k-means algorithm to cluster the codebook, and (iii) the recover stage uses LoRA for performance recovery. The paper conducts experiments on Llama-7b and vicuna-7b, and compares with both pruning and quantization baselines. The results demonstrate the superiority of LLM-codebook in achieving higher compression ratios.

### Strengths
1. It achieves higher compression ratios for LLMs. 
2. This paper refrains from viewing pruning and quantization as two distinct paths for LLM compression. Instead, it perceives them as techniques for information compression[1]. Consequently, the paper's narrative does not adhere to the existing quantization or pruning pipeline. It introduces a unique compression technique: compressing LLM weights by clustering them and storing them in kilobyte-scale codebooks. This perspective is novel.

### Weaknesses
 - The experimental results are not very clear in terms of fair comparison with previous methods.
- To make the paper stronger, the authors should provide more insightful explanations to connect the components of the proposed method, otherwise can be easily understood as a simple combination of two mature methods.

- Eq(5) implies that the estimation of model weight salience depends on the selected dataset and I noticed that the authors used only 15 randomly selected samples from the Bookcorpus dataset. I wonder how sensitive this estimation is in terms of 1) the data source. Eg, how about 15 samples from Wiki or a similar corpus? 2) the number of samples. Eg, is 15 samples enough for a good estimation of salience? What’s the possible influence of the salience estimation error on the later recovery stage?  


- In Table 3, the Lora-based tuning looks more critical to prevent the performance from unacceptable degradation. This makes the readers very curious about several questions. 1) With only vanilla K-means, is it possible to match the best performance if more effort is put in tuning the recovery stage? 2) What’s the must-be reason to use Hessian-aware K-means instead of vanllina k-means given its extra computation cost of estimation and secondary role in recovering model performance?   
  

- Following Q.2 above, what are the baselines in Table 1 that support Lora-based tuning? If an extra recovery stage based on Lora tuning was carefully added, will those baseline performances catch up with the proposed method?    

- In Table 3 last row, The salience-adopted clustering stage leads to more performance degradation compared to the vanilla baseline: -3.5 vs - 6.3. Can the author explain the reason for this observation?

### Questions
Please refer to the weaknesses section

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a model weights compression algorithm method based on Hessian-aware K-means, especially for extreme reduction of model size. The authors empirically demonstrate the efficacy of Hessian-aware K-means and Lora-based recovery stage in compression and performance maintenance.

### Strengths
- The paper proposed to adopt an importance-aware K-means for model weights compression.  
- The paper is well-written and easy to follow.

### Weaknesses
●	It is unclear how can this method be combined with downstream LLM finetuning or if it is only effective for post-finetuning compression. After the compression, each linear layer consists of a codebook and an index map, how can the model be further finetuned under this structure?

●	Since the method requires full model finetuning using Lora for performance recovery, would the memory cost be huge when meeting with a larger base model like llama-70B? 

●	It is still being determined why the layer is randomly selected for compression during the Lora finetuning procedure.

●	The compressed weight tensor in Figure. 2 seems like a copy of the original weight tensor, which looks too similar to be a real compressed visualization. Please explain this part.

●	Some statements in this paper related to existing compression methods are given lacking enough verification. The latest works are left without discussion. Taking the low-bit compression parts as an example, though the selected baseline GPTQ in this paper does not give a good performance for lower-bit like 2-bit, there are already several works showing promising results for lower-bit compression [1-3]. For example, both omniquant and low_bit_llama show that llama families (1.1B-70B) can be well compressed to 2-bit with good performance. It is suggested to reorganize this part and discuss the possibility of combining low-bit compression with structure-clustering for further compression.

### Questions
- Eq(5) implies that the estimation of model weight salience depends on the selected dataset and I noticed that the authors used only 15 randomly selected samples from the Bookcorpus dataset. I wonder how sensitive this estimation is in terms of 1) the data source. Eg, how about 15 samples from Wiki or a similar corpus? 2) the number of samples. Eg, is 15 samples enough for a good estimation of salience? What’s the possible influence of the salience estimation error on the later recovery stage?  


- In Table 3, the Lora-based tuning looks more critical to prevent the performance from unacceptable degradation. This makes the readers very curious about several questions. 1) With only vanilla K-means, is it possible to match the best performance if more effort is put in tuning the recovery stage? 2) What’s the must-be reason to use Hessian-aware K-means instead of vanllina k-means given its extra computation cost of estimation and secondary role in recovering model performance?   
  

- Following Q.2 above, what are the baselines in Table 1 that support Lora-based tuning? If an extra recovery stage based on Lora tuning was carefully added, will those baseline performances catch up with the proposed method?    

- In Table 3 last row, The salience-adopted clustering stage leads to more performance degradation compared to the vanilla baseline: -3.5 vs - 6.3. Can the author explain the reason for this observation?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes LLM-Codebook, an effective structure-clustering-based LLM compression technique for extreme compression. The main technology parts of this method consist of three steps: (1) Salient weight detection; (2) Hessian-aware K-means algorithm for weight clustering and compression; (3) Lora-based finetuning for retaining performance. The overall method is simple and effective. The manuscript is well-written with clear logic.

### Strengths
●	The paper is well-written and easy to follow.

●	The proposed LLM codebook shows good compression performance for a lower compression ratio as compared to recent compression works like GPTQ, SparseGPT, and LLM-Pruner.

### Weaknesses
●	It is unclear how can this method be combined with downstream LLM finetuning or if it is only effective for post-finetuning compression. After the compression, each linear layer consists of a codebook and an index map, how can the model be further finetuned under this structure?

●	Since the method requires full model finetuning using Lora for performance recovery, would the memory cost be huge when meeting with a larger base model like llama-70B? 

●	It is still being determined why the layer is randomly selected for compression during the Lora finetuning procedure.

●	The compressed weight tensor in Figure. 2 seems like a copy of the original weight tensor, which looks too similar to be a real compressed visualization. Please explain this part.

●	Some statements in this paper related to existing compression methods are given lacking enough verification. The latest works are left without discussion. Taking the low-bit compression parts as an example, though the selected baseline GPTQ in this paper does not give a good performance for lower-bit like 2-bit, there are already several works showing promising results for lower-bit compression ([1-3]). For example, both omniquant and low_bit_llama show that llama families (1.1B-70B) can be well compressed to 2-bit with good performance. It is suggested to reorganize this part and discuss the possibility of combining low-bit compression with structure-clustering for further compression.

Overall, this paper presents a method for compressing LLMs using structure clustering. The algorithm is verified on recent small LLMs like LLaMA-7B and shows good compression performance as compared to some of the existing techniques. The overall method is simple and effective. Some statements in the paper are not well verified.

[1] omniquant: omnidirectionally calibrated quantization for large language models

[2] https://github.com/GreenBitAI/low_bit_llama

[3] QA-LoRA: Quantization-Aware Low-Rank Adaptation of Large Language Models

### Questions
Pls. see the weaknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

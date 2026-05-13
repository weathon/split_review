# SwiftKV: Fast Prefill-Optimized Inference with Knowledge-Preserving Model Transformation

- Decision: Reject
- Scores: 5, 6, 6, 5

## Abstract
LLM inference for popular enterprise use cases, such as summarization, RAG, and code-generation, typically observes orders of magnitude longer prompt lengths than generation lengths. 
This characteristic leads to high cost of prefill and increased response latency. 
In this paper, we present \OURS, a novel model transformation and distillation procedure specifically designed to reduce the time and cost of processing prompt tokens while preserving high quality of generated tokens. 
\OURS combines three key mechanisms: i) SingleInputKV, which prefills later layers' KV cache using a much earlier layer's output, allowing prompt tokens to skip much of the model computation, 
ii) AcrossKV, which merges the KV caches of neighboring layers to reduce the memory footprint and support larger batch size for higher throughput, 
and iii) a knowledge-preserving distillation procedure that can adapt existing LLMs for \OURS with minimal accuracy impact and low compute and data requirement. 
For Llama-3.1-8B and 70B, \OURS reduces the compute requirement of prefill by 50\% and the memory requirement of the KV cache by 62.5\% while incurring minimum quality degradation across a wide range of tasks. 
In the end-to-end inference serving using an optimized vLLM implementation, \OURS realizes up to \(2\times\) higher aggregate throughput and 60\% lower time per output token. 
It can achieve a staggering 560 TFlops/GPU of normalized inference throughput, which translates to 16K tokens/s for Llama-3.1-70B in 16-bit precision on 4\(\times\) H100 GPUs. 
Our training, inference, and model implementations are open-sourced and can be found through \url{https://huggingface.co/collections/Snowflake/swiftkv-models-674f7d7474eb789e185d31cb}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies the optimization of inference in Transformer-based LLMs. It presents SwiftKV, a solution to reducing the KV cache and inference time to long contexts up to 128K. The proposed method features three parts: SingleInputKV, AcrossKV, and knowledge recovery. Experiments show the effectiveness of the proposed method and the usefulness of its components, as well as how they work jointly with other optimization techniques.

### Strengths
S1. Inference optimization for in Transformer-based LLMs is an important topic which has been extensively studied in recent years.

S2. Several key components have been proposed in this paper, with their usefulness showcased in the evaluation. 

S3. The proposed method is orthogonal to many existing optimizations and they can be used jointly to further optimize the performance.

### Weaknesses
W1. SingleInputKV borrows observations and ideas from previous works, as stated in the submission (such observation has also been utilized in the InfiniGen paper published at OSDI 2024).

W2. A core technique in the proposed method is cross-layer KV cache compression. The comparison/discussion with state-of-the-art KV cache compression/merging/cross-layer works is missing, e.g., PyramidKV and infini-attention. It is encouraged to discuss the difference and the novelty compared to existing KV cache compression techniques in the related work. Some surveys can be found here:
https://github.com/October2001/Awesome-KV-Cache-Compression

W3. Whereas the paper discusses long inputs, it lacks discussions with recent works on long contexts (see the above link), such as MInference, which optimize the prefilling of long contexts. Some of them exploit the sparsity to reduce KV cache and speed up inference, e.g., ALISA. 

W4. The proposed method is not training free, yet only Llama-3.1 models are evaluated. It is unclear if the performance (and its optimal parameter settings) also translates to models. Extension to other open models, such as Mistral, would be beneficial to understanding the contributions of this work.

### Questions
Q1. In Table 1, there is a significant drop in performance for 8B model on the math dataset GSK-8K. I suppose this is the harder case, meaning that the proposed method may not work well for the case of small models on tasks demanding more logic and reasoning. An analysis on why this performance drop occurs would be interesting. 

Q2. In Table 3, to show the impact of distillation, AcrossKV is disabled. However, to reduce KV cache, AcrossKV should be enabled for inference serving, right?

Q3. In Table 4, the performance of "our fine-tuned model" is significantly inferior to the base model. The result seems to be negative to the usefulness of your techniques. I don't quite understand the logic here.

### Soundness
3

### Presentation
4

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
This paper proposes two methods to reduce the cost of the prefill stage during LLM inference. 
The first method, called SingleInputKV, reuses the output hidden state vector from the i-th layer in attention layers as the input vector to generate key and value (KV) vectors of the subsequent layers. In previous methods, the j-th layer used the output hidden state vector from the (j-1)-th layer as input.
The second method, called AcrossKV, enables the KV vectors generated by the i-th layer to be reused by the following layers. In previous methods, each layer generates its own KV vectors by multiplying the input vector with its weight.
These techniques reduce computational costs by reusing the input and KV vectors of earlier layers for later layers. They also decrease the number of KV vectors that need to be cached for the decode stage. The proposed methods build on prior work [1], which showed minimal differences in the values of input vectors across layers as the number of layers increases in transformers.
The authors implemented these techniques in Llama-3.1-8B and Llama-3.1-70B models,  showing that while the performance on the LLM benchmark remains largely unaffected, both time and memory usage in the prefill stage are reduced by almost two times.

[1] Songwei Liu, Chao Zeng, Lianqiang Li, Chenqian Yan, Lean Fu, Xing Mei, and Fangmin Chen. Foldgpt: Simple and effective large language model compression scheme, 2024c. URL https://arxiv.org/abs/2407.00928.

### Strengths
S1. The paper proposes two techniques derived from insights from prior research, demonstrating their efficacy in reducing computational and memory costs during LLM inference.

S2. The authors show that fine-tuning can alleviate the decline in benchmark scores, emphasizing the practicality of the proposed methods without notably sacrificing model performance.

### Weaknesses
W1. The experiments in the paper are somewhat limited.
- The authors evaluate the proposed techniques only on Llama-3.1 models. Testing a wider variety of models would strengthen the results. If the proposed methods could demonstrate their benefits across transformer models with different attention mechanisms (e.g., sparse attention, low-rank attention), scaling approaches (e.g., wide scaling, deep scaling, sparse scaling), and sizes (Llama-3.2-1B, Llama-3.2-3B, Llama-3.2-8B,  Llama-3.2.-11B, Llama-2-13b, and Llama-3.2-70B, Llama-3.2-90B, and Llama-3.1-405B), it would enhance the paper’s contribution. Specifically, the paper lacks experiments on models employing sparse attention or low-rank approximations, which are increasingly common in efficient LLM architectures. Furthermore, the study should explore the impact of SwiftKV on models with varying scaling strategies, such as wide or deep scaling, to determine if the techniques are universally applicable or if they are more effective under certain architectural choices. The absence of these experiments limits the generalizability of the findings.
- The authors need to demonstrate whether applying SwiftKV to larger models yields more significant results compared to small models. Incorporate models such as  Llama-2-13B and Llama-2-7B. If applying the proposed methods to Llama-2-13B yields better results than Llama-2-7B in terms of both cost and the benchmark scores, it would strengthen the contribution of the paper. It is crucial to show that the benefits of SwiftKV scale with model size, as this would justify its use in more resource-intensive scenarios. Without this, it is unclear if the proposed method offers a practical advantage over simply using a smaller model.
- There is no experiment to show the independent effect of AcrossKV without the presence of SingleInputKV, leaving the isolated impact of AcrossKV unexplored. The authors need to compare a baseline model to one with only AcrossKV applied. This is important because the combined effect of SingleInputKV and AcrossKV might mask the true contribution of AcrossKV. Understanding the isolated impact of AcrossKV is critical for determining its actual utility and potential for further optimization.

W2. The justification for the claimed reduction in computational cost is insufficient. The paper needs to specify which operations are being skipped by SingleInputKV clearly by providing a detailed breakdown of the computational costs for each component of a Transformer model, comparing the baseline to SwiftKV. In Figure 1, SingleInputKV still appears to need to generate the output hidden state vector of every attention layer, which is a primary computational task in Transformer models. This is because the proposed method needs to generate the query vector for each attention layer in Figure 1, and the output hidden state vector from the (i-1)th layer is required to compute the query vector for the i-th layer. The paper should provide a more granular analysis of the computational cost, detailing the specific matrix multiplications, activation functions, and other operations that are avoided by using SingleInputKV. This would help in quantifying the actual savings and provide a clearer understanding of the method's efficiency.

### Questions
Please refer to W1 and W2.

### Soundness
2

### Presentation
2

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
SwiftKV proposes several techniques to improve to reduce computation and memory footprint for LLM inference while maintaining a similar level of accuracy. In particular, they propose to skip the pre-fill stage of later layers by rewiring the model and rely instead on intermediate computation results from an earlier layer, leading to a reduced amount of computation. The authors also reduce the memory footprint of later layers by sharing a KV cache across multiple subsequent layers. Additional they use a distillation/fine-tuning process of the affected model part to reduce the difference in accuracy compared to the original model. They show in their evaluation computation improvements for throughput as well as latency.

### Strengths
The ideas for the various optimizations are presented reasonable clearly and they seem novel as well, especially their combination. The evaluation on a number of models and datasets/benchmarks supports their performance claims and a reasonable ablation study is provided as well.

### Weaknesses
For me, the biggest issue is that end-to-end results are missing, which makes it hard for me to put the presented inference results (throughput, latency) into context, which also makes me question how useful the presented numbers are.

* apart from SingleInputKV, all the other optimizations are not properly motivated regarding the reasoning why they should work (some form of microbenchmark)
* end to end results are missing, especially since some of their writing, if I am not mistaken, suggests that they target a part of the pipeline that only compromises 5% of the "runtime"
* line 314: "The accuracy drops by another 0.32, going from 2-way to 8-way" - it is actually 1.32 according to the table
  * similarly the number for 16-way is wrong as well
* The authors might consider removing 5.5 to have more space for presenting the other content/result in more detail.
* not clear why the used benchmarks are representative for the use cases mentioned as motivation in the introduction

detailed copy editing comments:
* related work:
  * "their optimized implementations in TensorRT (NVIDIA, 2019)" - all previously mentioned techniques were published after 2019
* Figure 2, right side:
  * The parameters used in the legend are not explained at all in the caption. It is possible to understand after reading the subsequent text.
  * The subfigure is never actually referenced in the text, except in the appendix, as "proof" for some statement later and in a footnote.
* Figure 4: Artifacts in the layering of the curves, sometimes a dot is at the top for one datapoint and and then further down for other datapoints. But maybe that was intentional?
* Table 3: There is a horizontal line missing after "(a) The effect of distillation".
* line 447: "which suggest that MLP layers player a more prominent role" - missing verb, probably it should be "play" instead of "player"
* Figure 5 is not readable
* minor issues:
  * typos:
    * line 119: "Tensor-Parallelism(Shoeybi et al., 2020)" - missing space
    * lines 130 to 138: additional brackets around the year for the citations
    * line 157/158: "(Holmes et al., 2024; Agrawal et al., 2024))" - additional bracket at the end 
    * line 360: "toks/sec" - probably "token/sec"
    * line 859: "superme" - perhaps "supreme"?
    * line 923: "hyper-paramter" - missing e
    * line 923: "but did not invest deeper" - probably "investigated"
  * references:
    * Clark et al. 2018: cited differently than the other arXiv papers
    * Cobbe et al. 2021: misses place, where the paper was published
    * Dao et al. 2024:
      * year states 2024, but conference abbreviation suggests 2022
      * conference abbreviation is nowadays NeurIPS
    * Ding et al. 2021: misses place, where the paper was published
    * Elhage et al. 2021: url not clickable
    * GretelAI 2024: url not clickable
    * Hendrycks et al. 2021: cited differently than the other ICLR papers
    * Hinton et al. 2015: cited differently than the other arXiv papers
    * Kuzim et al. 2024:
      * year states 2024, but conference abbreviation suggests 2022
      * conference abbreviation is nowadays NeurIPS
    * Lewis et al. 2020: conference abbreviation is nowadays NeurIPS
    * Liu et al. 2024a:
      * cited differently than the other arXiv papers
      * cited twice (2024b)
    * Liu et al. 2024d:
      * year states 2024, but conference abbreviation suggests 2023
      * conference abbreviation is nowadays NeurIPS
    * Meng et al. 2024:
      * year states 2024, but conference abbreviation suggests 2022
      * conference abbreviation is nowadays NeurIPS
    * Pourreza and Rafiei 2024:
      * year states 2024, but conference abbreviation suggests 2023
      * conference abbreviation is nowadays NeurIPS
    * Sakaguchi et al. 2019: cited differently than the other arXiv papers
    * Wei et al. 2023: cited differently than the other arXiv papers

### Questions
* Section 3.4, Knowledge Recovery: The description suggests that the distillation is done for every of the later layers, but Figure 1 suggests that at least W_K and W_V are only trained for the initial layer of each AcrossKV block.
* Why are the results more or less consistently better for 4-way caching compared to 2-way caching for the 70B model? That seems kind of counterintuitive.
* footnote 5, page 7: What are the end-to-end results?
* Section 4.3: "a combined throughput of over 16K toks/sec over 4xH100 GPUs which corresponds to 560 TFLOPS/GPU"
  * So that is around 4k token per second for each GPU compared to 30k tokens/sec/GPU for 8B Llama model. But because the 70B model is much more complex, there are more floating point operations necessary?
  * Any notion why the pure compute performance increases despite a more "distributed" setting (multiple GPUs)?
* Any notion why the full model fine-tuning performs so much worse than the partial model fine-tuning?
* Section 5.3: "This may be due to the lack of math and coding examples in the two datasets we picked to train the model."
  * Why did you choose these datasets, if at least the coding use case is serving as a motivational example?
* Doesn't the discussion in Appendix B the whole point of the paper, i.e. trying to optimize a part than accounts for less than 5% of the total compute time?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes SwiftKV, a method that reduces LLM inference latency while preserving knowledge. SwiftKV combines Early Exit, KV cache compression, and Knowledge Distillation techniques, demonstrating latency improvements in performance evaluation.

### Strengths
1. The writing is good.  
2. Experimental results indicate that the proposed method effectively reduces latency while preserving knowledge.

### Weaknesses
1. Limited Efficient Experiments: VLLM serves as the only baseline in the performance results, which limits the demonstration of this work’s necessity and effectiveness. The authors’ method is a lossy optimization approach, and they should compare it with more serving systems to demonstrate respective performance improvements and knowledge retention. Although other methods may not conflict with the authors' approach, they may not be easily integrated (e.g. the strategy of Early Exit can hardly apply to Speculative Decoding, or combined with certain sparse attention methods like PowerInfer, quantization method like GPTQ may result in significant performance degradation.). If the authors cannot demonstrate the effectiveness of their method compared to others, or show that it can integrate with other methods for added benefits, the significance of this work is greatly diminished.

2. Lack of Key Assumptions: Some critical assumptions are missing, such as noting that latency-sensitive servers often adopt disaggregated systems to handle the prefill and decode stages separately. This omission could impact the reported TTFT and TPOT performance results, because in the disaggregated systems, TPOT will hardly be influenced due to improvements in the prefill stage.

### Questions
1. The code link appears to be invalid. Could you make the code open-source to enhance reproducibility?
2. SwiftKV focuses primarily on optimization during the prefill stage. How should we interpret the decrease in TPOT shown in the performance results?
3. Could you provide results comparing the performance of SwiftKV with more competitive baselines, such as Minicache, as mentioned in your paper? Could you clarify the connections and differences between your method and existing work, including its strengths and weaknesses? Could you demonstrate whether your method can be integrated with other approaches? Additionally, could you outline the potential application scenarios for your method?
4. As I understand, most datasets used in your paper consist of multiple-choice questions, leading to longer prefill times and shorter decoding times. I’m interested in seeing SwiftKV's performance on more diverse datasets.

### Soundness
2

### Presentation
3

### Contribution
2

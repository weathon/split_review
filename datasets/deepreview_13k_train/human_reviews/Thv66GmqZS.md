# Bi-Share LoRA: Enhancing the Parameter Efficiency of LoRA with Intra-Layer and Inter-Layer Sharing

- Decision: Reject
- Scores: 6, 6, 6, 3

## Abstract
Low-Rank Adaptation (LoRA) is a widely adopted parameter-efficient fine-tuning method for large language models (LLMs) to adapt to downstream tasks. However, in scenarios where multiple LoRA models are deployed simultaneously, standard LoRA introduces substantial trainable parameters, resulting in significant memory overhead and inference latency, particularly when supporting thousands of downstream tasks on a single server. While existing methods reduce stored parameters via parameter sharing, they fail to capture both local and global information simultaneously. To address this issue, we propose Bi-Share LoRA, which integrates local parameters with intra-layer and inter-layer shared parameters to more effectively capture information at both local and global levels. By sharing parameters both within and across layers, our method significantly reduces the number of trainable parameters while preserving or improving model performance. Additionally, we set a local LoRA to capture local parameters, enabling more precise and fine-grained information extraction at the local level. The final implementation introduces three parallel sub-LoRAs and designs transformation techniques to adapt shared parameters of varying shapes, ensuring compatibility and efficient sharing. Experiments on the 7B, 8B, and 13B versions of Llama show
that Bi-Share LoRA, with only 44.59% of the parameters of standard LoRA, outperforms LoRA by approximately 0.33% on commonsense reasoning and 2.08% on MMLU benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a method to improve the memory efficiency of Low-Rank Adaptation (LoRA) in large language models by introducing Bi-Share LoRA, which integrates local, intra-layer, and inter-layer parameter sharing. This approach captures both local and global information, effectively reducing redundancy and cutting down trainable parameters without compromising performance. The authors also propose three shape transformation techniques—Slice Sharing, Gate Transformation, and Kronecker Extension—to ensure compatibility across varying parameter shapes within model layers. Experimental results demonstrate that Bi-Share LoRA achieves a 56.4% reduction in parameters, underscoring its efficiency and adaptability in multi-task environments​.

### Strengths
1. The paper introduces a novel combination of intra-layer and inter-layer parameter sharing within the LoRA framework, significantly enhancing memory efficiency for large-scale language models by capturing both local and global information.

2. The structure and explanations are clear, with useful visuals that clarify complex processes, though a bit more simplification on the shape transformation techniques would make these sections more accessible.

3. The experimental results are solid, with Bi-Share LoRA consistently cutting parameter use by 56.4% without sacrificing performance.

### Weaknesses
1. The approach lacks a precise mechanism to identify redundancies across layers, relying instead on generalized intra- and inter-layer sharing. This can lead to unnecessary parameter updates in layers where redundancy is minimal. Specifically, the method does not account for the varying importance of different layers or modules within the network, potentially leading to suboptimal parameter sharing. For example, some layers might be more sensitive to changes in their parameters than others, and indiscriminately sharing parameters across all layers could degrade performance in these critical areas. A more adaptive approach that considers the sensitivity of each layer would be beneficial.

2. The experiments are primarily conducted on LLaMA models without exploring performance across diverse tasks or modalities. This narrow focus limits the generalizability of the findings. The method's effectiveness on other architectures, such as transformer variants or models trained on different types of data (e.g., image or audio), remains unclear. The lack of evaluation across different tasks, such as text classification, question answering, or machine translation, also raises concerns about the robustness of the proposed approach.

3. The paper could benefit from more detailed ablations, particularly on the impacts of intra-layer versus inter-layer sharing under different rank settings. The current analysis does not sufficiently disentangle the effects of these two sharing strategies. It is unclear whether one strategy is more effective than the other, or if their combination is crucial for achieving the reported performance gains. Furthermore, the impact of varying the rank of the low-rank matrices used in LoRA, in conjunction with the sharing strategies, is not thoroughly explored.

4. There is a lack of thorough analysis of training and inference costs associated with the proposed parameter-sharing methods. The paper does not provide detailed information on the computational overhead introduced by the shape transformation techniques or the impact of parameter sharing on training convergence. Additionally, the inference costs, such as latency and memory usage, are not adequately addressed, which is crucial for practical deployment.

### Questions
1. Could the authors elaborate on any criteria or heuristic used for determining layer redundancy in the intra- and inter-layer sharing approach? 

2. Given the primary focus on LLaMA models, are there plans to extend evaluations across different domains or task types?

3. Could the authors conduct more in-depth ablation studies to separate the contributions of intra-layer versus inter-layer sharing, especially under varying rank settings? 

4. Could the authors provide further analysis on computational trade-offs, such as training and inference time or memory usage?

### Soundness
4

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
This paper introduces the bishare LoRA, which uses the intra-layer and inter-layer sharing to reduce the number of parameters of the standard LoRA method, which keeps competitive or better performance on commonsense reasoning & MMLU. Overall, this paper is well-written and easy to follow. This method seems promising to reduce the number of parameters while keeping competitive performance. Although this paper could be interesting to a certain group of researchers, the experiments require more baselines/ablations to demonstrate the effectiveness of this method. Also, the gains between VeRA and Bi-Share LoRA is not significant enough but VeRA requires much less parameters.

### Strengths
This paper is well-written and easy to follow. The method compares with standard Lora and achieves significant gains with fewer parameters. This paper conducts multiple ablation experiments, which show various aspects of this method. This paper studies three different dimension transform methods, which could provide some insights to other researches required this methods.

### Weaknesses
1. This method uses both inter- and intra-layer sharing but does not have the baselines of either only using intra or inter-sharing. These experiments are quite useful to better understand which parts provide more gains.
2 For LLama 1, the performance gains are higher and more consistent than llama3, especially on VeRA. VeRA uses a much smaller number of parameters. This raises the question of whether this method is still useful for more powerful LLMs. 
3. One of the motivations of this paper is that when serving multiple LoRAs, memory is important. However, this paper does not provide an analysis of the comparison of multiple Lora servings.

### Questions
1. What would be the performance if only use inter- or intra-layer sharing?
2. Why is the performance on llama3 less significant than llama1 performance?
3. With the new method, how many more LoRAs can be served?

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
This paper proposes a novel Bi-Share LoRA method to enable different LoRA modules within a model to have both shared intra-layer and inter-layer parameters. Additionally, this paper presents three shape transformation methods, including Slice Sharing, Gate Transformation, and Kronecker Extension, to tackle the challenge of adapting shared parameters to all modules with different shapes. Results on commonsense reasoning and MMLU benchmarks show Bi-Share LoRA achieves significant parameter savings of about 50% while maintaining or even improving the model’s performance compared to standard LoRA and other existing methods.

### Strengths
1. The proposed method, Bi-Share LoRA, along with its three shape transformation methods, is both novel and promising. The idea is well-motivated with supporting visualizations, such as average similarity within and across layers. The shape transformation methods are logical and intuitive.

2. This paper is well-organized and easy to read.

3. This method is evaluated across multiple large language models on various tasks including commonsense reasoning and MMLU, making the results convincing.   

4. Some analysis of results is provided to improve interpretability of Bi-Share LoRA.

### Weaknesses
1. Some details in the section of Kronecker extension shape transformation lack clarity. Specifically, it is unclear how the method handles cases where $m/k$ and $n/k$ are not integers. Additionally, the value of k used in the experiments is not specified. In the pseudocode for Kronecker Extension, it states $k = din\mod r$, but this appears to be incorrect. Did the author mean $k = din // r$ instead? This section would benefit from revision for improved clarity.

2. While the paper is generally well organized, numerous small typos and formatting issues detract from its quality. Examples include typographical errors such as ‘frozon’ and ‘Traget’ in Figure 2, and a formatting issue in the caption of a table: ‘(University, 2023).’ A thorough proofreading is needed to address these minor errors in paper writing.

3. The code of Bi-Share LoRA is not shared.

### Questions
Please refer to the points outlined in the weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
1. The paper introduces Bi-Share LoRA, an efficient fine-tuning method for large language models (LLMs) designed to reduce memory and latency issues when deploying multiple LoRA models simultaneously. By combining intra-layer and inter-layer parameter sharing with local parameters, Bi-Share LoRA captures both local and global information more effectively. 

2. The method uses three parallel sub-LoRAs and transformation techniques to manage shared parameters of different shapes. Experiments on Llama models (7B, 8B, and 13B) show that Bi-Share LoRA, with 44.59% fewer parameters than standard LoRA, achieves improved performance, outperforming standard LoRA by 0.33% on commonsense reasoning and 2.08% on MMLU benchmarks.

### Strengths
1. The paper is clearly written and logically structured.

2. The paper leverages the observation of parameter redundancy and sharing across model layers to propose three distinct LoRA modules: Intra-Layer Module, Inter-Layer Module, and Local Module. The overall approach is well-motivated.

3. The authors validate their method using LLaMA models and multiple datasets, including the Commonsense Reasoning benchmark.

### Weaknesses
1. The approach of leveraging inter-layer redundancy to design shared LoRA modules is not sufficiently novel, as several existing works have already explored this concept, such as “ShareLoRA: Parameter Efficient and Robust Large Language Model Fine-tuning via Shared Low-Rank Adaptation” and “Tied-LoRA: Enhancing Parameter Efficiency of LoRA with Weight Tying”. These ideas and techniques are already quite prevalent.

2. Using only the Alpaca dataset for fine-tuning is insufficient to demonstrate the method’s generalizability. Other datasets, such as FLAN, CoT, or domain-specific instruction fine-tuning datasets, should be used for instruction tuning to further validate the algorithm.

3. Although the paper proposes a parameter-efficient version of LoRA, it does not provide details on the overall training time for instruction fine-tuning or the inference time using the proposed method.

4. The authors did not conduct experiments on additional models, such as Mistral or Qwen, to demonstrate the robustness of their algorithm.

### Questions
1. Can the authors conduct experiments on other instruction fine-tuning datasets?

2. Can the authors provide the speedup ratio during the instruction fine-tuning process/ inference process?

3. Could the authors also test their method on models other than LLaMA?

### Soundness
2

### Presentation
2

### Contribution
1
